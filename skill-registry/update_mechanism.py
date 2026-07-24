#!/usr/bin/env python3
"""
Skill 自动更新机制主控脚本
=========================
触发词: "更新"
功能: 检测每个skill的原始来源是否更新 → 分析变更 → 本地升级 → 生成免费/付费双版本 → 同步到SkillHub

用法:
  python update_mechanism.py check              # 检查所有skill的来源更新状态
  python update_mechanism.py check --slug xxx   # 检查指定skill
  python update_mechanism.py generate <slug>    # 生成双版本payload
  python update_mechanism.py upload <slug>      # 上传skill到平台
  python update_mechanism.py upload-all         # 上传所有已变更skill
  python update_mechanism.py status             # 显示所有skill当前状态
  python update_mechanism.py report             # 生成更新报告(给AI分析用)
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR
from project_config import TOOLS_DIR
from project_config import DB_PATH
from project_config import CLAWHUB_DOWNLOADED_DIR
from project_config import PROJECT_ROOT
# === End Phase 1 ===
SKILLS_ROOT = PROJECT_ROOT
SKILL_REGISTRY_DIR = TOOLS_DIR


import argparse
import json
import sqlite3
import hashlib
import urllib.request
import urllib.error
import urllib.parse
import re
import os
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

# ============================================================
# 配置
# ============================================================

# DB_PATH imported from config
# SKILLS_ROOT = PROJECT_ROOT (imported from config)
# SKILL_REGISTRY_DIR = TOOLS_DIR (imported from config)
PAYLOADS_DIR = Path(r"c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\payloads")
ENTERPRISE_UPLOAD_DIR = SKILLS_ROOT / "enterprise-upload"
PACKAGED_SKILLS_DIR = SKILLS_ROOT / "packaged-skills" / "skillhub"
OPENSOURCE_SKILLS_DIR = SKILLS_ROOT / "opensource-skills" / "packaged"
# DIFFERENTIATED_SKILLS_DIR = DIFFERENTIATED_DIR (imported from config)
# CLAWHUB_DOWNLOADED_DIR imported from config

# clawhub 来源URL模式: https://clawhub.ai/{author}/skills/{slug}
CLAWHUB_URL_PATTERN = re.compile(r"https?://clawhub\.ai/[^/]+/skills/([^/]+)")
# GitHub raw URL模式: https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}
GITHUB_RAW_PATTERN = re.compile(r"https?://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)")
# GitHub 仓库URL模式: https://github.com/{owner}/{repo}
GITHUB_REPO_PATTERN = re.compile(r"https?://github\.com/([^/]+)/([^/]+)")

# SkillHub API
SKILLHUB_API_BASE = "https://api.skillhub.cn"
SKILLHUB_CLI_PATH = os.path.expanduser("~/.local/bin/skillhub")
SKILLHUB_RUNNER = str(SKILLS_ROOT / "run-skillhub.sh")

# 默认定价
DEFAULT_PAID_PRICE = "9.90"
DEFAULT_CURRENCY = "CNY"

# 来源类型
SOURCE_CLAWHUB_TYPES = {"clawhub_download", "clawhub_differentiated", "clawhub"}
SOURCE_OPENSOURCE_TYPES = {"opensource_modified"}
SOURCE_ORIGINAL_TYPES = {"original_creation"}
# 兼容旧常量
SOURCE_CLAWHUB = "clawhub_download"
SOURCE_OPENSOURCE = "opensource_modified"
SOURCE_ORIGINAL = "original_creation"

# ============================================================
# 数据库操作
# ============================================================

def get_db():
    """获取数据库连接"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def compute_hash(content: str) -> str:
    """计算内容的SHA256"""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def compute_file_hash(file_path: Path) -> str:
    """计算文件的SHA256"""
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def parse_skill_md(skill_md_path: Path) -> Tuple[Dict[str, Any], str]:
    """解析SKILL.md的frontmatter和body"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]

    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    frontmatter_text = parts[1].strip()
    body = parts[2].strip()

    metadata = {}
    current_key = None
    current_list = []

    for line in frontmatter_text.split('\n'):
        if line.startswith('  - '):
            if current_key:
                current_list.append(line[4:].strip())
            continue
        if line.startswith('  '):
            if current_key:
                if not isinstance(metadata.get(current_key), list):
                    metadata[current_key] = []
                metadata[current_key].append(line.strip())
            continue
        if ':' in line:
            if current_key and current_list:
                metadata[current_key] = current_list
                current_list = []
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val and val != '|-' and val != '|':
                metadata[key] = val
            else:
                current_key = key

    if current_key and current_list:
        metadata[current_key] = current_list

    return metadata, body

def get_all_skills() -> List[Dict[str, Any]]:
    """获取数据库中所有skill"""
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT s.*,
            (SELECT content_hash FROM versions WHERE skill_id = s.id
             ORDER BY created_at DESC LIMIT 1) as last_hash,
            (SELECT MAX(upload_date) FROM platform_uploads WHERE skill_id = s.id) as last_upload,
            (SELECT GROUP_CONCAT(DISTINCT platform || ':' || upload_status)
             FROM platform_uploads WHERE skill_id = s.id) as upload_history
        FROM skills s
        ORDER BY s.category, s.slug
    """)
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results

def get_skills_with_sources() -> List[Dict[str, Any]]:
    """获取所有有来源信息的skill（非原创）"""
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT s.*,
            (SELECT content_hash FROM versions WHERE skill_id = s.id
             ORDER BY created_at DESC LIMIT 1) as last_hash
        FROM skills s
        WHERE s.source_slug IS NOT NULL AND s.source_slug != ''
        ORDER BY s.source, s.slug
    """)
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results

def update_skill_version(skill_id: int, new_version: str, new_hash: str,
                         changelog: str, file_size: int, line_count: int,
                         changes_summary: str):
    """更新skill版本记录"""
    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()

    # 更新主表
    c.execute("""
        UPDATE skills SET current_version = ?, updated_at = ?, current_status = 'updated'
        WHERE id = ?
    """, (new_version, now, skill_id))

    # 插入版本记录
    c.execute("""
        INSERT INTO versions (skill_id, version, created_at, changelog, content_hash,
                             file_size, line_count, changes_summary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, new_version, now, changelog, new_hash, file_size, line_count, changes_summary))

    # 记录操作
    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (skill_id, 'auto_update', now, 'update_mechanism',
          f'Auto-updated to v{new_version}: {changes_summary}', 'updated'))

    conn.commit()
    conn.close()

def record_upload(skill_id: int, version: str, platform: str, platform_slug: str,
                  status: str, http_status: int = None, error: str = None,
                  visibility: str = None, pricing: str = None):
    """记录上传结果"""
    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO platform_uploads (skill_id, version, platform, platform_slug,
            upload_date, upload_status, http_status, error_message, visibility, pricing_on_platform)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, version, platform, platform_slug, now, status,
          http_status, error, visibility, pricing))

    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (skill_id, f'upload_{platform}', now, 'update_mechanism',
          f'Uploaded {version} to {platform}: {status}', status))

    conn.commit()
    conn.close()

# ============================================================
# 来源检测
# ============================================================

def fetch_url(url: str, timeout: int = 15) -> Optional[str]:
    """安全地获取URL内容"""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read().decode('utf-8', errors='replace')
            return content
    except urllib.error.HTTPError as e:
        return None
    except urllib.error.URLError as e:
        return None
    except Exception as e:
        return None

def find_source_skill_md(slug: str, source_url: str, source_slug: str) -> Optional[Path]:
    """在本地查找原始skill的SKILL.md路径"""
    # 1. 在clawhub下载目录中查找
    if source_slug:
        for category_dir in CLAWHUB_DOWNLOADED_DIR.iterdir():
            if not category_dir.is_dir():
                continue
            skill_dir = category_dir / source_slug
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                return skill_dir / "SKILL.md"

    # 2. 在差异化目录中查找
    if source_slug:
        for category_dir in DIFFERENTIATED_SKILLS_DIR.iterdir():
            if not category_dir.is_dir():
                continue
            skill_dir = category_dir / source_slug
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                return skill_dir / "SKILL.md"

    return None

def fetch_clawhub_skill(source_url: str, source_slug: str) -> Optional[str]:
    """从clawhub获取最新skill内容"""
    # 尝试本地下载的文件
    local_path = find_source_skill_md(source_slug, source_url, source_slug)
    if local_path and local_path.exists():
        return local_path.read_text(encoding='utf-8')

    # 尝试clawhub API
    if source_url:
        match = CLAWHUB_URL_PATTERN.match(source_url)
        if match:
            # 尝试API端点
            api_urls = [
                f"https://mirror-cn.clawhub.com/api/skills/{source_slug}",
                f"https://clawhub.ai/api/skills/{source_slug}",
                source_url,
            ]
            for url in api_urls:
                content = fetch_url(url)
                if content and 'slug' in content.lower():
                    return content

    return None

def fetch_github_skill(source_url: str, source_slug: str) -> Optional[str]:
    """从GitHub获取最新skill内容"""
    if not source_url:
        return None

    # 尝试 raw.githubusercontent.com URL
    raw_match = GITHUB_RAW_PATTERN.match(source_url)
    if raw_match:
        content = fetch_url(source_url)
        if content:
            return content

    # 尝试从 GitHub 仓库 URL 构建 raw URL
    repo_match = GITHUB_REPO_PATTERN.match(source_url)
    if repo_match:
        owner, repo = repo_match.group(1), repo_match.group(2)
        # 常见路径模式
        raw_urls = [
            f"https://raw.githubusercontent.com/{owner}/{repo}/main/skills/{source_slug}/SKILL.md",
            f"https://raw.githubusercontent.com/{owner}/{repo}/main/SKILL.md",
            f"https://raw.githubusercontent.com/{owner}/{repo}/master/skills/{source_slug}/SKILL.md",
            f"https://raw.githubusercontent.com/{owner}/{repo}/master/SKILL.md",
        ]
        for url in raw_urls:
            content = fetch_url(url)
            if content and len(content) > 50:
                return content

    # 查找本地下载
    local_path = find_source_skill_md(source_slug, source_url, source_slug)
    if local_path and local_path.exists():
        return local_path.read_text(encoding='utf-8')

    return None

def check_skill_update(skill: Dict[str, Any]) -> Dict[str, Any]:
    """检查单个skill的来源更新状态"""
    slug = skill['slug']
    source = skill.get('source', '')
    source_slug = skill.get('source_slug', '')
    source_url = skill.get('source_url', '')
    last_hash = skill.get('last_hash', '')
    local_path = skill.get('local_path', '')

    result = {
        'slug': slug,
        'display_name': skill.get('current_display_name', slug),
        'source': source,
        'source_slug': source_slug,
        'source_url': source_url,
        'current_version': skill.get('current_version', '1.0.0'),
        'last_hash': last_hash,
        'status': 'unknown',
        'new_hash': None,
        'changed': False,
        'change_type': None,
        'error': None,
        'local_path': local_path,
    }

    # 原创skill无外部来源，检查本地文件是否变化
    if source in SOURCE_ORIGINAL_TYPES or not source_slug:
        result['status'] = 'no_source'
        result['change_type'] = 'original_creation'
        return result

    # 获取最新源内容
    latest_content = None

    if source in SOURCE_CLAWHUB_TYPES:
        # 对于clawhub来源，直接使用local_path查找原始文件
        # clawhub_download: local_path 指向原始下载
        # clawhub_differentiated: local_path 指向差异化版本，需要通过source_slug找原始
        if source == 'clawhub_download' and local_path:
            skill_md = Path(local_path) / "SKILL.md"
            if not skill_md.exists():
                skill_md = Path(local_path)
            if skill_md.exists() and skill_md.suffix == '.md':
                latest_content = skill_md.read_text(encoding='utf-8')
        else:
            # 通过source_slug在下载目录中查找原始文件
            latest_content = fetch_clawhub_skill(source_url, source_slug)
        result['change_type'] = 'clawhub'
    elif source in SOURCE_OPENSOURCE_TYPES:
        # 开源改造skill：优先尝试GitHub远程检查，回退到本地文件检查
        latest_content = fetch_github_skill(source_url, source_slug)
        if latest_content is None and local_path:
            # GitHub获取失败，使用本地文件检查（检测本地文件是否被修改）
            skill_md = Path(local_path) / "SKILL.md"
            if not skill_md.exists():
                skill_md = Path(local_path)
            if skill_md.exists() and skill_md.suffix == '.md':
                latest_content = skill_md.read_text(encoding='utf-8')
                result['change_type'] = 'local_check'
        else:
            result['change_type'] = 'github'

    if latest_content is None:
        result['status'] = 'fetch_failed'
        result['error'] = f'无法从来源获取内容: source_url={source_url}, source_slug={source_slug}, local_path={local_path}'
        return result

    # 计算hash时使用文件原始字节，与init_baseline.py保持一致
    new_hash = None
    if local_path and (source in SOURCE_CLAWHUB_TYPES or result.get('change_type') == 'local_check'):
        skill_md = Path(local_path) / "SKILL.md"
        if not skill_md.exists():
            skill_md = Path(local_path)
        if skill_md.exists() and skill_md.suffix == '.md':
            new_hash = compute_file_hash(skill_md)
    
    if new_hash is None:
        # 回退到文本hash
        new_hash = compute_hash(latest_content)
    result['new_hash'] = new_hash

    if not last_hash:
        result['status'] = 'no_baseline'
        result['changed'] = False
        return result

    if new_hash == last_hash:
        result['status'] = 'up_to_date'
        result['changed'] = False
    else:
        result['status'] = 'changed'
        result['changed'] = True
        result['latest_content'] = latest_content[:500]  # 预览前500字符

    return result

def check_all_sources(specific_slug: str = None) -> Dict[str, Any]:
    """检查所有skill的来源更新状态"""
    if specific_slug:
        conn = get_db()
        c = conn.cursor()
        c.execute("""
            SELECT s.*,
                (SELECT content_hash FROM versions WHERE skill_id = s.id
                 ORDER BY created_at DESC LIMIT 1) as last_hash
            FROM skills s
            WHERE s.slug = ?
        """, (specific_slug,))
        row = c.fetchone()
        conn.close()
        if not row:
            return {
                'check_time': datetime.now().isoformat(),
                'total_checked': 0,
                'changed': [],
                'up_to_date': [],
                'failed': [],
                'no_source': [],
                'details': [],
                'error': f'Skill not found: {specific_slug}'
            }
        skills = [dict(row)]
    else:
        skills = get_skills_with_sources()

    results = {
        'check_time': datetime.now().isoformat(),
        'total_checked': len(skills),
        'changed': [],
        'up_to_date': [],
        'failed': [],
        'no_source': [],
        'details': []
    }

    for skill in skills:
        result = check_skill_update(skill)
        results['details'].append(result)

        if result['status'] == 'changed':
            results['changed'].append(result['slug'])
        elif result['status'] == 'up_to_date':
            results['up_to_date'].append(result['slug'])
        elif result['status'] == 'no_source':
            results['no_source'].append(result['slug'])
        else:
            results['failed'].append({
                'slug': result['slug'],
                'error': result.get('error', 'Unknown error')
            })

    return results

# ============================================================
# Payload 生成
# ============================================================

def find_skill_md(slug: str) -> Optional[Path]:
    """查找skill的SKILL.md文件"""
    search_dirs = [
        PACKAGED_SKILLS_DIR / slug,
        OPENSOURCE_SKILLS_DIR / slug,
        DIFFERENTIATED_SKILLS_DIR,
        ENTERPRISE_UPLOAD_DIR / slug,
    ]

    for d in search_dirs:
        if d.is_dir():
            md = d / "SKILL.md"
            if md.exists():
                return md

    # 在差异化目录中按分类查找
    if DIFFERENTIATED_SKILLS_DIR.is_dir():
        for cat_dir in DIFFERENTIATED_SKILLS_DIR.iterdir():
            if cat_dir.is_dir():
                md = cat_dir / slug / "SKILL.md"
                if md.exists():
                    return md

    return None

def generate_payload(slug: str, version: str = None, is_paid: bool = False,
                     price: str = None, changelog: str = None) -> Dict[str, Any]:
    """生成上传payload"""
    skill_md = find_skill_md(slug)
    if not skill_md:
        return {'error': f'SKILL.md not found for: {slug}'}

    metadata, body = parse_skill_md(skill_md)

    # 提取字段
    payload = {
        'slug': slug,
        'version': version or metadata.get('version', '1.0.0'),
        'displayName': metadata.get('displayName', slug),
        'summary': metadata.get('summary', ''),
        'description': metadata.get('description', metadata.get('summary', '')),
        'changelog': changelog or f'版本更新: {version or metadata.get("version", "1.0.0")}',
        'tags': metadata.get('tags', []) if isinstance(metadata.get('tags'), list) else [metadata.get('tags', '')],
        'iconUrl': None,
        'categoryIds': [],
    }

    # 付费版本添加定价
    if is_paid:
        payload['pricing'] = {
            'billingType': 'per_call',
            'pricingMode': 'unified',
            'pricePerCall': price or DEFAULT_PAID_PRICE,
            'currency': DEFAULT_CURRENCY,
        }

    return payload

def save_payload(slug: str, payload: Dict[str, Any], is_paid: bool):
    """保存payload到文件"""
    PAYLOADS_DIR.mkdir(parents=True, exist_ok=True)

    suffix = '-paid' if is_paid else '-free'
    filename = f"{slug}{suffix}.json"
    filepath = PAYLOADS_DIR / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    return filepath

def generate_dual_payloads(slug: str, new_version: str = None,
                           changelog: str = None, price: str = None) -> Dict[str, Any]:
    """生成免费和付费双版本payload"""
    results = {
        'slug': slug,
        'free_payload': None,
        'paid_payload': None,
        'free_path': None,
        'paid_path': None,
    }

    # 免费版
    free_payload = generate_payload(slug, version=new_version, is_paid=False, changelog=changelog)
    if 'error' not in free_payload:
        free_path = save_payload(slug, free_payload, is_paid=False)
        results['free_payload'] = free_payload
        results['free_path'] = str(free_path)

    # 付费版
    paid_payload = generate_payload(slug, version=new_version, is_paid=True, price=price, changelog=changelog)
    if 'error' not in paid_payload:
        paid_path = save_payload(slug, paid_payload, is_paid=True)
        results['paid_payload'] = paid_payload
        results['paid_path'] = str(paid_path)

    return results

# ============================================================
# 平台同步
# ============================================================

def upload_free_via_cli(slug: str, skill_md_path: Path,
                        max_retries: int = 3) -> Dict[str, Any]:
    """通过CLI上传免费版本 (v1.1: 增加指数退避重试 + 完整保存响应 + 区分错误类型)

    重试策略:
        - 可重试: subprocess超时, 非零退出码(非业务错误), 网络错误
        - 不可重试: protected slug, slug冲突, 未授权, 已存在(业务错误)
        - 退避间隔: 1s, 2s, 4s (指数退避)
    """
    result = {'slug': slug, 'platform': 'skillhub_free', 'method': 'cli',
              'attempts': [], 'max_retries': max_retries}

    # 不可重试的错误模式(基于skillhub CLI实际输出)
    NON_RETRYABLE_PATTERNS = [
        'protected', 'already exists', 'slug conflict',
        'unauthorized', 'forbidden', 'authentication failed',
        'invalid token', 'permission denied',
    ]

    skill_dir = skill_md_path.parent
    cmd = ['bash', SKILLHUB_RUNNER, 'publish', str(skill_dir)]

    for attempt in range(1, max_retries + 1):
        attempt_info = {'attempt': attempt, 'started_at': datetime.now().isoformat()}

        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            # 完整保存输出, 不截断
            attempt_info['exit_code'] = proc.returncode
            attempt_info['stdout'] = proc.stdout  # 完整保存, 不截断
            attempt_info['stderr'] = proc.stderr  # 完整保存, 不截断
            attempt_info['finished_at'] = datetime.now().isoformat()

            if proc.returncode == 0:
                # 成功
                attempt_info['status'] = 'success'
                result['attempts'].append(attempt_info)
                result['status'] = 'success'
                result['exit_code'] = 0
                result['stdout'] = proc.stdout
                result['stderr'] = proc.stderr
                result['total_attempts'] = attempt
                return result

            # 失败: 判断是否可重试
            stderr_lower = proc.stderr.lower()
            stdout_lower = proc.stdout.lower()
            combined = stderr_lower + stdout_lower

            is_non_retryable = any(p in combined for p in NON_RETRYABLE_PATTERNS)

            if is_non_retryable:
                attempt_info['status'] = 'failed_non_retryable'
                attempt_info['reason'] = '业务错误(protected/conflict/auth), 不重试'
                result['attempts'].append(attempt_info)
                result['status'] = 'failed_non_retryable'
                result['exit_code'] = proc.returncode
                result['stdout'] = proc.stdout
                result['stderr'] = proc.stderr
                result['total_attempts'] = attempt
                result['error'] = f'不可重试错误: {[p for p in NON_RETRYABLE_PATTERNS if p in combined]}'
                return result
            else:
                attempt_info['status'] = 'failed_retryable'
                attempt_info['reason'] = f'非零退出码({proc.returncode}), 可重试'

        except subprocess.TimeoutExpired as e:
            attempt_info['status'] = 'failed_retryable'
            attempt_info['reason'] = f'超时(60s), 可重试'
            attempt_info['error'] = str(e)
            attempt_info['finished_at'] = datetime.now().isoformat()

        except Exception as e:
            attempt_info['status'] = 'failed_retryable'
            attempt_info['reason'] = f'异常: {type(e).__name__}, 可重试'
            attempt_info['error'] = str(e)
            attempt_info['finished_at'] = datetime.now().isoformat()

        result['attempts'].append(attempt_info)

        # 如果不是最后一次, 等待退避时间
        if attempt < max_retries:
            backoff = 2 ** (attempt - 1)  # 1s, 2s, 4s
            time.sleep(backoff)

    # 所有重试都失败
    result['status'] = 'failed'
    result['total_attempts'] = max_retries
    result['error'] = f'重试{max_retries}次后仍失败'
    return result

def upload_paid_via_api(slug: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """通过企业API上传付费版本"""
    result = {'slug': slug, 'platform': 'skillhub_paid', 'method': 'enterprise_api'}

    # 注意: 企业API需要session cookies认证
    # 这里生成payload文件，实际上传由AI通过浏览器MCP完成
    payload_path = PAYLOADS_DIR / f"{slug}-paid.json"
    result['payload_path'] = str(payload_path)
    result['payload'] = payload
    result['status'] = 'payload_ready'
    result['note'] = '企业API上传需要浏览器session cookies认证，请通过browser_evaluate执行上传'

    return result

def sync_skill_to_platform(slug: str, skill_id: int, new_version: str,
                           changelog: str = None,
                           skip_quality_gate: bool = False,
                           skip_l2: bool = False,
                           skip_l3: bool = False) -> Dict[str, Any]:
    """同步单个skill到平台（免费+付费）

    v1.1: 增加质量门禁检查(L1), 上传前强制调用quality_gate
          skip_quality_gate=True可跳过(仅用于调试, 生产环境禁止)
    v1.2: 集成三层验证体系
          L1 静态检查 (quality_gate.py, <1秒) - 格式合规性
          L2 LLM模拟验证 (llm_validator.py, ~30秒) - 内容质量+TRACE评分
          L3 真实agent试运行 (agent_trial.py, ~2分钟) - 真实可运行性
          skip_l2/skip_l3=True可跳过对应层级(批量场景使用)
          L3需AI预先执行, 此处只检查L3最终报告是否通过
    """
    results = {
        'slug': slug,
        'version': new_version,
        'free_upload': None,
        'paid_upload': None,
        'validation': {
            'l1_static': None,
            'l2_llm': None,
            'l3_trial': None,
        },
    }

    # 查找SKILL.md
    skill_md = find_skill_md(slug)
    if not skill_md:
        results['error'] = f'SKILL.md not found for: {slug}'
        return results

    # === L1: 质量门禁检查 (静态格式检查, <1秒) ===
    if not skip_quality_gate:
        from quality_gate import run_quality_gate
        gate_result = run_quality_gate(skill_md)
        results['validation']['l1_static'] = {
            'passed': gate_result.get('overall_passed', False),
            'score': f"{gate_result.get('passed_checks', 0)}/{gate_result.get('total_checks', 0)}",
            'failed_checks': [c['name'] for c in gate_result.get('checks', []) if not c['passed']],
        }

        if not gate_result.get('overall_passed'):
            # L1未通过, 阻止上传
            results['status'] = 'blocked_by_l1_quality_gate'
            results['error'] = f"L1质量门禁未通过: {gate_result.get('failed_checks', 0)}/{gate_result.get('total_checks', 0)}项失败"
            results['failed_checks'] = results['validation']['l1_static']['failed_checks']
            # 记录被阻止的操作到DB
            record_upload(skill_id, new_version, 'skillhub', slug,
                          'blocked_by_l1_quality_gate',
                          http_status=None,
                          error=results['error'],
                          visibility='public')
            print(f"✗ L1质量门禁阻止上传: {slug}")
            for c in gate_result.get('checks', []):
                if not c['passed']:
                    print(f"  [{c['severity']}] {c['name']}: {c['details']}")
            return results
        else:
            print(f"✓ L1质量门禁通过: {slug} ({gate_result.get('passed_checks', 0)}/{gate_result.get('total_checks', 0)})")
    else:
        results['validation']['l1_static'] = {'passed': None, 'score': 'skipped', 'note': 'skip_quality_gate=True'}
        print(f"⚠ L1质量门禁已跳过: {slug}")

    # === L2: LLM模拟验证 (内容质量+TRACE评分, ~30秒) ===
    if not skip_l2:
        import json as _json
        from llm_validator import find_skill_md as _find_md, run_l2_validation
        from trace_llm_scorer import read_skill_md as _read_md, static_check as _static_check, calculate_static_scores as _calc_scores

        # 生成L2验证报告(静态部分)
        l2_report_path = SKILL_REGISTRY_DIR / f'l2_validation_report_{slug}.json'
        l2_result = run_l2_validation(slug, output_json=True, output_file=str(l2_report_path))

        if l2_result.get('status') == 'error':
            results['validation']['l2_llm'] = {'passed': False, 'error': l2_result.get('error', 'L2验证失败')}
            results['status'] = 'blocked_by_l2_validation_error'
            results['error'] = f"L2验证执行错误: {l2_result.get('error')}"
            record_upload(skill_id, new_version, 'skillhub', slug,
                          'blocked_by_l2_validation_error',
                          http_status=None, error=results['error'], visibility='public')
            print(f"✗ L2验证执行错误: {slug} - {l2_result.get('error')}")
            return results

        # 检查L2最终报告是否存在(AI已执行评估并import)
        l2_final_path = SKILL_REGISTRY_DIR / f'l2_final_report_{slug}.json'
        if not l2_final_path.exists():
            # L2最终报告不存在, 说明AI尚未执行L2评估
            results['validation']['l2_llm'] = {
                'passed': None,
                'status': 'pending_ai_eval',
                'report_path': str(l2_report_path),
                'note': 'L2验证报告已生成, 需AI执行评估并运行: python llm_validator.py import ' + slug + ' <评估结果.json>'
            }
            results['status'] = 'blocked_by_l2_pending'
            results['error'] = f"L2验证待AI评估: 报告已生成在 {l2_report_path}, 请AI执行评估后重试"
            record_upload(skill_id, new_version, 'skillhub', slug,
                          'blocked_by_l2_pending',
                          http_status=None, error=results['error'], visibility='public')
            print(f"⚠ L2验证待AI评估: {slug}")
            print(f"  报告路径: {l2_report_path}")
            print(f"  下一步: AI读取报告执行评估, 然后运行 python llm_validator.py import {slug} <评估结果.json>")
            return results

        # 读取L2最终报告
        with open(l2_final_path, 'r', encoding='utf-8') as f:
            l2_final = _json.load(f)

        l2_passed = l2_final.get('l2_passed', False)
        trace_total = l2_final.get('trace_total', 0)
        results['validation']['l2_llm'] = {
            'passed': l2_passed,
            'trace_total': trace_total,
            'trace_grade': l2_final.get('trace_grade', 'D'),
            'checks_summary': l2_final.get('checks_summary', {}),
        }

        if not l2_passed:
            results['status'] = 'blocked_by_l2_validation'
            results['error'] = f"L2验证未通过: TRACE总分{trace_total}/50 (阈值35), 等级{results['validation']['l2_llm']['trace_grade']}"
            record_upload(skill_id, new_version, 'skillhub', slug,
                          'blocked_by_l2_validation',
                          http_status=None, error=results['error'], visibility='public')
            print(f"✗ L2验证未通过: {slug} (TRACE {trace_total}/50, 等级{results['validation']['l2_llm']['trace_grade']})")
            return results
        else:
            print(f"✓ L2验证通过: {slug} (TRACE {trace_total}/50, 等级{results['validation']['l2_llm']['trace_grade']})")
    else:
        results['validation']['l2_llm'] = {'passed': None, 'score': 'skipped', 'note': 'skip_l2=True'}
        print(f"⚠ L2验证已跳过: {slug}")

    # === L3: 真实agent试运行 (~2分钟, 需AI预先执行) ===
    if not skip_l3:
        import json as _json2
        l3_final_path = SKILL_REGISTRY_DIR / f'l3_final_report_{slug}.json'

        if not l3_final_path.exists():
            # L3最终报告不存在, 说明AI尚未执行L3试运行
            results['validation']['l3_trial'] = {
                'passed': None,
                'status': 'pending_ai_trial',
                'note': 'L3试运行需AI预先执行: python agent_trial.py trial ' + slug + ' → AI执行 → python agent_trial.py import ' + slug + ' <结果.json>'
            }
            results['status'] = 'blocked_by_l3_pending'
            results['error'] = f"L3试运行待AI执行: 请先运行 python agent_trial.py trial {slug}, AI执行6个用例后import, 再重试上传"
            record_upload(skill_id, new_version, 'skillhub', slug,
                          'blocked_by_l3_pending',
                          http_status=None, error=results['error'], visibility='public')
            print(f"⚠ L3试运行待AI执行: {slug}")
            print(f"  下一步: python agent_trial.py trial {slug} → AI执行6用例 → python agent_trial.py import {slug} <结果.json>")
            return results

        # 读取L3最终报告
        with open(l3_final_path, 'r', encoding='utf-8') as f:
            l3_final = _json2.load(f)

        l3_passed = l3_final.get('l3_passed', False)
        l3_score = l3_final.get('l3_score', 0)
        results['validation']['l3_trial'] = {
            'passed': l3_passed,
            'score': l3_score,
            'grade': l3_final.get('l3_grade', 'D'),
            'checks_summary': l3_final.get('checks_summary', {}),
        }

        if not l3_passed:
            results['status'] = 'blocked_by_l3_trial'
            results['error'] = f"L3试运行未通过: 评分{l3_score}/100, 等级{results['validation']['l3_trial']['grade']}"
            record_upload(skill_id, new_version, 'skillhub', slug,
                          'blocked_by_l3_trial',
                          http_status=None, error=results['error'], visibility='public')
            print(f"✗ L3试运行未通过: {slug} (评分{l3_score}/100, 等级{results['validation']['l3_trial']['grade']})")
            return results
        else:
            print(f"✓ L3试运行通过: {slug} (评分{l3_score}/100, 等级{results['validation']['l3_trial']['grade']})")
    else:
        results['validation']['l3_trial'] = {'passed': None, 'score': 'skipped', 'note': 'skip_l3=True'}
        print(f"⚠ L3试运行已跳过: {slug}")

    # === 三层验证全部通过, 开始上传 ===
    print(f"✓ 三层验证全部通过: {slug}, 开始上传...")

    # 生成双版本payload
    dual = generate_dual_payloads(slug, new_version, changelog)
    results['payloads'] = dual

    # 上传免费版
    if dual.get('free_path'):
        free_result = upload_free_via_cli(slug, skill_md)
        results['free_upload'] = free_result
        record_upload(skill_id, new_version, 'skillhub', slug,
                      free_result['status'],
                      http_status=free_result.get('exit_code'),
                      error=free_result.get('error'),
                      visibility='public')

    # 准备付费版上传
    if dual.get('paid_payload'):
        paid_result = upload_paid_via_api(slug, dual['paid_payload'])
        results['paid_upload'] = paid_result

    return results

# ============================================================
# 报告生成
# ============================================================

def generate_update_report() -> str:
    """生成更新报告（给AI分析用）"""
    check_result = check_all_sources()

    report_lines = [
        f"# Skill 更新检查报告",
        f"",
        f"检查时间: {check_result['check_time']}",
        f"总检查数: {check_result['total_checked']}",
        f"已变更: {len(check_result['changed'])}",
        f"最新版: {len(check_result['up_to_date'])}",
        f"无来源: {len(check_result['no_source'])}",
        f"检查失败: {len(check_result['failed'])}",
        f"",
        f"## 变更详情",
        f"",
    ]

    for detail in check_result['details']:
        if detail['status'] == 'changed':
            report_lines.append(f"### {detail['slug']} ({detail.get('display_name', '')})")
            report_lines.append(f"- 来源类型: {detail.get('change_type', 'unknown')}")
            report_lines.append(f"- 来源URL: {detail.get('source_url', 'N/A')}")
            report_lines.append(f"- 当前版本: {detail.get('current_version', '1.0.0')}")
            report_lines.append(f"- 状态: **已变更**")
            report_lines.append(f"- 旧hash: {detail.get('last_hash', 'N/A')[:16]}...")
            report_lines.append(f"- 新hash: {detail.get('new_hash', 'N/A')[:16]}...")
            if detail.get('latest_content'):
                report_lines.append(f"- 内容预览:")
                report_lines.append(f"```")
                report_lines.append(detail['latest_content'][:300])
                report_lines.append(f"```")
            report_lines.append("")

    if check_result['failed']:
        report_lines.append("## 检查失败")
        report_lines.append("")
        for fail in check_result['failed']:
            report_lines.append(f"- {fail['slug']}: {fail['error']}")
        report_lines.append("")

    report_lines.append("## 待处理")
    report_lines.append("")
    report_lines.append("AI需要对以下已变更的skill进行分析和更新:")
    for slug in check_result['changed']:
        report_lines.append(f"1. `{slug}` - 分析变更内容，重新应用差异化改造，更新SKILL.md")
    report_lines.append("")
    report_lines.append("完成分析更新后，运行:")
    report_lines.append("```bash")
    report_lines.append(f"python update_mechanism.py upload-all")
    report_lines.append("```")

    return "\n".join(report_lines)

def generate_status_report() -> str:
    """生成所有skill的状态报告"""
    skills = get_all_skills()

    lines = [
        f"# Skill Registry 状态报告",
        f"",
        f"生成时间: {datetime.now().isoformat()}",
        f"总Skill数: {len(skills)}",
        f"",
        f"| # | Slug | 版本 | 来源 | 状态 | 上传历史 | 路径 |",
        f"|---|------|------|------|------|---------|------|",
    ]

    for i, skill in enumerate(skills, 1):
        slug = skill.get('slug', '')
        version = skill.get('current_version', '')
        source = skill.get('source', '')
        status = skill.get('current_status', '')
        upload_history = skill.get('upload_history', '') or '未上传'
        path = skill.get('local_path', '')
        lines.append(f"| {i} | {slug} | {version} | {source} | {status} | {upload_history} | {path} |")

    return "\n".join(lines)

# ============================================================
# 主入口
# ============================================================

def cmd_check(args):
    """检查来源更新"""
    print("正在检查所有skill的来源更新状态...")
    results = check_all_sources(args.slug)

    print(f"\n检查完成:")
    print(f"  总计: {results['total_checked']}")
    print(f"  已变更: {len(results['changed'])}")
    print(f"  最新版: {len(results['up_to_date'])}")
    print(f"  无来源: {len(results['no_source'])}")
    print(f"  检查失败: {len(results['failed'])}")

    if results['changed']:
        print(f"\n已变更的skill:")
        for slug in results['changed']:
            print(f"  - {slug}")

    if results['failed']:
        print(f"\n检查失败的skill:")
        for fail in results['failed']:
            print(f"  - {fail['slug']}: {fail['error']}")

    # 保存详细报告
    report_path = SKILLS_ROOT / "skill-registry" / "update-report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n详细报告已保存: {report_path}")

    return results

def cmd_generate(args):
    """生成payload"""
    print(f"生成 {args.slug} 的双版本payload...")

    new_version = args.version
    if not new_version:
        # 自动递增版本号
        skill_md = find_skill_md(args.slug)
        if skill_md:
            metadata, _ = parse_skill_md(skill_md)
            current = metadata.get('version', '1.0.0')
            parts = current.split('.')
            if len(parts) >= 3:
                parts[-1] = str(int(parts[-1]) + 1)
                new_version = '.'.join(parts)
            else:
                new_version = current + '.1'

    results = generate_dual_payloads(args.slug, new_version, args.changelog, args.price)

    print(f"\nPayload生成完成:")
    print(f"  Slug: {results['slug']}")
    print(f"  版本: {new_version}")
    if results.get('free_path'):
        print(f"  免费版: {results['free_path']}")
    if results.get('paid_path'):
        print(f"  付费版: {results['paid_path']}")

    return results

def cmd_upload(args):
    """上传skill到平台"""
    print(f"上传 {args.slug} 到SkillHub...")

    # 获取skill_id
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, current_version FROM skills WHERE slug = ?", (args.slug,))
    row = c.fetchone()
    conn.close()

    if not row:
        print(f"错误: skill {args.slug} 未在数据库中注册")
        return

    skill_id = row['id']
    version = args.version or row['current_version']

    result = sync_skill_to_platform(args.slug, skill_id, version, args.changelog)
    print(f"\n上传结果:")
    print(json.dumps(result, ensure_ascii=False, indent=2))

def cmd_upload_all(args):
    """上传所有已变更的skill"""
    print("检查变更并上传所有已更新的skill...")

    check_result = check_all_sources()
    changed_slugs = check_result['changed']

    if not changed_slugs:
        print("没有检测到变更的skill，无需上传。")
        return

    print(f"\n检测到 {len(changed_slugs)} 个已变更skill:")
    for slug in changed_slugs:
        print(f"  - {slug}")

    print(f"\n开始逐个上传...")

    upload_results = []
    for slug in changed_slugs:
        print(f"\n处理: {slug}")

        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT id, current_version FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        conn.close()

        if not row:
            print(f"  跳过: 未在数据库中注册")
            continue

        result = sync_skill_to_platform(slug, row['id'], row['current_version'])
        upload_results.append(result)

        if result.get('free_upload', {}).get('status') == 'success':
            print(f"  免费版: 上传成功")
        else:
            print(f"  免费版: {result.get('free_upload', {}).get('status', '未知')}")

        if result.get('paid_upload', {}).get('status') == 'payload_ready':
            print(f"  付费版: payload已准备，等待API上传")

    # 保存上传结果
    results_path = SKILLS_ROOT / "skill-registry" / "upload-results.json"
    with open(results_path, 'w', encoding='utf-8') as f:
        json.dump(upload_results, f, ensure_ascii=False, indent=2)
    print(f"\n上传结果已保存: {results_path}")

def cmd_status(args):
    """显示状态"""
    report = generate_status_report()
    print(report)

def cmd_report(args):
    """生成更新报告"""
    report = generate_update_report()
    report_path = SKILLS_ROOT / "skill-registry" / "update-report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(report)
    print(f"\n报告已保存: {report_path}")

def main():
    parser = argparse.ArgumentParser(
        description='Skill 自动更新机制 - 检测来源更新、生成双版本、同步到平台',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python update_mechanism.py check              # 检查所有来源更新
  python update_mechanism.py check --slug xxx   # 检查指定skill
  python update_mechanism.py generate xxx       # 生成双版本payload
  python update_mechanism.py upload xxx         # 上传指定skill
  python update_mechanism.py upload-all         # 上传所有已变更skill
  python update_mechanism.py status             # 显示所有skill状态
  python update_mechanism.py report             # 生成更新报告
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # check
    p_check = subparsers.add_parser('check', help='检查来源更新状态')
    p_check.add_argument('--slug', help='指定skill slug')

    # generate
    p_gen = subparsers.add_parser('generate', help='生成双版本payload')
    p_gen.add_argument('slug', help='skill slug')
    p_gen.add_argument('--version', help='新版本号')
    p_gen.add_argument('--changelog', help='变更说明')
    p_gen.add_argument('--price', help='付费价格', default=DEFAULT_PAID_PRICE)

    # upload
    p_upload = subparsers.add_parser('upload', help='上传skill到平台')
    p_upload.add_argument('slug', help='skill slug')
    p_upload.add_argument('--version', help='版本号')
    p_upload.add_argument('--changelog', help='变更说明')

    # upload-all
    subparsers.add_parser('upload-all', help='上传所有已变更skill')

    # status
    subparsers.add_parser('status', help='显示所有skill状态')

    # report
    subparsers.add_parser('report', help='生成更新报告')

    args = parser.parse_args()

    if args.command == 'check':
        cmd_check(args)
    elif args.command == 'generate':
        cmd_generate(args)
    elif args.command == 'upload':
        cmd_upload(args)
    elif args.command == 'upload-all':
        cmd_upload_all(args)
    elif args.command == 'status':
        cmd_status(args)
    elif args.command == 'report':
        cmd_report(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
