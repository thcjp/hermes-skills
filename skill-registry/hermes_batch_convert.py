#!/usr/bin/env python3
"""Round 35: Hermes format converter - batch convert 759 free skills to agentskills.io standard

Conversion rules:
  slug → name (must match directory name)
  description → description (max 1024 chars)
  license → license (direct)
  tools → allowed-tools (space-separated string)
  displayName → metadata.displayName
  version → metadata.version
  summary → metadata.summary
  tags → metadata.tags (list)

Output: D:\skills\hermes-skills\ (converted copies ready for GitHub publishing)
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===


import json
import re
import shutil
from pathlib import Path
from datetime import datetime

DB_FILE = Path(r"D:\skills\skill-registry\upload_tracking.json")
PACKAGED_DIR = Path(r"D:\skills\packaged-skills\skillhub")
# DIFFERENTIATED_DIR imported from config
OUTPUT_DIR = Path(r"D:\skills\hermes-skills")
NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def parse_frontmatter_full(content):
    """Parse YAML frontmatter preserving all fields"""
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith('---'):
        return {}, content
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}, content
    fm_text = parts[1].strip()
    body = parts[2]
    
    fm = {}
    current_key = None
    
    for line in fm_text.split('\n'):
        line_stripped = line.rstrip()
        if not line_stripped:
            continue
        if line.startswith('  - '):
            val = line[4:].strip().strip('"')
            if current_key:
                if current_key not in fm:
                    fm[current_key] = []
                if isinstance(fm[current_key], list):
                    fm[current_key].append(val)
        elif ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip().strip('"')
            if val and val not in ('|-', '|', '>-', '>'):
                fm[key] = val
            elif val in ('|-', '|', '>-', '>'):
                current_key = key
                fm[key] = ''
            else:
                current_key = key
                fm[key] = []
    return fm, body

def build_hermes_frontmatter(fm):
    """Build agentskills.io compatible YAML frontmatter"""
    lines = ['---']
    
    # Required: name (from slug, must match directory name)
    name = fm.get('slug', '')
    lines.append(f'name: "{name}"')
    
    # Required: description (max 1024 chars)
    desc = fm.get('description', '') or fm.get('summary', '')
    if not desc:
        desc = fm.get('displayName', '') + ' - AI skill'
    if len(desc) > 1024:
        desc = desc[:1021] + '...'
    # Escape quotes in description
    desc = desc.replace('"', '\\"').replace('\n', ' ')
    lines.append(f'description: "{desc}"')
    
    # Optional: license
    if fm.get('license'):
        lines.append(f'license: {fm["license"]}')
    
    # Optional: allowed-tools (from tools, space-separated)
    tools = fm.get('tools', [])
    if isinstance(tools, list) and tools:
        # Flatten nested lists (some entries are like ['- read', 'exec'])
        flat_tools = []
        for t in tools:
            if isinstance(t, list):
                flat_tools.extend(t)
            else:
                flat_tools.append(t)
        # Clean and deduplicate
        clean_tools = []
        seen = set()
        for t in flat_tools:
            t = t.strip().lstrip('-').strip()
            if t and t not in seen:
                clean_tools.append(t)
                seen.add(t)
        if clean_tools:
            lines.append(f'allowed-tools: {" ".join(clean_tools)}')
    
    # Optional: compatibility
    lines.append('compatibility: "Requires LLM with tool-use capability"')
    
    # Metadata block for extra fields
    metadata_entries = []
    if fm.get('displayName'):
        metadata_entries.append(('displayName', fm['displayName']))
    if fm.get('version'):
        metadata_entries.append(('version', fm['version']))
    if fm.get('summary'):
        summary = fm['summary'].replace('"', '\\"')
        metadata_entries.append(('summary', summary))
    
    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    if tags:
        metadata_entries.append(('tags', tags))
    
    # Add source metadata
    metadata_entries.append(('source', 'SkillHub'))
    metadata_entries.append(('converted_at', NOW))
    
    if metadata_entries:
        lines.append('metadata:')
        for key, val in metadata_entries:
            if isinstance(val, list):
                lines.append(f'  {key}:')
                for item in val:
                    lines.append(f'    - "{item}"')
            else:
                val_str = str(val).replace('"', '\\"')
                lines.append(f'  {key}: "{val_str}"')
    
    lines.append('---')
    return '\n'.join(lines)

def convert_skill(skill_path, output_path):
    """Convert a single SKILL.md to agentskills.io format"""
    content = skill_path.read_text(encoding='utf-8', errors='replace')
    fm, body = parse_frontmatter_full(content)
    
    # Build new frontmatter
    new_fm = build_hermes_frontmatter(fm)
    
    # Combine: new frontmatter + original body
    converted = new_fm + '\n' + body
    
    # Write to output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(converted, encoding='utf-8')
    return True

def main():
    # Load database to find free skills
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
    
    # Collect all free skill paths
    free_skills = []
    
    for slug, s in db["skills"].items():
        if s.get("is_source"):
            continue
        if not s.get("is_free"):
            continue
        
        # Find the skill directory
        skill_md = None
        source_type = ""
        
        # Check packaged
        p = PACKAGED_DIR / slug / "SKILL.md"
        if p.exists():
            skill_md = p
            source_type = "packaged"
        else:
            # Check differentiated
            if DIFFERENTIATED_DIR.exists():
                for cat_dir in DIFFERENTIATED_DIR.iterdir():
                    p2 = cat_dir / slug / "SKILL.md"
                    if p2.exists():
                        skill_md = p2
                        source_type = f"differentiated/{cat_dir.name}"
                        break
        
        if skill_md:
            free_skills.append((slug, skill_md, source_type))
    
    print(f"Found {len(free_skills)} free skills to convert")
    
    # Clear output directory if exists
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    
    # Convert all
    converted = 0
    errors = 0
    error_list = []
    
    for slug, skill_path, source_type in free_skills:
        output_path = OUTPUT_DIR / slug / "SKILL.md"
        try:
            convert_skill(skill_path, output_path)
            converted += 1
        except Exception as e:
            errors += 1
            error_list.append(f"{slug}: {e}")
    
    # Copy any bundled resources (scripts/, references/, assets/)
    for slug, skill_path, source_type in free_skills:
        src_dir = skill_path.parent
        dst_dir = OUTPUT_DIR / slug
        for subdir_name in ['scripts', 'references', 'assets']:
            src_subdir = src_dir / subdir_name
            if src_subdir.exists() and src_subdir.is_dir():
                dst_subdir = dst_dir / subdir_name
                shutil.copytree(src_subdir, dst_subdir, dirs_exist_ok=True)
    
    # Save conversion report
    report = {
        "converted_at": NOW,
        "total_free_skills": len(free_skills),
        "converted": converted,
        "errors": errors,
        "error_details": error_list,
        "output_dir": str(OUTPUT_DIR),
        "format": "agentskills.io v1.0",
        "field_mapping": {
            "slug": "name",
            "description": "description (max 1024 chars)",
            "license": "license",
            "tools": "allowed-tools (space-separated)",
            "displayName": "metadata.displayName",
            "version": "metadata.version",
            "summary": "metadata.summary",
            "tags": "metadata.tags",
        },
    }
    
    report_path = Path(r"D:\skills\skill-registry\hermes_conversion_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== Conversion Complete ===")
    print(f"Converted: {converted}/{len(free_skills)}")
    print(f"Errors: {errors}")
    if error_list:
        print(f"Error details:")
        for e in error_list[:10]:
            print(f"  {e}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Report: {report_path}")
    
    # Verify a sample
    if converted > 0:
        sample_slug = free_skills[0][0]
        sample_path = OUTPUT_DIR / sample_slug / "SKILL.md"
        if sample_path.exists():
            print(f"\n=== Sample: {sample_slug} ===")
            lines = sample_path.read_text(encoding='utf-8').split('\n')
            for line in lines[:25]:
                print(f"  {line}")

if __name__ == "__main__":
    main()
