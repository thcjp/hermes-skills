#!/usr/bin/env python3
"""
跨skill多样性分析器 (Cross-Skill Diversity Analyzer)
=====================================================

检测同类别内的skill同质化问题。
对同类别的所有skill进行两两对比，计算相似度。

相似度指标:
  1. 章节结构相似度 (Jaccard of ## headers)
  2. 核心能力描述重合度 (keyword overlap)
  3. 错误处理表重合度 (error scenario overlap)
  4. FAQ问题重合度 (question overlap)
  5. 综合相似度 (加权平均)

阈值: 同类别内任意两个skill的综合相似度 > 60% 则标记为同质化风险

Usage:
    python cross_skill_diversity.py
    python cross_skill_diversity.py --category Creative
    python cross_skill_diversity.py --threshold 0.5
"""

import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime
from itertools import combinations
from collections import defaultdict

SKILL_REGISTRY_DIR = Path(__file__).parent
PACKAGED_DIR = Path(r'D:\skills\packaged-skills\skillhub')
SCAN_RESULT = SKILL_REGISTRY_DIR / 'capability_scan_result.json'


def extract_chapters(content):
    """提取 ## 级别的章节标题"""
    headers = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    return set(h.strip().lower() for h in headers)


def extract_error_scenarios(content):
    """提取错误处理章节中的场景（支持表格格式和###标题格式）"""
    scenarios = set()
    in_error_section = False
    for line in content.split('\n'):
        if re.match(r'^##\s+.*异常.*|^##\s+.*错误.*', line, re.IGNORECASE):
            in_error_section = True
            continue
        if re.match(r'^##\s+', line) and in_error_section:
            in_error_section = False
        if not in_error_section:
            continue
        # 格式1: 表格行 | 错误场景 | ... |
        if '|' in line:
            cells = [c.strip() for c in line.split('|')]
            if len(cells) >= 2 and cells[1] and not cells[1].startswith('---') and cells[1] not in ('错误场景', '场景', '错误', 'Error', 'Issue'):
                scenarios.add(cells[1].lower())
        # 格式2: ### 标题
        heading_match = re.match(r'^###\s+(.+)$', line)
        if heading_match:
            scenarios.add(heading_match.group(1).strip().lower())
    return scenarios


def extract_faqs(content):
    """提取FAQ问题（支持Q1:格式和### 问题？格式）"""
    faqs = set()
    # 格式1: ### Q1: ... 或 **Q1:** ...
    for m in re.finditer(r'(?:###\s+)?(?:\*\*)?Q\d*[:：]\s*(.+?)(?:\*\*)?$', content, re.MULTILINE):
        faqs.add(m.group(1).strip().lower()[:50])
    # 格式2: ### 问题？ (在常见问题章节内的###标题)
    in_faq_section = False
    for line in content.split('\n'):
        if re.match(r'^##\s+.*常见问题.*|^##\s+.*FAQ.*', line, re.IGNORECASE):
            in_faq_section = True
            continue
        if re.match(r'^##\s+', line) and in_faq_section:
            in_faq_section = False
        if in_faq_section:
            heading_match = re.match(r'^###\s+(.+)$', line)
            if heading_match:
                faqs.add(heading_match.group(1).strip().lower()[:50])
    return faqs


def extract_domain_keywords(content):
    """提取领域关键词（专有名词、API名、命令名等）"""
    keywords = set()
    # 匹配反引号包裹的代码/命令
    for m in re.finditer(r'`([a-zA-Z_][a-zA-Z0-9_\-\.]+)`', content):
        kw = m.group(1)
        if len(kw) > 2 and kw not in ('read', 'exec', 'write', 'true', 'false', 'null', 'none'):
            keywords.add(kw.lower())
    # 匹配大写开头的专有名词
    for m in re.finditer(r'\b([A-Z][a-zA-Z]{3,})\b', content):
        kw = m.group(1)
        if kw not in ('Skill', 'Agent', 'Note', 'Important', 'Warning', 'Error', 'Table', 'Usage'):
            keywords.add(kw.lower())
    return keywords


def jaccard_similarity(set1, set2):
    """计算Jaccard相似度。两个空集返回0.0（无数据，不视为相似）"""
    if not set1 and not set2:
        return 0.0  # 两个空集视为无数据，不判定为相似
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


def compute_similarity(content1, content2):
    """计算两个skill内容的综合相似度"""
    # 1. 章节结构相似度 (权重 25%)
    chapters1 = extract_chapters(content1)
    chapters2 = extract_chapters(content2)
    chapter_sim = jaccard_similarity(chapters1, chapters2)
    
    # 2. 错误处理表重合度 (权重 25%)
    errors1 = extract_error_scenarios(content1)
    errors2 = extract_error_scenarios(content2)
    error_sim = jaccard_similarity(errors1, errors2)
    
    # 3. FAQ问题重合度 (权重 20%)
    faqs1 = extract_faqs(content1)
    faqs2 = extract_faqs(content2)
    faq_sim = jaccard_similarity(faqs1, faqs2)
    
    # 4. 领域关键词差异度 (权重 30%) - 越多不同越好
    kw1 = extract_domain_keywords(content1)
    kw2 = extract_domain_keywords(content2)
    kw_sim = jaccard_similarity(kw1, kw2)
    
    # 综合相似度 (加权平均)
    overall = chapter_sim * 0.25 + error_sim * 0.25 + faq_sim * 0.20 + kw_sim * 0.30
    
    return {
        'overall': round(overall, 3),
        'chapter': round(chapter_sim, 3),
        'error': round(error_sim, 3),
        'faq': round(faq_sim, 3),
        'keyword': round(kw_sim, 3),
        'chapters_1': len(chapters1),
        'chapters_2': len(chapters2),
        'errors_1': len(errors1),
        'errors_2': len(errors2),
        'faqs_1': len(faqs1),
        'faqs_2': len(faqs2),
        'keywords_1': len(kw1),
        'keywords_2': len(kw2),
    }


def load_skills_by_category():
    """加载已生成的skill并按类别分组"""
    if not SCAN_RESULT.exists():
        print("ERROR: capability_scan_result.json not found")
        return {}
    
    data = json.loads(SCAN_RESULT.read_text(encoding='utf-8'))
    skills_by_cat = defaultdict(list)
    
    for skill_info in data.get('skills_to_process', []):
        slug = skill_info['slug']
        category = skill_info['category']
        # 检查paid版本是否存在
        skill_md = PACKAGED_DIR / slug / 'SKILL.md'
        if skill_md.exists():
            skills_by_cat[category].append({
                'slug': slug,
                'path': str(skill_md),
                'content': skill_md.read_text(encoding='utf-8'),
            })
    
    return dict(skills_by_cat)


def analyze_diversity(threshold=0.6, category_filter=None):
    """分析跨skill多样性"""
    skills_by_cat = load_skills_by_category()
    
    report = {
        'analysis_time': datetime.now().isoformat(),
        'threshold': threshold,
        'categories': {},
        'summary': {
            'total_skills': 0,
            'total_pairs': 0,
            'high_risk_pairs': 0,
            'medium_risk_pairs': 0,
            'low_risk_pairs': 0,
        }
    }
    
    for cat, skills in sorted(skills_by_cat.items()):
        if category_filter and cat != category_filter:
            continue
        if len(skills) < 2:
            continue
        
        cat_report = {
            'skill_count': len(skills),
            'pairs_analyzed': 0,
            'avg_similarity': 0,
            'max_similarity': 0,
            'high_risk_pairs': [],
            'medium_risk_pairs': [],
            'low_risk_pairs': [],
        }
        
        total_sim = 0
        max_sim = 0
        
        for s1, s2 in combinations(skills, 2):
            sim = compute_similarity(s1['content'], s2['content'])
            cat_report['pairs_analyzed'] += 1
            total_sim += sim['overall']
            if sim['overall'] > max_sim:
                max_sim = sim['overall']
            
            pair_info = {
                'skill_1': s1['slug'],
                'skill_2': s2['slug'],
                'similarity': sim['overall'],
                'details': sim,
            }
            
            if sim['overall'] >= threshold:
                cat_report['high_risk_pairs'].append(pair_info)
                report['summary']['high_risk_pairs'] += 1
            elif sim['overall'] >= threshold * 0.7:
                cat_report['medium_risk_pairs'].append(pair_info)
                report['summary']['medium_risk_pairs'] += 1
            else:
                cat_report['low_risk_pairs'].append(pair_info)
                report['summary']['low_risk_pairs'] += 1
        
        cat_report['avg_similarity'] = round(total_sim / cat_report['pairs_analyzed'], 3) if cat_report['pairs_analyzed'] > 0 else 0
        cat_report['max_similarity'] = round(max_sim, 3)
        report['summary']['total_skills'] += len(skills)
        report['summary']['total_pairs'] += cat_report['pairs_analyzed']
        report['categories'][cat] = cat_report
        
        # Print category summary
        print("Category: " + cat + " (" + str(len(skills)) + " skills, " + str(cat_report['pairs_analyzed']) + " pairs)")
        print("  Avg similarity: " + str(cat_report['avg_similarity']))
        print("  Max similarity: " + str(cat_report['max_similarity']))
        print("  High risk (≥" + str(threshold) + "): " + str(len(cat_report['high_risk_pairs'])))
        print("  Medium risk (≥" + str(round(threshold * 0.7, 2)) + "): " + str(len(cat_report['medium_risk_pairs'])))
        
        # Show high risk pairs
        for pair in cat_report['high_risk_pairs'][:5]:
            print("    HIGH: " + pair['skill_1'] + " vs " + pair['skill_2'] + " = " + str(pair['similarity']))
            print("      chapter=" + str(pair['details']['chapter']) + " error=" + str(pair['details']['error']) + " faq=" + str(pair['details']['faq']) + " keyword=" + str(pair['details']['keyword']))
    
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cross-skill diversity analyzer')
    parser.add_argument('--threshold', type=float, default=0.6, help='Similarity threshold for high risk (default: 0.6)')
    parser.add_argument('--category', type=str, default=None, help='Filter by category')
    args = parser.parse_args()
    
    print("=" * 70)
    print("Cross-Skill Diversity Analyzer")
    print("Threshold: " + str(args.threshold))
    print("=" * 70)
    
    report = analyze_diversity(threshold=args.threshold, category_filter=args.category)
    
    print("\n" + "=" * 70)
    print("OVERALL SUMMARY")
    print("=" * 70)
    s = report['summary']
    print("  Total skills: " + str(s['total_skills']))
    print("  Total pairs analyzed: " + str(s['total_pairs']))
    print("  High risk pairs (≥" + str(args.threshold) + "): " + str(s['high_risk_pairs']))
    print("  Medium risk pairs: " + str(s['medium_risk_pairs']))
    print("  Low risk pairs: " + str(s['low_risk_pairs']))
    
    if s['total_pairs'] > 0:
        risk_rate = (s['high_risk_pairs'] + s['medium_risk_pairs']) / s['total_pairs'] * 100
        diversity_score = 100 - risk_rate
        print("\n  Diversity Score: " + str(round(diversity_score, 1)) + "%")
        print("  Homogenization Risk: " + str(round(risk_rate, 1)) + "%")
    
    # Save report
    output_file = SKILL_DATA_DIR / "reports" / "diversity_report.json"
    output_file.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print("\nReport saved to: " + str(output_file))
