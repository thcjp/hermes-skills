#!/usr/bin/env python3
"""
初始化基线数据:
1. 导入 packaged-skills/skillhub 中的JueJin原创skill到数据库
2. 导入 opensource-skills/packaged 中的开源改造skill到数据库
3. 导入 enterprise-upload 中的企业版skill到数据库
4. 为所有skill计算并存储content_hash基线
"""
import sqlite3
import hashlib
import os
from pathlib import Path
from datetime import datetime
import re

DB_PATH = r"d:\skills\skill-registry.db"
SKILLS_ROOT = Path(r"d:\skills")

def compute_file_hash(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def parse_frontmatter(content):
    """解析YAML frontmatter"""
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith('---'):
        return {}
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}
    fm_text = parts[1].strip()
    metadata = {}
    for line in fm_text.split('\n'):
        if ':' in line and not line.startswith('  '):
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val and val != '|-' and val != '|':
                metadata[key] = val
    return metadata

def import_packaged_skills():
    """导入packaged-skills/skillhub中的JueJin原创skill"""
    packaged_dir = SKILLS_ROOT / "packaged-skills" / "skillhub"
    if not packaged_dir.exists():
        print(f"目录不存在: {packaged_dir}")
        return 0

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    imported = 0
    for skill_dir in packaged_dir.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        slug = skill_dir.name
        # 检查是否已存在
        c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
        if c.fetchone():
            continue

        content = skill_md.read_text(encoding='utf-8')
        metadata = parse_frontmatter(content)
        content_hash = compute_file_hash(skill_md)

        # 计算行数和文件大小
        line_count = len(content.split('\n'))
        file_size = skill_md.stat().st_size

        now = datetime.now().isoformat()
        version = metadata.get('version', '1.0.0')

        c.execute("""
            INSERT INTO skills (slug, current_name, current_version, category, source, source_slug, source_url,
                               local_path, current_status, is_differentiated, pricing_model, edition,
                               parent_slug, current_display_name, skill_type, workflow_state,
                               created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            slug,
            metadata.get('name', slug),
            version,
            metadata.get('category', 'original'),
            'original_creation',
            '',  # no source_slug for original
            '',  # no source_url
            str(skill_dir),
            'published',
            0,
            'free',
            'free',
            None,
            metadata.get('displayName', slug),
            'original_creation',
            'completed',
            now, now
        ))

        skill_id = c.lastrowid

        # 插入版本记录（含content_hash基线）
        c.execute("""
            INSERT INTO versions (skill_id, version, created_at, changelog, content_hash,
                                 file_size, line_count, changes_summary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (skill_id, version, now, '初始版本', content_hash, file_size, line_count, '初始导入'))

        # 插入操作记录
        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (skill_id, 'import', now, 'baseline_init', '基线初始化导入', 'published'))

        imported += 1
        print(f"  导入: {slug} v{version} (hash: {content_hash[:16]}...)")

    conn.commit()
    conn.close()
    return imported

def import_opensource_skills():
    """导入opensource-skills/packaged中的开源改造skill"""
    oss_dir = SKILLS_ROOT / "opensource-skills" / "packaged"
    if not oss_dir.exists():
        print(f"目录不存在: {oss_dir}")
        return 0

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    imported = 0
    for skill_dir in oss_dir.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        slug = skill_dir.name
        c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
        if c.fetchone():
            continue

        content = skill_md.read_text(encoding='utf-8')
        metadata = parse_frontmatter(content)
        content_hash = compute_file_hash(skill_md)
        line_count = len(content.split('\n'))
        file_size = skill_md.stat().st_size

        now = datetime.now().isoformat()
        version = metadata.get('version', '1.0.0')

        # 从catalog.md中查找来源信息
        source_repo = metadata.get('homepage', '')

        c.execute("""
            INSERT INTO skills (slug, current_name, current_version, category, source, source_slug, source_url,
                               local_path, current_status, is_differentiated, pricing_model, edition,
                               parent_slug, current_display_name, skill_type, workflow_state,
                               created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            slug,
            metadata.get('name', slug),
            version,
            'opensource',
            'opensource_modified',
            slug,  # source_slug = self (原始仓库)
            source_repo,
            str(skill_dir),
            'packaged',
            1,
            'dual',
            'free',
            None,
            metadata.get('displayName', slug),
            'opensource_modified',
            'completed',
            now, now
        ))

        skill_id = c.lastrowid
        c.execute("""
            INSERT INTO versions (skill_id, version, created_at, changelog, content_hash,
                                 file_size, line_count, changes_summary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (skill_id, version, now, '开源改造初始版本', content_hash, file_size, line_count, '初始导入'))

        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (skill_id, 'import', now, 'baseline_init', '基线初始化导入', 'packaged'))

        imported += 1
        print(f"  导入开源: {slug} v{version}")

    conn.commit()
    conn.close()
    return imported

def update_baseline_hashes():
    """为所有skill更新content_hash基线（如果versions表中hash为NULL）"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # 找出所有hash为NULL的版本记录
    c.execute("""
        SELECT v.id, v.skill_id, s.slug, s.local_path, s.current_version
        FROM versions v
        JOIN skills s ON v.skill_id = s.id
        WHERE v.content_hash IS NULL
    """)

    rows = c.fetchall()
    print(f"\n需要更新hash的版本记录: {len(rows)}")

    updated = 0
    for row in rows:
        local_path = row['local_path']
        if not local_path:
            continue

        skill_md = Path(local_path) / "SKILL.md"
        if not skill_md.exists():
            skill_md = Path(local_path)
            if not skill_md.exists() or skill_md.suffix != '.md':
                continue

        try:
            content_hash = compute_file_hash(skill_md)
            c.execute("UPDATE versions SET content_hash = ? WHERE id = ?",
                     (content_hash, row['id']))
            updated += 1
        except Exception as e:
            print(f"  跳过 {row['slug']}: {e}")

    conn.commit()
    print(f"已更新 {updated} 条hash记录")
    conn.close()
    return updated

def import_enterprise_skills():
    """导入enterprise-upload中的企业版skill"""
    ent_dir = SKILLS_ROOT / "enterprise-upload"
    if not ent_dir.exists():
        return 0

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    imported = 0
    for skill_dir in ent_dir.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        slug = skill_dir.name
        # 检查是否已存在（企业版slug可能与packaged版相同）
        c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
        if c.fetchone():
            # 已存在，更新edition为dual
            c.execute("""
                UPDATE skills SET edition = 'dual', pricing_model = 'dual',
                       local_path = ?, updated_at = ?
                WHERE slug = ?
            """, (str(skill_dir), datetime.now().isoformat(), slug))
            continue

        content = skill_md.read_text(encoding='utf-8')
        metadata = parse_frontmatter(content)
        content_hash = compute_file_hash(skill_md)
        line_count = len(content.split('\n'))
        file_size = skill_md.stat().st_size

        now = datetime.now().isoformat()
        version = metadata.get('version', '1.0.0')

        c.execute("""
            INSERT INTO skills (slug, current_name, current_version, category, source, source_slug, source_url,
                               local_path, current_status, is_differentiated, pricing_model, edition,
                               parent_slug, current_display_name, skill_type, workflow_state,
                               created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            slug,
            metadata.get('name', slug),
            version,
            'enterprise',
            'original_creation',
            '', '', str(skill_dir),
            'published', 0, 'dual', 'dual',
            None,
            metadata.get('displayName', slug),
            'original_creation',
            'completed',
            now, now
        ))

        skill_id = c.lastrowid
        c.execute("""
            INSERT INTO versions (skill_id, version, created_at, changelog, content_hash,
                                 file_size, line_count, changes_summary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (skill_id, version, now, '企业版初始版本', content_hash, file_size, line_count, '初始导入'))

        imported += 1
        print(f"  导入企业版: {slug} v{version}")

    conn.commit()
    conn.close()
    return imported

def main():
    print("=" * 60)
    print("Skill Registry 基线数据初始化")
    print("=" * 60)

    print("\n1. 导入JueJin原创skill (packaged-skills/skillhub)...")
    n1 = import_packaged_skills()
    print(f"   导入 {n1} 个原创skill")

    print("\n2. 导入开源改造skill (opensource-skills/packaged)...")
    n2 = import_opensource_skills()
    print(f"   导入 {n2} 个开源改造skill")

    print("\n3. 导入/更新企业版skill (enterprise-upload)...")
    n3 = import_enterprise_skills()
    print(f"   导入 {n3} 个企业版skill")

    print("\n4. 更新content_hash基线...")
    n4 = update_baseline_hashes()

    # 统计
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM skills")
    total = c.fetchone()[0]
    c.execute("SELECT source, COUNT(*) FROM skills GROUP BY source ORDER BY COUNT(*) DESC")
    sources = c.fetchall()
    c.execute("SELECT COUNT(*) FROM versions WHERE content_hash IS NOT NULL")
    hashed = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM versions WHERE content_hash IS NULL")
    no_hash = c.fetchone()[0]
    conn.close()

    print(f"\n{'=' * 60}")
    print(f"初始化完成!")
    print(f"  总skill数: {total}")
    print(f"  有hash的版本记录: {hashed}")
    print(f"  无hash的版本记录: {no_hash}")
    print(f"\n来源分布:")
    for source, count in sources:
        print(f"  {source}: {count}")

if __name__ == '__main__':
    main()
