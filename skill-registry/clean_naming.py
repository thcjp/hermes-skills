#!/usr/bin/env python3
"""
Skill 命名治理脚本
==================
功能: 清理 skill-registry.db 中的命名规范问题

治理内容:
1. 合并 -free/-pro 成对记录为统一base slug + edition字段
2. 清理版本号写入slug的问题
3. 统一 pricing_model 和 edition 字段
4. 清理 category 被 source 污染的问题
5. 已上传到平台的slug保持不变(legacy)

用法:
  python clean_naming.py dry-run           # 预览治理结果(不修改DB)
  python clean_naming.py execute           # 执行治理
  python clean_naming.py report            # 生成治理报告
  python clean_naming.py merge-pairs       # 仅合并-free/-pro成对记录
  python clean_naming.py fix-fields        # 仅修复字段不一致
  python clean_naming.py fix-category      # 仅修复category污染
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
# === End Phase 1 ===


import argparse
import json
import sqlite3
import re
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple, Set

# DB_PATH imported from config
REPORT_PATH = Path(r"d:\skills\skill-registry\governance-report.json")

# ============================================================
# 工具函数
# ============================================================

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def get_uploaded_slugs() -> Set[str]:
    """获取已上传成功的slug（不可修改）"""
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT s.slug FROM skills s
        JOIN platform_uploads p ON s.id = p.skill_id
        WHERE p.upload_status = 'success'
    """)
    slugs = {row[0] for row in c.fetchall()}
    conn.close()
    return slugs

def extract_base_slug(slug: str) -> Tuple[str, str]:
    """从slug中提取base slug和edition后缀
    返回: (base_slug, edition)
    edition: 'free' | 'pro' | 'paid' | ''
    """
    # 按优先级匹配后缀
    for suffix, edition in [('-tool-free', 'free'), ('-tool-pro', 'pro'),
                            ('-free', 'free'), ('-pro', 'pro')]:
        if slug.endswith(suffix):
            base = slug[:-len(suffix)]
            return base, edition
    return slug, ''

def normalize_pricing(edition: str, pricing_model: str) -> Tuple[str, str]:
    """标准化 pricing_model 和 edition 字段
    返回: (pricing_model, edition)
    
    规范:
    - 免费版: pricing_model='free', edition='free'
    - 付费版: pricing_model='per_call'/'monthly'/'dual', edition='paid'
    - 免费增值: pricing_model='freemium', edition='paid'
    """
    # 如果edition为空但pricing_model有值
    if not edition and pricing_model:
        if pricing_model == 'free':
            return 'free', 'free'
        elif pricing_model in ('monthly', 'per_call', 'dual', 'freemium'):
            return pricing_model, 'paid'
        return pricing_model, 'paid'

    # 如果edition有值但pricing_model为空
    if edition and not pricing_model:
        if edition == 'free':
            return 'free', 'free'
        elif edition == 'pro':
            return 'per_call', 'paid'
        elif edition == 'dual':
            return 'dual', 'paid'
        return 'free', edition

    # 两者都有值，统一edition为paid/free
    if edition == 'pro':
        return pricing_model or 'per_call', 'paid'
    if edition == 'free':
        return pricing_model or 'free', 'free'
    if edition == 'dual':
        return pricing_model or 'dual', 'paid'

    return pricing_model, edition

# ============================================================
# 治理操作
# ============================================================

def analyze_pairs() -> Dict[str, Any]:
    """分析 -free/-pro 成对记录"""
    conn = get_db()
    c = conn.cursor()
    uploaded = get_uploaded_slugs()

    # 获取所有未上传的含后缀slug
    c.execute("""
        SELECT id, slug, current_display_name, source, source_slug,
               pricing_model, edition, parent_slug, local_path, current_version,
               category, current_status
        FROM skills
        WHERE (slug LIKE '%-free' OR slug LIKE '%-pro')
        ORDER BY slug
    """)

    all_rows = [dict(r) for r in c.fetchall()]
    conn.close()

    # 按base slug分组
    groups = defaultdict(list)
    unpaired = []
    for row in all_rows:
        if row['slug'] in uploaded:
            continue  # 跳过已上传的

        base, edition = extract_base_slug(row['slug'])
        row['_base_slug'] = base
        row['_extracted_edition'] = edition
        groups[base].append(row)

    # 分离成对和单独的
    pairs = {}
    singles = {}
    for base, items in groups.items():
        editions = {item['_extracted_edition'] for item in items}
        if 'free' in editions and 'pro' in editions:
            pairs[base] = items
        else:
            singles[base] = items

    return {
        'total_with_suffix': len(all_rows),
        'uploaded_skipped': len([r for r in all_rows if r['slug'] in uploaded]),
        'pair_groups': len(pairs),
        'single_groups': len(singles),
        'pairs': pairs,
        'singles': singles,
    }

def plan_merge_pairs(analysis: Dict) -> List[Dict[str, Any]]:
    """生成成对记录合并计划
    
    策略:
    - base slug 作为付费版slug (edition=paid)
    - base-free 作为免费版slug (edition=free, parent_slug=base)
    - 合并两条记录的metadata，保留pro版的pricing_model
    - 删除原来的 -tool-free/-tool-pro 记录
    """
    plans = []
    
    for base_slug, items in analysis['pairs'].items():
        free_item = None
        pro_item = None
        
        for item in items:
            if item['_extracted_edition'] == 'free':
                free_item = item
            elif item['_extracted_edition'] == 'pro':
                pro_item = item

        if not free_item or not pro_item:
            continue

        # 检查base slug是否已被占用
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT id FROM skills WHERE slug = ?", (base_slug,))
        existing = c.fetchone()
        conn.close()

        if existing:
            # base slug已被占用，使用 base-paid 和 base-free
            paid_slug = f"{base_slug}-paid"
        else:
            paid_slug = base_slug

        free_slug = f"{base_slug}-free"

        # 标准化pricing
        paid_pricing, _ = normalize_pricing('pro', pro_item.get('pricing_model'))
        free_pricing, _ = normalize_pricing('free', 'free')

        plan = {
            'base_slug': base_slug,
            'paid_slug': paid_slug,
            'free_slug': free_slug,
            'old_pro_slug': pro_item['slug'],
            'old_free_slug': free_item['slug'],
            'old_pro_id': pro_item['id'],
            'old_free_id': free_item['id'],
            'paid_pricing_model': paid_pricing,
            'free_pricing_model': 'free',
            'paid_display_name': pro_item['current_display_name'],
            'free_display_name': f"{free_item['current_display_name']}免费版"
                                 if '免费' not in free_item['current_display_name']
                                 else free_item['current_display_name'],
            'source': pro_item['source'],
            'source_slug': pro_item['source_slug'],
            'local_path': pro_item['local_path'],
            'action': 'rename_pro_to_base' if not existing else 'rename_pro_to_paid',
        }
        plans.append(plan)

    return plans

def analyze_version_in_slug() -> List[Dict[str, Any]]:
    """分析版本号写入slug的记录"""
    conn = get_db()
    c = conn.cursor()
    uploaded = get_uploaded_slugs()

    c.execute("""
        SELECT id, slug, current_version, current_display_name, source, source_slug, local_path
        FROM skills
        WHERE slug GLOB '*-[0-9]*'
        AND slug NOT LIKE '%-free' AND slug NOT LIKE '%-pro'
    """)

    results = []
    for row in c.fetchall():
        item = dict(row)
        item['is_uploaded'] = item['slug'] in uploaded
        # 提取版本号部分
        match = re.search(r'-(\d+[-\.]\d+[-\.]?\d*|\d+)$', item['slug'])
        if match:
            item['version_in_slug'] = match.group(1)
            item['clean_slug'] = item['slug'][:match.start()]
        else:
            item['version_in_slug'] = None
            item['clean_slug'] = item['slug']
        results.append(item)

    conn.close()
    return results

def analyze_field_inconsistency() -> List[Dict[str, Any]]:
    """分析 pricing_model 和 edition 字段不一致"""
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        SELECT id, slug, pricing_model, edition, current_display_name
        FROM skills
        WHERE (pricing_model IS NULL AND edition IS NOT NULL)
           OR (pricing_model IS NOT NULL AND edition IS NULL)
           OR (pricing_model = 'free' AND edition = 'pro')
           OR (pricing_model = 'monthly' AND edition = 'free')
    """)

    results = []
    for row in c.fetchall():
        item = dict(row)
        new_pricing, new_edition = normalize_pricing(
            item.get('edition', ''),
            item.get('pricing_model', '')
        )
        item['new_pricing_model'] = new_pricing
        item['new_edition'] = new_edition
        results.append(item)

    conn.close()
    return results

def analyze_category_pollution() -> List[Dict[str, Any]]:
    """分析 category 字段被 source 污染的问题"""
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        SELECT id, slug, category, source, source_slug
        FROM skills
        WHERE category IN ('opensource', 'original', 'enterprise')
    """)

    results = []
    for row in c.fetchall():
        item = dict(row)
        # 根据source推断正确category
        if item['category'] == 'opensource':
            item['new_category'] = 'Development'
        elif item['category'] == 'original':
            item['new_category'] = 'Productivity'
        elif item['category'] == 'enterprise':
            item['new_category'] = 'Productivity'
        results.append(item)

    conn.close()
    return results

# ============================================================
# 执行治理
# ============================================================

def execute_merge_pairs(dry_run: bool = True) -> Dict[str, Any]:
    """执行成对记录合并"""
    analysis = analyze_pairs()
    plans = plan_merge_pairs(analysis)

    result = {
        'operation': 'merge_pairs',
        'dry_run': dry_run,
        'total_pairs': len(plans),
        'executed': 0,
        'skipped': 0,
        'errors': [],
        'details': [],
    }

    if dry_run:
        result['details'] = plans[:20]  # 预览前20个
        return result

    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()

    for plan in plans:
        try:
            # 1. 更新pro记录为新slug (付费版)
            c.execute("""
                UPDATE skills SET 
                    slug = ?,
                    edition = 'paid',
                    pricing_model = ?,
                    current_display_name = ?,
                    parent_slug = NULL,
                    updated_at = ?
                WHERE id = ?
            """, (
                plan['paid_slug'],
                plan['paid_pricing_model'],
                plan['paid_display_name'],
                now,
                plan['old_pro_id']
            ))

            # 2. 更新free记录为新slug (免费版)，设置parent_slug
            c.execute("""
                UPDATE skills SET 
                    slug = ?,
                    edition = 'free',
                    pricing_model = 'free',
                    current_display_name = ?,
                    parent_slug = ?,
                    updated_at = ?
                WHERE id = ?
            """, (
                plan['free_slug'],
                plan['free_display_name'],
                plan['paid_slug'],
                now,
                plan['old_free_id']
            ))

            # 3. 记录操作日志
            for old_id, old_slug, new_slug in [
                (plan['old_pro_id'], plan['old_pro_slug'], plan['paid_slug']),
                (plan['old_free_id'], plan['old_free_slug'], plan['free_slug']),
            ]:
                c.execute("""
                    INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    old_id, 'naming_governance', now, 'clean_naming.py',
                    f'Renamed slug: {old_slug} → {new_slug}',
                    'renamed'
                ))

            result['executed'] += 1
        except Exception as e:
            result['errors'].append({
                'base_slug': plan['base_slug'],
                'error': str(e)
            })
            result['skipped'] += 1

    conn.commit()
    conn.close()
    return result

def execute_fix_fields(dry_run: bool = True) -> Dict[str, Any]:
    """修复 pricing_model 和 edition 字段不一致"""
    inconsistencies = analyze_field_inconsistency()

    result = {
        'operation': 'fix_fields',
        'dry_run': dry_run,
        'total': len(inconsistencies),
        'executed': 0,
        'details': inconsistencies[:20],
    }

    if dry_run:
        return result

    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()

    for item in inconsistencies:
        c.execute("""
            UPDATE skills SET 
                pricing_model = ?,
                edition = ?,
                updated_at = ?
            WHERE id = ?
        """, (item['new_pricing_model'], item['new_edition'], now, item['id']))

        result['executed'] += 1

    conn.commit()
    conn.close()
    return result

def execute_fix_category(dry_run: bool = True) -> Dict[str, Any]:
    """修复 category 字段污染"""
    polluted = analyze_category_pollution()

    result = {
        'operation': 'fix_category',
        'dry_run': dry_run,
        'total': len(polluted),
        'executed': 0,
        'details': polluted[:20],
    }

    if dry_run:
        return result

    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()

    for item in polluted:
        c.execute("""
            UPDATE skills SET category = ?, updated_at = ? WHERE id = ?
        """, (item['new_category'], now, item['id']))
        result['executed'] += 1

    conn.commit()
    conn.close()
    return result

# ============================================================
# 报告生成
# ============================================================

def generate_report() -> Dict[str, Any]:
    """生成完整治理报告"""
    pair_analysis = analyze_pairs()
    version_issues = analyze_version_in_slug()
    field_issues = analyze_field_inconsistency()
    category_issues = analyze_category_pollution()

    report = {
        'report_time': datetime.now().isoformat(),
        'summary': {
            'total_skills': 0,
            'pair_groups': pair_analysis['pair_groups'],
            'single_groups': pair_analysis['single_groups'],
            'version_in_slug': len(version_issues),
            'field_inconsistencies': len(field_issues),
            'category_pollution': len(category_issues),
        },
        'pair_analysis': {
            'total_with_suffix': pair_analysis['total_with_suffix'],
            'uploaded_skipped': pair_analysis['uploaded_skipped'],
            'pair_groups': pair_analysis['pair_groups'],
            'single_groups': pair_analysis['single_groups'],
        },
        'version_in_slug': [v for v in version_issues if not v['is_uploaded']],
        'field_inconsistencies': field_issues,
        'category_pollution': category_issues,
    }

    # 获取总数
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM skills")
    report['summary']['total_skills'] = c.fetchone()[0]
    conn.close()

    # 保存报告
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    return report

# ============================================================
# 命令处理
# ============================================================

def cmd_dry_run(args):
    """预览治理结果"""
    print("=" * 60)
    print("命名治理预览 (Dry Run)")
    print("=" * 60)

    report = generate_report()

    print(f"\n总Skill数: {report['summary']['total_skills']}")
    print(f"\n问题统计:")
    print(f"  1. -free/-pro 成对记录: {report['pair_analysis']['pair_groups']} 组")
    print(f"     (含后缀总数: {report['pair_analysis']['total_with_suffix']}, 已上传跳过: {report['pair_analysis']['uploaded_skipped']})")
    print(f"  2. 单独的-free/-pro: {report['pair_analysis']['single_groups']} 组")
    print(f"  3. 版本号写入slug: {report['summary']['version_in_slug']} 条")
    print(f"  4. 字段不一致: {report['summary']['field_inconsistencies']} 条")
    print(f"  5. category污染: {report['summary']['category_pollution']} 条")

    # 显示合并计划预览
    analysis = analyze_pairs()
    plans = plan_merge_pairs(analysis)

    print(f"\n合并计划预览 (前10个):")
    print(f"{'Base Slug':<35} {'付费版slug':<35} {'免费版slug':<40}")
    print("-" * 110)
    for plan in plans[:10]:
        print(f"{plan['base_slug']:<35} {plan['paid_slug']:<35} {plan['free_slug']:<40}")

    # 显示字段修复预览
    field_issues = analyze_field_inconsistency()
    print(f"\n字段修复预览 (前10个):")
    print(f"{'Slug':<35} {'旧pricing/edition':<25} {'新pricing/edition':<25}")
    print("-" * 85)
    for item in field_issues[:10]:
        old = f"{item.get('pricing_model','(NULL)')}/{item.get('edition','(NULL)')}"
        new = f"{item['new_pricing_model']}/{item['new_edition']}"
        print(f"{item['slug']:<35} {old:<25} {new:<25}")

    print(f"\n完整报告已保存: {REPORT_PATH}")
    print(f"\n执行治理: python clean_naming.py execute")

def cmd_execute(args):
    """执行治理"""
    print("=" * 60)
    print("执行命名治理")
    print("=" * 60)

    # 1. 合并成对记录
    print("\n1. 合并 -free/-pro 成对记录...")
    merge_result = execute_merge_pairs(dry_run=False)
    print(f"   总组数: {merge_result['total_pairs']}")
    print(f"   成功: {merge_result['executed']}")
    print(f"   跳过: {merge_result['skipped']}")
    if merge_result['errors']:
        print(f"   错误: {len(merge_result['errors'])}")
        for err in merge_result['errors'][:5]:
            print(f"     - {err['base_slug']}: {err['error']}")

    # 2. 修复字段不一致
    print("\n2. 修复 pricing_model/edition 字段不一致...")
    field_result = execute_fix_fields(dry_run=False)
    print(f"   总数: {field_result['total']}")
    print(f"   成功: {field_result['executed']}")

    # 3. 修复category污染
    print("\n3. 修复 category 字段污染...")
    cat_result = execute_fix_category(dry_run=False)
    print(f"   总数: {cat_result['total']}")
    print(f"   成功: {cat_result['executed']}")

    # 4. 生成最终报告
    print("\n4. 生成治理报告...")
    report = generate_report()
    print(f"   报告已保存: {REPORT_PATH}")

    print(f"\n{'=' * 60}")
    print(f"治理完成!")
    print(f"  合并成对记录: {merge_result['executed']} 组")
    print(f"  修复字段: {field_result['executed']} 条")
    print(f"  修复category: {cat_result['executed']} 条")

def cmd_report(args):
    """生成报告"""
    report = generate_report()
    print(f"报告已保存: {REPORT_PATH}")
    print(f"\n摘要:")
    for k, v in report['summary'].items():
        print(f"  {k}: {v}")

def cmd_merge_pairs(args):
    """仅合并成对记录"""
    if args.dry_run:
        result = execute_merge_pairs(dry_run=True)
        print(f"预览: {result['total_pairs']} 组待合并")
        for plan in result['details'][:10]:
            print(f"  {plan['old_pro_slug']} → {plan['paid_slug']}")
            print(f"  {plan['old_free_slug']} → {plan['free_slug']}")
    else:
        result = execute_merge_pairs(dry_run=False)
        print(f"合并完成: {result['executed']}/{result['total_pairs']}")

def cmd_fix_fields(args):
    """仅修复字段"""
    if args.dry_run:
        result = execute_fix_fields(dry_run=True)
        print(f"预览: {result['total']} 条待修复")
    else:
        result = execute_fix_fields(dry_run=False)
        print(f"修复完成: {result['executed']}/{result['total']}")

def cmd_fix_category(args):
    """仅修复category"""
    if args.dry_run:
        result = execute_fix_category(dry_run=True)
        print(f"预览: {result['total']} 条待修复")
    else:
        result = execute_fix_category(dry_run=False)
        print(f"修复完成: {result['executed']}/{result['total']}")

def main():
    parser = argparse.ArgumentParser(
        description='Skill 命名治理脚本 - 清理DB中的命名规范问题',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('dry-run', help='预览治理结果(不修改DB)')
    subparsers.add_parser('execute', help='执行全部治理')
    subparsers.add_parser('report', help='生成治理报告')

    p_merge = subparsers.add_parser('merge-pairs', help='仅合并-free/-pro成对记录')
    p_merge.add_argument('--dry-run', action='store_true', default=True)
    p_merge.add_argument('--execute', action='store_true')

    p_fields = subparsers.add_parser('fix-fields', help='仅修复字段不一致')
    p_fields.add_argument('--dry-run', action='store_true', default=True)
    p_fields.add_argument('--execute', action='store_true')

    p_cat = subparsers.add_parser('fix-category', help='仅修复category污染')
    p_cat.add_argument('--dry-run', action='store_true', default=True)
    p_cat.add_argument('--execute', action='store_true')

    args = parser.parse_args()

    if args.command == 'dry-run':
        cmd_dry_run(args)
    elif args.command == 'execute':
        cmd_execute(args)
    elif args.command == 'report':
        cmd_report(args)
    elif args.command == 'merge-pairs':
        args.dry_run = not args.execute
        cmd_merge_pairs(args)
    elif args.command == 'fix-fields':
        args.dry_run = not args.execute
        cmd_fix_fields(args)
    elif args.command == 'fix-category':
        args.dry_run = not args.execute
        cmd_fix_category(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
