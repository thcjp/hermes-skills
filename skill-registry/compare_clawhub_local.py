#!/usr/bin/env python3
"""Compare ClawHub published skills with local packaged skills to find old skills to withdraw."""
import json
import os
import sys
from pathlib import Path

# === Phase 1: 统一配置导入 ===
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, PACKAGED_SKILLS_DIR, DIFFERENTIATED_DIR
# === End Phase 1 ===

# Load ClawHub published slugs
with open(str(TOOLS_DIR / "clawhub_published_slugs.json"), "r", encoding="utf-8") as f:
    clawhub_slugs = set(json.load(f))

# Get local packaged skill folder names
local_skills_dir = str(PACKAGED_SKILLS_DIR)
local_slugs = set()
for item in os.listdir(local_skills_dir):
    item_path = os.path.join(local_skills_dir, item)
    if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "SKILL.md")):
        local_slugs.add(item)

# Also get differentiated skill slugs
diff_skills_dir = str(DIFFERENTIATED_DIR)
diff_slugs = set()
if os.path.exists(diff_skills_dir):
    for category in os.listdir(diff_skills_dir):
        cat_path = os.path.join(diff_skills_dir, category)
        if os.path.isdir(cat_path):
            for skill in os.listdir(cat_path):
                skill_path = os.path.join(cat_path, skill)
                if os.path.isdir(skill_path) and os.path.exists(os.path.join(skill_path, "SKILL.md")):
                    diff_slugs.add(skill)

# Skills on ClawHub but NOT in local packaged or differentiated
all_local = local_slugs | diff_slugs
on_clawhub_not_local = clawhub_slugs - all_local
on_local_not_clawhub = all_local - clawhub_slugs

# Skills in both
in_both = clawhub_slugs & all_local

print(f"ClawHub published: {len(clawhub_slugs)}")
print(f"Local packaged: {len(local_slugs)}")
print(f"Local differentiated: {len(diff_slugs)}")
print(f"All local: {len(all_local)}")
print(f"In both: {len(in_both)}")
print(f"On ClawHub but NOT local: {len(on_clawhub_not_local)}")
print(f"On local but NOT ClawHub: {len(on_local_not_clawhub)}")
print()
print("=== Skills on ClawHub but NOT in local (candidates for withdrawal) ===")
for slug in sorted(on_clawhub_not_local):
    print(f"  {slug}")

# Save the withdrawal list
withdrawal_list = sorted(on_clawhub_not_local)
with open(r"D:\skills\skill-registry\clawhub_withdrawal_list.json", "w", encoding="utf-8") as f:
    json.dump(withdrawal_list, f, indent=2, ensure_ascii=False)

print(f"\nWithdrawal list saved to D:\\skills\\skill-registry\\clawhub_withdrawal_list.json ({len(withdrawal_list)} skills)")
