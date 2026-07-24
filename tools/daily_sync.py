#!/usr/bin/env python3
"""
每日同步脚本 (Daily Sync)
=========================
统一入口，执行完整的每日同步流程：
1. 发现新 Skill + 检测变更
2. 版本同步流水线
3. 质量审计
4. 平台同步（GitHub、SkillHub、ClawHub）
5. 数据库记录
6. 生成每日报告

使用方式:
    python tools/daily_sync.py              # 完整同步
    python tools/daily_sync.py --discover   # 仅发现
    python tools/daily_sync.py --audit      # 仅审计
    python tools/daily_sync.py --report     # 仅生成报告
"""

import sys
import os
import json
import subprocess
import sqlite3
from pathlib import Path
from datetime import datetime

# 统一配置导入
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import (
    DB_PATH, TOOLS_DIR, DATA_DIR, REPORT_DIR,
    HEALTH_REPORT_DIR, DISCOVERY_DIR
)
from platform_config import GITHUB_REPOS


def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")


def run_script(script_name, args=None):
    """运行工具脚本"""
    script_path = TOOLS_DIR / script_name
    if not script_path.exists():
        log(f"  ERROR: {script_name} not found")
        return False

    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            cwd=str(TOOLS_DIR.parent)
        )
        if result.returncode == 0:
            log(f"  OK: {script_name}")
            if result.stdout:
                log(f"  Output: {result.stdout[:500]}")
            return True
        else:
            log(f"  FAIL: {script_name} (exit {result.returncode})")
            if result.stderr:
                log(f"  Error: {result.stderr[:500]}")
            return False
    except subprocess.TimeoutExpired:
        log(f"  TIMEOUT: {script_name}")
        return False
    except Exception as e:
        log(f"  ERROR: {script_name}: {e}")
        return False


def step_discover():
    """阶段1: 发现新 Skill + 检测变更"""
    log("=" * 50)
    log("阶段1: DISCOVER - 发现与变更检测")
    log("=" * 50)
    run_script("version_sync_pipeline.py", ["scan"])
    run_script("auto_discover.py")


def step_audit():
    """阶段4: 质量审计"""
    log("=" * 50)
    log("阶段4: VALIDATE - L1-L8 质量审计")
    log("=" * 50)
    run_script("deep_quality_audit.py")


def step_sync_github():
    """阶段5: GitHub 同步"""
    log("=" * 50)
    log("阶段5: SYNC_GITHUB - GitHub 双仓库同步")
    log("=" * 50)
    # Git push to both remotes
    for repo in GITHUB_REPOS:
        try:
            result = subprocess.run(
                ["git", "push", repo["name"], "main"],
                capture_output=True, text=True, timeout=120,
                cwd=str(TOOLS_DIR.parent)
            )
            if result.returncode == 0:
                log(f"  OK: git push {repo['name']}")
            else:
                log(f"  FAIL: git push {repo['name']}: {result.stderr[:200]}")
        except Exception as e:
            log(f"  ERROR: git push {repo['name']}: {e}")


def step_sync_clawhub():
    """阶段7: ClawHub 同步"""
    log("=" * 50)
    log("阶段7: SYNC_CLAWHUB - ClawHub 批量上传")
    log("=" * 50)
    run_script("clawhub_batch_uploader.py", ["--dry-run"])


def generate_daily_report():
    """生成每日报告"""
    log("=" * 50)
    log("生成每日同步报告")
    log("=" * 50)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    report = {
        "date": datetime.now().strftime('%Y-%m-%d'),
        "timestamp": datetime.now().isoformat(),
        "summary": {},
        "three_track": {},
        "platforms": {},
        "quality": {},
    }

    # 总览
    c.execute("SELECT COUNT(*) as cnt FROM skills")
    report["summary"]["total_skills"] = c.fetchone()["cnt"]

    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'active'")
    report["summary"]["active"] = c.fetchone()["cnt"]

    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'updated'")
    report["summary"]["updated"] = c.fetchone()["cnt"]

    c.execute("SELECT COUNT(*) as cnt FROM skills WHERE current_status = 'stale'")
    report["summary"]["stale"] = c.fetchone()["cnt"]

    # 三轨模型
    c.execute("SELECT skill_type, COUNT(*) as cnt FROM skills GROUP BY skill_type ORDER BY cnt DESC")
    report["three_track"] = {row["skill_type"]: row["cnt"] for row in c.fetchall()}

    # 平台上传状态
    c.execute("SELECT platform, upload_status, COUNT(*) as cnt FROM platform_uploads GROUP BY platform, upload_status ORDER BY platform")
    for row in c.fetchall():
        p = row["platform"]
        if p not in report["platforms"]:
            report["platforms"][p] = {}
        report["platforms"][p][row["upload_status"]] = row["cnt"]

    # 定价分层
    c.execute("SELECT pricing_tier, COUNT(*) as cnt FROM skills GROUP BY pricing_tier ORDER BY cnt DESC")
    report["quality"]["pricing_tiers"] = {row["pricing_tier"]: row["cnt"] for row in c.fetchall()}

    # 最近操作
    c.execute("""SELECT operation_type, COUNT(*) as cnt 
                 FROM operations 
                 WHERE operation_date >= date('now', '-1 day') 
                 GROUP BY operation_type ORDER BY cnt DESC""")
    report["recent_operations"] = {row["operation_type"]: row["cnt"] for row in c.fetchall()}

    conn.close()

    # 保存报告
    report_path = HEALTH_REPORT_DIR / f"daily_sync_{datetime.now().strftime('%Y%m%d')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    log(f"  报告已保存: {report_path}")

    # 打印摘要
    log(f"\n  总 Skill 数: {report['summary']['total_skills']}")
    log(f"  三轨分布: {report['three_track']}")
    for platform, statuses in report["platforms"].items():
        log(f"  {platform}: {statuses}")

    return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description="每日同步脚本")
    parser.add_argument("--discover", action="store_true", help="仅执行发现阶段")
    parser.add_argument("--audit", action="store_true", help="仅执行审计阶段")
    parser.add_argument("--report", action="store_true", help="仅生成报告")
    parser.add_argument("--full", action="store_true", help="完整同步（默认）")
    args = parser.parse_args()

    log("每日同步开始")
    log(f"数据库: {DB_PATH}")

    if args.discover:
        step_discover()
    elif args.audit:
        step_audit()
    elif args.report:
        generate_daily_report()
    else:
        # 完整流程
        step_discover()
        step_audit()
        step_sync_github()
        step_sync_clawhub()
        generate_daily_report()

    log("\n每日同步完成!")


if __name__ == "__main__":
    main()
