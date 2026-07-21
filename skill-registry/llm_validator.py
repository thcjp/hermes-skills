#!/usr/bin/env python3
"""
Skill LLM模拟验证器 (L2验证层)
================================

在L1静态检查(quality_gate.py)通过后, 进入上传队列前执行L2验证。
用LLM模拟"用户输入典型请求 → skill响应 → 评估输出质量"。

设计理念:
  - 不硬编码调用外部LLM API
  - 生成评估prompt, 由AI(当前会话)充当LLM评估器
  - 复用trace_llm_scorer.py的static_check能力(T+C维度)
  - AI评估R+A+E维度后, 通过import命令导入结果

L2验证4项检查:
  1. 触发精准度: 给定3个典型用户输入, skill是否被正确触发
  2. 输出完整性: 模拟skill执行, 输出是否包含承诺的核心能力
  3. 依赖可达性: 检查skill引用的API endpoint/包名是否真实存在
  4. TRACE快评: T/R/A/C/E五维度评分(总分≥35才通过)

Usage:
    python llm_validator.py --help                           # 显示帮助
    python llm_validator.py validate <slug>                  # 验证单个skill
    python llm_validator.py validate <slug> --json           # 输出JSON报告
    python llm_validator.py validate <slug> -o report.json   # 保存报告到文件
    python llm_validator.py import <slug> <result.json>      # 导入AI评估结果

流程:
    Step 1: 读取SKILL.md内容
    Step 2: 静态检查(复用trace_llm_scorer.static_check)
    Step 3: 生成LLM评估prompt(含触发测试用例+TRACE评分模板)
    Step 4: AI评估(当前会话执行, 非脚本自动)
    Step 5: 导入评估结果, 合并静态+LLM评分
    Step 6: 输出L2验证报告
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

# 确保能导入skill_registry模块
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

# 复用现有模块
from config import (
    DB_PATH, TRACE_PASS_THRESHOLD, PACKAGED_SKILLS_DIR,
    OPENSOURCE_SKILLS_DIR, get_db_connection
)
from trace_llm_scorer import (
    read_skill_md, static_check, calculate_static_scores,
    save_trace_score, TRACE_EVAL_PROMPT
)


# ============ Skill查找 ============

def find_skill_md(slug: str) -> Optional[Path]:
    """查找skill的SKILL.md路径
    
    查找顺序:
      1. packaged-skills/skillhub/{slug}/SKILL.md
      2. opensource-skills/packaged/{slug}/SKILL.md
      3. DB中的local_path
    """
    # 1. packaged-skills
    packaged_path = PACKAGED_SKILLS_DIR / slug / "SKILL.md"
    if packaged_path.exists():
        return packaged_path

    # 2. opensource-skills
    opensource_path = OPENSOURCE_SKILLS_DIR / slug / "SKILL.md"
    if opensource_path.exists():
        return opensource_path

    # 3. DB查找
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT local_path FROM skills WHERE slug = ? AND workflow_state != 'deprecated'", (slug,))
        row = c.fetchone()
        conn.close()
        if row and row['local_path']:
            p = Path(row['local_path'])
            if p.name == 'SKILL.md' and p.exists():
                return p
            skill_md = p / 'SKILL.md'
            if skill_md.exists():
                return skill_md
    except Exception:
        pass

    return None


def get_skill_id(slug: str) -> Optional[int]:
    """从DB获取skill_id"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT id FROM skills WHERE slug = ? AND workflow_state != 'deprecated'", (slug,))
        row = c.fetchone()
        conn.close()
        return row['id'] if row else None
    except Exception:
        return None


# ============ 触发测试用例生成 ============

def generate_trigger_test_cases(skill_content: str, slug: str) -> List[Dict[str, str]]:
    """根据SKILL.md内容生成3个触发测试用例
    
    从description和适用场景中提取典型用户输入
    """
    # 解析frontmatter获取description
    import re
    desc = ''
    summary = ''
    if skill_content.startswith('---'):
        parts = re.split(r'^---\s*$', skill_content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm = parts[1]
            # 提取description中的触发关键词
            desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
            if desc_match:
                desc = desc_match.group(1).strip()
            summary_match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if summary_match:
                summary = summary_match.group(1).strip()

    # 从description中提取触发关键词(中文逗号/顿号分隔)
    trigger_keywords = []
    if desc:
        # 找"触发关键词:"后面的内容
        kw_match = re.search(r'触发关键词[：:](.+?)(?:\n|$)', desc)
        if kw_match:
            keywords_text = kw_match.group(1)
            # 按中文逗号、顿号、英文逗号分隔
            parts = re.split(r'[，、,]', keywords_text)
            trigger_keywords = [p.strip() for p in parts if p.strip()][:5]

    # 生成3个测试用例
    test_cases = []
    if trigger_keywords:
        for i, kw in enumerate(trigger_keywords[:3]):
            test_cases.append({
                'id': f'tc{i+1}',
                'user_input': f'帮我{kw}',
                'expected_trigger': True,
                'reason': f'从description触发关键词提取: {kw}'
            })
    
    # 如果提取不到足够的测试用例, 用通用用例补充
    while len(test_cases) < 3:
        fallback_inputs = [
            {'input': f'使用{slug}处理一个任务', 'reason': '通用fallback用例'},
            {'input': f'我需要{slug}的功能', 'reason': '通用fallback用例'},
            {'input': f'请执行{slug}', 'reason': '通用fallback用例'},
        ]
        idx = len(test_cases)
        if idx < len(fallback_inputs):
            test_cases.append({
                'id': f'tc{idx+1}',
                'user_input': fallback_inputs[idx]['input'],
                'expected_trigger': True,
                'reason': fallback_inputs[idx]['reason']
            })
        else:
            break

    return test_cases[:3]


# ============ 外部依赖提取 ============

def extract_external_dependencies(skill_content: str) -> List[Dict[str, str]]:
    """从SKILL.md中提取外部依赖
    
    识别:
      - API endpoint (https://xxx/api)
      - npm包 (npm install xxx)
      - PyPI包 (pip install xxx)
      - 模型名 (GPT-4, BERT等)
    """
    import re
    deps = []

    # API endpoint
    api_pattern = r'https?://[a-zA-Z0-9._/-]+api[a-zA-Z0-9._/-]*'
    for m in re.finditer(api_pattern, skill_content, re.IGNORECASE):
        url = m.group(0)
        if url not in [d['name'] for d in deps]:
            deps.append({
                'type': 'api_endpoint',
                'name': url,
                'verification_method': 'HTTP HEAD请求',
                'verified': False,
                'status': 'pending'
            })

    # npm包 (排除常见系统词)
    npm_pattern = r'npm\s+(?:install|i)\s+([a-zA-Z0-9@/_-]+)'
    for m in re.finditer(npm_pattern, skill_content):
        pkg = m.group(1)
        if pkg and not pkg.startswith('@types/') and pkg not in [d['name'] for d in deps]:
            deps.append({
                'type': 'npm_package',
                'name': pkg,
                'verification_method': 'npm view <package>',
                'verified': False,
                'status': 'pending'
            })

    # PyPI包
    pypi_pattern = r'pip\s+install\s+([a-zA-Z0-9_-]+)'
    for m in re.finditer(pypi_pattern, skill_content):
        pkg = m.group(1)
        if pkg and pkg not in [d['name'] for d in deps]:
            deps.append({
                'type': 'pypi_package',
                'name': pkg,
                'verification_method': 'pip index versions <package>',
                'verified': False,
                'status': 'pending'
            })

    # 已知模型名
    known_models = [
        'GPT-4', 'GPT-3.5', 'GPT-4o', 'o1', 'o3',
        'Claude', 'Claude-3', 'Claude-3.5', 'Sonnet', 'Opus', 'Haiku',
        'BERT', 'RoBERTa', 'T5', 'LLaMA', 'GLM-4', '文心', '通义', 'DeepSeek',
        'Whisper', 'CLIP', 'DALL-E', 'Stable Diffusion',
    ]
    for model in known_models:
        if model.lower() in skill_content.lower():
            if model not in [d['name'] for d in deps]:
                deps.append({
                    'type': 'ai_model',
                    'name': model,
                    'verification_method': '已知模型列表比对',
                    'verified': True,
                    'status': 'known_model'
                })

    return deps


# ============ L2验证核心 ============

def generate_llm_eval_prompt(skill_content: str, slug: str, trigger_test_cases: List[Dict]) -> str:
    """生成LLM评估prompt
    
    AI(当前会话)读取此prompt后执行评估, 输出JSON结果
    """
    prompt = f"""# L2验证: LLM模拟评估任务

## 被评估Skill: {slug}

## SKILL.md内容
{skill_content[:3000]}{'...(截断)' if len(skill_content) > 3000 else ''}

## 评估任务

请作为Skill质量评估专家, 完成以下4项评估:

### 检查1: 触发精准度
对以下3个测试用例, 判断SKILL.md的description是否能精准触发:
"""
    for tc in trigger_test_cases:
        prompt += f"- {tc['id']}: 用户输入「{tc['user_input']}」 → 预期触发: {tc['expected_trigger']}\n"

    prompt += """
评估标准:
- PASS: 3/3个用例的触发判断与预期一致
- WARN: 2/3一致
- FAIL: ≤1/3一致

### 检查2: 输出完整性
模拟skill执行, 评估输出是否包含SKILL.md承诺的核心能力:
- 读取"核心能力"章节
- 模拟1个典型输入的执行
- 判断输出是否覆盖承诺的能力点

评估标准:
- PASS: 输出覆盖所有核心能力
- WARN: 覆盖大部分但有遗漏
- FAIL: 输出与承诺严重不符

### 检查3: 依赖可达性
检查SKILL.md引用的外部依赖是否真实可用:
- API endpoint是否可达
- npm/PyPI包是否存在
- AI模型是否为已知模型

评估标准:
- PASS: 所有依赖可达/存在
- WARN: 部分依赖未验证
- FAIL: 依赖不存在或不可达

### 检查4: TRACE快评
按TRACE五维度评分(每维度0-10分):

- T (Trust 可信任度): 安全性、国内可用性、中文支持
- R (Reliability 可靠性): 异常处理、边界输入、失败反馈
- A (Adaptability 适用性): description精准、能力边界清晰
- C (Convention 规范性): 信息架构、文档充分性
- E (Effectiveness 有效性): 解决问题、输出可用

通过标准: 总分≥35/50

## 输出格式(严格JSON)

```json
{
  "slug": "%s",
  "validated_at": "<ISO时间>",
  "checks": {
    "trigger_accuracy": {
      "status": "PASS|WARN|FAIL",
      "score": "3/3",
      "details": "评估说明"
    },
    "output_completeness": {
      "status": "PASS|WARN|FAIL",
      "covered_capabilities": ["能力1", "能力2"],
      "missing_capabilities": [],
      "details": "评估说明"
    },
    "dependency_reachability": {
      "status": "PASS|WARN|FAIL",
      "total_deps": 0,
      "verified_deps": 0,
      "failed_deps": [],
      "details": "评估说明"
    },
    "trace_quick_score": {
      "trust": 0,
      "reliability": 0,
      "adaptability": 0,
      "convention": 0,
      "effectiveness": 0,
      "total": 0,
      "grade": "A|B|C|D",
      "passed": true,
      "details": "评估说明"
    }
  },
  "overall_passed": false,
  "overall_summary": "总结"
}
```
""" % slug

    return prompt


def run_l2_validation(slug: str, output_json: bool = False, output_file: str = None) -> Dict[str, Any]:
    """运行L2验证
    
    流程:
      1. 查找SKILL.md
      2. 静态检查(复用trace_llm_scorer)
      3. 生成触发测试用例
      4. 提取外部依赖
      5. 生成LLM评估prompt(供AI执行)
      6. 输出报告(静态部分自动完成, LLM部分待AI评估)
    """
    result = {
        'slug': slug,
        'validated_at': datetime.now().isoformat(),
        'l2_version': '1.0',
        'status': 'pending_llm_eval',
    }

    # Step 1: 查找SKILL.md
    skill_md_path = find_skill_md(slug)
    if not skill_md_path:
        result['status'] = 'error'
        result['error'] = f'SKILL.md not found for slug: {slug}'
        return result

    result['skill_md_path'] = str(skill_md_path)
    skill_content = read_skill_md(str(skill_md_path.parent))

    if not skill_content:
        result['status'] = 'error'
        result['error'] = 'SKILL.md内容为空'
        return result

    # Step 2: 静态检查(复用trace_llm_scorer)
    checks = static_check(skill_content)
    static_scores = calculate_static_scores(checks)
    result['static_check'] = {
        'issues': checks['issues'],
        'static_scores': static_scores,
        'body_line_count': checks['body_line_count'],
        'description_length': checks['description_length'],
    }

    # Step 3: 生成触发测试用例
    trigger_test_cases = generate_trigger_test_cases(skill_content, slug)
    result['trigger_test_cases'] = trigger_test_cases

    # Step 4: 提取外部依赖
    external_deps = extract_external_dependencies(skill_content)
    result['external_dependencies'] = external_deps

    # Step 5: 生成LLM评估prompt
    llm_prompt = generate_llm_eval_prompt(skill_content, slug, trigger_test_cases)
    result['llm_eval_prompt'] = llm_prompt
    result['llm_eval_prompt_length'] = len(llm_prompt)

    # Step 6: 静态预评估(T+C维度)
    result['static_pre_eval'] = {
        'trust_static': static_scores['trust_static'],
        'convention_static': static_scores['convention_static'],
        'static_total': round(static_scores['trust_static'] + static_scores['convention_static'], 1),
        'note': 'T+C维度静态分, R+A+E维度需LLM评估'
    }

    # 保存报告
    if output_file:
        report_path = Path(output_file)
    else:
        report_path = SKILL_REGISTRY_DIR / f'l2_validation_report_{slug}.json'

    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    result['report_path'] = str(report_path)

    # 终端输出
    if not output_json:
        print(f"\n{'='*70}")
        print(f"L2验证报告: {slug}")
        print(f"{'='*70}")
        print(f"SKILL.md路径: {skill_md_path}")
        print(f"验证时间: {result['validated_at']}")
        print(f"\n--- 静态检查 ---")
        print(f"  T(Trust)静态分: {static_scores['trust_static']}/10")
        print(f"  C(Convention)静态分: {static_scores['convention_static']}/10")
        print(f"  静态合计: {result['static_pre_eval']['static_total']}/20 (T+C维度)")
        if checks['issues']:
            print(f"  问题: {checks['issues']}")
        print(f"\n--- 触发测试用例 ---")
        for tc in trigger_test_cases:
            print(f"  {tc['id']}: 「{tc['user_input']}」 (原因: {tc['reason']})")
        print(f"\n--- 外部依赖 ---")
        if external_deps:
            for dep in external_deps:
                status_tag = '✓已知' if dep['verified'] else '⚠待验证'
                print(f"  [{dep['type']}] {dep['name']} {status_tag}")
        else:
            print(f"  无外部依赖")
        print(f"\n--- LLM评估 ---")
        print(f"  状态: 待AI评估 (prompt已生成, {len(llm_prompt)}字符)")
        print(f"  报告路径: {report_path}")
        print(f"\n下一步: AI读取报告中的llm_eval_prompt字段, 执行评估后")
        print(f"        运行: python llm_validator.py import {slug} <评估结果.json>")
        print(f"{'='*70}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    return result


def import_llm_eval_result(slug: str, result_file: str) -> Dict[str, Any]:
    """导入AI评估结果, 合并静态+LLM评分
    
    流程:
      1. 读取AI评估结果JSON
      2. 从DB获取skill_id
      3. 重新读取SKILL.md做静态检查
      4. 调用save_trace_score合并保存
      5. 输出最终L2验证结论
    """
    result_path = Path(result_file)
    if not result_path.exists():
        return {'error': f'评估结果文件不存在: {result_file}'}

    with open(result_path, 'r', encoding='utf-8') as f:
        llm_result = json.load(f)

    # 获取skill_id
    skill_id = get_skill_id(slug)
    if not skill_id:
        return {'error': f'DB中找不到skill: {slug}'}

    # 读取SKILL.md做静态检查
    skill_md_path = find_skill_md(slug)
    if not skill_md_path:
        return {'error': f'SKILL.md not found: {slug}'}

    skill_content = read_skill_md(str(skill_md_path.parent))
    checks = static_check(skill_content)
    static_scores = calculate_static_scores(checks)

    # 格式转换: 将L2验证的扁平格式转换为save_trace_score期望的嵌套格式
    # L2格式: llm_result['checks']['trace_quick_score']['trust'] = 9
    # 期望格式: llm_result['trace_scores']['trust']['score'] = 9
    trace_quick = llm_result.get('checks', {}).get('trace_quick_score', {})
    adapted_llm_result = {
        'trace_scores': {
            dim: {'score': trace_quick.get(dim, 0), 'suggestion': trace_quick.get('details', '')}
            for dim in ['trust', 'reliability', 'adaptability', 'convention', 'effectiveness']
        },
        'quality_grade': trace_quick.get('grade', 'D'),
        'top_3_issues': [],
    }

    # 合并保存到DB
    db_result = save_trace_score(skill_id, checks, static_scores, adapted_llm_result)

    # 构建L2最终结论
    trace_scores = llm_result.get('checks', {}).get('trace_quick_score', {})
    total_trace = trace_scores.get('total', 0)
    passed = total_trace >= TRACE_PASS_THRESHOLD

    final_result = {
        'slug': slug,
        'skill_id': skill_id,
        'imported_at': datetime.now().isoformat(),
        'trace_total': total_trace,
        'trace_grade': trace_scores.get('grade', 'D'),
        'l2_passed': passed,
        'db_result': db_result,
        'checks_summary': {
            'trigger_accuracy': llm_result.get('checks', {}).get('trigger_accuracy', {}).get('status', 'N/A'),
            'output_completeness': llm_result.get('checks', {}).get('output_completeness', {}).get('status', 'N/A'),
            'dependency_reachability': llm_result.get('checks', {}).get('dependency_reachability', {}).get('status', 'N/A'),
            'trace_score': f"{total_trace}/50",
        }
    }

    # 保存最终报告
    final_report_path = SKILL_REGISTRY_DIR / f'l2_final_report_{slug}.json'
    with open(final_report_path, 'w', encoding='utf-8') as f:
        json.dump(final_result, f, ensure_ascii=False, indent=2)

    # 终端输出
    print(f"\n{'='*70}")
    print(f"L2验证最终结论: {slug}")
    print(f"{'='*70}")
    print(f"  TRACE总分: {total_trace}/50 (阈值: {TRACE_PASS_THRESHOLD})")
    print(f"  等级: {trace_scores.get('grade', 'D')}")
    print(f"  L2通过: {'✓ PASS' if passed else '✗ FAIL'}")
    print(f"\n  检查项汇总:")
    for check_name, status in final_result['checks_summary'].items():
        print(f"    {check_name}: {status}")
    print(f"\n  DB保存: skill_id={skill_id}, score_type=trace_llm")
    print(f"  最终报告: {final_report_path}")
    print(f"{'='*70}")

    return final_result


# ============ CLI ============

def main():
    parser = argparse.ArgumentParser(
        description='Skill LLM模拟验证器 (L2验证层) - 在L1静态检查通过后, 进入上传队列前执行',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 验证单个skill(生成prompt, 待AI评估)
  python llm_validator.py validate sales-copy-writer

  # 输出JSON格式
  python llm_validator.py validate sales-copy-writer --json

  # 保存报告到指定文件
  python llm_validator.py validate sales-copy-writer -o report.json

  # 导入AI评估结果
  python llm_validator.py import sales-copy-writer eval_result.json

流程说明:
  1. validate: 生成L2验证报告(含LLM评估prompt), 静态部分自动完成
  2. AI读取报告中的llm_eval_prompt, 执行评估, 保存为JSON
  3. import: 导入AI评估结果, 合并静态+LLM评分, 输出最终结论
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # validate子命令
    val_parser = subparsers.add_parser('validate', help='验证单个skill')
    val_parser.add_argument('slug', help='Skill slug名称')
    val_parser.add_argument('--json', action='store_true', help='输出JSON格式')
    val_parser.add_argument('-o', '--output', help='报告保存路径')

    # import子命令
    imp_parser = subparsers.add_parser('import', help='导入AI评估结果')
    imp_parser.add_argument('slug', help='Skill slug名称')
    imp_parser.add_argument('result_file', help='AI评估结果JSON文件路径')

    args = parser.parse_args()

    if args.command == 'validate':
        run_l2_validation(args.slug, output_json=args.json, output_file=args.output)
    elif args.command == 'import':
        import_llm_eval_result(args.slug, args.result_file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
