#!/usr/bin/env python3
"""
Skill 质量看板 (Quality Dashboard)
====================================

可视化质量监控面板，输出5个维度的质量指标。
不依赖外部可视化库，纯终端表格 + JSON输出。

5个维度:
  1. 验证覆盖率: L1/L2/L3各层验证的skill数量和覆盖率
  2. 质量分布: L2 TRACE评分分布 (A/B/C/D等级)
  3. 模板使用: 5种模板的使用数量和平均评分
  4. 推广进度: 10步workflow_states的完成分布
  5. 平台状态: SkillHub/ClawHub的上传成功率和待审核数

Usage:
    python quality_dashboard.py                      # 完整看板（终端表格）
    python quality_dashboard.py --json               # JSON 格式输出
    python quality_dashboard.py --dimension 1        # 仅查看维度1
    python quality_dashboard.py -o dashboard.json    # 保存到文件
    python quality_dashboard.py --dimension 3 --json # 仅模板使用(JSON)

维度编号:
    1=验证覆盖率  2=质量分布  3=模板使用  4=推广进度  5=平台状态
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

from config import (
    DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR,
    TRACE_PASS_THRESHOLD, get_db_connection
)

# 10步workflow定义
WORKFLOW_STEPS = [
    (1, 'read_original'), (2, 'parse_metadata'), (3, 'analyze_content'),
    (4, 'select_template'), (5, 'add_deps'), (6, 'generate_skill'),
    (7, 'validate'), (8, 'upload_free'), (9, 'upload_paid'), (10, 'completed'),
]

# 5种模板名称
TEMPLATE_NAMES = [
    'tool_wrapper_template', 'generator_template', 'reviewer_template',
    'inversion_template', 'pipeline_template',
]

# 已验证的模板-skill映射 (Round 06 + Round 09)
VERIFIED_TEMPLATES = {
    'generator_template': {'slug': 'daily-report-writer', 'l2_score': 47, 'round': 'R06'},
    'reviewer_template': {'slug': 'code-quality', 'l2_score': 38, 'round': 'R06'},
    'pipeline_template': {'slug': 'auto-workflow', 'l2_score': 37, 'round': 'R06'},
    'tool_wrapper_template': {'slug': 'aws-toolkit', 'l2_score': 44, 'round': 'R09'},
    'inversion_template': {'slug': 'doc-parse', 'l2_score': 47, 'round': 'R09'},
}


# ============================================================
# 维度1: 验证覆盖率
# ============================================================

def check_validation_coverage() -> Dict[str, Any]:
    """验证覆盖率: L1/L2/L3各层验证的skill数量和覆盖率"""
    conn = get_db_connection()
    c = conn.cursor()

    # 总skill数 (非deprecated)
    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE workflow_state != 'deprecated'")
    total_skills = c.fetchone()['cnt']

    # L1覆盖: 有quality_gate检查记录的skill (通过generation_report或workflow_state判断)
    c.execute("""
        SELECT COUNT(DISTINCT skill_id) as cnt
        FROM workflow_states
        WHERE step_number >= 7 AND status = 'completed'
    """)
    l1_covered = c.fetchone()['cnt']

    # L2覆盖: 有trace_llm评分记录的skill
    c.execute("""
        SELECT COUNT(DISTINCT skill_id) as cnt
        FROM scores
        WHERE score_type = 'trace_llm'
    """)
    l2_covered = c.fetchone()['cnt']

    # L3覆盖: 有agent_trial评分记录的skill
    c.execute("""
        SELECT COUNT(DISTINCT skill_id) as cnt
        FROM scores
        WHERE score_type = 'agent_trial'
    """)
    l3_covered = c.fetchone()['cnt']

    # L2通过率
    c.execute("""
        SELECT COUNT(DISTINCT skill_id) as cnt
        FROM scores
        WHERE score_type = 'trace_llm' AND is_pass = 1
    """)
    l2_passed = c.fetchone()['cnt']

    # L3通过率
    c.execute("""
        SELECT COUNT(DISTINCT skill_id) as cnt
        FROM scores
        WHERE score_type = 'agent_trial' AND is_pass = 1
    """)
    l3_passed = c.fetchone()['cnt']

    conn.close()

    def pct(n, d):
        return round(n / d * 100, 1) if d > 0 else 0

    return {
        'dimension': '验证覆盖率',
        'total_skills': total_skills,
        'l1': {
            'covered': l1_covered,
            'coverage_rate': pct(l1_covered, total_skills),
        },
        'l2': {
            'covered': l2_covered,
            'coverage_rate': pct(l2_covered, total_skills),
            'passed': l2_passed,
            'pass_rate': pct(l2_passed, l2_covered) if l2_covered > 0 else 0,
        },
        'l3': {
            'covered': l3_covered,
            'coverage_rate': pct(l3_covered, total_skills),
            'passed': l3_passed,
            'pass_rate': pct(l3_passed, l3_covered) if l3_covered > 0 else 0,
        },
    }


# ============================================================
# 维度2: 质量分布
# ============================================================

def check_quality_distribution() -> Dict[str, Any]:
    """质量分布: L2 TRACE评分分布 (A/B/C/D等级)"""
    conn = get_db_connection()
    c = conn.cursor()

    # L2评分等级分布
    c.execute("""
        SELECT
            CASE
                WHEN total_score >= 45 THEN 'A'
                WHEN total_score >= 40 THEN 'B'
                WHEN total_score >= 35 THEN 'C'
                WHEN total_score >= 28 THEN 'D'
                ELSE 'F'
            END as grade,
            COUNT(*) as cnt,
            ROUND(AVG(total_score), 1) as avg_score,
            MIN(total_score) as min_score,
            MAX(total_score) as max_score
        FROM scores
        WHERE score_type = 'trace_llm'
        GROUP BY grade
        ORDER BY grade
    """)
    grade_rows = c.fetchall()

    # L2维度平均分 (T/R/A/C/E)
    c.execute("""
        SELECT
            ROUND(AVG(debranding_score), 1) as avg_trust,
            ROUND(AVG(quality_score), 1) as avg_reliability,
            ROUND(AVG(practicality_score), 1) as avg_adaptability,
            ROUND(AVG(simplicity_score), 1) as avg_convention,
            ROUND(AVG(performance_score), 1) as avg_effectiveness,
            ROUND(AVG(total_score), 1) as avg_total
        FROM scores
        WHERE score_type = 'trace_llm'
    """)
    avg_row = c.fetchone()

    # L3评分分布
    c.execute("""
        SELECT
            CASE
                WHEN total_score >= 90 THEN 'A'
                WHEN total_score >= 80 THEN 'B'
                WHEN total_score >= 70 THEN 'C'
                ELSE 'D'
            END as grade,
            COUNT(*) as cnt
        FROM scores
        WHERE score_type = 'agent_trial'
        GROUP BY grade
        ORDER BY grade
    """)
    l3_grades = c.fetchall()

    conn.close()

    grade_dist = {}
    for r in grade_rows:
        grade_dist[r['grade']] = {
            'count': r['cnt'],
            'avg_score': r['avg_score'],
            'min_score': r['min_score'],
            'max_score': r['max_score'],
        }

    l3_dist = {r['grade']: r['cnt'] for r in l3_grades}

    return {
        'dimension': '质量分布',
        'l2_grade_distribution': grade_dist,
        'l2_dimension_averages': {
            'T_Trust': avg_row['avg_trust'] if avg_row['avg_trust'] else 0,
            'R_Reliability': avg_row['avg_reliability'] if avg_row['avg_reliability'] else 0,
            'A_Adaptability': avg_row['avg_adaptability'] if avg_row['avg_adaptability'] else 0,
            'C_Convention': avg_row['avg_convention'] if avg_row['avg_convention'] else 0,
            'E_Effectiveness': avg_row['avg_effectiveness'] if avg_row['avg_effectiveness'] else 0,
            'Total': avg_row['avg_total'] if avg_row['avg_total'] else 0,
        },
        'l3_grade_distribution': l3_dist,
        'pass_threshold': TRACE_PASS_THRESHOLD,
    }


# ============================================================
# 维度3: 模板使用
# ============================================================

def check_template_usage() -> Dict[str, Any]:
    """模板使用: 5种模板的使用数量和平均评分"""
    conn = get_db_connection()
    c = conn.cursor()

    # 从generation_report中统计模板使用
    template_stats = {}
    for tmpl in TEMPLATE_NAMES:
        template_stats[tmpl] = {
            'generated_count': 0,
            'verified_slug': VERIFIED_TEMPLATES.get(tmpl, {}).get('slug', ''),
            'l2_score': VERIFIED_TEMPLATES.get(tmpl, {}).get('l2_score', 0),
            'verified_round': VERIFIED_TEMPLATES.get(tmpl, {}).get('round', ''),
        }

    # 扫描generation_report_*.json文件
    for report_file in SKILL_REGISTRY_DIR.glob("generation_report_*.json"):
        try:
            report = json.loads(report_file.read_text(encoding='utf-8'))
            tmpl = report.get('template_used')
            if tmpl and tmpl in template_stats:
                template_stats[tmpl]['generated_count'] += 1
        except (json.JSONDecodeError, KeyError):
            continue

    # 计算总生成数和平均分
    total_generated = sum(s['generated_count'] for s in template_stats.values())
    verified_scores = [s['l2_score'] for s in template_stats.values() if s['l2_score'] > 0]
    avg_verified_score = round(sum(verified_scores) / len(verified_scores), 1) if verified_scores else 0

    conn.close()

    return {
        'dimension': '模板使用',
        'total_generated': total_generated,
        'templates': template_stats,
        'avg_verified_l2_score': avg_verified_score,
        'all_templates_verified': len(verified_scores) == len(TEMPLATE_NAMES),
    }


# ============================================================
# 维度4: 推广进度
# ============================================================

def check_rollout_progress() -> Dict[str, Any]:
    """推广进度: 10步workflow_states的完成分布"""
    conn = get_db_connection()
    c = conn.cursor()

    # 各步骤完成数
    step_dist = []
    for step_num, step_name in WORKFLOW_STEPS:
        c.execute("""
            SELECT COUNT(DISTINCT skill_id) as cnt
            FROM workflow_states
            WHERE step_number = ? AND status = 'completed'
        """, (step_num,))
        cnt = c.fetchone()['cnt']
        step_dist.append({
            'step': step_num,
            'name': step_name,
            'completed': cnt,
        })

    # skills表的workflow_state分布
    c.execute("""
        SELECT workflow_state, COUNT(*) as cnt
        FROM skills
        WHERE workflow_state != 'deprecated'
        GROUP BY workflow_state
        ORDER BY cnt DESC
    """)
    state_rows = c.fetchall()
    state_dist = {r['workflow_state']: r['cnt'] for r in state_rows}

    # 总skill数
    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE workflow_state != 'deprecated'")
    total = c.fetchone()['cnt']

    # 完成率
    completed = state_dist.get('completed', 0)
    completion_rate = round(completed / total * 100, 1) if total > 0 else 0

    conn.close()

    return {
        'dimension': '推广进度',
        'total_skills': total,
        'completion_rate': completion_rate,
        'workflow_step_distribution': step_dist,
        'current_state_distribution': state_dist,
    }


# ============================================================
# 维度5: 平台状态
# ============================================================

def check_platform_status() -> Dict[str, Any]:
    """平台状态: SkillHub/ClawHub的上传成功率和待审核数"""
    conn = get_db_connection()
    c = conn.cursor()

    # 检查platform_uploads表是否存在
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='platform_uploads'")
    if not c.fetchone():
        conn.close()
        return {
            'dimension': '平台状态',
            'error': 'platform_uploads表不存在',
            'platforms': {},
        }

    # 各平台上传状态
    c.execute("""
        SELECT platform, upload_status, COUNT(*) as cnt
        FROM platform_uploads
        GROUP BY platform, upload_status
        ORDER BY platform, upload_status
    """)
    upload_rows = c.fetchall()

    platforms = {}
    for r in upload_rows:
        plat = r['platform']
        if plat not in platforms:
            platforms[plat] = {'total': 0, 'success': 0, 'pending': 0, 'failed': 0}
        platforms[plat]['total'] += r['cnt']
        if r['upload_status'] == 'success':
            platforms[plat]['success'] = r['cnt']
        elif r['upload_status'] in ('pending', 'reviewing', 'pending_review'):
            platforms[plat]['pending'] = r['cnt']
        elif r['upload_status'] in ('failed', 'error', 'rejected'):
            platforms[plat]['failed'] = r['cnt']

    # 计算成功率
    for plat in platforms.values():
        plat['success_rate'] = round(plat['success'] / plat['total'] * 100, 1) if plat['total'] > 0 else 0

    # 付费/免费分布 (通过pricing_on_platform字段判断)
    c.execute("""
        SELECT
            CASE
                WHEN pricing_on_platform IS NOT NULL AND pricing_on_platform != '' AND pricing_on_platform != 'free' THEN 'paid'
                WHEN pricing_on_platform = 'free' THEN 'free'
                ELSE 'unspecified'
            END as type,
            COUNT(*) as cnt
        FROM platform_uploads
        WHERE upload_status = 'success'
        GROUP BY type
    """)
    price_rows = c.fetchall()
    price_dist = {r['type']: r['cnt'] for r in price_rows}

    conn.close()

    return {
        'dimension': '平台状态',
        'platforms': platforms,
        'price_distribution': price_dist,
    }


# ============================================================
# 看板输出
# ============================================================

def print_table(headers, rows, col_widths=None):
    """打印终端表格"""
    if not col_widths:
        col_widths = []
        for i, h in enumerate(headers):
            max_len = len(str(h))
            for r in rows:
                if i < len(r):
                    max_len = max(max_len, len(str(r[i])))
            col_widths.append(max_len + 2)

    # 表头
    header_line = '|' + '|'.join(f' {str(h):<{col_widths[i] - 2}} ' for i, h in enumerate(headers)) + '|'
    separator = '+' + '+'.join('-' * col_widths[i] for i in range(len(headers))) + '+'

    print(separator)
    print(header_line)
    print(separator)

    for row in rows:
        row_line = '|' + '|'.join(f' {str(row[i]):<{col_widths[i] - 2}} ' for i in range(len(headers))) + '|'
        print(row_line)

    print(separator)


def print_dashboard(dimension, data):
    """打印单个维度的看板"""
    print(f"\n{'='*70}")
    print(f"  维度{dimension}: {data['dimension']}")
    print(f"{'='*70}")

    if dimension == 1:
        print(f"\n  总Skill数: {data['total_skills']}")
        print_table(
            ['验证层', '覆盖数', '覆盖率', '通过数', '通过率'],
            [
                ['L1 静态检查', data['l1']['covered'], f"{data['l1']['coverage_rate']}%", '-', '-'],
                ['L2 LLM评估', data['l2']['covered'], f"{data['l2']['coverage_rate']}%",
                 data['l2']['passed'], f"{data['l2']['pass_rate']}%"],
                ['L3 Agent试运行', data['l3']['covered'], f"{data['l3']['coverage_rate']}%",
                 data['l3']['passed'], f"{data['l3']['pass_rate']}%"],
            ]
        )

    elif dimension == 2:
        print(f"\n  L2 TRACE评分等级分布 (通过阈值≥{data['pass_threshold']}):")
        grade_rows = []
        for grade in ['A', 'B', 'C', 'D', 'F']:
            if grade in data['l2_grade_distribution']:
                g = data['l2_grade_distribution'][grade]
                grade_rows.append([grade, g['count'], g['avg_score'], g['min_score'], g['max_score']])
        print_table(
            ['等级', '数量', '平均分', '最低分', '最高分'],
            grade_rows
        )

        print(f"\n  L2 TRACE五维度平均分:")
        avgs = data['l2_dimension_averages']
        print_table(
            ['维度', '平均分'],
            [
                ['T (Trust 可信任度)', avgs['T_Trust']],
                ['R (Reliability 可靠性)', avgs['R_Reliability']],
                ['A (Adaptability 适用性)', avgs['A_Adaptability']],
                ['C (Convention 规范性)', avgs['C_Convention']],
                ['E (Effectiveness 有效性)', avgs['E_Effectiveness']],
                ['Total (总分)', avgs['Total']],
            ]
        )

        if data['l3_grade_distribution']:
            print(f"\n  L3 Agent试运行等级分布:")
            l3_rows = [[g, c] for g, c in data['l3_grade_distribution'].items()]
            print_table(['等级', '数量'], l3_rows)

    elif dimension == 3:
        print(f"\n  总生成数: {data['total_generated']}")
        print(f"  已验证模板数: {sum(1 for t in data['templates'].values() if t['l2_score'] > 0)}/5")
        print(f"  已验证模板平均L2分: {data['avg_verified_l2_score']}")
        print(f"  全模板验证完成: {'✓' if data['all_templates_verified'] else '✗'}")

        print(f"\n  模板使用详情:")
        tmpl_rows = []
        for name, stats in data['templates'].items():
            tmpl_rows.append([
                name.replace('_template', ''),
                stats['generated_count'],
                stats['verified_slug'] or '-',
                stats['l2_score'] or '-',
                stats['verified_round'] or '-',
            ])
        print_table(
            ['模板', '生成数', '验证skill', 'L2分数', '轮次'],
            tmpl_rows
        )

    elif dimension == 4:
        print(f"\n  总Skill数: {data['total_skills']}")
        print(f"  完成率: {data['completion_rate']}%")

        print(f"\n  10步Workflow完成分布:")
        step_rows = [[s['step'], s['name'], s['completed']] for s in data['workflow_step_distribution']]
        print_table(['步骤', '名称', '完成数'], step_rows)

        print(f"\n  当前workflow_state分布:")
        state_rows = [[k, v] for k, v in data['current_state_distribution'].items()]
        print_table(['workflow_state', '数量'], state_rows)

    elif dimension == 5:
        if 'error' in data:
            print(f"\n  ⚠ {data['error']}")
            return

        for plat_name, plat_data in data['platforms'].items():
            print(f"\n  平台: {plat_name}")
            print_table(
                ['指标', '数值'],
                [
                    ['总上传数', plat_data['total']],
                    ['成功', plat_data['success']],
                    ['待审核', plat_data['pending']],
                    ['失败', plat_data['failed']],
                    ['成功率', f"{plat_data['success_rate']}%"],
                ]
            )

        if data['price_distribution']:
            print(f"\n  付费/免费分布 (成功上传):")
            price_rows = [[k, v] for k, v in data['price_distribution'].items()]
            print_table(['类型', '数量'], price_rows)


def run_dashboard(dimension=None, output_json=False, output_file=None):
    """运行质量看板"""
    dimensions = {
        1: check_validation_coverage,
        2: check_quality_distribution,
        3: check_template_usage,
        4: check_rollout_progress,
        5: check_platform_status,
    }

    if dimension:
        dims_to_run = {dimension: dimensions[dimension]}
    else:
        dims_to_run = dimensions

    results = {}
    for dim_num, dim_func in dims_to_run.items():
        results[dim_num] = dim_func()

    # 输出
    if output_json:
        output = json.dumps(results, ensure_ascii=False, indent=2)
        print(output)
    else:
        for dim_num, data in results.items():
            print_dashboard(dim_num, data)

    # 保存到文件
    if output_file:
        report_path = Path(output_file)
        report_path.write_text(
            json.dumps({
                'generated_at': datetime.now().isoformat(),
                'dimensions': results,
            }, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )
        if not output_json:
            print(f"\n  看板已保存: {report_path}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Skill质量看板 - 5维度质量监控"
    )
    parser.add_argument('--dimension', type=int, choices=[1, 2, 3, 4, 5],
                        help='查看指定维度 (1=验证覆盖率 2=质量分布 3=模板使用 4=推广进度 5=平台状态)')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')
    parser.add_argument('-o', '--output', help='保存报告到文件')

    args = parser.parse_args()

    run_dashboard(
        dimension=args.dimension,
        output_json=args.json,
        output_file=args.output
    )


if __name__ == '__main__':
    main()
