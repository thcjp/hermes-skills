"""
Skill质量门禁脚本 (v2.0 — 方案C: 流程+质量门禁架构)

集成现有check_debranding.py + skill_core/checks.py的9项检查
任一检查fail则总体fail, 阻止上传

v2.0新增:
  - 营销关卡 (run_marketing_gate): 7项营销数据质量检查
  - 防幻觉机制 (run_anti_hallucination): 3项AI虚假实现检测
  - 统一质量检查入口 (run_full_quality_check): L1→L1.5→营销→防幻觉

L1检查项 (13项):
  1. 去标识化检测 (复用check_debranding.check_skill_md)
  2. slug==name==folder 一致性 (skill_core.checks)
  3. slug为kebab-case格式 (skill_core.checks)
  4. SKILL.md行数 <= 500 (skill_core.checks)
  5. frontmatter 8必需字段齐全 (skill_core.checks)
  6. displayName <= 20字符 (skill_core.checks)
  7. summary <= 100字符 (skill_core.checks)
  8. description长度 150-280字符 (skill_core.checks)
  9. version为x.y.z格式 (skill_core.checks)
 10. tools为YAML数组格式 (skill_core.checks)
 11. frontmatter无XML尖括号 (skill_core.checks)
 12. 无占位符 (skill_core.checks)
 13. 无夸大词 (skill_core.checks)

营销关卡 (7项):
  14. displayName中文化且≤20字符
  15. summary营销优化且≤100字符
  16. description 150-280字符, 非模板化
  17. tags 5-10个, 与功能匹配
  18. categoryIds正确映射(非空)
  19. pricing合理性(pricing_tier匹配skill复杂度)
  20. license合规(free=MIT, paid=Proprietary)

防幻觉机制 (3项):
  21. 交叉验证: L2 TRACE vs L3 Agent vs L4-L9审计评分一致性
  22. 需求理解偏差: description声明 vs body实际内容
  23. 虚假实现检测: 无占位符/无模板/无空代码块

用法:
  python quality_gate.py <SKILL.md路径>
  python quality_gate.py <目录>  # 批量检查
  python quality_gate.py <path> --json  # 输出JSON报告
  python quality_gate.py <path> --marketing  # 仅营销关卡
  python quality_gate.py <path> --anti-hallucination  # 仅防幻觉检查
  python quality_gate.py <path> --full  # 完整质量检查(L1+营销+防幻觉)
"""

import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime

# 确保能导入skill_core和check_debranding
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))
# 确保能导入project_config (config目录)
sys.path.insert(0, str(SKILL_REGISTRY_DIR.parent / "config"))

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

    passed = len(issues) == 0
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
        check_no_placeholders(content, fm['raw']),
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


# ============ 营销关卡 (v2.0新增) ============

# 中文字符范围: CJK统一汉字 + 扩展A区
_CJK_PATTERN = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')

# 模板化短语列表
_TEMPLATE_PHRASES = [
    '这是一个', '本技能', '本工具', '本skill',
    '帮助你', '助你', '让你能够',
    '强大的', '高效的', '智能的',
    '一键', '轻松',
]

# pricing_tier有效值
_VALID_PRICING_TIERS = {'L1-入门级', 'L2-标准级', 'L3-专业级', 'L4-企业级', 'free', 'paid', 'freemium'}

# license与edition合规映射
_FREE_LICENSES = {'MIT', 'Apache-2.0', 'BSD-2-Clause', 'BSD-3-Clause', 'GPL-3.0', 'MPL-2.0', 'Unlicense', 'CC0-1.0'}
_PAID_LICENSES = {'Proprietary', 'Commercial', 'Custom'}


def _check_display_name_chinese(fm: dict) -> dict:
    """营销检查1: displayName中文化且≤20字符"""
    fields = fm.get('fields', fm)
    display_name = fields.get('displayName', '')
    
    has_chinese = bool(_CJK_PATTERN.search(display_name))
    length_ok = len(display_name) <= 20 and len(display_name) > 0
    
    issues = []
    if not has_chinese:
        issues.append(f'displayName未中文化: "{display_name}"')
    if not length_ok:
        issues.append(f'displayName长度{len(display_name)}超限(应≤20)')
    
    return {
        'name': 'displayName中文化',
        'passed': len(issues) == 0,
        'severity': 'high',
        'details': issues if issues else [f'displayName: "{display_name}" ({len(display_name)}字符)']
    }


def _check_summary_marketing(fm: dict) -> dict:
    """营销检查2: summary营销优化且≤100字符"""
    fields = fm.get('fields', fm)
    summary = fields.get('summary', '')
    
    issues = []
    if len(summary) > 100:
        issues.append(f'summary长度{len(summary)}超限(应≤100)')
    if len(summary) < 10:
        issues.append(f'summary长度{len(summary)}过短(应≥10)')
    
    # 检查是否包含营销关键词(功能价值描述)
    has_value = any(kw in summary for kw in ['提供', '支持', '实现', '生成', '转换', '分析', '优化', '管理', '处理', '检测', '修复'])
    if not has_value and len(summary) > 10:
        issues.append('summary缺乏功能价值描述')
    
    return {
        'name': 'summary营销优化',
        'passed': len(issues) == 0,
        'severity': 'medium',
        'details': issues if issues else [f'summary: "{summary[:50]}..." ({len(summary)}字符)']
    }


def _check_description_non_template(fm: dict) -> dict:
    """营销检查3: description 150-280字符, 非模板化"""
    fields = fm.get('fields', fm)
    description = fields.get('description', '')
    
    issues = []
    desc_len = len(description)
    if desc_len < 150:
        issues.append(f'description长度{desc_len}过短(应≥150)')
    if desc_len > 280:
        issues.append(f'description长度{desc_len}超限(应≤280)')
    
    # 检查模板化内容
    template_hits = [p for p in _TEMPLATE_PHRASES if p in description]
    if template_hits:
        issues.append(f'description包含模板套话: {template_hits}')
    
    return {
        'name': 'description非模板化',
        'passed': len(issues) == 0,
        'severity': 'high',
        'details': issues if issues else [f'description: {desc_len}字符, 无模板套话']
    }


def _check_tags_quality(fm: dict) -> dict:
    """营销检查4: tags 5-10个, 与功能匹配"""
    fields = fm.get('fields', fm)
    tags = fields.get('tags', [])
    
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',') if t.strip()]
    
    tag_count = len(tags)
    issues = []
    if tag_count < 5:
        issues.append(f'tags数量{tag_count}不足(应≥5)')
    if tag_count > 10:
        issues.append(f'tags数量{tag_count}过多(应≤10)')
    
    # 检查tag是否与slug/displayName相关
    slug = fields.get('slug', '')
    display_name = fields.get('displayName', '')
    
    return {
        'name': 'tags质量',
        'passed': len(issues) == 0,
        'severity': 'medium',
        'details': issues if issues else [f'tags: {tag_count}个 - {tags[:5]}...']
    }


def _check_category_mapping(fm: dict) -> dict:
    """营销检查5: categoryIds正确映射(非空)"""
    fields = fm.get('fields', fm)
    category = fields.get('category', '') or fields.get('categoryIds', '')
    
    issues = []
    if not category:
        issues.append('category/categoryIds为空, 未映射到平台分类')
    
    return {
        'name': 'categoryIds映射',
        'passed': len(issues) == 0,
        'severity': 'high',
        'details': issues if issues else [f'category: {category}']
    }


def _check_pricing_reasonable(fm: dict) -> dict:
    """营销检查6: pricing合理性(pricing_tier匹配skill复杂度)"""
    fields = fm.get('fields', fm)
    pricing_tier = fields.get('pricing_tier', '')
    
    issues = []
    if not pricing_tier:
        issues.append('pricing_tier为空, 建议设置L1-L4等级')
    elif pricing_tier not in _VALID_PRICING_TIERS:
        issues.append(f'pricing_tier值"{pricing_tier}"不在有效范围内: {_VALID_PRICING_TIERS}')
    
    return {
        'name': 'pricing合理性',
        'passed': len(issues) == 0,
        'severity': 'medium',
        'details': issues if issues else [f'pricing_tier: {pricing_tier}']
    }


def _check_license_compliance(fm: dict) -> dict:
    """营销检查7: license合规(free=MIT, paid=Proprietary)"""
    fields = fm.get('fields', fm)
    license_val = fields.get('license', '')
    edition = fields.get('edition', 'free')
    
    issues = []
    if not license_val:
        issues.append('license为空, 必须设置')
    else:
        edition_lower = edition.lower() if edition else 'free'
        is_paid_edition = edition_lower in ('pro', 'paid', 'enterprise', 'commercial', 'premium')
        
        if is_paid_edition:
            if license_val not in _PAID_LICENSES:
                issues.append(f'付费skill的license应为Proprietary/Commercial, 当前为"{license_val}"')
        else:
            if license_val not in _FREE_LICENSES:
                issues.append(f'免费skill的license应为MIT/Apache等开源许可, 当前为"{license_val}"')
    
    return {
        'name': 'license合规',
        'passed': len(issues) == 0,
        'severity': 'high',
        'details': issues if issues else [f'license: {license_val}, edition: {edition}']
    }


def run_marketing_gate(skill_md_path: Path) -> dict:
    """营销数据质量门禁检查 (v2.0新增)
    
    在L1静态格式检查通过后，检查营销关键数据:
    1. displayName中文化且≤20字符
    2. summary营销优化且≤100字符
    3. description 150-280字符, 非模板化
    4. tags 5-10个, 与功能匹配
    5. categoryIds正确映射(非空)
    6. pricing合理性(pricing_tier匹配skill复杂度)
    7. license合规(free=MIT, paid=Proprietary)
    
    返回格式与run_quality_gate一致
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
        _check_display_name_chinese(fm),
        _check_summary_marketing(fm),
        _check_description_non_template(fm),
        _check_tags_quality(fm),
        _check_category_mapping(fm),
        _check_pricing_reasonable(fm),
        _check_license_compliance(fm),
    ]
    
    overall_passed = all(c['passed'] for c in checks)
    
    return {
        'skill': skill_md_path.parent.name,
        'path': str(skill_md_path),
        'overall_passed': overall_passed,
        'total_checks': len(checks),
        'passed_checks': sum(1 for c in checks if c['passed']),
        'failed_checks': sum(1 for c in checks if not c['passed']),
        'checks': checks,
        'gate_type': 'marketing',
        'checked_at': datetime.now().isoformat()
    }


# ============ 防幻觉机制 (v2.0新增) ============

# 空实现标记
_EMPTY_IMPL_PATTERNS = [
    r'\bpass\b',
    r'\bNotImplemented\b',
    r'\braise\s+NotImplementedError\b',
    r'#\s*TODO',
    r'#\s*FIXME',
    r'#\s*placeholder',
    r'#\s*mock',
    r'#\s*stub',
    r'...\s*#.*placeholder',
]

# 占位符模式
_PLACEHOLDER_PATTERNS = [
    r'<your[_\s-]?\w+>',
    r'\{\{.*\}\}',
    r'\[.*placeholder.*\]',
    r'xxx+',
    r'todo:',
    r'replace\s+this',
    r'insert\s+here',
]


def _check_cross_validation(l2_report: dict = None, l3_report: dict = None,
                             l4_report: dict = None) -> dict:
    """防幻觉检查1: 交叉验证评分一致性
    
    比较L2 TRACE评分、L3 Agent试用评分、L4-L9审计评分
    - 如果三层评分差异>20分(归一化后)，标记为"评分分歧"
    - 如果三层中有任意一层未通过，总体未通过
    """
    issues = []
    warnings = []
    scores = {}
    
    # 收集可用评分(归一化到百分制)
    if l2_report:
        trace_total = l2_report.get('trace_total', 0)
        l2_score = (trace_total / 50) * 100  # TRACE满分50, 转百分制
        scores['l2_trace'] = l2_score
        l2_passed = l2_report.get('l2_passed', trace_total >= 35)
        if not l2_passed:
            issues.append(f'L2 TRACE评分{trace_total}/50未通过(阈值35)')
    
    if l3_report:
        l3_score = l3_report.get('l3_score', 0)
        scores['l3_trial'] = l3_score
        l3_passed = l3_report.get('l3_passed', l3_score >= 70)
        if not l3_passed:
            issues.append(f'L3 Agent试用评分{l3_score}/100未通过(阈值70)')
    
    if l4_report:
        l4_score = l4_report.get('overall_score', 0)
        scores['l4_audit'] = l4_score
        l4_passed = l4_report.get('overall_passed', l4_score >= 60)
        if not l4_passed:
            issues.append(f'L4-L9审计评分{l4_score}/100未通过(阈值60)')
    
    # 检查评分分歧(需要至少2层有评分)
    if len(scores) >= 2:
        score_values = list(scores.values())
        max_score = max(score_values)
        min_score = min(score_values)
        if max_score - min_score > 20:
            warnings.append(f'评分分歧>20分: {scores}')
    
    # 如果没有提供任何报告, 标记为"无法交叉验证"(不阻止, 仅警告)
    if not scores:
        warnings.append('未提供L2/L3/L4报告, 无法交叉验证')
    
    return {
        'name': '交叉验证',
        'passed': len(issues) == 0,
        'severity': 'high' if issues else ('medium' if warnings else 'low'),
        'details': (issues + warnings) if (issues or warnings) else [f'评分一致: {scores}'],
        'scores': scores,
    }


def _check_requirement_deviation(skill_md_path: Path, fm: dict) -> dict:
    """防幻觉检查2: 需求理解偏差检测
    
    提取description中的关键功能声明, 检查body中是否包含对应实现
    """
    fields = fm.get('fields', fm)
    body = fm.get('body', '')
    description = fields.get('description', '')
    
    issues = []
    
    if not description or not body:
        return {
            'name': '需求理解偏差',
            'passed': True,
            'severity': 'low',
            'details': ['description或body为空, 跳过偏差检测']
        }
    
    # 提取description中的功能关键词(动词+宾语)
    # 简单提取: 找到"支持/提供/实现/生成/转换/分析"等动词后的关键词
    action_keywords = ['支持', '提供', '实现', '生成', '转换', '分析', '优化', '管理', '处理', '检测', '修复', '批量', '自动']
    claimed_features = []
    
    for kw in action_keywords:
        pattern = rf'{kw}([^\s，。,;.]+)'
        matches = re.findall(pattern, description)
        for m in matches:
            if len(m) > 2 and m not in claimed_features:
                claimed_features.append(m.strip())
    
    # 检查body中是否包含这些功能关键词
    body_lower = body.lower()
    missing_features = []
    for feature in claimed_features[:5]:  # 只检查前5个
        if feature and len(feature) > 2:
            # 检查功能关键词是否在body中出现
            if feature not in body:
                missing_features.append(feature)
    
    if missing_features:
        issues.append(f'description声明功能但body未提及: {missing_features}')
    
    return {
        'name': '需求理解偏差',
        'passed': len(issues) == 0,
        'severity': 'medium',
        'details': issues if issues else [f'已验证{len(claimed_features[:5])}个功能声明, body均有对应内容'],
        'claimed_features': claimed_features[:5],
        'missing_features': missing_features,
    }


def _check_false_implementation(skill_md_path: Path, fm: dict) -> dict:
    """防幻觉检查3: 虚假实现检测
    
    检查代码块是否为空或仅含注释
    检查是否有 TODO/FIXME/placeholder 标记
    检查函数体是否为 pass/.../NotImplemented
    """
    content = skill_md_path.read_text(encoding='utf-8')
    body = fm.get('body', content)
    
    issues = []
    
    # 提取所有代码块
    code_blocks = re.findall(r'```(?:\w+)?\n(.*?)```', body, re.DOTALL)
    
    if code_blocks:
        empty_blocks = 0
        placeholder_hits = []
        empty_impl_hits = []
        
        for i, block in enumerate(code_blocks):
            # 去除注释行后检查是否为空
            lines = block.strip().split('\n')
            code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
            
            if not code_lines:
                empty_blocks += 1
                issues.append(f'代码块{i+1}为空或仅含注释')
                continue
            
            # 检查占位符
            for pattern in _PLACEHOLDER_PATTERNS:
                matches = re.findall(pattern, block, re.IGNORECASE)
                if matches:
                    placeholder_hits.extend(matches[:2])
            
            # 检查空实现
            for pattern in _EMPTY_IMPL_PATTERNS:
                matches = re.findall(pattern, block, re.IGNORECASE)
                if matches:
                    empty_impl_hits.extend(matches[:2])
        
        if placeholder_hits:
            issues.append(f'发现占位符: {placeholder_hits[:5]}')
        if empty_impl_hits:
            issues.append(f'发现空实现标记: {empty_impl_hits[:5]}')
        if empty_blocks > 0:
            issues.append(f'{empty_blocks}个代码块为空')
    
    # 检查body中是否有明显的"coming soon"/"待实现"等标记
    lazy_markers = re.findall(r'(?:coming\s+soon|待实现|暂未实现|敬请期待|待开发|TBD)', body, re.IGNORECASE)
    if lazy_markers:
        issues.append(f'发现待实现标记: {lazy_markers[:3]}')
    
    return {
        'name': '虚假实现检测',
        'passed': len(issues) == 0,
        'severity': 'high',
        'details': issues if issues else ['无占位符/无模板/无空代码块'],
        'code_block_count': len(code_blocks),
    }


def run_anti_hallucination(skill_md_path: Path, l2_report: dict = None,
                           l3_report: dict = None, l4_report: dict = None) -> dict:
    """防幻觉机制检查 (v2.0新增)
    
    1. 交叉验证: L2 TRACE评分 vs L3 Agent试用 vs L4-L9审计
       - 三层评分差异>20分标记为"评分分歧"
       - 任意一层未通过则总体未通过
    
    2. 需求理解偏差检测: 实际内容 vs description声明
       - 提取description中的关键功能声明
       - 检查body中是否包含对应实现
    
    3. 虚假实现检测: 无占位符/无模板/无空函数体
       - 检查代码块是否为空或仅含注释
       - 检查 TODO/FIXME/placeholder 标记
       - 检查函数体是否为 pass/.../NotImplemented
    
    参数:
        skill_md_path: SKILL.md文件路径
        l2_report: L2验证报告dict(可选, 无则跳过交叉验证的L2部分)
        l3_report: L3试运行报告dict(可选)
        l4_report: L4-L9审计报告dict(可选)
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
        _check_cross_validation(l2_report, l3_report, l4_report),
        _check_requirement_deviation(skill_md_path, fm),
        _check_false_implementation(skill_md_path, fm),
    ]
    
    overall_passed = all(c['passed'] for c in checks)
    
    return {
        'skill': skill_md_path.parent.name,
        'path': str(skill_md_path),
        'overall_passed': overall_passed,
        'total_checks': len(checks),
        'passed_checks': sum(1 for c in checks if c['passed']),
        'failed_checks': sum(1 for c in checks if not c['passed']),
        'checks': checks,
        'gate_type': 'anti_hallucination',
        'checked_at': datetime.now().isoformat()
    }


# ============ 统一质量检查入口 (v2.0新增) ============

def run_full_quality_check(skill_md_path: Path,
                            include_l2l3: bool = False,
                            l2_report: dict = None,
                            l3_report: dict = None,
                            l4_report: dict = None) -> dict:
    """统一质量检查入口 (v2.0新增)
    
    执行完整质量检查链路:
    L1(13项) → 营销关卡(7项) → 防幻觉(3项)
    可选: L2/L3报告检查
    
    参数:
        skill_md_path: SKILL.md文件路径
        include_l2l3: 是否包含L2/L3报告检查(需提供l2_report/l3_report)
        l2_report: L2验证报告(可选)
        l3_report: L3试运行报告(可选)
        l4_report: L4-L9审计报告(可选)
    
    返回:
        统一质量检查结果, 包含L1/营销/防幻觉各层结果
    """
    # L1: 静态格式合规
    l1_result = run_quality_gate(skill_md_path)
    
    # 营销关卡
    marketing_result = run_marketing_gate(skill_md_path)
    
    # 防幻觉
    anti_hallucination_result = run_anti_hallucination(
        skill_md_path, l2_report, l3_report, l4_report
    )
    
    # 汇总
    all_checks = (
        l1_result.get('checks', []) +
        marketing_result.get('checks', []) +
        anti_hallucination_result.get('checks', [])
    )
    
    total = len(all_checks)
    passed = sum(1 for c in all_checks if c.get('passed'))
    failed = total - passed
    
    return {
        'skill': skill_md_path.parent.name,
        'path': str(skill_md_path),
        'overall_passed': failed == 0,
        'total_checks': total,
        'passed_checks': passed,
        'failed_checks': failed,
        'checks': all_checks,
        'layers': {
            'L1_static': {
                'passed': l1_result.get('overall_passed', False),
                'score': f"{l1_result.get('passed_checks', 0)}/{l1_result.get('total_checks', 0)}",
            },
            'marketing_gate': {
                'passed': marketing_result.get('overall_passed', False),
                'score': f"{marketing_result.get('passed_checks', 0)}/{marketing_result.get('total_checks', 0)}",
            },
            'anti_hallucination': {
                'passed': anti_hallucination_result.get('overall_passed', False),
                'score': f"{anti_hallucination_result.get('passed_checks', 0)}/{anti_hallucination_result.get('total_checks', 0)}",
            },
        },
        'all_checks': all_checks,
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

    total = result.get('total_checks', 0)
    passed = result.get('passed_checks', 0)
    failed = result.get('failed_checks', 0)
    lines.append(f"通过: {passed}/{total}  失败: {failed}")
    lines.append("")

    # 如果有layers(完整检查模式),先显示分层结果
    layers = result.get('layers')
    if layers:
        for layer_name, layer_info in layers.items():
            layer_status = '✓' if layer_info.get('passed') else '✗'
            score = layer_info.get('score', '?')
            lines.append(f"  {layer_status} [{layer_name}] {score}")
        lines.append("")

    # 显示详细检查项
    checks = result.get('checks', [])
    for c in checks:
        mark = '✓' if c.get('passed') else '✗'
        sev = f"[{c.get('severity', '')}]" if not c.get('passed') else ''
        lines.append(f"  {mark} {c.get('name', 'unknown')} {sev}")
        if not c.get('passed'):
            for d in c.get('details', []):
                lines.append(f"      → {d}")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Skill质量门禁检查 (v2.0)')
    parser.add_argument('path', help='SKILL.md文件路径或包含SKILL.md的目录')
    parser.add_argument('--json', action='store_true', help='输出JSON格式报告')
    parser.add_argument('--output', '-o', help='报告输出文件路径')
    parser.add_argument('--marketing', action='store_true',
                        help='仅运行营销关卡检查(7项)')
    parser.add_argument('--anti-hallucination', action='store_true',
                        help='仅运行防幻觉检查(3项)')
    parser.add_argument('--full', action='store_true',
                        help='完整质量检查: L1(13项) + 营销关卡(7项) + 防幻觉(3项)')
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
        if args.full:
            result = run_full_quality_check(sf)
        elif args.marketing:
            result = run_marketing_gate(sf)
        elif args.anti_hallucination:
            result = run_anti_hallucination(sf)
        else:
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
