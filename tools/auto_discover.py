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
from project_config import TOOLS_DIR, CLAWHUB_DOWNLOADED_DIR, DISCOVERY_DIR, PLATFORM_CONFIG # V123 W2: 合并重复import
from platform_config import GITHUB_SCAN_REPOS
# === End Phase 1 ===


import argparse
import json
import sys
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Set

# 导入统一解析层
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
from skill_core.parser import parse_frontmatter
from skill_core import db as db_module  # V117 W4: 统一db入口

# ============================================================
# 配置
# ============================================================

# DB_PATH imported from config
# SKILLS_ROOT = PROJECT_ROOT (imported from config)
# CLAWHUB_DOWNLOADED_DIR imported from config
# DISCOVERY_DIR imported from config
CANDIDATES_FILE = DISCOVERY_DIR / "candidates.json"

# ClawHub API (v1.3: 从PLATFORM_CONFIG统一读取)
CLAWHUB_API_BASE = PLATFORM_CONFIG['clawhub']['api_base']
CLAWHUB_MIRROR = PLATFORM_CONFIG['clawhub']['mirror']

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

def get_existing_source_slugs() -> Set[str]:
    """获取本地DB中所有已有的source_slug

    V126 W4: 委托到 skill_core.db.get_existing_source_slugs_from_db(TD-184)
    V129 Z10 (TD-219): 复核确认 — 已委托到 skill_core.db, 无重复实现。
    github_scanner.get_existing_source_slugs 同样委托到同一入口, 二者均为薄包装,
    不合并(保留各自模块入口)。
    """
    return db_module.get_existing_source_slugs_from_db()

def get_existing_display_names() -> Set[str]:
    """获取本地DB中所有已有的display_name

    V128 Y7: 委托到skill_core.db.get_existing_display_names_from_db(TD-207)
    """
    return db_module.get_existing_display_names_from_db()

def get_existing_slugs() -> Set[str]:
    """获取本地DB中所有已有的slug

    V126 W4: 委托到 skill_core.db.get_existing_slugs_from_db(TD-184)
    """
    return db_module.get_existing_slugs_from_db()

# ============================================================
# ClawHub 扫描器
# ============================================================

def fetch_url(url: str, timeout: int = 15) -> Optional[str]:
    """安全获取URL内容

    V129 Z9 (TD-218): 本函数与 update_mechanism.fetch_url 同名但实现不同。
    本版本面向 ClawHub JSON API: 请求头额外带 'Accept: application/json', 仅用宽泛 except 兜底;
    update_mechanism.fetch_url 为通用 URL 抓取(无 Accept 头, 细分 HTTPError/URLError/Exception 三段捕获)。
    请求头与异常处理行为有差异, 不合并。
    """
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception:  # [V130 A1] 宽泛捕获: HTTP请求可能因网络/超时/解码等多种原因失败
        return None

def scan_clawhub_category(category: str, limit: int = 50) -> List[Dict[str, Any]]:
    """扫描clawhub指定类别的新skill"""
    skills = []

    # 尝试API端点 (v1端点优先，已验证可用)
    api_urls = [
        f"{CLAWHUB_API_BASE}/skills?category={category}&page=1&pageSize={limit}",
        f"{CLAWHUB_MIRROR}/skills?category={category}&page=1&pageSize={limit}",
        f"{CLAWHUB_API_BASE}/skills?sort=newest&limit={limit}",
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
                metadata = parse_frontmatter(content)['fields']
                skills.append({
                    'source_slug': slug,
                    'source_platform': 'clawhub',
                    'source_url': f"{PLATFORM_CONFIG['clawhub']['host']}/skills/{slug}",
                    'display_name': metadata.get('displayName', slug),
                    'summary': metadata.get('summary', ''),
                    'category': category_dir.name,
                    'local_path': str(skill_dir),
                    'content': content[:500],
                })
            except Exception:  # [V130 A1] 宽泛捕获: 文件读取和frontmatter解析可能因编码/格式等多种原因失败
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
                metadata = parse_frontmatter(skill_content)['fields']
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

# [V131 B5: 与github_scanner.deduplicate不同(本版处理发现技能去重, 对方处理GitHub扫描结果)]
def deduplicate(discovered_skills: List[Dict[str, Any]]) -> Dict[str, Any]:
    """去重比对，分离新skill和已存在skill
    
    v3.3: 新增content_hash内容相似度检查,防止相同内容以不同slug上传
    """
    existing_slugs = get_existing_slugs()
    existing_source_slugs = get_existing_source_slugs()
    existing_names = get_existing_display_names()
    
    # v3.3: 加载已有content_hash集合,用于内容去重
    # V153 R8修复: content_hash加载失败时raise(fail-safe),原为跳过去重(fail-open)
    # 原因: existing_content_hashes为空时,所有候选都会被视为"新内容",去重失效
    existing_content_hashes = set()
    try:
        conn = db_module.get_db()
        for row in conn.execute("SELECT content_hash FROM skills WHERE content_hash IS NOT NULL AND content_hash != ''"):
            existing_content_hashes.add(row[0])
        conn.close()
    except Exception as e:
        raise RuntimeError(f"content_hash加载失败 — 内容去重不可用,阻断(fail-safe): {e}")

    result = {
        'dedup_time': datetime.now().isoformat(),
        'total_discovered': len(discovered_skills),
        'new_skills': [],
        'duplicate_by_source_slug': [],
        'duplicate_by_display_name': [],
        'duplicate_by_slug': [],
        'duplicate_by_content_hash': [],  # v3.3: 内容指纹去重
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

        # v3.3: 检查content_hash是否已存在(内容指纹去重)
        content = skill.get('content', '')
        if content and existing_content_hashes:
            import hashlib
            content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]
            if content_hash in existing_content_hashes:
                result['duplicate_by_content_hash'].append(skill)
                continue

        result['new_skills'].append(skill)

    return result

# ============================================================
# 工具函数
# ============================================================

def ensure_dir():
    """确保发现目录存在

    V128 Y8: 评估结论 — 此函数仅为1行DISCOVERY_DIR.mkdir()调用,
    不适合作为通用工具迁移到skill_core.utils(非通用函数)。
    保留在auto_discover.py中作为本地辅助函数。
    """
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

    # V187: 同步更新 candidates_unified.json (auto_differentiate.py 读取的文件)
    unified_file = DISCOVERY_DIR / "candidates_unified.json"
    existing_candidates = []
    existing_ids = set()
    if unified_file.exists():
        try:
            with open(unified_file, 'r', encoding='utf-8') as uf:
                unified_data = json.load(uf)
            existing_candidates = unified_data.get('candidates', [])
            existing_ids = {c.get('source_id', c.get('name', '')) for c in existing_candidates}
        except Exception:
            pass

    # 转换新候选为统一格式
    new_unified = []
    for skill in dedup_result.get('new_skills', []):
        sid = skill.get('source_slug', skill.get('display_name', ''))
        if sid not in existing_ids:
            new_unified.append({
                'source': skill.get('source_platform', 'unknown'),
                'source_id': sid,
                'name': sid,
                'description': skill.get('summary', ''),
                'category': skill.get('category', ''),
                'content_preview': skill.get('content', '')[:500],
                'url': skill.get('source_url', ''),
                'metadata': {
                    'source_platform': skill.get('source_platform', ''),
                    'original_slug': sid,
                    'local_path': skill.get('local_path', ''),
                },
                'discovered_at': datetime.now().isoformat(),
            })

    if new_unified:
        all_candidates = existing_candidates + new_unified
        unified_result = {
            'generated_at': datetime.now().isoformat(),
            'total_count': len(all_candidates),
            'candidates': all_candidates,
        }
        with open(unified_file, 'w', encoding='utf-8') as uf:
            json.dump(unified_result, uf, ensure_ascii=False, indent=2)
        print(f"统一候选文件已更新: {unified_file} (+{len(new_unified)} 新候选, 总计{len(all_candidates)}个)")

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

    # v3.0安全增强: 停止生成-free派生slug,改为单一slug + edition/pricing_model元数据
    # 根因: 2026-07-24批量上传中, 990个-free/-pro派生skill被平台内容指纹系统
    #       识别为"批量生产的近似重复内容"并批量封禁(封禁率93.4%)
    # 修复: 新导入的skill只生成一个slug(paid版), 免费版由平台原生定价机制承载
    #       不再创建base_slug-free独立skill
    base_slug = args.slug
    paid_slug = base_slug

    # 从候选数据提取信息
    display_name = target.get('display_name', base_slug)
    source_platform = target.get('source_platform', 'unknown')
    source_url = target.get('source_url', '')
    source_author = target.get('source_author', '')
    source_license = target.get('source_license', '')
    skill_type = target.get('skill_type', 'general')
    category = target.get('category', 'Productivity')

    # 导入到DB (v3.0: 仅生成单一skill,不再生成-free派生)
    # V117 W4: register_skill统一通过db_module访问

    # v1.3: 计算content_hash (从源内容计算SHA-256前16位)
    source_content = target.get('content', '')
    if not source_content and target.get('local_path'):
        # 如果有本地路径,读取完整SKILL.md内容
        try:
            source_content = Path(target['local_path']).joinpath('SKILL.md').read_text(encoding='utf-8')
        except Exception:  # [V130 A1] 宽泛捕获: 文件读取可能因路径/编码等多种原因失败
            source_content = ''
    content_hash = hashlib.sha256(source_content.encode('utf-8')).hexdigest()[:16] if source_content else None

    # V188修复: 如果候选已有本地路径(如clawhub_downloaded的本地扫描结果),直接使用
    candidate_local_path = target.get('local_path', '')
    has_local_skill_md = False
    if candidate_local_path:
        skill_md_check = Path(candidate_local_path) / 'SKILL.md'
        has_local_skill_md = skill_md_check.exists()

    paid_skill_id = db_module.register_skill(
        slug=paid_slug,
        name=paid_slug,
        display_name=display_name,
        version='1.0.0',
        category=category,
        source=source_platform,
        local_path=candidate_local_path if has_local_skill_md else '',  # V188: 有本地SKILL.md则直接使用,否则留空待差异化
        source_slug=args.slug,
        source_url=source_url,
        source_author=source_author,
        source_license=source_license,
        skill_type=skill_type,
        pricing_model='per_call',
        is_differentiated=1 if has_local_skill_md else 0,  # V188: 已有SKILL.md则标记为已差异化
        edition='paid',
        parent_slug=None,
        content_hash=content_hash,
        workflow_state='completed' if has_local_skill_md else 'step1_read_original',
        notes=f"Imported from discovery. Source: {source_platform}"
    )

    # v1.3: 填充simhash (接入去重管道)
    # V153 R9修复: simhash填充失败时记录警告(非阻断,但标记需人工复查)
    if source_content:
        try:
            from content_dedup import update_simhash
            update_simhash(paid_slug, source_content)
        except ImportError as e:
            print(f"[WARN] content_dedup模块不可用,simhash未填充(近似去重对该skill失效): {e}")
        except Exception as e:
            print(f"[WARN] simhash填充失败(近似去重对该skill失效,需人工复查): {e}")

    print(f"✓ 导入成功: {args.slug}")
    print(f"  slug={paid_slug}, skill_id={paid_skill_id}, workflow_state=step1_read_original")
    print(f"  来源: {source_platform}")
    print(f"  displayName: {display_name}")
    print(f"\n注意: v3.0已停止生成-free派生slug,由平台原生定价机制承载免费版")
    print(f"差异化改造完成后，使用以下命令上传:")
    print(f"  python update_mechanism.py generate {paid_slug}")
    print(f"  python update_mechanism.py upload {paid_slug}")

def cmd_import_all(args):
    """批量导入所有候选skill到本地DB

    V188新增: 支持一次性导入所有scan发现的候选skill, 不需要逐个import
    """
    if not CANDIDATES_FILE.exists():
        print("未找到候选列表，请先执行 scan 命令")
        return

    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_skills = data.get('new_skills', [])
    if not new_skills:
        print("候选列表为空，没有需要导入的skill")
        return

    print(f"开始批量导入 {len(new_skills)} 个候选skill...")
    success_count = 0
    fail_count = 0
    skip_count = 0

    for i, target in enumerate(new_skills, 1):
        slug = target.get('source_slug', '')
        if not slug:
            skip_count += 1
            continue

        # 检查是否已存在
        existing_slugs = get_existing_slugs()
        if slug in existing_slugs:
            skip_count += 1
            continue

        # 复用 cmd_import 的逻辑
        base_slug = slug
        display_name = target.get('display_name', base_slug)
        source_platform = target.get('source_platform', 'unknown')
        source_url = target.get('source_url', '')
        source_author = target.get('source_author', '')
        source_license = target.get('source_license', '')
        skill_type = target.get('skill_type', 'general')
        category = target.get('category', 'Productivity')

        # V188: 使用候选的local_path(如果SKILL.md存在)
        candidate_local_path = target.get('local_path', '')
        has_local_skill_md = False
        if candidate_local_path:
            skill_md_check = Path(candidate_local_path) / 'SKILL.md'
            has_local_skill_md = skill_md_check.exists()

        # 计算content_hash
        source_content = target.get('content', '')
        if not source_content and candidate_local_path:
            try:
                source_content = Path(candidate_local_path).joinpath('SKILL.md').read_text(encoding='utf-8')
            except Exception:
                source_content = ''
        content_hash = hashlib.sha256(source_content.encode('utf-8')).hexdigest()[:16] if source_content else None

        try:
            skill_id = db_module.register_skill(
                slug=base_slug,
                name=base_slug,
                display_name=display_name,
                version='1.0.0',
                category=category,
                source=source_platform,
                local_path=candidate_local_path if has_local_skill_md else '',
                source_slug=base_slug,
                source_url=source_url,
                source_author=source_author,
                source_license=source_license,
                skill_type=skill_type,
                pricing_model='per_call',
                is_differentiated=1 if has_local_skill_md else 0,
                edition='paid',
                parent_slug=None,
                content_hash=content_hash,
                workflow_state='completed' if has_local_skill_md else 'step1_read_original',
                notes=f"Batch imported from discovery. Source: {source_platform}"
            )

            # 填充simhash
            if source_content:
                try:
                    from content_dedup import update_simhash
                    update_simhash(base_slug, source_content)
                except Exception:
                    pass  # simhash失败非阻断

            success_count += 1
            if i % 50 == 0:
                print(f"  进度: {i}/{len(new_skills)} (成功={success_count}, 跳过={skip_count}, 失败={fail_count})")
        except Exception as e:
            print(f"  [FAIL] {slug}: {e}")
            fail_count += 1

    print(f"\n批量导入完成:")
    print(f"  成功: {success_count}")
    print(f"  跳过(已存在): {skip_count}")
    print(f"  失败: {fail_count}")
    print(f"  总计: {len(new_skills)}")


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

    # import-all (V188新增)
    subparsers.add_parser('import-all', help='批量导入所有候选skill')

    args = parser.parse_args()

    if args.command == 'scan':
        cmd_scan(args)
    elif args.command == 'dedup':
        cmd_dedup(args)
    elif args.command == 'candidates':
        cmd_candidates(args)
    elif args.command == 'import':
        cmd_import(args)
    elif args.command == 'import-all':
        cmd_import_all(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
