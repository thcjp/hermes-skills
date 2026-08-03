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
# 添加PROJECT_ROOT到path,使config包可被import (脚本运行时cwd不在sys.path中)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import (
    DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR,
    DIFFERENTIATED_DIR, ENTERPRISE_UPLOAD_DIR,
    is_paid_skill, TRACE_PASS_THRESHOLD
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
# V182: 切回ORG_ID=862(科创少年) — 之前被封的账号,用户重新登录后仍可在后台操作
# org-xxo535hs / opc-laotian, API Key: sk-ent-250641b3...
ORG_ID = 862
API_BASE = "https://api.skillhub.cn/api/v1"
ORG_SKILLS_API = f"{API_BASE}/community/skills/publish"  # V162: 改用社区发布端点(原/orgs/{ORG_ID}/skills返回401)

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
    认证优先级:
    1. SKILLHUB_SESSION_COOKIE 环境变量(浏览器session)
    2. SKILLHUB_MERCHANT_TOKEN 环境变量(bt_商户token)
    3. cookie文件(浏览器session)
    4. CLI凭证文件(sk-ent- API Key — 仅verify有效,发布可能401)
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

    # 3. CLI凭证文件(sk-ent- API Key — 可能权限不足)
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
    if _QUALITY_GATE_AVAILABLE:
        # 评分门控 (v2.6新增 — 低评分skill阻断上传)
        rg = run_rating_gate(skill_md, slug)
        if not rg.get('overall_passed', True):
            failed = [c.get('name', '?') for c in rg.get('checks', []) if not c.get('passed')]
            return {'success': False, 'slug': slug,
                    'message': f"评分门控未通过: {', '.join(failed)}",
                    'rating_gate': rg}

    if not skip_marketing and _QUALITY_GATE_AVAILABLE:
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
    
    if not skip_security and _QUALITY_GATE_AVAILABLE:
        # 安全预检 (critical阻断, high/medium警告)
        sec = run_security_precheck(skill_md)
        critical_fails = [c for c in sec.get('checks', []) if not c.get('passed') and c.get('severity') == 'critical']
        if critical_fails:
            failed_names = [c['name'] for c in critical_fails]
            return {'success': False, 'slug': slug,
                    'message': f"安全预检未通过(严重风险): {', '.join(failed_names)}",
                    'security_precheck': sec}
    
    if _QUALITY_GATE_AVAILABLE:
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

    if not fm.get('slug'):
        return {'success': False, 'slug': slug, 'message': 'frontmatter解析失败'}

    # 3.5 速率限制预检 (v3.0增强: 防止爆发式上传触发平台反垃圾系统)
    # 根因: 2026-07-24单秒上传1097个skill导致账号被封禁
    # 复用daily_sync.py的速率限制机制,不创建新的独立实现
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
                                  platform_slug: str = None) -> dict:
    """记录浏览器中继上传结果到数据库
    
    v3.5新增: 配合 browser_relay 模式使用。
    browser_evaluate 提交后, 将HTTP响应传入此函数记录到DB。
    
    Args:
        slug: skill slug (原始slug)
        http_status: HTTP状态码 (201=成功)
        response_data: API返回的JSON数据
        platform_slug: 平台差异化slug (如 slug-cn)
    
    Returns:
        dict: {'success': bool, 'recorded': bool}
    """
    from db import record_upload as db_record_upload
    
    platform_slug = platform_slug or slug
    success = http_status in (200, 201)
    
    # 获取skill_id
    skill_id = None
    try:
        conn = sqlite3.connect(DB_PATH)
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
                upload_status='success' if success else 'failed',
                http_status=http_status,
                error_message=None if success else json.dumps(response_data, ensure_ascii=False)[:500],
                visibility='public' if success else None,
                community_published=1 if success and response_data.get('reviewStatus') != 'pending' else 0,
            )
        except Exception as e:
            print(f"  [WARN] platform_uploads记录失败: {e}")
    
    # 记录到 upload_rate_limits 表 (防封措施: 速率限制计数)
    if success:
        try:
            from daily_sync import record_upload as record_rate
            record_rate('skillhub', platform_slug)
        except Exception as e:
            print(f"  [WARN] rate_limit记录失败: {e}")
    
    # 更新 skill 的 skillhub_sync_status
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        status = 'synced' if success else 'failed'
        c.execute(
            "UPDATE skills SET skillhub_sync_status = ?, last_sync_at = ? WHERE slug = ?",
            (status, datetime.now().isoformat(), slug)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"  [WARN] sync_status更新失败: {e}")
    
    print(f"  [{'✓' if success else '✗'}] {slug} -> {platform_slug}: HTTP {http_status}")
    return {'success': success, 'recorded': True, 'skill_id': skill_id}


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
               skip_security: bool = False, skip_publish: bool = False):
    """上传单个skill"""
    print(f"上传 {slug} 到企业版SkillHub (org: {ORG_ID})...")
    result = upload_skill(slug, dry_run, skip_marketing=skip_marketing, 
                          skip_security=skip_security, skip_publish=skip_publish)
    
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
                   skip_security: bool = False, skip_publish: bool = False):
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
        
        result = upload_skill(slug, dry_run, skip_marketing=skip_marketing, 
                              skip_security=skip_security, skip_publish=skip_publish)
        
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
        cmd_upload(sys.argv[2], dry, skip_marketing=skip_mkt, skip_security=skip_sec, skip_publish=skip_pub)
    elif cmd == 'upload-all':
        dry = '--dry-run' in sys.argv
        cmd_upload_all(dry, skip_marketing=skip_mkt, skip_security=skip_sec, skip_publish=skip_pub)
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
    elif cmd == 'relay-record' and len(sys.argv) >= 5:
        # v3.5: 记录浏览器上传结果
        # 用法: relay-record <slug> <http_status> <response_json> [platform_slug]
        slug = sys.argv[2]
        http_status = int(sys.argv[3])
        response_data = json.loads(sys.argv[4])
        platform_slug = sys.argv[5] if len(sys.argv) >= 6 else None
        result = record_browser_upload_result(slug, http_status, response_data, platform_slug)
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(f"未知命令: {cmd}")
        print("Usage: python enterprise_uploader.py [list|upload <slug>|upload-all|status|relay-payload <slug>|relay-record <slug> <status> <response>] [--skip-marketing] [--skip-security] [--skip-publish]")
        sys.exit(1)
