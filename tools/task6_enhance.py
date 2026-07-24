from pathlib import Path
import re

DASHBOARD = TOOLS_DIR / "dashboard_server.py"
c = DASHBOARD.read_text(encoding="utf-8")

# === Step 1: Add data functions ===
new_funcs = '''

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
            s["cleaned"] = d.get("skills_cleaned", 0)
            s["remaining_issues"] = d.get("remaining_issues", 0)
        op = rd / "marketing_optimization_report.json"
        if op.exists():
            import json as _j
            d = _j.loads(op.read_text(encoding="utf-8"))
            s["optimized"] = d.get("summaries_optimized", 0)
            s["pro_tables_added"] = d.get("pro_tables_added", 0)
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

'''
marker = "def get_file_stats():"
c = c.replace(marker, new_funcs + "\n" + marker, 1)

# === Step 2: Add API endpoints ===
old_api = "        elif path == '/api/task-status':"
new_api = """        elif path == '/api/l7-audit':
            self._json(get_l7_audit_stats())

        elif path == '/api/pricing':
            self._json(get_pricing_stats())

        elif path == '/api/marketing':
            self._json(get_marketing_stats())

        elif path == '/api/license':
            self._json(get_license_stats())

        elif path == '/api/task-status':"""
c = c.replace(old_api, new_api, 1)

# === Step 3: Add HTML blocks ===
old_src = """  <!-- 来源分布 -->
  <div class="card col-6">
    <div class="card-title">来源分布</div>
    <div class="bar-chart" id="sourceChart">
      <div style="color:var(--text-dim);text-align:center;padding:20px;">加载中...</div>
    </div>
  </div>"""

new_src = old_src + """
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
"""
c = c.replace(old_src, new_src, 1)

# === Step 4: Add JS data loading ===
old_js = "    // 来源分布\n    renderBarChart('sourceChart', stats.sources, 'info');"
new_js = """    // 来源分布
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
    }"""
c = c.replace(old_js, new_js, 1)

# Write back
DASHBOARD.write_text(c, encoding="utf-8")

# Verify
vc = DASHBOARD.read_text(encoding="utf-8")
checks = [
    ("get_l7_audit_stats", "get_l7_audit_stats" in vc),
    ("get_pricing_stats", "get_pricing_stats" in vc),
    ("get_marketing_stats", "get_marketing_stats" in vc),
    ("get_license_stats", "get_license_stats" in vc),
    ("/api/l7-audit", "/api/l7-audit" in vc),
    ("/api/pricing", "/api/pricing" in vc),
    ("/api/marketing", "/api/marketing" in vc),
    ("/api/license", "/api/license" in vc),
    ("Layer 7 语义审计", "Layer 7 语义审计" in vc),
    ("定价分布", "定价分布 (L1-L4)" in vc),
    ("营销话术质量", "营销话术质量" in vc),
    ("License 一致性", "License 一致性" in vc),
    ("l7GradeChart", "l7GradeChart" in vc),
    ("pricingChart", "pricingChart" in vc),
    ("JS l7-audit", "fetchAPI('/api/l7-audit')" in vc),
    ("JS pricing", "fetchAPI('/api/pricing')" in vc),
    ("JS marketing", "fetchAPI('/api/marketing')" in vc),
    ("JS license", "fetchAPI('/api/license')" in vc),
]
all_ok = all(ok for _, ok in checks)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print(f"\nResult: {'ALL PASS' if all_ok else 'HAS FAILURES'}")
print(f"File size: {len(vc)} chars")
