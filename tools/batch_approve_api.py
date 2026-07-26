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
    """获取待审核skill列表
    
    注意: API的reviewStatus过滤器可能不生效，返回所有skill。
    调用方需通过skill对象中的reviewStatus字段做二次过滤。
    """
    url = f"{API_BASE}/orgs/{ORG_ID}/admin/skills?page={page}&pageSize={pageSize}"
    req = Request(url, headers=HEADERS)
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data
    except Exception as e:
        print(f"  获取skill列表失败(page={page}): {e}")
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
    """批量审核通过所有admin_review状态的skill
    
    修复: API的reviewStatus过滤器不生效，需二次过滤。
    已发布的skill(visibility=public且reviewStatus为空)自动跳过。
    """
    # 进度文件
    progress_file = REPORT_DIR / "batch_approve_progress.json"

    # 加载已有进度
    approved = []
    failed = []
    skipped = []
    if progress_file.exists():
        try:
            old = json.loads(progress_file.read_text(encoding='utf-8'))
            approved = old.get('approved', [])
            failed = old.get('failed', [])
            skipped = old.get('skipped', [])
            print(f"断点续传: 已审核 {len(approved)} 个，失败 {len(failed)} 个，跳过 {len(skipped)} 个")
        except Exception:
            pass

    approved_set = set(approved)
    skipped_set = set(skipped)

    # 获取总数
    data = get_pending_skills(page=1, pageSize=1)
    total = data.get('total', 0)
    print(f"\n平台skill总数: {total}")

    if total == 0:
        print("✅ 无skill")
        return

    # 分页获取所有skill，二次过滤出admin_review状态
    all_admin_review = []
    pages = (total // 100) + 1
    print(f"需扫描 {pages} 页...")

    for page in range(1, pages + 1):
        data = get_pending_skills(page=page, pageSize=100)
        skills = data.get('skills', [])
        if not skills:
            break
        for sk in skills:
            slug = sk.get('slug', '')
            if not slug or slug in approved_set or slug in skipped_set:
                continue
            rs = sk.get('reviewStatus', '')
            vis = sk.get('visibility', '')
            # 只审核admin_review状态的skill
            if rs == 'admin_review':
                all_admin_review.append(slug)
            # 已发布的skill跳过(reviewStatus为空 + visibility=public)
            elif vis == 'public' and not rs:
                skipped.append(slug)
                skipped_set.add(slug)
            # pending状态也尝试审核(某些版本API可能需要)
            elif rs == 'pending':
                all_admin_review.append(slug)
        if page % 5 == 0:
            print(f"  已扫描 {page}/{pages} 页，待审核={len(all_admin_review)}，已跳过={len(skipped)}")

    print(f"\n待审核(admin_review): {len(all_admin_review)} 个")
    print(f"已发布跳过: {len(skipped)} 个")

    if not all_admin_review:
        print("✅ 所有skill已发布或无需审核")
        # 保存最终进度
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump({'approved': approved, 'failed': failed, 'skipped': skipped}, f, ensure_ascii=False)
        return

    # 批量审核
    success_count = 0
    fail_count = 0
    skip_count = 0
    start_time = time.time()

    for i, slug in enumerate(all_admin_review):
        success, result = approve_skill(slug)

        if success:
            success_count += 1
            approved.append(slug)
            approved_set.add(slug)
        else:
            error_msg = result.get('error', 'unknown')
            # "not in admin_review status" = 已发布，跳过不算失败
            if 'not in admin_review' in error_msg or 'not in admin' in error_msg.lower():
                skip_count += 1
                skipped.append(slug)
                skipped_set.add(slug)
            else:
                fail_count += 1
                failed = [f for f in failed if f.get('slug') != slug]
                failed.append({'slug': slug, 'error': error_msg})

        # 进度输出
        if (i + 1) % 50 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            remaining = (len(all_admin_review) - i - 1) / rate if rate > 0 else 0
            print(f"  [{i+1}/{len(all_admin_review)}] 成功={success_count}, 失败={fail_count}, 跳过={skip_count}, "
                  f"速率={rate:.1f}/s, 剩余={remaining:.0f}s")

            # 保存进度
            with open(progress_file, 'w', encoding='utf-8') as f:
                json.dump({'approved': approved, 'failed': failed, 'skipped': skipped}, f, ensure_ascii=False)

        # 延迟
        if delay > 0 and (i + 1) % 10 == 0:
            time.sleep(delay)

    # 最终保存
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump({'approved': approved, 'failed': failed, 'skipped': skipped}, f, ensure_ascii=False)

    elapsed = time.time() - start_time
    print(f"\n=== 批量审核完成 ===")
    print(f"✅ 成功: {success_count}")
    print(f"⏭ 已发布跳过: {skip_count}")
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
