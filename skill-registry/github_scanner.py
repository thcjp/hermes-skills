#!/usr/bin/env python3
"""
GitHub Skill 来源扫描器
=======================
从GitHub高星仓库拉取skill目录，去重后输出候选列表

优化点:
- 使用GitHub API（api.github.com）获取目录结构
- 支持超时和重试
- 增量扫描（跳过已入库的）
- 输出结构化候选列表
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
from platform_config import GITHUB_REPOS
# === End Phase 1 ===

import json
import sqlite3
import urllib.request
import urllib.error
import os
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Set

# 导入统一解析层
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from skill_core.parser import parse_frontmatter as _parse_fm

# DB_PATH imported from config
from project_config import TOOLS_DIR as _TOOLS_DIR
CANDIDATES_FILE = _TOOLS_DIR / "discovery" / "github-candidates.json"

# GitHub 来源仓库配置 - GITHUB_REPOS imported from config

def fetch_json(url: str, timeout: int = 15) -> Optional[Any]:
    """获取JSON响应"""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'skill-discovery/1.0',
            'Accept': 'application/vnd.github.v3+json'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print(f"    GitHub API限流，等待30秒...")
            time.sleep(30)
            return None
        return None
    except Exception:
        return None

def fetch_text(url: str, timeout: int = 15) -> Optional[str]:
    """获取文本响应"""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'skill-discovery/1.0',
            'Accept': 'text/plain'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception:
        return None

def get_repo_contents(owner: str, repo: str, path: str = "") -> List[Dict]:
    """获取GitHub仓库目录内容"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    data = fetch_json(url)
    if isinstance(data, list):
        return data
    return []

def find_skill_dirs(owner: str, repo: str) -> List[str]:
    """查找仓库中的skill目录"""
    # 先尝试根目录
    root_contents = get_repo_contents(owner, repo)
    skill_dirs = []

    for item in root_contents:
        if item.get('type') == 'dir':
            name = item['name'].lower()
            # 匹配可能的skill目录名
            if name in ('skills', 'skill', 'plugins', 'plugin'):
                skill_dirs.append(item['name'])
            # 也可能是直接以skill命名的目录
            elif 'skill' in name or 'plugin' in name:
                skill_dirs.append(item['name'])

    # 如果根目录没有skills目录，检查每个子目录是否包含SKILL.md
    if not skill_dirs:
        for item in root_contents:
            if item.get('type') == 'dir':
                sub_contents = get_repo_contents(owner, repo, item['name'])
                for sub in sub_contents:
                    if sub.get('name') == 'SKILL.md':
                        # 这个目录本身就是一个skill
                        skill_dirs.append('')
                        break

    return skill_dirs if skill_dirs else ['']  # 默认根目录

def scan_repo(repo_config: Dict) -> List[Dict[str, Any]]:
    """扫描单个GitHub仓库"""
    owner = repo_config['owner']
    repo = repo_config['repo']
    print(f"  扫描: {owner}/{repo} ({repo_config.get('star', '?')}★)")

    # 获取skill目录列表
    skill_dirs = find_skill_dirs(owner, repo)
    if not skill_dirs:
        print(f"    未找到skill目录")
        return []

    all_skills = []

    for skill_dir in skill_dirs:
        if skill_dir:
            print(f"    目录: {skill_dir}/")
            contents = get_repo_contents(owner, repo, skill_dir)
        else:
            # 根目录直接是skill
            contents = get_repo_contents(owner, repo)

        for item in contents:
            if item.get('type') != 'dir':
                continue

            skill_name = item['name']
            # 跳过非skill目录
            if skill_name.startswith('.') or skill_name in ('node_modules', 'scripts', 'docs', 'test', 'tests'):
                continue

            # 获取SKILL.md
            if skill_dir:
                skill_md_path = f"{skill_dir}/{skill_name}/SKILL.md"
            else:
                skill_md_path = f"{skill_name}/SKILL.md"

            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{skill_md_path}"
            skill_content = fetch_text(raw_url)

            if not skill_content or len(skill_content) < 50:
                # 尝试master分支
                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{skill_md_path}"
                skill_content = fetch_text(raw_url)

            if not skill_content or len(skill_content) < 50:
                continue

            # 解析frontmatter
            metadata = parse_frontmatter(skill_content)

            skill_info = {
                'source_slug': skill_name,
                'source_platform': 'github',
                'source_url': f"https://github.com/{owner}/{repo}/tree/main/{skill_md_path.rsplit('/', 1)[0]}",
                'source_repo': f"{owner}/{repo}",
                'source_license': repo_config.get('license', 'unknown'),
                'source_repo_star': repo_config.get('star', 'unknown'),
                'display_name': metadata.get('displayName', metadata.get('name', skill_name)),
                'summary': metadata.get('summary', metadata.get('description', ''))[:200],
                'category': 'Development',
                'content_preview': skill_content[:500],
                'content_length': len(skill_content),
            }
            all_skills.append(skill_info)
            print(f"      ✓ {skill_name}")

    print(f"    发现 {len(all_skills)} 个skill")
    return all_skills

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """解析YAML frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    return result.get('fields', {})

def get_existing_source_slugs() -> Set[str]:
    """获取本地DB中已有的source_slug"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT source_slug FROM skills
        WHERE source_slug IS NOT NULL AND source_slug != ''
    """)
    slugs = {row[0] for row in c.fetchall()}
    conn.close()
    return slugs

def deduplicate(discovered: List[Dict]) -> Dict[str, Any]:
    """去重比对"""
    existing = get_existing_source_slugs()

    result = {
        'scan_time': datetime.now().isoformat(),
        'total_discovered': len(discovered),
        'new_skills': [],
        'duplicates': [],
    }

    for skill in discovered:
        source_slug = skill.get('source_slug', '')
        if source_slug in existing:
            result['duplicates'].append(skill)
        else:
            result['new_skills'].append(skill)

    return result

def main():
    print("=" * 60)
    print("GitHub Skill 来源扫描器")
    print("=" * 60)

    all_discovered = []

    for repo_config in GITHUB_REPOS:
        skills = scan_repo(repo_config)
        all_discovered.extend(skills)
        # 避免GitHub API限流
        time.sleep(2)

    print(f"\n总计发现 {len(all_discovered)} 个GitHub skill")

    # 去重
    print("\n执行去重比对...")
    result = deduplicate(all_discovered)

    print(f"\n去重结果:")
    print(f"  新skill: {len(result['new_skills'])}")
    print(f"  已存在: {len(result['duplicates'])}")

    # 保存候选列表
    CANDIDATES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CANDIDATES_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n候选列表已保存: {CANDIDATES_FILE}")

    # 显示新skill
    if result['new_skills']:
        print(f"\n新skill列表:")
        for i, skill in enumerate(result['new_skills'], 1):
            print(f"  {i}. [{skill['source_repo']}] {skill['source_slug']}")
            if skill.get('display_name'):
                print(f"     名称: {skill['display_name']}")
            if skill.get('summary'):
                print(f"     摘要: {skill['summary'][:60]}")

if __name__ == '__main__':
    main()
