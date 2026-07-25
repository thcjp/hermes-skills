#!/usr/bin/env python3
"""
初始化基线数据:
1. 导入 packaged-skills/skillhub 中的JueJin原创skill到数据库
2. 导入 opensource-skills/packaged 中的开源改造skill到数据库
3. 导入 enterprise-upload 中的企业版skill到数据库
4. 为所有skill计算并存储content_hash基线
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import PROJECT_ROOT
from project_config import DB_PATH
# === End Phase 1 ===
SKILLS_ROOT = PROJECT_ROOT

import sqlite3
import hashlib
import os
import sys
from pathlib import Path
from datetime import datetime
import re

# 导入统一解析层
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from skill_core.parser import parse_frontmatter as _parse_fm

import db as db_module

# DB_PATH imported from config
# SKILLS_ROOT = PROJECT_ROOT (imported from config)

def compute_file_hash(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def parse_frontmatter(content):
    """解析YAML frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    return result.get('fields', {})

def import_packaged_skills():
    """导入packaged-skills/skillhub中的JueJin原创skill"""
    packaged_dir = SKILLS_ROOT / "packaged-skills" / "skillhub"
    if not packaged_dir.exists():
        print(f"目录不存在: {packaged_dir}")
        return 0

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
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

        skill_id = db_module.insert_skill(
            slug=slug,
            name=metadata.get('name', slug),
            display_name=metadata.get('displayName', slug),
            version=version,
            category=metadata.get('category', 'original'),
            source='original_creation',
            local_path=str(skill_dir),
            current_status='published',
            is_differentiated=0,
            pricing_model='free',
            edition='free',
            parent_slug=None,
            skill_type='original_creation',
            workflow_state='completed',
            source_slug='',
            source_url='',
        )

        # 插入版本记录（含content_hash基线）
        db_module.add_version(skill_id, version, changelog='初始版本',
                              content_hash=content_hash, file_size=file_size,
                              line_count=line_count, changes_summary='初始导入')

        # 插入操作记录
        db_module.record_operation(skill_id, 'import', '基线初始化导入', after_state='published')

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
    conn.execute("PRAGMA foreign_keys = ON")
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

        skill_id = db_module.insert_skill(
            slug=slug,
            name=metadata.get('name', slug),
            display_name=metadata.get('displayName', slug),
            version=version,
            category='opensource',
            source='opensource_modified',
            local_path=str(skill_dir),
            current_status='packaged',
            is_differentiated=1,
            pricing_model='dual',
            edition='free',
            parent_slug=None,
            skill_type='opensource_modified',
            workflow_state='completed',
            source_slug=slug,
            source_url=source_repo,
        )

        db_module.add_version(skill_id, version, changelog='开源改造初始版本',
                              content_hash=content_hash, file_size=file_size,
                              line_count=line_count, changes_summary='初始导入')

        db_module.record_operation(skill_id, 'import', '基线初始化导入',
                                   operator='baseline_init', after_state='packaged')

        imported += 1
        print(f"  导入开源: {slug} v{version}")

    conn.commit()
    conn.close()
    return imported

def update_baseline_hashes():
    """为所有skill更新content_hash基线（如果versions表中hash为NULL）"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
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
            db_module.update_version_hash(row['id'], content_hash)
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
    conn.execute("PRAGMA foreign_keys = ON")
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
        existing = c.fetchone()
        if existing:
            # 已存在，更新edition为dual
            skill_id = existing[0]
            db_module.update_skill_fields(skill_id, edition='dual',
                                          pricing_model='dual',
                                          local_path=str(skill_dir))
            continue

        content = skill_md.read_text(encoding='utf-8')
        metadata = parse_frontmatter(content)
        content_hash = compute_file_hash(skill_md)
        line_count = len(content.split('\n'))
        file_size = skill_md.stat().st_size

        version = metadata.get('version', '1.0.0')

        skill_id = db_module.insert_skill(
            slug=slug,
            name=metadata.get('name', slug),
            display_name=metadata.get('displayName', slug),
            version=version,
            category='enterprise',
            source='original_creation',
            local_path=str(skill_dir),
            current_status='published',
            is_differentiated=0,
            pricing_model='dual',
            edition='dual',
            parent_slug=None,
            skill_type='original_creation',
            workflow_state='completed',
            source_slug='',
            source_url='',
        )

        db_module.add_version(skill_id, version, changelog='企业版初始版本',
                              content_hash=content_hash, file_size=file_size,
                              line_count=line_count, changes_summary='初始导入')

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
    conn.execute("PRAGMA foreign_keys = ON")
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
