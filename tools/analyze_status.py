"""
Skill项目状态分析报告
分析：已优化/未优化、已上传/未上传、收费/免费、去除标识检测
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
# === End Phase 1 ===


import sqlite3
import sys
from pathlib import Path
from datetime import datetime

# DB_PATH imported from config


def analyze_status():
    """分析skill状态"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    print("=" * 70)
    print("  Skill项目状态分析报告")
    print(f"  生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # 1. 总体统计
    c.execute("SELECT COUNT(*) FROM skills")
    total = c.fetchone()[0]
    print(f"\n📊 总体统计")
    print(f"  总skill数: {total}")

    c.execute("""
        SELECT
            is_differentiated,
            COUNT(*) as count
        FROM skills
        GROUP BY is_differentiated
    """)
    for row in c.fetchall():
        label = "已差异化" if row['is_differentiated'] else "原始下载"
        print(f"  {label}: {row['count']}")

    # 2. 按状态分类
    c.execute("""
        SELECT current_status, COUNT(*) as count
        FROM skills
        GROUP BY current_status
        ORDER BY count DESC
    """)
    print(f"\n📋 按状态分类")
    for row in c.fetchall():
        print(f"  {row['current_status']}: {row['count']}")

    # 3. 按分类统计
    c.execute("""
        SELECT category,
               COUNT(*) as total,
               SUM(CASE WHEN is_differentiated = 1 THEN 1 ELSE 0 END) as differentiated,
               SUM(CASE WHEN is_differentiated = 0 THEN 1 ELSE 0 END) as not_differentiated
        FROM skills
        GROUP BY category
        ORDER BY total DESC
    """)
    print(f"\n📁 按分类统计")
    print(f"  {'分类':<15} {'总数':>6} {'已优化':>6} {'未优化':>6} {'优化率':>8}")
    print(f"  {'-'*15} {'-'*6} {'-'*6} {'-'*6} {'-'*8}")
    for row in c.fetchall():
        rate = (row['differentiated'] / row['total'] * 100) if row['total'] > 0 else 0
        print(f"  {row['category']:<15} {row['total']:>6} {row['differentiated']:>6} {row['not_differentiated']:>6} {rate:>7.1f}%")

    # 4. 上传统计
    c.execute("""
        SELECT platform,
               upload_status,
               COUNT(*) as count
        FROM platform_uploads
        GROUP BY platform, upload_status
        ORDER BY platform, upload_status
    """)
    print(f"\n📤 上传统计")
    print(f"  {'平台':<10} {'状态':<10} {'数量':>6}")
    print(f"  {'-'*10} {'-'*10} {'-'*6}")
    for row in c.fetchall():
        print(f"  {row['platform']:<10} {row['upload_status']:<10} {row['count']:>6}")

    # 5. 需要优化的skill（未差异化）
    c.execute("""
        SELECT category, COUNT(*) as count
        FROM skills
        WHERE is_differentiated = 0
        GROUP BY category
        ORDER BY count DESC
    """)
    print(f"\n⚠️  需要优化的skill（未差异化）")
    total_to_optimize = 0
    for row in c.fetchall():
        print(f"  {row['category']:<15} {row['count']:>6}")
        total_to_optimize += row['count']
    print(f"  {'总计':<15} {total_to_optimize:>6}")

    # 6. 已优化但未上传到某平台的skill
    c.execute("""
        SELECT s.slug, s.category, s.current_display_name
        FROM skills s
        WHERE s.is_differentiated = 1
        AND s.id NOT IN (
            SELECT DISTINCT skill_id
            FROM platform_uploads
            WHERE platform = 'clawhub' AND upload_status = 'success'
        )
        ORDER BY s.category, s.slug
    """)
    not_on_clawhub = c.fetchall()

    c.execute("""
        SELECT s.slug, s.category, s.current_display_name
        FROM skills s
        WHERE s.is_differentiated = 1
        AND s.id NOT IN (
            SELECT DISTINCT skill_id
            FROM platform_uploads
            WHERE platform = 'skillhub' AND upload_status = 'success'
        )
        ORDER BY s.category, s.slug
    """)
    not_on_skillhub = c.fetchall()

    print(f"\n📤 已优化但未上传")
    print(f"  未上传到clawhub: {len(not_on_clawhub)}个")
    for row in not_on_clawhub[:10]:
        print(f"    - {row['slug']} ({row['current_display_name']})")
    if len(not_on_clawhub) > 10:
        print(f"    ... 还有{len(not_on_clawhub) - 10}个")

    print(f"\n  未上传到skillhub: {len(not_on_skillhub)}个")
    for row in not_on_skillhub[:10]:
        print(f"    - {row['slug']} ({row['current_display_name']})")
    if len(not_on_skillhub) > 10:
        print(f"    ... 还有{len(not_on_skillhub) - 10}个")

    # 7. 收费策略统计
    c.execute("""
        SELECT pricing_model, COUNT(*) as count
        FROM skills
        GROUP BY pricing_model
        ORDER BY count DESC
    """)
    print(f"\n💰 收费策略统计")
    for row in c.fetchall():
        print(f"  {row['pricing_model']}: {row['count']}")

    # 8. 建议的下一步工作
    print(f"\n🎯 建议的下一步工作")
    print(f"  1. 优化 {total_to_optimize} 个未差异化的skill")
    print(f"  2. 上传 {len(not_on_clawhub)} 个已优化skill到clawhub")
    print(f"  3. 上传 {len(not_on_skillhub)} 个已优化skill到skillhub")
    print(f"  4. 为已上传的skill制定收费策略")

    conn.close()


def list_skills_to_optimize(limit=None):
    """列出需要优化的skill"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    query = """
        SELECT slug, category, current_display_name, source_slug, source_url
        FROM skills
        WHERE is_differentiated = 0
        ORDER BY category, slug
    """
    if limit:
        query += f" LIMIT {limit}"

    c.execute(query)
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results


def list_skills_to_upload(platform='clawhub'):
    """列出需要上传到指定平台的skill"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("""
        SELECT s.slug, s.category, s.current_display_name, s.local_path
        FROM skills s
        WHERE s.is_differentiated = 1
        AND s.id NOT IN (
            SELECT DISTINCT skill_id
            FROM platform_uploads
            WHERE platform = ? AND upload_status = 'success'
        )
        ORDER BY s.category, s.slug
    """, (platform,))

    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results


if __name__ == '__main__':
    analyze_status()
