"""
skill_core.rules - 规则常量(单一来源)

从quality_gate.py迁移, 消除quality_gate.py和check_debranding.py的规则重复
所有阈值、保留词、夸大词、占位符模式集中在此
"""

# ============ 阈值常量 ============

MAX_SKILL_MD_LINES = 500
MAX_DISPLAY_NAME_LEN = 20
MAX_SUMMARY_LEN = 100
MIN_DESCRIPTION_LEN = 50
MAX_DESCRIPTION_LEN = 300

# ============ frontmatter必需字段 ============

REQUIRED_FRONTMATTER_FIELDS = [
    'slug', 'name', 'version', 'displayName',
    'summary', 'license', 'description', 'tools'
]

# ============ 占位符模式 ============
# (正则模式, 描述)

PLACEHOLDER_PATTERNS = [
    (r'待补充', '占位符-待补充'),
    (r'TODO', '占位符-TODO'),
    (r'FIXME', '占位符-FIXME'),
    (r'能力1[::]', '占位符-能力1模板'),
    (r'场景1[::]', '占位符-场景1模板'),
    (r'步骤1[::]', '占位符-步骤1模板'),
    (r'\{\{[a-zA-Z_][a-zA-Z0-9_]*\}\}', '占位符-未填充模板变量'),
    (r'\[.*?\]\s*\(.*?\)', '占位符-未替换链接'),  # 仅在frontmatter中检查
]

# ============ 夸大词模式 ============

EXAGGERATION_WORDS = [
    '万能', '超级', '最强', '最佳', '最完美', '最专业',
    '全球首发', '业界第一', '独一无二', '绝无仅有',
]

# ============ 格式正则 ============

# slug必须为kebab-case
SLUG_KEBAB_PATTERN = r'^[a-z0-9]+(-[a-z0-9]+)*$'

# version必须为x.y.z格式
VERSION_PATTERN = r'^\d+\.\d+\.\d+'

# ============ 不可重试的上传错误模式 ============
# (用于update_mechanism.py upload_free_via_cli判断是否重试)

NON_RETRYABLE_UPLOAD_PATTERNS = [
    'protected', 'already exists', 'slug conflict',
    'unauthorized', 'forbidden', 'authentication failed',
    'invalid token', 'permission denied',
]
