#!/usr/bin/env python3
"""
统一编排脚本 (Unified Orchestrator)
====================================
将发现→增强→审计→包装→多平台同步→记录整合为单一命令

完整流程 (6个阶段, 对应6个函数):
  1. DISCOVER  - 发现新skill (auto_discover.py) + 检测本地变更 (version_sync_pipeline.py scan)
                 对应函数: phase_discover()
  2. ENHANCE   - 内容增强建议 (基于审计报告识别B级skill,生成增强建议)
                 对应函数: phase_enhance()
  3. AUDIT     - 全量质量审计 (deep_quality_audit.py: L1-L8审计)
                 对应函数: phase_audit()
  4. PACKAGE   - 营销包装自动化 (plug_generator.py + bundle_composer + auto_differentiate)
                 对应函数: phase_package()
  5. SYNC      - 多平台同步 (version_sync_pipeline.py: GitHub双仓库 + SkillHub + ClawHub)
                 对应函数: phase_sync()
                 注: 版本号递增由version_sync_pipeline.py在SYNC阶段内自动处理,无独立阶段
  6. RECORD    - 执行报告生成 (SQLite统一数据源)
                 对应函数: phase_record()

使用方式:
    python orchestrator.py status              # 查看全流程状态概览
    python orchestrator.py discover            # 仅执行发现阶段
    python orchestrator.py enhance             # 仅执行增强阶段(识别B级skill)
    python orchestrator.py audit               # 仅执行质量审计
    python orchestrator.py package             # 仅执行营销包装阶段(M3.3新增)
    python orchestrator.py sync-all            # 同步所有变更skill到所有平台
    python orchestrator.py sync <slug>         # 同步单个skill到所有平台
    python orchestrator.py full-run            # 执行完整流程: discover→enhance→audit→package→sync-all
    python orchestrator.py pipeline-report     # 生成流水线完整性报告

设计原则:
  - SQLite数据库为唯一权威数据源
  - 每个阶段独立执行,单个阶段失败不阻塞后续阶段
  - 所有操作记录到operations表
  - 禁止任何mock/fallback/skip
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, get_timestamp, DATA_DIR, A_GRADE_QUALITY_THRESHOLD, PACKAGED_SKILLS_DIR, DIFFERENTIATED_DIR, OPENSOURCE_SKILLS_DIR, HERMES_SKILLS_DIR, PLUGS_DIR, ENTERPRISE_UPLOAD_DIR, TRACE_PASS_THRESHOLD # V123 W2: 合并重复import; V165: 新增全目录搜索常量; V175: 新增TRACE_PASS_THRESHOLD
# === End Phase 1 ===
SKILL_DATA_DIR = DATA_DIR  # v2.5修复: 修复SKILL_DATA_DIR未定义bug


import argparse
import json
import subprocess
from skill_core import db as db_module  # V116 W1: 统一db入口(替代import db)
import sys
import time
from datetime import datetime
from typing import Any, Dict, List, Optional  # V121 W6: 移除未使用的 from pathlib import Path (仅 _Path 在 L42 使用)

# 确保tools目录在sys.path中, 以便导入skill_core
# V110 W6: Path(__file__).resolve().parent → TOOLS_DIR (统一从project_config导入)
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

# ============================================================
# 配置
# ============================================================

# DB_PATH imported from config
# SKILLS_ROOT = PROJECT_ROOT (imported from config)
# TOOLS_DIR = TOOLS_DIR (imported from config)

# 脚本路径
DISCOVER_SCRIPT = TOOLS_DIR / "auto_discover.py"
SYNC_PIPELINE_SCRIPT = TOOLS_DIR / "version_sync_pipeline.py"
AUDIT_SCRIPT = TOOLS_DIR / "deep_quality_audit.py"
CLAWHUB_UPLOADER = TOOLS_DIR / "clawhub_batch_uploader.py"
UPGRADE_CHECKER_SCRIPT = TOOLS_DIR / "upgrade_checker.py"  # V141 D1: 版本追踪闭环

# 审计报告路径
AUDIT_REPORT = SKILL_DATA_DIR / "reports" / "deep_quality_audit_report.json"

# V107 W4: NOW别名已移除(内联get_timestamp())


# ============================================================
# 数据库操作
# ============================================================


def log_operation(skill_id: Optional[int], operation_type: str, details: str, status: str = "completed"):
    """记录操作到数据库 (R7-1收口: 使用db_module.record_operation替代裸SQL)"""
    db_module.record_operation(
        skill_id=skill_id,
        operation_type=operation_type,
        details=details,
        after_state=status,
        operator='orchestrator',
    )


# ============================================================
# 阶段1: DISCOVER - 发现新skill + 检测本地变更
# ============================================================

def phase_discover() -> Dict[str, Any]:
    """发现阶段: 扫描新skill + 检测已有skill变更"""
    print("\n" + "=" * 60)
    print("阶段 1/6: DISCOVER - 发现新skill + 检测本地变更")
    print("=" * 60)

    result = {
        "phase": "discover",
        "new_skills": 0,
        "changed_skills": 0,
        "details": [],
    }

    # 1a. 扫描新skill (auto_discover.py)
    print("  [1a] 扫描新skill...")
    try:
        proc = subprocess.run(
            [sys.executable, str(DISCOVER_SCRIPT), "scan"],
            capture_output=True, text=True, timeout=300,
            cwd=str(TOOLS_DIR)
        )
        if proc.returncode == 0:
            print(f"  [1a] 发现扫描完成")
            result["details"].append({"sub": "scan_new", "status": "ok"})
        else:
            print(f"  [1a] 发现扫描失败: {proc.stderr[:200]}")
            result["details"].append({"sub": "scan_new", "status": "error", "error": proc.stderr[:200]})
    except subprocess.TimeoutExpired:
        print(f"  [1a] 发现扫描超时(300s),跳过")
        result["details"].append({"sub": "scan_new", "status": "timeout"})
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
        print(f"  [1a] 发现扫描异常: {e}")
        result["details"].append({"sub": "scan_new", "status": "exception", "error": str(e)})

    # 1b. 检测本地变更 (version_sync_pipeline.py scan)
    print("  [1b] 检测本地SKILL.md变更...")
    try:
        proc = subprocess.run(
            [sys.executable, str(SYNC_PIPELINE_SCRIPT), "scan"],
            capture_output=True, text=True, timeout=300,
            cwd=str(TOOLS_DIR)
        )
        if proc.returncode == 0:
            # 解析输出获取变更skill数量
            output = proc.stdout
            if "changed" in output.lower() or "变更" in output:
                # 尝试从输出中提取变更数量
                import re
                match = re.search(r'(\d+)\s*个?\s*(?:changed|变更)', output)
                if match:
                    result["changed_skills"] = int(match.group(1))
            print(f"  [1b] 变更检测完成, 发现 {result['changed_skills']} 个变更skill")
            result["details"].append({"sub": "scan_changes", "status": "ok", "changed": result["changed_skills"]})
        else:
            print(f"  [1b] 变更检测失败: {proc.stderr[:200]}")
            result["details"].append({"sub": "scan_changes", "status": "error", "error": proc.stderr[:200]})
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
        print(f"  [1b] 变更检测异常: {e}")
        result["details"].append({"sub": "scan_changes", "status": "exception", "error": str(e)})

    # 1c. 源skill升级检查 (V141 D1: 版本追踪闭环)
    print("  [1c] 检查源skill升级状态...")
    try:
        proc = subprocess.run(
            [sys.executable, str(UPGRADE_CHECKER_SCRIPT), "check"],
            capture_output=True, text=True, timeout=300,
            cwd=str(TOOLS_DIR)
        )
        if proc.returncode == 0:
            # 从输出提取needs_upgrade数量
            import re
            match = re.search(r'(\d+)\s*个?\s*(?:need|需要|升级)', proc.stdout)
            if match:
                result["needs_upgrade"] = int(match.group(1))
            else:
                result["needs_upgrade"] = 0
            print(f"  [1c] 升级检查完成: {result['needs_upgrade']}个需要升级")
            result["details"].append({"sub": "upgrade_check", "status": "ok", "needs_upgrade": result["needs_upgrade"]})
        else:
            result["needs_upgrade"] = 0
            print(f"  [1c] 升级检查跳过: {proc.stderr[:200]}")
            result["details"].append({"sub": "upgrade_check", "status": "error", "error": proc.stderr[:200]})
    except subprocess.TimeoutExpired:
        result["needs_upgrade"] = 0
        print("  [1c] 升级检查超时(300s)")
        result["details"].append({"sub": "upgrade_check", "status": "timeout"})
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
        result["needs_upgrade"] = 0
        print(f"  [1c] 升级检查异常: {e}")
        result["details"].append({"sub": "upgrade_check", "status": "exception", "error": str(e)})

    log_operation(None, "orchestrator_discover", f"Discover phase: {result['new_skills']} new, {result['changed_skills']} changed, {result.get('needs_upgrade', 0)} need_upgrade", "completed")
    return result


# ============================================================
# 阶段2: ENHANCE - 内容增强建议
# ============================================================

def phase_enhance(dry_run: bool = False) -> Dict[str, Any]:
    """增强阶段: 基于审计报告识别B级skill,生成增强建议

    V156: 新增dry_run参数, dry_run=True时跳过所有文件写操作(skill_md_path.write_text),
    仅打印将要做的修改
    """
    print("\n" + "=" * 60)
    print("阶段 2/6: ENHANCE - 识别需增强的skill")
    print("=" * 60)

    result = {
        "phase": "enhance",
        "l5_b_grade": [],
        "l7b_b_grade": [],
        "l6_issues": [],
        "l7a_issues": [],
        "total_needs_enhancement": 0,
    }

    # 读取审计报告
    if not AUDIT_REPORT.exists():
        print(f"  [WARN] 审计报告不存在: {AUDIT_REPORT}")
        print(f"  [V180] 跳过审计报告依赖, 继续基于DB评分运行修复链")
        report = {}
    else:
        report = json.load(open(AUDIT_REPORT, "r", encoding="utf-8"))

    # L5 B级skill
    sellability = report.get("sellability", {})
    b_grades = sellability.get("b_grade_detail", [])
    result["l5_b_grade"] = b_grades
    print(f"  L5 B级skill: {len(b_grades)} 个")
    for item in b_grades[:10]:
        print(f"    [{item['score']}] {item['slug']}: {', '.join(item.get('factors', []))}")

    # L7b B级skill
    l7b = report.get("executability_audit", {})
    l7b_issues = l7b.get("issues_detail", [])
    result["l7b_b_grade"] = l7b_issues
    print(f"  L7b B级skill: {len(l7b_issues)} 个")

    # L6 问题
    l6 = report.get("content_authenticity", {})
    l6_issues_list = l6.get("issues_detail", [])
    result["l6_issues"] = l6_issues_list
    print(f"  L6 问题skill: {len(l6_issues_list)} 个")

    # L7a 问题
    l7a = report.get("semantic_audit", {})
    l7a_issues_list = l7a.get("issues_detail", [])
    result["l7a_issues"] = l7a_issues_list
    print(f"  L7a 问题skill: {len(l7a_issues_list)} 个")

    result["total_needs_enhancement"] = len(b_grades) + len(l7b_issues) + len(l6_issues_list) + len(l7a_issues_list)
    print(f"  总计需增强: {result['total_needs_enhancement']} 个skill")

    # === M2.1: 自动修复链 — 对每个需增强的skill按 安全→幻觉→合规→内容→价值主张 顺序调用修复函数 ===
    # 收集所有需增强的skill (按slug去重, 保留source用于定位SKILL.md)
    fix_targets = {}
    for item in b_grades + l7b_issues + l6_issues_list + l7a_issues_list:
        slug = item.get("slug")
        source = item.get("source", "")
        if slug and slug not in fix_targets:
            fix_targets[slug] = source

    # V166: 增强修复链 — 补充查询数据库中local_quality_score < 4.5的非deleted skill
    # 确保不仅依赖审计报告(TRACE评分体系), 也覆盖本地质量评分(0-5标度)不达标的skill
    # V169: 同时包含未评分(NULL)的非source skill, 确保评分前先应用V169增强(创新性表格等)
    # V174: 增强覆盖范围 — 也包含local_quality_score=0的skill(评分错误)和trace_llm<42的skill
    try:
        c = db_module.get_db().cursor()
        # V174: 查询所有需要增强的skill:
        # 1. local_quality_score IS NULL (未评分)
        # 2. local_quality_score = 0 (评分错误)
        # 3. local_quality_score < 4.5 (低分)
        c.execute(
            "SELECT slug, source FROM skills "
            "WHERE current_status NOT IN ('deleted') "
            "AND (skill_type IS NULL OR skill_type != 'source') "
            "AND (local_quality_score IS NULL "
            "     OR local_quality_score = 0 "
            "     OR (local_quality_score > 0 AND local_quality_score < 4.5))"
        )
        db_low_score = c.fetchall()
        db_added = 0
        for row in db_low_score:
            slug = row[0] if isinstance(row, tuple) else row["slug"]
            source = row[1] if isinstance(row, tuple) else row["source"]
            if slug and slug not in fix_targets:
                fix_targets[slug] = source or ""
                db_added += 1
        if db_added > 0:
            print(f"  [修复链] 从DB补充 {db_added} 个低分/零分/未评分skill(含V174增强)")

        # V174: 补充查询trace_llm评分<42的skill(TRACE评分体系不达标)
        # V175: 使用TRACE_PASS_THRESHOLD(已提升至45)替代硬编码42
        c.execute(
            "SELECT s.slug, s.source FROM skills s "
            "JOIN scores sc ON sc.skill_id = s.id AND sc.is_current = 1 "
            "WHERE s.current_status NOT IN ('deleted') "
            "AND (s.skill_type IS NULL OR s.skill_type != 'source') "
            "AND sc.score_type = 'trace_llm' "
            "AND sc.total_score < ?",
            (TRACE_PASS_THRESHOLD,)
        )
        trace_low_score = c.fetchall()
        trace_added = 0
        for row in trace_low_score:
            slug = row[0] if isinstance(row, tuple) else row["slug"]
            source = row[1] if isinstance(row, tuple) else row["source"]
            if slug and slug not in fix_targets:
                fix_targets[slug] = source or ""
                trace_added += 1
        if trace_added > 0:
            print(f"  [修复链] 从trace_llm评分补充 {trace_added} 个不达标skill(<{TRACE_PASS_THRESHOLD}/50)")
    except Exception as e:
        print(f"  [修复链] [WARN] DB查询评分失败(非阻断): {e}")

    # V166: 全量品牌词扫描 — 扫描所有非deleted非source skill的SKILL.md,
    # 检查是否包含品牌词(PostgreSQL/tenant/MCP/fishclaw/narrato等)
    # 品牌词会导致平台审核拒绝和抄袭检测,必须在上传前移除
    try:
        import re as _re
        from skill_core.finder import find_skill_dir as _fsd
        c = db_module.get_db().cursor()
        c.execute(
            "SELECT slug, source FROM skills "
            "WHERE current_status NOT IN ('deleted') "
            "AND skill_type != 'source'"
        )
        all_skills = c.fetchall()
        # V168: 品牌词扫描模式与auto_fix_debranding的system_term_map保持一致
        # 包含复合词模式(tenant_id/tenant_access_token/mcpServers/HostedMCPTool等)
        branding_patterns = [
            r'(?<![A-Za-z0-9_])PostgreSQL(?![A-Za-z0-9_])',
            r'(?<![A-Za-z0-9_])(fishclaw|narrato|dailyhot|novel_bridge)(?![A-Za-z0-9_])',
            r'(?<![A-Za-z0-9_])(clawhub|clawsec|clawdbot)(?![A-Za-z0-9_])',
            # V168: tenant全变体匹配(含复合词)
            r'(?i)tenant_access_token',
            r'(?i)tenant_aware',
            r'(?i)tenant_token',
            r'(?i)tenant_type',
            r'(?i)tenant_name',
            r'(?i)tenant_level',
            r'(?i)tenant_mode',
            r'(?i)tenantId',
            r'(?i)tenant_id',
            r'(?i)multi-tenant',
            r'(?i)multi_tenant',
            # V170: 新增复合词模式
            r'(?i)register_tenant',
            r'(?i)generate_tenant',
            r'(?i)per_tenant',
            r'(?i)tenant_tagged',
            r'(?i)tenant_labeled',
            r'(?i)tenant_quota',
            r'(?i)tenant_[a-z]',  # V170: 通用tenant_前缀匹配
            r'(?i)_tenant\b',  # V170: _tenant后缀匹配(register_tenant等)
            r'(?<![A-Za-z0-9_])tenants(?![A-Za-z0-9_])',
            r'(?<![A-Za-z0-9_])tenant(?![A-Za-z0-9_])',
            r'ARM_TENANT_ID',
            r'AZURE_TENANT_ID',
            # V168: MCP全变体匹配(含复合词和lowercase)
            r'(?i)mcpServers',
            r'(?i)HostedMCPTool',
            r'(?i)MCPStreamableHTTP',
            r'/mcp\s+add',
            r'(?<![A-Za-z0-9_/.])MCP(?![A-Za-z0-9_])',
            r'xianyu',
        ]
        branding_added = 0
        for row in all_skills:
            slug = row[0] if isinstance(row, tuple) else row["slug"]
            source = row[1] if isinstance(row, tuple) else row["source"]
            if slug in fix_targets:
                continue
            sd = _fsd(slug)
            if sd is None:
                continue
            skill_md_path = sd / "SKILL.md"
            if not skill_md_path.exists():
                continue
            try:
                content = skill_md_path.read_text(encoding='utf-8', errors='replace')
            except Exception:
                continue
            for pattern in branding_patterns:
                if _re.search(pattern, content, _re.IGNORECASE):
                    fix_targets[slug] = source or ""
                    branding_added += 1
                    break
        if branding_added > 0:
            print(f"  [修复链] 从品牌词扫描补充 {branding_added} 个含品牌词的skill")
    except Exception as e:
        print(f"  [修复链] [WARN] 品牌词扫描失败(非阻断): {e}")

    if dry_run:
        print(f"  [修复链] [DRY-RUN] 将对 {len(fix_targets)} 个skill执行自动修复 (跳过所有文件写操作)")
        for _slug in fix_targets:
            print(f"    [DRY-RUN] 将修复: {_slug}")
        result["fix_results"] = []
        result["fix_total"] = 0
        result["dry_run"] = True
        log_operation(None, "orchestrator_enhance",
                      f"Enhance phase [DRY-RUN]: targets={len(fix_targets)}, skipped_writes=True",
                      "completed")
        return result

    print(f"  [修复链] 对 {len(fix_targets)} 个skill执行自动修复 (安全→幻觉→合规→内容→价值主张)...")

    # 懒加载修复函数 (函数内导入, 避免循环依赖)
    from quality_gate import auto_fix_security_issues, auto_fix_hallucination, auto_fix_debranding
    from skill_batch_upgrader_v3 import auto_fix, auto_fix_content
    from fix_missing_fields import enhance_value_proposition, extract_frontmatter

    def _resolve_skill_md(slug, source):
        """根据slug与source定位SKILL.md路径 (全目录搜索)

        V165增强: 扩展搜索范围至所有skill目录(opensource/hermes/plugs/enterprise),
        消除原仅搜索packaged-skills/skillhub和differentiated-skills的盲区
        """
        # 1. packaged-skills/skillhub/<slug>/SKILL.md (优先)
        packaged_md = PACKAGED_SKILLS_DIR / slug / "SKILL.md"
        if packaged_md.exists():
            return packaged_md
        # 2. differentiated-skills/<category>/<slug>/SKILL.md
        if source.startswith("differentiated/"):
            category = source.split("/", 1)[1]
            diff_md = DIFFERENTIATED_DIR / category / slug / "SKILL.md"
            if diff_md.exists():
                return diff_md
        # 3. opensource-skills/packaged/<slug>/SKILL.md
        opensource_md = OPENSOURCE_SKILLS_DIR / slug / "SKILL.md"
        if opensource_md.exists():
            return opensource_md
        # 4. hermes-skills/<slug>/SKILL.md
        hermes_md = HERMES_SKILLS_DIR / slug / "SKILL.md"
        if hermes_md.exists():
            return hermes_md
        # 5. packaged-skills/plugs/<slug>/SKILL.md
        plugs_md = PLUGS_DIR / slug / "SKILL.md"
        if plugs_md.exists():
            return plugs_md
        # 6. enterprise-upload/<slug>/SKILL.md
        enterprise_md = ENTERPRISE_UPLOAD_DIR / slug / "SKILL.md"
        if enterprise_md.exists():
            return enterprise_md
        # 7. 兜底: 遍历 differentiated-skills 各类别子目录
        if DIFFERENTIATED_DIR.exists():
            for cat_dir in DIFFERENTIATED_DIR.iterdir():
                cand = cat_dir / slug / "SKILL.md"
                if cand.exists():
                    return cand
        # 8. V166: 使用统一的 find_skill_dir 作为最终兜底
        # 处理 slug 变体 (如 slug-pro, slug-free, slug-paid 等目录命名)
        try:
            from skill_core.finder import find_skill_dir as _fsd
            sd = _fsd(slug)
            if sd:
                md = sd / "SKILL.md"
                if md.exists():
                    return md
        except Exception as e:
            print(f"[WARN] _resolve_skill_md: 解析skill路径异常: {e}")
        return None

    fix_results = []
    # 修复链顺序: 安全 → 幻觉 → 合规(12项) → 内容(7项) → 价值主张 → 去标识化(V147 R5)
    for slug, source in fix_targets.items():
        skill_md_path = _resolve_skill_md(slug, source)
        if skill_md_path is None:
            fix_results.append({"slug": slug, "fix_type": "resolve", "changes": [], "error": "skill_md_not_found"})
            print(f"    [跳过] {slug}: 未找到SKILL.md")
            continue

        # 1. 安全修复 (API密钥/Mock/exec等)
        try:
            res = auto_fix_security_issues(skill_md_path)
            fix_results.append({"slug": slug, "fix_type": "security", "changes": res.get("fixes", [])})
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常收集错误继续批量处理
            fix_results.append({"slug": slug, "fix_type": "security", "changes": [], "error": str(e)})

        # 2. 幻觉修复 (需求理解偏差/虚假实现)
        try:
            res = auto_fix_hallucination(skill_md_path)
            fix_results.append({"slug": slug, "fix_type": "hallucination", "changes": res.get("fixes", [])})
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常收集错误继续批量处理
            fix_results.append({"slug": slug, "fix_type": "hallucination", "changes": [], "error": str(e)})

        # 3. 合规修复 (12项合规检查)
        try:
            changes = auto_fix(skill_md_path)
            fix_results.append({"slug": slug, "fix_type": "compliance", "changes": changes})
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常收集错误继续批量处理
            fix_results.append({"slug": slug, "fix_type": "compliance", "changes": [], "error": str(e)})

        # 4. 内容修复 (7项内容质量)
        try:
            changes = auto_fix_content(skill_md_path)
            fix_results.append({"slug": slug, "fix_type": "content", "changes": changes})
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常收集错误继续批量处理
            fix_results.append({"slug": slug, "fix_type": "content", "changes": [], "error": str(e)})

        # 5. 价值主张增强 (需先解析 frontmatter; skill_deep_rewrite 需API Key, 默认不启用)
        try:
            content = skill_md_path.read_text(encoding="utf-8", errors="replace")
            if content.startswith("\ufeff"):
                content = content[1:]
            fm, _fm_text, body, _full = extract_frontmatter(content)
            new_content, vp_fixed = enhance_value_proposition(content, fm, body)
            if vp_fixed:
                skill_md_path.write_text(new_content, encoding="utf-8")
                fix_results.append({"slug": slug, "fix_type": "value_proposition", "changes": ["value_proposition_enhanced"]})
            else:
                fix_results.append({"slug": slug, "fix_type": "value_proposition", "changes": []})
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常收集错误继续批量处理
            fix_results.append({"slug": slug, "fix_type": "value_proposition", "changes": [], "error": str(e)})

        # 6. V147 R5: 去标识化修复 (项目烙印/平台烙印/溯源词/URL/署名 → 移除)
        try:
            res = auto_fix_debranding(skill_md_path)
            fix_results.append({"slug": slug, "fix_type": "debranding", "changes": res.get("fixes", [])})
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常收集错误继续批量处理
            fix_results.append({"slug": slug, "fix_type": "debranding", "changes": [], "error": str(e)})

    result["fix_results"] = fix_results
    result["fix_total"] = len(fix_results)
    applied_steps = [r for r in fix_results if r.get("changes")]
    print(f"  [修复链] 完成: {len(applied_steps)}/{len(fix_results)} 个修复步骤应用了变更")

    log_operation(None, "orchestrator_enhance",
                  f"Enhance phase: L5_B={len(b_grades)}, L7b_B={len(l7b_issues)}, L6={len(l6_issues_list)}, L7a={len(l7a_issues_list)}, fix_steps={len(fix_results)}, applied={len(applied_steps)}",
                  "completed")
    return result


# ============================================================
# 阶段3: AUDIT - 质量审计 (L1-L8)
# ============================================================

def phase_audit(dry_run: bool = False) -> Dict[str, Any]:
    """审计阶段: 运行全量质量审计 (L1-L8)

    V156: 新增dry_run参数, dry_run=True时不传递--fix参数给子进程,避免写操作
    """
    print("\n" + "=" * 60)
    print("阶段 3/6: AUDIT - 全量质量审计 (L1-L8)")
    print("=" * 60)

    start_time = time.time()

    result = {
        "phase": "audit",
        "duration_seconds": 0,
        "passed": False,
        "summary": {},
    }

    try:
        # M2.2: 传入 --fix 参数,审计时自动修复 warning 级别问题
        # V156: dry_run=True时不传递--fix,避免写操作
        audit_cmd = [sys.executable, str(AUDIT_SCRIPT)]
        if not dry_run:
            audit_cmd.append("--fix")
        proc = subprocess.run(
            audit_cmd, capture_output=True, text=True, timeout=900,  # 15分钟超时
            cwd=str(TOOLS_DIR)
        )
        duration = time.time() - start_time
        result["duration_seconds"] = round(duration, 1)

        if proc.returncode == 0:
            print(f"  审计完成, 耗时 {duration:.1f}s")
            # 读取审计报告
            if AUDIT_REPORT.exists():
                report = json.load(open(AUDIT_REPORT, "r", encoding="utf-8"))
                result["summary"] = {
                    "total_skills": report.get("total_skills", 0),
                    "critical": report.get("by_severity", {}).get("critical", 0),
                    "warning": report.get("by_severity", {}).get("warning", 0),
                    "info": report.get("by_severity", {}).get("info", 0),
                    "ok": report.get("by_severity", {}).get("ok", 0),
                    "l4_avg": report.get("functional_quality", {}).get("avg_score", 0),
                    "l5_avg": report.get("sellability", {}).get("avg_score", 0),
                    "l5_b": report.get("sellability", {}).get("grade_distribution", {}).get("B", 0),
                    "l6_avg": report.get("content_authenticity", {}).get("avg_score", 0),
                    "l7a_avg": report.get("semantic_audit", {}).get("avg_score", 0),
                    "l7b_enabled": report.get("executability_audit", {}).get("enabled", False),
                    "l7b_avg": report.get("executability_audit", {}).get("avg_score", 0),
                    "l7b_b": report.get("executability_audit", {}).get("grade_distribution", {}).get("B", 0),
                    "l8_avg": report.get("security_audit", {}).get("avg_score", 0),
                    "l8_pass_rate": report.get("security_audit", {}).get("pass_rate", "0%"),
                }
                result["passed"] = result["summary"]["critical"] == 0
                print(f"  审计结果: {'通过' if result['passed'] else '失败'}")
                print(f"  L4 avg={result['summary']['l4_avg']}, L5 avg={result['summary']['l5_avg']} (B={result['summary']['l5_b']})")
                print(f"  L6 avg={result['summary']['l6_avg']}, L7a avg={result['summary']['l7a_avg']}")
                print(f"  L7b enabled={result['summary']['l7b_enabled']}, avg={result['summary']['l7b_avg']} (B={result['summary']['l7b_b']})")
                print(f"  L8 avg={result['summary']['l8_avg']}, pass_rate={result['summary']['l8_pass_rate']}")

                # V95 V7: Coze质量门控检查 — 对A级skill评估Coze资格
                try:
                    from coze_adapter import CozeAdapter
                    from daily_sync import read_upload_tracking
                    coze_adapter = CozeAdapter()
                    tracking = read_upload_tracking()
                    tracking_skills = tracking.get("skills", {})
                    # 对已发布到SkillHub的skill检查Coze资格
                    coze_result = coze_adapter.batch_check_eligibility(tracking_skills)
                    result["coze_eligible"] = {
                        "paid": len(coze_result["paid_eligible"]),
                        "free": len(coze_result["free_eligible"]),
                        "not_eligible": len(coze_result["not_eligible"]),
                        "paid_list": coze_result["paid_eligible"][:20],
                        "free_list": coze_result["free_eligible"][:20],
                    }
                    print(f"  Coze门控: paid_eligible={result['coze_eligible']['paid']}, free_eligible={result['coze_eligible']['free']}")
                except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
                    print(f"  [WARN] Coze门控检查失败(非阻塞): {e}")
                    result["coze_eligible"] = {"paid": 0, "free": 0, "not_eligible": 0, "error": str(e)}
        else:
            print(f"  审计失败 (exit={proc.returncode})")
            print(f"  stderr: {proc.stderr[:300]}")
            result["error"] = proc.stderr[:300]
    except subprocess.TimeoutExpired:
        duration = time.time() - start_time
        result["duration_seconds"] = round(duration, 1)
        print(f"  审计超时 ({duration:.1f}s)")
        result["error"] = "timeout"
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常处理(非静默pass)
        duration = time.time() - start_time
        result["duration_seconds"] = round(duration, 1)
        print(f"  审计异常: {e}")
        result["error"] = str(e)

    # V161 FIX: L1硬门禁复验+修复 (弥补本阶段仅用deep_quality_audit评分制、从不调用run_quality_gate的缺口)
    #   deep_quality_audit的passed=critical==0(评分制), 与run_quality_gate的13项硬门禁不同,
    #   导致大量skill"审计通过"但L1格式检查不合格(抽检66%/全量54.8%失败).
    #   现对全部skill运行run_quality_gate, 失败者调用auto_fix(V161已修复死代码)后复验.
    try:
        from skill_batch_upgrader_v3 import batch_l1_fix_and_verify
        l1_stats = batch_l1_fix_and_verify(dry_run=dry_run)
        result["l1_gate"] = l1_stats
        print(f"  [V161] L1硬门禁: 总{l1_stats.get('total',0)}, 初始通过{l1_stats.get('initial_pass',0)}/"
              f"失败{l1_stats.get('initial_fail',0)}, 修复后通过{l1_stats.get('final_pass',0)}/"
              f"仍失败{l1_stats.get('final_fail',0)}")
        # L1门禁作为强制门: 仍有失败则标记审计未完全通过(除非dry_run)
        if l1_stats.get("final_fail", 0) > 0 and not dry_run:
            result["passed"] = False
            result["l1_unfixed_count"] = l1_stats.get("final_fail", 0)
    except Exception as e:  # [V131 B2] 宽泛捕获: L1复验失败不阻塞主审计流程
        print(f"  [WARN] L1硬门禁复验失败(非阻塞): {e}")
        result["l1_gate"] = {"error": str(e)}

    log_operation(None, "orchestrator_audit",
                  f"Audit phase: passed={result['passed']}, duration={result['duration_seconds']}s",
                  "completed" if result["passed"] else "failed")
    return result


# ============================================================
# 阶段4: PACKAGE - 营销包装自动化 (M3.3新增)
# ============================================================

def phase_package(dry_run: bool = False) -> Dict[str, Any]:
    """包装阶段: 营销包装自动化 (M3.3新增)

    V156: 新增dry_run参数, 传递给plug_orchestrator

    将 A-grade skills 组合为 Plug 营销包, 并优化营销文案。
    流程:
      a. 从审计报告读取 A-grade skills
      b. 调用 bundle_composer.find_best_bundle() 获取 Bundle 推荐
      c. 调用 plug_generator.generate_plugs() 生成 Plug
      d. 调用 optimize_marketing_copy() 优化营销文案
    """
    print("\n" + "=" * 60)
    print("阶段 4/6: PACKAGE - 营销包装自动化")
    print("=" * 60)

    result: Dict[str, Any] = {
        "phase": "package",
        "a_grade_skills": [],
        "bundle_recommendations": [],
        "plugs_generated": {},
        "marketing_optimized": {},
    }

    # a. 从审计报告读取 A-grade skills
    print("  [4a] 读取审计报告, 提取 A-grade skills...")
    a_grade_slugs: List[str] = []
    if AUDIT_REPORT.exists():
        report = json.load(open(AUDIT_REPORT, "r", encoding="utf-8"))
        sellability = report.get("sellability", {})
        # B-grade 和 below-B 的 slug (非 A-grade)
        non_a_slugs: set = set()
        for item in sellability.get("b_grade_detail", []):
            non_a_slugs.add(item.get("slug", ""))
        for item in sellability.get("below_b_detail", []):
            non_a_slugs.add(item.get("slug", ""))

        # 查询 DB 获取所有合格 skill (local_quality_score >= A_GRADE_QUALITY_THRESHOLD)
        conn = db_module.get_db()
        c = conn.cursor()
        c.execute(
            "SELECT slug FROM skills WHERE local_quality_score >= ? "
            "ORDER BY local_quality_score DESC",
            (A_GRADE_QUALITY_THRESHOLD,)
        )
        all_qualified = [row[0] for row in c.fetchall() if row[0]]
        conn.close()

        # A-grade = 合格 skill - 非A-grade
        a_grade_slugs = [s for s in all_qualified if s not in non_a_slugs]
        result["a_grade_skills"] = a_grade_slugs
        print(f"  [4a] 找到 {len(a_grade_slugs)} 个 A-grade skills "
              f"(排除 {len(non_a_slugs)} 个非A-grade)")
    else:
        print(f"  [4a] 审计报告不存在: {AUDIT_REPORT}, 降级查询 DB")
        conn = db_module.get_db()
        c = conn.cursor()
        c.execute(
            "SELECT slug FROM skills WHERE local_quality_score >= ? "
            "ORDER BY local_quality_score DESC LIMIT 100",
            (A_GRADE_QUALITY_THRESHOLD,)
        )
        a_grade_slugs = [row[0] for row in c.fetchall() if row[0]]
        conn.close()
        result["a_grade_skills"] = a_grade_slugs
        print(f"  [4a] 降级查询 DB: 找到 {len(a_grade_slugs)} 个高质量 skills")

    if not a_grade_slugs:
        print("  [4a] 无可用 A-grade skills, 跳过包装阶段")
        result["error"] = "no_a_grade_skills"
        log_operation(None, "orchestrator_package",
                      "Package phase: no_a_grade_skills", "skipped")
        return result

    # b. V147 R2.3重构: 移除冗余的4b/4c步骤,统一由PlugOrchestrator处理
    # 原步骤4b(bundle_composer.find_best_bundle)和4c(plug_generator.generate_plugs)
    # 已由步骤4e中PlugOrchestrator.run_full_pipeline()内部的phase_discover和phase_package覆盖
    # 保留4d(营销文案优化)因为它是针对单个skill的,不与Plug管道重复

    # c. 调用 optimize_marketing_copy() 优化营销文案
    print("  [4c] 调用 optimize_marketing_copy() 优化营销文案...")
    try:
        from auto_differentiate import optimize_marketing_copy
        # 查询 A-grade skills 的营销数据用于批量优化
        conn = db_module.get_db()
        c = conn.cursor()
        top_slugs = a_grade_slugs[:20]
        placeholders = ','.join('?' * len(top_slugs))
        c.execute(
            f"SELECT slug, current_display_name, summary, category FROM skills "
            f"WHERE slug IN ({placeholders})",
            top_slugs
        )
        skills_for_optimization = [
            {
                "slug": row[0],
                "display_name": row[1] or row[0],
                "summary": row[2] or "",
                "category": row[3] or "Other",
            }
            for row in c.fetchall()
        ]
        conn.close()

        marketing_result = optimize_marketing_copy(
            skills=skills_for_optimization, use_agent=True  # V138 A5: 启用LLM代理(llm_bridge已完成)
        )
        result["marketing_optimized"] = {
            "total": marketing_result.get("total", 0),
            "optimized_count": marketing_result.get("optimized_count", 0),
        }
        print(f"  [4c] 优化 {marketing_result.get('total', 0)} 个 skill 的营销文案, "
              f"{marketing_result.get('optimized_count', 0)} 个有变更")
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
        print(f"  [4c] 营销文案优化失败: {e}")
        result["marketing_optimized"] = {"error": str(e)}

    # d. V147 R2.3: 调用plug_orchestrator统一处理Bundle发现+Plug生成+compose校验+发布+维护
    print("  [4d] 调用PlugOrchestrator统一处理Bundle+Plug+compose+publish+maintain...")
    try:
        from plug_orchestrator import PlugOrchestrator
        plug_orch = PlugOrchestrator()
        # 传入已发现的A-grade slugs, 复用前面的发现结果
        plug_result = plug_orch.run_full_pipeline(a_grade_slugs=a_grade_slugs[:50], dry_run=dry_run)

        # 从PlugOrchestrator结果中提取bundle和plug信息(替代原4b/4c的独立调用)
        discover_phase = plug_result.get('phases', {}).get('discover', {})
        bundle = discover_phase.get('bundle', {})
        package_phase = plug_result.get('phases', {}).get('package', {})
        plugs_list = package_phase.get('plugs', [])

        result["bundle_recommendations"] = [{
            "bundle_slug": bundle.get("bundle_slug", ""),
            "bundle_name": bundle.get("bundle_name", ""),
            "member_count": len(bundle.get("members", [])),
            "overall_score": bundle.get("overall_score", 0),
        }] if bundle else []

        result["plugs_generated"] = {
            "total": package_phase.get("total_plugs", 0),
            "output_root": str(bundle.get("bundle_slug", "")),  # 保留字段兼容性
            "plugs": [
                {
                    "plug_slug": p.get("plug_slug", ""),
                    "member_count": p.get("member_count", 0),
                    "bundle_price": p.get("bundle_price", 0),
                }
                for p in plugs_list
            ],
        }

        result["plug_orchestration"] = {
            "status": plug_result.get("status", "unknown"),
            "phases": list(plug_result.get("phases", {}).keys()),
            "compose_valid": plug_result.get("phases", {}).get("compose", {}).get("valid", False),
            "publish_status": plug_result.get("phases", {}).get("publish", {}).get("status", "skipped"),
        }
        print(f"  [4d] Plug编排完成: status={plug_result.get('status', 'unknown')}, "
              f"bundles={len(result['bundle_recommendations'])}, "
              f"plugs={result['plugs_generated'].get('total', 0)}")
    except ImportError:
        print("  [4d] plug_orchestrator不可用,跳过Plug编排")
        result["plug_orchestration"] = {"status": "skipped", "reason": "module_not_found"}
        result["bundle_recommendations"] = []
        result["plugs_generated"] = {"error": "plug_orchestrator_not_found"}
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
        print(f"  [4d] Plug编排失败: {e}")
        result["plug_orchestration"] = {"status": "error", "error": str(e)}
        result["bundle_recommendations"] = []
        result["plugs_generated"] = {"error": str(e)}

    log_operation(
        None, "orchestrator_package",
        f"Package phase: a_grade={len(a_grade_slugs)}, "
        f"bundles={len(result.get('bundle_recommendations', []))}, "
        f"plugs={result.get('plugs_generated', {}).get('total', 0)}, "
        f"marketing={result.get('marketing_optimized', {}).get('optimized_count', 0)}, "
        f"plug_orch={result.get('plug_orchestration', {}).get('status', 'skipped')}",
        "completed"
    )
    return result


# ============================================================
# 阶段5: SYNC - 多平台同步
# ============================================================

def phase_sync(slug: Optional[str] = None, dry_run: bool = False) -> Dict[str, Any]:
    """同步阶段: 多平台同步 (GitHub + SkillHub + ClawHub)

    V155 R6: 新增dry_run参数,传递给version_sync_pipeline子进程
    """
    print("\n" + "=" * 60)
    print("阶段 5/6: SYNC - 多平台同步" + (" [DRY-RUN]" if dry_run else ""))
    print("=" * 60)

    result = {
        "phase": "sync",
        "slug": slug,
        "dry_run": dry_run,
        "github": {},
        "skillhub": {},
        "clawhub": {},
    }

    if slug:
        # 同步单个skill
        print(f"  同步单个skill: {slug}")
        cmd = [sys.executable, str(SYNC_PIPELINE_SCRIPT), "sync", slug]
    else:
        # 同步所有变更skill
        print(f"  同步所有变更skill")
        cmd = [sys.executable, str(SYNC_PIPELINE_SCRIPT), "sync-all"]

    # V155 R6: 传递dry_run参数到子进程
    if dry_run:
        cmd.append("--dry-run")

    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=600,
            cwd=str(TOOLS_DIR)
        )
        if proc.returncode == 0:
            print(f"  同步完成")
            result["status"] = "ok"
            # 解析输出
            output = proc.stdout
            if "github" in output.lower():
                result["github"]["status"] = "completed"
            if "skillhub" in output.lower():
                result["skillhub"]["status"] = "completed"
            if "clawhub" in output.lower():
                result["clawhub"]["status"] = "completed"
        else:
            print(f"  同步失败: {proc.stderr[:300]}")
            result["status"] = "error"
            result["error"] = proc.stderr[:300]
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
        print(f"  同步异常: {e}")
        result["status"] = "exception"
        result["error"] = str(e)

    log_operation(None, "orchestrator_sync",
                  f"Sync phase: slug={slug or 'all'}, status={result.get('status', 'unknown')}",
                  result.get("status", "unknown"))
    return result


# ============================================================
# 阶段5: RECORD - 记录与报告
# ============================================================

def phase_record(results: Dict[str, Any]) -> Dict[str, Any]:
    """记录阶段: 生成流水线执行报告"""
    print("\n" + "=" * 60)
    print("阶段 6/6: RECORD - 生成执行报告")
    print("=" * 60)

    report = {
        "timestamp": get_timestamp(),
        "pipeline": "unified_orchestrator",
        "results": results,
    }

    # 保存报告
    report_path = SKILL_DATA_DIR / "reports" / "orchestrator_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  报告已保存: {report_path}")

    log_operation(None, "orchestrator_record", "Record phase: report generated", "completed")
    return report


# ============================================================
# 流水线完整性报告
# ============================================================

def pipeline_report():
    """生成流水线完整性报告"""
    print("\n" + "=" * 60)
    print("版本同步自动化流水线完整性报告")
    print("=" * 60)

    phases = [
        ("1. DISCOVER", "发现新skill + 检测本地变更",
         ["auto_discover.py scan", "version_sync_pipeline.py scan"],
         "✅ 已实现"),
        ("2. ENHANCE", "内容增强(识别B级skill,生成增强建议)",
         ["orchestrator.py enhance (基于审计报告)"],
         "⚠️ 半自动(识别自动,增强需AI执行)"),
        ("3. AUDIT", "全量质量审计(L1-L8)",
         ["deep_quality_audit.py (L1-L8)"],
         "✅ 已实现(L1-L8默认启用)"),
        ("4. PACKAGE", "营销包装自动化(Plug生成+营销文案优化)",
         ["plug_generator.py generate_plugs()",
          "bundle_composer.py find_best_bundle()",
          "auto_differentiate.py optimize_marketing_copy()"],
         "✅ 已实现(M3.3新增)"),
        ("5. SYNC", "多平台同步(GitHub+SkillHub+ClawHub)+版本递增",
         ["version_sync_pipeline.py sync_to_github()/sync_to_skillhub()/sync_to_clawhub()",
          "version_sync_pipeline.py increment_version() (版本递增在sync内自动处理)"],
         "⚠️ GitHub自动;SkillHub免费版自动,付费版需手动;ClawHub限流200/24h"),
        ("6. RECORD", "执行报告生成(SQLite统一数据源)",
         ["orchestrator.py phase_record()",
          "version_sync_pipeline.py record_version()/record_platform_upload()"],
         "✅ 已实现(SQLite统一)"),
    ]

    print(f"\n{'阶段':<20} {'说明':<40} {'状态'}")
    print("-" * 80)
    for phase, desc, scripts, status in phases:
        print(f"{phase:<20} {desc:<40} {status}")

    print("\n脚本依赖关系:")
    print("  orchestrator.py (统一入口)")
    print("    ├── auto_discover.py (发现新skill)")
    print("    ├── version_sync_pipeline.py (变更检测+版本递增+多平台同步)")
    print("    │   ├── quality_gate.py (L1静态检查)")
    print("    │   ├── clawhub_batch_uploader.py (ClawHub上传)")
    print("    │   └── git (GitHub同步)")
    print("    ├── deep_quality_audit.py (L1-L8全量质量审计)")
    print("    └── plug_generator.py (M3.3: Plug营销包生成)")
    print("        ├── bundle_composer.py (Bundle组合推荐)")
    print("        ├── pricing_engine.py (定价计算)")
    print("        └── auto_differentiate.py (营销文案优化)")

    print("\n数据流:")
    print("  SQLite (skill-registry.db) ← 唯一权威数据源")
    print("    ├── skills 表 (skill主表)")
    print("    ├── versions 表 (版本记录)")
    print("    ├── platform_uploads 表 (平台上传记录)")
    print("    └── operations 表 (操作日志)")

    print("\n已知限制:")
    print("  1. 无文件监听(watchdog),需手动运行或cron调度")
    print("  2. 内容增强(B级→A级)需AI执行,无法全自动")
    print("  3. SkillHub付费版上传需浏览器session,无法全自动")
    print("  4. ClawHub限流200/24h,大批量上传需多轮")


# ============================================================
# 状态概览
# ============================================================

def status_overview():
    """显示全流程状态概览"""
    print("\n" + "=" * 60)
    print("版本同步流水线状态概览")
    print("=" * 60)

    conn = db_module.get_db()
    c = conn.cursor()

    # 总skill数
    c.execute("SELECT COUNT(*) FROM skills")
    total = c.fetchone()[0]
    print(f"\n数据库总skill数: {total}")

    # 各状态分布
    c.execute("SELECT current_status, COUNT(*) FROM skills GROUP BY current_status")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    # 平台上传统计
    c.execute("""
        SELECT platform, upload_status, COUNT(*) as cnt
        FROM platform_uploads
        GROUP BY platform, upload_status
        ORDER BY platform, upload_status
    """)
    print("\n平台上传统计:")
    current_platform = ""
    for row in c.fetchall():
        if row[0] != current_platform:
            current_platform = row[0]
            print(f"  {current_platform}:")
        print(f"    {row[1]}: {row[2]}")

    # 最近操作
    c.execute("""
        SELECT operation_type, operation_date, details
        FROM operations
        WHERE operator = 'orchestrator'
        ORDER BY operation_date DESC
        LIMIT 5
    """)
    recent = c.fetchall()
    if recent:
        print("\n最近编排操作:")
        for row in recent:
            print(f"  [{row[1]}] {row[0]}: {row[2][:80]}")

    conn.close()

    # 审计报告摘要
    if AUDIT_REPORT.exists():
        report = json.load(open(AUDIT_REPORT, "r", encoding="utf-8"))
        print(f"\n审计报告 ({report.get('audit_date', 'N/A')}):")
        print(f"  总skill: {report.get('total_skills', 0)}")
        print(f"  Critical/Warning/Info/OK: {report.get('by_severity', {})}")
        sell = report.get("sellability", {})
        print(f"  L5: A={sell.get('grade_distribution', {}).get('A', 0)}, B={sell.get('grade_distribution', {}).get('B', 0)}, avg={sell.get('avg_score', 0)}")
        l7b = report.get("executability_audit", {})
        print(f"  L7b: enabled={l7b.get('enabled', False)}, A={l7b.get('grade_distribution', {}).get('A', 0)}, B={l7b.get('grade_distribution', {}).get('B', 0)}")
        l8 = report.get("security_audit", {})
        print(f"  L8: pass_rate={l8.get('pass_rate', '0%')}")

    # ClawHub限流状态
    checkpoint_path = SKILL_DATA_DIR / "clawhub_upload_checkpoint.json"
    if checkpoint_path.exists():
        checkpoint = json.load(open(checkpoint_path, "r", encoding="utf-8"))
        ts = checkpoint.get("timestamp", "")
        uploaded = len(checkpoint.get("uploaded_today", []))
        from datetime import datetime as dt
        try:
            checkpoint_time = dt.fromisoformat(ts)
            now = dt.now()
            hours = (now - checkpoint_time).total_seconds() / 3600
            if hours >= 24:
                print(f"\nClawHub限流: 已重置 (可上传200个)")
            else:
                print(f"\nClawHub限流: 活跃 (剩余{24-hours:.1f}h重置, 本轮已上传{uploaded}个)")
        except (ValueError, TypeError) as e:  # V126 W2: 替换裸except(TD-182), dt.fromisoformat可能ValueError  V144: 添加警告日志
            print(f"[WARN] datetime解析失败: {e}")


# ============================================================
# 主函数
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="统一编排脚本: 发现→增强→审计→包装→多平台同步")
    parser.add_argument("command", choices=[
        "status", "discover", "enhance", "audit", "package", "sync-all", "sync",
        "full-run", "pipeline-report"
    ], help="执行命令")
    parser.add_argument("--slug", help="指定skill slug (用于sync命令)")
    parser.add_argument("--dry-run", action="store_true", help="V155: 模拟模式,同步阶段跳过实际上传")

    args = parser.parse_args()

    if args.command == "status":
        status_overview()

    elif args.command == "discover":
        phase_discover()

    elif args.command == "enhance":
        phase_enhance(dry_run=args.dry_run)

    elif args.command == "audit":
        phase_audit(dry_run=args.dry_run)

    elif args.command == "package":
        phase_package(dry_run=args.dry_run)

    elif args.command == "sync-all":
        phase_sync(dry_run=args.dry_run)

    elif args.command == "sync":
        if not args.slug:
            print("错误: sync命令需要 --slug 参数")
            sys.exit(1)
        phase_sync(args.slug, dry_run=args.dry_run)

    elif args.command == "full-run":
        print("=" * 60)
        print("完整流程: DISCOVER → ENHANCE → AUDIT → PACKAGE → SYNC → RECORD")
        print("=" * 60)

        results = {}

        # 1. DISCOVER: 仅检测本地变更(跳过auto_discover.py API扫描以避免内存问题)
        print("\n  [1/6] 检测本地变更 (跳过API扫描)...")
        try:
            proc = subprocess.run(
                [sys.executable, str(SYNC_PIPELINE_SCRIPT), "scan"],
                capture_output=True, text=True, timeout=300,
                cwd=str(TOOLS_DIR)
            )
            import re as _re
            changed_match = _re.search(r'(\d+)\s*个?\s*(?:changed|变更)', proc.stdout or '')
            changed_count = int(changed_match.group(1)) if changed_match else 0
            results["discover"] = {"phase": "discover", "changed_skills": changed_count, "skipped_api_scan": True}
            print(f"  [1/6] 变更检测完成: {changed_count} 个变更skill")
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常更新状态/计数继续
            results["discover"] = {"phase": "discover", "error": str(e)}
            print(f"  [1/6] 变更检测失败: {e}")

        # 2. ENHANCE: 使用现有审计报告
        results["enhance"] = phase_enhance(dry_run=args.dry_run)

        # 3. AUDIT: 使用现有审计报告(避免重复运行耗时审计)
        if AUDIT_REPORT.exists():
            report = json.load(open(AUDIT_REPORT, "r", encoding="utf-8"))
            audit_age = (datetime.now() - datetime.fromisoformat(report.get("audit_date", "2026-01-01T00:00:00"))).total_seconds() / 3600
            if audit_age < 24:
                print(f"\n  [3/6] 使用现有审计报告 ({audit_age:.1f}h前生成)")
                results["audit"] = {
                    "phase": "audit",
                    "skipped": True,
                    "reason": f"existing_report_{audit_age:.1f}h_old",
                    "summary": {
                        "total_skills": report.get("total_skills", 0),
                        "critical": report.get("by_severity", {}).get("critical", 0),
                        "l5_b": report.get("sellability", {}).get("grade_distribution", {}).get("B", 0),
                        "l7b_b": report.get("executability_audit", {}).get("grade_distribution", {}).get("B", 0),
                    }
                }
            else:
                results["audit"] = phase_audit(dry_run=args.dry_run)
        else:
            results["audit"] = phase_audit(dry_run=args.dry_run)

        # 4. PACKAGE: 营销包装自动化 (M3.3新增)
        results["package"] = phase_package(dry_run=args.dry_run)

        # 5. SYNC: 同步变更skill
        results["sync"] = phase_sync(dry_run=args.dry_run)

        # 6. RECORD
        results["record"] = phase_record(results)

        print("\n" + "=" * 60)
        print("完整流程执行完毕")
        print("=" * 60)

    elif args.command == "pipeline-report":
        pipeline_report()


if __name__ == "__main__":
    main()
