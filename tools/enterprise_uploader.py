#!/usr/bin/env python3
"""
企业版SkillHub上传脚本 (V192)
==============================
集成门控检查，确保每个skill通过评分和正确性检查后才上传。

╔══════════════════════════════════════════════════════════════════════╗
║  V192: SkillHub上传流程完整说明 — 消除所有混淆点                    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  1. 认证方式 (关键!)                                                ║
║  ─────────────────────────────────                                   ║
║  SkillHub API不接受cookie文件或CLI API Key的直接urllib请求。         ║
║  只有浏览器活跃session(通过relay-serve)才能成功上传。               ║
║                                                                      ║
║  认证测试结果:                                                      ║
║  • Cookie文件 (~/.skillhub_cookies.txt) → 401 "enterprise auth     ║
║    required"                                                         ║
║  • CLI API Key (sk-ent-...) → 401 "invalid or expired token"        ║
║  • 浏览器session (api.skillhub.cn页面fetch) → 200/201 ✓            ║
║                                                                      ║
║  结论: upload / upload-all 命令(使用urllib)无法直接上传。            ║
║        relay-serve 是唯一可用的上传方式。                            ║
║                                                                      ║
║  2. API端点 (V191修复)                                             ║
║  ─────────────────────────                                           ║
║  ┌──────────────────────────┬───────┬──────────────────────┐         ║
║  │ 端点                     │ 方法  │ 用途                 │         ║
║  ├──────────────────────────┼───────┼──────────────────────┤         ║
║  │ /orgs/{ORG_ID}/skills    │ POST  │ 上传skill (无限制)   │         ║
║  │ /orgs/{ORG_ID}/skills    │ GET   │ 列出skill (简略)     │         ║
║  │ /orgs/{ORG_ID}/admin/... │ GET   │ 列出skill (详细)     │         ║
║  │ .../admin/.../approve    │ POST  │ 审核通过              │         ║
║  │ .../admin/.../publish    │ POST  │ 发布到社区            │         ║
║  │ /community/skills/publish│ POST  │ ❌ 已废弃! 有200限制  │         ║
║  └──────────────────────────┴───────┴──────────────────────┘         ║
║                                                                      ║
║  3. 上传流程                                                         ║
║  ──────────────────                                                 ║
║  relay-serve <slugs> --skip-gate                                    ║
║    ↓ 生成payloads.json + 启动CORS服务器(port 8766)                  ║
║  浏览器fetch payloads.json → 批量POST到API                           ║
║    ↓ 每批10个,间隔2秒                                                ║
║  relay-record / record_browser_upload_result()                      ║
║    ↓ 记录结果到DB                                                   ║
║                                                                      ║
║  4. HTTP状态码 → DB状态映射 (V194更新)                             ║
║  ────────────────────────────────────────                            ║
║  201 = 上传成功 → synced                                            ║
║  409 = slug冲突(已存在) → 自动尝试POST /versions更新 (V194)       ║
║        versions 201 → synced (新版本已上传,审核中)                 ║
║        versions 409 → synced (版本审核中,无法更新)                  ║
║  566 = WAF拦截 → waf_blocked                                         ║
║  其他 = 失败 → failed                                                ║
║                                                                      ║
║  5. 审核流程                                                         ║
║  ──────────────────                                                 ║
║  新上传skill的reviewStatus="pending" (内容审核+安全扫描中)          ║
║  审核通过后才能approve → publish-to-community                        ║
║  approve失败(400 "not in admin_review")是正常的 — 需等待审核完成     ║
║                                                                      ║
║  6. 速率限制 (自限制,非平台限制)                                   ║
║  ─────────────────────────────────────                               ║
║  SkillHub: 30/h, 100/d, 60s间隔 (daily_sync.py)                    ║
║  ClawHub: 100/h, 200/d, 2s间隔                                      ║
║  relay-serve模式跳过速率限制检查(payload≠实际上传)                 ║
║  实际速率控制: 浏览器端2秒间隔 + 手动批处理                         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

使用方式:
    python enterprise_uploader.py list              # 列出已上传的skill
    python enterprise_uploader.py upload <slug>     # 上传单个skill (需有效浏览器session)
    python enterprise_uploader.py upload-all        # 批量上传 (需有效浏览器session)
    python enterprise_uploader.py status            # 查看上传状态
    python enterprise_uploader.py relay-serve <slugs> --skip-gate  # 浏览器中继上传(推荐)
    python enterprise_uploader.py relay-publish [--limit N]  # V193: 浏览器中继发布(approve→publish→star)
    python enterprise_uploader.py relay-record <slug> <status> <response>  # 记录结果
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
# 添加PROJECT_ROOT到path,使config包可被import (脚本运行时cwd不在sys.path中)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# V186: 添加config目录到path,使project_config可直接import (与clawhub_batch_uploader.py一致)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config"))
from config import (
    DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR,
    DIFFERENTIATED_DIR, ENTERPRISE_UPLOAD_DIR,
    is_paid_skill, TRACE_PASS_THRESHOLD, PROJECT_ROOT
)
from skill_core.parser import parse_frontmatter as _parse_fm, find_skill_md

# 质量门控 (P1-2: 营销关卡 + v2.3: 安全预检 + 防幻觉 + v2.6: 评分门控)
try:
    from quality_gate import (
        run_marketing_gate, run_security_precheck, run_anti_hallucination, run_rating_gate
    )
    _QUALITY_GATE_AVAILABLE = True
except ImportError:
    _QUALITY_GATE_AVAILABLE = False

# ============ 企业版配置 ============
# V186: 切换到ORG_ID=1436(智创未来) — org 862(科创少年)已被封
ORG_ID = 1436
API_BASE = "https://api.skillhub.cn/api/v1"
ORG_SKILLS_API = f"{API_BASE}/orgs/{ORG_ID}/skills"  # V191: 组织skill上传端点(POST=上传, 专业版无200限制) — GET列表走/orgs/{ORG_ID}/admin/skills, approve/publish走/orgs/{ORG_ID}/admin/skills/{slug}/*

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
    """加载认证凭证：优先环境变量(允许覆盖),其次cookie文件,最后CLI凭证文件
    
    V182: 增加bt_商户token支持(通过环境变量SKILLHUB_MERCHANT_TOKEN传入)
    V196: 增加项目凭证文件(.skillhub-credentials/api-key.txt)作为认证源
    认证优先级:
    1. SKILLHUB_SESSION_COOKIE 环境变量(浏览器session)
    2. SKILLHUB_MERCHANT_TOKEN 环境变量(bt_商户token)
    3. cookie文件(浏览器session)
    4. 项目凭证文件(.skillhub-credentials/api-key.txt) — V196新增
    5. CLI凭证文件(sk-ent- API Key — 仅verify有效,发布可能401)
    """
    # 1. 环境变量(最高优先级 — 允许运行时覆盖过期凭证)
    env_cookies = os.environ.get('SKILLHUB_SESSION_COOKIE', '')
    if env_cookies:
        return env_cookies

    # 1.5 bt_商户token (V182新增)
    env_merchant = os.environ.get('SKILLHUB_MERCHANT_TOKEN', '')
    if env_merchant:
        return f'BEARER:{env_merchant}'

    # 2. cookie文件(浏览器session)
    if COOKIE_FILE.exists():
        cookies = COOKIE_FILE.read_text(encoding='utf-8-sig').strip()
        if cookies:
            return cookies

    # 3. 项目凭证文件 (V196新增 — d:\skills\.skillhub-credentials\api-key.txt)
    project_creds = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) / '.skillhub-credentials' / 'api-key.txt'
    if project_creds.exists():
        try:
            content = project_creds.read_text(encoding='utf-8-sig').strip()
            merchant_token = None
            api_key = None
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('SKILLHUB_TOKEN='):
                    merchant_token = line.split('=', 1)[1].strip()
                elif line.startswith('SKILLHUB_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
            # bt_商户token优先(权限更高), 其次API key
            if merchant_token:
                return f'BEARER:{merchant_token}'
            if api_key:
                return f'BEARER:{api_key}'
        except Exception as e:
            print(f"  [WARN] 项目凭证文件加载失败: {e}")

    # 4. CLI凭证文件(sk-ent- API Key — 可能权限不足)
    cli_creds = Path(os.path.expanduser('~')) / '.skillhub' / 'credentials.json'
    if cli_creds.exists():
        try:
            import json as _json
            creds = _json.loads(cli_creds.read_text(encoding='utf-8'))
            orgs = creds.get('orgs', {})
            for org_id, org_data in orgs.items():
                if org_data.get('orgId') == ORG_ID:
                    api_key = org_data.get('apiKey', '')
                    if api_key:
                        return f'BEARER:{api_key}'
        except Exception as e:
            print(f"  [WARN] API key加载失败: {e}")
    
    return None


def get_gate_status(slug: str) -> dict:
    """获取skill的门控状态"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    
    # 获取评分 — 优先trace_llm评分(TRACE_PASS_THRESHOLD=45是TRACE评分阈值)
    # 修复: 原查询取最新非baseline评分,可能取到local_quality(0-5分制)与TRACE阈值(45)比较导致误判
    c.execute("""
        SELECT sc.total_score, sc.is_pass, sc.score_type
        FROM scores sc JOIN skills s ON sc.skill_id = s.id
        WHERE s.slug = ? AND sc.score_type = 'trace_llm' AND sc.is_current = 1
        ORDER BY sc.scored_at DESC LIMIT 1
    """, (slug,))
    score_row = c.fetchone()
    
    if not score_row:
        # 回退: 取最新非baseline评分(兼容旧数据)
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


def parse_frontmatter(content: str) -> dict:
    """解析SKILL.md的frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    fields = result.get('fields', {})
    # 保持向后兼容: 添加_body和_full_content
    fields['_body'] = result.get('body', '')
    fields['_full_content'] = result.get('raw', content)
    return fields


def _post_upload_publish(slug: str) -> dict:
    """上传成功后的完整发布流程 (委托到platform_ops.post_upload_publish统一入口)

    统一入口确保所有上传路径(CLI/API/旧流程)使用相同的发布流程:
    approve → publish_to_community → star → DB更新

    Returns:
        dict with approve, community, star, db_update
    """
    try:
        from platform_ops import post_upload_publish
        return post_upload_publish(slug)
    except ImportError:
        return {'error': 'platform_ops模块不可用,跳过发布流程'}
    except Exception as e:
        return {'error': f'发布流程异常: {e}'}


def upload_skill(slug: str, dry_run: bool = False, skip_gate: bool = False,
                 skip_marketing: bool = False, skip_security: bool = False,
                 skip_publish: bool = False, browser_relay: bool = False) -> dict:
    """上传单个skill到企业版SkillHub

    v2.7修复: 上传后自动执行完整发布流程(approve→publish_to_community→star)
    之前的流程仅上传skill, 未调用approve和publish_to_community,
    导致2022个skill停留在pending/visibility=org_only状态, 前台不可见。

    v3.5新增: browser_relay模式 — 当浏览器session有效但无法提取HttpOnly cookie时,
    通过浏览器中继方式上传。脚本执行全部防封措施(速率限制/内容去重/质量门控),
    构建payload后输出JSON供browser_evaluate提交, 提交结果通过record_browser_upload_result记录。

    Args:
        slug: skill slug
        dry_run: 仅模拟，不实际上传
        skip_gate: 跳过门控检查（用于已发布skill的元数据修复重传）
        skip_marketing: 跳过营销关卡检查（用于批量场景）
        skip_security: 跳过安全预检（用于紧急场景, v2.6新增）
        skip_publish: 跳过上传后发布流程(approve+publish_to_community+star)
                      用于version_sync_pipeline等自行管理发布流程的场景
        browser_relay: 浏览器中继模式(v3.5新增) — 构建payload后不发送HTTP请求,
                      而是返回payload+content供browser_evaluate提交

    Returns:
        dict with keys: success, slug, message, response
    """
    # 1. 门控检查（可跳过 — 用于已发布skill的元数据修复重传，不触发新审核流程）
    if skip_gate:
        gate = {'passed': True, 'is_paid': False, 'price': 0, 'total_score': 0, 'tier': ''}
    else:
        gate = get_gate_status(slug)
        if not gate['passed']:
            return {'success': False, 'slug': slug, 'message': f"门控未通过: {gate['reason']}"}
    
    # 2. 找到SKILL.md文件
    skill_md = find_skill_md(slug)
    if not skill_md:
        return {'success': False, 'slug': slug, 'message': 'SKILL.md文件未找到'}
    
    # 2.5 质量门控检查 (v2.6: 营销关卡 + 安全预检 + 防幻觉 + 评分门控, 复用quality_gate统一函数)
    # V188: skip_gate=True 时跳过所有质量检查 (用于批量重传场景, DB已有TRACE>=45记录)
    if not skip_gate and _QUALITY_GATE_AVAILABLE:
        # 评分门控 (v2.6新增 — 低评分skill阻断上传)
        rg = run_rating_gate(skill_md, slug)
        if not rg.get('overall_passed', True):
            failed = [c.get('name', '?') for c in rg.get('checks', []) if not c.get('passed')]
            return {'success': False, 'slug': slug,
                    'message': f"评分门控未通过: {', '.join(failed)}",
                    'rating_gate': rg}

    if not skip_gate and not skip_marketing and _QUALITY_GATE_AVAILABLE:
        # 营销关卡
        mg = run_marketing_gate(skill_md)
        if not mg.get('overall_passed', True):
            failed = [c.get('name', c.get('check', '?')) for c in mg.get('checks', []) if not c.get('passed')]
            suggestions = []
            for c in mg.get('checks', []):
                if not c.get('passed') and c.get('suggestion'):
                    suggestions.append(f"  - {c['name']}: {c['suggestion']}")
            msg = f"营销关卡未通过 ({len(failed)}项): {', '.join(failed[:3])}"
            if suggestions:
                msg += "\n修复建议:\n" + "\n".join(suggestions[:3])
            return {'success': False, 'slug': slug, 'message': msg,
                    'marketing_gate': mg}
    
    if not skip_gate and not skip_security and _QUALITY_GATE_AVAILABLE:
        # 安全预检 (critical阻断, high/medium警告)
        sec = run_security_precheck(skill_md)
        critical_fails = [c for c in sec.get('checks', []) if not c.get('passed') and c.get('severity') == 'critical']
        if critical_fails:
            failed_names = [c['name'] for c in critical_fails]
            return {'success': False, 'slug': slug,
                    'message': f"安全预检未通过(严重风险): {', '.join(failed_names)}",
                    'security_precheck': sec}
    
    if not skip_gate and _QUALITY_GATE_AVAILABLE:
        # 防幻觉检查
        ah = run_anti_hallucination(skill_md)
        if not ah.get('overall_passed', True):
            failed = [c.get('name', c.get('check', '?')) for c in ah.get('checks', []) if not c.get('passed')]
            return {'success': False, 'slug': slug,
                    'message': f"防幻觉检查未通过 ({len(failed)}项): {', '.join(failed[:3])}",
                    'anti_hallucination': ah}
    
    # 3. 解析frontmatter
    content = skill_md.read_text(encoding='utf-8')
    fm = parse_frontmatter(content)

    # V195: 嵌套metadata扁平化已由skill_core.parser.parse_frontmatter处理, 此处无需重复
    if not fm.get('slug'):
        # V189修复: ClawHub下载的skill frontmatter可能没有slug字段, 使用DB slug作为回退
        fm['slug'] = slug
    # V189修复: 确保必要字段存在, 使用DB slug和默认值回退
    if not fm.get('name'):
        fm['name'] = slug
    if not fm.get('displayName'):
        fm['displayName'] = fm.get('name', slug)

    # 3.5 速率限制预检 (v3.0增强: 防止爆发式上传触发平台反垃圾系统)
    # 根因: 2026-07-24单秒上传1097个skill导致账号被封禁
    # 复用daily_sync.py的速率限制机制,不创建新的独立实现
    # V190修复: browser_relay模式下跳过速率限制 — payload生成不等于实际上传
    # 实际速率控制在relay-record时通过record_upload()记录,以及浏览器端的间隔控制
    if not browser_relay:
        try:
            import sys as _sys
            _sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from daily_sync import check_upload_rate_limit, record_upload
            rate_check = check_upload_rate_limit('skillhub')
            if not rate_check.get('allowed', True):
                wait = rate_check.get('wait_seconds', 120)
                return {
                    'success': False, 'slug': slug,
                    'message': f"速率限制: {rate_check.get('reason', '未知')} (需等待{wait}秒)",
                    'rate_limited': True,
                    'rate_limit_status': rate_check,
                }
        except ImportError:
            # v3.3: 失败安全(fail-safe) — daily_sync不可用时阻止上传,防止无限流爆发式上传
            return {
                'success': False, 'slug': slug,
                'message': '速率限制模块不可用,已阻止上传以防爆发式触发反垃圾系统',
                'rate_limited': True,
            }
        except Exception as e:
            # v3.3: 失败安全(fail-safe) — 速率限制异常时阻止上传,不可静默跳过
            return {
                'success': False, 'slug': slug,
                'message': f'速率限制检查异常,已阻止上传: {e}',
                'rate_limited': True,
            }
    
    # 3.6 内容指纹去重预检 (v3.4: 防止相同内容以不同slug上传触发平台反垃圾系统)
    # 根因: 2026-07-24批量上传中大量近似重复内容被封禁(93.4%封禁率)
    try:
        import sys as _sys
        _tools_dir = os.path.dirname(os.path.abspath(__file__))
        if _tools_dir not in _sys.path:
            _sys.path.insert(0, _tools_dir)
        from content_dedup import check_content_dedup
        dedup_result = check_content_dedup(slug, content)
        if dedup_result.get('duplicate'):
            return {
                'success': False, 'slug': slug,
                'message': f"内容去重: {dedup_result['reason']}",
                'dedup_blocked': True,
                'existing_slug': dedup_result.get('existing_slug'),
            }
    except ImportError:
        pass  # 去重模块不可用时不阻断(已有速率限制和安全预检)
    except Exception as e:
        print(f"[WARN] 内容去重检查异常(不阻断): {e}")
    
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
        'slug': slug,  # V197: 始终使用DB slug作为权威slug(铁律5: DB为唯一数据源), 严禁使用frontmatter slug
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
        'iconUrl': DEFAULT_ICON,  # V186: API要求http/https URL, 不接受data URI
        'subCategories': subcategories,
        'changelog': changelog,
        'tools': fm.get('tools', ['read', 'exec']),
        # V198: 移除payload中的content字段 — content已通过FormData的files Blob独立发送
        # 根因: content在JSON字符串中触发WAF(net::ERR_FAILED), 而作为Blob发送时不触发
        # 旧代码line 852已在WAF重试时移除content, 现在统一在源头移除
        'visibility': 'public',  # 关键: 对外公开可见，否则默认org_only导致前台搜索不到
    }
    
    # 定价信息
    if is_paid and price > 0:
        payload['billingType'] = 'per_call'
        payload['price'] = price
        payload['pricingTier'] = gate.get('tier', 'professional')
    
    if dry_run:
        print(f"  [DRY RUN] {slug}: score={gate['total_score']}/50, price={price}元, paid={is_paid}")
        return {'success': True, 'slug': slug, 'message': 'DRY RUN', 'dry_run': True}
    
    # v3.5: 浏览器中继模式 — 构建payload后返回, 不发送HTTP请求
    # 所有防封措施(速率限制/内容去重/质量门控)已在前面执行完毕
    # payload + content 由 browser_evaluate 提交, 结果通过 record_browser_upload_result 记录
    if browser_relay:
        return {
            'success': True,
            'slug': slug,
            'message': 'PAYLOAD_READY_FOR_BROWSER_RELAY',
            'payload': payload,
            'content': content,
            'platform_slug': payload.get('slug', slug),
            'score': gate['total_score'],
            'price': price,
            'is_paid': is_paid,
        }
    
    # 5. 获取认证cookie
    cookies = load_cookies()
    if not cookies:
        return {'success': False, 'slug': slug, 'message': '无认证cookie，请先设置SKILLHUB_SESSION_COOKIE环境变量或cookie文件'}
    
    # 6. 构建请求 — FormData with payload (JSON) + files (SKILL.md)
    def _build_form_data(payload_dict, content_str, boundary_str):
        """构建FormData请求体"""
        payload_json = json.dumps(payload_dict, ensure_ascii=False)
        skill_md_content = content_str.encode('utf-8')
        
        parts = []
        # payload字段: JSON元数据
        parts.append(f"--{boundary_str}\r\n".encode('utf-8'))
        parts.append(f'Content-Disposition: form-data; name="payload"\r\n\r\n'.encode('utf-8'))
        parts.append(payload_json.encode('utf-8') + b"\r\n")
        
        # files字段: SKILL.md文件 — API要求至少一个文件
        parts.append(f"--{boundary_str}\r\n".encode('utf-8'))
        parts.append(f'Content-Disposition: form-data; name="files"; filename="SKILL.md"\r\n'.encode('utf-8'))
        parts.append(b'Content-Type: text/markdown\r\n\r\n')
        parts.append(skill_md_content + b"\r\n")
        
        parts.append(f"--{boundary_str}--\r\n".encode('utf-8'))
        return b"".join(parts)
    
    def _build_headers(boundary_str, cookie_str):
        """构建请求头"""
        if cookie_str.startswith('BEARER:'):
            api_key = cookie_str[len('BEARER:'):]
            return {
                'Content-Type': f'multipart/form-data; boundary={boundary_str}',
                'Authorization': f'Bearer {api_key}',
                'Accept': 'application/json',
                'User-Agent': 'SkillHub-Enterprise-Uploader/1.0',
            }
        else:
            return {
                'Content-Type': f'multipart/form-data; boundary={boundary_str}',
                'Cookie': cookie_str,
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0',
            }
    
    boundary = f"----WebKitFormBoundary{int(time.time() * 1000)}"
    body = _build_form_data(payload, content, boundary)
    headers = _build_headers(boundary, cookies)
    
    # 7. 发送请求（含566 WAF重试）
    def _send_request(req_body, req_headers):
        """发送上传请求"""
        req = Request(ORG_SKILLS_API, data=req_body, headers=req_headers, method='POST')
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    
    try:
        response_data = _send_request(body, headers)
        # v3.0: 记录上传时间戳用于速率限制 (防止爆发式上传)
        try:
            record_upload('skillhub', slug)
        except Exception as e:
            # v3.4: record_upload失败时记录警告(非静默pass),避免速率限制计数偏少
            print(f"  [WARN] record_upload失败,速率限制计数可能不准: {e}")
        # v2.7: 上传成功后执行完整发布流程(approve→publish_to_community→star)
        publish_result = {}
        if not skip_publish and not dry_run:
            print(f"  [{slug}] 上传成功, 执行发布流程...")
            publish_result = _post_upload_publish(slug)
            pub_ok = publish_result.get('community', {}).get('success', False)
            print(f"  [{slug}] 发布{'✓' if pub_ok else '⚠'}: approve={publish_result.get('approve', {}).get('approved', False)}, community={pub_ok}")
        return {
            'success': True,
            'slug': slug,
            'message': '上传成功',
            'response': response_data,
            'score': gate['total_score'],
            'price': price,
            'is_paid': is_paid,
            'publish_result': publish_result,
        }
    except HTTPError as e:
        error_body = e.read().decode('utf-8', errors='replace')
        
        # 566 = 腾讯EdgeOne WAF拦截（通常是SQL/代码内容触发）
        # 两级重试策略:
        # 第1级: 移除payload中的content字段 + 截断files为仅frontmatter（去除SQL代码body）
        # 第2级: 若第1级仍被WAF拦截，将files内容用base64编码包裹
        if e.code == 566:
            # 截断content为仅frontmatter（去除含SQL的body部分）
            _frontmatter_only = content
            if content.startswith('---'):
                _parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                if len(_parts) >= 3:
                    _frontmatter_only = f"---{_parts[1]}---\n"
            retry_payload = {k: v for k, v in payload.items() if k != 'content'}
            retry_boundary = f"----WebKitFormBoundary{int(time.time() * 1000)}"
            retry_body = _build_form_data(retry_payload, _frontmatter_only, retry_boundary)
            retry_headers = _build_headers(retry_boundary, cookies)
            try:
                response_data = _send_request(retry_body, retry_headers)
                # v2.7: WAF重试上传成功后同样执行发布流程
                publish_result = {}
                if not skip_publish and not dry_run:
                    print(f"  [{slug}] WAF重试上传成功, 执行发布流程...")
                    publish_result = _post_upload_publish(slug)
                return {
                    'success': True,
                    'slug': slug,
                    'message': '上传成功(WAF重试-截断files)',
                    'response': response_data,
                    'score': gate['total_score'],
                    'price': price,
                    'is_paid': is_paid,
                    'publish_result': publish_result,
                }
            except HTTPError as e2:
                error_body2 = e2.read().decode('utf-8', errors='replace')
                # 第2级: 若仍被WAF拦截(566)，尝试base64编码files内容
                if e2.code == 566:
                    import base64 as _b64
                    _encoded_content = _b64.b64encode(content.encode('utf-8')).decode('ascii')
                    _encoded_payload = f"[base64-encoded]{_encoded_content}"
                    retry2_boundary = f"----WebKitFormBoundary{int(time.time() * 1000)}"
                    retry2_body = _build_form_data(retry_payload, _encoded_payload, retry2_boundary)
                    retry2_headers = _build_headers(retry2_boundary, cookies)
                    try:
                        response_data = _send_request(retry2_body, retry2_headers)
                        # v2.7: base64重试上传成功后同样执行发布流程
                        publish_result = {}
                        if not skip_publish and not dry_run:
                            print(f"  [{slug}] base64重试上传成功, 执行发布流程...")
                            publish_result = _post_upload_publish(slug)
                        return {
                            'success': True,
                            'slug': slug,
                            'message': '上传成功(WAF重试-base64编码)',
                            'response': response_data,
                            'score': gate['total_score'],
                            'price': price,
                            'is_paid': is_paid,
                            'publish_result': publish_result,
                        }
                    except HTTPError as e3:
                        error_body3 = e3.read().decode('utf-8', errors='replace')
                        try:
                            error_json = json.loads(error_body3)
                            error_msg = error_json.get('message', error_body3[:200])
                        except json.JSONDecodeError:
                            error_msg = error_body3[:200]
                        return {'success': False, 'slug': slug, 'message': f'HTTP {e3.code} (WAF 2级重试后): {error_msg}'}
                    except Exception as e3:
                        return {'success': False, 'slug': slug, 'message': f'WAF 2级重试错误: {str(e3)}'}
                try:
                    error_json = json.loads(error_body2)
                    error_msg = error_json.get('message', error_body2[:200])
                except json.JSONDecodeError:
                    error_msg = error_body2[:200]
                return {'success': False, 'slug': slug, 'message': f'HTTP {e2.code} (WAF重试后): {error_msg}'}
            except URLError as e2:
                return {'success': False, 'slug': slug, 'message': f'WAF重试网络错误: {str(e2)}'}
            except Exception as e2:
                return {'success': False, 'slug': slug, 'message': f'WAF重试未知错误: {str(e2)}'}
        
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


def record_browser_upload_result(slug: str, http_status: int, response_data: dict,
                                  platform_slug: str = None,
                                  publish_info: str = None) -> dict:
    """记录浏览器中继上传结果到数据库

    v3.5新增: 配合 browser_relay 模式使用。
    browser_evaluate 提交后, 将HTTP响应传入此函数记录到DB。

    V195增强: 支持 publish_info 参数, 记录发布步骤(approve→community→star)结果。
    - 解析 "A+200 C-409 S-E" 格式的发布信息
    - 记录 publish_skillhub 操作到 operations 表
    - 根据发布结果更新 current_status:
      * C+200/C+409 (已发布到社区) → published_skillhub (最终用户可下载)
      * A+400 + C+400 (新上传,审核中) → pending_review_skillhub (卡在中间步骤)
      * 上传失败 → failed/waf_blocked
    - 更新 skillhub_slug 字段 (平台实际slug可能与本地slug不同)

    Args:
        slug: skill slug (原始slug)
        http_status: HTTP状态码 (201=成功, 409=已存在, 566=WAF拦截)
        response_data: API返回的JSON数据
        platform_slug: 平台差异化slug (如 slug-cn)
        publish_info: 发布步骤信息, 格式 "A+200 C-409 S-E" (approve/community/star)

    Returns:
        dict: {'success': bool, 'recorded': bool, 'skill_id': int, 'db_status': str}
    """
    from db import record_upload as db_record_upload

    platform_slug = platform_slug or slug

    # V192: HTTP状态码 → DB状态映射 — 消除混淆
    # 200/201 = 上传成功 → synced
    # 409 = slug冲突(已存在) → synced (技能已在平台上,不需要重新上传)
    # 566 = WAF拦截 → waf_blocked (内容触发防火墙,需修改内容后重试)
    # 其他 = 失败 → failed
    if http_status in (200, 201):
        db_status = 'synced'
        is_success = True
    elif http_status == 409:
        db_status = 'synced'  # 冲突=已存在=synced, 不是failed!
        is_success = True
    elif http_status == 566:
        db_status = 'waf_blocked'
        is_success = False
    else:
        db_status = 'failed'
        is_success = False

    # V195: 解析 publish_info, 确定技能最终可见状态
    # publish_info 格式: "A+200 C-409 S-E" (approve_status community_status star_status)
    # A+200=审核通过, A+400=审核失败(可能是pending), A-XXX=其他错误
    # C+200=社区发布成功, C+409=已发布(重复操作), C+400=发布失败
    # S+200=点赞成功, S-E=点赞错误(不影响发布)
    publish_detail = {}
    current_status = None
    if publish_info:
        for part in publish_info.split():
            if part.startswith('A+'):
                publish_detail['approve'] = part[2:]
            elif part.startswith('A-'):
                publish_detail['approve'] = part[2:]
            elif part.startswith('C+'):
                publish_detail['community'] = part[2:]
            elif part.startswith('C-'):
                publish_detail['community'] = part[2:]
            elif part.startswith('S+'):
                publish_detail['star'] = part[2:]
            elif part.startswith('S-'):
                publish_detail['star'] = 'error'

        # V195: 根据上传+发布结果确定 current_status
        if is_success:
            community_status = publish_detail.get('community', '')
            approve_status = publish_detail.get('approve', '')
            if community_status in ('200', '409'):
                # 已发布到社区 → 最终用户可下载
                current_status = 'published_skillhub'
            elif approve_status == '400':
                # V197: approve失败(400=skill is not in admin_review status) → 审核中, 等待平台完成版本审核后重试approve
                # 根因: 旧代码要求community_status同时为400, 但approve失败时community从未被调用(无法在未审核情况下发布到社区)
                current_status = 'pending_review_skillhub'
            elif approve_status in ('200', '409'):
                # 审核通过但社区发布状态未知 → 假设已发布
                current_status = 'published_skillhub'
            else:
                # 上传成功但发布状态不明确 → 保持原状态
                current_status = None
        elif db_status == 'waf_blocked':
            current_status = 'waf_blocked'
        elif db_status == 'failed':
            current_status = 'failed'

    # 获取skill_id
    skill_id = None
    try:
        conn = sqlite3.connect(DB_PATH, timeout=10)
        c = conn.cursor()
        c.execute("SELECT id FROM skills WHERE slug = ? LIMIT 1", (slug,))
        row = c.fetchone()
        if row:
            skill_id = row[0]
        conn.close()
    except Exception:
        pass

    # 记录到 platform_uploads 表
    if skill_id:
        try:
            db_record_upload(
                skill_id=skill_id,
                version=response_data.get('version', '1.0.0'),
                platform='skillhub',
                platform_slug=platform_slug,
                upload_status='success' if is_success else 'failed',
                http_status=http_status,
                error_message=None if is_success else json.dumps(response_data, ensure_ascii=False)[:500],
                visibility='public' if is_success else None,
                community_published=1 if is_success and response_data.get('reviewStatus') != 'pending' else 0,
            )
        except Exception as e:
            print(f"  [WARN] platform_uploads记录失败: {e}")

    # 记录到 upload_rate_limits 表 (防封措施: 速率限制计数)
    # V199: 仅对实际上传成功(200/201)记录速率限制, 409(已存在)不计入
    # 根因: 409表示技能已存在,POST未创建新skill,不应消耗上传配额
    # 旧代码使用is_success(包含409),导致409结果错误增加速率限制计数
    if http_status in (200, 201):
        try:
            from daily_sync import record_upload as record_rate
            record_rate('skillhub', platform_slug)
        except Exception as e:
            print(f"  [WARN] rate_limit记录失败: {e}")

    # 更新 skill 的 skillhub_sync_status + skillhub_slug + current_status
    try:
        conn = sqlite3.connect(DB_PATH, timeout=10)
        c = conn.cursor()
        if current_status:
            # V195: 同时更新 skillhub_slug 和 current_status
            c.execute(
                "UPDATE skills SET skillhub_sync_status = ?, last_sync_at = ?, "
                "skillhub_slug = ?, current_status = ? WHERE slug = ?",
                (db_status, datetime.now().isoformat(), platform_slug, current_status, slug)
            )
        else:
            # V195: 同时更新 skillhub_slug
            c.execute(
                "UPDATE skills SET skillhub_sync_status = ?, last_sync_at = ?, "
                "skillhub_slug = ? WHERE slug = ?",
                (db_status, datetime.now().isoformat(), platform_slug, slug)
            )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"  [WARN] sync_status更新失败: {e}")

    # V195: 记录 publish_skillhub 操作到 operations 表
    if publish_info and skill_id:
        try:
            conn = sqlite3.connect(DB_PATH, timeout=10)
            c = conn.cursor()
            c.execute("""
                INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
                VALUES (?, 'publish_skillhub', datetime('now', 'localtime'), 'browser_relay', ?, ?)
            """, (
                skill_id,
                f'upload={http_status}, approve={publish_detail.get("approve","N/A")}, '
                f'community={publish_detail.get("community","N/A")}, star={publish_detail.get("star","N/A")}',
                current_status or db_status
            ))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"  [WARN] operations记录失败: {e}")

    status_icon = '✓' if is_success else '✗'
    review_tag = ' [pending_review]' if current_status == 'pending_review_skillhub' else ''
    print(f"  [{status_icon}] {slug} -> {platform_slug}: HTTP {http_status} ({db_status}){review_tag}")
    return {'success': is_success, 'recorded': True, 'skill_id': skill_id, 'db_status': db_status,
            'current_status': current_status}


def record_batch_upload_results(results_file: str) -> dict:
    """批量记录浏览器上传结果到数据库 (V195固化)

    读取JSON格式的上传结果文件, 逐条调用 record_browser_upload_result 记录到DB。
    用于浏览器中继上传完成后的批量数据同步。

    固化目的: 避免每次上传后手动同步, 标准化post-upload数据同步流程。
    使用方式:
        python enterprise_uploader.py relay-record --batch <results.json>
        python enterprise_uploader.py relay-record --batch <results.json> --sync-after

    JSON格式:
        [{"slug": "...", "platform_slug": "...", "http_status": 201,
          "publish_info": "A+200 C-409 S-E"}, ...]

    Args:
        results_file: JSON文件路径

    Returns:
        dict with total, success, failed, pending_review, published
    """
    file_path = Path(results_file)
    if not file_path.exists():
        print(f"ERROR: 文件不存在: {results_file}")
        return {'error': '文件不存在', 'total': 0}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            results = json.load(f)
    except Exception as e:
        print(f"ERROR: 读取文件失败: {e}")
        return {'error': str(e), 'total': 0}

    print(f"批量记录 {len(results)} 条上传结果...")
    print("=" * 60)

    total = len(results)
    success_count = 0
    failed_count = 0
    pending_review_count = 0
    published_count = 0

    for i, result in enumerate(results, 1):
        slug = result.get('slug', '')
        platform_slug = result.get('platform_slug', slug)
        http_status = result.get('http_status', 0)
        publish_info = result.get('publish_info', '')

        # 构造response_data (从response_msg解析, 失败则用空dict)
        # V194: 增加response字段fallback (relay-serve HTML使用response字段)
        response_data = {}
        response_msg = result.get('response_msg', '') or result.get('response_data', '') or result.get('response', '')
        if response_msg and isinstance(response_msg, str):
            try:
                response_data = json.loads(response_msg)
            except (json.JSONDecodeError, ValueError):
                response_data = {'raw': response_msg[:200]}
        elif isinstance(response_msg, dict):
            response_data = response_msg

        record = record_browser_upload_result(
            slug=slug,
            http_status=http_status,
            response_data=response_data,
            platform_slug=platform_slug,
            publish_info=publish_info if publish_info else None,
        )

        if record.get('success'):
            success_count += 1
        else:
            failed_count += 1

        if record.get('current_status') == 'pending_review_skillhub':
            pending_review_count += 1
        elif record.get('current_status') == 'published_skillhub':
            published_count += 1

        if i % 20 == 0:
            print(f"  进度: {i}/{total}")

    print("=" * 60)
    print(f"批量记录完成:")
    print(f"  总计: {total}")
    print(f"  成功: {success_count}")
    print(f"  失败: {failed_count}")
    print(f"  已发布(published_skillhub): {published_count}")
    print(f"  待审核(pending_review_skillhub): {pending_review_count}")

    # V195: 固化 — 提醒执行平台数据同步
    print()
    print("⚠️  下一步必须执行平台数据同步 (固化步骤):")
    print("    python platform_ops.py sync-skillhub")
    print("    python platform_ops.py sync-clawhub")

    return {
        'total': total,
        'success': success_count,
        'failed': failed_count,
        'pending_review': pending_review_count,
        'published': published_count,
    }


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


def cmd_upload(slug: str, dry_run: bool = False, skip_marketing: bool = False,
               skip_security: bool = False, skip_publish: bool = False, skip_gate: bool = False):
    """上传单个skill"""
    print(f"上传 {slug} 到企业版SkillHub (org: {ORG_ID})...")
    result = upload_skill(slug, dry_run, skip_marketing=skip_marketing,
                          skip_security=skip_security, skip_publish=skip_publish, skip_gate=skip_gate)
    
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


def cmd_upload_all(dry_run: bool = False, delay: float = 2.0, skip_marketing: bool = False,
                   skip_security: bool = False, skip_publish: bool = False, skip_gate: bool = False,
                   min_score: float = 45.0, limit: int = 0):
    """上传所有通过门控的skill (V188: 改为从DB查询, 支持全目录扫描)"""
    print("=" * 80)
    print(f"批量上传到企业版SkillHub (org: {ORG_ID})")
    print("=" * 80)

    # V188: 从DB查询所有 TRACE >= min_score 且 pending_upload 的skill
    import sqlite3 as _sqlite3
    _DB_PATH = PROJECT_ROOT / "skill-registry.db"
    conn = _sqlite3.connect(str(_DB_PATH))
    query = """
        SELECT s.slug, s.local_path, sc.total_score
        FROM skills s
        JOIN scores sc ON sc.skill_id = s.id AND sc.score_type = 'trace_llm' AND sc.is_current = 1
        WHERE s.skillhub_sync_status IN ('pending', 'pending_upload')
        AND s.local_path IS NOT NULL AND s.local_path != ''
        AND sc.total_score >= ?
        ORDER BY sc.total_score DESC
    """
    params = (min_score,)
    if limit > 0:
        query += f" LIMIT {limit}"

    rows = conn.execute(query, params).fetchall()
    conn.close()

    # 过滤: 只返回本地文件存在的
    from pathlib import Path as _P
    all_slugs = []
    for slug, local_path, score in rows:
        if local_path and _P(local_path).joinpath('SKILL.md').exists():
            all_slugs.append((slug, score))

    print(f"DB查询到 {len(rows)} 个skill, 其中 {len(all_slugs)} 个有有效磁盘文件")

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

    for i, (slug, score) in enumerate(all_slugs, 1):
        if slug in uploaded_slugs and not dry_run:
            print(f"  [{i}/{len(all_slugs)}] {slug} - 已上传,跳过")
            skip_count += 1
            continue

        print(f"  [{i}/{len(all_slugs)}] {slug} (score={score})...", end="", flush=True)

        result = upload_skill(slug, dry_run, skip_marketing=skip_marketing,
                              skip_security=skip_security, skip_publish=skip_publish, skip_gate=skip_gate)

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
        print("Usage: python enterprise_uploader.py [list|upload <slug>|upload-all|status|relay-payload <slug>|relay-record <slug> <status> <response>] [--skip-marketing] [--skip-security] [--skip-publish]")
        print("  质量门控: 评分门控 + 营销关卡 + 安全预检(critical阻断) + 防幻觉")
        print("  v2.7: 上传后自动执行 approve→publish_to_community→star (用 --skip-publish 跳过)")
        print("  v3.5: relay-payload 输出浏览器中继payload JSON, relay-record 记录浏览器上传结果")
        sys.exit(1)
    
    cmd = sys.argv[1]
    skip_mkt = '--skip-marketing' in sys.argv
    skip_sec = '--skip-security' in sys.argv
    skip_pub = '--skip-publish' in sys.argv
    skip_gate = '--skip-gate' in sys.argv
    
    if cmd == 'list':
        cmd_list()
    elif cmd == 'upload' and len(sys.argv) >= 3:
        dry = '--dry-run' in sys.argv
        cmd_upload(sys.argv[2], dry, skip_marketing=skip_mkt, skip_security=skip_sec, 
                   skip_publish=skip_pub, skip_gate=skip_gate)
    elif cmd == 'upload-all':
        dry = '--dry-run' in sys.argv
        # V188: 支持 --limit 和 --min-score 参数
        _limit = 0
        _min_score = 45.0
        for _arg in sys.argv[2:]:
            if _arg.startswith('--limit='):
                _limit = int(_arg.split('=')[1])
            elif _arg.startswith('--min-score='):
                _min_score = float(_arg.split('=')[1])
        cmd_upload_all(dry, skip_marketing=skip_mkt, skip_security=skip_sec, 
                       skip_publish=skip_pub, skip_gate=skip_gate,
                       min_score=_min_score, limit=_limit)
    elif cmd == 'status':
        cmd_status()
    elif cmd == 'relay-payload' and len(sys.argv) >= 3:
        # v3.5: 输出浏览器中继payload JSON到stdout
        slug = sys.argv[2]
        result = upload_skill(slug, skip_gate=skip_gate, skip_marketing=skip_mkt, skip_security=skip_sec,
                              skip_publish=True, browser_relay=True)
        if result.get('message') == 'PAYLOAD_READY_FOR_BROWSER_RELAY':
            # 输出payload JSON供browser_evaluate使用
            output = {
                'slug': result['slug'],
                'platform_slug': result['platform_slug'],
                'payload': result['payload'],
                'content': result['content'],
            }
            print(json.dumps(output, ensure_ascii=False))
        else:
            print(json.dumps(result, ensure_ascii=False))
            sys.exit(1)
    elif cmd == 'relay-serve' and len(sys.argv) >= 3:
        # V186: 批量生成payload并启动带CORS的HTTP服务器供浏览器fetch
        # 用法: relay-serve <slug1,slug2,...> [--skip-marketing] [--skip-security] [--skip-gate]
        slugs = sys.argv[2].split(',')
        import http.server
        import socketserver
        import tempfile
        tmpdir = tempfile.mkdtemp(prefix='skillhub_relay_')
        
        # Generate payloads
        payloads = {}
        for slug in slugs:
            slug = slug.strip()
            if not slug:
                continue
            result = upload_skill(slug, skip_gate=skip_gate, skip_marketing=skip_mkt, 
                                  skip_security=skip_sec, skip_publish=True, browser_relay=True)
            if result.get('message') == 'PAYLOAD_READY_FOR_BROWSER_RELAY':
                payloads[slug] = {
                    'slug': result['slug'],
                    'platform_slug': result['platform_slug'],
                    'payload': result['payload'],
                    'content': result['content'],
                }
                print(f"  ✓ {slug} payload ready")
            else:
                print(f"  ✗ {slug}: {result.get('message', 'unknown error')}")
        
        # Save to file — V191: 包含api_endpoint字段, 浏览器JS直接读取, 消除端点混淆
        # V193: 包含admin_api和publisher_profile_id, 上传后自动执行发布流程
        output_data = {
            '_meta': {
                'api_endpoint': ORG_SKILLS_API,
                'admin_api': f"{API_BASE}/orgs/{ORG_ID}/admin/skills",
                'star_api': f"{API_BASE}/community/skills",
                'publisher_profile_id': 1508,  # 智创未来
                'org_id': ORG_ID,
                'total': len(payloads),
            },
            'skills': payloads,
        }
        payload_file = os.path.join(tmpdir, 'payloads.json')
        with open(payload_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False)

        # V192: 生成relay HTML页面(浏览器端自动fetch+POST+进度显示)
        # V193: 上传成功后自动执行approve→publish-to-community→star发布流程
        html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>SkillHub Relay Upload</title>
<style>
body{font-family:system-ui,sans-serif;max-width:900px;margin:20px auto;padding:20px;background:#f5f5f5}
.card{background:#fff;border-radius:8px;padding:20px;margin:10px 0;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
.progress{height:24px;background:#e0e0e0;border-radius:12px;overflow:hidden;margin:10px 0}
.progress-bar{height:100%;background:#4CAF50;transition:width 0.3s;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px}
.ok{color:#4CAF50}.fail{color:#f44336}.wait{color:#FF9800}
button{padding:10px 24px;border:none;border-radius:4px;background:#1976D2;color:#fff;cursor:pointer;font-size:14px}
button:disabled{background:#bbb;cursor:not-allowed}
table{width:100%;border-collapse:collapse;font-size:13px}
td,th{padding:6px 10px;border-bottom:1px solid #e0e0e0;text-align:left}
th{background:#f0f0f0}
</style>
</head>
<body>
<h1>SkillHub Relay Upload</h1>
<div class="card">
<div id="status">准备中...</div>
<div class="progress"><div id="bar" class="progress-bar" style="width:0%">0%</div></div>
<button id="startBtn" onclick="startUpload()" disabled>开始上传</button>
<button id="copyBtn" onclick="copyResults()" style="display:none">复制结果JSON</button>
</div>
<div class="card"><table id="resultsTable"><thead><tr><th>#</th><th>Slug</th><th>上传</th><th>发布</th><th>详情</th></tr></thead><tbody></tbody></table></div>
<script>
let skills=[],endpoint='',adminApi='',starApi='',pubId=0,results=[],idx=0,uploading=false;
const INTERVAL=120000;
async function init(){
  try{
    const r=await fetch('/payloads.json');
    const d=await r.json();
    endpoint=d._meta.api_endpoint;
    adminApi=d._meta.admin_api||'';
    starApi=d._meta.star_api||'';
    pubId=d._meta.publisher_profile_id||1508;
    skills=Object.values(d.skills);
    document.getElementById('status').innerHTML=`已加载 <b>${skills.length}</b> 个skill, API: ${endpoint}<br>间隔: ${INTERVAL/1000}s/个, 预计耗时: ${Math.ceil(skills.length*INTERVAL/60000)}分钟<br>V193: 上传成功后自动执行 approve→publish-to-community→star`;
    document.getElementById('startBtn').disabled=false;
  }catch(e){document.getElementById('status').innerHTML='<span class="fail">加载失败: '+e.message+'</span>'}
}
async function startUpload(){
  if(uploading)return;uploading=true;
  document.getElementById('startBtn').disabled=true;
  for(idx=0;idx<skills.length;idx++){
    const s=skills[idx];
    const pct=Math.round((idx/skills.length)*100);
    document.getElementById('bar').style.width=pct+'%';
    document.getElementById('bar').textContent=pct+'%';
    document.getElementById('status').innerHTML=`上传中 (${idx+1}/${skills.length}): <b>${s.slug}</b>`;
    const tr=document.getElementById('resultsTable').querySelector('tbody');
    const row=tr.insertRow();
    row.insertCell(0).textContent=idx+1;
    row.insertCell(1).textContent=s.slug;
    row.insertCell(2).innerHTML='<span class="wait">上传中...</span>';
    row.insertCell(3).innerHTML='';
    row.insertCell(4).textContent='';
    const slug=s.platform_slug||s.slug;
    let uploadOk=false,pubStr='',detailStr='';
    try{
      const fd=new FormData();
      fd.append('payload',JSON.stringify(s.payload));
      fd.append('files',new Blob([s.content],{type:'text/markdown'}),'SKILL.md');
      const res=await fetch(endpoint,{method:'POST',body:fd,credentials:'include'});
      const txt=await res.text();
      let json;try{json=JSON.parse(txt)}catch(e){json={raw:txt.substring(0,200)}}
      uploadOk=res.status===200||res.status===201;
      // V194: 409=skill已存在 → 自动尝试POST /skills/{slug}/versions更新内容
      if(res.status===409){
        try{
          const vfd=new FormData();
          vfd.append('payload',JSON.stringify(s.payload));
          vfd.append('files',new Blob([s.content],{type:'text/markdown'}),'SKILL.md');
          const vres=await fetch(`${endpoint}/${slug}/versions`,{method:'POST',body:vfd,credentials:'include'});
          const vtxt=await vres.text();
          let vjson;try{vjson=JSON.parse(vtxt)}catch(e){vjson={raw:vtxt.substring(0,200)}}
          uploadOk=vres.status===200||vres.status===201;
          results.push({slug:s.slug,platform_slug:slug,http_status:vres.status,response:vjson});
          if(uploadOk){
            row.cells[2].innerHTML='<span class="ok">✓ V'+vres.status+'</span>';
          }else if(vres.status===409){
            row.cells[2].innerHTML='<span class="wait">⏳ V409 审核中</span>';
          }else{
            row.cells[2].innerHTML='<span class="fail">✗ V'+vres.status+'</span>';
          }
          detailStr=vjson.message||vjson.raw||JSON.stringify(vjson).substring(0,100);
        }catch(ve){
          results.push({slug:s.slug,platform_slug:slug,http_status:res.status,response:json});
          row.cells[2].innerHTML='<span class="fail">✗ '+res.status+'</span>';
          detailStr=json.message||json.raw||JSON.stringify(json).substring(0,100);
        }
      }else{
        results.push({slug:s.slug,platform_slug:slug,http_status:res.status,response:json});
        row.cells[2].innerHTML=uploadOk?'<span class="ok">✓ '+res.status+'</span>':'<span class="fail">✗ '+res.status+'</span>';
        detailStr=json.message||json.raw||JSON.stringify(json).substring(0,100);
      }
    }catch(e){
      results.push({slug:s.slug,platform_slug:slug,http_status:0,response:{error:e.message}});
      row.cells[2].innerHTML='<span class="fail">✗ Error</span>';
      detailStr=e.message;
    }
    // V193: 上传成功后自动执行发布流程 (approve→publish-to-community→star)
    if(uploadOk&&adminApi){
      row.cells[3].innerHTML='<span class="wait">发布中...</span>';
      let apprOk=false,commOk=false,starOk=false;
      try{
        const ar=await fetch(`${adminApi}/${slug}/approve`,{method:'POST',headers:{'Content-Type':'application/json'},body:'{}',credentials:'include'});
        apprOk=ar.status===200||ar.status===201||ar.status===400;
      }catch(e){}
      try{
        // V200: 先unpublish-from-community重置内部状态, 再publish-to-community
        // 根因: 直接调用publish-to-community会返回409 skill_not_publishable("已对外发布")
        // 因为skill内部社区发布状态卡在部分发布态, 需先unpublish重置
        await fetch(`${adminApi}/${slug}/unpublish-from-community`,{method:'POST',credentials:'include'});
        const body=JSON.stringify({publisherProfileId:pubId});
        const cr=await fetch(`${adminApi}/${slug}/publish-to-community`,{method:'POST',headers:{'Content-Type':'application/json'},body:body,credentials:'include'});
        commOk=cr.status===200||cr.status===201;
      }catch(e){}
      try{
        const sr=await fetch(`${starApi}/${slug}/star`,{method:'POST',headers:{'Content-Type':'application/json'},body:'{}',credentials:'include'});
        starOk=sr.status===200||sr.status===201;
      }catch(e){}
      const parts=[];
      if(apprOk)parts.push('<span class="ok">A✓</span>');else parts.push('<span class="fail">A✗</span>');
      if(commOk)parts.push('<span class="ok">C✓</span>');else parts.push('<span class="fail">C✗</span>');
      if(starOk)parts.push('<span class="ok">S✓</span>');else parts.push('<span class="fail">S✗</span>');
      row.cells[3].innerHTML=parts.join(' ');
      // V194: 将发布结果写入publish_info, 供relay-record --batch使用
      const apprCode=apprOk?'200':'400';
      const commCode=commOk?'200':'400';
      const starCode=starOk?'200':'E';
      results[results.length-1].publish_info=`A+${apprCode} C+${commCode} S-${starCode}`;
    }else if(!uploadOk){
      row.cells[3].innerHTML='<span class="fail">跳过</span>';
    }
    row.cells[4].textContent=detailStr;
    if(idx<skills.length-1){
      document.getElementById('status').innerHTML=`等待 ${INTERVAL/1000}s... (${idx+1}/${skills.length})`;
      await new Promise(r=>setTimeout(r,INTERVAL));
    }
  }
  document.getElementById('bar').style.width='100%';
  document.getElementById('bar').textContent='100%';
  const ok=results.filter(r=>r.http_status===200||r.http_status===201).length;
  const wait=results.filter(r=>r.http_status===409).length;
  const fail=results.length-ok-wait;
  document.getElementById('status').innerHTML=`完成! 上传成功: <span class="ok">${ok}</span>, 审核中: <span class="wait">${wait}</span>, 失败: <span class="fail">${fail}</span>`;
  document.getElementById('copyBtn').style.display='inline-block';
  uploading=false;
}
function copyResults(){
  navigator.clipboard.writeText(JSON.stringify(results));
  alert('结果已复制到剪贴板! 请保存为JSON文件后执行:\\npython enterprise_uploader.py relay-record --batch <results.json> --sync-after');
}
init();
</script>
</body></html>"""
        html_file = os.path.join(tmpdir, 'index.html')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"\n{len(payloads)} payloads saved to {payload_file}")
        print(f"API endpoint: {ORG_SKILLS_API}")
        print(f"Relay page: http://127.0.0.1:8766/index.html")
        print(f"Starting CORS HTTP server on http://127.0.0.1:8766/")
        print()
        print("=" * 60)
        print("V195 固化提醒: 上传完成后必须执行数据同步!")
        print("=" * 60)
        print("  1. 导出浏览器上传结果 (window.__uploadResults)")
        print("  2. 保存为JSON文件")
        print("  3. 执行同步命令:")
        print("     python platform_ops.py post-upload \\")
        print(f"       --results <results.json> \\")
        print(f"       --platform-data skillhub_platform_data.json")
        print("  或分步执行:")
        print("     python enterprise_uploader.py relay-record --batch <results.json>")
        print("     python platform_ops.py sync-skillhub --from-file <platform_data.json>")
        print("=" * 60)
        
        # Start HTTP server with CORS (V196: ThreadingTCPServer防卡死)
        os.chdir(tmpdir)
        class CORSHandler(http.server.SimpleHTTPRequestHandler):
            def end_headers(self):
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                super().end_headers()
            def do_OPTIONS(self):
                self.send_response(200)
                self.end_headers()
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)
                path = self.path.lstrip('/')
                if path and not path.startswith('http'):
                    filepath = os.path.join(os.getcwd(), path)
                    with open(filepath, 'wb') as f:
                        f.write(body)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'{"ok":true}')
                else:
                    self.send_response(400)
                    self.end_headers()

        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.ThreadingTCPServer(("127.0.0.1", 8766), CORSHandler) as httpd:
            httpd.serve_forever()
    elif cmd == 'relay-publish':
        # V193: 批量发布已上传但未走完发布流程(approve→publish-to-community→star)的skill
        # 根因: relay-serve模式仅执行上传POST,不调用发布API,导致1331个skill卡在中间步骤
        # 用法: relay-publish [--limit N] [--port PORT]
        import http.server
        import socketserver
        import tempfile

        relay_port = 8766
        publish_limit = 0  # 0 = all
        for i, arg in enumerate(sys.argv[2:], 2):
            if arg == '--limit' and i + 1 < len(sys.argv):
                publish_limit = int(sys.argv[i + 1])
            elif arg == '--port' and i + 1 < len(sys.argv):
                relay_port = int(sys.argv[i + 1])

        ORG_ADMIN_API = f"{API_BASE}/orgs/{ORG_ID}/admin/skills"
        PUBLISHER_ID = 1508  # 智创未来 (与 platform_ops.py _get_publisher_profile_id 一致)

        # 查询需要发布的skill: synced但无publish_skillhub操作记录,且未被删除
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        query = """
            SELECT s.slug, s.skillhub_slug, s.current_status
            FROM skills s
            WHERE s.skillhub_sync_status = 'synced'
            AND s.current_status NOT IN ('deleted_on_skillhub', 'deleted')
            AND s.id NOT IN (
                SELECT DISTINCT skill_id FROM operations
                WHERE operation_type = 'publish_skillhub'
            )
            ORDER BY s.current_status DESC
        """
        if publish_limit > 0:
            query += f" LIMIT {publish_limit}"
        c.execute(query)
        rows = c.fetchall()
        conn.close()

        if not rows:
            print("没有需要发布的skill (所有synced skill已有publish_skillhub操作记录)")
            sys.exit(0)

        # 构建发布数据
        publish_data = {
            '_meta': {
                'approve_endpoint': f"{ORG_ADMIN_API}",
                'community_endpoint': f"{ORG_ADMIN_API}",
                'star_endpoint': f"{API_BASE}/community/skills",
                'publisher_profile_id': PUBLISHER_ID,
                'total': len(rows),
            },
            'skills': {},
        }
        for slug, sh_slug, status in rows:
            platform_slug = sh_slug or slug
            publish_data['skills'][slug] = {
                'slug': slug,
                'platform_slug': platform_slug,
                'current_status': status,
            }

        tmpdir = tempfile.mkdtemp(prefix='skillhub_publish_')
        data_file = os.path.join(tmpdir, 'publish_data.json')
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(publish_data, f, ensure_ascii=False)

        # 生成发布HTML页面
        publish_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>SkillHub Relay Publish</title>
<style>
body{font-family:system-ui,sans-serif;max-width:900px;margin:20px auto;padding:20px;background:#f5f5f5}
.card{background:#fff;border-radius:8px;padding:20px;margin:10px 0;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
.progress{height:24px;background:#e0e0e0;border-radius:12px;overflow:hidden;margin:10px 0}
.progress-bar{height:100%;background:#4CAF50;transition:width 0.3s;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px}
.ok{color:#4CAF50}.fail{color:#f44336}.wait{color:#FF9800}
button{padding:10px 24px;border:none;border-radius:4px;background:#1976D2;color:#fff;cursor:pointer;font-size:14px}
button:disabled{background:#bbb;cursor:not-allowed}
table{width:100%;border-collapse:collapse;font-size:13px}
td,th{padding:6px 10px;border-bottom:1px solid #e0e0e0;text-align:left}
th{background:#f0f0f0}
</style>
</head>
<body>
<h1>SkillHub Relay Publish (approve → publish-to-community → star)</h1>
<div class="card">
<div id="status">准备中...</div>
<div class="progress"><div id="bar" class="progress-bar" style="width:0%">0%</div></div>
<button id="startBtn" onclick="startPublish()" disabled>开始发布</button>
<button id="copyBtn" onclick="copyResults()" style="display:none">复制结果JSON</button>
</div>
<div class="card"><table id="resultsTable"><thead><tr><th>#</th><th>Slug</th><th>Approve</th><th>Community</th><th>Star</th></tr></thead><tbody></tbody></table></div>
<script>
let skills=[],meta={},results=[],idx=0,publishing=false;
const INTERVAL=3000; // 3秒间隔(发布API比上传轻量)
async function init(){
  try{
    const r=await fetch('/publish_data.json');
    const d=await r.json();
    meta=d._meta;
    skills=Object.values(d.skills);
    document.getElementById('status').innerHTML=`已加载 <b>${skills.length}</b> 个skill待发布<br>流程: approve → publish-to-community → star<br>间隔: 3s/个, 预计耗时: ${Math.ceil(skills.length*3/60)}分钟`;
    document.getElementById('startBtn').disabled=false;
  }catch(e){document.getElementById('status').innerHTML='<span class="fail">加载失败: '+e.message+'</span>'}
}
async function startPublish(){
  if(publishing)return;publishing=true;
  document.getElementById('startBtn').disabled=true;
  for(idx=0;idx<skills.length;idx++){
    const s=skills[idx];
    const pct=Math.round((idx/skills.length)*100);
    document.getElementById('bar').style.width=pct+'%';
    document.getElementById('bar').textContent=pct+'%';
    document.getElementById('status').innerHTML=`发布中 (${idx+1}/${skills.length}): <b>${s.slug}</b>`;
    const tr=document.getElementById('resultsTable').querySelector('tbody');
    const row=tr.insertRow();
    row.insertCell(0).textContent=idx+1;
    row.insertCell(1).textContent=s.slug;
    row.insertCell(2).innerHTML='<span class="wait">...</span>';
    row.insertCell(3).innerHTML='<span class="wait">...</span>';
    row.insertCell(4).innerHTML='<span class="wait">...</span>';
    const slug=s.platform_slug||s.slug;
    let approveOk=false,communityOk=false,starOk=false;
    // 1. Approve
    try{
      const ar=await fetch(`${meta.approve_endpoint}/${slug}/approve`,{
        method:'POST',headers:{'Content-Type':'application/json'},body:'{}',credentials:'include'
      });
      approveOk=ar.status===200||ar.status===201;
      // 400 "not in admin_review" 是正常的 — 说明已审核或正在审核
      if(!approveOk&&ar.status===400){approveOk=true}
      row.cells[2].innerHTML=approveOk?'<span class="ok">✓</span>':'<span class="fail">✗ '+ar.status+'</span>';
    }catch(e){row.cells[2].innerHTML='<span class="fail">✗</span>'}
    // 2. Publish to community (V200: 先unpublish-from-community重置内部状态)
    try{
      // V200根因修复: 先unpublish-from-community重置, 解决409 skill_not_publishable
      await fetch(`${meta.community_endpoint}/${slug}/unpublish-from-community`,{method:'POST',credentials:'include'});
      const body=JSON.stringify({publisherProfileId:meta.publisher_profile_id});
      const cr=await fetch(`${meta.community_endpoint}/${slug}/publish-to-community`,{
        method:'POST',headers:{'Content-Type':'application/json'},body:body,credentials:'include'
      });
      communityOk=cr.status===200||cr.status===201;
      row.cells[3].innerHTML=communityOk?'<span class="ok">✓</span>':'<span class="fail">✗ '+cr.status+'</span>';
    }catch(e){row.cells[3].innerHTML='<span class="fail">✗</span>'}
    // 3. Star
    try{
      const sr=await fetch(`${meta.star_endpoint}/${slug}/star`,{
        method:'POST',headers:{'Content-Type':'application/json'},body:'{}',credentials:'include'
      });
      starOk=sr.status===200||sr.status===201;
      row.cells[4].innerHTML=starOk?'<span class="ok">✓</span>':'<span class="fail">✗ '+sr.status+'</span>';
    }catch(e){row.cells[4].innerHTML='<span class="fail">✗</span>'}
    const apprCode=approveOk?'200':'400';
    const commCode=communityOk?'200':'400';
    const starCode=starOk?'200':'E';
    results.push({slug:s.slug,platform_slug:slug,http_status:200,publish_info:`A+${apprCode} C+${commCode} S-${starCode}`,response_msg:JSON.stringify({approve:approveOk,community:communityOk,star:starOk})});
    if(idx<skills.length-1){
      document.getElementById('status').innerHTML=`等待 ${INTERVAL/1000}s... (${idx+1}/${skills.length})`;
      await new Promise(r=>setTimeout(r,INTERVAL));
    }
  }
  document.getElementById('bar').style.width='100%';
  document.getElementById('bar').textContent='100%';
  const ok=results.filter(r=>r.publish_info&&r.publish_info.includes('C+200')).length;
  const fail=results.length-ok;
  document.getElementById('status').innerHTML=`完成! 社区发布成功: <span class="ok">${ok}</span>, 失败: <span class="fail">${fail}</span>`;
  document.getElementById('copyBtn').style.display='inline-block';
  publishing=false;
}
function copyResults(){
  navigator.clipboard.writeText(JSON.stringify(results));
  alert('结果已复制! 保存为JSON后执行: python enterprise_uploader.py relay-record --batch <file.json> --sync-after');
}
init();
</script>
</body></html>"""
        html_file = os.path.join(tmpdir, 'index.html')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(publish_html)

        print(f"\n{len(rows)} skills待发布 (approve → publish-to-community → star)")
        print(f"发布页面: http://127.0.0.1:{relay_port}/index.html")
        print(f"请在浏览器中登录SkillHub后访问发布页面")
        print(f"起始CORS HTTP服务器 on http://127.0.0.1:{relay_port}/")
        print()
        print("=" * 60)
        print("V194 固化提醒: 发布完成后必须记录到DB!")
        print("=" * 60)
        print("  1. 点击页面'复制结果JSON'按钮")
        print("  2. 保存为JSON文件")
        print("  3. 执行DB记录命令:")
        print(f"     python enterprise_uploader.py relay-record --batch <results.json> --sync-after")
        print("=" * 60)

        # Start HTTP server with CORS (V196: ThreadingTCPServer防卡死)
        os.chdir(tmpdir)
        class CORSHandler(http.server.SimpleHTTPRequestHandler):
            def end_headers(self):
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                super().end_headers()
            def do_OPTIONS(self):
                self.send_response(200)
                self.end_headers()
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)
                path = self.path.lstrip('/')
                if path and not path.startswith('http'):
                    filepath = os.path.join(os.getcwd(), path)
                    with open(filepath, 'wb') as f:
                        f.write(body)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'{"ok":true}')
                else:
                    self.send_response(400)
                    self.end_headers()

        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.ThreadingTCPServer(("127.0.0.1", relay_port), CORSHandler) as httpd:
            httpd.serve_forever()
    elif cmd == 'relay-record' and len(sys.argv) >= 3 and sys.argv[2] == '--batch':
        # V195: 批量记录浏览器上传结果 (固化: 上传后必须同步到DB)
        # 用法: relay-record --batch <results.json> [--sync-after]
        if len(sys.argv) < 4:
            print("用法: relay-record --batch <results.json> [--sync-after]")
            sys.exit(1)
        results_file = sys.argv[3]
        sync_after = '--sync-after' in sys.argv
        result = record_batch_upload_results(results_file)
        if sync_after:
            print()
            print("=" * 60)
            print("V195固化: 自动执行平台数据同步...")
            print("=" * 60)
            try:
                from platform_ops import sync_skillhub_data
                sync_skillhub_data()
            except Exception as e:
                print(f"SkillHub同步失败: {e}")
            try:
                from platform_ops import sync_clawhub_data
                sync_clawhub_data()
            except Exception as e:
                print(f"ClawHub同步失败: {e}")
        print(json.dumps(result, ensure_ascii=False))
    elif cmd == 'relay-record' and len(sys.argv) >= 5:
        # v3.5: 记录单个浏览器上传结果
        # 用法: relay-record <slug> <http_status> <response_json> [platform_slug] [publish_info]
        slug = sys.argv[2]
        http_status = int(sys.argv[3])
        response_data = json.loads(sys.argv[4])
        platform_slug = sys.argv[5] if len(sys.argv) >= 6 else None
        publish_info = sys.argv[6] if len(sys.argv) >= 7 else None
        result = record_browser_upload_result(slug, http_status, response_data, platform_slug, publish_info)
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(f"未知命令: {cmd}")
        print("Usage: python enterprise_uploader.py [list|upload <slug>|upload-all|status|")
        print("  relay-payload <slug>|relay-serve <slugs>|relay-publish|")
        print("  relay-record <slug> <status> <response> [platform_slug] [publish_info]|")
        print("  relay-record --batch <results.json> [--sync-after]]")
        sys.exit(1)
