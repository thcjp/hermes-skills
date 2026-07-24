"""
扫描所有现有skill目录，导入到SQLite数据库
- d:\skills\clawhub-skills\downloaded\ (原始下载)
- str(DIFFERENTIATED_DIR)\ (已差异化)
- d:\skills\opensource-skills\packaged\ (开源改造)
- d:\skills\packaged-skills\skillhub\ (skillhub打包)
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===


import sys
import os
from pathlib import Path
from datetime import datetime

# Add parent dir to path
sys.path.insert(0, str(Path(__file__).parent))
from db import (init_database, parse_skill_md, register_skill, record_upload,
                record_operation, compute_file_hash)

SCAN_DIRS = [
    {
        'path': r'd:\skills\clawhub-skills\downloaded',
        'source': 'clawhub_download',
        'skill_type': 'original_download',
        'is_differentiated': 0
    },
    {
        'path': r'str(DIFFERENTIATED_DIR)',
        'source': 'clawhub_download',
        'skill_type': 'differentiated',
        'is_differentiated': 1
    },
    {
        'path': r'd:\skills\opensource-skills\packaged',
        'source': 'opensource_modified',
        'skill_type': 'opensource_modified',
        'is_differentiated': 1
    },
    {
        'path': r'd:\skills\packaged-skills\skillhub',
        'source': 'original_creation',
        'skill_type': 'original_creation',
        'is_differentiated': 1
    }
]

# Original slug mapping (differentiated -> original)
SLUG_MAPPING = {
    # differentiated-skills/Agents -> clawhub-skills/downloaded/Agents
    'ad-insight-hub': ('admapix', 'clawhub'),
    'agent-copilot-pro': ('ai-agent-helper', 'clawhub'),
    'persistent-memory-engine': ('memory', 'clawhub'),
    'memory-distiller': ('memory-compress', 'clawhub'),
    'memory-distiller-v2': ('memory-compress', 'clawhub'),
    'memory-radar': ('memory-scan', 'clawhub'),
    'memo-quickstart': ('simple-memory-skill', 'clawhub'),
    'memory-orchestrator': ('smart-memory-manager', 'clawhub'),
    'memory-orchestrator-v2': ('smart-memory-manager', 'clawhub'),
    'token-guard-pro': ('token-saver-skill', 'clawhub'),
    'longmemo-elite': ('elite-longterm-memory', 'clawhub'),
    'localmemo-pro': ('elite-longterm-memory-local', 'clawhub'),
    'decision-architect': ('neosoul-decision-agent', 'clawhub'),
    'neurocache-pro': ('neural-memory-enhanced', 'clawhub'),
    'knowledge-ontology': ('ontology', 'clawhub'),
    'productivity-boost': ('productivity', 'clawhub'),
    'redis-cache-master': ('redis-store', 'clawhub'),
    'evolution-engine': ('self-improving', 'clawhub'),
    'evolution-engine-v2': ('self-improving', 'clawhub'),
    'self-evolving-ai': ('self-improving-agent', 'clawhub'),
    'multi-agent-dev': ('subagent-driven-development', 'clawhub'),
    'multi-agent-dev-v2': ('subagent-driven-development', 'clawhub'),
    'tool-orchestrator': ('totalreclaw', 'clawhub'),
    'aws-graph-agent': ('aws-agentcore-langgraph', 'clawhub'),
    'aws-cloud-architect': ('aws-infra', 'clawhub'),
    'azure-cloud-architect': ('azure-infra', 'clawhub'),
    'netdisk-sync-pro': ('baidu-netdisk-skills', 'clawhub'),
    'llm-assistant-hub': ('claude', 'clawhub'),
    # differentiated-skills/Automation -> clawhub-skills/downloaded/Automation
    'biz-auto-hub': ('afrexai-business-automation', 'clawhub'),
    'excel-maestro': ('automate-excel', 'clawhub'),
    'flow-architect': ('automation-workflow-builder', 'clawhub'),
    'workflow-symphony': ('automation-workflows', 'clawhub'),
    'workflow-lite': ('automation-workflows-0-1-0', 'clawhub'),
    'update-guardian': ('auto-updater', 'clawhub'),
    'autopilot-flow': ('auto-workflow', 'clawhub'),
    'batch-processor-pro': ('batch', 'clawhub'),
    'cdp-browser-master': ('browser-automation-cdp', 'clawhub'),
    'security-radar': ('clawsec-feed', 'clawhub'),
    'cloud-ops-orchestrator': ('cloud-infra-automation', 'clawhub'),
    'system-controller': ('control', 'clawhub'),
    'cron-scheduler-pro': ('cron', 'clawhub'),
    'cron-assist': ('cron-helper', 'clawhub'),
    'cron-master-pro': ('cron-mastery', 'clawhub'),
    'cron-guard': ('cron-worker-guardrails', 'clawhub'),
    'desktop-autopilot': ('desktop-control', 'clawhub'),
    'cad-insight-pro': ('drawing-analyzer', 'clawhub'),
    'pcb-design-assistant': ('jlc-eda-drawing', 'clawhub'),
    'linear-cli-pro': ('kyaukyuai-linear-cli', 'clawhub'),
    'linear-workflow-bot': ('linear-autopilot', 'clawhub'),
    'macro-pulse': ('macro-monitor', 'clawhub'),
    'flow-editor-pro': ('node-red-manager', 'clawhub'),
    'vault-master-pro': ('obsidian', 'clawhub'),
    'vault-sync-engine': ('obsidian-1-0-0', 'clawhub'),
    'notes-cli-toolkit': ('obsidian-notesmd-cli', 'clawhub'),
    'office-productivity-hub': ('office-automation-pro', 'clawhub'),
}


def scan_directory(scan_config):
    """扫描目录下所有skill"""
    base_path = scan_config['path']
    source = scan_config['source']
    skill_type = scan_config['skill_type']
    is_differentiated = scan_config['is_differentiated']

    if not Path(base_path).exists():
        print(f"  Path not found: {base_path}")
        return []

    skills = []
    for category_dir in Path(base_path).iterdir():
        if not category_dir.is_dir():
            continue
        category = category_dir.name

        for skill_dir in category_dir.iterdir():
            if not skill_dir.is_dir():
                continue

            skill_md = skill_dir / 'SKILL.md'
            if not skill_md.exists():
                continue

            metadata, body = parse_skill_md(skill_md)
            if not metadata or 'slug' not in metadata:
                print(f"  SKIP (no frontmatter): {skill_dir}")
                continue

            slug = metadata.get('slug', skill_dir.name)
            name = metadata.get('name', slug)
            display_name = metadata.get('displayName', slug)
            version = metadata.get('version', '1.0.0')
            license_str = metadata.get('license', 'MIT')

            # Get source mapping
            original_slug = None
            source_platform = None
            if slug in SLUG_MAPPING:
                original_slug, source_platform = SLUG_MAPPING[slug]
            elif source == 'clawhub_download' and skill_type == 'original_download':
                original_slug = slug
                source_platform = 'clawhub'
            elif source == 'original_creation':
                original_slug = None
                source_platform = None

            skill_info = {
                'slug': slug,
                'name': name,
                'display_name': display_name,
                'version': version,
                'category': category,
                'source': source,
                'source_slug': original_slug,
                'source_url': f"https://clawhub.ai/{original_slug}" if original_slug else None,
                'source_author': None,
                'source_license': license_str,
                'local_path': str(skill_dir),
                'skill_type': skill_type,
                'is_differentiated': is_differentiated,
                'source_platform': source_platform,
                'file_hash': compute_file_hash(skill_md),
                'file_size': skill_md.stat().st_size,
            }
            skills.append(skill_info)

    return skills


def import_skills_to_db(skills):
    """导入skill列表到数据库"""
    from db import register_skill, record_operation

    count = 0
    for skill in skills:
        pricing_model = 'free'  # default
        if skill['skill_type'] == 'original_creation':
            pricing_model = 'freemium'  # 原创skill默认免费增值
        elif skill['skill_type'] == 'differentiated':
            pricing_model = 'freemium'
        elif skill['skill_type'] == 'original_download':
            pricing_model = 'free'

        skill_id = register_skill(
            slug=skill['slug'],
            name=skill['name'],
            display_name=skill['display_name'],
            version=skill['version'],
            category=skill['category'],
            source=skill['source'],
            local_path=skill['local_path'],
            source_slug=skill['source_slug'],
            source_url=skill['source_url'],
            source_author=skill['source_author'],
            source_license=skill['source_license'],
            skill_type=skill['skill_type'],
            pricing_model=pricing_model,
            is_differentiated=skill['is_differentiated'],
            notes=f"File hash: {skill['file_hash'][:16]}, size: {skill['file_size']}b"
        )

        # Update status
        if skill['is_differentiated']:
            status = 'optimized'
        else:
            status = 'registered'

        import sqlite3
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE skills SET current_status = ? WHERE id = ?", (status, skill_id))
        conn.commit()
        conn.close()

        count += 1

    return count


def import_upload_logs():
    """导入上传日志"""
    import sqlite3
    import csv

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Import clawhub upload log (original)
    clawhub_log = r'd:\skills\clawhub-skills\upload-log.csv'
    if Path(clawhub_log).exists():
        with open(clawhub_log, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                slug = (row.get('slug') or '').strip()
                status = (row.get('status') or '').strip()
                if not slug or not status:
                    continue

                # Find original skill (original_download type)
                c.execute("SELECT id FROM skills WHERE slug = ? AND source = 'clawhub_download'", (slug,))
                result = c.fetchone()
                if not result:
                    continue

                skill_id = result[0]
                platform_slug = f"@thcjp/{slug}" if status == 'success' else slug
                visibility = 'hidden' if status == 'success' else None

                record_upload(
                    skill_id=skill_id,
                    version='1.0.0',
                    platform='clawhub',
                    platform_slug=platform_slug,
                    upload_status='success' if status == 'success' else 'fail',
                    http_status=200 if status == 'success' else 1,
                    error_message=row.get('error', ''),
                    visibility=visibility
                )

    # Import differentiated skills upload log
    diff_log = r'str(DIFFERENTIATED_DIR)\upload-log.csv'
    if Path(diff_log).exists():
        with open(diff_log, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                slug = (row.get('slug') or '').strip()
                platform = (row.get('platform') or '').strip()
                status = (row.get('status') or '').strip()
                if not slug or not platform:
                    continue

                c.execute("SELECT id FROM skills WHERE slug = ? AND is_differentiated = 1", (slug,))
                result = c.fetchone()
                if not result:
                    continue

                skill_id = result[0]
                http_code = 200 if status == 'success' else (409 if status == 'conflict' else 500)

                record_upload(
                    skill_id=skill_id,
                    version='1.0.0',
                    platform=platform,
                    platform_slug=slug,
                    upload_status=status,
                    http_status=http_code,
                    error_message=row.get('error', '')
                )

    conn.commit()
    conn.close()


def print_stats():
    """打印统计信息"""
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    print("\n" + "=" * 60)
    print("  Skill Registry Database Statistics")
    print("=" * 60)

    # Total skills
    c.execute("SELECT COUNT(*) FROM skills")
    print(f"Total skills: {c.fetchone()[0]}")

    # By source
    c.execute("SELECT source, COUNT(*) FROM skills GROUP BY source")
    print("\nBy source:")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    # By category
    c.execute("SELECT category, COUNT(*) FROM skills GROUP BY category ORDER BY COUNT(*) DESC")
    print("\nBy category:")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    # By status
    c.execute("SELECT current_status, COUNT(*) FROM skills GROUP BY current_status")
    print("\nBy status:")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    # By skill_type
    c.execute("SELECT skill_type, COUNT(*) FROM skills GROUP BY skill_type")
    print("\nBy skill_type:")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    # Uploads
    c.execute("""
        SELECT platform, upload_status, COUNT(*) FROM platform_uploads
        GROUP BY platform, upload_status ORDER BY platform, upload_status
    """)
    print("\nUpload status:")
    for row in c.fetchall():
        print(f"  {row[0]} - {row[1]}: {row[2]}")

    # Differentiated vs not
    c.execute("SELECT is_differentiated, COUNT(*) FROM skills GROUP BY is_differentiated")
    print("\nDifferentiation status:")
    for row in c.fetchall():
        label = "Differentiated" if row[0] else "Original"
        print(f"  {label}: {row[1]}")

    conn.close()


def main():
    print("Initializing database...")
    init_database()

    all_skills = []
    for scan_config in SCAN_DIRS:
        print(f"\nScanning: {scan_config['path']}")
        skills = scan_directory(scan_config)
        print(f"  Found {len(skills)} skills")
        all_skills.extend(skills)

    print(f"\nTotal skills found: {len(all_skills)}")
    print("\nImporting to database...")
    count = import_skills_to_db(all_skills)
    print(f"Imported {count} skills")

    print("\nImporting upload logs...")
    import_upload_logs()
    print("Upload logs imported")

    print_stats()


if __name__ == '__main__':
    main()
