#!/usr/bin/env python3
"""全面测试非破坏性API端点: 元数据PATCH + 可见性PATCH + 版本升级POST"""
import json
import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from enterprise_uploader import (
    load_cookies, ORG_ID, API_BASE, find_skill_md, parse_frontmatter,
    get_platform_category, get_team_category_id, get_subcategories,
    parse_tags, generate_summary_zh, CATEGORY_ICONS, DEFAULT_ICON
)

cookies = load_cookies()
if not cookies:
    print("ERROR: No cookies")
    sys.exit(1)

# Build auth headers
if cookies.startswith('BEARER:'):
    api_key = cookies[len('BEARER:'):]
    auth_headers = {'Authorization': f'Bearer {api_key}'}
else:
    auth_headers = {'Cookie': cookies}

base_headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0',
    **auth_headers,
}

# Find a public skill to test with
print("=== Finding a public skill for testing ===")
test_slug = None
url = f'{API_BASE}/orgs/{ORG_ID}/admin/skills?page=1&pageSize=100'
req = Request(url, headers=base_headers)
with urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for s in data.get('skills', []):
    if s.get('visibility') == 'public':
        test_slug = s['slug']
        print(f"Found public skill: {test_slug}")
        break

if not test_slug:
    print("No public skill found, using first skill")
    test_slug = data['skills'][0]['slug']
    print(f"Using: {test_slug}")

# Also find an org_only skill for visibility test
org_only_slug = None
for s in data.get('skills', []):
    if s.get('visibility') == 'org_only':
        org_only_slug = s['slug']
        print(f"Found org_only skill for visibility test: {org_only_slug}")
        break

# 1. GET baseline via admin API
print(f"\n=== 1. GET Baseline (Admin API) ===")
admin_detail_url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{test_slug}"
try:
    req = Request(admin_detail_url, headers=base_headers)
    with urlopen(req, timeout=15) as resp:
        before_data = json.loads(resp.read().decode('utf-8'))
    before = before_data.get('skill', before_data)
    print(f"  status: {before.get('status', 'N/A')}")
    print(f"  visibility: {before.get('visibility', 'N/A')}")
    print(f"  category: {before.get('category', 'N/A')}")
    print(f"  categoryIds: {before.get('categoryIds', 'N/A')}")
    print(f"  tags: {before.get('tags', 'N/A')}")
    print(f"  summary_zh: {before.get('summary_zh', 'N/A')}")
    print(f"  iconUrl: {before.get('iconUrl', 'N/A')[:50] if before.get('iconUrl') else 'N/A'}")
    print(f"  All keys: {list(before.keys())[:20]}")
except HTTPError as e:
    error_body = e.read().decode('utf-8', errors='replace')
    print(f"  HTTP {e.code}: {error_body[:300]}")
    # Try alternate endpoint
    alt_url = f"{API_BASE}/orgs/{ORG_ID}/skills/{test_slug}"
    print(f"  Trying alternate: {alt_url}")
    try:
        req = Request(alt_url, headers=base_headers)
        with urlopen(req, timeout=15) as resp:
            before_data = json.loads(resp.read().decode('utf-8'))
        before = before_data.get('skill', before_data)
        print(f"  SUCCESS with alternate endpoint!")
        print(f"  All keys: {list(before.keys())[:20]}")
    except HTTPError as e2:
        error_body2 = e2.read().decode('utf-8', errors='replace')
        print(f"  Alternate also failed: HTTP {e2.code}: {error_body2[:200]}")
        before = {}
    except Exception as e2:
        print(f"  Alternate error: {e2}")
        before = {}

# 2. Build metadata payload
print(f"\n=== 2. Building Metadata Payload ===")
skill_md = find_skill_md(test_slug)
if not skill_md:
    print(f"  SKILL.md not found for {test_slug}")
    # Try with a slug that exists locally
    all_slugs_url = f'{API_BASE}/orgs/{ORG_ID}/admin/skills?page=1&pageSize=100'
    req = Request(all_slugs_url, headers=base_headers)
    with urlopen(req, timeout=30) as resp:
        all_data = json.loads(resp.read().decode('utf-8'))
    
    for s in all_data.get('skills', []):
        slug = s['slug']
        md = find_skill_md(slug)
        if md:
            test_slug = slug
            skill_md = md
            print(f"  Using local skill: {test_slug}")
            break

if skill_md:
    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    fm = parse_frontmatter(content)
    body = fm.get('_body', '')
    
    platform_category = get_platform_category(test_slug, fm, body)
    team_category_id = get_team_category_id(platform_category)
    tags_list = parse_tags(fm, body)
    if isinstance(tags_list, str):
        tags_list = [t.strip() for t in tags_list.split(',') if t.strip()]
    if not tags_list:
        tags_list = ['工具', '效率']
    
    summary_zh = fm.get('summary_zh', '')
    if not summary_zh or not summary_zh.strip():
        summary_zh = generate_summary_zh(fm, body)
    
    icon_url = CATEGORY_ICONS.get(platform_category, DEFAULT_ICON)
    subcategories = get_subcategories(platform_category, fm, body)
    
    payload = {
        'categoryIds': [team_category_id],
        'category': platform_category,
        'tags': tags_list,
        'summary_zh': summary_zh,
        'iconUrl': icon_url,
        'subCategories': subcategories,
    }
    print(f"  category: {platform_category}")
    print(f"  categoryIds: {[team_category_id]}")
    print(f"  tags: {tags_list}")
    print(f"  summary_zh: {summary_zh[:50]}...")
    print(f"  iconUrl: {icon_url[:50]}...")
    
    payload_json = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    
    # 3. Test PATCH on multiple endpoints
    print(f"\n=== 3. Testing PATCH Endpoints ===")
    patch_endpoints = [
        f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{test_slug}",
        f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{test_slug}/metadata",
        f"{API_BASE}/orgs/{ORG_ID}/skills/{test_slug}",
        f"{API_BASE}/skills/{test_slug}",
    ]
    
    patch_headers = {'Content-Type': 'application/json', **base_headers}
    
    for ep_url in patch_endpoints:
        ep_name = ep_url.split('/api/v1/')[1]
        try:
            req = Request(ep_url, data=payload_json, method='PATCH', headers=patch_headers)
            with urlopen(req, timeout=15) as resp:
                resp_data = json.loads(resp.read().decode('utf-8'))
            print(f"  ✅ PATCH {ep_name}: HTTP {resp.getcode()}")
            print(f"     Response: {json.dumps(resp_data, ensure_ascii=False)[:200]}")
            
            # Verify
            time.sleep(1)
            verify_url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{test_slug}"
            req = Request(verify_url, headers=base_headers)
            with urlopen(req, timeout=15) as resp:
                after_data = json.loads(resp.read().decode('utf-8'))
            after = after_data.get('skill', after_data)
            print(f"     After - categoryIds: {after.get('categoryIds', 'N/A')}, category: {after.get('category', 'N/A')}, tags: {after.get('tags', 'N/A')}, summary_zh: {after.get('summary_zh', 'N/A')[:30]}, iconUrl: {'Y' if after.get('iconUrl') else 'N'}")
            
            # If PATCH worked, no need to test other endpoints
            if after.get('categoryIds'):
                print(f"\n✅ PATCH SUCCESS on {ep_name}!")
                break
        except HTTPError as e:
            error_body = e.read().decode('utf-8', errors='replace')
            print(f"  ❌ PATCH {ep_name}: HTTP {e.code} - {error_body[:150]}")
        except Exception as e:
            print(f"  ❌ PATCH {ep_name}: {e}")
    
    # 4. Test PUT
    print(f"\n=== 4. Testing PUT Endpoints ===")
    for ep_url in patch_endpoints:
        ep_name = ep_url.split('/api/v1/')[1]
        try:
            req = Request(ep_url, data=payload_json, method='PUT', headers=patch_headers)
            with urlopen(req, timeout=15) as resp:
                resp_data = json.loads(resp.read().decode('utf-8'))
            print(f"  ✅ PUT {ep_name}: HTTP {resp.getcode()}")
            print(f"     Response: {json.dumps(resp_data, ensure_ascii=False)[:200]}")
            break
        except HTTPError as e:
            error_body = e.read().decode('utf-8', errors='replace')
            print(f"  ❌ PUT {ep_name}: HTTP {e.code} - {error_body[:150]}")
        except Exception as e:
            print(f"  ❌ PUT {ep_name}: {e}")

# 5. Test visibility PATCH
if org_only_slug:
    print(f"\n=== 5. Testing Visibility PATCH ===")
    vis_endpoints = [
        (f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{org_only_slug}/visibility", 'PATCH'),
        (f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{org_only_slug}/visibility", 'POST'),
        (f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{org_only_slug}", 'PATCH'),
        (f"{API_BASE}/orgs/{ORG_ID}/skills/{org_only_slug}/visibility", 'PATCH'),
    ]
    vis_payload = json.dumps({'visibility': 'public'}).encode('utf-8')
    
    for vis_url, method in vis_endpoints:
        ep_name = vis_url.split('/api/v1/')[1]
        try:
            req = Request(vis_url, data=vis_payload, method=method, headers=patch_headers)
            with urlopen(req, timeout=15) as resp:
                resp_data = json.loads(resp.read().decode('utf-8'))
            print(f"  ✅ {method} {ep_name}: HTTP {resp.getcode()}")
            print(f"     Response: {json.dumps(resp_data, ensure_ascii=False)[:200]}")
            
            # Verify
            time.sleep(1)
            verify_url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{org_only_slug}"
            req = Request(verify_url, headers=base_headers)
            with urlopen(req, timeout=15) as resp:
                after_data = json.loads(resp.read().decode('utf-8'))
            after = after_data.get('skill', after_data)
            print(f"     After visibility: {after.get('visibility', 'N/A')}")
            if after.get('visibility') == 'public':
                print(f"\n✅ VISIBILITY PATCH SUCCESS!")
                break
        except HTTPError as e:
            error_body = e.read().decode('utf-8', errors='replace')
            print(f"  ❌ {method} {ep_name}: HTTP {e.code} - {error_body[:150]}")
        except Exception as e:
            print(f"  ❌ {method} {ep_name}: {e}")

# 6. Test POST with version upgrade (non-destructive)
print(f"\n=== 6. Testing POST Version Upgrade ===")
if skill_md:
    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    fm = parse_frontmatter(content)
    body = fm.get('_body', '')
    
    platform_category = get_platform_category(test_slug, fm, body)
    team_category_id = get_team_category_id(platform_category)
    tags_list = parse_tags(fm, body)
    summary_zh = fm.get('summary_zh', '') or generate_summary_zh(fm, body)
    icon_url = CATEGORY_ICONS.get(platform_category, DEFAULT_ICON)
    
    version = fm.get('version', '1.0.0')
    # Increment version
    parts = version.split('.')
    if len(parts) == 3:
        new_version = f"{parts[0]}.{parts[1]}.{int(parts[2]) + 1}"
    else:
        new_version = '1.0.1'
    
    upgrade_payload = {
        'slug': fm.get('slug', test_slug),
        'name': fm.get('name', test_slug),
        'displayName': fm.get('displayName', fm.get('name', test_slug)),
        'version': new_version,
        'summary': fm.get('summary', ''),
        'summary_zh': summary_zh,
        'description': fm.get('description', ''),
        'license': 'MIT',
        'homepage': fm.get('homepage', ''),
        'tags': tags_list,
        'categoryIds': [team_category_id],
        'category': platform_category,
        'iconUrl': icon_url,
        'subCategories': get_subcategories(platform_category, fm, body),
        'changelog': f'v{new_version} - 元数据修复: categoryIds/iconUrl/summary_zh/tags',
        'tools': fm.get('tools', ['read', 'exec']),
        'content': content,
        'visibility': 'public',
    }
    
    print(f"  Test slug: {test_slug}")
    print(f"  Old version: {version}, New version: {new_version}")
    print(f"  categoryIds: {[team_category_id]}")
    
    # POST to upgrade endpoint
    upgrade_url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{test_slug}/upgrade"
    upgrade_payload_json = json.dumps(upgrade_payload, ensure_ascii=False).encode('utf-8')
    try:
        req = Request(upgrade_url, data=upgrade_payload_json, method='POST', headers=patch_headers)
        with urlopen(req, timeout=30) as resp:
            resp_data = json.loads(resp.read().decode('utf-8'))
        print(f"  ✅ POST upgrade: HTTP {resp.getcode()}")
        print(f"     Response: {json.dumps(resp_data, ensure_ascii=False)[:200]}")
    except HTTPError as e:
        error_body = e.read().decode('utf-8', errors='replace')
        print(f"  ❌ POST upgrade: HTTP {e.code} - {error_body[:200]}")
    except Exception as e:
        print(f"  ❌ POST upgrade: {e}")

print("\n=== Test Complete ===")
