#!/usr/bin/env python3
"""Round 34: Hermes Skills Hub format converter and evaluator

Converts our SKILL.md format to agentskills.io standard:
  slug → name (must match directory name)
  displayName → metadata.displayName
  version → metadata.version
  summary → metadata.summary (or merge into description)
  license → license (direct)
  description → description (direct, max 1024 chars)
  tools → allowed-tools (space-separated)
  tags → metadata.tags

Also evaluates all free skills for Hermes publication eligibility.
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR, DATA_DIR
# === End Phase 1 ===


import json
import re
from pathlib import Path
from datetime import datetime

DB_FILE = DATA_DIR / "upload_tracking.json"
PACKAGED_DIR = Path(r"D:\skills\packaged-skills\skillhub")
# DIFFERENTIATED_DIR imported from config
NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def parse_frontmatter(content):
    """Parse YAML frontmatter from SKILL.md"""
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
            if val:
                fm[key] = val
            else:
                current_key = key
                fm[key] = []
    return fm, body

def convert_to_hermes_format(fm, body):
    """Convert our frontmatter to agentskills.io standard"""
    hermes_fm = {}
    metadata = {}
    
    # Required fields
    hermes_fm['name'] = fm.get('slug', '')
    desc = fm.get('description', '') or fm.get('summary', '')
    if len(desc) > 1024:
        desc = desc[:1021] + '...'
    hermes_fm['description'] = desc
    
    # Optional direct fields
    if fm.get('license'):
        hermes_fm['license'] = fm['license']
    
    # Tools → allowed-tools (convert from list to space-separated)
    tools = fm.get('tools', [])
    if isinstance(tools, list) and tools:
        hermes_fm['allowed-tools'] = ' '.join(tools)
    elif isinstance(tools, str) and tools:
        hermes_fm['allowed-tools'] = tools
    
    # Extra fields → metadata
    if fm.get('displayName'):
        metadata['displayName'] = fm['displayName']
    if fm.get('version'):
        metadata['version'] = fm['version']
    if fm.get('summary'):
        metadata['summary'] = fm['summary']
    
    tags = fm.get('tags', [])
    if isinstance(tags, list) and tags:
        metadata['tags'] = tags
    elif isinstance(tags, str) and tags:
        metadata['tags'] = [tags]
    
    if metadata:
        hermes_fm['metadata'] = metadata
    
    # compatibility field
    hermes_fm['compatibility'] = 'Requires LLM with tool-use capability'
    
    return hermes_fm

def build_hermes_yaml(fm_dict):
    """Build YAML frontmatter string from dict"""
    lines = ['---']
    
    # Required fields first
    if 'name' in fm_dict:
        lines.append(f'name: {fm_dict["name"]}')
    if 'description' in fm_dict:
        desc = fm_dict['description'].replace('"', '\\"')
        lines.append(f'description: "{desc}"')
    if 'license' in fm_dict:
        lines.append(f'license: {fm_dict["license"]}')
    if 'allowed-tools' in fm_dict:
        lines.append(f'allowed-tools: {fm_dict["allowed-tools"]}')
    if 'compatibility' in fm_dict:
        lines.append(f'compatibility: "{fm_dict["compatibility"]}"')
    
    # Metadata as nested mapping
    if 'metadata' in fm_dict:
        lines.append('metadata:')
        for k, v in fm_dict['metadata'].items():
            if isinstance(v, list):
                lines.append(f'  {k}:')
                for item in v:
                    lines.append(f'    - {item}')
            else:
                v_str = str(v).replace('"', '\\"')
                lines.append(f'  {k}: "{v_str}"')
    
    lines.append('---')
    return '\n'.join(lines)

def evaluate_hermes_eligibility(db):
    """Evaluate all free skills for Hermes publication"""
    skills = db["skills"]
    eligible = 0
    not_eligible = 0
    
    for slug, s in skills.items():
        if s.get("is_source"):
            continue
        
        is_free = s.get("is_free", False)
        
        s.setdefault("hermes", {})
        s["hermes"]["evaluated"] = True
        s["hermes"]["evaluated_at"] = NOW
        
        if is_free:
            s["hermes"]["eligible"] = True
            s["hermes"]["status"] = "eligible"
            s["hermes"]["format"] = "agentskills.io"
            s["hermes"]["conversion"] = "field_mapping_required"
            s["hermes"]["monetization"] = "none"
            s["hermes"]["purpose"] = "exposure"
            eligible += 1
        else:
            s["hermes"]["eligible"] = False
            s["hermes"]["status"] = "not_eligible"
            s["hermes"]["reason"] = "paid_skill_not_for_free_platform"
            not_eligible += 1
    
    return eligible, not_eligible

def main():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
    
    # Evaluate Hermes eligibility
    eligible, not_eligible = evaluate_hermes_eligibility(db)
    
    # Update stats
    db.setdefault("stats", {})
    db["stats"]["hermes_eligible"] = eligible
    db["stats"]["hermes_not_eligible"] = not_eligible
    db["stats"]["hermes_evaluated"] = eligible + not_eligible
    db["metadata"]["last_updated"] = NOW
    
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    
    print(f"Hermes Skills Hub 评估完成:")
    print(f"  可发布(eligible): {eligible} (免费skill)")
    print(f"  不可发布: {not_eligible} (付费skill)")
    print(f"  格式: agentskills.io标准 (SKILL.md + YAML frontmatter)")
    print(f"  兼容性: 基本兼容, 需字段映射 (slug→name, tools→allowed-tools, 其他→metadata)")
    print(f"  变现: 无 (仅曝光/引流)")
    print(f"  审核: 自动安全扫描 (无人工审核)")
    print(f"  发布方式: GitHub仓库 + hermes skills publish CLI")
    print(f"  生态规模: 57K+ Star, 9万+技能")
    print(f"\n字段映射方案:")
    print(f"  slug → name (必须与目录名一致)")
    print(f"  description → description (max 1024 chars)")
    print(f"  license → license (直接兼容)")
    print(f"  tools → allowed-tools (空格分隔)")
    print(f"  displayName → metadata.displayName")
    print(f"  version → metadata.version")
    print(f"  summary → metadata.summary")
    print(f"  tags → metadata.tags")

if __name__ == "__main__":
    main()
