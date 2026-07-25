#!/usr/bin/env python3
"""诊断566错误 - 获取完整错误响应"""
import json, sys, os, time, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from enterprise_uploader import (
    load_cookies, ORG_ID, API_BASE, find_skill_md, parse_frontmatter,
    get_platform_category, get_team_category_id, get_subcategories,
    parse_tags, generate_summary_zh, CATEGORY_ICONS, DEFAULT_ICON, ORG_SKILLS_API
)

cookies = load_cookies()

# Test with clickhouse-olap-expert
slug = 'clickhouse-olap-expert'
skill_md = find_skill_md(slug)
content = skill_md.read_text(encoding='utf-8')
if content.startswith('\ufeff'):
    content = content[1:]
fm = parse_frontmatter(content)
body = fm.get('_body', '')

platform_category = get_platform_category(slug, fm, body)
team_category_id = get_team_category_id(platform_category)
tags_list = parse_tags(fm, body)
summary_zh = fm.get('summary_zh', '') or generate_summary_zh(fm, body)
icon_url = CATEGORY_ICONS.get(platform_category, DEFAULT_ICON)

version = fm.get('version', '1.0.0')
parts = version.split('.')
if len(parts) == 3:
    new_version = f"{parts[0]}.{parts[1]}.{int(parts[2]) + 1}"
else:
    new_version = '1.0.1'

payload = {
    'slug': fm.get('slug', slug),
    'name': fm.get('name', slug),
    'displayName': fm.get('displayName', fm.get('name', slug)),
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
    'changelog': f'v{new_version} - 元数据修复',
    'tools': fm.get('tools', ['read', 'exec']),
    'content': content,
    'visibility': 'public',
}

print(f'Slug: {slug}')
print(f'Content size: {len(content)} chars')
print(f'Payload size: {len(json.dumps(payload, ensure_ascii=False))} chars')

# Build FormData
boundary = f"----WebKitFormBoundary{int(time.time() * 1000)}"
payload_json = json.dumps(payload, ensure_ascii=False)
skill_md_content = content.encode('utf-8')

body_parts = []
body_parts.append(f"--{boundary}\r\n".encode('utf-8'))
body_parts.append(f'Content-Disposition: form-data; name="payload"\r\n\r\n'.encode('utf-8'))
body_parts.append(payload_json.encode('utf-8') + b"\r\n")
body_parts.append(f"--{boundary}\r\n".encode('utf-8'))
body_parts.append(f'Content-Disposition: form-data; name="files"; filename="SKILL.md"\r\n'.encode('utf-8'))
body_parts.append(b'Content-Type: text/markdown\r\n\r\n')
body_parts.append(skill_md_content + b"\r\n")
body_parts.append(f"--{boundary}--\r\n".encode('utf-8'))
body_data = b"".join(body_parts)

headers = {
    'Content-Type': f'multipart/form-data; boundary={boundary}',
    'Cookie': cookies,
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

print(f'\nTotal request body size: {len(body_data)} bytes')
print(f'Attempting upload...')

try:
    req = Request(ORG_SKILLS_API, data=body_data, headers=headers, method='POST')
    with urlopen(req, timeout=30) as resp:
        response_data = json.loads(resp.read().decode('utf-8'))
        print(f'✅ Success: {json.dumps(response_data, ensure_ascii=False)[:200]}')
except HTTPError as e:
    error_body = e.read().decode('utf-8', errors='replace')
    print(f'❌ HTTP {e.code}')
    print(f'Response headers: {dict(e.headers)}')
    print(f'Response body (first 1000 chars): {error_body[:1000]}')
    
    # Check if it's a WAF block
    if 'aegis' in error_body.lower() or 'waf' in error_body.lower() or '安全' in error_body:
        print('\n⚠️ WAF block detected!')
    
    # Try with truncated content
    print('\n--- Retrying with truncated content (10000 chars) ---')
    truncated_content = content[:10000]
    if not truncated_content.endswith('---'):
        truncated_content += '\n---\n'
    
    payload['content'] = truncated_content
    payload_json2 = json.dumps(payload, ensure_ascii=False)
    
    body_parts2 = []
    body_parts2.append(f"--{boundary}\r\n".encode('utf-8'))
    body_parts2.append(f'Content-Disposition: form-data; name="payload"\r\n\r\n'.encode('utf-8'))
    body_parts2.append(payload_json2.encode('utf-8') + b"\r\n")
    body_parts2.append(f"--{boundary}\r\n".encode('utf-8'))
    body_parts2.append(f'Content-Disposition: form-data; name="files"; filename="SKILL.md"\r\n'.encode('utf-8'))
    body_parts2.append(b'Content-Type: text/markdown\r\n\r\n')
    body_parts2.append(truncated_content.encode('utf-8') + b"\r\n")
    body_parts2.append(f"--{boundary}--\r\n".encode('utf-8'))
    body_data2 = b"".join(body_parts2)
    
    headers2 = {
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'Cookie': cookies,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0',
    }
    
    try:
        req2 = Request(ORG_SKILLS_API, data=body_data2, headers=headers2, method='POST')
        with urlopen(req2, timeout=30) as resp2:
            response_data2 = json.loads(resp2.read().decode('utf-8'))
            print(f'✅ Truncated upload success: {json.dumps(response_data2, ensure_ascii=False)[:200]}')
    except HTTPError as e2:
        error_body2 = e2.read().decode('utf-8', errors='replace')
        print(f'❌ Truncated also failed: HTTP {e2.code}')
        print(f'Response (first 500): {error_body2[:500]}')
    except Exception as e2:
        print(f'❌ Truncated error: {e2}')
except Exception as e:
    print(f'❌ Error: {e}')
