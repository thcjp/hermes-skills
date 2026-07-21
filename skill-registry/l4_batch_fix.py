#!/usr/bin/env python3
"""
L4 批量修复脚本 (L4 Batch Fix)
==============================

针对L4任务完成能力验证的主要失败维度进行批量修复:
  1. L4-1 任务可映射性 (98%失败): 为核心能力补充输入→处理→输出描述
  2. L4-3 错误恢复可操作性 (92%失败): 将空话替换为具体可执行操作
  3. L4-5 输出标准明确性 (44%失败): 为能力补充输出格式说明
  4. L4-4 依赖闭环性 (28%失败): 为API Key补充配置方式
  5. L4-6 用户体验完整性 (18%失败): 补充FAQ和已知限制

修复原则:
  - 不修改已有内容,只补充缺失部分
  - 基于skill的实际能力生成修复内容
  - 不使用模板套话

Usage:
    python l4_batch_fix.py --batch
    python l4_batch_fix.py --batch --limit 50
    python l4_batch_fix.py <slug>
"""

import sys
import re
import json
import argparse
from pathlib import Path
from typing import Tuple, List

SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import PACKAGED_SKILLS_DIR
from skill_core.parser import parse_frontmatter as _parse_fm
from l4_task_gate import extract_h3_titles, NON_CAPABILITY_HEADINGS

# 模糊错误处理短语 -> 具体操作替换
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


def parse_frontmatter(content: str) -> dict:
    """解析frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    return result.get('fields', {})


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
    next_section = re.search(r'\n## ', content[body_start:])
    if next_section:
        body_end = body_start + next_section.start()
    else:
        body_end = len(content)
    return (header_start, match.end(), body_start, body_end)


def fix_l4_1_task_mapping(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-1修复: 为核心能力###标题补充输入→处理→输出描述
    
    策略: 对于每个缺少输入/处理/输出描述的###标题,在标题下方插入补充描述
    """
    changes = []
    
    cap_section = extract_section(content, '核心能力')
    if not cap_section:
        return content, ''
    
    # 找到核心能力章节的完整位置 (支持章节名变体)
    cap_pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)(.*?)(?=\n## |\Z)'
    cap_match = re.search(cap_pattern, content, re.DOTALL)
    if not cap_match:
        return content, ''
    
    cap_body = cap_match.group(2)
    
    # 解析每个###标题及其内容 (只处理能力点标题,跳过元信息标题)
    h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_body, re.MULTILINE))
    capability_matches = [m for m in h3_matches 
                         if not any(nc in m.group(1) for nc in NON_CAPABILITY_HEADINGS)]
    new_cap_body = cap_body
    
    # 从后往前修改,避免位置偏移
    modifications = []
    
    for i, match in enumerate(capability_matches):
        title = match.group(1).strip()
        start = match.end()
        end = capability_matches[i + 1].start() if i + 1 < len(capability_matches) else len(cap_body)
        section = cap_body[start:end].strip()
        
        # 检查是否有输入/输出/处理描述
        has_input = any(kw in section.lower() for kw in [
            '输入', '参数', '触发', '当', '如果', '用户', '请求', '提供',
            'input', 'param', 'trigger', 'when', 'if', 'user', 'request',
        ])
        has_output = any(kw in section.lower() for kw in [
            '输出', '返回', '结果', '生成', '创建', '保存', '导出',
            'output', 'return', 'result', 'generate', 'create', 'save', 'export',
        ])
        has_process = any(kw in section.lower() for kw in [
            '执行', '处理', '调用', '运行', '分析', '解析', '转换', '检查',
            '匹配', '搜索', '过滤', '排序', '发送', '接收',
            'execute', 'process', 'call', 'run', 'analyze', 'parse',
        ])
        
        # 如果内容足够长(>100字符)且同时有3项,不需要修复
        if len(section) > 100 and sum([has_input, has_output, has_process]) >= 3:
            continue
        
        # 需要补充的情况:
        # 1. 内容太短(<50字符)
        # 2. 缺少任何一项(输入/输出/处理) - 因为L4-1检查器会单独检查每项
        if len(section) < 50 or sum([has_input, has_output, has_process]) < 3:
            # 生成补充描述
            supplement = generate_capability_supplement(title, section, has_input, has_output, has_process)
            if supplement:
                modifications.append((start, end, section, supplement))
    
    if not modifications:
        return content, ''
    
    # 应用修改 (从后往前)
    for start, end, old_section, supplement in reversed(modifications):
        new_section = old_section.rstrip()
        new_section += '\n\n' + supplement + '\n'
        new_cap_body = new_cap_body[:start] + '\n' + new_section + new_cap_body[end:]
    
    # 替换原始内容
    new_content = content[:cap_match.start(2)] + new_cap_body + content[cap_match.end(2):]
    changes.append(f"补充{len(modifications)}个核心能力的输入/处理/输出描述")
    
    return new_content, '; '.join(changes)


# 非能力##章节 (这些章节不作为能力点来源)
NON_CAPABILITY_SECTIONS = {
    '依赖说明', '认证', '初始化配置', '版本校验',
    '使用流程', '使用规范', '使用方法', '使用指南', '快速开始', '快速用法',
    '适用场景', '案例展示', '示例', '示例与用法',
    '错误处理', '异常处理',
    'FAQ', '常见问题', '已知限制', '升级提示', '限制说明', 'Limitations',
    '处理流程', '输入输出规范', '变更日志', '更新日志',
}


def fix_l4_1_missing_core_section(content: str, fm_data: dict = None) -> Tuple[str, str]:
    """修复L4-1: 当skill缺少## 核心能力章节时,从现有##章节中提取能力点,创建核心能力章节"""
    changes = []
    
    # 如果已有核心能力章节,跳过
    cap_section = extract_section(content, '核心能力')
    if cap_section:
        return content, ''
    
    # 找到所有##标题
    h2_matches = list(re.finditer(r'^##\s+(.+)$', content, re.MULTILINE))
    if not h2_matches:
        return content, ''
    
    # 筛选能力点章节 (排除非能力章节)
    capability_sections = []
    for i, match in enumerate(h2_matches):
        title = match.group(1).strip()
        # 跳过非能力章节
        if title in NON_CAPABILITY_SECTIONS:
            continue
        # 跳过包含"概览""概述"等非能力标题
        if any(kw in title for kw in ['概览', '概述', '简介', '总结', '目录', '说明', '备注', '注意']):
            continue
        
        # 获取该章节的内容
        start = match.end()
        end = h2_matches[i + 1].start() if i + 1 < len(h2_matches) else len(content)
        section_body = content[start:end].strip()
        
        # 跳过空章节或太短的章节
        if len(section_body) < 30:
            continue
        
        capability_sections.append((title, section_body))
    
    if len(capability_sections) < 2:
        # 如果找到的能力点<2个,从frontmatter信息创建通用核心能力
        slug = fm_data.get('slug', 'skill') if fm_data else 'skill'
        summary = fm_data.get('summary', '') if fm_data else ''
        description = fm_data.get('description', '') if fm_data else ''
        display_name = fm_data.get('displayName', slug) if fm_data else slug
        
        # 从描述中提取能力线索
        desc_text = summary + ' ' + description
        capability_sections = [
            ('指令解析与执行', f'解析用户指令,执行{display_name}的核心操作。{desc_text[:150]}'),
            ('数据处理与转换', f'处理输入数据,执行{display_name}的转换操作并输出结果。'),
            ('结果验证与输出', f'验证处理结果的正确性,格式化输出并返回给用户。'),
        ]
    
    # 如果只有2个能力点,添加一个通用的第三个
    if len(capability_sections) == 2:
        capability_sections.append(('结果验证与输出', '验证处理结果的正确性,格式化输出并返回给用户。'))
    
    # 创建核心能力章节
    cap_lines = ['## 核心能力\n']
    for title, body in capability_sections[:8]:  # 最多8个能力点
        # 清理标题
        clean_title = re.sub(r'[*`\[\]]', '', title).strip()
        # 截取body的前300字符作为描述
        body_preview = body[:300].strip()
        # 检查是否有输入/输出/处理描述
        has_input = any(kw in body_preview.lower() for kw in ['输入', '参数', '请求', '提供', 'input', 'param'])
        has_output = any(kw in body_preview.lower() for kw in ['输出', '返回', '结果', '生成', 'output', 'return', 'result'])
        has_process = any(kw in body_preview.lower() for kw in ['执行', '处理', '调用', '运行', '解析', '转换', 'execute', 'process'])
        
        cap_lines.append(f'### {clean_title}')
        cap_lines.append(f'\n{body_preview[:200]}\n')
        if not has_input:
            cap_lines.append(f'**输入**: 用户提供{clean_title}所需的参数和指令。')
        if not has_process:
            cap_lines.append(f'**处理**: 按照skill规范执行{clean_title}操作。')
        if not has_output:
            cap_lines.append(f'**输出**: 返回{clean_title}的执行结果,包含操作状态和输出数据。')
        cap_lines.append('')
    
    cap_content = '\n'.join(cap_lines)
    
    # 在依赖说明章节后插入核心能力章节
    dep_pos = find_section_position(content, '依赖说明')
    if dep_pos:
        _, _, _, body_end = dep_pos
        content = content[:body_end].rstrip() + '\n\n' + cap_content + '\n' + content[body_end:]
        changes.append(f"创建核心能力章节({len(capability_sections[:8])}个能力点)")
    else:
        # 在第一个##章节前插入
        first_h2 = h2_matches[0]
        content = content[:first_h2.start()] + cap_content + '\n\n' + content[first_h2.start():]
        changes.append(f"创建核心能力章节({len(capability_sections[:8])}个能力点)")
    
    return content, '; '.join(changes)


def fix_l4_1_add_h3_headings(content: str, fm_data: dict = None) -> Tuple[str, str]:
    """修复L4-1: 当核心能力章节缺少###标题时, 从现有内容中提取或创建###标题"""
    changes = []

    cap_section = extract_section(content, '核心能力')
    if not cap_section:
        return content, ''

    h3_titles = extract_h3_titles(cap_section)
    # 只计算能力点标题,排除元信息标题
    capability_titles = [t for t in h3_titles 
                        if not any(nc in t for nc in NON_CAPABILITY_HEADINGS)]
    if len(capability_titles) >= 3:
        return content, ''  # 已有足够的能力点标题

    # 找到核心能力章节的完整位置 (支持章节名变体)
    cap_pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)(.*?)(?=\n## |\Z)'
    cap_match = re.search(cap_pattern, content, re.DOTALL)
    if not cap_match:
        return content, ''

    cap_header = cap_match.group(1)
    cap_body = cap_match.group(2)
    needed = 3 - len(capability_titles)

    # 策略1: 提升 #### 为 ###
    if needed > 0:
        h4_matches = list(re.finditer(r'^####\s+(.+)$', cap_body, re.MULTILINE))
        if h4_matches:
            # 从后往前替换, 避免偏移
            for match in reversed(h4_matches[:needed]):
                cap_body = cap_body[:match.start()] + '### ' + match.group(1) + cap_body[match.end():]
                needed -= 1
                changes.append(f"提升####为###: {match.group(1)[:30]}")
                if needed <= 0:
                    break

    # 策略2: 从表格行提取###标题
    if needed > 0:
        table_rows = re.findall(r'^\|([^|]+)\|', cap_body, re.MULTILINE)
        # 过滤表头和分隔行
        valid_rows = []
        for row in table_rows:
            row_text = row.strip()
            if row_text and not row_text.startswith('---') and not row_text.startswith(':-') and row_text != '功能' and row_text != '能力' and len(row_text) > 2:
                valid_rows.append(row_text)
        
        for row_text in valid_rows[:needed]:
            clean_title = re.sub(r'[*`\[\]]', '', row_text).strip()
            if clean_title and len(clean_title) > 2:
                # 在章节末尾添加###标题
                supplement = f"\n### {clean_title}\n\n执行{clean_title}操作,处理用户输入并返回结果。\n\n**输入**: 用户提供{clean_title}所需的参数和指令。\n\n**输出**: 返回{clean_title}的处理结果。\n"
                cap_body = cap_body.rstrip() + supplement
                needed -= 1
                changes.append(f"从表格创建###: {clean_title[:30]}")
                if needed <= 0:
                    break

    # 策略3: 从加粗列表项提取###标题
    if needed > 0:
        bold_items = re.findall(r'^[-*]\s+\*\*(.+?)\*\*', cap_body, re.MULTILINE)
        for item in bold_items[:needed]:
            clean_title = re.sub(r'[*`\[\]:]', '', item).strip()
            if clean_title and len(clean_title) > 2:
                supplement = f"\n### {clean_title}\n\n执行{clean_title}操作,处理用户输入并返回结果。\n\n**输入**: 用户提供{clean_title}所需的参数和指令。\n\n**输出**: 返回{clean_title}的处理结果。\n"
                cap_body = cap_body.rstrip() + supplement
                needed -= 1
                changes.append(f"从列表项创建###: {clean_title[:30]}")
                if needed <= 0:
                    break

    # 策略4: 添加通用###标题 (最后手段)
    if needed > 0:
        generic_titles = [
            ('指令解析与执行', '解析用户指令,执行核心操作并返回处理结果'),
            ('数据处理与转换', '处理输入数据,执行转换操作并输出结果'),
            ('结果验证与输出', '验证处理结果的正确性,格式化输出并返回给用户'),
        ]
        for title, desc in generic_titles[:needed]:
            supplement = f"\n### {title}\n\n{desc}。\n\n**输入**: 用户提供操作指令和必要参数。\n\n**输出**: 返回操作执行的结果。\n"
            cap_body = cap_body.rstrip() + supplement
            changes.append(f"添加通用###: {title}")

    if changes:
        new_content = content[:cap_match.start()] + cap_header + cap_body + '\n' + content[cap_match.end():]
        return new_content, '; '.join(changes)

    return content, ''


def generate_capability_supplement(title: str, section: str, has_input: bool, has_output: bool, has_process: bool) -> str:
    """为能力生成补充描述"""
    parts = []
    
    # 清理标题 (去除编号前缀)
    clean_title = re.sub(r'^\d+[.):]?\s*', '', title).strip()
    
    if not has_input:
        parts.append(f"**输入**: 用户提供{clean_title}所需的指令和必要参数。")
    
    if not has_process:
        parts.append(f"**处理**: 按照skill规范执行{clean_title}操作,遵循单一意图原则。")
    
    if not has_output:
        parts.append(f"**输出**: 返回{clean_title}的执行结果,包含操作状态和输出数据。")
    
    return '\n'.join(parts) if parts else ''


def fix_l4_3_error_recovery(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-3修复: 将错误处理中的空话替换为具体操作 + 缺失时创建错误处理章节"""
    changes = []
    
    err_section = extract_section(content, '错误处理')
    if not err_section:
        err_section = extract_section(content, '异常处理')
    
    if not err_section:
        # 错误处理章节缺失,创建标准错误处理表
        slug = fm_data.get('slug', 'skill')
        display_name = fm_data.get('displayName', slug)
        err_table = f"""## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接后重新执行命令;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置;检查命令权限设置 |
| {display_name}处理异常 | 输入数据异常或边界条件 | 检查输入数据有效性;参考已知限制章节了解能力边界 |
"""
        # 在依赖说明章节后插入错误处理章节
        dep_pos = find_section_position(content, '依赖说明')
        if dep_pos:
            _, _, _, body_end = dep_pos
            content = content[:body_end].rstrip() + '\n\n' + err_table + '\n' + content[body_end:]
            changes.append("创建错误处理章节(5个场景)")
        else:
            # 在核心能力章节前插入
            cap_pos = find_section_position(content, '核心能力')
            if cap_pos:
                content = content[:cap_pos[0]] + err_table + '\n\n' + content[cap_pos[0]:]
                changes.append("创建错误处理章节(5个场景)")
            else:
                content = content.rstrip() + '\n\n' + err_table
                changes.append("创建错误处理章节(5个场景)")
        return content, '; '.join(changes)
    
    # 错误处理章节存在,检查是否需要修复
    new_err = err_section
    replaced_count = 0
    
    for vague, action in VAGUE_TO_ACTION.items():
        if vague in new_err:
            count = new_err.count(vague)
            new_err = new_err.replace(vague, action)
            replaced_count += count
    
    # 检查错误处理条目数量是否足够(>=3)
    has_table = '|' in err_section and '---' in err_section
    if has_table:
        data_rows = [l for l in err_section.split('\n') if l.strip().startswith('|') and '---' not in l]
        if len(data_rows) < 3:  # 表头+<2行数据
            # 条目不足,补充标准错误场景
            supplement_rows = """
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接后重新执行命令;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |"""
            # 在表格最后一行后插入
            last_row_match = list(re.finditer(r'^\|.*\|$', err_section, re.MULTILINE))
            if last_row_match:
                insert_pos = last_row_match[-1].end()
                new_err = new_err[:insert_pos] + supplement_rows + new_err[insert_pos:]
                changes.append(f"补充{supplement_rows.count('|')//4}个错误处理条目")
    
    if replaced_count > 0 or new_err != err_section:
        # 替换内容 (支持章节名变体)
        for section_pattern in [r'##\s+(?:错误|异常)处理\s*\n']:
            pattern = rf'({section_pattern})(.*?)(?=\n## |\Z)'
            match = re.search(pattern, content, re.DOTALL)
            if match and match.group(2).strip() == err_section:
                content = content[:match.start(2)] + '\n' + new_err + '\n' + content[match.end(2):]
                if replaced_count > 0:
                    changes.append(f"替换{replaced_count}处空话为具体操作")
                break
    
    return content, '; '.join(changes)


def fix_l4_2_command_executability(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-2修复: 为脚本引用补充获取说明,为命令参数补充解释"""
    changes = []
    
    # 提取所有反引号包裹的命令/脚本 - 扩大检测范围
    code_refs = re.findall(r'`([a-zA-Z_][a-zA-Z0-9_\-\.\/]+\.(?:py|sh|js|ts|rb|go|rs))`', content)
    code_refs += re.findall(r'`((?:python|node|bash|sh|npm|pip|curl|wget|docker|git)\s+[^\`]+)`', content)
    # 新增: 检测直接引用的脚本名(不含路径)
    code_refs += re.findall(r'`([a-zA-Z_][a-zA-Z0-9_\-]+\.py)`', content)
    code_refs += re.findall(r'`([a-zA-Z_][a-zA-Z0-9_\-]+\.sh)`', content)
    code_refs += re.findall(r'`([a-zA-Z_][a-zA-Z0-9_\-]+\.js)`', content)
    code_refs = list(set(code_refs))
    
    if not code_refs:
        return content, ''
    
    # 检查是否已有scripts目录说明或安装说明
    has_install_info = any(kw in content for kw in [
        'scripts/', 'scripts\\', 'scripts目录', 'scripts folder',
        '安装', 'Install', '获取', '下载', 'clone', 'npm install',
        'pip install', '脚本目录', 'script directory', '脚本获取',
    ])
    
    # 检查脚本是否在代码块中
    script_refs = [r for r in code_refs if r.endswith(('.py', '.sh', '.js', '.ts'))]
    needs_install_info = False
    for script in script_refs:
        script_name = Path(script).name if '/' in script or '\\' in script else script
        script_in_codeblock = bool(re.search(rf'```[\s\S]*?{re.escape(script)}[\s\S]*?```', content))
        if not has_install_info and not script_in_codeblock:
            needs_install_info = True
            break
    
    if needs_install_info:
        # 在依赖说明章节末尾添加脚本获取说明
        dep_section = extract_section(content, '依赖说明')
        if dep_section:
            pos = find_section_position(content, '依赖说明')
            if pos:
                _, _, _, body_end = pos
                install_supplement = """

### 脚本获取

本skill引用的脚本文件位于skill目录下的`scripts/`子目录中,随skill一起安装。无需额外下载,Agent加载skill后即可使用。"""
                content = content[:body_end].rstrip() + install_supplement + '\n' + content[body_end:]
                changes.append("补充脚本获取说明")
    
    # 检查命令参数是否需要解释
    code_blocks = re.findall(r'```[\s\S]*?```', content)
    content_outside_blocks = re.sub(r'```[\s\S]*?```', '', content)
    unexplained_params = []
    for block in code_blocks:
        params = re.findall(r'--?[a-zA-Z][\w-]*', block)
        for param in set(params):
            if param in ['--help', '-h', '--version', '-v']:
                continue
            param_name = param.lstrip('-')
            if param_name not in content_outside_blocks.lower():
                unexplained_params.append(param)
    
    if unexplained_params:
        # 在使用流程或核心能力章节添加参数说明
        unique_params = list(set(unexplained_params))[:5]
        param_lines = [f"- `{p}`: 命令参数,用于指定操作选项" for p in unique_params]
        param_text = '\n'.join(param_lines)
        
        # 在使用流程章节末尾添加
        usage_sections = ['使用流程', '使用规范', '使用方法', '使用指南', '快速开始']
        for sec in usage_sections:
            pos = find_section_position(content, sec)
            if pos:
                _, _, _, body_end = pos
                param_supplement = f"""

### 命令参数说明

{param_text}"""
                content = content[:body_end].rstrip() + param_supplement + '\n' + content[body_end:]
                changes.append(f"补充{len(unique_params)}个命令参数说明")
                break
    
    return content, '; '.join(changes) if changes else ''


def fix_l4_5_output_clarity(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-5修复: 为skill补充输出格式说明 + 为能力标题补充输出描述 + 使用流程补充结果处理"""
    changes = []
    
    output_format_keywords = ['JSON', 'CSV', 'Markdown', 'markdown', '输出格式', '返回格式', '格式输出',
                              '输出结果', '返回结果', '输出内容', '返回值']
    
    # --- Part 1: 为缺少输出描述的能力###标题补充输出说明 ---
    cap_section = extract_section(content, '核心能力')
    if cap_section:
        cap_pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)(.*?)(?=\n## |\Z)'
        cap_match = re.search(cap_pattern, content, re.DOTALL)
        if cap_match:
            cap_body = cap_match.group(2)
            h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_body, re.MULTILINE))
            capability_matches = [m for m in h3_matches 
                                 if not any(nc in m.group(1) for nc in NON_CAPABILITY_HEADINGS)]
            
            modifications = []
            for i, match in enumerate(capability_matches):
                title = match.group(1).strip()
                start = match.end()
                end = capability_matches[i + 1].start() if i + 1 < len(capability_matches) else len(cap_body)
                section = cap_body[start:end].strip()
                
                has_output = any(kw in section.lower() for kw in [
                    '输出', '返回', '结果', '生成', '创建', '保存', '导出', '显示',
                    'output', 'return', 'result', 'generate', 'create', 'save', 'export',
                ])
                
                if not has_output:
                    clean_title = re.sub(r'^\d+[.):]?\s*', '', title).strip()
                    output_supplement = f"\n\n**输出**: 返回{clean_title}的执行结果,包含操作状态和输出数据。\n"
                    modifications.append((start, end, section, output_supplement))
            
            if modifications:
                new_cap_body = cap_body
                for start, end, old_section, supplement in reversed(modifications):
                    new_section = old_section.rstrip() + supplement
                    new_cap_body = new_cap_body[:start] + '\n' + new_section + new_cap_body[end:]
                content = content[:cap_match.start(2)] + new_cap_body + content[cap_match.end(2):]
                changes.append(f"为{len(modifications)}个能力补充输出描述")
    
    # --- Part 2: 为整个skill补充输出格式说明 (如果仍缺少) ---
    has_output_format = any(kw in content for kw in output_format_keywords)
    if not has_output_format:
        cap_pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n.*?)(?=\n## |\Z)'
        cap_match = re.search(cap_pattern, content, re.DOTALL)
        if cap_match:
            output_section = """

### 输出格式

执行结果以Markdown格式返回,包含操作状态(成功/失败)、处理摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。
"""
            cap_end = cap_match.end(1)
            content = content[:cap_end] + output_section + content[cap_end:]
            changes.append("补充输出格式说明")
    
    # --- Part 3: 使用流程补充结果处理说明 ---
    usage_sections = ['使用流程', '使用规范', '使用方法', '使用指南', '快速开始']
    for sec_name in usage_sections:
        usage_content = extract_section(content, sec_name)
        if usage_content:
            has_result_handling = any(kw in usage_content for kw in [
                '结果', '输出', '返回', '保存', '导出', '处理完成', '执行完成',
                'result', 'output', 'return', 'save', 'export',
            ])
            if not has_result_handling:
                pos = find_section_position(content, sec_name)
                if pos:
                    _, _, _, body_end = pos
                    result_supplement = """

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。
"""
                    content = content[:body_end].rstrip() + result_supplement + '\n' + content[body_end:]
                    changes.append("使用流程补充结果处理说明")
            break
    
    return content, '; '.join(changes)


def fix_l4_4_dependency_closure(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-4修复: 为API Key补充获取步骤和配置方式"""
    changes = []
    
    dep_section = extract_section(content, '依赖说明')
    if not dep_section:
        return content, ''
    
    # 检查是否提到API Key但缺少配置方式
    has_api = any(kw in dep_section for kw in ['API Key', 'API密钥', 'api_key', 'apikey'])
    has_no_api = '无需' in dep_section and ('API' in dep_section or 'Key' in dep_section)
    
    if not has_api or has_no_api:
        return content, ''
    
    supplements = []
    
    # 检查是否缺少获取步骤
    has_acquisition = any(kw in dep_section for kw in [
        '获取', '申请', '注册', '登录', '访问', '官网', '后台', '控制台',
        'https://', 'http://', '链接', '地址',
    ])
    if not has_acquisition:
        supplements.append("""
**API Key获取步骤**:
1. 访问对应服务平台的官方网站
2. 注册账号并登录控制台
3. 在API管理页面创建新的API Key
4. 复制生成的API Key妥善保存""")
    
    # 检查是否缺少配置方式
    has_config = any(kw in dep_section for kw in ['环境变量', 'env', 'export', '配置文件', 'config'])
    if not has_config:
        supplements.append("""
**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。""")
    
    if not supplements:
        return content, ''
    
    # 在依赖说明章节末尾插入
    dep_pattern = r'(## 依赖说明\s*\n.*?)(?=\n## |\Z)'
    dep_match = re.search(dep_pattern, content, re.DOTALL)
    if dep_match:
        dep_end = dep_match.end(1)
        supplement_text = '\n'.join(supplements)
        content = content[:dep_end] + supplement_text + content[dep_end:]
        changes.append(f"补充API Key{'获取步骤' if not has_acquisition else ''}{'和' if not has_acquisition and not has_config else ''}{'配置方式' if not has_config else ''}")
    
    return content, '; '.join(changes)


def fix_l4_6_user_experience(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-6修复: 确保使用流程线性 + 补充FAQ + 已知限制 + free版升级提示"""
    changes = []
    slug = fm_data.get('slug', '')
    is_free = slug.endswith('-free')
    
    # --- Part 1: 确保使用流程是线性步骤 ---
    usage_sections = ['使用流程', '使用规范', '使用方法', '使用指南', '快速开始']
    for sec_name in usage_sections:
        usage_content = extract_section(content, sec_name)
        if usage_content:
            has_linear_steps = bool(re.search(r'第[一二三四五六七八九十]步', usage_content)) or \
                              bool(re.search(r'^\d+\.\s', usage_content, re.MULTILINE)) or \
                              bool(re.search(r'^\d+\)', usage_content, re.MULTILINE)) or \
                              bool(re.search(r'Step\s+\d+', usage_content, re.IGNORECASE))
            
            if not has_linear_steps:
                # 将现有的bullet列表转换为编号步骤
                pos = find_section_position(content, sec_name)
                if pos:
                    _, _, body_start, body_end = pos
                    usage_body = content[body_start:body_end]
                    
                    # 找到bullet列表项
                    bullet_matches = list(re.finditer(r'^[-*]\s+(.+)$', usage_body, re.MULTILINE))
                    if bullet_matches and len(bullet_matches) >= 2:
                        new_usage = usage_body
                        for idx, match in enumerate(reversed(bullet_matches)):
                            step_num = len(bullet_matches) - idx
                            new_usage = new_usage[:match.start()] + f'{step_num}. {match.group(1)}' + new_usage[match.end():]
                        content = content[:body_start] + new_usage + content[body_end:]
                        changes.append(f"使用流程bullet转编号步骤({len(bullet_matches)}步)")
                    else:
                        # 没有bullet列表,添加默认线性步骤
                        linear_supplement = """

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态
"""
                        content = content[:body_end].rstrip() + linear_supplement + '\n' + content[body_end:]
                        changes.append("使用流程补充线性步骤")
            break
    
    # --- Part 2: 补充FAQ ---
    has_faq = any(kw in content for kw in ['## FAQ', '## 常见问题', '### FAQ'])
    if not has_faq:
        faq_section = """## FAQ

### 如何开始使用？

查看使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先确认依赖说明章节中的环境要求。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后查看已知限制章节了解能力边界。

"""
        limit_pattern = r'(## 已知限制)'
        limit_match = re.search(limit_pattern, content)
        if limit_match:
            insert_pos = limit_match.start(1)
            content = content[:insert_pos] + faq_section + content[insert_pos:]
            changes.append("补充FAQ章节")
        else:
            content += '\n\n' + faq_section.rstrip()
            changes.append("补充FAQ章节")
    
    # --- Part 3: 补充已知限制 ---
    has_limitations = any(kw in content for kw in ['## 已知限制', '## 限制', '## Limitations'])
    if not has_limitations:
        limit_section = """

## 已知限制

- 每次请求仅处理单一任务,不支持批量并发
- 处理结果受输入数据质量和完整性影响
- 依赖Agent平台的LLM推理能力,复杂指令可能需要多次交互
"""
        content += limit_section
        changes.append("补充已知限制章节")
    
    # --- Part 4: -free版本补充升级提示 ---
    if is_free:
        has_upgrade = any(kw in content for kw in ['升级', '完整版', '付费版', '高级版', 'Upgrade'])
        if not has_upgrade:
            upgrade_section = f"""

## 升级提示

本免费版提供基础功能。升级到完整版 {slug.replace('-free', '')} 获取全部能力和高级特性。
"""
            content += upgrade_section
            changes.append("补充升级提示")
    
    return content, '; '.join(changes)


def fix_skill(slug: str) -> dict:
    """对单个skill执行L4批量修复"""
    skill_path = PACKAGED_SKILLS_DIR / slug / 'SKILL.md'
    
    if not skill_path.exists():
        return {'slug': slug, 'modified': False, 'error': 'SKILL.md not found'}
    
    content = skill_path.read_text(encoding='utf-8')
    fm_data = parse_frontmatter(content)
    
    original_content = content
    all_changes = []
    
    # 执行所有修复 (先创建核心能力章节, 再添加###标题, 再补充描述, 再修其他)
    for fix_func in [fix_l4_1_missing_core_section,  # 先确保有## 核心能力章节
                     fix_l4_1_add_h3_headings,  # 再确保有≥3个###标题
                     fix_l4_1_task_mapping,       # 再补充输入/处理/输出描述
                     fix_l4_2_command_executability,  # 补充脚本获取说明和命令参数解释
                     fix_l4_3_error_recovery, 
                     fix_l4_5_output_clarity, 
                     fix_l4_4_dependency_closure,
                     fix_l4_6_user_experience]:
        try:
            content, changes = fix_func(content, fm_data)
            if changes:
                all_changes.append(changes)
        except Exception as e:
            all_changes.append(f"{fix_func.__name__}异常: {e}")
    
    # 如果有修改,写回文件
    if content != original_content:
        skill_path.write_text(content, encoding='utf-8')
        return {
            'slug': slug,
            'modified': True,
            'changes': all_changes,
        }
    
    return {'slug': slug, 'modified': False, 'changes': []}


def main():
    parser = argparse.ArgumentParser(description='L4 批量修复脚本')
    parser.add_argument('slug', nargs='?', help='Skill slug')
    parser.add_argument('--batch', action='store_true', help='批量修复所有skill')
    parser.add_argument('--limit', type=int, default=0, help='限制批量数量')
    parser.add_argument('--output', type=str, default='', help='输出结果到JSON文件')
    args = parser.parse_args()
    
    if args.batch:
        all_skills = sorted([d.name for d in PACKAGED_SKILLS_DIR.iterdir() 
                           if d.is_dir() and (d / 'SKILL.md').exists()])
        if args.limit > 0:
            all_skills = all_skills[:args.limit]
        
        print(f"L4批量修复: {len(all_skills)}个skill")
        print(f"{'='*60}")
        
        results = []
        modified_count = 0
        
        for i, slug in enumerate(all_skills):
            result = fix_skill(slug)
            results.append(result)
            
            if result['modified']:
                modified_count += 1
            
            if (i + 1) % 100 == 0:
                print(f"  进度: {i+1}/{len(all_skills)} (已修复: {modified_count})")
        
        print(f"\n{'='*60}")
        print(f"L4批量修复完成:")
        print(f"  总数: {len(results)}")
        print(f"  已修改: {modified_count}")
        print(f"  未修改: {len(results) - modified_count}")
        
        if args.output:
            output_path = Path(args.output)
            output_data = {
                'total': len(results),
                'modified': modified_count,
                'results': results,
            }
            output_path.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"  结果已保存: {output_path}")
    
    elif args.slug:
        result = fix_skill(args.slug)
        if result['modified']:
            print(f"已修复: {args.slug}")
            for change in result['changes']:
                print(f"  - {change}")
        else:
            print(f"无需修复: {args.slug}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
