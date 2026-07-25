#!/usr/bin/env python3
"""验证重传skill的元数据"""
import json, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from urllib.request import urlopen, Request
from enterprise_uploader import load_cookies, ORG_ID, API_BASE

cookies = load_cookies()
headers = {'Cookie': cookies, 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}

time.sleep(2)
slug = 'ad-creative-intel-free'
url = f'{API_BASE}/orgs/{ORG_ID}/skills/{slug}'
req = Request(url, headers=headers)
with urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode('utf-8'))
skill = data.get('skill', data)
print(f'=== {slug} verification ===')
print(f'  status: {skill.get("status", "N/A")}')
print(f'  visibility: {skill.get("visibility", "N/A")}')
print(f'  category: {skill.get("category", "N/A")}')
print(f'  categories: {skill.get("categories", "N/A")}')
print(f'  tags: {skill.get("tags", "N/A")}')
print(f'  summary_zh: {skill.get("summary_zh", "N/A")}')
print(f'  iconUrl: {"Y" if skill.get("iconUrl") else "N/A"}')
print(f'  displayName: {skill.get("displayName", "N/A")}')
print(f'  All keys: {list(skill.keys())}')
