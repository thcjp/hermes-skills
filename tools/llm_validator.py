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
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, get_max_content_chars, TRACE_PASS_THRESHOLD, get_db_connection # V123 W2: 合并重复import
sys.path.insert(0, str(TOOLS_DIR))
from trace_llm_scorer import (
    read_skill_md, static_check, calculate_static_scores,
    save_trace_score,
)
from skill_core.parser import find_skill_md


# ============ Skill查找 ============

def get_skill_id(slug: str) -> Optional[int]:
    """从DB获取skill_id"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT id FROM skills WHERE slug = ? AND workflow_state != 'deprecated'", (slug,))
        row = c.fetchone()
        conn.close()
        return row['id'] if row else None
    except Exception:  # [V130 A1] 宽泛捕获: DB查询可能因连接/表不存在等多种原因失败
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

# [V135 F1] 模块级常量: 从extract_external_dependencies提取(TD-252)
_KNOWN_MODELS = [
    'GPT-4', 'GPT-3.5', 'GPT-4o', 'o1', 'o3',
    'Claude', 'Claude-3', 'Claude-3.5', 'Sonnet', 'Opus', 'Haiku',
    'BERT', 'RoBERTa', 'T5', 'LLaMA', 'GLM-4', '文心', '通义', 'DeepSeek',
    'Whisper', 'CLIP', 'DALL-E', 'Stable Diffusion',
]



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
    known_models = _KNOWN_MODELS  # [V135 F1] 已提取为模块级常量
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


# V130 A9: 与generate_skill.run_l2_validation不是重复定义。
# 差异: 本函数签名(slug,output_json,output_file), 进程内直接执行静态检查+生成触发测试用例+
#       提取依赖+生成LLM评估prompt, 返回详细验证数据; generate_skill版签名(slug), 通过
#       subprocess调用本脚本, 读取报告文件返回含trace_total/trace_grade的汇总。
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
        report_path = TOOLS_DIR / f'l2_validation_report_{slug}.json'

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
    final_report_path = TOOLS_DIR / f'l2_final_report_{slug}.json'
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


# ============ E1: Trigger验证增强 ============

def generate_negative_trigger_test_cases(skill_content: str, slug: str) -> List[Dict[str, str]]:
    """生成不应触发skill的负向测试用例（E1增强）

    负向测试用例用于验证skill的description不会过度匹配，
    即不会在不相关的请求中误触发。

    参数:
        skill_content: SKILL.md内容
        slug: skill的slug

    返回:
        负向测试用例列表，每项包含:
        {
            'id': str,
            'user_input': str,       # 用户输入
            'expected_trigger': False,  # 不应触发
            'reason': str,
        }
    """
    import re

    # 从frontmatter提取category/summary
    category = ''
    summary = ''
    if skill_content.startswith('---'):
        parts = re.split(r'^---\s*$', skill_content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm = parts[1]
            cat_match = re.search(r'^category:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if cat_match:
                category = cat_match.group(1).strip()
            summary_match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if summary_match:
                summary = summary_match.group(1).strip()

    # 生成与当前skill不相关的负向用例
    # 根据category生成不相关领域的请求
    negative_inputs = [
        {'input': '帮我查一下今天的天气', 'reason': '天气查询与skill无关'},
        {'input': '帮我写一首诗', 'reason': '诗歌创作与skill无关'},
        {'input': '帮我翻译一段英文', 'reason': '翻译任务与skill无关'},
    ]

    # 根据category添加更精准的负向用例
    if category:
        category_negatives = {
            'Finance': [
                {'input': '帮我画一个头像', 'reason': '图像生成与财务无关'},
                {'input': '帮我安排会议日程', 'reason': '日程管理与财务无关'},
            ],
            'Creative': [
                {'input': '帮我计算贷款月供', 'reason': '贷款计算与创作无关'},
                {'input': '帮我部署一个服务器', 'reason': '服务器部署与创作无关'},
            ],
            'Developer': [
                {'input': '帮我制定健身计划', 'reason': '健身计划与开发无关'},
                {'input': '帮我做菜谱推荐', 'reason': '菜谱推荐与开发无关'},
            ],
        }
        negatives = category_negatives.get(category, [])
        if negatives:
            negative_inputs = negatives

    test_cases = []
    for i, item in enumerate(negative_inputs[:2]):
        test_cases.append({
            'id': f'neg_tc{i+1}',
            'user_input': item['input'],
            'expected_trigger': False,
            'reason': item['reason'],
        })

    return test_cases


def calculate_trigger_accuracy(
    positive_results: List[Dict],
    negative_results: List[Dict]
) -> Dict[str, Any]:
    """计算触发精准度（E1增强）

    综合正向和负向测试结果，计算精准度。

    参数:
        positive_results: 正向测试结果列表（应触发）
        negative_results: 负向测试结果列表（不应触发）

    返回:
        {
            'accuracy': float,          # 精准度(0.0-1.0)
            'positive_pass_rate': float, # 正向通过率
            'negative_pass_rate': float, # 负向通过率
            'false_positive_rate': float, # 误触发率
            'false_negative_rate': float, # 漏触发率
            'status': str,              # PASS/WARN/FAIL
            'details': str,
        }
    """
    # 正向测试：应触发且实际触发的比例
    pos_total = len(positive_results)
    pos_correct = sum(1 for r in positive_results if r.get('triggered', False) == r.get('expected_trigger', True))
    pos_rate = pos_correct / pos_total if pos_total > 0 else 0

    # 负向测试：不应触发且实际未触发的比例
    neg_total = len(negative_results)
    neg_correct = sum(1 for r in negative_results if r.get('triggered', True) == r.get('expected_trigger', False))
    neg_rate = neg_correct / neg_total if neg_total > 0 else 0

    # 误触发率和漏触发率
    false_positive = sum(1 for r in negative_results if r.get('triggered', False))  # 不应触发但触发了
    false_negative = sum(1 for r in positive_results if not r.get('triggered', True))  # 应触发但没触发
    fpr = false_positive / neg_total if neg_total > 0 else 0
    fnr = false_negative / pos_total if pos_total > 0 else 0

    # 综合精准度
    accuracy = (pos_rate + neg_rate) / 2

    # 状态判定
    if accuracy >= 0.9:
        status = 'PASS'
    elif accuracy >= 0.7:
        status = 'WARN'
    else:
        status = 'FAIL'

    details = (
        f"正向通过率: {pos_rate:.0%}({pos_correct}/{pos_total}), "
        f"负向通过率: {neg_rate:.0%}({neg_correct}/{neg_total}), "
        f"误触发率: {fpr:.0%}, 漏触发率: {fnr:.0%}"
    )

    return {
        'accuracy': round(accuracy, 3),
        'positive_pass_rate': round(pos_rate, 3),
        'negative_pass_rate': round(neg_rate, 3),
        'false_positive_rate': round(fpr, 3),
        'false_negative_rate': round(fnr, 3),
        'status': status,
        'details': details,
    }


# ============ E13: TRAE Work AI代理集成 ============

def generate_agent_prompt(
    task_type: str,
    skill_data: dict,
    context: dict = None
) -> str:
    """生成TRAE Work AI代理执行的结构化prompt（E13核心）

    推广llm_validator.py已有的generate_llm_eval_prompt()模式：
    - 明确任务描述
    - 提供完整skill内容
    - 指定输出格式（严格JSON）
    - 由AI代理（当前会话）执行

    支持4种task_type:
      - generate: Skill内容生成（替代模板填充）
      - score: 质量评分（替代外部API评分）
      - rewrite: 深度重写（替代外部API重写）
      - analyze: 差异化分析（替代硬编码映射表）

    参数:
        task_type: 任务类型 (generate|score|rewrite|analyze)
        skill_data: skill内容数据，必须包含:
            - skill_content: SKILL.md内容（score/rewrite/analyze时必需）
            - slug: skill的slug（所有类型必需）
            - name: skill名称（generate时必需）
        context: 额外上下文（可选）
            - defect_dims: 缺陷维度列表(rewrite用)
            - category: 分类(analyze用)
            - description: 描述(analyze用)

    返回:
        结构化prompt字符串，供AI代理执行

    异常:
        ValueError: 当skill_data缺少必需字段时
    """
    # F-08: prompt质量校验 — 检查必需字段
    if 'slug' not in skill_data or not skill_data['slug']:
        raise ValueError("skill_data必须包含非空的'slug'字段")

    if task_type in ('score', 'rewrite', 'analyze') and 'skill_content' not in skill_data:
        raise ValueError(f"task_type='{task_type}'需要skill_data包含'skill_content'字段")

    if task_type == 'generate' and 'name' not in skill_data:
        raise ValueError("task_type='generate'需要skill_data包含'name'字段")

    slug = skill_data['slug']
    skill_content = skill_data.get('skill_content', '')
    name = skill_data.get('name', slug)
    context = context or {}

    if task_type == 'generate':
        return _build_generate_prompt(slug, name, skill_content, context)
    elif task_type == 'score':
        return _build_score_prompt(slug, skill_content, context)
    elif task_type == 'rewrite':
        return _build_rewrite_prompt(slug, skill_content, context)
    elif task_type == 'analyze':
        return _build_analyze_prompt(slug, skill_content, context)
    else:
        raise ValueError(f"不支持的task_type: {task_type}")


def _build_generate_prompt(slug: str, name: str, skill_content: str, context: dict) -> str:
    """构建Skill生成prompt"""
    category = context.get('category', 'Other')
    description = context.get('description', '')

    prompt = f"""# Skill内容生成任务

## 任务
请为以下skill生成高质量的SKILL.md内容：

- **slug**: {slug}
- **name**: {name}
- **category**: {category}
- **description**: {description}

## 生成要求
1. 生成完整的SKILL.md，包含frontmatter和正文
2. frontmatter必须包含: slug, name, displayName(<=20字符), summary(<=100字符), license, description
3. description必须包含触发关键词，用于精准匹配用户请求
4. 正文必须包含以下章节: 核心能力、使用流程、参数说明、FAQ
5. 内容必须与{name}领域强相关，不要泛泛而谈
6. 禁止使用"最佳/最强/万能/超级"等夸大词

## 输出格式（严格JSON）
```json
{{
  "slug": "{slug}",
  "skill_content": "<完整的SKILL.md内容>",
  "display_name": "<<=20字符的显示名>",
  "summary": "<<=100字符的摘要>"
}}
```"""
    return prompt


def _build_score_prompt(slug: str, skill_content: str, context: dict) -> str:
    """构建质量评分prompt"""
    prompt = f"""# SKILL质量评分任务

## 被评分Skill: {slug}

## SKILL.md内容
{skill_content[:15000]}{'...(截断)' if len(skill_content) > 15000 else ''}

## 评分维度（每维度0.0-1.0）
1. **completeness（功能完整性）**: 核心能力是否完整、边界条件是否覆盖
2. **accuracy（准确性）**: 内容是否准确、示例是否可运行
3. **usability（易用性）**: 是否易于上手、FAQ是否充分
4. **security（安全性）**: 安全注意事项是否充分
5. **innovation（创新性）**: 是否有差异化亮点

## 输出格式（严格JSON）
```json
{{
  "slug": "{slug}",
  "total_score": 0.0,
  "dimensions": {{
    "completeness": {{"score": 0.0, "reason": "评分理由"}},
    "accuracy": {{"score": 0.0, "reason": "评分理由"}},
    "usability": {{"score": 0.0, "reason": "评分理由"}},
    "security": {{"score": 0.0, "reason": "评分理由"}},
    "innovation": {{"score": 0.0, "reason": "评分理由"}}
  }},
  "feedback": "改进建议汇总",
  "passed": false
}}
```"""
    return prompt


def _build_rewrite_prompt(slug: str, skill_content: str, context: dict) -> str:
    """构建深度重写prompt"""
    defect_dims = context.get('defect_dims', [])
    gaps_text = "\n".join(f"- {d}" for d in defect_dims) if defect_dims else "综合提升"

    prompt = f"""# SKILL深度重写任务

## 被重写Skill: {slug}

## SKILL.md当前内容
{skill_content[:20000]}{'...(截断)' if len(skill_content) > 20000 else ''}

## 需要改进的维度
{gaps_text}

## 重写要求
1. 只补齐缺失部分，不要重复已有内容
2. 内容必须与skill领域强相关
3. 每个增强部分150-300字，直击要害
4. 格式为Markdown

## 输出格式（严格JSON）
```json
{{
  "slug": "{slug}",
  "enhancements": [
    {{
      "dimension": "维度名",
      "section_title": "增强内容标题",
      "content": "增强内容（Markdown格式）",
      "insert_after": "SKILL.md中的现有标题或append"
    }}
  ]
}}
```"""
    return prompt


def _build_analyze_prompt(slug: str, skill_content: str, context: dict) -> str:
    """构建差异化分析prompt"""
    category = context.get('category', 'Other')
    description = context.get('description', '')

    prompt = f"""# Skill差异化分析任务

## 被分析Skill: {slug}
- **category**: {category}
- **description**: {description}

## SKILL.md内容
{skill_content[:15000]}{'...(截断)' if len(skill_content) > 15000 else ''}

## 分析任务
请分析此skill的目标用户痛点、核心能力、差异化方向：

## 输出格式（严格JSON）
```json
{{
  "slug": "{slug}",
  "pain_points": ["痛点1", "痛点2"],
  "target_users": ["目标用户1", "目标用户2"],
  "core_capabilities": ["核心能力1", "核心能力2"],
  "summary": "<基于痛点+方案+量化的摘要，<=100字符>"
}}
```"""
    return prompt


def validate_agent_prompt(prompt: str) -> dict:
    """验证AI代理prompt质量（F-08修正）

    检查prompt是否包含必需的字段：
    - task_type/skill_content/output_format

    参数:
        prompt: generate_agent_prompt()生成的prompt

    返回:
        {
            'valid': bool,
            'missing_fields': list,
            'issues': list,
        }
    """
    issues = []
    missing_fields = []

    # 检查是否包含任务描述
    if '# ' not in prompt:
        issues.append("prompt缺少任务标题(以#开头)")

    # 检查是否包含skill内容或slug
    if 'skill' not in prompt.lower() and 'slug' not in prompt.lower():
        missing_fields.append('skill_content')
        issues.append("prompt缺少skill相关内容")

    # 检查是否指定了输出格式
    if 'json' not in prompt.lower() and '输出格式' not in prompt:
        missing_fields.append('output_format')
        issues.append("prompt未指定输出格式")

    # 检查是否有slug字段
    if 'slug' not in prompt:
        missing_fields.append('slug')
        issues.append("prompt缺少slug标识")

    return {
        'valid': len(issues) == 0,
        'missing_fields': missing_fields,
        'issues': issues,
    }


# ============ CLI ============

# ============ E10: Token压缩优化 ============

def compress_skill_content(
    skill_content: str,
    task_type: str = 'score',
    max_chars: int = None,
) -> Dict[str, Any]:
    """E10: Token压缩优化 — 智能截断SKILL.md内容

    基于E11的max_content_chars配置截断SKILL.md内容。
    智能截断策略: 保留frontmatter完整 + 正文按优先级保留关键章节

    截断优先级(高→低):
    1. frontmatter(完整保留, 含slug/name/description等元信息)
    2. 核心功能章节
    3. 输入格式章节
    4. 输出格式章节
    5. 依赖说明章节
    6. 其他章节(按出现顺序, 超出预算时截断)

    参数:
        skill_content: 完整SKILL.md内容字符串
        task_type: 任务类型(score/generate/rewrite/evaluate), 决定截断阈值
        max_chars: 自定义最大字符数(None则从E11配置读取)

    返回:
        {
            'compressed_content': str,   # 压缩后的内容
            'original_length': int,      # 原始长度
            'compressed_length': int,    # 压缩后长度
            'compression_ratio': float,  # 压缩比(0-1)
            'sections_kept': list,       # 保留的章节列表
            'sections_truncated': list,  # 被截断的章节列表
            'task_type': str,            # 使用的任务类型
            'max_chars': int,            # 使用的最大字符数
        }
    """
    import re

    # 1. 确定最大字符数(复用E11的max_content_chars配置)
    if max_chars is None:
        try:
            # 延迟导入避免循环依赖
            max_chars = get_max_content_chars(task_type)
        except ImportError:
            # E11配置不可用时使用默认值(非mock, 真实降级到合理默认)
            _DEFAULT_MAX_CHARS = {
                'score': 15000, 'generate': 20000,
                'rewrite': 20000, 'evaluate': 10000,
            }
            max_chars = _DEFAULT_MAX_CHARS.get(task_type, 15000)

    original_length = len(skill_content)

    # 如果原始内容未超限, 直接返回
    if original_length <= max_chars:
        return {
            'compressed_content': skill_content,
            'original_length': original_length,
            'compressed_length': original_length,
            'compression_ratio': 1.0,
            'sections_kept': ['all'],
            'sections_truncated': [],
            'task_type': task_type,
            'max_chars': max_chars,
        }

    # 2. 分离frontmatter和正文
    frontmatter = ''
    body = skill_content

    if skill_content.startswith('---'):
        parts = re.split(r'^---\s*$', skill_content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            frontmatter = f'---\n{parts[1].strip()}\n---'
            body = parts[2].strip()
        elif len(parts) == 2:
            frontmatter = f'---\n{parts[1].strip()}\n---'
            body = ''

    # 3. 按章节拆分正文
    sections = _split_sections(body)

    # 4. 按优先级分配字符预算
    fm_budget = len(frontmatter)
    remaining_budget = max_chars - fm_budget - 100  # 留100字符余量

    # 章节优先级(高→低)
    priority_sections = ['核心功能', 'core', '输入格式', 'input',
                         '输出格式', 'output', '依赖说明', 'dependency']
    high_priority = []
    low_priority = []
    for section in sections:
        title_lower = section['title'].lower()
        is_high = any(p.lower() in title_lower for p in priority_sections)
        if is_high:
            high_priority.append(section)
        else:
            low_priority.append(section)

    # 5. 按优先级填充内容
    sections_kept = []
    sections_truncated = []
    result_body_parts = []

    # 高优先级章节: 保留完整(或截断到合理长度)
    for section in high_priority:
        section_text = section['full_text']
        if remaining_budget <= 0:
            sections_truncated.append(section['title'])
            continue
        if len(section_text) <= remaining_budget:
            result_body_parts.append(section_text)
            remaining_budget -= len(section_text) + 2
            sections_kept.append(section['title'])
        else:
            # 截断到剩余预算
            truncated = section_text[:remaining_budget] + '\n...(章节已截断)'
            result_body_parts.append(truncated)
            sections_truncated.append(section['title'])
            remaining_budget = 0

    # 低优先级章节: 有剩余预算才保留
    for section in low_priority:
        if remaining_budget <= 0:
            sections_truncated.append(section['title'])
            continue
        if len(section['full_text']) <= remaining_budget:
            result_body_parts.append(section['full_text'])
            remaining_budget -= len(section['full_text']) + 2
            sections_kept.append(section['title'])
        else:
            truncated = section['full_text'][:remaining_budget] + '\n...(章节已截断)'
            result_body_parts.append(truncated)
            sections_truncated.append(section['title'])
            remaining_budget = 0

    # 6. 组装压缩后的内容
    compressed_body = '\n\n'.join(result_body_parts)
    if frontmatter:
        compressed_content = f'{frontmatter}\n\n{compressed_body}'
    else:
        compressed_content = compressed_body

    compressed_length = len(compressed_content)

    # 7. 确保不超过max_chars
    if compressed_length > max_chars:
        compressed_content = compressed_content[:max_chars - 20] + '\n...(内容已截断)'
        compressed_length = len(compressed_content)

    return {
        'compressed_content': compressed_content,
        'original_length': original_length,
        'compressed_length': compressed_length,
        'compression_ratio': round(compressed_length / original_length, 3) if original_length > 0 else 0,
        'sections_kept': sections_kept,
        'sections_truncated': sections_truncated,
        'task_type': task_type,
        'max_chars': max_chars,
    }


def _split_sections(body: str) -> list:
    """将正文按markdown章节(## 标题)拆分

    参数:
        body: SKILL.md正文(frontmatter之后的内容)

    返回:
        [
            {
                'title': str,      # 章节标题(不含##)
                'full_text': str,  # 完整章节文本(含标题行)
            }
        ]
    """
    sections = []
    current_title = ''
    current_lines = []

    for line in body.split('\n'):
        # 检测二级标题(## 标题)
        if line.startswith('## '):
            # 保存前一个章节
            if current_title or current_lines:
                sections.append({
                    'title': current_title,
                    'full_text': '\n'.join(current_lines),
                })
            current_title = line[3:].strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    # 保存最后一个章节
    if current_title or current_lines:
        sections.append({
            'title': current_title,
            'full_text': '\n'.join(current_lines),
        })

    return sections

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
