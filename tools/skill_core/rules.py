"""
skill_core.rules - 规则常量(单一来源)

从quality_gate.py迁移, 消除quality_gate.py和check_debranding.py的规则重复
所有阈值、保留词、夸大词、占位符模式集中在此
"""

import sys
from pathlib import Path

# Q1修复: description阈值从project_config(SSOT)导入，消除与project_config.py的不一致
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "config"))
# [V131 B1] 以下常量为re-export: 从project_config导入并重新导出供其他模块使用(非未使用import)
from project_config import (
    MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN,
    MAX_SKILL_MD_LINES, MAX_DISPLAY_NAME_LEN, MAX_SUMMARY_LEN,  # V119 W4: 从project_config统一导入, 消除本地副本
)

# ============ 阈值常量 ============
# V119 W4: 所有阈值常量统一从 project_config (SSOT) 导入, 不再本地定义

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
    # V161 FIX: xxx/XXX 改为词边界精确匹配(恰好3个x/X, 前后非字母数字)
    #   原r'xxx'/r'XXX'会误报 +1XXXXXXXXXX(美国电话格式串,10个X)等合法格式文档,
    #   导致 clawcall 等skill 无占位符 检查假阳性. 词边界版仍能命中独立 xxx/XXX 占位符.
    (r'(?<![A-Za-z0-9])[xX][xX][xX](?![A-Za-z0-9])', '占位符-xxx/XXX'),
    (r'HACK', '占位符-HACK'),
    (r'\[PLACEHOLDER\]', '占位符-PLACEHOLDER标记'),
    # Q3修复: 支持\d+任意数字，不再仅匹配字面"1"
    (r'能力\d+[::]', '占位符-能力N模板'),
    (r'场景\d+[::]', '占位符-场景N模板'),
    (r'步骤\d+[::]', '占位符-步骤N模板'),
    (r'\{\{[a-zA-Z_][a-zA-Z0-9_]*\}\}', '占位符-未填充模板变量'),
    (r'\[.*?\]\s*\(.*?\)', '占位符-未替换链接'),  # 仅在frontmatter中检查
    # v1.3: 合并deep_quality_audit.py的REAL_PLACEHOLDER_PATTERNS差异模式
    (r'(?m)^[\s/#*;]*TODO[:\s]', '占位符-TODO标记(行首)'),
    (r'(?m)^[\s/#*;]*FIXME[:\s]', '占位符-FIXME标记(行首)'),
    (r'lorem ipsum', '占位符-LoremIpsum'),
    (r'placeholder\s+content', '占位符-占位内容'),
    (r'replace[_ ]this', '占位符-替换占位'),
    (r'示例文本内容', '占位符-示例占位文本'),
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
RESERVED_WORDS = ['claude', 'anthropic', 'openai', 'chatgpt', 'gemini', 'bard', 'copilot', 'gpt-4', 'gpt-3']

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

# ============ V104 W1: 模板套话列表 (统一来源) ============
# 从3个文件合并: l3_function_checker.py(9项) + l3_batch_fix.py(13项) + diff_l4_batch_fix.py(14项)
# 以diff_l4_batch_fix.py的14项为基准(最全),包含全角/半角逗号变体

TEMPLATE_PHRASES = [
    '本Skill基于Markdown指令',
    '通过自然语言指令驱动Agent执行任务',
    '纯Markdown指令,部分功能需要exec命令行执行能力',
    '纯Markdown指令，部分功能需要exec命令行执行能力',
    '需要LLM支持，无LLM环境无法使用',
    '需要LLM支持,无LLM环境无法使用',
    '复杂场景可能需要人工辅助判断',
    '性能取决于底层模型能力',
    '请先阅读使用流程章节',
    '请参考错误处理章节',
    '请参考已知限制章节了解具体限制',
    '不适用于需要人工判断的复杂决策场景',
    '基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务',
    '触发关键词',
]

# ============ V104 W2: 非能力点标题 (统一22项扩展集合) ============
# 修复checker/fixer口径不一致: l3_function_checker使用22项,其他文件仅用15项
# 统一为22项扩展集合,确保检查与修复判定一致

NON_CAPABILITY_HEADINGS = [
    # 基础15项
    '能力覆盖范围', '技术细节', '处理流程', '输入输出规范',
    '能力参数', '适用场景', '能力概览', '功能概览',
    '输出格式', '脚本获取', '命令参数说明', '输出说明', '输入说明',
    '源能力映射', '领域术语',
    # 扩展7项 (l3_function_checker使用,其他文件之前缺失)
    '能力边界', '功能边界', '工作流程', '工作原理',
    '设计理念', '使用说明', '注意事项',
]

# ============ V104 W3: 检查结果常量 ============

PASS = 'PASS'
FAIL = 'FAIL'
WARN = 'WARN'

# ============ Skill类型/领域分类 ============
# v1.3: 统一classify_skill,消除deduplicate_all_v36.py和deduplicate_blocks.py的重复实现
# 返回 (skill_type, skill_domain)

_CLASSIFY_DOMAIN_RULES = [
    ("finance", ["finance", "accounting", "估值", "财务", "金融", "trading", "stock", "投资"]),
    ("security", ["security", "安全", "audit", "vulnerability", "vuln", "pentest", "scan", "firewall", "encrypt", "加密"]),
    ("dev", ["code", "git", "docker", "python", "java", "javascript", "typescript", "rust", "go ", "golang", "compile", "lint", "develop", "开发", "scaffold", "framework", "sdk"]),
    ("browser", ["browser", "浏览器", "web-auto", "scrape", "crawl", "爬虫"]),
    ("comm", ["email", "chat", "message", "discord", "telegram", "slack", "whatsapp", "feishu", "飞书", "通知", "邮件", "消息"]),
    ("creative", ["image", "video", "music", "design", "podcast", "audio", "图", "视频", "音乐", "设计", "画", "logo", "figma", "ui", "ux", "frontend", "前端"]),
    ("data", ["api", "data", "csv", "json", "sql", "database", "db", "数据库", "excel", "图表", "chart", "analytics", "分析"]),
    ("auto", ["automation", "workflow", "cron", "schedule", "自动化", "定时", "任务", "batch", "queue"]),
    ("research", ["research", "search", "news", "feed", "rss", "研究", "搜索", "新闻", "监控", "monitor"]),
    ("productivity", ["productivity", "task", "calendar", "reminder", "note", "效率", "日程", "提醒", "笔记", "todo"]),
    ("platform", ["dashboard", "admin", "manage", "console", "平台", "管理", "控制台"]),
]

_CLASSIFY_TYPE_RULES = [
    ("platform", ["dashboard", "admin", "console", "manage", "平台", "管理"]),
    ("service", ["api", "service", "服务", "接口"]),
    ("creative", ["image", "video", "music", "design", "画", "创意", "creative"]),
    ("dev", ["code", "git", "docker", "develop", "开发", "lint", "compile"]),
    ("browser", ["browser", "浏览器", "scrape", "crawl"]),
    ("comm", ["email", "chat", "message", "discord", "通知", "消息"]),
    ("data", ["data", "csv", "json", "sql", "database", "excel", "chart"]),
    ("auto", ["automation", "workflow", "cron", "自动化", "定时"]),
]


def classify_skill(meta):
    """根据 slug/displayName/summary/tags 判断 skill 类型和领域。

    统一规范源(v1.3),替代deduplicate_all_v36.py和deduplicate_blocks.py的重复实现。

    参数:
        meta: dict,包含 slug/displayName/summary/tags 字段

    返回:
        (skill_type, skill_domain)
        skill_type: tool/platform/service/creative/dev/browser/comm/data/auto
        skill_domain: finance/security/dev/browser/comm/creative/data/auto/research/productivity/platform/other
    """
    slug = (meta.get("slug") or "").lower()
    display = (meta.get("displayName") or "").lower()
    summary = (meta.get("summary") or "").lower()
    tags = (meta.get("tags") or "").lower()
    combined = " ".join([slug, display, summary, tags])

    skill_domain = "other"
    for domain, keywords in _CLASSIFY_DOMAIN_RULES:
        if any(kw in combined for kw in keywords):
            skill_domain = domain
            break

    skill_type = "tool"
    for stype, keywords in _CLASSIFY_TYPE_RULES:
        if any(kw in combined for kw in keywords):
            skill_type = stype
            break

    return skill_type, skill_domain


# ============ V107 W1: ACTION_VERBS 动作动词列表 (统一来源) ============
# 合并 Set A (diff_batch_fix2/3, 48项) + Set B (diff_l4_batch_fix, 43项) 超集
# Set A 中文: 创建/删除/修改/查询/执行/配置/安装/运行/启动/停止/导入/导出/解析/转换/生成/提取/检查/验证/分析/处理/发送/接收/保存/加载
# Set B 中文额外: 重启/切换/压缩/清理/更新/替换/设置/确认/提供/补充/参考/排查/恢复
# Set A 英文: create/delete/update/query/execute/config/install/run/start/stop/import/export/parse/convert/generate/extract/check/verify/analyze/process/send/receive/save/load/use/call/set/get/add/remove/apply
# Set B 英文额外: modify/restart/switch/compress/clean/replace/provide/validate

ACTION_VERBS = [
    # 中文 (Set A + Set B 合并)
    '创建', '删除', '修改', '查询', '执行', '配置', '安装', '运行',
    '启动', '停止', '导入', '导出', '解析', '转换', '生成', '提取',
    '检查', '验证', '分析', '处理', '发送', '接收', '保存', '加载',
    '重启', '切换', '压缩', '清理', '更新', '替换', '设置',
    '确认', '提供', '补充', '参考', '排查', '恢复',
    # 英文 (Set A + Set B 合并)
    'create', 'delete', 'update', 'query', 'execute', 'config',
    'install', 'run', 'start', 'stop', 'import', 'export',
    'parse', 'convert', 'generate', 'extract', 'check', 'verify',
    'analyze', 'process', 'send', 'receive', 'save', 'load',
    'use', 'call', 'set', 'get', 'add', 'remove', 'apply',
    'modify', 'restart', 'switch', 'compress', 'clean', 'replace',
    'provide', 'validate',
]

# ============ V107 W2: OUTPUT_FORMAT_KEYWORDS 输出格式关键词 (统一来源) ============
# 合并 diff_batch_fix.py 和 diff_l4_batch_fix.py 的定义 (内容一致,仅顺序不同)

OUTPUT_FORMAT_KEYWORDS = [
    'JSON', 'CSV', 'Markdown', 'markdown', '文本', '表格',
    'JSON格式', '格式输出', '输出格式', '返回格式', '返回结果',
    '输出结果', '返回值', '输出内容', 'output format',
]

# ============ V105 W4: 模糊错误处理短语→具体操作替换 (统一来源) ============
# 从 diff_l4_batch_fix.py 和 l4_batch_fix.py 统一迁移
VAGUE_TO_ACTION = {
    '重试': '检查网络连接后重新执行命令',
    '稍后重试': '等待30秒后检查服务状态,确认服务恢复后重新执行',
    '联系客服': '收集错误日志和请求ID,通过工单系统提交给技术支持',
    '联系技术支持': '收集错误码和复现步骤,提交工单或发送邮件至技术支持',
    '检查网络': '执行ping命令测试网络连通性,检查防火墙和代理设置',
    '检查配置': '对照依赖说明章节逐项验证配置项,确认环境变量已正确设置',
    '确认权限': '检查当前用户角色和权限设置,确保有对应操作的执行权限',
    '确保网络畅通': '执行ping命令测试连通性,检查DNS解析和防火墙规则',
}

# ============ V108 W1: RESULT_HANDLING_KEYWORDS 结果处理关键词 (统一来源) ============
# 从 diff_l4_batch_fix.py 迁移 (与L4-5检查器一致)

RESULT_HANDLING_KEYWORDS = [
    '结果', '输出', '返回', '保存', '导出', '处理完成', '执行完成',
    'result', 'output', 'return', 'save', 'export',
]

# ============ V108 W1: CAPABILITY_OUTPUT_KEYWORDS 能力点输出描述关键词 (统一来源) ============
# 从 diff_l4_batch_fix.py 迁移 (与L4-5检查器一致)

CAPABILITY_OUTPUT_KEYWORDS = [
    '输出', '返回', '结果', '生成', '创建', '保存', '导出', '显示',
    'output', 'return', 'result', 'generate', 'create', 'save', 'export',
]

# ============ V108 W1: VAGUE_SOLUTIONS 错误处理空话列表 (统一来源) ============
# 从 diff_l4_batch_fix.py 迁移 (与L4-3检查器一致)

VAGUE_SOLUTIONS = ['重试', '稍后', '联系', '确保', '建议', 'retry', 'try again']

# ============ V108 W1: GENERIC_CAPABILITIES 通用能力点模板 (统一来源) ============
# 从 diff_batch_fix2.py 迁移 (当核心能力<3个###标题时使用)

GENERIC_CAPABILITIES = [
    ('核心功能执行', 'input_params', '创建/查询/导出'),
    ('参数配置与调用', 'config_options', '修改/重置/导入'),
    ('结果处理与输出', 'output_format', '导出/保存/转换'),
]

# ============ V108 W1: CN_NUM_MAP 中文数字到阿拉伯数字映射 (统一来源) ============
# 从 diff_batch_fix.py 迁移

CN_NUM_MAP = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
    '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
}

# ============ V108 W1: UPGRADE_KEYWORDS 升级关键词 (统一来源) ============
# 从 diff_batch_fix.py 迁移 (用于free版本检测)

UPGRADE_KEYWORDS = ['升级', '完整版', '付费版', '高级版', 'Upgrade', 'upgrade']

# ============ V109 W2: TEMPLATE_PHRASE_REPLACEMENTS 模板套话替换映射 (统一来源) ============
# 从 diff_batch_fix2.py + diff_batch_fix3.py 合并 (diff_batch_fix3为超集,含第三轮新增项)
# 长串优先,避免子串问题

TEMPLATE_PHRASE_REPLACEMENTS = [
    # 完整行替换 (第一轮fix的LIMITATIONS_SECTION产生的变体)
    ('- 性能取决于底层模型能力和网络状况',
     '- 执行效率受模型能力与网络环境影响'),
    # 逐短语替换
    ('纯Markdown指令,部分功能需要exec命令行执行能力',
     '纯Markdown指令,部分功能需exec命令行执行'),
    ('请参考已知限制章节了解具体限制',
     '可查阅已知限制章节了解具体限制'),
    ('通过自然语言指令驱动Agent执行任务',
     '通过自然语言指令驱动Agent完成操作'),
    ('复杂场景可能需要人工辅助判断',
     '复杂业务场景建议结合人工经验判断'),
    ('性能取决于底层模型能力',
     '执行效率受模型能力与网络环境影响'),
    ('请先阅读使用流程章节',
     '建议先查看使用流程'),
    ('请参考错误处理章节',
     '可查阅错误处理章节'),
    ('本Skill基于Markdown指令',
     '本skill基于Markdown指令规范'),
    ('需要LLM支持，无LLM环境无法使用',
     '需LLM支持,无LLM环境不可用'),
    # 第三轮新增: 处理L3-4引入的变体
    ('如遇错误请参考错误处理章节进行排查',
     '如遇错误可查阅错误处理章节进行排查'),
    ('请参考错误处理章节进行排查',
     '可查阅错误处理章节进行排查'),
    # V114: 从l3_batch_fix.py合并的独有映射项
    ('本Skill基于Markdown指令，无需额外API Key(除内容中明确标注的外部API)',
     '本Skill基于指令驱动'),
    ('本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)',
     '本Skill基于指令驱动'),
    ('基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务',
     'AI Skill,驱动Agent执行任务'),
    ('纯Markdown指令，部分功能需要exec命令行执行能力',
     '指令驱动为主，部分功能需exec命令行支持'),
    ('需要LLM支持,无LLM环境无法使用',
     '依赖LLM能力'),
    ('请先阅读使用流程章节，确认环境满足依赖说明中的要求。',
     '查看使用流程章节,确认环境满足依赖要求。'),
    ('请参考错误处理章节，按照表格中的处理方式操作。',
     '查看错误处理章节,对照表格进行处理。'),
    ('请参考已知限制章节了解具体限制。',
     '查看已知限制章节了解能力边界。'),
    ('不适用于需要人工判断的复杂决策场景',
     '不适用于批量自动化处理场景'),
]

# ============ V135 F3: L4 checker/fixer 共享常量 (统一来源) ============
# 消除 l4_task_gate.py (checker) 和 l4_batch_fix.py (fixer) 的重复内联列表

# 能力点输入描述关键词 (L4-1 checker/fixer 共享)
CAPABILITY_INPUT_KEYWORDS = [
    '输入', '参数', '触发', '当', '如果', '用户', '请求', '提供',
    'input', 'param', 'trigger', 'when', 'if', 'user', 'request',
]

# 能力点处理描述关键词 (L4-1 checker/fixer 共享)
CAPABILITY_PROCESS_KEYWORDS = [
    '执行', '处理', '调用', '运行', '分析', '解析', '转换', '检查',
    '匹配', '搜索', '过滤', '排序', '发送', '接收',
    'execute', 'process', 'call', 'run', 'analyze', 'parse',
]

# 使用流程章节名称列表 (L4-5/L4-6 checker/fixer 共享)
USAGE_SECTION_NAMES = [
    '使用流程', '使用规范', '使用方法', '使用指南', '快速开始', 'Quick Start',
]

# 标准命令参数 (排除检查, L4-2 checker/fixer 共享)
STANDARD_CMD_PARAMS = ['--help', '-h', '--version', '-v']

# 脚本获取/安装信息关键词 (L4-2 checker/fixer 共享)
INSTALL_INFO_KEYWORDS = [
    'scripts/', 'scripts\\', 'scripts目录', 'scripts folder',
    '安装', 'Install', '获取', '下载', 'clone', 'npm install',
    'pip install', '脚本目录', 'script directory', '脚本获取',
]

# 错误处理方式关键词 (L4-3 非表格格式 checker/fixer 共享)
ERROR_SOLUTION_KEYWORDS = ['处理', '解决', '修复', '方式', '应', '需', '可']

# LLM依赖检测关键词 (L4-4 checker/fixer 共享)
LLM_MENTION_KEYWORDS = ['LLM', 'llm', 'AI', 'Agent', '大模型']

# LLM具体能力关键词 (L4-4 checker/fixer 共享)
LLM_SPECIFIC_KEYWORDS = [
    'Claude', 'GPT', 'Gemini', 'Qwen', 'GLM', 'DeepSeek',
    '推理', '理解', '生成', '分析能力', '自然语言',
    'Agent内置', 'Agent平台', 'reasoning', 'understanding',
]

# API Key检测关键词 (L4-4 checker/fixer 共享)
API_MENTION_KEYWORDS = ['API Key', 'API密钥', 'api_key', 'apikey']

# API Key获取步骤关键词 (L4-4 checker/fixer 共享)
API_ACQUISITION_KEYWORDS = [
    '获取', '申请', '注册', '登录', '访问', '官网', '后台', '控制台',
    'https://', 'http://', '链接', '地址',
]

# API Key配置方式关键词 (L4-4 checker/fixer 共享)
API_CONFIG_KEYWORDS = ['环境变量', 'env', 'export', '配置文件', 'config']

# 运行环境检测关键词 (L4-4 checker/fixer 共享)
ENV_MENTION_KEYWORDS = ['运行环境', '操作系统', 'Windows', 'macOS', 'Linux', 'Agent平台']

# 具体运行环境平台关键词 (L4-4 checker/fixer 共享)
ENV_SPECIFIC_KEYWORDS = [
    'Windows', 'macOS', 'Linux', 'Claude Code', 'Cursor', 'Codex',
    'Gemini CLI', 'TRAE', 'Agent',
]

# FAQ章节检测关键词 (L4-6 checker/fixer 共享)
FAQ_KEYWORDS = ['## FAQ', '## 常见问题', '## Frequently Asked', '### FAQ']

# 已知限制章节检测关键词 (L4-6 checker/fixer 共享)
LIMITATIONS_KEYWORDS = ['## 已知限制', '## 限制', '## Limitations', '## 限制说明']

# 非任务标题关键词 (L4-1 checker: 判断###标题是否非可执行任务)
NON_TASK_KEYWORDS = ['概述', '简介', '总结', '说明', '备注', '注意', '概览', '目录', 'Overview', 'Summary']

# 错误处理表格表头列检测关键词 (L4-3 checker/fixer 共享)
TABLE_HEADER_SCENARIO_KEYWORDS = ['场景', '错误', '问题', 'error', 'scenario']
TABLE_HEADER_SOLUTION_KEYWORDS = ['处理', '解决', '修复', '方式', 'solution', 'fix']


# ============ V116 W3: SLUG冲突解决 (统一来源) ============
# 合并 auto_differentiate.py 和 finance_differentiate.py 的 resolve_slug_conflict
# auto_differentiate: v3.3后返回None(不自动追加后缀,避免反垃圾系统检测)
# finance_differentiate: 仍使用自动后缀(-v2/-pro等)

SLUG_CONFLICT_SUFFIXES = ['-v2', '-pro', '-v3', '-plus', '-v4', '-max', '-v5', '-elite']


def resolve_slug_conflict(base_slug, existing_slugs, batch_slugs, auto_suffix=False):
    """检测并解决slug冲突 (统一入口)

    V116 W3: 合并 auto_differentiate.py 和 finance_differentiate.py 的实现。
    
    Args:
        base_slug: 候选slug
        existing_slugs: 数据库中已存在的slug集合
        batch_slugs: 当前批次已分配的slug集合
        auto_suffix: 冲突时是否自动追加后缀
            False (默认, v3.3行为): 冲突时返回None, 由调用方语义化重命名
            True (finance行为): 自动追加 -v2/-pro 等后缀

    Returns:
        str: 可用的slug (无冲突时返回base_slug)
        None: 存在冲突且auto_suffix=False时
    """
    all_used = existing_slugs | batch_slugs
    if base_slug not in all_used:
        return base_slug
    if not auto_suffix:
        return None
    # auto_suffix模式: 尝试预定义后缀
    for suffix in SLUG_CONFLICT_SUFFIXES:
        candidate = f"{base_slug}{suffix}"
        if candidate not in all_used:
            return candidate
    # 预定义后缀耗尽: 生成 -v6, -v7, ...
    counter = 6
    while True:
        candidate = f"{base_slug}-v{counter}"
        if candidate not in all_used:
            return candidate
        counter += 1
