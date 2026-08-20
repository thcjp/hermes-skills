#!/usr/bin/env python3
"""
平台运营操作工具 (platform_ops.py)
==================================
被 enterprise_uploader.py 和 daily_sync.py 引用的管道组件。
负责上传后的发布流程(approve→publish→star)和封禁检测。

使用方式:
    python platform_ops.py check-banned          # 检查封禁技能
    python platform_ops.py publish <slug>         # 执行发布流程
    python platform_ops.py status                 # 查看平台状态
"""

import json
import os
import sys
import sqlite3
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config"))

from config import DB_PATH, REPORT_DIR

# 企业版配置 (与 enterprise_uploader.py 一致)
ORG_ID = 1436
API_BASE = "https://api.skillhub.cn/api/v1"
CLAWHUB_REGISTRY = "https://clawhub.ai"  # V193: 与 clawhub_batch_uploader.py 一致, inspect命令必须传此参数

# V191: SkillHub API端点完整说明 — 消除所有端点混淆
# ┌────────────────────────────────────────────────────────────────────┐
# │ 端点                                 │ 方法  │ 用途               │
# ├──────────────────────────────────────┼───────┼────────────────────┤
# │ /orgs/{ORG_ID}/skills                │ POST  │ 上传skill (无200限制)│
# │ /orgs/{ORG_ID}/skills                │ GET   │ 列出skill (简略)    │
# │ /orgs/{ORG_ID}/admin/skills          │ GET   │ 列出skill (详细)    │
# │ /orgs/{ORG_ID}/admin/skills/{slug}/approve │ POST │ 审核通过       │
# │ /orgs/{ORG_ID}/admin/skills/{slug}/publish-to-community │ POST │ 发布到社区│
# │ /community/skills/{slug}/star        │ POST  │ 点赞               │
# │ /community/skills/publish            │ POST  │ ❌ 已废弃! 有200限制 │
# └────────────────────────────────────────────────────────────────────┘
ORG_SKILLS_UPLOAD_API = f"{API_BASE}/orgs/{ORG_ID}/skills"  # 上传端点
ORG_ADMIN_SKILLS_API = f"{API_BASE}/orgs/{ORG_ID}/admin/skills"  # 管理端点 (GET列表/approve/publish)
COMMUNITY_PUBLISH_API = f"{API_BASE}/community/skills/publish"  # ❌ V191废弃: 有200社区限制, 禁用于上传

# V186: publisherProfileId — 从API动态获取,有缓存
_PUBLISHER_PROFILE_ID = None

def _get_publisher_profile_id():
    """从SkillHub API获取publisher profile ID (智创未来=1508)"""
    global _PUBLISHER_PROFILE_ID
    if _PUBLISHER_PROFILE_ID:
        return _PUBLISHER_PROFILE_ID
    try:
        auth = _load_auth()
        if not auth:
            return None
        url = f"{API_BASE}/orgs/{ORG_ID}/admin/publisher-profiles"
        headers = {'Accept': 'application/json'}
        if auth.startswith('BEARER:'):
            headers['Authorization'] = f'Bearer {auth[7:]}'
        else:
            headers['Cookie'] = auth
        req = Request(url, headers=headers, method='GET')
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            profiles = data.get('profiles', [])
            for p in profiles:
                if p.get('auditStatus') == 'passed':
                    _PUBLISHER_PROFILE_ID = p.get('id')
                    return _PUBLISHER_PROFILE_ID
    except Exception as e:
        print(f"[WARN] 获取publisherProfileId失败: {e}")
    return None

# 认证 (与 enterprise_uploader.py load_cookies 一致)
COOKIE_FILE = Path(os.environ.get(
    'SKILLHUB_COOKIE_FILE',
    os.path.join(os.path.expanduser('~'), '.skillhub_cookies.txt')
))


def _load_auth():
    """加载认证信息 (与 enterprise_uploader.py load_cookies 一致)

    V196: 增加项目凭证文件(.skillhub-credentials/api-key.txt)作为认证源,
    消除对浏览器session cookie的依赖, 解决API 401问题。
    认证优先级:
    1. SKILLHUB_SESSION_COOKIE 环境变量(浏览器session)
    2. SKILLHUB_MERCHANT_TOKEN 环境变量(bt_商户token)
    3. Cookie文件(浏览器session)
    4. 项目凭证文件(.skillhub-credentials/api-key.txt) — V196新增
    5. CLI凭证文件(sk-ent- API Key)
    """
    # 1. 环境变量(最高优先级 — 允许运行时覆盖过期凭证)
    env_cookies = os.environ.get('SKILLHUB_SESSION_COOKIE', '')
    if env_cookies:
        return env_cookies

    # 1.5 bt_商户token (V182/V196)
    env_merchant = os.environ.get('SKILLHUB_MERCHANT_TOKEN', '')
    if env_merchant:
        return f'BEARER:{env_merchant}'

    # 2. Cookie文件(浏览器session)
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
        except Exception:
            pass

    # 4. CLI凭证文件(sk-ent- API Key — 可能权限不足)
    cli_creds = Path(os.path.expanduser('~')) / '.skillhub' / 'credentials.json'
    if cli_creds.exists():
        try:
            creds = json.loads(cli_creds.read_text(encoding='utf-8'))
            orgs = creds.get('orgs', {})
            for org_id, org_data in orgs.items():
                if org_data.get('orgId') == ORG_ID:
                    api_key = org_data.get('apiKey', '')
                    if api_key:
                        return f'BEARER:{api_key}'
        except Exception:
            pass

    return None


def _build_headers(cookie_str, content_type='application/json'):
    """构建请求头"""
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'SkillHub-PlatformOps/1.0',
    }
    if cookie_str.startswith('BEARER:'):
        api_key = cookie_str[len('BEARER:'):]
        headers['Authorization'] = f'Bearer {api_key}'
    else:
        headers['Cookie'] = cookie_str
    if content_type:
        headers['Content-Type'] = content_type
    return headers


def post_upload_publish(slug: str) -> dict:
    """上传成功后的完整发布流程: approve → publish_to_community → star

    被 enterprise_uploader.py 的 _post_upload_publish() 调用。

    Args:
        slug: skill slug

    Returns:
        dict with approve, community, star, db_update
    """
    result = {
        'approve': {'success': False, 'message': ''},
        'community': {'success': False, 'message': ''},
        'star': {'success': False, 'message': ''},
        'db_update': {'success': False, 'message': ''},
    }

    auth = _load_auth()
    if not auth:
        result['error'] = '无认证信息'
        return result

    # 1. Approve — 通过审核 (企业版API)
    try:
        approve_url = f"{ORG_ADMIN_SKILLS_API}/{slug}/approve"
        req = Request(approve_url, data=b'{}', headers=_build_headers(auth), method='POST')
        with urlopen(req, timeout=15) as resp:
            resp_data = json.loads(resp.read().decode('utf-8'))
            result['approve'] = {'success': True, 'message': '已审核', 'data': resp_data}
    except HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')[:200]
        result['approve'] = {'success': False, 'message': f'HTTP {e.code}: {body}'}
    except Exception as e:
        result['approve'] = {'success': False, 'message': str(e)}

    # 2. Publish to community — 发布到社区
    try:
        publisher_id = _get_publisher_profile_id()
        publish_body = json.dumps({'publisherProfileId': publisher_id}).encode('utf-8') if publisher_id else b'{}'
        publish_url = f"{ORG_ADMIN_SKILLS_API}/{slug}/publish-to-community"
        req = Request(publish_url, data=publish_body, headers=_build_headers(auth), method='POST')
        with urlopen(req, timeout=15) as resp:
            resp_data = json.loads(resp.read().decode('utf-8'))
            result['community'] = {'success': True, 'message': '已发布到社区', 'data': resp_data}
    except HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')[:200]
        result['community'] = {'success': False, 'message': f'HTTP {e.code}: {body}'}
    except Exception as e:
        result['community'] = {'success': False, 'message': str(e)}

    # 3. Star — 点赞
    try:
        star_url = f"{API_BASE}/community/skills/{slug}/star"
        req = Request(star_url, data=b'{}', headers=_build_headers(auth), method='POST')
        with urlopen(req, timeout=15) as resp:
            resp_data = json.loads(resp.read().decode('utf-8'))
            result['star'] = {'success': True, 'message': '已点赞', 'data': resp_data}
    except HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')[:200]
        result['star'] = {'success': False, 'message': f'HTTP {e.code}: {body}'}
    except Exception as e:
        result['star'] = {'success': False, 'message': str(e)}

    # 4. DB更新 — 记录发布状态
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            UPDATE skills
            SET skillhub_sync_status = 'synced',
                last_sync_at = datetime('now')
            WHERE slug = ?
        """, (slug,))
        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
            SELECT id, 'publish_skillhub', datetime('now'), 'platform_ops',
                   'approve=' || ? || ', community=' || ? || ', star=' || ?,
                   'synced'
            FROM skills WHERE slug = ?
        """, (
            str(result['approve']['success']),
            str(result['community']['success']),
            str(result['star']['success']),
            slug
        ))
        conn.commit()
        conn.close()
        result['db_update'] = {'success': True, 'message': 'DB已更新'}
    except Exception as e:
        result['db_update'] = {'success': False, 'message': str(e)}

    return result


def check_banned_skills() -> dict:
    """检查 SkillHub 上哪些 skill 已被封禁/删除

    被 daily_sync.py 的 step_check_banned_skills() 通过 CLI 调用。
    检测到的封禁技能在 DB 中标记为 deleted_on_skillhub。

    Returns:
        dict with total_checked, banned_count, banned_slugs
    """
    auth = _load_auth()
    if not auth:
        print("ERROR: 无认证信息")
        return {'error': '无认证信息', 'banned_count': 0}

    # 获取所有已上传到 skillhub 的 skill
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT slug FROM skills
        WHERE skillhub_sync_status = 'synced'
        AND current_status != 'deleted_on_skillhub'
    """)
    synced_slugs = [row[0] for row in c.fetchall()]
    conn.close()

    print(f"检查 {len(synced_slugs)} 个已上传skill的封禁状态...")

    banned_slugs = []
    checked = 0

    for slug in synced_slugs:
        checked += 1
        try:
            # 检查 skill 是否存在于社区
            url = f"{API_BASE}/community/skills/{slug}"
            req = Request(url, headers=_build_headers(auth), method='GET')
            with urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                # skill 存在,检查状态
                status = data.get('status', '')
                if status in ('deleted', 'banned', 'removed'):
                    banned_slugs.append(slug)
                    _mark_banned(slug)
        except HTTPError as e:
            if e.code == 404:
                # skill 不存在,已被删除
                banned_slugs.append(slug)
                _mark_banned(slug)
            elif e.code == 403:
                # 可能被封禁
                banned_slugs.append(slug)
                _mark_banned(slug)
        except Exception:
            pass

        # 速率限制: 每次检查间隔 1 秒
        if checked % 10 == 0:
            print(f"  已检查 {checked}/{len(synced_slugs)}, 封禁 {len(banned_slugs)}")
            import time
            time.sleep(1)

    print(f"\n检查完成: {checked} 个skill, {len(banned_slugs)} 个被封禁")
    if banned_slugs:
        print(f"封禁列表: {banned_slugs[:20]}")
    return {
        'total_checked': checked,
        'banned_count': len(banned_slugs),
        'banned_slugs': banned_slugs,
    }


def _mark_banned(slug: str):
    """在DB中标记skill为 deleted_on_skillhub"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        UPDATE skills
        SET current_status = 'deleted_on_skillhub',
            skillhub_sync_status = 'banned'
        WHERE slug = ?
    """, (slug,))
    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        SELECT id, 'banned_detected', datetime('now'), 'platform_ops',
               'SkillHub封禁检测: skill已不存在或状态为deleted/banned',
               'deleted_on_skillhub'
        FROM skills WHERE slug = ?
    """, (slug,))
    conn.commit()
    conn.close()


def cmd_status():
    """查看平台状态"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT skillhub_sync_status, COUNT(*)
        FROM skills
        GROUP BY skillhub_sync_status
    """)
    print("SkillHub 同步状态:")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    c.execute("""
        SELECT current_status, COUNT(*)
        FROM skills
        WHERE current_status LIKE '%skillhub%' OR current_status = 'deleted'
        GROUP BY current_status
    """)
    print("\nSkill 相关状态:")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    c.execute("""
        SELECT platform, upload_status, COUNT(*)
        FROM platform_uploads
        GROUP BY platform, upload_status
        ORDER BY platform, upload_status
    """)
    print("\n平台上传记录:")
    for row in c.fetchall():
        print(f"  {row[0]}/{row[1]}: {row[2]}")

    conn.close()


def _find_npx():
    """查找npx可执行文件路径 (Windows兼容)"""
    import shutil
    npx = shutil.which('npx')
    if npx:
        return npx
    # 常见路径回退
    for p in [
        r'C:\Program Files\nodejs\npx.cmd',
        r'C:\Program Files\nodejs\npx',
        r'C:\nodejs\npx.cmd',
    ]:
        if Path(p).exists():
            return p
    return 'npx'


def _update_skillhub_skill_in_db(c, slug, downloads, stars, audit_status=None):
    """更新单个SkillHub技能数据到DB (内部辅助函数)

    V196修复: 不再将所有非deleted状态覆盖为published_skillhub。
    - audit_status='pending' → current_status='pending_review_skillhub' (审核中,不可下载)
    - audit_status=其他/None → current_status='published_skillhub' (已发布,可下载)
    - 保留deleted状态不变
    - 已是pending_review_skillhub的,不会被覆盖为published_skillhub(即使audit_status非pending,
      需要手动确认审核通过后才升级)

    Returns:
        bool: True=已更新, False=未找到
    """
    c.execute(
        "SELECT id FROM skills WHERE skillhub_slug = ? OR slug = ?",
        (slug, slug)
    )
    row = c.fetchone()
    if row:
        skill_id = row[0]
        if audit_status == 'pending':
            # V196: 审核中 → pending_review_skillhub (不覆盖deleted)
            c.execute("""
                UPDATE skills
                SET platform_downloads = ?,
                    platform_stars = ?,
                    skillhub_sync_status = 'synced',
                    last_platform_sync_at = datetime('now', 'localtime'),
                    current_status = CASE
                        WHEN current_status = 'deleted' THEN current_status
                        ELSE 'pending_review_skillhub'
                    END
                WHERE id = ?
            """, (downloads, stars, skill_id))
        else:
            # V196: 已审核 → published_skillhub (不覆盖deleted和pending_review_skillhub)
            c.execute("""
                UPDATE skills
                SET platform_downloads = ?,
                    platform_stars = ?,
                    skillhub_sync_status = 'synced',
                    last_platform_sync_at = datetime('now', 'localtime'),
                    current_status = CASE
                        WHEN current_status IN ('deleted', 'pending_review_skillhub') THEN current_status
                        ELSE 'published_skillhub'
                    END
                WHERE id = ?
            """, (downloads, stars, skill_id))
        return True
    return False


def sync_skillhub_data(from_file=None, from_stdin=False, from_data=None) -> dict:
    """同步SkillHub平台数据到本地DB

    从SkillHub admin API获取所有已发布技能的最新数据(下载数、星标数、可见性等),
    更新到本地DB的skills表。支持分页获取全部技能。

    认证方式:
    - API直连: 通过_load_auth()获取凭证(V196: 支持api-key.txt中的bt_商户token)
    --from-stdin: 通过stdin传入JSON数据(浏览器fetch结果直接管道, 无需文件)
    --from-file: 通过JSON文件传入数据(应急用, 不推荐作为常规方式)

    V194增强: 同步完成后自动对账 — 标记DB中skillhub_sync_status='synced'但
    平台上已不存在的技能为deleted_on_skillhub(根因: 旧org被封禁后技能消失)。
    V196修复: 不再将pending_review_skillhub覆盖为published_skillhub;
              根据contentAuditStatus正确设置current_status。

    使用方式:
        python platform_ops.py sync-skillhub                    # 从API同步
        echo '<json>' | python platform_ops.py sync-skillhub --from-stdin  # 从stdin同步

    Args:
        from_file: 可选, 从JSON文件读取平台数据(应急用)
        from_stdin: 可选, 从stdin读取JSON平台数据(推荐: 浏览器fetch结果直接管道)

    Returns:
        dict with total_synced, updated, not_found, errors, missing_from_platform
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    total_synced = 0
    updated = 0
    not_found = 0
    errors = 0
    platform_slugs = set()  # V194: 收集平台技能slug, 用于后续对账

    if from_data is not None:
        # V196: 直接从内存数据同步 (浏览器fetch结果直接传入, 无需文件/stdin)
        all_skills = from_data
        print(f"从内存加载 {len(all_skills)} 条平台数据")
    elif from_stdin or from_file:
        # V196: 从stdin或文件读取平台数据 (浏览器fetch结果)
        if from_stdin:
            try:
                all_skills = json.loads(sys.stdin.read())
                print(f"从stdin加载 {len(all_skills)} 条平台数据")
            except Exception as e:
                print(f"ERROR: stdin读取失败: {e}")
                conn.close()
                return {'error': str(e), 'total_synced': 0}
        else:
            file_path = Path(from_file)
            if not file_path.exists():
                print(f"ERROR: 文件不存在: {from_file}")
                conn.close()
                return {'error': '文件不存在', 'total_synced': 0}
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    all_skills = json.load(f)
                print(f"从文件加载 {len(all_skills)} 条平台数据: {from_file}")
            except Exception as e:
                print(f"ERROR: 读取文件失败: {e}")
                conn.close()
                return {'error': str(e), 'total_synced': 0}

    # V196: 共享处理逻辑 — from_data和from_stdin/from_file路径统一处理
    if from_data is not None or from_stdin or from_file:
        for skill in all_skills:
            slug = skill.get('slug', '')
            downloads = skill.get('downloads', 0)
            stars = skill.get('stars', 0)
            audit_status = skill.get('contentAuditStatus', '')  # V196: 获取审核状态
            if not slug:
                continue
            platform_slugs.add(slug)  # V194: 收集平台slug
            if _update_skillhub_skill_in_db(c, slug, downloads, stars, audit_status):
                updated += 1
            else:
                not_found += 1
                if not_found <= 10:
                    print(f"  WARN: 平台技能 '{slug}' 在本地DB中未找到")
            total_synced += 1
    else:
        # 从API同步
        auth = _load_auth()
        if not auth:
            print("ERROR: 无认证信息, 请使用 --from-file 从浏览器导出的数据同步")
            conn.close()
            return {'error': '无认证信息', 'total_synced': 0}

        page = 1
        while True:
            url = f"{ORG_ADMIN_SKILLS_API}?page={page}&pageSize=100"
            try:
                req = Request(url, headers=_build_headers(auth), method='GET')
                with urlopen(req, timeout=30) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
            except Exception as e:
                print(f"ERROR: 获取第{page}页失败: {e}")
                errors += 1
                break

            skills = data.get('skills', [])
            total = data.get('total', 0)
            if not skills:
                break

            for skill in skills:
                slug = skill.get('slug', '')
                downloads = skill.get('downloads', 0)
                stars = skill.get('stars', 0)
                audit_status = skill.get('contentAuditStatus', '')  # V196: 获取审核状态
                if not slug:
                    continue
                platform_slugs.add(slug)  # V194: 收集平台slug
                if _update_skillhub_skill_in_db(c, slug, downloads, stars, audit_status):
                    updated += 1
                else:
                    not_found += 1
                    if not_found <= 10:
                        print(f"  WARN: 平台技能 '{slug}' 在本地DB中未找到")
                total_synced += 1

            print(f"  第{page}页: {len(skills)}个技能, 累计{total_synced}/{total}")
            if total_synced >= total or len(skills) < 100:
                break
            page += 1

    # V194: 平台对账 — 标记DB中synced但平台上不存在的技能为deleted_on_skillhub
    # 根因: 旧org(862)被封禁后, 上传到该org的技能从平台消失, 但DB中仍标记为synced
    missing_from_platform = 0
    if platform_slugs and errors == 0:
        c.execute("""
            SELECT id, slug, skillhub_slug FROM skills
            WHERE skillhub_sync_status = 'synced'
            AND current_status NOT IN ('deleted_on_skillhub', 'deleted')
        """)
        for skill_id, slug, skillhub_slug in c.fetchall():
            if slug not in platform_slugs and (skillhub_slug is None or skillhub_slug not in platform_slugs):
                c.execute(
                    "UPDATE skills SET current_status = 'deleted_on_skillhub' WHERE id = ?",
                    (skill_id,)
                )
                missing_from_platform += 1
        if missing_from_platform > 0:
            print(f"  V194对账: {missing_from_platform}个技能在平台上不存在, 标记为deleted_on_skillhub")

    # 记录操作日志
    c.execute("""
        INSERT INTO operations (operation_type, operation_date, operator, details, after_state)
        VALUES ('sync_skillhub_data', datetime('now', 'localtime'), 'platform_ops', ?, 'completed')
    """, (f'total={total_synced}, updated={updated}, not_found={not_found}, errors={errors}, missing_from_platform={missing_from_platform}',))
    conn.commit()
    conn.close()

    print(f"\nSkillHub同步完成: 共{total_synced}个技能, 更新{updated}个, 未找到{not_found}个, 错误{errors}个, 平台缺失{missing_from_platform}个")
    return {
        'total_synced': total_synced,
        'updated': updated,
        'not_found': not_found,
        'errors': errors,
        'missing_from_platform': missing_from_platform,
    }


def sync_clawhub_data(failed_only=False) -> dict:
    """同步ClawHub平台数据到本地DB

    通过ClawHub CLI (npx clawhub inspect) 验证已发布技能状态,
    更新到本地DB的skills表。inspect命令无需认证。

    使用方式:
        python platform_ops.py sync-clawhub              # 检查synced+failed
        python platform_ops.py sync-clawhub --failed-only  # 只检查failed (快速)

    Args:
        failed_only: True=只检查failed状态的技能(快速验证哪些failed实际已存在)

    Returns:
        dict with total_synced, updated, errors
    """
    import subprocess

    conn = sqlite3.connect(DB_PATH, timeout=30)  # V194: 增加timeout防止并发锁
    c = conn.cursor()

    # V197: 查询synced和failed状态的技能 (failed也可能实际上传成功,只是token过期导致误报失败)
    if failed_only:
        c.execute(
            "SELECT id, slug, clawhub_slug, clawhub_sync_status FROM skills WHERE clawhub_sync_status = 'failed'"
        )
    else:
        c.execute(
            "SELECT id, slug, clawhub_slug, clawhub_sync_status FROM skills WHERE clawhub_sync_status IN ('synced', 'failed')"
        )
    db_skills = c.fetchall()

    if not db_skills:
        print("DB中无ClawHub已同步或失败的技能")
        conn.close()
        return {'total_synced': 0, 'updated': 0, 'errors': 0, 'failed_recovered': 0}

    synced_count = sum(1 for s in db_skills if s[3] == 'synced')
    failed_count = sum(1 for s in db_skills if s[3] == 'failed')
    print(f"DB中ClawHub技能: synced={synced_count}, failed={failed_count}, 共{len(db_skills)}个, 开始验证...")

    total_synced = 0
    updated = 0
    not_found = 0
    errors = 0
    failed_recovered = 0  # V197: failed→synced的数量
    npx_cmd = _find_npx()

    for skill_id, db_slug, clawhub_slug, orig_status in db_skills:
        inspect_slug = clawhub_slug or db_slug
        if not inspect_slug:
            continue

        try:
            result = subprocess.run(
                [npx_cmd, 'clawhub', 'inspect', inspect_slug, '--registry', CLAWHUB_REGISTRY],
                capture_output=True, text=True, timeout=30,
                cwd=str(Path(__file__).resolve().parent.parent),
                shell=True
            )
        except Exception as e:
            print(f"  ERROR: {inspect_slug} 检查失败: {e}")
            errors += 1
            total_synced += 1
            continue

        if result.returncode == 0:
            # 技能存在且可访问 → 标记为synced
            c.execute("""
                UPDATE skills
                SET clawhub_sync_status = 'synced',
                    last_platform_sync_at = datetime('now', 'localtime')
                WHERE id = ?
            """, (skill_id,))
            conn.commit()
            updated += 1
            if orig_status == 'failed':
                failed_recovered += 1
                print(f"  RECOVERED: {inspect_slug} (was failed → now synced)")
            else:
                print(f"  OK: {inspect_slug}")
        else:
            # 技能可能已删除或不可访问
            stderr = result.stderr.strip()[:200] if result.stderr else ''
            stdout = result.stdout.strip()[:200] if result.stdout else ''
            combined = (stderr + ' ' + stdout).lower()
            # V197: "Found multiple skills" 表示slug有多个发布者, 但技能确实存在
            if 'found multiple skills' in combined or 'multiple skills with the slug' in combined:
                c.execute("""
                    UPDATE skills
                    SET clawhub_sync_status = 'synced',
                        last_platform_sync_at = datetime('now', 'localtime')
                    WHERE id = ?
                """, (skill_id,))
                conn.commit()
                updated += 1
                if orig_status == 'failed':
                    failed_recovered += 1
                    print(f"  RECOVERED (multiple): {inspect_slug} (exists with duplicate slug → synced)")
                else:
                    print(f"  OK (multiple): {inspect_slug} (exists with duplicate slug)")
            elif 'not found' in combined or '404' in combined:
                if orig_status == 'synced':
                    # 曾经synced但现在不存在 → 被删除
                    c.execute("""
                        UPDATE skills
                        SET clawhub_sync_status = 'deleted_on_clawhub',
                            last_platform_sync_at = datetime('now', 'localtime')
                        WHERE id = ?
                    """, (skill_id,))
                    conn.commit()
                    not_found += 1
                    print(f"  DELETED: {inspect_slug}")
                else:
                    # 原本就是failed, 平台上确实不存在 → 保持failed (等待重新上传)
                    print(f"  STILL FAILED: {inspect_slug} (confirmed not on ClawHub)")
            else:
                errors += 1
                print(f"  ERROR: {inspect_slug} - {stderr}")

        total_synced += 1

    c.execute("""
        INSERT INTO operations (operation_type, operation_date, operator, details, after_state)
        VALUES ('sync_clawhub_data', datetime('now', 'localtime'), 'platform_ops', ?, 'completed')
    """, (f'total={total_synced}, updated={updated}, not_found={not_found}, errors={errors}, failed_recovered={failed_recovered}',))
    conn.commit()
    conn.close()

    print(f"\nClawHub同步完成: 共{total_synced}个技能, 正常{updated}个(其中failed恢复{failed_recovered}个), 已删除{not_found}个, 错误{errors}个")
    return {
        'total_synced': total_synced,
        'updated': updated,
        'not_found': not_found,
        'errors': errors,
        'failed_recovered': failed_recovered,
    }


def sync_all_platform_data():
    """同步所有平台数据到本地DB (SkillHub + ClawHub)"""
    print("=" * 50)
    print("同步SkillHub平台数据")
    print("=" * 50)
    sh_result = sync_skillhub_data()

    print()
    print("=" * 50)
    print("同步ClawHub平台数据")
    print("=" * 50)
    ch_result = sync_clawhub_data()

    print()
    print("=" * 50)
    print("平台数据同步汇总")
    print("=" * 50)
    print(f"  SkillHub: {sh_result.get('updated', 0)}个已更新")
    print(f"  ClawHub:  {ch_result.get('updated', 0)}个已更新")

    return {'skillhub': sh_result, 'clawhub': ch_result}


def reconcile_sync_status(platform: str = None, dry_run: bool = False) -> dict:
    """修复skills表与platform_uploads表之间的sync_status不一致

    根因: 历史上传(旧API模式/手动上传)可能更新了platform_uploads但未更新
    skills.{platform}_sync_status,导致DB状态不一致。
    本函数通过platform_uploads的成功记录反推,批量修复sync_status。

    V193增强: 同时修复current_status不一致 — 当skill有平台指标(downloads/stars > 0)
    但current_status仍为'local_only'时,更新为'published_skillhub'。
    根因: sync_skillhub_data()最后一次运行只处理了212个skill,后续通过reconcile
    标记为synced的skill未经过sync_skillhub_data()更新current_status。

    非冗余确认:
    - sync_skillhub_data(): 从SkillHub API拉取下载数/星标等指标 — 不同用途
    - sync_clawhub_data(): 从ClawHub API拉取平台数据 — 不同用途
    - 本函数: 基于本地platform_uploads表修复skills表状态 — 唯一功能

    Args:
        platform: 指定平台('skillhub'/'clawhub'), None=全部
        dry_run: True=仅显示不执行

    Returns:
        dict with updated count, total synced, still pending, current_status_fixed
    """
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()

    platforms = [platform] if platform else ['skillhub', 'clawhub']
    results = {}

    for plat in platforms:
        sync_col = f'{plat}_sync_status'

        # 检查列是否存在
        c.execute(f"PRAGMA table_info(skills)")
        columns = [row[1] for row in c.fetchall()]
        if sync_col not in columns:
            results[plat] = {'error': f'column {sync_col} not found'}
            continue

        # 统计待修复
        c.execute(f"""
            SELECT COUNT(DISTINCT s.id) FROM skills s
            INNER JOIN platform_uploads pu ON s.id = pu.skill_id
            WHERE pu.http_status IN (200, 201)
            AND pu.platform = ?
            AND pu.upload_status = 'success'
            AND s.{sync_col} != 'synced'
        """, (plat,))
        pending_count = c.fetchone()[0]

        if dry_run:
            c.execute(f"""
                SELECT COUNT(*) FROM skills WHERE {sync_col} = 'synced'
            """)
            current_synced = c.fetchone()[0]
            # V193: dry-run中也检查current_status待修复数量
            cs_fixed = 0
            if plat == 'skillhub':
                c.execute("""
                    SELECT COUNT(*) FROM skills
                    WHERE skillhub_sync_status = 'synced'
                    AND current_status = 'local_only'
                    AND (platform_downloads > 0 OR platform_stars > 0)
                """)
                cs_fixed = c.fetchone()[0]
            results[plat] = {
                'dry_run': True,
                'would_update': pending_count,
                'current_synced': current_synced,
                'current_status_fixed': cs_fixed,
            }
            continue

        # 执行修复
        c.execute(f"""
            UPDATE skills
            SET {sync_col} = 'synced',
                last_sync_at = ?
            WHERE id IN (
                SELECT DISTINCT skill_id FROM platform_uploads
                WHERE http_status IN (200, 201)
                AND platform = ?
                AND upload_status = 'success'
            )
            AND {sync_col} != 'synced'
        """, (datetime.now().isoformat(), plat))
        updated = c.rowcount

        c.execute(f"SELECT COUNT(*) FROM skills WHERE {sync_col} = 'synced'")
        total_synced = c.fetchone()[0]

        # V199: 基于current_status修复sync_status — 处理无platform_uploads记录的skill
        # 根因: batch-check-and-approve(browser_evaluate)和mark-pending-upload直接更新
        # current_status但不创建platform_uploads记录,导致reconcile无法通过platform_uploads
        # 反推sync_status. 这些skill的current_status已准确反映平台状态,可直接用于修复.
        # 修复规则:
        # 1. current_status为published/pending_review且sync_status仍为pending_upload/waf_blocked → synced
        #    (waf_blocked的published skill说明V198修复后已成功上传,旧waf_blocked状态已过期)
        # 2. current_status为deleted/deleted_on_skillhub且sync_status仍为pending_upload/waf_blocked/failed → not_applicable
        #    (已删除的skill不需要上传,任何上传相关状态都是过期的)
        cs_synced = 0
        cs_not_applicable = 0
        if plat == 'skillhub':
            c.execute("""
                UPDATE skills
                SET skillhub_sync_status = 'synced', last_sync_at = ?
                WHERE current_status IN ('published_skillhub', 'pending_review_skillhub')
                AND skillhub_sync_status IN ('pending_upload', 'waf_blocked')
            """, (datetime.now().isoformat(),))
            cs_synced = c.rowcount

            c.execute("""
                UPDATE skills
                SET skillhub_sync_status = 'not_applicable'
                WHERE current_status IN ('deleted', 'deleted_on_skillhub')
                AND skillhub_sync_status IN ('pending_upload', 'waf_blocked', 'failed')
            """)
            cs_not_applicable = c.rowcount

        # V193: 修复current_status不一致 — 仅skillhub平台
        # 当skill有平台指标(downloads/stars > 0)但current_status仍为'local_only'时,
        # 说明skill曾在平台上存在过(sync_skillhub_data曾拉取过指标),但current_status未被更新。
        # 安全条件: 仅更新current_status='local_only'且synced的skill,不触碰deleted/published等状态
        current_status_fixed = 0
        if plat == 'skillhub':
            c.execute("""
                UPDATE skills
                SET current_status = 'published_skillhub'
                WHERE skillhub_sync_status = 'synced'
                AND current_status = 'local_only'
                AND (platform_downloads > 0 OR platform_stars > 0)
            """)
            current_status_fixed = c.rowcount

        results[plat] = {
            'updated': updated,
            'total_synced': total_synced,
            'still_pending': pending_count - updated,
            'current_status_fixed': current_status_fixed,
            'cs_synced': cs_synced,
            'cs_not_applicable': cs_not_applicable,
        }

    conn.commit()
    conn.close()

    print("=" * 50)
    print("sync_status一致性修复")
    print("=" * 50)
    for plat, r in results.items():
        if 'error' in r:
            print(f"  {plat}: 错误 - {r['error']}")
        elif r.get('dry_run'):
            print(f"  {plat} (dry-run): 将修复{r['would_update']}个, 当前synced={r['current_synced']}, current_status待修复={r.get('current_status_fixed', 0)}")
        else:
            cs_info = f", current_status修复={r.get('current_status_fixed', 0)}"
            if r.get('cs_synced', 0) or r.get('cs_not_applicable', 0):
                cs_info += f", V199: synced={r['cs_synced']}, not_applicable={r['cs_not_applicable']}"
            print(f"  {plat}: 修复{r['updated']}个, synced总数={r['total_synced']}, 遗留={r['still_pending']}{cs_info}")

    return results


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python platform_ops.py [check-banned|publish <slug>|status|sync-skillhub|sync-clawhub [--failed-only]|sync-data|reconcile-sync]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == 'check-banned':
        check_banned_skills()
    elif cmd == 'publish' and len(sys.argv) >= 3:
        result = post_upload_publish(sys.argv[2])
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif cmd == 'status':
        cmd_status()
    elif cmd == 'sync-skillhub':
        from_file = None
        from_stdin = '--from-stdin' in sys.argv
        if not from_stdin and len(sys.argv) >= 4 and sys.argv[2] == '--from-file':
            from_file = sys.argv[3]
        sync_skillhub_data(from_file=from_file, from_stdin=from_stdin)
    elif cmd == 'sync-clawhub':
        failed_only = '--failed-only' in sys.argv
        sync_clawhub_data(failed_only=failed_only)
    elif cmd == 'sync-data':
        sync_all_platform_data()
    elif cmd == 'reconcile-sync':
        plat = None
        dry = '--dry-run' in sys.argv
        if '--platform' in sys.argv:
            idx = sys.argv.index('--platform')
            if idx + 1 < len(sys.argv):
                plat = sys.argv[idx + 1]
        reconcile_sync_status(platform=plat, dry_run=dry)
    elif cmd == 'post-upload':
        # V196固化: 上传后标准化同步流程 — 直接从API同步到DB, 无需JSON中转文件
        # DB是所有skill状态的唯一数据源, 严禁新建JSON格式数据存储
        # 用法: post-upload [--skillhub-only] [--clawhub-only]
        skillhub_only = '--skillhub-only' in sys.argv
        clawhub_only = '--clawhub-only' in sys.argv

        print("=" * 60)
        print("V196 固化流程: 上传后数据直接同步到DB")
        print("=" * 60)

        # Step 1: 同步SkillHub平台数据 (直接从API → DB)
        if not clawhub_only:
            print(f"\n[Step 1] 同步SkillHub平台数据 (API → DB)...")
            try:
                result = sync_skillhub_data()
                print(f"  结果: 共{result.get('total_synced', 0)}个技能, "
                      f"更新{result.get('updated', 0)}个, "
                      f"缺失{result.get('missing_from_platform', 0)}个")
            except Exception as e:
                print(f"  [ERROR] SkillHub同步失败: {e}")

        # Step 2: 同步ClawHub平台数据 (直接从CLI → DB)
        if not skillhub_only:
            print(f"\n[Step 2] 同步ClawHub平台数据 (CLI → DB)...")
            try:
                result = sync_clawhub_data()
                print(f"  结果: 共{result.get('total_synced', 0)}个技能, "
                      f"更新{result.get('updated', 0)}个")
            except Exception as e:
                print(f"  [ERROR] ClawHub同步失败: {e}")

        # Step 3: 显示最终状态
        print(f"\n[Step 3] 最终DB状态:")
        cmd_status()
        print("\n" + "=" * 60)
        print("V196 固化流程完成")
        print("=" * 60)
    elif cmd == 'mark-pending-upload' and len(sys.argv) >= 3:
        # 批量标记slug为pending_upload (从JSON文件读取)
        json_file = sys.argv[2]
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        slugs = data.get('slugs', data) if isinstance(data, dict) else data
        if not isinstance(slugs, list):
            print("Error: JSON必须包含slugs数组")
            sys.exit(1)
        conn = sqlite3.connect(str(DB_PATH))
        c = conn.cursor()
        updated = 0
        for slug in slugs:
            c.execute("UPDATE skills SET skillhub_sync_status='pending_upload' WHERE slug=? AND skillhub_sync_status='synced'", (slug,))
            updated += c.rowcount
        conn.commit()
        conn.close()
        print(f"已标记 {updated}/{len(slugs)} 个skill为pending_upload")
    else:
        print(f"未知命令: {cmd}")
        print("可用命令: check-banned, publish <slug>, status, sync-skillhub, sync-clawhub, sync-data,")
        print("  reconcile-sync [--platform <name>] [--dry-run],")
        print("  post-upload [--skillhub-only] [--clawhub-only],")
        print("  mark-pending-upload <json_file>")
        sys.exit(1)
