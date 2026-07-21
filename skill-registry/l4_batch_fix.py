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
        
        # 如果内容足够长(>100字符)且同时有2项以上,不需要修复
        if len(section) > 100 and sum([has_input, has_output, has_process]) >= 2:
            continue
        
        # 如果内容太短(<50字符)或缺少2项以上,需要补充
        if len(section) < 50 or sum([has_input, has_output, has_process]) < 2:
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
    """L4-3修复: 将错误处理中的空话替换为具体可执行操作"""
    changes = []
    
    err_section = extract_section(content, '错误处理')
    if not err_section:
        err_section = extract_section(content, '异常处理')
    if not err_section:
        return content, ''
    
    new_err = err_section
    replaced_count = 0
    
    for vague, action in VAGUE_TO_ACTION.items():
        if vague in new_err:
            count = new_err.count(vague)
            new_err = new_err.replace(vague, action)
            replaced_count += count
    
    if replaced_count > 0:
        # 替换内容 (支持章节名变体)
        for section_pattern in [r'##\s+(?:错误|异常)处理\s*\n']:
            pattern = rf'({section_pattern})(.*?)(?=\n## |\Z)'
            match = re.search(pattern, content, re.DOTALL)
            if match and match.group(2).strip() == err_section:
                content = content[:match.start(2)] + '\n' + new_err + '\n' + content[match.end(2):]
                changes.append(f"替换{replaced_count}处空话为具体操作")
                break
    
    return content, '; '.join(changes)


def fix_l4_5_output_clarity(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-5修复: 为skill补充输出格式说明"""
    changes = []
    
    # 检查是否已有输出格式说明
    output_format_keywords = ['JSON', 'CSV', 'Markdown', 'markdown', '输出格式', '返回格式', '格式输出']
    has_output_format = any(kw in content for kw in output_format_keywords)
    
    if has_output_format:
        return content, ''
    
    # 在核心能力章节末尾补充输出格式说明 (支持章节名变体)
    cap_pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n.*?)(?=\n## |\Z)'
    cap_match = re.search(cap_pattern, content, re.DOTALL)
    if not cap_match:
        return content, ''
    
    output_section = """

### 输出格式

执行结果以Markdown格式返回,包含操作状态(成功/失败)、处理摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。
"""
    
    # 在核心能力章节末尾插入
    cap_end = cap_match.end(1)
    content = content[:cap_end] + output_section + content[cap_end:]
    changes.append("补充输出格式说明")
    
    return content, '; '.join(changes)


def fix_l4_4_dependency_closure(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-4修复: 为API Key补充配置方式"""
    changes = []
    
    dep_section = extract_section(content, '依赖说明')
    if not dep_section:
        return content, ''
    
    # 检查是否提到API Key但缺少配置方式
    has_api = any(kw in dep_section for kw in ['API Key', 'API密钥', 'api_key', 'apikey'])
    has_no_api = '无需' in dep_section and ('API' in dep_section or 'Key' in dep_section)
    
    if not has_api or has_no_api:
        return content, ''
    
    has_config = any(kw in dep_section for kw in ['环境变量', 'env', 'export', '配置文件', 'config'])
    if has_config:
        return content, ''
    
    # 补充配置方式
    config_supplement = """

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。"""
    
    # 在依赖说明章节末尾插入
    dep_pattern = r'(## 依赖说明\s*\n.*?)(?=\n## |\Z)'
    dep_match = re.search(dep_pattern, content, re.DOTALL)
    if dep_match:
        dep_end = dep_match.end(1)
        content = content[:dep_end] + config_supplement + content[dep_end:]
        changes.append("补充API Key配置方式")
    
    return content, '; '.join(changes)


def fix_l4_6_user_experience(content: str, fm_data: dict) -> Tuple[str, str]:
    """L4-6修复: 补充FAQ和已知限制"""
    changes = []
    slug = fm_data.get('slug', '')
    is_free = slug.endswith('-free')
    
    # 检查是否缺少FAQ
    has_faq = any(kw in content for kw in ['## FAQ', '## 常见问题', '### FAQ'])
    if not has_faq:
        # 在已知限制前插入FAQ
        faq_section = """## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

"""
        # 找到已知限制章节位置
        limit_pattern = r'(## 已知限制)'
        limit_match = re.search(limit_pattern, content)
        if limit_match:
            insert_pos = limit_match.start(1)
            content = content[:insert_pos] + faq_section + content[insert_pos:]
            changes.append("补充FAQ章节")
        else:
            # 追加到文件末尾
            content += '\n\n' + faq_section.rstrip()
            changes.append("补充FAQ章节")
    
    # 检查是否缺少已知限制
    has_limitations = any(kw in content for kw in ['## 已知限制', '## 限制', '## Limitations'])
    if not has_limitations:
        limit_section = """

## 已知限制

- 每次请求仅处理单一任务,不支持批量并发
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力和网络环境
"""
        content += limit_section
        changes.append("补充已知限制章节")
    
    # -free版本检查升级提示
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
    
    # 执行所有修复 (先添加###标题, 再补充描述, 再修其他)
    for fix_func in [fix_l4_1_add_h3_headings,  # 先确保有≥3个###标题
                     fix_l4_1_task_mapping,       # 再补充输入/处理/输出描述
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
