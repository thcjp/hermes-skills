"""
更新数据库：记录v2 skill的上传结果 + 重新扫描目录
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===


import sqlite3
from datetime import datetime
from pathlib import Path

# DB_PATH imported from config

def update_v2_uploads():
    """记录v2 skill的clawhub上传结果"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()

    v2_skills = [
        ('evolution-engine-v2', 'evolution-engine'),
        ('memory-distiller-v2', 'memory-distiller'),
        ('memory-orchestrator-v2', 'memory-orchestrator'),
        ('multi-agent-dev-v2', 'multi-agent-dev'),
    ]

    for new_slug, original_slug in v2_skills:
        # Find the skill
        c.execute("SELECT id FROM skills WHERE slug = ?", (new_slug,))
        row = c.fetchone()
        if not row:
            # Register the v2 skill
            c.execute("SELECT * FROM skills WHERE slug = ?", (original_slug,))
            orig = c.fetchone()
            if orig:
                c.execute("""
                    INSERT INTO skills (
                        slug, current_name, current_display_name, current_version,
                        category, source, source_slug, local_path,
                        created_at, updated_at, current_status,
                        is_differentiated, pricing_model, skill_type, notes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (new_slug, orig[2], orig[3], orig[4], orig[5],
                      orig[6], orig[7], orig[9],
                      now, now, 'optimized', 1, 'freemium', 'differentiated',
                      f'V2 slug to avoid conflict'))
                skill_id = c.lastrowid
            else:
                continue
        else:
            skill_id = row[0]

        # Record upload
        c.execute("""
            INSERT INTO platform_uploads (
                skill_id, version, platform, platform_slug, upload_date,
                upload_status, http_status, error_message, visibility
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (skill_id, '1.0.0', 'clawhub', new_slug, now, 'success', 200, None, 'public'))

        # Record operation
        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (skill_id, 'upload_clawhub', now, 'system',
              f'Uploaded {new_slug} v1.0.0 to clawhub', 'published'))

    # Also register skill-production-standards
    skill_path = r'str(DIFFERENTIATED_DIR)\Agents\skill-production-standards'
    c.execute("SELECT id FROM skills WHERE slug = 'skill-production-standards'")
    if not c.fetchone():
        c.execute("""
            INSERT INTO skills (
                slug, current_name, current_display_name, current_version,
                category, source, local_path,
                created_at, updated_at, current_status,
                is_differentiated, pricing_model, skill_type, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, ('skill-production-standards', 'skill-production-standards', 'Skill生产规范',
              '1.0.0', 'Agents', 'original_creation', skill_path,
              now, now, 'optimized', 1, 'free', 'original_creation',
              'Production standards skill for guiding all skill optimization'))

    conn.commit()
    conn.close()
    print("V2 uploads and skill-production-standards recorded in database")


def final_report():
    """生成最终报告"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    print("\n" + "=" * 70)
    print("  最终状态报告")
    print(f"  生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # Total
    c.execute("SELECT COUNT(*) FROM skills")
    print(f"\n总skill数: {c.fetchone()[0]}")

    # Differentiated
    c.execute("SELECT is_differentiated, COUNT(*) FROM skills GROUP BY is_differentiated")
    for row in c.fetchall():
        label = "已差异化" if row[0] else "原始下载"
        print(f"  {label}: {row[1]}")

    # Uploads by platform
    c.execute("""
        SELECT platform,
               SUM(CASE WHEN upload_status = 'success' THEN 1 ELSE 0 END) as success,
               SUM(CASE WHEN upload_status != 'success' THEN 1 ELSE 0 END) as fail
        FROM platform_uploads
        GROUP BY platform
    """)
    print(f"\n上传统计:")
    for row in c.fetchall():
        print(f"  {row['platform']}: 成功{row['success']} / 失败{row['fail']}")

    # Skills that are differentiated and on both platforms
    c.execute("""
        SELECT COUNT(DISTINCT s.id) as count
        FROM skills s
        WHERE s.is_differentiated = 1
        AND s.id IN (SELECT skill_id FROM platform_uploads WHERE platform = 'clawhub' AND upload_status = 'success')
    """)
    on_clawhub = c.fetchone()[0]

    c.execute("""
        SELECT COUNT(DISTINCT s.id) as count
        FROM skills s
        WHERE s.is_differentiated = 1
        AND s.id IN (SELECT skill_id FROM platform_uploads WHERE platform = 'skillhub' AND upload_status = 'success')
    """)
    on_skillhub = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM skills WHERE is_differentiated = 1")
    total_diff = c.fetchone()[0]

    print(f"\n差异化skill上传覆盖:")
    print(f"  总差异化skill: {total_diff}")
    print(f"  已上传clawhub: {on_clawhub}")
    print(f"  已上传skillhub: {on_skillhub}")

    conn.close()


if __name__ == '__main__':
    update_v2_uploads()
    final_report()
