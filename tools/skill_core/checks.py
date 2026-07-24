"""
skill_core.checks - 通用检查函数(单一来源)

从quality_gate.py迁移, 消除quality_gate.py和其他模块的检查逻辑重复
所有检查函数返回统一格式: {
    'name': 检查名,
    'passed': bool,
    'severity': 'high'|'medium'|'low',
    'details': [str],
    'issue_count': int
}

注意: 去标识化检查(check_debranding)依赖check_debranding.py,
      不在此模块, 仍在quality_gate.py中(因为它依赖外部模块)
"""

import re
from pathlib import Path

from .parser import parse_frontmatter
from .rules import (
    MAX_SKILL_MD_LINES, MAX_DISPLAY_NAME_LEN, MAX_SUMMARY_LEN,
    MIN_DESCRIPTION_LEN, MAX_DESCRIPTION_LEN,
    REQUIRED_FRONTMATTER_FIELDS,
    PLACEHOLDER_PATTERNS, EXAGGERATION_WORDS,
    SLUG_KEBAB_PATTERN, VERSION_PATTERN,
)


def check_slug_name_folder_consistency(skill_md_path: Path, fm: dict) -> dict:
    """检查: slug==name==folder一致性 (SkillHub审核必拒点)"""
    fields = fm['fields']
    folder_name = skill_md_path.parent.name
    slug = fields.get('slug', '')
    name = fields.get('name', '')

    issues = []
    if slug != name:
        issues.append(f"slug='{slug}' ≠ name='{name}'")
    if slug != folder_name:
        issues.append(f"slug='{slug}' ≠ folder='{folder_name}'")
    if name != folder_name:
        issues.append(f"name='{name}' ≠ folder='{folder_name}'")

    return {
        'name': 'slug==name==folder一致性',
        'passed': len(issues) == 0,
        'severity': 'high',
        'details': issues if issues else [f"slug=name=folder='{slug}'"],
        'issue_count': len(issues)
    }


def check_line_count(skill_md_path: Path) -> dict:
    """检查: SKILL.md行数 <= 500"""
    content = skill_md_path.read_text(encoding='utf-8')
    line_count = len(content.split('\n'))

    return {
        'name': '行数≤500',
        'passed': line_count <= MAX_SKILL_MD_LINES,
        'severity': 'high',
        'details': [f"当前{line_count}行 (上限{MAX_SKILL_MD_LINES})"],
        'issue_count': 0 if line_count <= MAX_SKILL_MD_LINES else 1
    }


def check_required_frontmatter(fm: dict) -> dict:
    """检查: frontmatter 8必需字段齐全"""
    fields = fm['fields']
    missing = [f for f in REQUIRED_FRONTMATTER_FIELDS if f not in fields or not fields[f]]

    return {
        'name': 'frontmatter 8必需字段',
        'passed': len(missing) == 0,
        'severity': 'high',
        'details': [f"缺失: {missing}"] if missing else [f"8字段齐全: {REQUIRED_FRONTMATTER_FIELDS}"],
        'issue_count': len(missing)
    }


def check_display_name_length(fm: dict) -> dict:
    """检查: displayName <= 20字符"""
    fields = fm['fields']
    dn = fields.get('displayName', '')
    if not dn:
        return {
            'name': 'displayName≤20字符',
            'passed': False, 'severity': 'high',
            'details': ['displayName缺失'], 'issue_count': 1
        }

    return {
        'name': 'displayName≤20字符',
        'passed': len(dn) <= MAX_DISPLAY_NAME_LEN,
        'severity': 'medium',
        'details': [f"当前{len(dn)}字符: '{dn}' (上限{MAX_DISPLAY_NAME_LEN})"],
        'issue_count': 0 if len(dn) <= MAX_DISPLAY_NAME_LEN else 1
    }


def check_summary_length(fm: dict) -> dict:
    """检查: summary <= 100字符"""
    fields = fm['fields']
    sm = fields.get('summary', '')
    if not sm:
        return {
            'name': 'summary≤100字符',
            'passed': False, 'severity': 'high',
            'details': ['summary缺失'], 'issue_count': 1
        }

    return {
        'name': 'summary≤100字符',
        'passed': len(sm) <= MAX_SUMMARY_LEN,
        'severity': 'medium',
        'details': [f"当前{len(sm)}字符 (上限{MAX_SUMMARY_LEN})"],
        'issue_count': 0 if len(sm) <= MAX_SUMMARY_LEN else 1
    }


def check_tools_format(fm: dict) -> dict:
    """检查: tools为YAML数组格式"""
    fields = fm['fields']
    tools = fields.get('tools')

    if tools is None:
        return {
            'name': 'tools为YAML数组',
            'passed': False, 'severity': 'high',
            'details': ['tools字段缺失'], 'issue_count': 1
        }

    if isinstance(tools, list):
        return {
            'name': 'tools为YAML数组',
            'passed': True, 'severity': 'low',
            'details': [f"数组格式: {tools}"], 'issue_count': 0
        }

    # 字符串形式(如 "read, exec" 或 "read") - 不合规
    return {
        'name': 'tools为YAML数组',
        'passed': False, 'severity': 'medium',
        'details': [f"当前为字符串: '{tools}', 应为YAML数组格式(- read)"],
        'issue_count': 1
    }


def check_no_xml_brackets(fm: dict) -> dict:
    """检查: frontmatter无XML尖括号"""
    raw = fm['raw']
    if '<' in raw or '>' in raw:
        # 找到包含尖括号的行
        bad_lines = [l for l in raw.split('\n') if '<' in l or '>' in l]
        return {
            'name': 'frontmatter无XML尖括号',
            'passed': False, 'severity': 'medium',
            'details': [f"含尖括号的行: {bad_lines}"], 'issue_count': len(bad_lines)
        }

    return {
        'name': 'frontmatter无XML尖括号',
        'passed': True, 'severity': 'low',
        'details': ['无尖括号'], 'issue_count': 0
    }


def check_no_placeholders(content: str) -> dict:
    """检查: 无占位符"""
    issues = []
    for pattern, desc in PLACEHOLDER_PATTERNS:
        # 跳过链接检查(链接在正文中合法)
        if '未替换链接' in desc:
            continue
        for m in re.finditer(pattern, content):
            issues.append(f"{desc}: '{m.group(0)}'")

    return {
        'name': '无占位符',
        'passed': len(issues) == 0,
        'severity': 'medium',
        'details': issues if issues else ['无占位符'],
        'issue_count': len(issues)
    }


def check_no_exaggeration(content: str) -> dict:
    """检查: 无夸大词"""
    issues = []
    for word in EXAGGERATION_WORDS:
        if word in content:
            issues.append(f"夸大词: '{word}'")

    return {
        'name': '无夸大词',
        'passed': len(issues) == 0,
        'severity': 'medium',
        'details': issues if issues else ['无夸大词'],
        'issue_count': len(issues)
    }


def check_slug_kebab_case(fm: dict) -> dict:
    """检查: slug必须为kebab-case格式"""
    fields = fm['fields']
    slug = fields.get('slug', '')
    if not slug:
        return {
            'name': 'slug为kebab-case',
            'passed': False, 'severity': 'high',
            'details': ['slug缺失'], 'issue_count': 1
        }

    passed = bool(re.match(SLUG_KEBAB_PATTERN, slug))
    return {
        'name': 'slug为kebab-case',
        'passed': passed,
        'severity': 'high',
        'details': [f"slug='{slug}'"] if passed else [f"slug='{slug}'不符合kebab-case"],
        'issue_count': 0 if passed else 1
    }


def check_version_format(fm: dict) -> dict:
    """检查: version必须为x.y.z格式"""
    fields = fm['fields']
    version = fields.get('version', '')
    if not version:
        return {
            'name': 'version格式',
            'passed': False, 'severity': 'high',
            'details': ['version缺失'], 'issue_count': 1
        }

    passed = bool(re.match(VERSION_PATTERN, version))
    return {
        'name': 'version格式',
        'passed': passed,
        'severity': 'high',
        'details': [f"version='{version}'"] if passed else [f"version='{version}'不符合x.y.z格式"],
        'issue_count': 0 if passed else 1
    }


def check_description_length(fm: dict) -> dict:
    """检查: description长度在MIN_DESCRIPTION_LEN~MAX_DESCRIPTION_LEN之间"""
    fields = fm['fields']
    desc = fields.get('description', '')
    if not desc:
        return {
            'name': 'description长度',
            'passed': False, 'severity': 'high',
            'details': ['description缺失'], 'issue_count': 1
        }

    desc_len = len(desc)
    passed = MIN_DESCRIPTION_LEN <= desc_len <= MAX_DESCRIPTION_LEN
    return {
        'name': 'description长度',
        'passed': passed,
        'severity': 'medium',
        'details': [f"当前{desc_len}字符 (建议{MIN_DESCRIPTION_LEN}-{MAX_DESCRIPTION_LEN})"],
        'issue_count': 0 if passed else 1
    }
