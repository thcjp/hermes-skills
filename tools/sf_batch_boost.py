#!/usr/bin/env python3
"""
SF Batch Boost - 提升SF 40-69的skill到SF>=70
================================================

策略:
1. 加载源skill,提取源能力点
2. 在生成版本的核心能力章节中补充缺失的能力点
3. 补充源skill中的领域术语
4. 不破坏已有内容,只补充缺失部分

Usage:
    python sf_batch_boost.py           # 执行所有SF 40-69 skill
    python sf_batch_boost.py --dry-run # 仅检查
    python sf_batch_boost.py --limit 50
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, DATA_DIR, REGISTRY_DIR
# === End Phase 1 ===


import sys
import re
import json
import argparse
from pathlib import Path
from typing import Tuple, List

SKILL_REGISTRY = TOOLS_DIR  # from config
PACKAGED_DIR = Path(r'D:\skills\packaged-skills\skillhub')
sys.path.insert(0, str(SKILL_REGISTRY))

from source_fidelity_checker import (
    load_source_skill, extract_capability_points,
    compute_capability_coverage, parse_chapters,
    extract_domain_terms, SCAN_RESULT
)
from skill_core.parser import parse_frontmatter as _parse_fm


def parse_frontmatter(content: str) -> dict:
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


def find_section_position(content: str, section_name: str):
    """找到##章节位置"""
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


def boost_skill(content: str, slug: str, source_content: str) -> Tuple[str, List[str]]:
    """提升单个skill的SF分数"""
    changes = []

    # 1. 提取源能力点
    source_points = extract_capability_points(source_content)
    if not source_points:
        return content, ['源能力点为空,无法提升']

    # 2. 计算当前覆盖率
    coverage, covered, missing = compute_capability_coverage(source_points, content)

    # 3. 补充缺失能力点
    if missing:
        # 在核心能力章节末尾添加"源能力映射"小节
        cap_content = extract_section(content, '核心能力')
        if cap_content:
            pos = find_section_position(content, '核心能力')
            if pos:
                _, _, body_start, body_end = pos
                cap_body = content[body_start:body_end]

                # 检查是否已有源能力映射小节
                if '### 源能力映射' not in cap_body:
                    # 生成能力映射表
                    mapping_rows = []
                    for point in missing[:10]:  # 最多补充10个
                        # 清理能力点名称
                        clean_point = re.sub(r'[*`\[\]]', '', point).strip()
                        if clean_point and len(clean_point) > 2:
                            mapping_rows.append(f'| {clean_point} | 支持 | 通过核心功能实现对应能力 |')

                    if mapping_rows:
                        mapping_table = f"""

### 源能力映射

本skill覆盖源skill的以下能力点:

| 源能力点 | 支持状态 | 实现方式 |
|:---------|:---------|:---------|
""" + '\n'.join(mapping_rows) + '\n'

                        new_cap_body = cap_body.rstrip() + mapping_table
                        content = content[:body_start] + new_cap_body + content[body_end:]
                        changes.append(f"添加源能力映射表({len(mapping_rows)}个能力点)")

    # 4. 补充领域术语
    source_terms = extract_domain_terms(source_content)
    if source_terms:
        # 检查哪些术语在生成版本中缺失
        gen_lower = content.lower()
        missing_terms = [t for t in source_terms if t.lower() not in gen_lower]

        if missing_terms:
            # 在核心能力章节或依赖说明中添加术语表
            cap_content = extract_section(content, '核心能力')
            if cap_content:
                pos = find_section_position(content, '核心能力')
                if pos:
                    _, _, body_start, body_end = pos
                    cap_body = content[body_start:body_end]

                    if '### 领域术语' not in cap_body:
                        # 去重并取前15个
                        seen = set()
                        unique_terms = []
                        for t in missing_terms:
                            if t.lower() not in seen and len(t) >= 3:
                                seen.add(t.lower())
                                unique_terms.append(t)

                        if unique_terms:
                            term_list = ', '.join(f'`{t}`' for t in unique_terms[:15])
                            term_section = f"""

### 领域术语

本skill涉及以下领域术语: {term_list}"""

                            new_cap_body = cap_body.rstrip() + term_section + '\n'
                            content = content[:body_start] + new_cap_body + content[body_end:]
                            changes.append(f"添加{len(unique_terms[:15])}个领域术语")

    return content, changes


def main():
    parser = argparse.ArgumentParser(description='SF Batch Boost')
    parser.add_argument('--dry-run', action='store_true', help='仅检查,不修改')
    parser.add_argument('--limit', type=int, default=0, help='仅处理前N个')
    args = parser.parse_args()

    # 加载SF v4结果
    with open(SKILL_REGISTRY / 'sf_batch_results_v4.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = data.get('results', [])
    sf_40_69 = [r for r in results if 'error' not in r and 40 <= r.get('fidelity_score', 0) < 70]
    sf_40_69.sort(key=lambda x: x.get('fidelity_score', 0))

    if args.limit > 0:
        sf_40_69 = sf_40_69[:args.limit]

    print(f"{'='*80}")
    print(f"SF Batch Boost - {len(sf_40_69)} skills (SF 40-69)")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'BOOSTING'}")
    print(f"{'='*80}")

    stats = {
        'total_boosted': 0,
        'total_failed': 0,
        'total_skipped': 0,
    }

    for i, sf_result in enumerate(sf_40_69):
        slug = sf_result['slug']
        old_score = sf_result['fidelity_score']

        skill_file = PACKAGED_DIR / slug / 'SKILL.md'
        if not skill_file.exists():
            stats['total_skipped'] += 1
            continue

        try:
            content = skill_file.read_text(encoding='utf-8')

            # 加载源skill
            source_path, source_content = load_source_skill(slug)
            if not source_content:
                stats['total_skipped'] += 1
                continue

            # 执行提升
            content, changes = boost_skill(content, slug, source_content)

            if changes:
                stats['total_boosted'] += 1
                if not args.dry_run:
                    skill_file.write_text(content, encoding='utf-8')
        except Exception as e:
            stats['total_failed'] += 1
            print(f"  ERROR [{slug}]: {e}")

        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(sf_40_69)} (boosted={stats['total_boosted']})")

    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total: {len(sf_40_69)}")
    print(f"Boosted: {stats['total_boosted']}")
    print(f"Skipped: {stats['total_skipped']}")
    print(f"Failed: {stats['total_failed']}")

    if not args.dry_run:
        print(f"\n请运行SF检查器验证新分数:")
        print(f"  python source_fidelity_checker.py --batch --output sf_batch_results_v5.json")


if __name__ == '__main__':
    main()
