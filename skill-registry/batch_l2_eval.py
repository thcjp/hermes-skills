#!/usr/bin/env python3
"""
批量L2评估脚本 (可复用)
========================

对已生成的skill批量执行L2评估（静态T+C + 内容R+A+E），保存评分到DB。
支持按workflow_state、category、L2已评估状态筛选。

Usage:
    python batch_l2_eval.py --limit 100                # 评估100个
    python batch_l2_eval.py --category Automation      # 按类别
    python batch_l2_eval.py --only-unevaluated         # 仅评估未评估的skill
    python batch_l2_eval.py --dry-run                  # 仅查看候选
"""
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection, TRACE_PASS_THRESHOLD
from trace_llm_scorer import read_skill_md, static_check, calculate_static_scores, save_trace_score

PACKAGED_DIR = Path(r"D:\skills\packaged-skills\skillhub")


def evaluate_r_a_e(content: str) -> dict:
    """基于内容质量评估R(可靠性)、A(适用性)、E(有效性)维度"""
    # R维度
    r_score = 5
    if '异常处理' in content or '错误处理' in content: r_score += 2
    if '边界' in content or '空输入' in content or '超长' in content: r_score += 1
    if '降级' in content or '默认值' in content: r_score += 1
    if '重试' in content: r_score += 1
    r_score = min(10, r_score)

    # A维度
    a_score = 5
    if '适用场景' in content or '使用场景' in content: a_score += 2
    if '不适用' in content: a_score += 1
    if '触发' in content: a_score += 1
    a_score = min(10, a_score)

    # E维度
    e_score = 5
    if '案例' in content or '示例' in content: e_score += 2
    if '```json' in content or '```python' in content: e_score += 1
    if '输出格式' in content: e_score += 1
    if 'FAQ' in content or '常见问题' in content: e_score += 1
    e_score = min(10, e_score)

    return {
        'reliability': r_score,
        'adaptability': a_score,
        'effectiveness': e_score,
    }


def query_candidates(limit: int = 100, category: str = None,
                     only_unevaluated: bool = False) -> list:
    """查询待评估的skill"""
    conn = get_db_connection()
    c = conn.cursor()

    query = """
        SELECT s.slug, s.category, s.workflow_state, s.local_path
        FROM skills s
        WHERE s.workflow_state IN ('step7_validate', 'step6_generate_skill', 'step8_upload_free', 'completed')
          AND s.slug NOT LIKE '%-free%' AND s.slug NOT LIKE '%-pro%'
          AND s.workflow_state != 'deprecated'
    """
    params = []

    if only_unevaluated:
        query += """
          AND s.id NOT IN (
            SELECT DISTINCT skill_id FROM scores WHERE score_type = 'trace_llm'
          )
        """

    if category:
        query += " AND s.category = ?"
        params.append(category)

    query += " ORDER BY s.category, s.slug LIMIT ?"
    params.append(limit)

    c.execute(query, params)
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results


def evaluate_skill(slug: str, skill_md_path: Path) -> dict:
    """评估单个skill的L2评分"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]

    # 静态检查 (T+C维度)
    checks = static_check(content)
    static_scores = calculate_static_scores(checks)

    # R+A+E评估
    rae = evaluate_r_a_e(content)

    trust_score = static_scores['trust_static']
    convention_score = static_scores['convention_static']
    total = round(trust_score + rae['reliability'] + rae['adaptability'] +
                  convention_score + rae['effectiveness'], 1)

    if total >= 45: grade = 'A'
    elif total >= 40: grade = 'B'
    elif total >= 35: grade = 'C'
    else: grade = 'D'

    return {
        'trust': trust_score,
        'reliability': rae['reliability'],
        'adaptability': rae['adaptability'],
        'convention': convention_score,
        'effectiveness': rae['effectiveness'],
        'total': total,
        'grade': grade,
        'is_pass': total >= TRACE_PASS_THRESHOLD,
        'checks': checks,
        'static_scores': static_scores,
    }


def save_to_db(slug: str, eval_result: dict):
    """保存L2评分到DB"""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
    row = c.fetchone()
    if not row:
        conn.close()
        return False

    skill_id = row['id']
    c.execute("DELETE FROM scores WHERE skill_id = ? AND score_type = 'trace_llm'", (skill_id,))
    conn.commit()
    conn.close()

    llm_result = {
        'trace_scores': {
            'trust': {'score': eval_result['trust'], 'reason': '静态检查', 'suggestion': ''},
            'reliability': {'score': eval_result['reliability'], 'reason': '内容评估', 'suggestion': ''},
            'adaptability': {'score': eval_result['adaptability'], 'reason': '内容评估', 'suggestion': ''},
            'convention': {'score': eval_result['convention'], 'reason': '静态检查', 'suggestion': ''},
            'effectiveness': {'score': eval_result['effectiveness'], 'reason': '内容评估', 'suggestion': ''},
        },
        'total_score': eval_result['total'],
        'quality_grade': eval_result['grade'],
        'top_3_issues': eval_result['checks'].get('issues', [])[:3],
    }

    save_trace_score(skill_id, eval_result['checks'], eval_result['static_scores'], llm_result)
    return True


def run_batch(candidates: list) -> dict:
    """批量执行L2评估"""
    total = len(candidates)
    results = []
    passed = 0
    failed = 0
    errors = 0
    start_time = time.time()

    grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for i, cand in enumerate(candidates, 1):
        slug = cand['slug']
        print(f"[{i}/{total}] 评估: {slug} ({cand['category']})")

        # 查找SKILL.md
        skill_md_path = PACKAGED_DIR / slug / "SKILL.md"
        if not skill_md_path.exists():
            # 尝试从local_path查找
            if cand.get('local_path'):
                alt_path = Path(cand['local_path']) / "SKILL.md"
                if alt_path.exists():
                    skill_md_path = alt_path
                else:
                    print(f"  ✗ SKILL.md未找到")
                    errors += 1
                    results.append({'slug': slug, 'status': 'error', 'error': 'SKILL.md not found'})
                    continue
            else:
                print(f"  ✗ SKILL.md未找到")
                errors += 1
                results.append({'slug': slug, 'status': 'error', 'error': 'SKILL.md not found'})
                continue

        try:
            eval_result = evaluate_skill(slug, skill_md_path)

            if eval_result['is_pass']:
                passed += 1
            else:
                failed += 1

            grade_dist[eval_result['grade']] += 1

            # 保存到DB
            save_to_db(slug, eval_result)

            print(f"  T={eval_result['trust']:.0f} R={eval_result['reliability']:.0f} "
                  f"A={eval_result['adaptability']:.0f} C={eval_result['convention']:.0f} "
                  f"E={eval_result['effectiveness']:.0f} | Total={eval_result['total']} "
                  f"Grade={eval_result['grade']} {'✓' if eval_result['is_pass'] else '✗'}")

            results.append({
                'slug': slug,
                'category': cand['category'],
                'total': eval_result['total'],
                'grade': eval_result['grade'],
                'is_pass': eval_result['is_pass'],
                'scores': {
                    'T': eval_result['trust'],
                    'R': eval_result['reliability'],
                    'A': eval_result['adaptability'],
                    'C': eval_result['convention'],
                    'E': eval_result['effectiveness'],
                }
            })

        except Exception as e:
            errors += 1
            print(f"  ✗ 异常: {e}")
            results.append({'slug': slug, 'status': 'error', 'error': str(e)})

    total_time = time.time() - start_time

    avg_score = sum(r.get('total', 0) for r in results if r.get('total')) / max(len(results) - errors, 1)

    return {
        'batch_date': datetime.now().isoformat(),
        'total_evaluated': total,
        'passed': passed,
        'failed': failed,
        'errors': errors,
        'avg_score': round(avg_score, 1),
        'grade_distribution': grade_dist,
        'pass_threshold': TRACE_PASS_THRESHOLD,
        'duration_sec': round(total_time, 1),
        'results': results,
    }


def main():
    parser = argparse.ArgumentParser(description='批量L2评估脚本')
    parser.add_argument('--limit', type=int, default=100, help='最大评估数量')
    parser.add_argument('--category', help='按类别筛选')
    parser.add_argument('--only-unevaluated', action='store_true', help='仅评估未评估的skill')
    parser.add_argument('--dry-run', action='store_true', help='仅查看候选')
    parser.add_argument('-o', '--output', help='报告输出文件')

    args = parser.parse_args()

    candidates = query_candidates(
        limit=args.limit,
        category=args.category,
        only_unevaluated=args.only_unevaluated
    )

    print(f"{'='*70}")
    print(f"批量L2评估")
    print(f"{'='*70}")
    print(f"候选数: {len(candidates)}")

    if args.dry_run:
        print(f"\n候选列表 (dry-run):")
        for i, c in enumerate(candidates, 1):
            print(f"  {i:3d}. {c['slug']:40s} | {c['category']}")
        return

    if not candidates:
        print("无候选skill")
        return

    summary = run_batch(candidates)

    # 保存报告
    if not args.output:
        report_path = SKILL_REGISTRY_DIR / f"batch_l2_eval_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    else:
        report_path = Path(args.output)

    report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"\n{'='*70}")
    print(f"批量L2评估汇总")
    print(f"{'='*70}")
    print(f"  评估数: {summary['total_evaluated']}")
    print(f"  通过: {summary['passed']} (阈值≥{summary['pass_threshold']})")
    print(f"  未通过: {summary['failed']}")
    print(f"  错误: {summary['errors']}")
    print(f"  平均分: {summary['avg_score']}/50")
    print(f"  等级分布: A={summary['grade_distribution']['A']} "
          f"B={summary['grade_distribution']['B']} "
          f"C={summary['grade_distribution']['C']} "
          f"D={summary['grade_distribution']['D']}")
    print(f"  耗时: {summary['duration_sec']}秒")
    print(f"  报告: {report_path}")


if __name__ == '__main__':
    main()
