#!/usr/bin/env python3
"""
上传门控检查 v2.0 (重构: 编排L1-L4, 消除冗余)
================================================
编排四层质量门禁 + 上传特有的合规/定价/安全检查:
  L1 (quality_gate) → L2-SF (source_fidelity) → L2-Cap (TRACE评分)
  → L3 (l3_function_checker) → L4 (l4_task_gate)
  → 合规检查 → 定价检查 → 上传

v2.0变更:
  - 删除与quality_gate.py重复的frontmatter/章节/字段检查
  - 编排L1-L4检查器, 不再重新实现
  - 使用skill_core.parser统一解析
  - 保留上传特有的: 合规(安全)、定价、TRACE评分

Usage:
    python upload_gate.py check <skill_dir>          # 检查单个skill
    python upload_gate.py check-all                    # 检查所有packaged skill
    python upload_gate.py check-all --json             # JSON输出
    python upload_gate.py gate <skill_dir>             # 门控检查（严格模式，失败即阻止上传）
"""

import json
import re
import sqlite3
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# 导入统一配置
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)

from config import (
    DB_PATH, MIN_TRACE_SCORE, TRACE_PASS_THRESHOLD, is_paid_skill,
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR,
    MIN_PRICE, MAX_PRICE
)

# 导入L1-L4检查器 (编排, 不重新实现)
from quality_gate import run_quality_gate
from l3_function_checker import check_l3_function
from l4_task_gate import check_l4_task_gate

# 导入统一解析层
from skill_core.parser import parse_frontmatter

# 尝试导入L2-SF检查器 (可能因源skill不存在而跳过)
try:
    from source_fidelity_checker import check_source_fidelity
    _has_sf_checker = True
except ImportError:
    _has_sf_checker = False


# ============ 工具函数 ============

def strip_code_blocks(text: str) -> str:
    """移除代码块内容，只保留正文"""
    result = []
    in_code_block = False
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        if not in_code_block:
            result.append(line)
    return '\n'.join(result)


# ============ 上传特有检查 (不覆盖L1-L4) ============

# 安全检查模式 (upload特有, L1-L4不覆盖)
SECURITY_PATTERNS = [
    (r'password\s*[:=]\s*["\'][^"\']+["\']', '不应硬编码密码'),
    (r'api_key\s*[:=]\s*["\'][^"\']+["\']', '不应硬编码API Key'),
    (r'token\s*[:=]\s*["\'][^"\']+["\']', '不应硬编码Token'),
    (r'localhost|127\.0\.0\.1|192\.168\.', '不应包含内网地址'),
    (r'\beval\s*\(', '不应使用eval函数'),
    (r'exec\s*\(\s*input', '不应执行用户输入'),
]


def get_trace_score(slug: str) -> Optional[Dict]:
    """从数据库获取TRACE评分 (L2-Cap)"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scores'")
    if not c.fetchone():
        conn.close()
        return None

    c.execute("""
        SELECT sc.total_score, sc.is_pass, sc.score_type
        FROM scores sc
        JOIN skills s ON sc.skill_id = s.id
        WHERE s.slug = ? AND sc.score_type != 'baseline'
        ORDER BY sc.scored_at DESC LIMIT 1
    """, (slug,))

    row = c.fetchone()
    conn.close()

    if row:
        total = row[0]
        if total >= TRACE_PASS_THRESHOLD + 3:
            grade = 'A+'
        elif total >= TRACE_PASS_THRESHOLD:
            grade = 'A'
        elif total >= 35:
            grade = 'B'
        elif total >= 28:
            grade = 'C'
        else:
            grade = 'D'
        return {'total': total, 'grade': grade, 'is_pass': row[1]}
    return None


def check_score(slug: str) -> List[Dict]:
    """L2-Cap: TRACE评分门控 (upload特有, 从DB读取)"""
    issues = []

    score = get_trace_score(slug)
    if not score:
        issues.append({'severity': 'BLOCKER', 'category': 'score', 'message': '无TRACE评分记录，请先运行评分'})
        return issues

    if score['total'] < MIN_TRACE_SCORE:
        issues.append({
            'severity': 'BLOCKER',
            'category': 'score',
            'message': f'TRACE评分 {score["total"]}/50 低于阈值 {MIN_TRACE_SCORE}'
        })

    if score['grade'] not in ['A', 'A+']:
        issues.append({
            'severity': 'BLOCKER',
            'category': 'score',
            'message': f'评级 {score["grade"]} 低于要求 A级'
        })

    return issues


def check_pricing(fm_fields: dict) -> List[Dict]:
    """定价检查 (upload特有, 使用skill_core.parser解析的fields)"""
    issues = []

    suggested_price = fm_fields.get('suggested_price')
    pricing_tier = fm_fields.get('pricing_tier')
    license_val = fm_fields.get('license') or ''
    edition_val = fm_fields.get('edition') or ''

    is_paid = is_paid_skill(license_val, edition_val)

    if is_paid:
        if not suggested_price or suggested_price == '0':
            issues.append({'severity': 'BLOCKER', 'category': 'pricing', 'message': '付费skill缺少suggested_price'})
        else:
            try:
                price = float(suggested_price)
                if price < MIN_PRICE or price > MAX_PRICE:
                    issues.append({'severity': 'WARN', 'category': 'pricing', 'message': f'定价 {price}元 超出合理范围({MIN_PRICE}-{MAX_PRICE})'})
            except (ValueError, TypeError):
                issues.append({'severity': 'BLOCKER', 'category': 'pricing', 'message': f'suggested_price格式错误: {suggested_price}'})

        if not pricing_tier:
            issues.append({'severity': 'WARN', 'category': 'pricing', 'message': '缺少pricing_tier分层'})

    return issues


def check_compliance(content: str) -> List[Dict]:
    """合规/安全检查 (upload特有, 不覆盖L1的去标识化检查)"""
    issues = []

    body_no_code = strip_code_blocks(content)

    for pattern, message in SECURITY_PATTERNS:
        matches = re.findall(pattern, body_no_code, re.IGNORECASE)
        if matches:
            issues.append({'severity': 'BLOCKER', 'category': 'security', 'message': f'{message} ({len(matches)}处)'})

    # TODO/FIXME检查
    todo_matches = re.findall(r'\bTODO\b|\bFIXME\b|\bHACK\b', body_no_code, re.IGNORECASE)
    if todo_matches:
        issues.append({'severity': 'WARN', 'category': 'quality', 'message': f'正文包含未完成标记: {len(todo_matches)}处'})

    return issues


# ============ 编排函数 ============

def run_gate_check(skill_dir: str) -> Dict:
    """运行完整上传门控检查: L1→L2→L3→L4→合规→定价"""
    skill_path = Path(skill_dir)
    if skill_path.is_file() and skill_path.name == 'SKILL.md':
        skill_md = skill_path
    else:
        skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return {
            'slug': skill_path.name,
            'passed': False,
            'issues': [{'severity': 'BLOCKER', 'category': 'format', 'message': 'SKILL.md不存在'}],
            'summary': 'SKILL.md文件不存在',
        }

    content = skill_md.read_text(encoding='utf-8')
    fm_result = parse_frontmatter(content)
    fm_fields = fm_result['fields']
    slug = fm_fields.get('slug') or skill_path.name

    all_issues = []
    layer_results = {}

    # === L1: 格式检查 (quality_gate, 13项) ===
    l1_result = run_quality_gate(skill_md)
    layer_results['L1'] = {
        'passed': l1_result.get('overall_passed', False),
        'checks': l1_result.get('total_checks', 0),
        'failed': l1_result.get('failed_checks', 0),
    }
    if not l1_result.get('overall_passed'):
        for check in l1_result.get('checks', []):
            if not check['passed']:
                severity = 'BLOCKER' if check['severity'] == 'high' else 'WARN'
                for detail in check['details']:
                    all_issues.append({
                        'severity': severity,
                        'category': 'L1-format',
                        'message': f"[L1] {check['name']}: {detail}"
                    })

    # === L2-SF: 源保真度 (source_fidelity_checker) ===
    if _has_sf_checker:
        try:
            l2sf_result = check_source_fidelity(slug)
            sf_score = l2sf_result.get('fidelity_score', 0)
            layer_results['L2-SF'] = {
                'passed': sf_score >= 50,
                'score': sf_score,
            }
            if sf_score < 50:
                all_issues.append({
                    'severity': 'BLOCKER',
                    'category': 'L2-SF',
                    'message': f"[L2-SF] 源保真度 {sf_score}/100 低于阈值 50"
                })
        except Exception as e:
            layer_results['L2-SF'] = {'passed': True, 'note': f'SF检查跳过: {e}'}
    else:
        layer_results['L2-SF'] = {'passed': True, 'note': 'SF检查器未导入'}

    # === L2-Cap: TRACE评分 (从DB) ===
    score_issues = check_score(slug)
    all_issues.extend(score_issues)
    score = get_trace_score(slug)
    layer_results['L2-Cap'] = {
        'passed': len(score_issues) == 0,
        'score': f"{score['total']}/50 ({score['grade']})" if score else '无评分',
    }

    # === L3: 功能验证 (l3_function_checker) ===
    l3_result = check_l3_function(slug)
    layer_results['L3'] = {
        'passed': l3_result.get('verdict') == 'PASS',
        'verdict': l3_result.get('verdict'),
        'score': l3_result.get('overall_score', 0),
    }
    if l3_result.get('verdict') == 'FAIL':
        for check_id, check in l3_result.get('checks', {}).items():
            if check['status'] == 'FAIL':
                for err in check['errors'][:2]:
                    all_issues.append({
                        'severity': 'BLOCKER',
                        'category': 'L3',
                        'message': f"[L3-{check_id}] {check['name']}: {err}"
                    })

    # === L4: 任务完成能力 (l4_task_gate) ===
    l4_result = check_l4_task_gate(slug)
    layer_results['L4'] = {
        'passed': l4_result.get('verdict') == 'PASS',
        'verdict': l4_result.get('verdict'),
        'score': l4_result.get('overall_score', 0),
    }
    if l4_result.get('verdict') == 'FAIL':
        for check_id, check in l4_result.get('checks', {}).items():
            if check['status'] == 'FAIL':
                for err in check['errors'][:2]:
                    all_issues.append({
                        'severity': 'BLOCKER',
                        'category': 'L4',
                        'message': f"[L4-{check_id}] {check['name']}: {err}"
                    })

    # === 合规检查 (upload特有) ===
    compliance_issues = check_compliance(content)
    all_issues.extend(compliance_issues)
    layer_results['compliance'] = {
        'passed': len(compliance_issues) == 0,
    }

    # === 定价检查 (upload特有) ===
    pricing_issues = check_pricing(fm_fields)
    all_issues.extend(pricing_issues)
    layer_results['pricing'] = {
        'passed': len(pricing_issues) == 0,
    }

    # === 统计 ===
    blockers = [i for i in all_issues if i['severity'] == 'BLOCKER']
    warnings = [i for i in all_issues if i['severity'] == 'WARN']

    score_str = f"{score['total']}/50 ({score['grade']})" if score else "无评分"
    price = fm_fields.get('suggested_price') or '未设置'
    tier = fm_fields.get('pricing_tier') or '未设置'

    return {
        'slug': slug,
        'skill_md': str(skill_md),
        'passed': len(blockers) == 0,
        'blocker_count': len(blockers),
        'warning_count': len(warnings),
        'score': score_str,
        'price': f"{price}元 ({tier})",
        'layers': layer_results,
        'issues': all_issues,
        'summary': f"{'通过' if len(blockers) == 0 else '阻止'} | {len(blockers)}阻断 {len(warnings)}警告 | 评分:{score_str} | 定价:{price}元",
    }


def cmd_check(skill_dir: str):
    """检查单个skill"""
    result = run_gate_check(skill_dir)

    print(f"\n{'='*80}")
    print(f"门控检查: {result['slug']}")
    print(f"{'='*80}")
    print(f"结果: {'✓ 通过' if result['passed'] else '✗ 阻止'}")
    print(f"评分: {result['score']}")
    print(f"定价: {result['price']}")
    print(f"阻断: {result['blocker_count']}  警告: {result['warning_count']}")

    # 打印各层结果
    if 'layers' in result:
        print(f"\n各层门禁:")
        for layer, info in result['layers'].items():
            status = '✓' if info.get('passed') else '✗'
            extra = ''
            if 'score' in info:
                extra = f" ({info['score']})"
            elif 'verdict' in info:
                extra = f" ({info['verdict']})"
            elif 'checks' in info:
                extra = f" ({info['checks']}项, 失败{info.get('failed', 0)})"
            print(f"  {status} {layer}{extra}")

    if result['issues']:
        print(f"\n{'='*80}")
        print("详细问题:")
        for issue in result['issues']:
            icon = '✗' if issue['severity'] == 'BLOCKER' else '⚠'
            print(f"  [{issue['severity']}] {icon} [{issue['category']}] {issue['message']}")

    return result


def cmd_check_all(json_output: bool = False):
    """检查所有packaged skill"""
    skills_dirs = [
        PACKAGED_SKILLS_DIR,
        OPENSOURCE_SKILLS_DIR,
    ]

    all_results = []
    for skills_dir in skills_dirs:
        if not skills_dir.exists():
            continue
        for d in sorted(skills_dir.iterdir()):
            if d.is_dir() and (d / "SKILL.md").exists():
                result = run_gate_check(str(d))
                all_results.append(result)

    passed = [r for r in all_results if r['passed']]
    blocked = [r for r in all_results if not r['passed']]

    if json_output:
        print(json.dumps({
            'total': len(all_results),
            'passed': len(passed),
            'blocked': len(blocked),
            'results': all_results,
        }, ensure_ascii=False, indent=2))
    else:
        print(f"\n{'='*120}")
        print(f"上传门控检查报告 - {len(all_results)}个Skills")
        print(f"{'='*120}")
        print(f"{'Slug':<40} {'结果':<8} {'阻断':>4} {'警告':>4} {'评分':<16} {'定价':<16}")
        print(f"{'-'*120}")

        for r in all_results:
            status = '✓ 通过' if r['passed'] else '✗ 阻止'
            print(f"{r['slug']:<40} {status:<8} {r['blocker_count']:>4} {r['warning_count']:>4} {r['score']:<16} {r['price']:<16}")

        print(f"\n{'='*60}")
        print(f"总计: {len(all_results)} | 通过: {len(passed)} | 阻止: {len(blocked)}")
        if all_results:
            print(f"通过率: {len(passed)/len(all_results)*100:.1f}%")

        if blocked:
            print(f"\n阻止的Skills:")
            for r in blocked:
                blockers = [i for i in r['issues'] if i['severity'] == 'BLOCKER']
                blocker_msgs = '; '.join(i['message'][:60] for i in blockers[:3])
                print(f"  ✗ {r['slug']}: {blocker_msgs}")

    # 保存报告
    report_path = REPORT_DIR / "gate_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total': len(all_results),
            'passed': len(passed),
            'blocked': len(blocked),
            'results': all_results,
        }, f, ensure_ascii=False, indent=2)

    if not json_output:
        print(f"\n报告保存到: {report_path}")

    return all_results


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]
    if cmd == 'check' and len(sys.argv) > 2:
        cmd_check(sys.argv[2])
    elif cmd == 'check-all':
        json_out = '--json' in sys.argv
        cmd_check_all(json_out)
    elif cmd == 'gate' and len(sys.argv) > 2:
        result = run_gate_check(sys.argv[2])
        if result['passed']:
            print(f"✓ 门控通过: {result['slug']}")
            sys.exit(0)
        else:
            print(f"✗ 门控阻止: {result['slug']}")
            for issue in result['issues']:
                if issue['severity'] == 'BLOCKER':
                    print(f"  [BLOCKER] {issue['message']}")
            sys.exit(1)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
