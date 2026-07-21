#!/usr/bin/env python3
"""
LLM能力重生成流水线 (Capability Regeneration Pipeline)
=======================================================

系统化处理全量1320个派生skill的LLM重生成。

流程:
  1. 扫描所有源skill(clawhub-skills/downloaded/)
  2. 评估现有packaged版本的L2-Capability评分
  3. 识别需要重新生成的skill(cap_score < 70)
  4. 按领域分组,生成分批任务文件
  5. 驱动子代理并行生成高质量SKILL.md

Usage:
    python capability_pipeline.py --scan           # 扫描并识别需要重新生成的skill
    python capability_pipeline.py --batch 1        # 生成分批任务文件
    python capability_pipeline.py --stats          # 查看统计信息
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# 确保能导入skill_registry模块
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection, PACKAGED_SKILLS_DIR
from l2_capability_checker import evaluate_capability

# 源skill目录
CLAWHUB_DOWNLOADED_DIR = Path(r'D:\skills\clawhub-skills\downloaded')
DIFFERENTIATED_DIR = Path(r'D:\skills\differentiated-skills')

# 质量阈值
CAP_PASS_THRESHOLD = 70

# 分批大小
BATCH_SIZE = 10


def find_source_skills() -> List[Dict[str, Any]]:
    """扫描所有源skill,返回详细信息"""
    sources = []
    
    # 扫描clawhub-skills/downloaded/
    if CLAWHUB_DOWNLOADED_DIR.exists():
        for cat_dir in CLAWHUB_DOWNLOADED_DIR.iterdir():
            if not cat_dir.is_dir():
                continue
            for skill_dir in cat_dir.iterdir():
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / 'SKILL.md'
                if skill_md.exists():
                    content = skill_md.read_text(encoding='utf-8')
                    lines = content.split('\n')
                    
                    # 提取slug
                    slug = skill_dir.name
                    for line in lines[:20]:
                        if line.startswith('slug:'):
                            slug = line.split(':', 1)[1].strip().strip('"').strip("'")
                            break
                    
                    # 跳过已有-free/-pro后缀的派生skill,只处理源skill
                    if slug.endswith('-free') or slug.endswith('-pro'):
                        continue
                    
                    sources.append({
                        'slug': slug,
                        'category': cat_dir.name,
                        'original_path': str(skill_md),
                        'original_lines': len(lines),
                        'source': 'clawhub_downloaded',
                    })
    
    # 扫描differentiated-skills/
    if DIFFERENTIATED_DIR.exists():
        for cat_dir in DIFFERENTIATED_DIR.iterdir():
            if not cat_dir.is_dir():
                continue
            for skill_dir in cat_dir.iterdir():
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / 'SKILL.md'
                if skill_md.exists():
                    slug = skill_dir.name
                    # 跳过已在clawhub_downloaded中的
                    if any(s['slug'] == slug for s in sources):
                        continue
                    # 跳过已有-free/-pro后缀的派生skill
                    if slug.endswith('-free') or slug.endswith('-pro'):
                        continue
                    
                    content = skill_md.read_text(encoding='utf-8')
                    lines = content.split('\n')
                    
                    sources.append({
                        'slug': slug,
                        'category': cat_dir.name,
                        'original_path': str(skill_md),
                        'original_lines': len(lines),
                        'source': 'differentiated',
                    })
    
    return sources


def evaluate_existing_packaged(slug: str) -> Optional[Dict[str, Any]]:
    """评估现有packaged版本的L2-Capability评分"""
    # 检查付费版
    paid_path = PACKAGED_SKILLS_DIR / slug / 'SKILL.md'
    paid_result = None
    if paid_path.exists():
        paid_result = evaluate_capability(paid_path)
    
    # 检查免费版
    free_slug = slug + '-free'
    free_path = PACKAGED_SKILLS_DIR / free_slug / 'SKILL.md'
    free_result = None
    if free_path.exists():
        free_result = evaluate_capability(free_path)
    
    return {
        'paid': paid_result,
        'free': free_result,
    }


def scan_and_identify() -> Dict[str, Any]:
    """扫描所有源skill,识别需要重新生成的"""
    print('=== 扫描源skill ===')
    sources = find_source_skills()
    print('  源skill总数: %d' % len(sources))
    
    # 按领域统计
    cat_stats = {}
    for s in sources:
        cat = s['category']
        cat_stats[cat] = cat_stats.get(cat, 0) + 1
    print()
    print('  按领域分布:')
    for cat in sorted(cat_stats.keys()):
        print('    %-30s: %d' % (cat, cat_stats[cat]))
    
    # 评估现有packaged版本
    print()
    print('=== 评估现有packaged版本 ===')
    
    need_regen = []
    already_good = []
    no_packaged = []
    
    for i, source in enumerate(sources):
        slug = source['slug']
        
        if (i + 1) % 50 == 0:
            print('  进度: %d/%d' % (i + 1, len(sources)))
        
        existing = evaluate_existing_packaged(slug)
        
        paid = existing['paid']
        free = existing['free']
        
        source['paid_eval'] = paid
        source['free_eval'] = free
        
        paid_ok = paid and paid['cap_pass']
        free_ok = free and free['cap_pass']
        
        if paid_ok and free_ok:
            already_good.append(source)
        elif not paid and not free:
            no_packaged.append(source)
        else:
            need_regen.append(source)
    
    print()
    print('=== 识别结果 ===')
    print('  已达标(无需重生成): %d' % len(already_good))
    print('  需要重生成: %d' % len(need_regen))
    print('  无packaged版本: %d' % len(no_packaged))
    print('  总计需要处理: %d' % (len(need_regen) + len(no_packaged)))
    
    # 合并需要处理的
    to_process = need_regen + no_packaged
    
    # 按领域分组
    by_category = {}
    for s in to_process:
        cat = s['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(s)
    
    print()
    print('  按领域分组(需处理):')
    for cat in sorted(by_category.keys()):
        print('    %-30s: %d' % (cat, len(by_category[cat])))
    
    # 保存扫描结果
    scan_result = {
        'scan_time': datetime.now().isoformat(),
        'total_sources': len(sources),
        'already_good': len(already_good),
        'need_regen': len(need_regen),
        'no_packaged': len(no_packaged),
        'to_process': len(to_process),
        'by_category': {cat: len(items) for cat, items in by_category.items()},
        'skills_to_process': [
            {
                'slug': s['slug'],
                'category': s['category'],
                'original_path': s['original_path'],
                'original_lines': s['original_lines'],
                'source': s['source'],
                'paid_score': s['paid_eval']['capability_score'] if s['paid_eval'] else None,
                'free_score': s['free_eval']['capability_score'] if s['free_eval'] else None,
            }
            for s in to_process
        ],
    }
    
    output_path = SKILL_REGISTRY_DIR / 'capability_scan_result.json'
    output_path.write_text(
        json.dumps(scan_result, ensure_ascii=False, indent=2),
        encoding='utf-8')
    print()
    print('  扫描结果已保存: %s' % output_path)
    
    return scan_result


def generate_batch_task(batch_num: int) -> str:
    """生成分批任务文件"""
    scan_path = SKILL_REGISTRY_DIR / 'capability_scan_result.json'
    if not scan_path.exists():
        print('请先运行 --scan 扫描')
        return ''
    
    scan = json.loads(scan_path.read_text(encoding='utf-8'))
    skills = scan['skills_to_process']
    
    # 按领域排序,同领域的放在一起
    skills.sort(key=lambda x: (x['category'], x['slug']))
    
    start = (batch_num - 1) * BATCH_SIZE
    end = start + BATCH_SIZE
    batch = skills[start:end]
    
    if not batch:
        print('批次 %d 无数据' % batch_num)
        return ''
    
    # 生成任务文件
    task = {
        'batch_num': batch_num,
        'total_batches': (len(skills) + BATCH_SIZE - 1) // BATCH_SIZE,
        'batch_size': len(batch),
        'skills': batch,
        'generation_guidelines': {
            'requirements': [
                '必须基于源skill的原始内容生成,保留真实领域知识',
                '所有章节内容必须领域具体化,不得使用通用模板填充',
                '异常处理表必须包含领域特定错误,不得使用通用3行模板',
                'FAQ必须包含领域特定问题,不得使用通用Q1/Q2/Q3',
                '适用场景表必须有具体输入输出,不得使用"基础使用|用户请求|处理结果"',
                '案例展示必须有真实数据,不得使用"示例数据"占位符',
                '使用流程必须是领域特定步骤,不得使用通用4步模板',
                '付费版:完整功能,200-400行,3个案例,8+异常,5+FAQ',
                '免费版:基础功能,150-250行,1-2个案例,5+异常,3+FAQ,含升级提示',
            ],
            'forbidden_patterns': [
                '配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求',
                '运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明',
                '网络错误 | 连接超时或不可达 | 检查网络连接后重试',
                'Q1: 如何开始使用',
                'Q2: 遇到错误怎么办',
                'Q3:.*有什么限制',
                '基础使用 | 用户请求 | 处理结果',
                '确认运行环境满足依赖说明中的要求',
                '根据适用场景选择合适的使用方式',
                '执行操作并检查输出结果',
                '如遇错误，参考错误处理章节',
                '示例数据', '示例输入', '示例内容', '示例输出',
                '待补充', '待填充', '（根据实际场景填充）',
            ],
        },
    }
    
    task_path = SKILL_REGISTRY_DIR / ('capability_batch_%03d.json' % batch_num)
    task_path.write_text(
        json.dumps(task, ensure_ascii=False, indent=2),
        encoding='utf-8')
    print('批次 %d 任务文件已生成: %s (%d skills)' % (batch_num, task_path, len(batch)))
    
    # 输出每个skill的信息
    for s in batch:
        paid_score = s.get('paid_score')
        free_score = s.get('free_score')
        print('  %-35s %-15s %s/%s' % (
            s['slug'], s['category'],
            '%d' % paid_score if paid_score else 'N/A',
            '%d' % free_score if free_score else 'N/A'))
    
    return str(task_path)


def show_stats():
    """显示统计信息"""
    scan_path = SKILL_REGISTRY_DIR / 'capability_scan_result.json'
    if not scan_path.exists():
        print('请先运行 --scan 扫描')
        return
    
    scan = json.loads(scan_path.read_text(encoding='utf-8'))
    
    print('=== 能力重生成流水线统计 ===')
    print()
    print('  扫描时间: %s' % scan['scan_time'])
    print('  源skill总数: %d' % scan['total_sources'])
    print('  已达标(无需重生成): %d' % scan['already_good'])
    print('  需要重生成: %d' % scan['need_regen'])
    print('  无packaged版本: %d' % scan['no_packaged'])
    print('  总计需要处理: %d' % scan['to_process'])
    print('  总批次(每批%d): %d' % (BATCH_SIZE, (scan['to_process'] + BATCH_SIZE - 1) // BATCH_SIZE))
    print()
    print('  按领域分布:')
    for cat in sorted(scan['by_category'].keys()):
        print('    %-30s: %d' % (cat, scan['by_category'][cat]))
    
    # 检查已生成的批次
    batch_files = list(SKILL_REGISTRY_DIR.glob('capability_batch_*.json'))
    print()
    print('  已生成批次文件: %d' % len(batch_files))


def main():
    parser = argparse.ArgumentParser(description='LLM能力重生成流水线')
    parser.add_argument('--scan', action='store_true', help='扫描并识别需要重新生成的skill')
    parser.add_argument('--batch', type=int, help='生成指定批次的任务文件')
    parser.add_argument('--stats', action='store_true', help='查看统计信息')
    
    args = parser.parse_args()
    
    if args.scan:
        scan_and_identify()
    elif args.batch:
        generate_batch_task(args.batch)
    elif args.stats:
        show_stats()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
