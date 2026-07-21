#!/usr/bin/env python3
"""
skill-registry 统一配置
======================
集中管理所有路径常量、阈值和共享逻辑，消除硬编码。
所有模块从此文件导入配置。

修复问题：U-21（硬编码路径）、U-23（阈值不一致）、U-24（付费判断不一致）
"""

import os
import tempfile
from pathlib import Path

# ============ 路径配置 ============

# 项目根目录：优先从环境变量获取，默认为skill-registry的父目录
PROJECT_ROOT = Path(os.environ.get(
    'SKILL_REGISTRY_ROOT',
    r'd:\skills'
))

# 数据库路径
DB_PATH = str(PROJECT_ROOT / "skill-registry.db")

# 注册表目录（脚本所在目录）
REGISTRY_DIR = PROJECT_ROOT / "skill-registry"

# Packaged Skills 目录
PACKAGED_SKILLS_DIR = PROJECT_ROOT / "packaged-skills" / "skillhub"
OPENSOURCE_SKILLS_DIR = PROJECT_ROOT / "opensource-skills" / "packaged"

# 市场数据目录
MARKET_DATA_DIR = REGISTRY_DIR / "market-data"

# 导出目录（使用系统临时目录，不再硬编码用户路径）
EXPORT_DIR = Path(os.environ.get(
    'SKILL_REGISTRY_EXPORT_DIR',
    os.path.join(tempfile.gettempdir(), 'skill-registry-exports')
))
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# 备份目录
BACKUP_DIR = REGISTRY_DIR / "backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# 报告目录
REPORT_DIR = REGISTRY_DIR

# ============ TRACE评分阈值（统一） ============

TRACE_PASS_THRESHOLD = 42        # TRACE评分通过阈值（统一为42，修复U-23）
TRACE_GRADE_A_PLUS = 45          # A+级阈值
TRACE_GRADE_A = 42               # A级阈值
TRACE_GRADE_B = 35               # B级阈值
TRACE_GRADE_C = 28               # C级阈值

# L2评分分层阈值 (Round 09 Step 5.4优化项4)
# 区分"最低通过"和"优秀"两个层次, 解决计划要求≥35与config设42的矛盾
L2_PASS_THRESHOLD = 35           # L2最低通过阈值 (低于此分需重新生成)
L2_EXCELLENT_THRESHOLD = 45      # L2优秀阈值 (达到此分可跳过AI手动优化)
L2_MANUAL_REVIEW_THRESHOLD = 40  # L2需AI手动优化的阈值 (低于此分标注需优化)

# L3评分阈值
L3_PASS_THRESHOLD = 70           # L3试运行通过阈值 (百分制)

# ============ 门控阈值 ============

MIN_TRACE_SCORE = TRACE_PASS_THRESHOLD  # 门控最低评分（与TRACE通过阈值一致）
MAX_SKILL_MD_LINES = 500                # SKILL.md最大行数
MIN_SKILL_MD_LINES = 50                 # SKILL.md最小行数
MIN_DESCRIPTION_LEN = 150               # description最小长度
MAX_DESCRIPTION_LEN = 280               # description最大长度
MAX_DISPLAYNAME_LEN = 20                # displayName最大长度
MIN_SUMMARY_LEN = 10                    # summary最小长度
MAX_SUMMARY_LEN = 100                   # summary最大长度

# ============ 付费判断（统一，修复U-24） ============

PAID_LICENSE_KEYWORDS = ['proprietary', 'commercial', 'paid', 'pro', 'enterprise', 'custom']
PAID_EDITION_KEYWORDS = ['pro', 'paid', 'enterprise', 'commercial', 'standard', 'premium']
OPEN_LICENSE_KEYWORDS = ['mit', 'apache', 'gpl', 'bsd', 'mpl', 'unlicense', 'cc0', 'cc-by']

# ============ 数据库表名常量 ============

SCORE_TYPE_TRACE_LLM = 'trace_llm'
SCORE_TYPE_BASELINE = 'baseline'

# ============ TRACE维度到scores表字段映射（修复U-01） ============
# 由于scores表字段名与TRACE维度名不一致，使用此映射保证语义正确
# trust → debranding_score, reliability → quality_score, etc.
TRACE_FIELD_MAPPING = {
    'trust': 'debranding_score',           # Trust分存入debranding_score
    'reliability': 'quality_score',         # Reliability分存入quality_score
    'adaptability': 'practicality_score',   # Adaptability分存入practicality_score
    'convention': 'simplicity_score',       # Convention分存入simplicity_score
    'effectiveness': 'performance_score',   # Effectiveness分存入performance_score
}

# ============ 批量操作安全 ============

MAX_SCAN_PAGES = 100              # 市场扫描最大页数（修复U-27）
BATCH_BACKUP_ENABLED = True       # 批量操作是否自动备份

# ============ 定价范围 ============

MIN_PRICE = 0.99
MAX_PRICE = 99.0


def get_db_connection():
    """获取数据库连接（带row_factory）"""
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def is_paid_skill(license_val: str, edition: str) -> bool:
    """统一付费判断逻辑（修复U-24）
    
    Args:
        license_val: license字段值
        edition: edition字段值
    
    Returns:
        True if 付费skill, False if 免费skill
    """
    license_lower = (license_val or '').lower()
    edition_lower = (edition or '').lower()
    
    # 1. edition明确标注pro/paid/enterprise → 付费
    if any(kw in edition_lower for kw in PAID_EDITION_KEYWORDS):
        return True
    # 2. license为Proprietary/Commercial/Paid → 付费
    if license_val and any(kw in license_lower for kw in PAID_LICENSE_KEYWORDS):
        return True
    # 3. edition为free/community → 免费
    if edition_lower in ['free', 'community', 'opensource', 'open-source']:
        return False
    # 4. license为MIT/Apache等开源协议 → 免费
    if license_val and any(kw in license_lower for kw in OPEN_LICENSE_KEYWORDS):
        return False
    # 5. 默认免费
    return False


def safe_float(val, default=0.0):
    """安全转换为float"""
    try:
        return float(val) if val else default
    except (ValueError, TypeError):
        return default


def safe_int(val, default=0):
    """安全转换为int"""
    try:
        return int(val) if val else default
    except (ValueError, TypeError):
        return default


def create_backup(file_path, backup_dir=None):
    """创建文件备份（修复U-08）
    
    Args:
        file_path: 要备份的文件路径
        backup_dir: 备份目录，默认使用BACKUP_DIR
    
    Returns:
        备份文件路径，失败返回None
    """
    import shutil
    from datetime import datetime
    
    src = Path(file_path)
    if not src.exists():
        return None
    
    bdir = Path(backup_dir) if backup_dir else BACKUP_DIR
    bdir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{src.stem}_{timestamp}{src.suffix}"
    backup_path = bdir / backup_name
    
    try:
        shutil.copy2(src, backup_path)
        return str(backup_path)
    except Exception as e:
        print(f"  备份失败: {e}")
        return None
