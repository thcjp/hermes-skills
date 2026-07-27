#!/usr/bin/env python3
"""
Skill批量升级脚本 v3.0
融合SkillHub/Coze/Claude Skills审核规则 + 营销优化策略

v3.0新增功能:
1. 平台合规检查: name与文件夹同名、禁止夸大词、禁止XML尖括号、禁止保留词
2. 营销优化: 标题关键词、description触发词、定价梯度
3. 合规预检: 30项上传前必检清单
4. 自动修复: 检测到问题自动修复

Usage:
    python skill_batch_upgrader_v3.py check          # 检查所有skill合规性
    python skill_batch_upgrader_v3.py fix             # 自动修复合规问题
    python skill_batch_upgrader_v3.py fix --slug xxx  # 修复单个skill
    python skill_batch_upgrader_v3.py report          # 生成合规报告
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH, DATA_DIR, PROJECT_ROOT
from project_config import PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR
from project_config import ENTERPRISE_UPLOAD_DIR, DIFFERENTIATED_DIR
# === End Phase 1 ===


import os
import re
import sys
import json
import sqlite3
from pathlib import Path
from datetime import datetime

# 导入v2.0的功能
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skill_batch_upgrader_v2 import (
    SECTION_MAP, DOMESTIC_ALTERNATIVES,
    parse_skill_md, find_section_header, check_missing_sections,
    extract_section_content, rename_section, optimize_description,
    generate_section_content, upgrade_skill
)

# DB_PATH imported from config

# A3修复: 从skill_core导入RESERVED_WORDS,消除本地重复硬编码
from skill_core.rules import RESERVED_WORDS
# 统一使用skill_core.parser的find_skill_md,消除本地重复实现
from skill_core.parser import find_skill_md

# v3.0新增: 夸大词替换映射
EXAGGERATION_MAP = {
    '万能': '全能',
    '超级': '高效',
    '最强': '专业',
    '最好': '优质',
    '最佳': '优选',
    '终极': '完整',
    '完美': '完善',
    '第一': '领先',
    '顶级': '高级',
    '极致': '精细',
}

# v3.0新增: 保留词检查 (A3修复: 已迁移至skill_core.rules,此处不再重复定义)

# v3.0新增: 摘要式描述模式（需要改写）
SUMMARY_PATTERNS = [
    r'这是一个',
    r'这是一款',
    r'本工具',
    r'本技能用于帮助用户',
    r'帮助用户处理各种',
    r'帮助用户完成各种',
]

# v3.1新增: 内容质量模式
# 模板化短语(批量生成脚本产出的通用套话)
TEMPLATE_CONTENT_PATTERNS = [
    r'按照skill规范执行',
    r'遵循单一意图原则',
    r'解析.*任务的输入参数,完成核心解析逻辑,返回结构化响应和完成状态',
    r'解析.*的输入参数,执行核心处理逻辑,返回结构化结果和执行状态',
    r'返回.*处理结果,包含执行状态码、结果数据和执行日志',
    r'验证执行结果，确认输出符合预期格式',
    r'参考.*相关配置参数进行设置',
    r'处理输入数据,执行转换操作并输出结果',
]

# 占位符内容模式
PLACEHOLDER_CONTENT_PATTERNS = [
    r'根据实际场景填充',
    r'相关说明',
    r'用户提供.*所需的指令和必要参数',
    r'用户提供操作指令和必要参数',
    r'返回操作执行的结果',
    r'输入: 用户请求',
    r'处理: 根据使用流程执行',
    r'输出: 处理结果',
    r'result: "browser 相关配置参数"',
    r'result: "相关说明"',
]

# 空节区检测模式
EMPTY_SECTION_PATTERNS = [
    r'API Key 配置\s*\n-\s*\n',
    r'可用性分类.*MD\+EXEC\(\)',
]

# v3.0新增: 硬编码凭证模式
HARDCODED_KEY_PATTERNS = [
    r'sk-[a-zA-Z0-9]{20,}',  # OpenAI API Key
    r'AKIA[A-Z0-9]{16}',     # AWS Access Key
    r'ghp_[a-zA-Z0-9]{36}',  # GitHub PAT
    r'Bearer[ \t]+[a-zA-Z0-9._-]{10,}[ \t]*(?:\n|$)',  # Bearer token (同行, 至少10字符, 不跨行)
    r'password[ \t]*=[ \t]*["\'][^"\']+["\']',  # password = "xxx"
    r'api_key[ \t]*=[ \t]*["\'][^"\']+["\']',   # api_key = "xxx"
    r'secret[ \t]*=[ \t]*["\'][^"\']+["\']',     # secret = "xxx"
]

# v3.0新增: 营销关键词（按类别）
MARKETING_KEYWORDS = {
    '文案创作': ['文案', '写作', '内容创作', '爆款', '标题', '钩子', 'copywriting', 'writer', 'content'],
    '数据分析': ['分析', '报表', '统计', '可视化', '洞察', '数据', 'analytics', 'data', 'report', 'chart'],
    'SEO优化': ['SEO', '排名', '关键词', '搜索', '流量', '收录', 'search', 'rank', 'traffic'],
    '编程开发': ['代码', '编程', '开发', '调试', '测试', '部署', 'code', 'dev', 'debug', 'test', 'deploy', 'programming'],
    '设计创作': ['设计', '海报', '图标', 'UI', '配色', '排版', 'design', 'poster', 'icon', 'theme', 'brand'],
    '营销推广': ['营销', '推广', '广告', '转化', '获客', '裂变', 'marketing', 'ad', 'conversion', 'growth'],
    '效率工具': ['效率', '自动化', '批量', '快捷', '省时', '提速', 'automation', 'batch', 'productivity', 'workflow'],
    '安全合规': ['安全', '加密', '合规', '审计', '防护', '检测', 'security', 'crypto', 'compliance', 'audit', 'vulnerability'],
    '翻译': ['翻译', 'translate', '语言', 'language', '多语言', 'i18n'],
    '数据库': ['数据库', 'database', 'SQL', 'DB', '查询', 'query', '存储', 'storage'],
    'API集成': ['API', '集成', 'integration', '接口', 'webhook', '连接', 'connect'],
    '文件处理': ['文件', 'file', '文档', 'document', 'PDF', 'Word', 'Excel', '转换', 'convert'],
    '视频音频': ['视频', 'video', '音频', 'audio', '音乐', 'music', '配音', 'voice', 'media'],
    '通信消息': ['消息', 'message', '通知', 'notify', '邮件', 'email', '短信', 'SMS', '推送', 'push'],
    '项目管理': ['项目', 'project', '任务', 'task', '管理', 'manage', '计划', 'plan', '进度'],
    'AI模型': ['AI', 'LLM', 'GPT', '模型', 'model', '智能', 'agent', '助手', 'assistant'],
    '监控运维': ['监控', 'monitor', '运维', 'ops', '日志', 'log', '告警', 'alert', '部署'],
    '电商': ['电商', 'ecommerce', '商品', 'product', '店铺', 'shop', '订单', 'order', '支付', 'payment'],
}

# 触发短语模板（按类别）
TRIGGER_TEMPLATES = {
    '文案创作': 'Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。',
    '数据分析': 'Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。',
    'SEO优化': 'Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。',
    '编程开发': 'Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。',
    '设计创作': 'Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。',
    '营销推广': 'Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。',
    '效率工具': 'Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。',
    '安全合规': 'Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。',
    '翻译': 'Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。',
    '数据库': 'Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。',
    'API集成': 'Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。',
    '文件处理': 'Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。',
    '视频音频': 'Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。',
    '通信消息': 'Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。',
    '项目管理': 'Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。',
    'AI模型': 'Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。',
    '监控运维': 'Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。',
    '电商': 'Use when 需要电商运营、商品管理、订单处理、支付集成时使用。不适用于虚假交易和刷单。',
}


def check_name_folder_consistency(skill_md_path):
    """检查name字段与文件夹名是否一致"""
    folder_name = skill_md_path.parent.name
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    
    # 提取name字段
    name_match = re.search(r'^name:\s*["\']?([^"\'\n]+)["\']?\s*$', fm, re.MULTILINE)
    if not name_match:
        return False, "name字段不存在"
    
    name = name_match.group(1).strip()
    if name == folder_name:
        return True, "一致"
    else:
        return False, f"name='{name}' != folder='{folder_name}'"


def check_reserved_words(skill_md_path):
    """检查displayName和summary是否含保留词（不检查name/slug，因为它们必须与文件夹同名）"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    issues = []
    
    # 只检查displayName和summary，不检查name/slug（它们必须与文件夹同名）
    for field in ['displayName', 'summary']:
        match = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if match:
            value = match.group(1)
            value_lower = value.lower()
            for word in RESERVED_WORDS:
                # 使用词边界匹配，避免"anthropics"匹配"anthropic"
                if re.search(rf'\b{word}\b', value_lower):
                    issues.append(f"{field}='{value}' 含保留词 '{word}'")
    
    return len(issues) == 0, issues


def check_xml_brackets(skill_md_path):
    """检查frontmatter是否含XML尖括号"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            # 检查是否有XML尖括号（排除代码块中的合法使用）
            # 只检查frontmatter部分
            xml_matches = re.findall(r'[<>]', fm)
            if xml_matches:
                return False, f"frontmatter含{len(xml_matches)}个XML尖括号"
    
    return True, "无XML尖括号"


def check_exaggeration_words(skill_md_path):
    """检查是否含夸大词"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, body = parse_skill_md(content)
    issues = []
    
    # 检查displayName和summary
    for field in ['displayName', 'summary', 'description']:
        match = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if match:
            value = match.group(1)
            for word in EXAGGERATION_MAP:
                if word in value:
                    issues.append(f"{field}含夸大词'{word}'")
    
    return len(issues) == 0, issues


def check_summary_style_description(skill_md_path):
    """检查description是否为摘要式"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    
    # 提取description
    desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
    if desc_match:
        desc = desc_match.group(1).strip()
    else:
        desc_match = re.search(r'description:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip()
        else:
            return True, "description不存在(无需检查)"
    
    for pattern in SUMMARY_PATTERNS:
        if re.search(pattern, desc):
            return False, f"摘要式描述: 含'{pattern}'"
    
    return True, "非摘要式"


def check_line_count(skill_md_path):
    """检查SKILL.md行数是否≤500"""
    content = skill_md_path.read_text(encoding='utf-8')
    lines = len(content.split('\n'))
    if lines > 500:
        return False, f"{lines}行 (>500)"
    return True, f"{lines}行"


def check_license(skill_md_path):
    """检查license是否正确"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    
    license_match = re.search(r'^license:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if not license_match:
        return False, "license字段不存在"
    
    license_value = license_match.group(1).strip()
    if license_value in ['MIT', 'MIT-0', 'Proprietary', 'Apache-2.0', 'ISC', 'BSD-2-Clause', 'BSD-3-Clause', 'GPL-3.0', 'MPL-2.0', 'Unlicense']:
        return True, license_value
    else:
        return False, f"非标准license: {license_value}"


def check_tools_format(skill_md_path):
    """检查tools是否为YAML数组格式"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    
    # 检查tools是否为YAML数组（以 - 开头）
    tools_match = re.search(r'^tools:\s*\n((?:\s+-\s+.+\n?)+)', fm, re.MULTILINE)
    if tools_match:
        return True, "YAML数组格式"
    
    # 检查是否为字符串格式（错误格式）
    tools_str = re.search(r'^tools:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if tools_str:
        return False, f"字符串格式(应为YAML数组): {tools_str.group(1)}"
    
    return False, "tools字段不存在"


def check_display_name_length(skill_md_path):
    """检查displayName是否≤20字符"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    
    match = re.search(r'^displayName:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if not match:
        return False, "displayName不存在"
    
    value = match.group(1).strip()
    if len(value) > 20:
        return False, f"{len(value)}字符 (>20): {value}"
    return True, f"{len(value)}字符: {value}"


def check_summary_length(skill_md_path):
    """检查summary是否≤100字符"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    
    match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if not match:
        return False, "summary不存在"
    
    value = match.group(1).strip()
    if len(value) > 100:
        return False, f"{len(value)}字符 (>100)"
    return True, f"{len(value)}字符"


def check_hardcoded_keys(skill_md_path):
    """检查是否含硬编码凭证（排除代码块和占位符）"""
    content = skill_md_path.read_text(encoding='utf-8')
    issues = []
    
    # 排除代码块中的内容（```...```之间）
    content_no_codeblock = re.sub(r'```[\s\S]*?```', '', content)
    
    # 占位符文本（这些不是真实凭证）
    PLACEHOLDER_PATTERNS = [
        'your-token', 'your_token', 'your-api-key', 'your_api_key',
        'your-key', 'your_key', 'xxx', 'XXX', 'placeholder',
        'example', 'sample', 'demo', 'test-token', 'test_token',
        '<token>', '<key>', '<your', 'YOUR_', 'your-access',
        'token-here', 'token_here', 'apikey', 'your-bearer',
        # 中文占位符
        '你的key', '你的key', '你的_api', '你的-api', '你的密钥',
        # 已脱敏标记
        'redacted', '[redacted]', '[脱敏]',
    ]
    
    for pattern in HARDCODED_KEY_PATTERNS:
        matches = re.findall(pattern, content_no_codeblock, re.IGNORECASE)
        if matches:
            # 过滤掉占位符
            real_matches = []
            for m in matches:
                m_lower = m.lower() if isinstance(m, str) else ''
                is_placeholder = any(p.lower() in m_lower for p in PLACEHOLDER_PATTERNS)
                if not is_placeholder:
                    real_matches.append(m)
            if real_matches:
                issues.append(f"发现{len(real_matches)}处硬编码凭证: {pattern[:30]}")
    
    return len(issues) == 0, issues


def check_description_length(skill_md_path):
    """检查description长度是否150-280字符"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    
    desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
    if desc_match:
        desc = desc_match.group(1).strip()
    else:
        desc_match = re.search(r'description:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip()
        else:
            return False, "description不存在"
    
    desc_len = len(desc)
    if desc_len < 150:
        return False, f"太短({desc_len}c <150)"
    elif desc_len > 280:
        return False, f"太长({desc_len}c >280)"
    else:
        return True, f"合格({desc_len}c)"


# ============ v3.1新增: 内容质量检查 ============

def check_duplicate_summary(skill_md_path):
    """检查summary是否包含重复文本"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    fm, _ = parse_skill_md(content)
    match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if not match:
        return True, "summary不存在(无需检查)"
    value = match.group(1).strip()
    # 检测: 前半段和后半段是否重复
    half = len(value) // 2
    if half > 10:
        first_half = value[:half].rstrip('.。 ')
        second_half = value[half:].lstrip('.。 ')
        if first_half and second_half and first_half == second_half:
            return False, f"summary前后重复: '{first_half[:30]}...'"
    # 检测: 连续重复的短语
    for i in range(10, len(value) // 2):
        segment = value[:i]
        if value.count(segment) >= 2 and len(segment) > 10:
            return False, f"summary含重复段落: '{segment[:30]}...'"
    return True, "无重复"


def check_duplicate_description(skill_md_path):
    """检查description是否包含重复文本"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    fm, _ = parse_skill_md(content)
    desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
    if desc_match:
        desc = desc_match.group(1).strip()
    else:
        desc_match = re.search(r'description:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip()
        else:
            return True, "description不存在(无需检查)"
    # 检测重复的句子(以.或。分隔)
    sentences = re.split(r'[.。]', desc)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    seen = set()
    for s in sentences:
        if s in seen:
            return False, f"description含重复句子: '{s[:40]}...'"
        seen.add(s)
    # 检测前半段和后半段重复
    half = len(desc) // 2
    if half > 20:
        first = desc[:half].rstrip('.。 ')
        second = desc[half:].lstrip('.。 ')
        if first and second and first == second:
            return False, "description前后重复"
    return True, "无重复"


def check_template_content(skill_md_path):
    """检查是否含模板化套话"""
    content = skill_md_path.read_text(encoding='utf-8')
    issues = []
    for pattern in TEMPLATE_CONTENT_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            issues.append(f"模板短语: {matches[0][:50]}")
    return len(issues) == 0, issues


def check_placeholder_content(skill_md_path):
    """检查是否含占位符内容"""
    content = skill_md_path.read_text(encoding='utf-8')
    issues = []
    for pattern in PLACEHOLDER_CONTENT_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            issues.append(f"占位符: {matches[0][:50]}")
    return len(issues) == 0, issues


def check_duplicate_sentences_body(skill_md_path):
    """检查body中是否有重复句子"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    parts = content.split('---', 2)
    body = parts[2] if len(parts) >= 3 else content
    # 提取所有句子(以.或。或!或?结尾, 长度>20)
    sentences = re.findall(r'[^.。\n!?]{20,}[.。!?]', body)
    seen = {}
    duplicates = []
    for s in sentences:
        s = s.strip()
        if s in seen:
            duplicates.append(s[:50])
        else:
            seen[s] = True
    if duplicates:
        return False, f"{len(duplicates)}处重复句子: {duplicates[0][:40]}..."
    return True, "无重复"


def check_section_merging(skill_md_path):
    """检查章节是否错误合并(### 标题直接跟在上一行末尾)"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    # 检测: 某行末尾直接跟### 标题(无换行)
    merged = re.findall(r'[^\n]###\s', content)
    if merged:
        return False, f"{len(merged)}处章节合并"
    return True, "无合并"


def check_empty_input_table(skill_md_path):
    """检查输入格式表是否为空(只有表头没有数据行)"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    # 查找 ## 输入格式 后的表格
    input_section = re.search(r'##\s*输入格式\s*\n(.*?)(?=\n##\s|\Z)', content, re.DOTALL)
    if input_section:
        section_text = input_section.group(1)
        # 检查表格行数(排除表头和分隔行)
        table_rows = [l for l in section_text.split('\n') if l.strip().startswith('|') and '---' not in l]
        # 表头行通常1行, 如果只有表头没有数据行
        if len(table_rows) <= 1:
            return False, "输入格式表为空(只有表头)"
    return True, "正常"


def run_content_quality_check(skill_md_path):
    """运行全部内容质量检查(v3.1新增)"""
    results = {
        'path': str(skill_md_path),
        'slug': skill_md_path.parent.name,
        'checks': [],
        'pass_count': 0,
        'fail_count': 0,
    }
    checks = [
        ('dup_summary', 'summary无重复', lambda: check_duplicate_summary(skill_md_path)),
        ('dup_description', 'description无重复', lambda: check_duplicate_description(skill_md_path)),
        ('template_content', '无模板化套话', lambda: check_template_content(skill_md_path)),
        ('placeholder_content', '无占位符内容', lambda: check_placeholder_content(skill_md_path)),
        ('dup_sentences', 'body无重复句子', lambda: check_duplicate_sentences_body(skill_md_path)),
        ('section_merging', '章节无错误合并', lambda: check_section_merging(skill_md_path)),
        ('empty_input_table', '输入格式表非空', lambda: check_empty_input_table(skill_md_path)),
    ]
    for check_id, check_name, check_func in checks:
        try:
            passed, message = check_func()
            results['checks'].append({
                'id': check_id,
                'name': check_name,
                'passed': passed,
                'message': message if isinstance(message, str) else str(message),
            })
            if passed:
                results['pass_count'] += 1
            else:
                results['fail_count'] += 1
        except Exception as e:
            results['checks'].append({
                'id': check_id,
                'name': check_name,
                'passed': False,
                'message': f'检查异常: {e}',
            })
            results['fail_count'] += 1
    return results


# ============ v3.1新增: 内容质量修复函数 ============

def fix_duplicate_summary(skill_md_path):
    """修复summary重复: 取前半段"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    fm, body = parse_skill_md(content)
    match = re.search(r'^(summary):\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if not match:
        return False
    value = match.group(2).strip()
    half = len(value) // 2
    if half > 10:
        first_half = value[:half].rstrip('.。 ')
        second_half = value[half:].lstrip('.。 ')
        if first_half and second_half and first_half == second_half:
            new_value = first_half
            new_fm = fm.replace(match.group(0), f'{match.group(1)}: "{new_value}"')
            new_content = f'---{new_fm}---{body}'
            skill_md_path.write_text(new_content, encoding='utf-8')
            return True
    # 检测连续重复短语
    for i in range(10, len(value) // 2):
        segment = value[:i]
        if value.count(segment) >= 2 and len(segment) > 10:
            new_value = segment
            new_fm = fm.replace(match.group(0), f'{match.group(1)}: "{new_value}"')
            new_content = f'---{new_fm}---{body}'
            skill_md_path.write_text(new_content, encoding='utf-8')
            return True
    return False


def fix_duplicate_description(skill_md_path):
    """修复description重复: 去除重复句子"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    fm, body = parse_skill_md(content)
    desc_match = re.search(r'(description:\s*\|-\s*\n)((?:\s+.+\n?)+)', fm)
    if desc_match:
        desc = desc_match.group(2).strip()
        old_block = desc_match.group(0)
    else:
        desc_match = re.search(r'^(description:\s*)["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(2).strip()
            old_block = desc_match.group(0)
        else:
            return False
    # 去重: 按.或。分割, 保留首次出现
    sentences = re.split(r'([.。])', desc)
    deduped = []
    seen = set()
    i = 0
    while i < len(sentences):
        if i + 1 < len(sentences) and sentences[i+1] in '.。':
            sent = sentences[i] + sentences[i+1]
            sent_stripped = sent.strip()
            if sent_stripped and sent_stripped not in seen and len(sent_stripped) > 5:
                deduped.append(sent)
                seen.add(sent_stripped)
            i += 2
        else:
            if sentences[i].strip():
                deduped.append(sentences[i])
            i += 1
    new_desc = ''.join(deduped).strip()
    if new_desc != desc:
        if 'description: |-' in old_block:
            new_block = f'description: |-\n  {new_desc}\n'
        else:
            new_block = f'description: "{new_desc}"'
        new_fm = fm.replace(old_block, new_block)
        new_content = f'---{new_fm}---{body}'
        skill_md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def fix_template_content(skill_md_path):
    """修复模板化套话: 删除模板短语"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    original = content
    # 删除模板化短语所在的整行
    for pattern in TEMPLATE_CONTENT_PATTERNS:
        # 删除包含模板短语的**输入/处理/输出**行
        content = re.sub(r'\*\*输入\*\*:.*' + pattern + r'.*\n?', '', content)
        content = re.sub(r'\*\*处理\*\*:.*' + pattern + r'.*\n?', '', content)
        content = re.sub(r'\*\*输出\*\*:.*' + pattern + r'.*\n?', '', content)
        # 删除独立行的模板短语
        content = re.sub(r'^.*' + pattern + r'.*$', '', content, flags=re.MULTILINE)
    # 清理连续空行
    content = re.sub(r'\n{3,}', '\n\n', content)
    if content != original:
        skill_md_path.write_text(content, encoding='utf-8')
        return True
    return False


def fix_placeholder_content(skill_md_path):
    """修复占位符内容: 删除含占位符的行"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    original = content
    for pattern in PLACEHOLDER_CONTENT_PATTERNS:
        # 删除包含占位符的表格行
        content = re.sub(r'^\|.*' + pattern + r'.*\|?\s*$', '', content, flags=re.MULTILINE)
        # 删除包含占位符的整行(非表格)
        content = re.sub(r'^.*' + pattern + r'.*$', '', content, flags=re.MULTILINE)
    # 清理连续空行
    content = re.sub(r'\n{3,}', '\n\n', content)
    if content != original:
        skill_md_path.write_text(content, encoding='utf-8')
        return True
    return False


def fix_section_merging(skill_md_path):
    """修复章节合并: 在### 前添加换行"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    # 在非行首的### 前添加换行
    new_content = re.sub(r'([^\n])(###\s)', r'\1\n\2', content)
    if new_content != content:
        skill_md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def fix_empty_input_table(skill_md_path):
    """修复空输入表: 补充基本输入参数(v3.2增强: 支持空行和可变列数)"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    # v3.2: 更灵活的正则,允许header和separator之间有空行
    input_section = re.search(
        r'(##\s*输入格式\s*\n)\s*\n?(\|.*\|\n)\s*\n?(\|[-:\s|]+\|\n)(\s*\n*)(?=\n?##\s|\Z)',
        content
    )
    if input_section:
        # 补充基本输入行
        new_rows = "| instruction | string | 是 | 用户指令文本 |\n| context | string | 否 | 上下文信息 |\n"
        new_content = content[:input_section.end()] + new_rows + content[input_section.end():]
        skill_md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def fix_duplicate_sentences_body(skill_md_path):
    """修复body重复句子: 保留首次出现,删除后续重复(v3.2新增)"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    fm = parts[1]
    body = parts[2]

    # 与check_duplicate_sentences_body相同的句子提取逻辑
    sentence_pattern = r'[^.。\n!?]{20,}[.。!?]'
    all_matches = list(re.finditer(sentence_pattern, body))

    # 找出重复句子(非首次出现)
    seen = set()
    duplicates_to_remove = []  # (start, end, sentence)
    for m in all_matches:
        s = m.group().strip()
        if s in seen:
            duplicates_to_remove.append((m.start(), m.end(), s))
        else:
            seen.add(s)

    if not duplicates_to_remove:
        return False

    # 从后往前删除,避免位置偏移
    new_body = body
    for start, end, s in sorted(duplicates_to_remove, key=lambda x: -x[0]):
        # 找到句子所在行的范围
        line_start = new_body.rfind('\n', 0, start) + 1
        line_end = new_body.find('\n', end)
        if line_end == -1:
            line_end = len(new_body)
        line_content = new_body[line_start:line_end].strip()
        # 如果整行只有这个句子,删除整行
        if line_content == s or (len(line_content) < len(s) + 20 and s in line_content):
            new_body = new_body[:line_start] + new_body[line_end + 1:]
        else:
            # 只删除句子本身
            new_body = new_body[:start] + new_body[end:]

    # 清理连续空行
    new_body = re.sub(r'\n{3,}', '\n\n', new_body)

    if new_body != body:
        new_content = f'---{fm}---{new_body}'
        skill_md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def auto_fix_content(skill_md_path):
    """自动修复内容质量问题(v3.2增强)"""
    fixes = []
    # 1. 修复summary重复
    ok, _ = check_duplicate_summary(skill_md_path)
    if not ok and fix_duplicate_summary(skill_md_path):
        fixes.append('summary去重')
    # 2. 修复description重复
    ok, _ = check_duplicate_description(skill_md_path)
    if not ok and fix_duplicate_description(skill_md_path):
        fixes.append('description去重')
    # 3. 修复章节合并
    ok, _ = check_section_merging(skill_md_path)
    if not ok and fix_section_merging(skill_md_path):
        fixes.append('章节换行')
    # 4. 修复模板化内容
    ok, _ = check_template_content(skill_md_path)
    if not ok and fix_template_content(skill_md_path):
        fixes.append('模板内容清理')
    # 5. 修复占位符内容
    ok, _ = check_placeholder_content(skill_md_path)
    if not ok and fix_placeholder_content(skill_md_path):
        fixes.append('占位符清理')
    # 6. 修复空输入表
    ok, _ = check_empty_input_table(skill_md_path)
    if not ok and fix_empty_input_table(skill_md_path):
        fixes.append('输入表补充')
    # 7. 修复body重复句子 (v3.2新增)
    ok, _ = check_duplicate_sentences_body(skill_md_path)
    if not ok and fix_duplicate_sentences_body(skill_md_path):
        fixes.append('body去重')
    return fixes


def fix_name_folder(skill_md_path):
    """修复name与文件夹同名"""
    folder_name = skill_md_path.parent.name
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    # 替换name字段
    new_content = re.sub(
        r'^(name:\s*)["\']?[^"\'\n]+["\']?\s*$',
        rf'\g<1>{folder_name}',
        content,
        count=1,
        flags=re.MULTILINE
    )
    
    if new_content != content:
        skill_md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def fix_exaggeration_words(skill_md_path):
    """修复夸大词"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    original = content
    for old_word, new_word in EXAGGERATION_MAP.items():
        content = content.replace(old_word, new_word)
    
    if content != original:
        skill_md_path.write_text(content, encoding='utf-8')
        return True
    return False


def fix_xml_brackets(skill_md_path):
    """修复frontmatter中的XML尖括号"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            # 替换尖括号为全角
            fm_fixed = fm.replace('<', '〈').replace('>', '〉')
            if fm != fm_fixed:
                new_content = '---' + fm_fixed + '---' + parts[2]
                skill_md_path.write_text(new_content, encoding='utf-8')
                return True
    return False


def fix_reserved_words(skill_md_path):
    """修复保留词（不修改name字段，因为name必须与文件夹同名）"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    # 分离frontmatter和body
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
        else:
            fm = ''
            body = content
    else:
        fm = ''
        body = content
    
    # 替换映射
    replace_map = {
        'claude': 'ai-assistant',
        'anthropic': 'ai-provider',
        'openai': 'llm-provider',
        'chatgpt': 'ai-chat',
    }
    
    original_fm = fm
    original_body = body
    
    # 在frontmatter中：只替换displayName/summary/description，不替换name
    for word, replacement in replace_map.items():
        # 只替换displayName和summary行中的保留词
        for field in ['displayName', 'summary']:
            pattern = rf'(^{field}:\s*["\']?)(.+?)(["\']?\s*$)'
            def replace_in_field(m):
                return m.group(1) + re.sub(rf'\b{word}\b', replacement, m.group(2), flags=re.IGNORECASE) + m.group(3)
            fm = re.sub(pattern, replace_in_field, fm, flags=re.MULTILINE)
        
        # 替换description块中的保留词
        # description可能是 block style 或 inline style
        desc_block = re.search(r'(description:\s*\|-\s*\n)((?:\s+.+\n?)+)', fm)
        if desc_block:
            old_block = desc_block.group(0)
            new_text = re.sub(rf'\b{word}\b', replacement, desc_block.group(2), flags=re.IGNORECASE)
            fm = fm.replace(old_block, f"{desc_block.group(1)}{new_text}")
    
    # 在body中替换所有保留词
    for word, replacement in replace_map.items():
        body = re.sub(rf'\b{word}\b', replacement, body, flags=re.IGNORECASE)
    
    # 重建内容
    if fm != original_fm or body != original_body:
        if content.startswith('---'):
            new_content = f'---{fm}---{body}'
        else:
            new_content = body
        skill_md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def fix_tools_format(skill_md_path):
    """修复tools格式为YAML数组"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    # 查找tools字段
    tools_str_match = re.search(r'^tools:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if tools_str_match:
        tools_str = tools_str_match.group(1).strip()
        # 解析为列表
        if ',' in tools_str:
            tools_list = [t.strip().strip('"\'') for t in tools_str.split(',')]
        else:
            tools_list = [tools_str]
        
        # 清理每个工具项：移除前导的 "- " 或 "* "
        tools_list = [re.sub(r'^[-*]\s*', '', t.strip()) for t in tools_list]
        # 移除空项
        tools_list = [t for t in tools_list if t]
        
        if not tools_list:
            return False
        
        # 生成YAML数组格式
        yaml_tools = "tools:\n"
        for t in tools_list:
            yaml_tools += f"  - {t}\n"
        
        # 替换原tools字段
        new_content = re.sub(
            r'^tools:\s*["\']?.+?["\']?\s*$',
            yaml_tools.rstrip(),
            content,
            count=1,
            flags=re.MULTILINE
        )
        
        if new_content != content:
            skill_md_path.write_text(new_content, encoding='utf-8')
            return True
    return False


def fix_display_name_too_long(skill_md_path):
    """修复displayName过长"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    match = re.search(r'^displayName:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if match:
        value = match.group(1).strip()
        if len(value) > 20:
            # 截断到20字符
            new_value = value[:20]
            new_content = re.sub(
                r'^(displayName:\s*)["\']?.+?["\']?\s*$',
                rf'\g<1>{new_value}',
                content,
                count=1,
                flags=re.MULTILINE
            )
            if new_content != content:
                skill_md_path.write_text(new_content, encoding='utf-8')
                return True
    return False


def fix_summary_too_long(skill_md_path):
    """修复summary过长"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, _ = parse_skill_md(content)
    match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if match:
        value = match.group(1).strip()
        if len(value) > 100:
            # 截断到97字符加省略号
            new_value = value[:97] + '...'
            new_content = re.sub(
                r'^(summary:\s*)["\']?.+?["\']?\s*$',
                rf'\g<1>{new_value}',
                content,
                count=1,
                flags=re.MULTILINE
            )
            if new_content != content:
                skill_md_path.write_text(new_content, encoding='utf-8')
                return True
    return False


def fix_summary_style_description(skill_md_path):
    """修复摘要式描述：替换'本工具'等为更具体的表述"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    # 获取displayName用于替换
    fm, _ = parse_skill_md(content)
    name_match = re.search(r'^displayName:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    display_name = name_match.group(1).strip() if name_match else '此技能'
    
    # 替换映射
    replacements = {
        '本工具': display_name,
        '这是一个': '',
        '这是一款': '',
        '本技能用于帮助用户': display_name + '可',
        '帮助用户处理各种': '处理',
        '帮助用户完成各种': '完成',
    }
    
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # 清理多余空格
    content = re.sub(r'description:\s*\|-\s*\n\s*\s+', 'description: |-\n  ', content)
    
    if content != original:
        skill_md_path.write_text(content, encoding='utf-8')
        return True
    return False


def categorize_skill(slug, display_name, summary, description):
    """根据关键词对skill分类"""
    # 合并所有文本用于关键词匹配
    all_text = f"{slug} {display_name} {summary} {description}".lower()
    
    # 统计每个类别的匹配数
    category_scores = {}
    for category, keywords in MARKETING_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in all_text)
        if score > 0:
            category_scores[category] = score
    
    if category_scores:
        # 返回匹配数最多的类别
        best_category = max(category_scores, key=category_scores.get)
        return best_category
    
    return None


def expand_short_description(skill_md_path):
    """扩展过短的description（<150c）到150-280c"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    fm, body = parse_skill_md(content)
    
    # 提取当前description
    desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
    if desc_match:
        desc = desc_match.group(1).strip()
        old_block = desc_match.group(0)
    else:
        desc_match = re.search(r'description:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip()
            old_block = desc_match.group(0)
        else:
            return False
    
    desc_len = len(desc)
    if desc_len >= 150:
        return False  # 不需要扩展
    
    # 提取slug, displayName, summary用于分类
    slug = skill_md_path.parent.name
    name_match = re.search(r'^displayName:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    display_name = name_match.group(1).strip() if name_match else slug
    summary_match = re.search(r'^summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    summary = summary_match.group(1).strip() if summary_match else ''
    
    # 分类
    category = categorize_skill(slug, display_name, summary, desc)
    
    if category and category in TRIGGER_TEMPLATES:
        trigger = TRIGGER_TEMPLATES[category]
    else:
        # 默认触发词
        trigger = f"Use when 用户需要{display_name}相关功能时使用。不适用于超出本技能能力范围的复杂需求。"
    
    # 组合新description
    new_desc = desc.rstrip('。.') + '。' + trigger
    
    # 如果仍然太短，逐步添加更多上下文
    if len(new_desc) < 150:
        new_desc += f"适用于独立开发者、企业团队和自动化工作流场景。"
    
    # 如果仍然太短，添加更多详细信息
    if len(new_desc) < 150:
        new_desc += f"支持中文交互，无需复杂配置即开即用。"
    
    # 如果仍然太短，添加技术细节
    if len(new_desc) < 150:
        new_desc += f"输出结果可直接使用，减少二次加工成本。"
    
    # 如果太长，截断
    if len(new_desc) > 280:
        new_desc = new_desc[:277].rsplit('，', 1)[0] + '...'
    
    # 替换
    if 'description: |-' in old_block:
        new_block = f'description: |-\n  {new_desc}\n'
    else:
        new_block = f'description: "{new_desc}"'
    
    new_fm = fm.replace(old_block, new_block)
    if new_fm != fm:
        new_content = f'---{new_fm}---{body}'
        skill_md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def trim_long_skill(skill_md_path):
    """优化过长skill的行数：移除多余空行、引用块、分隔线等（不影响frontmatter）"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    lines = content.split('\n')
    original_count = len(lines)
    
    if original_count <= 500:
        return False
    
    # 分离frontmatter和body，后续操作只对body进行
    fm_text = ''
    body_text = content
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm_text = f'---{parts[1]}---'
            body_text = parts[2]
        elif len(parts) == 2:
            # frontmatter没有闭合---，不处理
            fm_text = ''
            body_text = content
    
    # 1. 移除body中的连续空行（最多保留1个空行）
    body_lines = body_text.split('\n')
    new_lines = []
    prev_empty = False
    for line in body_lines:
        is_empty = line.strip() == ''
        if is_empty and prev_empty:
            continue
        new_lines.append(line)
        prev_empty = is_empty
    
    # 2. 移除行尾空格
    new_lines = [line.rstrip() for line in new_lines]
    
    result = '\n'.join(new_lines)
    
    # 3. 移除body中的章节标题后的多余空行
    result = re.sub(r'(#{1,6}\s+.+)\n{2,}', r'\1\n', result)
    
    # 检查是否已经足够
    current_count = len((fm_text + result).split('\n'))
    if current_count > 500:
        # 4. 移除body中的水平分隔线（---, ***, ___独占一行）
        result = re.sub(r'\n(?:---|\*\*\*|___)\s*\n', '\n', result)
    
    current_count = len((fm_text + result).split('\n'))
    if current_count > 500:
        # 5. 移除body中的blockquote引用块（> 开头的行），但保留第一个
        blockquote_blocks = re.findall(r'((?:^>.*\n?)+)', result, re.MULTILINE)
        if len(blockquote_blocks) > 1:
            for block in blockquote_blocks[1:]:
                result = result.replace(block, '', 1)
    
    current_count = len((fm_text + result).split('\n'))
    if current_count > 500:
        # 6. 移除body代码块中的注释行
        def trim_code_comments(match):
            code = match.group(0)
            code_lines = code.split('\n')
            new_code_lines = []
            for line in code_lines:
                stripped = line.strip()
                if stripped.startswith('#') and not stripped.startswith('#!'):
                    if len(stripped) < 80:
                        continue
                new_code_lines.append(line)
            return '\n'.join(new_code_lines)
        
        result = re.sub(r'```[\s\S]*?```', trim_code_comments, result)
    
    # 再次清理连续空行
    body_lines = result.split('\n')
    new_lines = []
    prev_empty = False
    for line in body_lines:
        is_empty = line.strip() == ''
        if is_empty and prev_empty:
            continue
        new_lines.append(line)
        prev_empty = is_empty
    result = '\n'.join(new_lines)
    
    # 重建完整内容
    final_content = fm_text + result if fm_text else result
    
    new_count = len(final_content.split('\n'))
    
    if new_count < original_count:
        skill_md_path.write_text(final_content, encoding='utf-8')
        return True
    return False


def run_compliance_check(skill_md_path):
    """运行全部合规检查(含v3.1内容质量检查)"""
    results = {
        'path': str(skill_md_path),
        'slug': skill_md_path.parent.name,
        'checks': [],
        'pass_count': 0,
        'fail_count': 0,
    }
    
    checks = [
        ('name_folder', 'name与文件夹同名', lambda: check_name_folder_consistency(skill_md_path)),
        ('reserved_words', '无保留词', lambda: check_reserved_words(skill_md_path)),
        ('xml_brackets', '无XML尖括号', lambda: check_xml_brackets(skill_md_path)),
        ('exaggeration', '无夸大词', lambda: check_exaggeration_words(skill_md_path)),
        ('summary_style', '非摘要式描述', lambda: check_summary_style_description(skill_md_path)),
        ('line_count', '≤500行', lambda: check_line_count(skill_md_path)),
        ('license', 'license正确', lambda: check_license(skill_md_path)),
        ('tools_format', 'tools为YAML数组', lambda: check_tools_format(skill_md_path)),
        ('display_name', 'displayName≤20字符', lambda: check_display_name_length(skill_md_path)),
        ('summary_length', 'summary≤100字符', lambda: check_summary_length(skill_md_path)),
        ('hardcoded_keys', '无硬编码凭证', lambda: check_hardcoded_keys(skill_md_path)),
        ('desc_length', 'description 150-280c', lambda: check_description_length(skill_md_path)),
        # v3.1新增: 内容质量检查
        ('dup_summary', 'summary无重复', lambda: check_duplicate_summary(skill_md_path)),
        ('dup_description', 'description无重复', lambda: check_duplicate_description(skill_md_path)),
        ('template_content', '无模板化套话', lambda: check_template_content(skill_md_path)),
        ('placeholder_content', '无占位符内容', lambda: check_placeholder_content(skill_md_path)),
        ('dup_sentences', 'body无重复句子', lambda: check_duplicate_sentences_body(skill_md_path)),
        ('section_merging', '章节无错误合并', lambda: check_section_merging(skill_md_path)),
        ('empty_input_table', '输入格式表非空', lambda: check_empty_input_table(skill_md_path)),
    ]
    
    for check_id, check_name, check_func in checks:
        try:
            passed, message = check_func()
            results['checks'].append({
                'id': check_id,
                'name': check_name,
                'passed': passed,
                'message': message if isinstance(message, str) else str(message),
            })
            if passed:
                results['pass_count'] += 1
            else:
                results['fail_count'] += 1
        except Exception as e:
            results['checks'].append({
                'id': check_id,
                'name': check_name,
                'passed': False,
                'message': f'检查异常: {e}',
            })
            results['fail_count'] += 1
    
    return results


def auto_fix(skill_md_path):
    """自动修复合规问题"""
    fixes = []
    
    # 1. 修复name与文件夹同名
    ok, _ = check_name_folder_consistency(skill_md_path)
    if not ok and fix_name_folder(skill_md_path):
        fixes.append('name与文件夹同名')
    
    # 2. 修复夸大词
    ok, _ = check_exaggeration_words(skill_md_path)
    if not ok and fix_exaggeration_words(skill_md_path):
        fixes.append('夸大词替换')
    
    # 3. 修复XML尖括号
    ok, _ = check_xml_brackets(skill_md_path)
    if not ok and fix_xml_brackets(skill_md_path):
        fixes.append('XML尖括号替换')
    
    # 4. 修复保留词
    ok, _ = check_reserved_words(skill_md_path)
    if not ok and fix_reserved_words(skill_md_path):
        fixes.append('保留词替换')
    
    # 5. 修复tools格式
    ok, _ = check_tools_format(skill_md_path)
    if not ok and fix_tools_format(skill_md_path):
        fixes.append('tools格式')
    
    # 6. 修复displayName过长
    ok, _ = check_display_name_length(skill_md_path)
    if not ok and fix_display_name_too_long(skill_md_path):
        fixes.append('displayName截断')
    
    # 7. 修复summary过长
    ok, _ = check_summary_length(skill_md_path)
    if not ok and fix_summary_too_long(skill_md_path):
        fixes.append('summary截断')
    
    # 8. 修复description过长(调用v2.0的优化)
    ok, msg = check_description_length(skill_md_path)
    if not ok and '太长' in msg:
        try:
            content = skill_md_path.read_text(encoding='utf-8')
            if content.startswith('\ufeff'):
                content = content[1:]
            fm, body = parse_skill_md(content)
            new_fm, changed = optimize_description(fm)
            if changed:
                new_content = f'---\n{new_fm}\n---\n{body}'
                skill_md_path.write_text(new_content, encoding='utf-8')
                fixes.append('description精简')
        except Exception:
            pass  # 跳过无法自动修复的description
    
    # 9. 修复摘要式描述（"本工具"等）
    ok, _ = check_summary_style_description(skill_md_path)
    if not ok and fix_summary_style_description(skill_md_path):
        fixes.append('摘要式描述修复')
    
    # 10. 扩展过短的description（<150c → 150-280c）
    ok, msg = check_description_length(skill_md_path)
    if not ok and '太短' in msg:
        if expand_short_description(skill_md_path):
            fixes.append('description扩展')
    
    # 11. 优化过长skill的行数（>500行 → 移除多余空行）
    ok, msg = check_line_count(skill_md_path)
    if not ok:
        if trim_long_skill(skill_md_path):
            fixes.append('行数优化')
    
    # 12. v3.1新增: 内容质量修复
    content_fixes = auto_fix_content(skill_md_path)
    fixes.extend(content_fixes)
    
    return fixes


def get_all_skills():
    """获取所有skill路径"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("""
        SELECT slug, local_path FROM skills
        WHERE workflow_state != 'deprecated' AND local_path IS NOT NULL
        ORDER BY slug
    """)
    skills = [(r['slug'], r['local_path']) for r in c.fetchall()]
    conn.close()
    return skills


def get_packaged_skills():
    """获取60个packaged skills路径"""
    paths = []
    
    # JueJin 20个
    skillhub_dir = Path(r"d:\skills\packaged-skills\skillhub")
    for d in sorted(skillhub_dir.iterdir()):
        if d.is_dir():
            skill_md = d / "SKILL.md"
            if skill_md.exists():
                paths.append((d.name, str(skill_md)))
    
    # Open Source 40个
    opensource_dir = Path(r"d:\skills\opensource-skills\packaged")
    if opensource_dir.exists():
        for d in sorted(opensource_dir.iterdir()):
            if d.is_dir():
                skill_md = d / "SKILL.md"
                if skill_md.exists():
                    paths.append((d.name, str(skill_md)))
    
    return paths


def cmd_check(args):
    """检查所有skill合规性"""
    if args and args[0] == '--packaged':
        skills = get_packaged_skills()
        print(f"检查 {len(skills)} 个packaged skills...")
    else:
        skills = get_all_skills()
        print(f"检查 {len(skills)} 个skills...")
    
    all_results = []
    fail_stats = {}
    
    for slug, local_path in skills:
        skill_md = Path(local_path) / "SKILL.md"
        if not skill_md.exists():
            # 直接尝试local_path作为SKILL.md路径
            skill_md = Path(local_path)
            if not skill_md.exists():
                continue
        
        result = run_compliance_check(skill_md)
        all_results.append(result)
        
        if result['fail_count'] > 0:
            for check in result['checks']:
                if not check['passed']:
                    fail_stats[check['name']] = fail_stats.get(check['name'], 0) + 1
    
    # 汇总
    total = len(all_results)
    all_pass = sum(1 for r in all_results if r['fail_count'] == 0)
    has_fail = sum(1 for r in all_results if r['fail_count'] > 0)
    
    print(f"\n{'='*80}")
    print(f"合规检查报告")
    print(f"{'='*80}")
    print(f"总计: {total}个skill")
    print(f"  全部通过: {all_pass}个 ({all_pass/total*100:.1f}%)")
    print(f"  有失败项: {has_fail}个 ({has_fail/total*100:.1f}%)")
    
    if fail_stats:
        print(f"\n失败项统计(按检查项):")
        for name, count in sorted(fail_stats.items(), key=lambda x: -x[1]):
            print(f"  {name}: {count}个失败")
    
    # 保存报告
    report_path = DATA_DIR / "reports" / "compliance_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total': total,
            'all_pass': all_pass,
            'has_fail': has_fail,
            'fail_stats': fail_stats,
            'results': all_results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\n报告保存到: {report_path}")
    
    return all_results


def cmd_fix(args):
    """自动修复合规问题"""
    if args and args[0] == '--slug':
        slug = args[1]
        # 查找skill
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT local_path FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        conn.close()
        if not row:
            print(f"Skill '{slug}' 不存在")
            return
        skill_md = Path(row['local_path']) / "SKILL.md"
        if not skill_md.exists():
            skill_md = Path(row['local_path'])
        skills = [(slug, str(skill_md.parent))]
    elif args and args[0] == '--packaged':
        skills = get_packaged_skills()
    else:
        skills = get_all_skills()
    
    print(f"修复 {len(skills)} 个skills...")
    
    fixed_count = 0
    fix_stats = {}
    
    for slug, local_path in skills:
        skill_md = Path(local_path) / "SKILL.md"
        if not skill_md.exists():
            skill_md = Path(local_path)
            if not skill_md.exists():
                continue
        
        fixes = auto_fix(skill_md)
        if fixes:
            fixed_count += 1
            for fix in fixes:
                fix_stats[fix] = fix_stats.get(fix, 0) + 1
            print(f"  [FIXED] {slug}: {', '.join(fixes)}")
    
    print(f"\n{'='*80}")
    print(f"修复完成: {fixed_count}/{len(skills)} 个skill被修复")
    if fix_stats:
        print(f"\n修复统计:")
        for fix, count in sorted(fix_stats.items(), key=lambda x: -x[1]):
            print(f"  {fix}: {count}个")


def cmd_report():
    """生成合规报告"""
    report_path = DATA_DIR / "reports" / "compliance_report.json"
    if not report_path.exists():
        print("请先运行 check 命令")
        return
    
    with open(report_path, 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    print(f"\n{'='*80}")
    print(f"Skill合规报告 v3.0")
    print(f"生成时间: {report['timestamp']}")
    print(f"{'='*80}")
    
    print(f"\n总览:")
    print(f"  总计: {report['total']}个")
    print(f"  全部通过: {report['all_pass']}个 ({report['all_pass']/report['total']*100:.1f}%)")
    print(f"  有失败项: {report['has_fail']}个 ({report['has_fail']/report['total']*100:.1f}%)")
    
    print(f"\n失败项TOP10:")
    for name, count in sorted(report['fail_stats'].items(), key=lambda x: -x[1])[:10]:
        print(f"  {name}: {count}个 ({count/report['total']*100:.1f}%)")
    
    # 列出最严重的skill
    worst = sorted(report['results'], key=lambda x: -x['fail_count'])[:20]
    print(f"\n问题最多的20个skill:")
    for r in worst:
        if r['fail_count'] > 0:
            failed_names = [c['name'] for c in r['checks'] if not c['passed']]
            print(f"  {r['slug']}: {r['fail_count']}项失败 - {', '.join(failed_names)}")


def cmd_content_check(args):
    """v3.1新增: 内容质量检查"""
    if args and args[0] == '--slug':
        slug = args[1]
        skill_md = find_skill_md(slug)
        if not skill_md:
            print(f"Skill '{slug}' 的SKILL.md未找到")
            return
        skills = [(slug, str(skill_md.parent))]
    else:
        skills = get_all_skills()
    
    print(f"内容质量检查 {len(skills)} 个skills...")
    
    all_results = []
    issue_stats = {}
    
    for slug, local_path in skills:
        # v3.1.1修复: 优先使用find_skill_md搜索发布目录,而非数据库local_path
        skill_md = find_skill_md(slug)
        if not skill_md:
            # 回退到local_path
            skill_md = Path(local_path) / "SKILL.md"
            if not skill_md.exists():
                skill_md = Path(local_path)
                if not skill_md.exists():
                    continue
        
        result = run_content_quality_check(skill_md)
        all_results.append(result)
        
        if result['fail_count'] > 0:
            for check in result['checks']:
                if not check['passed']:
                    issue_stats[check['name']] = issue_stats.get(check['name'], 0) + 1
    
    total = len(all_results)
    all_pass = sum(1 for r in all_results if r['fail_count'] == 0)
    has_fail = sum(1 for r in all_results if r['fail_count'] > 0)
    
    print(f"\n{'='*80}")
    print(f"内容质量检查报告 v3.1")
    print(f"{'='*80}")
    print(f"总计: {total}个skill")
    print(f"  全部通过: {all_pass}个 ({all_pass/total*100:.1f}%)")
    print(f"  有内容问题: {has_fail}个 ({has_fail/total*100:.1f}%)")
    
    if issue_stats:
        print(f"\n问题分布(按检查项):")
        for name, count in sorted(issue_stats.items(), key=lambda x: -x[1]):
            print(f"  {name}: {count}个")
    
    # 保存报告
    report_path = DATA_DIR / "reports" / "content_quality_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total': total,
            'all_pass': all_pass,
            'has_fail': has_fail,
            'issue_stats': issue_stats,
            'results': all_results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\n报告保存到: {report_path}")
    
    return all_results


def cmd_content_fix(args):
    """v3.1新增: 内容质量修复"""
    if args and args[0] == '--slug':
        slug = args[1]
        skill_md = find_skill_md(slug)
        if not skill_md:
            print(f"Skill '{slug}' 的SKILL.md未找到")
            return
        skills = [(slug, str(skill_md.parent))]
    elif args and args[0] == '--top':
        # 只修复问题最多的N个skill
        n = int(args[1]) if len(args) > 1 else 50
        report_path = DATA_DIR / "reports" / "content_quality_report.json"
        if not report_path.exists():
            print("请先运行: python skill_batch_upgrader_v3.py content-check")
            return
        with open(report_path, 'r', encoding='utf-8') as f:
            report = json.load(f)
        # 按fail_count降序
        sorted_results = sorted(report['results'], key=lambda x: -x['fail_count'])
        top_slugs = [r['slug'] for r in sorted_results[:n] if r['fail_count'] > 0]
        skills = [(slug, '') for slug in top_slugs]
        print(f"修复问题最多的 {len(skills)} 个skills...")
    else:
        skills = get_all_skills()
        print(f"修复 {len(skills)} 个skills...")
    
    fixed_count = 0
    fix_stats = {}
    
    for slug, local_path in skills:
        # v3.1.1修复: 优先使用find_skill_md搜索发布目录
        skill_md = find_skill_md(slug)
        if not skill_md:
            # 回退到local_path
            skill_md = Path(local_path) / "SKILL.md"
            if not skill_md.exists():
                skill_md = Path(local_path)
                if not skill_md.exists():
                    continue
        
        fixes = auto_fix_content(skill_md)
        if fixes:
            fixed_count += 1
            for fix in fixes:
                fix_stats[fix] = fix_stats.get(fix, 0) + 1
            print(f"  [FIXED] {slug}: {', '.join(fixes)}")
    
    print(f"\n{'='*80}")
    print(f"内容质量修复完成: {fixed_count}/{len(skills)} 个skill被修复")
    if fix_stats:
        print(f"\n修复统计:")
        for fix, count in sorted(fix_stats.items(), key=lambda x: -x[1]):
            print(f"  {fix}: {count}个")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    args = sys.argv[2:] if len(sys.argv) > 2 else []
    
    if cmd == 'check':
        cmd_check(args)
    elif cmd == 'fix':
        cmd_fix(args)
    elif cmd == 'report':
        cmd_report()
    elif cmd == 'content-check':
        cmd_content_check(args)
    elif cmd == 'content-fix':
        cmd_content_fix(args)
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)


if __name__ == '__main__':
    main()
