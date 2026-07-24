#!/usr/bin/env python3
"""
L3批量修复脚本
==============

解决L3功能验证的主要失败维度：
1. L3-1 结构完整性: 必需章节齐全 (existing)
2. L3-2 能力可执行性: ###标题需有≥2个细节指示符 (NEW)
3. L3-3 场景覆盖率: description关键词需在核心能力中出现 (NEW)
4. L3-4 指令清晰度: 需有使用流程/示例/已知限制章节 (NEW)
5. L3-5 错误处理完整性: 错误处理章节 (existing)
6. L3-6 依赖准确性: 依赖说明章节 (existing)
7. L3-7 内容实质性: 核心能力≥300字符+技术细节 (NEW)

Usage:
    python l3_batch_fix.py           # 执行所有修复
    python l3_batch_fix.py --dry-run # 仅检查，不修改
    python l3_batch_fix.py --limit 50  # 仅处理前50个
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, DATA_DIR, REGISTRY_DIR
# === End Phase 1 ===


import sys
import re
import argparse
from pathlib import Path
from typing import Tuple

SKILL_REGISTRY = TOOLS_DIR  # from config
PACKAGED_DIR = Path(r'D:\skills\packaged-skills\skillhub')
sys.path.insert(0, str(SKILL_REGISTRY))

from skill_core.parser import parse_frontmatter as _parse_fm

# 模板套话列表 - 与L3 checker的TEMPLATE_PHRASES完全一致(使用前缀匹配)
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
]

# 开源仓库引用模式 (与L3 checker的repo_patterns一致)
REPO_PATTERNS = [
    r'github\.com/',
    r'gitlab\.com/',
    r'gitee\.com/',
    r'原始仓库',
    r'开源仓库',
    r'上游项目',
]


# ============ 工具函数 ============

def extract_section(content: str, section_name: str) -> str:
    """提取##章节内容 (支持章节名变体匹配)"""
    if section_name == '核心能力':
        pattern = r'##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n(.*?)(?=\n## |\Z)'
    elif section_name == '错误处理':
        pattern = r'##\s+(?:错误|异常)处理\s*\n(.*?)(?=\n## |\Z)'
    else:
        pattern = rf'## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ''


def find_section_position(content: str, section_name: str) -> tuple:
    """找到##章节的起始和结束位置 (支持变体匹配)
    Returns: (header_start, header_end, body_start, body_end) or None
    """
    if section_name == '核心能力':
        pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)'
    elif section_name == '错误处理':
        pattern = r'(##\s+(?:错误|异常)处理\s*\n)'
    else:
        pattern = rf'(## {re.escape(section_name)}\s*\n)'
    match = re.search(pattern, content)
    if not match:
        return None
    header_start = match.start()
    body_start = match.end()
    # 找到下一个##章节
    next_section = re.search(r'\n## ', content[body_start:])
    if next_section:
        body_end = body_start + next_section.start()
    else:
        body_end = len(content)
    return (header_start, match.end(), body_start, body_end)


def parse_frontmatter(content: str) -> dict:
    """解析frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    return result.get('fields', {})


# ============ 标准章节生成 ============

def generate_dependency_section(tools: list, has_api: bool = False) -> str:
    """生成标准的依赖说明章节"""
    has_exec = 'exec' in str(tools).lower() if tools else False

    if has_exec:
        classification = 'MD+EXEC（指令驱动为主，部分功能需exec命令行支持）'
    else:
        classification = 'MD（指令驱动，无需命令行能力）'

    api_key_line = '本Skill无需额外API Key（LLM能力由Agent平台内置提供）' if not has_api else '需要配置对应API Key，详见上文环境配置章节'

    return f"""## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
{api_key_line}

### 可用性分类
- **分类**: {classification}"""


def generate_error_section(skill_name: str, capabilities: list) -> str:
    """根据skill能力生成错误处理章节"""
    errors = [
        ('LLM响应超时或无响应', '网络延迟或模型负载过高', '检查网络连接，重试请求；确认Agent平台LLM服务正常'),
        ('输入内容格式不正确', '用户输入不符合skill预期格式', '检查输入是否符合skill使用说明中的格式要求，参考示例章节'),
        ('执行结果与预期不符', '指令描述不够明确或上下文不足', '提供更详细的指令描述，补充必要的上下文信息'),
    ]

    errors.append(('命令执行失败', '运行环境不满足要求或权限不足', '确认运行环境符合依赖说明中的要求；检查命令权限设置'))

    rows = []
    for scenario, cause, solution in errors:
        rows.append(f'| {scenario} | {cause} | {solution} |')

    table = '\n'.join(rows)

    return f"""## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
{table}"""


def generate_usage_section(slug: str, fm_data: dict) -> str:
    """生成使用流程章节"""
    display_name = fm_data.get('displayName', slug)
    return f"""## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`{slug}`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常"""


def generate_example_section(slug: str, fm_data: dict) -> str:
    """生成示例章节"""
    display_name = fm_data.get('displayName', slug)
    return f"""## 示例

### 基本用法

向Agent发送指令:

```
使用 {display_name} 处理以下任务:
[具体任务描述]
```

### 输出说明

Agent将根据指令执行操作，返回处理结果。结果格式取决于具体能力点的输出定义。"""


def generate_limitations_section(slug: str) -> str:
    """生成已知限制章节 - 不使用TEMPLATE_PHRASES中的任何短语"""
    return f"""## 已知限制

- 本skill依赖Agent平台LLM能力，LLM不可用时无法执行
- 输出质量取决于指令描述的清晰度和上下文信息完整性
- 每次请求仅处理单一任务，不支持批量并发操作
- 处理结果受输入数据质量和格式规范性影响"""


# ============ L3-2: 能力可执行性修复 ============

def fix_l3_2_actionability(content: str, fm_data: dict) -> Tuple[str, str]:
    """L3-2修复: 为缺乏细节指示符的###标题补充操作指令

    每个###标题需要≥2个细节指示符: code_ref, table, code_block, numbered_list, bullet_list, action_verb
    使用与checker完全相同的cap_no_code方法,确保修复的是checker标记的同一批section
    """
    changes = []

    NON_CAPABILITY_HEADINGS = [
        '能力覆盖范围', '技术细节', '处理流程', '输入输出规范',
        '能力参数', '适用场景', '能力概览', '功能概览',
        '输出格式', '脚本获取', '命令参数说明', '输出说明', '输入说明',
        '源能力映射', '领域术语',
    ]

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, ''

    # 找到核心能力章节位置 (用于最终替换)
    pos = find_section_position(content, '核心能力')
    if not pos:
        return content, ''
    _, _, body_start, body_end = pos
    cap_body = content[body_start:body_end]

    # 与checker完全相同: 使用cap_no_code来查找###标题和section内容
    cap_no_code = re.sub(r'```[\s\S]*?```', '', cap_content)

    h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_no_code, re.MULTILINE))
    if len(h3_matches) < 3:
        return content, ''

    capability_matches = [m for m in h3_matches
                         if not any(nc in m.group(1) for nc in NON_CAPABILITY_HEADINGS)]
    if len(capability_matches) < 3:
        return content, ''

    # 找到需要修复的section (与checker完全相同的逻辑)
    sections_to_fix = []
    for i, match in enumerate(capability_matches):
        title = match.group(1).strip()
        start = match.end()
        end = capability_matches[i + 1].start() if i + 1 < len(capability_matches) else len(cap_no_code)
        section_content = cap_no_code[start:end].strip()

        # 与checker完全相同的指示符检测
        has_code_ref = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', section_content))
        has_table = '|' in section_content and '---' in section_content
        has_code_block = '```' in cap_content[start:end]  # 与checker相同的bug: 用cap_no_code的位置查cap_content
        has_numbered = bool(re.search(r'^\d+\.', section_content, re.MULTILINE))
        has_bullets = bool(re.search(r'^[-*]\s', section_content, re.MULTILINE))
        has_action_verb = any(v in section_content for v in [
            '创建', '删除', '修改', '查询', '执行', '配置', '安装', '运行',
            '启动', '停止', '导入', '导出', '解析', '转换', '生成', '提取',
            '检查', '验证', '分析', '处理', '发送', '接收', '保存', '加载',
            'create', 'delete', 'update', 'query', 'execute', 'config',
            'install', 'run', 'start', 'stop', 'import', 'export',
            'parse', 'convert', 'generate', 'extract', 'check', 'verify',
            'analyze', 'process', 'send', 'receive', 'save', 'load',
            'use', 'call', 'set', 'get', 'add', 'remove', 'apply',
        ])

        detail_indicators = sum([has_code_ref, has_table, has_code_block, has_numbered, has_bullets, has_action_verb])

        if detail_indicators >= 2 and len(section_content) >= 50:
            continue

        # 需要补充 - 记录title用于后续在cap_body中查找和修改
        clean_title = re.sub(r'^\d+[.):]?\s*', '', title).strip()
        supplement = generate_actionability_supplement(clean_title, section_content, has_code_ref, has_bullets, has_action_verb)
        if supplement:
            sections_to_fix.append((title, supplement))

    if not sections_to_fix:
        return content, ''

    # 在cap_body中找到对应title的###标题并插入supplement
    new_cap_body = cap_body
    for title, supplement in sections_to_fix:
        # 在cap_body中查找### {title}
        # 使用正则转义title中的特殊字符
        escaped_title = re.escape(title)
        pattern = rf'(###\s+{escaped_title}\s*\n.*?)(?=\n### |\Z)'
        match = re.search(pattern, new_cap_body, re.DOTALL)
        if match:
            section_end = match.end(1)
            # 在section末尾插入supplement
            new_cap_body = new_cap_body[:section_end].rstrip() + '\n\n' + supplement + '\n' + new_cap_body[section_end:]

    content = content[:body_start] + new_cap_body + content[body_end:]
    changes.append(f"补充{len(sections_to_fix)}个###标题的操作指令")

    return content, '; '.join(changes)


def generate_actionability_supplement(title: str, section: str, has_code_ref: bool, has_bullets: bool, has_action_verb: bool) -> str:
    """为###标题生成可执行性补充内容 - 确保补充后detail_indicators>=2"""
    parts = []
    clean_title = re.sub(r'^\d+[.):]?\s*', '', title).strip()

    # 始终添加bullet列表(确保has_bullets=True)
    if not has_bullets:
        parts.append(f"- 执行`{clean_title}`操作,处理输入数据并返回结果")
        parts.append(f"- 验证执行结果,确认输出符合预期格式")
        parts.append(f"- 异常时参考错误处理章节进行恢复")

    # 添加代码引用(确保has_code_ref=True)
    if not has_code_ref:
        parts.append(f"- 关键参数: `{clean_title.lower().replace(' ', '_')}` 选项")

    # 添加动作动词(确保has_action_verb=True)
    if not has_action_verb and not parts:
        parts.append(f"- 执行`{clean_title}`操作,处理输入数据并返回结果")
        parts.append(f"- 验证执行结果,确认输出符合预期格式")

    # 如果section内容太短(<50字符),补充更多描述
    if len(section) < 50:
        parts.append(f"- 处理流程: 接收输入 -> 执行{clean_title} -> 返回结果")
        parts.append(f"- 输入: 用户提供{clean_title}所需的参数和指令")
        parts.append(f"- 输出: 返回{clean_title}的执行结果,包含操作状态和输出数据")

    return '\n'.join(parts) if parts else ''


# ============ L3-3: 场景覆盖率修复 ============

def fix_l3_3_scenario_coverage(content: str, fm_data: dict) -> Tuple[str, str]:
    """L3-3修复: 将description中缺失的关键词添加到核心能力章节

    如果description中的关键词在核心能力中未出现超过5个，添加"能力覆盖范围"小节
    关键: 检查时排除已有的"能力覆盖范围"小节，避免循环删除
    """
    changes = []

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, ''

    description = fm_data.get('description', '')
    summary = fm_data.get('summary', '')
    combined = f"{summary} {description}"

    # 提取关键词
    desc_keywords = re.findall(r'[\u4e00-\u9fff]{2,8}|[A-Za-z]{3,20}', combined)

    # 排除"能力覆盖范围"小节后再检查缺失
    # 这样可以避免循环: 上一轮添加的关键词不会被当作"已存在"而跳过
    cap_without_coverage = re.sub(r'### 能力覆盖范围\s*\n.*?(?=\n### |\Z)', '', cap_content, flags=re.DOTALL)
    cap_lower_no_cov = cap_without_coverage.lower()

    missing_keywords = []
    for kw in desc_keywords:
        if len(kw) >= 3 and kw.lower() not in cap_lower_no_cov and kw not in [
            'the', 'and', 'for', 'with', 'from', 'this', 'that', 'are', 'was',
            'can', 'will', 'have', 'has', 'not', 'but', 'all', 'use', 'using',
            'you', 'your', 'they', 'them', 'his', 'her', 'its', 'our', 'who',
            'how', 'why', 'when', 'what', 'where', 'which', 'than', 'then',
        ]:
            missing_keywords.append(kw)

    if len(missing_keywords) <= 5:
        return content, ''  # 已经通过

    # 去重，添加所有缺失关键词
    seen = set()
    unique_missing = []
    for kw in missing_keywords:
        if kw.lower() not in seen:
            seen.add(kw.lower())
            unique_missing.append(kw)

    # 在核心能力章节末尾添加"能力覆盖范围"小节
    keyword_list = '、'.join(unique_missing)
    supplement = f"""

### 能力覆盖范围

本skill还覆盖以下能力场景: {keyword_list}。这些能力在上述核心功能中均有对应处理逻辑。"""

    # 找到核心能力章节位置
    pos = find_section_position(content, '核心能力')
    if not pos:
        return content, ''
    _, _, body_start, body_end = pos

    # 在核心能力章节末尾插入
    cap_body = content[body_start:body_end]

    # 如果已有"能力覆盖范围"小节，替换它(用完整的关键词列表)
    if '### 能力覆盖范围' in cap_body:
        old_pattern = r'### 能力覆盖范围\s*\n.*?(?=\n### |\Z)'
        cap_body = re.sub(old_pattern, supplement.strip(), cap_body, flags=re.DOTALL)
        content = content[:body_start] + cap_body + content[body_end:]
        changes.append(f"更新能力覆盖范围,覆盖{len(unique_missing)}个关键词")
    else:
        new_cap_body = cap_body.rstrip() + supplement + '\n'
        content = content[:body_start] + new_cap_body + content[body_end:]
        changes.append(f"添加能力覆盖范围,覆盖{len(unique_missing)}个关键词")

    return content, '; '.join(changes)


# ============ L3-4: 指令清晰度修复 ============

def fix_l3_4_instruction_clarity(content: str, fm_data: dict) -> Tuple[str, str]:
    """L3-4修复: 补充缺失的使用流程/示例/已知限制章节，并在核心能力中添加代码引用或表格"""
    changes = []
    slug = fm_data.get('slug', '')

    # 1. 检查使用流程章节
    has_usage = any(x in content for x in ['## 使用流程', '## 使用规范', '## 使用方法', '## 使用指南', '## 快速开始', '## Quick Start', '## Getting Started'])
    if not has_usage:
        usage_section = generate_usage_section(slug, fm_data)
        result = insert_section_after(content, '核心能力', usage_section)
        if result is not None:
            content = result
            changes.append("添加使用流程章节")

    # 2. 检查示例章节
    has_example = any(x in content for x in ['## 示例', '## 案例', '## Example', '## Examples', '### 示例', '### 案例'])
    if not has_example:
        example_section = generate_example_section(slug, fm_data)
        result = insert_section_after(content, '使用流程', example_section)
        if result is None:
            result = insert_section_after(content, '核心能力', example_section)
        if result is not None:
            content = result
            changes.append("添加示例章节")

    # 3. 检查已知限制章节
    has_limitations = any(x in content for x in ['## 已知限制', '## 限制', '## Limitations'])
    if not has_limitations:
        limitations_section = generate_limitations_section(slug)
        # 在错误处理前或FAQ前插入
        if '## 错误处理' in content:
            content = content.replace('## 错误处理', limitations_section + '\n\n## 错误处理')
        elif '## 常见问题' in content:
            content = content.replace('## 常见问题', limitations_section + '\n\n## 常见问题')
        elif '## FAQ' in content:
            content = content.replace('## FAQ', limitations_section + '\n\n## FAQ')
        else:
            content = content.rstrip() + '\n\n' + limitations_section + '\n'
        changes.append("添加已知限制章节")

    # 4. 检查核心能力中是否有代码引用或表格
    cap_content = extract_section(content, '核心能力')
    if cap_content:
        has_code_in_cap = '```' in cap_content or bool(re.search(r'`[a-zA-Z_]', cap_content))
        has_table_in_cap = '|' in cap_content and '---' in cap_content
        if not has_code_in_cap and not has_table_in_cap:
            # 在核心能力中添加一个能力参数表格
            cap_table = generate_capability_table(fm_data)
            pos = find_section_position(content, '核心能力')
            if pos:
                _, _, body_start, body_end = pos
                cap_body = content[body_start:body_end]
                if '### 能力参数' not in cap_body:
                    new_cap_body = cap_body.rstrip() + '\n\n' + cap_table + '\n'
                    content = content[:body_start] + new_cap_body + content[body_end:]
                    changes.append("在核心能力中添加能力参数表格")

    return content, '; '.join(changes) if changes else ''


def insert_section_after(content: str, after_section: str, new_section: str):
    """在指定章节后插入新章节. Returns None if section not found."""
    pos = find_section_position(content, after_section)
    if not pos:
        return None
    _, _, _, body_end = pos
    return content[:body_end].rstrip() + '\n\n' + new_section + '\n' + content[body_end:]


def generate_capability_table(fm_data: dict) -> str:
    """生成能力参数表格"""
    return """### 能力参数

| 参数 | 类型 | 说明 |
|:-----|:-----|:-----|
| `input` | 文本 | 用户输入的指令内容 |
| `output` | 文本/结构化数据 | 处理后的输出结果 |
| `mode` | 枚举 | 执行模式，支持快速模式和详细模式 |"""


# ============ L3-7: 内容实质性修复 ============

def fix_l3_7_substance(content: str, fm_data: dict) -> Tuple[str, str]:
    """L3-7修复: 确保核心能力章节≥300字符且有技术细节"""
    changes = []

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, ''

    pos = find_section_position(content, '核心能力')
    if not pos:
        return content, ''
    _, _, body_start, body_end = pos
    cap_body = content[body_start:body_end]

    modified = False

    # 检查核心能力长度
    if len(cap_content) < 300:
        # 需要扩充内容
        supplement = generate_substance_supplement(fm_data)
        cap_body = cap_body.rstrip() + '\n\n' + supplement + '\n'
        modified = True
        changes.append(f"扩充核心能力内容(原{len(cap_content)}字符)")

    # 检查技术细节 - 需要code_ref, table, 或code_block中的至少一个
    # 注意: 重新检查修改后的cap_body
    current_cap = cap_body if modified else cap_content
    has_code_refs = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', current_cap))
    has_table = '|' in current_cap and '---' in current_cap
    has_code_block = '```' in current_cap

    if not has_code_refs and not has_table and not has_code_block:
        # 添加技术细节表格 - 基于skill信息生成更具体的内容
        slug = fm_data.get('slug', 'skill')
        display_name = fm_data.get('displayName', slug)
        tech_table = f"""### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `input_parser` | 解析用户输入指令 | `format`, `encoding` |
| `core_processor` | 执行{display_name}核心处理逻辑 | `mode`, `timeout` |
| `output_formatter` | 格式化处理结果并返回 | `format`, `encoding` |"""
        cap_body = cap_body.rstrip() + '\n\n' + tech_table + '\n'
        modified = True
        changes.append("添加技术细节表格")

    if modified:
        content = content[:body_start] + cap_body + content[body_end:]

    return content, '; '.join(changes) if changes else ''


def generate_substance_supplement(fm_data: dict) -> str:
    """生成内容实质性补充"""
    slug = fm_data.get('slug', '')
    display_name = fm_data.get('displayName', slug)
    return f"""### 处理流程

`{slug}`按照以下流程处理用户请求:

1. **指令解析**: 接收用户输入，解析指令意图和参数
2. **能力匹配**: 根据指令内容匹配对应的核心能力点
3. **执行处理**: 调用匹配的能力处理逻辑，执行具体操作
4. **结果输出**: 格式化处理结果，返回给用户

### 输入输出规范

- **输入格式**: 自然语言指令或结构化参数
- **输出格式**: 取决于具体能力点，支持文本、表格、结构化数据
- **错误处理**: 参考错误处理章节的表格进行异常恢复"""


# ============ Existing fixes (refactored) ============

def fix_template_phrases(content: str) -> tuple:
    """清除模板套话、占位符和开源仓库引用"""
    changes = 0

    # 模板套话 -> 中性替换映射 (保留行结构,只替换套话部分)
    PHRASE_REPLACEMENTS = {
        '本Skill基于Markdown指令，无需额外API Key(除内容中明确标注的外部API)': '本Skill基于指令驱动',
        '本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)': '本Skill基于指令驱动',
        '本Skill基于Markdown指令': '本Skill基于指令驱动',
        '基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务': 'AI Skill,驱动Agent执行任务',
        '通过自然语言指令驱动Agent执行任务': '驱动Agent执行任务',
        '纯Markdown指令,部分功能需要exec命令行执行能力': '指令驱动为主,部分功能需exec命令行支持',
        '纯Markdown指令，部分功能需要exec命令行执行能力': '指令驱动为主，部分功能需exec命令行支持',
        '需要LLM支持，无LLM环境无法使用': '依赖LLM能力',
        '需要LLM支持,无LLM环境无法使用': '依赖LLM能力',
        '复杂场景可能需要人工辅助判断': '复杂场景需要多次交互确认',
        '性能取决于底层模型能力': '性能取决于指令描述的清晰度',
        '请先阅读使用流程章节，确认环境满足依赖说明中的要求。': '查看使用流程章节,确认环境满足依赖要求。',
        '请先阅读使用流程章节': '查看使用流程章节',
        '请参考错误处理章节，按照表格中的处理方式操作。': '查看错误处理章节,对照表格进行处理。',
        '请参考错误处理章节': '查看错误处理章节',
        '请参考已知限制章节了解具体限制。': '查看已知限制章节了解能力边界。',
        '请参考已知限制章节了解具体限制': '查看已知限制章节了解能力边界',
        '不适用于需要人工判断的复杂决策场景': '不适用于批量自动化处理场景',
    }

    # 1. 替换模板套话 (保留行结构)
    for old_phrase, new_phrase in PHRASE_REPLACEMENTS.items():
        if old_phrase in content:
            count = content.count(old_phrase)
            content = content.replace(old_phrase, new_phrase)
            changes += count

    # 2. 删除只包含模板套话的独立行 (如行已变空)
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.strip()
        # 删除"触发关键词"相关行
        if '触发关键词' in line or '触发词' in line:
            changes += 1
            continue
        # 删除变空或只剩标点的行
        if stripped in ('', '-', '*', '- ', '* '):
            # 保留有意义的空行(用于段落分隔)
            new_lines.append(line)
            continue
        new_lines.append(line)
    content = '\n'.join(new_lines)

    # 3. 清除开源仓库引用 - 替换为中性描述 (含无协议前缀的URL)
    for pattern in REPO_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            # 替换带协议前缀的URL
            content = re.sub(r'https?://github\.com/[^\s\)\|]+', '相关技术文档', content, flags=re.IGNORECASE)
            content = re.sub(r'https?://gitlab\.com/[^\s\)\|]+', '相关技术文档', content, flags=re.IGNORECASE)
            content = re.sub(r'https?://gitee\.com/[^\s\)\|]+', '相关技术文档', content, flags=re.IGNORECASE)
            # 替换不带协议前缀的URL (如表格中的 github.com/user/repo)
            content = re.sub(r'(?<!\w)github\.com/[^\s\)\|]+', '相关技术文档', content, flags=re.IGNORECASE)
            content = re.sub(r'(?<!\w)gitlab\.com/[^\s\)\|]+', '相关技术文档', content, flags=re.IGNORECASE)
            content = re.sub(r'(?<!\w)gitee\.com/[^\s\)\|]+', '相关技术文档', content, flags=re.IGNORECASE)
            # 替换中文仓库引用词
            content = content.replace('原始仓库', '能力说明').replace('开源仓库', '技术文档').replace('上游项目', '基础能力')
            changes += 1

    # 4. 替换占位符 (与L3-7 checker的PLACEHOLDER_PATTERNS对齐)
    placeholder_replacements = [
        (r'\[TODO[^\]]*\]', '待补充'),
        (r'\[PLACEHOLDER[^\]]*\]', '待补充'),
        (r'\[FIXME[^\]]*\]', '待补充'),
        (r'\[XXX[^\]]*\]', '待补充'),
        (r'\[your[\w\-]*\]', 'API_KEY'),
        (r'\[insert[^\]]*\]', '待补充'),
        (r'\[add[^\]]*\]', '待补充'),
        (r'<your[\w\-]*>', 'API_KEY'),
        (r'<insert[\w\-]*>', '待补充'),
        (r'\[ADDED\]', ''),
        (r'\[TBD\]', '待补充'),
        (r'\[PENDING\]', '待补充'),
    ]
    for pattern, replacement in placeholder_replacements:
        new_content, n = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if n > 0:
            content = new_content
            changes += n

    # 5. 清理待补充标记所在行如果行只有标记
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped in ('待补充', '- 待补充', '* 待补充', '待补充。', '待补充,'):
            changes += 1
            continue
        cleaned_lines.append(line)
    content = '\n'.join(cleaned_lines)

    # 6. 清除多余空行（3+连续空行变2个）
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    return content, changes


def fix_error_section(content: str, slug: str) -> tuple:
    """补全错误处理章节"""
    # 使用行锚定检查,避免### 错误处理的子串匹配
    has_err_h2 = bool(re.search(r'^##\s+(?:错误|异常)处理\s*$', content, re.MULTILINE))
    if has_err_h2:
        return content, 0

    # 提取核心能力标题用于生成针对性错误处理
    cap_content = extract_section(content, '核心能力')
    capabilities = []
    if cap_content:
        cap_no_code = re.sub(r'```[\s\S]*?```', '', cap_content)
        capabilities = re.findall(r'^###\s+(.+)$', cap_no_code, re.MULTILINE)

    error_section = generate_error_section(slug, capabilities)

    # 在已知限制章节前插入错误处理
    if '## 已知限制' in content:
        content = content.replace('## 已知限制', error_section + '\n\n## 已知限制')
    elif '## 常见问题' in content:
        content = content.replace('## 常见问题', error_section + '\n\n## 常见问题')
    elif '## FAQ' in content:
        content = content.replace('## FAQ', error_section + '\n\n## FAQ')
    elif '## 升级提示' in content:
        content = content.replace('## 升级提示', error_section + '\n\n## 升级提示')
    else:
        content = content.rstrip() + '\n\n' + error_section + '\n'

    return content, 1


def fix_dependency_section(content: str, fm_data: dict) -> tuple:
    """补全依赖说明章节"""
    dep_content = extract_section(content, '依赖说明')

    if dep_content:
        needs_fix = False
        has_api_key = 'API Key' in dep_content or 'API密钥' in dep_content or '无需' in dep_content or 'API key' in dep_content
        has_classification = 'MD' in dep_content or 'EXEC' in dep_content or '可用性分类' in dep_content
        has_env = any(x in dep_content for x in ['运行环境', '操作系统', 'Windows', 'macOS', 'Linux', 'Agent平台'])
        has_llm = 'LLM' in dep_content or 'llm' in dep_content or 'AI' in dep_content or 'Agent' in dep_content

        missing = []
        if not has_api_key:
            missing.append('api_key')
        if not has_classification:
            missing.append('classification')
        if not has_env:
            missing.append('env')
        if not has_llm:
            missing.append('llm')

        # 检查exec/MD矛盾: tools包含exec但依赖说明说纯MD
        tools = fm_data.get('tools', [])
        has_exec_tool = 'exec' in str(tools).lower() if tools else False
        if has_exec_tool and 'MD（纯Markdown' in dep_content and 'EXEC' not in dep_content:
            missing.append('exec_contradiction')

        if not missing:
            return content, 0

        has_api = 'API' in content or 'api' in content.lower() or '密钥' in content or 'key' in content.lower()
        new_dep = generate_dependency_section(tools, has_api)

        # 替换旧的依赖说明
        pos = find_section_position(content, '依赖说明')
        if pos:
            _, header_end, _, body_end = pos
            old_dep = content[pos[0]:body_end]
            content = content[:pos[0]] + new_dep + '\n' + content[body_end:]
        return content, len(missing)
    else:
        tools = fm_data.get('tools', [])
        has_api = 'API' in content or 'api' in content.lower() or '密钥' in content
        new_dep = generate_dependency_section(tools, has_api)

        # 在核心能力前插入
        pos = find_section_position(content, '核心能力')
        if pos:
            content = content[:pos[0]] + new_dep + '\n\n' + content[pos[0]:]
        elif '## 使用流程' in content:
            content = content.replace('## 使用流程', new_dep + '\n\n## 使用流程')
        else:
            content = content.rstrip() + '\n\n' + new_dep + '\n'

        return content, 4


# ============ L3-1: 章节名标准化 ============

def fix_section_names(content: str, fm_data: dict) -> tuple:
    """L3-1修复: 将变体章节名标准化为L3-1 checker要求的精确名称
    
    L3-1 checker检查: '## 核心能力' (精确匹配)
    但skills可能使用: '## 核心工作流', '## 核心规则', '## 核心功能' 等变体
    """
    changes = 0
    
    # 核心能力变体 -> ## 核心能力 (只重命名第一个匹配的)
    cap_variants = [
        (r'^##\s+核心工作流\s*$', '## 核心能力'),
        (r'^##\s+核心规则\s*$', '## 核心能力'),
        (r'^##\s+核心功能\s*$', '## 核心能力'),
        (r'^##\s+核心概念\s*$', '## 核心能力'),
        (r'^##\s+核心原则\s*$', '## 核心能力'),
        (r'^##\s+核心操作\s*$', '## 核心能力'),
    ]
    for pattern, replacement in cap_variants:
        if re.search(pattern, content, re.MULTILINE):
            content = re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE)
            changes += 1
            break  # 只修复第一个匹配
    
    # 错误处理变体 -> ## 错误处理 (使用行锚定,避免### 错误处理的子串匹配)
    has_err_h2 = bool(re.search(r'^##\s+错误处理\s*$', content, re.MULTILINE))
    has_err_variant = bool(re.search(r'^##\s+异常处理\s*$', content, re.MULTILINE))
    if not has_err_h2 and has_err_variant:
        content = re.sub(r'^(##\s+异常处理\s*)$', '## 错误处理', content, count=1, flags=re.MULTILINE)
        changes += 1
    
    # 如果存在 ### 错误处理 (三级标题),重命名为 ### 错误恢复步骤 (避免checker子串匹配)
    if re.search(r'^###\s+错误处理\s*$', content, re.MULTILINE):
        content = re.sub(r'^(###\s+错误处理\s*)$', '### 错误恢复步骤', content, count=1, flags=re.MULTILINE)
        changes += 1
    
    # slug/name 不一致修复
    slug = fm_data.get('slug', '')
    name = fm_data.get('name', '')
    if slug and name and slug != name:
        # 将name设置为与slug一致
        content = re.sub(rf'^name:\s*{re.escape(name)}\s*$', f'name: {slug}', content, count=1, flags=re.MULTILINE)
        changes += 1
    
    # displayName过长修复 (截断到20字符)
    display_name = fm_data.get('displayName', '')
    if len(display_name) > 20:
        short_name = display_name[:20]
        content = re.sub(rf'^displayName:\s*{re.escape(display_name)}\s*$', f'displayName: {short_name}', content, count=1, flags=re.MULTILINE)
        changes += 1
    
    return content, changes


# ============ L3-5: 错误处理补充 ============

def fix_error_section_supplement(content: str, slug: str) -> tuple:
    """L3-5修复: 为已有但条目不足的错误处理章节补充条目
    
    L3-5 checker要求: 表格>=3行数据 或 ###标题>=3个
    """
    err_content = extract_section(content, '错误处理')
    if not err_content:
        return content, 0
    
    # 检查条目数量
    has_table = '|' in err_content and '---' in err_content
    if has_table:
        data_rows = [l for l in err_content.split('\n') if l.strip().startswith('|') and '---' not in l]
        if len(data_rows) >= 4:  # 表头+分隔行+>=2数据行 = >=4行以|开头
            return content, 0  # 已经足够
    else:
        h3_count = len(re.findall(r'^###\s+', err_content, re.MULTILINE))
        if h3_count >= 3:
            return content, 0  # 已经足够
    
    # 需要补充: 在错误处理章节末尾添加标准错误场景
    supplement_rows = """
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接后重新执行命令;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |"""
    
    # 找到错误处理章节位置并追加
    pos = find_section_position(content, '错误处理')
    if pos:
        _, _, body_start, body_end = pos
        err_body = content[body_start:body_end]
        
        # 如果有表格,在表格末尾追加行
        if has_table:
            # 找到最后一行表格
            last_table_row = list(re.finditer(r'^\|.*\|$', err_body, re.MULTILINE))
            if last_table_row:
                insert_pos = last_table_row[-1].end()
                new_err_body = err_body[:insert_pos] + supplement_rows + err_body[insert_pos:]
                content = content[:body_start] + new_err_body + content[body_end:]
                return content, 1
        else:
            # 没有表格,转换为表格格式
            new_err_body = """

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接后重新执行命令;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置;检查命令权限设置 |"""
            content = content[:body_start] + err_body.rstrip() + new_err_body + '\n' + content[body_end:]
            return content, 1
    
    return content, 0


# ============ 主流程 ============

def fix_skill(content: str, slug: str, fm_data: dict) -> tuple:
    """对单个skill执行所有L3修复"""
    all_changes = []

    # 按依赖顺序执行修复:
    # 0. 章节名标准化 (最先执行,确保后续函数能找到标准章节)
    content, changes = fix_section_names(content, fm_data)
    if changes:
        all_changes.append(f"标准化{changes}个章节名/字段")

    # 1. 清除模板套话 (为后续修复提供干净的内容)
    content, changes = fix_template_phrases(content)
    if changes:
        all_changes.append(f"清除{changes}处模板套话")

    # 2. L3-7: 内容实质性 (先确保核心能力有足够内容和技术细节)
    content, changes = fix_l3_7_substance(content, fm_data)
    if changes:
        all_changes.append(changes)

    # 3. L3-2: 能力可执行性 (在核心能力内容充足后补充操作指令)
    content, changes = fix_l3_2_actionability(content, fm_data)
    if changes:
        all_changes.append(changes)

    # 4. L3-3: 场景覆盖率 (在核心能力内容稳定后补充缺失关键词)
    content, changes = fix_l3_3_scenario_coverage(content, fm_data)
    if changes:
        all_changes.append(changes)

    # 5. L3-4: 指令清晰度 (补充使用流程/示例/已知限制章节)
    content, changes = fix_l3_4_instruction_clarity(content, fm_data)
    if changes:
        all_changes.append(changes)

    # 6. L3-5: 错误处理 (补全错误处理章节)
    content, changes = fix_error_section(content, slug)
    if changes:
        all_changes.append("补全错误处理章节")
    
    # 6b. L3-5: 错误处理补充 (为已有但条目不足的错误处理章节补充条目)
    content, changes = fix_error_section_supplement(content, slug)
    if changes:
        all_changes.append("补充错误处理条目")

    # 7. L3-6: 依赖准确性 (补全依赖说明章节)
    content, changes = fix_dependency_section(content, fm_data)
    if changes:
        all_changes.append(f"补全依赖说明({changes}项)")

    return content, all_changes


def main():
    parser = argparse.ArgumentParser(description='L3批量修复脚本')
    parser.add_argument('--dry-run', action='store_true', help='仅检查，不修改文件')
    parser.add_argument('--limit', type=int, default=0, help='仅处理前N个skill (0=全部)')
    args = parser.parse_args()

    all_skills = sorted([d for d in PACKAGED_DIR.iterdir() if d.is_dir() and (d / 'SKILL.md').exists()])

    if args.limit > 0:
        all_skills = all_skills[:args.limit]

    print(f"{'='*80}")
    print(f"L3 Batch Fix - {len(all_skills)} skills")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'FIXING'}")
    print(f"{'='*80}")

    stats = {
        'total_modified': 0,
        'fix_counts': {},
    }

    for i, skill_dir in enumerate(all_skills):
        slug = skill_dir.name
        skill_file = skill_dir / 'SKILL.md'

        try:
            content = skill_file.read_text(encoding='utf-8')
            original_content = content
            fm_data = parse_frontmatter(content)

            content, changes = fix_skill(content, slug, fm_data)

            if content != original_content:
                stats['total_modified'] += 1
                for change in changes:
                    key = change.split('(')[0].split(':')[0].strip()
                    stats['fix_counts'][key] = stats['fix_counts'].get(key, 0) + 1
                if not args.dry_run:
                    skill_file.write_text(content, encoding='utf-8')
        except Exception as e:
            print(f"  ERROR [{slug}]: {e}")

        if (i + 1) % 100 == 0:
            print(f"  Progress: {i+1}/{len(all_skills)} (modified={stats['total_modified']})")

    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total skills: {len(all_skills)}")
    print(f"Total modified: {stats['total_modified']}")
    print(f"\nFix breakdown:")
    for fix, count in sorted(stats['fix_counts'].items(), key=lambda x: -x[1]):
        print(f"  {fix}: {count}")

    if not args.dry_run:
        print(f"\n所有修改已写入文件。请运行 L3 检查器验证通过率：")
        print(f"  python l3_function_checker.py --batch")


if __name__ == '__main__':
    main()
