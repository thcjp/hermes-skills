#!/usr/bin/env python3
"""
运维闭环脚本 (Ops Closed-Loop)
==============================
整合 health_check + quality_dashboard + trace_llm_scorer.annotate
形成完整的运维闭环: 检测 → 识别问题 → 标注优化 → 生成报告

闭环流程:
  1. 运行 health_check → 识别DB/文件/平台问题
  2. 运行 quality_dashboard → 识别质量分布
  3. 运行 annotate → 标注需优化skill
  4. 汇总生成运维报告

Usage:
    python ops闭环.py                     # 完整闭环（终端输出）
    python ops闭环.py --json              # JSON 格式输出
    python ops闭环.py -o ops_report.json  # 保存报告到文件
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List

SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection, TRACE_PASS_THRESHOLD, L2_PASS_THRESHOLD, L2_EXCELLENT_THRESHOLD


def run_health_check() -> dict:
    """运行健康检查"""
    result = subprocess.run(
        ['python', 'health_check.py', '--json'],
        capture_output=True, text=True, cwd=str(SKILL_REGISTRY_DIR)
    )
    if result.returncode == 0 and result.stdout:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {'error': 'health_check JSON解析失败', 'raw': result.stdout[:500]}
    return {'error': f'health_check执行失败: {result.stderr[:200]}'}


def run_quality_dashboard() -> dict:
    """运行质量看板"""
    result = subprocess.run(
        ['python', 'quality_dashboard.py', '--json'],
        capture_output=True, text=True, cwd=str(SKILL_REGISTRY_DIR)
    )
    if result.returncode == 0 and result.stdout:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {'error': 'quality_dashboard JSON解析失败', 'raw': result.stdout[:500]}
    return {'error': f'quality_dashboard执行失败: {result.stderr[:200]}'}


def run_low_score_annotation() -> dict:
    """运行低分标注"""
    # 直接查询DB获取低分skill
    conn = get_db_connection()
    c = conn.cursor()
    
    # 查询B/C级skill
    c.execute("""
        SELECT s.slug, s.category, sc.total_score
        FROM scores sc 
        JOIN skills s ON s.id = sc.skill_id 
        WHERE sc.score_type='trace_llm' AND sc.total_score < ?
        ORDER BY sc.total_score ASC
    """, (L2_EXCELLENT_THRESHOLD,))
    
    low_scores = c.fetchall()
    
    # 统计等级分布
    c.execute("""
        SELECT 
          CASE 
            WHEN total_score >= 45 THEN 'A'
            WHEN total_score >= 40 THEN 'B'
            WHEN total_score >= 35 THEN 'C'
            ELSE 'D'
          END as grade,
          COUNT(*) as cnt
        FROM scores 
        WHERE score_type='trace_llm' 
        GROUP BY grade
    """)
    grade_dist = {row[0]: row[1] for row in c.fetchall()}
    
    conn.close()
    
    return {
        'low_score_count': len(low_scores),
        'low_score_skills': [
            {'slug': row[0], 'category': row[1], 'score': row[2]}
            for row in low_scores[:20]  # 前20个
        ],
        'grade_distribution': grade_dist,
    }


def run_l3_coverage_check() -> dict:
    """检查L3覆盖率"""
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM scores WHERE score_type='agent_trial'")
    l3_count = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) FROM skills WHERE workflow_state != 'deprecated'")
    total = c.fetchone()[0]
    
    c.execute("""
        SELECT s.slug, sc.total_score
        FROM scores sc 
        JOIN skills s ON s.id = sc.skill_id 
        WHERE sc.score_type='agent_trial'
        ORDER BY sc.total_score DESC
    """)
    l3_skills = [{'slug': row[0], 'score': row[1]} for row in c.fetchall()]
    
    conn.close()
    
    return {
        'l3_count': l3_count,
        'total_skills': total,
        'l3_coverage': round(l3_count / max(total, 1) * 100, 2),
        'l3_skills': l3_skills,
    }


def run_coverage_check() -> dict:
    """直接从DB查询覆盖率"""
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM skills WHERE workflow_state != 'deprecated'")
    total = c.fetchone()[0]
    
    # L1覆盖率: step6+的skill
    c.execute("""
        SELECT COUNT(*) FROM skills 
        WHERE workflow_state IN ('step6_generate_skill','step7_validate','step8_upload_free','step9_upload_paid','completed')
    """)
    l1_count = c.fetchone()[0]
    
    # L2覆盖率
    c.execute("SELECT COUNT(*) FROM scores WHERE score_type='trace_llm'")
    l2_count = c.fetchone()[0]
    
    # 完成率
    c.execute("SELECT COUNT(*) FROM skills WHERE workflow_state='completed'")
    completed = c.fetchone()[0]
    
    conn.close()
    
    return {
        'total_skills': total,
        'l1_count': l1_count,
        'l1_coverage': round(l1_count / max(total, 1) * 100, 1),
        'l2_count': l2_count,
        'l2_coverage': round(l2_count / max(total, 1) * 100, 1),
        'completed': completed,
        'completion_rate': round(completed / max(total, 1) * 100, 1),
    }


def generate_ops_report() -> dict:
    """生成完整运维报告"""
    report_time = datetime.now()
    
    print("正在运行运维闭环检查...")
    print("  [1/4] 健康检查...")
    health = run_health_check()
    
    print("  [2/4] 质量看板...")
    quality = run_quality_dashboard()
    
    print("  [3/4] 低分标注...")
    low_scores = run_low_score_annotation()
    
    print("  [4/4] L3覆盖率...")
    l3_coverage = run_l3_coverage_check()
    
    print("  [补充] 覆盖率直接查询...")
    coverage = run_coverage_check()
    
    # 汇总状态
    issues = []
    
    # 检查健康状态
    if 'overall_status' in health:
        if health['overall_status'] == 'critical':
            issues.append('健康检查: 有严重问题')
        elif health['overall_status'] == 'warning':
            issues.append('健康检查: 有警告')
    
    # 检查L1覆盖率
    l1_coverage = coverage.get('l1_coverage', 0)
    if l1_coverage < 80:
        issues.append(f'L1覆盖率不足: {l1_coverage}% (目标≥80%)')
    
    # 检查L2 A级比例
    grade_dist = low_scores.get('grade_distribution', {})
    total_l2 = sum(grade_dist.values())
    a_count = grade_dist.get('A', 0)
    a_ratio = a_count / max(total_l2, 1) * 100
    if a_ratio < 98:
        issues.append(f'L2 A级比例不足: {a_ratio:.1f}% (目标≥98%)')
    
    # 检查L3覆盖率
    l3_pct = l3_coverage.get('l3_coverage', 0)
    if l3_pct < 1:
        issues.append(f'L3覆盖率不足: {l3_pct}% (目标≥1%)')
    
    # 检查低分skill
    low_count = low_scores.get('low_score_count', 0)
    if low_count > 0:
        issues.append(f'低分skill数量: {low_count} (目标0)')
    
    # 确定整体状态
    if any('严重' in i or 'critical' in i for i in issues):
        overall_status = 'critical'
    elif issues:
        overall_status = 'warning'
    else:
        overall_status = 'healthy'
    
    report = {
        'report_time': report_time.isoformat(),
        'overall_status': overall_status,
        'issues': issues,
        'health_check': health,
        'quality_dashboard': quality,
        'low_score_annotation': low_scores,
        'l3_coverage': l3_coverage,
        'coverage': coverage,
        'summary': {
            'total_skills': coverage.get('total_skills', 0),
            'l1_coverage': l1_coverage,
            'l2_coverage': coverage.get('l2_coverage', 0),
            'l2_a_ratio': round(a_ratio, 1),
            'l3_coverage': l3_pct,
            'low_score_count': low_count,
            'completion_rate': coverage.get('completion_rate', 0),
            'issues_count': len(issues),
        }
    }
    
    return report


def print_terminal_report(report: dict):
    """终端输出运维报告"""
    print(f"\n{'='*70}")
    print(f"运维闭环报告 (Ops Closed-Loop Report)")
    print(f"{'='*70}")
    print(f"时间: {report['report_time']}")
    print(f"整体状态: {report['overall_status'].upper()}")
    
    summary = report.get('summary', {})
    print(f"\n--- 汇总指标 ---")
    print(f"  总skill数: {summary.get('total_skills', 'N/A')}")
    print(f"  L1覆盖率: {summary.get('l1_coverage', 'N/A')}%")
    print(f"  L2覆盖率: {summary.get('l2_coverage', 'N/A')}%")
    print(f"  L2 A级比例: {summary.get('l2_a_ratio', 'N/A')}%")
    print(f"  L3覆盖率: {summary.get('l3_coverage', 'N/A')}%")
    print(f"  低分skill数: {summary.get('low_score_count', 'N/A')}")
    
    if report['issues']:
        print(f"\n--- 发现问题 ({len(report['issues'])}个) ---")
        for i, issue in enumerate(report['issues'], 1):
            print(f"  [{i}] {issue}")
    else:
        print(f"\n--- 无问题 ---")
    
    # 低分skill列表
    low_scores = report.get('low_score_annotation', {})
    low_skills = low_scores.get('low_score_skills', [])
    if low_skills:
        print(f"\n--- 低分skill (前{len(low_skills)}个) ---")
        for s in low_skills:
            print(f"  {s['slug']} [{s['category']}]: {s['score']}/50")
    
    # L3 skill列表
    l3_info = report.get('l3_coverage', {})
    l3_skills = l3_info.get('l3_skills', [])
    if l3_skills:
        print(f"\n--- L3试运行skill ({len(l3_skills)}个) ---")
        for s in l3_skills:
            print(f"  {s['slug']}: {s['score']}/100")
    
    print(f"\n{'='*70}")


def main():
    parser = argparse.ArgumentParser(description='运维闭环脚本')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')
    parser.add_argument('-o', '--output', type=str, help='保存报告到文件')
    args = parser.parse_args()
    
    report = generate_ops_report()
    
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_terminal_report(report)
    
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n报告已保存: {output_path}")


if __name__ == '__main__':
    main()
