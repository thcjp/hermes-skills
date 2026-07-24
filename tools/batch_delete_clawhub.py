#!/usr/bin/env python3
"""Batch delete old skills from ClawHub that are no longer in local directory."""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, DATA_DIR
# === End Phase 1 ===

import json
import subprocess
import time
import sys

# Load withdrawal list
with open(str(DATA_DIR / "reports" / "clawhub_withdrawal_list.json"), "r", encoding="utf-8") as f:
    withdrawal_list = json.load(f)

print(f"Total skills to delete: {len(withdrawal_list)}")

success = []
failed = []

for i, slug in enumerate(withdrawal_list):
    print(f"[{i+1}/{len(withdrawal_list)}] Deleting {slug}...", end=" ", flush=True)
    try:
        result = subprocess.run(
            f'npx clawhub --registry "https://clawhub.ai" delete {slug} --reason "Replaced by quality-verified version" --yes',
            capture_output=True, text=True, timeout=30, cwd=r"D:\skills", shell=True
        )
        if result.returncode == 0:
            print("OK")
            success.append(slug)
        else:
            err = result.stderr.strip()[:100] if result.stderr else result.stdout.strip()[:100]
            print(f"FAIL: {err}")
            failed.append({"slug": slug, "error": err})
    except subprocess.TimeoutExpired:
        print("TIMEOUT")
        failed.append({"slug": slug, "error": "timeout"})
    except Exception as e:
        print(f"ERROR: {e}")
        failed.append({"slug": slug, "error": str(e)})
    
    # Small delay to avoid rate limiting
    time.sleep(0.5)

print(f"\n=== Summary ===")
print(f"Success: {len(success)}")
print(f"Failed: {len(failed)}")

# Save results
with open(str(DATA_DIR / "reports" / "clawhub_delete_results.json"), "w", encoding="utf-8") as f:
    json.dump({"success": success, "failed": failed}, f, indent=2, ensure_ascii=False)

print(f"Results saved to data/reports/clawhub_delete_results.json")
