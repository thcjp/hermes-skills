#!/usr/bin/env python3
"""
Skill 注册表健康检查 (Health Check)
====================================

一键输出 DB + 文件 + 平台健康报告，检测注册表整体状态。

设计理念:
  - 不修改任何数据，纯只读检查
  - 分三个维度: DB完整性 / 文件完整性 / 平台状态
  - overall_status: healthy(无问题) / warning(有警告) / critical(有严重问题)
  - 支持 --section 参数按维度单独检查
  - 支持 --json 输出和 -o 保存报告

Usage:
    python health_check.py                    # 完整健康报告（终端输出）
    python health_check.py --json             # JSON 格式输出
    python health_check.py --section db       # 仅检查 DB
    python health_check.py --section files    # 仅检查文件
    python health_check.py --section platform # 仅检查平台
    python health_check.py -o report.json     # 保存报告到文件

检查项:
    DB: workflow_state覆盖率 / 孤儿记录 / 重复slug / TRACE评分覆盖率 / 状态分布
    文件: local_path有效性 / SKILL.md存在性 / 行数合规 / frontmatter完整性
    平台: 上传成功率 / 平台分布 / 付费分布 / 上传流水线状态
"""

import sys
import json
import argparse
import random
import re
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

# 确保能导入skill_registry模块
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import (
    DB_PATH, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR,
    MAX_SKILL_MD_LINES, get_db_connection
)

# 文件检查抽样数量
FILE_SAMPLE_SIZE = 50

# frontmatter 8 必需字段
REQUIRED_FRONTMATTER_FIELDS = [
    'slug', 'name', 'version', 'displayName',
    'summary', 'license', 'description', 'tools'
]

# 严重问题阈值
CRITICAL_ORPHAN_THRESHOLD = 10       # 孤儿记录 ≥10 为 critical
CRITICAL_DUPLICATE_THRESHOLD = 5     # 重复slug ≥5 为 critical
WARNING_UPLOAD_SUCCESS_RATE = 90.0   # 上传成功率 <90% 为 warning
CRITICAL_UPLOAD_SUCCESS_RATE = 70.0  # 上传成功率 <70% 为 critical


# ============================================================
# DB 完整性检查
# ============================================================

def check_db_health() -> Dict[str, Any]:
    """检查 DB 完整性

    检查项:
    1. workflow_state 覆盖率
    2. 孤儿记录数 (local_path 指向不存在的文件)
    3. 重复 slug (同一 slug 多条 active 记录)
    4. TRACE 评分覆盖率
    5. workflow_state 分布
    """
    result = {
        'total_skills': 0,
        'active': 0,
        'deprecated': 0,
        'null_state': 0,
        'workflow_state_coverage': '0%',
        'orphan_records': 0,
        'duplicate_slugs': 0,
        'trace_score_coverage': '0%',
        'state_distribution': {},
        'issues': []
    }

    try:
        conn = get_db_connection()
        c = conn.cursor()

        # 1. 总数和状态分布
        c.execute("""
            SELECT
                COUNT(*) as total,
                SUM(CASE WHEN workflow_state = 'deprecated' THEN 1 ELSE 0 END) as deprecated,
                SUM(CASE WHEN workflow_state IS NULL OR workflow_state = '' THEN 1 ELSE 0 END) as null_state,
                SUM(CASE WHEN workflow_state IS NOT NULL AND workflow_state != '' AND workflow_state != 'deprecated' THEN 1 ELSE 0 END) as active
            FROM skills
        """)
        row = c.fetchone()
        result['total_skills'] = row['total']
        result['deprecated'] = row['deprecated']
        result['null_state'] = row['null_state']
        result['active'] = row['active']

        if result['total_skills'] > 0:
            coverage = (result['total_skills'] - result['null_state']) / result['total_skills'] * 100
            result['workflow_state_coverage'] = f"{coverage:.1f}%"

        if result['null_state'] > 0:
            result['issues'].append({
                'severity': 'warning',
                'message': f"{result['null_state']} 条记录 workflow_state 为空"
            })

        # 2. workflow_state 详细分布
        c.execute("""
            SELECT workflow_state, COUNT(*) as cnt
            FROM skills
            GROUP BY workflow_state
            ORDER BY cnt DESC
        """)
        for r in c.fetchall():
            state = r['workflow_state'] if r['workflow_state'] else '(NULL)'
            result['state_distribution'][state] = r['cnt']

        # 3. 孤儿记录 (local_path 不存在)
        c.execute("""
            SELECT id, slug, local_path
            FROM skills
            WHERE workflow_state != 'deprecated'
              AND local_path IS NOT NULL AND local_path != ''
        """)
        orphan_count = 0
        orphan_samples = []
        for r in c.fetchall():
            path = Path(r['local_path'])
            # local_path 可能是目录或文件
            if not path.exists():
                # 尝试作为目录，检查是否有 SKILL.md
                skill_md = path / 'SKILL.md'
                if not skill_md.exists():
                    orphan_count += 1
                    if len(orphan_samples) < 5:
                        orphan_samples.append({
                            'id': r['id'],
                            'slug': r['slug'],
                            'path': r['local_path']
                        })

        result['orphan_records'] = orphan_count
        if orphan_count > 0:
            severity = 'critical' if orphan_count >= CRITICAL_ORPHAN_THRESHOLD else 'warning'
            result['issues'].append({
                'severity': severity,
                'message': f"{orphan_count} 条记录 local_path 指向不存在的文件",
                'samples': orphan_samples
            })

        # 4. 重复 slug (多条 active 记录)
        c.execute("""
            SELECT slug, COUNT(*) as cnt
            FROM skills
            WHERE workflow_state != 'deprecated'
            GROUP BY slug
            HAVING COUNT(*) > 1
            ORDER BY cnt DESC
        """)
        dup_count = 0
        dup_samples = []
        for r in c.fetchall():
            dup_count += r['cnt'] - 1  # 每组多出的记录数
            if len(dup_samples) < 5:
                dup_samples.append({'slug': r['slug'], 'count': r['cnt']})

        result['duplicate_slugs'] = dup_count
        if dup_count > 0:
            severity = 'critical' if dup_count >= CRITICAL_DUPLICATE_THRESHOLD else 'warning'
            result['issues'].append({
                'severity': severity,
                'message': f"{dup_count} 条重复 slug 记录",
                'samples': dup_samples
            })

        # 5. TRACE 评分覆盖率
        c.execute("""
            SELECT COUNT(DISTINCT s.id) as scored_count
            FROM skills s
            INNER JOIN scores sc ON s.id = sc.skill_id
            WHERE sc.score_type = 'trace_llm'
              AND s.workflow_state != 'deprecated'
        """)
        scored = c.fetchone()['scored_count']
        if result['active'] > 0:
            result['trace_score_coverage'] = f"{scored / result['active'] * 100:.1f}%"
        else:
            result['trace_score_coverage'] = '0%'

        result['scored_skills'] = scored

        conn.close()

    except Exception as e:
        result['issues'].append({
            'severity': 'critical',
            'message': f"DB 检查异常: {str(e)}"
        })

    return result


# ============================================================
# 文件完整性检查
# ============================================================

def check_file_health(sample_size: int = FILE_SAMPLE_SIZE) -> Dict[str, Any]:
    """检查文件完整性 (抽样检查)

    检查项:
    1. local_path 有效性
    2. SKILL.md 存在性
    3. 文件行数合规 (≤500)
    4. frontmatter 8 必需字段完整性
    """
    result = {
        'checked_count': 0,
        'valid_paths': 0,
        'invalid_paths': 0,
        'skill_md_exists': 0,
        'skill_md_missing': 0,
        'line_count_compliant': 0,
        'line_count_violations': 0,
        'frontmatter_complete': 0,
        'frontmatter_incomplete': 0,
        'issues': []
    }

    try:
        conn = get_db_connection()
        c = conn.cursor()

        # 获取所有 active 记录
        c.execute("""
            SELECT id, slug, local_path
            FROM skills
            WHERE workflow_state != 'deprecated'
              AND local_path IS NOT NULL AND local_path != ''
            ORDER BY RANDOM()
            LIMIT ?
        """, (sample_size,))

        records = c.fetchall()
        conn.close()

        result['checked_count'] = len(records)

        for r in records:
            slug = r['slug']
            local_path_str = r['local_path']
            path = Path(local_path_str)

            # 1. local_path 有效性
            if not path.exists():
                result['invalid_paths'] += 1
                if result['invalid_paths'] <= 5:
                    result['issues'].append({
                        'severity': 'warning',
                        'message': f"路径不存在: {slug} -> {local_path_str}"
                    })
                continue

            result['valid_paths'] += 1

            # 2. 确定 SKILL.md 路径
            if path.is_dir():
                skill_md_path = path / 'SKILL.md'
            elif path.name == 'SKILL.md':
                skill_md_path = path
            else:
                skill_md_path = path

            if not skill_md_path.exists():
                # 尝试在 packaged-skills/skillhub 中查找
                packaged_path = PACKAGED_SKILLS_DIR / slug / 'SKILL.md'
                if packaged_path.exists():
                    skill_md_path = packaged_path
                else:
                    result['skill_md_missing'] += 1
                    if result['skill_md_missing'] <= 5:
                        result['issues'].append({
                            'severity': 'warning',
                            'message': f"SKILL.md 不存在: {slug}"
                        })
                    continue

            result['skill_md_exists'] += 1

            # 3. 读取文件内容检查行数和 frontmatter
            try:
                content = skill_md_path.read_text(encoding='utf-8')
                if content.startswith('\ufeff'):
                    content = content[1:]

                lines = content.split('\n')
                line_count = len(lines)

                if line_count <= MAX_SKILL_MD_LINES:
                    result['line_count_compliant'] += 1
                else:
                    result['line_count_violations'] += 1
                    if result['line_count_violations'] <= 3:
                        result['issues'].append({
                            'severity': 'warning',
                            'message': f"行数超标: {slug} ({line_count}行 > {MAX_SKILL_MD_LINES})"
                        })

                # 4. frontmatter 完整性
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        fm_text = parts[1]
                        missing_fields = []
                        for field in REQUIRED_FRONTMATTER_FIELDS:
                            # 检查字段是否存在 (字段名:)
                            if not re.search(rf'^{field}\s*:', fm_text, re.MULTILINE):
                                missing_fields.append(field)

                        if missing_fields:
                            result['frontmatter_incomplete'] += 1
                            if result['frontmatter_incomplete'] <= 3:
                                result['issues'].append({
                                    'severity': 'warning',
                                    'message': f"frontmatter 缺失字段: {slug} -> {missing_fields}"
                                })
                        else:
                            result['frontmatter_complete'] += 1
                    else:
                        result['frontmatter_incomplete'] += 1
                else:
                    result['frontmatter_incomplete'] += 1
                    if result['frontmatter_incomplete'] <= 3:
                        result['issues'].append({
                            'severity': 'warning',
                            'message': f"无 frontmatter: {slug}"
                        })

            except Exception as e:
                result['issues'].append({
                    'severity': 'warning',
                    'message': f"读取文件失败: {slug} -> {str(e)}"
                })

    except Exception as e:
        result['issues'].append({
            'severity': 'critical',
            'message': f"文件检查异常: {str(e)}"
        })

    return result


# ============================================================
# 平台状态检查
# ============================================================

def check_platform_health() -> Dict[str, Any]:
    """检查平台状态

    检查项:
    1. 上传成功率 (success / total)
    2. 平台分布 (skillhub vs clawhub)
    3. 付费分布 (is_paid=1 vs is_paid=0/NULL)
    4. 上传流水线状态 (step8_upload_free 等)
    """
    result = {
        'total_uploads': 0,
        'success_count': 0,
        'fail_count': 0,
        'upload_success_rate': '0%',
        'platform_distribution': {},
        'pending_review': 0,
        'free_count': 0,
        'paid_count': 0,
        'upload_pipeline': {},
        'issues': []
    }

    try:
        conn = get_db_connection()
        c = conn.cursor()

        # 1. 上传记录统计
        c.execute("""
            SELECT
                COUNT(*) as total,
                SUM(CASE WHEN upload_status = 'success' THEN 1 ELSE 0 END) as success,
                SUM(CASE WHEN upload_status IN ('fail', 'failed') THEN 1 ELSE 0 END) as fail
            FROM platform_uploads
        """)
        row = c.fetchone()
        result['total_uploads'] = row['total']
        result['success_count'] = row['success']
        result['fail_count'] = row['fail']

        if row['total'] > 0:
            rate = row['success'] / row['total'] * 100
            result['upload_success_rate'] = f"{rate:.1f}%"

            if rate < CRITICAL_UPLOAD_SUCCESS_RATE:
                result['issues'].append({
                    'severity': 'critical',
                    'message': f"上传成功率过低: {rate:.1f}% (< {CRITICAL_UPLOAD_SUCCESS_RATE}%)"
                })
            elif rate < WARNING_UPLOAD_SUCCESS_RATE:
                result['issues'].append({
                    'severity': 'warning',
                    'message': f"上传成功率偏低: {rate:.1f}% (< {WARNING_UPLOAD_SUCCESS_RATE}%)"
                })

        # 2. 平台分布
        c.execute("""
            SELECT platform, COUNT(*) as cnt
            FROM platform_uploads
            GROUP BY platform
            ORDER BY cnt DESC
        """)
        for r in c.fetchall():
            platform = r['platform'] if r['platform'] else '(unknown)'
            result['platform_distribution'][platform] = r['cnt']

        # 3. 上传状态详细分布
        c.execute("""
            SELECT upload_status, COUNT(*) as cnt
            FROM platform_uploads
            GROUP BY upload_status
            ORDER BY cnt DESC
        """)
        result['upload_status_distribution'] = {}
        for r in c.fetchall():
            status = r['upload_status'] if r['upload_status'] else '(unknown)'
            result['upload_status_distribution'][status] = r['cnt']

        # 4. 付费分布
        c.execute("""
            SELECT
                SUM(CASE WHEN is_paid = 1 THEN 1 ELSE 0 END) as paid,
                SUM(CASE WHEN is_paid = 0 THEN 1 ELSE 0 END) as free,
                SUM(CASE WHEN is_paid IS NULL THEN 1 ELSE 0 END) as unspecified
            FROM skills
            WHERE workflow_state != 'deprecated'
        """)
        row = c.fetchone()
        result['paid_count'] = row['paid']
        result['free_count'] = row['free']
        result['unspecified_paid'] = row['unspecified']

        # 5. 上传流水线状态 (在 step8_upload_free 等状态的 skill)
        c.execute("""
            SELECT workflow_state, COUNT(*) as cnt
            FROM skills
            WHERE workflow_state LIKE 'step8%' OR workflow_state LIKE 'step9%' OR workflow_state = 'completed'
            GROUP BY workflow_state
            ORDER BY cnt DESC
        """)
        for r in c.fetchall():
            result['upload_pipeline'][r['workflow_state']] = r['cnt']

        # 6. 待审核数 (上传到 skillhub 但未 completed 的)
        c.execute("""
            SELECT COUNT(DISTINCT s.id) as pending
            FROM skills s
            INNER JOIN platform_uploads pu ON s.id = pu.skill_id
            WHERE pu.platform = 'skillhub'
              AND pu.upload_status = 'success'
              AND s.workflow_state != 'completed'
              AND s.workflow_state != 'deprecated'
        """)
        result['pending_review'] = c.fetchone()['pending']

        if result['pending_review'] > 0:
            result['issues'].append({
                'severity': 'info',
                'message': f"{result['pending_review']} 个 skill 已上传 SkillHub 但未完成审核"
            })

        conn.close()

    except Exception as e:
        result['issues'].append({
            'severity': 'critical',
            'message': f"平台检查异常: {str(e)}"
        })

    return result


# ============================================================
# 综合健康报告
# ============================================================

def determine_overall_status(db_health: Dict, file_health: Dict, platform_health: Dict) -> str:
    """根据三个维度的检查结果确定整体健康状态

    规则:
    - critical: 任意维度有 critical 级别问题
    - warning: 任意维度有 warning 级别问题 (但无 critical)
    - healthy: 所有维度无问题
    """
    all_issues = (
        db_health.get('issues', []) +
        file_health.get('issues', []) +
        platform_health.get('issues', [])
    )

    has_critical = any(i.get('severity') == 'critical' for i in all_issues)
    has_warning = any(i.get('severity') == 'warning' for i in all_issues)

    if has_critical:
        return 'critical'
    elif has_warning:
        return 'warning'
    else:
        return 'healthy'


def generate_recommendations(db_health: Dict, file_health: Dict, platform_health: Dict) -> List[str]:
    """根据检查结果生成改进建议"""
    recommendations = []

    # DB 建议
    if db_health['null_state'] > 0:
        recommendations.append(f"修复 {db_health['null_state']} 条 workflow_state 为空的记录")
    if db_health['orphan_records'] > 0:
        recommendations.append(f"清理 {db_health['orphan_records']} 条孤儿记录 (local_path 无效)")
    if db_health['duplicate_slugs'] > 0:
        recommendations.append(f"合并 {db_health['duplicate_slugs']} 条重复 slug 记录")
    trace_cov = float(db_health['trace_score_coverage'].rstrip('%'))
    if trace_cov < 50:
        recommendations.append(f"TRACE 评分覆盖率仅 {db_health['trace_score_coverage']}，建议批量补充 L2 验证")

    # 文件建议
    if file_health['invalid_paths'] > 0:
        recommendations.append(f"修复 {file_health['invalid_paths']} 个无效文件路径")
    if file_health['skill_md_missing'] > 0:
        recommendations.append(f"补充 {file_health['skill_md_missing']} 个缺失的 SKILL.md")
    if file_health['line_count_violations'] > 0:
        recommendations.append(f"精简 {file_health['line_count_violations']} 个超 500 行的 SKILL.md")
    if file_health['frontmatter_incomplete'] > 0:
        recommendations.append(f"补全 {file_health['frontmatter_incomplete']} 个 frontmatter 缺失字段")

    # 平台建议
    if platform_health['fail_count'] > 0:
        recommendations.append(f"排查 {platform_health['fail_count']} 个上传失败记录")
    if platform_health['pending_review'] > 0:
        recommendations.append(f"跟踪 {platform_health['pending_review']} 个待审核 skill 的审核状态")

    if not recommendations:
        recommendations.append("所有检查项通过，注册表状态健康")

    return recommendations


def run_full_check(section: str = None, output_json: bool = False,
                   output_file: str = None) -> Dict[str, Any]:
    """运行完整健康检查

    参数:
    - section: 指定检查维度 (db/files/platform)，None 表示全部
    - output_json: 是否输出 JSON 格式
    - output_file: 保存报告到文件
    """
    report = {
        'checked_at': datetime.now().isoformat(),
        'db_path': DB_PATH,
        'overall_status': 'unknown'
    }

    db_health = None
    file_health = None
    platform_health = None

    if section is None or section == 'db':
        print("正在检查 DB 完整性..." if not output_json else "", file=sys.stderr)
        db_health = check_db_health()
        report['db_health'] = db_health

    if section is None or section == 'files':
        print("正在检查文件完整性..." if not output_json else "", file=sys.stderr)
        file_health = check_file_health()
        report['file_health'] = file_health

    if section is None or section == 'platform':
        print("正在检查平台状态..." if not output_json else "", file=sys.stderr)
        platform_health = check_platform_health()
        report['platform_health'] = platform_health

    # 确定整体状态
    if db_health and file_health and platform_health:
        report['overall_status'] = determine_overall_status(db_health, file_health, platform_health)
        report['recommendations'] = generate_recommendations(db_health, file_health, platform_health)
    elif db_health:
        report['overall_status'] = 'critical' if any(i.get('severity') == 'critical' for i in db_health.get('issues', [])) else \
                                    'warning' if any(i.get('severity') == 'warning' for i in db_health.get('issues', [])) else 'healthy'
    elif file_health:
        report['overall_status'] = 'critical' if any(i.get('severity') == 'critical' for i in file_health.get('issues', [])) else \
                                    'warning' if any(i.get('severity') == 'warning' for i in file_health.get('issues', [])) else 'healthy'
    elif platform_health:
        report['overall_status'] = 'critical' if any(i.get('severity') == 'critical' for i in platform_health.get('issues', [])) else \
                                    'warning' if any(i.get('severity') == 'warning' for i in platform_health.get('issues', [])) else 'healthy'

    # 保存报告
    if output_file:
        report_path = Path(output_file)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        report['report_path'] = str(report_path)

    return report


# ============================================================
# 终端输出格式化
# ============================================================

def print_report(report: Dict[str, Any]):
    """格式化输出健康报告到终端"""

    status_emoji = {
        'healthy': '✓',
        'warning': '⚠',
        'critical': '✗'
    }
    status_label = {
        'healthy': '健康',
        'warning': '警告',
        'critical': '严重'
    }

    overall = report.get('overall_status', 'unknown')
    emoji = status_emoji.get(overall, '?')
    label = status_label.get(overall, '未知')

    print(f"\n{'='*70}")
    print(f"  Skill 注册表健康报告")
    print(f"{'='*70}")
    print(f"  检查时间: {report['checked_at']}")
    print(f"  数据库: {report['db_path']}")
    print(f"  整体状态: {emoji} {label}")
    print(f"{'='*70}")

    # DB 健康
    if 'db_health' in report:
        db = report['db_health']
        print(f"\n--- DB 完整性 ---")
        print(f"  总记录数: {db['total_skills']}")
        print(f"  Active: {db['active']} | Deprecated: {db['deprecated']} | NULL状态: {db['null_state']}")
        print(f"  workflow_state 覆盖率: {db['workflow_state_coverage']}")
        print(f"  孤儿记录: {db['orphan_records']}")
        print(f"  重复 slug: {db['duplicate_slugs']}")
        print(f"  TRACE 评分覆盖率: {db['trace_score_coverage']} ({db.get('scored_skills', 0)} 个已评分)")
        print(f"  状态分布:")
        for state, cnt in db.get('state_distribution', {}).items():
            print(f"    {state}: {cnt}")
        if db.get('issues'):
            print(f"  问题:")
            for issue in db['issues']:
                print(f"    [{issue['severity']}] {issue['message']}")

    # 文件健康
    if 'file_health' in report:
        fh = report['file_health']
        print(f"\n--- 文件完整性 (抽样 {fh['checked_count']} 条) ---")
        print(f"  有效路径: {fh['valid_paths']} | 无效路径: {fh['invalid_paths']}")
        print(f"  SKILL.md 存在: {fh['skill_md_exists']} | 缺失: {fh['skill_md_missing']}")
        print(f"  行数合规(≤{MAX_SKILL_MD_LINES}): {fh['line_count_compliant']} | 超标: {fh['line_count_violations']}")
        print(f"  frontmatter 完整: {fh['frontmatter_complete']} | 不完整: {fh['frontmatter_incomplete']}")
        if fh.get('issues'):
            print(f"  问题:")
            for issue in fh['issues']:
                print(f"    [{issue['severity']}] {issue['message']}")

    # 平台健康
    if 'platform_health' in report:
        ph = report['platform_health']
        print(f"\n--- 平台状态 ---")
        print(f"  上传记录: {ph['total_uploads']} (成功: {ph['success_count']}, 失败: {ph['fail_count']})")
        print(f"  上传成功率: {ph['upload_success_rate']}")
        print(f"  待审核: {ph['pending_review']}")
        print(f"  付费分布: 付费 {ph['paid_count']} | 免费 {ph['free_count']} | 未指定 {ph.get('unspecified_paid', 0)}")
        print(f"  平台分布: {ph.get('platform_distribution', {})}")
        print(f"  上传状态分布: {ph.get('upload_status_distribution', {})}")
        print(f"  上传流水线: {ph.get('upload_pipeline', {})}")
        if ph.get('issues'):
            print(f"  问题:")
            for issue in ph['issues']:
                print(f"    [{issue['severity']}] {issue['message']}")

    # 建议
    if 'recommendations' in report:
        print(f"\n--- 改进建议 ---")
        for i, rec in enumerate(report['recommendations'], 1):
            print(f"  {i}. {rec}")

    print(f"\n{'='*70}\n")


# ============================================================
# CLI 入口
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='Skill 注册表健康检查',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
检查维度:
  db        DB 完整性 (workflow_state/orphan/duplicate/trace_score)
  files     文件完整性 (local_path/SKILL.md/行数/frontmatter)
  platform  平台状态 (上传成功率/付费分布/待审核)

示例:
  python health_check.py                    # 完整报告
  python health_check.py --section db       # 仅 DB
  python health_check.py --json -o rep.json # JSON 保存到文件
        """
    )
    parser.add_argument('--section', choices=['db', 'files', 'platform'],
                        help='仅检查指定维度')
    parser.add_argument('--json', action='store_true',
                        help='输出 JSON 格式')
    parser.add_argument('-o', '--output', type=str,
                        help='保存报告到指定文件')

    args = parser.parse_args()

    report = run_full_check(
        section=args.section,
        output_json=args.json,
        output_file=args.output
    )

    if args.json:
        # JSON 输出 (不包含 report_path 如果未指定 -o)
        if not args.output:
            print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report)

    # 退出码: 0=healthy, 1=warning, 2=critical
    status = report.get('overall_status', 'critical')
    sys.exit(0 if status == 'healthy' else 1 if status == 'warning' else 2)


if __name__ == '__main__':
    main()
