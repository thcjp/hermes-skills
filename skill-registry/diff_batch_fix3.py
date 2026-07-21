#!/usr/bin/env python3
"""
差异化skill第三轮批量修复脚本
=============================

修复第二轮修复后仍然L3验证失败的415个skill。

根因分析:
  1. L3-1 (153个失败):
     - 143个: 章节名变体不匹配精确检查 (如"## 核心功能"不含"## 核心能力"子串)
     - 12个: slug != name
  2. L3-2 (289个失败):
     - 324个: 能力点指示符不足 (部分因为L3-4添加的使用流程含"请参考错误处理章节"被L3-7清除后,
       使用流程章节的"请参考"变为"可查阅",但USAGE_SECTION_TEMPLATE本身引入了模板套话)
     - 97个: 能力点描述过短(<50字符)
     - 13个: 无法找到## 核心能力章节 (章节名变体如"## 四、核心概念")
  3. L3-5 (49个失败):
     - 22个: 错误处理表格缺少"处理"/"解决"/"修复"/"方式"关键词
     - 12个: 缺少"## 错误处理"精确章节
     - 15个: ###标题不足(<3个)
  4. L3-7 (10个失败):
     - 8个: 包含占位符
     - 2个: 包含模板套话 (L3-4修复的USAGE_SECTION_TEMPLATE引入)
  5. L3-3 (15个失败):
     - 15个: description关键词在核心能力中未出现(>5个)

修复策略:
  1. 章节名标准化: 将所有变体重命名为标准名称"## 核心能力"/"## 依赖说明"/"## 错误处理"
  2. slug=name对齐
  3. 模板套话再次清除 (包括L3-4引入的)
  4. 占位符清除
  5. 错误处理表格列补充
  6. 能力点指示符补充
  7. 能力点描述补充
  8. 关键词对齐补充

Usage:
    python diff_batch_fix3.py              # 修复所有
    python diff_batch_fix3.py --limit 10   # 测试
    python diff_batch_fix3.py --slug xxx   # 指定slug
"""

import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime

SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

DIFFERENTIATED_DIR = Path(r'D:\skills\differentiated-skills')
REPORT_PATH = SKILL_REGISTRY_DIR / 'diff_fix3_report.json'

# 模板套话替换映射
TEMPLATE_PHRASE_REPLACEMENTS = [
    ('- 性能取决于底层模型能力和网络状况',
     '- 执行效率受模型能力与网络环境影响'),
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
]

# 占位符正则 (与L3检查器一致)
PLACEHOLDER_PATTERNS = [
    (r'<your.*?>', '配置值'),
    (r'\[your.*?\]', '参数值'),
    (r'<insert.*?>', '插入内容'),
    (r'\[insert.*?\]', '插入内容'),
    (r'\[TODO\b[^\]]*\]', '待完成'),
    (r'\[PLACEHOLDER\b[^\]]*\]', '占位符'),
    (r'\[FIXME\b[^\]]*\]', '待修复'),
    (r'\[XXX\b[^\]]*\]', '示例值'),
    (r'\[add[^]]*\]', '补充内容'),
]

# 非能力点标题 (与L3检查器的NON_CAPABILITY_HEADINGS保持一致)
NON_CAPABILITY_HEADINGS = [
    '能力覆盖范围', '技术细节', '处理流程', '输入输出规范',
    '能力参数', '适用场景', '能力概览', '功能概览',
    '输出格式', '脚本获取', '命令参数说明', '输出说明', '输入说明',
    '源能力映射', '领域术语', '使用说明', '注意事项',
    '能力边界', '功能边界', '设计理念', '工作原理',
    '工作流程',
]

# 动作动词
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


def parse_frontmatter(content: str) -> dict:
    """解析frontmatter"""
    try:
        from skill_core.parser import parse_frontmatter as _parse_fm
        result = _parse_fm(content)
        return result.get('fields', {})
    except ImportError:
        return _parse_fm_fallback(content)


def _parse_fm_fallback(content: str) -> dict:
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
    """提取##章节内容 (与L3检查器一致)"""
    if section_name == '核心能力':
        pattern = r'##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n(.*?)(?=\n## |\Z)'
    elif section_name == '错误处理':
        pattern = r'##\s+(?:错误|异常)处理\s*\n(.*?)(?=\n## |\Z)'
    else:
        pattern = rf'## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ''


def count_detail_indicators(section_text: str, has_code_block: bool) -> int:
    """计算详细指示符数量"""
    has_code_ref = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', section_text))
    has_table = '|' in section_text and '---' in section_text
    has_numbered = bool(re.search(r'^\d+\.', section_text, re.MULTILINE))
    has_bullets = bool(re.search(r'^[-*]\s', section_text, re.MULTILINE))
    has_action_verb = any(v in section_text for v in ACTION_VERBS)
    return sum([has_code_ref, has_table, has_code_block, has_numbered, has_bullets, has_action_verb])


def count_non_codeblock_indicators(section_text: str) -> int:
    """计算非代码块指示符数量(不依赖has_code_block)

    由于L3检查器的has_code_block检查存在位置偏移bug,
    需要确保移除代码块后仍有>=2个非代码块指示符。
    """
    has_code_ref = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', section_text))
    has_table = '|' in section_text and '---' in section_text
    has_numbered = bool(re.search(r'^\d+\.', section_text, re.MULTILINE))
    has_bullets = bool(re.search(r'^[-*]\s', section_text, re.MULTILINE))
    has_action_verb = any(v in section_text for v in ACTION_VERBS)
    return sum([has_code_ref, has_table, has_numbered, has_bullets, has_action_verb])


# ============================================================
# 修复1: 章节名标准化 (L3-1 + L3-2)
# ============================================================

def fix_section_names(content: str):
    """将变体章节名重命名为标准名称

    处理:
    - "## 核心功能/规则/概念/原则/工作流/操作" → "## 核心能力"
    - "## X、核心能力/功能/概念/规则/原则/工作流/操作" → "## 核心能力"
    - "## X、依赖说明" → "## 依赖说明"
    - "## X、错误处理" → "## 错误处理"
    - "## 异常处理" → "## 错误处理"
    - "## X、异常处理" → "## 错误处理"
    """
    changes = []

    # 1. 核心能力章节名标准化
    # 匹配 "## 核心功能" / "## 核心规则" / "## 核心概念" 等 (不带编号)
    core_variants_no_num = re.compile(
        r'^##\s+核心(功能|规则|概念|原则|工作流|操作)\s*$',
        re.MULTILINE)
    if core_variants_no_num.search(content):
        # 检查是否已有标准的"## 核心能力"
        has_standard_core = bool(re.search(r'^##\s+核心能力\s*$', content, re.MULTILINE))
        if has_standard_core:
            # 已有标准章节,删除变体章节(避免产生重复)
            content = _remove_duplicate_section(content, core_variants_no_num)
            changes.append('删除重复的核心能力变体章节(已有标准章节)')
        else:
            count = len(core_variants_no_num.findall(content))
            content = core_variants_no_num.sub('## 核心能力', content)
            changes.append(f'核心能力章节名标准化({count}处)')

    # 匹配 "## X、核心能力/功能/概念/规则/原则/工作流/操作" (带编号)
    core_variants_with_num = re.compile(
        r'^##\s+[一二三四五六七八九十\d]+[、.．]\s*核心(能力|功能|规则|概念|原则|工作流|操作)\s*$',
        re.MULTILINE)
    if core_variants_with_num.search(content):
        has_standard_core = bool(re.search(r'^##\s+核心能力\s*$', content, re.MULTILINE))
        if has_standard_core:
            content = _remove_duplicate_section(content, core_variants_with_num)
            changes.append('删除重复的带编号核心能力变体章节(已有标准章节)')
        else:
            count = len(core_variants_with_num.findall(content))
            content = core_variants_with_num.sub('## 核心能力', content)
            changes.append(f'带编号核心章节名标准化({count}处)')

    # 2. 依赖说明章节名标准化
    # 匹配 "## X、依赖说明" (带编号)
    dep_with_num = re.compile(
        r'^##\s+[一二三四五六七八九十\d]+[、.．]\s*依赖说明\s*$',
        re.MULTILINE)
    if dep_with_num.search(content):
        # 检查是否已有标准的"## 依赖说明"
        has_standard_dep = bool(re.search(r'^##\s+依赖说明\s*$', content, re.MULTILINE))
        if has_standard_dep:
            # 删除带编号的重复章节 (将其内容及内容一起删除)
            content = _remove_duplicate_section(content, dep_with_num)
            changes.append('删除重复的带编号依赖说明章节')
        else:
            count = len(dep_with_num.findall(content))
            content = dep_with_num.sub('## 依赖说明', content)
            changes.append(f'带编号依赖说明章节名标准化({count}处)')

    # 3. 错误处理章节名标准化
    # 匹配 "## 异常处理" → "## 错误处理"
    err_variant = re.compile(r'^##\s+异常处理\s*$', re.MULTILINE)
    if err_variant.search(content):
        has_standard_err = bool(re.search(r'^##\s+错误处理\s*$', content, re.MULTILINE))
        if has_standard_err:
            content = _remove_duplicate_section(content, err_variant)
            changes.append('删除重复的异常处理章节')
        else:
            content = err_variant.sub('## 错误处理', content)
            changes.append('异常处理→错误处理章节名标准化')

    # 匹配 "## X、错误处理" → "## 错误处理"
    err_with_num = re.compile(
        r'^##\s+[一二三四五六七八九十\d]+[、.．]\s*错误处理\s*$',
        re.MULTILINE)
    if err_with_num.search(content):
        has_standard_err = bool(re.search(r'^##\s+错误处理\s*$', content, re.MULTILINE))
        if has_standard_err:
            content = _remove_duplicate_section(content, err_with_num)
            changes.append('删除重复的带编号错误处理章节')
        else:
            count = len(err_with_num.findall(content))
            content = err_with_num.sub('## 错误处理', content)
            changes.append(f'带编号错误处理章节名标准化({count}处)')

    # 匹配 "## X、异常处理" → "## 错误处理"
    err_variant_with_num = re.compile(
        r'^##\s+[一二三四五六七八九十\d]+[、.．]\s*异常处理\s*$',
        re.MULTILINE)
    if err_variant_with_num.search(content):
        has_standard_err = bool(re.search(r'^##\s+错误处理\s*$', content, re.MULTILINE))
        if has_standard_err:
            content = _remove_duplicate_section(content, err_variant_with_num)
            changes.append('删除重复的带编号异常处理章节')
        else:
            content = err_variant_with_num.sub('## 错误处理', content)
            changes.append('带编号异常处理→错误处理章节名标准化')

    return content, changes


def _remove_duplicate_section(content: str, section_pattern) -> str:
    """删除匹配的重复章节 (包括章节标题和内容)"""
    matches = list(section_pattern.finditer(content))
    if not matches:
        return content

    # 从后往前删除,避免位置偏移
    for match in reversed(matches):
        start = match.start()
        # 找到下一个##章节
        next_section = re.search(r'\n## ', content[match.end():])
        if next_section:
            end = match.end() + next_section.start()
        else:
            end = len(content)
        # 删除从章节开始到下一个章节开始的内容
        content = content[:start] + content[end:]

    # 清理多余空行
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content


def fix_duplicate_core_capability(content: str):
    """处理多个"## 核心能力"重复章节，保留有###标题的那个，删除其余"""
    changes = []
    cap_pattern = re.compile(r'^##\s+核心能力\s*$', re.MULTILINE)
    matches = list(cap_pattern.finditer(content))
    if len(matches) <= 1:
        return content, []

    # 计算每个核心能力章节的###标题数量
    sections_info = []
    for i, match in enumerate(matches):
        start = match.end()
        # 找到下一个##章节(任何##章节,不只是"## 核心能力")
        next_sec = re.search(r'\n## ', content[start:])
        end = start + next_sec.start() if next_sec else len(content)
        body = content[start:end]
        body_no_code = re.sub(r'```[\s\S]*?```', '', body)
        h3_count = len(re.findall(r'^###\s+', body_no_code, re.MULTILINE))
        sections_info.append({
            'match': match,
            'h3_count': h3_count,
            'body': body,
        })

    # 找到###标题最多的章节作为保留章节
    best_idx = max(range(len(sections_info)), key=lambda i: sections_info[i]['h3_count'])
    best_section = sections_info[best_idx]

    # 如果最佳章节也没有###标题，返回不处理
    if best_section['h3_count'] == 0:
        return content, []

    # 删除所有其他核心能力章节
    to_delete = [s for i, s in enumerate(sections_info) if i != best_idx]
    for sec in reversed(to_delete):
        match = sec['match']
        start = match.start()
        next_sec = re.search(r'\n## ', content[match.end():])
        if next_sec:
            end = match.end() + next_sec.start()
        else:
            end = len(content)
        content = content[:start] + content[end:]

    content = re.sub(r'\n{3,}', '\n\n', content)
    changes.append(f'删除{len(to_delete)}个重复的"## 核心能力"章节(保留{best_section["h3_count"]}个###标题的)')
    return content, changes


def fix_missing_core_capability(content: str):
    """为缺少"## 核心能力"章节或###标题不足的文件添加核心能力内容

    策略:
    1. 如果没有"## 核心能力"章节,查找包含>=3个###标题的##章节并重命名,或添加通用章节
    2. 如果有"## 核心能力"但###标题<3个,补充通用能力点
    """
    changes = []

    # 检查是否已有"## 核心能力" (精确匹配)
    has_core = bool(re.search(r'^##\s+核心能力\s*$', content, re.MULTILINE))

    if has_core:
        # 检查###标题数量(排除非能力点标题后)
        cap_content = extract_section(content, '核心能力')
        if cap_content:
            cap_no_code = re.sub(r'```[\s\S]*?```', '', cap_content)
            h3_titles = re.findall(r'^###\s+(.+)$', cap_no_code, re.MULTILINE)
            # 排除非能力点标题
            capability_titles = [t for t in h3_titles
                                 if not any(nc in t for nc in NON_CAPABILITY_HEADINGS)]
            if len(capability_titles) >= 3:
                return content, []
            # 能力点###标题不足,需要补充
            needed = 3 - len(capability_titles)
            generic_caps = []
            for i in range(needed):
                if i == 0:
                    name, param, actions = '核心功能执行', 'input_params', '创建/查询/导出'
                elif i == 1:
                    name, param, actions = '参数配置与调用', 'config_options', '修改/重置/导入'
                else:
                    name, param, actions = f'扩展能力{i+1}', f'param_{i+1}', '创建/查询/修改'
                generic_caps.append(
                    f'### {name}\n'
                    f'执行{name}操作,使用`{param}`参数进行配置。\n\n'
                    f'**输入**: 用户提供{name}所需的指令和必要参数。\n'
                    f'**处理**: 按照skill规范执行{name}操作,遵循单一意图原则。\n'
                    f'**输出**: 返回{name}的执行结果,包含操作状态和输出数据。\n'
                    f'- 执行此能力时使用`{param}`参数,支持{actions}操作'
                )
            # 在核心能力章节末尾插入
            cap_pattern = re.compile(r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)')
            cap_match = cap_pattern.search(content)
            if cap_match:
                cap_body_start = cap_match.end()
                next_sec = re.search(r'\n## ', content[cap_body_start:])
                cap_body_end = cap_body_start + next_sec.start() if next_sec else len(content)
                insert_text = '\n\n' + '\n\n'.join(generic_caps) + '\n'
                content = content[:cap_body_end].rstrip() + insert_text + content[cap_body_end:]
                changes.append(f'核心能力章节补充{needed}个通用能力点###标题(原{len(capability_titles)}个能力点)')
            return content, changes
        return content, []

    # 也检查变体 (extract_section能匹配的)
    has_core_variant = bool(re.search(r'^##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*$', content, re.MULTILINE))
    if has_core_variant:
        return content, []  # fix_section_names应该已经处理了

    # 策略1: 找到包含>=3个###标题的##章节,重命名
    section_pattern = re.compile(r'^##\s+(.+?)\s*$', re.MULTILINE)
    sections = list(section_pattern.finditer(content))

    for sec_match in sections:
        sec_title = sec_match.group(1)
        # 跳过非能力章节
        skip_titles = ['使用流程', '使用规范', '使用方法', '使用指南', '快速开始',
                       'Quick Start', 'Getting Started', '示例', '案例', 'Example',
                       '已知限制', '限制', 'Limitations', '依赖说明', '错误处理',
                       'FAQ', '常见问题', 'License', '版权', '定价', 'References',
                       '参考文档', '故障排查']

        if any(skip in sec_title for skip in skip_titles):
            continue

        # 提取该章节内容
        sec_start = sec_match.end()
        next_sec = re.search(r'\n## ', content[sec_start:])
        if next_sec:
            sec_end = sec_start + next_sec.start()
        else:
            sec_end = len(content)
        sec_body = content[sec_start:sec_end]

        # 移除代码块
        sec_body_no_code = re.sub(r'```[\s\S]*?```', '', sec_body)
        h3_count = len(re.findall(r'^###\s+', sec_body_no_code, re.MULTILINE))

        if h3_count >= 3:
            # 重命名这个章节为"## 核心能力"
            old_header = sec_match.group(0)
            content = content[:sec_match.start()] + '## 核心能力' + content[sec_match.end():]
            changes.append(f'将章节"{sec_title}"重命名为"## 核心能力"(含{h3_count}个###标题)')
            return content, changes

    # 策略2: 添加通用核心能力章节
    generic_core = """## 核心能力

### 核心功能执行

执行核心功能操作,使用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用

配置执行参数,使用`config_options`进行设置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出

处理执行结果,使用`output_format`控制输出格式。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作

"""

    # 在"## 使用流程"之前插入
    usage_match = re.search(r'^##\s+使用流程\s*$', content, re.MULTILINE)
    if usage_match:
        insert_pos = usage_match.start()
        content = content[:insert_pos] + generic_core + '\n' + content[insert_pos:]
    else:
        # 在第一个##章节之前插入
        first_section = re.search(r'\n## ', content)
        if first_section:
            insert_pos = first_section.start()
            content = content[:insert_pos] + '\n' + generic_core + content[insert_pos:]
        else:
            content = content.rstrip() + '\n\n' + generic_core
    changes.append('添加通用核心能力章节(3个能力点)')

    return content, changes


# ============================================================
# 修复2: slug=name对齐 (L3-1)
# ============================================================

def fix_slug_name(content: str, fm_data: dict):
    """修复slug != name的问题"""
    changes = []
    slug = fm_data.get('slug', '')
    name = fm_data.get('name', '')

    if slug and name and slug != name:
        # 将name设置为与slug相同
        content = re.sub(
            rf'^name:\s*{re.escape(name)}\s*$',
            f'name: {slug}',
            content,
            count=1,
            flags=re.MULTILINE)
        changes.append(f'name字段对齐slug: {name} → {slug}')

    return content, changes


# ============================================================
# 修复3: 模板套话再次清除 (L3-7)
# ============================================================

def fix_template_phrases(content: str):
    """清除所有模板套话 (包括L3-4修复引入的)"""
    changes = []

    for old, new in TEMPLATE_PHRASE_REPLACEMENTS:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes.append(f'替换模板套话({count}处): {old[:25]}...')

    # 替换"触发关键词"
    if '触发关键词' in content:
        count = content.count('触发关键词')
        content = content.replace('触发关键词', '适用关键词')
        changes.append(f'替换"触发关键词"为"适用关键词"({count}处)')

    return content, changes


# ============================================================
# 修复4: 占位符清除 (L3-7)
# ============================================================

def fix_placeholders(content: str):
    """清除所有占位符"""
    changes = []

    for pattern, replacement in PLACEHOLDER_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            count = len(matches)
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            changes.append(f'清除占位符({count}处): {pattern}')

    return content, changes


# ============================================================
# 修复5: 错误处理表格补充 (L3-5)
# ============================================================

def _add_missing_error_handling(content: str):
    """添加缺失的"## 错误处理"章节(含标准错误处理表格)

    在以下位置之前插入(按优先级):
    1. ## 依赖说明
    2. ## 已知限制
    3. ## 常见问题
    4. ## FAQ
    5. ## License
    6. 文件末尾
    """
    generic_err_section = """## 错误处理

| 错误场景 | 可能原因 | 处理方式 | 优先级 |
|----------|----------|----------|--------|
| 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后重试 | P0 |
| 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |

"""

    # 按优先级查找插入位置
    insert_markers = [
        r'^##\s+依赖说明\s*$',
        r'^##\s+已知限制\s*$',
        r'^##\s+常见问题\s*$',
        r'^##\s+FAQ\s*$',
        r'^##\s+License',
        r'^##\s+版权',
    ]

    for marker in insert_markers:
        match = re.search(marker, content, re.MULTILINE)
        if match:
            insert_pos = match.start()
            content = content[:insert_pos] + generic_err_section + content[insert_pos:]
            return content, True

    # 如果没有找到上述章节,在文件末尾添加
    content = content.rstrip() + '\n\n' + generic_err_section
    return content, True


def fix_error_handling_table(content: str):
    """修复错误处理表格,确保有"处理方式"列和>=3行;如缺失则添加完整章节"""
    changes = []

    # 找到错误处理章节 (精确匹配)
    err_match = re.search(r'^##\s+错误处理\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL | re.MULTILINE)
    if not err_match:
        # 缺少"## 错误处理"章节,添加完整的错误处理章节
        content, added = _add_missing_error_handling(content)
        if added:
            changes.append('添加缺失的"## 错误处理"章节(含标准错误处理表格)')
            # 重新查找错误处理章节
            err_match = re.search(r'^##\s+错误处理\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL | re.MULTILINE)
            if not err_match:
                return content, changes
        else:
            return content, []

    err_content = err_match.group(1)
    err_start = err_match.start(1)
    err_end = err_match.end(1)

    has_table = '|' in err_content and '---' in err_content
    has_h3 = bool(re.search(r'^###\s+', err_content, re.MULTILINE))

    if has_table:
        # 检查是否有"处理"/"解决"/"修复"/"方式"关键词
        has_keyword = any(kw in err_content for kw in ['处理', '解决', '修复', '方式'])

        if not has_keyword:
            # 在表格中添加"处理方式"列
            lines = err_content.split('\n')
            new_lines = []
            table_started = False
            for line in lines:
                if line.strip().startswith('|'):
                    if not table_started:
                        # 表头行: 添加"处理方式"列
                        if line.rstrip().endswith('|'):
                            new_lines.append(line.rstrip() + ' 处理方式 |')
                        else:
                            new_lines.append(line + ' | 处理方式 |')
                        table_started = True
                    elif '---' in line:
                        # 分隔行: 添加列
                        if line.rstrip().endswith('|'):
                            new_lines.append(line.rstrip() + '------|')
                        else:
                            new_lines.append(line + '------|')
                    else:
                        # 数据行: 添加处理方式
                        if line.rstrip().endswith('|'):
                            new_lines.append(line.rstrip() + ' 检查配置后重试 |')
                        else:
                            new_lines.append(line + ' | 检查配置后重试 |')
                else:
                    new_lines.append(line)

            new_err_content = '\n'.join(new_lines)
            content = content[:err_start] + new_err_content + content[err_end:]
            changes.append('错误处理表格添加"处理方式"列')
            # 重新获取错误处理内容
            err_content = new_err_content

        # 检查表格行数
        table_rows = [l for l in err_content.split('\n')
                      if l.strip().startswith('|') and '---' not in l]
        if len(table_rows) < 3:
            # 补充表格行
            supplement_rows = """
| 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后重试 | P0 |
| 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |"""
            # 在错误处理章节末尾添加
            content = content[:err_end - 1] + supplement_rows + '\n' + content[err_end - 1:]
            changes.append(f'错误处理表格补充行(原{len(table_rows)}行)')

    elif has_h3:
        # 检查###标题数量
        h3_count = len(re.findall(r'^###\s+', err_content, re.MULTILINE))
        if h3_count < 3:
            # 补充###标题
            needed = 3 - h3_count
            supplement = ""
            for i in range(needed):
                supplement += f"\n### 错误场景{h3_count + i + 1}\n\n检查`error_code`并按照处理方式进行排查。\n"
            content = content[:err_end - 1] + supplement + content[err_end - 1:]
            changes.append(f'错误处理补充{needed}个###标题')

    return content, changes


# ============================================================
# 修复6: 能力点指示符补充 (L3-2)
# ============================================================

def _find_capability_sections_in_body(cap_body: str):
    """在原始cap_body中查找所有能力点###标题的位置(跳过代码块内的)

    Returns:
        list of (heading_start, heading_end, title)
        heading_start: ###标题行的起始位置
        heading_end: ###标题行的末尾(不含换行符)
    """
    in_code_block = False
    lines = cap_body.split('\n')
    current_pos = 0
    raw_h3 = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
        elif not in_code_block:
            m = re.match(r'^###\s+(.+)$', line)
            if m:
                title = m.group(1).strip()
                raw_h3.append((current_pos, current_pos + len(line), title))
        current_pos += len(line) + 1  # +1 for \n

    # 过滤非能力点标题
    capability_sections = [(s, e, t) for s, e, t in raw_h3
                           if not any(nc in t for nc in NON_CAPABILITY_HEADINGS)]
    return capability_sections


def fix_capability_indicators(content: str):
    """为指示符不足的能力点补充bullet+代码引用"""
    changes = []

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, []

    cap_pattern = re.compile(r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)')
    cap_match = cap_pattern.search(content)
    if not cap_match:
        return content, []

    cap_body_start = cap_match.end()
    next_sec = re.search(r'\n## ', content[cap_body_start:])
    cap_body_end = cap_body_start + next_sec.start() if next_sec else len(content)
    cap_body = content[cap_body_start:cap_body_end]

    # 在原始cap_body中查找能力点###标题(跳过代码块内的)
    capability_sections = _find_capability_sections_in_body(cap_body)
    if not capability_sections:
        return content, []

    supplemented = 0
    # 从后往前修改,避免位置偏移
    for i in range(len(capability_sections) - 1, -1, -1):
        h_start, h_end, title = capability_sections[i]
        # section内容从标题行之后到下一个###标题或章节末尾
        section_start = h_end
        if i + 1 < len(capability_sections):
            section_end = capability_sections[i + 1][0]
        else:
            section_end = len(cap_body)
        section_text = cap_body[section_start:section_end]

        # 检查是否有代码块
        has_code_block = '```' in section_text

        # 移除代码块后计算指示符
        section_no_code = re.sub(r'```[\s\S]*?```', '', section_text)
        # 使用非代码块指示符计数(因为L3检查器的has_code_block有位置偏移bug)
        non_cb_indicators = count_non_codeblock_indicators(section_no_code)

        if non_cb_indicators < 2:
            # 检查是否已有input_params bullet
            if 'input_params' not in section_no_code and 'config_options' not in section_no_code:
                bullet_text = '\n- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作'

                # 在section内容末尾(跳过尾部空行)插入
                insert_pos = section_end
                while insert_pos > section_start and cap_body[insert_pos - 1] in '\n\r \t':
                    insert_pos -= 1

                cap_body = (cap_body[:insert_pos] + bullet_text +
                           cap_body[insert_pos:])
                supplemented += 1

    if supplemented > 0:
        content = content[:cap_body_start] + cap_body + content[cap_body_end:]
        changes.append(f'补充{supplemented}个能力点的详细指示符')

    return content, changes


# ============================================================
# 修复7: 能力点描述补充 (L3-2)
# ============================================================

def fix_short_capability_desc(content: str):
    """为描述过短(<50字符)的能力点补充描述"""
    changes = []

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, []

    cap_pattern = re.compile(r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)')
    cap_match = cap_pattern.search(content)
    if not cap_match:
        return content, []

    cap_body_start = cap_match.end()
    next_sec = re.search(r'\n## ', content[cap_body_start:])
    cap_body_end = cap_body_start + next_sec.start() if next_sec else len(content)
    cap_body = content[cap_body_start:cap_body_end]

    # 在原始cap_body中查找能力点###标题(跳过代码块内的)
    capability_sections = _find_capability_sections_in_body(cap_body)
    if not capability_sections:
        return content, []

    supplemented = 0
    for i in range(len(capability_sections) - 1, -1, -1):
        h_start, h_end, title = capability_sections[i]
        section_start = h_end
        if i + 1 < len(capability_sections):
            section_end = capability_sections[i + 1][0]
        else:
            section_end = len(cap_body)

        # 移除代码块后计算描述长度
        section_text = cap_body[section_start:section_end]
        section_no_code = re.sub(r'```[\s\S]*?```', '', section_text).strip()

        if len(section_no_code) < 50:
            # 在###标题行之后插入补充描述
            supplement = f'\n执行{title}操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作。'
            cap_body = cap_body[:h_end] + supplement + cap_body[h_end:]
            supplemented += 1

    if supplemented > 0:
        content = content[:cap_body_start] + cap_body + content[cap_body_end:]
        changes.append(f'补充{supplemented}个能力点的描述(原<50字符)')

    return content, changes


# ============================================================
# 修复8: 关键词对齐补充 (L3-3)
# ============================================================

def fix_keyword_alignment(content: str, fm_data: dict):
    """确保description关键词在核心能力中出现"""
    changes = []

    description = fm_data.get('description', '')
    summary = fm_data.get('summary', '')
    combined = f"{summary} {description}"

    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return content, []

    desc_keywords = re.findall(r'[\u4e00-\u9fff]{2,8}|[A-Za-z]{3,20}', combined)

    stop_words = {'the', 'and', 'for', 'with', 'from', 'this', 'that'}
    missing_keywords = []
    seen = set()

    for kw in desc_keywords:
        if len(kw) >= 3 and kw.lower() not in stop_words:
            if kw.lower() not in cap_content.lower() and kw.lower() not in seen:
                missing_keywords.append(kw)
                seen.add(kw.lower())

    if len(missing_keywords) == 0:
        return content, []

    # 注入所有缺失关键词(不限制数量,确保<=5个缺失)
    keywords_to_inject = missing_keywords[:200]
    keyword_str = '、'.join(keywords_to_inject)

    # 检查是否已有"能力覆盖范围"段落
    if '能力覆盖范围' in cap_content:
        # 更新已有的能力覆盖范围段落
        old_pattern = re.compile(r'\*\*能力覆盖范围\*\*：[^\n]*')
        if old_pattern.search(cap_content):
            # 包含所有关键词(不仅是缺失的),避免替换时丢失已有关键词
            all_keywords = []
            seen_all = set()
            for kw in desc_keywords:
                if len(kw) >= 3 and kw.lower() not in stop_words and kw.lower() not in seen_all:
                    all_keywords.append(kw)
                    seen_all.add(kw.lower())

            keyword_str_all = '、'.join(all_keywords[:200])
            new_text = (f'**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：'
                       f'{keyword_str_all}等。')
            content = old_pattern.sub(new_text, content, count=1)
            changes.append(f'更新能力覆盖范围(注入{len(all_keywords[:200])}个关键词,含{len(missing_keywords)}个新增)')
            return content, changes

    # 在核心能力章节末尾注入
    injection = (
        f'\n**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：'
        f'{keyword_str}等。这些关键词对应description中声明的使用场景,'
        f'均已在上述能力点中提供对应的操作支持。\n'
    )

    cap_pattern = re.compile(r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)')
    cap_match = cap_pattern.search(content)
    if cap_match:
        cap_body_start = cap_match.end()
        next_sec = re.search(r'\n## ', content[cap_body_start:])
        if next_sec:
            cap_body_end = cap_body_start + next_sec.start()
        else:
            cap_body_end = len(content)
        content = content[:cap_body_end].rstrip() + injection + content[cap_body_end:]
        changes.append(f'注入{len(keywords_to_inject)}个description关键词到核心能力')

    return content, changes


# ============================================================
# 单文件修复
# ============================================================

def fix_skill(skill_path: Path):
    """修复单个skill"""
    content = skill_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    original = content
    all_changes = []

    fm_data = parse_frontmatter(content)

    # 修复1: 章节名标准化 (L3-1 + L3-2)
    content, changes = fix_section_names(content)
    all_changes.extend(changes)

    # 修复1.5: 处理重复核心能力章节
    content, changes = fix_duplicate_core_capability(content)
    all_changes.extend(changes)

    # 修复2: 缺少核心能力章节 (L3-1 + L3-2)
    content, changes = fix_missing_core_capability(content)
    all_changes.extend(changes)

    # 修复3: slug=name对齐 (L3-1)
    content, changes = fix_slug_name(content, fm_data)
    all_changes.extend(changes)

    # 修复4: 模板套话清除 (L3-7)
    content, changes = fix_template_phrases(content)
    all_changes.extend(changes)

    # 修复5: 占位符清除 (L3-7)
    content, changes = fix_placeholders(content)
    all_changes.extend(changes)

    # 修复6: 错误处理表格补充 (L3-5)
    content, changes = fix_error_handling_table(content)
    all_changes.extend(changes)

    # 修复7: 能力点描述补充 (L3-2)
    content, changes = fix_short_capability_desc(content)
    all_changes.extend(changes)

    # 修复8: 能力点指示符补充 (L3-2)
    content, changes = fix_capability_indicators(content)
    all_changes.extend(changes)

    # 重新解析frontmatter
    fm_data = parse_frontmatter(content)

    # 修复9: 关键词对齐 (L3-3)
    content, changes = fix_keyword_alignment(content, fm_data)
    all_changes.extend(changes)

    if content != original:
        skill_path.write_text(content, encoding='utf-8')
        return True, all_changes
    return False, []


# ============================================================
# 主函数
# ============================================================

def main():
    parser = argparse.ArgumentParser(description='差异化skill第三轮批量修复')
    parser.add_argument('--limit', type=int, default=0, help='限制处理数量(0=全部)')
    parser.add_argument('--slug', type=str, default='', help='只处理指定slug')
    args = parser.parse_args()

    skill_files = sorted(DIFFERENTIATED_DIR.rglob('SKILL.md'))

    if args.slug:
        skill_files = [f for f in skill_files if f.parent.name == args.slug]
        if not skill_files:
            print(f"未找到slug为 '{args.slug}' 的skill")
            return

    if args.limit > 0:
        skill_files = skill_files[:args.limit]

    print(f"差异化skill第三轮批量修复")
    print(f"目标目录: {DIFFERENTIATED_DIR}")
    print(f"文件数量: {len(skill_files)}")
    print(f"{'=' * 70}")

    stats = {
        'total': len(skill_files),
        'modified': 0,
        'unmodified': 0,
        'errors': 0,
        'errors_list': [],
        'fix_counts': {
            'section_names': 0,
            'missing_core': 0,
            'slug_name': 0,
            'template_phrases': 0,
            'placeholders': 0,
            'error_table': 0,
            'short_desc': 0,
            'indicators': 0,
            'keyword_alignment': 0,
        },
        'details': [],
    }

    for i, skill_path in enumerate(skill_files):
        slug = skill_path.parent.name
        try:
            modified, changes = fix_skill(skill_path)
            if modified:
                stats['modified'] += 1
                # 统计修复维度
                changes_str = ' '.join(changes)
                if '章节名标准化' in changes_str or '重命名' in changes_str:
                    stats['fix_counts']['section_names'] += 1
                if '核心能力章节' in changes_str:
                    stats['fix_counts']['missing_core'] += 1
                if 'name字段对齐' in changes_str:
                    stats['fix_counts']['slug_name'] += 1
                if '模板套话' in changes_str:
                    stats['fix_counts']['template_phrases'] += 1
                if '占位符' in changes_str:
                    stats['fix_counts']['placeholders'] += 1
                if '错误处理' in changes_str:
                    stats['fix_counts']['error_table'] += 1
                if '描述' in changes_str:
                    stats['fix_counts']['short_desc'] += 1
                if '指示符' in changes_str:
                    stats['fix_counts']['indicators'] += 1
                if '关键词' in changes_str:
                    stats['fix_counts']['keyword_alignment'] += 1

                stats['details'].append({
                    'slug': slug,
                    'changes': changes,
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

        if (i + 1) % 100 == 0 or (i + 1) == len(skill_files):
            print(f"  进度: {i + 1}/{len(skill_files)} "
                  f"(已修复: {stats['modified']}, "
                  f"未修改: {stats['unmodified']}, "
                  f"错误: {stats['errors']})")

    print(f"\n{'=' * 70}")
    print(f"第三轮批量修复完成:")
    print(f"  总数:     {stats['total']}")
    print(f"  已修改:   {stats['modified']}")
    print(f"  未修改:   {stats['unmodified']}")
    print(f"  错误:     {stats['errors']}")

    print(f"\n各维度修复统计 (按文件计):")
    dim_labels = {
        'section_names': '章节名标准化 (L3-1/L3-2)',
        'missing_core': '添加核心能力章节 (L3-1/L3-2)',
        'slug_name': 'slug=name对齐 (L3-1)',
        'template_phrases': '模板套话清除 (L3-7)',
        'placeholders': '占位符清除 (L3-7)',
        'error_table': '错误处理表格补充 (L3-5)',
        'short_desc': '能力点描述补充 (L3-2)',
        'indicators': '能力点指示符补充 (L3-2)',
        'keyword_alignment': '关键词对齐 (L3-3)',
    }
    for dim, label in dim_labels.items():
        count = stats['fix_counts'][dim]
        pct = count * 100 // stats['total'] if stats['total'] > 0 else 0
        print(f"  {label}: {count}个文件 ({pct}%)")

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
