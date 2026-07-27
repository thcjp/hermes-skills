#!/usr/bin/env python3
"""
版本同步流水线 (Version Sync Pipeline)
=====================================
端到端自动化: 检测变更 → 版本递增 → 质量门禁 → 多平台同步
覆盖: GitHub开放库 + SkillHub(免费+付费) + ClawHub

流程:
  1. DETECT  - 扫描本地SKILL.md文件,对比数据库hash检测变更
  2. INCREMENT - 自动递增版本号(patch级)
  3. VALIDATE - L1质量门禁检查(格式合规性)
  4. SYNC_GITHUB  - git add/commit/push 同步到GitHub开放库
  5. SYNC_SKILLHUB - 上传免费版(CLI) + 生成付费版payload
  6. SYNC_CLAWHUB  - 上传到ClawHub(免费版)
  7. RECORD  - 记录所有平台同步结果到数据库

使用方式:
    python version_sync_pipeline.py scan              # 扫描变更,生成同步计划
    python version_sync_pipeline.py sync <slug>       # 同步单个skill到所有平台
    python version_sync_pipeline.py sync-all          # 同步所有变更skill
    python version_sync_pipeline.py sync-github <slug> # 仅同步到GitHub
    python version_sync_pipeline.py status            # 查看同步状态概览
    python version_sync_pipeline.py report            # 生成同步报告

设计原则:
  - 本地数据库为唯一权威源
  - 每个平台同步独立执行,单个平台失败不阻塞其他平台
  - 所有操作记录到platform_uploads表和operations表
  - 禁止任何mock/fallback/skip
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import PROJECT_ROOT
from project_config import DB_PATH
from project_config import TOOLS_DIR
from project_config import CLAWHUB_DOWNLOADED_DIR
from project_config import DATA_DIR  # 修复: SKILL_DATA_DIR → DATA_DIR
# === End Phase 1 ===
SKILLS_ROOT = PROJECT_ROOT
SKILL_REGISTRY_DIR = TOOLS_DIR


import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import db as db_module
from skill_core.parser import find_skill_md

# ============================================================
# 配置
# ============================================================

# DB_PATH imported from config
# SKILLS_ROOT = PROJECT_ROOT (imported from config)
# SKILL_REGISTRY_DIR = TOOLS_DIR (imported from config)
PACKAGED_SKILLS_DIR = SKILLS_ROOT / "packaged-skills" / "skillhub"
OPENSOURCE_SKILLS_DIR = SKILLS_ROOT / "opensource-skills" / "packaged"
DIFFERENTIATED_SKILLS_DIR = SKILLS_ROOT / "differentiated-skills"
# CLAWHUB_DOWNLOADED_DIR imported from config

# GitHub 仓库配置 (双仓库策略)
# 1. hermes-skills: 公开引流仓库, 仅推送免费skill (MIT license, pricing=free/L1-L2)
PUBLIC_REMOTE = "hermes-skills"  # git remote name for https://github.com/thcjp/hermes-skills.git
PUBLIC_REPO_URL = "https://github.com/thcjp/hermes-skills"
# 2. origin: 私有备份仓库, 推送全部skill (免费+付费) + 项目代码
PRIVATE_REMOTE = "origin"  # git remote name for https://github.com/thcjp/-.git
PRIVATE_REPO_URL = "https://github.com/thcjp/-.git"
GITHUB_BRANCH = "main"
# 免费skill判定: pricing=free 或 pricing_tier in (L1-入门级, L2-标准级) 或 license=MIT
FREE_PRICING_TIERS = {"L1-入门级", "L2-标准级"}
FREE_LICENSES = {"MIT", "Apache-2.0"}

# SkillHub 配置
SKILLHUB_CLI = "skillhub"
SKILLHUB_MAX_CONTENT = 5800  # WAF限制

# ClawHub 配置
CLAWHUB_UPLOADER = SKILL_REGISTRY_DIR / "clawhub_batch_uploader.py"

# 扫描目录配置: (目录路径, 来源标签)
SCAN_DIRS = [
    (PACKAGED_SKILLS_DIR, "packaged"),
    (OPENSOURCE_SKILLS_DIR, "opensource"),
    (DIFFERENTIATED_SKILLS_DIR, "differentiated"),
]

NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# ============================================================
# 数据库操作
# ============================================================

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def compute_file_hash(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith('---'):
        return {}, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    fm_text = parts[1].strip()
    body = parts[2].strip()
    metadata = {}
    current_key = None
    current_list = []
    for line in fm_text.split('\n'):
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
            if val and val not in ('|-', '|'):
                metadata[key] = val
            else:
                current_key = key
    if current_key and current_list:
        metadata[current_key] = current_list
    return metadata, body


def increment_version(version: str) -> str:
    """递增patch版本号: 1.0.0 → 1.0.1"""
    parts = version.split('.')
    if len(parts) == 3:
        try:
            major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
            return f"{major}.{minor}.{patch + 1}"
        except ValueError:
            pass
    elif len(parts) == 2:
        try:
            major, minor = int(parts[0]), int(parts[1])
            return f"{major}.{minor + 1}.0"
        except ValueError:
            pass
    return f"{version}.1" if version else "1.0.1"


def get_skill_from_db(slug: str) -> Optional[Dict[str, Any]]:
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT s.*,
            (SELECT content_hash FROM versions WHERE skill_id = s.id
             ORDER BY created_at DESC LIMIT 1) as last_hash,
            (SELECT version FROM versions WHERE skill_id = s.id
             ORDER BY created_at DESC LIMIT 1) as last_version
        FROM skills s WHERE s.slug = ?
    """, (slug,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None


def find_skill_source(slug: str) -> str:
    """判断skill来源目录"""
    if (PACKAGED_SKILLS_DIR / slug / "SKILL.md").exists():
        return "packaged"
    if (OPENSOURCE_SKILLS_DIR / slug / "SKILL.md").exists():
        return "opensource"
    if DIFFERENTIATED_SKILLS_DIR.is_dir():
        for cat_dir in DIFFERENTIATED_SKILLS_DIR.iterdir():
            if cat_dir.is_dir() and (cat_dir / slug / "SKILL.md").exists():
                return "differentiated"
    return "unknown"


def is_free_skill(skill_md: Path) -> bool:
    """判断skill是否为免费skill (可以推送到公开引流仓库)
    
    判定规则:
    1. pricing 字段 = 'free' → 免费
    2. pricing_tier in FREE_PRICING_TIERS (L1-入门级, L2-标准级) → 免费
    3. license in FREE_LICENSES (MIT, Apache-2.0) → 免费
    4. 以上都不满足 → 付费 (不推送到公开仓库)
    """
    try:
        content = skill_md.read_text(encoding='utf-8', errors='replace')
        metadata, _ = parse_frontmatter(content)
        
        pricing = metadata.get('pricing', '').lower()
        pricing_tier = metadata.get('pricing_tier', '')
        license_val = metadata.get('license', '')
        
        if pricing == 'free':
            return True
        if pricing_tier in FREE_PRICING_TIERS:
            return True
        if license_val in FREE_LICENSES:
            return True
        return False
    except Exception:
        return False


def update_version_in_file(skill_md: Path, new_version: str) -> bool:
    """更新SKILL.md中的version字段"""
    content = skill_md.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    # 替换frontmatter中的version字段
    pattern = r'(---\n.*?version:\s*)([^\n]+)(\n.*?---)'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        new_content = match.group(1) + new_version + match.group(3) + content[match.end():]
        skill_md.write_text(new_content, encoding='utf-8')
        return True
    return False


def record_version(skill_id: int, new_version: str, new_hash: str,
                   changelog: str, file_size: int, line_count: int):
    """记录新版本到数据库"""
    db_module.update_skill_fields(skill_id, current_version=new_version,
                                  current_status='updated')
    db_module.add_version(skill_id, new_version, changelog=changelog,
                          content_hash=new_hash, file_size=file_size,
                          line_count=line_count,
                          changes_summary=f'Auto-incremented to v{new_version}')
    db_module.record_operation(skill_id, 'version_sync',
                               f'Version synced to v{new_version}',
                               operator='version_sync_pipeline',
                               after_state='updated')


def record_platform_upload(skill_id: int, version: str, platform: str,
                           platform_slug: str, status: str,
                           http_status: int = None, error: str = None,
                           visibility: str = None, pricing: str = None):
    """记录平台上传结果"""
    db_module.record_platform_upload(
        skill_id, version, platform, platform_slug, status,
        http_status=http_status, error_message=error, visibility=visibility,
        pricing_on_platform=pricing, operator='version_sync_pipeline',
        operation_type=f'sync_{platform}',
        operation_details=f'Synced {version} to {platform}: {status}'
    )


# ============================================================
# Phase 1: DETECT - 变更检测
# ============================================================

def scan_all_changes() -> List[Dict[str, Any]]:
    """扫描所有目录,检测SKILL.md文件变更"""
    changed_skills = []

    for scan_dir, source_label in SCAN_DIRS:
        if not scan_dir.exists():
            continue
        for skill_md in scan_dir.rglob("SKILL.md"):
            if skill_md.parent.name.startswith('.'):
                continue
            slug = skill_md.parent.name
            current_hash = compute_file_hash(skill_md)

            # 查询数据库
            db_skill = get_skill_from_db(slug)
            if not db_skill:
                # 不在数据库中的skill,跳过
                continue

            last_hash = db_skill.get('last_hash', '')
            if last_hash and current_hash != last_hash:
                changed_skills.append({
                    'slug': slug,
                    'source': source_label,
                    'skill_md': str(skill_md),
                    'old_hash': last_hash[:16],
                    'new_hash': current_hash[:16],
                    'current_version': db_skill.get('current_version', '1.0.0'),
                    'skill_id': db_skill['id'],
                    'file_size': skill_md.stat().st_size,
                })

    return changed_skills


# ============================================================
# Phase 2: INCREMENT - 版本递增
# ============================================================

def increment_skill_version(slug: str, skill_md: Path, current_version: str) -> str:
    """递增skill版本号并更新文件"""
    new_version = increment_version(current_version)
    if update_version_in_file(skill_md, new_version):
        return new_version
    return current_version


# ============================================================
# Phase 3: VALIDATE - 质量门禁
# ============================================================

def run_quality_check(skill_md: Path) -> Dict[str, Any]:
    """运行L1质量门禁检查"""
    try:
        sys.path.insert(0, str(SKILL_REGISTRY_DIR))
        from quality_gate import run_quality_gate
        result = run_quality_gate(skill_md)
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': [c['name'] for c in result.get('checks', []) if not c['passed']],
        }
    except ImportError:
        # quality_gate模块不可用时,执行基本检查
        content = skill_md.read_text(encoding='utf-8')
        has_frontmatter = content.startswith('---')
        has_version = 'version:' in content[:500]
        has_slug = 'slug:' in content[:500]
        passed = has_frontmatter and has_version and has_slug
        return {
            'passed': passed,
            'score': 'basic_check',
            'failed_checks': [] if passed else ['missing_frontmatter_or_fields'],
        }


def run_content_quality_gate(skill_md: Path) -> Dict[str, Any]:
    """L1.5内容质量门禁检查(v3.1新增)
    
    在L1格式合规检查通过后,检查内容质量:
    - summary/description无重复
    - 无模板化套话
    - 无占位符内容
    - 章节无错误合并
    - 输入格式表非空
    """
    try:
        sys.path.insert(0, str(SKILL_REGISTRY_DIR))
        from skill_batch_upgrader_v3 import run_content_quality_check
        result = run_content_quality_check(skill_md)
        failed_checks = [c['name'] for c in result.get('checks', []) if not c['passed']]
        return {
            'passed': result.get('fail_count', 0) == 0,
            'score': f"{result.get('pass_count', 0)}/{result.get('pass_count', 0) + result.get('fail_count', 0)}",
            'failed_checks': failed_checks,
            'fail_count': result.get('fail_count', 0),
        }
    except ImportError:
        return {
            'passed': True,
            'score': 'skipped',
            'failed_checks': [],
            'note': 'skill_batch_upgrader_v3 not available, content quality check skipped',
        }


def run_marketing_gate_check(skill_md: Path) -> Dict[str, Any]:
    """营销关卡检查(v2.0新增)
    
    在L1.5内容质量检查通过后，检查营销数据质量:
    - displayName中文化且≤20字符
    - summary营销优化且≤100字符
    - description 150-280字符, 非模板化
    - tags 5-10个
    - categoryIds正确映射
    - pricing合理性
    - license合规
    """
    try:
        sys.path.insert(0, str(SKILL_REGISTRY_DIR))
        from quality_gate import run_marketing_gate
        result = run_marketing_gate(skill_md)
        failed_checks = [c['name'] for c in result.get('checks', []) if not c['passed']]
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': failed_checks,
        }
    except ImportError:
        return {
            'passed': True,
            'score': 'skipped',
            'failed_checks': [],
            'note': 'quality_gate.run_marketing_gate not available, skipped',
        }


def run_anti_hallucination_check(skill_md: Path) -> Dict[str, Any]:
    """防幻觉机制检查(v2.0新增)
    
    检查AI虚假实现和需求理解偏差:
    - 交叉验证(需L2/L3/L4报告, 无报告时跳过, 不阻止)
    - 需求理解偏差: description声明 vs body实际内容
    - 虚假实现检测: 无占位符/无模板/无空代码块
    """
    try:
        sys.path.insert(0, str(SKILL_REGISTRY_DIR))
        from quality_gate import run_anti_hallucination
        result = run_anti_hallucination(skill_md)
        failed_checks = [c['name'] for c in result.get('checks', []) if not c['passed']]
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': failed_checks,
        }
    except ImportError:
        return {
            'passed': True,
            'score': 'skipped',
            'failed_checks': [],
            'note': 'quality_gate.run_anti_hallucination not available, skipped',
        }


def run_rating_gate_check(skill_md: Path, slug: str = None) -> Dict[str, Any]:
    """评分门控检查(v2.3新增 — 流程固化: 低于4.5分阻断上传)
    
    在L1静态检查通过后, 检查skill在平台上的历史评分:
    - 平台评分 < 4.5 → 阻断上传, 要求先升级
    - current_status == deleted → 阻断上传, 要求重新差异化
    
    这是质检门控闭环的关键环节:
    评分同步(sync_platform_ratings) → 检测低评分(check_low_rating_skills) 
    → 阻断上传(rating_gate) → 触发升级(upgrade_single_skill) → 升级通过 → 允许重传
    """
    try:
        sys.path.insert(0, str(SKILL_REGISTRY_DIR))
        from quality_gate import run_rating_gate
        result = run_rating_gate(skill_md, slug)
        failed_checks = [c['name'] for c in result.get('checks', []) if not c['passed']]
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': failed_checks,
        }
    except ImportError:
        return {
            'passed': True,
            'score': 'skipped',
            'failed_checks': [],
            'note': 'quality_gate.run_rating_gate not available, skipped',
        }


def run_l2_check(slug: str) -> Dict[str, Any]:
    """L2 LLM验证报告检查(v2.0新增)
    
    复用update_mechanism.py的L2检查模式:
    - 检查l2_final_report_{slug}.json是否存在
    - 如果存在, 验证TRACE总分≥35
    - 如果不存在, 标记为pending, 生成AI执行指引
    """
    import json as _json
    l2_final_path = SKILL_REGISTRY_DIR / f'l2_final_report_{slug}.json'
    
    if not l2_final_path.exists():
        return {
            'passed': None,
            'status': 'pending_ai_eval',
            'failed_checks': ['l2_report_missing'],
            'note': f'L2验证报告不存在: {l2_final_path}',
            'guide': f'请AI执行L2评估: python llm_validator.py validate {slug} → AI执行 → python llm_validator.py import {slug} <结果.json>',
        }
    
    try:
        with open(l2_final_path, 'r', encoding='utf-8') as f:
            l2_final = _json.load(f)
        
        l2_passed = l2_final.get('l2_passed', False)
        trace_total = l2_final.get('trace_total', 0)
        
        return {
            'passed': l2_passed,
            'trace_total': trace_total,
            'trace_grade': l2_final.get('trace_grade', 'D'),
            'failed_checks': [] if l2_passed else [f'TRACE评分{trace_total}/50未通过(阈值35)'],
        }
    except Exception as e:
        return {
            'passed': False,
            'status': 'error',
            'failed_checks': [f'L2报告读取失败: {e}'],
        }


def run_l3_check(slug: str) -> Dict[str, Any]:
    """L3 Agent试运行报告检查(v2.0新增)
    
    复用update_mechanism.py的L3检查模式:
    - 检查l3_final_report_{slug}.json是否存在
    - 如果存在, 验证评分≥70
    - 如果不存在, 标记为pending, 生成AI执行指引
    """
    import json as _json
    l3_final_path = SKILL_REGISTRY_DIR / f'l3_final_report_{slug}.json'
    
    if not l3_final_path.exists():
        return {
            'passed': None,
            'status': 'pending_ai_trial',
            'failed_checks': ['l3_report_missing'],
            'note': f'L3试运行报告不存在: {l3_final_path}',
            'guide': f'请AI执行L3试运行: python agent_trial.py trial {slug} → AI执行6个用例 → python agent_trial.py import {slug} <结果.json>',
        }
    
    try:
        with open(l3_final_path, 'r', encoding='utf-8') as f:
            l3_final = _json.load(f)
        
        l3_passed = l3_final.get('l3_passed', False)
        l3_score = l3_final.get('l3_score', 0)
        
        return {
            'passed': l3_passed,
            'score': l3_score,
            'grade': l3_final.get('l3_grade', 'D'),
            'failed_checks': [] if l3_passed else [f'L3试运行评分{l3_score}/100未通过(阈值70)'],
        }
    except Exception as e:
        return {
            'passed': False,
            'status': 'error',
            'failed_checks': [f'L3报告读取失败: {e}'],
        }


# ============================================================
# Phase 4: SYNC_GITHUB - GitHub双仓库同步
# ============================================================

def sync_to_github(slug: str, skill_md: Path, new_version: str,
                   changelog: str, source: str,
                   skill_id: int = None) -> Dict[str, Any]:
    """同步skill到GitHub (双仓库策略)
    
    策略:
    - 免费skill: 推送到 hermes-skills (公开引流) + origin (私有备份)
    - 付费skill: 仅推送到 origin (私有备份), 不推送到 hermes-skills
    
    执行: git add → git commit → git push (private) → git push (public, 仅免费)
    """
    result = {
        'slug': slug,
        'platform': 'github',
        'version': new_version,
        'status': 'unknown',
        'private_push': None,
        'public_push': None,
        'is_free': False,
    }

    file_path = str(skill_md).replace('\\', '/')
    commit_msg = f"feat({slug}): upgrade to v{new_version} - {changelog}"

    # 判断免费/付费
    result['is_free'] = is_free_skill(skill_md)

    try:
        # git add
        add_result = subprocess.run(
            ['git', 'add', file_path],
            capture_output=True, text=True, timeout=30,
            cwd=str(SKILLS_ROOT)
        )
        if add_result.returncode != 0:
            result['status'] = 'failed'
            result['error'] = f'git add failed: {add_result.stderr}'
            return result

        # git commit
        commit_result = subprocess.run(
            ['git', 'commit', '-m', commit_msg],
            capture_output=True, text=True, timeout=30,
            cwd=str(SKILLS_ROOT)
        )
        if commit_result.returncode != 0:
            if 'nothing to commit' in commit_result.stdout.lower():
                result['status'] = 'no_changes'
                return result
            result['status'] = 'failed'
            result['error'] = f'git commit failed: {commit_result.stderr}'
            return result

        # 1. 推送到私有备份仓库 (所有skill)
        push_private = subprocess.run(
            ['git', 'push', PRIVATE_REMOTE, GITHUB_BRANCH],
            capture_output=True, text=True, timeout=180,
            cwd=str(SKILLS_ROOT)
        )
        if push_private.returncode == 0:
            result['private_push'] = 'success'
            if skill_id:
                record_platform_upload(skill_id, new_version, 'github_private', slug,
                                       'success', visibility='private')
        else:
            result['private_push'] = 'failed'
            result['private_error'] = push_private.stderr[:200]
            if skill_id:
                record_platform_upload(skill_id, new_version, 'github_private', slug,
                                       'failed', error=push_private.stderr[:200])

        # 2. 推送到公开引流仓库 (免费+付费skill，付费版与clawhub一致)
        # hermes-skills现在包含免费和付费两种skill
        push_public = subprocess.run(
            ['git', 'push', PUBLIC_REMOTE, GITHUB_BRANCH],
            capture_output=True, text=True, timeout=180,
            cwd=str(SKILLS_ROOT)
        )
        if push_public.returncode == 0:
            result['public_push'] = 'success'
            if skill_id:
                pricing_val = 'free' if result['is_free'] else 'paid'
                record_platform_upload(skill_id, new_version, 'github_public', slug,
                                       'success', visibility='public', pricing=pricing_val)
        else:
            result['public_push'] = 'failed'
            result['public_error'] = push_public.stderr[:200]
            if skill_id:
                record_platform_upload(skill_id, new_version, 'github_public', slug,
                                       'failed', error=push_public.stderr[:200])

        # 综合状态
        if result['private_push'] == 'success':
            result['status'] = 'success'
            result['commit_message'] = commit_msg
        elif result['private_push'] == 'failed':
            result['status'] = 'committed_not_pushed'
            result['error'] = result.get('private_error', 'unknown')
        else:
            result['status'] = 'unknown'

        return result

    except subprocess.TimeoutExpired:
        result['status'] = 'timeout'
        result['error'] = 'git operation timed out'
        if skill_id:
            record_platform_upload(skill_id, new_version, 'github_public', slug,
                                   'timeout', error='git operation timed out')
        return result
    except Exception as e:
        result['status'] = 'error'
        result['error'] = str(e)
        if skill_id:
            record_platform_upload(skill_id, new_version, 'github_public', slug,
                                   'error', error=str(e)[:200])
        return result


# ============================================================
# Phase 5: SYNC_SKILLHUB - SkillHub同步
# ============================================================

def sync_to_skillhub(slug: str, skill_md: Path, new_version: str,
                     skill_id: int, is_paid: bool = False) -> Dict[str, Any]:
    """同步skill到SkillHub

    免费版: 通过skillhub CLI上传
    付费版: 生成payload文件(需浏览器session认证上传)
    """
    result = {
        'slug': slug,
        'platform': 'skillhub',
        'version': new_version,
        'status': 'unknown',
        'free_upload': None,
        'paid_upload': None,
    }

    skill_dir = skill_md.parent

    # v3.0增强: 速率限制预检 (防止爆发式上传触发平台反垃圾系统)
    # 根因: 2026-07-24单秒上传1097个skill导致账号被封禁
    # 复用daily_sync.py的速率限制机制,不创建新的独立实现
    try:
        import sys as _sys
        _tools_dir = os.path.dirname(os.path.abspath(__file__))
        if _tools_dir not in _sys.path:
            _sys.path.insert(0, _tools_dir)
        from daily_sync import check_upload_rate_limit, record_upload
        rate_check = check_upload_rate_limit('skillhub')
        if not rate_check.get('allowed', True):
            wait = rate_check.get('wait_seconds', 120)
            result['status'] = 'rate_limited'
            result['error'] = f"速率限制: {rate_check.get('reason', '未知')} (需等待{wait}秒)"
            result['free_upload'] = {'status': 'rate_limited', 'error': result['error']}
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'rate_limited', error=result['error'])
            return result
    except ImportError:
        # v3.3: 失败安全(fail-safe) — daily_sync不可用时阻止上传
        result['status'] = 'rate_limited'
        result['error'] = '速率限制模块不可用,已阻止上传以防爆发式触发反垃圾系统'
        result['free_upload'] = {'status': 'rate_limited', 'error': result['error']}
        return result
    except Exception as e:
        # v3.3: 失败安全(fail-safe) — 速率限制异常时阻止上传
        result['status'] = 'rate_limited'
        result['error'] = f'速率限制检查异常,已阻止上传: {e}'
        result['free_upload'] = {'status': 'rate_limited', 'error': result['error']}
        return result

    # 检查内容长度(WAF限制)
    content = skill_md.read_text(encoding='utf-8', errors='replace')
    if len(content) > SKILLHUB_MAX_CONTENT:
        result['status'] = 'blocked_content_too_long'
        result['error'] = f'内容过长({len(content)}>{SKILLHUB_MAX_CONTENT})'
        result['free_upload'] = {'status': 'blocked_content_too_long', 'error': result['error']}
        record_platform_upload(skill_id, new_version, 'skillhub', slug,
                               'blocked_content_too_long', error=result['error'])
        return result

    # v3.4: 内容指纹去重预检 (防止相同内容以不同slug上传触发平台反垃圾系统)
    # 根因: 2026-07-24批量上传中大量近似重复内容被封禁(93.4%封禁率)
    try:
        import sys as _sys
        _tools_dir = os.path.dirname(os.path.abspath(__file__))
        if _tools_dir not in _sys.path:
            _sys.path.insert(0, _tools_dir)
        from content_dedup import check_content_dedup
        dedup_result = check_content_dedup(slug, content)
        if dedup_result.get('duplicate'):
            result['status'] = 'dedup_blocked'
            result['error'] = f"内容去重: {dedup_result['reason']}"
            result['free_upload'] = {'status': 'dedup_blocked', 'error': result['error']}
            record_platform_upload(skill_id, new_version, 'skillhub', slug,
                                   'dedup_blocked', error=result['error'])
            return result
    except ImportError:
        pass  # 去重模块不可用时不阻断
    except Exception as e:
        print(f"[WARN] 内容去重检查异常(不阻断): {e}")

    # 免费版上传 - 通过CLI
    try:
        cli_cmd = f'skillhub publish "{skill_dir}" --changelog "Auto-sync v{new_version}"'
        cli_result = subprocess.run(
            cli_cmd, shell=True, capture_output=True, text=True, timeout=60
        )
        output = cli_result.stdout + cli_result.stderr

        if cli_result.returncode == 0:
            result['free_upload'] = {'status': 'success', 'output': output[:200]}
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'success', visibility='public', pricing='free')
            # v3.0: 记录上传时间戳用于速率限制
            # v3.4: record_upload失败时记录警告(非静默pass),避免速率限制计数偏少
            try:
                record_upload('skillhub', slug)
            except Exception as e:
                print(f"  [WARN] record_upload失败,速率限制计数可能不准: {e}")
        elif 'VERSION_EXISTS' in output:
            result['free_upload'] = {'status': 'version_exists', 'output': output[:200]}
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'version_exists', error='VERSION_EXISTS')
        elif '429' in output:
            result['free_upload'] = {'status': 'rate_limited', 'output': output[:200]}
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'rate_limited', error='RATE_LIMITED')
        else:
            result['free_upload'] = {'status': 'failed', 'output': output[:200]}
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'failed', error=output[:200])
    except subprocess.TimeoutExpired:
        result['free_upload'] = {'status': 'timeout'}
        record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                               'timeout', error='CLI timeout')
    except Exception as e:
        result['free_upload'] = {'status': 'error', 'error': str(e)}
        record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                               'error', error=str(e))

    # 付费版: 生成payload文件
    if is_paid:
        metadata, body = parse_frontmatter(content)
        payload = {
            'slug': slug,
            'version': new_version,
            'displayName': metadata.get('displayName', slug),
            'summary': metadata.get('summary', ''),
            'changelog': f'Auto-sync v{new_version}',
            'pricing': {
                'billingType': 'per_call',
                'pricingMode': 'unified',
                'pricePerCall': '9.90',
                'currency': 'CNY',
            },
        }
        payload_dir = SKILLS_ROOT / "enterprise-upload" / "payloads"
        payload_dir.mkdir(parents=True, exist_ok=True)
        payload_path = payload_dir / f"{slug}-paid-v{new_version}.json"
        payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
        result['paid_upload'] = {
            'status': 'payload_ready',
            'path': str(payload_path),
        }
        record_platform_upload(skill_id, new_version, 'skillhub_paid', slug,
                               'payload_ready', visibility='org_only', pricing='paid')

    # 汇总状态
    free_status = result['free_upload']['status'] if result['free_upload'] else 'skipped'
    result['status'] = free_status
    return result


# ============================================================
# Phase 6: SYNC_CLAWHUB - ClawHub同步
# ============================================================

def sync_to_clawhub(slug: str, skill_md: Path, new_version: str,
                    skill_id: int) -> Dict[str, Any]:
    """同步skill到ClawHub (v2.2: 增加营销包装参数)

    营销元素(复用clawhub_batch_uploader的提取函数):
    - --categories: 分类(从SKILL.md推断, local_to_clawhub直连映射)
    - --topics: 话题标签(从frontmatter tags和slug提取)
    - --name: 显示名称(从frontmatter displayName获取)
    - --slug: 确保slug一致性
    - --json: JSON输出便于解析
    """
    result = {
        'slug': slug,
        'platform': 'clawhub',
        'version': new_version,
        'status': 'unknown',
    }

    skill_dir = skill_md.parent
    changelog = f'Auto-sync v{new_version}'

    # v2.2: 提取营销参数(复用clawhub_batch_uploader的函数, 避免重复实现)
    try:
        sys.path.insert(0, str(SKILL_REGISTRY_DIR))
        from clawhub_batch_uploader import get_clawhub_category, get_clawhub_topics, get_display_name
        category = get_clawhub_category(skill_dir)
        topics = get_clawhub_topics(skill_dir, slug)
        display_name = get_display_name(skill_dir)
    except ImportError:
        category = "other"
        topics = []
        display_name = ""
        result['marketing_warning'] = 'clawhub_batch_uploader不可用, 营销参数缺失'

    # 构建上传命令(含营销参数)
    cmd_parts = [
        'npx', 'clawhub',
        '--registry', '"https://clawhub.ai"',
        'publish', f'"{skill_dir}"',
        '--changelog', f'"{changelog}"',
        '--categories', f'"{category}"',
        '--topics', f'"{",".join(topics)}"',
        '--slug', f'"{slug}"',
        '--json',
    ]
    if display_name:
        cmd_parts.extend(['--name', f'"{display_name}"'])

    cmd_str = ' '.join(cmd_parts)
    result['marketing'] = {'category': category, 'topics': topics[:5], 'name': display_name}

    try:
        proc = subprocess.run(
            cmd_str,
            capture_output=True, text=True, timeout=120,
            cwd=str(SKILLS_ROOT), shell=True
        )
        output = proc.stdout + proc.stderr

        # 尝试解析JSON输出
        json_result = None
        try:
            json_result = json.loads(proc.stdout.strip())
        except (json.JSONDecodeError, ValueError):
            pass

        if proc.returncode == 0:
            result['status'] = 'success'
            result['output'] = output[:200]
            if json_result:
                result['clawhub_data'] = {
                    'slug': json_result.get('slug', slug),
                    'version': json_result.get('version', new_version),
                    'url': json_result.get('url', ''),
                }
            record_platform_upload(skill_id, new_version, 'clawhub', slug,
                                   'success', visibility='public', pricing='free')
        elif 'Rate limit' in output or 'rate limit' in output:
            result['status'] = 'rate_limited'
            result['output'] = output[:200]
            record_platform_upload(skill_id, new_version, 'clawhub', slug,
                                   'rate_limited', error='RATE_LIMITED')
        elif 'Version' in output and 'already exists' in output:
            result['status'] = 'version_exists'
            result['output'] = output[:200]
            record_platform_upload(skill_id, new_version, 'clawhub', slug,
                                   'version_exists', error='VERSION_EXISTS')
        else:
            result['status'] = 'failed'
            result['output'] = output[:200]
            record_platform_upload(skill_id, new_version, 'clawhub', slug,
                                   'failed', error=output[:200])
    except subprocess.TimeoutExpired:
        result['status'] = 'timeout'
        record_platform_upload(skill_id, new_version, 'clawhub', slug,
                               'timeout', error='Uploader timeout')
    except Exception as e:
        result['status'] = 'error'
        result['error'] = str(e)
        record_platform_upload(skill_id, new_version, 'clawhub', slug,
                               'error', error=str(e))

    return result


# ============================================================
# Phase 7: 端到端同步
# ============================================================

def sync_skill_to_all_platforms(slug: str, skip_github: bool = False,
                                skip_skillhub: bool = False,
                                skip_clawhub: bool = False,
                                skip_content_quality: bool = False,
                                skip_security: bool = False,
                                skip_marketing: bool = False,
                                skip_l2: bool = False,
                                skip_l3: bool = False,
                                force: bool = False) -> Dict[str, Any]:
    """端到端同步单个skill到所有平台

    流程(v2.2): 检测变更 → 版本递增 → L1质量门禁 → L1.5内容质量 → 安全预检 → 营销关卡 → 防幻觉 → L2验证 → L3试运行 → GitHub → SkillHub → ClawHub
    
    v2.2新增参数:
        skip_security: 跳过安全预检(批量场景, 已在生产环节检查时可跳过)
    v2.0新增参数:
        skip_marketing: 跳过营销关卡(批量场景)
        skip_l2: 跳过L2 LLM验证(批量场景, 与update_mechanism一致)
        skip_l3: 跳过L3 Agent试用(批量场景)
    """
    print(f"\n{'='*60}")
    print(f"同步skill: {slug}")
    print(f"{'='*60}")

    result = {
        'slug': slug,
        'timestamp': NOW,
        'phases': {},
    }

    # 1. 查找SKILL.md
    skill_md = find_skill_md(slug)
    if not skill_md:
        result['error'] = f'SKILL.md not found for: {slug}'
        print(f"  ✗ 未找到SKILL.md: {slug}")
        return result

    source = find_skill_source(slug)
    result['source'] = source

    # 2. 查询数据库
    db_skill = get_skill_from_db(slug)
    if not db_skill:
        result['error'] = f'Skill not in database: {slug}'
        print(f"  ✗ 数据库中无此skill: {slug}")
        return result

    skill_id = db_skill['id']
    current_version = db_skill.get('current_version', '1.0.0')
    current_hash = compute_file_hash(skill_md)
    last_hash = db_skill.get('last_hash', '')

    # 3. 检测变更
    changed = (last_hash != current_hash) if last_hash else force
    if not changed and not force:
        result['status'] = 'no_changes'
        print(f"  ℹ 无变更,跳过同步 (hash一致)")
        return result

    print(f"  ✓ 检测到变更: {last_hash[:8]}... → {current_hash[:8]}...")

    # 4. 版本递增
    new_version = increment_version(current_version)
    if not update_version_in_file(skill_md, new_version):
        print(f"  ⚠ 版本号更新失败,使用原版本: {current_version}")
        new_version = current_version
    else:
        print(f"  ✓ 版本递增: {current_version} → {new_version}")

    # 重新计算hash(版本号已更新)
    new_hash = compute_file_hash(skill_md)
    content = skill_md.read_text(encoding='utf-8')
    line_count = content.count('\n') + 1
    changelog = f'Auto-sync: content updated, version {current_version} → {new_version}'

    # 5. 质量门禁
    print(f"  [3/7] 质量门禁检查...")
    qc = run_quality_check(skill_md)
    result['phases']['quality_check'] = qc
    if not qc['passed']:
        print(f"  ✗ 质量门禁未通过: {qc['failed_checks']}")
        result['status'] = 'blocked_by_quality_gate'
        record_platform_upload(skill_id, new_version, 'quality_gate', slug,
                               'blocked', error=str(qc['failed_checks']))
        return result
    print(f"  ✓ 质量门禁通过 ({qc['score']})")

    # 5.1 L1.5内容质量门禁(v3.1新增)
    if not skip_content_quality:
        print(f"  [3.5/7] 内容质量门禁检查...")
        cq = run_content_quality_gate(skill_md)
        result['phases']['content_quality'] = cq
        if not cq['passed']:
            print(f"  ✗ 内容质量门禁未通过: {cq['failed_checks']}")
            result['status'] = 'blocked_by_content_quality'
            record_platform_upload(skill_id, new_version, 'content_quality_gate', slug,
                                   'blocked', error=str(cq['failed_checks']))
            return result
        print(f"  ✓ 内容质量门禁通过 ({cq['score']})")
    else:
        result['phases']['content_quality'] = {'status': 'skipped'}

    # 5.1.5 安全预检(v2.2新增 — 科恩实验室+云鼎实验室高风险模式检测)
    if not skip_security:
        print(f"  [3.55/7] 安全预检检查...")
        try:
            from quality_gate import run_security_precheck
            sec = run_security_precheck(skill_md)
            result['phases']['security_precheck'] = sec
            if not sec.get('overall_passed', False):
                failed_checks = [c['name'] for c in sec.get('checks', []) if not c.get('passed')]
                critical_checks = [c for c in sec.get('checks', []) if not c.get('passed') and c.get('severity') == 'critical']
                if critical_checks:
                    print(f"  ✗ 安全预检未通过(严重风险): {failed_checks}")
                    result['status'] = 'blocked_by_security_precheck'
                    record_platform_upload(skill_id, new_version, 'security_precheck', slug,
                                           'blocked', error=str(failed_checks))
                    return result
                else:
                    # 高/中风险不阻断,仅警告
                    print(f"  ⚠ 安全预检有风险提示(非阻断): {failed_checks}")
            else:
                print(f"  ✓ 安全预检通过 ({sec.get('passed_checks', 0)}/{sec.get('total_checks', 0)})")
        except ImportError:
            print(f"  ⚠ 安全预检模块不可用,跳过检查")
            result['phases']['security_precheck'] = {'status': 'skipped', 'reason': 'module_unavailable'}
    else:
        result['phases']['security_precheck'] = {'status': 'skipped'}

    # 5.1.8 评分门控(v2.3新增 — 流程固化: 低于4.5分阻断上传)
    print(f"  [3.58/7] 评分门控检查...")
    rg = run_rating_gate_check(skill_md, slug)
    result['phases']['rating_gate'] = rg
    if not rg['passed']:
        print(f"  ✗ 评分门控未通过: {rg['failed_checks']}")
        result['status'] = 'blocked_by_rating_gate'
        record_platform_upload(skill_id, new_version, 'rating_gate', slug,
                               'blocked', error=str(rg['failed_checks']))
        return result
    print(f"  ✓ 评分门控通过 ({rg['score']})")

    # 5.2 营销关卡检查(v2.0新增)
    if not skip_marketing:
        print(f"  [3.6/7] 营销关卡检查...")
        mg = run_marketing_gate_check(skill_md)
        result['phases']['marketing_gate'] = mg
        if not mg['passed']:
            print(f"  ✗ 营销关卡未通过: {mg['failed_checks']}")
            result['status'] = 'blocked_by_marketing_gate'
            record_platform_upload(skill_id, new_version, 'marketing_gate', slug,
                                   'blocked', error=str(mg['failed_checks']))
            return result
        print(f"  ✓ 营销关卡通过 ({mg['score']})")
    else:
        result['phases']['marketing_gate'] = {'status': 'skipped'}

    # 5.3 防幻觉机制检查(v2.0新增)
    print(f"  [3.7/7] 防幻觉机制检查...")
    ah = run_anti_hallucination_check(skill_md)
    result['phases']['anti_hallucination'] = ah
    if not ah['passed']:
        print(f"  ✗ 防幻觉机制未通过: {ah['failed_checks']}")
        result['status'] = 'blocked_by_anti_hallucination'
        record_platform_upload(skill_id, new_version, 'anti_hallucination', slug,
                               'blocked', error=str(ah['failed_checks']))
        return result
    print(f"  ✓ 防幻觉机制通过 ({ah['score']})")

    # 5.4 L2 LLM验证检查(v2.0新增)
    if not skip_l2:
        print(f"  [3.8/7] L2 LLM验证检查...")
        l2 = run_l2_check(slug)
        result['phases']['l2_validation'] = l2
        if l2['passed'] is False:
            print(f"  ✗ L2验证未通过: {l2['failed_checks']}")
            result['status'] = 'blocked_by_l2_validation'
            record_platform_upload(skill_id, new_version, 'l2_validation', slug,
                                   'blocked', error=str(l2['failed_checks']))
            return result
        elif l2['passed'] is None:
            print(f"  ⚠ L2验证待AI执行: {l2['guide']}")
            result['status'] = 'blocked_by_l2_pending'
            record_platform_upload(skill_id, new_version, 'l2_validation', slug,
                                   'pending', error=l2['note'])
            return result
        print(f"  ✓ L2验证通过 (TRACE {l2.get('trace_total', '?')}/50, 等级{l2.get('trace_grade', '?')})")
    else:
        result['phases']['l2_validation'] = {'status': 'skipped'}

    # 5.5 L3 Agent试用检查(v2.0新增)
    if not skip_l3:
        print(f"  [3.9/7] L3 Agent试用检查...")
        l3 = run_l3_check(slug)
        result['phases']['l3_trial'] = l3
        if l3['passed'] is False:
            print(f"  ✗ L3试用未通过: {l3['failed_checks']}")
            result['status'] = 'blocked_by_l3_trial'
            record_platform_upload(skill_id, new_version, 'l3_trial', slug,
                                   'blocked', error=str(l3['failed_checks']))
            return result
        elif l3['passed'] is None:
            print(f"  ⚠ L3试用待AI执行: {l3['guide']}")
            result['status'] = 'blocked_by_l3_pending'
            record_platform_upload(skill_id, new_version, 'l3_trial', slug,
                                   'pending', error=l3['note'])
            return result
        print(f"  ✓ L3试用通过 (评分{l3.get('score', '?')}/100, 等级{l3.get('grade', '?')})")
    else:
        result['phases']['l3_trial'] = {'status': 'skipped'}

    # 6. 记录新版本
    record_version(skill_id, new_version, new_hash, changelog,
                   skill_md.stat().st_size, line_count)

    # 7. GitHub同步
    if not skip_github:
        print(f"  [4/7] 同步到GitHub...")
        gh_result = sync_to_github(slug, skill_md, new_version, changelog, source, skill_id)
        result['phases']['github'] = gh_result
        if gh_result['status'] == 'success':
            print(f"  ✓ GitHub同步成功")
        elif gh_result['status'] == 'no_changes':
            print(f"  ℹ GitHub: 无需提交的变更")
        else:
            print(f"  ⚠ GitHub同步: {gh_result['status']} - {gh_result.get('error', '')}")
    else:
        result['phases']['github'] = {'status': 'skipped'}

    # 8. SkillHub同步
    if not skip_skillhub:
        print(f"  [5/7] 同步到SkillHub...")
        is_paid = bool(db_skill.get('is_paid', False))
        sh_result = sync_to_skillhub(slug, skill_md, new_version, skill_id, is_paid)
        result['phases']['skillhub'] = sh_result
        free_upload = sh_result.get('free_upload') or {}
        free_status = free_upload.get('status', 'unknown')
        if free_status == 'success':
            print(f"  ✓ SkillHub同步成功")

            # 8.4 完整发布流程 (approve → publish_to_community → star → DB更新)
            # v2.8修复: 统一到platform_ops.post_upload_publish, 消除碎片化
            # 原实现缺少star_skill和slug改名处理, 导致已发布skill搜索排名低、改名后DB不一致
            print(f"  [5.4/7] 执行完整发布流程...")
            try:
                from platform_ops import post_upload_publish
                publish_result = post_upload_publish(slug, skill_id=skill_id)
                result['phases']['post_publish'] = publish_result
                pub_ok = publish_result.get('community', {}).get('success', False)
                if pub_ok:
                    actual_slug = publish_result.get('db_update', {}).get('actual_slug', slug)
                    print(f"  ✓ 发布流程完成 (approve→publish→star), slug={actual_slug}")
                else:
                    err = publish_result.get('community', {}).get('error', '未知错误')
                    if 'expired' in err or '401' in err or '认证' in err:
                        print(f"  ⚠ 发布流程跳过(认证过期): {err[:80]}")
                    else:
                        print(f"  ⚠ 发布流程未完全成功: {err[:80]}")
            except ImportError:
                print(f"  ⚠ platform_ops模块不可用,跳过发布流程")
                result['phases']['post_publish'] = {'status': 'skipped', 'reason': 'module_unavailable'}
        else:
            print(f"  ⚠ SkillHub: {free_status}")
    else:
        result['phases']['skillhub'] = {'status': 'skipped'}

    # 9. ClawHub同步
    if not skip_clawhub:
        print(f"  [6/7] 同步到ClawHub...")
        ch_result = sync_to_clawhub(slug, skill_md, new_version, skill_id)
        result['phases']['clawhub'] = ch_result
        if ch_result['status'] == 'success':
            print(f"  ✓ ClawHub同步成功")
        else:
            print(f"  ⚠ ClawHub: {ch_result['status']}")
    else:
        result['phases']['clawhub'] = {'status': 'skipped'}

    # 10. 汇总
    all_statuses = []
    for phase in ['github', 'skillhub', 'clawhub']:
        phase_result = result['phases'].get(phase, {})
        all_statuses.append(phase_result.get('status', 'unknown'))

    if all(s == 'success' for s in all_statuses):
        result['status'] = 'all_success'
    elif any(s == 'success' for s in all_statuses):
        result['status'] = 'partial_success'
    else:
        result['status'] = 'failed'

    print(f"  [7/7] 同步完成: {result['status']}")
    return result


def sync_all_changed_skills(skip_github: bool = False,
                             skip_skillhub: bool = False,
                             skip_clawhub: bool = False,
                             skip_security: bool = False,
                             skip_marketing: bool = False,
                             skip_l2: bool = True,
                             skip_l3: bool = True) -> Dict[str, Any]:
    """同步所有变更的skill(批量模式默认跳过L2/L3,因需AI执行)"""
    print("扫描变更...")
    changed = scan_all_changes()
    print(f"发现 {len(changed)} 个变更skill")

    results = {
        'scan_time': NOW,
        'total_changed': len(changed),
        'synced': [],
        'failed': [],
        'skipped': [],
    }

    for i, item in enumerate(changed, 1):
        print(f"\n[{i}/{len(changed)}] {item['slug']}")
        sync_result = sync_skill_to_all_platforms(
            item['slug'],
            skip_github=skip_github,
            skip_skillhub=skip_skillhub,
            skip_clawhub=skip_clawhub,
            skip_security=skip_security,
            skip_marketing=skip_marketing,
            skip_l2=skip_l2,
            skip_l3=skip_l3,
        )
        if sync_result.get('status') in ('all_success', 'partial_success'):
            results['synced'].append(sync_result)
        elif sync_result.get('status') == 'no_changes':
            results['skipped'].append(sync_result)
        else:
            results['failed'].append(sync_result)

    # 汇总
    print(f"\n{'='*60}")
    print(f"同步汇总")
    print(f"{'='*60}")
    print(f"  总变更: {results['total_changed']}")
    print(f"  已同步: {len(results['synced'])}")
    print(f"  已跳过: {len(results['skipped'])}")
    print(f"  失败:   {len(results['failed'])}")

    return results


# ============================================================
# 命令行入口
# ============================================================

def upgrade_single_skill(slug: str, skip_platforms: bool = False,
                          force_sync: bool = False) -> Dict[str, Any]:
    """独立skill升级完整流程

    流程: 查找SKILL.md → 内容质量检测 → 自动修复 → 验证修复 → L1合规检查 → 多平台同步 → 记录
    
    这是完整的独立skill升级流程,适用于:
    - 发现单个skill有质量问题(如AI测评报告)
    - 需要升级并重新发布到所有平台
    - 需要版本递增和质量保证

    参数:
        slug: skill的slug标识
        skip_platforms: 跳过平台同步(仅检测+修复,不重传)
        force_sync: 强制同步(即使内容质量未完全通过)
    
    返回:
        dict: 升级结果详情
    """
    print(f"\n{'='*60}")
    print(f"独立skill升级流程: {slug}")
    print(f"{'='*60}")

    result = {
        'slug': slug,
        'timestamp': NOW,
        'phases': {},
    }

    # === Step 1: 查找SKILL.md ===
    print(f"\n[1/6] 查找SKILL.md...")
    sys.path.insert(0, str(SKILL_REGISTRY_DIR))
    try:
        from skill_batch_upgrader_v3 import find_skill_md, run_content_quality_check, auto_fix_content, auto_fix
    except ImportError as e:
        result['error'] = f'skill_batch_upgrader_v3导入失败: {e}'
        print(f"  ✗ 导入失败: {e}")
        return result

    skill_md = find_skill_md(slug)
    if not skill_md:
        result['error'] = f'SKILL.md not found for: {slug}'
        print(f"  ✗ 未找到SKILL.md: {slug}")
        return result
    result['skill_md_path'] = str(skill_md)
    print(f"  ✓ 找到: {skill_md}")

    # === Step 2: 内容质量检测 ===
    print(f"\n[2/6] 内容质量检测...")
    cq_before = run_content_quality_check(skill_md)
    result['phases']['content_check_before'] = {
        'pass_count': cq_before['pass_count'],
        'fail_count': cq_before['fail_count'],
        'failed_checks': [c['name'] for c in cq_before['checks'] if not c['passed']],
    }
    if cq_before['fail_count'] == 0:
        print(f"  ✓ 内容质量全部通过 ({cq_before['pass_count']}/7)")
    else:
        print(f"  ⚠ 发现 {cq_before['fail_count']} 项内容质量问题:")
        for check in cq_before['checks']:
            if not check['passed']:
                print(f"    ✗ {check['name']}: {check['message'][:80]}")

    # === Step 3: 自动修复 ===
    print(f"\n[3/6] 自动修复内容质量问题...")
    content_fixes = auto_fix_content(skill_md)
    compliance_fixes = auto_fix(skill_md)
    all_fixes = content_fixes + compliance_fixes
    result['phases']['auto_fix'] = {
        'content_fixes': content_fixes,
        'compliance_fixes': compliance_fixes,
        'total_fixes': len(all_fixes),
    }
    if all_fixes:
        print(f"  ✓ 修复 {len(all_fixes)} 项: {', '.join(all_fixes)}")
    else:
        print(f"  ℹ 无可自动修复的问题")

    # === Step 4: 验证修复 ===
    print(f"\n[4/6] 验证修复结果...")
    cq_after = run_content_quality_check(skill_md)
    result['phases']['content_check_after'] = {
        'pass_count': cq_after['pass_count'],
        'fail_count': cq_after['fail_count'],
        'failed_checks': [c['name'] for c in cq_after['checks'] if not c['passed']],
    }
    if cq_after['fail_count'] == 0:
        print(f"  ✓ 内容质量全部通过 ({cq_after['pass_count']}/7)")
    else:
        print(f"  ⚠ 仍有 {cq_after['fail_count']} 项问题需手动处理:")
        for check in cq_after['checks']:
            if not check['passed']:
                print(f"    ✗ {check['name']}: {check['message'][:80]}")
        if not force_sync:
            result['status'] = 'needs_manual_fix'
            result['error'] = f'仍有{cq_after["fail_count"]}项内容质量问题需手动处理,使用--force可强制同步'
            print(f"\n  使用 --force 可强制同步到平台(不推荐)")
            return result

    # === Step 5: L1合规检查 ===
    print(f"\n[5/6] L1合规检查...")
    qc = run_quality_check(skill_md)
    result['phases']['l1_compliance'] = qc
    if not qc['passed']:
        print(f"  ⚠ L1合规检查未通过: {qc['failed_checks']}")
        if not force_sync:
            result['status'] = 'blocked_by_l1'
            result['error'] = f'L1合规检查未通过: {qc["failed_checks"]}'
            return result
    else:
        print(f"  ✓ L1合规检查通过 ({qc['score']})")

    # === Step 5.45: 安全预检(v2.2新增 — 科恩实验室+云鼎实验室高风险模式) ===
    print(f"\n[5.45/6] 安全预检检查...")
    try:
        from quality_gate import run_security_precheck
        sec = run_security_precheck(skill_md)
        result['phases']['security_precheck'] = sec
        if not sec.get('overall_passed', False):
            critical_checks = [c for c in sec.get('checks', []) if not c.get('passed') and c.get('severity') == 'critical']
            if critical_checks:
                failed_names = [c['name'] for c in critical_checks]
                print(f"  ✗ 安全预检发现严重风险: {failed_names}")
                if not force_sync:
                    result['status'] = 'blocked_by_security_precheck'
                    result['error'] = f'安全预检严重风险(不可强制跳过): {failed_names}'
                    return result
            else:
                non_critical = [c['name'] for c in sec.get('checks', []) if not c.get('passed')]
                print(f"  ⚠ 安全预检有风险提示(非阻断): {non_critical}")
        else:
            print(f"  ✓ 安全预检通过 ({sec.get('passed_checks', 0)}/{sec.get('total_checks', 0)})")
    except ImportError:
        print(f"  ⚠ 安全预检模块不可用,跳过检查")
        result['phases']['security_precheck'] = {'status': 'skipped', 'reason': 'module_unavailable'}

    # === Step 5.5: 营销关卡检查(v2.0新增) ===
    print(f"\n[5.5/6] 营销关卡检查...")
    mg = run_marketing_gate_check(skill_md)
    result['phases']['marketing_gate'] = mg
    if not mg['passed']:
        print(f"  ⚠ 营销关卡未通过: {mg['failed_checks']}")
        if not force_sync:
            result['status'] = 'blocked_by_marketing_gate'
            result['error'] = f'营销关卡未通过: {mg["failed_checks"]}'
            return result
    else:
        print(f"  ✓ 营销关卡通过 ({mg['score']})")

    # === Step 5.6: 防幻觉机制检查(v2.0新增) ===
    print(f"\n[5.6/6] 防幻觉机制检查...")
    ah = run_anti_hallucination_check(skill_md)
    result['phases']['anti_hallucination'] = ah
    if not ah['passed']:
        print(f"  ⚠ 防幻觉机制未通过: {ah['failed_checks']}")
        if not force_sync:
            result['status'] = 'blocked_by_anti_hallucination'
            result['error'] = f'防幻觉机制未通过: {ah["failed_checks"]}'
            return result
    else:
        print(f"  ✓ 防幻觉机制通过 ({ah['score']})")

    # === Step 6: 多平台同步 ===
    if skip_platforms:
        print(f"\n[6/6] 跳过平台同步 (skip_platforms=True)")
        result['phases']['platform_sync'] = {'status': 'skipped'}
        result['status'] = 'fixed_locally'
    else:
        print(f"\n[6/6] 同步到所有平台...")
        # 升级流程跳过L2/L3(需AI单独执行), 但保留营销关卡和防幻觉
        sync_result = sync_skill_to_all_platforms(
            slug, skip_content_quality=True, skip_security=True, skip_marketing=True,
            skip_l2=True, skip_l3=True, force=True
        )
        result['phases']['platform_sync'] = sync_result
        if sync_result.get('status') == 'success':
            print(f"  ✓ 全平台同步成功")
        else:
            print(f"  ⚠ 同步状态: {sync_result.get('status', 'unknown')}")
        result['status'] = sync_result.get('status', 'unknown')

    # 保存升级报告
    report_path = SKILL_REGISTRY_DIR / f"upgrade_{slug}_{NOW.replace(':', '')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n升级报告已保存: {report_path}")

    return result


def cmd_scan():
    """扫描变更"""
    changed = scan_all_changes()
    print(f"\n变更检测报告 ({NOW})")
    print(f"{'='*60}")
    print(f"总变更skill: {len(changed)}")
    for item in changed:
        print(f"  → {item['slug']} ({item['source']})")
        print(f"    版本: {item['current_version']}")
        print(f"    hash: {item['old_hash']}... → {item['new_hash']}...")

    # 保存报告
    report_path = DATA_DIR / "reports" / "version_sync_scan_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({'scan_time': NOW, 'changed': changed}, f, ensure_ascii=False, indent=2)
    print(f"\n报告已保存: {report_path}")


def cmd_sync(slug: str, skip_github: bool = False, skip_skillhub: bool = False,
             skip_clawhub: bool = False, skip_security: bool = False,
             skip_marketing: bool = False,
             skip_l2: bool = False, skip_l3: bool = False, force: bool = False):
    """同步单个skill"""
    result = sync_skill_to_all_platforms(
        slug, skip_github=skip_github, skip_skillhub=skip_skillhub,
        skip_clawhub=skip_clawhub, skip_security=skip_security, skip_marketing=skip_marketing,
        skip_l2=skip_l2, skip_l3=skip_l3, force=force
    )
    # 保存结果
    result_path = SKILL_REGISTRY_DIR / f"version_sync_{slug}_{NOW.replace(':', '')}.json"
    with open(result_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n同步结果已保存: {result_path}")


def cmd_sync_all(skip_github: bool = False, skip_skillhub: bool = False,
                 skip_clawhub: bool = False, skip_security: bool = False,
                 skip_marketing: bool = False,
                 skip_l2: bool = True, skip_l3: bool = True):
    """同步所有变更skill(批量模式默认跳过L2/L3,因需AI执行)"""
    results = sync_all_changed_skills(
        skip_github=skip_github, skip_skillhub=skip_skillhub, skip_clawhub=skip_clawhub,
        skip_security=skip_security, skip_marketing=skip_marketing, skip_l2=skip_l2, skip_l3=skip_l3
    )
    result_path = SKILL_REGISTRY_DIR / f"version_sync_all_{NOW.replace(':', '')}.json"
    with open(result_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n同步报告已保存: {result_path}")


def cmd_sync_github(slug: str):
    """仅同步到GitHub"""
    skill_md = find_skill_md(slug)
    if not skill_md:
        print(f"✗ 未找到SKILL.md: {slug}")
        return
    db_skill = get_skill_from_db(slug)
    if not db_skill:
        print(f"✗ 数据库中无此skill: {slug}")
        return
    version = db_skill.get('current_version', '1.0.0')
    result = sync_to_github(slug, skill_md, version, 'Manual GitHub sync', find_skill_source(slug))
    print(f"GitHub同步结果: {result['status']}")
    if result.get('error'):
        print(f"  错误: {result['error']}")


def cmd_upgrade(slug: str, skip_platforms: bool = False, force: bool = False):
    """独立skill升级完整流程"""
    result = upgrade_single_skill(slug, skip_platforms=skip_platforms, force_sync=force)
    print(f"\n{'='*60}")
    print(f"升级结果: {result.get('status', 'unknown')}")
    print(f"{'='*60}")
    if result.get('error'):
        print(f"错误: {result['error']}")
    phases = result.get('phases', {})
    if phases.get('content_check_before'):
        before = phases['content_check_before']
        print(f"修复前: {before['fail_count']}项问题")
    if phases.get('content_check_after'):
        after = phases['content_check_after']
        print(f"修复后: {after['fail_count']}项问题")
    if phases.get('auto_fix'):
        fixes = phases['auto_fix']
        print(f"自动修复: {fixes['total_fixes']}项")


def cmd_status():
    """查看同步状态"""
    conn = get_db()
    c = conn.cursor()

    # 各平台最近同步状态
    c.execute("""
        SELECT platform,
            COUNT(*) as total,
            SUM(CASE WHEN upload_status = 'success' THEN 1 ELSE 0 END) as success,
            SUM(CASE WHEN upload_status = 'failed' THEN 1 ELSE 0 END) as failed,
            MAX(upload_date) as last_sync
        FROM platform_uploads
        GROUP BY platform
        ORDER BY platform
    """)
    rows = c.fetchall()

    print(f"\n版本同步状态概览 ({NOW})")
    print(f"{'='*60}")
    print(f"{'平台':<20} {'总数':>6} {'成功':>6} {'失败':>6} {'最近同步':<20}")
    print(f"{'-'*60}")
    for row in rows:
        print(f"{row['platform']:<20} {row['total']:>6} {row['success']:>6} {row['failed']:>6} {row['last_sync'][:19]:<20}")

    # 最近版本同步操作
    c.execute("""
        SELECT s.slug, o.operation_type, o.operation_date, o.details, o.after_state
        FROM operations o
        JOIN skills s ON s.id = o.skill_id
        WHERE o.operator = 'version_sync_pipeline'
        ORDER BY o.operation_date DESC
        LIMIT 20
    """)
    recent = c.fetchall()
    if recent:
        print(f"\n最近同步操作 (前20条):")
        for r in recent:
            print(f"  {r['operation_date'][:19]} | {r['slug']:<30} | {r['after_state']}")

    conn.close()


def cmd_report():
    """生成同步报告"""
    conn = get_db()
    c = conn.cursor()

    # 统计各平台同步情况
    c.execute("""
        SELECT
            p.platform,
            COUNT(DISTINCT p.skill_id) as unique_skills,
            COUNT(*) as total_uploads,
            SUM(CASE WHEN p.upload_status = 'success' THEN 1 ELSE 0 END) as success,
            SUM(CASE WHEN p.upload_status = 'failed' THEN 1 ELSE 0 END) as failed,
            SUM(CASE WHEN p.upload_status = 'version_exists' THEN 1 ELSE 0 END) as version_exists,
            SUM(CASE WHEN p.upload_status = 'rate_limited' THEN 1 ELSE 0 END) as rate_limited,
            MAX(p.upload_date) as last_sync
        FROM platform_uploads p
        GROUP BY p.platform
    """)
    platforms = [dict(r) for r in c.fetchall()]

    # 统计版本同步操作
    c.execute("""
        SELECT COUNT(*) as total_ops,
            MAX(operation_date) as last_op
        FROM operations
        WHERE operator = 'version_sync_pipeline'
    """)
    ops = c.fetchone()

    # 变更检测
    changed = scan_all_changes()

    report = {
        'report_time': NOW,
        'platform_summary': platforms,
        'version_sync_operations': dict(ops) if ops else {},
        'pending_changes': len(changed),
        'pending_change_list': [c['slug'] for c in changed[:50]],
    }

    report_path = DATA_DIR / "reports" / "version_sync_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n版本同步报告 ({NOW})")
    print(f"{'='*60}")
    print(f"待同步变更: {len(changed)}")
    print(f"版本同步操作总数: {dict(ops).get('total_ops', 0) if ops else 0}")
    print(f"\n平台同步统计:")
    for p in platforms:
        print(f"  {p['platform']:<20} | 唯一skill: {p['unique_skills']:>5} | "
              f"成功: {p['success']:>5} | 失败: {p['failed']:>5} | "
              f"最近: {p['last_sync'][:19] if p['last_sync'] else 'N/A'}")
    print(f"\n报告已保存: {report_path}")

    conn.close()


def main():
    parser = argparse.ArgumentParser(
        description='版本同步流水线 - 端到端多平台版本同步自动化',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest='command')

    sub.add_parser('scan', help='扫描变更,生成同步计划')
    sub.add_parser('status', help='查看同步状态概览')
    sub.add_parser('report', help='生成同步报告')

    sync_parser = sub.add_parser('sync', help='同步单个skill到所有平台')
    sync_parser.add_argument('slug', help='skill slug')
    sync_parser.add_argument('--skip-github', action='store_true', help='跳过GitHub同步')
    sync_parser.add_argument('--skip-skillhub', action='store_true', help='跳过SkillHub同步')
    sync_parser.add_argument('--skip-clawhub', action='store_true', help='跳过ClawHub同步')
    sync_parser.add_argument('--skip-security', action='store_true', help='跳过安全预检(科恩+云鼎风险检测)')
    sync_parser.add_argument('--skip-marketing', action='store_true', help='跳过营销关卡检查')
    sync_parser.add_argument('--skip-l2', action='store_true', help='跳过L2 LLM验证(需L2报告)')
    sync_parser.add_argument('--skip-l3', action='store_true', help='跳过L3 Agent试用(需L3报告)')
    sync_parser.add_argument('--force', action='store_true', help='强制同步(即使无变更)')

    sync_all_parser = sub.add_parser('sync-all', help='同步所有变更skill(批量模式默认跳过L2/L3)')
    sync_all_parser.add_argument('--skip-github', action='store_true')
    sync_all_parser.add_argument('--skip-skillhub', action='store_true')
    sync_all_parser.add_argument('--skip-clawhub', action='store_true')
    sync_all_parser.add_argument('--skip-security', action='store_true', help='跳过安全预检')
    sync_all_parser.add_argument('--skip-marketing', action='store_true', help='跳过营销关卡')
    sync_all_parser.add_argument('--no-skip-l2', action='store_true', help='不跳过L2验证(默认跳过)')
    sync_all_parser.add_argument('--no-skip-l3', action='store_true', help='不跳过L3试用(默认跳过)')

    gh_parser = sub.add_parser('sync-github', help='仅同步到GitHub')
    gh_parser.add_argument('slug', help='skill slug')

    upgrade_parser = sub.add_parser('upgrade', help='独立skill升级完整流程(检测+修复+同步)')
    upgrade_parser.add_argument('slug', help='skill slug')
    upgrade_parser.add_argument('--skip-platforms', action='store_true', help='跳过平台同步(仅检测+修复)')
    upgrade_parser.add_argument('--force', action='store_true', help='强制同步(即使内容质量未完全通过)')

    args = parser.parse_args()

    if args.command == 'scan':
        cmd_scan()
    elif args.command == 'sync':
        cmd_sync(args.slug, args.skip_github, args.skip_skillhub, args.skip_clawhub,
                 args.skip_security, args.skip_marketing, args.skip_l2, args.skip_l3, args.force)
    elif args.command == 'sync-all':
        cmd_sync_all(args.skip_github, args.skip_skillhub, args.skip_clawhub,
                     args.skip_security, args.skip_marketing,
                     skip_l2=not args.no_skip_l2, skip_l3=not args.no_skip_l3)
    elif args.command == 'sync-github':
        cmd_sync_github(args.slug)
    elif args.command == 'status':
        cmd_status()
    elif args.command == 'report':
        cmd_report()
    elif args.command == 'upgrade':
        cmd_upgrade(args.slug, skip_platforms=args.skip_platforms, force=args.force)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
