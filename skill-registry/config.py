#!/usr/bin/env python3
"""
[向后兼容 shim] 配置入口
========================
此文件已迁移到 d:\\skills\\config\\ 目录。
本文件保留为向后兼容层，自动将所有导入转发到新位置。

所有新代码应直接使用:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
    from project_config import DB_PATH, ...
"""

import sys
from pathlib import Path

# 将 config/ 目录加入 sys.path
_config_dir = Path(__file__).resolve().parent.parent / "config"
if str(_config_dir) not in sys.path:
    sys.path.insert(0, str(_config_dir))

# 从新位置重新导出所有内容
from project_config import *  # noqa: F401, F403
from project_config import (  # noqa: F401
    PROJECT_ROOT, DB_PATH, TOOLS_DIR, REGISTRY_DIR, DATA_DIR,
    PACKAGED_SKILLS_DIR, HERMES_SKILLS_DIR, OPENSOURCE_SKILLS_DIR,
    ENTERPRISE_UPLOAD_DIR, CLAWHUB_DOWNLOADED_DIR, DIFFERENTIATED_DIR,
    REPORT_DIR, MARKET_DATA_DIR, BACKUP_DIR, DISCOVERY_DIR,
    HEALTH_REPORT_DIR, EXPORT_DIR, CREDENTIALS_DIR,
    TRACE_PASS_THRESHOLD, TRACE_GRADE_A_PLUS, TRACE_GRADE_A,
    TRACE_GRADE_B, TRACE_GRADE_C,
    L2_PASS_THRESHOLD, L2_EXCELLENT_THRESHOLD, L2_MANUAL_REVIEW_THRESHOLD,
    L3_PASS_THRESHOLD,
    MIN_TRACE_SCORE, MAX_SKILL_MD_LINES, MIN_SKILL_MD_LINES,
    MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN,
    MAX_DISPLAYNAME_LEN, MIN_SUMMARY_LEN, MAX_SUMMARY_LEN,
    PAID_LICENSE_KEYWORDS, PAID_EDITION_KEYWORDS, OPEN_LICENSE_KEYWORDS,
    SCORE_TYPE_TRACE_LLM, SCORE_TYPE_BASELINE,
    TRACE_FIELD_MAPPING,
    MAX_SCAN_PAGES, BATCH_BACKUP_ENABLED,
    MIN_PRICE, MAX_PRICE,
    get_db_connection, is_paid_skill, safe_float, safe_int,
    create_backup, ensure_config_in_path,
)

# 也导出平台配置
from platform_config import (  # noqa: F401
    GITHUB_REPOS, GITHUB_PUBLIC_REMOTE, GITHUB_PRIVATE_REMOTE,
    GITHUB_BRANCH, is_free_skill, get_push_strategy,
    SKILLHUB_CLI_PATH, SKILLHUB_API_URL, SKILLHUB_WAF_CHAR_LIMIT,
    CLAWHUB_CLI_PATH, CLAWHUB_DAILY_UPLOAD_LIMIT,
)
