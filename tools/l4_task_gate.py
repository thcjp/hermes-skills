#!/usr/bin/env python3
"""
L4 任务完成能力验证关卡 (Task Completion Gate)
================================================

上传平台前的最终关卡。不是检查文档写得好不好（那是L3的职责），
而是验证skill能否实际指导Agent完成任务。

核心问题: "用户安装这个skill后,Agent真的能按指令完成任务吗?"

验证维度:
  L4-1 任务可映射性: 每个核心能力是否对应一个明确的用户任务
  L4-2 命令可执行性: 引用的命令/脚本是否有完整获取和使用说明
  L4-3 错误恢复可操作性: 错误处理有可执行的恢复步骤,不是空话
  L4-4 依赖闭环性: 用户按说明能否完整配置环境
  L4-5 输出标准明确性: 每个能力有明确的成功输出描述
  L4-6 用户体验完整性: 使用流程线性、有FAQ、有升级提示(free版)

打回机制:
  - 任一维度FAIL → 标记状态"不通过"
  - 生成打回报告,指明具体问题
  - 打回生成/修改/包装步骤重做
  - 循环直到通过

Usage:
    python l4_task_gate.py <slug>
    python l4_task_gate.py <slug> --json
    python l4_task_gate.py --batch --limit 50
    python l4_task_gate.py --batch --output l4_results.json
"""

import sys
import re
import json
import argparse
from pathlib import Path
from typing import List, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, PACKAGED_SKILLS_DIR
sys.path.insert(0, str(TOOLS_DIR))

from skill_core.parser import parse_frontmatter, extract_section
from skill_core.rules import (  # V135 F3: 统一checker/fixer共享常量
    NON_CAPABILITY_HEADINGS, PASS, FAIL, WARN, ACTION_VERBS, VAGUE_SOLUTIONS,  # V104 W2/W3 + V134 E6
    CAPABILITY_INPUT_KEYWORDS, CAPABILITY_PROCESS_KEYWORDS, CAPABILITY_OUTPUT_KEYWORDS,  # L4-1/L4-5
    USAGE_SECTION_NAMES, STANDARD_CMD_PARAMS, INSTALL_INFO_KEYWORDS,  # L4-2/L4-5/L4-6
    ERROR_SOLUTION_KEYWORDS, TABLE_HEADER_SCENARIO_KEYWORDS, TABLE_HEADER_SOLUTION_KEYWORDS,  # L4-3
    LLM_MENTION_KEYWORDS, LLM_SPECIFIC_KEYWORDS,  # L4-4
    API_MENTION_KEYWORDS, API_ACQUISITION_KEYWORDS, API_CONFIG_KEYWORDS,  # L4-4
    ENV_MENTION_KEYWORDS, ENV_SPECIFIC_KEYWORDS,  # L4-4
    FAQ_KEYWORDS, LIMITATIONS_KEYWORDS, UPGRADE_KEYWORDS, NON_TASK_KEYWORDS,  # L4-6
    OUTPUT_FORMAT_KEYWORDS, RESULT_HANDLING_KEYWORDS,  # L4-5
)


def extract_h3_titles(section_content: str) -> List[str]:
    """提取###标题列表"""
    # 移除代码块
    no_code = re.sub(r'```[\s\S]*?```', '', section_content)
    return [m.strip() for m in re.findall(r'^###\s+(.+)$', no_code, re.MULTILINE)]


def check_l4_task_mapping(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L4-1: 任务可映射性检查
    
    每个核心能力###标题是否对应一个明确的用户任务:
    - 标题是动作短语或功能名（不是"概述"、"简介"等）
    - 标题下有"输入→处理→输出"的描述（直接或间接）
    """
    errors = []
    
    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return (FAIL, ["无法找到## 核心能力章节"])
    
    h3_titles = extract_h3_titles(cap_content)
    # 过滤掉非能力点标题(元信息/补充说明)
    capability_titles = [t for t in h3_titles 
                        if not any(nc in t for nc in NON_CAPABILITY_HEADINGS)]
    if len(capability_titles) < 3:
        return (FAIL, [f"核心能力仅{len(capability_titles)}个能力点###标题,需要>=3个用户任务"])
    
    # 检查标题是否是有效任务（非"概述"、"简介"等非任务标题）
    for title in capability_titles:
        is_non_task = any(kw.lower() in title.lower() for kw in NON_TASK_KEYWORDS)  # [V135 F3] 统一常量
        if is_non_task:
            errors.append(f"核心能力标题'{title}'不是可执行任务(含'概述/简介'等)")
    
    # 检查每个能力是否有输入输出描述 (只检查能力点标题,跳过元信息标题)
    h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_content, re.MULTILINE))
    capability_matches = [m for m in h3_matches 
                         if not any(nc in m.group(1) for nc in NON_CAPABILITY_HEADINGS)]
    
    for i, match in enumerate(capability_matches):
        title = match.group(1).strip()
        start = match.end()
        end = capability_matches[i + 1].start() if i + 1 < len(capability_matches) else len(cap_content)
        section = cap_content[start:end].strip()
        
        # 检查是否有输入/触发条件描述
        has_input = any(kw in section.lower() for kw in CAPABILITY_INPUT_KEYWORDS)  # [V135 F3] 统一常量
        
        # 检查是否有输出/结果描述
        has_output = any(kw in section.lower() for kw in CAPABILITY_OUTPUT_KEYWORDS)  # [V135 F3] 统一常量
        
        # 检查是否有处理/执行描述
        has_process = any(kw in section.lower() for kw in CAPABILITY_PROCESS_KEYWORDS)  # [V135 F3] 统一常量
        
        if not has_input and not has_output:
            errors.append(f"能力'{title}'缺少输入/输出描述,Agent无法理解任务流程")
        if not has_process:
            errors.append(f"能力'{title}'缺少处理/执行描述,Agent不知道如何完成任务")
    
    return (FAIL if errors else PASS, errors)


def check_l4_command_executability(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L4-2: 命令可执行性检查
    
    skill中引用的命令/脚本是否有完整的获取和使用说明:
    - 反引号命令是否有安装/获取说明
    - 脚本路径是否有对应scripts目录说明
    - 命令参数是否完整解释
    """
    errors = []
    
    # 提取所有反引号包裹的命令/脚本
    # 排除纯变量名（不含路径分隔符或命令特征）
    code_refs = re.findall(r'`([a-zA-Z_][a-zA-Z0-9_\-\.\/]+\.(?:py|sh|js|ts|rb|go|rs))`', content)
    code_refs += re.findall(r'`((?:python|node|bash|sh|npm|pip|curl|wget|docker|git)\s+[^\`]+)`', content)
    code_refs = list(set(code_refs))
    
    if not code_refs:
        # 没有引用命令,检查是否是纯MD skill
        tools = fm_data.get('tools', [])
        has_exec = 'exec' in str(tools).lower() if tools else False
        if has_exec:
            errors.append("tools声明exec但skill中无任何命令/脚本引用")
        # 纯MD skill不检查命令,直接通过
        return (PASS if not errors else FAIL, errors)
    
    # 检查脚本路径引用是否有获取说明
    script_refs = [r for r in code_refs if r.endswith(('.py', '.sh', '.js', '.ts'))]
    for script in script_refs:
        # 提取脚本名
        script_name = Path(script).name if '/' in script or '\\' in script else script
        
        # 检查是否有scripts目录说明或安装说明
        has_install_info = any(kw in content for kw in INSTALL_INFO_KEYWORDS)  # [V135 F3] 统一常量
        
        # 检查脚本是否在代码块中给出了完整调用示例
        script_in_codeblock = bool(re.search(
            rf'```[\s\S]*?{re.escape(script)}[\s\S]*?```', content
        ))
        
        if not has_install_info and not script_in_codeblock:
            errors.append(f"脚本'{script_name}'被引用但无获取方式或完整调用示例")
    
    # 检查命令参数是否完整解释
    # 找到代码块中的命令调用
    code_blocks = re.findall(r'```[\s\S]*?```', content)
    for block in code_blocks:
        # 找到命令中的参数（--xxx 或 -x 格式）
        params = re.findall(r'--?[a-zA-Z][\w-]*', block)
        for param in set(params):
            # 检查参数是否在skill内容中有解释
            # 排除常见标准参数
            if param in STANDARD_CMD_PARAMS:  # [V135 F3] 统一常量
                continue
            # 检查参数是否在代码块外有解释
            content_outside_blocks = re.sub(r'```[\s\S]*?```', '', content)
            param_explained = param in content_outside_blocks or param.lstrip('-') in content_outside_blocks.lower()
            if not param_explained:
                # 宽松检查: 参数名是否出现在任何位置
                param_name = param.lstrip('-')
                if param_name not in content.lower():
                    errors.append(f"命令参数'{param}'在代码块中使用但未在skill中解释")
    
    return (FAIL if errors else PASS, errors)


def check_l4_error_recovery(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L4-3: 错误恢复可操作性检查
    
    错误处理不仅是列出来,还要有可执行的恢复步骤:
    - 每个错误场景有具体的恢复操作（不是"重试"这种空话）
    - 恢复操作包含动作动词
    """
    errors = []
    
    err_content = extract_section(content, '错误处理')
    if not err_content:
        # 也检查"异常处理"
        err_content = extract_section(content, '异常处理')
    if not err_content:
        return (FAIL, ["缺少## 错误处理章节"])
    
    # 检查表格格式的错误处理
    has_table = '|' in err_content and '---' in err_content
    
    if has_table:
        # 解析表格行
        lines = [l for l in err_content.split('\n') if l.strip().startswith('|') and '---' not in l]
        if len(lines) < 2:  # 至少表头+1行
            return (FAIL, ["错误处理表格无数据行"])
        
        # 检查表头是否包含必要列
        header = lines[0].lower()
        has_scenario = any(kw in header for kw in TABLE_HEADER_SCENARIO_KEYWORDS)  # [V135 F3] 统一常量
        has_solution = any(kw in header for kw in TABLE_HEADER_SOLUTION_KEYWORDS)  # [V135 F3] 统一常量
        
        if not has_scenario:
            errors.append("错误处理表格缺少'错误场景'列")
        if not has_solution:
            errors.append("错误处理表格缺少'处理方式'列")
        
        # 检查每个错误处理条目是否有具体可执行的恢复步骤
        # 注意: "检查"和"确认"在中文中是动作动词(如"检查输入格式"),不是空话
        # 真正的空话是仅有"重试"/"稍后"等无具体对象的词
        vague_solutions = VAGUE_SOLUTIONS  # [V134 E6] 统一使用skill_core.rules.VAGUE_SOLUTIONS
        action_verbs = ACTION_VERBS  # [V134 E6] 统一使用skill_core.rules.ACTION_VERBS
        
        data_rows = lines[1:]  # 跳过表头
        vague_count = 0
        for row in data_rows:
            cells = [c.strip() for c in row.split('|')[1:-1]]  # 去掉首尾空cell
            if len(cells) < 2:
                continue
            
            solution_cell = cells[-1]  # 最后一列通常是处理方式
            
            # 检查是否只有空话无具体操作
            has_vague = any(v in solution_cell for v in vague_solutions)
            has_action = any(v in solution_cell.lower() for v in action_verbs)
            
            if has_vague and not has_action:
                vague_count += 1
        
        if vague_count > 0:
            errors.append(f"{vague_count}个错误处理条目仅有空话(如'重试')无具体可执行操作")
    
    else:
        # 非表格格式,检查###标题或bullet列表
        h3_titles = extract_h3_titles(err_content)
        bullets = re.findall(r'^[-*]\s+(.+)$', err_content, re.MULTILINE)
        
        total_items = len(h3_titles) + len(bullets)
        if total_items < 3:
            errors.append(f"错误处理仅{total_items}个条目,需要>=3个错误场景")
        
        # 检查每个条目是否有处理方式
        all_items = h3_titles + [b[:50] for b in bullets]
        for item in all_items:
            # 在err_content中查找该条目的上下文
            item_context = ''
            if item in err_content:
                idx = err_content.find(item)
                item_context = err_content[idx:idx+300]
            
            has_solution = any(kw in item_context for kw in ERROR_SOLUTION_KEYWORDS)  # [V135 F3] 统一常量
            if not has_solution:
                errors.append(f"错误条目'{item[:30]}'缺少处理方式描述")
    
    return (FAIL if errors else PASS, errors)


def check_l4_dependency_closure(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L4-4: 依赖闭环性检查
    
    用户按依赖说明能否完整配置环境:
    - LLM依赖有具体能力要求(不只是"需要LLM")
    - API Key有获取步骤(不只是"需要API Key")
    - 运行环境有明确版本要求
    """
    errors = []
    
    dep_content = extract_section(content, '依赖说明')
    if not dep_content:
        return (FAIL, ["缺少## 依赖说明章节"])
    
    # 检查LLM依赖描述是否具体
    has_llm_mention = any(kw in dep_content for kw in LLM_MENTION_KEYWORDS)  # [V135 F3] 统一常量
    # V148 T3: 检测否定语义(如"无需LLM"、"不依赖AI"等),避免误报
    has_no_llm = any(neg in dep_content for neg in ['无需', '不需要', '不依赖', '不使用', '无需LLM', 'no LLM', 'without LLM']) \
                 and any(kw in dep_content for kw in LLM_MENTION_KEYWORDS)
    if has_llm_mention and not has_no_llm:
        # LLM依赖是否具体(不只是"需要LLM支持")
        llm_specific = any(kw in dep_content for kw in LLM_SPECIFIC_KEYWORDS)  # [V135 F3] 统一常量
        if not llm_specific:
            errors.append("LLM依赖描述过于笼统(仅说'需要LLM'),未说明需要什么能力")
    
    # 检查API Key获取说明
    has_api_mention = any(kw in dep_content for kw in API_MENTION_KEYWORDS)  # [V135 F3] 统一常量
    has_no_api = '无需' in dep_content and ('API' in dep_content or 'Key' in dep_content or '密钥' in dep_content)
    
    if has_api_mention and not has_no_api:
        # API Key是否给出获取步骤
        has_acquisition = any(kw in dep_content for kw in API_ACQUISITION_KEYWORDS)  # [V135 F3] 统一常量
        if not has_acquisition:
            errors.append("声明需要API Key但未给出获取步骤(官网链接/注册流程)")
        
        # API Key是否说明配置方式
        has_config = any(kw in dep_content for kw in API_CONFIG_KEYWORDS)  # [V135 F3] 统一常量
        if not has_config:
            errors.append("声明需要API Key但未说明配置方式(环境变量/配置文件)")
    
    # 检查运行环境是否明确
    has_env = any(kw in dep_content for kw in ENV_MENTION_KEYWORDS)  # [V135 F3] 统一常量
    if has_env:
        # 是否有具体平台要求
        env_specific = any(kw in dep_content for kw in ENV_SPECIFIC_KEYWORDS)  # [V135 F3] 统一常量
        if not env_specific:
            errors.append("运行环境描述过于笼统,未指定具体支持的平台")
    
    return (FAIL if errors else PASS, errors)


def check_l4_output_clarity(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L4-5: 输出标准明确性检查
    
    每个能力是否有明确的成功输出描述:
    - 有输出格式说明(JSON/CSV/Markdown/文本)
    - 有输出内容描述(返回什么数据)
    - 有成功/失败判断标准
    """
    errors = []
    
    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return (FAIL, ["无法找到## 核心能力章节"])
    
    # 检查整个skill是否有输出格式说明
    has_output_format = any(kw in content for kw in OUTPUT_FORMAT_KEYWORDS)  # [V135 F3] 统一常量
    
    if not has_output_format:
        errors.append("skill未说明输出格式(JSON/CSV/Markdown/文本),Agent无法判断输出标准")
    
    # 检查使用流程/使用规范中是否有结果处理说明
    usage_content = ''
    for sec in USAGE_SECTION_NAMES:  # [V135 F3] 统一常量
        c = extract_section(content, sec)
        if c:
            usage_content = c
            break
    
    if usage_content:
        # 检查是否有结果处理/输出处理说明
        has_result_handling = any(kw in usage_content for kw in RESULT_HANDLING_KEYWORDS)  # [V135 F3] 统一常量
        if not has_result_handling:
            errors.append("使用流程中未说明结果处理方式,用户不知道执行后会得到什么")
    
    # 检查核心能力中是否有成功标准 (只检查能力点标题,跳过元信息标题)
    h3_titles = extract_h3_titles(cap_content)
    h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_content, re.MULTILINE))
    capability_matches = [m for m in h3_matches 
                         if not any(nc in m.group(1) for nc in NON_CAPABILITY_HEADINGS)]
    
    no_output_count = 0
    for i, match in enumerate(capability_matches):
        title = match.group(1).strip()
        start = match.end()
        end = capability_matches[i + 1].start() if i + 1 < len(capability_matches) else len(cap_content)
        section = cap_content[start:end].strip()
        
        # 检查该能力是否有输出描述
        has_output = any(kw in section.lower() for kw in CAPABILITY_OUTPUT_KEYWORDS)  # [V135 F3] 统一常量
        
        if not has_output:
            no_output_count += 1
    
    capability_count = len(capability_matches)
    if no_output_count > 0 and capability_count > 0:
        ratio = no_output_count / capability_count
        if ratio > 0.5:
            errors.append(f"{no_output_count}/{capability_count}个核心能力缺少输出描述,Agent无法判断任务是否完成")
    
    return (FAIL if errors else PASS, errors)


def check_l4_user_experience(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L4-6: 用户体验完整性检查
    
    从用户角度能否顺利使用:
    - 使用流程是线性的(第一步→第二步→第三步)
    - 有FAQ解决常见疑问
    - -free版本有升级提示
    - 有已知限制说明
    """
    errors = []
    
    slug = fm_data.get('slug', '')
    is_free = slug.endswith('-free')
    
    # 检查使用流程是否线性（有"第一步"、"第二步"或编号步骤）
    usage_content = ''
    for sec in USAGE_SECTION_NAMES:  # [V135 F3] 统一常量
        c = extract_section(content, sec)
        if c:
            usage_content = c
            break
    
    if usage_content:
        # 检查是否是线性步骤
        has_linear_steps = bool(re.search(r'第[一二三四五六七八九十]步', usage_content)) or \
                          bool(re.search(r'^\d+\.\s', usage_content, re.MULTILINE)) or \
                          bool(re.search(r'Step\s+\d+', usage_content, re.IGNORECASE))
        
        if not has_linear_steps:
            errors.append("使用流程非线性(缺少'第一步/第二步'或编号步骤),用户可能不知道执行顺序")
    
    # 检查FAQ
    has_faq = any(kw in content for kw in FAQ_KEYWORDS)  # [V135 F3] 统一常量
    if not has_faq:
        errors.append("缺少FAQ章节,用户常见疑问无法自助解决")
    
    # -free版本检查升级提示
    if is_free:
        has_upgrade = any(kw in content for kw in UPGRADE_KEYWORDS)  # [V135 F3] 统一常量
        if not has_upgrade:
            errors.append("免费版缺少升级提示,用户不知道有完整版可用")
    
    # 检查已知限制
    has_limitations = any(kw in content for kw in LIMITATIONS_KEYWORDS)  # [V135 F3] 统一常量
    if not has_limitations:
        errors.append("缺少已知限制章节,用户可能误用skill能力范围")
    
    return (FAIL if errors else PASS, errors)


def check_l4_task_gate(slug: str) -> dict:
    """对单个skill执行L4任务完成能力验证"""
    skill_path = PACKAGED_SKILLS_DIR / slug / 'SKILL.md'
    
    if not skill_path.exists():
        return {
            'slug': slug,
            'verdict': FAIL,
            'overall_score': 0,
            'checks': {},
            'errors': [f"SKILL.md not found: {skill_path}"],
            'rejection_report': [],
        }
    
    content = skill_path.read_text(encoding='utf-8')
    fm_data = parse_frontmatter(content)['fields']
    
    # 执行所有检查
    checks = {}
    all_errors = []
    
    for check_id, check_func, check_name in [
        ('L4-1', check_l4_task_mapping, '任务可映射性'),
        ('L4-2', check_l4_command_executability, '命令可执行性'),
        ('L4-3', check_l4_error_recovery, '错误恢复可操作性'),
        ('L4-4', check_l4_dependency_closure, '依赖闭环性'),
        ('L4-5', check_l4_output_clarity, '输出标准明确性'),
        ('L4-6', check_l4_user_experience, '用户体验完整性'),
    ]:
        status, errors = check_func(content, fm_data)
        checks[check_id] = {
            'name': check_name,
            'status': status,
            'errors': errors,
        }
        all_errors.extend(errors)
    
    # 总体判定: 所有检查必须PASS才能通过
    fail_count = sum(1 for c in checks.values() if c['status'] == FAIL)
    
    if fail_count == 0:
        verdict = PASS
        overall_score = 100
    elif fail_count <= 1:
        verdict = WARN
        overall_score = sum(1 for c in checks.values() if c['status'] == PASS) * 100 // len(checks)
    else:
        verdict = FAIL
        overall_score = sum(1 for c in checks.values() if c['status'] == PASS) * 100 // len(checks)
    
    # 生成打回报告
    rejection_report = []
    if verdict == FAIL:
        for check_id, check in checks.items():
            if check['status'] == FAIL:
                for err in check['errors']:
                    rejection_report.append(f"[{check_id} {check['name']}] {err}")
    
    return {
        'slug': slug,
        'verdict': verdict,
        'overall_score': overall_score,
        'checks': checks,
        'errors': all_errors,
        'rejection_report': rejection_report,
    }


def main():
    parser = argparse.ArgumentParser(description='L4 任务完成能力验证关卡')
    parser.add_argument('slug', nargs='?', help='Skill slug to check')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--batch', action='store_true', help='Batch check all skills')
    parser.add_argument('--limit', type=int, default=0, help='Limit batch size')
    parser.add_argument('--output', type=str, default='', help='Output JSON results to file')
    args = parser.parse_args()
    
    if args.batch:
        # Batch mode
        all_skills = sorted([d.name for d in PACKAGED_SKILLS_DIR.iterdir() 
                           if d.is_dir() and (d / 'SKILL.md').exists()])
        if args.limit > 0:
            all_skills = all_skills[:args.limit]
        
        print(f"L4批量验证: {len(all_skills)}个skill")
        print(f"{'='*80}")
        
        results = []
        pass_count = 0
        fail_count = 0
        warn_count = 0
        
        # 统计各维度失败情况
        dim_fail_counts = {f'L4-{i}': 0 for i in range(1, 7)}
        
        for i, slug in enumerate(all_skills):
            result = check_l4_task_gate(slug)
            results.append(result)
            
            if result['verdict'] == PASS:
                pass_count += 1
            elif result['verdict'] == WARN:
                warn_count += 1
            else:
                fail_count += 1
            
            # 统计各维度失败
            for check_id in dim_fail_counts:
                if result['checks'].get(check_id, {}).get('status') == FAIL:
                    dim_fail_counts[check_id] += 1
            
            if (i + 1) % 50 == 0:
                print(f"  进度: {i+1}/{len(all_skills)} (PASS={pass_count}, WARN={warn_count}, FAIL={fail_count})")
        
        total = len(results)
        print(f"\n{'='*80}")
        print(f"L4 批量验证结果")
        print(f"{'='*80}")
        print(f"总数: {total}")
        print(f"通过: {pass_count} ({pass_count*100//total}%)")
        print(f"警告: {warn_count} ({warn_count*100//total}%)")
        print(f"不通过: {fail_count} ({fail_count*100//total}%)")
        
        print(f"\n各维度失败统计:")
        dim_names = {
            'L4-1': '任务可映射性',
            'L4-2': '命令可执行性',
            'L4-3': '错误恢复可操作性',
            'L4-4': '依赖闭环性',
            'L4-5': '输出标准明确性',
            'L4-6': '用户体验完整性',
        }
        for did, dname in dim_names.items():
            cnt = dim_fail_counts[did]
            print(f"  {did} {dname}: {cnt}个失败 ({cnt*100//total}%)")
        
        # 输出不通过的skill列表
        failures = [r for r in results if r['verdict'] == FAIL]
        if failures:
            print(f"\n{'='*80}")
            print(f"不通过skill列表 ({len(failures)}个) - 需打回重做")
            print(f"{'='*80}")
            for f in failures[:30]:
                print(f"\n  {f['slug']} (score={f['overall_score']}):")
                for report in f['rejection_report'][:5]:
                    print(f"    - {report}")
        
        # 保存结果到文件
        if args.output:
            output_path = Path(args.output)
            output_data = {
                'summary': {
                    'total': total,
                    'pass': pass_count,
                    'warn': warn_count,
                    'fail': fail_count,
                    'pass_rate': f"{pass_count*100//total}%",
                    'dim_fail_counts': dim_fail_counts,
                },
                'results': results,
            }
            output_path.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"\n结果已保存: {output_path}")
    
    elif args.slug:
        result = check_l4_task_gate(args.slug)
        
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"\n{'='*80}")
            print(f"L4 任务完成能力验证: {args.slug}")
            print(f"{'='*80}")
            print(f"判定: {result['verdict']}")
            print(f"得分: {result['overall_score']}/100")
            print()
            
            for check_id, check in result['checks'].items():
                status_icon = '✓' if check['status'] == PASS else ('⚠' if check['status'] == WARN else '✗')
                print(f"  {status_icon} {check_id} {check['name']}: {check['status']}")
                for e in check['errors']:
                    print(f"      - {e}")
            
            if result['verdict'] == FAIL:
                print(f"\n{'='*80}")
                print(f"打回报告: 此skill无法高质量完成任务,需重新生成/修改/包装")
                print(f"{'='*80}")
                for report in result['rejection_report']:
                    print(f"  - {report}")
            elif result['verdict'] == WARN:
                print(f"\n{'='*80}")
                print(f"警告: 存在质量风险,建议修改后再上传")
                print(f"{'='*80}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
