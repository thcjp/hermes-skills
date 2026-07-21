"""
skill_core - Skill项目共享核心层 (P1-1)

集中管理5个模块(auto_discover/update_mechanism/check_debranding/quality_gate/trace_llm_scorer)
的重复实现:
- parser.py: frontmatter解析(单一来源)
- rules.py: 保留词/夸大词/占位符/阈值常量(单一来源)
- db.py: DB连接(单一来源)
- checks.py: 通用检查函数(单一来源)

迁移原则:
- 每次只迁移1个模块(本次仅quality_gate.py)
- 迁移后必须验证行为与迁移前完全一致
- 不破坏其他模块的现有调用
"""

from .parser import parse_frontmatter, parse_frontmatter_from_file
from .rules import (
    MAX_SKILL_MD_LINES, MAX_DISPLAY_NAME_LEN, MAX_SUMMARY_LEN,
    MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN,
    REQUIRED_FRONTMATTER_FIELDS,
    PLACEHOLDER_PATTERNS, EXAGGERATION_WORDS,
)
from .db import get_db, DB_PATH
from .checks import (
    check_slug_name_folder_consistency,
    check_line_count,
    check_required_frontmatter,
    check_display_name_length,
    check_summary_length,
    check_tools_format,
    check_no_xml_brackets,
    check_no_placeholders,
    check_no_exaggeration,
)

__all__ = [
    'parse_frontmatter', 'parse_frontmatter_from_file',
    'MAX_SKILL_MD_LINES', 'MAX_DISPLAY_NAME_LEN', 'MAX_SUMMARY_LEN',
    'MIN_DESCRIPTION_LEN', 'MAX_DESCRIPTION_LEN',
    'REQUIRED_FRONTMATTER_FIELDS',
    'PLACEHOLDER_PATTERNS', 'EXAGGERATION_WORDS',
    'get_db', 'DB_PATH',
    'check_slug_name_folder_consistency', 'check_line_count',
    'check_required_frontmatter', 'check_display_name_length',
    'check_summary_length', 'check_tools_format',
    'check_no_xml_brackets', 'check_no_placeholders', 'check_no_exaggeration',
]
