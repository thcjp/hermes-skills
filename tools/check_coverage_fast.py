#!/usr/bin/env python3
"""快速检查本地skill覆盖 - 先构建slug索引再比对"""
import json
import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pathlib import Path
from config import PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, DIFFERENTIATED_DIR

# 1. Build local slug index by scanning all directories once
def build_slug_index():
    """扫描所有目录，构建 slug -> path 的索引"""
    index = {}
    
    for base_dir in [PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, DIFFERENTIATED_DIR]:
        if not base_dir.exists():
            continue
        
        # Handle both flat and nested structures
        for item in base_dir.iterdir():
            if not item.is_dir():
                continue
            
            # Check if this is a skill directory (has SKILL.md directly)
            skill_md = item / "SKILL.md"
            if skill_md.exists():
                try:
                    content = skill_md.read_text(encoding='utf-8')
                    if content.startswith('\ufeff'):
                        content = content[1:]
                    if content.startswith('---'):
                        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                        if len(parts) >= 3:
                            slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', parts[1], re.MULTILINE)
                            if slug_match:
                                slug = slug_match.group(1).strip()
                                if slug not in index:  # First found wins
                                    index[slug] = str(skill_md)
                except Exception:
                    pass
            
            # For nested structure (differentiated-skills/{category}/{slug}/)
            if base_dir == DIFFERENTIATED_DIR:
                if item.is_dir():
                    for sub_item in item.iterdir():
                        if not sub_item.is_dir():
                            continue
                        skill_md = sub_item / "SKILL.md"
                        if skill_md.exists():
                            try:
                                content = skill_md.read_text(encoding='utf-8')
                                if content.startswith('\ufeff'):
                                    content = content[1:]
                                if content.startswith('---'):
                                    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                                    if len(parts) >= 3:
                                        slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', parts[1], re.MULTILINE)
                                        if slug_match:
                                            slug = slug_match.group(1).strip()
                                            if slug not in index:
                                                index[slug] = str(skill_md)
                            except Exception:
                                pass
    
    return index

print("Building local slug index...")
local_index = build_slug_index()
print(f"Local skills found: {len(local_index)}")

# 2. Load SkillHub slugs
all_slugs = json.loads(Path('../data/reports/all_skillhub_slugs.json').read_text(encoding='utf-8'))
org_only_slugs = json.loads(Path('../data/reports/org_only_slugs.json').read_text(encoding='utf-8'))

print(f"SkillHub total: {len(all_slugs)}")
print(f"SkillHub org_only: {len(org_only_slugs)}")

# 3. Check overlap
local_slugs = list(local_index.keys())
local_set = set(local_slugs)

skillhub_local = [s for s in all_slugs if s in local_set]
skillhub_missing = [s for s in all_slugs if s not in local_set]

print(f"\n=== Coverage ===")
print(f"SkillHub skills with local SKILL.md: {len(skillhub_local)}")
print(f"SkillHub skills without local SKILL.md: {len(skillhub_missing)}")

org_only_local = [s for s in org_only_slugs if s in local_set]
org_only_missing = [s for s in org_only_slugs if s not in local_set]
print(f"\nOrg_only with local: {len(org_only_local)} / {len(org_only_slugs)}")
print(f"Org_only without local: {len(org_only_missing)}")
if org_only_missing:
    print(f"  Missing org_only (first 30): {org_only_missing[:30]}")

# 4. Rejected skills check
rejected_slugs = [
    'ai-writing-style-cloner', 'api-design-architect', 'auth-security-architect',
    'azure-cloud-automator', 'brand-identity-creator', 'c-suite-advisor',
    'canvas-art-designer', 'clickhouse-olap-expert', 'cloudflare-edge-developer',
    'code-review-sentinel', 'competitive-ad-spy', 'compliance-manager',
    'content-cms-architect', 'content-refiner', 'copywriting-master',
    'csv-insight-miner', 'drama-hit-producer', 'ebook-factory',
    'ecommerce-pricing-strategist', 'geo-rank-architect', 'hook-retention-master',
    'intel-sentinel', 'novel-autopilot', 'poetry-craftsman', 'requirement-explorer-pro',
    'sales-copy-writer', 'seo-doctor', 'seo-rank-monopolizer', 'stealth-browser-assistant',
    'title-hook-factory', 'topic-hunter', 'viral-decoder', 'viral-prophet',
    'ai-artist-workstation-pro', 'lead-research-hunter', 'duckdb-analytics-engine',
    'docx-document-master', 'debug-doctor'
]
rejected_local = [s for s in rejected_slugs if s in local_set]
rejected_missing = [s for s in rejected_slugs if s not in local_set]
print(f"\nRejected with local: {len(rejected_local)} / {len(rejected_slugs)}")
if rejected_missing:
    print(f"  Missing rejected: {rejected_missing}")

# 5. Save plan
plan = {
    'total_skillhub': len(all_slugs),
    'total_local': len(local_slugs),
    'skillhub_with_local': len(skillhub_local),
    'skillhub_without_local': len(skillhub_missing),
    'org_only_total': len(org_only_slugs),
    'org_only_with_local': len(org_only_local),
    'org_only_without_local': len(org_only_missing),
    'rejected_total': len(rejected_slugs),
    'rejected_with_local': len(rejected_local),
    'rejected_without_local': len(rejected_missing),
    'reupload_all_slugs': skillhub_local,
    'org_only_reupload_slugs': org_only_local,
    'rejected_reupload_slugs': rejected_local,
    'missing_slugs': skillhub_missing,
    'local_index': local_index,
}

plan_file = Path('../data/reports/reupload_plan.json')
with open(plan_file, 'w', encoding='utf-8') as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
print(f"\nPlan saved to: {plan_file}")
print(f"\n=== Action Plan ===")
print(f"1. Re-upload {len(skillhub_local)} skills (fixes metadata + visibility)")
print(f"   - Includes {len(org_only_local)} org_only skills → will become public")
print(f"   - Includes {len(rejected_local)} rejected skills → re-enter review")
print(f"2. Cannot fix {len(skillhub_missing)} skills (no local SKILL.md)")
print(f"   - Includes {len(org_only_missing)} org_only skills")
print(f"   - Includes {len(rejected_missing)} rejected skills")
