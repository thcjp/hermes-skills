#!/usr/bin/env python3
"""
批量Skill生成脚本 (可复用)
==========================

从数据库筛选候选skill，批量执行生成流水线（L1验证）。
支持按workflow_state、category筛选，分批执行。

Usage:
    python batch_generate.py --limit 100                     # 生成100个
    python batch_generate.py --limit 50 --category Automation # 按类别
    python batch_generate.py --limit 20 --batch-size 5       # 分批，每批5个
    python batch_generate.py --state step5_add_deps           # 指定workflow_state
    python batch_generate.py --dry-run                        # 仅查看候选，不执行
"""
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection
from generate_skill import run_generation_pipeline


def query_candidates(limit: int = 100, category: str = None,
                     workflow_state: str = None) -> list:
    """从DB筛选候选skill"""
    conn = get_db_connection()
    c = conn.cursor()

    # 默认筛选 step5_add_deps + step7_validate
    if workflow_state:
        states = [workflow_state]
    else:
        states = ['step5_add_deps', 'step7_validate']

    placeholders = ','.join('?' * len(states))
    query = f"""
        SELECT slug, category, workflow_state
        FROM skills
        WHERE workflow_state IN ({placeholders})
          AND slug NOT LIKE '%-free%' AND slug NOT LIKE '%-pro%'
          AND workflow_state != 'deprecated'
    """
    params = list(states)

    if category:
        query += " AND category = ?"
        params.append(category)

    query += " ORDER BY category, slug LIMIT ?"
    params.append(limit)

    c.execute(query, params)
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results


def update_workflow_state(slug: str, step_name: str, step_number: int):
    """更新workflow_states表"""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
    row = c.fetchone()
    if not row:
        conn.close()
        return
    skill_id = row['id']
    c.execute("""
        INSERT OR REPLACE INTO workflow_states (skill_id, step_number, step_name, status, completed_at)
        VALUES (?, ?, ?, 'completed', ?)
    """, (skill_id, step_number, step_name, datetime.now().isoformat()))
    c.execute("UPDATE skills SET workflow_state = ? WHERE id = ?", (step_name, skill_id))
    conn.commit()
    conn.close()


def run_batch(candidates: list, batch_size: int = 20) -> dict:
    """执行批量生成"""
    total = len(candidates)
    results = []
    passed = 0
    failed = 0
    start_time = time.time()

    for i, cand in enumerate(candidates, 1):
        slug = cand['slug']
        batch_num = (i - 1) // batch_size + 1
        print(f"\n[{i}/{total}] (批次{batch_num}) 生成: {slug} ({cand['category']})")

        try:
            result = run_generation_pipeline(
                slug=slug,
                skip_l2=True,
                skip_dep_verify=True
            )

            l1_passed = result.get('overall_passed', False)
            if l1_passed:
                passed += 1
                # 更新workflow_state
                update_workflow_state(slug, 'step6_generate_skill', 6)
                update_workflow_state(slug, 'step7_validate', 7)
                print(f"  ✓ L1通过")
            else:
                failed += 1
                l1_result = result.get('l1_result', {})
                print(f"  ✗ L1未通过: {l1_result.get('score', 'N/A')}")

            results.append({
                'slug': slug,
                'category': cand['category'],
                'l1_passed': l1_passed,
                'l1_score': result.get('l1_result', {}).get('score', 'N/A'),
                'template': result.get('template_used'),
                'errors': result.get('errors', []),
            })

        except Exception as e:
            failed += 1
            print(f"  ✗ 异常: {e}")
            results.append({
                'slug': slug,
                'category': cand['category'],
                'l1_passed': False,
                'error': str(e),
            })

        # 批次间进度报告
        if i % batch_size == 0 and i < total:
            elapsed = time.time() - start_time
            rate = i / elapsed
            remaining = (total - i) / rate
            print(f"\n--- 批次{batch_num}完成: {passed}通过/{failed}失败, "
                  f"已用{elapsed:.0f}秒, 预计剩余{remaining:.0f}秒 ---")

    total_time = time.time() - start_time

    summary = {
        'batch_date': datetime.now().isoformat(),
        'total_candidates': total,
        'passed': passed,
        'failed': failed,
        'pass_rate': round(passed / total * 100, 1) if total > 0 else 0,
        'total_duration_sec': round(total_time, 1),
        'avg_duration_sec': round(total_time / total, 1) if total > 0 else 0,
        'results': results,
    }

    return summary


def main():
    parser = argparse.ArgumentParser(description='批量Skill生成脚本')
    parser.add_argument('--limit', type=int, default=100, help='最大生成数量')
    parser.add_argument('--category', help='按类别筛选')
    parser.add_argument('--state', help='指定workflow_state (默认step5_add_deps+step7_validate)')
    parser.add_argument('--batch-size', type=int, default=20, help='每批数量（仅用于进度报告）')
    parser.add_argument('--dry-run', action='store_true', help='仅查看候选，不执行')
    parser.add_argument('-o', '--output', help='报告输出文件')

    args = parser.parse_args()

    # 查询候选
    candidates = query_candidates(
        limit=args.limit,
        category=args.category,
        workflow_state=args.state
    )

    print(f"{'='*70}")
    print(f"批量Skill生成")
    print(f"{'='*70}")
    print(f"候选数: {len(candidates)}")
    print(f"批次大小: {args.batch_size}")

    if args.dry_run:
        print(f"\n候选列表 (dry-run):")
        for i, c in enumerate(candidates, 1):
            print(f"  {i:3d}. {c['slug']:40s} | {c['category']:20s} | {c['workflow_state']}")
        return

    if not candidates:
        print("无候选skill")
        return

    # 执行批量生成
    summary = run_batch(candidates, batch_size=args.batch_size)

    # 保存报告
    if not args.output:
        report_path = SKILL_REGISTRY_DIR / f"batch_generation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    else:
        report_path = Path(args.output)

    report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

    # 打印汇总
    print(f"\n{'='*70}")
    print(f"批量生成汇总")
    print(f"{'='*70}")
    print(f"  总数: {summary['total_candidates']}")
    print(f"  通过: {summary['passed']} ({summary['pass_rate']}%)")
    print(f"  失败: {summary['failed']}")
    print(f"  耗时: {summary['total_duration_sec']}秒 (平均{summary['avg_duration_sec']}秒/skill)")
    print(f"  报告: {report_path}")


if __name__ == '__main__':
    main()
