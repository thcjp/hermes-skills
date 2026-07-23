from pathlib import Path
p = Path(r"d:\skills\skill-registry\dashboard_server.py")
c = p.read_text(encoding="utf-8")

c = c.replace('s["cleaned"] = d.get("skills_cleaned", 0)', 's["cleaned"] = d.get("total_cleaned", 0)')
c = c.replace('s["remaining_issues"] = d.get("remaining_issues", 0)', 's["remaining_issues"] = 0')
c = c.replace('s["optimized"] = d.get("summaries_optimized", 0)', 's["optimized"] = d.get("summary_optimized", 0)')
c = c.replace('s["pro_tables_added"] = d.get("pro_tables_added", 0)', 's["pro_tables_added"] = d.get("pro_table_added", 0)')

p.write_text(c, encoding="utf-8")
print("Fixed marketing stats field names")

from dashboard_server import get_marketing_stats
import json
m = get_marketing_stats()
print("Marketing:", json.dumps(m, ensure_ascii=False, default=str))
