#!/usr/bin/env python3
"""
Skill批量升级脚本 v2.0 - 基础层

为 skill_batch_upgrader_v3.py 提供基础函数支持。
复用 skill_core.parser 单一来源，消除重复实现。

主要功能:
1. parse_skill_md - 解析 SKILL.md frontmatter 和 body
2. optimize_description - 精简过长的 description
3. 章节操作函数 - 查找/提取/重命名章节
4. upgrade_skill - 综合升级入口

Usage:
    被 v3 导入使用，不直接运行
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN
# === End Phase 1 ===

import re
from pathlib import Path
from skill_core.parser import parse_frontmatter

# v2.0 标准章节映射
SECTION_MAP = {
    '能力清单': '## 能力清单',
    '使用场景': '## 使用场景',
    '操作步骤': '## 操作步骤',
    '依赖说明': '## 依赖说明',
    '注意事项': '## 注意事项',
    '设计动机': '## 设计动机',
    '使用流程': '## 使用流程',
    '常见问题': '## 常见问题',
    '更新日志': '## 更新日志',
}

# v2.0 国外服务到国内服务的映射
DOMESTIC_ALTERNATIVES = {
    'GitHub': 'Gitee',
    'OpenAI': '通义千问',
    'Google': '百度',
    'AWS': '阿里云',
    'Azure': '腾讯云',
    'Stripe': '微信支付',
    'Twilio': '阿里云短信',
    'SendGrid': '阿里云邮件推送',
    'Vercel': '阿里云函数计算',
    'Heroku': '阿里云容器服务',
    'Slack': '飞书',
    'Notion': '语雀',
    'Airtable': '腾讯文档',
    'Zapier': '腾讯自动化',
    'YouTube': 'B站',
    'Twitter': '微博',
}


def parse_skill_md(content: str):
    """解析 SKILL.md 的 frontmatter 和 body

    复用 skill_core.parser.parse_frontmatter (单一来源原则)

    Args:
        content: SKILL.md 文件内容

    Returns:
        tuple: (raw_frontmatter, body)
            - raw_frontmatter: str, --- 之间的原始文本(不含 --- 标记)
            - body: str, 第二个 --- 之后的内容
    """
    result = parse_frontmatter(content)
    return result['raw'], result['body']


def optimize_description(fm_raw: str):
    """精简过长的 description

    检查 frontmatter 中 description 的长度:
    - 超过 MAX_DESCRIPTION_LEN(280) 时截断到 280 字符(在句号/逗号处截断)
    - 其他情况不修改

    Args:
        fm_raw: str, 原始 frontmatter 文本

    Returns:
        tuple: (new_fm_raw, changed)
            - new_fm_raw: str, 修改后的 frontmatter 文本
            - changed: bool, 是否进行了修改
    """
    # 尝试匹配块标量格式 description: |-
    block_match = re.search(
        r'(description:\s*\|-\s*\n)((?:\s+.+\n?)+)',
        fm_raw
    )
    if block_match:
        prefix = block_match.group(1)
        desc_lines = block_match.group(2)
        # 提取纯文本
        desc_text = '\n'.join(
            line.strip() for line in desc_lines.strip().split('\n')
        )
        if len(desc_text) > MAX_DESCRIPTION_LEN:
            # 在 MAX_DESCRIPTION_LEN 范围内找最后一个句号或逗号
            truncated = desc_text[:MAX_DESCRIPTION_LEN]
            last_punct = max(
                truncated.rfind('。'),
                truncated.rfind('，'),
                truncated.rfind('. '),
                truncated.rfind(', '),
            )
            if last_punct > MIN_DESCRIPTION_LEN // 2:
                truncated = truncated[:last_punct + 1]
            else:
                truncated = truncated.rstrip() + '。'
            # 重建块标量格式
            new_desc_lines = '\n'.join(
                f'  {line}' for line in truncated.split('\n')
            )
            new_block = f'{prefix}{new_desc_lines}\n'
            new_fm = fm_raw[:block_match.start()] + new_block + fm_raw[block_match.end():]
            return new_fm, True
        return fm_raw, False

    # 尝试匹配普通键值对格式 description: "xxx"
    kv_match = re.search(
        r'(description:\s*)["\']?(.+?)["\']?\s*$',
        fm_raw,
        re.MULTILINE
    )
    if kv_match:
        prefix = kv_match.group(1)
        desc_text = kv_match.group(2)
        if len(desc_text) > MAX_DESCRIPTION_LEN:
            truncated = desc_text[:MAX_DESCRIPTION_LEN]
            last_punct = max(
                truncated.rfind('。'),
                truncated.rfind('，'),
                truncated.rfind('. '),
                truncated.rfind(', '),
            )
            if last_punct > MIN_DESCRIPTION_LEN // 2:
                truncated = truncated[:last_punct + 1]
            else:
                truncated = truncated.rstrip() + '。'
            new_line = f'{prefix}"{truncated}"'
            new_fm = fm_raw[:kv_match.start()] + new_line + fm_raw[kv_match.end():]
            return new_fm, True
        return fm_raw, False

    # description 不存在，无法优化
    return fm_raw, False


def find_section_header(body: str, section_name: str):
    """查找章节标题在 body 中的位置

    Args:
        body: SKILL.md 正文
        section_name: 章节名称(不含 ## 前缀)

    Returns:
        int: 章节标题的行偏移(0-based)，未找到返回 -1
    """
    pattern = rf'^#+\s*{re.escape(section_name)}\s*$'
    match = re.search(pattern, body, re.MULTILINE)
    if match:
        return body[:match.start()].count('\n')
    return -1


def check_missing_sections(fm_raw: str, body: str):
    """检查缺失的标准章节

    Args:
        fm_raw: frontmatter 原始文本
        body: SKILL.md 正文

    Returns:
        list: 缺失的章节名称列表
    """
    missing = []
    for section_name in SECTION_MAP:
        if find_section_header(body, section_name) == -1:
            missing.append(section_name)
    return missing


def extract_section_content(body: str, section_name: str):
    """提取指定章节的内容

    Args:
        body: SKILL.md 正文
        section_name: 章节名称

    Returns:
        str: 章节内容(不含标题行)，未找到返回空字符串
    """
    pattern = rf'^#+\s*{re.escape(section_name)}\s*\n(.*?)(?=\n#+\s|\Z)'
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return ''


def rename_section(body: str, old_name: str, new_name: str):
    """重命名章节标题

    Args:
        body: SKILL.md 正文
        old_name: 原章节名称
        new_name: 新章节名称

    Returns:
        str: 修改后的 body，未找到原章节返回原 body
    """
    pattern = rf'^(#+\s*){re.escape(old_name)}(\s*)$'
    replacement = rf'\g<1>{new_name}\g<2>'
    new_body, count = re.subn(pattern, replacement, body, count=1, flags=re.MULTILINE)
    return new_body


def generate_section_content(section_name: str, skill_data: dict):
    """生成章节的默认内容

    Args:
        section_name: 章节名称
        skill_data: dict, 包含 skill 元数据(name, description 等)

    Returns:
        str: 章节内容(含标题行)
    """
    name = skill_data.get('name', '本技能')
    desc = skill_data.get('description', '')

    templates = {
        '能力清单': f'## 能力清单\n\n- {desc}\n',
        '使用场景': f'## 使用场景\n\n- 适用于需要 {name} 功能的场景\n',
        '操作步骤': f'## 操作步骤\n\n1. 确认环境配置完成\n2. 调用 {name} 相关接口\n3. 处理返回结果\n',
        '依赖说明': f'## 依赖说明\n\n- 需要有效的 LLM API Key\n- Python 3.8+\n',
        '注意事项': f'## 注意事项\n\n- 请勿在公开代码库中暴露 API Key\n- 建议在沙箱环境中运行\n',
    }
    return templates.get(section_name, f'## {section_name}\n\n(待补充)\n')


def upgrade_skill(skill_md_path):
    """综合升级 skill (v2.0 基础版)

    调用 v3 的 auto_fix 进行完整升级。
    此函数为 v3 的 upgrade_skill 提供兼容入口。

    Args:
        skill_md_path: Path, SKILL.md 文件路径

    Returns:
        dict: 升级结果 {'fixes': [...], 'errors': [...]}
    """
    skill_md_path = Path(skill_md_path)
    if not skill_md_path.exists():
        return {'fixes': [], 'errors': [f'文件不存在: {skill_md_path}']}

    # 基础检查: 文件可读
    try:
        content = skill_md_path.read_text(encoding='utf-8')
        if content.startswith('\ufeff'):
            content = content[1:]
            skill_md_path.write_text(content, encoding='utf-8')
    except Exception as e:
        return {'fixes': [], 'errors': [f'读取失败: {e}']}

    # 调用 v3 的完整 auto_fix (延迟导入避免循环)
    try:
        from skill_batch_upgrader_v3 import auto_fix
        return auto_fix(skill_md_path)
    except ImportError:
        # v3 不可用时执行基础修复
        fixes = []
        fm_raw, body = parse_skill_md(content)

        # 基础: 确保有 frontmatter
        if not fm_raw.strip():
            fixes.append('警告: 无 frontmatter')

        return {'fixes': fixes, 'errors': []}
