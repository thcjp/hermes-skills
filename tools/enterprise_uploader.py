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
from skill_core.parser import parse_frontmatter as _parse_fm

# ============ 企业版配置 ============
ORG_ID = 862
API_BASE = "https://api.skillhub.cn/api/v1"
ORG_SKILLS_API = f"{API_BASE}/orgs/{ORG_ID}/skills"

# ============ 分类映射 ============
CATEGORY_MAP_FILE = Path(__file__).parent.parent / "data" / "category_mapping.json"

# ============ 团队分类ID映射（API要求的categoryIds字段） ============
# 从 category_mapping.json 的 team_categories 提取
# API要求 categoryIds 为数字ID数组，如 [11039]
TEAM_CATEGORY_IDS = {
    "通用办公": 11039,
    "研发工具": 11040,
    "系统运维": 11041,
    "质量测试": 11042,
    "需求设计": 11043,
    "信息检索": 11044,
    "项目管理": 11045,
    "数据分析": 11046,
    "安全合规": 11047,
    "其他": 11048,
}

# ============ 分类图标配置 ============
# 12个平台分类的图标URL映射
# 使用腾讯云COS公共资源URL + SVG data URI双重保障
ICON_BASE_URL = "https://cloudcache.tencent-cloud.com/qcloud/ui/static/other_external_resource/"

# 默认图标（SkillHub平台通用图标占位符）
DEFAULT_ICON = ICON_BASE_URL + "0860fda4-ff95-4bbc-b3ad-f6b7ad8e0774.png"

# 12个平台分类的图标 — 使用SVG data URI，每个分类不同颜色和图标符号
# SVG格式: 圆角矩形背景 + 分类首字母/图标符号 + 分类色调
import base64 as _base64

def _make_icon_svg(color: str, symbol: str) -> str:
    """生成SVG图标data URI"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">
  <rect width="128" height="128" rx="28" fill="{color}"/>
  <text x="64" y="82" font-size="56" font-weight="bold" text-anchor="middle" fill="white" font-family="sans-serif">{symbol}</text>
</svg>'''
    encoded = _base64.b64encode(svg.encode('utf-8')).decode('ascii')
    return f'data:image/svg+xml;base64,{encoded}'

CATEGORY_ICONS = {
    'office-efficiency': _make_icon_svg('#0052d9', '办'),      # 办公效率 - 腾讯蓝
    'content-creation': _make_icon_svg('#e8a200', '创'),        # 内容创作 - 橙色
    'dev-programming': _make_icon_svg('#007e3e', '码'),         # 开发编程 - 绿色
    'data-analysis': _make_icon_svg('#7b2d8e', '数'),           # 数据分析 - 紫色
    'design-media': _make_icon_svg('#d63384', '设'),            # 设计多媒体 - 粉色
    'ai-agent': _make_icon_svg('#0ca6a6', 'AI'),                # AI Agent - 青色
    'knowledge-management': _make_icon_svg('#364fc7', '知'),    # 知识管理 - 靛色
    'business-ops': _make_icon_svg('#8b5e3c', '商'),            # 商业运营 - 褐色
    'education': _make_icon_svg('#74b816', '学'),               # 教育学习 - 黄绿色
    'professional': _make_icon_svg('#495057', '专'),            # 行业专业 - 灰蓝色
    'it-ops-security': _make_icon_svg('#c92a2a', '安'),         # IT运维安全 - 红色
    'life-service': _make_icon_svg('#20c997', '活'),            # 生活服务 - 浅绿色
}

def _load_category_map():
    """加载分类映射配置"""
    if CATEGORY_MAP_FILE.exists():
        with open(CATEGORY_MAP_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

_CATEGORY_MAP_CACHE = None

def get_platform_category(slug: str, fm: dict, body: str) -> str:
    """根据slug、frontmatter和body内容推断SkillHub平台分类键"""
    global _CATEGORY_MAP_CACHE
    if _CATEGORY_MAP_CACHE is None:
        _CATEGORY_MAP_CACHE = _load_category_map()
    
    # 1. 从frontmatter的category字段获取
    fm_category = fm.get('category', '')
    if fm_category:
        # 如果已经是平台分类键，直接返回
        platform_cats = _CATEGORY_MAP_CACHE.get('platform_categories', {})
        if fm_category in platform_cats:
            return fm_category
        # 如果是本地分类名，映射到平台分类
        local_to_platform = _CATEGORY_MAP_CACHE.get('local_to_platform', {})
        if fm_category in local_to_platform:
            return local_to_platform[fm_category]
    
    # 2. 从slug推断
    slug_lower = slug.lower()
    keyword_map = {
        'ai-agent': ['agent', 'ai', 'llm', 'gpt', 'claude', 'memory', 'orchestrat'],
        'dev-programming': ['code', 'dev', 'program', 'api', 'debug', 'test', 'review', 'git', 'ci', 'cd'],
        'data-analysis': ['data', 'sql', 'analytic', 'csv', 'excel', 'chart', 'bi', 'dashboard'],
        'office-efficiency': ['doc', 'office', 'pdf', 'word', 'sheet', 'presentation', 'email', 'calendar'],
        'content-creation': ['content', 'write', 'copy', 'article', 'blog', 'social', 'media', 'video'],
        'design-media': ['design', 'graphic', 'ui', 'ux', 'image', 'photo', '3d', 'render'],
        'knowledge-management': ['knowledge', 'note', 'wiki', 'search', 'bookmark', 'research'],
        'business-ops': ['business', 'project', 'manage', 'crm', 'sales', 'finance', 'hr', 'account'],
        'it-ops-security': ['ops', 'devops', 'monitor', 'security', 'audit', 'compliance', 'deploy'],
        'education': ['edu', 'learn', 'teach', 'course', 'study', 'language'],
        'professional': ['legal', 'medical', 'finance', 'engineering', 'consult'],
        'life-service': ['life', 'travel', 'health', 'food', 'shopping', 'weather'],
    }
    for cat_key, keywords in keyword_map.items():
        for kw in keywords:
            if kw in slug_lower:
                return cat_key
    
    # 3. 从body内容推断
    body_lower = body[:2000].lower()
    for cat_key, keywords in keyword_map.items():
        matches = sum(1 for kw in keywords if kw in body_lower)
        if matches >= 2:
            return cat_key
    
    # 4. 默认分类
    return 'office-efficiency'

def get_team_category_id(platform_category: str) -> int:
    """从平台分类键获取团队分类数字ID
    
    映射链: platform_category(字符串) → platform_to_team(中文名) → TEAM_CATEGORY_IDS(数字ID)
    例: "office-efficiency" → "通用办公" → 11039
    
    Args:
        platform_category: 平台分类键，如 "office-efficiency"
    
    Returns:
        团队分类数字ID，如 11039。未知分类返回 11048（其他）
    """
    global _CATEGORY_MAP_CACHE
    if _CATEGORY_MAP_CACHE is None:
        _CATEGORY_MAP_CACHE = _load_category_map()
    
    platform_to_team = _CATEGORY_MAP_CACHE.get('platform_to_team', {})
    team_name = platform_to_team.get(platform_category, '其他')
    return TEAM_CATEGORY_IDS.get(team_name, 11048)

def get_subcategories(platform_category: str, fm: dict, body: str) -> list:
    """根据平台分类获取子分类列表"""
    global _CATEGORY_MAP_CACHE
    if _CATEGORY_MAP_CACHE is None:
        _CATEGORY_MAP_CACHE = _load_category_map()
    
    subcat_map = _CATEGORY_MAP_CACHE.get('subcategory_mapping', {})
    subcats = subcat_map.get(platform_category, [])
    
    # 根据body内容选择最相关的1-3个子分类
    if not subcats:
        return []
    
    body_lower = body[:2000].lower()
    scored = []
    for sc in subcats:
        score = 0
        # 检查子分类key中的关键词是否在body中出现
        key_parts = sc['key'].split('-')[1:]  # 去掉前缀
        for part in key_parts:
            if part in body_lower:
                score += 1
        scored.append((sc, score))
    
    # 按分数排序，取前3个
    scored.sort(key=lambda x: x[1], reverse=True)
    top = [sc for sc, _ in scored[:3]]
    return top

def parse_tags(fm: dict, body: str) -> list:
    """从frontmatter和body解析tags为字符串数组"""
    raw_tags = fm.get('tags', '')
    
    if isinstance(raw_tags, list):
        return raw_tags
    
    if isinstance(raw_tags, str) and raw_tags.strip():
        # 尝试解析为YAML列表或逗号分隔
        raw_tags = raw_tags.strip()
        if raw_tags.startswith('['):
            try:
                return json.loads(raw_tags)
            except json.JSONDecodeError:
                pass
        # 逗号分隔
        parts = [t.strip().strip('"\'') for t in raw_tags.split(',')]
        return [t for t in parts if t]
    
    # 从body提取关键词作为tags
    body_lower = body[:2000].lower()
    extracted_tags = []
    tag_keywords = {
        '自动化': ['自动化', '自动', 'auto', 'automat'],
        '分析': ['分析', 'analytic', 'analysis'],
        '生成': ['生成', 'generate', 'create'],
        '优化': ['优化', 'optim', 'improve'],
        '监控': ['监控', 'monitor', 'watch'],
        '管理': ['管理', 'manage', 'admin'],
        '转换': ['转换', 'convert', 'transform'],
        '搜索': ['搜索', 'search', 'find'],
        '安全': ['安全', 'security', 'safe'],
        '测试': ['测试', 'test', 'qa'],
    }
    for tag_name, keywords in tag_keywords.items():
        for kw in keywords:
            if kw in body_lower:
                extracted_tags.append(tag_name)
                break
    
    # 从slug提取
    slug_parts = fm.get('slug', '').split('-')
    for part in slug_parts:
        if len(part) > 2 and part not in ['the', 'and', 'for', 'pro', 'sk']:
            extracted_tags.append(part)
    
    # 去重，最多5个
    seen = set()
    unique_tags = []
    for t in extracted_tags:
        if t not in seen:
            seen.add(t)
            unique_tags.append(t)
        if len(unique_tags) >= 5:
            break
    
    return unique_tags[:5] if unique_tags else ['工具', '效率']

def generate_summary_zh(fm: dict, body: str) -> str:
    """生成中文摘要"""
    # 如果frontmatter已有summary_zh，直接使用
    existing = fm.get('summary_zh', '')
    if existing and existing.strip():
        return existing.strip()
    
    # 使用displayName和summary组合
    display_name = fm.get('displayName', fm.get('name', ''))
    summary = fm.get('summary', '')
    
    if summary:
        # 如果summary是中文，直接使用
        if any('\u4e00' <= c <= '\u9fff' for c in summary):
            return summary
        # 否则生成中文摘要
        return f"{display_name} - {summary[:100]}" if summary else display_name
    
    return display_name or '技能工具'

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
    conn.execute("PRAGMA foreign_keys = ON")
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
    """解析SKILL.md的frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    fields = result.get('fields', {})
    # 保持向后兼容: 添加_body和_full_content
    fields['_body'] = result.get('body', '')
    fields['_full_content'] = result.get('raw', content)
    return fields


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
    
    body = fm.get('_body', '')
    
    # 获取平台分类和子分类
    platform_category = get_platform_category(slug, fm, body)
    subcategories = get_subcategories(platform_category, fm, body)
    
    # 解析tags为数组，确保始终非空且为list格式
    tags_list = parse_tags(fm, body)
    if not tags_list:
        tags_list = ['工具', '效率']
    # 确保tags是list而非string
    if isinstance(tags_list, str):
        tags_list = [t.strip() for t in tags_list.split(',') if t.strip()]
        if not tags_list:
            tags_list = ['工具', '效率']
    
    # 生成中文摘要 — 优先使用frontmatter中的summary_zh，否则动态生成
    summary_zh = fm.get('summary_zh', '')
    if not summary_zh or not summary_zh.strip():
        summary_zh = generate_summary_zh(fm, body)
    
    # 版本更新说明
    version = fm.get('version', '1.0.0')
    changelog = fm.get('changelog', f'v{version} - MIT license, 分类: {platform_category}')
    
    # 确保license为MIT(修正MIT-0等变体)
    license_val = fm.get('license', 'MIT')
    if license_val and 'MIT' in license_val.upper() and license_val != 'MIT':
        license_val = 'MIT'
    
    # 获取团队分类数字ID（API必需字段）
    team_category_id = get_team_category_id(platform_category)
    
    payload = {
        'slug': fm.get('slug', slug),
        'name': fm.get('name', slug),
        'displayName': fm.get('displayName', fm.get('name', slug)),
        'version': version,
        'summary': fm.get('summary', ''),
        'summary_zh': summary_zh,
        'description': fm.get('description', ''),
        'license': license_val,
        'homepage': fm.get('homepage', ''),
        'tags': tags_list,
        'categoryIds': [team_category_id],  # API必需: 团队分类数字ID数组
        'category': platform_category,       # 保留作为备份，不影响功能
        'iconUrl': CATEGORY_ICONS.get(platform_category, DEFAULT_ICON),
        'subCategories': subcategories,
        'changelog': changelog,
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
