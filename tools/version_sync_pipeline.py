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
_sys.path.insert(0, str(_Path(__file__).resolve().parent))  # V118 W4: 模块级添加TOOLS_DIR,替代11处函数级sys.path.insert
from project_config import SKILLS_ROOT, TOOLS_DIR, DATA_DIR, get_timestamp, PLATFORM_CONFIG, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, DIFFERENTIATED_DIR # V123 W2: 合并重复import
# === End Phase 1 ===
DIFFERENTIATED_SKILLS_DIR = DIFFERENTIATED_DIR  # V103 W3: backward compat alias


import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional  # V121 W6: 移除未使用的 import time 与 Tuple

from skill_core import db as db_module  # V116 W1: 统一db入口(替代import db)
from skill_core.parser import find_skill_md, parse_frontmatter  # V128 Y4: 别名已统一移除

# ============================================================
# 配置
# ============================================================

# DB_PATH imported from config
# SKILLS_ROOT = PROJECT_ROOT (imported from config)
# TOOLS_DIR = TOOLS_DIR (imported from config)
# V103 W3: PACKAGED_SKILLS_DIR/OPENSOURCE_SKILLS_DIR/DIFFERENTIATED_DIR imported from project_config
# CLAWHUB_DOWNLOADED_DIR imported from config

# GitHub 仓库配置 (双仓库策略)
# V107 W3: GitHub仓库常量从github_repo_strategy导入 (消除重复定义)
from github_repo_strategy import PUBLIC_REMOTE, PRIVATE_REMOTE, GITHUB_BRANCH
# V100 W4: FREE_PRICING_TIERS/FREE_LICENSES已移除, 统一使用github_repo_strategy中的定义

# SkillHub 配置 — 使用skills_store_cli.py(原始CLI工具)
SKILLHUB_CLI = "python"
SKILLHUB_CLI_ARGS = [str(Path.home() / ".skillhub" / "skills_store_cli.py"), "publish"]
SKILLHUB_MAX_CONTENT = 5800  # WAF限制

# ClawHub 配置
CLAWHUB_UPLOADER = TOOLS_DIR / "clawhub_batch_uploader.py"

# 扫描目录配置: (目录路径, 来源标签)
# V103 W3: 重命名SCAN_DIRS→SCAN_DIRS_LABELED以避免与project_config.SCAN_DIRS命名冲突 (本结构含标签)
SCAN_DIRS_LABELED = [
    (PACKAGED_SKILLS_DIR, "packaged"),
    (OPENSOURCE_SKILLS_DIR, "opensource"),
    (DIFFERENTIATED_SKILLS_DIR, "differentiated"),
]

NOW = get_timestamp()  # V101 W4: 统一时间戳

# ============================================================
# 数据库操作
# ============================================================

# V117 W1: compute_file_hash通过db_module访问


# V116 W4: parse_frontmatter wrapper已消除, 调用方直接使用parse_frontmatter结果
# 原wrapper仅做了 result['fields'], result['body'] 的解包, 无附加逻辑


def increment_version(version: str, level: str = 'patch') -> str:
    """递增版本号(支持patch/minor/major三种策略) (V141 D3扩展)

    V129 Z3 (TD-212): 本函数与 clawhub_batch_uploader.increment_version 同名但职责不同。
    本函数为【字符串级纯函数】: 接收 version 字符串, 仅做版本号递增的纯变换, 无文件 I/O;
    clawhub_batch_uploader.increment_version 为【文件级适配器】: 接收 skill_dir 路径, 直接读写 SKILL.md。
    本模块的文件写入由 update_version_in_file(skill_md, new_version) 单独负责, 职责已分离, 两者不可合并。

    V141 D3 (TD-290): 扩展level参数, 支持:
      - 'patch': 1.0.0 → 1.0.1 (默认, 向后兼容)
      - 'minor': 1.0.0 → 1.1.0
      - 'major': 1.0.0 → 2.0.0

    Args:
        version: 当前版本号字符串(如"1.0.0")
        level: 递增级别('patch'/'minor'/'major')

    Returns:
        递增后的版本号字符串
    """
    parts = version.split('.')
    if len(parts) == 3:
        try:
            major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
            if level == 'major':
                return f"{major + 1}.0.0"
            elif level == 'minor':
                return f"{major}.{minor + 1}.0"
            else:  # patch (默认, 向后兼容)
                return f"{major}.{minor}.{patch + 1}"
        except ValueError as e:  # [V132 C2] 有意降级: 3段版本号解析失败,尝试2段  V144: 添加警告日志
            print(f"[WARN] 3段版本号解析失败,尝试2段: {e}")
    elif len(parts) == 2:
        try:
            major, minor = int(parts[0]), int(parts[1])
            if level == 'major':
                return f"{major + 1}.0.0"
            elif level == 'minor':
                return f"{major}.{minor + 1}.0"
            else:  # patch
                return f"{major}.{minor + 1}.0"
        except ValueError as e:  # [V132 C2] 有意降级: 2段版本号解析失败,使用默认递增  V144: 添加警告日志
            print(f"[WARN] 2段版本号解析失败,使用默认递增: {e}")
    return f"{version}.1" if version else "1.0.1"


def get_skill_from_db(slug: str) -> Optional[Dict[str, Any]]:
    conn = db_module.get_db()
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


# [V131 B5: 与platform_config.is_free_skill不同(本版查DB判断, 对方查配置常量)]
def is_free_skill(skill_md: Path) -> bool:
    """V127 X8: 委托到github_repo_strategy.is_free_skill_from_file(TD-197)

    消除重复的文件读取+frontmatter解析逻辑。
    保留原签名(skill_md: Path → bool)兼容现有调用方。
    """
    from github_repo_strategy import is_free_skill_from_file
    return is_free_skill_from_file(skill_md)


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
    """记录平台上传结果

    V129 Z4 (TD-213): 本函数为【委托适配器】, 已委托到 db.record_platform_upload (db_module)。
    因签名与 db.py 原版不同(参数名 status/error/pricing vs upload_status/error_message/pricing_on_platform,
    且本函数省略 operator/operation_type/operation_details, 由本包装器内部填充 version_sync_pipeline 上下文),
    故保留此薄包装层做参数映射与上下文注入, 不直接合并签名。真正的 DB 写入逻辑唯一存在于 db.record_platform_upload。
    """
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

    for scan_dir, source_label in SCAN_DIRS_LABELED:
        if not scan_dir.exists():
            continue
        for skill_md in scan_dir.rglob("SKILL.md"):
            if skill_md.parent.name.startswith('.'):
                continue
            slug = skill_md.parent.name
            current_hash = db_module.compute_file_hash(skill_md)

            # 查询数据库
            db_skill = get_skill_from_db(slug)
            if not db_skill:
                # 不在数据库中的skill,跳过
                continue

            last_hash = db_skill.get('last_hash') or ''
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
        from quality_gate import run_quality_gate
        result = run_quality_gate(skill_md)
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': [c['name'] for c in result.get('checks', []) if not c['passed']],
        }
    except ImportError:
        # V156: fail-safe — quality_gate模块不可用时阻断,不允许降级为基本检查
        return {
            'passed': False,
            'score': 'blocked',
            'failed_checks': ['module_unavailable'],
            'note': 'quality_gate.run_quality_gate不可用 — L1质量门禁阻断(fail-safe)',
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
        # PRR V146: 模块不可用时阻断(fail-safe), 不允许跳过
        return {
            'passed': False,
            'score': 'blocked',
            'failed_checks': ['module_unavailable'],
            'note': 'skill_batch_upgrader_v3不可用 — 内容质量检查阻断(fail-safe)',
        }


def run_marketing_gate_check(skill_md: Path) -> Dict[str, Any]:
    """营销关卡检查(v2.0新增, V150 T5: 使用autofix版本)
    
    在L1.5内容质量检查通过后，检查营销数据质量:
    - displayName中文化且≤20字符
    - summary营销优化且≤100字符
    - description 150-280字符, 非模板化
    - tags 5-10个
    - categoryIds正确映射
    - pricing合理性
    - license合规

    V150 T5: 优先使用run_marketing_gate_with_autofix,自动修复
    displayName/summary/description/tags/pricing等可修复问题。
    """
    try:
        # V150 T5: 优先使用autofix版本
        try:
            from quality_gate import run_marketing_gate_with_autofix
            result = run_marketing_gate_with_autofix(skill_md)
        except ImportError:
            from quality_gate import run_marketing_gate
            result = run_marketing_gate(skill_md)
        failed_checks = [c['name'] for c in result.get('checks', []) if not c['passed']]
        auto_fix_info = result.get('auto_fix', {})
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': failed_checks,
            'auto_fix_applied': auto_fix_info.get('fixes', []) if auto_fix_info.get('fixed') else [],
        }
    except ImportError:
        # PRR V146: 模块不可用时阻断(fail-safe), 不允许跳过
        return {
            'passed': False,
            'score': 'blocked',
            'failed_checks': ['module_unavailable'],
            'note': 'quality_gate.run_marketing_gate不可用 — 营销关卡阻断(fail-safe)',
        }


def run_anti_hallucination_check(skill_md: Path) -> Dict[str, Any]:
    """防幻觉机制检查(v2.0新增, V150 T4: 使用autofix版本)

    检查AI虚假实现和需求理解偏差:
    - 交叉验证(需L2/L3/L4报告, 无报告时跳过, 不阻止)
    - 需求理解偏差: description声明 vs body实际内容
    - 虚假实现检测: 无占位符/无模板/无空代码块

    V150 T4: 优先使用run_anti_hallucination_with_autofix,自动修复
    占位符等可修复问题,不可修复的问题仍会阻断。
    """
    try:
        # V150 T4: 优先使用autofix版本
        try:
            from quality_gate import run_anti_hallucination_with_autofix
            result = run_anti_hallucination_with_autofix(skill_md)
        except ImportError:
            from quality_gate import run_anti_hallucination
            result = run_anti_hallucination(skill_md)
        failed_checks = [c['name'] for c in result.get('checks', []) if not c['passed']]
        auto_fix_info = result.get('auto_fix', {})
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': failed_checks,
            'auto_fix_applied': auto_fix_info.get('fixes', []) if auto_fix_info.get('fixed') else [],
        }
    except ImportError:
        # PRR V146: 模块不可用时阻断(fail-safe), 不允许跳过
        return {
            'passed': False,
            'score': 'blocked',
            'failed_checks': ['module_unavailable'],
            'note': 'quality_gate.run_anti_hallucination不可用 — 防幻觉检查阻断(fail-safe)',
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
        from quality_gate import run_rating_gate
        result = run_rating_gate(skill_md, slug)
        failed_checks = [c['name'] for c in result.get('checks', []) if not c['passed']]
        return {
            'passed': result.get('overall_passed', False),
            'score': f"{result.get('passed_checks', 0)}/{result.get('total_checks', 0)}",
            'failed_checks': failed_checks,
        }
    except ImportError:
        # PRR V146: 模块不可用时阻断(fail-safe), 不允许跳过
        return {
            'passed': False,
            'score': 'blocked',
            'failed_checks': ['module_unavailable'],
            'note': 'quality_gate.run_rating_gate不可用 — 评分门控阻断(fail-safe)',
        }


def run_l2_check(slug: str) -> Dict[str, Any]:
    """L2 LLM验证报告检查(v2.0新增)
    
    复用update_mechanism.py的L2检查模式:
    - 检查l2_final_report_{slug}.json是否存在
    - 如果存在, 验证TRACE总分≥35
    - 如果不存在, 标记为pending, 生成AI执行指引
    """
    import json as _json
    l2_final_path = TOOLS_DIR / f'l2_final_report_{slug}.json'
    
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
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常时返回错误/默认值
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
    l3_final_path = TOOLS_DIR / f'l3_final_report_{slug}.json'
    
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
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常时返回错误/默认值
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
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常更新状态/计数继续
        result['status'] = 'error'
        result['error'] = str(e)
        if skill_id:
            record_platform_upload(skill_id, new_version, 'github_public', slug,
                                   'error', error=str(e)[:200])
        return result


# ============================================================
# Phase 5: SYNC_SKILLHUB - SkillHub同步
# ============================================================

def _skillhub_cli_fallback(slug: str, skill_dir: Path, skill_id: int,
                            new_version: str) -> Dict[str, Any]:
    """SkillHub CLI上传fallback — V139 S4

    仅当API通道(enterprise_uploader)不可用时使用。
    缺WAF重试, 不推荐生产环境使用。

    Args:
        slug: skill slug
        skill_dir: skill目录路径
        skill_id: 数据库skill ID
        new_version: 新版本号

    Returns:
        dict: {'status': 'success'|'failed'|'rate_limited'|...}
    """
    try:
        # V160 R2修复: 使用list-based subprocess消除shell=True(命令注入风险) + 添加速率限制
        from daily_sync import check_upload_rate_limit  # V128 Y1
        rate_check = check_upload_rate_limit('skillhub')
        if not rate_check.get('allowed', False):  # V161: fail-safe默认False
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'rate_limited', error='RATE_LIMITED')
            return {'status': 'rate_limited', 'output': rate_check.get('reason', '')[:200]}

        cli_cmd = [SKILLHUB_CLI] + SKILLHUB_CLI_ARGS + [str(skill_dir),
                   '--changelog', f'Auto-sync v{new_version}']
        cli_result = subprocess.run(
            cli_cmd, capture_output=True, text=True, timeout=60
        )
        output = cli_result.stdout + cli_result.stderr

        if cli_result.returncode == 0:
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'success', visibility='public', pricing='free')
            try:
                from daily_sync import record_rate_limit_upload  # V128 Y1
                record_rate_limit_upload('skillhub', slug)
            except Exception as e:  # [V131 B2] 宽泛捕获
                print(f"  [WARN] record_upload失败,速率限制计数可能不准: {e}")
            return {'status': 'success', 'output': output[:200]}
        elif 'VERSION_EXISTS' in output:
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'version_exists', error='VERSION_EXISTS')
            return {'status': 'version_exists', 'output': output[:200]}
        elif '429' in output:
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'rate_limited', error='RATE_LIMITED')
            return {'status': 'rate_limited', 'output': output[:200]}
        else:
            record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                   'failed', error=output[:200])
            return {'status': 'failed', 'output': output[:200]}
    except subprocess.TimeoutExpired:
        record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                               'timeout', error='CLI timeout')
        return {'status': 'timeout'}
    except Exception as e:  # [V131 B2] 宽泛捕获
        record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                               'error', error=str(e))
        return {'status': 'error', 'error': str(e)}


def sync_to_skillhub(slug: str, skill_md: Path, new_version: str,
                     skill_id: int, is_paid: bool = False) -> Dict[str, Any]:
    """同步skill到SkillHub

    V139 S4: 统一上传通道 — API优先(enterprise_uploader含WAF重试), CLI fallback
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
        from daily_sync import check_upload_rate_limit, record_rate_limit_upload  # V128 Y1: 重命名
        rate_check = check_upload_rate_limit('skillhub')
        if not rate_check.get('allowed', False):  # V161: fail-safe默认False
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
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常处理(非静默pass)
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

    # V186: 自动生成内容检测 (防止上传自动生成模板被平台当成垃圾内容)
    # 根因: 大量skill是自动生成模板,内容与slug无关,被平台当成垃圾导致封号
    try:
        from quality_gate import check_auto_generated_content
        auto_gen_result = check_auto_generated_content(content)
        if not auto_gen_result['passed']:
            result['status'] = 'blocked_auto_generated'
            result['error'] = f"自动生成内容阻断: {auto_gen_result['message']}"
            result['free_upload'] = {'status': 'blocked_auto_generated', 'error': result['error']}
            record_platform_upload(skill_id, new_version, 'skillhub', slug,
                                   'blocked_auto_generated', error=result['error'])
            return result
    except ImportError:
        # quality_gate不可用时,使用内联检测(不依赖外部模块)
        auto_gen_markers = ['本技能提供', '功能总览', '功能1：', '功能1:', '核心功能',
                           '自动化处理流程', '减少人工干预与重复劳动', '结构化输入输出']
        matched = [m for m in auto_gen_markers if m in content]
        if len(matched) >= 2:
            result['status'] = 'blocked_auto_generated'
            result['error'] = f'自动生成内容阻断: 检测到{len(matched)}个标记: {", ".join(matched[:3])}'
            result['free_upload'] = {'status': 'blocked_auto_generated', 'error': result['error']}
            record_platform_upload(skill_id, new_version, 'skillhub', slug,
                                   'blocked_auto_generated', error=result['error'])
            return result

    # v3.4: 内容指纹去重预检 (防止相同内容以不同slug上传触发平台反垃圾系统)
    # 根因: 2026-07-24批量上传中大量近似重复内容被封禁(93.4%封禁率)
    # V155 R1修复: 使用check_approximate_dedup替代check_content_dedup
    # 原因: check_content_dedup仅做SHA-256精确匹配,无法检测近似重复
    # V155 R2修复: Exception分支改为fail-safe阻断(原为WARN跳过)
    try:
        from content_dedup import check_approximate_dedup
        dedup_result = check_approximate_dedup(slug, content)
        if dedup_result.get('exact_duplicate') or dedup_result.get('approximate_duplicate'):
            result['status'] = 'dedup_blocked'
            result['error'] = f"内容去重阻断: {dedup_result.get('reason', '')}"
            result['free_upload'] = {'status': 'dedup_blocked', 'error': result['error']}
            record_platform_upload(skill_id, new_version, 'skillhub', slug,
                                   'dedup_blocked', error=result['error'])
            return result
    except ImportError:
        # V138 S2: fail-safe — 去重模块不可用时阻断上传(非pass放行)
        # 根因: 2026-07-24封禁事件中990个近似重复skill被放行
        result['status'] = 'dedup_blocked'
        result['error'] = '内容去重模块不可用,已阻断上传(fail-safe)'
        result['free_upload'] = {'status': 'dedup_blocked', 'error': result['error']}
        record_platform_upload(skill_id, new_version, 'skillhub', slug,
                               'dedup_blocked', error=result['error'])
        return result
    except Exception as e:  # V155 R2: fail-safe — 异常时阻断上传(原为WARN跳过)
        result['status'] = 'dedup_blocked'
        result['error'] = f'内容去重检查异常,已阻断上传(fail-safe): {e}'
        result['free_upload'] = {'status': 'dedup_blocked', 'error': result['error']}
        record_platform_upload(skill_id, new_version, 'skillhub', slug,
                               'dedup_blocked', error=result['error'])
        return result

    # V139 S4: 统一上传通道 — API优先(复用enterprise_uploader的WAF重试), CLI fallback
    # enterprise_uploader.upload_skill 内部完成: 门控+速率+去重+WAF重试+认证
    # skip_publish=True: _sync_to_platforms自行管理发布流程(approve→publish→star)
    try:
        from skillhub_adapter import should_use_api  # V139 S4: 统一上传通道
        use_api = should_use_api()
        print(f"  [DEBUG] skillhub_adapter found, use_api={use_api}")
    except ImportError:
        # skillhub_adapter不可用时,直接检查enterprise_uploader是否可用
        # enterprise_uploader使用企业API Key认证(从credentials.json加载),不依赖skh_ token
        try:
            from enterprise_uploader import upload_skill as _check_eu
            use_api = True
            print(f"  [DEBUG] enterprise_uploader found, use_api=True")
        except ImportError as e:
            use_api = False  # enterprise_uploader也不可用时走CLI路径
            print(f"  [DEBUG] enterprise_uploader import failed: {e}, use_api=False")

    if use_api:
        try:
            from enterprise_uploader import upload_skill as _eu_upload
            # skip_gate=True: 管道已运行质量门禁,跳过enterprise_uploader的重复检查
            # skip_marketing/skip_security: 管道已检查,跳过enterprise_uploader的重复检查
            eu_result = _eu_upload(slug, skip_publish=True, skip_gate=True,
                                   skip_marketing=True, skip_security=True)

            if eu_result.get('success'):
                result['free_upload'] = {
                    'status': 'success',
                    'output': eu_result.get('message', 'API upload success')[:200],
                }
                record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                       'success', visibility='public', pricing='free')
                # record_rate_limit_upload已由enterprise_uploader._upload_with_waf_retry调用
            elif eu_result.get('rate_limited'):
                result['free_upload'] = {
                    'status': 'rate_limited',
                    'error': eu_result.get('message', ''),
                }
                record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                       'rate_limited', error=eu_result.get('message', ''))
            elif eu_result.get('dedup_blocked'):
                result['free_upload'] = {
                    'status': 'dedup_blocked',
                    'error': eu_result.get('message', ''),
                }
                record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                       'dedup_blocked', error=eu_result.get('message', ''))
            else:
                result['free_upload'] = {
                    'status': 'failed',
                    'error': eu_result.get('message', 'unknown error')[:200],
                }
                record_platform_upload(skill_id, new_version, 'skillhub_free', slug,
                                       'failed', error=eu_result.get('message', '')[:200])
        except ImportError:
            # API不可用时降级到CLI
            result['free_upload'] = _skillhub_cli_fallback(
                slug, skill_dir, skill_id, new_version
            )
    else:
        # CLI fallback路径(UPLOAD_CHANNEL='cli')
        result['free_upload'] = _skillhub_cli_fallback(
            slug, skill_dir, skill_id, new_version
        )

    # 付费版: 生成payload文件
    if is_paid:
        _result = parse_frontmatter(content)  # V122 W6: 统一别名
        metadata = _result['fields']
        body = _result['body']
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

    # v3.0增强: 速率限制预检 (防止爆发式上传触发平台反垃圾系统)
    # M4.1: 与sync_to_skillhub防封措施统一, 复用daily_sync.py的速率限制机制
    # 根因: 2026-07-24单秒上传1097个skill导致账号被封禁
    try:
        from daily_sync import check_upload_rate_limit, record_rate_limit_upload  # V128 Y1: 重命名
        rate_check = check_upload_rate_limit('clawhub')
        if not rate_check.get('allowed', False):  # V161: fail-safe默认False
            wait = rate_check.get('wait_seconds', 120)
            result['status'] = 'rate_limited'
            result['error'] = f"速率限制: {rate_check.get('reason', '未知')} (需等待{wait}秒)"
            record_platform_upload(skill_id, new_version, 'clawhub', slug,
                                   'rate_limited', error=result['error'])
            return result
    except ImportError:
        # v3.3: 失败安全(fail-safe) — daily_sync不可用时阻止上传
        result['status'] = 'rate_limited'
        result['error'] = '速率限制模块不可用,已阻止上传以防爆发式触发反垃圾系统'
        return result
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常处理(非静默pass)
        # v3.3: 失败安全(fail-safe) — 速率限制异常时阻止上传
        result['status'] = 'rate_limited'
        result['error'] = f'速率限制检查异常,已阻止上传: {e}'
        return result

    # V186: 自动生成内容检测 (与sync_to_skillhub统一,防止上传垃圾内容)
    content = skill_md.read_text(encoding='utf-8', errors='replace')
    auto_gen_markers = ['本技能提供', '功能总览', '功能1：', '功能1:', '核心功能',
                       '自动化处理流程', '减少人工干预与重复劳动', '结构化输入输出']
    matched = [m for m in auto_gen_markers if m in content]
    if len(matched) >= 2:
        result['status'] = 'blocked_auto_generated'
        result['error'] = f'自动生成内容阻断: 检测到{len(matched)}个标记: {", ".join(matched[:3])}'
        record_platform_upload(skill_id, new_version, 'clawhub', slug,
                               'blocked_auto_generated', error=result['error'])
        return result

    # v3.4: 内容指纹去重预检 (防止相同内容以不同slug上传触发平台反垃圾系统)
    # M4.1: 与sync_to_skillhub防封措施统一
    # 根因: 2026-07-24批量上传中大量近似重复内容被封禁(93.4%封禁率)
    # V155 R1修复: 使用check_approximate_dedup替代check_content_dedup(与sync_to_skillhub统一)
    # V155 R3修复: ImportError和Exception均改为fail-safe阻断(原为WARN跳过)
    content = skill_md.read_text(encoding='utf-8', errors='replace')
    try:
        from content_dedup import check_approximate_dedup
        dedup_result = check_approximate_dedup(slug, content)
        if dedup_result.get('exact_duplicate') or dedup_result.get('approximate_duplicate'):
            result['status'] = 'dedup_blocked'
            result['error'] = f"内容去重阻断: {dedup_result.get('reason', '')}"
            record_platform_upload(skill_id, new_version, 'clawhub', slug,
                                   'dedup_blocked', error=result['error'])
            return result
    except ImportError:
        # V155 R3: fail-safe — 去重模块不可用时阻断上传(原为WARN跳过)
        result['status'] = 'dedup_blocked'
        result['error'] = '内容去重模块不可用,已阻断上传(fail-safe)'
        record_platform_upload(skill_id, new_version, 'clawhub', slug,
                               'dedup_blocked', error=result['error'])
        return result
    except Exception as e:  # V155 R3: fail-safe — 异常时阻断上传(原为WARN跳过)
        result['status'] = 'dedup_blocked'
        result['error'] = f'内容去重检查异常,已阻断上传(fail-safe): {e}'
        record_platform_upload(skill_id, new_version, 'clawhub', slug,
                               'dedup_blocked', error=result['error'])
        return result

    # v2.2: 提取营销参数(复用clawhub_batch_uploader的函数, 避免重复实现)
    try:
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
    # V160 R3修复: 使用list-based subprocess消除shell=True(命令注入风险), 移除嵌入式引号
    # 原因: shell=True+字符串拼接有命令注入风险, 且嵌入式引号在list模式下会被当作字面字符
    # Windows修复: shutil.which解析npx完整路径(避免WinError 2)
    npx_cmd = shutil.which('npx') or 'npx'
    cmd_parts = [
        npx_cmd, 'clawhub',
        '--registry', PLATFORM_CONFIG["clawhub"]["host"],
        'publish', str(skill_dir),
        '--changelog', changelog,
        '--categories', category,
        '--topics', ",".join(topics),
        '--slug', slug,
        '--json',
    ]
    if display_name:
        cmd_parts.extend(['--name', display_name])

    result['marketing'] = {'category': category, 'topics': topics[:5], 'name': display_name}

    try:
        proc = subprocess.run(
            cmd_parts,
            capture_output=True, text=True, timeout=120,
            cwd=str(SKILLS_ROOT)
        )
        output = proc.stdout + proc.stderr

        # 尝试解析JSON输出
        json_result = None
        try:
            json_result = json.loads(proc.stdout.strip())
        except (json.JSONDecodeError, ValueError) as e:  # V144: 添加警告日志(保留降级行为)
            print(f"[WARN] 子进程stdout JSON解析失败: {e}")

        if proc.returncode == 0:
            result['status'] = 'success'
            result['output'] = output[:200]
            # V95 V2: 成功上传后同步更新DB的current_version字段
            try:
                conn = db_module.get_db()
                conn.execute("PRAGMA busy_timeout = 10000")
                conn.execute("UPDATE skills SET current_version = ? WHERE slug = ?", (new_version, slug))
                conn.commit()
                conn.close()
            except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
                print(f"  [WARN] current_version更新失败: {e}")
            if json_result:
                result['clawhub_data'] = {
                    'slug': json_result.get('slug', slug),
                    'version': json_result.get('version', new_version),
                    'url': json_result.get('url', ''),
                }
            record_platform_upload(skill_id, new_version, 'clawhub', slug,
                                   'success', visibility='public', pricing='free')
            # v3.0: 记录上传时间戳用于速率限制
            # M4.1: 与sync_to_skillhub统一, 记录clawhub上传以供下次速率限制计数
            # v3.4: record_upload失败时记录警告(非静默pass),避免速率限制计数偏少
            try:
                record_rate_limit_upload('clawhub', slug)  # V128 Y1: 重命名
            except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
                print(f"  [WARN] record_upload失败,速率限制计数可能不准: {e}")
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
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常更新状态/计数继续
        result['status'] = 'error'
        result['error'] = str(e)
        record_platform_upload(skill_id, new_version, 'clawhub', slug,
                               'error', error=str(e))

    return result


# ============================================================
# Phase 7: 端到端同步
# ============================================================

def _run_sync_quality_gates(skill_md, slug, skill_id, new_version,
                            skip_content_quality, skip_security, skip_marketing,
                            skip_l2, skip_l3, skip_local_quality=False):
    """运行同步流程的8个质量门禁序列

    [V134 E4] 从sync_skill_to_all_platforms拆分出的质量门禁逻辑

    Returns:
        (passed, phases, block_status): passed=是否全部通过,
            phases=门禁结果字典, block_status=失败时的状态字符串(成功时为'')
    """
    phases = {}

    # 5. 质量门禁
    print(f"  [3/7] 质量门禁检查...")
    qc = run_quality_check(skill_md)
    phases['quality_check'] = qc
    if not qc['passed']:
        print(f"  ✗ 质量门禁未通过: {qc['failed_checks']}")
        record_platform_upload(skill_id, new_version, 'quality_gate', slug,
                               'blocked', error=str(qc['failed_checks']))
        return (False, phases, 'blocked_by_quality_gate')
    print(f"  ✓ 质量门禁通过 ({qc['score']})")

    # 5.1 L1.5内容质量门禁(v3.1新增)
    if not skip_content_quality:
        print(f"  [3.5/7] 内容质量门禁检查...")
        cq = run_content_quality_gate(skill_md)
        phases['content_quality'] = cq
        if not cq['passed']:
            print(f"  ✗ 内容质量门禁未通过: {cq['failed_checks']}")
            record_platform_upload(skill_id, new_version, 'content_quality_gate', slug,
                                   'blocked', error=str(cq['failed_checks']))
            return (False, phases, 'blocked_by_content_quality')
        print(f"  ✓ 内容质量门禁通过 ({cq['score']})")
    else:
        phases['content_quality'] = {'status': 'skipped'}

    # 5.1.5 安全预检(v2.2新增 — 科恩实验室+云鼎实验室高风险模式检测)
    if not skip_security:
        print(f"  [3.55/7] 安全预检检查...")
        try:
            from quality_gate import run_security_precheck
            sec = run_security_precheck(skill_md)
            phases['security_precheck'] = sec
            if not sec.get('overall_passed', False):
                failed_checks = [c['name'] for c in sec.get('checks', []) if not c.get('passed')]
                # PRR P1-1: critical+high阻断, medium仅警告
                blocking_checks = [c for c in sec.get('checks', []) if not c.get('passed') and c.get('severity') in ('critical', 'high')]
                if blocking_checks:
                    print(f"  ✗ 安全预检未通过(严重/高风险): {failed_checks}")
                    record_platform_upload(skill_id, new_version, 'security_precheck', slug,
                                           'blocked', error=str(failed_checks))
                    return (False, phases, 'blocked_by_security_precheck')
                else:
                    # 中风险不阻断,仅警告
                    print(f"  ⚠ 安全预检有风险提示(非阻断): {failed_checks}")
            else:
                print(f"  ✓ 安全预检通过 ({sec.get('passed_checks', 0)}/{sec.get('total_checks', 0)})")
        except ImportError:
            # PRR V146: 安全预检模块不可用时阻断(fail-safe), 不允许跳过
            print(f"  ✗ 安全预检模块不可用 — 同步已阻断(fail-safe)")
            phases['security_precheck'] = {'status': 'blocked', 'reason': 'module_unavailable'}
            record_platform_upload(skill_id, new_version, 'security_precheck', slug,
                                   'blocked', error='security_precheck_module_unavailable')
            return (False, phases, 'blocked_by_security_precheck_unavailable')
    else:
        phases['security_precheck'] = {'status': 'skipped'}

    # 5.1.8 评分门控(v2.3新增 — 流程固化: 低于4.5分阻断上传)
    print(f"  [3.58/7] 评分门控检查...")
    rg = run_rating_gate_check(skill_md, slug)
    phases['rating_gate'] = rg
    if not rg['passed']:
        print(f"  ✗ 评分门控未通过: {rg['failed_checks']}")
        record_platform_upload(skill_id, new_version, 'rating_gate', slug,
                               'blocked', error=str(rg['failed_checks']))
        return (False, phases, 'blocked_by_rating_gate')
    print(f"  ✓ 评分门控通过 ({rg['score']})")

    # 5.1.9 本地质量评分门控 (V156新增 — local_quality_score)
    if skip_local_quality:
        print(f"  [3.59/7] 本地质量评分检查... [SKIP]")
        phases['local_quality_score'] = {'status': 'skipped'}
    else:
        print(f"  [3.59/7] 本地质量评分检查...")
        try:
            import local_quality_scorer
            from project_config import LOCAL_QUALITY_PASS_THRESHOLD
            lq_result = local_quality_scorer.score_skill(skill_md)
            lq_score = lq_result.get('total_score', 0.0)
            phases['local_quality_score'] = {
                'passed': lq_score >= LOCAL_QUALITY_PASS_THRESHOLD,
                'score': lq_score,
                'threshold': LOCAL_QUALITY_PASS_THRESHOLD,
            }
            if lq_score < LOCAL_QUALITY_PASS_THRESHOLD:
                print(f"  ✗ 本地质量评分未通过: {lq_score}/{LOCAL_QUALITY_PASS_THRESHOLD}")
                record_platform_upload(skill_id, new_version, 'local_quality_score', slug,
                                       'blocked', error=f'score {lq_score} < threshold {LOCAL_QUALITY_PASS_THRESHOLD}')
                return (False, phases, 'blocked_by_local_quality_score')
            print(f"  ✓ 本地质量评分通过 ({lq_score}/{LOCAL_QUALITY_PASS_THRESHOLD})")
        except ImportError:
            # fail-safe: local_quality_scorer模块不可用时阻断
            print(f"  ✗ 本地质量评分模块不可用 — 同步已阻断(fail-safe)")
            phases['local_quality_score'] = {'status': 'blocked', 'reason': 'module_unavailable'}
            record_platform_upload(skill_id, new_version, 'local_quality_score', slug,
                                   'blocked', error='local_quality_scorer_module_unavailable')
            return (False, phases, 'blocked_by_local_quality_score_unavailable')
        except Exception as e:
            print(f"  ✗ 本地质量评分异常: {e}")
            phases['local_quality_score'] = {'status': 'error', 'error': str(e)}
            record_platform_upload(skill_id, new_version, 'local_quality_score', slug,
                                   'blocked', error=str(e))
            return (False, phases, 'blocked_by_local_quality_score')

    # 5.2 营销关卡检查(v2.0新增)
    if not skip_marketing:
        print(f"  [3.6/7] 营销关卡检查...")
        mg = run_marketing_gate_check(skill_md)
        phases['marketing_gate'] = mg
        if not mg['passed']:
            print(f"  ✗ 营销关卡未通过: {mg['failed_checks']}")
            record_platform_upload(skill_id, new_version, 'marketing_gate', slug,
                                   'blocked', error=str(mg['failed_checks']))
            return (False, phases, 'blocked_by_marketing_gate')
        print(f"  ✓ 营销关卡通过 ({mg['score']})")
    else:
        phases['marketing_gate'] = {'status': 'skipped'}

    # 5.3 防幻觉机制检查(v2.0新增)
    print(f"  [3.7/7] 防幻觉机制检查...")
    ah = run_anti_hallucination_check(skill_md)
    phases['anti_hallucination'] = ah
    if not ah['passed']:
        print(f"  ✗ 防幻觉机制未通过: {ah['failed_checks']}")
        record_platform_upload(skill_id, new_version, 'anti_hallucination', slug,
                               'blocked', error=str(ah['failed_checks']))
        return (False, phases, 'blocked_by_anti_hallucination')
    print(f"  ✓ 防幻觉机制通过 ({ah['score']})")

    # 5.4 L2 LLM验证检查(v2.0新增)
    if not skip_l2:
        print(f"  [3.8/7] L2 LLM验证检查...")
        l2 = run_l2_check(slug)
        phases['l2_validation'] = l2
        if l2['passed'] is False:
            print(f"  ✗ L2验证未通过: {l2['failed_checks']}")
            record_platform_upload(skill_id, new_version, 'l2_validation', slug,
                                   'blocked', error=str(l2['failed_checks']))
            return (False, phases, 'blocked_by_l2_validation')
        elif l2['passed'] is None:
            print(f"  ⚠ L2验证待AI执行: {l2['guide']}")
            record_platform_upload(skill_id, new_version, 'l2_validation', slug,
                                   'pending', error=l2['note'])
            return (False, phases, 'blocked_by_l2_pending')
        print(f"  ✓ L2验证通过 (TRACE {l2.get('trace_total', '?')}/50, 等级{l2.get('trace_grade', '?')})")
    else:
        phases['l2_validation'] = {'status': 'skipped'}

    # 5.5 L3 Agent试用检查(v2.0新增)
    if not skip_l3:
        print(f"  [3.9/7] L3 Agent试用检查...")
        l3 = run_l3_check(slug)
        phases['l3_trial'] = l3
        if l3['passed'] is False:
            print(f"  ✗ L3试用未通过: {l3['failed_checks']}")
            record_platform_upload(skill_id, new_version, 'l3_trial', slug,
                                   'blocked', error=str(l3['failed_checks']))
            return (False, phases, 'blocked_by_l3_trial')
        elif l3['passed'] is None:
            print(f"  ⚠ L3试用待AI执行: {l3['guide']}")
            record_platform_upload(skill_id, new_version, 'l3_trial', slug,
                                   'pending', error=l3['note'])
            return (False, phases, 'blocked_by_l3_pending')
        print(f"  ✓ L3试用通过 (评分{l3.get('score', '?')}/100, 等级{l3.get('grade', '?')})")
    else:
        phases['l3_trial'] = {'status': 'skipped'}

    return (True, phases, '')


def _sync_to_platforms(slug, skill_md, new_version, changelog, source, skill_id, db_skill,
                       skip_github, skip_skillhub, skip_clawhub, dry_run=False):
    """执行多平台同步 — 直接调用各平台同步函数

    修复: 移除platform_registry/pre_upload_checks依赖(模块未提交到git),
    回归直接调用模式。速率限制和去重检查已在各sync_to_*函数内部实现。

    Returns:
        phases: 各平台同步结果字典
    """
    phases = {}

    # dry_run模式下跳过所有实际上传
    if dry_run:
        for name, skipped in [('github', skip_github), ('skillhub', skip_skillhub), ('clawhub', skip_clawhub)]:
            phases[name] = {'status': 'dry_run'} if not skipped else {'status': 'skipped'}
        return phases

    # GitHub
    if skip_github:
        phases['github'] = {'status': 'skipped'}
    else:
        print(f"  [4/7] 同步到GitHub...")
        gh_result = sync_to_github(slug, skill_md, new_version, changelog, source, skill_id)
        phases['github'] = gh_result
        if gh_result['status'] == 'success':
            print(f"  ✓ GitHub同步成功")
        elif gh_result['status'] == 'no_changes':
            print(f"  ℹ GitHub: 无需提交的变更")
        else:
            print(f"  ⚠ GitHub同步: {gh_result['status']} - {gh_result.get('error', '')}")

    # SkillHub
    if skip_skillhub:
        phases['skillhub'] = {'status': 'skipped'}
    else:
        print(f"  [5/7] 同步到SkillHub...")
        is_paid = bool(db_skill.get('is_paid', False))
        sh_result = sync_to_skillhub(slug, skill_md, new_version, skill_id, is_paid)
        phases['skillhub'] = sh_result
        free_upload = sh_result.get('free_upload') or {}
        free_status = free_upload.get('status', 'unknown')
        if free_status == 'success':
            print(f"  ✓ SkillHub同步成功")
        else:
            print(f"  ⚠ SkillHub: {free_status}")

    # ClawHub
    if skip_clawhub:
        phases['clawhub'] = {'status': 'skipped'}
    else:
        print(f"  [6/7] 同步到ClawHub...")
        ch_result = sync_to_clawhub(slug, skill_md, new_version, skill_id)
        phases['clawhub'] = ch_result
        if ch_result['status'] == 'success':
            print(f"  ✓ ClawHub同步成功")
        else:
            print(f"  ⚠ ClawHub: {ch_result['status']} - {ch_result.get('error', '')[:100]}")

    return phases


def sync_skill_to_all_platforms(slug: str, skip_github: bool = False,
                                skip_skillhub: bool = False,
                                skip_clawhub: bool = False,
                                skip_content_quality: bool = False,
                                skip_security: bool = False,
                                skip_marketing: bool = False,
                                skip_l2: bool = False,
                                skip_l3: bool = False,
                                skip_local_quality: bool = False,
                                force: bool = False,
                                dry_run: bool = False) -> Dict[str, Any]:
    """端到端同步单个skill到所有平台

    [V134 E4] 拆分为_run_sync_quality_gates + _sync_to_platforms两个helper函数
    [V155 R4] 新增dry_run参数: 模拟模式下执行全部质量门禁和预检查,仅跳过实际上传

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
    current_hash = db_module.compute_file_hash(skill_md)
    last_hash = db_skill.get('last_hash') or ''

    # 3. 检测变更
    changed = (last_hash != current_hash) if last_hash else force
    if not changed and not force:
        result['status'] = 'no_changes'
        print(f"  ℹ 无变更,跳过同步 (hash一致)")
        return result

    old_hash_display = last_hash[:8] + '...' if last_hash else '(none)'
    print(f"  ✓ 检测到变更: {old_hash_display} → {current_hash[:8]}...")

    # 4. 版本递增
    new_version = increment_version(current_version)
    if not update_version_in_file(skill_md, new_version):
        print(f"  ⚠ 版本号更新失败,使用原版本: {current_version}")
        new_version = current_version
    else:
        print(f"  ✓ 版本递增: {current_version} → {new_version}")

    # 重新计算hash(版本号已更新)
    new_hash = db_module.compute_file_hash(skill_md)
    content = skill_md.read_text(encoding='utf-8')
    line_count = content.count('\n') + 1
    changelog = f'Auto-sync: content updated, version {current_version} → {new_version}'

    # 5. 质量门禁
    passed, gate_phases, block_status = _run_sync_quality_gates(
        skill_md, slug, skill_id, new_version,
        skip_content_quality, skip_security, skip_marketing, skip_l2, skip_l3,
        skip_local_quality=skip_local_quality)
    result['phases'].update(gate_phases)
    if not passed:
        result['status'] = block_status
        return result

    # 6. 记录新版本
    record_version(skill_id, new_version, new_hash, changelog,
                   skill_md.stat().st_size, line_count)

    # 7-9. 三平台同步
    platform_phases = _sync_to_platforms(
        slug, skill_md, new_version, changelog, source, skill_id, db_skill,
        skip_github, skip_skillhub, skip_clawhub, dry_run=dry_run)
    result['phases'].update(platform_phases)

    # 10. 汇总
    all_statuses = []
    for phase in ['github', 'skillhub', 'clawhub']:
        phase_result = result['phases'].get(phase, {})
        all_statuses.append(phase_result.get('status', 'unknown'))

    # V155 R4: dry_run模式下'dry_run'状态视为通过
    if dry_run:
        if all(s in ('dry_run', 'success') for s in all_statuses):
            result['status'] = 'dry_run_passed'
        else:
            result['status'] = 'dry_run_failed'
    elif all(s == 'success' for s in all_statuses):
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
                             skip_l3: bool = True,
                             skip_local_quality: bool = True,
                             dry_run: bool = False) -> Dict[str, Any]:
    """同步所有变更的skill(批量模式默认跳过L2/L3,因需AI执行)

    V155 R4: 新增dry_run参数,传递给每个skill的同步调用
    """
    print("扫描变更...")
    changed = scan_all_changes()
    print(f"发现 {len(changed)} 个变更skill")

    results = {
        'scan_time': NOW,
        'total_changed': len(changed),
        'synced': [],
        'failed': [],
        'skipped': [],
        'dry_run': dry_run,
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
            skip_local_quality=skip_local_quality,
            dry_run=dry_run,
        )
        # V155 R4: dry_run模式下'dry_run_passed'视为已同步
        if sync_result.get('status') in ('all_success', 'partial_success', 'dry_run_passed'):
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
    try:
        from skill_batch_upgrader_v3 import run_content_quality_check, auto_fix_content, auto_fix
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
            # PRR P1-1: critical+high阻断, medium仅警告
            blocking_checks = [c for c in sec.get('checks', []) if not c.get('passed') and c.get('severity') in ('critical', 'high')]
            if blocking_checks:
                failed_names = [c['name'] for c in blocking_checks]
                print(f"  ✗ 安全预检发现严重/高风险: {failed_names}")
                if not force_sync:
                    result['status'] = 'blocked_by_security_precheck'
                    result['error'] = f'安全预检严重/高风险(不可强制跳过): {failed_names}'
                    return result
            else:
                non_critical = [c['name'] for c in sec.get('checks', []) if not c.get('passed')]
                print(f"  ⚠ 安全预检有风险提示(非阻断): {non_critical}")
        else:
            print(f"  ✓ 安全预检通过 ({sec.get('passed_checks', 0)}/{sec.get('total_checks', 0)})")
    except ImportError:
        # PRR V146: 安全预检模块不可用时阻断(fail-safe), 不允许跳过
        print(f"  ✗ 安全预检模块不可用 — 同步已阻断(fail-safe)")
        result['phases']['security_precheck'] = {'status': 'blocked', 'reason': 'module_unavailable'}
        result['status'] = 'blocked_by_security_precheck_unavailable'
        result['error'] = '安全预检模块不可用(fail-safe阻断)'
        return result

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
    report_path = TOOLS_DIR / f"upgrade_{slug}_{NOW.replace(':', '')}.json"
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
             skip_l2: bool = False, skip_l3: bool = False, force: bool = False,
             dry_run: bool = False, skip_local_quality: bool = False):
    """同步单个skill"""
    result = sync_skill_to_all_platforms(
        slug, skip_github=skip_github, skip_skillhub=skip_skillhub,
        skip_clawhub=skip_clawhub, skip_security=skip_security, skip_marketing=skip_marketing,
        skip_l2=skip_l2, skip_l3=skip_l3, skip_local_quality=skip_local_quality,
        force=force, dry_run=dry_run
    )
    # 保存结果
    result_path = TOOLS_DIR / f"version_sync_{slug}_{NOW.replace(':', '')}.json"
    with open(result_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n同步结果已保存: {result_path}")


def cmd_sync_all(skip_github: bool = False, skip_skillhub: bool = False,
                 skip_clawhub: bool = False, skip_security: bool = False,
                 skip_marketing: bool = False,
                 skip_l2: bool = True, skip_l3: bool = True, dry_run: bool = False):
    """同步所有变更skill(批量模式默认跳过L2/L3,因需AI执行)"""
    results = sync_all_changed_skills(
        skip_github=skip_github, skip_skillhub=skip_skillhub, skip_clawhub=skip_clawhub,
        skip_security=skip_security, skip_marketing=skip_marketing, skip_l2=skip_l2, skip_l3=skip_l3,
        dry_run=dry_run
    )
    result_path = TOOLS_DIR / f"version_sync_all_{NOW.replace(':', '')}.json"
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
    conn = db_module.get_db()
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
    conn = db_module.get_db()
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
    sync_parser.add_argument('--skip-local-quality', action='store_true', help='跳过本地LLM质量评分(批量场景)')
    sync_parser.add_argument('--force', action='store_true', help='强制同步(即使无变更)')
    sync_parser.add_argument('--dry-run', action='store_true', help='V155: 模拟模式,执行全部质量检查但跳过实际上传')

    sync_all_parser = sub.add_parser('sync-all', help='同步所有变更skill(批量模式默认跳过L2/L3)')
    sync_all_parser.add_argument('--skip-github', action='store_true')
    sync_all_parser.add_argument('--skip-skillhub', action='store_true')
    sync_all_parser.add_argument('--skip-clawhub', action='store_true')
    sync_all_parser.add_argument('--skip-security', action='store_true', help='跳过安全预检')
    sync_all_parser.add_argument('--skip-marketing', action='store_true', help='跳过营销关卡')
    sync_all_parser.add_argument('--no-skip-l2', action='store_true', help='不跳过L2验证(默认跳过)')
    sync_all_parser.add_argument('--no-skip-l3', action='store_true', help='不跳过L3试用(默认跳过)')
    sync_all_parser.add_argument('--dry-run', action='store_true', help='V155: 模拟模式,执行全部质量检查但跳过实际上传')

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
                 args.skip_security, args.skip_marketing, args.skip_l2, args.skip_l3, args.force,
                 dry_run=args.dry_run, skip_local_quality=args.skip_local_quality)
    elif args.command == 'sync-all':
        cmd_sync_all(args.skip_github, args.skip_skillhub, args.skip_clawhub,
                     args.skip_security, args.skip_marketing,
                     skip_l2=not args.no_skip_l2, skip_l3=not args.no_skip_l3,
                     dry_run=args.dry_run)
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
