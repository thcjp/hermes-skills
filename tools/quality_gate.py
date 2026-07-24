"""
Skill质量门禁脚本 (P0-1, P1-1重构)

集成现有check_debranding.py + skill_core/checks.py的9项检查
任一检查fail则总体fail, 阻止上传

P1-1变更: 从skill_core导入parser/rules/checks, 不再自带重复实现
           行为与P0-1完全一致

检查项:
  1. 去标识化检测 (复用check_debranding.check_skill_md)
  2. slug==name==folder 一致性 (skill_core.checks)
  3. slug为kebab-case格式 (skill_core.checks)
  4. SKILL.md行数 <= 500 (skill_core.checks)
  5. frontmatter 8必需字段齐全 (skill_core.checks)
  6. displayName <= 20字符 (skill_core.checks)
  7. summary <= 100字符 (skill_core.checks)
  8. description长度 50-300字符 (skill_core.checks)
  9. version为x.y.z格式 (skill_core.checks)
 10. tools为YAML数组格式 (skill_core.checks)
 11. frontmatter无XML尖括号 (skill_core.checks)
 12. 无占位符 (skill_core.checks)
 13. 无夸大词 (skill_core.checks)

用法:
  python quality_gate.py <SKILL.md路径>
  python quality_gate.py <目录>  # 批量检查
  python quality_gate.py <path> --json  # 输出JSON报告
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# 确保能导入skill_core和check_debranding
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

# 从skill_core导入(单一来源, P1-1)
from skill_core.parser import parse_frontmatter
from skill_core.checks import (
    check_slug_name_folder_consistency,
    check_line_count,
    check_required_frontmatter,
    check_display_name_length,
    check_summary_length,
    check_tools_format,
    check_no_xml_brackets,
    check_no_placeholders,
    check_no_exaggeration,
    check_slug_kebab_case,
    check_version_format,
    check_description_length,
)

# 复用现有去标识检测(依赖外部check_debranding.py)
from check_debranding import check_skill_md as check_debranding_only


# ============ 去标识化检查(保留在此, 依赖外部模块) ============

def check_debranding(skill_md_path: Path) -> dict:
    """检查1: 去标识化(复用check_debranding.py)"""
    issues, error = check_debranding_only(skill_md_path)
    if error:
        return {'name': '去标识化', 'passed': False, 'severity': 'high',
                'details': f'检查错误: {error}'}

    high_issues = [i for i in issues if i['severity'] == 'high']
    medium_issues = [i for i in issues if i['severity'] == 'medium']

    passed = len(high_issues) == 0
    details = []
    for i in issues:
        details.append(f"[{i['severity']}] {i['description']}: {i['match']}")

    return {
        'name': '去标识化',
        'passed': passed,
        'severity': 'high' if high_issues else ('medium' if medium_issues else 'low'),
        'details': details if details else ['无标识残留'],
        'issue_count': len(issues)
    }


# ============ 主检查函数 ============

def run_quality_gate(skill_md_path: Path) -> dict:
    """对单个SKILL.md运行全部质量门禁检查

    返回: {
        'skill': skill名,
        'path': 路径,
        'overall_passed': bool,
        'checks': [检查结果列表],
        'checked_at': 时间戳
    }
    """
    if not skill_md_path.exists():
        return {
            'skill': skill_md_path.parent.name,
            'path': str(skill_md_path),
            'overall_passed': False,
            'error': f'文件不存在: {skill_md_path}',
            'checked_at': datetime.now().isoformat()
        }

    content = skill_md_path.read_text(encoding='utf-8')
    fm = parse_frontmatter(content)

    checks = [
        check_debranding(skill_md_path),
        check_slug_name_folder_consistency(skill_md_path, fm),
        check_slug_kebab_case(fm),
        check_line_count(skill_md_path),
        check_required_frontmatter(fm),
        check_display_name_length(fm),
        check_summary_length(fm),
        check_description_length(fm),
        check_version_format(fm),
        check_tools_format(fm),
        check_no_xml_brackets(fm),
        check_no_placeholders(content),
        check_no_exaggeration(content),
    ]

    # 任一high级fail则总体fail
    overall_passed = all(c['passed'] for c in checks)

    return {
        'skill': skill_md_path.parent.name,
        'path': str(skill_md_path),
        'overall_passed': overall_passed,
        'total_checks': len(checks),
        'passed_checks': sum(1 for c in checks if c['passed']),
        'failed_checks': sum(1 for c in checks if not c['passed']),
        'checks': checks,
        'checked_at': datetime.now().isoformat()
    }


def format_terminal_output(result: dict) -> str:
    """格式化终端输出"""
    lines = []
    skill = result.get('skill', 'unknown')
    status = '✓ PASS' if result.get('overall_passed') else '✗ FAIL'
    lines.append(f"\n{'='*60}")
    lines.append(f"Skill: {skill}  |  总体: {status}")
    lines.append(f"{'='*60}")

    if 'error' in result:
        lines.append(f"  ERROR: {result['error']}")
        return '\n'.join(lines)

    lines.append(f"通过: {result['passed_checks']}/{result['total_checks']}  失败: {result['failed_checks']}")
    lines.append("")

    for c in result['checks']:
        mark = '✓' if c['passed'] else '✗'
        sev = f"[{c['severity']}]" if not c['passed'] else ''
        lines.append(f"  {mark} {c['name']} {sev}")
        if not c['passed']:
            for d in c['details']:
                lines.append(f"      → {d}")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Skill质量门禁检查')
    parser.add_argument('path', help='SKILL.md文件路径或包含SKILL.md的目录')
    parser.add_argument('--json', action='store_true', help='输出JSON格式报告')
    parser.add_argument('--output', '-o', help='报告输出文件路径')
    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(f"错误: 路径不存在 - {target}")
        sys.exit(1)

    # 收集要检查的SKILL.md文件
    if target.is_file():
        skill_files = [target]
    else:
        skill_files = list(target.rglob('SKILL.md'))

    if not skill_files:
        print(f"错误: 未找到SKILL.md文件 - {target}")
        sys.exit(1)

    results = []
    for sf in skill_files:
        result = run_quality_gate(sf)
        results.append(result)
        if not args.json:
            print(format_terminal_output(result))

    # 汇总
    total = len(results)
    passed = sum(1 for r in results if r.get('overall_passed'))
    failed = total - passed

    if args.json:
        report = {
            'summary': {'total': total, 'passed': passed, 'failed': failed},
            'results': results,
            'generated_at': datetime.now().isoformat()
        }
        output = json.dumps(report, ensure_ascii=False, indent=2)
        print(output)
        if args.output:
            Path(args.output).write_text(output, encoding='utf-8')
            print(f"\n报告已保存: {args.output}", file=sys.stderr)
    else:
        print(f"\n{'='*60}")
        print(f"汇总: 总计{total}  通过{passed}  失败{failed}")
        print(f"{'='*60}")

        if args.output:
            report = {
                'summary': {'total': total, 'passed': passed, 'failed': failed},
                'results': results,
                'generated_at': datetime.now().isoformat()
            }
            Path(args.output).write_text(
                json.dumps(report, ensure_ascii=False, indent=2),
                encoding='utf-8'
            )
            print(f"报告已保存: {args.output}")

    # 退出码: 有失败则1, 全通过则0
    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()
