#!/usr/bin/env python3
"""
Skill真实agent试运行器 (L3验证层)
===================================

L3是分层验证的最深层级,在定稿发布前执行。
实际启动agent加载SKILL.md,用3个典型输入测试真实输出。

与L2的区别:
  - L2: 模拟评估(判断skill"是否可能"正确运行)
  - L3: 真实执行(实际运行skill流程,产出真实输出)

验证内容:
  1. 真实加载: agent能否正确加载SKILL.md并理解指令
  2. 真实执行: 3个典型输入能否产出预期结果
  3. 异常处理: 边界输入(空/超长/非法)是否有合理反馈
  4. 输出可用性: 输出结果是否可直接使用(非占位符/非模板)

设计理念:
  - 不硬编码调用外部agent框架
  - 生成试运行prompt,由AI(当前会话)充当agent执行
  - 复用 llm_validator.py 的 find_skill_md 和触发测试用例
  - 试运行结果保存为JSON报告

Usage:
    python agent_trial.py --help
    python agent_trial.py trial <slug>                    # 生成试运行prompt
    python agent_trial.py trial <slug> --json              # 输出JSON格式
    python agent_trial.py trial <slug> -o report.json      # 保存报告到文件
    python agent_trial.py import <slug> <result.json>      # 导入试运行结果

流程:
    Step 1: 读取SKILL.md内容
    Step 2: 生成3个典型输入(复用llm_validator的触发测试用例)
    Step 3: 生成3个异常输入(空/超长/非法)
    Step 4: 生成试运行prompt(含SKILL.md内容+输入+评估标准)
    Step 5: AI执行试运行(当前会话,非脚本自动)
    Step 6: 导入试运行结果,输出L3验证结论
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

from config import get_db_connection, DB_PATH
from trace_llm_scorer import read_skill_md, save_trace_score, static_check, calculate_static_scores
from llm_validator import find_skill_md, get_skill_id, generate_trigger_test_cases


# ============ 异常输入生成 ============

def generate_edge_case_inputs(slug: str) -> List[Dict[str, Any]]:
    """生成3个边界异常输入用于异常处理测试
    
    类型:
      1. 空输入: 必填字段为空
      2. 超长输入: 超出合理长度
      3. 非法参数: 参数值不在允许范围内
    """
    return [
        {
            'id': 'edge_empty',
            'type': 'empty_input',
            'input': {'topic': '', 'platform': ''},
            'expected_behavior': '返回success=false, error="主题不能为空"',
            'reason': '测试必填字段为空时的异常处理'
        },
        {
            'id': 'edge_too_long',
            'type': 'too_long_input',
            'input': {'topic': 'A' * 5000, 'platform': 'xiaohongshu'},
            'expected_behavior': '正常处理或截断,不应崩溃或超时',
            'reason': '测试超长输入的健壮性'
        },
        {
            'id': 'edge_invalid_param',
            'type': 'invalid_param',
            'input': {'topic': '测试主题', 'platform': 'invalid_platform_xyz', 'hook_type': 'invalid_hook'},
            'expected_behavior': 'platform降级为通用文案,hook_type默认pain_resonance,标注warning',
            'reason': '测试非法参数值的降级处理'
        }
    ]


# ============ 试运行prompt生成 ============

def generate_trial_prompt(skill_content: str, slug: str,
                          typical_inputs: List[Dict],
                          edge_inputs: List[Dict]) -> str:
    """生成L3试运行prompt
    
    AI(当前会话)读取此prompt后,作为agent真实执行skill流程
    """
    prompt = f"""# L3验证: 真实agent试运行任务

## 被试运行Skill: {slug}

## 完整SKILL.md内容
{skill_content}

## 试运行任务

请作为真实agent,加载上方SKILL.md,执行以下6个试运行用例。
每个用例都要**实际执行**skill定义的流程,产出真实输出(非占位符/非模板)。

### 第一部分: 3个典型输入(真实执行)

"""
    for i, tc in enumerate(typical_inputs, 1):
        prompt += f"""#### 典型用例 {i}: {tc['id']}
- **用户输入**: 「{tc['user_input']}」
- **试运行要求**: 
  1. 按SKILL.md的"使用流程"执行完整流程
  2. 构造符合"输入格式"的JSON输入(基于用户输入意图)
  3. 产出符合"输出格式"的真实JSON输出
  4. 输出内容必须真实可用,不能是占位符(如"xxx"/"..."/"待填充")
- **评估标准**:
  - PASS: 产出完整JSON,包含所有输出字段,内容真实可用
  - WARN: 产出基本完整,但部分字段内容简略
  - FAIL: 未产出/产出占位符/格式错误

"""
    prompt += """### 第二部分: 3个异常输入(异常处理测试)

"""
    for i, ei in enumerate(edge_inputs, 1):
        prompt += f"""#### 异常用例 {i}: {ei['id']} ({ei['type']})
- **输入**: {json.dumps(ei['input'], ensure_ascii=False)}
- **预期行为**: {ei['expected_behavior']}
- **评估标准**:
  - PASS: 按预期处理(返回错误/降级/默认值),不崩溃
  - WARN: 有处理但与预期不完全一致
  - FAIL: 崩溃/无响应/未按异常处理表处理

"""
    prompt += """### 第三部分: 输出可用性评估

完成上述6个试运行后,评估所有输出的可用性:

1. **非占位符检查**: 所有输出字段是否为真实内容(非"xxx"/"..."等占位符)
2. **非模板检查**: 输出是否针对具体输入定制(非套用固定模板)
3. **直接可用性**: 输出结果是否能直接使用(无需人工补充)
4. **格式合规性**: 输出是否符合SKILL.md定义的输出格式

## 输出格式(严格JSON)

```json
{
  "slug": "%s",
  "trial_executed_at": "<ISO时间>",
  "typical_inputs_results": [
    {
      "id": "tc1",
      "status": "PASS|WARN|FAIL",
      "input_used": {},
      "actual_output": {},
      "evaluation": "评估说明"
    }
  ],
  "edge_inputs_results": [
    {
      "id": "edge_empty",
      "status": "PASS|WARN|FAIL",
      "actual_behavior": "实际行为",
      "evaluation": "评估说明"
    }
  ],
  "output_usability": {
    "non_placeholder": true,
    "non_template": true,
    "directly_usable": true,
    "format_compliant": true,
    "details": "可用性评估说明"
  },
  "l3_passed": false,
  "l3_summary": "L3试运行总结"
}
```
""" % slug

    return prompt


# ============ L3验证核心 ============

def run_l3_trial(slug: str, output_json: bool = False, output_file: str = None) -> Dict[str, Any]:
    """运行L3试运行
    
    流程:
      1. 查找SKILL.md
      2. 生成3个典型输入(复用llm_validator)
      3. 生成3个异常输入
      4. 生成试运行prompt(供AI执行)
      5. 输出报告(待AI试运行)
    """
    result = {
        'slug': slug,
        'trial_started_at': datetime.now().isoformat(),
        'l3_version': '1.0',
        'status': 'pending_trial',
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

    # Step 2: 生成3个典型输入
    typical_inputs = generate_trigger_test_cases(skill_content, slug)
    result['typical_inputs'] = typical_inputs

    # Step 3: 生成3个异常输入
    edge_inputs = generate_edge_case_inputs(slug)
    result['edge_inputs'] = edge_inputs

    # Step 4: 生成试运行prompt
    trial_prompt = generate_trial_prompt(skill_content, slug, typical_inputs, edge_inputs)
    result['trial_prompt'] = trial_prompt
    result['trial_prompt_length'] = len(trial_prompt)

    # Step 5: 预评估信息
    result['pre_eval_info'] = {
        'total_test_cases': len(typical_inputs) + len(edge_inputs),
        'typical_count': len(typical_inputs),
        'edge_count': len(edge_inputs),
        'note': 'AI需执行6个试运行用例(3典型+3异常),评估输出可用性'
    }

    # 保存报告
    if output_file:
        report_path = Path(output_file)
    else:
        report_path = SKILL_REGISTRY_DIR / f'l3_trial_report_{slug}.json'

    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    result['report_path'] = str(report_path)

    # 终端输出
    if not output_json:
        print(f"\n{'='*70}")
        print(f"L3试运行报告: {slug}")
        print(f"{'='*70}")
        print(f"SKILL.md路径: {skill_md_path}")
        print(f"试运行启动时间: {result['trial_started_at']}")
        print(f"\n--- 典型输入({len(typical_inputs)}个) ---")
        for tc in typical_inputs:
            print(f"  {tc['id']}: 「{tc['user_input']}」")
        print(f"\n--- 异常输入({len(edge_inputs)}个) ---")
        for ei in edge_inputs:
            print(f"  {ei['id']} ({ei['type']}): {ei['reason']}")
        print(f"\n--- 试运行任务 ---")
        print(f"  状态: 待AI执行 (prompt已生成, {len(trial_prompt)}字符)")
        print(f"  总用例数: {result['pre_eval_info']['total_test_cases']}")
        print(f"  报告路径: {report_path}")
        print(f"\n下一步: AI读取报告中的trial_prompt字段, 执行6个试运行用例后")
        print(f"        运行: python agent_trial.py import {slug} <试运行结果.json>")
        print(f"{'='*70}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    return result


def import_trial_result(slug: str, result_file: str) -> Dict[str, Any]:
    """导入AI试运行结果,输出L3验证最终结论
    
    流程:
      1. 读取AI试运行结果JSON
      2. 获取skill_id
      3. 评估L3是否通过(3/3典型PASS + 异常处理PASS + 输出可用)
      4. 保存L3最终报告
    """
    result_path = Path(result_file)
    if not result_path.exists():
        return {'error': f'试运行结果文件不存在: {result_file}'}

    with open(result_path, 'r', encoding='utf-8') as f:
        trial_result = json.load(f)

    # 获取skill_id
    skill_id = get_skill_id(slug)
    if not skill_id:
        return {'error': f'DB中找不到skill: {slug}'}

    # 评估典型输入结果
    typical_results = trial_result.get('typical_inputs_results', [])
    typical_pass_count = sum(1 for r in typical_results if r.get('status') == 'PASS')
    typical_total = len(typical_results)

    # 评估异常输入结果
    edge_results = trial_result.get('edge_inputs_results', [])
    edge_pass_count = sum(1 for r in edge_results if r.get('status') == 'PASS')
    edge_total = len(edge_results)

    # 评估输出可用性
    output_usability = trial_result.get('output_usability', {})
    usability_pass = all([
        output_usability.get('non_placeholder', False),
        output_usability.get('non_template', False),
        output_usability.get('directly_usable', False),
        output_usability.get('format_compliant', False),
    ])

    # L3通过标准: 3/3典型PASS + 2/3以上异常PASS + 输出可用
    typical_pass = typical_pass_count == typical_total and typical_total >= 3
    edge_pass = edge_pass_count >= 2 and edge_total >= 3
    l3_passed = typical_pass and edge_pass and usability_pass

    # 计算L3评分(0-100)
    typical_score = (typical_pass_count / max(typical_total, 1)) * 40  # 40分
    edge_score = (edge_pass_count / max(edge_total, 1)) * 30  # 30分
    usability_score = (sum([
        output_usability.get('non_placeholder', False),
        output_usability.get('non_template', False),
        output_usability.get('directly_usable', False),
        output_usability.get('format_compliant', False),
    ]) / 4) * 30  # 30分
    l3_score = round(typical_score + edge_score + usability_score, 1)

    # 确定等级
    if l3_score >= 90:
        l3_grade = 'A'
    elif l3_score >= 80:
        l3_grade = 'B'
    elif l3_score >= 70:
        l3_grade = 'C'
    else:
        l3_grade = 'D'

    final_result = {
        'slug': slug,
        'skill_id': skill_id,
        'imported_at': datetime.now().isoformat(),
        'l3_score': l3_score,
        'l3_grade': l3_grade,
        'l3_passed': l3_passed,
        'typical_results': {
            'pass_count': typical_pass_count,
            'total': typical_total,
            'all_pass': typical_pass,
            'details': typical_results,
        },
        'edge_results': {
            'pass_count': edge_pass_count,
            'total': edge_total,
            'sufficient_pass': edge_pass,
            'details': edge_results,
        },
        'output_usability': {
            'all_pass': usability_pass,
            'details': output_usability,
        },
        'checks_summary': {
            'typical_execution': f"{typical_pass_count}/{typical_total} PASS",
            'exception_handling': f"{edge_pass_count}/{edge_total} PASS",
            'output_usability': 'PASS' if usability_pass else 'FAIL',
        }
    }

    # 保存最终报告
    final_report_path = SKILL_REGISTRY_DIR / f'l3_final_report_{slug}.json'
    with open(final_report_path, 'w', encoding='utf-8') as f:
        json.dump(final_result, f, ensure_ascii=False, indent=2)

    # 写入 DB scores 表 (与 trace_llm_scorer.save_trace_score 保持一致)
    try:
        conn = get_db_connection()
        c = conn.cursor()
        # 先删除旧的 agent_trial 评分记录(避免重复)
        c.execute("DELETE FROM scores WHERE skill_id = ? AND score_type = 'agent_trial'", (skill_id,))
        # 插入新的评分记录 (使用与 scores 表结构匹配的字段)
        # L3 评分映射: typical_score→quality_score, edge_score→practicality_score,
        #              usability_score→simplicity_score, l3_score→total_score
        notes = json.dumps({
            'l3_grade': l3_grade,
            'l3_passed': l3_passed,
            'typical_pass': f"{typical_pass_count}/{typical_total}",
            'edge_pass': f"{edge_pass_count}/{edge_total}",
            'usability_pass': usability_pass,
        }, ensure_ascii=False)
        c.execute("""
            INSERT INTO scores (skill_id, score_type, total_score,
                quality_score, practicality_score, simplicity_score,
                performance_score, debranding_score, differentiation_score,
                compliance_score, cost_score, scored_at, reviewer, notes, is_pass, pass_threshold)
            VALUES (?, 'agent_trial', ?, ?, ?, ?, 0, 0, 0, 0, 0, ?, 'agent_trial_v1', ?, ?, 70)
        """, (
            skill_id,
            int(l3_score),
            int(typical_score),
            int(edge_score),
            int(usability_score),
            datetime.now().isoformat(),
            notes,
            1 if l3_passed else 0
        ))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"  ⚠ DB写入scores表失败: {e}")

    # 终端输出
    print(f"\n{'='*70}")
    print(f"L3试运行最终结论: {slug}")
    print(f"{'='*70}")
    print(f"  L3评分: {l3_score}/100")
    print(f"  等级: {l3_grade}")
    print(f"  L3通过: {'✓ PASS' if l3_passed else '✗ FAIL'}")
    print(f"\n  检查项汇总:")
    print(f"    典型输入执行: {typical_pass_count}/{typical_total} PASS")
    print(f"    异常处理测试: {edge_pass_count}/{edge_total} PASS")
    print(f"    输出可用性: {'PASS' if usability_pass else 'FAIL'}")
    print(f"      - 非占位符: {'✓' if output_usability.get('non_placeholder') else '✗'}")
    print(f"      - 非模板: {'✓' if output_usability.get('non_template') else '✗'}")
    print(f"      - 直接可用: {'✓' if output_usability.get('directly_usable') else '✗'}")
    print(f"      - 格式合规: {'✓' if output_usability.get('format_compliant') else '✗'}")
    print(f"\n  典型输入详情:")
    for r in typical_results:
        status_icon = '✓' if r.get('status') == 'PASS' else ('⚠' if r.get('status') == 'WARN' else '✗')
        print(f"    {status_icon} {r.get('id', 'N/A')}: {r.get('status', 'N/A')}")
    print(f"\n  异常输入详情:")
    for r in edge_results:
        status_icon = '✓' if r.get('status') == 'PASS' else ('⚠' if r.get('status') == 'WARN' else '✗')
        print(f"    {status_icon} {r.get('id', 'N/A')}: {r.get('status', 'N/A')}")
    print(f"\n  最终报告: {final_report_path}")
    print(f"{'='*70}")

    return final_result


# ============ CLI ============

def main():
    parser = argparse.ArgumentParser(
        description='Skill真实agent试运行器 (L3验证层) - 定稿发布前执行真实试运行',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 生成试运行prompt
  python agent_trial.py trial sales-copy-writer

  # 输出JSON格式
  python agent_trial.py trial sales-copy-writer --json

  # 保存报告到指定文件
  python agent_trial.py trial sales-copy-writer -o report.json

  # 导入AI试运行结果
  python agent_trial.py import sales-copy-writer trial_result.json

流程说明:
  1. trial: 生成L3试运行报告(含试运行prompt),待AI执行
  2. AI读取报告中的trial_prompt, 作为agent执行6个试运行用例(3典型+3异常)
  3. import: 导入AI试运行结果, 输出L3验证最终结论

L3通过标准:
  - 3/3典型输入PASS
  - 2/3以上异常输入PASS
  - 输出可用性4项全部PASS(非占位符/非模板/直接可用/格式合规)
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # trial子命令
    trial_parser = subparsers.add_parser('trial', help='生成试运行prompt')
    trial_parser.add_argument('slug', help='Skill slug名称')
    trial_parser.add_argument('--json', action='store_true', help='输出JSON格式')
    trial_parser.add_argument('-o', '--output', help='报告保存路径')

    # import子命令
    imp_parser = subparsers.add_parser('import', help='导入AI试运行结果')
    imp_parser.add_argument('slug', help='Skill slug名称')
    imp_parser.add_argument('result_file', help='AI试运行结果JSON文件路径')

    args = parser.parse_args()

    if args.command == 'trial':
        run_l3_trial(args.slug, output_json=args.json, output_file=args.output)
    elif args.command == 'import':
        import_trial_result(args.slug, args.result_file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
