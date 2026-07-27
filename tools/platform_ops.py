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
    python platform_ops.py star <slug>...        # 收藏skill (Star API)
    python platform_ops.py batch-approve [slug...]# 批量审核通过pending (无参数=全部)
    python platform_ops.py handle-rejected <slug># 分析被拒绝skill的原因并给建议
    python platform_ops.py platform-status <slug># 查询skill平台实时状态(含前台可见性)
    python platform_ops.py pipeline <slug>        # 一键流水线: 查询→审核→收藏→标记
    python platform_ops.py auto-publish <slug>...  # 自动发布到社区: 查询→审核→社区发布→收藏
    python platform_ops.py publish-community <slug>... # 单独发布到社区(visibility=public)
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, DATA_DIR, REGISTRY_DIR
# === End Phase 1 ===


import json
import sys
import time
import sqlite3
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import HTTPError

# REGISTRY_DIR imported from config
DB_FILE = DATA_DIR / "upload_tracking.json"
NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# ============ SkillHub API配置 (复用enterprise_uploader的认证) ============
_API_BASE = "https://api.skillhub.cn/api/v1"
_ADMIN_ORG_ID = 862

def _load_api_auth():
    """加载SkillHub API认证 — 复用enterprise_uploader的load_cookies"""
    try:
        from enterprise_uploader import load_cookies
        cookies = load_cookies()
        if not cookies:
            return None, None
        if cookies.startswith('BEARER:'):
            api_key = cookies[len('BEARER:'):]
            return None, {'Authorization': f'Bearer {api_key}', 'Accept': 'application/json'}
        return cookies, {'Cookie': cookies, 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}
    except Exception:
        return None, None

def _api_request(method, url, headers, data=None, timeout=30):
    """统一API请求封装"""
    req = Request(url, data=data, method=method, headers=headers)
    try:
        with urlopen(req, timeout=timeout) as resp:
            return True, json.loads(resp.read().decode('utf-8'))
    except HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')[:500]
        return False, {'error': f'HTTP {e.code}: {body}'}
    except Exception as e:
        return False, {'error': str(e)}

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

# ============ 统一平台操作API (P1-1: 平台操作固化) ============
# 将散落在batch_approve_api.py、auto_publish.py等脚本中的操作统一为单一入口
# 向后兼容: 现有脚本仍可独立运行

def star_skill(slug: str) -> dict:
    """收藏SkillHub上的skill (复用V63发现的Star API)
    
    API: POST /api/v1/skills/{slug}/star
    """
    cookies, headers = _load_api_auth()
    if not cookies and not headers:
        return {'success': False, 'slug': slug, 'error': '无认证凭证'}
    
    url = f"{_API_BASE}/skills/{slug}/star"
    success, result = _api_request('POST', url, headers, data=b'{}')
    
    if success:
        # 同步到本地DB
        db = load_db()
        if slug in db['skills']:
            db['skills'][slug].setdefault('skillhub', {})['starred'] = True
            db['skills'][slug]['skillhub']['starred_at'] = NOW
            save_db(db)
        return {'success': True, 'slug': slug, 'message': '已收藏'}
    else:
        return {'success': False, 'slug': slug, 'error': result.get('error', 'unknown')}

def batch_approve(slugs: list = None, delay: float = 0.3) -> dict:
    """批量审核通过SkillHub pending skills (复用batch_approve_api逻辑)
    
    API: POST /orgs/{ORG_ID}/admin/skills/{slug}/approve
    如果slugs为None, 自动获取所有pending skill
    """
    cookies, headers = _load_api_auth()
    if not cookies and not headers:
        return {'success': False, 'error': '无认证凭证'}
    
    # 如果没传slugs, 自动获取所有pending
    if slugs is None:
        url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?reviewStatus=pending&page=1&pageSize=1"
        success, data = _api_request('GET', url, headers)
        if not success:
            return {'success': False, 'error': f'获取pending列表失败: {data.get("error")}'}
        total = data.get('total', 0)
        if total == 0:
            return {'success': True, 'approved': 0, 'message': '无pending skill'}
        
        # 分页获取所有pending slug
        # H2修复: reviewStatus=pending API过滤器可能不生效, 需客户端二次过滤
        slugs = []
        pages = (total // 100) + 1
        for page in range(1, pages + 1):
            url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?reviewStatus=pending&page={page}&pageSize=100"
            success, data = _api_request('GET', url, headers)
            if not success:
                break
            for sk in data.get('skills', []):
                slug = sk.get('slug', '')
                # 客户端二次过滤: 仅保留reviewStatus确实为pending的skill
                rs = sk.get('reviewStatus', sk.get('review_status', ''))
                if slug and rs == 'pending':
                    slugs.append(slug)
                elif slug and rs != 'pending':
                    # API过滤器未生效, 返回了非pending的skill, 跳过
                    pass
            if page % 5 == 0:
                print(f"  已扫描 {page}/{pages} 页, 收集 {len(slugs)} 个pending")
    
    if not slugs:
        return {'success': True, 'approved': 0, 'message': '无pending skill'}
    
    print(f"待审核: {len(slugs)} 个")
    approved = []
    failed = []
    
    for i, slug in enumerate(slugs):
        url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{slug}/approve"
        success, result = _api_request('POST', url, headers, data=b'{}', timeout=15)
        
        if success:
            approved.append(slug)
        else:
            failed.append({'slug': slug, 'error': result.get('error', 'unknown')})
        
        if (i + 1) % 50 == 0:
            print(f"  [{i+1}/{len(slugs)}] 成功={len(approved)}, 失败={len(failed)}")
        if delay > 0 and (i + 1) % 10 == 0:
            time.sleep(delay)
    
    # 同步到本地DB
    db = load_db()
    for slug in approved:
        if slug in db['skills']:
            db['skills'][slug].setdefault('skillhub', {})['review_status'] = 'published'
            db['skills'][slug]['skillhub']['reviewed_at'] = NOW
            db['skills'][slug].setdefault('lifecycle', {})['stage'] = 'published'
    save_db(db)
    
    print(f"\n=== 批量审核完成 ===")
    print(f"✅ 成功: {len(approved)}")
    print(f"❌ 失败: {len(failed)}")
    
    return {'success': len(failed) == 0, 'approved': approved, 'failed': failed}

def handle_rejected(slug: str) -> dict:
    """处理被拒绝的skill — 分析原因并给出修复建议
    
    复用auto_publish.py的retry_rejected逻辑
    """
    db = load_db()
    if slug not in db['skills']:
        return {'success': False, 'slug': slug, 'error': '不在数据库中'}
    
    skill = db['skills'][slug]
    sh = skill.get('skillhub', {})
    rs = sh.get('review_status', '')
    
    if rs != 'rejected':
        return {'success': False, 'slug': slug, 'error': f'当前状态不是rejected ({rs})'}
    
    # 分析拒绝原因
    notes = sh.get('notes', '')
    analysis = {
        'slug': slug,
        'status': rs,
        'notes': notes,
        'actions': [],
    }
    
    # 常见拒绝原因和修复建议
    if len(slug) <= 4:
        analysis['actions'].append(f'名称太短, 建议改名: {slug}-tool 或 {slug}-assistant')
        analysis['needs_rename'] = True
    elif 'slug' in notes.lower() or 'conflict' in notes.lower():
        analysis['actions'].append('slug冲突, 需改名为唯一slug')
        analysis['needs_rename'] = True
    
    # 检查SKILL.md内容质量
    from pathlib import Path as _P
    skill_md = None
    for search_dir in [_P(r'D:\skills\packaged-skills\skillhub'),
                       _P(r'D:\skills\enterprise-upload')]:
        candidate = search_dir / slug / 'SKILL.md'
        if candidate.exists():
            skill_md = candidate
            break
    
    if skill_md:
        content = skill_md.read_text(encoding='utf-8', errors='replace')
        if len(content) < 200:
            analysis['actions'].append(f'内容过短({len(content)}字符), 需扩充')
        if 'TODO' in content or 'FIXME' in content or 'placeholder' in content.lower():
            analysis['actions'].append('含占位符/TODO标记, 需清除')
        analysis['content_length'] = len(content)
        analysis['skill_md_path'] = str(skill_md)
    else:
        analysis['actions'].append('SKILL.md文件未找到')
    
    if not analysis['actions']:
        analysis['actions'].append('未知拒绝原因, 建议检查内容后DELETE+重传')
    
    # 标记为需处理
    sh['needs_fix'] = True
    sh['fix_actions'] = analysis['actions']
    save_db(db)
    
    return {'success': True, 'slug': slug, 'analysis': analysis}

def get_platform_status(slug: str) -> dict:
    """查询skill在SkillHub平台的实时状态 (统一状态查询)"""
    cookies, headers = _load_api_auth()
    if not cookies and not headers:
        return {'success': False, 'slug': slug, 'error': '无认证凭证'}
    
    # 1. 查询Admin API获取审核状态
    url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?slug={slug}&page=1&pageSize=1"
    success, data = _api_request('GET', url, headers)
    
    platform_info = {'slug': slug, 'timestamp': NOW}
    
    if success and data.get('skills'):
        skill = data['skills'][0]
        platform_info.update({
            'review_status': skill.get('reviewStatus', 'unknown'),
            'visibility': skill.get('visibility', 'unknown'),
            'download_ready': skill.get('downloadReady', False),
            'namespace': skill.get('namespace', ''),
            'version': skill.get('version', ''),
            'downloads': skill.get('downloadCount', 0),
            'stars': skill.get('starCount', 0),
        })
    else:
        platform_info['admin_error'] = data.get('error', 'API查询失败')
    
    # 2. 查询公开API获取前台可见性
    url2 = f"{_API_BASE}/skills/{slug}"
    success2, data2 = _api_request('GET', url2, headers)
    if success2:
        platform_info['front_visible'] = True
        platform_info['front_data'] = {
            'name': data2.get('name', ''),
            'summary': data2.get('summary', ''),
            'version': data2.get('version', ''),
        }
    else:
        platform_info['front_visible'] = False
        platform_info['front_error'] = data2.get('error', '')
    
    # 3. 本地DB状态
    db = load_db()
    if slug in db['skills']:
        sh = db['skills'][slug].get('skillhub', {})
        platform_info['db_status'] = sh.get('review_status', 'not_uploaded')
        platform_info['db_starred'] = sh.get('starred', False)
    
    platform_info['success'] = True
    return platform_info

def run_platform_pipeline(slug: str) -> dict:
    """一键执行平台操作流水线: 查询状态 → 审核 → 收藏 → 标记发布
    
    自动化流程:
    1. 查询平台状态
    2. 如果pending, 自动approve
    3. 如果published, 自动star
    4. 更新本地DB
    """
    result = {'slug': slug, 'timestamp': NOW, 'steps': {}}
    
    # Step 1: 查询状态
    status = get_platform_status(slug)
    result['steps']['status'] = status
    if not status.get('success'):
        result['status'] = 'failed'
        result['error'] = '状态查询失败'
        return result
    
    review_status = status.get('review_status', 'unknown')
    result['current_status'] = review_status
    
    # Step 2: 如果pending, 审核通过
    if review_status == 'pending':
        print(f"  [{slug}] pending → approving...")
        approve_result = batch_approve([slug])
        result['steps']['approve'] = approve_result
        if approve_result.get('success') and slug in approve_result.get('approved', []):
            review_status = 'published'
        else:
            result['status'] = 'approve_failed'
            return result
    
    # Step 3: 如果published, 收藏
    if review_status in ('published', 'approved', 'public_published'):
        if not status.get('db_starred'):
            print(f"  [{slug}] published → starring...")
            star_result = star_skill(slug)
            result['steps']['star'] = star_result
        else:
            result['steps']['star'] = {'success': True, 'message': 'already starred'}
    
    # Step 4: 检查前台可见性
    if not status.get('front_visible'):
        result['steps']['visibility_warning'] = 'skill在前台不可见, 可能需要设置visibility=public'
    
    result['status'] = 'completed'
    return result

# ============ auto_publish: 自动发布到社区 (P1-1补全) ============
# 复用auto_publish.py的publish-to-community逻辑, 集成到platform_ops统一入口
# 解决企业页可见性问题: published → public (前台可见)

_ADMIN_PUBLISHER_ID = 742  # SkillHub发布者Profile ID

def publish_to_community(slug: str) -> dict:
    """将已上架skill发布到社区 (设置visibility=public)
    
    完整流程(v2.3增强):
      1. 先尝试直接publish-to-community
      2. 如果409 slug_conflict:
         a. unpublish-from-community (取消已有对外发布)
         b. 依次尝试rename-slug到 xxx-sk, xxx-sk1, xxx-sk2
         c. rename成功后publish-to-community
    
    API:
      - POST /orgs/{ORG_ID}/admin/skills/{slug}/publish-to-community
      - POST /orgs/{ORG_ID}/admin/skills/{slug}/unpublish-from-community
      - PUT  /orgs/{ORG_ID}/admin/skills/{slug}/rename-slug
    
    参数:
        slug: skill slug
    
    返回:
        {'success': bool, 'slug': str, 'message': str}
    """
    cookies, headers = _load_api_auth()
    if not cookies and not headers:
        return {'success': False, 'slug': slug, 'error': '无认证凭证'}
    
    if headers.get('Content-Type') is None:
        headers['Content-Type'] = 'application/json'
    body = json.dumps({'publisherProfileId': _ADMIN_PUBLISHER_ID}).encode('utf-8')
    
    # Step 1: 直接尝试publish
    url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{slug}/publish-to-community"
    success, result = _api_request('POST', url, headers, data=body, timeout=30)
    
    if success:
        _update_db_community_published(slug, slug)
        return {'success': True, 'slug': slug, 'message': '已发布到社区(visibility=public)'}
    
    # Step 2: slug冲突 → unpublish + rename + publish
    err_str = str(result.get('error', ''))
    if '409' not in err_str and 'slug' not in err_str.lower() and 'conflict' not in err_str.lower():
        return {'success': False, 'slug': slug, 'error': err_str}
    
    # 2a: unpublish-from-community
    unpub_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{slug}/unpublish-from-community"
    _api_request('POST', unpub_url, headers, data=b'{}', timeout=15)
    time.sleep(0.2)
    
    # 2b: 尝试多个后缀 (C2修复: 清理已有-sk*后缀避免畸形slug如 foo-sk-sk1)
    # 先从输入slug中剥离已有的-sk/-sk1/-sk2/-sk3后缀, 得到干净的基础slug
    base_slug = slug
    for existing_suffix in ['-sk3', '-sk2', '-sk1', '-sk']:
        if base_slug.endswith(existing_suffix) and len(base_slug) > len(existing_suffix):
            base_slug = base_slug[:-len(existing_suffix)]
            break

    current_slug = slug
    for suffix in ['-sk', '-sk1', '-sk2', '-sk3']:
        if current_slug.endswith(suffix):
            continue
        new_slug = base_slug + suffix  # 基于清理后的base_slug生成, 避免畸形叠加
        rename_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{current_slug}/rename-slug"
        rename_body = json.dumps({'newSlug': new_slug}).encode('utf-8')
        rename_success, rename_result = _api_request('PUT', rename_url, headers, data=rename_body, timeout=15)
        
        if rename_success:
            current_slug = new_slug  # 更新current_slug
            time.sleep(0.2)
            retry_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{new_slug}/publish-to-community"
            retry_success, retry_result = _api_request('POST', retry_url, headers, data=body, timeout=30)
            if retry_success:
                _update_db_community_published(slug, new_slug)
                return {'success': True, 'slug': new_slug, 'original_slug': slug,
                        'message': f'slug冲突,已改名为{new_slug}并发布到社区'}
            # publish失败,继续尝试下一个后缀(此时current_slug=new_slug)
        # rename失败(409=已占用),继续尝试下一个后缀
    
    # C1修复增强: 如果rename成功过, current_slug可能已不同于原始slug
    # 返回current_slug而非原始slug, 让调用方知道平台上的实际slug
    if current_slug != slug:
        return {'success': False, 'slug': current_slug, 'original_slug': slug,
                'error': f'slug已改名为{current_slug}但发布到社区失败: {err_str}'}
    return {'success': False, 'slug': slug, 'error': f'slug冲突且所有后缀(-sk/-sk1/-sk2/-sk3)均被占用: {err_str}'}


def _update_db_community_published(original_slug: str, community_slug: str):
    """更新本地DB中的社区发布状态"""
    try:
        db = load_db()
        if original_slug in db['skills']:
            sh = db['skills'][original_slug].setdefault('skillhub', {})
            sh['review_status'] = 'public_published'
            sh['public_published'] = True
            sh['public_published_at'] = NOW
            sh['last_sync'] = NOW
            if community_slug != original_slug:
                sh['community_slug'] = community_slug
            db['skills'][original_slug].setdefault('lifecycle', {})['stage'] = 'public_published'
            save_db(db)
    except Exception:
        pass

def batch_republish_to_community(limit: int = 0, delay: float = 0.5) -> dict:
    """批量重新发布到社区 — 修复"已发布但前台不可见"的2022个skill

    根因: 之前的upload_skill未调用publish_to_community, 导致visibility=org_only
    此函数扫描admin API中所有skill, 对非public的逐一重新发布

    流程:
      1. 分页获取所有admin skill
      2. 筛选 visibility != 'public' 的skill
      3. 对每个调用 publish_to_community(slug)
      4. 记录结果到JSON + SQLite

    参数:
        limit: 最多处理多少个 (0=全部)
        delay: 每个skill之间的延迟(秒)

    返回:
        {'total': N, 'processed': N, 'success': N, 'failed': N, 'already_public': N}
    """
    cookies, headers = _load_api_auth()
    if not cookies and not headers:
        return {'success': False, 'error': '无认证凭证'}

    if headers.get('Content-Type') is None:
        headers['Content-Type'] = 'application/json'

    # 1. 分页获取所有skill
    all_skills = []
    page = 1
    while True:
        url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills?page={page}&pageSize=100"
        success, data = _api_request('GET', url, headers, timeout=30)
        if not success:
            print(f"获取admin skill列表失败: {data.get('error', '')}")
            break
        skills = data.get('skills', [])
        if not skills:
            break
        all_skills.extend(skills)
        total = data.get('total', 0)
        if len(all_skills) >= total:
            break
        if page % 5 == 0:
            print(f"  已扫描 {page} 页, {len(all_skills)}/{total}")
        page += 1

    print(f"\n总共获取 {len(all_skills)} 个skill")

    # 2. 筛选非public的skill
    needs_republish = []
    already_public = 0
    for sk in all_skills:
        visibility = sk.get('visibility', '')
        if visibility != 'public':
            needs_republish.append(sk.get('slug', ''))
        else:
            already_public += 1

    print(f"需要重新发布: {len(needs_republish)} 个")
    print(f"已是public: {already_public} 个")

    if limit > 0:
        needs_republish = needs_republish[:limit]
        print(f"限制处理: {len(needs_republish)} 个")

    # 3. 批量发布
    success_count = 0
    failed_count = 0
    renamed_count = 0
    failed_list = []

    for i, slug in enumerate(needs_republish, 1):
        result = publish_to_community(slug)

        if result.get('success'):
            success_count += 1
            if result.get('original_slug'):
                renamed_count += 1
                print(f"  [{i}/{len(needs_republish)}] {slug} → {result['slug']} ✓ (改名+发布)")
            else:
                print(f"  [{i}/{len(needs_republish)}] {slug} ✓")
        else:
            failed_count += 1
            failed_list.append({'slug': slug, 'error': result.get('error', '')[:100]})
            err = result.get('error', '')[:60]
            print(f"  [{i}/{len(needs_republish)}] {slug} ✗ {err}")

        if delay > 0 and i % 10 == 0:
            time.sleep(delay)
        elif i % 50 == 0:
            print(f"  --- 进度: {i}/{len(needs_republish)} ---")

    # 4. 汇总
    summary = {
        'total': len(all_skills),
        'needs_republish': len(needs_republish),
        'processed': len(needs_republish),
        'success': success_count,
        'failed': failed_count,
        'renamed': renamed_count,
        'already_public': already_public,
        'failed_list': failed_list[:20],
    }

    print(f"\n=== 批量重新发布完成 ===")
    print(f"总skill数: {summary['total']}")
    print(f"需要重新发布: {summary['needs_republish']}")
    print(f"✅ 成功: {success_count}")
    print(f"✗ 失败: {failed_count}")
    print(f"改名: {renamed_count}")
    print(f"已是public: {already_public}")

    return summary

def check_banned_skills(limit: int = 0, use_admin_verify: bool = True) -> dict:
    """检查被封禁的skill — 通过公开API检测404 + admin API交叉验证

    H1修复: 之前仅凭公开API 404判定封禁, 但404可能意味着:
      (a) 曾发布到社区后被封禁(真封禁)
      (b) 仅上传到组织(visibility=org_only), 从未发布到公开社区(非封禁)
      (c) 仍处于pending审核状态(非封禁)
      (d) slug已被改名(非封禁, 需用新slug查询)

    修复: 对404结果使用admin API交叉验证:
      - admin API也404/不存在 → 确认 'banned'(真封禁)
      - admin API存在但visibility != 'public' → 标记 'never_published'(非封禁)
      - admin API存在且visibility == 'public' → 标记 'inconsistent'(异常,需人工排查)
      - admin API存在且reviewStatus == 'pending' → 标记 'pending_review'(非封禁)

    参数:
        limit: 最多检查多少个 (0=全部)
        use_admin_verify: 是否使用admin API交叉验证(需要认证)

    返回:
        {'checked': N, 'accessible': N, 'banned': N, 'never_published': N,
         'banned_slugs': [...], 'never_published_slugs': [...]}
    """
    import sqlite3 as _sqlite3

    DB_PATH = _Path(__file__).resolve().parent.parent / "skill-registry.db"

    # 1. 从DB获取所有synced_from_skillhub的slug
    conn = _sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON")
    rows = conn.execute("""
        SELECT slug FROM skills 
        WHERE current_status = 'synced_from_skillhub'
        ORDER BY slug
    """).fetchall()
    conn.close()

    all_slugs = [r[0] for r in rows]
    if limit > 0:
        all_slugs = all_slugs[:limit]

    print(f"检查 {len(all_slugs)} 个skill的封禁状态...")

    # 加载admin API认证(用于交叉验证)
    admin_cookies, admin_headers = (None, None)
    if use_admin_verify:
        admin_cookies, admin_headers = _load_api_auth()
        if not admin_cookies and not admin_headers:
            print("⚠ 无admin认证凭证, 跳过交叉验证(仅使用公开API)")
            use_admin_verify = False

    # 2. 逐一检查公开API
    accessible = 0
    banned = 0
    never_published = 0
    pending_review = 0
    inconsistent = 0
    banned_slugs = []
    never_published_slugs = []
    error_slugs = []

    # 无认证请求头
    pub_headers = {'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}

    for i, slug in enumerate(all_slugs, 1):
        url = f"{_API_BASE}/skills/{slug}"
        try:
            req = Request(url, headers=pub_headers)
            with urlopen(req, timeout=10) as resp:
                accessible += 1
        except HTTPError as e:
            if e.code == 404:
                # 公开API返回404 — 需要admin API交叉验证
                if use_admin_verify:
                    admin_url = f"{_API_BASE}/orgs/{_ADMIN_ORG_ID}/admin/skills/{slug}"
                    admin_success, admin_data = _api_request('GET', admin_url, admin_headers, timeout=15)

                    if admin_success:
                        # admin API能访问 — 非封禁
                        visibility = admin_data.get('visibility', '')
                        review_status = admin_data.get('reviewStatus', admin_data.get('review_status', ''))

                        # H1修复: 先检查pending状态, 再检查visibility
                        # 因为pending skill的visibility通常不是public(尚未发布到社区),
                        # 如果先检查visibility会误判pending为never_published
                        if review_status == 'pending':
                            # 仍在审核中 — 非封禁
                            pending_review += 1
                            if i % 50 == 0:
                                print(f"  [{i}/{len(all_slugs)}] {slug} — pending (审核中)")
                        elif visibility != 'public':
                            # 从未发布到社区 — 非封禁
                            never_published += 1
                            never_published_slugs.append(slug)
                            if i % 50 == 0:
                                print(f"  [{i}/{len(all_slugs)}] {slug} — org_only (未发布到社区)")
                        else:
                            # admin可见且public但公开API 404 — 异常
                            inconsistent += 1
                            error_slugs.append({'slug': slug, 'code': 'inconsistent',
                                                'detail': f'admin: vis={visibility}, rs={review_status}'})
                            if i % 50 == 0:
                                print(f"  [{i}/{len(all_slugs)}] {slug} — ⚠ 状态不一致")
                    else:
                        # admin API也返回错误 — 确认封禁
                        banned += 1
                        banned_slugs.append(slug)
                        if i % 50 == 0:
                            print(f"  [{i}/{len(all_slugs)}] {slug} — ❌ 确认封禁(admin验证)")
                else:
                    # 无admin验证 — 按原逻辑标记为封禁(可能含误判)
                    banned += 1
                    banned_slugs.append(slug)
                    if i % 50 == 0:
                        print(f"  [{i}/{len(all_slugs)}] {slug} — ❌ 404 (未验证)")
            else:
                error_slugs.append({'slug': slug, 'code': e.code})
                if i % 100 == 0:
                    print(f"  [{i}/{len(all_slugs)}] {slug} — HTTP {e.code}")
        except Exception as e:
            error_slugs.append({'slug': slug, 'error': str(e)[:50]})
            if i % 100 == 0:
                print(f"  [{i}/{len(all_slugs)}] {slug} — Error: {str(e)[:50]}")

        if i % 200 == 0:
            print(f"  --- 进度: {i}/{len(all_slugs)} | 正常={accessible} 封禁={banned} 未发布={never_published} ---")

    # 3. 更新DB — 仅将确认封禁的skill标记为deleted_on_skillhub
    if banned_slugs:
        conn = _sqlite3.connect(str(DB_PATH))
        conn.execute("PRAGMA foreign_keys = ON")
        for slug in banned_slugs:
            conn.execute("""
                UPDATE skills SET current_status = 'deleted_on_skillhub'
                WHERE slug = ? AND current_status = 'synced_from_skillhub'
            """, (slug,))
        conn.commit()
        conn.close()
        print(f"\n已将 {len(banned_slugs)} 个确认封禁skill标记为 deleted_on_skillhub")

    # never_published的skill保持synced_from_skillhub状态(它们没被封禁,只是没发布到社区)
    # 但需要标记需要重新发布到社区
    if never_published_slugs:
        conn = _sqlite3.connect(str(DB_PATH))
        conn.execute("PRAGMA foreign_keys = ON")
        for slug in never_published_slugs:
            conn.execute("""
                UPDATE platform_uploads SET community_published = 0
                WHERE skill_id = (SELECT id FROM skills WHERE slug = ?)
                AND platform = 'skillhub'
            """, (slug,))
        conn.commit()
        conn.close()
        print(f"已将 {len(never_published_slugs)} 个未发布到社区的skill标记 community_published=0 (需重新发布)")

    # 4. 分析封禁原因
    print(f"\n=== 封禁原因分析 ===")
    if banned_slugs:
        # 检查被封禁skill的共性
        has_special = [s for s in banned_slugs if '-' in s and len(s.split('-')) > 3]
        has_suffix = [s for s in banned_slugs if s.endswith(('-sk', '-sk1', '-sk2', '-sk3'))]
        has_free_pro = [s for s in banned_slugs if s.endswith(('-free', '-pro', '-tool-free', '-tool-pro'))]
        short_slugs = [s for s in banned_slugs if len(s) <= 8]

        print(f"  封禁总数: {len(banned_slugs)}")
        print(f"  含-sk后缀(改名): {len(has_suffix)}")
        print(f"  含-free/-pro后缀(派生): {len(has_free_pro)}")
        print(f"  slug较短(<=8字符): {len(short_slugs)}")
        print(f"  多段slug(>3段): {len(has_special)}")

        if has_suffix:
            print(f"\n  改名skill被封禁 (可能原因: slug冲突改名后又被占用)")
            for s in has_suffix[:10]:
                print(f"    - {s}")

    if never_published > 0:
        print(f"\n  未发布到社区(非封禁): {never_published}")
        print(f"  → 这些skill需要通过 batch_republish_to_community 重新发布")

    if pending_review > 0:
        print(f"  仍在审核中(非封禁): {pending_review}")

    if inconsistent > 0:
        print(f"  ⚠ 状态不一致(需人工排查): {inconsistent}")

    return {
        'checked': len(all_slugs),
        'accessible': accessible,
        'banned': banned,
        'never_published': never_published,
        'pending_review': pending_review,
        'inconsistent': inconsistent,
        'banned_slugs': banned_slugs,
        'never_published_slugs': never_published_slugs,
        'error_slugs': error_slugs[:20],
    }


def auto_publish(slug: str) -> dict:
    """自动发布skill到社区 (统一入口: 查询→审核→社区发布→收藏)
    
    完整自动化流程:
    1. 查询平台状态
    2. 如果pending, 自动approve
    3. 如果published但不可见(org_only/null), 发布到社区
    4. 收藏
    5. 更新本地DB
    
    复用auto_publish.py的auto_flow逻辑, 但通过API直接调用(无需浏览器JS)
    
    参数:
        slug: skill slug
    
    返回:
        {'slug': str, 'status': str, 'steps': {...}}
    """
    result = {'slug': slug, 'timestamp': NOW, 'steps': {}}
    
    # Step 1: 查询状态
    status = get_platform_status(slug)
    result['steps']['status'] = status
    if not status.get('success'):
        result['status'] = 'failed'
        result['error'] = '状态查询失败'
        return result
    
    review_status = status.get('review_status', 'unknown')
    visibility = status.get('visibility', 'unknown')
    front_visible = status.get('front_visible', False)
    result['current_status'] = review_status
    result['current_visibility'] = visibility
    
    # Step 2: 如果pending, 审核通过
    if review_status == 'pending':
        print(f"  [{slug}] pending → approving...")
        approve_result = batch_approve([slug])
        result['steps']['approve'] = approve_result
        if approve_result.get('success') and slug in approve_result.get('approved', []):
            review_status = 'published'
        else:
            result['status'] = 'approve_failed'
            return result
    
    # Step 3: 如果published但不可见, 发布到社区
    if review_status in ('published', 'approved', 'public_published'):
        if visibility != 'public' or not front_visible:
            print(f"  [{slug}] published → publishing to community...")
            pub_result = publish_to_community(slug)
            result['steps']['publish_to_community'] = pub_result
            if pub_result.get('success'):
                visibility = 'public'
                front_visible = True
            else:
                result['steps']['publish_to_community_warning'] = pub_result.get('error', '')
        
        # Step 4: 收藏
        if not status.get('db_starred'):
            print(f"  [{slug}] published → starring...")
            star_result = star_skill(slug)
            result['steps']['star'] = star_result
        else:
            result['steps']['star'] = {'success': True, 'message': 'already starred'}
    
    result['status'] = 'completed'
    result['final_visibility'] = visibility
    result['final_front_visible'] = front_visible
    return result

# ============ ClawHub 统一上传入口 (v2.1新增) ============
# 将 clawhub_batch_uploader.py 的上传逻辑收口到 platform_ops 统一入口
# 消除碎片化: 后续所有 ClawHub 上传通过 platform_ops.py clawhub-upload 命令调用

def upload_to_clawhub(slug: str, skip_security: bool = False, dry_run: bool = False) -> dict:
    """上传单个skill到ClawHub (统一入口)
    
    集成:
    1. 安全审核预检 (v2.1新增, 防止高风险skill被平台拒绝)
    2. 营销参数提取 (分类/标签/显示名)
    3. CLI上传 (含营销参数)
    4. DB状态更新
    
    参数:
        slug: skill slug
        skip_security: 跳过安全预检(批量场景使用, 默认False)
        dry_run: 试运行模式
    
    返回:
        {'success': bool, 'slug': str, 'message': str, ...}
    """
    from clawhub_batch_uploader import (
        find_skill_dir, upload_skill, get_clawhub_category,
        get_clawhub_topics, get_display_name
    )
    
    # 加载dir mapping
    dir_mapping_path = DATA_DIR / "round40_clawhub_dir_mapping.json"
    dir_mapping = {}
    if dir_mapping_path.exists():
        import json as _json
        data = _json.loads(dir_mapping_path.read_text(encoding='utf-8'))
        dir_mapping = data.get('found_mapping', {})
    
    # Step 1: 找到skill目录
    skill_dir = find_skill_dir(slug, dir_mapping)
    if not skill_dir:
        return {'success': False, 'slug': slug, 'error': 'DIR_NOT_FOUND',
                'message': f'找不到skill目录: {slug}'}
    
    # Step 2: 安全审核预检 + 营销关卡 + 防幻觉 (v2.3增强: 与enterprise_uploader对齐)
    if not skip_security:
        try:
            from quality_gate import run_security_precheck, run_marketing_gate, run_anti_hallucination
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                # 2a: 安全预检(21项)
                sec_result = run_security_precheck(skill_md)
                if not sec_result.get('overall_passed', False):
                    failed_checks = [c for c in sec_result.get('checks', []) if not c.get('passed')]
                    critical_fails = [c for c in failed_checks if c.get('severity') == 'critical']
                    if critical_fails:
                        return {
                            'success': False, 'slug': slug, 'error': 'SECURITY_PRECHECK_FAILED',
                            'message': f'安全审核预检未通过({len(failed_checks)}项失败, {len(critical_fails)}项critical)',
                            'failed_checks': failed_checks,
                            'skill_dir': str(skill_dir)
                        }

                # 2b: 营销关卡(7项)
                mkt_result = run_marketing_gate(skill_md)
                if not mkt_result.get('overall_passed', False):
                    mkt_failed = [c for c in mkt_result.get('checks', []) if not c.get('passed')]
                    print(f"  ⚠ 营销关卡警告({len(mkt_failed)}项未通过): {[c['name'] for c in mkt_failed]}")

                # 2c: 防幻觉检查(3项)
                hall_result = run_anti_hallucination(skill_md)
                if not hall_result.get('overall_passed', False):
                    hall_failed = [c for c in hall_result.get('checks', []) if not c.get('passed')]
                    high_fails = [c for c in hall_failed if c.get('severity') == 'high']
                    if high_fails:
                        return {
                            'success': False, 'slug': slug, 'error': 'ANTI_HALLUCINATION_FAILED',
                            'message': f'防幻觉检查未通过({len(high_fails)}项high级失败)',
                            'failed_checks': high_fails,
                            'skill_dir': str(skill_dir)
                        }
        except ImportError:
            pass  # quality_gate不可用时跳过
    
    # Step 3: 提取营销参数(用于日志记录)
    category = get_clawhub_category(skill_dir)
    topics = get_clawhub_topics(skill_dir, slug)
    display_name = get_display_name(skill_dir)
    
    # Step 4: 执行上传(含营销参数)
    result = upload_skill(skill_dir, slug, dry_run=dry_run)
    
    # 附加营销参数到结果
    if isinstance(result, dict):
        result['marketing'] = {
            'category': category,
            'topics': topics,
            'display_name': display_name,
        }
    
    # Step 5: 更新SQLite DB状态
    if result.get('success') and not dry_run:
        try:
            import sqlite3 as _sqlite3
            _DB_PATH = Path(__file__).resolve().parent.parent / "skill-registry.db"
            conn = _sqlite3.connect(str(_DB_PATH))
            c = conn.cursor()
            c.execute(
                "UPDATE skills SET clawhub_sync_status = 'synced', updated_at = ? WHERE slug = ?",
                (datetime.now().isoformat(), slug)
            )
            conn.commit()
            conn.close()
        except Exception:
            pass  # DB更新失败不影响上传结果
    
    return result


def batch_upload_clawhub(limit: int = 200, skip_security: bool = True, dry_run: bool = False) -> dict:
    """批量上传pending skills到ClawHub
    
    参数:
        limit: 单次上传上限(默认200, ClawHub每日限制)
        skip_security: 批量模式默认跳过安全预检(已在生产环节检查)
        dry_run: 试运行模式
    
    返回:
        {'total': N, 'success': N, 'failed': N, 'skipped': N, 'results': [...]}
    """
    conn = sqlite3.connect(str(Path(__file__).resolve().parent.parent / "skill-registry.db"))
    c = conn.cursor()
    
    # 获取pending状态的skill
    c.execute("SELECT slug FROM skills WHERE clawhub_sync_status = 'pending' ORDER BY slug LIMIT ?", (limit,))
    slugs = [row[0] for row in c.fetchall()]
    conn.close()
    
    if not slugs:
        return {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0,
                'message': '无pending状态的skill'}
    
    results = {'success': [], 'failed': [], 'skipped': []}
    
    for i, slug in enumerate(slugs):
        result = upload_to_clawhub(slug, skip_security=skip_security, dry_run=dry_run)
        
        if result.get('success'):
            results['success'].append(slug)
        elif result.get('error') == 'DIR_NOT_FOUND':
            results['skipped'].append(slug)
        else:
            results['failed'].append({'slug': slug, 'error': result.get('error', 'unknown')})
        
        # 进度输出
        if (i + 1) % 10 == 0:
            print(f"  [{i+1}/{len(slugs)}] success={len(results['success'])}, "
                  f"fail={len(results['failed'])}, skip={len(results['skipped'])}")
        
        # 限流延迟
        if not dry_run and i < len(slugs) - 1:
            import time as _time
            _time.sleep(2)
    
    return {
        'total': len(slugs),
        'success': len(results['success']),
        'failed': len(results['failed']),
        'skipped': len(results['skipped']),
        'results': results
    }


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
    elif cmd == "star":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py star <slug> [slug...]")
            return
        for slug in sys.argv[2:]:
            r = star_skill(slug)
            print(f"{'✅' if r['success'] else '❌'} {slug}: {r.get('message', r.get('error', ''))}")
    elif cmd == "batch-approve":
        # 无参数=自动获取所有pending; 有参数=指定slug列表
        slugs = sys.argv[2:] if len(sys.argv) > 2 else None
        batch_approve(slugs)
    elif cmd == "handle-rejected":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py handle-rejected <slug>")
            return
        r = handle_rejected(sys.argv[2])
        if r.get('success'):
            print(f"\n{sys.argv[2]} 拒绝分析:")
            for action in r['analysis']['actions']:
                print(f"  → {action}")
        else:
            print(f"❌ {r.get('error', 'unknown')}")
    elif cmd == "platform-status":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py platform-status <slug>")
            return
        r = get_platform_status(sys.argv[2])
        if r.get('success'):
            print(f"\n{sys.argv[2]} 平台状态:")
            print(f"  审核状态: {r.get('review_status', 'unknown')}")
            print(f"  可见性:   {r.get('visibility', 'unknown')}")
            print(f"  前台可见: {'是' if r.get('front_visible') else '否'}")
            print(f"  下载量:   {r.get('downloads', 0)}")
            print(f"  收藏数:   {r.get('stars', 0)}")
            print(f"  DB状态:   {r.get('db_status', 'unknown')}")
            if not r.get('front_visible'):
                print(f"\n  ⚠ 前台不可见! 需设置visibility=public")
        else:
            print(f"❌ {r.get('error', 'unknown')}")
    elif cmd == "pipeline":
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py pipeline <slug>")
            return
        r = run_platform_pipeline(sys.argv[2])
        print(f"\n流水线结果: {r.get('status', 'unknown')}")
        for step, result in r.get('steps', {}).items():
            if isinstance(result, dict):
                print(f"  {step}: {'✅' if result.get('success') else '⚠'} {result.get('message', result.get('error', ''))}")
            else:
                print(f"  {step}: {result}")
    elif cmd == "auto-publish":
        # 自动发布到社区 (查询→审核→社区发布→收藏)
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py auto-publish <slug> [slug...]")
            return
        for slug in sys.argv[2:]:
            r = auto_publish(slug)
            print(f"\n{'✅' if r.get('status') == 'completed' else '⚠'} {slug}: {r.get('status', 'unknown')}")
            print(f"  审核状态: {r.get('current_status', 'unknown')} → 最终可见性: {r.get('final_visibility', 'unknown')}")
            for step, result in r.get('steps', {}).items():
                if isinstance(result, dict) and 'success' in result:
                    print(f"  {step}: {'✅' if result.get('success') else '⚠'} {result.get('message', result.get('error', ''))}")
    elif cmd == "publish-community":
        # 单独发布到社区 (仅publish-to-community)
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py publish-community <slug> [slug...]")
            return
        for slug in sys.argv[2:]:
            r = publish_to_community(slug)
            print(f"{'✅' if r['success'] else '❌'} {slug}: {r.get('message', r.get('error', ''))}")
    elif cmd == "clawhub-upload":
        # 上传单个skill到ClawHub (含安全预检+营销参数)
        if len(sys.argv) < 3:
            print("用法: python platform_ops.py clawhub-upload <slug> [--skip-security] [--dry-run]")
            return
        slug = sys.argv[2]
        skip_sec = '--skip-security' in sys.argv
        dry = '--dry-run' in sys.argv
        r = upload_to_clawhub(slug, skip_security=skip_sec, dry_run=dry)
        if r.get('success'):
            print(f"✅ {slug}: {r.get('message', '')[:100]}")
            if r.get('marketing'):
                print(f"   分类: {r['marketing']['category']}")
                print(f"   标签: {r['marketing']['topics']}")
                print(f"   名称: {r['marketing']['display_name']}")
        else:
            print(f"❌ {slug}: {r.get('error', '')} - {r.get('message', '')[:200]}")
            if r.get('failed_checks'):
                for fc in r['failed_checks']:
                    print(f"   ✗ {fc['name']} [{fc['severity']}]")
    elif cmd == "clawhub-batch":
        # 批量上传pending skills到ClawHub
        limit = 200
        for arg in sys.argv[2:]:
            if arg.startswith('--limit='):
                limit = int(arg.split('=')[1])
        dry = '--dry-run' in sys.argv
        print(f"批量上传ClawHub (limit={limit}, dry_run={dry})")
        r = batch_upload_clawhub(limit=limit, skip_security=True, dry_run=dry)
        print(f"\n=== 批量上传完成 ===")
        print(f"  总计: {r['total']}")
        print(f"  成功: {r['success']}")
        print(f"  失败: {r['failed']}")
        print(f"  跳过: {r['skipped']}")
    elif cmd == "batch-republish":
        # 批量重新发布到社区 — 修复"已发布但前台不可见"的skill
        limit = 0
        for arg in sys.argv[2:]:
            if arg.startswith('--limit='):
                limit = int(arg.split('=')[1])
        print(f"批量重新发布到社区 (limit={limit if limit > 0 else '全部'})")
        r = batch_republish_to_community(limit=limit)
        if r.get('success') is False:
            print(f"❌ {r.get('error', '未知错误')}")
        else:
            print(f"\n=== 批量重新发布完成 ===")
            print(f"  总skill数: {r.get('total', 0)}")
            print(f"  需要重新发布: {r.get('needs_republish', 0)}")
            print(f"  ✅ 成功: {r.get('success', 0)}")
            print(f"  ❌ 失败: {r.get('failed', 0)}")
            print(f"  改名: {r.get('renamed', 0)}")
            print(f"  已是public: {r.get('already_public', 0)}")
    elif cmd == "check-banned":
        # 检查被封禁的skill — 通过公开API检测404
        limit = 0
        for arg in sys.argv[2:]:
            if arg.startswith('--limit='):
                limit = int(arg.split('=')[1])
        r = check_banned_skills(limit=limit)
        print(f"\n=== 封禁检查完成 ===")
        print(f"  检查总数: {r.get('checked', 0)}")
        print(f"  正常: {r.get('accessible', 0)}")
        print(f"  封禁/404: {r.get('banned', 0)}")
        if r.get('banned_slugs'):
            print(f"  被封禁列表 (前20):")
            for s in r['banned_slugs'][:20]:
                print(f"    - {s}")
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)

if __name__ == "__main__":
    main()
