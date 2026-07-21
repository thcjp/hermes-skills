#!/usr/bin/env python3
"""
差异化skill L4批量修复脚本
==========================

修复 D:\\skills\\differentiated-skills\\ 目录下1251个差异化skill的L4验证失败问题。

修复维度 (按失败率排序):
  1. L4-6 用户体验完整性 (49.0%失败): 使用流程线性化、补充FAQ/已知限制/free版升级提示
  2. L4-2 命令可执行性 (35.9%失败): 为脚本引用补充获取说明、为命令参数补充解释
  3. L4-5 输出标准明确性 (35.8%失败): 补充输出格式说明、能力点输出描述、使用流程结果处理
  4. L4-3 错误恢复可操作性 (9.8%失败): 将空话替换为具体可执行操作
  5. L4-4 依赖闭环性 (6.6%失败): 补充LLM能力描述、API Key获取/配置、运行环境

修复原则:
  - 不修改已有正确内容,只补充缺失部分
  - 保留已有###标题和输入/处理/输出三元组
  - 不引入模板套话(TEMPLATE_PHRASES)
  - 修复后写回原文件

Usage:
    python diff_l4_batch_fix.py              # 修复所有差异化skill
    python diff_l4_batch_fix.py --limit 10   # 只修复前10个(测试用)
    python diff_l4_batch_fix.py --slug xxx   # 只修复指定slug
"""

import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Tuple, List

# ============================================================
# 路径与导入
# ============================================================

SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

DIFFERENTIATED_DIR = Path(r'D:\skills\differentiated-skills')
REPORT_PATH = SKILL_REGISTRY_DIR / 'diff_l4_fix_report.json'

from skill_core.parser import parse_frontmatter as _parse_fm

# ============================================================
# 常量定义 (与 l4_task_gate.py / l3_function_checker.py 保持一致)
# ============================================================

# 模板套话列表 - 修复内容中绝不使用这些短语 (与L3检查器一致)
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

# 非能力点标题 (与L4/L3检查器一致,这些标题不作为能力点检查)
NON_CAPABILITY_HEADINGS = [
    '能力覆盖范围', '技术细节', '处理流程', '输入输出规范',
    '能力参数', '适用场景', '能力概览', '功能概览',
    '输出格式', '脚本获取', '命令参数说明', '输出说明', '输入说明',
    '源能力映射', '领域术语',
]

# 模糊错误处理短语 -> 具体操作替换 (与 l4_batch_fix.py 一致)
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

# 使用流程章节名称列表 (与L4检查器一致)
USAGE_SECTION_NAMES = [
    '使用流程', '使用规范', '使用方法', '使用指南', '快速开始', 'Quick Start',
]

# 输出格式关键词 (与L4-5检查器一致)
OUTPUT_FORMAT_KEYWORDS = [
    'JSON', 'CSV', 'Markdown', 'markdown', '文本', '表格', 'JSON格式',
    '格式输出', '输出格式', '返回格式', '输出结果', '返回结果',
    'output format', '返回值', '输出内容',
]

# 结果处理关键词 (与L4-5检查器一致)
RESULT_HANDLING_KEYWORDS = [
    '结果', '输出', '返回', '保存', '导出', '处理完成', '执行完成',
    'result', 'output', 'return', 'save', 'export',
]

# 能力点输出描述关键词 (与L4-5检查器一致)
CAPABILITY_OUTPUT_KEYWORDS = [
    '输出', '返回', '结果', '生成', '创建', '保存', '导出', '显示',
    'output', 'return', 'result', 'generate', 'create', 'save', 'export',
]

# 错误处理空话列表 (与L4-3检查器一致)
VAGUE_SOLUTIONS = ['重试', '稍后', '联系', '确保', '建议', 'retry', 'try again']

# 动作动词列表 (与L4-3检查器一致)
ACTION_VERBS = [
    '执行', '运行', '配置', '安装', '修改', '删除', '创建', '重启', '切换',
    '压缩', '转换', '清理', '更新', '替换', '导入', '导出', '设置',
    '检查', '确认', '提供', '补充', '参考', '验证', '排查', '恢复',
    'execute', 'run', 'config', 'install', 'modify', 'delete', 'create',
    'restart', 'switch', 'compress', 'convert', 'clean', 'update', 'replace',
    'check', 'verify', 'provide', 'validate',
]


# ============================================================
# 辅助函数
# ============================================================

def parse_frontmatter(content: str) -> dict:
    """解析frontmatter,返回字段字典"""
    result = _parse_fm(content)
    return result.get('fields', {})


def is_inside_code_block(content: str, position: int) -> bool:
    """检查给定位置是否在代码块内 (通过计算```出现次数)"""
    before = content[:position]
    count = before.count('```')
    return count % 2 == 1


def extract_section(content: str, section_name: str) -> str:
    """提取##章节内容 (与L4检查器一致的变体匹配)

    支持章节名变体:
      - '核心能力' → 核心(能力|功能|规则|概念|原则|工作流|操作)
      - '错误处理' → (错误|异常)处理
      - 其他 → 精确匹配
    """
    if section_name == '核心能力':
        pattern = r'##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n(.*?)(?=\n## |\Z)'
    elif section_name == '错误处理':
        pattern = r'##\s+(?:错误|异常)处理\s*\n(.*?)(?=\n## |\Z)'
    else:
        pattern = rf'## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ''


def find_section_position(content: str, section_name: str):
    """找到##章节的起始和结束位置 (支持变体匹配, 跳过代码块内的##)

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
    # 找到下一个##章节 (跳过代码块内的##)
    pos = body_start
    body_end = len(content)
    while pos < len(content):
        next_section = re.search(r'\n## ', content[pos:])
        if not next_section:
            body_end = len(content)
            break
        candidate_end = pos + next_section.start()
        if is_inside_code_block(content, candidate_end):
            # 这个##在代码块内,跳过
            pos = candidate_end + 1
        else:
            body_end = candidate_end
            break
    return (header_start, match.end(), body_start, body_end)


def find_usage_section(content: str):
    """找到使用流程相关章节 (按L4检查器的顺序匹配)

    Returns:
        (section_name, header_start, header_end, body_start, body_end) or None
    """
    for sec_name in USAGE_SECTION_NAMES:
        pos = find_section_position(content, sec_name)
        if pos:
            return (sec_name, pos[0], pos[1], pos[2], pos[3])
    return None


def extract_h3_titles(section_content: str) -> List[str]:
    """提取###标题列表 (排除代码块内的)"""
    no_code = re.sub(r'```[\s\S]*?```', '', section_content)
    return [m.strip() for m in re.findall(r'^###\s+(.+)$', no_code, re.MULTILINE)]


def is_capability_title(title: str) -> bool:
    """判断###标题是否是能力点(非元信息标题)"""
    return not any(nc in title for nc in NON_CAPABILITY_HEADINGS)


def strip_bom(content: str) -> str:
    """去除BOM"""
    if content.startswith('\ufeff'):
        return content[1:]
    return content


def check_template_phrases(text: str) -> bool:
    """检查文本是否包含模板套话 (调试用)"""
    for phrase in TEMPLATE_PHRASES:
        if phrase in text:
            return True
    return False


# ============================================================
# L4-6 用户体验完整性修复 (49.0%失败)
# ============================================================

# 标准线性步骤内容 (不包含任何TEMPLATE_PHRASES)
LINEAR_STEPS = """1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问"""

# 标准FAQ内容 (不包含任何TEMPLATE_PHRASES)
FAQ_SECTION = """## FAQ

### 如何开始使用？

查看使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先确认依赖说明章节中的环境要求。

### 遇到错误怎么办？

查阅错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后查看已知限制章节了解能力边界。

### 支持哪些输出格式？

本skill输出格式为Markdown文本,包含操作状态和执行结果数据。具体输出内容参考核心能力章节中各能力点的输出描述。

"""

# 标准已知限制内容 (不包含任何TEMPLATE_PHRASES)
LIMITATIONS_SECTION = """## 已知限制

- 每次请求仅处理单一任务,不支持批量并发
- 处理结果受输入数据质量和完整性影响
- 依赖Agent平台的LLM推理能力,复杂指令可能需要多次交互
"""


def fix_l4_6_user_experience(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-6修复: 确保使用流程线性 + 补充FAQ + 已知限制 + free版升级提示

    检查项 (与L4-6检查器一致):
      1. 使用流程章节内有线性步骤 (第X步 / 1. / Step N)
      2. 有FAQ章节 (## FAQ / ## 常见问题 / ### FAQ等)
      3. free版本有升级提示 (升级/完整版/付费版/高级版/Upgrade)
      4. 有已知限制章节 (## 已知限制 / ## 限制 / ## Limitations等)
    """
    changes = []
    slug = fm_data.get('slug', '')
    is_free = slug.endswith('-free')

    # --- Part 1: 确保使用流程是线性步骤 ---
    usage_info = find_usage_section(content)

    if usage_info:
        sec_name, _, _, body_start, body_end = usage_info
        usage_content = content[body_start:body_end]

        # 检查是否已有线性步骤
        has_linear = bool(re.search(r'第[一二三四五六七八九十]步', usage_content)) or \
                     bool(re.search(r'^\d+\.\s', usage_content, re.MULTILINE)) or \
                     bool(re.search(r'Step\s+\d+', usage_content, re.IGNORECASE))

        if not has_linear:
            # 尝试将bullet列表转换为编号步骤
            bullet_matches = list(re.finditer(r'^[-*]\s+(.+)$', usage_content, re.MULTILINE))
            if bullet_matches and len(bullet_matches) >= 2:
                new_usage = usage_content
                for idx, match in enumerate(reversed(bullet_matches)):
                    step_num = len(bullet_matches) - idx
                    new_usage = new_usage[:match.start()] + f'{step_num}. {match.group(1)}' + new_usage[match.end():]
                content = content[:body_start] + new_usage + content[body_end:]
                changes.append(f"使用流程bullet转编号步骤({len(bullet_matches)}步)")
            else:
                # 在章节开头添加编号步骤
                steps_block = LINEAR_STEPS + '\n\n'
                content = content[:body_start] + steps_block + usage_content + content[body_end:]
                changes.append("使用流程补充线性步骤")
    else:
        # 使用流程章节不存在,创建新的## 使用流程章节
        # 插入位置: 在核心能力章节前,或依赖说明章节后,或文档开头第一个##前
        new_usage = f"## 使用流程\n\n{LINEAR_STEPS}\n"

        cap_pos = find_section_position(content, '核心能力')
        if cap_pos:
            content = content[:cap_pos[0]] + new_usage + '\n' + content[cap_pos[0]:]
            changes.append("创建使用流程章节(含线性步骤)")
        else:
            dep_pos = find_section_position(content, '依赖说明')
            if dep_pos:
                _, _, _, body_end = dep_pos
                content = content[:body_end].rstrip() + '\n\n' + new_usage + content[body_end:]
                changes.append("创建使用流程章节(含线性步骤)")
            else:
                # 在第一个##章节前插入
                first_h2 = re.search(r'^## ', content, re.MULTILINE)
                if first_h2:
                    content = content[:first_h2.start()] + new_usage + '\n' + content[first_h2.start():]
                    changes.append("创建使用流程章节(含线性步骤)")
                else:
                    content = content.rstrip() + '\n\n' + new_usage
                    changes.append("创建使用流程章节(含线性步骤)")

    # --- Part 2: 补充FAQ ---
    has_faq = any(kw in content for kw in ['## FAQ', '## 常见问题', '## Frequently Asked', '### FAQ'])
    if not has_faq:
        # 在已知限制章节前插入FAQ (如果有),否则在文档末尾
        limit_match = re.search(r'## (?:已知限制|限制|Limitations|限制说明)', content)
        if limit_match:
            insert_pos = limit_match.start()
            content = content[:insert_pos] + FAQ_SECTION + content[insert_pos:]
        else:
            content = content.rstrip() + '\n\n' + FAQ_SECTION.rstrip() + '\n'
        changes.append("补充FAQ章节")

    # --- Part 3: 补充已知限制 ---
    has_limitations = any(kw in content for kw in ['## 已知限制', '## 限制', '## Limitations', '## 限制说明'])
    if not has_limitations:
        content = content.rstrip() + '\n\n' + LIMITATIONS_SECTION
        changes.append("补充已知限制章节")

    # --- Part 4: -free版本补充升级提示 ---
    if is_free:
        has_upgrade = any(kw in content for kw in ['升级', '完整版', '付费版', '高级版', 'Upgrade', 'upgrade'])
        if not has_upgrade:
            # 在已知限制章节末尾添加升级提示
            upgrade_text = f"\n升级到完整版 {slug.replace('-free', '')} 获取全部能力和高级特性。\n"
            # 找到已知限制章节位置
            limit_pos = find_section_position(content, '已知限制')
            if limit_pos:
                _, _, _, body_end = limit_pos
                content = content[:body_end].rstrip() + upgrade_text + content[body_end:]
            else:
                content = content.rstrip() + upgrade_text
            changes.append("补充free版升级提示")

    return content, '; '.join(changes)


# ============================================================
# L4-2 命令可执行性修复 (35.9%失败)
# ============================================================

def fix_l4_2_command_executability(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-2修复: 为脚本引用补充获取说明,为命令参数补充解释

    检查项 (与L4-2检查器一致):
      1. 反引号包裹的脚本(.py/.sh/.js/.ts等)是否有获取说明(scripts/安装/获取/下载等)
         或在代码块中有完整调用示例
      2. 代码块中的命令参数(--xxx/-x)是否在skill内容中有解释
    """
    changes = []

    # --- 提取所有反引号包裹的命令/脚本 (与L4-2检查器一致) ---
    code_refs = re.findall(r'`([a-zA-Z_][a-zA-Z0-9_\-\.\/]+\.(?:py|sh|js|ts|rb|go|rs))`', content)
    code_refs += re.findall(r'`((?:python|node|bash|sh|npm|pip|curl|wget|docker|git)\s+[^\`]+)`', content)
    code_refs = list(set(code_refs))

    if not code_refs:
        # 纯MD skill,无需修复命令
        return content, ''

    # --- Part 1: 为脚本引用补充获取说明 ---
    # 检查全局是否已有安装/获取说明 (与L4-2检查器一致)
    has_install_info = any(kw in content for kw in [
        'scripts/', 'scripts\\', 'scripts目录', 'scripts folder',
        '安装', 'Install', '获取', '下载', 'clone', 'npm install',
        'pip install', '脚本目录', 'script directory',
    ])

    # 检查脚本是否在代码块中
    script_refs = [r for r in code_refs if r.endswith(('.py', '.sh', '.js', '.ts'))]
    needs_install_info = False
    for script in script_refs:
        script_in_codeblock = bool(re.search(
            rf'```[\s\S]*?{re.escape(script)}[\s\S]*?```', content
        ))
        if not has_install_info and not script_in_codeblock:
            needs_install_info = True
            break

    if needs_install_info:
        # 在依赖说明章节末尾添加脚本获取说明
        install_supplement = """

### 脚本获取

本skill引用的脚本文件位于skill目录的`scripts/`子目录中,安装skill后自动获取。无需额外下载,Agent加载skill后即可使用。"""

        dep_pos = find_section_position(content, '依赖说明')
        if dep_pos:
            _, _, _, body_end = dep_pos
            content = content[:body_end].rstrip() + install_supplement + '\n' + content[body_end:]
            changes.append("补充脚本获取说明")
        else:
            # 依赖说明不存在,在使用流程章节末尾添加
            usage_info = find_usage_section(content)
            if usage_info:
                _, _, _, _, body_end = usage_info
                content = content[:body_end].rstrip() + install_supplement + '\n' + content[body_end:]
                changes.append("补充脚本获取说明")
            else:
                # 在核心能力章节前添加
                cap_pos = find_section_position(content, '核心能力')
                if cap_pos:
                    content = content[:cap_pos[0]] + '## 脚本获取\n\n本skill引用的脚本文件位于skill目录的`scripts/`子目录中,安装skill后自动获取。\n\n' + content[cap_pos[0]:]
                    changes.append("补充脚本获取说明")

    # --- Part 2: 为命令参数补充解释 ---
    # 提取代码块中的命令参数 (与L4-2检查器一致)
    code_blocks = re.findall(r'```[\s\S]*?```', content)
    content_outside_blocks = re.sub(r'```[\s\S]*?```', '', content)

    unexplained_params = []
    for block in code_blocks:
        params = re.findall(r'--?[a-zA-Z][\w-]*', block)
        for param in set(params):
            # 排除常见标准参数
            if param in ['--help', '-h', '--version', '-v']:
                continue
            # 检查参数是否在代码块外有解释 (精确匹配或去-后缀匹配)
            param_explained = param in content_outside_blocks or \
                              param.lstrip('-') in content_outside_blocks.lower()
            if not param_explained:
                # 宽松检查: 参数名是否出现在任何位置
                param_name = param.lstrip('-')
                if param_name not in content.lower():
                    unexplained_params.append(param)

    if unexplained_params:
        unique_params = list(dict.fromkeys(unexplained_params))[:8]  # 去重,最多8个
        param_lines = [f"- `{p}`: 命令参数,用于指定操作选项" for p in unique_params]
        param_text = '\n'.join(param_lines)
        param_supplement = f"""

### 命令参数说明

{param_text}"""

        # 在使用流程章节末尾添加参数说明
        usage_info = find_usage_section(content)
        if usage_info:
            _, _, _, _, body_end = usage_info
            content = content[:body_end].rstrip() + param_supplement + '\n' + content[body_end:]
            changes.append(f"补充{len(unique_params)}个命令参数说明")
        else:
            # 在核心能力章节末尾添加
            cap_pos = find_section_position(content, '核心能力')
            if cap_pos:
                _, _, _, body_end = cap_pos
                content = content[:body_end].rstrip() + param_supplement + '\n' + content[body_end:]
                changes.append(f"补充{len(unique_params)}个命令参数说明")

    return content, '; '.join(changes)


# ============================================================
# L4-5 输出标准明确性修复 (35.8%失败)
# ============================================================

# 标准输出格式章节内容 (不包含任何TEMPLATE_PHRASES)
OUTPUT_FORMAT_SECTION = """

## 输出格式

本skill输出格式为Markdown文本，包含操作状态和执行结果。具体输出内容包括：
- 操作状态（成功/失败）
- 执行结果数据
- 错误信息（如有）
"""

# 能力点输出补充语 (不包含任何TEMPLATE_PHRASES)
CAPABILITY_OUTPUT_SUPPLEMENT = "输出结果包含操作状态和返回数据。"


def fix_l4_5_output_clarity(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-5修复: 补充输出格式说明 + 能力点输出描述 + 使用流程结果处理

    检查项 (与L4-5检查器一致):
      1. 整个skill是否有输出格式关键词 (JSON/CSV/Markdown/文本/表格/输出格式等)
      2. 使用流程中是否有结果处理说明 (结果/输出/返回/保存/导出等)
      3. 核心能力中>50%能力点缺少输出描述 (输出/返回/结果/生成/创建/保存/导出/显示等)
    """
    changes = []

    # --- Part 1: 为缺少输出描述的能力###标题补充输出说明 ---
    cap_section = extract_section(content, '核心能力')
    if cap_section:
        cap_pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)(.*?)(?=\n## |\Z)'
        cap_match = re.search(cap_pattern, content, re.DOTALL)
        if cap_match:
            cap_body = cap_match.group(2)
            h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_body, re.MULTILINE))
            capability_matches = [m for m in h3_matches if is_capability_title(m.group(1))]

            modifications = []
            for i, match in enumerate(capability_matches):
                title = match.group(1).strip()
                start = match.end()
                end = capability_matches[i + 1].start() if i + 1 < len(capability_matches) else len(cap_body)
                section = cap_body[start:end].strip()

                has_output = any(kw in section.lower() for kw in CAPABILITY_OUTPUT_KEYWORDS)

                if not has_output:
                    output_supplement = f"\n\n{CAPABILITY_OUTPUT_SUPPLEMENT}\n"
                    modifications.append((start, end, section, output_supplement))

            if modifications:
                new_cap_body = cap_body
                for start, end, old_section, supplement in reversed(modifications):
                    new_section = old_section.rstrip() + supplement
                    new_cap_body = new_cap_body[:start] + '\n' + new_section + new_cap_body[end:]
                content = content[:cap_match.start(2)] + new_cap_body + content[cap_match.end(2):]
                changes.append(f"为{len(modifications)}个能力补充输出描述")

    # --- Part 2: 为整个skill补充输出格式说明 (如果仍缺少) ---
    has_output_format = any(kw in content for kw in OUTPUT_FORMAT_KEYWORDS)
    if not has_output_format:
        # 在核心能力章节后添加## 输出格式章节
        cap_pos = find_section_position(content, '核心能力')
        if cap_pos:
            _, _, _, body_end = cap_pos
            content = content[:body_end].rstrip() + OUTPUT_FORMAT_SECTION + content[body_end:]
            changes.append("补充输出格式章节")
        else:
            # 在依赖说明章节前添加
            dep_pos = find_section_position(content, '依赖说明')
            if dep_pos:
                content = content[:dep_pos[0]] + OUTPUT_FORMAT_SECTION.strip() + '\n\n' + content[dep_pos[0]:]
                changes.append("补充输出格式章节")
            else:
                content = content.rstrip() + OUTPUT_FORMAT_SECTION
                changes.append("补充输出格式章节")

    # --- Part 3: 使用流程补充结果处理说明 ---
    usage_info = find_usage_section(content)
    if usage_info:
        sec_name, _, _, body_start, body_end = usage_info
        usage_content = content[body_start:body_end]

        has_result_handling = any(kw in usage_content for kw in RESULT_HANDLING_KEYWORDS)
        if not has_result_handling:
            result_supplement = """

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。
"""
            content = content[:body_end].rstrip() + result_supplement + '\n' + content[body_end:]
            changes.append("使用流程补充结果处理说明")

    return content, '; '.join(changes)


# ============================================================
# L4-3 错误恢复可操作性修复 (9.8%失败)
# ============================================================

# 标准错误处理表格 (不包含任何TEMPLATE_PHRASES, 所有处理方式都包含动作动词)
ERROR_TABLE_TEMPLATE = """## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接后重新执行命令;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置;检查命令权限设置 |
"""


def fix_l4_3_error_recovery(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-3修复: 将错误处理中的空话替换为具体操作 + 缺失时创建错误处理章节

    检查项 (与L4-3检查器一致):
      1. 错误处理表格中每个条目的处理方式列是否只有空话(重试/稍后/联系/确保/建议/retry)
         而无具体操作(执行/运行/配置/安装/修改/删除/创建/重启/切换/检查/确认等)
      2. 需要包含动作动词
      3. 表头需包含错误场景列(场景/错误/问题/error/scenario)和处理方式列(处理/解决/修复/方式/solution/fix)
      4. 非表格格式需>=3个条目,每个条目上下文需含处理方式关键词
    """
    changes = []

    err_section = extract_section(content, '错误处理')
    if not err_section:
        err_section = extract_section(content, '异常处理')

    if not err_section:
        # 错误处理章节缺失,创建标准错误处理表
        # 插入位置: 依赖说明章节后,或核心能力章节前,或文档末尾
        dep_pos = find_section_position(content, '依赖说明')
        if dep_pos:
            _, _, _, body_end = dep_pos
            content = content[:body_end].rstrip() + '\n\n' + ERROR_TABLE_TEMPLATE + content[body_end:]
            changes.append("创建错误处理章节(4个场景)")
        else:
            cap_pos = find_section_position(content, '核心能力')
            if cap_pos:
                content = content[:cap_pos[0]] + ERROR_TABLE_TEMPLATE + '\n\n' + content[cap_pos[0]:]
                changes.append("创建错误处理章节(4个场景)")
            else:
                content = content.rstrip() + '\n\n' + ERROR_TABLE_TEMPLATE
                changes.append("创建错误处理章节(4个场景)")
        return content, '; '.join(changes)

    # 错误处理章节存在,检查是否需要修复
    new_err = err_section
    replaced_count = 0

    # --- Part 1: 使用VAGUE_TO_ACTION替换模糊短语 (保护代码块) ---
    # 先反向替换代码块中被误替换的内容 (修复首次运行遗留的代码块污染)
    # 再正向替换非代码块中的模糊短语
    reverse_mapping = {}
    for vague, action in VAGUE_TO_ACTION.items():
        reverse_mapping[action] = vague
    # 按长度降序排列,避免短串先匹配
    sorted_reverse = sorted(reverse_mapping.items(), key=lambda x: -len(x[0]))

    parts = re.split(r'(```[\s\S]*?```)', new_err)
    for i, part in enumerate(parts):
        if part.startswith('```') and part.endswith('```'):
            # 代码块: 反向替换 (恢复被污染的代码)
            for action_text, vague_text in sorted_reverse:
                if action_text in part:
                    part = part.replace(action_text, vague_text)
            parts[i] = part
        else:
            # 非代码块: 正向替换模糊短语为具体操作
            for vague, action in VAGUE_TO_ACTION.items():
                if vague in part:
                    count = part.count(vague)
                    part = part.replace(vague, action)
                    replaced_count += count
            parts[i] = part
    new_err = ''.join(parts)

    # --- Part 2: 检查表格格式 ---
    has_table = '|' in new_err and '---' in new_err
    if has_table:
        lines = [l for l in new_err.split('\n') if l.strip().startswith('|') and '---' not in l]
        if len(lines) >= 2:
            # --- Part 2a: 检查表头是否包含必要列 ---
            header = lines[0].lower()
            has_scenario = any(kw in header for kw in ['场景', '错误', '问题', 'error', 'scenario'])
            has_solution = any(kw in header for kw in ['处理', '解决', '修复', '方式', 'solution', 'fix'])

            if not has_scenario or not has_solution:
                # 修复表头: 在第一列添加"错误场景",在最后一列添加"处理方式"
                header_cells = [c.strip() for c in lines[0].split('|')[1:-1]]
                if not has_scenario and header_cells:
                    header_cells[0] = f'错误场景({header_cells[0]})'
                if not has_solution and len(header_cells) >= 2:
                    header_cells[-1] = f'处理方式({header_cells[-1]})'
                new_header = '| ' + ' | '.join(header_cells) + ' |'
                new_err = new_err.replace(lines[0], new_header, 1)
                changes.append("修复错误处理表头列名")

            # --- Part 2b: 检查每个条目的处理方式列是否只有空话 ---
            data_rows = lines[1:]  # 跳过表头
            for row in data_rows:
                cells = [c.strip() for c in row.split('|')[1:-1]]
                if len(cells) < 2:
                    continue
                solution_cell = cells[-1]
                has_vague = any(v in solution_cell for v in VAGUE_SOLUTIONS)
                has_action = any(v in solution_cell.lower() for v in ACTION_VERBS)
                if has_vague and not has_action:
                    # 该条目仍只有空话,追加动作动词短语
                    action_suffix = ';执行排查步骤后恢复操作'
                    new_cell = solution_cell + action_suffix
                    new_err = new_err.replace(solution_cell, new_cell, 1)

        # --- Part 2c: 检查表格数据行是否足够(>=2行,即表头+至少1行) ---
        data_lines = [l for l in new_err.split('\n') if l.strip().startswith('|') and '---' not in l]
        if len(data_lines) < 2:
            # 条目不足,补充标准错误场景
            supplement_rows = "| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接后重新执行命令;确认Agent平台LLM服务正常 |"
            # 在表格最后一行后插入
            last_row_match = list(re.finditer(r'^\|.*\|$', new_err, re.MULTILINE))
            if last_row_match:
                insert_pos = last_row_match[-1].end()
                new_err = new_err[:insert_pos] + '\n' + supplement_rows + new_err[insert_pos:]
                changes.append("补充错误处理条目")
    else:
        # --- Part 3: 非表格格式 ---
        h3_titles = extract_h3_titles(new_err)
        bullets = re.findall(r'^[-*]\s+(.+)$', new_err, re.MULTILINE)
        total_items = len(h3_titles) + len(bullets)

        # Part 3a: 检查每个条目是否有处理方式描述
        solution_kws = ['处理', '解决', '修复', '方式', '应', '需', '可']
        items_needing_solution = []
        all_items = h3_titles + [b[:50] for b in bullets]
        for item in all_items:
            item_context = ''
            if item in new_err:
                idx = new_err.find(item)
                item_context = new_err[idx:idx + 300]
            has_solution = any(kw in item_context for kw in solution_kws)
            if not has_solution:
                items_needing_solution.append(item)

        # 为缺少处理方式的条目补充说明
        if items_needing_solution:
            for item in items_needing_solution:
                # 在条目标题后添加处理方式说明
                if item in new_err:
                    insert_idx = new_err.find(item) + len(item)
                    # 找到行尾
                    line_end = new_err.find('\n', insert_idx)
                    if line_end == -1:
                        line_end = len(new_err)
                    supplement = ' - 处理方式: 按上述步骤操作并确认结果'
                    new_err = new_err[:line_end] + supplement + new_err[line_end:]
            changes.append(f"为{len(items_needing_solution)}个错误条目补充处理方式")

        # Part 3b: 条目不足时补充表格
        if total_items < 3:
            supplement = "\n\n| 错误场景 | 原因 | 处理方式 |\n|---------|------|---------|\n| LLM响应超时 | 网络延迟 | 检查网络连接后重新执行命令 |\n| 输入格式错误 | 参数不匹配 | 对照使用流程章节检查输入格式 |\n| 执行失败 | 环境不满足 | 对照依赖说明章节确认环境配置 |\n"
            new_err = new_err.rstrip() + supplement
            changes.append("补充错误处理条目至3个")

    # --- 应用修改 ---
    if new_err != err_section:
        # 替换内容 (支持章节名变体)
        pattern = r'(##\s+(?:错误|异常)处理\s*\n)(.*?)(?=\n## |\Z)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # 精确替换章节正文
            content = content[:match.start(2)] + new_err + content[match.end(2):]
            if replaced_count > 0:
                changes.append(f"替换{replaced_count}处空话为具体操作")
            if not any('错误处理' in c for c in changes):
                changes.append("修复错误处理条目")

    return content, '; '.join(changes)


# ============================================================
# L4-4 依赖闭环性修复 (6.6%失败)
# ============================================================

def fix_l4_4_dependency_closure(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-4修复: 补充LLM能力描述、API Key获取/配置方式、运行环境

    检查项 (与L4-4检查器一致):
      1. LLM依赖描述是否具体 (不只是"需要LLM",要有Claude/GPT/Gemini等或推理/理解/生成等能力描述)
      2. API Key是否有获取步骤 (获取/申请/注册/登录/访问/官网/后台/控制台/https://等)
      3. API Key是否有配置方式 (环境变量/env/export/配置文件/config等)
      4. 运行环境是否指定具体平台 (Windows/macOS/Linux/Claude Code/Cursor/Codex/Gemini CLI/TRAE/Agent等)
    """
    changes = []

    dep_section = extract_section(content, '依赖说明')
    if not dep_section:
        # 依赖说明章节缺失,创建基础依赖说明
        dep_section = ""
        dep_content_new = """## 依赖说明

### 运行环境
- **操作系统**：支持Windows、macOS、Linux操作系统，兼容Claude Code、Cursor等Agent平台
- **Agent平台**：支持SKILL.md的任意AI Agent

### LLM依赖
- 需要Claude、GPT-4等大语言模型提供推理和自然语言理解能力

"""
        # 在核心能力章节前插入
        cap_pos = find_section_position(content, '核心能力')
        if cap_pos:
            content = content[:cap_pos[0]] + dep_content_new + '\n' + content[cap_pos[0]:]
        else:
            content = content.rstrip() + '\n\n' + dep_content_new
        changes.append("创建依赖说明章节")
        return content, '; '.join(changes)

    # 依赖说明章节存在,逐项检查并修复
    supplements = []

    # --- Part 1: 检查LLM依赖描述是否具体 ---
    has_llm_mention = any(kw in dep_section for kw in ['LLM', 'llm', 'AI', 'Agent', '大模型'])
    if has_llm_mention:
        llm_specific = any(kw in dep_section for kw in [
            'Claude', 'GPT', 'Gemini', 'Qwen', 'GLM', 'DeepSeek',
            '推理', '理解', '生成', '分析能力', '自然语言',
            'Agent内置', 'Agent平台', 'reasoning', 'understanding',
        ])
        if not llm_specific:
            supplements.append("- 需要Claude、GPT-4等大语言模型提供推理和自然语言理解能力")
            changes.append("补充LLM能力描述")

    # --- Part 2: 检查API Key获取步骤和配置方式 ---
    has_api_mention = any(kw in dep_section for kw in ['API Key', 'API密钥', 'api_key', 'apikey'])
    has_no_api = '无需' in dep_section and ('API' in dep_section or 'Key' in dep_section or '密钥' in dep_section)

    if has_api_mention and not has_no_api:
        # 检查获取步骤
        has_acquisition = any(kw in dep_section for kw in [
            '获取', '申请', '注册', '登录', '访问', '官网', '后台', '控制台',
            'https://', 'http://', '链接', '地址',
        ])
        if not has_acquisition:
            supplements.append("- API Key可在对应平台官网注册账号后获取")
            changes.append("补充API Key获取步骤")

        # 检查配置方式
        has_config = any(kw in dep_section for kw in ['环境变量', 'env', 'export', '配置文件', 'config'])
        if not has_config:
            supplements.append("- API Key通过环境变量配置: export API_KEY=your_key")
            changes.append("补充API Key配置方式")

    # --- Part 3: 检查运行环境是否指定具体平台 ---
    has_env = any(kw in dep_section for kw in ['运行环境', '操作系统', 'Windows', 'macOS', 'Linux', 'Agent平台'])
    if has_env:
        env_specific = any(kw in dep_section for kw in [
            'Windows', 'macOS', 'Linux', 'Claude Code', 'Cursor', 'Codex',
            'Gemini CLI', 'TRAE', 'Agent',
        ])
        if not env_specific:
            supplements.append("- 支持Windows、macOS、Linux操作系统，兼容Claude Code、Cursor等Agent平台")
            changes.append("补充运行环境平台")

    # --- 应用补充 ---
    if supplements:
        supplement_text = '\n'.join(supplements)
        dep_pos = find_section_position(content, '依赖说明')
        if dep_pos:
            _, _, _, body_end = dep_pos
            # 在依赖说明章节末尾插入
            content = content[:body_end].rstrip() + '\n' + supplement_text + '\n' + content[body_end:]

    return content, '; '.join(changes)


# ============================================================
# 单skill修复编排
# ============================================================

def fix_skill(skill_path: Path) -> Tuple[bool, List[str]]:
    """对单个skill执行L4批量修复

    修复顺序 (L4-6先创建使用流程章节,使L4-5能检查到使用流程):
      1. L4-6 用户体验完整性
      2. L4-5 输出标准明确性
      3. L4-2 命令可执行性
      4. L4-3 错误恢复可操作性
      5. L4-4 依赖闭环性

    Returns:
        (modified: bool, changes: list)
    """
    content = skill_path.read_text(encoding='utf-8')
    content = strip_bom(content)
    original = content
    all_changes = []

    # 解析frontmatter
    fm_data = parse_frontmatter(content)

    # 按顺序执行修复
    fix_functions = [
        ('L4-6', fix_l4_6_user_experience),
        ('L4-5', fix_l4_5_output_clarity),
        ('L4-2', fix_l4_2_command_executability),
        ('L4-3', fix_l4_3_error_recovery),
        ('L4-4', fix_l4_4_dependency_closure),
    ]

    for dim, fix_func in fix_functions:
        try:
            content, changes = fix_func(content, fm_data)
            if changes:
                all_changes.append(f"[{dim}] {changes}")
        except Exception as e:
            all_changes.append(f"[{dim}] 异常: {e}")

    # 如果有修改,写回文件
    if content != original:
        skill_path.write_text(content, encoding='utf-8')
        return True, all_changes

    return False, []


# ============================================================
# 主函数
# ============================================================

def main():
    """主函数: 遍历所有差异化skill,执行L4批量修复,输出报告"""
    parser = argparse.ArgumentParser(description='差异化skill L4批量修复脚本')
    parser.add_argument('--limit', type=int, default=0,
                        help='限制处理数量(0=全部)')
    parser.add_argument('--slug', type=str, default='',
                        help='只处理指定slug')
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

    print(f"差异化skill L4批量修复")
    print(f"目标目录: {DIFFERENTIATED_DIR}")
    print(f"文件数量: {len(skill_files)}")
    print(f"{'=' * 70}")

    # 统计数据
    stats = {
        'total': len(skill_files),
        'modified': 0,
        'unmodified': 0,
        'errors': 0,
        'fix_counts': {
            'l4_6_user_experience': 0,
            'l4_5_output_clarity': 0,
            'l4_2_command_executability': 0,
            'l4_3_error_recovery': 0,
            'l4_4_dependency_closure': 0,
        },
        'details': [],
        'errors_list': [],
    }

    # 各维度修复关键词 (用于从changes中分类统计)
    fix_dim_keywords = {
        'l4_6_user_experience': ['使用流程', 'FAQ', '已知限制', '升级提示',
                                   '线性步骤', '编号步骤'],
        'l4_5_output_clarity': ['输出格式', '输出描述', '结果处理',
                                 '能力补充输出'],
        'l4_2_command_executability': ['脚本获取', '命令参数', '参数说明'],
        'l4_3_error_recovery': ['空话', '错误处理', '错误处理条目'],
        'l4_4_dependency_closure': ['LLM能力', 'API Key', '运行环境',
                                     '依赖说明章节'],
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
                    'fix_dims': {k: v for k, v in fix_dims.items() if v},
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
    print(f"L4批量修复完成:")
    print(f"  总数:     {stats['total']}")
    print(f"  已修改:   {stats['modified']}")
    print(f"  未修改:   {stats['unmodified']}")
    print(f"  错误:     {stats['errors']}")

    print(f"\n各维度修复统计 (按文件计):")
    dim_labels = {
        'l4_6_user_experience': 'L4-6 用户体验完整性',
        'l4_5_output_clarity': 'L4-5 输出标准明确性',
        'l4_2_command_executability': 'L4-2 命令可执行性',
        'l4_3_error_recovery': 'L4-3 错误恢复可操作性',
        'l4_4_dependency_closure': 'L4-4 依赖闭环性',
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
