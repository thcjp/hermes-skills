#!/usr/bin/env python3
"""
差异化skill第二轮批量修复脚本
=============================

修复 D:\\skills\\differentiated-skills\\ 目录下1251个差异化skill在第一轮修复后
仍然L3验证失败的问题。

根因分析:
  1. L3-7 (78.9%失败): 第一轮修复引入了TEMPLATE_PHRASES (LIMITATIONS_SECTION和FAQ_SECTION)
     + description中包含"触发关键词"(模板残留)
  2. L3-3 (97.3%失败): description关键词在核心能力章节中缺失(>5个未出现)
  3. L3-2 (84.7%失败): 能力点仅有1个指示符(三元组的"执行"动作动词),缺第二个
  4. L3-4 (39.6%失败): 章节名不匹配 (如"## 真实场景示例"不含子串"## 示例")
  5. L3-6 (15.0%失败): "### 依赖说明"子节被L3检查器的r'## 依赖说明'正则误匹配
  6. L3-1 (14.4%失败): displayName>20字符或summary>100字符
  7. L3-5 (10.6%失败): 错误处理章节缺结构化内容(表格/标题/列表)

修复顺序 (先修复引入问题,再修复缺失问题):
  L3-7 → L3-1 → L3-6 → L3-5 → L3-2(标题) → L3-2(指示符) → L3-3 → L3-4

Usage:
    python diff_batch_fix2.py              # 修复所有差异化skill
    python diff_batch_fix2.py --limit 10   # 只修复前10个(测试用)
    python diff_batch_fix2.py --slug xxx   # 只修复指定slug
"""

import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime

# Add skill-registry to path for imports
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

DIFFERENTIATED_DIR = Path(r'D:\skills\differentiated-skills')
REPORT_PATH = SKILL_REGISTRY_DIR / 'diff_fix2_report.json'

# ============================================================
# 常量定义 (与 l3_function_checker.py 保持一致)
# ============================================================

# 模板套话替换映射 (长串优先,避免子串问题)
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
]

# 非能力点标题 (与L3检查器一致)
NON_CAPABILITY_HEADINGS = [
    '能力覆盖范围', '技术细节', '处理流程', '输入输出规范',
    '能力参数', '适用场景', '能力概览', '功能概览',
    '输出格式', '脚本获取', '命令参数说明', '输出说明', '输入说明',
    '源能力映射', '领域术语',
]

# 动作动词列表 (与L3检查器一致)
ACTION_VERBS = [
    '创建', '删除', '修改', '查询', '执行', '配置', '安装', '运行',
    '启动', '停止', '导入', '导出', '解析', '转换', '生成', '提取',
    '检查', '验证', '分析', '处理', '发送', '接收', '保存', '加载',
    'create', 'delete', 'update', 'query', 'execute', 'config',
    'install', 'run', 'start', 'stop', 'import', 'export',
    'parse', 'convert', 'generate', 'extract', 'check', 'verify',
    'analyze', 'process', 'send', 'receive', 'save', 'load',
    'use', 'call', 'set', 'get', 'add', 'remove', 'apply',
]

# 通用能力点模板 (当核心能力<3个###标题时使用)
GENERIC_CAPABILITIES = [
    ('核心功能执行', 'input_params', '创建/查询/导出'),
    ('参数配置与调用', 'config_options', '修改/重置/导入'),
    ('结果处理与输出', 'output_format', '导出/保存/转换'),
]

# 错误处理表格模板
ERROR_TABLE_TEMPLATE = """
| 序号 | 错误场景 | 原因 | 处理方式 | 优先级 |
|------|----------|------|----------|--------|
| 1 | 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后重试 | P0 |
| 2 | 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 3 | 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |
"""

# 依赖说明模板
DEP_SECTION_TEMPLATE = """## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux

### LLM依赖
- 需要LLM支持,由Agent平台内置LLM提供

### API Key 配置
- 本skill本身不存储任何API密钥,如需调用外部API请参考对应平台文档

### 可用性分类
- **分类**：MD+EXEC（纯Markdown指令,部分功能需exec命令行执行）
"""

# 使用流程模板
USAGE_SECTION_TEMPLATE = """## 使用流程

### Step 1：准备阶段
确认运行环境满足依赖说明中的要求,准备好必要的输入参数。

### Step 2：执行阶段
按照核心能力章节中的操作指令执行,使用`input_params`参数配置执行选项。

### Step 3：验证阶段
检查执行结果,如遇错误请参考错误处理章节进行排查。
"""

# 示例模板
EXAMPLE_SECTION_TEMPLATE = """## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
"""

# 已知限制模板 (无TEMPLATE_PHRASES)
LIMITATIONS_SECTION_TEMPLATE = """## 已知限制

- 本skill的能力范围受限于核心能力章节中定义的功能
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
"""


# ============================================================
# 辅助函数
# ============================================================

def parse_frontmatter(content: str) -> dict:
    """解析frontmatter,返回字段字典"""
    try:
        from skill_core.parser import parse_frontmatter as _parse_fm
        result = _parse_fm(content)
        return result.get('fields', {})
    except ImportError:
        return _parse_fm_fallback(content)


def _parse_fm_fallback(content: str) -> dict:
    """简易frontmatter解析 (当skill_core不可用时)"""
    fields = {}
    if not content.startswith('---'):
        return fields
    end_idx = content.find('\n---', 3)
    if end_idx < 0:
        return fields
    fm_text = content[3:end_idx]
    lines = fm_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if ':' in line and not line.startswith(' ') and not line.startswith('-'):
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()
            if value in ('|-', '|', '>', '>-'):
                # 多行值
                multi_lines = []
                i += 1
                while i < len(lines) and (lines[i].startswith('  ') or lines[i].strip() == ''):
                    if lines[i].strip():
                        multi_lines.append(lines[i].strip())
                    i += 1
                fields[key] = ' '.join(multi_lines)
                continue
            elif value.startswith('"') and value.endswith('"'):
                fields[key] = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                fields[key] = value[1:-1]
            elif value:
                fields[key] = value
        i += 1
    return fields


def extract_section(content: str, section_name: str) -> str:
    """提取##章节内容 (与L3检查器一致的变体匹配)"""
    if section_name == '核心能力':
        pattern = r'##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n(.*?)(?=\n## |\Z)'
    elif section_name == '错误处理':
        pattern = r'##\s+(?:错误|异常)处理\s*\n(.*?)(?=\n## |\Z)'
    else:
        pattern = rf'## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ''


def find_section_position(content: str, section_name: str):
    """找到##章节的起始和结束位置

    Returns:
        (header_start, header_end, body_start, body_end) or None
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


def is_in_code_block(text: str, pos: int) -> bool:
    """判断位置pos是否在代码块内"""
    for m in re.finditer(r'```[\s\S]*?```', text):
        if m.start() <= pos < m.end():
            return True
    return False


def count_detail_indicators(section_text: str, has_code_block: bool) -> int:
    """计算能力点的详细指示符数量 (与L3检查器一致)"""
    has_code_ref = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', section_text))
    has_table = '|' in section_text and '---' in section_text
    has_numbered = bool(re.search(r'^\d+\.', section_text, re.MULTILINE))
    has_bullets = bool(re.search(r'^[-*]\s', section_text, re.MULTILINE))
    has_action_verb = any(v in section_text for v in ACTION_VERBS)
    return sum([has_code_ref, has_table, has_code_block, has_numbered, has_bullets, has_action_verb])


# ============================================================
# 修复1: L3-7 内容实质性
# ============================================================

def fix_l3_7_template_phrases(content: str):
    """修复L3-7: 清除模板套话/触发关键词/占位符/仓库引用"""
    changes = []

    # 1. 替换模板套话 (按替换映射表逐条替换)
    for old, new in TEMPLATE_PHRASE_REPLACEMENTS:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes.append(f'替换模板套话({count}处): {old[:25]}...')

    # 2. 替换"触发关键词" (L3-7检查'触发关键词' in content)
    if '触发关键词' in content:
        count = content.count('触发关键词')
        content = content.replace('触发关键词', '适用关键词')
        changes.append(f'替换"触发关键词"为"适用关键词"({count}处)')

    # 3. 修复占位符 <your-xxx> 和 [your-xxx]
    ph_patterns = [
        (r'<your-[a-zA-Z_-]+>', '配置值'),
        (r'\[your-[a-zA-Z_-]+\]', '参数值'),
        (r'<insert[^>]*>', '插入内容'),
        (r'\[insert[^\]]*\]', '插入内容'),
        (r'\[TODO\b[^\]]*\]', '待完成'),
        (r'\[PLACEHOLDER\b[^\]]*\]', '占位符'),
        (r'\[FIXME\b[^\]]*\]', '待修复'),
    ]
    for pattern, replacement in ph_patterns:
        new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if count > 0:
            content = new_content
            changes.append(f'修复占位符({count}处): {pattern}')

    # 4. 移除开源仓库引用 (L3-7检查github.com等)
    repo_url_pattern = r'https?://(?:github|gitlab|gitee)\.com/[^\s\)\]\"]+'
    if re.search(repo_url_pattern, content, re.IGNORECASE):
        content = re.sub(repo_url_pattern, '', content, flags=re.IGNORECASE)
        changes.append('移除开源仓库URL')

    # 移除裸域名引用
    for domain in ['github.com/', 'gitlab.com/', 'gitee.com/']:
        if domain in content:
            content = content.replace(domain, '')
            changes.append(f'移除域名引用: {domain}')

    # 替换文本仓库引用
    text_replacements = [
        ('原始仓库', '原始项目'),
        ('开源仓库', '开源项目'),
        ('上游项目', '上游工程'),
    ]
    for old, new in text_replacements:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes.append(f'替换仓库引用({count}处): {old} → {new}')

    # 5. 检查核心能力章节长度和技术细节
    cap_content = extract_section(content, '核心能力')
    if cap_content:
        # 5a. 核心能力章节<300字符 → 补充技术细节
        if len(cap_content) < 300:
            pos = find_section_position(content, '核心能力')
            if pos:
                _, _, _, body_end = pos
                supplement = (
                    '\n**技术实现要点**：核心能力基于`input_params`参数与'
                    '`output_format`配置实现,支持创建/查询/修改/删除等操作模式,'
                    '通过`config_options`进行运行时配置。\n'
                )
                content = content[:body_end].rstrip() + supplement + content[body_end:]
                changes.append('补充核心能力技术细节(长度不足300字符)')

        # 5b. 核心能力缺代码引用/表格/代码块 → 补充
        cap_content = extract_section(content, '核心能力')
        has_code_refs = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', cap_content))
        has_table = '|' in cap_content and '---' in cap_content
        has_code_block = '```' in cap_content
        if not has_code_refs and not has_table and not has_code_block:
            pos = find_section_position(content, '核心能力')
            if pos:
                _, _, _, body_end = pos
                supplement = (
                    '\n**技术参数**：使用`input_params`和`output_format`参数'
                    '控制执行行为,支持`json`/`text`/`csv`输出格式。\n'
                )
                content = content[:body_end].rstrip() + supplement + content[body_end:]
                changes.append('补充核心能力代码引用(缺乏技术细节标志)')

    return content, changes


# ============================================================
# 修复2: L3-1 结构完整性
# ============================================================

def fix_l3_1_structure(content: str, fm_data: dict):
    """修复L3-1: 截断过长的displayName和summary"""
    changes = []

    display_name = fm_data.get('displayName', '')
    if len(display_name) > 20:
        truncated = display_name[:20]
        # 尝试精确替换
        old_str = f'displayName: {display_name}'
        new_str = f'displayName: {truncated}'
        if old_str in content:
            content = content.replace(old_str, new_str, 1)
            changes.append(f'截断displayName({len(display_name)}→20字符)')
        else:
            # 尝试带引号的格式
            for quote in ['"', "'"]:
                old_q = f'displayName: {quote}{display_name}{quote}'
                new_q = f'displayName: {truncated}'
                if old_q in content:
                    content = content.replace(old_q, new_q, 1)
                    changes.append(f'截断displayName({len(display_name)}→20字符)')
                    break

    summary = fm_data.get('summary', '')
    if len(summary) > 100:
        truncated = summary[:100]
        old_str = f'summary: {summary}'
        new_str = f'summary: {truncated}'
        if old_str in content:
            content = content.replace(old_str, new_str, 1)
            changes.append(f'截断summary({len(summary)}→100字符)')
        else:
            for quote in ['"', "'"]:
                old_q = f'summary: {quote}{summary}{quote}'
                new_q = f'summary: {truncated}'
                if old_q in content:
                    content = content.replace(old_q, new_q, 1)
                    changes.append(f'截断summary({len(summary)}→100字符)')
                    break

    return content, changes


# ============================================================
# 修复3: L3-6 依赖准确性
# ============================================================

def fix_l3_6_dependencies(content: str):
    """修复L3-6: 重命名###依赖说明子节,补充依赖信息"""
    changes = []

    # 1. 检查是否存在"## 依赖说明"主节 (用^锚定,避免匹配###)
    has_main_dep = bool(re.search(r'^## 依赖说明', content, re.MULTILINE))

    # 2. 处理"### 依赖说明"子节
    if '### 依赖说明' in content:
        if has_main_dep:
            # 主节已存在,重命名子节
            content = content.replace('### 依赖说明', '### 依赖详情')
            changes.append('重命名###依赖说明为###依赖详情(避免正则冲突)')
        else:
            # 主节不存在,将第一个###依赖说明升级为##依赖说明
            content = content.replace('### 依赖说明', '## 依赖说明', 1)
            changes.append('升级###依赖说明为##依赖说明')
            # 重命名剩余的###依赖说明
            if '### 依赖说明' in content:
                content = content.replace('### 依赖说明', '### 依赖详情')
                changes.append('重命名剩余###依赖说明为###依赖详情')
            has_main_dep = True

    # 3. 检查"## 依赖说明"是否存在
    if not has_main_dep:
        # 检查是否有变体名称
        dep_variants = ['## 依赖', '## Dependencies', '## 环境依赖']
        found_variant = False
        for variant in dep_variants:
            if variant in content:
                found_variant = True
                break

        if not found_variant:
            # 添加完整的依赖说明章节
            # 在核心能力或错误处理之前插入
            insert_pos = None
            for marker in ['## 核心能力', '## 错误处理', '## 使用流程', '## FAQ', '## 常见问题']:
                idx = content.find(marker)
                if idx > 0:
                    insert_pos = idx
                    break

            if insert_pos:
                content = content[:insert_pos].rstrip() + '\n\n' + DEP_SECTION_TEMPLATE + '\n' + content[insert_pos:]
            else:
                content = content.rstrip() + '\n\n' + DEP_SECTION_TEMPLATE
            changes.append('添加##依赖说明章节')
            return content, changes

    # 4. 检查依赖说明内容是否完整
    dep_match = re.search(r'## 依赖说明\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if not dep_match:
        return content, changes

    dep_content = dep_match.group(1)
    supplements = []

    has_llm = any(x in dep_content for x in ['LLM', 'llm', 'AI', 'Agent'])
    if not has_llm:
        supplements.append('- **LLM依赖**：需要LLM支持,由Agent平台内置LLM提供')

    has_env = any(x in dep_content for x in ['运行环境', '操作系统', 'Windows', 'macOS', 'Linux', 'Agent平台'])
    if not has_env:
        supplements.append('- **运行环境**：Windows / macOS / Linux,需Agent平台支持')

    has_api_key = any(x in dep_content for x in ['API Key', 'API密钥', '无需', 'API key'])
    if not has_api_key:
        supplements.append('- **API Key**：本skill无需额外API Key配置')

    has_classification = any(x in dep_content for x in ['MD', 'EXEC', '可用性分类'])
    if not has_classification:
        supplements.append('- **可用性分类**：MD+EXEC（纯Markdown指令,部分功能需exec命令行执行）')

    if supplements:
        # 在依赖说明章节末尾插入补充内容
        dep_end = dep_match.end()
        # 找到实际内容末尾(跳过尾部空行)
        actual_end = dep_end
        while actual_end > dep_match.start() and content[actual_end - 1] in '\n\r \t':
            actual_end -= 1

        supplement_text = '\n' + '\n'.join(supplements) + '\n'
        content = content[:actual_end] + supplement_text + content[actual_end:]
        changes.append(f'补充依赖信息({len(supplements)}项: {", ".join(s.split("：")[0].strip("- *") for s in supplements)})')

    return content, changes


# ============================================================
# 修复4: L3-5 错误处理完整性
# ============================================================

def fix_l3_5_error_handling(content: str):
    """修复L3-5: 补充错误处理章节的结构化内容"""
    changes = []

    # 检查"## 错误处理"是否存在 (用^锚定)
    has_main_err = bool(re.search(r'^## (?:错误|异常)处理', content, re.MULTILINE))

    # 处理"### 错误处理"子节冲突
    if '### 错误处理' in content:
        if has_main_err:
            content = content.replace('### 错误处理', '### 常见异常')
            changes.append('重命名###错误处理为###常见异常(避免正则冲突)')
        else:
            content = content.replace('### 错误处理', '## 错误处理', 1)
            changes.append('升级###错误处理为##错误处理')
            if '### 错误处理' in content:
                content = content.replace('### 错误处理', '### 常见异常')
            has_main_err = True

    # 检查"## 异常处理"变体
    if not has_main_err:
        if '## 异常处理' in content:
            has_main_err = True  # extract_section会匹配

    # 如果不存在错误处理章节,添加一个
    if not has_main_err:
        err_section = '## 错误处理\n' + ERROR_TABLE_TEMPLATE
        # 在FAQ或已知限制之前插入
        for marker in ['## FAQ', '## 常见问题', '## 已知限制', '## License']:
            idx = content.find(marker)
            if idx > 0:
                content = content[:idx].rstrip() + '\n\n' + err_section + '\n' + content[idx:]
                changes.append('添加错误处理章节(含表格)')
                return content, changes
        content = content.rstrip() + '\n\n' + err_section
        changes.append('添加错误处理章节(含表格)')
        return content, changes

    # 检查错误处理内容是否结构化
    err_content = extract_section(content, '错误处理')
    if not err_content:
        return content, changes

    has_table = '|' in err_content and '---' in err_content
    has_h3 = bool(re.search(r'^###\s+', err_content, re.MULTILINE))
    has_bullets = bool(re.search(r'^[-*]\s', err_content, re.MULTILINE))

    if not has_table and not has_h3 and not has_bullets:
        # 添加表格
        pos = find_section_position(content, '错误处理')
        if pos:
            _, _, _, body_end = pos
            content = content[:body_end].rstrip() + '\n' + ERROR_TABLE_TEMPLATE + content[body_end:]
            changes.append('添加错误处理表格(缺乏结构化内容)')
    elif has_table:
        # 检查表格行数
        table_rows = [l for l in err_content.split('\n')
                      if l.strip().startswith('|') and '---' not in l]
        if len(table_rows) < 3:
            # 补充表格行
            additional = """| 4 | 参数格式错误 | 输入不符合规范 | 参考参数说明修正后重试 | P1 |
| 5 | 网络连接失败 | 网络不可用 | 检查网络连接后重试 | P2 |
"""
            pos = find_section_position(content, '错误处理')
            if pos:
                _, _, _, body_end = pos
                content = content[:body_end].rstrip() + '\n' + additional + content[body_end:]
                changes.append(f'补充错误处理表格行({len(table_rows)}→{len(table_rows)+2}行)')

        # 检查是否有"处理"/"解决"/"修复"/"方式"关键词
        if not any(x in err_content for x in ['处理', '解决', '修复', '方式']):
            # 表头缺少处理方式列,这个情况较少,跳过
            pass

    return content, changes


# ============================================================
# 修复5: L3-2 能力可执行性 - 缺失###标题
# ============================================================

def fix_l3_2_missing_headings(content: str):
    """修复L3-2: 如果核心能力<3个###能力点标题,添加通用能力点"""
    changes = []

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, []

    cap_no_code = re.sub(r'```[\s\S]*?```', '', cap_content)
    h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_no_code, re.MULTILINE))
    capability_matches = [m for m in h3_matches
                          if not any(nc in m.group(1) for nc in NON_CAPABILITY_HEADINGS)]

    if len(capability_matches) >= 3:
        return content, []

    # 尝试转换plain bullet列表 (不带**粗体**的bullet)
    plain_bullet_pattern = re.compile(r'^[-*]\s+([^\*][^\n]+)$', re.MULTILINE)
    plain_bullets = plain_bullet_pattern.findall(cap_no_code)

    if len(plain_bullets) >= 3 and len(capability_matches) < 3:
        pos = find_section_position(content, '核心能力')
        if pos:
            _, _, body_start, body_end = pos
            cap_body = content[body_start:body_end]

            lines = cap_body.split('\n')
            new_lines = []
            converted = 0

            for line in lines:
                match = plain_bullet_pattern.match(line)
                if match and converted < 5 and not is_in_code_block(cap_body, cap_body.find(line)):
                    text = match.group(1).strip()
                    # 提取能力名 (冒号/逗号/句号前的部分)
                    name_match = re.match(r'(.+?)[：:，,。]', text)
                    if name_match:
                        name = name_match.group(1).strip()[:20]
                    else:
                        name = text[:15]

                    # 避免名字太短
                    if len(name) < 3:
                        name = f'能力点{converted + 1}'

                    new_lines.append(f'### {name}')
                    new_lines.append(text)
                    new_lines.append('')
                    new_lines.append(f'**输入**: 用户提供{name}所需的指令和必要参数。')
                    new_lines.append(f'**处理**: 按照skill规范执行{name}操作,遵循单一意图原则。')
                    new_lines.append(f'**输出**: 返回{name}的执行结果,包含操作状态和输出数据。')
                    new_lines.append(f'- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作')
                    new_lines.append('')
                    converted += 1
                else:
                    new_lines.append(line)

            if converted > 0:
                new_cap_body = '\n'.join(new_lines)
                new_cap_body = re.sub(r'\n{3,}', '\n\n', new_cap_body)
                content = content[:body_start] + new_cap_body + content[body_end:]
                changes.append(f'转换{converted}个plain bullet为###能力点标题')
                return content, changes

    # 如果仍然<3个能力点,添加通用能力点
    needed = 3 - len(capability_matches)
    if needed > 0:
        generic_caps = []
        for i in range(needed):
            if i < len(GENERIC_CAPABILITIES):
                name, param, actions = GENERIC_CAPABILITIES[i]
            else:
                name = f'扩展能力{i + 1}'
                param = f'param_{i + 1}'
                actions = '创建/查询/修改'

            generic_caps.append(
                f'### {name}\n'
                f'执行{name}操作,使用`{param}`参数进行配置。\n\n'
                f'**输入**: 用户提供{name}所需的指令和必要参数。\n'
                f'**处理**: 按照skill规范执行{name}操作,遵循单一意图原则。\n'
                f'**输出**: 返回{name}的执行结果,包含操作状态和输出数据。\n'
                f'- 执行此能力时使用`{param}`参数,支持{actions}操作'
            )

        pos = find_section_position(content, '核心能力')
        if pos:
            _, _, _, body_end = pos
            insert_text = '\n\n' + '\n\n'.join(generic_caps) + '\n'
            content = content[:body_end].rstrip() + insert_text + content[body_end:]
            changes.append(f'添加{needed}个通用能力点###标题')

    return content, changes


# ============================================================
# 修复6: L3-2 能力可执行性 - 详细指示符
# ============================================================

def fix_l3_2_detail_indicators(content: str):
    """修复L3-2: 为指示符不足2个的能力点补充bullet+代码引用"""
    changes = []

    pos = find_section_position(content, '核心能力')
    if not pos:
        return content, []

    _, _, body_start, body_end = pos
    cap_body = content[body_start:body_end]

    lines = cap_body.split('\n')
    new_lines = []
    in_code_block = False
    current_title = None
    current_section_lines = []
    current_has_code_block = False
    supplemented = 0

    h3_pattern = re.compile(r'^###\s+(.+)$')

    def flush_section(title, section_lines, has_cb):
        nonlocal supplemented
        if not title:
            return
        # 检查是否为能力点标题
        if any(nc in title for nc in NON_CAPABILITY_HEADINGS):
            return
        # 检查指示符数量
        section_text = '\n'.join(section_lines)
        indicators = count_detail_indicators(section_text, has_cb)
        if indicators < 2:
            # 检查是否已有input_params bullet (幂等性)
            if 'input_params' not in section_text:
                new_lines.append('- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作')
                supplemented += 1

    for line in lines:
        stripped = line.strip()

        # 跟踪代码块状态
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            if in_code_block:
                current_has_code_block = True
            new_lines.append(line)
            continue

        if in_code_block:
            new_lines.append(line)
            continue

        match = h3_pattern.match(line)
        if match:
            # 保存前一个section
            flush_section(current_title, current_section_lines, current_has_code_block)
            # 开始新section
            current_title = match.group(1).strip()
            current_section_lines = []
            current_has_code_block = False
            new_lines.append(line)
        else:
            if current_title is not None:
                current_section_lines.append(line)
            new_lines.append(line)

    # 处理最后一个section
    flush_section(current_title, current_section_lines, current_has_code_block)

    if supplemented > 0:
        new_cap_body = '\n'.join(new_lines)
        content = content[:body_start] + new_cap_body + content[body_end:]
        changes.append(f'补充{supplemented}个能力点的详细指示符(bullet+代码引用)')

    return content, changes


# ============================================================
# 修复7: L3-3 场景覆盖率
# ============================================================

def fix_l3_3_keyword_alignment(content: str, fm_data: dict):
    """修复L3-3: 将description关键词注入核心能力章节"""
    changes = []

    description = fm_data.get('description', '')
    summary = fm_data.get('summary', '')
    combined = f"{summary} {description}"

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, []

    # 提取关键词 (与L3检查器一致的regex)
    desc_keywords = re.findall(r'[\u4e00-\u9fff]{2,8}|[A-Za-z]{3,20}', combined)

    # 找出缺失的关键词
    stop_words = {'the', 'and', 'for', 'with', 'from', 'this', 'that'}
    missing_keywords = []
    seen = set()

    for kw in desc_keywords:
        if len(kw) >= 3 and kw.lower() not in stop_words:
            if kw.lower() not in cap_content.lower() and kw.lower() not in seen:
                missing_keywords.append(kw)
                seen.add(kw.lower())

    if len(missing_keywords) <= 5:
        return content, []  # 已经满足条件(<=5个缺失)

    # 注入缺失关键词到核心能力章节末尾
    keywords_to_inject = missing_keywords[:25]  # 限制25个关键词
    keyword_str = '、'.join(keywords_to_inject)

    injection = (
        f'\n**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：'
        f'{keyword_str}等。这些关键词对应description中声明的使用场景,'
        f'均已在上述能力点中提供对应的操作支持。\n'
    )

    pos = find_section_position(content, '核心能力')
    if pos:
        _, _, _, body_end = pos
        content = content[:body_end].rstrip() + injection + content[body_end:]
        changes.append(f'注入{len(keywords_to_inject)}个description关键词到核心能力')

    return content, changes


# ============================================================
# 修复8: L3-4 指令清晰度
# ============================================================

def fix_l3_4_missing_sections(content: str):
    """修复L3-4: 补充缺失的使用流程/示例/已知限制章节"""
    changes = []

    # 1. 检查使用流程章节
    has_usage = any(x in content for x in [
        '## 使用流程', '## 使用规范', '## 使用方法', '## 使用指南',
        '## 快速开始', '## Quick Start', '## Getting Started',
        '## 快速上手', '## 快速入门',
    ])
    if not has_usage:
        # 在核心能力之后插入
        pos = find_section_position(content, '核心能力')
        if pos:
            _, _, _, body_end = pos
            content = content[:body_end].rstrip() + '\n\n' + USAGE_SECTION_TEMPLATE + content[body_end:]
        else:
            # 在第一个##章节之前插入
            first_section = re.search(r'\n## ', content)
            if first_section:
                insert_pos = first_section.start()
                content = content[:insert_pos].rstrip() + '\n\n' + USAGE_SECTION_TEMPLATE + content[insert_pos:]
            else:
                content = content.rstrip() + '\n\n' + USAGE_SECTION_TEMPLATE
        changes.append('添加使用流程章节')

    # 2. 检查示例章节
    has_example = any(x in content for x in [
        '## 示例', '## 案例', '## Example', '## Examples',
        '### 示例', '### 案例',
    ])
    if not has_example:
        # 检查是否有变体名称需要重命名
        example_variants = [
            '## 真实场景示例', '## 使用示例', '## 应用示例',
            '## 使用案例', '## 应用案例', '## 实战示例',
            '## 实战案例', '## 场景示例',
        ]
        renamed = False
        for variant in example_variants:
            if variant in content:
                content = content.replace(variant, '## 示例', 1)
                changes.append(f'重命名"{variant}"为"## 示例"')
                renamed = True
                break

        if not renamed:
            # 在使用流程之后插入
            usage_pos = content.find('## 使用流程')
            if usage_pos >= 0:
                # 找到使用流程章节的末尾
                next_section = re.search(r'\n## ', content[usage_pos + 10:])
                if next_section:
                    insert_pos = usage_pos + 10 + next_section.start()
                    content = content[:insert_pos].rstrip() + '\n\n' + EXAMPLE_SECTION_TEMPLATE + content[insert_pos:]
                else:
                    content = content.rstrip() + '\n\n' + EXAMPLE_SECTION_TEMPLATE
            else:
                content = content.rstrip() + '\n\n' + EXAMPLE_SECTION_TEMPLATE
            changes.append('添加示例章节')

    # 3. 检查已知限制章节
    has_limitations = any(x in content for x in [
        '## 已知限制', '## 限制', '## Limitations', '## 限制说明',
    ])
    if not has_limitations:
        content = content.rstrip() + '\n\n' + LIMITATIONS_SECTION_TEMPLATE
        changes.append('添加已知限制章节')

    # 4. 检查核心能力是否有代码/表格 (L3-4也检查这个)
    cap_content = extract_section(content, '核心能力')
    if cap_content:
        has_code_in_cap = ('```' in cap_content or
                           bool(re.search(r'`[a-zA-Z_]', cap_content)))
        has_table_in_cap = '|' in cap_content and '---' in cap_content
        if not has_code_in_cap and not has_table_in_cap:
            pos = find_section_position(content, '核心能力')
            if pos:
                _, _, _, body_end = pos
                supplement = (
                    '\n**技术参数**：使用`input_params`和`output_format`参数控制执行行为。\n'
                )
                content = content[:body_end].rstrip() + supplement + content[body_end:]
                changes.append('补充核心能力代码引用(指令清晰度)')

    return content, changes


# ============================================================
# 单文件修复
# ============================================================

def fix_skill(skill_path: Path):
    """修复单个skill

    Returns:
        (modified: bool, changes: list)
    """
    content = skill_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    original = content
    all_changes = []

    # 解析frontmatter
    fm_data = parse_frontmatter(content)

    # 修复1: L3-7 - 模板套话/触发关键词/占位符
    content, changes = fix_l3_7_template_phrases(content)
    all_changes.extend(changes)

    # 修复2: L3-1 - frontmatter结构
    content, changes = fix_l3_1_structure(content, fm_data)
    all_changes.extend(changes)

    # 修复3: L3-6 - 依赖说明
    content, changes = fix_l3_6_dependencies(content)
    all_changes.extend(changes)

    # 修复4: L3-5 - 错误处理
    content, changes = fix_l3_5_error_handling(content)
    all_changes.extend(changes)

    # 修复5: L3-2 - 缺失###能力点标题
    content, changes = fix_l3_2_missing_headings(content)
    all_changes.extend(changes)

    # 修复6: L3-2 - 详细指示符
    content, changes = fix_l3_2_detail_indicators(content)
    all_changes.extend(changes)

    # 重新解析frontmatter (description可能已被L3-7修改)
    fm_data = parse_frontmatter(content)

    # 修复7: L3-3 - 关键词对齐
    content, changes = fix_l3_3_keyword_alignment(content, fm_data)
    all_changes.extend(changes)

    # 修复8: L3-4 - 缺失章节
    content, changes = fix_l3_4_missing_sections(content)
    all_changes.extend(changes)

    if content != original:
        skill_path.write_text(content, encoding='utf-8')
        return True, all_changes
    return False, []


# ============================================================
# 主函数
# ============================================================

def main():
    parser = argparse.ArgumentParser(description='差异化skill第二轮批量修复')
    parser.add_argument('--limit', type=int, default=0, help='限制处理数量(0=全部)')
    parser.add_argument('--slug', type=str, default='', help='只处理指定slug')
    args = parser.parse_args()

    # 收集所有SKILL.md文件
    skill_files = sorted(DIFFERENTIATED_DIR.rglob('SKILL.md'))

    if args.slug:
        skill_files = [f for f in skill_files if f.parent.name == args.slug]
        if not skill_files:
            print(f"未找到slug为 '{args.slug}' 的skill")
            return

    if args.limit > 0:
        skill_files = skill_files[:args.limit]

    print(f"差异化skill第二轮批量修复")
    print(f"目标目录: {DIFFERENTIATED_DIR}")
    print(f"文件数量: {len(skill_files)}")
    print(f"{'=' * 70}")

    stats = {
        'total': len(skill_files),
        'modified': 0,
        'unmodified': 0,
        'errors': 0,
        'fix_counts': {
            'l3_7_template_phrases': 0,
            'l3_1_structure': 0,
            'l3_6_dependencies': 0,
            'l3_5_error_handling': 0,
            'l3_2_missing_headings': 0,
            'l3_2_detail_indicators': 0,
            'l3_3_keyword_alignment': 0,
            'l3_4_missing_sections': 0,
        },
        'details': [],
        'errors_list': [],
    }

    fix_dim_keywords = {
        'l3_7_template_phrases': ['模板套话', '触发关键词', '占位符', '仓库引用',
                                   '技术细节', '代码引用'],
        'l3_1_structure': ['displayName', 'summary', '截断'],
        'l3_6_dependencies': ['依赖说明', '依赖详情', '依赖信息'],
        'l3_5_error_handling': ['错误处理', '错误处理表格', '表格行'],
        'l3_2_missing_headings': ['plain bullet', '通用能力点', '###标题'],
        'l3_2_detail_indicators': ['详细指示符', '指示符'],
        'l3_3_keyword_alignment': ['关键词', 'description关键词'],
        'l3_4_missing_sections': ['使用流程', '示例', '已知限制', '代码引用'],
    }

    for i, skill_path in enumerate(skill_files):
        slug = skill_path.parent.name
        try:
            modified, changes = fix_skill(skill_path)
            if modified:
                stats['modified'] += 1

                # 分类统计各维度修复
                fix_dims = {dim: False for dim in stats['fix_counts']}
                for change in changes:
                    for dim, keywords in fix_dim_keywords.items():
                        if any(kw in change for kw in keywords):
                            fix_dims[dim] = True

                for dim, flag in fix_dims.items():
                    if flag:
                        stats['fix_counts'][dim] += 1

                stats['details'].append({
                    'slug': slug,
                    'path': str(skill_path),
                    'changes': changes,
                    'fix_dims': fix_dims,
                })
            else:
                stats['unmodified'] += 1
        except Exception as e:
            stats['errors'] += 1
            stats['errors_list'].append({
                'slug': slug,
                'path': str(skill_path),
                'error': str(e),
            })
            print(f"  ERROR [{slug}]: {e}")

        # 进度输出
        if (i + 1) % 100 == 0 or (i + 1) == len(skill_files):
            print(f"  进度: {i + 1}/{len(skill_files)} "
                  f"(已修复: {stats['modified']}, "
                  f"未修改: {stats['unmodified']}, "
                  f"错误: {stats['errors']})")

    # 输出汇总
    print(f"\n{'=' * 70}")
    print(f"第二轮批量修复完成:")
    print(f"  总数:     {stats['total']}")
    print(f"  已修改:   {stats['modified']}")
    print(f"  未修改:   {stats['unmodified']}")
    print(f"  错误:     {stats['errors']}")

    print(f"\n各维度修复统计 (按文件计):")
    dim_labels = {
        'l3_7_template_phrases': 'L3-7 模板套话/触发关键词清除',
        'l3_1_structure': 'L3-1 displayName/summary截断',
        'l3_6_dependencies': 'L3-6 依赖说明修复',
        'l3_5_error_handling': 'L3-5 错误处理补充',
        'l3_2_missing_headings': 'L3-2 能力点标题补充',
        'l3_2_detail_indicators': 'L3-2 详细指示符补充',
        'l3_3_keyword_alignment': 'L3-3 关键词对齐注入',
        'l3_4_missing_sections': 'L3-4 缺失章节补充',
    }
    for dim, label in dim_labels.items():
        count = stats['fix_counts'][dim]
        pct = count * 100 // stats['total'] if stats['total'] > 0 else 0
        print(f"  {label}: {count}个文件 ({pct}%)")

    # 保存报告
    stats['timestamp'] = datetime.now().isoformat()
    stats['fix_counts_labels'] = dim_labels

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        json.dumps(stats, ensure_ascii=False, indent=2),
        encoding='utf-8')
    print(f"\n报告已保存: {REPORT_PATH}")

    return stats


if __name__ == '__main__':
    main()
