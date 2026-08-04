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
COMMUNITY_PUBLISH_API = f"{API_BASE}/community/skills/publish"
ORG_ADMIN_SKILLS_API = f"{API_BASE}/orgs/{ORG_ID}/admin/skills"

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
    """加载认证信息 (与 enterprise_uploader.py load_cookies 一致)"""
    # 1. 环境变量
    env_cookies = os.environ.get('SKILLHUB_SESSION_COOKIE', '')
    if env_cookies:
        return env_cookies

    # 2. Cookie文件
    if COOKIE_FILE.exists():
        cookies = COOKIE_FILE.read_text(encoding='utf-8-sig').strip()
        if cookies:
            return cookies

    # 3. CLI凭证文件
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


def _update_skillhub_skill_in_db(c, slug, downloads, stars):
    """更新单个SkillHub技能数据到DB (内部辅助函数)

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
        c.execute("""
            UPDATE skills
            SET platform_downloads = ?,
                platform_stars = ?,
                skillhub_sync_status = 'synced',
                last_platform_sync_at = datetime('now', 'localtime'),
                current_status = CASE
                    WHEN current_status = 'deleted_on_skillhub' THEN current_status
                    ELSE 'published_skillhub'
                END
            WHERE id = ?
        """, (downloads, stars, skill_id))
        return True
    return False


def sync_skillhub_data(from_file=None) -> dict:
    """同步SkillHub平台数据到本地DB

    从SkillHub admin API获取所有已发布技能的最新数据(下载数、星标数、可见性等),
    更新到本地DB的skills表。支持分页获取全部技能。

    当cookie文件过期时, 可通过 from_file 参数传入浏览器导出的JSON数据文件。

    使用方式:
        python platform_ops.py sync-skillhub                  # 从API同步
        python platform_ops.py sync-skillhub --from-file <p>  # 从文件同步

    Args:
        from_file: 可选, 从JSON文件读取平台数据(绕过API认证)

    Returns:
        dict with total_synced, updated, not_found, errors
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    total_synced = 0
    updated = 0
    not_found = 0
    errors = 0

    if from_file:
        # 从文件读取平台数据 (浏览器导出)
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

        for skill in all_skills:
            slug = skill.get('slug', '')
            downloads = skill.get('downloads', 0)
            stars = skill.get('stars', 0)
            if not slug:
                continue
            if _update_skillhub_skill_in_db(c, slug, downloads, stars):
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
                if not slug:
                    continue
                if _update_skillhub_skill_in_db(c, slug, downloads, stars):
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

    # 记录操作日志
    c.execute("""
        INSERT INTO operations (operation_type, operation_date, operator, details, after_state)
        VALUES ('sync_skillhub_data', datetime('now', 'localtime'), 'platform_ops', ?, 'completed')
    """, (f'total={total_synced}, updated={updated}, not_found={not_found}, errors={errors}',))
    conn.commit()
    conn.close()

    print(f"\nSkillHub同步完成: 共{total_synced}个技能, 更新{updated}个, 未找到{not_found}个, 错误{errors}个")
    return {
        'total_synced': total_synced,
        'updated': updated,
        'not_found': not_found,
        'errors': errors,
    }


def sync_clawhub_data() -> dict:
    """同步ClawHub平台数据到本地DB

    通过ClawHub CLI (npx clawhub inspect) 验证已发布技能状态,
    更新到本地DB的skills表。inspect命令无需认证。

    使用方式:
        python platform_ops.py sync-clawhub

    Returns:
        dict with total_synced, updated, errors
    """
    import subprocess

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 查询DB中标记为clawhub synced的技能
    c.execute(
        "SELECT id, slug, clawhub_slug FROM skills WHERE clawhub_sync_status = 'synced'"
    )
    db_skills = c.fetchall()

    if not db_skills:
        print("DB中无ClawHub已同步技能")
        conn.close()
        return {'total_synced': 0, 'updated': 0, 'errors': 0}

    print(f"DB中ClawHub已同步技能: {len(db_skills)}个, 开始验证...")

    total_synced = 0
    updated = 0
    not_found = 0
    errors = 0
    npx_cmd = _find_npx()

    for skill_id, db_slug, clawhub_slug in db_skills:
        inspect_slug = clawhub_slug or db_slug
        if not inspect_slug:
            continue

        try:
            result = subprocess.run(
                [npx_cmd, 'clawhub', 'inspect', inspect_slug],
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
            # 技能存在且可访问
            c.execute("""
                UPDATE skills
                SET clawhub_sync_status = 'synced',
                    last_platform_sync_at = datetime('now', 'localtime')
                WHERE id = ?
            """, (skill_id,))
            updated += 1
            print(f"  OK: {inspect_slug}")
        else:
            # 技能可能已删除或不可访问
            stderr = result.stderr.strip()[:100] if result.stderr else ''
            if 'not found' in stderr.lower() or '404' in stderr:
                c.execute("""
                    UPDATE skills
                    SET clawhub_sync_status = 'deleted_on_clawhub',
                        last_platform_sync_at = datetime('now', 'localtime')
                    WHERE id = ?
                """, (skill_id,))
                not_found += 1
                print(f"  DELETED: {inspect_slug}")
            else:
                errors += 1
                print(f"  ERROR: {inspect_slug} - {stderr}")

        total_synced += 1

    c.execute("""
        INSERT INTO operations (operation_type, operation_date, operator, details, after_state)
        VALUES ('sync_clawhub_data', datetime('now', 'localtime'), 'platform_ops', ?, 'completed')
    """, (f'total={total_synced}, updated={updated}, not_found={not_found}, errors={errors}',))
    conn.commit()
    conn.close()

    print(f"\nClawHub同步完成: 共{total_synced}个技能, 正常{updated}个, 已删除{not_found}个, 错误{errors}个")
    return {
        'total_synced': total_synced,
        'updated': updated,
        'not_found': not_found,
        'errors': errors,
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


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python platform_ops.py [check-banned|publish <slug>|status|sync-skillhub|sync-clawhub|sync-data]")
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
        if len(sys.argv) >= 4 and sys.argv[2] == '--from-file':
            from_file = sys.argv[3]
        sync_skillhub_data(from_file=from_file)
    elif cmd == 'sync-clawhub':
        sync_clawhub_data()
    elif cmd == 'sync-data':
        sync_all_platform_data()
    else:
        print(f"未知命令: {cmd}")
        print("Usage: python platform_ops.py [check-banned|publish <slug>|status|sync-skillhub|sync-clawhub|sync-data]")
        sys.exit(1)
