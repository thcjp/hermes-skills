"""
去除标识自动化检测脚本
检查SKILL.md中是否包含禁止的标识词
"""

import re
import sys
from pathlib import Path
import sqlite3
from datetime import datetime

# 禁止的标识模式
# 注意：不使用\b，因为Python 3的\w匹配Unicode含中文，导致\b在中英文边界处失效
# 改用ASCII-only lookarounds: (?<![A-Za-z0-9_])(?![A-Za-z0-9_])
FORBIDDEN_PATTERNS = [
    # 平台烙印
    (r'(?<![A-Za-z0-9_])(clawhub|clawsec|clawdbot|openclaw)(?![A-Za-z0-9_])', '平台烙印词', 'high'),
    (r'(?<![A-Za-z0-9_])(clawhut|clawhob|clawhvb)(?![A-Za-z0-9_])', '平台烙印词变体', 'high'),

    # 项目烙印
    (r'(?<![A-Za-z0-9_])(fishclaw|narrato|dailyhot|novel_bridge|totalreclaw|kyaukyuai)(?![A-Za-z0-9_])', '项目烙印词', 'high'),

    # 内部系统词（在代码块/反引号中作为技术术语allowlist可跳过）
    (r'(?<![A-Za-z0-9_])PostgreSQL(?![A-Za-z0-9_])', '内部系统词-PostgreSQL', 'high'),
    (r'(?<![A-Za-z0-9_])MCP(?![A-Za-z0-9_])', '内部系统词-MCP', 'medium'),  # MCP在某些上下文是合法的
    (r'(?<![A-Za-z0-9_])tenant(?![A-Za-z0-9_])', '内部系统词-tenant', 'high'),
    (r'xianyu', '内部系统词-xianyu', 'high'),
    (r'老田和小甜甜', '内部代号', 'high'),

    # 溯源词
    (r'(?i)based on', '溯源词-based on', 'high'),
    (r'(?i)forked from', '溯源词-forked from', 'high'),
    (r'(?i)inspired by', '溯源词-inspired by', 'high'),
    (r'(?i)adapted from', '溯源词-adapted from', 'high'),
    (r'(?i)modified from', '溯源词-modified from', 'high'),
    (r'(?i)original:', '溯源词-original:', 'high'),

    # GitHub/原仓库URL
    (r'https?://github\.com/\S+', 'GitHub仓库URL', 'high'),
    (r'https?://\S*(clawhub|openclaw|narrato|fishclaw)\S*', '原仓库URL', 'high'),

    # 原作者署名
    (r'(?i)author:\s*\S+', '原作者署名-author字段', 'medium'),
    (r'(?i)created by\s+\w+', '原作者署名-created by', 'medium'),
]

# 允许的上下文（在这些上下文中出现是合法的）
ALLOWED_CONTEXTS = [
    'SkillHub',  # 平台名，在双平台适配章节出现合法
    'skillhub.cn',
    'SkillPay',
    '工具协议',  # MCP作为工具协议标准术语时合法
    'Agent工具协议',
    'MCP工具',  # MCP工具/MCP工具链是合法技术术语
    'MCP 工具',  # 带空格变体
    'MCP端点',
    'MCP server',
    'MCP 服务器',  # 中文变体
    'MCP生态',
    'MCP 配置',  # MCP配置是合法技术术语
    'MCP 环境',  # MCP环境是合法技术术语
    'MCP服务',  # MCP服务是合法技术术语
    'transport',  # Gateway transport类型中MCP合法
    'Transport',
    'Gateway',
    'Azure CLI',  # tenant作为Azure CLI标准参数时合法
    'az login',
    '订阅',
    '租户',
    '数据库',  # PostgreSQL作为主流数据库时合法
    '数据源',
    'SQLite',
    'MySQL',
]


def check_skill_md(file_path):
    """检查单个SKILL.md文件"""
    path = Path(file_path)
    if not path.exists():
        return [], f"File not found: {file_path}"

    content = path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]

    issues = []
    for pattern, desc, severity in FORBIDDEN_PATTERNS:
        # 直接用finditer遍历所有匹配，避免外层循环导致重复报告
        for m in re.finditer(pattern, content):
            match = m.group(0)
            start = max(0, m.start() - 50)
            end = min(len(content), m.end() + 50)
            context = content[start:end]

            # 如果在允许的上下文中，跳过
            if any(allowed in context for allowed in ALLOWED_CONTEXTS):
                continue

            # 如果在命令行参数上下文中（反引号包裹），跳过 --tenant 等
            if '`' in context:
                before = content[:m.start()]
                backtick_count_before = before.count('`')
                if backtick_count_before % 2 == 1:
                    continue

            # 如果在 ``` 代码块中，跳过技术术语allowlist（MCP/tenant/PostgreSQL等）
            # v1.2.1扩展：author:/created by在代码块中是模板字段名（如YAML模板、API配置），非原作者署名
            codeblock_starts = list(re.finditer(r'```', content[:m.start()]))
            if len(codeblock_starts) % 2 == 1:
                # v1.1技术术语allowlist：代码块中的MCP、tenant、PostgreSQL是合法的
                if 'tenant' in pattern.lower() or 'MCP' in pattern or 'PostgreSQL' in pattern:
                    continue
                # v1.2.1修复：代码块中的author:/created by是模板字段名，非原作者署名
                if 'author' in desc or 'created by' in desc:
                    continue

            issues.append({
                'pattern': pattern,
                'description': desc,
                'severity': severity,
                'match': match,
                'context': context.strip()
            })

    return issues, None


def check_all_skills(directory, exclude_dirs=None):
    """检查目录下所有SKILL.md"""
    results = {}
    exclude_dirs = exclude_dirs or []

    for skill_md in Path(directory).rglob('SKILL.md'):
        # Skip excluded directories
        if any(excluded in str(skill_md) for excluded in exclude_dirs):
            continue

        issues, error = check_skill_md(skill_md)
        if error:
            results[str(skill_md)] = {'error': error}
        elif issues:
            results[str(skill_md)] = {'issues': issues}
        else:
            results[str(skill_md)] = {'issues': []}

    return results


def generate_report(results, output_file=None):
    """生成报告"""
    total = len(results)
    clean = sum(1 for r in results.values() if not r.get('issues') and not r.get('error'))
    with_issues = sum(1 for r in results.values() if r.get('issues'))

    report = []
    report.append(f"# 去除标识检测报告")
    report.append(f"")
    report.append(f"- 检查文件总数: {total}")
    report.append(f"- 通过（无问题）: {clean}")
    report.append(f"- 有问题: {with_issues}")
    report.append(f"")

    if with_issues > 0:
        report.append(f"## 有问题的文件")
        report.append(f"")
        for file_path, result in results.items():
            issues = result.get('issues', [])
            if not issues:
                continue

            report.append(f"### {Path(file_path).parent.name}")
            report.append(f"")
            report.append(f"| 严重度 | 问题类型 | 匹配内容 | 上下文 |")
            report.append(f"|--------|----------|----------|--------|")
            for issue in issues:
                context = issue['context'][:80].replace('|', '\\|').replace('\n', ' ')
                report.append(f"| {issue['severity']} | {issue['description']} | `{issue['match']}` | {context} |")
            report.append(f"")

    report_text = '\n'.join(report)

    if output_file:
        Path(output_file).write_text(report_text, encoding='utf-8')
        print(f"Report saved to: {output_file}")

    return report_text


def update_database_with_check_results(results):
    """将检测结果更新到数据库"""
    conn = sqlite3.connect(r'd:\skills\skill-registry.db')
    c = conn.cursor()

    now = datetime.now().isoformat()
    debranding_pass_count = 0
    debranding_fail_count = 0

    for file_path, result in results.items():
        issues = result.get('issues', [])
        slug = Path(file_path).parent.name

        # Find skill in database
        c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        if not row:
            continue

        skill_id = row[0]
        status = 'pass' if not issues else 'fail'

        if status == 'pass':
            debranding_pass_count += 1
        else:
            debranding_fail_count += 1

        # Record operation
        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (skill_id, 'debranding_check', now, 'script',
              f'Found {len(issues)} issues', status))

    conn.commit()
    conn.close()

    print(f"\nDatabase updated:")
    print(f"  Debranding pass: {debranding_pass_count}")
    print(f"  Debranding fail: {debranding_fail_count}")


if __name__ == '__main__':

    target_dir = sys.argv[1] if len(sys.argv) > 1 else r'd:\skills\differentiated-skills'

    # Exclude the skill-production-standards itself (it documents the detection rules)
    exclude_dirs = ['skill-production-standards']

    print(f"Scanning: {target_dir}")
    print(f"Excluding: {exclude_dirs}")
    results = check_all_skills(target_dir, exclude_dirs=exclude_dirs)

    report = generate_report(results, r'd:\skills\skill-registry\debranding-report.md')
    print(report[:500] + '...' if len(report) > 500 else report)

    update_database_with_check_results(results)
