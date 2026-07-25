#!/usr/bin/env python3
"""检查本地skill与SkillHub skill的重叠，确定可重新上传的范围"""
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pathlib import Path
from enterprise_uploader import find_skill_md, load_cookies, ORG_ID, API_BASE
from urllib.request import urlopen, Request

# 1. Load SkillHub slugs
all_slugs = json.loads(Path('../data/reports/all_skillhub_slugs.json').read_text(encoding='utf-8'))
org_only_slugs = json.loads(Path('../data/reports/org_only_slugs.json').read_text(encoding='utf-8'))

print(f"SkillHub total: {len(all_slugs)}")
print(f"SkillHub org_only: {len(org_only_slugs)}")

# 2. Check which slugs have local SKILL.md files
local_slugs = []
missing_slugs = []

for i, slug in enumerate(all_slugs):
    md = find_skill_md(slug)
    if md:
        local_slugs.append(slug)
    else:
        missing_slugs.append(slug)
    
    if (i + 1) % 500 == 0:
        print(f"  Checked {i+1}/{len(all_slugs)}...")

print(f"\n=== Local SKILL.md Coverage ===")
print(f"Skills with local SKILL.md: {len(local_slugs)}")
print(f"Skills without local SKILL.md: {len(missing_slugs)}")

# 3. Check org_only overlap
org_only_local = [s for s in org_only_slugs if s in local_slugs]
org_only_missing = [s for s in org_only_slugs if s not in local_slugs]
print(f"\n=== Org_only Coverage ===")
print(f"Org_only with local SKILL.md: {len(org_only_local)}")
print(f"Org_only without local SKILL.md: {len(org_only_missing)}")
if org_only_missing:
    print(f"Missing org_only slugs: {org_only_missing[:20]}")

# 4. Check rejected skills coverage
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
rejected_local = [s for s in rejected_slugs if s in local_slugs]
rejected_missing = [s for s in rejected_slugs if s not in local_slugs]
print(f"\n=== Rejected Skills Coverage ===")
print(f"Rejected with local SKILL.md: {len(rejected_local)}/{len(rejected_slugs)}")
if rejected_missing:
    print(f"Missing rejected slugs: {rejected_missing}")

# 5. Save the re-upload plan
plan = {
    'total_skillhub': len(all_slugs),
    'total_local': len(local_slugs),
    'total_missing': len(missing_slugs),
    'org_only_total': len(org_only_slugs),
    'org_only_local': len(org_only_local),
    'org_only_missing': len(org_only_missing),
    'rejected_total': len(rejected_slugs),
    'rejected_local': len(rejected_local),
    'rejected_missing': len(rejected_missing),
    'reupload_slugs': local_slugs,
    'org_only_reupload_slugs': org_only_local,
    'missing_slugs': missing_slugs,
}

plan_file = Path('../data/reports/reupload_plan.json')
with open(plan_file, 'w', encoding='utf-8') as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
print(f"\nRe-upload plan saved to: {plan_file}")
print(f"\n=== Summary ===")
print(f"Can re-upload: {len(local_slugs)} skills (will fix metadata + visibility)")
print(f"Cannot re-upload: {len(missing_slugs)} skills (no local SKILL.md)")
print(f"Org_only fixable: {len(org_only_local)} / {len(org_only_slugs)}")
