#!/usr/bin/env python3
"""
Skill 自动发现系统
==================
功能: 扫描多平台来源(ClawHub/GitHub/Hermes)，发现本地不存在的新skill，
      去重比对后输出候选列表供AI差异化改造

用法:
  python auto_discover.py scan                    # 扫描所有来源
  python auto_discover.py scan --source clawhub   # 仅扫描clawhub
  python auto_discover.py scan --source github    # 仅扫描github
  python auto_discover.py scan --category Creative # 按类别扫描
  python auto_discover.py dedup                   # 去重比对，输出新skill列表
  python auto_discover.py candidates              # 显示候选新skill
  python auto_discover.py import <slug>           # 导入指定skill到本地
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import PROJECT_ROOT
from project_config import DB_PATH
from project_config import CLAWHUB_DOWNLOADED_DIR
from project_config import DISCOVERY_DIR
from platform_config import GITHUB_SCAN_REPOS
# === End Phase 1 ===
SKILLS_ROOT = PROJECT_ROOT


import argparse
import json
import sqlite3
import urllib.request
import urllib.error
import os
import sys
import subprocess
import re
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Set

# 导入统一解析层
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from skill_core.parser import parse_frontmatter as _parse_fm

# ============================================================
# 配置
# ============================================================

# DB_PATH imported from config
# SKILLS_ROOT = PROJECT_ROOT (imported from config)
# CLAWHUB_DOWNLOADED_DIR imported from config
# DISCOVERY_DIR imported from config
CANDIDATES_FILE = DISCOVERY_DIR / "candidates.json"

# ClawHub API
CLAWHUB_API_BASE = "https://clawhub.ai/api"
CLAWHUB_MIRROR = "https://mirror-cn.clawhub.com/api"

# GitHub 来源仓库
# GITHUB_REPOS imported from config

# ClawHub 分类映射
CLAWHUB_CATEGORIES = [
    "Integrations", "Creative", "Research", "Development", "Automation",
    "Productivity", "Communication", "Agents", "Knowledge", "Security",
    "Lifestyle", "Operations", "Finance", "Other"
]

# ============================================================
# 数据库操作
# ============================================================

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_existing_source_slugs() -> Set[str]:
    """获取本地DB中所有已有的source_slug"""
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT source_slug FROM skills
        WHERE source_slug IS NOT NULL AND source_slug != ''
    """)
    slugs = {row[0] for row in c.fetchall()}
    conn.close()
    return slugs

def get_existing_display_names() -> Set[str]:
    """获取本地DB中所有已有的display_name"""
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT current_display_name FROM skills
        WHERE current_display_name IS NOT NULL AND current_display_name != ''
    """)
    names = {row[0].lower() for row in c.fetchall()}
    conn.close()
    return names

def get_existing_slugs() -> Set[str]:
    """获取本地DB中所有已有的slug"""
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT DISTINCT slug FROM skills")
    slugs = {row[0] for row in c.fetchall()}
    conn.close()
    return slugs

# ============================================================
# ClawHub 扫描器
# ============================================================

def fetch_url(url: str, timeout: int = 15) -> Optional[str]:
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception:
        return None

def scan_clawhub_category(category: str, limit: int = 50) -> List[Dict[str, Any]]:
    """扫描clawhub指定类别的新skill"""
    skills = []

    # 尝试API端点
    api_urls = [
        f"{CLAWHUB_API_BASE}/skills?category={category}&sort=newest&limit={limit}",
        f"{CLAWHUB_MIRROR}/skills?category={category}&sort=newest&limit={limit}",
        f"{CLAWHUB_API_BASE}/v1/skills?category={category}&page=1&pageSize={limit}",
    ]

    for url in api_urls:
        content = fetch_url(url)
        if not content:
            continue
        try:
            data = json.loads(content)
            if isinstance(data, dict) and 'skills' in data:
                skills = data['skills']
            elif isinstance(data, list):
                skills = data
            if skills:
                break
        except json.JSONDecodeError:
            continue

    return skills

def scan_clawhub_all(limit_per_category: int = 20) -> List[Dict[str, Any]]:
    """扫描clawhub所有类别"""
    all_skills = []
    for category in CLAWHUB_CATEGORIES:
        print(f"  扫描类别: {category}...")
        skills = scan_clawhub_category(category, limit_per_category)
        for s in skills:
            s['_source_platform'] = 'clawhub'
            s['_category'] = category
        all_skills.extend(skills)
        print(f"    获取 {len(skills)} 个skill")
    return all_skills

def scan_clawhub_local() -> List[Dict[str, Any]]:
    """扫描本地已下载但未入库的clawhub skill"""
    skills = []
    if not CLAWHUB_DOWNLOADED_DIR.exists():
        return skills

    # 获取已入库的source_slug
    existing = get_existing_source_slugs()

    for category_dir in CLAWHUB_DOWNLOADED_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        for skill_dir in category_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue

            slug = skill_dir.name
            if slug in existing:
                continue  # 已入库

            # 解析SKILL.md获取基本信息
            try:
                content = skill_md.read_text(encoding='utf-8')
                metadata = parse_frontmatter(content)
                skills.append({
                    'source_slug': slug,
                    'source_platform': 'clawhub',
                    'source_url': f"https://clawhub.ai/skills/{slug}",
                    'display_name': metadata.get('displayName', slug),
                    'summary': metadata.get('summary', ''),
                    'category': category_dir.name,
                    'local_path': str(skill_dir),
                    'content': content[:500],
                })
            except Exception:
                continue

    return skills

# ============================================================
# GitHub 扫描器
# ============================================================

def scan_github_repo(owner: str, repo: str) -> List[Dict[str, Any]]:
    """扫描GitHub仓库中的skill"""
    skills = []

    # 尝试通过GitHub API获取目录结构
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
    content = fetch_url(api_url)
    if not content:
        return skills

    try:
        items = json.loads(content)
    except json.JSONDecodeError:
        return skills

    # 查找skill目录
    for item in items:
        if item.get('type') == 'dir':
            skill_md_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{item['name']}/SKILL.md"
            skill_content = fetch_url(skill_md_url)
            if not skill_content:
                skill_md_url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{item['name']}/SKILL.md"
                skill_content = fetch_url(skill_md_url)

            if skill_content and len(skill_content) > 50:
                metadata = parse_frontmatter(skill_content)
                skills.append({
                    'source_slug': item['name'],
                    'source_platform': 'github',
                    'source_url': f"https://github.com/{owner}/{repo}/tree/main/{item['name']}",
                    'source_repo': f"{owner}/{repo}",
                    'display_name': metadata.get('displayName', item['name']),
                    'summary': metadata.get('summary', ''),
                    'category': 'Development',
                    'content': skill_content[:500],
                })

    return skills

def scan_github_all() -> List[Dict[str, Any]]:
    """扫描所有配置的GitHub仓库"""
    all_skills = []
    for repo_config in GITHUB_SCAN_REPOS:
        print(f"  扫描仓库: {repo_config['owner']}/{repo_config['repo']}...")
        skills = scan_github_repo(repo_config['owner'], repo_config['repo'])
        for s in skills:
            s['_source_platform'] = 'github'
            s['_license'] = repo_config['license']
        all_skills.extend(skills)
        print(f"    获取 {len(skills)} 个skill")
    return all_skills

# ============================================================
# 去重比对
# ============================================================

def deduplicate(discovered_skills: List[Dict[str, Any]]) -> Dict[str, Any]:
    """去重比对，分离新skill和已存在skill"""
    existing_slugs = get_existing_slugs()
    existing_source_slugs = get_existing_source_slugs()
    existing_names = get_existing_display_names()

    result = {
        'dedup_time': datetime.now().isoformat(),
        'total_discovered': len(discovered_skills),
        'new_skills': [],
        'duplicate_by_source_slug': [],
        'duplicate_by_display_name': [],
        'duplicate_by_slug': [],
    }

    for skill in discovered_skills:
        source_slug = skill.get('source_slug', '')
        display_name = skill.get('display_name', '').lower()
        slug = skill.get('slug', source_slug)

        # 检查source_slug是否已存在
        if source_slug and source_slug in existing_source_slugs:
            result['duplicate_by_source_slug'].append(skill)
            continue

        # 检查display_name是否已存在
        if display_name and display_name in existing_names:
            result['duplicate_by_display_name'].append(skill)
            continue

        # 检查slug是否已存在
        if slug in existing_slugs:
            result['duplicate_by_slug'].append(skill)
            continue

        result['new_skills'].append(skill)

    return result

# ============================================================
# 工具函数
# ============================================================

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """解析YAML frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    return result.get('fields', {})

def ensure_dir():
    """确保发现目录存在"""
    DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# 命令处理
# ============================================================

def cmd_scan(args):
    """扫描来源平台"""
    print("=" * 60)
    print("Skill 自动发现系统 - 来源扫描")
    print("=" * 60)

    all_discovered = []

    if args.source in ('clawhub', 'all'):
        print("\n1. 扫描ClawHub本地已下载...")
        local_skills = scan_clawhub_local()
        print(f"   发现 {len(local_skills)} 个本地未入库skill")
        all_discovered.extend(local_skills)

        if args.source == 'clawhub' and args.remote:
            print("\n2. 扫描ClawHub远程API...")
            remote_skills = scan_clawhub_all(limit_per_category=args.limit)
            print(f"   发现 {len(remote_skills)} 个远程skill")
            all_discovered.extend(remote_skills)

    if args.source in ('github', 'all'):
        print("\n3. 扫描GitHub仓库...")
        github_skills = scan_github_all()
        print(f"   发现 {len(github_skills)} 个GitHub skill")
        all_discovered.extend(github_skills)

    print(f"\n总计发现 {len(all_discovered)} 个候选skill")

    # 去重比对
    print("\n执行去重比对...")
    dedup_result = deduplicate(all_discovered)

    print(f"\n去重结果:")
    print(f"  新skill: {len(dedup_result['new_skills'])}")
    print(f"  source_slug重复: {len(dedup_result['duplicate_by_source_slug'])}")
    print(f"  display_name重复: {len(dedup_result['duplicate_by_display_name'])}")
    print(f"  slug重复: {len(dedup_result['duplicate_by_slug'])}")

    # 保存候选列表
    ensure_dir()
    with open(CANDIDATES_FILE, 'w', encoding='utf-8') as f:
        json.dump(dedup_result, f, ensure_ascii=False, indent=2)
    print(f"\n候选列表已保存: {CANDIDATES_FILE}")

    return dedup_result

def cmd_dedup(args):
    """仅执行去重比对（使用上次扫描结果）"""
    if not CANDIDATES_FILE.exists():
        print("未找到扫描结果，请先执行 scan 命令")
        return

    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 重新去重
    result = deduplicate(data.get('new_skills', []))
    with open(CANDIDATES_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"去重完成: {len(result['new_skills'])} 个新skill")

def cmd_candidates(args):
    """显示候选新skill"""
    if not CANDIDATES_FILE.exists():
        print("未找到候选列表，请先执行 scan 命令")
        return

    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_skills = data.get('new_skills', [])
    print(f"\n候选新skill ({len(new_skills)} 个):")
    print("-" * 80)

    for i, skill in enumerate(new_skills[:50], 1):
        print(f"{i:3d}. [{skill.get('source_platform', '?')}] "
              f"{skill.get('source_slug', '?'):30s} "
              f"| {skill.get('display_name', '?')[:30]}")
        if skill.get('summary'):
            print(f"     {skill['summary'][:70]}")

    if len(new_skills) > 50:
        print(f"\n... 还有 {len(new_skills) - 50} 个，查看完整列表: {CANDIDATES_FILE}")

def cmd_import(args):
    """导入指定skill到本地DB

    v1.1修复: 实际调用register_skill()写入DB, 不再仅print指导信息
    """
    if not CANDIDATES_FILE.exists():
        print("未找到候选列表，请先执行 scan 命令")
        return

    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 查找指定skill
    target = None
    for skill in data.get('new_skills', []):
        if skill.get('source_slug') == args.slug:
            target = skill
            break

    if not target:
        print(f"未在候选列表中找到: {args.slug}")
        return

    # 生成符合命名规范的双版本信息
    base_slug = args.slug
    paid_slug = base_slug
    free_slug = f"{base_slug}-free"

    # 从候选数据提取信息
    display_name = target.get('display_name', base_slug)
    source_platform = target.get('source_platform', 'unknown')
    source_url = target.get('source_url', '')
    source_author = target.get('source_author', '')
    source_license = target.get('source_license', '')
    skill_type = target.get('skill_type', 'general')
    category = target.get('category', 'Productivity')

    # 导入付费版到DB
    from db import register_skill
    paid_skill_id = register_skill(
        slug=paid_slug,
        name=paid_slug,
        display_name=display_name,
        version='1.0.0',
        category=category,
        source=source_platform,
        local_path='',  # 差异化改造后填入实际路径
        source_slug=args.slug,
        source_url=source_url,
        source_author=source_author,
        source_license=source_license,
        skill_type=skill_type,
        pricing_model='per_call',
        is_differentiated=0,
        edition='paid',
        parent_slug=None,
        workflow_state='step1_read_original',
        notes=f"Imported from discovery. Source: {source_platform}"
    )

    # 导入免费版到DB
    free_display_name = f"{display_name}免费版"
    free_skill_id = register_skill(
        slug=free_slug,
        name=free_slug,
        display_name=free_display_name,
        version='1.0.0',
        category=category,
        source=source_platform,
        local_path='',
        source_slug=args.slug,
        source_url=source_url,
        source_author=source_author,
        source_license=source_license,
        skill_type=skill_type,
        pricing_model='free',
        is_differentiated=0,
        edition='free',
        parent_slug=paid_slug,
        workflow_state='step1_read_original',
        notes=f"Imported from discovery. Source: {source_platform}"
    )

    print(f"✓ 导入成功: {args.slug}")
    print(f"  付费版: slug={paid_slug}, skill_id={paid_skill_id}, workflow_state=step1_read_original")
    print(f"  免费版: slug={free_slug}, skill_id={free_skill_id}, workflow_state=step1_read_original")
    print(f"  来源: {source_platform}")
    print(f"  displayName: {display_name}")
    print(f"\n注意: 下一步需要AI执行差异化改造，请参考NAMING_CONVENTION.md")
    print(f"差异化改造完成后，使用以下命令上传:")
    print(f"  python update_mechanism.py generate {paid_slug}")
    print(f"  python update_mechanism.py upload {paid_slug}")

def main():
    parser = argparse.ArgumentParser(
        description='Skill 自动发现系统 - 扫描多平台来源，发现新skill',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command')

    # scan
    p_scan = subparsers.add_parser('scan', help='扫描来源平台')
    p_scan.add_argument('--source', choices=['clawhub', 'github', 'all'],
                       default='all', help='来源平台')
    p_scan.add_argument('--remote', action='store_true', help='扫描clawhub远程API')
    p_scan.add_argument('--limit', type=int, default=20, help='每类别扫描数量')
    p_scan.add_argument('--category', help='指定类别')

    # dedup
    subparsers.add_parser('dedup', help='去重比对')

    # candidates
    subparsers.add_parser('candidates', help='显示候选新skill')

    # import
    p_import = subparsers.add_parser('import', help='导入指定skill')
    p_import.add_argument('slug', help='skill slug')

    args = parser.parse_args()

    if args.command == 'scan':
        cmd_scan(args)
    elif args.command == 'dedup':
        cmd_dedup(args)
    elif args.command == 'candidates':
        cmd_candidates(args)
    elif args.command == 'import':
        cmd_import(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
