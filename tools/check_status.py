#!/usr/bin/env python3
"""检查SkillHub当前状态: 审核队列、状态分布、可见性分布"""
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from urllib.request import urlopen, Request
from enterprise_uploader import load_cookies, ORG_ID, API_BASE

cookies = load_cookies()
if not cookies:
    print("ERROR: No cookies")
    sys.exit(1)

# 1. Check total skills and status distribution
print("=== 1. Skill Status Distribution ===")
all_statuses = {}
all_visibilities = {}
all_categories = {}
total_skills = 0
page = 1
while True:
    url = f'{API_BASE}/orgs/{ORG_ID}/admin/skills?page={page}&pageSize=100'
    req = Request(url, headers={
        'Cookie': cookies,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    })
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  Error on page {page}: {e}")
        break
    
    skills = data.get('skills', [])
    if not skills:
        break
    
    total_skills = data.get('total', total_skills)
    
    for s in skills:
        st = s.get('status', 'unknown')
        all_statuses[st] = all_statuses.get(st, 0) + 1
        vis = s.get('visibility', 'unknown')
        all_visibilities[vis] = all_visibilities.get(vis, 0) + 1
        cat = s.get('category', '')
        if cat:
            all_categories[cat] = all_categories.get(cat, 0) + 1
        else:
            all_categories['_empty'] = all_categories.get('_empty', 0) + 1
    
    if page * 100 >= total_skills:
        break
    page += 1
    if page > 30:  # Safety limit
        break

print(f"Total skills (API): {total_skills}")
print(f"Total skills (scanned): {sum(all_statuses.values())}")
print(f"\nStatus distribution:")
for st, cnt in sorted(all_statuses.items(), key=lambda x: -x[1]):
    print(f"  {st}: {cnt}")
print(f"\nVisibility distribution:")
for vis, cnt in sorted(all_visibilities.items(), key=lambda x: -x[1]):
    print(f"  {vis}: {cnt}")
print(f"\nCategory distribution:")
for cat, cnt in sorted(all_categories.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {cnt}")

# 2. Check review queue
print("\n=== 2. Review Queue ===")
review_endpoints = [
    f'{API_BASE}/orgs/{ORG_ID}/admin/skill-reviews?page=1&pageSize=10',
    f'{API_BASE}/orgs/{ORG_ID}/admin/reviews?page=1&pageSize=10',
    f'{API_BASE}/orgs/{ORG_ID}/skill-reviews?page=1&pageSize=10',
]
for rev_url in review_endpoints:
    try:
        req = Request(rev_url, headers={
            'Cookie': cookies,
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        with urlopen(req, timeout=15) as resp:
            rev_data = json.loads(resp.read().decode('utf-8'))
        print(f"  Endpoint: {rev_url.split('/api/v1/')[1]}")
        print(f"  Total: {rev_data.get('total', 'N/A')}")
        items = rev_data.get('reviews', rev_data.get('items', rev_data.get('skills', [])))
        print(f"  Items on page: {len(items)}")
        if items:
            print(f"  Sample item keys: {list(items[0].keys())[:10]}")
        break
    except Exception as e:
        print(f"  Endpoint failed: {rev_url.split('/api/v1/')[1]} - {e}")

# 3. Check categoryIds on first 10 skills
print("\n=== 3. CategoryIds Check (first 10 skills) ===")
url = f'{API_BASE}/orgs/{ORG_ID}/admin/skills?page=1&pageSize=10'
req = Request(url, headers={
    'Cookie': cookies,
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0'
})
with urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for s in data.get('skills', [])[:10]:
    slug = s.get('slug', '')
    cat_ids = s.get('categoryIds', s.get('category_ids', []))
    icon = s.get('iconUrl', '')
    summary_zh = s.get('summary_zh', '')
    tags = s.get('tags', [])
    status = s.get('status', '')
    visibility = s.get('visibility', '')
    print(f"  {slug}: status={status}, vis={visibility}, catIds={cat_ids}, icon={'Y' if icon else 'N'}, sumZh={'Y' if summary_zh else 'N'}, tags={len(tags) if isinstance(tags, list) else 'dict'}")

# 4. Check specific rejected skills
print("\n=== 4. Rejected Skills Check ===")
rejected_check = ['ai-writing-style-cloner', 'api-design-architect', 'debug-doctor']
for slug in rejected_check:
    try:
        url = f'{API_BASE}/skills/{slug}'
        req = Request(url, headers={
            'Cookie': cookies,
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        with urlopen(req, timeout=15) as resp:
            detail = json.loads(resp.read().decode('utf-8'))
        skill = detail.get('skill', detail)
        print(f"  {slug}: status={skill.get('status', 'N/A')}, visibility={skill.get('visibility', 'N/A')}")
    except Exception as e:
        print(f"  {slug}: {e}")

# 5. Check org_only skills
print("\n=== 5. Org_only Skills Check ===")
org_only_check = ['ai-artist-workstation-pro', 'clickhouse-olap-expert', 'requirement-explorer-pro', 'lead-research-hunter']
for slug in org_only_check:
    try:
        url = f'{API_BASE}/skills/{slug}'
        req = Request(url, headers={
            'Cookie': cookies,
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        with urlopen(req, timeout=15) as resp:
            detail = json.loads(resp.read().decode('utf-8'))
        skill = detail.get('skill', detail)
        print(f"  {slug}: status={skill.get('status', 'N/A')}, visibility={skill.get('visibility', 'N/A')}")
    except Exception as e:
        print(f"  {slug}: {e}")

print("\n=== Done ===")
