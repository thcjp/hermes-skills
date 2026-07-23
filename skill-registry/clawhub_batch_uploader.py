#!/usr/bin/env python3
"""
ClawHub Batch Uploader
======================
Batch upload skills to ClawHub using the clawhub CLI.

Usage:
    python clawhub_batch_uploader.py                    # Upload all remaining (up to daily limit)
    python clawhub_batch_uploader.py --limit 50         # Upload only 50
    python clawhub_batch_uploader.py --dry-run          # Dry run (no actual upload)
    python clawhub_batch_uploader.py --resume            # Resume from last checkpoint
"""
import json
import subprocess
import sys
import time
import re
from pathlib import Path
from datetime import datetime

REGISTRY_DIR = Path(r"D:\skills\skill-registry")
BATCHES_FILE = REGISTRY_DIR / "clawhub_upload_batches.json"
RESULTS_FILE = REGISTRY_DIR / "clawhub_upload_results.json"
DIR_MAPPING_FILE = REGISTRY_DIR / "round40_clawhub_dir_mapping.json"
REMAINING_FILE = REGISTRY_DIR / "clawhub_remaining.json"
CHECKPOINT_FILE = REGISTRY_DIR / "clawhub_upload_checkpoint.json"
PUBLISHED_SLUGS_FILE = REGISTRY_DIR / "clawhub_published_slugs.json"

REGISTRY = "https://clawhub.ai"
DAILY_LIMIT = 200
DELAY_BETWEEN_UPLOADS = 2  # seconds
CHANGELOG = "L7b quality fix - VAGUE_TASK cleared, input/output sections added"

# Alternative directory locations to check
ALT_DIRS = [
    Path(r"D:\skills\packaged-skills\skillhub"),
    Path(r"D:\skills\opensource-skills\packaged"),
    Path(r"D:\skills\differentiated-skills"),
]


def load_json(path):
    if not path.exists():
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def find_skill_dir(slug, dir_mapping):
    """Find skill directory using mapping or fallback search"""
    # Check dir mapping first
    d = dir_mapping.get(slug)
    if d and Path(d).exists() and (Path(d) / "SKILL.md").exists():
        return Path(d)

    # Fallback: search in alternative directories
    for base in ALT_DIRS:
        if not base.exists():
            continue
        # Direct match
        p = base / slug
        if p.exists() and (p / "SKILL.md").exists():
            return p
        # Search in subdirectories (for differentiated-skills which has category folders)
        if base.name == "differentiated-skills":
            for cat_dir in base.iterdir():
                if not cat_dir.is_dir():
                    continue
                p = cat_dir / slug
                if p.exists() and (p / "SKILL.md").exists():
                    return p

    return None


def upload_skill(skill_dir, slug, dry_run=False):
    """Upload a single skill to ClawHub via CLI"""
    if dry_run:
        return {'success': True, 'slug': slug, 'message': 'DRY RUN', 'dry_run': True}

    # Use shell=True on Windows so npx is found in PATH
    cmd_str = f'npx clawhub --registry "{REGISTRY}" publish "{skill_dir}" --changelog "{CHANGELOG}"'

    try:
        result = subprocess.run(
            cmd_str,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=r"D:\skills",
            shell=True
        )
        output = result.stdout + result.stderr

        if result.returncode == 0:
            # Extract version from output like "OK. Published slug@1.0.1 (xxx)"
            version_match = re.search(r'Published\s+\S+@(\S+)', output)
            version = version_match.group(1) if version_match else 'unknown'
            return {
                'success': True,
                'slug': slug,
                'version': version,
                'message': output.strip()
            }
        elif 'Rate limit' in output or 'rate limit' in output:
            return {
                'success': False,
                'slug': slug,
                'error': 'RATE_LIMITED',
                'message': output.strip()[:200]
            }
        elif 'Version' in output and 'already exists' in output:
            # Version conflict - try incrementing
            return {
                'success': False,
                'slug': slug,
                'error': 'VERSION_EXISTS',
                'message': output.strip()[:200]
            }
        elif 'Path must be a folder' in output:
            return {
                'success': False,
                'slug': slug,
                'error': 'PATH_ERROR',
                'message': output.strip()[:200]
            }
        else:
            return {
                'success': False,
                'slug': slug,
                'error': 'UNKNOWN',
                'message': output.strip()[:300]
            }
    except subprocess.TimeoutExpired:
        return {'success': False, 'slug': slug, 'error': 'TIMEOUT', 'message': '120s timeout'}
    except Exception as e:
        return {'success': False, 'slug': slug, 'error': str(e), 'message': str(e)[:200]}


def increment_version(skill_dir):
    """Increment version in SKILL.md"""
    skill_md = skill_dir / "SKILL.md"
    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]

    # Find version field
    version_pattern = r'^(version:\s*)(\d+)\.(\d+)\.(\d+)\s*$'
    match = re.search(version_pattern, content, re.MULTILINE)
    if match:
        prefix, major, minor, patch = match.groups()
        new_version = f"{major}.{minor}.{int(patch) + 1}"
        new_content = re.sub(version_pattern, f'{prefix}{new_version}', content, count=1, flags=re.MULTILINE)
        skill_md.write_text(new_content, encoding='utf-8')
        return new_version
    return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description='ClawHub Batch Uploader')
    parser.add_argument('--limit', type=int, default=DAILY_LIMIT, help='Max skills to upload')
    parser.add_argument('--dry-run', action='store_true', help='Dry run mode')
    parser.add_argument('--resume', action='store_true', help='Resume from checkpoint')
    args = parser.parse_args()

    # Load data
    dir_mapping = load_json(DIR_MAPPING_FILE)
    dir_mapping = dir_mapping['found_mapping'] if dir_mapping else {}

    remaining_data = load_json(REMAINING_FILE)
    if not remaining_data:
        print("ERROR: No remaining data found. Run calc_clawhub_remaining.py first.")
        sys.exit(1)

    all_slugs = remaining_data['slugs']
    print(f"Total remaining to upload: {len(all_slugs)}")
    print(f"Daily limit: {args.limit}")
    print(f"Dry run: {args.dry_run}")
    print()

    # Load checkpoint for resume
    uploaded_today = set()
    if args.resume and CHECKPOINT_FILE.exists():
        checkpoint = load_json(CHECKPOINT_FILE)
        uploaded_today = set(checkpoint.get('uploaded_today', []))
        print(f"Resuming: {len(uploaded_today)} already uploaded today")

    # Also load previous results to skip already uploaded
    prev_results = load_json(RESULTS_FILE)
    if prev_results:
        prev_success = set(prev_results.get('success', []))
    else:
        prev_success = set()

    # Load published slugs
    published = set(load_json(PUBLISHED_SLUGS_FILE) or [])

    # Filter out already uploaded
    to_upload = []
    for slug in all_slugs:
        if slug in uploaded_today:
            continue
        if slug in prev_success:
            continue
        if slug in published:
            continue
        to_upload.append(slug)

    # Apply limit
    to_upload = to_upload[:args.limit - len(uploaded_today)]
    print(f"Skills to upload this run: {len(to_upload)}")
    print(f"{'='*60}")

    # Upload loop
    success_count = 0
    fail_count = 0
    skip_count = 0
    rate_limited = False
    results = {'success': [], 'failed': [], 'skipped': []}

    for i, slug in enumerate(to_upload, 1):
        if rate_limited:
            print(f"\nRate limited! Stopping upload.")
            break

        # Find skill directory
        skill_dir = find_skill_dir(slug, dir_mapping)
        if not skill_dir:
            print(f"  [{i}/{len(to_upload)}] {slug} - SKIP (directory not found)")
            skip_count += 1
            results['skipped'].append(slug)
            continue

        # Upload
        print(f"  [{i}/{len(to_upload)}] {slug}...", end="", flush=True)
        result = upload_skill(skill_dir, slug, args.dry_run)

        if result['success']:
            print(f" OK ({result.get('version', '')})")
            success_count += 1
            results['success'].append(slug)
            uploaded_today.add(slug)
        elif result.get('error') == 'VERSION_EXISTS':
            # Try incrementing version and retry
            print(f" VERSION_EXISTS, incrementing...", end="", flush=True)
            new_ver = increment_version(skill_dir)
            if new_ver:
                result2 = upload_skill(skill_dir, slug, args.dry_run)
                if result2['success']:
                    print(f" OK (v{new_ver})")
                    success_count += 1
                    results['success'].append(slug)
                    uploaded_today.add(slug)
                else:
                    print(f" FAIL: {result2.get('error', '')}")
                    fail_count += 1
                    results['failed'].append({'slug': slug, 'error': result2.get('error', '')})
            else:
                print(f" FAIL (no version field)")
                fail_count += 1
                results['failed'].append({'slug': slug, 'error': 'NO_VERSION_FIELD'})
        elif result.get('error') == 'RATE_LIMITED':
            print(f" RATE LIMITED")
            fail_count += 1
            results['failed'].append({'slug': slug, 'error': 'RATE_LIMITED'})
            rate_limited = True
        else:
            print(f" FAIL: {result.get('error', '')}")
            fail_count += 1
            results['failed'].append({'slug': slug, 'error': result.get('error', '')})

        # Save checkpoint every 10 uploads
        if i % 10 == 0:
            save_json(CHECKPOINT_FILE, {
                'timestamp': datetime.now().isoformat(),
                'uploaded_today': list(uploaded_today),
                'total_success': success_count,
                'total_failed': fail_count
            })
            print(f"  [Checkpoint: {success_count} success, {fail_count} fail]")

        # Delay between uploads
        if not args.dry_run and i < len(to_upload) and not rate_limited:
            time.sleep(DELAY_BETWEEN_UPLOADS)

    # Save final results
    save_json(CHECKPOINT_FILE, {
        'timestamp': datetime.now().isoformat(),
        'uploaded_today': list(uploaded_today),
        'total_success': success_count,
        'total_failed': fail_count
    })

    # Merge with previous results
    if prev_results:
        prev_results['success'].extend(results['success'])
        prev_results['failed'].extend(results['failed'])
        save_json(RESULTS_FILE, prev_results)
    else:
        results['date'] = datetime.now().isoformat()
        save_json(RESULTS_FILE, results)

    # Update published slugs
    if results['success']:
        published_list = load_json(PUBLISHED_SLUGS_FILE) or []
        published_list.extend(results['success'])
        save_json(PUBLISHED_SLUGS_FILE, list(set(published_list)))

    print(f"\n{'='*60}")
    print(f"Upload Summary:")
    print(f"  Success: {success_count}")
    print(f"  Failed:  {fail_count}")
    print(f"  Skipped: {skip_count}")
    print(f"  Rate limited: {rate_limited}")
    print(f"  Total uploaded today: {len(uploaded_today)}")
    remaining_after = len(all_slugs) - len(uploaded_today) - len(prev_success)
    print(f"  Remaining after this run: {remaining_after}")
    print(f"{'='*60}")

    if rate_limited:
        print(f"\nRate limit reached. Try again after 24 hours.")
        print(f"Run: python clawhub_batch_uploader.py --resume")


if __name__ == '__main__':
    main()
