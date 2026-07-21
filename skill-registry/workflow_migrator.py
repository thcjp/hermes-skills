#!/usr/bin/env python3
"""
Workflow States 迁移器 (Workflow Migrator)
==========================================

将 workflow_states 从当前2步 (validate + upload_free) 扩展到完整10步,
为每个 active skill 补全缺失的步骤记录。

10步工作流定义:
  Step 1: read_original    - 读取原始SKILL.md
  Step 2: parse_metadata   - 解析frontmatter
  Step 3: analyze_content  - 分析核心能力
  Step 4: select_template  - 选择设计模式模板
  Step 5: add_deps         - 添加依赖说明
  Step 6: generate_skill   - 生成新SKILL.md
  Step 7: validate         - L1+L2验证
  Step 8: upload_free      - 上传免费版
  Step 9: upload_paid      - 上传付费版
  Step 10: completed       - 完成定稿

迁移逻辑:
  根据 skills.workflow_state 推断已完成的步骤, 补全缺失记录。
  已有的 step 7 (validate) 和 step 8 (upload_free) 记录保留不动。

Usage:
    python workflow_migrator.py --dry-run    # 预览迁移结果(不写入DB)
    python workflow_migrator.py migrate      # 执行迁移
    python workflow_migrator.py verify       # 验证迁移结果
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

# 确保能导入skill_registry模块
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection


# ============================================================
# 10步工作流定义
# ============================================================

WORKFLOW_STEPS = [
    {'step_number': 1, 'step_name': 'read_original'},
    {'step_number': 2, 'step_name': 'parse_metadata'},
    {'step_number': 3, 'step_name': 'analyze_content'},
    {'step_number': 4, 'step_name': 'select_template'},
    {'step_number': 5, 'step_name': 'add_deps'},
    {'step_number': 6, 'step_name': 'generate_skill'},
    {'step_number': 7, 'step_name': 'validate'},
    {'step_number': 8, 'step_name': 'upload_free'},
    {'step_number': 9, 'step_name': 'upload_paid'},
    {'step_number': 10, 'step_name': 'completed'},
]

# skills.workflow_state → 已完成的最高步骤号
STATE_TO_MAX_STEP = {
    'step1_read_original': 1,
    'step2_parse_metadata': 2,
    'step3_analyze_content': 3,
    'step4_select_template': 4,
    'step5_add_deps': 5,
    'step6_generate_skill': 6,
    'step7_validate': 7,
    'step8_upload_free': 8,
    'step9_upload_paid': 9,
    'completed': 10,
    # 兼容旧格式
    'validate': 7,
    'upload_free': 8,
    'differentiated': 5,  # 已差异化的认为完成到 add_deps
}


# ============================================================
# 迁移核心逻辑
# ============================================================

def get_existing_steps(skill_id: int, conn) -> Dict[int, Dict]:
    """获取skill已有的workflow_states记录"""
    c = conn.cursor()
    c.execute("""
        SELECT step_number, step_name, status, completed_at, id
        FROM workflow_states
        WHERE skill_id = ?
    """, (skill_id,))
    return {r['step_number']: dict(r) for r in c.fetchall()}


def get_skills_to_migrate(conn) -> List[Dict]:
    """获取需要迁移的active skill列表"""
    c = conn.cursor()
    c.execute("""
        SELECT id, slug, workflow_state
        FROM skills
        WHERE workflow_state != 'deprecated'
          AND workflow_state IS NOT NULL AND workflow_state != ''
        ORDER BY id
    """)
    return [dict(r) for r in c.fetchall()]


def migrate_skill(skill_id: int, slug: str, workflow_state: str,
                  conn, dry_run: bool = False) -> Dict[str, Any]:
    """为单个skill补全缺失的workflow_states记录

    返回: {skill_id, slug, workflow_state, max_step, existing_steps, added_steps, skipped}
    """
    # 确定已完成的最高步骤
    max_step = STATE_TO_MAX_STEP.get(workflow_state, 0)

    if max_step == 0:
        return {
            'skill_id': skill_id, 'slug': slug,
            'workflow_state': workflow_state,
            'status': 'skipped_unknown_state'
        }

    # 获取已有记录
    existing = get_existing_steps(skill_id, conn)

    # 计算需要添加的步骤
    steps_to_add = []
    for step_info in WORKFLOW_STEPS:
        step_num = step_info['step_number']
        if step_num > max_step:
            break  # 超过已完成步骤,不需要添加
        if step_num not in existing:
            steps_to_add.append(step_info)

    if not steps_to_add:
        return {
            'skill_id': skill_id, 'slug': slug,
            'workflow_state': workflow_state,
            'max_step': max_step,
            'existing_steps': len(existing),
            'added_steps': 0,
            'status': 'no_change_needed'
        }

    if dry_run:
        return {
            'skill_id': skill_id, 'slug': slug,
            'workflow_state': workflow_state,
            'max_step': max_step,
            'existing_steps': len(existing),
            'added_steps': len(steps_to_add),
            'steps_to_add': [s['step_name'] for s in steps_to_add],
            'status': 'dry_run'
        }

    # 实际写入DB
    c = conn.cursor()
    now = datetime.now().isoformat()
    for step_info in steps_to_add:
        result_data = json.dumps({
            'backfilled': True,
            'source': 'workflow_migrator_round08',
            'inferred_from': workflow_state
        }, ensure_ascii=False)

        c.execute("""
            INSERT INTO workflow_states
                (skill_id, step_number, step_name, completed_at, status, result_data, retry_count, notes)
            VALUES (?, ?, ?, ?, 'completed', ?, 0, '迁移器自动补全')
        """, (
            skill_id,
            step_info['step_number'],
            step_info['step_name'],
            now,
            result_data
        ))

    return {
        'skill_id': skill_id, 'slug': slug,
        'workflow_state': workflow_state,
        'max_step': max_step,
        'existing_steps': len(existing),
        'added_steps': len(steps_to_add),
        'steps_added': [s['step_name'] for s in steps_to_add],
        'status': 'migrated'
    }


def run_migration(dry_run: bool = False) -> Dict[str, Any]:
    """执行完整迁移"""
    conn = get_db_connection()

    skills = get_skills_to_migrate(conn)
    print(f"待迁移skill数: {len(skills)}")

    results = {
        'total_skills': len(skills),
        'migrated': 0,
        'no_change': 0,
        'skipped': 0,
        'total_steps_added': 0,
        'details': []
    }

    for i, skill in enumerate(skills):
        result = migrate_skill(
            skill['id'], skill['slug'], skill['workflow_state'],
            conn, dry_run
        )
        results['details'].append(result)

        if result['status'] == 'migrated':
            results['migrated'] += 1
            results['total_steps_added'] += result['added_steps']
        elif result['status'] == 'dry_run':
            results['migrated'] += 1
            results['total_steps_added'] += result['added_steps']
        elif result['status'] == 'no_change_needed':
            results['no_change'] += 1
        else:
            results['skipped'] += 1

        if (i + 1) % 200 == 0:
            print(f"  进度: {i+1}/{len(skills)}")

    if not dry_run:
        conn.commit()

    conn.close()
    return results


def verify_migration() -> Dict[str, Any]:
    """验证迁移结果"""
    conn = get_db_connection()
    c = conn.cursor()

    result = {
        'total_workflow_states': 0,
        'step_distribution': {},
        'skills_with_all_steps': 0,
        'skills_missing_steps': 0,
    }

    # 总记录数
    c.execute("SELECT COUNT(*) as cnt FROM workflow_states")
    result['total_workflow_states'] = c.fetchone()['cnt']

    # 各步骤分布
    c.execute("""
        SELECT step_number, step_name, COUNT(*) as cnt
        FROM workflow_states
        GROUP BY step_number, step_name
        ORDER BY step_number
    """)
    for r in c.fetchall():
        key = f"step{r['step_number']}_{r['step_name']}"
        result['step_distribution'][key] = r['cnt']

    # 检查有多少skill拥有所有10步
    c.execute("""
        SELECT skill_id, COUNT(DISTINCT step_number) as step_count
        FROM workflow_states
        GROUP BY skill_id
        HAVING COUNT(DISTINCT step_number) = 10
    """)
    result['skills_with_all_steps'] = len(c.fetchall())

    # 检查有多少skill缺少步骤
    c.execute("""
        SELECT skill_id, COUNT(DISTINCT step_number) as step_count
        FROM workflow_states
        GROUP BY skill_id
        HAVING COUNT(DISTINCT step_number) < 10
    """)
    result['skills_missing_steps'] = len(c.fetchall())

    conn.close()
    return result


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='Workflow States 迁移器 - 将2步扩展到10步',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
命令:
  python workflow_migrator.py --dry-run    # 预览迁移结果
  python workflow_migrator.py migrate      # 执行迁移
  python workflow_migrator.py verify       # 验证迁移结果
        """
    )
    parser.add_argument('command', choices=['migrate', 'verify'],
                        nargs='?', default='verify',
                        help='migrate: 执行迁移, verify: 验证结果')
    parser.add_argument('--dry-run', action='store_true',
                        help='预览模式,不写入DB')

    args = parser.parse_args()

    if args.dry_run:
        print("=== Dry Run 模式 (不写入DB) ===\n")
        results = run_migration(dry_run=True)
        print(f"\n=== Dry Run 结果 ===")
        print(f"  总skill数: {results['total_skills']}")
        print(f"  需要迁移: {results['migrated']}")
        print(f"  无需变更: {results['no_change']}")
        print(f"  跳过(未知状态): {results['skipped']}")
        print(f"  将添加的步骤总数: {results['total_steps_added']}")
        if results['details']:
            print(f"\n  前5个迁移详情:")
            for d in results['details'][:5]:
                if d.get('steps_to_add'):
                    print(f"    {d['slug']}: +{d['added_steps']}步 {d['steps_to_add']}")
    elif args.command == 'migrate':
        print("=== 执行迁移 ===\n")
        results = run_migration(dry_run=False)
        print(f"\n=== 迁移完成 ===")
        print(f"  总skill数: {results['total_skills']}")
        print(f"  已迁移: {results['migrated']}")
        print(f"  无需变更: {results['no_change']}")
        print(f"  跳过: {results['skipped']}")
        print(f"  添加的步骤记录总数: {results['total_steps_added']}")
    elif args.command == 'verify':
        print("=== 验证迁移结果 ===\n")
        result = verify_migration()
        print(f"  workflow_states 总记录数: {result['total_workflow_states']}")
        print(f"  拥有全部10步的skill数: {result['skills_with_all_steps']}")
        print(f"  缺少步骤的skill数: {result['skills_missing_steps']}")
        print(f"\n  各步骤分布:")
        for step, cnt in result['step_distribution'].items():
            print(f"    {step}: {cnt}")


if __name__ == '__main__':
    main()
