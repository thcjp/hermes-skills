#!/usr/bin/env python3
"""
平台运维工具 v4.0 (Platform Operations Tool)
=============================================
基于本地主数据库 (upload_tracking.json Schema v4.0) 驱动多平台运维。
支持源skill注册、来源追踪、升级管理、完整SkillHub生命周期、slug冲突跟踪、
对外发布自动化、ClawHub运维、Coze平台评估。

核心原则: 本地数据库为唯一权威源，平台操作后更新本地状态。

架构模型:
  源skill (is_source=true, 本地存储, 不上传)
    → 免费版 (SkillHub+ClawHub+HermesSkillsHub都传)
    → 付费版 (SkillHub全传+ClawHub 10%引流+Coze评估)

SkillHub完整生命周期:
  not_uploaded → pending → admin_review → platform_review → published → public_published
                ↓         ↓              ↓                ↓
              rejected  rejected      rejected          (可下架)
                ↓
          slug_conflict → (resolve) → pending

  pending:          三线并行安全审核中 (内容合规+科恩漏洞+云鼎AI安全)
  admin_review:     组织管理员审核 (API可approve/reject)
  platform_review:  平台二次审核 (API无法干预, 需联系skillhub_ipr@tencent.com)
  published:        已上架 (审核通过, 技术层发布)
  public_published: 对外发布 (面向社区公开可见, 可见性层发布)
  rejected:         审核拒绝 (需修改后重新上传)
  slug_conflict:    slug冲突 (技能标识符已被占用, 需改名重传)
  deleted:          已删除

多平台支持:
  SkillHub:  付费+免费, 有SkillPay变现 (企业认证+微信支付)
  ClawHub:   免费为主, 付费版10%引流
  Coze/扣子: 评估中, 有70%分成的付费插件机制
  Hermes:    评估中, Skills Hub有9万+技能但无变现

使用方式:
    python platform_ops.py status              # 查看当前状态概览 (含完整生命周期)
    python platform_ops.py pending             # 列出所有待处理操作 (全生命周期)
    python platform_ops.py lifecycle <slug>    # 查看单个skill的完整生命周期
    python platform_ops.py skillhub-actions    # 生成SkillHub操作清单
    python platform_ops.py clawhub-actions     # 生成ClawHub操作清单
    python platform_ops.py coze-actions        # 生成Coze平台评估清单
    python platform_ops.py mark-pending <slug>...              # 标记SkillHub审核中
    python platform_ops.py mark-approved <slug>...             # 标记SkillHub已审核
    python platform_ops.py mark-platform-review <slug>...      # 标记SkillHub平台审核中
    python platform_ops.py mark-published <slug>...            # 标记SkillHub已上架
    python platform_ops.py mark-public-published <slug>...     # 标记SkillHub对外发布
    python platform_ops.py mark-rejected <slug>...             # 标记SkillHub被拒绝
    python platform_ops.py mark-slug-conflict <slug>...        # 标记slug冲突
    python platform_ops.py resolve-slug-conflict <old> <new>   # 解决slug冲突(改名)
    python platform_ops.py mark-deleted <slug>...              # 标记SkillHub已删除
    python platform_ops.py mark-clawhub-published <slug>...    # 标记ClawHub已发布
    python platform_ops.py mark-clawhub-withdrawn <slug>...    # 标记ClawHub已撤回
    python platform_ops.py find-pending          # 查找pending状态skill
    python platform_ops.py find-slug-conflicts   # 查找slug冲突skill
    python platform_ops.py find-public-publishable # 查找可对外发布的skill
    python platform_ops.py find-promotional      # 查找ClawHub付费版宣传引流情况
    python platform_ops.py find-free-for-clawhub # 查找待上传ClawHub的免费版
    python platform_ops.py find-rejected         # 查找SkillHub被拒绝的skill
    python platform_ops.py find-platform-review  # 查找SkillHub平台审核中的skill
    python platform_ops.py find-untraced         # 查找未追溯到源的生产skill
    python platform_ops.py find-unpaired         # 查找未配对的免费/付费skill
    python platform_ops.py source-skills         # 列出所有源skill及其下载URL
    python platform_ops.py platform-comparison   # 多平台对比分析
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, DATA_DIR, REGISTRY_DIR
# === End Phase 1 ===


import json
import sys
from pathlib import Path
from datetime import datetime

# REGISTRY_DIR imported from config
DB_FILE = DATA_DIR / "upload_tracking.json"
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
        "public_published": 0,
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
        # SkillHub (完整生命周期)
        "sh_pending": 0, "sh_admin_review": 0, "sh_platform_review": 0,
        "sh_published": 0, "sh_public_published": 0, "sh_rejected": 0,
        "sh_slug_conflict": 0, "sh_deleted": 0,
        "sh_not_uploaded": 0, "sh_not_applicable": 0,
        # ClawHub
        "ch_published": 0, "ch_not_uploaded": 0, "ch_not_eligible": 0,
        "ch_withdrawn": 0, "ch_paid_promotional": 0, "ch_not_applicable": 0,
        # Coze (评估中)
        "coze_eligible": 0, "coze_evaluated": 0, "coze_not_eligible": 0,
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
        # 完整生命周期状态统计
        if sh_rs == "pending": stats["sh_pending"] += 1
        elif sh_rs == "admin_review": stats["sh_admin_review"] += 1
        elif sh_rs == "platform_review": stats["sh_platform_review"] += 1
        elif sh_rs == "published": stats["sh_published"] += 1
        elif sh_rs == "public_published": stats["sh_public_published"] += 1
        elif sh_rs == "rejected": stats["sh_rejected"] += 1
        elif sh_rs == "slug_conflict": stats["sh_slug_conflict"] += 1
        elif sh_rs == "deleted": stats["sh_deleted"] += 1
        elif sh_rs == "not_applicable": stats["sh_not_applicable"] += 1
        else: stats["sh_not_uploaded"] += 1

        # 对外发布统计 (兼容旧字段 approved → published)
        if sh_rs == "approved":
            stats["sh_published"] += 1  # approved = published (向后兼容)
        if sh.get("public_published"):
            stats["public_published"] += 1

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
    print(f"技能主数据库 v{meta.get('schema_version', '4.0')} (最后更新: {meta['last_updated']})")
    print(f"{'='*60}")
    print(f"总skill数: {meta['total_skills']}")
    print(f"{'─'*60}")
    print(f"源skill (本地存储, 不上传):")
    print(f"  ClawHub源:  {s['source_clawhub']}")
    print(f"  开源源:    {s['source_opensource']}")
    print(f"  小计:      {s['source_total']}")
    print(f"{'─'*60}")
    print(f"生产skill (可上传):")
    print(f"  包装skill:   {s['production_packaged']}")
    print(f"  差异化skill: {s['production_differentiated']}")
    print(f"  小计:        {s['production_total']}")
    print(f"  有源文件:    {s['has_source_file']}")
    print(f"{'─'*60}")
    print(f"商业属性:")
    print(f"  free (免费版):       {s['free']}")
    print(f"  paid (付费版):       {s['paid']}")
    print(f"  paired (已配对):     {s['paired']}")
    print(f"  unpaired_free:       {s['unpaired_free']}")
    print(f"  unpaired_paid:       {s['unpaired_paid']}")
    print(f"{'─'*60}")
    print(f"源追溯:")
    print(f"  已追溯: {s['traced_to_source']} (ClawHub: {s['traced_clawhub']}, 开源: {s['traced_opensource']}, JueJin: {s['traced_juejin']})")
    print(f"  待追溯: {s['untraced']}")
    print(f"{'─'*60}")
    print(f"SkillHub完整生命周期:")
    print(f"  pending (安全审核中):    {s['sh_pending']}")
    print(f"  admin_review (管理员审核): {s['sh_admin_review']}")
    print(f"  platform_review (平台审核): {s['sh_platform_review']}")
    print(f"  published (已上架):      {s['sh_published']}")
    print(f"  public_published (对外发布): {s['sh_public_published']}")
    print(f"  rejected (被拒绝):       {s['sh_rejected']}")
    print(f"  slug_conflict (slug冲突): {s['sh_slug_conflict']}")
    print(f"  deleted (已删除):        {s['sh_deleted']}")
    print(f"  not_uploaded (未上传):   {s['sh_not_uploaded']}")
    print(f"  not_applicable (源):     {s['sh_not_applicable']}")
    print(f"{'─'*60}")
    print(f"ClawHub状态:")
    print(f"  published (已发布):  {s['ch_published']}")
    print(f"  not_uploaded (待传): {s['ch_not_uploaded']}")
    print(f"  not_eligible (不可传): {s['ch_not_eligible']}")
    print(f"  not_applicable(源):  {s['ch_not_applicable']}")
    if s['ch_paid_promotional'] > 0:
        print(f"  ★ {s['ch_paid_promotional']}个付费版在ClawHub作宣传引流")
    print(f"{'─'*60}")
    print(f"Coze/扣子 (评估中):")
    print(f"  eligible (可上架):   {s.get('coze_eligible', 0)}")
    print(f"  evaluated (已评估):  {s.get('coze_evaluated', 0)}")
    print(f"  not_eligible:        {s.get('coze_not_eligible', 0)}")

def cmd_pending():
    db = load_db()
    skills = db["skills"]

    pending = {
        "skillhub_pending": [],
        "skillhub_admin_review": [],
        "skillhub_rejected": [],
        "skillhub_platform_review": [],
        "skillhub_slug_conflict": [],
        "skillhub_public_publishable": [],
        "clawhub_upload_candidates": [],
        "clawhub_paid_promotional": [],
    }

    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        sh = s.get("skillhub", {})
        ch = s.get("clawhub", {})
        sh_rs = sh.get("review_status", "")

        # 兼容旧状态 approved → published
        if sh_rs == "approved":
            sh_rs = "published"

        if sh_rs == "pending":
            pending["skillhub_pending"].append(slug)
        if sh_rs == "admin_review":
            pending["skillhub_admin_review"].append(slug)
        if sh_rs == "rejected":
            pending["skillhub_rejected"].append(slug)
        if sh_rs == "platform_review":
            pending["skillhub_platform_review"].append(slug)
        if sh_rs == "slug_conflict":
            pending["skillhub_slug_conflict"].append(slug)
        # 已上架但未对外发布的skill
        if sh_rs == "published" and not sh.get("public_published"):
            pending["skillhub_public_publishable"].append(slug)
        if ch.get("upload_eligible") and ch.get("status") == "not_uploaded":
            pending["clawhub_upload_candidates"].append(slug)
        if not s.get("is_free") and ch.get("status") == "published":
            pending["clawhub_paid_promotional"].append(slug)

    print("待处理操作清单 (全生命周期)")
    print(f"{'='*60}")
    print(f"\n1. SkillHub安全审核中 ({len(pending['skillhub_pending'])}个):")
    for slug in pending["skillhub_pending"][:10]:
        print(f"   → {slug}")
    if len(pending["skillhub_pending"]) > 10:
        print(f"   ... 还有 {len(pending['skillhub_pending'])-10} 个")

    print(f"\n2. SkillHub待管理员审核 ({len(pending['skillhub_admin_review'])}个):")
    for slug in pending["skillhub_admin_review"]:
        print(f"   → {slug}")

    print(f"\n3. SkillHub平台审核中 ({len(pending['skillhub_platform_review'])}个):")
    for slug in pending["skillhub_platform_review"][:10]:
        print(f"   → {slug}")
    if len(pending["skillhub_platform_review"]) > 10:
        print(f"   ... 还有 {len(pending['skillhub_platform_review'])-10} 个")
    if pending["skillhub_platform_review"]:
        print(f"   ⚠ API无法干预, 需联系 skillhub_ipr@tencent.com")

    print(f"\n4. SkillHub被拒绝 ({len(pending['skillhub_rejected'])}个):")
    for slug in pending["skillhub_rejected"]:
        print(f"   → {slug}")

    print(f"\n5. SkillHub slug冲突 ({len(pending['skillhub_slug_conflict'])}个):")
    for slug in pending["skillhub_slug_conflict"]:
        old_slug = skills[slug].get("skillhub", {}).get("conflict_detail", "")
        print(f"   → {slug}" + (f" ({old_slug})" if old_slug else ""))

    print(f"\n6. SkillHub可对外发布 ({len(pending['skillhub_public_publishable'])}个):")
    for slug in pending["skillhub_public_publishable"][:10]:
        print(f"   → {slug}")
    if len(pending["skillhub_public_publishable"]) > 10:
        print(f"   ... 还有 {len(pending['skillhub_public_publishable'])-10} 个")
    if pending["skillhub_public_publishable"]:
        print(f"   操作: 在SkillHub团队空间设置技能可见性为'公开'")

    print(f"\n7. ClawHub待上传免费版 ({len(pending['clawhub_upload_candidates'])}个):")
    if len(pending["clawhub_upload_candidates"]) <= 20:
        for slug in pending["clawhub_upload_candidates"]:
            print(f"   → {slug}")
    else:
        for slug in pending["clawhub_upload_candidates"][:10]:
            print(f"   → {slug}")
        print(f"   ... 还有 {len(pending['clawhub_upload_candidates'])-10} 个")

    print(f"\n8. ClawHub付费版宣传引流 ({len(pending['clawhub_paid_promotional'])}个):")
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
    """标记SkillHub已审核通过 (approved = published, 向后兼容)"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "published"
            db["skills"][slug]["skillhub"]["reviewed_at"] = NOW
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            db["skills"][slug]["skillhub"]["notes"] = ""
            # 更新生命周期
            db["skills"][slug]["lifecycle"]["stage"] = "published"
            db["skills"][slug]["lifecycle"]["last_modified"] = NOW
            print(f"  ✅ {slug} → published (已上架)")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)
    print(f"\n已更新 {len(slugs)} 个skill状态")

def cmd_mark_pending(slugs):
    """标记SkillHub安全审核中 (pending)"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "pending"
            db["skills"][slug]["skillhub"]["uploaded"] = True
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            print(f"  🔄 {slug} → pending (安全审核中)")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)

def cmd_mark_platform_review(slugs):
    """标记SkillHub平台审核中 (platform_review)"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "platform_review"
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            db["skills"][slug]["skillhub"]["notes"] = "平台二次审核, API无法干预"
            print(f"  ⏳ {slug} → platform_review (平台审核中)")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)

def cmd_mark_published(slugs):
    """标记SkillHub已上架 (published)"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "published"
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            db["skills"][slug]["lifecycle"]["stage"] = "published"
            db["skills"][slug]["lifecycle"]["last_modified"] = NOW
            print(f"  ✅ {slug} → published (已上架)")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)

def cmd_mark_public_published(slugs):
    """标记SkillHub对外发布 (public_published)"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "public_published"
            db["skills"][slug]["skillhub"]["public_published"] = True
            db["skills"][slug]["skillhub"]["public_published_at"] = NOW
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            db["skills"][slug]["lifecycle"]["stage"] = "public_published"
            db["skills"][slug]["lifecycle"]["last_modified"] = NOW
            print(f"  🌐 {slug} → public_published (对外发布)")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)

def cmd_mark_rejected(slugs):
    """标记SkillHub被拒绝 (rejected)"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "rejected"
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            print(f"  ❌ {slug} → rejected (被拒绝)")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)

def cmd_mark_slug_conflict(slugs):
    """标记slug冲突 (slug_conflict)"""
    db = load_db()
    for slug in slugs:
        if slug in db["skills"]:
            db["skills"][slug]["skillhub"]["review_status"] = "slug_conflict"
            db["skills"][slug]["skillhub"]["last_sync"] = NOW
            db["skills"][slug]["skillhub"]["conflict_detected_at"] = NOW
            print(f"  ⚠ {slug} → slug_conflict (标识符已被占用)")
        else:
            print(f"  ⚠ {slug} 不在数据库中")
    save_db(db)

def cmd_resolve_slug_conflict(old_slug, new_slug):
    """解决slug冲突 - 改名后重新上传"""
    db = load_db()
    if old_slug not in db["skills"]:
        print(f"  ⚠ {old_slug} 不在数据库中")
        return

    # 复制旧记录到新slug
    old_skill = db["skills"][old_slug]
    new_skill = json.loads(json.dumps(old_skill))  # deep copy
    new_skill["slug"] = new_slug
    new_skill["skillhub"]["review_status"] = "pending"
    new_skill["skillhub"]["uploaded"] = False
    new_skill["skillhub"]["last_sync"] = NOW
    new_skill["skillhub"]["conflict_resolved_from"] = old_slug
    new_skill["skillhub"]["notes"] = f"从 {old_slug} 改名解决slug冲突"

    # 旧记录标记为slug_conflict_resolved
    old_skill["skillhub"]["review_status"] = "deleted"
    old_skill["skillhub"]["conflict_resolved_to"] = new_slug
    old_skill["skillhub"]["notes"] = f"slug冲突, 已改名为 {new_slug}"

    db["skills"][new_slug] = new_skill

    save_db(db)
    print(f"  ✅ {old_slug} → {new_slug} (slug冲突已解决)")
    print(f"  新slug已标记为pending, 需要重新上传到SkillHub")

def cmd_find_pending():
    """查找pending状态skill"""
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        rs = s.get("skillhub", {}).get("review_status", "")
        if rs in ("pending", "approved"):  # approved可能是旧的pending状态
            found.append(slug)
    print(f"共 {len(found)} 个skill在SkillHub安全审核中")
    for slug in found[:20]:
        print(f"  → {slug}")
    if len(found) > 20:
        print(f"  ... 还有 {len(found)-20} 个")

def cmd_find_slug_conflicts():
    """查找slug冲突skill"""
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        if s.get("skillhub", {}).get("review_status") == "slug_conflict":
            detail = s.get("skillhub", {}).get("conflict_detail", "")
            found.append((slug, detail))
    print(f"共 {len(found)} 个skill存在slug冲突")
    for slug, detail in found:
        print(f"  → {slug}" + (f" ({detail})" if detail else ""))
    if found:
        print(f"\n解决方式: python platform_ops.py resolve-slug-conflict <old_slug> <new_slug>")

def cmd_find_public_publishable():
    """查找可对外发布的skill (已上架但未对外发布)"""
    db = load_db()
    skills = db["skills"]
    found = []
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        sh = s.get("skillhub", {})
        rs = sh.get("review_status", "")
        # 已上架(published或approved)但未对外发布
        if rs in ("published", "approved") and not sh.get("public_published"):
            found.append(slug)
    print(f"共 {len(found)} 个skill已上架但未对外发布")
    for slug in found[:20]:
        print(f"  → {slug}")
    if len(found) > 20:
        print(f"  ... 还有 {len(found)-20} 个")
    if found:
        print(f"\n操作: 在SkillHub团队空间中设置技能可见性为'公开'")
        print(f"标记: python platform_ops.py mark-public-published <slug>...")

def cmd_lifecycle(slug):
    """查看单个skill的完整生命周期"""
    db = load_db()
    if slug not in db["skills"]:
        print(f"  ⚠ {slug} 不在数据库中")
        return

    s = db["skills"][slug]
    print(f"Skill: {slug}")
    print(f"{'='*60}")
    print(f"类型: {'源skill' if s.get('is_source') else '生产skill'}")
    print(f"免费/付费: {'免费' if s.get('is_free') else '付费'}")
    if s.get("pair_slug"):
        print(f"配对: {s['pair_slug']}")
    print()

    # SkillHub生命周期
    sh = s.get("skillhub", {})
    rs = sh.get("review_status", "not_uploaded")
    print(f"SkillHub生命周期:")
    stages = [
        ("not_uploaded", "未上传"),
        ("pending", "安全审核中"),
        ("admin_review", "管理员审核"),
        ("platform_review", "平台审核"),
        ("published", "已上架"),
        ("public_published", "对外发布"),
    ]
    for code, name in stages:
        marker = " ← 当前" if rs == code else ""
        if code == "published" and rs == "approved":
            marker = " ← 当前 (approved=published)"
        print(f"  {name:15s} ({code}){marker}")

    if rs in ("rejected", "slug_conflict", "deleted"):
        print(f"\n  ⚠ 当前状态: {rs}")
        if rs == "rejected":
            print(f"  需修改内容后重新上传")
        elif rs == "slug_conflict":
            print(f"  需改名后重新上传")
            print(f"  解决: python platform_ops.py resolve-slug-conflict {slug} <new_slug>")
        elif rs == "deleted":
            print(f"  已从SkillHub删除")

    if sh.get("reviewed_at"):
        print(f"\n  审核时间: {sh['reviewed_at']}")
    if sh.get("public_published_at"):
        print(f"  对外发布时间: {sh['public_published_at']}")
    if sh.get("last_sync"):
        print(f"  最后同步: {sh['last_sync']}")
    if sh.get("notes"):
        print(f"  备注: {sh['notes']}")

    # ClawHub状态
    ch = s.get("clawhub", {})
    print(f"\nClawHub状态: {ch.get('status', 'not_uploaded')}")
    if ch.get("last_sync"):
        print(f"  最后同步: {ch['last_sync']}")

    # 质量审计
    func = s.get("quality", {}).get("functional", {})
    sell = s.get("quality", {}).get("sellability", {})
    auth = s.get("quality", {}).get("authenticity", {})
    if func or sell or auth:
        print(f"\n质量审计:")
        if func:
            print(f"  功能质量: {func.get('grade', '?')} ({func.get('score', 0)}分)")
        if sell:
            print(f"  可销售性: {sell.get('grade', '?')} ({sell.get('score', 0)}分)")
        if auth:
            print(f"  内容真实性: {auth.get('grade', '?')} ({auth.get('score', 0)}分)")

def cmd_coze_actions():
    """生成Coze平台评估清单"""
    db = load_db()
    skills = db["skills"]
    actions = {"paid_eligible": [], "free_eligible": [], "not_eligible": []}

    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        # Coze适合付费skill (70%分成) 和高流量免费skill (引流)
        sh = s.get("skillhub", {})
        rs = sh.get("review_status", "")
        if rs in ("published", "approved", "public_published"):
            if s.get("is_free"):
                actions["free_eligible"].append(slug)
            else:
                actions["paid_eligible"].append(slug)

    output_file = REGISTRY_DIR / "coze_pending_actions.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(actions, f, ensure_ascii=False, indent=2)

    print(f"Coze平台评估清单已生成: {output_file}")
    print(f"  付费skill (可70%分成): {len(actions['paid_eligible'])}个")
    print(f"  免费skill (引流): {len(actions['free_eligible'])}个")
    print(f"\nCoze变现模式:")
    print(f"  - 付费插件售卖 (创作者分成70%)")
    print(f"  - 智能体内订阅付费 (创作者留存70-80%)")
    print(f"  - 付费模板售卖")
    print(f"  - 官方创作者激励 (现金+算力)")
    print(f"  - 生态合伙人分销 (永久15%分成)")

def cmd_platform_comparison():
    """多平台对比分析"""
    print("="*70)
    print("多平台对比分析")
    print("="*70)
    print()
    print(f"{'平台':<12} {'市场':<8} {'变现':<8} {'分成':<12} {'适合':<20}")
    print(f"{'─'*70}")
    print(f"{'SkillHub':<12} {'✅':<8} {'✅ SkillPay':<12} {'按次计费':<12} {'付费+免费':<20}")
    print(f"{'ClawHub':<12} {'✅':<8} {'❌':<8} {'-':<12} {'免费引流':<20}")
    print(f"{'Coze/扣子':<12} {'✅':<8} {'✅ 最完善':<12} {'70%分成':<12} {'付费+免费':<20}")
    print(f"{'Hermes':<12} {'✅ 9万+':<8} {'❌':<8} {'-':<12} {'免费推广':<20}")
    print(f"{'n8n':<12} {'✅ 社区':<8} {'❌':<8} {'-':<12} {'免费推广':<20}")
    print(f"{'Dify':<12} {'✅ 成熟':<8} {'⚠ 有限':<12} {'Partner':<12} {'免费引流':<20}")
    print(f"{'FastGPT':<12} {'❌':<8} {'❌':<8} {'-':<12} {'不适合':<20}")
    print(f"{'LangChain':<12} {'⚠ Hub':<8} {'❌':<8} {'-':<12} {'不适合':<20}")
    print()
    print("结论:")
    print("  1. SkillHub: 主力变现平台 (SkillPay + 微信支付)")
    print("  2. Coze/扣子: 最佳第二变现平台 (70%分成, 多种变现路径)")
    print("  3. ClawHub: 免费引流平台 (付费版10%作宣传)")
    print("  4. Hermes: 免费推广平台 (9万+技能生态, 无变现)")
    print("  5. Dify: 评估Partner计划 (Marketplace成熟但无直接变现)")
    print("  6. n8n/FastGPT/LangChain: 不适合技能市场")

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
    elif cmd == "lifecycle":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py lifecycle <slug>")
            return
        cmd_lifecycle(sys.argv[2])
    elif cmd == "skillhub-actions":
        cmd_skillhub_actions()
    elif cmd == "clawhub-actions":
        cmd_clawhub_actions()
    elif cmd == "coze-actions":
        cmd_coze_actions()
    elif cmd == "platform-comparison":
        cmd_platform_comparison()
    elif cmd == "mark-pending":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-pending <slug> [slug...]")
            return
        cmd_mark_pending(sys.argv[2:])
    elif cmd == "mark-approved":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-approved <slug> [slug...]")
            return
        cmd_mark_approved(sys.argv[2:])
    elif cmd == "mark-platform-review":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-platform-review <slug> [slug...]")
            return
        cmd_mark_platform_review(sys.argv[2:])
    elif cmd == "mark-published":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-published <slug> [slug...]")
            return
        cmd_mark_published(sys.argv[2:])
    elif cmd == "mark-public-published":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-public-published <slug> [slug...]")
            return
        cmd_mark_public_published(sys.argv[2:])
    elif cmd == "mark-rejected":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-rejected <slug> [slug...]")
            return
        cmd_mark_rejected(sys.argv[2:])
    elif cmd == "mark-slug-conflict":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py mark-slug-conflict <slug> [slug...]")
            return
        cmd_mark_slug_conflict(sys.argv[2:])
    elif cmd == "resolve-slug-conflict":
        if len(sys.argv) < 4:
            print("用法: python platform_ops.py resolve-slug-conflict <old_slug> <new_slug>")
            return
        cmd_resolve_slug_conflict(sys.argv[2], sys.argv[3])
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
    elif cmd == "find-pending":
        cmd_find_pending()
    elif cmd == "find-slug-conflicts":
        cmd_find_slug_conflicts()
    elif cmd == "find-public-publishable":
        cmd_find_public_publishable()
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
