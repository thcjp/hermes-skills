#!/usr/bin/env python3
"""
平台运维工具 (Platform Operations Tool)
======================================
基于本地主数据库 (upload_tracking.json) 驱动 SkillHub/ClawHub 平台运维操作。

核心原则: 本地数据库为唯一权威源，平台操作后更新本地状态。

使用方式:
    python platform_ops.py status              # 查看当前状态概览
    python platform_ops.py pending             # 列出所有待处理操作
    python platform_ops.py skillhub-actions    # 生成SkillHub操作清单 (供浏览器执行)
    python platform_ops.py clawhub-actions     # 生成ClawHub操作清单
    python platform_ops.py mark-approved <slug> [slug...]     # 标记SkillHub已审核
    python platform_ops.py mark-deleted <slug> [slug...]      # 标记SkillHub已删除
    python platform_ops.py mark-clawhub-published <slug> [slug...]  # 标记ClawHub已发布
    python platform_ops.py mark-clawhub-withdrawn <slug> [slug...] # 标记ClawHub已撤回
    python platform_ops.py find-promotional      # 查找ClawHub付费版宣传引流情况
    python platform_ops.py find-free-for-clawhub # 查找待上传ClawHub的免费版
    python platform_ops.py find-rejected         # 查找SkillHub被拒绝的skill
    python platform_ops.py find-platform-review  # 查找SkillHub平台审核中的skill
"""

import json
import sys
from pathlib import Path
from datetime import datetime

REGISTRY_DIR = Path(r"D:\skills\skill-registry")
DB_FILE = REGISTRY_DIR / "upload_tracking.json"
NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def load_db():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    db["metadata"]["last_updated"] = NOW
    # 重算统计
    recalc_stats(db)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def recalc_stats(db):
    skills = db.get("skills", {})
    stats = {
        "published": 0, "uploaded": 0, "produced": 0, "deleted": 0,
        "free": 0, "paid": 0,
        "sh_approved": 0, "sh_rejected": 0, "sh_platform_review": 0,
        "sh_admin_review": 0, "sh_not_uploaded": 0,
        "ch_published": 0, "ch_not_uploaded": 0, "ch_not_eligible": 0,
        "ch_withdrawn": 0, "ch_paid_promotional": 0
    }
    for slug, s in skills.items():
        stage = s.get("lifecycle", {}).get("stage", "")
        if stage in stats:
            stats[stage] += 1

        if s.get("is_free"):
            stats["free"] += 1
        else:
            stats["paid"] += 1

        sh = s.get("skillhub", {})
        sh_rs = sh.get("review_status", "")
        if sh_rs == "approved": stats["sh_approved"] += 1
        elif sh_rs == "rejected": stats["sh_rejected"] += 1
        elif sh_rs == "platform_review": stats["sh_platform_review"] += 1
        elif sh_rs == "admin_review": stats["sh_admin_review"] += 1
        else: stats["sh_not_uploaded"] += 1

        ch = s.get("clawhub", {})
        ch_st = ch.get("status", "")
        if ch_st == "published":
            stats["ch_published"] += 1
            if not s.get("is_free"):
                stats["ch_paid_promotional"] += 1
        elif ch_st == "not_uploaded": stats["ch_not_uploaded"] += 1
        elif ch_st == "not_eligible": stats["ch_not_eligible"] += 1
        elif ch_st == "withdrawn": stats["ch_withdrawn"] += 1

    db["stats"] = stats

def cmd_status():
    db = load_db()
    s = db["stats"]
    print(f"技能主数据库状态 (最后更新: {db['metadata']['last_updated']})")
    print(f"{'='*55}")
    print(f"总skill数: {db['metadata']['total_skills']}")
    print(f"{'─'*55}")
    print(f"生命周期:")
    print(f"  published (已上架):  {s['published']}")
    print(f"  uploaded (已上传):   {s['uploaded']}")
    print(f"  produced (本地待传): {s['produced']}")
    print(f"  deleted (已删除):    {s['deleted']}")
    print(f"{'─'*55}")
    print(f"商业属性:")
    print(f"  free (免费版):       {s['free']}")
    print(f"  paid (付费版):       {s['paid']}")
    print(f"{'─'*55}")
    print(f"SkillHub状态:")
    print(f"  approved (已审核):   {s['sh_approved']}")
    print(f"  platform_review:     {s['sh_platform_review']}")
    print(f"  rejected (已拒绝):   {s['sh_rejected']}")
    print(f"  admin_review:        {s['sh_admin_review']}")
    print(f"  not_uploaded:        {s['sh_not_uploaded']}")
    print(f"{'─'*55}")
    print(f"ClawHub状态:")
    print(f"  published (已发布):  {s['ch_published']}")
    print(f"  not_uploaded (待传): {s['ch_not_uploaded']}")
    print(f"  not_eligible (不可传): {s['ch_not_eligible']}")
    print(f"  withdrawn (已撤回):  {s['ch_withdrawn']}")
    if s['ch_paid_promotional'] > 0:
        print(f"\n  ★ {s['ch_paid_promotional']}个付费版在ClawHub作宣传引流")

def cmd_pending():
    db = load_db()
    skills = db["skills"]

    pending = {
        "skillhub_admin_review": [],
        "skillhub_rejected": [],
        "skillhub_platform_review": [],
        "clawhub_upload_candidates": [],
        "clawhub_paid_promotional": []
    }

    for slug, s in skills.items():
        sh = s.get("skillhub", {})
        ch = s.get("clawhub", {})

        if sh.get("review_status") == "admin_review":
            pending["skillhub_admin_review"].append(slug)
        if sh.get("review_status") == "rejected":
            pending["skillhub_rejected"].append(slug)
        if sh.get("review_status") == "platform_review":
            pending["skillhub_platform_review"].append(slug)
        if ch.get("upload_eligible") and ch.get("status") == "not_uploaded":
            pending["clawhub_upload_candidates"].append(slug)
        if not s.get("is_free") and ch.get("status") == "published":
            pending["clawhub_paid_promotional"].append(slug)

    print("待处理操作清单")
    print(f"{'='*55}")
    print(f"\n1. SkillHub待管理员审核 ({len(pending['skillhub_admin_review'])}个):")
    for slug in pending["skillhub_admin_review"]:
        print(f"   → {slug}")

    print(f"\n2. SkillHub被拒绝 ({len(pending['skillhub_rejected'])}个):")
    for slug in pending["skillhub_rejected"]:
        print(f"   → {slug}")

    print(f"\n3. SkillHub平台审核中 ({len(pending['skillhub_platform_review'])}个):")
    for slug in pending["skillhub_platform_review"]:
        print(f"   → {slug}")

    print(f"\n4. ClawHub待上传免费版 ({len(pending['clawhub_upload_candidates'])}个):")
    if len(pending["clawhub_upload_candidates"]) <= 20:
        for slug in pending["clawhub_upload_candidates"]:
            print(f"   → {slug}")
    else:
        for slug in pending["clawhub_upload_candidates"][:10]:
            print(f"   → {slug}")
        print(f"   ... 还有 {len(pending['clawhub_upload_candidates'])-10} 个")

    print(f"\n5. ClawHub付费版宣传引流 ({len(pending['clawhub_paid_promotional'])}个):")
    if len(pending["clawhub_paid_promotional"]) <= 20:
        for slug in pending["clawhub_paid_promotional"]:
            print(f"   → {slug}")
    else:
        for slug in pending["clawhub_paid_promotional"][:10]:
            print(f"   → {slug}")
        print(f"   ... 还有 {len(pending['clawhub_paid_promotional'])-10} 个")

    return pending

def cmd_skillhub_actions():
    """生成SkillHub操作清单 (JSON格式，供浏览器批量执行)"""
    db = load_db()
    skills = db["skills"]

    actions = {"approve": [], "delete_rejected": []}

    for slug, s in skills.items():
        sh = s.get("skillhub", {})
        if sh.get("review_status") == "admin_review":
            actions["approve"].append(slug)
        # rejected的skill不自动删除，需人工确认

    output_file = REGISTRY_DIR / "skillhub_pending_actions.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(actions, f, ensure_ascii=False, indent=2)

    print(f"SkillHub操作清单已生成: {output_file}")
    print(f"  待审核(approve): {len(actions['approve'])}个")
    print(f"\n浏览器执行方式:")
    print(f"  1. 导航到 https://www.skillhub.cn/admin/skill-reviews")
    print(f"  2. 对每个slug执行: POST /api/v1/orgs/862/admin/skills/{{slug}}/approve")
    print(f"  3. 执行后运行: python platform_ops.py mark-approved <slug1> <slug2> ...")

def cmd_clawhub_actions():
    """生成ClawHub操作清单"""
    db = load_db()
    skills = db["skills"]

    actions = {"upload_free": [], "promotional_paid": []}

    for slug, s in skills.items():
        ch = s.get("clawhub", {})
        if ch.get("upload_eligible") and ch.get("status") == "not_uploaded":
            actions["upload_free"].append(slug)
        if not s.get("is_free") and ch.get("status") == "published":
            actions["promotional_paid"].append(slug)

    output_file = REGISTRY_DIR / "clawhub_pending_actions.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(actions, f, ensure_ascii=False, indent=2)

    print(f"ClawHub操作清单已生成: {output_file}")
    print(f"  待上传(免费版+引流候选): {len(actions['upload_free'])}个")
    print(f"  已发布付费版(宣传引流): {len(actions['promotional_paid'])}个")
    print(f"\n上传后运行:")
    print(f"  python platform_ops.py mark-clawhub-published <slug1> <slug2> ...")

def cmd_mark_approved(slugs):
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "approved"
            db["skills"][slug]["skillhub"]["reviewed_at"] = NOW
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            db["skills"][slug]["skillhub"]["notes"] = ""
            # 更新生命周期
            db["skills"][slug]["lifecycle"]["stage"] = "published"
            db["skills"][slug]["lifecycle"]["last_modified"] = NOW
            print(f"  ✅ {slug} → approved")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)
    print(f"\n已更新 {len(slugs)} 个skill状态")

def cmd_mark_deleted(slugs):
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "deleted"
            db["skills"][slug]["skillhub"]["uploaded"] = False
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            db["skills"][slug]["skillhub"]["notes"] = "已从SkillHub删除"
            print(f"  🗑 {slug} → deleted")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)
    print(f"\n已更新 {len(slugs)} 个skill状态")

def cmd_mark_clawhub_published(slugs):
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["clawhub"]["uploaded"] = True
            db["skills"][slug]["clawhub"]["status"] = "published"
            db["skills"][slug]["clawhub"]["last_sync"] = NOW
            db["skills"][slug]["clawhub"]["notes"] = ""
            print(f"  ✅ {slug} → clawhub published")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)
    print(f"\n已更新 {len(slugs)} 个skill状态")

def cmd_mark_clawhub_withdrawn(slugs):
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["clawhub"]["uploaded"] = False
            db["skills"][slug]["clawhub"]["status"] = "withdrawn"
            db["skills"][slug]["clawhub"]["last_sync"] = NOW
            db["skills"][slug]["clawhub"]["notes"] = "已从ClawHub撤回 (付费版不在免费平台)"
            print(f"  ↩ {slug} → clawhub withdrawn")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)
    print(f"\n已更新 {len(slugs)} 个skill状态")

def cmd_find_promotional():
    """查找ClawHub付费版宣传引流情况"""
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if not s.get("is_free") and s.get("clawhub", {}).get("status") == "published":
            found.append(slug)
            print(f"  → {slug} (pair: {s.get('pair_slug', 'N/A')})")
    total_paid = sum(1 for s in skills.values() if not s.get("is_free"))
    print(f"\n共 {len(found)} 个付费版在ClawHub作宣传引流 (总付费版: {total_paid}, 占比: {len(found)*100//total_paid}%)")
    return found

def cmd_find_free_for_clawhub():
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        ch = s.get("clawhub", {})
        if ch.get("upload_eligible") and ch.get("status") == "not_uploaded":
            found.append(slug)
    print(f"共 {len(found)} 个免费版待上传ClawHub")
    if len(found) <= 20:
        for slug in found:
            print(f"  → {slug}")
    else:
        for slug in found[:10]:
            print(f"  → {slug}")
        print(f"  ... 还有 {len(found)-10} 个")
    return found

def cmd_find_rejected():
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("skillhub", {}).get("review_status") == "rejected":
            found.append(slug)
            print(f"  → {slug}")
    print(f"\n共 {len(found)} 个skill被SkillHub拒绝")

def cmd_find_platform_review():
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("skillhub", {}).get("review_status") == "platform_review":
            found.append(slug)
            print(f"  → {slug}")
    print(f"\n共 {len(found)} 个skill在SkillHub平台审核中")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "status":
        cmd_status()
    elif cmd == "pending":
        cmd_pending()
    elif cmd == "skillhub-actions":
        cmd_skillhub_actions()
    elif cmd == "clawhub-actions":
        cmd_clawhub_actions()
    elif cmd == "mark-approved":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-approved <slug> [slug...]")
            return
        cmd_mark_approved(sys.argv[2:])
    elif cmd == "mark-deleted":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-deleted <slug> [slug...]")
            return
        cmd_mark_deleted(sys.argv[2:])
    elif cmd == "mark-clawhub-published":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-clawhub-published <slug> [slug...]")
            return
        cmd_mark_clawhub_published(sys.argv[2:])
    elif cmd == "mark-clawhub-withdrawn":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-clawhub-withdrawn <slug> [slug...]")
            return
        cmd_mark_clawhub_withdrawn(sys.argv[2:])
    elif cmd == "find-promotional":
        cmd_find_promotional()
    elif cmd == "find-free-for-clawhub":
        cmd_find_free_for_clawhub()
    elif cmd == "find-rejected":
        cmd_find_rejected()
    elif cmd == "find-platform-review":
        cmd_find_platform_review()
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)

if __name__ == "__main__":
    main()
