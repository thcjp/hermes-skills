"""
skill_core.rules - 规则常量(单一来源)

从quality_gate.py迁移, 消除quality_gate.py和check_debranding.py的规则重复
所有阈值、保留词、夸大词、占位符模式集中在此
"""

import sys
from pathlib import Path

# Q1修复: description阈值从project_config(SSOT)导入，消除与project_config.py的不一致
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "config"))
from project_config import MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN

# ============ 阈值常量 ============

MAX_SKILL_MD_LINES = 500
MAX_DISPLAY_NAME_LEN = 20
MAX_SUMMARY_LEN = 100
# MIN_DESCRIPTION_LEN 和 MAX_DESCRIPTION_LEN 从 project_config 导入 (SSOT, 值为150-280)

# ============ frontmatter必需字段 ============

REQUIRED_FRONTMATTER_FIELDS = [
    'slug', 'name', 'version', 'displayName',
    'summary', 'license', 'description', 'tools'
]

# ============ 占位符模式 ============
# (正则模式, 描述)

PLACEHOLDER_PATTERNS = [
    (r'待补充', '占位符-待补充'),
    (r'待填充', '占位符-待填充'),
    (r'待完善', '占位符-待完善'),
    (r'待确定', '占位符-待确定'),
    (r'TODO', '占位符-TODO'),
    (r'TBD', '占位符-TBD'),
    (r'FIXME', '占位符-FIXME'),
    (r'xxx', '占位符-xxx'),
    (r'XXX', '占位符-XXX'),
    (r'HACK', '占位符-HACK'),
    (r'\[PLACEHOLDER\]', '占位符-PLACEHOLDER标记'),
    # Q3修复: 支持\d+任意数字，不再仅匹配字面"1"
    (r'能力\d+[::]', '占位符-能力N模板'),
    (r'场景\d+[::]', '占位符-场景N模板'),
    (r'步骤\d+[::]', '占位符-步骤N模板'),
    (r'\{\{[a-zA-Z_][a-zA-Z0-9_]*\}\}', '占位符-未填充模板变量'),
    (r'\[.*?\]\s*\(.*?\)', '占位符-未替换链接'),  # 仅在frontmatter中检查
]

# ============ 夸大词模式 ============

EXAGGERATION_WORDS = [
    '万能', '超级', '最强', '最佳', '最完美', '最专业',
    '全球首发', '业界第一', '独一无二', '绝无仅有',
    # Q4修复: 合并generate_skill.py:622的夸大词，消除列表不一致
    '终极', '完美', '第一', '顶级', '极致', '最好',
]

# ============ 保留词模式 ============
# A3修复: 统一保留词列表,消除trace_llm_scorer.py和skill_batch_upgrader_v3.py的重复硬编码
RESERVED_WORDS = ['claude', 'anthropic', 'openai', 'chatgpt']

# ============ 格式正则 ============

# slug必须为kebab-case
SLUG_KEBAB_PATTERN = r'^[a-z0-9]+(-[a-z0-9]+)*$'

# version必须为x.y.z格式
VERSION_PATTERN = r'^\d+\.\d+\.\d+$'

# ============ 不可重试的上传错误模式 ============
# (用于update_mechanism.py upload_free_via_cli判断是否重试)

NON_RETRYABLE_UPLOAD_PATTERNS = [
    'protected', 'already exists', 'slug conflict',
    'unauthorized', 'forbidden', 'authentication failed',
    'invalid token', 'permission denied',
]
