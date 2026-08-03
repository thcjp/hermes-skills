#!/usr/bin/env python3
"""
L3 功能验证检查器 (Functional Verification Gate)
=================================================

上传平台前的最后一道关卡。检查skill是否能够按预期顺利、高质量完成任务。
如果验证不通过，标记为"不通过"，打回上一个步骤重新生成/修改/包装。

验证维度:
  L3-1 结构完整性: 必需章节齐全且格式正确
  L3-2 能力可执行性: 每个###能力点有足够详细的操作指令
  L3-3 场景覆盖率: 声明的使用场景有对应能力支撑
  L3-4 指令清晰度: Agent/用户能按指令完成任务
  L3-5 错误处理完整性: 已知错误场景有对应处理方案
  L3-6 依赖准确性: 依赖项与skill实际需求匹配
  L3-7 内容实质性: 非模板套话,有具体技术细节

Usage:
    python l3_function_checker.py <slug>
    python l3_function_checker.py <slug> --json
    python l3_function_checker.py --batch --limit 50
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
from skill_core.rules import PLACEHOLDER_PATTERNS, MAX_DISPLAY_NAME_LEN, MAX_SUMMARY_LEN  # v1.3: 统一占位符检测模式+displayName长度阈值; MAX_SUMMARY_LEN
from skill_core.rules import TEMPLATE_PHRASES, NON_CAPABILITY_HEADINGS, PASS, FAIL, WARN, ACTION_VERBS  # V104 W1/W2/W3: 统一常量; V134 E6: ACTION_VERBS统一(消除内联重复)

# V104 W1/W2/W3: TEMPLATE_PHRASES/NON_CAPABILITY_HEADINGS/PASS/FAIL/WARN已统一到skill_core.rules

# 通用占位符 (v1.3: 已统一为 from skill_core.rules import PLACEHOLDER_PATTERNS)
# 原本地定义已移除，使用规范源

# 必需章节
REQUIRED_SECTIONS = {
    '依赖说明': '## 依赖说明',
    '核心能力': '## 核心能力',
    '错误处理': '## 错误处理',
}


def check_l3_structure(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L3-1: 结构完整性检查"""
    errors = []
    
    # 检查frontmatter
    required_fm = ['slug', 'name', 'version', 'displayName', 'summary', 'license', 'description', 'tools']
    for field in required_fm:
        if field not in fm_data:
            errors.append(f"frontmatter缺少字段: {field}")
    
    # 检查displayName长度
    display_name = fm_data.get('displayName', '')
    if len(display_name) > MAX_DISPLAY_NAME_LEN:
        errors.append(f"displayName过长({len(display_name)}字符),应<={MAX_DISPLAY_NAME_LEN}: {display_name}")
    
    # 检查summary长度
    summary = fm_data.get('summary', '')
    if len(summary) > MAX_SUMMARY_LEN:
        errors.append(f"summary过长({len(summary)}字符),应<=100")
    
    # 检查必需章节
    for section_name, section_marker in REQUIRED_SECTIONS.items():
        if section_marker not in content:
            errors.append(f"缺少必需章节: {section_name}")
    
    # 检查slug == name
    slug = fm_data.get('slug', '')
    name = fm_data.get('name', '')
    if slug != name:
        errors.append(f"slug({slug}) != name({name})")
    
    return (FAIL if errors else PASS, errors)


def check_l3_actionable(content: str) -> Tuple[str, List[str]]:
    """L3-2: 能力可执行性检查 - 每个###能力点是否有足够详细的操作指令"""
    errors = []
    
    # V104 W2: NON_CAPABILITY_HEADINGS已从skill_core.rules导入(模块级)
    
    # 提取核心能力章节
    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return (FAIL, ["无法找到## 核心能力章节"])
    
    # 移除代码块（避免代码块内的###被误计）
    cap_no_code = re.sub(r'```[\s\S]*?```', '', cap_content)
    
    # 提取###标题
    h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_no_code, re.MULTILINE))
    if len(h3_matches) < 3:
        errors.append(f"核心能力仅{len(h3_matches)}个###标题,需要>=3")
        return (FAIL, errors)
    
    # 过滤掉非能力点标题
    capability_matches = [m for m in h3_matches 
                         if not any(nc in m.group(1) for nc in NON_CAPABILITY_HEADINGS)]
    
    if len(capability_matches) < 3:
        errors.append(f"核心能力仅{len(capability_matches)}个能力点###标题(排除元信息后),需要>=3")
        return (FAIL, errors)
    
    # 检查每个能力点标题下的内容是否足够详细
    for i, match in enumerate(capability_matches):
        title = match.group(1).strip()
        start = match.end()
        end = capability_matches[i + 1].start() if i + 1 < len(capability_matches) else len(cap_no_code)
        section_content = cap_no_code[start:end].strip()
        
        # 每个能力点至少要有50字符的描述
        if len(section_content) < 50:
            errors.append(f"能力点'{title}'描述过短({len(section_content)}字符),需要>=50")
        
        # 检查是否有具体操作指令（动词、代码引用、参数等）
        has_code_ref = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', section_content))
        has_table = '|' in section_content and '---' in section_content
        has_code_block = '```' in cap_content[start:end]  # 检查原始内容中的代码块
        has_numbered = bool(re.search(r'^\d+\.', section_content, re.MULTILINE))
        has_bullets = bool(re.search(r'^[-*]\s', section_content, re.MULTILINE))
        has_action_verb = any(v in section_content for v in ACTION_VERBS)  # [V134 E6] 统一使用skill_core.rules.ACTION_VERBS(消除55元素内联重复)
        
        detail_indicators = sum([has_code_ref, has_table, has_code_block, has_numbered, has_bullets, has_action_verb])
        if detail_indicators < 2:
            errors.append(f"能力点'{title}'缺乏具体操作指令(代码/表格/列表/动词),仅有{detail_indicators}个指示符")
    
    return (FAIL if errors else PASS, errors)


def check_l3_scenario_coverage(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L3-3: 场景覆盖率检查 - 声明的使用场景有对应能力支撑"""
    errors = []
    
    # 从description和summary中提取关键能力词
    description = fm_data.get('description', '')
    summary = fm_data.get('summary', '')
    combined = f"{summary} {description}"
    
    # 提取核心能力标题
    cap_content = extract_section(content, '核心能力')
    if not cap_content:
        return (WARN, ["无法检查场景覆盖率: 缺少核心能力章节"])
    
    cap_no_code = re.sub(r'```[\s\S]*?```', '', cap_content)
    h3_titles = re.findall(r'^###\s+(.+)$', cap_no_code, re.MULTILINE)
    
    # 检查description中提到的关键功能是否在核心能力中有对应
    # V148 T4: 优化关键词提取 — 使用滑动窗口方法处理中文,
    # 对>4字符的中文序列提取4字符窗口进行部分匹配,避免句子片段误报;
    # 使用百分比阈值(>50%缺失才报错)替代绝对计数,适应不同长度description
    _STOPWORDS = {'这是一个', '用于', '它是', '可以', '通过', '包括', '方面',
                  '提供', '帮助', '自动', '检测', '这是', '它的', '能够',
                  '用于验证', '完整的', '这是一个用于', '帮助开发者',
                  'the', 'and', 'for', 'with', 'from', 'this', 'that',
                  'will', 'can', 'has', 'have', 'are', 'not',
                  'but', 'all', 'any', 'was', 'were', 'been', 'into'}
    desc_keywords_raw = re.findall(r'[\u4e00-\u9fff]{4,8}|[A-Za-z]{4,20}', combined)
    desc_keywords = [kw for kw in desc_keywords_raw
                    if kw not in _STOPWORDS and kw.lower() not in _STOPWORDS]
    cap_text = ' '.join(h3_titles).lower()
    cap_content_lower = cap_content.lower()

    missing_keywords = []
    for kw in desc_keywords:
        if len(kw) >= 4:
            # V148 T4: 对中文关键词使用滑动窗口部分匹配
            if re.fullmatch(r'[\u4e00-\u9fff]+', kw) and len(kw) > 4:
                # 提取4字符滑动窗口,只要有一个窗口匹配就视为通过
                windows = [kw[i:i+4] for i in range(len(kw) - 3)]
                found = any(w.lower() in cap_text or w.lower() in cap_content_lower
                           for w in windows)
                if not found:
                    missing_keywords.append(kw)
            else:
                # 英文关键词或正好4字符的中文词:直接匹配
                if kw.lower() not in cap_text and kw.lower() not in cap_content_lower:
                    missing_keywords.append(kw)

    # V148 T4: 使用百分比阈值 — >50%的关键词缺失才报错(替代绝对计数>5)
    total_keywords = len(desc_keywords)
    missing_ratio = len(missing_keywords) / total_keywords if total_keywords > 0 else 0
    if missing_ratio > 0.5 and len(missing_keywords) > 5:
        errors.append(f"description中的关键词在核心能力中未出现: {missing_keywords[:5]}...")
    
    return (FAIL if errors else PASS, errors)


def check_l3_instruction_clarity(content: str) -> Tuple[str, List[str]]:
    """L3-4: 指令清晰度检查 - Agent/用户能按指令完成任务"""
    errors = []
    
    # 检查是否有使用流程/使用规范/使用方法章节
    has_usage = any(x in content for x in ['## 使用流程', '## 使用规范', '## 使用方法', '## 使用指南', '## 快速开始', '## Quick Start', '## Getting Started'])
    if not has_usage:
        errors.append("缺少使用流程/使用规范/快速开始章节,用户无法知道如何使用")
    
    # 检查是否有示例/案例
    has_example = any(x in content for x in ['## 示例', '## 案例', '## Example', '## Examples', '### 示例', '### 案例'])
    if not has_example:
        errors.append("缺少示例/案例章节,用户无法看到具体使用效果")
    
    # 检查是否有已知限制
    has_limitations = any(x in content for x in ['## 已知限制', '## 限制', '## Limitations'])
    if not has_limitations:
        errors.append("缺少已知限制章节,用户可能误用skill")
    
    # 检查核心能力章节是否有代码示例或命令
    cap_content = extract_section(content, '核心能力')
    if cap_content:
        has_code_in_cap = '```' in cap_content or bool(re.search(r'`[a-zA-Z_]', cap_content))
        has_table_in_cap = '|' in cap_content and '---' in cap_content
        if not has_code_in_cap and not has_table_in_cap:
            errors.append("核心能力章节缺乏代码示例或表格,指令不够具体")
    
    return (FAIL if errors else PASS, errors)


def check_l3_error_handling(content: str) -> Tuple[str, List[str]]:
    """L3-5: 错误处理完整性检查"""
    errors = []
    
    # 找到错误处理章节
    err_match = re.search(r'## 错误处理\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if not err_match:
        return (FAIL, ["缺少## 错误处理章节"])
    
    err_content = err_match.group(1)
    
    # 检查是否有表格格式的错误处理
    has_table = '|' in err_content and '---' in err_content
    has_h3 = bool(re.search(r'^###\s+', err_content, re.MULTILINE))
    has_bullets = bool(re.search(r'^[-*]\s', err_content, re.MULTILINE))
    
    if not has_table and not has_h3 and not has_bullets:
        errors.append("错误处理章节缺乏结构化内容(表格/标题/列表)")
    
    # 检查错误处理条目数量
    if has_table:
        # 表格行数（减去表头和分隔行）
        table_rows = [l for l in err_content.split('\n') if l.strip().startswith('|') and '---' not in l]
        if len(table_rows) < 3:
            errors.append(f"错误处理表格仅{len(table_rows)}行(含表头),需要>=3个错误场景")
    elif has_h3:
        h3_count = len(re.findall(r'^###\s+', err_content, re.MULTILINE))
        if h3_count < 3:
            errors.append(f"错误处理仅{h3_count}个###标题,需要>=3个错误场景")
    
    # 检查是否有处理方式/解决方案列
    if has_table:
        if '处理' not in err_content and '解决' not in err_content and '修复' not in err_content and '方式' not in err_content:
            errors.append("错误处理表格缺少'处理方式'或'解决方案'列")
    
    return (FAIL if errors else PASS, errors)


def check_l3_dependency_accuracy(content: str, fm_data: dict) -> Tuple[str, List[str]]:
    """L3-6: 依赖准确性检查"""
    errors = []
    
    # 找到依赖说明章节
    dep_match = re.search(r'## 依赖说明\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if not dep_match:
        return (FAIL, ["缺少## 依赖说明章节"])
    
    dep_content = dep_match.group(1)
    
    # 检查是否包含LLM依赖
    has_llm = 'LLM' in dep_content or 'llm' in dep_content or 'AI' in dep_content or 'Agent' in dep_content
    if not has_llm:
        errors.append("依赖说明中未提及LLM/AI依赖(几乎所有skill都需要)")
    
    # 检查是否有运行环境
    has_env = any(x in dep_content for x in ['运行环境', '操作系统', 'Windows', 'macOS', 'Linux', 'Agent平台'])
    if not has_env:
        errors.append("依赖说明中未提及运行环境(操作系统/Agent平台)")
    
    # 检查是否有API Key配置说明
    has_api_key = 'API Key' in dep_content or 'API密钥' in dep_content or '无需' in dep_content or 'API key' in dep_content
    if not has_api_key:
        errors.append("依赖说明中未说明API Key配置要求(或明确声明无需)")
    
    # 检查是否有可用性分类
    has_classification = 'MD' in dep_content or 'EXEC' in dep_content or '可用性分类' in dep_content
    if not has_classification:
        errors.append("依赖说明中缺少可用性分类(MD/EXEC)")
    
    # 检查tools字段与依赖是否匹配
    tools = fm_data.get('tools', [])
    if isinstance(tools, list):
        has_exec = 'exec' in str(tools).lower()
        has_read = 'read' in str(tools).lower()
    else:
        has_exec = 'exec' in str(tools).lower()
        has_read = 'read' in str(tools).lower()
    
    # 如果有exec tool但依赖说明说纯MD，或反之，是矛盾
    if has_exec and 'MD（纯Markdown' in dep_content and 'EXEC' not in dep_content:
        errors.append("tools包含exec但依赖说明声称纯Markdown,存在矛盾")
    
    return (FAIL if errors else PASS, errors)


def check_l3_substance(content: str) -> Tuple[str, List[str]]:
    """L3-7: 内容实质性检查 - 非模板套话"""
    errors = []
    
    # 检查模板套话
    for phrase in TEMPLATE_PHRASES:
        if phrase in content:
            errors.append(f"包含模板套话: '{phrase[:30]}...'")
    
    # 检查占位符 (v1.3: PLACEHOLDER_PATTERNS为元组列表(regex, desc))
    for pattern, desc in PLACEHOLDER_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"包含占位符({desc}): {matches[:3]}")
    
    # 检查"触发关键词"
    if '触发关键词' in content:
        errors.append("包含'触发关键词'(模板残留)")
    
    # 检查内容总长度（太短说明内容不充实）
    body_start = content.find('---', 4)  # 跳过frontmatter
    if body_start > 0:
        body = content[body_start:]
    else:
        body = content
    
    if len(body) < 1000:
        errors.append(f"内容过短({len(body)}字符),可能不够充实(需要>=1000)")
    
    # 检查核心能力章节的实质性
    cap_content = extract_section(content, '核心能力')
    if cap_content:
        # 核心能力章节应至少300字符
        if len(cap_content) < 300:
            errors.append(f"核心能力章节内容过短({len(cap_content)}字符),需要>=300")
        
        # 检查是否有反引号代码引用（技术细节标志）
        has_code_refs = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', cap_content))
        has_table = '|' in cap_content and '---' in cap_content
        has_code_block = '```' in cap_content
        
        if not has_code_refs and not has_table and not has_code_block:
            errors.append("核心能力章节缺乏技术细节(代码引用/表格/代码块)")
    
    # 检查是否引用开源仓库
    repo_patterns = [
        r'github\.com/', r'gitlab\.com/', r'gitee\.com/',
        r'原始仓库', r'开源仓库', r'上游项目',
    ]
    for pattern in repo_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            errors.append(f"包含开源仓库引用: {pattern}")
            break
    
    return (FAIL if errors else PASS, errors)


def check_l3_function(slug: str) -> dict:
    """对单个skill执行L3功能验证"""
    skill_path = PACKAGED_SKILLS_DIR / slug / 'SKILL.md'
    
    if not skill_path.exists():
        return {
            'slug': slug,
            'verdict': FAIL,
            'overall_score': 0,
            'checks': {},
            'errors': [f"SKILL.md not found: {skill_path}"],
        }
    
    content = skill_path.read_text(encoding='utf-8')
    fm_data = parse_frontmatter(content)['fields']
    
    # 执行所有检查
    checks = {}
    all_errors = []
    
    for check_id, check_func, check_name in [
        ('L3-1', check_l3_structure, '结构完整性'),
        ('L3-2', check_l3_actionable, '能力可执行性'),
        ('L3-3', check_l3_scenario_coverage, '场景覆盖率'),
        ('L3-4', check_l3_instruction_clarity, '指令清晰度'),
        ('L3-5', check_l3_error_handling, '错误处理完整性'),
        ('L3-6', check_l3_dependency_accuracy, '依赖准确性'),
        ('L3-7', check_l3_substance, '内容实质性'),
    ]:
        status, errors = check_func(content, fm_data) if check_id in ['L3-1', 'L3-3', 'L3-6'] else check_func(content)
        checks[check_id] = {
            'name': check_name,
            'status': status,
            'errors': errors,
        }
        all_errors.extend(errors)
    
    # 总体判定: 所有检查必须PASS才能通过
    critical_checks = ['L3-1', 'L3-2', 'L3-5', 'L3-6', 'L3-7']  # 关键检查项
    critical_fail = any(checks[cid]['status'] == FAIL for cid in critical_checks)
    warning_checks = ['L3-3', 'L3-4']  # 警告检查项
    warning_fail = any(checks[cid]['status'] == FAIL for cid in warning_checks)
    
    if critical_fail:
        verdict = FAIL
        overall_score = sum(1 for c in checks.values() if c['status'] == PASS) * 100 // len(checks)
    elif warning_fail:
        verdict = WARN
        overall_score = sum(1 for c in checks.values() if c['status'] == PASS) * 100 // len(checks)
    else:
        verdict = PASS
        overall_score = 100
    
    return {
        'slug': slug,
        'verdict': verdict,
        'overall_score': overall_score,
        'checks': checks,
        'errors': all_errors,
    }


def main():
    parser = argparse.ArgumentParser(description='L3 功能验证检查器')
    parser.add_argument('slug', nargs='?', help='Skill slug to check')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--batch', action='store_true', help='Batch check all skills')
    parser.add_argument('--limit', type=int, default=0, help='Limit batch size')
    args = parser.parse_args()
    
    if args.batch:
        # Batch mode
        all_skills = sorted([d.name for d in PACKAGED_SKILLS_DIR.iterdir() if d.is_dir() and (d / 'SKILL.md').exists()])
        if args.limit > 0:
            all_skills = all_skills[:args.limit]
        
        print(f"Batch checking {len(all_skills)} skills...")
        results = []
        pass_count = 0
        fail_count = 0
        warn_count = 0
        
        for i, slug in enumerate(all_skills):
            result = check_l3_function(slug)
            results.append(result)
            if result['verdict'] == PASS:
                pass_count += 1
            elif result['verdict'] == WARN:
                warn_count += 1
            else:
                fail_count += 1
            
            if (i + 1) % 50 == 0:
                print(f"  Progress: {i+1}/{len(all_skills)} (PASS={pass_count}, WARN={warn_count}, FAIL={fail_count})")
        
        print(f"\n{'='*80}")
        print(f"L3 BATCH SUMMARY")
        print(f"{'='*80}")
        print(f"Total: {len(results)}")
        print(f"PASS: {pass_count} ({pass_count*100//len(results)}%)")
        print(f"WARN: {warn_count} ({warn_count*100//len(results)}%)")
        print(f"FAIL: {fail_count} ({fail_count*100//len(results)}%)")
        
        # Show failures
        failures = [r for r in results if r['verdict'] == FAIL]
        if failures:
            print(f"\n{'='*80}")
            print(f"FAILURES ({len(failures)})")
            print(f"{'='*80}")
            for f in failures[:20]:
                print(f"\n  {f['slug']} (score={f['overall_score']}):")
                for check_id, check in f['checks'].items():
                    if check['status'] == FAIL:
                        print(f"    {check_id} {check['name']}: FAIL")
                        for e in check['errors'][:3]:
                            print(f"      - {e}")
    
    elif args.slug:
        result = check_l3_function(args.slug)
        
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"\n{'='*80}")
            print(f"L3 Functional Verification: {args.slug}")
            print(f"{'='*80}")
            print(f"Verdict: {result['verdict']}")
            print(f"Score: {result['overall_score']}/100")
            print()
            
            for check_id, check in result['checks'].items():
                status_icon = '✓' if check['status'] == PASS else ('⚠' if check['status'] == WARN else '✗')
                print(f"  {status_icon} {check_id} {check['name']}: {check['status']}")
                for e in check['errors']:
                    print(f"      - {e}")
            
            if result['errors']:
                print(f"\n{'='*80}")
                if result['verdict'] == FAIL:
                    print(f"ACTION REQUIRED: 打回重新生成/修改/包装")
                elif result['verdict'] == WARN:
                    print(f"WARNING: 建议修改后再上传")
                print(f"{'='*80}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
