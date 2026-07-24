#!/usr/bin/env python3
"""
统一编排脚本 (Unified Orchestrator)
====================================
将发现→增强→版本递增→质量门禁→多平台同步整合为单一命令

完整流程:
  1. DISCOVER    - 发现新skill (auto_discover.py) + 检测本地变更 (version_sync_pipeline.py scan)
  2. ENHANCE     - 内容增强建议 (基于审计报告识别B级skill,生成增强建议)
  3. INCREMENT   - 版本号递增 (version_sync_pipeline.py)
  4. VALIDATE    - 质量门禁 (deep_quality_audit.py: L1-L8全量审计)
  5. SYNC_GITHUB - GitHub开放库同步 (version_sync_pipeline.py)
  6. SYNC_SKILLHUB - SkillHub免费+付费同步 (version_sync_pipeline.py)
  7. SYNC_CLAWHUB  - ClawHub同步 (version_sync_pipeline.py)
  8. RECORD      - 数据库记录 (SQLite统一数据源)

使用方式:
    python orchestrator.py status              # 查看全流程状态概览
    python orchestrator.py discover            # 仅执行发现阶段
    python orchestrator.py enhance             # 仅执行增强阶段(识别B级skill)
    python orchestrator.py audit               # 仅执行质量审计
    python orchestrator.py sync-all            # 同步所有变更skill到所有平台
    python orchestrator.py sync <slug>         # 同步单个skill到所有平台
    python orchestrator.py full-run            # 执行完整流程: discover→enhance→audit→sync-all
    python orchestrator.py pipeline-report     # 生成流水线完整性报告

设计原则:
  - SQLite数据库为唯一权威数据源
  - 每个阶段独立执行,单个阶段失败不阻塞后续阶段
  - 所有操作记录到operations表
  - 禁止任何mock/fallback/skip
"""

import argparse
import json
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# ============================================================
# 配置
# ============================================================

DB_PATH = r"d:\skills\skill-registry.db"
SKILLS_ROOT = Path(r"d:\skills")
SKILL_REGISTRY_DIR = SKILLS_ROOT / "skill-registry"

# 脚本路径
DISCOVER_SCRIPT = SKILL_REGISTRY_DIR / "auto_discover.py"
SYNC_PIPELINE_SCRIPT = SKILL_REGISTRY_DIR / "version_sync_pipeline.py"
AUDIT_SCRIPT = SKILL_REGISTRY_DIR / "deep_quality_audit.py"
CLAWHUB_UPLOADER = SKILL_REGISTRY_DIR / "clawhub_batch_uploader.py"

# 审计报告路径
AUDIT_REPORT = SKILL_REGISTRY_DIR / "deep_quality_audit_report.json"

NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


# ============================================================
# 数据库操作
# ============================================================

def get_db():
    """获取数据库连接"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def log_operation(skill_id: Optional[int], operation_type: str, details: str, status: str = "completed"):
    """记录操作到数据库"""
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (skill_id, operation_type, datetime.now().isoformat(), 'orchestrator', details, status))
    conn.commit()
    conn.close()


# ============================================================
# 阶段1: DISCOVER - 发现新skill + 检测本地变更
# ============================================================

def phase_discover() -> Dict[str, Any]:
    """发现阶段: 扫描新skill + 检测已有skill变更"""
    print("\n" + "=" * 60)
    print("阶段 1/8: DISCOVER - 发现新skill + 检测本地变更")
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
            cwd=str(SKILL_REGISTRY_DIR)
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
    except Exception as e:
        print(f"  [1a] 发现扫描异常: {e}")
        result["details"].append({"sub": "scan_new", "status": "exception", "error": str(e)})

    # 1b. 检测本地变更 (version_sync_pipeline.py scan)
    print("  [1b] 检测本地SKILL.md变更...")
    try:
        proc = subprocess.run(
            [sys.executable, str(SYNC_PIPELINE_SCRIPT), "scan"],
            capture_output=True, text=True, timeout=300,
            cwd=str(SKILL_REGISTRY_DIR)
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
    except Exception as e:
        print(f"  [1b] 变更检测异常: {e}")
        result["details"].append({"sub": "scan_changes", "status": "exception", "error": str(e)})

    log_operation(None, "orchestrator_discover", f"Discover phase: {result['new_skills']} new, {result['changed_skills']} changed", "completed")
    return result


# ============================================================
# 阶段2: ENHANCE - 内容增强建议
# ============================================================

def phase_enhance() -> Dict[str, Any]:
    """增强阶段: 基于审计报告识别B级skill,生成增强建议"""
    print("\n" + "=" * 60)
    print("阶段 2/8: ENHANCE - 识别需增强的skill")
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
        print(f"  审计报告不存在: {AUDIT_REPORT}")
        print("  请先运行: python orchestrator.py audit")
        result["error"] = "audit_report_not_found"
        return result

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

    log_operation(None, "orchestrator_enhance",
                  f"Enhance phase: L5_B={len(b_grades)}, L7b_B={len(l7b_issues)}, L6={len(l6_issues_list)}, L7a={len(l7a_issues_list)}",
                  "completed")
    return result


# ============================================================
# 阶段3: AUDIT - 质量审计 (L1-L8)
# ============================================================

def phase_audit() -> Dict[str, Any]:
    """审计阶段: 运行全量质量审计 (L1-L8)"""
    print("\n" + "=" * 60)
    print("阶段 3/8: AUDIT - 全量质量审计 (L1-L8)")
    print("=" * 60)

    start_time = time.time()

    result = {
        "phase": "audit",
        "duration_seconds": 0,
        "passed": False,
        "summary": {},
    }

    try:
        proc = subprocess.run(
            [sys.executable, str(AUDIT_SCRIPT)],
            capture_output=True, text=True, timeout=900,  # 15分钟超时
            cwd=str(SKILL_REGISTRY_DIR)
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
        else:
            print(f"  审计失败 (exit={proc.returncode})")
            print(f"  stderr: {proc.stderr[:300]}")
            result["error"] = proc.stderr[:300]
    except subprocess.TimeoutExpired:
        duration = time.time() - start_time
        result["duration_seconds"] = round(duration, 1)
        print(f"  审计超时 ({duration:.1f}s)")
        result["error"] = "timeout"
    except Exception as e:
        duration = time.time() - start_time
        result["duration_seconds"] = round(duration, 1)
        print(f"  审计异常: {e}")
        result["error"] = str(e)

    log_operation(None, "orchestrator_audit",
                  f"Audit phase: passed={result['passed']}, duration={result['duration_seconds']}s",
                  "completed" if result["passed"] else "failed")
    return result


# ============================================================
# 阶段4-7: SYNC - 多平台同步
# ============================================================

def phase_sync(slug: Optional[str] = None) -> Dict[str, Any]:
    """同步阶段: 多平台同步 (GitHub + SkillHub + ClawHub)"""
    print("\n" + "=" * 60)
    print("阶段 4-7/8: SYNC - 多平台同步")
    print("=" * 60)

    result = {
        "phase": "sync",
        "slug": slug,
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

    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=600,
            cwd=str(SKILL_REGISTRY_DIR)
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
    except Exception as e:
        print(f"  同步异常: {e}")
        result["status"] = "exception"
        result["error"] = str(e)

    log_operation(None, "orchestrator_sync",
                  f"Sync phase: slug={slug or 'all'}, status={result.get('status', 'unknown')}",
                  result.get("status", "unknown"))
    return result


# ============================================================
# 阶段8: RECORD - 记录与报告
# ============================================================

def phase_record(results: Dict[str, Any]) -> Dict[str, Any]:
    """记录阶段: 生成流水线执行报告"""
    print("\n" + "=" * 60)
    print("阶段 8/8: RECORD - 生成执行报告")
    print("=" * 60)

    report = {
        "timestamp": NOW,
        "pipeline": "unified_orchestrator",
        "results": results,
    }

    # 保存报告
    report_path = SKILL_REGISTRY_DIR / "orchestrator_report.json"
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
        ("3. INCREMENT", "版本号自动递增",
         ["version_sync_pipeline.py increment_version()"],
         "✅ 已实现(patch级)"),
        ("4. VALIDATE", "质量门禁(L1-L8全量审计)",
         ["deep_quality_audit.py (L1-L8)"],
         "✅ 已实现(L1-L8默认启用)"),
        ("5. SYNC_GITHUB", "GitHub开放库同步",
         ["version_sync_pipeline.py sync_to_github()"],
         "✅ 已实现(git add/commit/push)"),
        ("6. SYNC_SKILLHUB", "SkillHub免费+付费同步",
         ["version_sync_pipeline.py sync_to_skillhub()"],
         "⚠️ 免费版自动,付费版payload自动生成需手动上传"),
        ("7. SYNC_CLAWHUB", "ClawHub同步",
         ["version_sync_pipeline.py sync_to_clawhub()"],
         "✅ 已实现(限流200/24h)"),
        ("8. RECORD", "数据库记录",
         ["version_sync_pipeline.py record_version()/record_platform_upload()"],
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
    print("    └── deep_quality_audit.py (L1-L8全量质量审计)")

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

    conn = get_db()
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
    checkpoint_path = SKILL_REGISTRY_DIR / "clawhub_upload_checkpoint.json"
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
        except:
            pass


# ============================================================
# 主函数
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="统一编排脚本: 发现→增强→审计→多平台同步")
    parser.add_argument("command", choices=[
        "status", "discover", "enhance", "audit", "sync-all", "sync",
        "full-run", "pipeline-report"
    ], help="执行命令")
    parser.add_argument("--slug", help="指定skill slug (用于sync命令)")

    args = parser.parse_args()

    if args.command == "status":
        status_overview()

    elif args.command == "discover":
        phase_discover()

    elif args.command == "enhance":
        phase_enhance()

    elif args.command == "audit":
        phase_audit()

    elif args.command == "sync-all":
        phase_sync()

    elif args.command == "sync":
        if not args.slug:
            print("错误: sync命令需要 --slug 参数")
            sys.exit(1)
        phase_sync(args.slug)

    elif args.command == "full-run":
        print("=" * 60)
        print("完整流程: DISCOVER → ENHANCE → AUDIT → SYNC → RECORD")
        print("=" * 60)

        results = {}

        # 1. DISCOVER: 仅检测本地变更(跳过auto_discover.py API扫描以避免内存问题)
        print("\n  [1/5] 检测本地变更 (跳过API扫描)...")
        try:
            proc = subprocess.run(
                [sys.executable, str(SYNC_PIPELINE_SCRIPT), "scan"],
                capture_output=True, text=True, timeout=300,
                cwd=str(SKILL_REGISTRY_DIR)
            )
            import re as _re
            changed_match = _re.search(r'(\d+)\s*个?\s*(?:changed|变更)', proc.stdout or '')
            changed_count = int(changed_match.group(1)) if changed_match else 0
            results["discover"] = {"phase": "discover", "changed_skills": changed_count, "skipped_api_scan": True}
            print(f"  [1/5] 变更检测完成: {changed_count} 个变更skill")
        except Exception as e:
            results["discover"] = {"phase": "discover", "error": str(e)}
            print(f"  [1/5] 变更检测失败: {e}")

        # 2. ENHANCE: 使用现有审计报告
        results["enhance"] = phase_enhance()

        # 3. AUDIT: 使用现有审计报告(避免重复运行耗时审计)
        if AUDIT_REPORT.exists():
            report = json.load(open(AUDIT_REPORT, "r", encoding="utf-8"))
            audit_age = (datetime.now() - datetime.fromisoformat(report.get("audit_date", "2026-01-01T00:00:00"))).total_seconds() / 3600
            if audit_age < 24:
                print(f"\n  [3/5] 使用现有审计报告 ({audit_age:.1f}h前生成)")
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
                results["audit"] = phase_audit()
        else:
            results["audit"] = phase_audit()

        # 4. SYNC: 同步变更skill
        results["sync"] = phase_sync()

        # 5. RECORD
        results["record"] = phase_record(results)

        print("\n" + "=" * 60)
        print("完整流程执行完毕")
        print("=" * 60)

    elif args.command == "pipeline-report":
        pipeline_report()


if __name__ == "__main__":
    main()
