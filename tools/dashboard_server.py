"""
Skill 管理看板 - 全自动流水线可视化
启动: python dashboard_server.py
访问: http://localhost:8765
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import REGISTRY_DIR
from project_config import DB_PATH
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===


import http.server
import sqlite3
import json
import subprocess
import threading
import time
import os
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# DB_PATH imported from config
# REGISTRY_DIR imported from config
PORT = 8765

# ====== 任务状态追踪 ======
task_status = {
    "discover": {"status": "idle", "message": "", "last_run": "", "result": ""},
    "update": {"status": "idle", "message": "", "last_run": "", "result": ""},
    "governance": {"status": "idle", "message": "", "last_run": "", "result": ""},
    "upload": {"status": "idle", "message": "", "last_run": "", "result": ""},
}


def get_db_stats():
    """从数据库获取统计数据"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    stats = {"total_skills": 0, "free_count": 0, "paid_count": 0,
             "categories": {}, "platforms": {}, "quality": {}, "recent_ops": [],
             "sources": {}, "workflow_states": {}}

    try:
        c.execute("SELECT COUNT(*) as cnt FROM skills")
        stats["total_skills"] = c.fetchone()["cnt"]

        # 付费/免费统计: 通过slug后缀判断(-free=免费, 无后缀=付费)
        c.execute("SELECT COUNT(*) as cnt FROM skills WHERE slug NOT LIKE '%%-free'")
        stats["paid_count"] = c.fetchone()["cnt"]
        c.execute("SELECT COUNT(*) as cnt FROM skills WHERE slug LIKE '%%-free'")
        stats["free_count"] = c.fetchone()["cnt"]

        c.execute("SELECT category, COUNT(*) as cnt FROM skills WHERE category IS NOT NULL GROUP BY category ORDER BY cnt DESC LIMIT 15")
        stats["categories"] = {row["category"]: row["cnt"] for row in c.fetchall()}

        c.execute("SELECT platform, upload_status, COUNT(*) as cnt FROM platform_uploads GROUP BY platform, upload_status")
        for row in c.fetchall():
            p = row["platform"]
            s = row["upload_status"]
            if p not in stats["platforms"]:
                stats["platforms"][p] = {}
            stats["platforms"][p][s] = row["cnt"]

        c.execute("SELECT current_status, COUNT(*) as cnt FROM skills GROUP BY current_status")
        stats["quality"] = {row["current_status"]: row["cnt"] for row in c.fetchall()}

        c.execute("SELECT source, COUNT(*) as cnt FROM skills GROUP BY source ORDER BY cnt DESC LIMIT 10")
        stats["sources"] = {row["source"]: row["cnt"] for row in c.fetchall()}

        c.execute("SELECT workflow_state, COUNT(*) as cnt FROM skills GROUP BY workflow_state")
        stats["workflow_states"] = {row["workflow_state"]: row["cnt"] for row in c.fetchall()}

        c.execute("""SELECT o.operation_type, o.operation_date, s.slug, s.current_display_name
                     FROM operations o JOIN skills s ON o.skill_id = s.id
                     ORDER BY o.operation_date DESC LIMIT 20""")
        stats["recent_ops"] = [{"type": r["operation_type"], "date": r["operation_date"],
                                "slug": r["slug"], "name": r["current_display_name"]} for r in c.fetchall()]
    except Exception as e:
        stats["error"] = str(e)
    finally:
        conn.close()
    return stats




def get_l7_audit_stats():
    audit_report = Path(DATA_DIR) / "reports" / "deep_quality_audit_report.json"
    if not audit_report.exists():
        return {"available": False}
    try:
        import json as _j
        data = _j.loads(audit_report.read_text(encoding="utf-8"))
        sa = data.get("semantic_audit", {})
        return {"available": True, "audit_date": data.get("audit_date", ""),
                "l7a_count": sa.get("l7a_available_count", 0),
                "grade_distribution": sa.get("grade_distribution", {}),
                "avg_score": sa.get("avg_score", 0),
                "total_template_blocks": sa.get("total_template_blocks", 0),
                "total_with_issues": sa.get("total_with_issues", 0)}
    except Exception as e:
        return {"available": False, "error": str(e)}


def get_l7b_stats():
    audit_report = Path(DATA_DIR) / "reports" / "l7b_executability_report.json"
    if not audit_report.exists():
        return {"available": False}
    try:
        import json as _j
        data = _j.loads(audit_report.read_text(encoding="utf-8"))
        return {"available": True, "generated_at": data.get("generated_at", ""),
                "total_skills": data.get("total_skills", 0),
                "grade_distribution": data.get("grade_distribution", {}),
                "checks_distribution": data.get("checks_distribution", {}),
                "pass_rate": data.get("pass_rate", "0%"),
                "avg_score": data.get("avg_l7b_score", 0),
                "executable_count": data.get("executable_count", 0)}
    except Exception as e:
        return {"available": False, "error": str(e)}


def get_l8_security_stats():
    """获取L8安全审计统计 (从 deep_quality_audit_report.json 读取)"""
    audit_report = Path(DATA_DIR) / "reports" / "deep_quality_audit_report.json"
    if not audit_report.exists():
        return {"available": False}
    try:
        import json as _j
        data = _j.loads(audit_report.read_text(encoding="utf-8"))
        sa = data.get("security_audit", {})
        if not sa:
            return {"available": False}
        return {"available": True, "audit_date": data.get("audit_date", ""),
                "enabled": sa.get("enabled", False),
                "l8_available_count": sa.get("l8_available_count", 0),
                "grade_distribution": sa.get("grade_distribution", {}),
                "avg_score": sa.get("avg_score", 0),
                "passed_count": sa.get("passed_count", 0),
                "failed_count": sa.get("failed_count", 0),
                "pass_rate": sa.get("pass_rate", "0%"),
                "category_distribution": sa.get("category_distribution", {}),
                "total_with_issues": sa.get("total_with_issues", 0)}
    except Exception as e:
        return {"available": False, "error": str(e)}


def get_pricing_stats():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    s = {"available": False, "tier_distribution": {}, "total_priced": 0,
         "avg_price": 0, "revenue_estimate": 0}
    try:
        c.execute("SELECT edition, COUNT(*) as cnt FROM pricing GROUP BY edition ORDER BY edition")
        for r in c.fetchall():
            s["tier_distribution"][r["edition"]] = r["cnt"]
        c.execute("SELECT COUNT(*) as cnt, AVG(price_amount) as avg FROM pricing")
        r = c.fetchone()
        s["total_priced"] = r["cnt"]
        s["avg_price"] = round(r["avg"] or 0, 1)
        c.execute("SELECT SUM(price_amount) as t FROM pricing WHERE price_model = ?", ("monthly",))
        m = c.fetchone()["t"] or 0
        c.execute("SELECT SUM(price_amount) as t FROM pricing WHERE price_model = ?", ("per_use",))
        pu = c.fetchone()["t"] or 0
        s["revenue_estimate"] = round(m + pu * 100, 0)
        s["available"] = True
    except Exception as e:
        s["error"] = str(e)
    finally:
        conn.close()
    return s


def get_marketing_stats():
    s = {"available": False, "total_paid": 0, "cleaned": 0,
         "optimized": 0, "pro_tables_added": 0, "remaining_issues": 0}
    rd = Path(DATA_DIR) / "reports"
    try:
        cr = rd / "marketing_cleanup_report.json"
        if cr.exists():
            import json as _j
            d = _j.loads(cr.read_text(encoding="utf-8"))
            s["cleaned"] = d.get("total_cleaned", 0)
            s["remaining_issues"] = 0
        op = rd / "marketing_optimization_report.json"
        if op.exists():
            import json as _j
            d = _j.loads(op.read_text(encoding="utf-8"))
            s["optimized"] = d.get("summary_optimized", 0)
            s["pro_tables_added"] = d.get("pro_table_added", 0)
        conn = sqlite3.connect(DB_PATH)
        cc = conn.cursor()
        cc.execute("SELECT COUNT(*) FROM skills WHERE slug NOT LIKE ?", ("%-free",))
        s["total_paid"] = cc.fetchone()[0]
        conn.close()
        s["available"] = True
    except Exception as e:
        s["error"] = str(e)
    return s


def get_license_stats():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    s = {"available": False, "proprietary_count": 0, "mit_count": 0,
         "total_checked": 0, "consistent": 0, "inconsistent": 0}
    try:
        c.execute("SELECT source_license, COUNT(*) as cnt FROM skills GROUP BY source_license")
        for r in c.fetchall():
            lic = r["source_license"] or "unknown"
            if "Proprietary" in lic:
                s["proprietary_count"] += r["cnt"]
            elif "MIT" in lic:
                s["mit_count"] += r["cnt"]
            s["total_checked"] += r["cnt"]
        lr = Path(DATA_DIR) / "reports" / "license_sync_report.json"
        if lr.exists():
            import json as _j
            d = _j.loads(lr.read_text(encoding="utf-8"))
            s["consistent"] = d.get("consistent_count", s["total_checked"])
            s["inconsistent"] = d.get("inconsistent_count", 0)
        else:
            s["consistent"] = s["total_checked"]
        s["available"] = True
    except Exception as e:
        s["error"] = str(e)
    finally:
        conn.close()
    return s


def get_file_stats():
    """从文件系统获取补充统计"""
    stats = {"skillhub_dirs": 0, "clawhub_dirs": 0, "diff_dirs": 0, "reports": []}
    sh = Path(r"d:\skills\packaged-skills\skillhub")
    if sh.exists():
        stats["skillhub_dirs"] = len([d for d in sh.iterdir() if d.is_dir()])
    ch = Path(r"d:\skills\packaged-skills\clawhub")
    if ch.exists():
        stats["clawhub_dirs"] = len([d for d in ch.iterdir() if d.is_dir()])
    df = DIFFERENTIATED_DIR
    if df.exists():
        stats["diff_dirs"] = len([d for d in df.iterdir() if d.is_dir()])

    reports_dir = Path(DATA_DIR) / "reports"
    if reports_dir.exists():
        reports = sorted(reports_dir.glob("*.html"), key=lambda p: p.stat().st_mtime, reverse=True)
        stats["reports"] = [{"name": r.name, "size": r.stat().st_size} for r in reports[:5]]
    return stats


def run_async_task(task_name, command, cwd=REGISTRY_DIR):
    """异步执行任务"""
    task_status[task_name]["status"] = "running"
    task_status[task_name]["message"] = f"正在执行: {command}"
    task_status[task_name]["last_run"] = time.strftime("%Y-%m-%d %H:%M:%S")

    def _run():
        try:
            result = subprocess.run(
                command, shell=True, cwd=cwd, capture_output=True, text=True, timeout=600
            )
            if result.returncode == 0:
                task_status[task_name]["status"] = "completed"
                task_status[task_name]["message"] = "执行完成"
                task_status[task_name]["result"] = result.stdout[-2000:] if result.stdout else ""
            else:
                task_status[task_name]["status"] = "failed"
                task_status[task_name]["message"] = f"执行失败 (exit {result.returncode})"
                task_status[task_name]["result"] = result.stderr[-2000:] if result.stderr else ""
        except subprocess.TimeoutExpired:
            task_status[task_name]["status"] = "timeout"
            task_status[task_name]["message"] = "执行超时 (10分钟)"
        except Exception as e:
            task_status[task_name]["status"] = "failed"
            task_status[task_name]["message"] = str(e)

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Skill 管理看板</title>
<style>
:root {
  --bg: #0F1117;
  --surface: #1A1D29;
  --surface-2: #232735;
  --border: #2E3343;
  --text: #E4E7EF;
  --text-muted: #8B92A5;
  --text-dim: #5C6378;
  --brand: #7C5CFC;
  --brand-light: rgba(124, 92, 252, 0.12);
  --accent: #00D4AA;
  --accent-light: rgba(0, 212, 170, 0.12);
  --warn: #FFB547;
  --warn-light: rgba(255, 181, 71, 0.12);
  --danger: #FF5C7A;
  --danger-light: rgba(255, 92, 122, 0.12);
  --info: #4DA3FF;
  --info-light: rgba(77, 163, 255, 0.12);
  --radius: 10px;
  --radius-sm: 6px;
  --font: -apple-system, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  --mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.6;
}
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 32px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}
.header h1 {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.5px;
}
.header h1 span { color: var(--brand); }
.header .meta {
  font-size: 13px;
  color: var(--text-muted);
}
.actions {
  display: flex;
  gap: 12px;
  padding: 20px 32px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  flex-wrap: wrap;
}
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface-2);
  color: var(--text);
  font-size: 14px;
  font-weight: 500;
  font-family: var(--font);
  cursor: pointer;
  transition: all 0.18s;
  white-space: nowrap;
}
.btn:hover {
  border-color: var(--brand);
  background: var(--brand-light);
  transform: translateY(-1px);
}
.btn:active { transform: translateY(0); }
.btn.primary { border-color: var(--brand); background: var(--brand); color: #fff; }
.btn.primary:hover { background: #6B4CE0; }
.btn.accent { border-color: var(--accent); color: var(--accent); }
.btn.accent:hover { background: var(--accent-light); }
.btn .icon { font-size: 16px; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
.task-badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 600;
  margin-left: 4px;
}
.task-badge.idle { background: var(--surface-2); color: var(--text-dim); }
.task-badge.running { background: var(--info-light); color: var(--info); }
.task-badge.completed { background: var(--accent-light); color: var(--accent); }
.task-badge.failed { background: var(--danger-light); color: var(--danger); }
.task-badge.timeout { background: var(--warn-light); color: var(--warn); }
.main {
  padding: 24px 32px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px;
}
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
}
.card-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.col-3 { grid-column: span 3; }
.col-4 { grid-column: span 4; }
.col-6 { grid-column: span 6; }
.col-8 { grid-column: span 8; }
.col-12 { grid-column: span 12; }
.metric {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.metric-value {
  font-size: 32px;
  font-weight: 700;
  font-family: var(--mono);
  letter-spacing: -1px;
}
.metric-value.brand { color: var(--brand); }
.metric-value.accent { color: var(--accent); }
.metric-value.warn { color: var(--warn); }
.metric-value.danger { color: var(--danger); }
.metric-label {
  font-size: 12px;
  color: var(--text-muted);
}
.metric-sub {
  font-size: 11px;
  color: var(--text-dim);
  margin-top: 2px;
}
.bar-chart {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.bar-row {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
}
.bar-label {
  width: 100px;
  text-align: right;
  color: var(--text-muted);
  flex-shrink: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.bar-track {
  flex: 1;
  height: 22px;
  background: var(--surface-2);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}
.bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  padding: 0 8px;
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.9);
  white-space: nowrap;
}
.bar-fill.brand { background: var(--brand); }
.bar-fill.accent { background: var(--accent); }
.bar-fill.warn { background: var(--warn); }
.bar-fill.info { background: var(--info); }
.bar-fill.danger { background: var(--danger); }
.platform-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.platform-card {
  background: var(--surface-2);
  border-radius: var(--radius-sm);
  padding: 16px;
  text-align: center;
}
.platform-name {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 8px;
}
.platform-stat {
  font-size: 24px;
  font-weight: 700;
  font-family: var(--mono);
}
.platform-detail {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 4px;
}
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}
.table th {
  text-align: left;
  padding: 8px 12px;
  border-bottom: 1px solid var(--border);
  color: var(--text-muted);
  font-weight: 600;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}
.table td {
  padding: 8px 12px;
  border-bottom: 1px solid var(--border);
}
.table tr:last-child td { border-bottom: none; }
.table tr:hover td { background: var(--surface-2); }
.tag {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
}
.tag.brand { background: var(--brand-light); color: var(--brand); }
.tag.accent { background: var(--accent-light); color: var(--accent); }
.tag.warn { background: var(--warn-light); color: var(--warn); }
.tag.danger { background: var(--danger-light); color: var(--danger); }
.tag.info { background: var(--info-light); color: var(--info); }
.log-panel {
  max-height: 300px;
  overflow-y: auto;
  background: #0A0C12;
  border-radius: var(--radius-sm);
  padding: 12px;
  font-family: var(--mono);
  font-size: 12px;
  line-height: 1.8;
}
.log-line { color: var(--text-muted); }
.log-line .ts { color: var(--text-dim); }
.log-line .ok { color: var(--accent); }
.log-line .err { color: var(--danger); }
.log-line .warn { color: var(--warn); }
.refresh-spin {
  display: inline-block;
  animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.loading-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(15, 17, 23, 0.8);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 999;
}
.loading-overlay.show { display: flex; }
.spinner {
  width: 40px; height: 40px;
  border: 3px solid var(--surface-2);
  border-top-color: var(--brand);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@media (max-width: 1200px) {
  .col-3 { grid-column: span 6; }
  .col-4 { grid-column: span 6; }
  .col-6 { grid-column: span 12; }
  .col-8 { grid-column: span 12; }
}
</style>
</head>
<body>

<div class="header">
  <h1>Skill <span>管理看板</span></h1>
  <div class="meta" id="lastRefresh">加载中...</div>
</div>

<div class="actions">
  <button class="btn primary" onclick="runTask('discover')">
    <span class="icon">🔍</span> 发现
    <span class="task-badge idle" id="badge-discover">待命</span>
  </button>
  <button class="btn accent" onclick="runTask('update')">
    <span class="icon">🔄</span> 更新
    <span class="task-badge idle" id="badge-update">待命</span>
  </button>
  <button class="btn" onclick="runTask('governance')">
    <span class="icon">🛡</span> 治理
    <span class="task-badge idle" id="badge-governance">待命</span>
  </button>
  <button class="btn" onclick="runTask('upload')">
    <span class="icon">📤</span> 上传运营
    <span class="task-badge idle" id="badge-upload">待命</span>
  </button>
  <button class="btn" onclick="refreshData()" style="margin-left:auto;">
    <span class="icon" id="refreshIcon">📊</span> 刷新数据
  </button>
</div>

<div class="main" id="dashboard">
  <!-- 核心指标 -->
  <div class="card col-3">
    <div class="metric">
      <div class="metric-value brand" id="m-total">--</div>
      <div class="metric-label">生产 Skill 总数</div>
      <div class="metric-sub" id="m-total-sub">--</div>
    </div>
  </div>
  <div class="card col-3">
    <div class="metric">
      <div class="metric-value accent" id="m-paid">--</div>
      <div class="metric-label">付费 Skill</div>
      <div class="metric-sub" id="m-paid-sub">--</div>
    </div>
  </div>
  <div class="card col-3">
    <div class="metric">
      <div class="metric-value warn" id="m-free">--</div>
      <div class="metric-label">免费 Skill</div>
      <div class="metric-sub" id="m-free-sub">--</div>
    </div>
  </div>
  <div class="card col-3">
    <div class="metric">
      <div class="metric-value" id="m-revenue">--</div>
      <div class="metric-label">月收入预估 (CNY)</div>
      <div class="metric-sub" id="m-revenue-sub">--</div>
    </div>
  </div>

  <!-- 三平台发布状态 -->
  <div class="card col-6">
    <div class="card-title">三平台发布状态</div>
    <div class="platform-grid" id="platformGrid">
      <div class="platform-card">
        <div class="platform-name" style="color:var(--brand)">SkillHub</div>
        <div class="platform-stat" id="p-skillhub">--</div>
        <div class="platform-detail" id="p-skillhub-detail">--</div>
      </div>
      <div class="platform-card">
        <div class="platform-name" style="color:var(--accent)">ClawHub</div>
        <div class="platform-stat" id="p-clawhub">--</div>
        <div class="platform-detail" id="p-clawhub-detail">--</div>
      </div>
      <div class="platform-card">
        <div class="platform-name" style="color:var(--info)">Hermes</div>
        <div class="platform-stat" id="p-hermes">--</div>
        <div class="platform-detail" id="p-hermes-detail">--</div>
      </div>
    </div>
  </div>

  <!-- 质量分布 -->
  <div class="card col-6">
    <div class="card-title">质量状态分布</div>
    <div class="bar-chart" id="qualityChart">
      <div style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</div>
    </div>
  </div>

  <!-- 分类分布 -->
  <div class="card col-6">
    <div class="card-title">分类分布 (Top 15)</div>
    <div class="bar-chart" id="categoryChart">
      <div style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</div>
    </div>
  </div>

  <!-- 来源分布 -->
  <div class="card col-6">
    <div class="card-title">来源分布</div>
    <div class="bar-chart" id="sourceChart">
      <div style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</div>
    </div>
  </div>
  <!-- L7语义审计结果 -->
  <div class="card col-6">
    <div class="card-title">Layer 7 语义审计</div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:12px;">
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--brand)" id="l7-avg">--</div>
        <div style="font-size:11px;color:var(--text-dim)">平均分</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--accent)" id="l7-count">--</div>
        <div style="font-size:11px;color:var(--text-dim)">审计数</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--warn)" id="l7-issues">--</div>
        <div style="font-size:11px;color:var(--text-dim)">问题skill</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--danger)" id="l7-templates">--</div>
        <div style="font-size:11px;color:var(--text-dim)">模板块</div>
      </div>
    </div>
    <div class="bar-chart" id="l7GradeChart">
      <div style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</div>
    </div>
  </div>

  <!-- L7b 可执行性审计 -->
  <div class="card col-6">
    <div class="card-title">L7b 可执行性审计</div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:12px;">
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--accent)" id="l7b-passrate">--</div>
        <div style="font-size:11px;color:var(--text-dim)">通过率</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--brand)" id="l7b-avg">--</div>
        <div style="font-size:11px;color:var(--text-dim)">平均分</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--info)" id="l7b-exec">--</div>
        <div style="font-size:11px;color:var(--text-dim)">可执行数</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--warn)" id="l7b-total">--</div>
        <div style="font-size:11px;color:var(--text-dim)">总审计数</div>
      </div>
    </div>
    <div class="bar-chart" id="l7bGradeChart">
      <div style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</div>
    </div>
    <div style="margin-top:12px;">
      <div style="font-size:12px;color:var(--text-muted);margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px;">检查项分布</div>
      <ul id="l7bChecksList" style="list-style:none;display:flex;flex-direction:column;gap:6px;">
        <li style="color:var(--text-dim);text-align:center;padding:12px;">加载中...</li>
      </ul>
    </div>
  </div>

  <!-- 定价分布 -->
  <div class="card col-6">
    <div class="card-title">定价分布 (L1-L4)</div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:12px;">
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--brand)" id="pr-total">--</div>
        <div style="font-size:11px;color:var(--text-dim)">已定价</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--accent)" id="pr-avg">--</div>
        <div style="font-size:11px;color:var(--text-dim)">均价(CNY)</div>
      </div>
      <div style="text-align:center;min-width:80px;">
        <div style="font-size:24px;font-weight:700;color:var(--warn)" id="pr-revenue">--</div>
        <div style="font-size:11px;color:var(--text-dim)">月收入预估</div>
      </div>
    </div>
    <div class="bar-chart" id="pricingChart">
      <div style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</div>
    </div>
  </div>

  <!-- 营销话术质量 -->
  <div class="card col-3">
    <div class="card-title">营销话术质量</div>
    <div style="text-align:center;padding:10px 0;">
      <div style="font-size:28px;font-weight:700;color:var(--accent)" id="mk-cleaned">--</div>
      <div style="font-size:12px;color:var(--text-dim)">已清理自毁话术</div>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px;">
      <div style="flex:1;text-align:center;padding:6px;background:var(--surface-2);border-radius:6px;">
        <div style="font-size:16px;font-weight:600;color:var(--brand)" id="mk-optimized">--</div>
        <div style="font-size:10px;color:var(--text-dim)">已优化</div>
      </div>
      <div style="flex:1;text-align:center;padding:6px;background:var(--surface-2);border-radius:6px;">
        <div style="font-size:16px;font-weight:600;color:var(--info)" id="mk-protables">--</div>
        <div style="font-size:10px;color:var(--text-dim)">专享表</div>
      </div>
      <div style="flex:1;text-align:center;padding:6px;background:var(--surface-2);border-radius:6px;">
        <div style="font-size:16px;font-weight:600;color:var(--danger)" id="mk-remaining">--</div>
        <div style="font-size:10px;color:var(--text-dim)">残留</div>
      </div>
    </div>
  </div>

  <!-- License一致性 -->
  <div class="card col-3">
    <div class="card-title">License 一致性</div>
    <div style="text-align:center;padding:10px 0;">
      <div style="font-size:28px;font-weight:700;color:var(--accent)" id="lic-consistent">--</div>
      <div style="font-size:12px;color:var(--text-dim)">一致性</div>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px;">
      <div style="flex:1;text-align:center;padding:6px;background:var(--surface-2);border-radius:6px;">
        <div style="font-size:16px;font-weight:600;color:var(--brand)" id="lic-prop">--</div>
        <div style="font-size:10px;color:var(--text-dim)">Proprietary</div>
      </div>
      <div style="flex:1;text-align:center;padding:6px;background:var(--surface-2);border-radius:6px;">
        <div style="font-size:16px;font-weight:600;color:var(--info)" id="lic-mit">--</div>
        <div style="font-size:10px;color:var(--text-dim)">MIT</div>
      </div>
      <div style="flex:1;text-align:center;padding:6px;background:var(--surface-2);border-radius:6px;">
        <div style="font-size:16px;font-weight:600;color:var(--danger)" id="lic-incons">--</div>
        <div style="font-size:10px;color:var(--text-dim)">不一致</div>
      </div>
    </div>
  </div>


  <!-- 最近操作 -->
  <div class="card col-8">
    <div class="card-title">最近操作记录</div>
    <table class="table" id="opsTable">
      <thead>
        <tr><th>时间</th><th>类型</th><th>Slug</th><th>名称</th></tr>
      </thead>
      <tbody id="opsBody">
        <tr><td colspan="4" style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</td></tr>
      </tbody>
    </table>
  </div>

  <!-- 任务日志 -->
  <div class="card col-4">
    <div class="card-title">任务执行日志</div>
    <div class="log-panel" id="logPanel">
      <div class="log-line"><span class="ts">[--:--:--]</span> 等待任务执行...</div>
    </div>
  </div>
</div>

<div class="loading-overlay" id="overlay">
  <div class="spinner"></div>
</div>

<script>
let autoRefreshTimer = null;

async function fetchAPI(path) {
  const resp = await fetch(path);
  return resp.json();
}

function formatNum(n) {
  if (n >= 10000) return (n / 10000).toFixed(1) + 'W';
  if (n >= 1000) return (n / 1000).toFixed(1) + 'K';
  return String(n);
}

function maxBarValue(obj) {
  return Math.max(...Object.values(obj), 1);
}

function renderBarChart(elementId, data, colorClass) {
  const el = document.getElementById(elementId);
  if (!data || Object.keys(data).length === 0) {
    el.innerHTML = '<div style="color:var(--text-dim);text-align:center;padding:20px;">暂无数据</div>';
    return;
  }
  const max = maxBarValue(data);
  const sorted = Object.entries(data).sort((a, b) => b[1] - a[1]);
  el.innerHTML = sorted.map(([label, val]) => {
    const pct = (val / max * 100).toFixed(1);
    return `<div class="bar-row">
      <div class="bar-label" title="${label}">${label}</div>
      <div class="bar-track">
        <div class="bar-fill ${colorClass}" style="width:${pct}%">${val}</div>
      </div>
    </div>`;
  }).join('');
}

async function refreshData() {
  const icon = document.getElementById('refreshIcon');
  icon.classList.add('refresh-spin');
  try {
    const [stats, files] = await Promise.all([
      fetchAPI('/api/stats'),
      fetchAPI('/api/files')
    ]);

    // 核心指标
    document.getElementById('m-total').textContent = formatNum(stats.total_skills);
    document.getElementById('m-total-sub').textContent = `本地目录: ${files.skillhub_dirs} packaged + ${files.diff_dirs} differentiated`;
    document.getElementById('m-paid').textContent = formatNum(stats.paid_count);
    document.getElementById('m-paid-sub').textContent = `占比 ${stats.total_skills ? (stats.paid_count / stats.total_skills * 100).toFixed(0) : 0}%`;
    document.getElementById('m-free').textContent = formatNum(stats.free_count);
    document.getElementById('m-free-sub').textContent = `占比 ${stats.total_skills ? (stats.free_count / stats.total_skills * 100).toFixed(0) : 0}%`;

    // 收入预估: 付费skill数 × 预估月100次 × 均价15 CNY
    const revenue = stats.paid_count * 100 * 15;
    document.getElementById('m-revenue').textContent = formatNum(revenue);
    document.getElementById('m-revenue-sub').textContent = `均价15 CNY × 月100次/skill`;

    // 平台状态
    const platforms = stats.platforms || {};
    const sh = platforms['skillhub'] || {};
    const shPublished = (sh['published'] || 0) + (sh['ok'] || 0) + (sh['success'] || 0);
    const shPending = (sh['pending'] || 0) + (sh['pending_review'] || 0);
    document.getElementById('p-skillhub').textContent = formatNum(shPublished);
    document.getElementById('p-skillhub-detail').textContent = `待审 ${shPending} · 总 ${shPublished + shPending}`;

    const ch = platforms['clawhub'] || {};
    const chPublished = (ch['published'] || 0) + (ch['ok'] || 0) + (ch['success'] || 0);
    const chPending = (ch['pending'] || 0);
    document.getElementById('p-clawhub').textContent = formatNum(chPublished);
    document.getElementById('p-clawhub-detail').textContent = `待传 ${chPending} · 限频200/天`;

    const hr = platforms['hermes'] || {};
    const hrPublished = (hr['published'] || 0) + (hr['ok'] || 0) + (hr['success'] || 0);
    document.getElementById('p-hermes').textContent = formatNum(hrPublished);
    document.getElementById('p-hermes-detail').textContent = `开源同步`;

    // 质量分布
    renderBarChart('qualityChart', stats.quality, 'brand');

    // 分类分布
    renderBarChart('categoryChart', stats.categories, 'accent');

    // 来源分布
    renderBarChart('sourceChart', stats.sources, 'info');

    // L7审计结果
    const l7 = await fetchAPI('/api/l7-audit');
    if (l7.available) {
      document.getElementById('l7-avg').textContent = (l7.avg_score || 0).toFixed(1);
      document.getElementById('l7-count').textContent = formatNum(l7.l7a_count || 0);
      document.getElementById('l7-issues').textContent = formatNum(l7.total_with_issues || 0);
      document.getElementById('l7-templates').textContent = formatNum(l7.total_template_blocks || 0);
      const grades = l7.grade_distribution || {};
      const gLabels = {'A': 'A级', 'B': 'B级', 'C': 'C级', 'D': 'D级', 'F': 'F级'};
      const gData = {};
      for (const [k, label] of Object.entries(gLabels)) {
        if (grades[k]) gData[label] = grades[k];
      }
      renderBarChart('l7GradeChart', gData, 'accent');
    }

    // L7b可执行性审计结果
    const l7b = await fetchAPI('/api/l7b-audit');
    if (l7b.available) {
      document.getElementById('l7b-passrate').textContent = l7b.pass_rate || '--';
      document.getElementById('l7b-avg').textContent = (l7b.avg_score || 0).toFixed(1);
      document.getElementById('l7b-exec').textContent = formatNum(l7b.executable_count || 0);
      document.getElementById('l7b-total').textContent = formatNum(l7b.total_skills || 0);
      const bGrades = l7b.grade_distribution || {};
      const bLabels = {'A': 'A级', 'B': 'B级', 'C': 'C级', 'D': 'D级', 'F': 'F级'};
      const bData = {};
      for (const [k, label] of Object.entries(bLabels)) {
        if (bGrades[k]) bData[label] = bGrades[k];
      }
      renderBarChart('l7bGradeChart', bData, 'info');
      const checks = l7b.checks_distribution || {};
      const checkLabels = {
        'L7B_NO_CODE': '无代码',
        'L7B_BROKEN_REF': '引用断裂',
        'L7B_VAGUE_TASK': '任务模糊',
        'L7B_MISSING_INPUT': '缺少输入',
        'L7B_NO_OUTPUT': '无输出说明',
        'L7B_CONTRADICTION': '内容矛盾'
      };
      const checksList = document.getElementById('l7bChecksList');
      const checkEntries = Object.entries(checkLabels)
        .map(([key, label]) => [label, checks[key] || 0])
        .filter(([, val]) => val > 0)
        .sort((a, b) => b[1] - a[1]);
      if (checkEntries.length === 0) {
        checksList.innerHTML = '<li style="color:var(--text-dim);text-align:center;padding:12px;">无检查项问题</li>';
      } else {
        checksList.innerHTML = checkEntries.map(([label, val]) => {
          const cls = val > 500 ? 'danger' : val > 100 ? 'warn' : 'info';
          return `<li style="display:flex;align-items:center;justify-content:space-between;padding:6px 10px;background:var(--surface-2);border-radius:6px;font-size:13px;">
            <span style="color:var(--text);">${label}</span>
            <span class="tag ${cls}">${formatNum(val)}</span>
          </li>`;
        }).join('');
      }
    }

    // 定价分布
    const pricing = await fetchAPI('/api/pricing');
    if (pricing.available) {
      document.getElementById('pr-total').textContent = formatNum(pricing.total_priced || 0);
      document.getElementById('pr-avg').textContent = (pricing.avg_price || 0).toFixed(1);
      document.getElementById('pr-revenue').textContent = formatNum(pricing.revenue_estimate || 0);
      const tLabels = {'L1': 'L1-入门(9.9)', 'L2': 'L2-标准(19.9)', 'L3': 'L3-专业(29.9)', 'L4': 'L4-企业(99.9)'};
      const tData = {};
      const tiers = pricing.tier_distribution || {};
      for (const [k, label] of Object.entries(tLabels)) {
        if (tiers[k]) tData[label] = tiers[k];
      }
      renderBarChart('pricingChart', tData, 'brand');
    }

    // 营销话术质量
    const marketing = await fetchAPI('/api/marketing');
    if (marketing.available) {
      document.getElementById('mk-cleaned').textContent = formatNum(marketing.cleaned || 0);
      document.getElementById('mk-optimized').textContent = formatNum(marketing.optimized || 0);
      document.getElementById('mk-protables').textContent = formatNum(marketing.pro_tables_added || 0);
      document.getElementById('mk-remaining').textContent = formatNum(marketing.remaining_issues || 0);
    }

    // License一致性
    const license = await fetchAPI('/api/license');
    if (license.available) {
      const pct = license.total_checked > 0 ? ((license.consistent / license.total_checked) * 100).toFixed(1) + '%' : '--';
      document.getElementById('lic-consistent').textContent = pct;
      document.getElementById('lic-prop').textContent = formatNum(license.proprietary_count || 0);
      document.getElementById('lic-mit').textContent = formatNum(license.mit_count || 0);
      document.getElementById('lic-incons').textContent = formatNum(license.inconsistent || 0);
    }

    // 操作记录
    const opsBody = document.getElementById('opsBody');
    if (stats.recent_ops && stats.recent_ops.length > 0) {
      opsBody.innerHTML = stats.recent_ops.map(op => {
        const tagClass = op.type.includes('upload') ? 'info' : op.type.includes('fix') ? 'warn' : 'brand';
        return `<tr>
          <td style="color:var(--text-dim);font-size:12px">${op.date || '--'}</td>
          <td><span class="tag ${tagClass}">${op.type || '--'}</span></td>
          <td style="font-family:var(--mono);font-size:12px">${op.slug || '--'}</td>
          <td>${op.name || '--'}</td>
        </tr>`;
      }).join('');
    } else {
      opsBody.innerHTML = '<tr><td colspan="4" style="color:var(--text-dim);text-align:center;padding:20px;">暂无操作记录</td></tr>';
    }

    document.getElementById('lastRefresh').textContent = '更新于 ' + new Date().toLocaleTimeString('zh-CN');
  } catch (e) {
    addLog('err', '数据刷新失败: ' + e.message);
  } finally {
    icon.classList.remove('refresh-spin');
  }
}

async function runTask(taskName) {
  const badge = document.getElementById('badge-' + taskName);
  badge.className = 'task-badge running';
  badge.textContent = '执行中';

  addLog('warn', `启动任务: ${taskName}`);
  try {
    const resp = await fetchAPI(`/api/run/${taskName}`);
    addLog('ok', `任务 ${taskName} 已启动: ${resp.message}`);
  } catch (e) {
    addLog('err', `任务启动失败: ${e.message}`);
    badge.className = 'task-badge failed';
    badge.textContent = '失败';
  }
}

async function checkTaskStatus() {
  try {
    const status = await fetchAPI('/api/task-status');
    for (const [name, info] of Object.entries(status)) {
      const badge = document.getElementById('badge-' + name);
      if (!badge) continue;
      const labels = {idle: '待命', running: '执行中', completed: '完成', failed: '失败', timeout: '超时'};
      badge.className = 'task-badge ' + info.status;
      badge.textContent = labels[info.status] || info.status;
      if (info.status === 'completed' && info.result) {
        addLog('ok', `${name} 完成: ${info.message}`);
      } else if (info.status === 'failed') {
        addLog('err', `${name} 失败: ${info.message}`);
      }
    }
  } catch(e) {}
}

function addLog(level, msg) {
  const panel = document.getElementById('logPanel');
  const ts = new Date().toLocaleTimeString('zh-CN');
  const line = document.createElement('div');
  line.className = 'log-line';
  line.innerHTML = `<span class="ts">[${ts}]</span> <span class="${level}">${msg}</span>`;
  panel.insertBefore(line, panel.firstChild);
  while (panel.children.length > 50) panel.removeChild(panel.lastChild);
}

// 初始化
refreshData();
setInterval(checkTaskStatus, 3000);
setInterval(refreshData, 30000); // 30秒自动刷新
</script>
</body>
</html>"""


class DashboardHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/' or path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(DASHBOARD_HTML.encode('utf-8'))

        elif path == '/api/stats':
            stats = get_db_stats()
            self._json(stats)

        elif path == '/api/files':
            self._json(get_file_stats())

        elif path == '/api/l7-audit':
            self._json(get_l7_audit_stats())

        elif path == '/api/l7b-audit':
            self._json(get_l7b_stats())

        elif path == '/api/l8-security':
            self._json(get_l8_security_stats())

        elif path == '/api/pricing':
            self._json(get_pricing_stats())

        elif path == '/api/marketing':
            self._json(get_marketing_stats())

        elif path == '/api/license':
            self._json(get_license_stats())

        elif path == '/api/task-status':
            self._json(task_status)

        elif path.startswith('/api/run/'):
            task_name = path.split('/api/run/')[1]
            self._handle_run(task_name)

        else:
            self.send_response(404)
            self.end_headers()

    def _json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False, default=str).encode('utf-8'))

    def _handle_run(self, task_name):
        if task_name not in task_status:
            self._json({"error": "unknown task"})
            return

        commands = {
            "discover": "python auto_discover.py scan --source all",
            "update": "python update_mechanism.py check",
            "governance": "python clean_naming.py execute",
            "upload": "python auto_publish.py auto-flow",
        }

        cmd = commands.get(task_name)
        if not cmd:
            self._json({"error": "no command for task"})
            return

        run_async_task(task_name, cmd)
        self._json({"message": f"任务 {task_name} 已启动", "command": cmd})


def main():
    print(f"Skill 管理看板启动中...")
    print(f"访问: http://localhost:{PORT}")
    print(f"数据库: {DB_PATH}")
    print(f"按 Ctrl+C 停止")

    server = http.server.HTTPServer(('0.0.0.0', PORT), DashboardHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n看板已停止")
        server.shutdown()


if __name__ == '__main__':
    main()
