#!/usr/bin/env python3
"""
Skill批量升级脚本 v2.0
提供SKILL.md解析、章节检查、描述优化等基础功能。

v3.0在此基础上增加平台合规检查、营销优化等功能。
本文件为v3提供基础函数接口,复用skill_core.parser单一来源。

Usage:
    from skill_batch_upgrader_v2 import (
        SECTION_MAP, DOMESTIC_ALTERNATIVES,
        parse_skill_md, find_section_header, check_missing_sections,
        extract_section_content, rename_section, optimize_description,
        generate_section_content, upgrade_skill
    )
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN
# === End Phase 1 ===


import re
from pathlib import Path

# 复用skill_core.parser的解析逻辑(单一来源原则)
_sys.path.insert(0, str(_Path(__file__).resolve().parent / "skill_core"))
from parser import parse_frontmatter


# ============================================================
# 常量定义
# ============================================================

# 标准章节映射: 章节名 → 默认优先级权重
SECTION_MAP = {
    '核心能力': 1,
    '适用场景': 2,
    '使用流程': 3,
    '依赖说明': 4,
    '常见问题': 5,
    '已知限制': 6,
    '错误处理': 7,
    '示例': 8,
}

# 国外→国内服务替代映射
DOMESTIC_ALTERNATIVES = {
    'GitHub': 'Gitee',
    'GitLab': 'Gitee',
    'OpenAI': '通义千问',
    'Anthropic Claude': '通义千问',
    'Claude': '通义千问',
    'GPT-4': '通义千问',
    'ChatGPT': '通义千问',
    'Slack': '飞书',
    'Discord': '钉钉',
    'Telegram': '飞书',
    'Twitter': '微博',
    'Reddit': '贴吧',
    'YouTube': 'B站',
    'Vercel': '阿里云函数计算',
    'Netlify': '腾讯云CloudBase',
    'AWS': '阿里云',
    'Google Cloud': '阿里云',
    'Azure': '阿里云',
    'Stripe': '支付宝/微信支付',
    'PayPal': '支付宝',
    'Twilio': '阿里云短信',
    'SendGrid': '阿里云邮件推送',
    'Notion': '飞书文档',
    'Airtable': '飞书多维表格',
    'Zapier': 'n8n',
    'IFTTT': 'n8n',
}


# ============================================================
# 解析函数
# ============================================================

def parse_skill_md(content: str) -> tuple:
    """解析SKILL.md内容,返回(raw_frontmatter, body)

    与skill_core.parser.parse_frontmatter互补:
    - parse_frontmatter返回dict(结构化)
    - parse_skill_md返回tuple(原始文本, 供正则操作)

    参数:
        content: SKILL.md文件内容字符串

    返回:
        (fm_raw, body):
            fm_raw: frontmatter原始文本(不含---分隔符)
            body: 正文内容(---之后的全部文本)
    """
    # 去BOM
    if content.startswith('\ufeff'):
        content = content[1:]

    # 匹配 --- ... ---
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not fm_match:
        return ('', content)

    fm_raw = fm_match.group(1)
    body = content[fm_match.end():]

    return (fm_raw, body)


# ============================================================
# 章节操作函数
# ============================================================

def find_section_header(body: str, section_name: str) -> int:
    """查找章节标题位置

    参数:
        body: 正文内容
        section_name: 章节名称(不含##前缀)

    返回:
        章节标题在body中的起始位置,未找到返回-1
    """
    pattern = rf'^##\s+{re.escape(section_name)}\s*$'
    match = re.search(pattern, body, re.MULTILINE)
    return match.start() if match else -1


def check_missing_sections(fm: str, body: str) -> list:
    """检查缺失的标准章节

    参数:
        fm: frontmatter原始文本(未使用,保留参数兼容性)
        body: 正文内容

    返回:
        缺失的章节名列表
    """
    missing = []
    for section_name in SECTION_MAP:
        if find_section_header(body, section_name) == -1:
            missing.append(section_name)
    return missing


def extract_section_content(body: str, section_name: str) -> str:
    """提取章节内容(从标题到下一个##或文件末尾)

    参数:
        body: 正文内容
        section_name: 章节名称

    返回:
        章节内容字符串(不含标题行),未找到返回空字符串
    """
    pos = find_section_header(body, section_name)
    if pos == -1:
        return ''

    # 从章节标题之后开始
    after_header = body[pos:]
    lines = after_header.split('\n')

    # 跳过标题行
    content_lines = lines[1:]

    # 收集内容直到下一个 ## 标题
    result = []
    for line in content_lines:
        if re.match(r'^##\s+', line):
            break
        result.append(line)

    return '\n'.join(result).strip()


def rename_section(body: str, old_name: str, new_name: str) -> str:
    """重命名章节标题

    参数:
        body: 正文内容
        old_name: 原章节名
        new_name: 新章节名

    返回:
        修改后的body,未找到原章节返回原body
    """
    pattern = rf'^(##\s+){re.escape(old_name)}\s*$'
    replacement = rf'\g<1>{new_name}'
    new_body, count = re.subn(pattern, replacement, body, flags=re.MULTILINE)
    return new_body if count > 0 else body


# ============================================================
# 描述优化函数
# ============================================================

def optimize_description(fm: str) -> tuple:
    """优化description长度到150-280范围

    参数:
        fm: frontmatter原始文本

    返回:
        (new_fm, changed):
            new_fm: 修改后的frontmatter文本
            changed: 是否发生了修改
    """
    # 提取当前description
    # 支持两种格式: description: "..." 或 description: |-\n  ...
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
            return (fm, False)

    desc_len = len(desc)
    changed = False
    new_desc = desc

    # 过长: 截断到280
    if desc_len > MAX_DESCRIPTION_LEN:
        new_desc = desc[:MAX_DESCRIPTION_LEN - 3] + '...'
        changed = True
    # 过短: 补充上下文
    elif desc_len < MIN_DESCRIPTION_LEN:
        # 尝试从summary提取信息
        summary_match = re.search(r'summary:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        summary = summary_match.group(1).strip() if summary_match else ''

        # 逐步补充
        new_desc = desc.rstrip('。.')

        if summary and summary not in new_desc:
            new_desc += f'。{summary}'

        if len(new_desc) < MIN_DESCRIPTION_LEN:
            new_desc += '。支持多种输入格式,输出结构化结果,适用于独立开发者与一人公司效率提升'

        if len(new_desc) < MIN_DESCRIPTION_LEN:
            new_desc += '。支持中文交互,无需复杂配置即开即用'

        if len(new_desc) < MIN_DESCRIPTION_LEN:
            new_desc += '。输出结果可直接使用,减少二次加工成本'

        if len(new_desc) > MAX_DESCRIPTION_LEN:
            new_desc = new_desc[:MAX_DESCRIPTION_LEN - 3] + '...'

        changed = True

    if not changed:
        return (fm, False)

    # 重建description行
    if 'description: |-' in old_block:
        new_block = f'description: |-\n  {new_desc}\n'
    else:
        new_block = f'description: "{new_desc}"'

    new_fm = fm.replace(old_block, new_block)
    return (new_fm, True)


# ============================================================
# 章节内容生成函数
# ============================================================

def generate_section_content(section_name: str, skill_data: dict) -> str:
    """生成标准章节模板内容

    参数:
        section_name: 章节名称
        skill_data: skill数据dict(含frontmatter fields和body)

    返回:
        章节内容字符串(含##标题行)
    """
    fields = skill_data.get('fields', {})
    slug = fields.get('slug', fields.get('name', 'skill'))
    display_name = fields.get('displayName', slug)
    summary = fields.get('summary', '')

    templates = {
        '核心能力': f"""## 核心能力

- {summary or display_name}
- 触发关键词: {slug}, 自动化, 效率提升, 工具""",
        '适用场景': f"""## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景""",
        '使用流程': f"""## 使用流程

1. 用户发起请求
2. Skill解析请求参数
3. 执行核心逻辑
4. 返回结构化结果""",
        '依赖说明': f"""## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务""",
        '常见问题': f"""## 常见问题

### Q1: 如何开始使用{display_name}？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: {display_name}有什么限制？
A: 请参考已知限制章节了解具体限制。""",
        '已知限制': f"""## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力""",
        '错误处理': f"""## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试 |""",
        '示例': f"""## 示例

### 示例1：基础用法

```
用户请求: 执行{display_name}
Skill响应: 处理完成,返回结果
```""",
    }

    return templates.get(section_name, f'## {section_name}\n\n(待补充)')


# ============================================================
# 综合升级函数
# ============================================================

def upgrade_skill(skill_md_path: Path) -> dict:
    """综合升级单个skill: 章节补全 + 描述优化

    参数:
        skill_md_path: SKILL.md文件路径

    返回:
        {
            'changed': bool,     # 是否发生了修改
            'changes': list,     # 修改项列表
        }
    """
    path = Path(skill_md_path)
    if not path.exists():
        return {'changed': False, 'changes': ['文件不存在']}

    content = path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]

    fm_raw, body = parse_skill_md(content)
    changes = []
    new_body = body
    new_fm = fm_raw

    # 1. 检查并补充缺失章节
    missing = check_missing_sections(fm_raw, new_body)
    for section_name in missing:
        # 使用parse_frontmatter获取结构化数据
        parsed = parse_frontmatter(content)
        section_content = generate_section_content(section_name, parsed)
        new_body = new_body.rstrip() + '\n\n' + section_content + '\n'
        changes.append(f'补充章节: {section_name}')

    # 2. 优化description长度
    new_fm, desc_changed = optimize_description(new_fm)
    if desc_changed:
        changes.append('description长度优化')

    # 3. 写回文件(如果有修改)
    changed = len(changes) > 0
    if changed:
        new_content = f'---\n{new_fm}\n---\n{new_body}'
        path.write_text(new_content, encoding='utf-8')

    return {'changed': changed, 'changes': changes}
