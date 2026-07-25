#!/usr/bin/env python3
"""
SkillHub批量审核通过脚本
========================
使用Admin API批量审核通过所有pending状态的skill。

API端点:
- 获取待审核列表: GET /orgs/{ORG_ID}/admin/skills?reviewStatus=pending
- 审核通过: POST /orgs/{ORG_ID}/admin/skills/{slug}/approve

使用方式:
    python batch_approve_api.py              # 批量审核所有pending
    python batch_approve_api.py --check      # 仅检查待审核数量
    python batch_approve_api.py --slug <s>   # 审核单个skill
"""
import json
import sys
import os
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enterprise_uploader import load_cookies, ORG_ID, API_BASE
from config import REPORT_DIR

COOKIES = None
HEADERS = None

def init_auth():
    global COOKIES, HEADERS
    COOKIES = load_cookies()
    if not COOKIES:
        print("错误: 无认证cookie")
        return False
    HEADERS = {
        'Cookie': COOKIES,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    # 验证认证
    try:
        url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills?page=1&pageSize=1"
        req = Request(url, headers=HEADERS)
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"✅ 认证成功! Skill总数: {data.get('total', 0)}")
            return True
    except Exception as e:
        print(f"❌ 认证失败: {e}")
        return False

def get_pending_skills(page=1, pageSize=100):
    """获取pending状态的skill列表"""
    url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills?reviewStatus=pending&page={page}&pageSize={pageSize}"
    req = Request(url, headers=HEADERS)
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data
    except Exception as e:
        print(f"  获取pending列表失败(page={page}): {e}")
        return {'skills': [], 'total': 0}

def approve_skill(slug):
    """审核通过单个skill"""
    url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/{slug}/approve"
    req = Request(url, data=b'{}', method='POST', headers={
        **HEADERS,
        'Content-Type': 'application/json'
    })
    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return True, data
    except HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')[:200]
        return False, {'error': f'HTTP {e.code}: {body}'}
    except Exception as e:
        return False, {'error': str(e)}

def batch_approve_all(delay=0.3):
    """批量审核通过所有pending skill"""
    # 进度文件
    progress_file = REPORT_DIR / "batch_approve_progress.json"

    # 加载已有进度
    approved = []
    failed = []
    if progress_file.exists():
        try:
            old = json.loads(progress_file.read_text(encoding='utf-8'))
            approved = old.get('approved', [])
            failed = old.get('failed', [])
            print(f"断点续传: 已审核 {len(approved)} 个，失败 {len(failed)} 个")
        except Exception:
            pass

    approved_set = set(approved)

    # 获取pending总数
    data = get_pending_skills(page=1, pageSize=1)
    total_pending = data.get('total', 0)
    print(f"\n待审核总数: {total_pending}")

    if total_pending == 0:
        print("✅ 无待审核skill")
        return

    # 分页获取所有pending slug
    all_pending = []
    pages = (total_pending // 100) + 1
    print(f"需扫描 {pages} 页...")

    for page in range(1, pages + 1):
        data = get_pending_skills(page=page, pageSize=100)
        skills = data.get('skills', [])
        if not skills:
            break
        for sk in skills:
            slug = sk.get('slug', '')
            if slug and slug not in approved_set:
                all_pending.append(slug)
        if page % 5 == 0:
            print(f"  已扫描 {page}/{pages} 页，收集 {len(all_pending)} 个待审核slug")

    print(f"\n待审核(去除已完成): {len(all_pending)} 个")

    if not all_pending:
        print("✅ 所有pending skill已审核完成")
        return

    # 批量审核
    success_count = 0
    fail_count = 0
    start_time = time.time()

    for i, slug in enumerate(all_pending):
        success, result = approve_skill(slug)

        if success:
            success_count += 1
            approved.append(slug)
            approved_set.add(slug)
        else:
            fail_count += 1
            failed = [f for f in failed if f.get('slug') != slug]
            failed.append({'slug': slug, 'error': result.get('error', 'unknown')})

        # 进度输出
        if (i + 1) % 50 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            remaining = (len(all_pending) - i - 1) / rate if rate > 0 else 0
            print(f"  [{i+1}/{len(all_pending)}] 成功={success_count}, 失败={fail_count}, "
                  f"速率={rate:.1f}/s, 剩余={remaining:.0f}s")

            # 保存进度
            with open(progress_file, 'w', encoding='utf-8') as f:
                json.dump({'approved': approved, 'failed': failed}, f, ensure_ascii=False)

        # 延迟
        if delay > 0 and (i + 1) % 10 == 0:
            time.sleep(delay)

    # 最终保存
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump({'approved': approved, 'failed': failed}, f, ensure_ascii=False)

    elapsed = time.time() - start_time
    print(f"\n=== 批量审核完成 ===")
    print(f"✅ 成功: {success_count}")
    print(f"❌ 失败: {fail_count}")
    print(f"⏱ 耗时: {elapsed:.1f}s")
    print(f"📁 进度文件: {progress_file}")

    if failed:
        print(f"\n失败详情(前20个):")
        for f in failed[:20]:
            print(f"  {f['slug']}: {f['error'][:80]}")

def check_pending():
    """仅检查待审核数量"""
    data = get_pending_skills(page=1, pageSize=1)
    total = data.get('total', 0)
    print(f"待审核skill数: {total}")

    # 也检查审核列表
    try:
        url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills/reviews?page=1&pageSize=1"
        req = Request(url, headers=HEADERS)
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"审核列表总数: {data.get('total', 0)}")
    except Exception as e:
        print(f"审核列表获取失败: {e}")

    # 检查已审核进度
    progress_file = REPORT_DIR / "batch_approve_progress.json"
    if progress_file.exists():
        prog = json.loads(progress_file.read_text(encoding='utf-8'))
        print(f"已审核: {len(prog.get('approved', []))}")
        print(f"审核失败: {len(prog.get('failed', []))}")

if __name__ == '__main__':
    if not init_auth():
        sys.exit(1)

    if len(sys.argv) > 1:
        if sys.argv[1] == '--check':
            check_pending()
        elif sys.argv[1] == '--slug':
            slug = sys.argv[2]
            success, result = approve_skill(slug)
            print(f"{'✅' if success else '❌'} {slug}: {json.dumps(result, ensure_ascii=False)[:200]}")
        else:
            print(f"未知参数: {sys.argv[1]}")
    else:
        batch_approve_all(delay=0.3)
