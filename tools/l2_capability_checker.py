#!/usr/bin/env python3
"""
L2-Capability 质量检查器 (Capability Quality Checker)
======================================================

检测skill的「能力质量」而非「格式质量」。
解决batch_l2_eval.py的evaluate_r_a_e()只检查关键词存在性、
无法检测内容同质化和信息缺失的问题。

10项能力检查 (每项10分,总分100):
  C1: description_completeness    描述完整性(检测截断)
  C2: core_capability_specificity 核心能力具体性(检测重复summary)
  C3: workflow_concreteness       流程具体性(检测通用步骤)
  C4: error_handling_specificity  异常处理具体性(检测通用3行表)
  C5: example_authenticity        示例真实性(检测"示例数据")
  C6: faq_relevance               FAQ相关性(检测通用Q1/Q2/Q3)
  C7: domain_keyword_coverage     领域关键词覆盖(检测内容与领域无关)
  C8: content_uniqueness          内容独特性(检测模板填充比例)
  C9: chapter_depth               章节深度(检测章节内容过少)
  C10: information_density        信息密度(检测领域实体密度)

Usage:
    python l2_capability_checker.py <skill_md_path>
    python l2_capability_checker.py <skill_md_path> --json
    python l2_capability_checker.py --batch --limit 50
"""

import sys
import re
import json
import hashlib
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime

# 确保能导入skill_registry模块
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection, PACKAGED_SKILLS_DIR


# ============================================================
# 通用模板填充模式 (跨skill完全相同的内容)
# ============================================================

# 通用错误处理表 (3行,所有模板填充skill完全相同)
GENERIC_ERROR_TABLE = [
    '配置错误', '参数缺失或格式错误', '检查依赖说明中的配置要求',
    '运行时错误', '运行环境不满足', '确认运行环境符合依赖说明',
    '网络错误', '连接超时或不可达', '检查网络连接后重试',
]

# 通用FAQ (3个Q,所有模板填充skill完全相同)
GENERIC_FAQ_PATTERNS = [
    r'Q1:\s*如何开始使用',
    r'请先阅读使用流程章节.*确认环境满足依赖说明',
    r'Q2:\s*遇到错误怎么办',
    r'请参考错误处理章节.*按照表格中的处理方式',
    r'Q3:\s*.*有什么限制',
    r'请参考已知限制章节了解具体限制',
]

# 通用适用场景表 (1行,所有模板填充skill完全相同)
GENERIC_SCENARIO_TABLE = [
    '| 场景 | 输入 | 输出 |',
    '|------|------|------|',
    '| 基础使用 | 用户请求 | 处理结果 |',
]

# 通用使用流程 (4步,所有模板填充skill完全相同)
GENERIC_WORKFLOW_STEPS = [
    '确认运行环境满足依赖说明中的要求',
    '根据适用场景选择合适的使用方式',
    '执行操作并检查输出结果',
    '如遇错误，参考错误处理章节',
]

# 通用已知限制 (3条,所有模板填充skill完全相同)
GENERIC_LIMITATIONS = [
    '需要LLM支持，无LLM环境无法使用',
    '复杂场景可能需要人工辅助判断',
    '性能取决于底层模型能力',
]

# 通用依赖说明 (所有模板填充skill完全相同)
GENERIC_DEPENDENCY = [
    '支持SKILL.md的任意AI Agent',
    'Windows / macOS / Linux',
    '由Agent内置LLM提供',
    'MD+EXEC',
]

# 占位符文本 (不应出现在最终输出中)
PLACEHOLDER_TEXTS = [
    '示例数据', '示例输入', '示例内容', '示例输出',
    '待补充', '待填充', '待完善',
    '（根据实际场景填充）', '(根据实际场景填充)',
    '相关信息', '相关说明',
    '处理结果', '用户请求',
]


# ============================================================
# 检查函数
# ============================================================

def parse_skill_md(content: str) -> Dict[str, Any]:
    """解析SKILL.md,分离frontmatter和章节"""
    if content.startswith('\ufeff'):
        content = content[1:]

    result = {
        'frontmatter': {},
        'frontmatter_raw': '',
        'body': '',
        'chapters': {},
        'slug': '',
        'summary': '',
        'description': '',
        'display_name': '',
    }

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            result['frontmatter_raw'] = parts[1]
            result['body'] = parts[2].strip()

            # 简单解析frontmatter
            for line in parts[1].split('\n'):
                if ':' in line and not line.startswith('  '):
                    key, _, val = line.partition(':')
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key == 'slug':
                        result['slug'] = val
                    elif key == 'summary':
                        result['summary'] = val
                    elif key == 'displayName':
                        result['display_name'] = val
                    elif key == 'description' and val and val not in ('|-', '|'):
                        result['description'] = val
                    elif key in result['frontmatter']:
                        pass
                    else:
                        result['frontmatter'][key] = val

            # description可能在多行块中
            if not result['description']:
                desc_match = re.search(r'description:\s*\|-\s*\n(.*?)(?=\n\w+:|\n---|\Z)', parts[1], re.DOTALL)
                if desc_match:
                    result['description'] = desc_match.group(1).strip()
    else:
        result['body'] = content

    # 解析章节
    chapter_pattern = re.compile(r'^## (.+)$', re.MULTILINE)
    chapter_matches = list(chapter_pattern.finditer(result['body']))

    for i, match in enumerate(chapter_matches):
        chapter_name = match.group(1).strip()
        start = match.end()
        end = chapter_matches[i + 1].start() if i + 1 < len(chapter_matches) else len(result['body'])
        chapter_content = result['body'][start:end].strip()
        result['chapters'][chapter_name] = chapter_content

    return result


def extract_domain_keywords(slug: str, summary: str, display_name: str) -> List[str]:
    """从slug/summary/display_name提取领域关键词"""
    keywords = set()

    # 从slug提取 (按-分割)
    for part in slug.split('-'):
        if len(part) > 2 and part not in ('the', 'and', 'for', 'pro', 'free', 'skill', 'tool', 'api'):
            keywords.add(part.lower())

    # 从display_name提取
    for word in display_name.split():
        word_clean = re.sub(r'[^a-zA-Z\u4e00-\u9fff]', '', word).strip()
        if len(word_clean) > 2:
            keywords.add(word_clean.lower())

    # 从summary提取中文词和英文词
    # 中文词(2-4字)
    cn_words = re.findall(r'[\u4e00-\u9fff]{2,4}', summary)
    for w in cn_words:
        if w not in ('核心', '能力', '场景', '工具', '支持', '使用', '提供', '适用'):
            keywords.add(w)

    # 英文词(>3字符)
    en_words = re.findall(r'[a-zA-Z]{4,}', summary)
    for w in en_words:
        if w.lower() not in ('skill', 'tool', 'this', 'that', 'with', 'from', 'your', 'have', 'will'):
            keywords.add(w.lower())

    return list(keywords)


# ============================================================
# 10项能力检查
# ============================================================

def check_c1_description_completeness(parsed: Dict) -> Tuple[int, str]:
    """C1: 描述完整性 - 检测description是否截断"""
    desc = parsed.get('description', '')
    summary = parsed.get('summary', '')

    score = 10
    issues = []

    if not desc:
        score = 0
        return 0, 'description为空'

    # 检测截断: 单词被切断 (如"emotional cu" → 没有完整句子结束)
    # 截断特征: description中有不完整的单词(以辅音结尾,无句号)
    truncated_patterns = [
        r'[a-z]{2,}\s+[a-z]{1,3}$',  # 末尾不完整单词
        r'emotional\s+cu',
        r'designed to\s*$',
        r'Use when\s*\(',
        r'估值建模和风\s*$',  # 中文截断
    ]

    for pattern in truncated_patterns:
        if re.search(pattern, desc, re.MULTILINE):
            score -= 5
            issues.append('检测到截断: %s' % pattern)

    # 检测description是否就是summary的重复
    if desc.strip() == summary.strip():
        score -= 3
        issues.append('description与summary完全相同')

    # 检测description长度过短
    if len(desc) < 50:
        score -= 3
        issues.append('description过短(%d字符)' % len(desc))

    score = max(0, score)
    return score, '; '.join(issues) if issues else '完整'


def find_chapter(chapters: Dict[str, str], keywords: List[str]) -> Tuple[str, str]:
    """灵活查找章节: 返回 (chapter_name, chapter_content)。
    
    匹配顺序:
    1. 精确匹配
    2. 包含关键词的章节名
    3. 章节名包含在关键词中
    """
    # 1. 精确匹配
    for kw in keywords:
        if kw in chapters:
            return kw, chapters[kw]
    
    # 2. 章节名包含任一关键词
    for name, content in chapters.items():
        for kw in keywords:
            if kw in name:
                return name, content
    
    # 3. 关键词包含章节名 (处理章节名更短的情况)
    for name, content in chapters.items():
        for kw in keywords:
            if name in kw:
                return name, content
    
    return '', ''


def check_c2_core_capability_specificity(parsed: Dict) -> Tuple[int, str]:
    """C2: 核心能力具体性 - 检测是否重复summary或只有通用内容"""
    chapter_name, chapter = find_chapter(parsed['chapters'], 
        ['核心能力', '核心功能', 'Core', '能力', '功能', 'Features', 'Capabilities', '主要功能',
         '核心原则', '核心规则', '核心', '原则', '规则'])
    summary = parsed.get('summary', '')

    # Fallback: find chapter with most ### headings (excluding FAQ/error/etc)
    if not chapter:
        max_h3 = 0
        for name, content in parsed['chapters'].items():
            if any(x in name for x in ['常见问题', 'FAQ', '错误', '异常', '依赖', '限制', '案例', '运行环境', '已知']):
                continue
            h3_count = len(re.findall(r'^###\s+', content, re.MULTILINE))
            if h3_count > max_h3:
                max_h3 = h3_count
                chapter = content
                chapter_name = name

    if not chapter:
        return 3, '无核心能力章节'

    score = 10
    issues = []

    # 检测: 核心能力就是summary的重复
    if summary and summary.strip() in chapter:
        score -= 5
        issues.append('核心能力重复summary')

    # 检测: 核心能力只有1-2条
    bullets = [l for l in chapter.split('\n') if l.strip().startswith('-') or l.strip().startswith('*')]
    if len(bullets) <= 1:
        score -= 3
        issues.append('核心能力仅%d条(应≥3条)' % len(bullets))

    # 检测: 触发关键词被截断 (如"估值建模和风")
    trigger_match = re.search(r'触发关键词:\s*(.+)', chapter)
    if trigger_match:
        trigger_text = trigger_match.group(1)
        # 检测中文词被截断 (2字后接非相关字)
        truncated_cn = re.findall(r'[\u4e00-\u9fff]{2,3}(?:和|与)[\u4e00-\u9fff]{1,2}(?:[,，]|$)', trigger_text)
        if truncated_cn:
            for t in truncated_cn:
                if len(re.findall(r'[\u4e00-\u9fff]', t)) < 5:
                    score -= 3
                    issues.append('触发关键词截断: %s' % t)

    # 检测: 核心能力包含通用填充词
    for placeholder in PLACEHOLDER_TEXTS:
        if placeholder in chapter:
            score -= 2
            issues.append('核心能力含占位符: %s' % placeholder)

    score = max(0, score)
    return score, '; '.join(issues) if issues else '具体'


def check_c3_workflow_concreteness(parsed: Dict) -> Tuple[int, str]:
    """C3: 流程具体性 - 检测是否为通用4步流程"""
    chapter_name, chapter = find_chapter(parsed['chapters'],
        ['使用流程', '使用方式', '使用方法', '使用指南', '流程', '使用', '用法', 'Workflow', 'Usage',
         '管线', '步骤', '操作', '工作流'])

    # Fallback: if no workflow chapter found, check if there's a chapter with numbered steps or ### headings
    if not chapter:
        for name, content in parsed['chapters'].items():
            if any(x in name for x in ['常见问题', 'FAQ', '错误', '异常', '依赖', '限制', '案例', '运行环境', '已知']):
                continue
            # Check if chapter has numbered steps (1. 2. 3.) or ### headings (规则一, 步骤一)
            numbered = len(re.findall(r'^\d+\.\s', content, re.MULTILINE))
            h3 = len(re.findall(r'^###\s+', content, re.MULTILINE))
            if numbered >= 2 or h3 >= 2:
                chapter = content
                chapter_name = name
                break

    if not chapter:
        return 3, '无使用流程章节'

    score = 10
    issues = []

    # 检测通用流程步骤
    generic_count = 0
    for step in GENERIC_WORKFLOW_STEPS:
        if step in chapter:
            generic_count += 1

    if generic_count >= 3:
        score -= 7
        issues.append('使用流程为通用模板(%d/%d步匹配)' % (generic_count, len(GENERIC_WORKFLOW_STEPS)))
    elif generic_count >= 1:
        score -= 3
        issues.append('使用流程含通用步骤(%d步)' % generic_count)

    # 检测流程是否有领域具体步骤 (非通用步骤)
    steps = re.findall(r'\d+\.\s*(.+)', chapter)
    domain_steps = [s for s in steps if not any(g in s for g in GENERIC_WORKFLOW_STEPS)]
    if len(domain_steps) == 0 and len(steps) > 0:
        score -= 3
        issues.append('所有流程步骤都是通用的')

    score = max(0, score)
    return score, '; '.join(issues) if issues else '具体'


def check_c4_error_handling_specificity(parsed: Dict) -> Tuple[int, str]:
    """C4: 异常处理具体性 - 检测是否为通用3行错误表"""
    chapter_name, chapter = find_chapter(parsed['chapters'],
        ['异常处理', '错误处理', '错误', '异常', 'Error', 'Troubleshooting'])

    if not chapter:
        return 3, '无异常处理章节'

    score = 10
    issues = []

    # 检测通用错误表
    generic_count = 0
    for pattern in GENERIC_ERROR_TABLE:
        if pattern in chapter:
            generic_count += 1

    if generic_count >= 6:
        score -= 7
        issues.append('异常处理为通用模板(%d/%d关键词匹配)' % (generic_count, len(GENERIC_ERROR_TABLE)))
    elif generic_count >= 3:
        score -= 4
        issues.append('异常处理含通用内容(%d个匹配)' % generic_count)

    # 检测通用边界处理
    if '空输入返回提示信息' in chapter and '超长输入自动截断' in chapter:
        score -= 3
        issues.append('含通用边界处理')

    if '降级策略: 异常时返回默认值' in chapter:
        score -= 2
        issues.append('含通用降级策略')

    score = max(0, score)
    return score, '; '.join(issues) if issues else '具体'


def check_c5_example_authenticity(parsed: Dict) -> Tuple[int, str]:
    """C5: 示例真实性 - 检测"示例数据"等占位符"""
    chapter_name, chapter = find_chapter(parsed['chapters'],
        ['案例展示', '案例', '示例', '实际案例', 'Examples', 'Case', 'Use Cases'])

    if not chapter:
        return 3, '无案例/示例章节'

    score = 10
    issues = []

    # 检测占位符文本
    for placeholder in PLACEHOLDER_TEXTS:
        if placeholder in chapter:
            score -= 3
            issues.append('含占位符: %s' % placeholder)

    # 检测通用JSON示例
    if '"input": "示例输入"' in chapter or '"output": "处理结果"' in chapter:
        score -= 5
        issues.append('含通用JSON示例(示例输入/处理结果)')

    # 检测示例是否有实际领域内容 (非占位符的代码块)
    code_blocks = re.findall(r'```[\w]*\n(.*?)```', chapter, re.DOTALL)
    real_content_blocks = 0
    for block in code_blocks:
        # 排除纯占位符的代码块
        is_placeholder = any(p in block for p in PLACEHOLDER_TEXTS)
        if not is_placeholder and len(block.strip()) > 20:
            real_content_blocks += 1

    if real_content_blocks == 0 and len(code_blocks) > 0:
        score -= 3
        issues.append('所有代码块都是占位符')

    score = max(0, score)
    return score, '; '.join(issues) if issues else '真实'


def check_c6_faq_relevance(parsed: Dict) -> Tuple[int, str]:
    """C6: FAQ相关性 - 检测通用Q1/Q2/Q3"""
    chapter_name, chapter = find_chapter(parsed['chapters'],
        ['常见问题', 'FAQ', '问题', 'Questions', 'Q&A'])

    if not chapter:
        return 3, '无FAQ章节'

    score = 10
    issues = []

    # 检测通用FAQ模式
    generic_count = 0
    for pattern in GENERIC_FAQ_PATTERNS:
        if re.search(pattern, chapter, re.IGNORECASE):
            generic_count += 1

    if generic_count >= 4:
        score -= 7
        issues.append('FAQ为通用模板(%d/%d模式匹配)' % (generic_count, len(GENERIC_FAQ_PATTERNS)))
    elif generic_count >= 2:
        score -= 4
        issues.append('FAQ含通用问题(%d个匹配)' % generic_count)

    score = max(0, score)
    return score, '; '.join(issues) if issues else '相关'


def check_c7_domain_keyword_coverage(parsed: Dict) -> Tuple[int, str]:
    """C7: 领域关键词覆盖 - 检测body中是否包含领域关键词"""
    slug = parsed.get('slug', '')
    summary = parsed.get('summary', '')
    display_name = parsed.get('display_name', '')
    body = parsed.get('body', '')

    keywords = extract_domain_keywords(slug, summary, display_name)

    if not keywords:
        return 5, '无法提取领域关键词'

    score = 10
    issues = []

    # 统计关键词在body中的出现率
    body_lower = body.lower()
    covered = 0
    for kw in keywords:
        if kw.lower() in body_lower:
            covered += 1

    coverage = covered / len(keywords) if keywords else 0

    if coverage < 0.3:
        score = 2
        issues.append('领域关键词覆盖率极低(%.0f%%, %d/%d)' % (coverage * 100, covered, len(keywords)))
    elif coverage < 0.5:
        score = 5
        issues.append('领域关键词覆盖率低(%.0f%%)' % (coverage * 100))
    elif coverage < 0.7:
        score = 7
        issues.append('领域关键词覆盖率中等(%.0f%%)' % (coverage * 100))

    # 检测body是否全是通用内容 (无任何领域关键词在非frontmatter部分)
    # 排除依赖说明等通用章节
    non_generic_body = body
    for chapter_name in ['依赖说明', '运行环境', '可用性分类']:
        if chapter_name in parsed['chapters']:
            non_generic_body = non_generic_body.replace(parsed['chapters'][chapter_name], '')

    domain_kw_in_body = sum(1 for kw in keywords if kw.lower() in non_generic_body.lower())
    if domain_kw_in_body == 0:
        score -= 4
        issues.append('非通用章节中无领域关键词')

    score = max(0, score)
    return score, '; '.join(issues) if issues else '覆盖良好(%.0f%%)' % (coverage * 100)


def check_c8_content_uniqueness(parsed: Dict) -> Tuple[int, str]:
    """C8: 内容独特性 - 检测通用模板填充比例"""
    body = parsed.get('body', '')
    chapters = parsed.get('chapters', {})

    if not body:
        return 0, 'body为空'

    score = 10
    issues = []

    # 统计通用内容占比
    generic_content_length = 0
    total_content_length = len(body)

    # 通用错误处理
    _, error_chapter = find_chapter(chapters, ['异常处理', '错误处理', '错误', '异常', 'Error'])
    if error_chapter:
        generic_in_error = sum(len(p) for p in GENERIC_ERROR_TABLE if p in error_chapter)
        if generic_in_error > 0 and len(error_chapter) > 0:
            ratio = generic_in_error / len(error_chapter)
            if ratio > 0.5:
                generic_content_length += len(error_chapter) * ratio

    # 通用FAQ
    _, faq_chapter = find_chapter(chapters, ['常见问题', 'FAQ', '问题', 'Questions'])
    if faq_chapter:
        generic_faq_count = sum(1 for p in GENERIC_FAQ_PATTERNS if re.search(p, faq_chapter, re.IGNORECASE))
        if generic_faq_count >= 4:
            generic_content_length += len(faq_chapter) * 0.8

    # 通用适用场景
    _, scenario_chapter = find_chapter(chapters, ['适用场景', '场景', '适用', 'Scenarios', 'Use Cases'])
    if scenario_chapter:
        generic_scenario_count = sum(1 for p in GENERIC_SCENARIO_TABLE if p in scenario_chapter)
        if generic_scenario_count >= 2:
            generic_content_length += len(scenario_chapter) * 0.7

    # 通用使用流程
    _, workflow_chapter = find_chapter(chapters, ['使用流程', '使用方式', '使用方法', '流程', '使用', 'Workflow'])
    if workflow_chapter:
        generic_workflow_count = sum(1 for p in GENERIC_WORKFLOW_STEPS if p in workflow_chapter)
        if generic_workflow_count >= 3:
            generic_content_length += len(workflow_chapter) * 0.8

    # 通用已知限制
    _, limit_chapter = find_chapter(chapters, ['已知限制', '限制', 'Limitations', 'Constraints'])
    if limit_chapter:
        generic_limit_count = sum(1 for p in GENERIC_LIMITATIONS if p in limit_chapter)
        if generic_limit_count >= 2:
            generic_content_length += len(limit_chapter) * 0.8

    # 通用依赖说明
    _, dep_chapter = find_chapter(chapters, ['依赖说明', '依赖', 'Dependencies'])
    if dep_chapter:
        generic_dep_count = sum(1 for p in GENERIC_DEPENDENCY if p in dep_chapter)
        if generic_dep_count >= 3:
            generic_content_length += len(dep_chapter) * 0.7

    # 计算通用内容占比
    if total_content_length > 0:
        generic_ratio = generic_content_length / total_content_length

        if generic_ratio > 0.5:
            score = 1
            issues.append('通用内容占比极高(%.0f%%)' % (generic_ratio * 100))
        elif generic_ratio > 0.35:
            score = 3
            issues.append('通用内容占比高(%.0f%%)' % (generic_ratio * 100))
        elif generic_ratio > 0.2:
            score = 6
            issues.append('通用内容占比中等(%.0f%%)' % (generic_ratio * 100))
        elif generic_ratio > 0.1:
            score = 8
            issues.append('通用内容占比低(%.0f%%)' % (generic_ratio * 100))

    score = max(0, score)
    return score, '; '.join(issues) if issues else '独特性良好'


def check_c9_chapter_depth(parsed: Dict) -> Tuple[int, str]:
    """C9: 章节深度 - 检测章节内容是否过少"""
    chapters = parsed.get('chapters', {})

    if not chapters:
        return 0, '无章节'

    score = 10
    issues = []

    # 关键章节列表
    key_chapters = ['核心能力', '适用场景', '使用流程', '异常处理', '案例展示', '常见问题', '已知限制']

    shallow_count = 0
    for chapter_name in key_chapters:
        # 模糊匹配
        matched_name = None
        for cn in chapters:
            if chapter_name in cn or cn in chapter_name:
                matched_name = cn
                break

        if matched_name:
            content = chapters[matched_name]
            lines = [l for l in content.split('\n') if l.strip()]
            if len(lines) < 3:
                shallow_count += 1
                issues.append('%s章节过浅(%d行)' % (matched_name, len(lines)))

    if shallow_count >= 4:
        score = 2
    elif shallow_count >= 3:
        score = 4
    elif shallow_count >= 2:
        score = 6
    elif shallow_count >= 1:
        score = 8

    score = max(0, score)
    return score, '; '.join(issues) if issues else '章节深度良好'


def check_c10_information_density(parsed: Dict) -> Tuple[int, str]:
    """C10: 信息密度 - 检测领域实体密度"""
    body = parsed.get('body', '')
    slug = parsed.get('slug', '')
    summary = parsed.get('summary', '')

    if not body:
        return 0, 'body为空'

    score = 10
    issues = []

    # 统计领域实体 (代码块、命令、技术术语、数据表)
    code_blocks = len(re.findall(r'```[\w]*\n', body))
    commands = len(re.findall(r'`[a-z]{3,}[\w-]*`', body))
    tables = len(re.findall(r'\|.*\|.*\|', body))
    cn_terms = len(re.findall(r'[\u4e00-\u9fff]{4,}', body))

    # 统计通用填充词
    filler_count = 0
    for text in PLACEHOLDER_TEXTS:
        filler_count += body.count(text)
    for text in GENERIC_ERROR_TABLE + GENERIC_WORKFLOW_STEPS + GENERIC_LIMITATIONS:
        if text in body:
            filler_count += 1

    # 计算信息密度
    domain_entities = code_blocks + commands + tables + (cn_terms // 3)
    total_content = len(body.split('\n'))

    if total_content > 0:
        density = domain_entities / total_content * 100

        if density < 2:
            score = 2
            issues.append('信息密度极低(%.1f, 领域实体=%d)' % (density, domain_entities))
        elif density < 5:
            score = 5
            issues.append('信息密度低(%.1f)' % density)
        elif density < 10:
            score = 7
            issues.append('信息密度中等(%.1f)' % density)

    # 填充词扣分
    if filler_count > 20:
        score -= 4
        issues.append('填充词过多(%d个)' % filler_count)
    elif filler_count > 10:
        score -= 2
        issues.append('填充词较多(%d个)' % filler_count)

    score = max(0, score)
    return score, '; '.join(issues) if issues else '信息密度良好(%.1f)' % density


# ============================================================
# C11/C12 增强检查 (Round 12 新增)
# ============================================================

def check_c11_functional_completeness(parsed: Dict) -> Tuple[int, str]:
    """C11: 功能完整性 - 检查skill是否覆盖足够的核心能力点且每个有具体描述"""
    body = parsed.get('body', '')
    chapters = parsed.get('chapters', {})
    score = 10
    issues = []

    # 找到核心能力章节 (支持多种命名)
    cap_chapter = None
    cap_chapter_name = None
    # 第一轮: 精确匹配常见能力章节名
    for name, content in chapters.items():
        if any(kw in name for kw in ['核心能力', '核心功能', 'Core', '能力', '功能', 'Features', 'Capabilities', '主要功能']):
            cap_chapter = content
            cap_chapter_name = name
            break
    # 第二轮: 匹配"核心"开头的章节 (核心工作流、核心规则等)
    if not cap_chapter:
        for name, content in chapters.items():
            if name.startswith('核心') or name.startswith('核心 '):
                cap_chapter = content
                cap_chapter_name = name
                break
    # 第三轮: 找###标题最多的章节作为能力章节 (fallback)
    if not cap_chapter:
        max_h3 = 0
        for name, content in chapters.items():
            h3_count = len(re.findall(r'^###\s+', content, re.MULTILINE))
            # 排除FAQ/错误处理等非能力章节
            if h3_count > max_h3 and not any(x in name for x in ['常见问题', 'FAQ', '错误', '异常', '依赖', '限制', '案例']):
                max_h3 = h3_count
                cap_chapter = content
                cap_chapter_name = name
        if cap_chapter:
            issues.append('能力章节为"%s"(非标准命名)' % cap_chapter_name)

    if not cap_chapter:
        score -= 5
        issues.append('未找到核心能力章节')
        cap_chapter = body

    # 统计能力点 (### 标题、编号列表、bullet列表、或表格行)
    capability_points = re.findall(r'^###\s+\d*\s*(.+)$', cap_chapter, re.MULTILINE)
    if not capability_points:
        # 尝试匹配编号列表 (1. **xxx**)
        capability_points = re.findall(r'^\d+\.\s+\*\*(.+?)\*\*', cap_chapter, re.MULTILINE)
    if not capability_points:
        # 尝试匹配bullet列表 (- **xxx** 或 - xxx)
        capability_points = re.findall(r'^[-*]\s+\*{0,2}(.+?)\*{0,2}$', cap_chapter, re.MULTILINE)
        capability_points = [p for p in capability_points if len(p) > 3]
    if not capability_points:
        # 尝试匹配表格行 (| 能力名 | ... |)
        table_rows = re.findall(r'^\|\s*([^|]+?)\s*\|', cap_chapter, re.MULTILINE)
        # 过滤表头和分隔行
        capability_points = [r.strip() for r in table_rows
                             if r.strip() and not r.strip().startswith('---')
                             and r.strip() not in ('能力', '说明', '功能', '特性', 'Capability', 'Feature', '名称', '描述')
                             and len(r.strip()) <= 20]

    if len(capability_points) < 3:
        score -= 4
        issues.append('核心能力点不足(%d个,建议≥3)' % len(capability_points))
    elif len(capability_points) < 5:
        score -= 2
        issues.append('核心能力点偏少(%d个)' % len(capability_points))

    # 检查每个能力点是否有具体描述 (至少50字符)
    sub_sections = re.split(r'^###\s+', cap_chapter, flags=re.MULTILINE)
    shallow_count = 0
    for section in sub_sections[1:]:  # skip first (before first ###)
        desc = re.sub(r'^[^\n]*\n', '', section).strip()  # get content after heading
        if len(desc) < 50:
            shallow_count += 1

    if shallow_count > 0:
        score -= min(3, shallow_count)
        issues.append('%d个能力点描述过浅(<50字符)' % shallow_count)

    # 工作流覆盖检查已移除: 工作流描述使用不同语言体系(步骤 vs 能力),
    # 导致大量误报。功能完整性通过能力点数量和描述深度已充分评估。

    score = max(0, score)
    return score, '; '.join(issues) if issues else '功能完整性良好(%d个能力点,章节:%s)' % (len(capability_points), cap_chapter_name or 'body')


def check_c12_domain_depth(parsed: Dict) -> Tuple[int, str]:
    """C12: 领域深度 - 检查是否包含领域专属的参数/配置/错误码/数值阈值/领域概念

    采用弹性评分: 4类领域深度信号中,只要总信号量足够即可,
    不强制要求每类都达标(创意类skill可能无API引用但有丰富领域概念)。
    """
    body = parsed.get('body', '')
    chapters = parsed.get('chapters', {})
    score = 10
    issues = []

    # 1. 领域专属数值 (参数、阈值、限制等)
    domain_numbers = re.findall(
        r'\d+\s*(?:字符|条|个|次|分钟|秒|MB|GB|KB|ms|Hz|MHz|GHz|像素|px|dpi|fps|bps|并发|请求|重试|超时|限制|上限|阈值|最大|最小|元|%)',
        body)

    # 2. 领域专属API/命令/工具名 (反引号包裹的代码)
    code_refs = re.findall(r'`([a-zA-Z_][a-zA-Z0-9_\-\./]+)`', body)
    generic_words = {'read', 'exec', 'write', 'true', 'false', 'null', 'none', 'bash', 'python', 'pip', 'npm',
                     'skill', 'agent', 'md', 'exec', 'json', 'yaml', 'MIT', 'Windows', 'macOS', 'Linux'}
    domain_codes = [c for c in code_refs if c.lower() not in generic_words and len(c) > 3]

    # 3. 领域专属错误场景
    error_chapter = None
    for name, content in chapters.items():
        if '异常' in name or '错误' in name or 'Error' in name:
            error_chapter = content
            break
    error_count = 0
    if error_chapter:
        error_rows = len(re.findall(r'^\|.*\|.*\|', error_chapter, re.MULTILINE))
        error_headings = len(re.findall(r'^###\s+', error_chapter, re.MULTILINE))
        error_count = max(error_rows - 1, error_headings)

    # 4. 配置参数 (环境变量、配置项、CLI选项)
    config_refs = re.findall(r'\$\{?\w+\}?|--[a-z][-a-z]*|ENV[A-Z_]+|配置项', body)

    # 5. 领域概念/术语 (新增: 适配创意/业务类skill)
    # 统计非通用的4字以上中文词组(可能是领域术语)
    cn_terms = re.findall(r'[\u4e00-\u9fff]{4,8}', body)
    generic_cn = {'依赖说明', '运行环境', '操作系统', '可用性分类', '已知限制', '常见问题',
                  '核心能力', '使用流程', '适用场景', '案例展示', '异常处理', '错误处理',
                  '自然语言', '结构化', '处理结果', '示例数据', '相关信息'}
    domain_concepts = [t for t in cn_terms if t not in generic_cn]
    # 去重
    domain_concepts = list(set(domain_concepts))

    # 弹性评分: 计算总信号量,各类信号可以互补
    signals = {
        '数值': len(domain_numbers),
        'API': len(domain_codes),
        '错误': error_count,
        '配置': len(config_refs),
        '概念': len(domain_concepts),
    }
    total_signals = sum(signals.values())

    # 总信号量阈值: ≥15为良好,≥8为合格,<8为不足
    if total_signals < 5:
        score = 2
        issues.append('领域深度极浅(总信号%d, 建议≥8)' % total_signals)
    elif total_signals < 8:
        score -= 5
        issues.append('领域深度不足(总信号%d, 建议≥8)' % total_signals)
    elif total_signals < 15:
        score -= 2
        issues.append('领域深度中等(总信号%d)' % total_signals)

    # 额外检查: 错误场景至少3个(不管什么类型的skill都需要)
    if error_count < 3 and error_chapter:
        score -= 2
        issues.append('错误场景不足(%d个,建议≥3)' % error_count)

    score = max(0, score)
    if issues:
        detail = '; '.join(issues)
    else:
        detail = '领域深度良好(数值%d/API%d/错误%d/配置%d/概念%d)' % (
            signals['数值'], signals['API'], signals['错误'], signals['配置'], signals['概念'])
    return score, detail


# ============================================================
# 主检查函数
# ============================================================

CHECKS = [
    ('C1', '描述完整性', check_c1_description_completeness),
    ('C2', '核心能力具体性', check_c2_core_capability_specificity),
    ('C3', '流程具体性', check_c3_workflow_concreteness),
    ('C4', '异常处理具体性', check_c4_error_handling_specificity),
    ('C5', '示例真实性', check_c5_example_authenticity),
    ('C6', 'FAQ相关性', check_c6_faq_relevance),
    ('C7', '领域关键词覆盖', check_c7_domain_keyword_coverage),
    ('C8', '内容独特性', check_c8_content_uniqueness),
    ('C9', '章节深度', check_c9_chapter_depth),
    ('C10', '信息密度', check_c10_information_density),
    ('C11', '功能完整性', check_c11_functional_completeness),
    ('C12', '领域深度', check_c12_domain_depth),
]


def evaluate_capability(skill_md_path: Path) -> Dict[str, Any]:
    """评估单个skill的能力质量 (12项检查,总分120,缩放至100)"""
    content = skill_md_path.read_text(encoding='utf-8')
    parsed = parse_skill_md(content)

    results = {}
    total_score = 0
    max_score = len(CHECKS) * 10  # 120

    for check_id, check_name, check_func in CHECKS:
        score, detail = check_func(parsed)
        results[check_id] = {
            'name': check_name,
            'score': score,
            'detail': detail,
        }
        total_score += score

    # 缩放至100分制
    scaled_score = round(total_score * 100 / max_score) if max_score > 0 else 0

    # 等级 (满分100)
    if scaled_score >= 85:
        grade = 'A'
    elif scaled_score >= 70:
        grade = 'B'
    elif scaled_score >= 50:
        grade = 'C'
    elif scaled_score >= 30:
        grade = 'D'
    else:
        grade = 'F'

    # 能力质量通过阈值
    cap_pass = scaled_score >= 70

    return {
        'slug': parsed.get('slug', skill_md_path.parent.name),
        'capability_score': scaled_score,
        'capability_grade': grade,
        'cap_pass': cap_pass,
        'checks': results,
        'file_path': str(skill_md_path),
        'line_count': len(content.split('\n')),
        'raw_score': total_score,
        'max_score': max_score,
    }


def run_batch(limit: int = 50, only_failing: bool = False) -> List[Dict]:
    """批量评估"""
    conn = get_db_connection()
    c = conn.cursor()

    c.execute("""
        SELECT slug FROM skills 
        WHERE workflow_state != 'deprecated'
        AND slug NOT LIKE '%-free' AND slug NOT LIKE '%-pro'
        ORDER BY slug LIMIT ?
    """, (limit,))

    slugs = [r['slug'] for r in c.fetchall()]
    conn.close()

    results = []
    for slug in slugs:
        skill_md = PACKAGED_SKILLS_DIR / slug / 'SKILL.md'
        if not skill_md.exists():
            continue

        result = evaluate_capability(skill_md)
        results.append(result)

        if only_failing and result['cap_pass']:
            continue

        print('%-35s: %3d/100 (%s) %s' % (
            slug, result['capability_score'], result['capability_grade'],
            '✓' if result['cap_pass'] else '✗'
        ))

    return results


def main():
    parser = argparse.ArgumentParser(description='L2-Capability质量检查器')
    parser.add_argument('skill_md_path', nargs='?', help='SKILL.md文件路径')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')
    parser.add_argument('--batch', action='store_true', help='批量评估模式')
    parser.add_argument('--limit', type=int, default=50, help='批量模式最大数量')
    parser.add_argument('--only-failing', action='store_true', help='仅显示未通过的')
    parser.add_argument('-o', '--output', help='报告输出文件')

    args = parser.parse_args()

    if args.batch:
        print('=== L2-Capability 批量评估 ===')
        results = run_batch(limit=args.limit, only_failing=args.only_failing)

        scores = [r['capability_score'] for r in results]
        avg = sum(scores) / len(scores) if scores else 0
        pass_rate = sum(1 for r in results if r['cap_pass']) / len(results) * 100 if results else 0

        grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        for r in results:
            grade_dist[r['capability_grade']] += 1

        print()
        print('=== 汇总 ===')
        print('  评估数: %d' % len(results))
        print('  平均分: %.1f/100' % avg)
        print('  通过率: %.1f%% (阈值≥70)' % pass_rate)
        print('  等级分布: A=%d B=%d C=%d D=%d F=%d' % (
            grade_dist['A'], grade_dist['B'], grade_dist['C'],
            grade_dist['D'], grade_dist['F']))

        if args.output:
            Path(args.output).write_text(
                json.dumps({'results': results, 'summary': {
                    'count': len(results), 'avg_score': round(avg, 1),
                    'pass_rate': round(pass_rate, 1), 'grade_dist': grade_dist
                }}, ensure_ascii=False, indent=2),
                encoding='utf-8')
        return

    if not args.skill_md_path:
        parser.print_help()
        return

    skill_md_path = Path(args.skill_md_path)
    if not skill_md_path.exists():
        print('文件不存在: %s' % skill_md_path)
        return

    result = evaluate_capability(skill_md_path)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print('=== L2-Capability 评估: %s ===' % result['slug'])
        print('文件: %s' % result['file_path'])
        print('行数: %d' % result['line_count'])
        print()
        print('总分: %d/100 (%s) %s' % (
            result['capability_score'], result['capability_grade'],
            '✓通过' if result['cap_pass'] else '✗未通过'))
        print()
        print('各项检查:')
        for check_id, check_name, _ in CHECKS:
            r = result['checks'][check_id]
            print('  %s %-20s: %2d/10  %s' % (check_id, check_name, r['score'], r['detail']))


if __name__ == '__main__':
    main()
