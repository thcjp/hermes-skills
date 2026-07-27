#!/usr/bin/env python3
"""
ClawHub Batch Uploader
======================
Batch upload skills to ClawHub using the clawhub CLI.
v2.3: 增加DB跟踪(上传成功后更新clawhub_sync_status) + --from-db模式

Usage:
    python clawhub_batch_uploader.py                    # Upload all remaining (up to daily limit)
    python clawhub_batch_uploader.py --limit 50         # Upload only 50
    python clawhub_batch_uploader.py --dry-run          # Dry run (no actual upload)
    python clawhub_batch_uploader.py --resume            # Resume from last checkpoint
    python clawhub_batch_uploader.py --from-db           # 从DB查询待上传skill(替代JSON)
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR, DATA_DIR, REGISTRY_DIR
# === End Phase 1 ===

import json
import os
import subprocess
import sys
import time
import re
import sqlite3
from pathlib import Path
from datetime import datetime

# v2.3: DB路径(复用project_config)
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
try:
    from config import DB_PATH as _DB_PATH
except ImportError:
    _DB_PATH = Path(r"d:\skills\skill-registry.db")

# v2.6: 质量门禁集成(复用quality_gate统一函数, 不创建碎片化代码)
# v3.2: 升级为autofix版本 — 上传前自动修复安全+幻觉问题, 减少审核拒绝率
try:
    from quality_gate import (
        run_security_precheck_with_autofix as run_security_precheck,
        run_marketing_gate,
        run_anti_hallucination_with_autofix as run_anti_hallucination,
        run_rating_gate,
    )
    _QUALITY_GATE_AVAILABLE = True
except ImportError:
    try:
        # 向后兼容: 如果autofix版本不可用, 退回到原始版本
        from quality_gate import run_security_precheck, run_marketing_gate, run_anti_hallucination, run_rating_gate
        _QUALITY_GATE_AVAILABLE = True
    except ImportError:
        _QUALITY_GATE_AVAILABLE = False

# ClawHub分类映射配置
CATEGORY_MAP_FILE = Path(__file__).resolve().parent.parent / "data" / "category_mapping.json"

def _load_category_map():
    """加载分类映射配置"""
    if CATEGORY_MAP_FILE.exists():
        with open(CATEGORY_MAP_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

_CATEGORY_MAP_CACHE = None

def get_clawhub_category(skill_dir):
    """从SKILL.md推断ClawHub分类 (v2.2: 修复映射链断裂bug)
    
    映射优先级:
    1. local_to_clawhub直连 (本地格式→ClawHub格式, 修复frontmatter category=Agents时断裂)
    2. clawhub_categories中转 (平台格式→ClawHub格式, 需先local_to_platform转换)
    3. slug关键词推断
    4. body内容推断
    """
    global _CATEGORY_MAP_CACHE
    if _CATEGORY_MAP_CACHE is None:
        _CATEGORY_MAP_CACHE = _load_category_map()
    
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return "other"
    
    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    # 解析frontmatter
    fm = {}
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) > 1:
            fm_str = parts[1]
            for line in fm_str.split('\n'):
                if ':' in line:
                    key, _, val = line.partition(':')
                    fm[key.strip()] = val.strip().strip('"\'')
    
    # 1. 优先: local_to_clawhub直连 (修复frontmatter category=Agents等本地格式时的映射断裂)
    fm_category = fm.get('category', '')
    if fm_category:
        local_to_clawhub = _CATEGORY_MAP_CACHE.get('local_to_clawhub', {})
        if fm_category in local_to_clawhub:
            return local_to_clawhub[fm_category]
        
        # 2. 中转: local_to_platform → clawhub_categories
        local_to_platform = _CATEGORY_MAP_CACHE.get('local_to_platform', {})
        platform_cat = local_to_platform.get(fm_category, '')
        if platform_cat:
            clawhub_map = _CATEGORY_MAP_CACHE.get('clawhub_categories', {})
            if platform_cat in clawhub_map:
                return clawhub_map[platform_cat]
        
        # 3. 兼容: frontmatter已经是平台格式(如ai-agent)
        clawhub_map = _CATEGORY_MAP_CACHE.get('clawhub_categories', {})
        if fm_category in clawhub_map:
            return clawhub_map[fm_category]
    
    # 2. 从slug推断
    slug = skill_dir.name.lower()
    keyword_map = {
        'agents': ['agent', 'ai', 'llm', 'gpt', 'claude', 'memory', 'orchestrat'],
        'productivity': ['code', 'dev', 'program', 'api', 'doc', 'office', 'pdf', 'word', 'sheet', 'task', 'manage'],
        'research': ['data', 'analytic', 'csv', 'excel', 'chart', 'search', 'research'],
        'creative': ['content', 'write', 'copy', 'article', 'design', 'graphic', 'image', 'media', 'video'],
        'security': ['security', 'audit', 'compliance', 'safe', 'vulnerab'],
        'knowledge': ['knowledge', 'note', 'wiki', 'bookmark', 'learn', 'edu', 'teach'],
        'automation': ['auto', 'deploy', 'ci', 'cd', 'monitor', 'devops'],
        'lifestyle': ['life', 'travel', 'health', 'food', 'weather'],
        'communication': ['email', 'chat', 'message', 'social', 'notify'],
        'integrations': ['integrat', 'connect', 'sync', 'webhook', 'api-gateway'],
    }
    for cat, keywords in keyword_map.items():
        for kw in keywords:
            if kw in slug:
                return cat
    
    # 3. 从body内容推断
    body_lower = content[:2000].lower()
    for cat, keywords in keyword_map.items():
        matches = sum(1 for kw in keywords if kw in body_lower)
        if matches >= 2:
            return cat
    
    return "other"


def get_clawhub_topics(skill_dir, slug=None):
    """从SKILL.md提取topics(话题标签)
    
    ClawHub的topics是真正的搜索曝光标签(不是API里的tags字段,那是版本号)
    从frontmatter的tags字段和body关键词提取
    """
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return []
    
    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    topics = []
    
    # 解析frontmatter
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) > 1:
            fm_str = parts[1]
            for line in fm_str.split('\n'):
                line = line.strip()
                if line.startswith('tags:'):
                    # tags可能在同一行或下一行
                    val = line[5:].strip()
                    if val.startswith('['):
                        try:
                            topics.extend(json.loads(val))
                        except:
                            pass
                    elif val:
                        # 逗号分隔
                        topics.extend([t.strip().strip('"\'') for t in val.split(',') if t.strip()])
    
    # 从slug提取关键词
    if slug:
        slug_parts = slug.split('-')
        for part in slug_parts:
            if len(part) > 2 and part not in ['the', 'and', 'for', 'pro', 'sk', 'free', 'paid', 'tool']:
                topics.append(part)
    
    # 去重，最多10个
    seen = set()
    unique = []
    for t in topics:
        t_lower = t.lower()
        if t_lower not in seen and t:
            seen.add(t_lower)
            unique.append(t)
        if len(unique) >= 10:
            break
    
    return unique[:10] if unique else ["tool", "automation"]


def get_display_name(skill_dir):
    """从SKILL.md获取displayName"""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None
    
    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) > 1:
            fm_str = parts[1]
            for line in fm_str.split('\n'):
                if line.strip().startswith('displayName:'):
                    val = line.strip()[12:].strip().strip('"\'')
                    if val:
                        return val
    
    return None

# ============ v2.3: DB跟踪 (上传成功后更新clawhub_sync_status) ============

def update_db_clawhub_status(slug, status='synced', version=None):
    """上传成功后更新DB的clawhub_sync_status (幂等, 含重试)
    
    Args:
        slug: skill slug
        status: 'synced' (成功) 或 'failed' (失败)
        version: 上传的版本号
    """
    import time as _time
    for attempt in range(3):
        try:
            conn = sqlite3.connect(str(_DB_PATH), timeout=10)
            conn.execute("PRAGMA foreign_keys = ON")
            conn.execute("PRAGMA journal_mode = WAL")
            
            # 更新skills表
            conn.execute("""
                UPDATE skills SET 
                    clawhub_sync_status = ?,
                    last_sync_at = ?
                WHERE slug = ?
            """, (status, datetime.now().isoformat(), slug))
            
            # 如果有skill_id, 也更新platform_uploads表
            row = conn.execute("SELECT id FROM skills WHERE slug = ?", (slug,)).fetchone()
            if row:
                skill_id = row[0]
                # 检查是否已有记录
                existing = conn.execute("""
                    SELECT id FROM platform_uploads 
                    WHERE skill_id = ? AND platform = 'clawhub'
                """, (skill_id,)).fetchone()
                
                if existing:
                    conn.execute("""
                        UPDATE platform_uploads SET 
                            upload_status = ?,
                            upload_date = ?
                        WHERE skill_id = ? AND platform = 'clawhub'
                    """, ('success' if status == 'synced' else 'failed', 
                          datetime.now().isoformat(), skill_id))
                else:
                    conn.execute("""
                        INSERT INTO platform_uploads 
                            (skill_id, platform, platform_slug, upload_date, upload_status, version)
                        VALUES (?, 'clawhub', ?, ?, ?, ?)
                    """, (skill_id, slug, datetime.now().isoformat(),
                          'success' if status == 'synced' else 'failed',
                          version or 'unknown'))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            if attempt < 2:
                _time.sleep(1)
                continue
            print(f"\n  [DB更新失败] {slug}: {e}")
            return False


def get_pending_slugs_from_db(limit=0):
    """从DB查询待上传ClawHub的skill (有本地文件的pending状态)
    
    Returns:
        list of slug strings
    """
    conn = sqlite3.connect(str(_DB_PATH))
    conn.row_factory = sqlite3.Row
    
    query = """
        SELECT slug, local_path FROM skills 
        WHERE clawhub_sync_status = 'pending'
        AND local_path IS NOT NULL AND local_path != ''
        ORDER BY slug
    """
    if limit > 0:
        query += f" LIMIT {limit}"
    
    rows = conn.execute(query).fetchall()
    conn.close()
    
    # 过滤: 只返回本地文件确实存在的
    valid_slugs = []
    for r in rows:
        local_path = r["local_path"]
        if local_path.startswith("/d/"):
            local_path = "d:" + local_path[2:]
        skill_md = Path(local_path) / "SKILL.md"
        if skill_md.exists():
            valid_slugs.append(r["slug"])
    
    return valid_slugs


# REGISTRY_DIR imported from config
BATCHES_FILE = DATA_DIR / "clawhub_upload_batches.json"
RESULTS_FILE = DATA_DIR / "clawhub_upload_results.json"
DIR_MAPPING_FILE = REGISTRY_DIR / "round40_clawhub_dir_mapping.json"
REMAINING_FILE = DATA_DIR / "clawhub_remaining.json"
CHECKPOINT_FILE = DATA_DIR / "clawhub_upload_checkpoint.json"
PUBLISHED_SLUGS_FILE = DATA_DIR / "clawhub_published_slugs.json"

REGISTRY = "https://clawhub.ai"
DAILY_LIMIT = 200
DELAY_BETWEEN_UPLOADS = 2  # seconds
CHANGELOG = "v2.3 quality enhancement - security audit + marketing packaging + slug-content validation"

# Alternative directory locations to check
ALT_DIRS = [
    Path(r"D:\skills\packaged-skills\skillhub"),
    Path(r"D:\skills\opensource-skills\packaged"),
    DIFFERENTIATED_DIR,
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
    """Find skill directory using mapping or fallback search 
    (v2.1: 增强slug变体匹配; v2.3: 优先使用DB的local_path)"""
    # v2.3: 优先从DB获取local_path (最可靠)
    try:
        conn = sqlite3.connect(str(_DB_PATH))
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT local_path FROM skills WHERE slug = ?", (slug,)).fetchone()
        conn.close()
        if row and row["local_path"]:
            local_path = row["local_path"]
            if local_path.startswith("/d/"):
                local_path = "d:" + local_path[2:]
            p = Path(local_path)
            if p.exists() and (p / "SKILL.md").exists():
                return p
    except Exception:
        pass

    # Check dir mapping
    d = dir_mapping.get(slug)
    if d and Path(d).exists() and (Path(d) / "SKILL.md").exists():
        return Path(d)

    # v2.1: 生成slug变体列表(处理 -sk, -free, -paid 等后缀)
    slug_variants = [slug]
    if slug.endswith('-sk'):
        slug_variants.append(slug[:-3])  # 去掉 -sk 后缀
    if slug.endswith('-free'):
        slug_variants.append(slug[:-5])  # 去掉 -free 后缀
    if slug.endswith('-paid'):
        slug_variants.append(slug[:-5])  # 去掉 -paid 后缀
    if slug.endswith('-pro-sk'):
        slug_variants.append(slug.replace('-pro-sk', '-pro'))
        slug_variants.append(slug.replace('-pro-sk', ''))
    # 去掉 -sk 后尝试其他变体
    base_slug = slug
    for suffix in ['-sk', '-free', '-paid']:
        if base_slug.endswith(suffix):
            base_slug = base_slug[:-len(suffix)]
            break
    if base_slug != slug:
        slug_variants.append(base_slug)

    # Fallback: search in alternative directories with all slug variants
    for base in ALT_DIRS:
        if not base.exists():
            continue
        for try_slug in slug_variants:
            # Direct match
            p = base / try_slug
            if p.exists() and (p / "SKILL.md").exists():
                return p
            # Search in subdirectories (for differentiated-skills which has category folders)
            if base.name == "differentiated-skills":
                for cat_dir in base.iterdir():
                    if not cat_dir.is_dir():
                        continue
                    p = cat_dir / try_slug
                    if p.exists() and (p / "SKILL.md").exists():
                        return p

    return None


def upload_skill(skill_dir, slug, dry_run=False, skip_quality_gate=False):
    """Upload a single skill to ClawHub via CLI (v2.6: 集成质量门禁)
    
    营销元素:
    - --categories: 分类(从SKILL.md推断,映射到ClawHub标准分类)
    - --topics: 话题标签(从frontmatter tags和slug提取)
    - --name: 显示名称(从frontmatter displayName获取)
    
    质量门禁 (v2.6新增):
    - 安全预检(21项): critical阻断上传
    - 营销关卡(7项): 检查营销数据质量
    - 防幻觉(3项): 检测虚假实现
    - 评分门控(2项): 检查平台历史评分
    """
    if dry_run:
        return {'success': True, 'slug': slug, 'message': 'DRY RUN', 'dry_run': True}

    # v2.6: 质量门禁检查 (上传前)
    if not skip_quality_gate and _QUALITY_GATE_AVAILABLE:
        skill_md_path = Path(skill_dir) / "SKILL.md"
        if skill_md_path.exists():
            # 安全预检 — critical阻断
            sec = run_security_precheck(skill_md_path)
            critical_fails = [c for c in sec.get('checks', []) if not c.get('passed') and c.get('severity') == 'critical']
            if critical_fails:
                failed_names = [c['name'] for c in critical_fails]
                return {'success': False, 'slug': slug,
                        'error': 'QUALITY_GATE_BLOCKED',
                        'message': f"安全预检未通过(critical): {', '.join(failed_names)}",
                        'quality_gate': {'security': sec}}

            # 评分门控 — 低评分阻断
            rg = run_rating_gate(skill_md_path, slug)
            if not rg.get('overall_passed', True):
                failed = [c.get('name', '?') for c in rg.get('checks', []) if not c.get('passed')]
                return {'success': False, 'slug': slug,
                        'error': 'RATING_GATE_BLOCKED',
                        'message': f"评分门控未通过: {', '.join(failed)}",
                        'quality_gate': {'rating': rg}}

            # 防幻觉检查
            ah = run_anti_hallucination(skill_md_path)
            if not ah.get('overall_passed', True):
                failed = [c.get('name', '?') for c in ah.get('checks', []) if not c.get('passed')]
                return {'success': False, 'slug': slug,
                        'error': 'ANTI_HALLUCINATION_BLOCKED',
                        'message': f"防幻觉检查未通过: {', '.join(failed)}",
                        'quality_gate': {'anti_hallucination': ah}}

            # 营销关卡 — 检查但不阻断(仅警告, ClawHub营销标准较宽松)
            mg = run_marketing_gate(skill_md_path)
            if not mg.get('overall_passed', True):
                failed = [c.get('name', '?') for c in mg.get('checks', []) if not c.get('passed')]
                # 营销关卡仅警告,不阻断ClawHub上传(ClawHub与SkillHub标准不同)
                print(f"  [WARNING] 营销关卡未通过({len(failed)}项): {', '.join(failed[:3])}")
        # SKILL.md不存在时跳过质量检查,后续上传命令会自然失败

    # v2.1: 提取营销参数
    category = get_clawhub_category(skill_dir)
    topics = get_clawhub_topics(skill_dir, slug)
    display_name = get_display_name(skill_dir)
    
    # 构建上传命令(含营销参数) — v2.4: 修复npx→clawhub, 正确引用含空格参数
    def _quote_arg(arg):
        """Windows shell引用: 含空格的参数加双引号"""
        if ' ' in str(arg):
            return f'"{arg}"'
        return str(arg)
    
    cmd_parts = [
        'clawhub',
        '--registry', REGISTRY,
        'publish', _quote_arg(skill_dir),
        '--changelog', _quote_arg(CHANGELOG),
        '--categories', category,
        '--topics', ','.join(topics),
    ]
    if display_name:
        cmd_parts.extend(['--name', _quote_arg(display_name)])
    
    cmd_str = ' '.join(cmd_parts)

    try:
        # v2.4: 设置CLAWHUB_REGISTRY环境变量, 确保CLI内部操作也使用正确的registry
        upload_env = os.environ.copy()
        upload_env['CLAWHUB_REGISTRY'] = REGISTRY
        result = subprocess.run(
            cmd_str,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=r"D:\skills",
            shell=True,
            env=upload_env
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
        elif 'Not logged in' in output or 'Run: clawhub login' in output:
            return {
                'success': False,
                'slug': slug,
                'error': 'NOT_LOGGED_IN',
                'message': 'ClawHub CLI not logged in. Run: npx clawhub --registry https://clawhub.ai login'
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
    parser = argparse.ArgumentParser(description='ClawHub Batch Uploader v2.6 (含质量门禁)')
    parser.add_argument('--limit', type=int, default=DAILY_LIMIT, help='Max skills to upload')
    parser.add_argument('--dry-run', action='store_true', help='Dry run mode')
    parser.add_argument('--resume', action='store_true', help='Resume from checkpoint')
    parser.add_argument('--from-db', action='store_true', help='从DB查询待上传skill(替代JSON)')
    parser.add_argument('--skip-quality-gate', action='store_true', help='跳过质量门禁检查(紧急场景)')
    # v3.0: 支持自定义上传间隔(秒), 默认2秒, daily_sync传入120(2分钟)以防止触发反垃圾系统
    parser.add_argument('--delay', type=int, default=DELAY_BETWEEN_UPLOADS,
                        help=f'Delay between uploads in seconds (default: {DELAY_BETWEEN_UPLOADS})')
    args = parser.parse_args()

    # Load dir_mapping (optional, fallback to ALT_DIRS search)
    dir_mapping = load_json(DIR_MAPPING_FILE)
    dir_mapping = dir_mapping['found_mapping'] if dir_mapping else {}

    # v2.3: 从DB获取待上传slugs, 或从JSON获取
    if args.from_db:
        all_slugs = get_pending_slugs_from_db(limit=0)  # 获取全部, 主循环处理limit
        print(f"[DB模式] 从数据库查询到 {len(all_slugs)} 个待上传skill")
    else:
        remaining_data = load_json(REMAINING_FILE)
        if not remaining_data:
            print("ERROR: No remaining data found. Run with --from-db or run calc_clawhub_remaining.py first.")
            sys.exit(1)
        all_slugs = remaining_data['slugs']
        print(f"[JSON模式] 从JSON加载 {len(all_slugs)} 个待上传slug")

    print(f"Daily limit: {args.limit}")
    print(f"Dry run: {args.dry_run}")
    print(f"Upload delay: {args.delay}s between uploads")
    print()

    # Load checkpoint for resume
    uploaded_today = set()
    if args.resume and CHECKPOINT_FILE.exists():
        checkpoint = load_json(CHECKPOINT_FILE)
        uploaded_today = set(checkpoint.get('uploaded_today', []))
        print(f"Resuming: {len(uploaded_today)} already uploaded today")

    # Also load previous results to skip already uploaded
    # v2.4: --from-db模式跳过JSON过滤, DB是唯一数据源
    if args.from_db:
        prev_success = set()
        published = set()
        prev_results = None  # 修复: 初始化prev_results避免NameError
    else:
        prev_results = load_json(RESULTS_FILE)
        if prev_results:
            prev_success = set(prev_results.get('success', []))
        else:
            prev_success = set()
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

        # v3.0: 速率限制预检 (防止爆发式上传触发平台反垃圾系统)
        # v3.1: 改为等待重试而非直接退出, 复用daily_sync.py的wait_for_upload_slot
        # v3.2: 修复函数名不匹配bug (wait_for_rate_limit→wait_for_upload_slot)
        try:
            from daily_sync import wait_for_upload_slot
            rate_check = wait_for_upload_slot('clawhub', max_wait_seconds=300)
            if not rate_check.get('allowed', True):
                print(f"\n  [{i}/{len(to_upload)}] RATE LIMITED (超时): {rate_check.get('reason', '未知')}")
                rate_limited = True
                break
        except ImportError:
            pass  # daily_sync不可用时跳过速率限制(向后兼容)
        except Exception:
            pass  # 速率限制异常不阻断上传(容错)

        # Upload
        print(f"  [{i}/{len(to_upload)}] {slug}...", end="", flush=True)
        result = upload_skill(skill_dir, slug, args.dry_run, skip_quality_gate=args.skip_quality_gate)

        if result['success']:
            print(f" OK ({result.get('version', '')})")
            success_count += 1
            results['success'].append(slug)
            uploaded_today.add(slug)
            # v2.3: 更新DB状态
            if not args.dry_run:
                update_db_clawhub_status(slug, 'synced', result.get('version'))
                # v3.0: 记录上传到速率限制表
                try:
                    from daily_sync import record_upload
                    record_upload('clawhub', slug)
                except Exception:
                    pass
        elif result.get('error') == 'VERSION_EXISTS':
            # Try incrementing version and retry
            print(f" VERSION_EXISTS, incrementing...", end="", flush=True)
            new_ver = increment_version(skill_dir)
            if new_ver:
                result2 = upload_skill(skill_dir, slug, args.dry_run, skip_quality_gate=args.skip_quality_gate)
                if result2['success']:
                    print(f" OK (v{new_ver})")
                    success_count += 1
                    results['success'].append(slug)
                    uploaded_today.add(slug)
                    # v2.3: 更新DB状态
                    if not args.dry_run:
                        update_db_clawhub_status(slug, 'synced', new_ver)
                        # v3.0: 记录上传到速率限制表
                        try:
                            from daily_sync import record_upload
                            record_upload('clawhub', slug)
                        except Exception:
                            pass
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
            time.sleep(args.delay)

    # Save final results
    save_json(CHECKPOINT_FILE, {
        'timestamp': datetime.now().isoformat(),
        'uploaded_today': list(uploaded_today),
        'total_success': success_count,
        'total_failed': fail_count
    })

    # Merge with previous results
    if prev_results:
        prev_results.setdefault('success', []).extend(results['success'])
        prev_results.setdefault('failed', []).extend(results['failed'])
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
        print(f"\nRate limit reached (wait timeout). Try again in a few minutes.")
        print(f"Run: python clawhub_batch_uploader.py --resume")


if __name__ == '__main__':
    main()
