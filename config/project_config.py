#!/usr/bin/env python3
"""
项目统一配置中心 - 路径与常量
================================
所有脚本统一从此模块导入路径常量和阈值，消除硬编码。
这是项目唯一的配置真相源（Single Source of Truth）。

使用方式:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
    from project_config import DB_PATH, TOOLS_DIR, DATA_DIR, ...
"""

import os
import tempfile
from pathlib import Path

# ============ 核心路径 ============

# 项目根目录：优先从环境变量获取
PROJECT_ROOT = Path(os.environ.get(
    'SKILLS_PROJECT_ROOT',
    r'd:\skills'
))

# 唯一数据库路径
DB_PATH = str(PROJECT_ROOT / "skill-registry.db")

# ============ 工具与数据目录 ============

# 工具脚本目录（Phase 2后从skill-registry/重命名为tools/）
# Phase 1期间仍指向skill-registry/，Phase 2后改为tools/
TOOLS_DIR = PROJECT_ROOT / "tools"
REGISTRY_DIR = TOOLS_DIR  # 向后兼容别名

# 数据存储目录（Phase 2后创建）
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ============ 产品Skill目录（保持不动） ============

# 免费版 - SkillHub
PACKAGED_SKILLS_DIR = PROJECT_ROOT / "packaged-skills" / "skillhub"

# 免费版 - Hermes公开引流
HERMES_SKILLS_DIR = PROJECT_ROOT / "hermes-skills"

# 开源版
OPENSOURCE_SKILLS_DIR = PROJECT_ROOT / "opensource-skills" / "packaged"

# 付费版 - 企业上传
ENTERPRISE_UPLOAD_DIR = PROJECT_ROOT / "enterprise-upload"

# 源skill - ClawHub下载
CLAWHUB_DOWNLOADED_DIR = PROJECT_ROOT / "clawhub-skills" / "downloaded"

# 差异化skill目录（含免费版和付费版）
DIFFERENTIATED_DIR = PROJECT_ROOT / "differentiated-skills"

# ============ 数据子目录 ============

# 报告目录
REPORT_DIR = DATA_DIR / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# 市场数据目录
MARKET_DATA_DIR = DATA_DIR / "market-data"
MARKET_DATA_DIR.mkdir(parents=True, exist_ok=True)

# 备份目录
BACKUP_DIR = DATA_DIR / "backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# 发现候选数据目录
DISCOVERY_DIR = DATA_DIR / "discovery"
DISCOVERY_DIR.mkdir(parents=True, exist_ok=True)

# 健康报告目录
HEALTH_REPORT_DIR = DATA_DIR / "health_reports"
HEALTH_REPORT_DIR.mkdir(parents=True, exist_ok=True)

# 导出目录（使用系统临时目录）
EXPORT_DIR = Path(os.environ.get(
    'SKILLS_EXPORT_DIR',
    os.path.join(tempfile.gettempdir(), 'skills-exports')
))
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# 凭证目录
CREDENTIALS_DIR = PROJECT_ROOT / ".credentials"
CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)

# ============ TRACE评分阈值（统一） ============

TRACE_PASS_THRESHOLD = 42        # TRACE评分通过阈值
TRACE_GRADE_A_PLUS = 45          # A+级阈值
TRACE_GRADE_A = 42               # A级阈值
TRACE_GRADE_B = 35               # B级阈值
TRACE_GRADE_C = 28               # C级阈值

# L2评分分层阈值
L2_PASS_THRESHOLD = 35           # L2最低通过阈值
L2_EXCELLENT_THRESHOLD = 45      # L2优秀阈值
L2_MANUAL_REVIEW_THRESHOLD = 40  # L2需AI手动优化的阈值

# L3评分阈值
L3_PASS_THRESHOLD = 70           # L3试运行通过阈值（百分制）

# ============ 门控阈值 ============

MIN_TRACE_SCORE = TRACE_PASS_THRESHOLD
MAX_SKILL_MD_LINES = 500
MIN_SKILL_MD_LINES = 50
MIN_DESCRIPTION_LEN = 150
MAX_DESCRIPTION_LEN = 280
MAX_DISPLAYNAME_LEN = 20
MIN_SUMMARY_LEN = 10
MAX_SUMMARY_LEN = 100

# ============ 付费判断（统一） ============

PAID_LICENSE_KEYWORDS = ['proprietary', 'commercial', 'paid', 'pro', 'enterprise', 'custom']
PAID_EDITION_KEYWORDS = ['pro', 'paid', 'enterprise', 'commercial', 'standard', 'premium']
OPEN_LICENSE_KEYWORDS = ['mit', 'apache', 'gpl', 'bsd', 'mpl', 'unlicense', 'cc0', 'cc-by']

# ============ 数据库表名常量 ============

SCORE_TYPE_TRACE_LLM = 'trace_llm'
SCORE_TYPE_BASELINE = 'baseline'

# ============ TRACE维度到scores表字段映射 ============

TRACE_FIELD_MAPPING = {
    'trust': 'debranding_score',
    'reliability': 'quality_score',
    'adaptability': 'practicality_score',
    'convention': 'simplicity_score',
    'effectiveness': 'performance_score',
}

# ============ 批量操作安全 ============

MAX_SCAN_PAGES = 100
BATCH_BACKUP_ENABLED = True

# ============ 定价范围 ============

MIN_PRICE = 0.99
MAX_PRICE = 99.0

# ============ 工具函数 ============


def get_db_connection():
    """获取数据库连接（带row_factory）"""
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def is_paid_skill(license_val: str, edition: str) -> bool:
    """统一付费判断逻辑

    Args:
        license_val: license字段值
        edition: edition字段值

    Returns:
        True if 付费skill, False if 免费skill
    """
    license_lower = (license_val or '').lower()
    edition_lower = (edition or '').lower()

    if any(kw in edition_lower for kw in PAID_EDITION_KEYWORDS):
        return True
    if license_val and any(kw in license_lower for kw in PAID_LICENSE_KEYWORDS):
        return True
    if edition_lower in ['free', 'community', 'opensource', 'open-source']:
        return False
    if license_val and any(kw in license_lower for kw in OPEN_LICENSE_KEYWORDS):
        return False
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
    """创建文件备份

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


def ensure_config_in_path():
    """确保config目录在sys.path中（供脚本调用）"""
    config_dir = Path(__file__).resolve().parent
    if str(config_dir) not in __import__('sys').path:
        __import__('sys').path.insert(0, str(config_dir))
