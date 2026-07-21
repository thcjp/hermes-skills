#!/usr/bin/env python3
"""
上传门控检查 v1.0
==================
每个skill上传前必须通过此门控检查，包括：
1. 正确性检查：SKILL.md格式、frontmatter字段、内容章节
2. 评分门控：TRACE评分 >= 42/50 (A级)
3. 合规检查：30项合规清单全部通过
4. 定价检查：suggested_price已设置且合理
5. 安全检查：无 prohibited content

只有全部通过才能上传。

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
from typing import Dict, List, Tuple, Optional

# 导入统一配置（修复U-21硬编码路径、U-23阈值不一致、U-24付费判断不一致）
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from config import (
    DB_PATH, MIN_TRACE_SCORE, MAX_SKILL_MD_LINES, MIN_SKILL_MD_LINES,
    MIN_DESCRIPTION_LEN, MAX_DISPLAYNAME_LEN, MIN_SUMMARY_LEN,
    TRACE_PASS_THRESHOLD, TRACE_FIELD_MAPPING, is_paid_skill,
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, REPORT_DIR,
    MIN_PRICE, MAX_PRICE
)

# TRACE维度到scores表字段的读取映射（与trace_llm_scorer.py写入映射一致，修复U-01）
TRACE_READ_MAPPING = {
    'trust': 'debranding_score',
    'reliability': 'quality_score',
    'adaptability': 'practicality_score',
    'convention': 'simplicity_score',
    'effectiveness': 'performance_score',
}

# 必须的frontmatter字段
REQUIRED_FM_FIELDS = ['slug', 'name', 'version', 'displayName', 'summary', 'license', 'description', 'tools']

# 必须的内容章节（8个标准章节）
REQUIRED_SECTIONS = [
    ('核心能力', r'^##\s+.*核心能力'),
    ('适用场景', r'^##\s+.*适用场景'),
    ('使用流程', r'^##\s+.*(使用流程|使用方法|快速开始|工作流程)'),
    ('示例', r'^##\s+.*示例'),
    ('错误处理', r'^##\s+.*错误处理'),
    ('依赖说明', r'^##\s+.*依赖说明'),
    ('常见问题', r'^##\s+.*常见问题'),
    ('已知限制', r'^##\s+.*已知限制'),
]

# 禁止的内容（仅检查frontmatter和正文非代码块部分）
# claude/anthropic只在slug/name/displayName中检查，不在body中检查
PROHIBITED_FM_PATTERNS = [
    (r'claude|anthropic', 'frontmatter包含Claude/Anthropic品牌引用'),
]

PROHIBITED_BODY_PATTERNS = [
    (r'dailyhot|narrato|fishclaw|novel_bridge|xianyu', '包含开源项目烙印'),
    (r'老田和小甜甜', '包含错误的品牌名称'),
]


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

# 合规检查清单（30项）
COMPLIANCE_CHECKS = {
    'security': [
        ('no_hardcoded_secrets', r'password\s*[:=]\s*["\'][^"\']+["\']', '不应硬编码密码'),
        ('no_api_keys', r'api_key\s*[:=]\s*["\'][^"\']+["\']', '不应硬编码API Key'),
        ('no_tokens', r'token\s*[:=]\s*["\'][^"\']+["\']', '不应硬编码Token'),
        ('no_private_urls', r'localhost|127\.0\.0\.1|192\.168\.', '不应包含内网地址'),
        ('no_eval', r'\beval\s*\(', '不应使用eval函数'),
        ('no_exec_unsafe', r'exec\s*\(\s*input', '不应执行用户输入'),
    ],
    'frontmatter': [
        ('slug_kebab', None, 'slug必须为kebab-case'),
        ('slug_unique', None, 'slug必须全局唯一'),
        ('displayname_length', None, 'displayName <= 20字符'),
        ('version_format', None, 'version必须为x.y.z格式'),
        ('summary_length', None, 'summary 10-100字符'),
        ('description_length', None, 'description 150-280字符'),
        ('license_valid', None, 'license必须为有效值'),
        ('tools_list', None, 'tools必须为列表格式'),
        ('homepage_not_github', None, 'homepage不应指向GitHub原始仓库'),
        ('tags_list', None, 'tags必须为列表格式'),
    ],
    'content': [
        ('has_core_capability', None, '必须有核心能力章节'),
        ('has_use_cases', None, '必须有适用场景章节'),
        ('has_workflow', None, '必须有使用流程章节'),
        ('has_examples', None, '必须有示例章节'),
        ('has_error_handling', None, '必须有错误处理章节'),
        ('has_dependencies', None, '必须有依赖说明章节'),
        ('has_faq', None, '必须有常见问题章节'),
        ('has_limitations', None, '必须有已知限制章节'),
        ('line_count', None, 'SKILL.md 50-500行'),
    ],
    'paid_extra': [
        ('has_pricing', None, '付费skill必须有suggested_price'),
        ('pricing_reasonable', None, '定价在0.99-99元范围内'),
        ('pricing_tier', None, '必须有pricing_tier分层'),
    ],
}


def parse_skill_md(skill_md_path: Path) -> Tuple[str, str, str]:
    """解析SKILL.md，返回(raw_content, frontmatter, body)"""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            return content, parts[1].strip(), parts[2]
    
    return content, '', content


def extract_fm_field(fm: str, field: str) -> Optional[str]:
    """提取frontmatter字段值"""
    # 尝试带引号
    match = re.search(rf'^{field}:\s*["\'](.+?)["\']\s*$', fm, re.MULTILINE)
    if match:
        return match.group(1).strip()
    # 尝试不带引号
    match = re.search(rf'^{field}:\s*(.+?)\s*$', fm, re.MULTILINE)
    if match:
        return match.group(1).strip()
    # 尝试多行description
    match = re.search(rf'^{field}:\s*\|-\s*\n((?:\s+.+\n?)+)', fm, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def check_tools_format(fm: str) -> Optional[str]:
    """检查tools字段格式，返回错误信息或None（修复U-11）
    
    正确格式：
    1. YAML数组格式：tools:\n  - read\n  - exec
    2. 内联数组格式：tools: [read, exec]
    
    错误格式：
    - tools: "read,exec"（字符串格式）
    - tools: read（无格式）
    - tools字段缺失
    """
    # 检查tools字段是否存在
    tools_exists = re.search(r'^tools:', fm, re.MULTILINE)
    if not tools_exists:
        return 'tools字段缺失'
    
    # 检查格式：必须是YAML数组或内联数组
    tools_yaml = re.search(r'^tools:\s*\n((?:\s+-\s+.+\n?)+)', fm, re.MULTILINE)
    tools_inline = re.search(r'^tools:\s*\[', fm, re.MULTILINE)
    
    if not tools_yaml and not tools_inline:
        # tools存在但格式错误
        tools_str = re.search(r'^tools:\s*(.+?)\s*$', fm, re.MULTILINE)
        if tools_str:
            return f'tools格式错误(应为YAML数组): {tools_str.group(1)}'
        return 'tools格式错误(应为YAML数组)'
    
    return None


def get_trace_score(slug: str) -> Optional[Dict]:
    """从数据库获取TRACE评分（修复U-01：使用TRACE_READ_MAPPING保证维度名称正确）"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 检查scores表是否存在
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scores'")
    if not c.fetchone():
        conn.close()
        return None
    
    # 使用映射常量明确字段语义（与trace_llm_scorer.py的写入映射一致）
    c.execute("""
        SELECT sc.total_score, 
               sc.debranding_score AS trust_score,
               sc.quality_score AS reliability_score,
               sc.practicality_score AS adaptability_score,
               sc.simplicity_score AS convention_score,
               sc.performance_score AS effectiveness_score,
               sc.differentiation_score, sc.compliance_score,
               sc.is_pass, sc.score_type
        FROM scores sc 
        JOIN skills s ON sc.skill_id = s.id 
        WHERE s.slug = ? AND sc.score_type != 'baseline'
        ORDER BY sc.scored_at DESC LIMIT 1
    """, (slug,))
    
    row = c.fetchone()
    conn.close()
    
    if row:
        total = row[0]
        # 计算评级（使用统一阈值）
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
        
        return {
            'total': total,
            'grade': grade,
            'trust': row[1],           # 正确读取Trust分
            'reliability': row[2],     # 正确读取Reliability分
            'adaptability': row[3],    # 正确读取Adaptability分
            'convention': row[4],      # 正确读取Convention分
            'effectiveness': row[5],   # 正确读取Effectiveness分
            'differentiation': row[6],
            'compliance': row[7],
            'is_pass': row[8],
        }
    return None


def check_correctness(content: str, fm: str, body: str, skill_md_path: Path) -> List[Dict]:
    """正确性检查"""
    issues = []
    
    # 1. Frontmatter格式
    if not fm:
        issues.append({'severity': 'BLOCKER', 'category': 'format', 'message': '缺少frontmatter'})
        return issues
    
    # 2. 必须字段检查
    for field in REQUIRED_FM_FIELDS:
        val = extract_fm_field(fm, field)
        if not val:
            issues.append({'severity': 'BLOCKER', 'category': 'frontmatter', 'message': f'缺少必须字段: {field}'})
    
    # 3. slug kebab-case检查
    slug = extract_fm_field(fm, 'slug')
    if slug:
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug):
            issues.append({'severity': 'BLOCKER', 'category': 'frontmatter', 'message': f'slug不符合kebab-case: {slug}'})
    
    # 4. displayName长度
    display_name = extract_fm_field(fm, 'displayName')
    if display_name and len(display_name) > MAX_DISPLAYNAME_LEN:
        issues.append({'severity': 'BLOCKER', 'category': 'frontmatter', 'message': f'displayName超过{MAX_DISPLAYNAME_LEN}字符: {len(display_name)}'})
    
    # 5. summary长度
    summary = extract_fm_field(fm, 'summary')
    if summary:
        if len(summary) < MIN_SUMMARY_LEN:
            issues.append({'severity': 'WARN', 'category': 'frontmatter', 'message': f'summary过短: {len(summary)}字符'})
        elif len(summary) > 100:
            issues.append({'severity': 'WARN', 'category': 'frontmatter', 'message': f'summary超过100字符: {len(summary)}'})
    
    # 6. description长度
    description = extract_fm_field(fm, 'description')
    if description:
        if len(description) < MIN_DESCRIPTION_LEN:
            issues.append({'severity': 'WARN', 'category': 'frontmatter', 'message': f'description过短: {len(description)}字符(建议{MIN_DESCRIPTION_LEN}+)'})
    
    # 7. version格式
    version = extract_fm_field(fm, 'version')
    if version and not re.match(r'^\d+\.\d+\.\d+', version):
        issues.append({'severity': 'BLOCKER', 'category': 'frontmatter', 'message': f'version格式错误: {version}'})
    
    # 8. tools格式检查（修复U-11：原逻辑第三条件永不触发）
    tools_error = check_tools_format(fm)
    if tools_error:
        issues.append({'severity': 'BLOCKER', 'category': 'frontmatter', 'message': tools_error})
    
    # 9. 行数检查
    line_count = len(content.split('\n'))
    if line_count > MAX_SKILL_MD_LINES:
        issues.append({'severity': 'BLOCKER', 'category': 'format', 'message': f'SKILL.md超过{MAX_SKILL_MD_LINES}行: {line_count}行'})
    elif line_count < MIN_SKILL_MD_LINES:
        issues.append({'severity': 'WARN', 'category': 'format', 'message': f'SKILL.md过短: {line_count}行'})
    
    # 10. 必须章节检查
    for section_name, pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, body, re.MULTILINE):
            issues.append({'severity': 'WARN', 'category': 'content', 'message': f'缺少章节: {section_name}'})
    
    # 11. 禁止内容检查
    # 检查frontmatter中的品牌引用
    for pattern, message in PROHIBITED_FM_PATTERNS:
        if re.search(pattern, fm, re.IGNORECASE):
            issues.append({'severity': 'BLOCKER', 'category': 'security', 'message': f'禁止内容: {message}'})
    
    # 检查正文中的禁止内容（排除代码块）
    body_no_code = strip_code_blocks(body)
    for pattern, message in PROHIBITED_BODY_PATTERNS:
        if re.search(pattern, body_no_code, re.IGNORECASE):
            issues.append({'severity': 'BLOCKER', 'category': 'security', 'message': f'禁止内容: {message}'})
    
    return issues


def check_score(slug: str) -> List[Dict]:
    """评分门控检查"""
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
    
    if score['grade'] and score['grade'] not in ['A', 'A+']:
        issues.append({
            'severity': 'BLOCKER',
            'category': 'score',
            'message': f'评级 {score["grade"]} 低于要求 A级'
        })
    
    # 各维度检查（使用正确的TRACE维度名称，修复U-01）
    dim_thresholds = {
        'trust': 5, 'reliability': 5, 'adaptability': 5, 
        'convention': 5, 'effectiveness': 5,
        'differentiation': 5, 'compliance': 5
    }
    for dim, threshold in dim_thresholds.items():
        val = score.get(dim)
        if val is not None and val < threshold:
            issues.append({
                'severity': 'WARN',
                'category': 'score',
                'message': f'{dim}维度 {val}/10 低于建议值 {threshold}'
            })
    
    return issues


def check_pricing(fm: str) -> List[Dict]:
    """定价检查（修复U-24：使用config.is_paid_skill统一付费判断）"""
    issues = []
    
    suggested_price = extract_fm_field(fm, 'suggested_price')
    pricing_tier = extract_fm_field(fm, 'pricing_tier')
    license_val = extract_fm_field(fm, 'license') or ''
    edition_val = extract_fm_field(fm, 'edition') or ''
    
    # 使用统一的付费判断逻辑
    is_paid = is_paid_skill(license_val, edition_val)
    
    if is_paid:
        if not suggested_price or suggested_price == '0':
            issues.append({'severity': 'BLOCKER', 'category': 'pricing', 'message': '付费skill缺少suggested_price'})
        else:
            try:
                price = float(suggested_price)
                if price < MIN_PRICE or price > MAX_PRICE:
                    issues.append({'severity': 'WARN', 'category': 'pricing', 'message': f'定价 {price}元 超出合理范围({MIN_PRICE}-{MAX_PRICE})'})
            except ValueError:
                issues.append({'severity': 'BLOCKER', 'category': 'pricing', 'message': f'suggested_price格式错误: {suggested_price}'})
        
        if not pricing_tier:
            issues.append({'severity': 'WARN', 'category': 'pricing', 'message': '缺少pricing_tier分层'})
    
    return issues


def check_compliance(content: str, fm: str, body: str) -> List[Dict]:
    """合规检查"""
    issues = []
    
    # 移除代码块后的正文
    body_no_code = strip_code_blocks(content)
    
    # 安全检查（在非代码块区域检查）
    for check_id, pattern, message in COMPLIANCE_CHECKS['security']:
        if pattern:
            matches = re.findall(pattern, body_no_code, re.IGNORECASE)
            if matches:
                issues.append({'severity': 'BLOCKER', 'category': 'security', 'message': f'{message} ({len(matches)}处)'})
    
    # 额外检查：TODO/FIXME在非代码块区域
    todo_matches = re.findall(r'\bTODO\b|\bFIXME\b|\bHACK\b', body_no_code, re.IGNORECASE)
    if todo_matches:
        issues.append({'severity': 'WARN', 'category': 'quality', 'message': f'正文包含未完成标记: {len(todo_matches)}处'})
    
    # homepage检查
    homepage = extract_fm_field(fm, 'homepage')
    if homepage and 'github.com' in homepage:
        issues.append({'severity': 'BLOCKER', 'category': 'frontmatter', 'message': f'homepage指向GitHub: {homepage}'})
    
    return issues


def run_gate_check(skill_dir: str) -> Dict:
    """运行完整门控检查"""
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
    
    content, fm, body = parse_skill_md(skill_md)
    slug = extract_fm_field(fm, 'slug') or skill_path.name
    
    # 运行所有检查
    all_issues = []
    all_issues.extend(check_correctness(content, fm, body, skill_md))
    all_issues.extend(check_score(slug))
    all_issues.extend(check_pricing(fm))
    all_issues.extend(check_compliance(content, fm, body))
    
    # 统计
    blockers = [i for i in all_issues if i['severity'] == 'BLOCKER']
    warnings = [i for i in all_issues if i['severity'] == 'WARN']
    
    # 获取评分
    score = get_trace_score(slug)
    score_str = f"{score['total']}/50 ({score['grade']})" if score else "无评分"
    
    # 获取定价
    price = extract_fm_field(fm, 'suggested_price') or '未设置'
    tier = extract_fm_field(fm, 'pricing_tier') or '未设置'
    
    return {
        'slug': slug,
        'skill_md': str(skill_md),
        'passed': len(blockers) == 0,
        'blocker_count': len(blockers),
        'warning_count': len(warnings),
        'score': score_str,
        'price': f"{price}元 ({tier})",
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
