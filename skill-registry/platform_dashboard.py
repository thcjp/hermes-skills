#!/usr/bin/env python3
"""
Three-Platform Publishing Dashboard
====================================
Reads upload_tracking.json and displays real-time status across:
1. SkillHub (main monetization platform)
2. ClawHub (free traffic, 200/day limit)
3. Hermes (free exposure, agentskills.io standard)

Usage:
    python platform_dashboard.py              # Full dashboard
    python platform_dashboard.py --json       # JSON output for automation
    python platform_dashboard.py --pending    # Show only pending/retry items
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import Counter

DB_FILE = Path(r"D:\skills\skill-registry\upload_tracking.json")
HERMES_DIR = Path(r"D:\skills\hermes-skills")


def load_db():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_hermes_count():
    """Count valid Hermes skills on disk."""
    if not HERMES_DIR.exists():
        return 0
    return len([d for d in HERMES_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()])


def analyze_skillhub(skills):
    """Analyze SkillHub status from database."""
    stats = {
        "public_published": 0,
        "published": 0,
        "pending_review": 0,
        "pending": 0,
        "pending_retry": 0,
        "uploaded": 0,
        "deleted": 0,
        "discovered": 0,
        "other": 0,
    }
    pending_list = []
    retry_list = []
    
    for slug, info in skills.items():
        if info.get("is_source"):
            continue
        stage = info.get("lifecycle", {}).get("stage", "unknown")
        if stage in stats:
            stats[stage] += 1
        else:
            stats["other"] += 1
        
        if stage == "pending":
            pending_list.append(slug)
        elif stage == "pending_retry":
            retry_list.append(slug)
    
    return stats, pending_list, retry_list


def analyze_clawhub(skills):
    """Analyze ClawHub status from database."""
    published = 0
    not_uploaded = 0
    not_eligible = 0
    
    for slug, info in skills.items():
        if info.get("is_source"):
            continue
        stage = info.get("lifecycle", {}).get("stage", "")
        if stage in ("deleted", "discovered"):
            continue
        
        is_free = info.get("is_free", False)
        clawhub = info.get("clawhub", {})
        ch_status = clawhub.get("status", "")
        
        if ch_status == "published":
            published += 1
        elif is_free and stage not in ("deleted",):
            not_uploaded += 1
        elif not is_free:
            not_eligible += 1
    
    return {
        "published": published,
        "not_uploaded": not_uploaded,
        "not_eligible": not_eligible,
    }


def analyze_hermes(skills):
    """Analyze Hermes status from database."""
    eligible = 0
    not_eligible = 0
    converted = get_hermes_count()
    
    for slug, info in skills.items():
        if info.get("is_source"):
            continue
        stage = info.get("lifecycle", {}).get("stage", "")
        if stage in ("deleted", "discovered"):
            continue
        
        is_free = info.get("is_free", False)
        hermes = info.get("hermes", {})
        
        if is_free:
            eligible += 1
        else:
            not_eligible += 1
    
    return {
        "eligible": eligible,
        "converted": converted,
        "published": 0,  # Not published to GitHub yet
        "not_eligible": not_eligible,
    }


def print_dashboard(db, show_pending=False, json_output=False):
    skills = db.get("skills", {})
    
    # Filter out source skills
    prod_skills = {s: i for s, i in skills.items() if not i.get("is_source")}
    total_prod = len(prod_skills)
    
    sh_stats, sh_pending, sh_retry = analyze_skillhub(prod_skills)
    ch_stats = analyze_clawhub(prod_skills)
    hermes_stats = analyze_hermes(prod_skills)
    
    if json_output:
        output = {
            "timestamp": datetime.now().isoformat(),
            "total_production_skills": total_prod,
            "skillhub": {**sh_stats, "pending_list": sh_pending, "retry_list": sh_retry},
            "clawhub": ch_stats,
            "hermes": hermes_stats,
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return
    
    if show_pending:
        print(f"\n=== Pending Items ===")
        print(f"\nSkillHub Pending ({len(sh_pending)}):")
        for s in sh_pending:
            print(f"  - {s}")
        print(f"\nSkillHub Pending Retry ({len(sh_retry)}):")
        for s in sh_retry:
            print(f"  - {s}")
        print(f"\nClawHub Not Uploaded: {ch_stats['not_uploaded']}")
        print(f"Hermes Not Published: {hermes_stats['eligible'] - hermes_stats['published']}")
        return
    
    print("=" * 70)
    print(f"  Three-Platform Publishing Dashboard")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    print(f"\n📊 Total Production Skills: {total_prod}")
    
    # SkillHub
    print(f"\n{'─'*70}")
    print(f" 📦 SkillHub (Main Monetization)")
    print(f"{'─'*70}")
    sh_total = sum(sh_stats.values())
    print(f"  Public Published : {sh_stats['public_published']:>6} ({sh_stats['public_published']*100//sh_total if sh_total else 0}%)")
    print(f"  Published        : {sh_stats['published']:>6}")
    print(f"  Pending Review   : {sh_stats['pending_review']:>6}  ← uploaded, awaiting review")
    print(f"  Pending          : {sh_stats['pending']:>6}  ← needs upload")
    print(f"  Pending Retry    : {sh_stats['pending_retry']:>6}  ← needs retry")
    print(f"  Uploaded         : {sh_stats['uploaded']:>6}")
    print(f"  Deleted          : {sh_stats['deleted']:>6}")
    print(f"  Discovered       : {sh_stats['discovered']:>6}")
    if sh_stats['other']:
        print(f"  Other            : {sh_stats['other']:>6}")
    print(f"  {'─'*40}")
    print(f"  Total            : {sh_total:>6}")
    
    # ClawHub
    print(f"\n{'─'*70}")
    print(f" 🦞 ClawHub (Free Traffic, 200/day limit)")
    print(f"{'─'*70}")
    ch_total = ch_stats['published'] + ch_stats['not_uploaded'] + ch_stats['not_eligible']
    print(f"  Published        : {ch_stats['published']:>6}")
    print(f"  Not Uploaded     : {ch_stats['not_uploaded']:>6}  ← free skills pending")
    print(f"  Not Eligible     : {ch_stats['not_eligible']:>6}  ← paid (10% promo only)")
    print(f"  {'─'*40}")
    print(f"  Total            : {ch_total:>6}")
    if ch_stats['not_uploaded'] > 0:
        days = (ch_stats['not_uploaded'] + 199) // 200
        print(f"  Est. days remaining: {days} (at 200/day)")
    
    # Hermes
    print(f"\n{'─'*70}")
    print(f" 🏛️ Hermes (Free Exposure, agentskills.io)")
    print(f"{'─'*70}")
    print(f"  Eligible         : {hermes_stats['eligible']:>6}")
    print(f"  Converted        : {hermes_stats['converted']:>6}  ← on disk, ready")
    print(f"  Published        : {hermes_stats['published']:>6}  ← GitHub repo")
    print(f"  Not Eligible     : {hermes_stats['not_eligible']:>6}  ← paid skills")
    
    # Summary
    print(f"\n{'='*70}")
    print(f" 📋 Action Items Summary")
    print(f"{'='*70}")
    actions = []
    if sh_stats['pending'] > 0:
        actions.append(f"  ⬆ SkillHub: Upload {sh_stats['pending']} pending skills")
    if sh_stats['pending_retry'] > 0:
        actions.append(f"  🔄 SkillHub: Retry {sh_stats['pending_retry']} rejected skills")
    if ch_stats['not_uploaded'] > 0:
        actions.append(f"  ⬆ ClawHub: Upload {ch_stats['not_uploaded']} free skills (~{(ch_stats['not_uploaded']+199)//200} days)")
    if hermes_stats['converted'] > 0 and hermes_stats['published'] == 0:
        actions.append(f"  📤 Hermes: Push {hermes_stats['converted']} skills to GitHub")
    
    if actions:
        for a in actions:
            print(a)
    else:
        print("  ✅ All platforms up to date!")
    
    print(f"\n{'='*70}")


def main():
    parser = argparse.ArgumentParser(description="Three-Platform Publishing Dashboard")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--pending", action="store_true", help="Show only pending items")
    args = parser.parse_args()
    
    db = load_db()
    print_dashboard(db, show_pending=args.pending, json_output=args.json)


if __name__ == "__main__":
    main()
