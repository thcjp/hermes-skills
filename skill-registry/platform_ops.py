#!/usr/bin/env python3
"""
平台运维工具 v3.0 (Platform Operations Tool)
=============================================
基于本地主数据库 (upload_tracking.json Schema v3.0) 驱动 SkillHub/ClawHub 平台运维。
支持源skill注册、来源追踪、升级管理、双平台状态。

核心原则: 本地数据库为唯一权威源，平台操作后更新本地状态。

架构模型:
  源skill (is_source=true, 本地存储, 不上传)
    → 免费版 (两平台都传)
    → 付费版 (SkillHub全传, ClawHub 10%宣传引流)

使用方式:
    python platform_ops.py status              # 查看当前状态概览 (含源/生产分离)
    python platform_ops.py pending             # 列出所有待处理操作
    python platform_ops.py skillhub-actions    # 生成SkillHub操作清单
    python platform_ops.py clawhub-actions     # 生成ClawHub操作清单
    python platform_ops.py mark-approved <slug> [slug...]     # 标记SkillHub已审核
    python platform_ops.py mark-deleted <slug> [slug...]      # 标记SkillHub已删除
    python platform_ops.py mark-clawhub-published <slug> [slug...]  # 标记ClawHub已发布
    python platform_ops.py mark-clawhub-withdrawn <slug> [slug...] # 标记ClawHub已撤回
    python platform_ops.py find-promotional      # 查找ClawHub付费版宣传引流情况
    python platform_ops.py find-free-for-clawhub # 查找待上传ClawHub的免费版
    python platform_ops.py find-rejected         # 查找SkillHub被拒绝的skill
    python platform_ops.py find-platform-review  # 查找SkillHub平台审核中的skill
    python platform_ops.py find-untraced         # 查找未追溯到源的生产skill
    python platform_ops.py find-unpaired         # 查找未配对的免费/付费skill
    python platform_ops.py source-skills         # 列出所有源skill及其下载URL
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
        # 生命周期
        "published": 0, "uploaded": 0, "produced": 0, "deleted": 0, "discovered": 0,
        # 源/生产
        "source_total": 0, "source_clawhub": 0, "source_opensource": 0,
        "production_total": 0, "production_packaged": 0, "production_differentiated": 0,
        # 商业属性 (仅生产skill)
        "free": 0, "paid": 0,
        # 源追溯
        "traced_to_source": 0, "untraced": 0,
        "traced_clawhub": 0, "traced_opensource": 0, "traced_juejin": 0,
        # 配对
        "paired": 0, "unpaired_free": 0, "unpaired_paid": 0,
        # SkillHub
        "sh_approved": 0, "sh_rejected": 0, "sh_platform_review": 0,
        "sh_admin_review": 0, "sh_not_uploaded": 0, "sh_not_applicable": 0,
        # ClawHub
        "ch_published": 0, "ch_not_uploaded": 0, "ch_not_eligible": 0,
        "ch_withdrawn": 0, "ch_paid_promotional": 0, "ch_not_applicable": 0,
        # 源文件关联
        "has_source_file": 0,
    }
    for slug, s in skills.items():
        stage = s.get("lifecycle", {}).get("stage", "")
        if stage in stats:
            stats[stage] += 1

        if s.get("is_source"):
            stats["source_total"] += 1
            origin = s.get("source_origin", {})
            if origin.get("type") == "clawhub":
                stats["source_clawhub"] += 1
            elif origin.get("type") == "opensource":
                stats["source_opensource"] += 1
        else:
            stats["production_total"] += 1
            src = s.get("source", "")
            if src == "packaged":
                stats["production_packaged"] += 1
            elif src == "differentiated":
                stats["production_differentiated"] += 1

            origin = s.get("source_origin", {})
            origin_type = origin.get("type", "unknown")
            if origin_type != "unknown":
                stats["traced_to_source"] += 1
                if origin_type == "clawhub": stats["traced_clawhub"] += 1
                elif origin_type == "opensource": stats["traced_opensource"] += 1
                elif origin_type == "juejin": stats["traced_juejin"] += 1
            else:
                stats["untraced"] += 1

            if s.get("is_free"):
                stats["free"] += 1
            else:
                stats["paid"] += 1

            if s.get("pair_slug"):
                stats["paired"] += 1
            elif s.get("is_free"):
                stats["unpaired_free"] += 1
            else:
                stats["unpaired_paid"] += 1

            if s.get("has_source_file"):
                stats["has_source_file"] += 1

        sh = s.get("skillhub", {})
        sh_rs = sh.get("review_status", "")
        if sh_rs == "approved": stats["sh_approved"] += 1
        elif sh_rs == "rejected": stats["sh_rejected"] += 1
        elif sh_rs == "platform_review": stats["sh_platform_review"] += 1
        elif sh_rs == "admin_review": stats["sh_admin_review"] += 1
        elif sh_rs == "not_applicable": stats["sh_not_applicable"] += 1
        else: stats["sh_not_uploaded"] += 1

        ch = s.get("clawhub", {})
        ch_st = ch.get("status", "")
        if ch_st == "published":
            stats["ch_published"] += 1
            if not s.get("is_free") and not s.get("is_source"):
                stats["ch_paid_promotional"] += 1
        elif ch_st == "not_uploaded": stats["ch_not_uploaded"] += 1
        elif ch_st == "not_eligible": stats["ch_not_eligible"] += 1
        elif ch_st == "withdrawn": stats["ch_withdrawn"] += 1
        elif ch_st == "not_applicable": stats["ch_not_applicable"] += 1

    db["stats"] = stats

def cmd_status():
    db = load_db()
    s = db["stats"]
    meta = db["metadata"]
    print(f"技能主数据库 v{meta.get('schema_version', '2.0')} (最后更新: {meta['last_updated']})")
    print(f"{'='*55}")
    print(f"总skill数: {meta['total_skills']}")
    print(f"{'─'*55}")
    print(f"源skill (本地存储, 不上传):")
    print(f"  ClawHub源:  {s['source_clawhub']}")
    print(f"  开源源:    {s['source_opensource']}")
    print(f"  小计:      {s['source_total']}")
    print(f"{'─'*55}")
    print(f"生产skill (可上传):")
    print(f"  包装skill:   {s['production_packaged']}")
    print(f"  差异化skill: {s['production_differentiated']}")
    print(f"  小计:        {s['production_total']}")
    print(f"  有源文件:    {s['has_source_file']}")
    print(f"{'─'*55}")
    print(f"商业属性:")
    print(f"  free (免费版):       {s['free']}")
    print(f"  paid (付费版):       {s['paid']}")
    print(f"  paired (已配对):     {s['paired']}")
    print(f"  unpaired_free:       {s['unpaired_free']}")
    print(f"  unpaired_paid:       {s['unpaired_paid']}")
    print(f"{'─'*55}")
    print(f"源追溯:")
    print(f"  已追溯: {s['traced_to_source']} (ClawHub: {s['traced_clawhub']}, 开源: {s['traced_opensource']}, JueJin: {s['traced_juejin']})")
    print(f"  待追溯: {s['untraced']}")
    print(f"{'─'*55}")
    print(f"SkillHub状态:")
    print(f"  approved (已审核):   {s['sh_approved']}")
    print(f"  platform_review:     {s['sh_platform_review']}")
    print(f"  rejected (已拒绝):   {s['sh_rejected']}")
    print(f"  admin_review:        {s['sh_admin_review']}")
    print(f"  not_applicable(源):  {s['sh_not_applicable']}")
    print(f"{'─'*55}")
    print(f"ClawHub状态:")
    print(f"  published (已发布):  {s['ch_published']}")
    print(f"  not_uploaded (待传): {s['ch_not_uploaded']}")
    print(f"  not_eligible (不可传): {s['ch_not_eligible']}")
    print(f"  not_applicable(源):  {s['ch_not_applicable']}")
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
        if s.get("is_source"):
            continue
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
        if s.get("is_source"):
            continue
        if not s.get("is_free") and s.get("clawhub", {}).get("status") == "published":
            found.append(slug)
            print(f"  → {slug} (pair: {s.get('pair_slug', 'N/A')})")
    total_paid = sum(1 for s in skills.values() if not s.get("is_source") and not s.get("is_free"))
    pct = len(found)*100//total_paid if total_paid else 0
    print(f"\n共 {len(found)} 个付费版在ClawHub作宣传引流 (总付费版: {total_paid}, 占比: {pct}%)")
    return found

def cmd_find_free_for_clawhub():
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
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
        if s.get("is_source"):
            continue
        if s.get("skillhub", {}).get("review_status") == "rejected":
            found.append(slug)
            print(f"  → {slug}")
    print(f"\n共 {len(found)} 个skill被SkillHub拒绝")

def cmd_find_platform_review():
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        if s.get("skillhub", {}).get("review_status") == "platform_review":
            found.append(slug)
            print(f"  → {slug}")
    print(f"\n共 {len(found)} 个skill在SkillHub平台审核中")

def cmd_find_untraced():
    """查找未追溯到源的生产skill"""
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        origin = s.get("source_origin", {})
        if origin.get("type", "unknown") == "unknown":
            found.append(slug)
        elif not origin.get("original_slug"):
            found.append(slug)
    print(f"共 {len(found)} 个生产skill未追溯到源")
    if len(found) <= 20:
        for slug in found:
            print(f"  → {slug}")
    else:
        for slug in found[:10]:
            print(f"  → {slug}")
        print(f"  ... 还有 {len(found)-10} 个")
    return found

def cmd_find_unpaired():
    """查找未配对的免费/付费skill"""
    db = load_db()
    skills = db["skills"]
    unpaired_free = []
    unpaired_paid = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        if not s.get("pair_slug"):
            if s.get("is_free"):
                unpaired_free.append(slug)
            else:
                unpaired_paid.append(slug)
    print(f"未配对免费版: {len(unpaired_free)}")
    for slug in unpaired_free[:10]:
        print(f"  → {slug}")
    print(f"\n未配对付费版: {len(unpaired_paid)}")
    for slug in unpaired_paid[:10]:
        print(f"  → {slug}")
    if len(unpaired_paid) > 10:
        print(f"  ... 还有 {len(unpaired_paid)-10} 个")

def cmd_source_skills():
    """列出所有源skill及其下载URL"""
    db = load_db()
    skills = db["skills"]
    sources = []
    for slug, s in skills.items():
        if not s.get("is_source"):
            continue
        origin = s.get("source_origin", {})
        sources.append({
            "slug": slug,
            "type": origin.get("type", ""),
            "download_url": origin.get("download_url", ""),
            "github_url": origin.get("github_url", ""),
            "owner": origin.get("owner", ""),
            "downloads": origin.get("source_downloads", 0),
            "production_slugs": s.get("production_slugs", []),
        })
    print(f"源skill总数: {len(sources)}")
    print(f"  ClawHub源: {sum(1 for s in sources if s['type'] == 'clawhub')}")
    print(f"  开源源:   {sum(1 for s in sources if s['type'] == 'opensource')}")
    print(f"\n有生产衍生的源skill: {sum(1 for s in sources if s['production_slugs'])}")
    print(f"无生产衍生的源skill: {sum(1 for s in sources if not s['production_slugs'])}")
    print(f"\n样本 (前10个):")
    for s in sources[:10]:
        print(f"  → {s['slug']} ({s['type']})")
        if s['download_url']:
            print(f"    URL: {s['download_url']}")
        if s['production_slugs']:
            print(f"    生产: {s['production_slugs'][:3]}")
    return sources

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
    elif cmd == "find-untraced":
        cmd_find_untraced()
    elif cmd == "find-unpaired":
        cmd_find_unpaired()
    elif cmd == "source-skills":
        cmd_source_skills()
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)

if __name__ == "__main__":
    main()
