#!/usr/bin/env python3
"""
企业版SkillHub上传脚本
======================
集成门控检查，确保每个skill通过评分和正确性检查后才上传。

使用方式:
    python enterprise_uploader.py list              # 列出已上传的skill
    python enterprise_uploader.py upload <slug>     # 上传单个skill
    python enterprise_uploader.py upload-all        # 上传所有通过门控的skill
    python enterprise_uploader.py status            # 查看上传状态
"""

import json
import os
import re
import sys
import time
import sqlite3
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (
    DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR,
    is_paid_skill, TRACE_PASS_THRESHOLD
)

# ============ 企业版配置 ============
ORG_ID = 862
API_BASE = "https://api.skillhub.cn/api/v1"
ORG_SKILLS_API = f"{API_BASE}/orgs/{ORG_ID}/skills"

# Cookie文件路径（从浏览器获取）
COOKIE_FILE = Path(os.environ.get(
    'SKILLHUB_COOKIE_FILE',
    os.path.join(os.path.expanduser('~'), '.skillhub_cookies.txt')
))

# 上传日志
UPLOAD_LOG = REPORT_DIR / "enterprise_upload_log.json"


def load_cookies():
    """加载浏览器cookie"""
    if COOKIE_FILE.exists():
        cookies = COOKIE_FILE.read_text(encoding='utf-8').strip()
        if cookies:
            return cookies
    
    # 尝试从环境变量获取
    env_cookies = os.environ.get('SKILLHUB_SESSION_COOKIE', '')
    if env_cookies:
        return env_cookies
    
    return None


def get_gate_status(slug: str) -> dict:
    """获取skill的门控状态"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 获取评分
    c.execute("""
        SELECT sc.total_score, sc.is_pass, sc.score_type
        FROM scores sc JOIN skills s ON sc.skill_id = s.id
        WHERE s.slug = ? AND sc.score_type != 'baseline'
        ORDER BY sc.scored_at DESC LIMIT 1
    """, (slug,))
    score_row = c.fetchone()
    
    # 获取定价
    c.execute("""
        SELECT suggested_price, pricing_tier, is_paid
        FROM skills WHERE slug = ?
    """, (slug,))
    price_row = c.fetchone()
    
    conn.close()
    
    if not score_row:
        return {'has_score': False, 'passed': False, 'reason': '无评分记录'}
    
    total = score_row[0] or 0
    is_pass = score_row[1] or 0
    
    if total < TRACE_PASS_THRESHOLD:
        return {'has_score': True, 'passed': False, 'reason': f'评分{total}/{TRACE_PASS_THRESHOLD}低于阈值'}
    
    return {
        'has_score': True,
        'passed': True,
        'total_score': total,
        'is_pass': is_pass,
        'price': price_row[0] if price_row else 0,
        'tier': price_row[1] if price_row else '',
        'is_paid': bool(price_row[2]) if price_row else False,
        'license': '',  # 从SKILL.md读取,不查DB
    }


def find_skill_md(slug: str) -> Path:
    """根据slug找到SKILL.md文件"""
    for base_dir in [PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR]:
        if not base_dir.exists():
            continue
        for d in base_dir.iterdir():
            if d.is_dir() and (d / "SKILL.md").exists():
                content = (d / "SKILL.md").read_text(encoding='utf-8')
                if content.startswith('\ufeff'):
                    content = content[1:]
                if content.startswith('---'):
                    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                    if len(parts) >= 3:
                        fm = parts[1]
                        slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                        if slug_match and slug_match.group(1).strip() == slug:
                            return d / "SKILL.md"
    return None


def parse_frontmatter(content: str) -> dict:
    """解析SKILL.md的frontmatter"""
    if content.startswith('\ufeff'):
        content = content[1:]
    
    if not content.startswith('---'):
        return {}
    
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    
    fm = parts[1]
    body = parts[2].strip()
    
    result = {}
    # 简单YAML解析
    for line in fm.split('\n'):
        match = re.match(r'^(\w+):\s*["\']?(.+?)["\']?\s*$', line)
        if match:
            result[match.group(1)] = match.group(2)
    
    # 解析多行description
    desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
    if desc_match:
        result['description'] = desc_match.group(1).strip()
    
    # 解析tools列表
    tools_match = re.findall(r'^\s+-\s+(.+)$', fm, re.MULTILINE)
    if tools_match:
        result['tools'] = tools_match
    
    result['_body'] = body
    result['_full_content'] = content
    return result


def upload_skill(slug: str, dry_run: bool = False) -> dict:
    """上传单个skill到企业版SkillHub
    
    Returns:
        dict with keys: success, slug, message, response
    """
    # 1. 门控检查
    gate = get_gate_status(slug)
    if not gate['passed']:
        return {'success': False, 'slug': slug, 'message': f"门控未通过: {gate['reason']}"}
    
    # 2. 找到SKILL.md文件
    skill_md = find_skill_md(slug)
    if not skill_md:
        return {'success': False, 'slug': slug, 'message': 'SKILL.md文件未找到'}
    
    # 3. 解析frontmatter
    content = skill_md.read_text(encoding='utf-8')
    fm = parse_frontmatter(content)
    
    if not fm.get('slug'):
        return {'success': False, 'slug': slug, 'message': 'frontmatter解析失败'}
    
    # 4. 构建上传payload
    is_paid = gate['is_paid'] or is_paid_skill(fm.get('license', ''), fm.get('edition', ''))
    price = gate['price'] or 0
    
    payload = {
        'slug': fm.get('slug', slug),
        'name': fm.get('name', slug),
        'displayName': fm.get('displayName', fm.get('name', slug)),
        'version': fm.get('version', '1.0.0'),
        'summary': fm.get('summary', ''),
        'description': fm.get('description', ''),
        'license': fm.get('license', 'MIT'),
        'homepage': fm.get('homepage', 'https://skillhub.cn'),
        'tags': fm.get('tags', ''),
        'tools': fm.get('tools', ['read', 'exec']),
        'content': content,  # 完整SKILL.md内容
    }
    
    # 定价信息
    if is_paid and price > 0:
        payload['billingType'] = 'per_call'
        payload['price'] = price
        payload['pricingTier'] = gate.get('tier', 'professional')
    
    if dry_run:
        print(f"  [DRY RUN] {slug}: score={gate['total_score']}/50, price={price}元, paid={is_paid}")
        return {'success': True, 'slug': slug, 'message': 'DRY RUN', 'dry_run': True}
    
    # 5. 获取认证cookie
    cookies = load_cookies()
    if not cookies:
        return {'success': False, 'slug': slug, 'message': '无认证cookie，请先设置SKILLHUB_SESSION_COOKIE环境变量或cookie文件'}
    
    # 6. 构建请求
    boundary = f"----WebKitFormBoundary{int(time.time() * 1000)}"
    
    # FormData with payload as JSON string
    payload_json = json.dumps(payload, ensure_ascii=False)
    
    body_parts = []
    body_parts.append(f"--{boundary}\r\n")
    body_parts.append(f'Content-Disposition: form-data; name="payload"\r\n\r\n')
    body_parts.append(payload_json + "\r\n")
    body_parts.append(f"--{boundary}--\r\n")
    
    body = "".join(body_parts).encode('utf-8')
    
    headers = {
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'Cookie': cookies,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0',
    }
    
    # 7. 发送请求
    try:
        req = Request(ORG_SKILLS_API, data=body, headers=headers, method='POST')
        with urlopen(req, timeout=30) as resp:
            response_data = json.loads(resp.read().decode('utf-8'))
            return {
                'success': True,
                'slug': slug,
                'message': '上传成功',
                'response': response_data,
                'score': gate['total_score'],
                'price': price,
                'is_paid': is_paid,
            }
    except HTTPError as e:
        error_body = e.read().decode('utf-8', errors='replace')
        try:
            error_json = json.loads(error_body)
            error_msg = error_json.get('message', error_body)
        except json.JSONDecodeError:
            error_msg = error_body[:200]
        return {'success': False, 'slug': slug, 'message': f'HTTP {e.code}: {error_msg}'}
    except URLError as e:
        return {'success': False, 'slug': slug, 'message': f'网络错误: {str(e)}'}
    except Exception as e:
        return {'success': False, 'slug': slug, 'message': f'未知错误: {str(e)}'}


def cmd_list():
    """列出所有待上传的skill及其门控状态"""
    print("=" * 80)
    print("企业版SkillHub上传状态 (org: {})".format(ORG_ID))
    print("=" * 80)
    
    all_slugs = []
    for base_dir in [PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR]:
        if not base_dir.exists():
            continue
        for d in sorted(base_dir.iterdir()):
            if d.is_dir() and (d / "SKILL.md").exists():
                content = (d / "SKILL.md").read_text(encoding='utf-8')
                if content.startswith('\ufeff'):
                    content = content[1:]
                if content.startswith('---'):
                    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                    if len(parts) >= 3:
                        fm = parts[1]
                        slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                        if slug_match:
                            all_slugs.append(slug_match.group(1).strip())
    
    print(f"\n共 {len(all_slugs)} 个skill\n")
    print(f"{'Slug':<40} {'门控':<6} {'评分':<10} {'定价':<10} {'类型':<8}")
    print("-" * 80)
    
    passed = 0
    for slug in all_slugs:
        gate = get_gate_status(slug)
        if gate['passed']:
            passed += 1
            score_str = f"{gate['total_score']}/50"
            price_str = f"{gate['price']}元" if gate['price'] else "免费"
            type_str = "付费" if gate['is_paid'] else "免费"
            print(f"{slug:<40} {'✓':<6} {score_str:<10} {price_str:<10} {type_str:<8}")
        else:
            print(f"{slug:<40} {'✗':<6} {gate['reason']}")
    
    print(f"\n通过门控: {passed}/{len(all_slugs)}")
    
    # 检查cookie
    cookies = load_cookies()
    if cookies:
        print(f"认证cookie: 已配置")
    else:
        print(f"认证cookie: 未配置 (请设置环境变量SKILLHUB_SESSION_COOKIE)")


def cmd_upload(slug: str, dry_run: bool = False):
    """上传单个skill"""
    print(f"上传 {slug} 到企业版SkillHub (org: {ORG_ID})...")
    result = upload_skill(slug, dry_run)
    
    if result['success']:
        print(f"  ✓ {result['message']}")
        if 'score' in result:
            print(f"    评分: {result['score']}/50, 定价: {result.get('price', 0)}元")
    else:
        print(f"  ✗ {result['message']}")
    
    # 记录日志
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        **result,
    }
    save_log(log_entry)


def cmd_upload_all(dry_run: bool = False, delay: float = 2.0):
    """上传所有通过门控的skill"""
    print("=" * 80)
    print(f"批量上传到企业版SkillHub (org: {ORG_ID})")
    print("=" * 80)
    
    # 获取所有通过门控的slug
    all_slugs = []
    for base_dir in [PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR]:
        if not base_dir.exists():
            continue
        for d in sorted(base_dir.iterdir()):
            if d.is_dir() and (d / "SKILL.md").exists():
                content = (d / "SKILL.md").read_text(encoding='utf-8')
                if content.startswith('\ufeff'):
                    content = content[1:]
                if content.startswith('---'):
                    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                    if len(parts) >= 3:
                        fm = parts[1]
                        slug_match = re.search(r'^slug:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                        if slug_match:
                            all_slugs.append(slug_match.group(1).strip())
    
    # 检查已上传的
    uploaded_slugs = set()
    if UPLOAD_LOG.exists():
        with open(UPLOAD_LOG, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if entry.get('success') and not entry.get('dry_run'):
                        uploaded_slugs.add(entry['slug'])
                except json.JSONDecodeError:
                    continue
    
    success_count = 0
    fail_count = 0
    skip_count = 0
    
    for i, slug in enumerate(all_slugs, 1):
        gate = get_gate_status(slug)
        
        if not gate['passed']:
            skip_count += 1
            continue
        
        if slug in uploaded_slugs and not dry_run:
            print(f"  [{i}/{len(all_slugs)}] {slug} - 已上传,跳过")
            skip_count += 1
            continue
        
        print(f"  [{i}/{len(all_slugs)}] {slug} (score={gate['total_score']}, price={gate['price']}元)...", end="")
        
        result = upload_skill(slug, dry_run)
        
        if result['success']:
            print(f" ✓ {result['message']}")
            success_count += 1
        else:
            print(f" ✗ {result['message']}")
            fail_count += 1
        
        # 记录日志
        log_entry = {'timestamp': datetime.now().isoformat(), **result}
        save_log(log_entry)
        
        # 延迟，避免API限流
        if not dry_run and i < len(all_slugs):
            time.sleep(delay)
    
    print(f"\n{'=' * 80}")
    print(f"上传完成: 成功 {success_count}, 失败 {fail_count}, 跳过 {skip_count}")
    print(f"{'=' * 80}")


def save_log(entry: dict):
    """保存上传日志"""
    with open(UPLOAD_LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')


def cmd_status():
    """查看上传状态"""
    if not UPLOAD_LOG.exists():
        print("暂无上传记录")
        return
    
    print("=" * 80)
    print("企业版上传日志")
    print("=" * 80)
    
    success = []
    fail = []
    
    with open(UPLOAD_LOG, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                if entry.get('success') and not entry.get('dry_run'):
                    success.append(entry)
                elif not entry.get('dry_run'):
                    fail.append(entry)
            except json.JSONDecodeError:
                continue
    
    print(f"\n成功上传: {len(success)} 个")
    for e in success[-10:]:  # 最近10条
        print(f"  ✓ {e['slug']} - {e.get('timestamp', '')}")
    
    if fail:
        print(f"\n上传失败: {len(fail)} 个")
        for e in fail[-10:]:
            print(f"  ✗ {e['slug']} - {e.get('message', '')}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python enterprise_uploader.py [list|upload <slug>|upload-all|status]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == 'list':
        cmd_list()
    elif cmd == 'upload' and len(sys.argv) >= 3:
        dry = '--dry-run' in sys.argv
        cmd_upload(sys.argv[2], dry)
    elif cmd == 'upload-all':
        dry = '--dry-run' in sys.argv
        cmd_upload_all(dry)
    elif cmd == 'status':
        cmd_status()
    else:
        print(f"未知命令: {cmd}")
        print("Usage: python enterprise_uploader.py [list|upload <slug>|upload-all|status]")
        sys.exit(1)
