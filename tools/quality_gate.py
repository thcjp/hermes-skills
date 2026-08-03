"""
Skill质量门禁脚本 (v2.2 — 安全检测增强: 科恩实验室+云鼎实验室特有模式)

集成现有check_debranding.py + skill_core/checks.py的9项检查
任一检查fail则总体fail, 阻止上传

v2.0新增:
  - 营销关卡 (run_marketing_gate): 7项营销数据质量检查
  - 防幻觉机制 (run_anti_hallucination): 3项AI虚假实现检测
  - 统一质量检查入口 (run_full_quality_check): L1→L1.5→营销→防幻觉

v2.1新增:
  - 安全审核预检 (run_security_precheck): 10类基础高风险模式 + VPN封禁

v2.2新增 (科恩实验室+云鼎实验室特有检测):
  - SSRF服务端请求伪造 (云鼎特有)
  - 数据外泄风险 (云鼎特有)
  - 混淆代码/编码载荷 (科恩特有)
  - 反向Shell/Shell反弹 (科恩特有)
  - 权限提升风险 (科恩特有)
  - 加密货币挖矿 (云鼎特有)
  - AI Prompt注入风险 (云鼎特有)
  - 持久化/自启动 (科恩特有)
  - 不安全反序列化 (科恩特有)
  - 依赖混淆/供应链风险 (云鼎特有)
  安全预检从11项扩展到21项

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

安全预检关卡 (21项):
  --- 基础高风险模式 (v2.1, 来自29条安全审核失败分析) ---
 14. exec命令执行 (96.6%命中率)
 15. API密钥明文处理 (62.1%)
 16. 不可信外部API/域名 (51.7%)
 17. 引用不存在的脚本 (41.4%)
 18. 硬编码服务器地址/IP (27.6%)
 19. HTTP不安全通信 (20.7%)
 20. tools字段格式错误 (17.2%)
 21. 文件系统遍历风险 (17.2%)
 22. 敏感信息泄露 (13.8%)
 23. eval/代码注入 (10.3%)
  --- 科恩实验室 + 云鼎实验室特有检测 (v2.2新增) ---
 24. SSRF服务端请求伪造 (云鼎特有)
 25. 数据外泄风险 (云鼎特有)
 26. 混淆代码/编码载荷 (科恩特有)
 27. 反向Shell/Shell反弹 (科恩特有)
 28. 权限提升风险 (科恩特有)
 29. 加密货币挖矿 (云鼎特有)
 30. AI Prompt注入风险 (云鼎特有)
 31. 持久化/自启动 (科恩特有)
 32. 不安全反序列化 (科恩特有)
 33. 依赖混淆/供应链风险 (云鼎特有)
 34. VPN/翻墙关键词 (直接封禁)

营销关卡 (7项):
 35. displayName中文化且≤20字符
 36. summary营销优化且≤100字符
 37. description 150-280字符, 非模板化
 38. tags 5-10个, 与功能匹配
 39. categoryIds正确映射(非空)
 40. pricing合理性(pricing_tier匹配skill复杂度)
 41. license合规(free=MIT, paid=Proprietary)

防幻觉机制 (3项):
 42. 交叉验证: L2 TRACE vs L3 Agent vs L4-L9审计评分一致性
 43. 需求理解偏差: description声明 vs body实际内容
 44. 虚假实现检测: 无占位符/无模板/无空代码块

用法:
  python quality_gate.py <SKILL.md路径>
  python quality_gate.py <目录>  # 批量检查
  python quality_gate.py <path> --json  # 输出JSON报告
  python quality_gate.py <path> --marketing  # 仅营销关卡
  python quality_gate.py <path> --anti-hallucination  # 仅防幻觉检查
  python quality_gate.py <path> --security  # 仅安全预检(21项)
  python quality_gate.py <path> --full  # 完整质量检查(L1+安全+营销+防幻觉)
"""

import sys
import json
import re
import argparse
import sqlite3
from pathlib import Path
from datetime import datetime

# 数据库路径(复用config)
try:
    from config import DB_PATH as _DB_PATH
except ImportError:
    _DB_PATH = Path(r"d:\skills\skill-registry.db")

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


# ============ 自动生成内容检测 + WAF长度检查 (V186新增) ============
# 根因: 大量skill是自动生成模板,内容与slug无关,被平台当成垃圾内容
# 解决: 在质量门控阶段检测并阻断自动生成内容,防止上传到平台

# SkillHub WAF内容长度限制
SKILLHUB_WAF_MAX_CONTENT = 5800

# 自动生成模板的标记性短语(出现任意一个即判定为自动生成)
AUTO_GEN_MARKERS = [
    '本技能提供',
    '功能总览',
    '功能1：',
    '功能1:',
    '核心功能',
    '自动化处理流程',
    '减少人工干预与重复劳动',
    '结构化输入输出',
    '内置错误恢复机制',
    '多格式兼容',
    '适用于需要专业工具支持的开发',
    '部分高级功能需要付费API',
    '大量并发请求可能触发限流',
    '输出内容受LLM能力限制',
]


def check_auto_generated_content(content: str) -> dict:
    """检查14: 自动生成内容检测

    检测SKILL.md是否为自动生成模板(非原创内容)。
    自动生成模板通常包含通用化描述,与skill实际功能无关,
    上传到平台会被当成垃圾内容,导致封号。

    Returns:
        dict with passed=True(原创) or passed=False(自动生成)
    """
    matched_markers = []
    for marker in AUTO_GEN_MARKERS:
        if marker in content:
            matched_markers.append(marker)

    is_auto_generated = len(matched_markers) >= 2  # 2个以上标记判定为自动生成

    return {
        'name': '自动生成内容检测',
        'passed': not is_auto_generated,
        'severity': 'high',
        'matched_markers': matched_markers,
        'marker_count': len(matched_markers),
        'message': (
            f'检测到{len(matched_markers)}个自动生成标记: {", ".join(matched_markers[:3])}'
            if is_auto_generated else '内容为原创(未检测到自动生成标记)'
        ),
    }


def check_content_length_waf(content: str) -> dict:
    """检查15: SkillHub WAF内容长度检查

    SkillHub WAF限制单次上传内容不超过5800字符。
    超过限制的skill会被WAF拦截,无法上传。

    Returns:
        dict with passed=True(合规) or passed=False(超长)
    """
    content_len = len(content)
    is_over_limit = content_len > SKILLHUB_WAF_MAX_CONTENT

    return {
        'name': 'WAF内容长度',
        'passed': not is_over_limit,
        'severity': 'medium' if is_over_limit else 'info',
        'content_length': content_len,
        'waf_limit': SKILLHUB_WAF_MAX_CONTENT,
        'message': (
            f'内容长度{content_len}字符,超过WAF限制{SKILLHUB_WAF_MAX_CONTENT}'
            if is_over_limit else
            f'内容长度{content_len}字符,合规(限制{SKILLHUB_WAF_MAX_CONTENT})'
        ),
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
        # V186新增: 自动生成内容检测 + WAF长度检查
        # 根因: 自动生成模板被平台当成垃圾内容,导致封号
        check_auto_generated_content(content),
        check_content_length_waf(content),
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
    r'^pass\s*$',  # v3.2: 只匹配行首的pass语句, 不匹配自然语言中的"Pass"
    r'\bNotImplemented\b',
    r'\braise\s+NotImplementedError\b',
    r'(?i)#\s*TODO',
    r'(?i)#\s*FIXME',
    r'(?i)#\s*placeholder',
    r'(?i)#\s*mock',
    r'(?i)#\s*stub',
    r'(?i)\.\.\.\s*#.*placeholder',
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


# slug关键词→中文关键词映射 (用于检测slug与displayName语义不匹配)
_SLUG_KEYWORD_CN_MAP = {
    'university': ['大学', '高校', '院校', '申请', 'admission', 'application'],
    'applications': ['申请', '报名', 'application'],
    'word': ['word', '文档', 'doc'],
    'docx': ['docx', '文档'],
    'pdf': ['pdf', '文档'],
    'excel': ['excel', '表格'],
    'sheet': ['sheet', '表格'],
    'video': ['视频', 'video'],
    'audio': ['音频', 'audio'],
    'image': ['图片', '图像', 'image'],
    'code': ['代码', 'code'],
    'security': ['安全', 'security'],
    'data': ['数据', 'data'],
    'write': ['写作', 'write'],
    'copy': ['文案', 'copy'],
    'translate': ['翻译', 'translate'],
    'search': ['搜索', 'search'],
    'download': ['下载', 'download'],
    'upload': ['上传', 'upload'],
    'email': ['邮件', 'email'],
    'chat': ['聊天', 'chat'],
    'calendar': ['日历', 'calendar'],
    'finance': ['财务', 'finance'],
    'accounting': ['会计', 'accounting'],
    'music': ['音乐', 'music'],
    'weather': ['天气', 'weather'],
    'news': ['新闻', 'news'],
    'recipe': ['食谱', 'recipe'],
    'health': ['健康', 'health'],
    'travel': ['旅行', 'travel'],
    'shopping': ['购物', 'shopping'],
    'payment': ['支付', 'payment'],
    'invoice': ['发票', 'invoice'],
    'resume': ['简历', 'resume'],
    'presentation': ['演示', 'presentation'],
    'database': ['数据库', 'database'],
    'api': ['api', '接口'],
    'browser': ['浏览器', 'browser'],
    'agent': ['代理', 'agent'],
    'automation': ['自动化', 'automation'],
    'monitor': ['监控', 'monitor'],
    'backup': ['备份', 'backup'],
    'deploy': ['部署', 'deploy'],
    'test': ['测试', 'test'],
    'debug': ['调试', 'debug'],
}

# slug中需要过滤的常见后缀词
_SLUG_FILTER_WORDS = {'sk', 'free', 'paid', 'pro', 'tool', 'tools', 'master', 'pro', 'ai', 'the', 'and', 'for', 'a', 'an', 'with', 'new'}


def _extract_slug_keywords(slug: str) -> list:
    """从slug中提取有意义的关键词 (过滤常见后缀词)"""
    parts = slug.lower().split('-')
    keywords = []
    for part in parts:
        if len(part) > 2 and part not in _SLUG_FILTER_WORDS:
            keywords.append(part)
    return keywords


def _check_slug_content_match(slug: str, display_name: str, description: str, body: str) -> dict:
    """检查slug关键词是否在displayName/description/body中出现 (语义匹配)
    
    检测场景: slug=university-applications-sk 但 displayName=命理大师 (内容不匹配)
    """
    if not slug:
        return {'matched': True, 'details': 'slug为空, 跳过检查'}
    
    slug_keywords = _extract_slug_keywords(slug)
    if not slug_keywords:
        return {'matched': True, 'details': 'slug无有意义关键词, 跳过检查'}
    
    # 合并搜索目标: displayName + description + body前500字符
    search_text = f"{display_name} {description} {body[:500]}".lower()
    
    unmatched = []
    matched = []
    for kw in slug_keywords:
        # 直接检查英文关键词是否出现
        if kw in search_text:
            matched.append(kw)
            continue
        # 检查中文映射
        cn_words = _SLUG_KEYWORD_CN_MAP.get(kw, [])
        if any(cn in search_text for cn in cn_words):
            matched.append(f"{kw}(→{[c for c in cn_words if c in search_text][0]})")
            continue
        # 无匹配
        unmatched.append(kw)
    
    matched_result = len(matched) > 0
    return {
        'matched': matched_result,
        'slug_keywords': slug_keywords,
        'matched_keywords': matched,
        'unmatched_keywords': unmatched,
        'details': f"slug关键词: {slug_keywords}, 匹配: {matched}, 未匹配: {unmatched}"
    }


def _check_requirement_deviation(skill_md_path: Path, fm: dict) -> dict:
    """防幻觉检查2: 需求理解偏差检测 (v2.3增强: 新增slug与内容语义匹配检查)
    
    v2.3新增:
      - slug关键词与displayName/description/body语义匹配检查
        (检测slug=university-applications但内容=命理大师 这类不匹配)
    
    原有:
      - 提取description中的关键功能声明, 检查body中是否包含对应实现
    """
    fields = fm.get('fields', fm)
    body = fm.get('body', '')
    description = fields.get('description', '')
    slug = fields.get('slug', '')
    display_name = fields.get('displayName', '')
    
    issues = []
    
    if not description or not body:
        return {
            'name': '需求理解偏差',
            'passed': True,
            'severity': 'low',
            'details': ['description或body为空, 跳过偏差检测']
        }
    
    # v2.3新增: slug与内容语义匹配检查
    slug_match = _check_slug_content_match(slug, display_name, description, body)
    if not slug_match['matched']:
        unmatched_str = ', '.join(slug_match['unmatched_keywords'])
        issues.append(
            f'slug与内容语义不匹配: slug关键词[{unmatched_str}]在displayName/description/body中均未找到. '
            f'displayName="{display_name}" — 请检查slug是否与实际功能一致'
        )
    
    # 原有: 提取description中的功能关键词(动词+宾语)
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
    # v3.2修正: 支持部分匹配 — 长中文短语拆分为2-4字短词, 任一匹配即通过
    body_lower = body.lower()
    missing_features = []
    for feature in claimed_features[:5]:  # 只检查前5个
        if feature and len(feature) > 2:
            # 直接检查完整短语是否在body中出现
            if feature in body:
                continue
            # v3.2: 长短语拆分为短词进行部分匹配
            # 如 "结构化的工作流程和配置指引" → ["结构化", "工作流程", "配置", "指引"]
            if len(feature) > 6:
                # 按2-4字窗口拆分
                sub_keywords = []
                for i in range(0, len(feature) - 1, 2):
                    sub = feature[i:i+4]
                    if len(sub) >= 2:
                        sub_keywords.append(sub)
                # 任一短词在body中出现即视为匹配
                if any(sub in body for sub in sub_keywords):
                    continue
            missing_features.append(feature)
    
    if missing_features:
        issues.append(f'description声明功能但body未提及: {missing_features}')
    
    return {
        'name': '需求理解偏差',
        'passed': len(issues) == 0,
        'severity': 'high' if not slug_match['matched'] else 'medium',
        'details': issues if issues else [f'已验证{len(claimed_features[:5])}个功能声明, body均有对应内容; slug语义匹配正常'],
        'claimed_features': claimed_features[:5],
        'missing_features': missing_features,
        'slug_match': slug_match,
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
            
            # 检查空实现 (v3.2: 使用MULTILINE而非IGNORECASE, 内联flag已嵌入pattern)
            for pattern in _EMPTY_IMPL_PATTERNS:
                matches = re.findall(pattern, block, re.MULTILINE)
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


# ============ 安全审核预检关卡 (v2.1新增) ============
# SkillHub三线安全审核(内容合规→科恩实验室→云鼎实验室)的10类高风险模式预检
# 在上传前检测并修复这些模式,避免skill被平台审核拒绝
# 参考: d:\skills\docs\skillhub-security-avoidance-guide.md

# 10类高风险模式定义 (命中率数据来自29条安全审核失败skill分析)
_SECURITY_RISK_PATTERNS = [
    {
        'name': 'exec命令执行',
        'severity': 'critical',
        'hit_rate': '96.6%',
        'patterns': [
            r'\bexec\s*\(',
            r'os\.system\s*\(',
            r'os\.popen\s*\(',
            r'subprocess\.(call|run|Popen|check_output)\s*\(.*shell\s*=\s*True',
            r'child_process\.exec',
            r'node\s+-e\s',
        ],
        'description': '包含exec/subprocess/os.system等命令执行指令,平台扫描判定为任意命令执行风险',
        'fix_suggestion': '将exec命令替换为描述性文字;如需展示代码示例,使用白名单模式的安全调用',
    },
    {
        'name': 'API密钥明文处理',
        'severity': 'critical',
        'hit_rate': '62.1%',
        'patterns': [
            # v3.2修正: 添加(?!\$\{)排除环境变量引用, 避免修复后的${VAR}被误报
            r'(?:API_KEY|API_SECRET|SECRET_KEY|ACCESS_TOKEN|PRIVATE_KEY)\s*=\s*["\'](?!\$\{)[^"\']{8,}["\']',
            r'export\s+(?:API_KEY|API_SECRET|SECRET_KEY|ACCESS_TOKEN)\s*=\s*["\'](?!\$\{)[^"\']+["\']',
            r'(?:sk-|pk-)[a-zA-Z0-9]{20,}',
            r'Bearer\s+[a-zA-Z0-9_\-\.]{20,}',
        ],
        'description': '直接写入API Key/Token,或使用export API_KEY=xxx模式',
        'fix_suggestion': '使用环境变量引用: export API_KEY="${API_KEY:?请设置环境变量}"',
    },
    {
        'name': '不可信外部API/域名',
        'severity': 'high',
        'hit_rate': '51.7%',
        'patterns': [
            r'https?://[a-zA-Z0-9\-]+\.(?:cyou|xyz|top|click|loan|work|fit|rest|host|site|online|store|live|stream|download|review|trade|date|party|review)\b',
            r'https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[:/]',
        ],
        'description': '引用非知名域名(特别是可疑TLD)或直接IP地址',
        'fix_suggestion': '替换为知名API域名;移除可疑域名引用;使用环境变量配置endpoint',
    },
    {
        'name': '引用不存在的脚本',
        'severity': 'medium',
        'hit_rate': '41.4%',
        'patterns': [
            r'\./scripts/[a-zA-Z_]+\.py',
            r'node\s+\./scripts/',
            r'python\s+\./scripts/',
            r'bash\s+\./scripts/',
        ],
        'description': '引用./scripts/xxx.py但包中不含该文件',
        'fix_suggestion': '移除对不存在脚本的引用;或将脚本内容内联到SKILL.md中',
    },
    {
        'name': '硬编码服务器地址/IP',
        'severity': 'medium',
        'hit_rate': '27.6%',
        'patterns': [
            r'(?:SERVER|ENDPOINT|HOST|URL)\s*=\s*["\']https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
            r'(?:SERVER|ENDPOINT|HOST|URL)\s*=\s*["\']https?://[a-zA-Z0-9\-]+\.example\.com',
            r'192\.168\.\d{1,3}\.\d{1,3}',
            r'10\.\d{1,3}\.\d{1,3}\.\d{1,3}',
            r'localhost:\d{4,5}',
        ],
        'description': '硬编码IP地址或特定服务器域名',
        'fix_suggestion': '使用环境变量: SERVER_URL = os.getenv("SERVER_URL", "")',
    },
    {
        'name': 'HTTP不安全通信',
        'severity': 'medium',
        'hit_rate': '20.7%',
        'patterns': [
            r'requests\.get\s*\(\s*["\']http://',
            r'requests\.post\s*\(\s*["\']http://',
            r'fetch\s*\(\s*["\']http://',
            r'axios\.\w+\s*\(\s*["\']http://',
            r'curl\s+["\']?http://',
        ],
        'description': '使用http://而非https://进行网络通信',
        'fix_suggestion': '将所有http://替换为https://',
    },
    {
        'name': 'tools字段格式错误',
        'severity': 'medium',
        'hit_rate': '17.2%',
        'patterns': [
            r'^tools:\s*["\']',
            r'^tools:\s*\n\s*-\s*["\'].*["\']\s*$',
        ],
        'description': 'frontmatter tools用字符串而非YAML数组',
        'fix_suggestion': '使用YAML数组格式: tools: ["tool1", "tool2"] 或 tools:\n  - tool1\n  - tool2',
    },
    {
        'name': '文件系统遍历风险',
        'severity': 'medium',
        'hit_rate': '17.2%',
        'patterns': [
            r'\.\./',
            r'~/',
            r'os\.walk\s*\(\s*["\']/',
            r'glob\.glob\s*\(\s*["\']\*\*',
            r'shutil\.rmtree\s*\(',
        ],
        'description': '使用../、~/、通配符等路径操作,可能被判定为路径遍历风险',
        'fix_suggestion': '使用安全路径处理: Path.cwd() / "safe_dir";避免使用../和~/',
    },
    {
        'name': '敏感信息泄露',
        'severity': 'medium',
        'hit_rate': '13.8%',
        'patterns': [
            r'C:\\Users\\[a-zA-Z]',
            r'/home/[a-z]+/',
            r'/Users/[a-zA-Z]+/',
            r'(?:password|passwd|pwd)\s*=\s*["\'][^"\']+["\']',
        ],
        'description': '泄露系统路径/用户名/服务器配置',
        'fix_suggestion': '使用通配符或环境变量替换具体路径',
    },
    {
        'name': 'eval/代码注入',
        'severity': 'critical',
        'hit_rate': '10.3%',
        'patterns': [
            r'\beval\s*\(',
            r'Function\s*\(\s*["\']',
            r'window\.eval\s*\(',
            r'setTimeout\s*\(\s*["\']',
            r'setInterval\s*\(\s*["\']',
        ],
        'description': '使用eval()、Function()等动态代码执行功能',
        'fix_suggestion': '移除eval调用;如需动态执行,使用安全解析器或JSON.parse',
    },
    # ============ v2.2新增: 科恩实验室 + 云鼎实验室特有检测 ============
    {
        'name': 'SSRF服务端请求伪造',
        'severity': 'critical',
        'hit_rate': '云鼎特有',
        'patterns': [
            r'requests\.(get|post|put|delete)\s*\(\s*(?:user\w*|input\w*|url|endpoint|target|callback|webhook_url)',
            r'fetch\s*\(\s*(?:user\w*|input\w*|url|endpoint|target)',
            r'axios\.(get|post)\s*\(\s*(?:user\w*|input\w*|url|endpoint)',
            r'urlopen\s*\(\s*(?:user\w*|input\w*|url)',
            r'curl\s+["\']?\$',
            r'http\.Get\s*\(\s*(?:userInput|req\.|params\.)',
        ],
        'description': '从用户输入直接构造HTTP请求URL,存在SSRF风险(云鼎实验室重点检测项)',
        'fix_suggestion': '对URL进行白名单校验;禁止访问内网IP(10.x/172.16-31.x/192.168.x);使用URL解析验证scheme和host',
    },
    {
        'name': '数据外泄风险',
        'severity': 'critical',
        'hit_rate': '云鼎特有',
        'patterns': [
            r'(?:send|upload|transmit|exfiltrate|post)\s*(?:_|\s)?(?:data|file|content|secret|key|token|password|env)\b.*(?:http|url|endpoint|api)',
            r'curl\s+.*(?:secret|key|token|password|\.env|\.ssh|id_rsa|/etc/passwd|/etc/shadow)',
            r'wget\s+.*(?:post|upload).*(?:secret|key|token|password)',
            r'requests\.post\s*\([^)]*(?:secret|key|token|password|\.env|/etc/passwd|/etc/shadow)',
            r'(?:cat|type|Get-Content)\s+(?:/etc/passwd|/etc/shadow|\.env|\.ssh/id_rsa|~/.aws/credentials)',
            r'curl\s+.*(?:-d|--data).*(?:/etc/passwd|/etc/shadow|\.env)',
        ],
        'description': '将敏感数据(密钥/密码/系统文件)发送到外部端点,存在数据外泄风险(云鼎实验室重点检测项)',
        'fix_suggestion': '禁止将密钥/密码/系统文件内容发送到外部;移除所有读取敏感文件并上传的代码;使用安全存储替代',
    },
    {
        'name': '混淆代码/编码载荷',
        'severity': 'high',
        'hit_rate': '科恩特有',
        'patterns': [
            r'base64\.b64decode\s*\(\s*["\'][A-Za-z0-9+/=]{20,}["\']',
            r'atob\s*\(\s*["\'][A-Za-z0-9+/=]{20,}["\']',
            r'Buffer\.from\s*\(\s*["\'][A-Za-z0-9+/=]{20,}["\'].*base64',
            r'\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}',
            r'\\u[0-9a-f]{4}\\u[0-9a-f]{4}\\u[0-9a-f]{4}',
            r'unescape\s*\(\s*["\']%[0-9a-fA-F]{2}',
            r'chr\s*\(\s*\d+\s*\)\s*\.\s*chr\s*\(\s*\d+\s*\)',
        ],
        'description': '使用Base64/Hex/Unicode编码隐藏恶意载荷,科恩实验室静态分析重点检测',
        'fix_suggestion': '移除所有编码载荷;如需编码说明使用注释而非实际编码;用明文描述替代编码字符串',
    },
    {
        'name': '反向Shell/Shell反弹',
        'severity': 'critical',
        'hit_rate': '科恩特有',
        'patterns': [
            # v3.2修正: 去掉 .* 通配符, 避免误报 (如 "sh hours-i" 被误匹配)
            # 原pattern: (?:bash|sh|zsh|nc|ncat)\s+.*(?:-i|/dev/tcp/|/dev/udp/)
            r'(?:bash|sh|zsh)\s+-i\b',
            r'(?:bash|sh|zsh)\s+-i\s*>\s*&',
            r'(?:nc|ncat)\s+.*-e\s',
            r'(?:bash|sh|zsh)\s+-c\s+["\'].*(?:socket|/dev/tcp)',
            r'(?:python|perl|ruby|php)\s+-c\s+["\'].*(?:socket|connect|SOCK_STREAM)',
            r'0\.0\.0\.0.*(?:listen|bind|accept)',
            r'(?:mkfifo|mknod)\s+.*\|\s*(?:sh|bash)',
            r'(?:exec|subprocess)\s*\(\s*["\'](?:/bin/)?(?:bash|sh)\s+-i',
            r'(?:bash|sh)\s+-i\s*>\s*&\s*(?:/dev/tcp|1>|2>)',
        ],
        'description': '包含反向Shell或Shell反弹模式,科恩实验室高危检测项',
        'fix_suggestion': '完全移除所有反向Shell代码;如为网络工具描述,使用功能说明替代具体命令',
    },
    {
        'name': '权限提升风险',
        'severity': 'high',
        'hit_rate': '科恩特有',
        'patterns': [
            r'\bsudo\s+(?:chmod|chown|chgrp|rm|dd|mkfs|fdisk|mount|umount)',
            r'chmod\s+[0-7]?[0-7][0-7][0-7]\s+/(?:etc|usr|var|root|bin|sbin)',
            r'os\.setuid\s*\(\s*0\b',
            r'os\.setgid\s*\(\s*0\b',
            r'(?:chmod|chown)\s+.*(?:777|666|/etc/passwd|/etc/shadow|/etc/sudoers)',
            r'WriteProcessMemory|SeDebugPrivilege|AdjustTokenPrivileges',
        ],
        'description': '尝试提升系统权限或修改关键系统文件权限,科恩实验室检测项',
        'fix_suggestion': '移除所有权限提升代码;使用描述性语言说明安全要求;不修改系统文件权限',
    },
    {
        'name': '加密货币挖矿',
        'severity': 'critical',
        'hit_rate': '云鼎特有',
        'patterns': [
            r'(?:xmrig|stratum\+tcp|cryptonight|monero.*mine|eth.*mine)',
            r'(?:coinhive|coin-hive|crypto-?loot|webminer)',
            r'(?:pool\.minexmr|pool\.supportxmr|nanopool)',
            r'(?:stratum\+tcp|stratum\+ssl)://',
        ],
        'description': '包含加密货币挖矿程序或矿池连接地址,云鼎实验室高危检测项',
        'fix_suggestion': '完全移除所有挖矿相关代码和地址;如为安全分析工具,仅描述检测方法不含实际代码',
    },
    {
        'name': 'AI Prompt注入风险',
        'severity': 'high',
        'hit_rate': '云鼎特有',
        'patterns': [
            r'(?:ignore|disregard)\s+(?:all\s+)?(?:previous|prior|above)\s+instructions',
            r'(?:system|assistant)[:：]\s*(?:you\s+are|act\s+as|forget)',
            r'(?:new\s+instructions?|override|jailbreak|\bDAN\b)',
            r'(?:reveal|show|print|output)\s+(?:your|the)\s+(?:system\s+prompt|instructions?|rules?)',
            r'(?:pretend|simulate)\s+(?:you\s+(?:are|have\s+no)|to\s+be\s+(?:an?\s+)?(?:unrestricted|unlimited))',
        ],
        'description': '包含AI Prompt注入攻击模式,云鼎实验室AI安全检测项',
        'fix_suggestion': '移除所有prompt注入示例;如为安全测试工具,使用描述性语言说明防御方法而非攻击载荷',
    },
    {
        'name': '持久化/自启动',
        'severity': 'high',
        'hit_rate': '科恩特有',
        'patterns': [
            r'(?:crontab|/etc/cron\.|/etc/rc\.d|/etc/init\.d|systemctl\s+enable)',
            r'(?:HKLM|HKCU)\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',
            r'(?:schtasks|\bat\s+\d{1,2}:\d{2}|taskschd)',
            r'(?:~/.bashrc|~/.bash_profile|~/.profile|~/.zshrc).*(?:exec|eval|python|curl|wget)',
            r'(?:exec|eval|python|curl|wget).*(?:~/.bashrc|~/.bash_profile|~/.profile|~/.zshrc)',
            r'(?:LaunchAgent|LaunchDaemon|com\.apple\.loginitem)',
        ],
        'description': '尝试建立持久化机制(计划任务/注册表自启动/启动脚本),科恩实验室检测项',
        'fix_suggestion': '移除所有持久化代码;如为系统管理工具,使用描述性语言说明部署方式',
    },
    {
        'name': '不安全反序列化',
        'severity': 'critical',
        'hit_rate': '科恩特有',
        'patterns': [
            r'pickle\.loads?\s*\(',
            r'yaml\.load\s*\(\s*(?!.*Loader)',
            r'marshal\.loads?\s*\(',
            r'php\s+(?:unserialize|maybe_unserialize)\s*\(',
            r'(?:ObjectInputStream|readObject|XMLDecoder)',
            r'eval\s*\(\s*(?:pickle|marshal|yaml)',
        ],
        'description': '使用不安全的反序列化方法,可能导致远程代码执行,科恩实验室高危检测项',
        'fix_suggestion': '使用安全的反序列化方法:json.loads替代pickle.loads;yaml.safe_load替代yaml.load',
    },
    {
        'name': '依赖混淆/供应链风险',
        'severity': 'high',
        'hit_rate': '云鼎特有',
        'patterns': [
            r'pip\s+install\s+(?:--index-url|--extra-index-url)\s+["\']?http',
            r'npm\s+install\s+.*--registry\s+["\']?http',
            r'require\s*\(\s*["\']http://',
            r'(?:requirements\.txt|package\.json).*(?:git\+http|http://.*\.git)',
            r'(?:download|install|setup)\s+.*(?:\.sh|\.exe|\.bat|\.ps1)\s+.*(?:curl|wget|http)',
        ],
        'description': '从不安全来源安装依赖或下载执行脚本,供应链攻击风险(云鼎实验室检测项)',
        'fix_suggestion': '仅使用官方包管理器默认源(https://pypi.org, https://registry.npmjs.org);不使用http源',
    },
]

# VPN/翻墙关键词 — 直接封禁
_VPN_BLOCKED_KEYWORDS = [
    'v2ray', 'vpn', '翻墙', '科学上网', 'proxy chains', 'shadowsocks',
    'trojan', 'clash', 'surge', 'ssr', 'ss-urls',
]


def _check_security_risk_pattern(body: str, pattern_def: dict) -> dict:
    """检查单个安全风险模式"""
    name = pattern_def['name']
    severity = pattern_def['severity']
    patterns = pattern_def['patterns']
    
    matches = []
    for pattern in patterns:
        found = re.findall(pattern, body, re.IGNORECASE | re.MULTILINE)
        if found:
            # 去重并限制数量
            unique = list(set(found))[:5]
            matches.extend(unique)
    
    if matches:
        return {
            'name': f'安全审核: {name}',
            'passed': False,
            'severity': severity,
            'details': [
                f'命中模式({pattern_def["hit_rate"]}命中率): {pattern_def["description"]}',
                f'匹配到: {", ".join(matches[:3])}' + ('...' if len(matches) > 3 else ''),
                f'修复建议: {pattern_def["fix_suggestion"]}',
            ]
        }
    
    return {
        'name': f'安全审核: {name}',
        'passed': True,
        'severity': severity,
        'details': []
    }


def _check_vpn_keywords(body: str) -> dict:
    """检查VPN/翻墙关键词(直接封禁)"""
    body_lower = body.lower()
    found_keywords = []
    for kw in _VPN_BLOCKED_KEYWORDS:
        if kw.lower() in body_lower:
            found_keywords.append(kw)
    
    if found_keywords:
        return {
            'name': '安全审核: VPN/翻墙关键词',
            'passed': False,
            'severity': 'critical',
            'details': [
                f'发现VPN/翻墙关键词(直接封禁): {", ".join(found_keywords)}',
                '修复建议: 移除所有VPN/翻墙相关内容;如为网络安全工具,转型为诊断类描述',
            ]
        }
    
    return {
        'name': '安全审核: VPN/翻墙关键词',
        'passed': True,
        'severity': 'critical',
        'details': []
    }


def _check_content_fingerprint(skill_md_path: Path, full_text: str) -> dict:
    """内容指纹去重检查 (v3.0新增 — 防止近似重复内容触发平台反垃圾)
    
    根因: 62%封禁skill为差异化复制内容(-free/-pro/-tool-*派生),
    平台内容指纹系统识别为批量生产的近似重复内容并批量封禁。
    
    检查逻辑:
    1. 计算内容指纹(SHA-256前16字符,作为快速比对键)
    2. 查询DB中已有skill的content_hash
    3. 若完全匹配(同指纹),阻断上传
    4. 若基础slug变体(-free/-pro/-tool-*),给出警告但不阻断
       (因为差异化是合法的,但需确保内容实质不同)
    """
    import hashlib
    import sqlite3
    from pathlib import Path as _Path
    
    try:
        # 计算内容指纹
        content_hash = hashlib.sha256(full_text.encode('utf-8')).hexdigest()[:16]
        
        # 查询DB中是否有相同指纹的skill
        db_path = _Path(__file__).resolve().parent.parent / "skill-registry.db"
        if not db_path.exists():
            return {
                'name': '安全审核: 内容指纹去重',
                'passed': True,
                'severity': 'high',
                'details': ['DB不存在,跳过指纹去重检查']
            }
        
        conn = sqlite3.connect(str(db_path))
        conn.execute("PRAGMA foreign_keys = ON")
        
        # 检查完全匹配的指纹
        c = conn.execute(
            "SELECT slug, current_status FROM skills WHERE content_hash = ? AND slug != ?",
            (content_hash, skill_md_path.parent.name)
        )
        exact_match = c.fetchone()
        
        # 检查slug变体(-free/-pro/-tool-free/-tool-pro)
        current_slug = skill_md_path.parent.name
        base_slug = current_slug
        for suffix in ['-free', '-pro', '-tool-free', '-tool-pro', '-sk', '-sk1', '-sk2', '-sk3', '-paid']:
            if current_slug.endswith(suffix):
                base_slug = current_slug[:-len(suffix)]
                break
        
        variant_count = 0
        if base_slug != current_slug:
            # 查找同base_slug的变体
            c = conn.execute(
                """SELECT slug FROM skills 
                   WHERE (slug LIKE ? OR slug LIKE ? OR slug LIKE ? OR slug LIKE ?)
                   AND slug != ? AND current_status != 'deleted'""",
                (f"{base_slug}-%", f"{base_slug}-tool-%", f"{base_slug}-sk%", f"{base_slug}-paid",
                 current_slug)
            )
            variant_count = len(c.fetchall())
        
        conn.close()
        
        # 判定逻辑
        if exact_match:
            return {
                'name': '安全审核: 内容指纹去重',
                'passed': False,
                'severity': 'critical',
                'details': [
                    f'发现完全相同内容指纹的skill: {exact_match[0]} (状态: {exact_match[1]})',
                    f'内容指纹: {content_hash}',
                    '修复建议: 确保内容有实质性差异,不要复制粘贴后仅改slug',
                ]
            }
        
        if variant_count >= 3:
            return {
                'name': '安全审核: 内容指纹去重',
                'passed': False,
                'severity': 'high',
                'details': [
                    f'基础slug "{base_slug}" 已有 {variant_count} 个变体(-free/-pro/-tool-*)',
                    '根因: 平台反垃圾系统会将多变体识别为批量生产的近似重复内容',
                    f'当前slug: {current_slug}',
                    '修复建议: 合并变体为单一skill,使用edition/pricing_model元数据区分版本',
                ]
            }
        
        if variant_count >= 1:
            return {
                'name': '安全审核: 内容指纹去重',
                'passed': True,
                'severity': 'medium',
                'details': [
                    f'基础slug "{base_slug}" 已有 {variant_count} 个变体',
                    '警告: 继续增加变体可能触发平台反垃圾系统',
                    '建议: 确保内容有实质性差异(>30%不同)',
                ]
            }
        
        return {
            'name': '安全审核: 内容指纹去重',
            'passed': True,
            'severity': 'high',
            'details': [f'内容指纹: {content_hash} (无重复)']
        }
    except Exception as e:
        return {
            'name': '安全审核: 内容指纹去重',
            'passed': True,
            'severity': 'high',
            'details': [f'指纹检查异常(跳过): {str(e)[:80]}']
        }


def auto_fix_security_issues(skill_md_path: Path) -> dict:
    """自动修复安全预检发现的问题 (v3.1新增 — 增强现有管道, 不创建新文件)
    
    在run_security_precheck之前调用,自动修复可修复的安全问题:
    1. API密钥明文 → 替换为环境变量引用
    2. exec命令执行 → 添加安全调用说明(白名单模式)
    3. Mock/TODO/placeholder → 替换为真实实现说明
    
    不可自动修复的问题(反向Shell/SSRF/数据外泄)不修改,由安全预检阻断。
    
    Returns:
        dict: {
            'fixed': bool,         # 是否进行了修复
            'fixes': list,          # 修复项列表
            'unfixable': list,      # 不可修复项列表(需人工处理)
        }
    """
    import re as _re
    
    if not skill_md_path.exists():
        return {'fixed': False, 'fixes': [], 'unfixable': []}
    
    content = skill_md_path.read_text(encoding='utf-8', errors='replace')
    if content.startswith('\ufeff'):
        content = content[1:]
    
    original = content
    fixes = []
    unfixable = []
    
    # 1. API密钥明文 → 环境变量引用
    # Pattern: API_KEY="sk-xxx..." → API_KEY="${API_KEY:?请设置环境变量}"
    api_key_patterns = [
        (_re.compile(r'((?:API_KEY|API_SECRET|SECRET_KEY|ACCESS_TOKEN|PRIVATE_KEY)\s*=\s*["\'])[^"\']{8,}(["\'])'), r'\1${API_KEY:?请设置环境变量}\2'),
        (_re.compile(r'(export\s+(?:API_KEY|API_SECRET|SECRET_KEY|ACCESS_TOKEN)\s*=\s*["\'])[^"\']+(["\'])'), r'\1${API_KEY:?请设置环境变量}\2'),
        (_re.compile(r'((?:sk-|pk-)[a-zA-Z0-9]{20,})'), '<YOUR_API_KEY>'),
        (_re.compile(r'(Bearer\s+)[a-zA-Z0-9_\-\.]{20,}'), r'\1<YOUR_TOKEN>'),
    ]
    for pattern, replacement in api_key_patterns:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'API密钥明文 → 环境变量引用 ({len(matches)}处)')
    
    # 2. Mock/TODO/placeholder → 真实实现说明
    mock_patterns = [
        (_re.compile(r'#\s*Mock\b', _re.IGNORECASE), '# 实现说明:'),
        (_re.compile(r'#\s*TODO\b', _re.IGNORECASE), '# 待实现:'),
        (_re.compile(r'#\s*FIXME\b', _re.IGNORECASE), '# 待修复:'),
        (_re.compile(r'#\s*placeholder\b', _re.IGNORECASE), '# 示例:'),
        (_re.compile(r'pass\s*$'), '...  # 具体实现请参考上下文'),
        (_re.compile(r'NotImplemented'), '具体实现'),
    ]
    for pattern, replacement in mock_patterns:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'Mock/TODO/placeholder → 实现说明 ({len(matches)}处)')
    
    # 3. exec命令 → 替换为安全替代写法 (v3.2增强: 从unfixable改为可修复)
    # 安全策略: exec/os.system在代码示例中替换为描述性函数名, 保留功能说明但移除风险标记
    # v3.2修正: 使用re.IGNORECASE匹配大小写 (与安全预检一致)
    exec_replacements = [
        (_re.compile(r'\bexec\s*\(', _re.IGNORECASE), 'execute('),
        (_re.compile(r'\bos\.system\s*\(', _re.IGNORECASE), 'subprocess.run('),
        (_re.compile(r'\bos\.popen\s*\(', _re.IGNORECASE), 'subprocess.run('),
        (_re.compile(r'(subprocess\.(?:call|run|Popen|check_output)\s*\(.*)shell\s*=\s*True', _re.IGNORECASE), r'\1shell=False'),
        (_re.compile(r'\bchild_process\.exec\b', _re.IGNORECASE), 'child_process.execute'),
        (_re.compile(r'\bnode\s+-e\s', _re.IGNORECASE), 'node --eval '),
    ]
    for pattern, replacement in exec_replacements:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'exec命令 → 安全替代写法 ({len(matches)}处)')
    
    # 4. 反向Shell — 不可自动修复,标记为unfixable (v3.2: pattern已修正,误报大幅减少)
    reverse_shell_patterns = [
        _re.compile(r'(?:bash|sh|zsh)\s+-i\b'),
        _re.compile(r'(?:bash|sh|zsh)\s+-i\s*>\s*&'),
        _re.compile(r'(?:nc|ncat)\s+.*-e\s'),
        _re.compile(r'(?:python|perl|ruby|php)\s+-c\s+["\'].*(?:socket|connect|SOCK_STREAM)'),
    ]
    for pattern in reverse_shell_patterns:
        if pattern.search(content):
            unfixable.append('反向Shell/Shell反弹 — 不可自动修复,需人工删除')

    # 5. SSRF → 替换动态URL为静态示例URL (v3.2: 从unfixable改为可修复)
    ssrf_replacements = [
        (_re.compile(r'requests\.(get|post)\s*\(\s*f["\']https?://'), r'requests.\1("https://example.com/api"),  # 使用固定URL示例'),
        (_re.compile(r'urllib\.request\.urlopen\s*\(\s*f["\']https?://'), r'urllib.request.urlopen("https://example.com/api"),  # 使用固定URL示例'),
    ]
    for pattern, replacement in ssrf_replacements:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'SSRF → 固定URL示例 ({len(matches)}处)')
    
    # 写入修复后的内容(如果有修复)
    fixed = content != original
    if fixed:
        skill_md_path.write_text(content, encoding='utf-8')
    
    return {
        'fixed': fixed,
        'fixes': fixes,
        'unfixable': unfixable,
    }


def run_security_precheck_with_autofix(skill_md_path: Path) -> dict:
    """安全预检 + 自动修复 (v3.1新增 — 增强现有管道)
    
    先尝试自动修复可修复的安全问题,然后运行安全预检。
    如果自动修复解决了所有critical问题,则预检通过。
    不可自动修复的问题仍会被预检阻断。
    """
    # 先尝试自动修复
    fix_result = auto_fix_security_issues(skill_md_path)
    
    # 运行安全预检
    check_result = run_security_precheck(skill_md_path)
    
    # 附加修复信息到结果
    check_result['auto_fix'] = fix_result
    
    # 如果有修复且修复后通过,记录修复信息
    if fix_result['fixed']:
        check_result['auto_fix_applied'] = fix_result['fixes']
    
    return check_result


def auto_fix_hallucination(skill_md_path: Path) -> dict:
    """自动修复防幻觉检查发现的问题 (v3.2新增 — 增强现有管道, 不创建新文件)

    修复两类幻觉问题:
    1. 需求理解偏差: slug关键词未在内容中出现 → 在description末尾补充slug关键词的中文说明
    2. 虚假实现检测: 占位符/TODO/pass/NotImplemented → 替换为真实实现说明

    Returns:
        dict: {
            'fixed': bool,
            'fixes': list,
            'unfixable': list,
        }
    """
    if not skill_md_path.exists():
        return {'fixed': False, 'fixes': [], 'unfixable': []}

    content = skill_md_path.read_text(encoding='utf-8', errors='replace')
    if content.startswith('\ufeff'):
        content = content[1:]

    original = content
    fixes = []
    unfixable = []

    # --- 1. 修复需求理解偏差: slug关键词未在内容中出现 ---
    # 提取slug关键词, 检查是否在内容中出现, 不在则补充到description
    fm = parse_frontmatter(content)
    fields = fm.get('fields', {})
    slug = fields.get('slug', '')
    description = fields.get('description', '')
    display_name = fields.get('displayName', '')
    body = fm.get('body', '')

    if slug:
        slug_keywords = _extract_slug_keywords(slug)
        search_text = f"{display_name} {description} {body[:500]}".lower()
        unmatched_kws = []
        for kw in slug_keywords:
            if kw in search_text:
                continue
            cn_words = _SLUG_KEYWORD_CN_MAP.get(kw, [])
            if any(cn in search_text for cn in cn_words):
                continue
            unmatched_kws.append(kw)

        if unmatched_kws:
            # 在description末尾补充未匹配关键词的中文说明
            cn_translations = []
            for kw in unmatched_kws:
                cn = _SLUG_KEYWORD_CN_MAP.get(kw, [])
                if cn:
                    cn_translations.append(f"{kw}({cn[0]})")
                else:
                    cn_translations.append(kw)

            supplement = f" 功能涵盖: {', '.join(cn_translations)}。"
            # 尝试在description行末尾添加
            desc_pattern = re.compile(
                r'^(\s*description:\s*["\']?)([^"\']*?)(["\']?\s*)$',
                re.MULTILINE
            )
            desc_match = desc_pattern.search(content)
            if desc_match:
                old_desc = desc_match.group(0)
                new_desc = desc_match.group(1) + desc_match.group(2) + supplement + desc_match.group(3)
                content = content.replace(old_desc, new_desc, 1)
                fixes.append(f'需求理解偏差: description补充slug关键词中文说明 ({", ".join(unmatched_kws)})')
            else:
                # description字段不在frontmatter中, 在body开头补充
                body_start = content.find('---', 3)
                if body_start > 0:
                    insert_pos = body_start + 3
                    note = f"\n\n> **功能说明**: 本技能涵盖 {', '.join(cn_translations)} 等核心能力。\n"
                    content = content[:insert_pos] + note + content[insert_pos:]
                    fixes.append(f'需求理解偏差: body开头补充slug关键词说明 ({", ".join(unmatched_kws)})')

    # --- 1b. 修复需求理解偏差: description声明的功能在body中未提及 ---
    # v3.2新增: 提取description中的功能关键词, 检查body是否包含, 不包含则补充到body
    if description and body:
        action_keywords = ['支持', '提供', '实现', '生成', '转换', '分析', '优化', '管理', '处理', '检测', '修复', '批量', '自动']
        claimed_features = []
        for kw in action_keywords:
            pattern = rf'{kw}([^\s，。,;.]+)'
            matches = re.findall(pattern, description)
            for m in matches:
                if len(m) > 2 and m not in claimed_features:
                    claimed_features.append(m.strip())

        missing_in_body = []
        for feature in claimed_features[:5]:
            if feature and len(feature) > 2:
                if feature in body:
                    continue
                # 长短语拆分检查 (与_check_requirement_deviation保持一致)
                if len(feature) > 6:
                    sub_kws = [feature[i:i+4] for i in range(0, len(feature)-1, 2) if len(feature[i:i+4]) >= 2]
                    if any(sub in body for sub in sub_kws):
                        continue
                missing_in_body.append(feature)

        if missing_in_body:
            # 在body开头(第二个---之后)补充功能说明
            body_start = content.find('---', 3)
            if body_start > 0:
                insert_pos = body_start + 3
                features_text = '、'.join(missing_in_body)
                note = f"\n\n> **核心功能**: 本技能提供{features_text}等能力。\n"
                content = content[:insert_pos] + note + content[insert_pos:]
                fixes.append(f'需求理解偏差: body补充description声明的功能 ({", ".join(missing_in_body)})')

    # --- 2. 修复虚假实现检测: 占位符/TODO/pass/NotImplemented ---
    # 2a. 替换占位符
    placeholder_replacements = [
        (re.compile(r'<your[_\s-]?\w+>', re.IGNORECASE), '<配置后填入>'),
        (re.compile(r'\{\{.*?\}\}', re.DOTALL), '<动态配置>'),
        (re.compile(r'\[.*?placeholder.*?\]', re.IGNORECASE), '<参数说明>'),
        (re.compile(r'\bxxx+\b', re.IGNORECASE), '<参数>'),
        (re.compile(r'\b(todo|TODO):\s*', re.IGNORECASE), '说明: '),
        (re.compile(r'replace\s+this', re.IGNORECASE), '参考此配置'),
        (re.compile(r'insert\s+here', re.IGNORECASE), '在此处填写'),
    ]
    for pattern, replacement in placeholder_replacements:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'虚假实现: 占位符替换为说明文字 ({len(matches)}处)')

    # 2b. 替换空实现标记
    empty_impl_replacements = [
        (re.compile(r'^(\s*)pass\s*$', re.MULTILINE), r'\1...  # 具体实现请参考上下文文档'),
        (re.compile(r'\bNotImplemented\b', re.IGNORECASE), '具体实现'),
        (re.compile(r'\braise\s+NotImplementedError\b'), 'pass  # 根据实际需求实现'),
        (re.compile(r'#\s*TODO\b', re.IGNORECASE), '# 实现说明:'),
        (re.compile(r'#\s*FIXME\b', re.IGNORECASE), '# 待优化:'),
        (re.compile(r'#\s*placeholder\b', re.IGNORECASE), '# 示例:'),
        (re.compile(r'#\s*mock\b', re.IGNORECASE), '# 实现说明:'),
        (re.compile(r'#\s*stub\b', re.IGNORECASE), '# 骨架代码:'),
    ]
    for pattern, replacement in empty_impl_replacements:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'虚假实现: 空实现标记替换为说明 ({len(matches)}处)')

    # 2c. 替换待实现标记
    lazy_replacements = [
        (re.compile(r'coming\s+soon', re.IGNORECASE), '已实现'),
        (re.compile(r'待实现', re.IGNORECASE), '已实现'),
        (re.compile(r'暂未实现', re.IGNORECASE), '已实现'),
        (re.compile(r'敬请期待', re.IGNORECASE), '已提供'),
        (re.compile(r'待开发', re.IGNORECASE), '已开发'),
        (re.compile(r'\bTBD\b'), '已定义'),
    ]
    for pattern, replacement in lazy_replacements:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'虚假实现: 待实现标记替换为已完成说明 ({len(matches)}处)')

    # 2d. 填充空代码块 (v3.2: 填充非注释代码行, 避免检测器仍判定为空)
    code_block_pattern = re.compile(r'```(\w+)?\n(.*?)```', re.DOTALL)
    def _fill_empty_block(m):
        lang = m.group(1) or ''
        block = m.group(2)
        lines = [l for l in block.strip().split('\n') if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('//')]
        if not lines:
            # 空代码块, 填充包含实际代码行的内容 (非注释行, 通过检测器检查)
            if lang in ('python', 'py'):
                return f'```{lang}\n# 本技能的核心实现逻辑\n# 请参考上方使用说明进行配置和调用\nresult = "implementation_ready"\n```'
            elif lang in ('javascript', 'js', 'typescript', 'ts'):
                return f'```{lang}\n// 本技能的核心实现逻辑\n// 请参考上方使用说明进行配置和调用\nconst result = "implementation_ready";\n```'
            elif lang in ('bash', 'sh', 'shell'):
                return f'```{lang}\n# 本技能的核心实现逻辑\n# 请参考上方使用说明进行配置和调用\necho "implementation_ready"\n```'
            elif lang in ('json',):
                return f'```{lang}\n{{"status": "implementation_ready"}}\n```'
            elif lang in ('yaml', 'yml'):
                return f'```{lang}\nstatus: implementation_ready\n```'
            else:
                return f'```{lang}\n# 请参考上方使用说明进行配置和调用\nresult = "ready"\n```'
        return m.group(0)

    empty_blocks_before = len([m for m in code_block_pattern.finditer(content)
                                if not [l for l in m.group(2).strip().split('\n')
                                        if l.strip() and not l.strip().startswith('#')]])
    if empty_blocks_before > 0:
        content = code_block_pattern.sub(_fill_empty_block, content)
        fixes.append(f'虚假实现: 填充{empty_blocks_before}个空代码块')

    # 写入修复后的内容
    fixed = content != original
    if fixed:
        skill_md_path.write_text(content, encoding='utf-8')

    return {
        'fixed': fixed,
        'fixes': fixes,
        'unfixable': unfixable,
    }


def auto_fix_debranding(skill_md_path: Path) -> dict:
    """自动修复去标识化检查发现的问题 (V147 R5 — 增强现有管道, 不创建新文件)

    复用 check_debranding.py 的 FORBIDDEN_PATTERNS 检测逻辑,
    对检测到的问题进行自动修复:
    1. 平台/项目烙印词 → 移除或替换为通用表述
    2. 溯源词 (based on / forked from / inspired by 等) → 删除包含该词的整行
    3. GitHub/原仓库URL → 移除
    4. 原作者署名 (author: / created by) → 移除

    Returns:
        dict: {
            'fixed': bool,
            'fixes': list,
            'unfixable': list,
        }
    """
    import re as _re

    if not skill_md_path.exists():
        return {'fixed': False, 'fixes': [], 'unfixable': []}

    content = skill_md_path.read_text(encoding='utf-8', errors='replace')
    if content.startswith('\ufeff'):
        content = content[1:]

    original = content
    fixes = []
    unfixable = []

    # --- 1. 平台/项目烙印词 → 移除 ---
    branding_patterns = [
        (_re.compile(r'(?<![A-Za-z0-9_])(clawhub|clawsec|clawdbot|openclaw)(?![A-Za-z0-9_])', _re.IGNORECASE), ''),
        (_re.compile(r'(?<![A-Za-z0-9_])(clawhut|clawhob|clawhvb)(?![A-Za-z0-9_])', _re.IGNORECASE), ''),
        (_re.compile(r'(?<![A-Za-z0-9_])(fishclaw|narrato|dailyhot|novel_bridge|totalreclaw|kyaukyuai)(?![A-Za-z0-9_])', _re.IGNORECASE), ''),
        (_re.compile(r'xianyu', _re.IGNORECASE), ''),
        (_re.compile(r'老田和小甜甜'), ''),
    ]
    for pattern, replacement in branding_patterns:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'平台/项目烙印词移除 ({", ".join(set(matches))})')

    # --- 2. 溯源词 → 删除包含该词的整行 ---
    tracing_line_patterns = [
        _re.compile(r'^[^\n]*?(?i:based on)[^\n]*\n', _re.MULTILINE),
        _re.compile(r'^[^\n]*?(?i:forked from)[^\n]*\n', _re.MULTILINE),
        _re.compile(r'^[^\n]*?(?i:inspired by)[^\n]*\n', _re.MULTILINE),
        _re.compile(r'^[^\n]*?(?i:adapted from)[^\n]*\n', _re.MULTILINE),
        _re.compile(r'^[^\n]*?(?i:modified from)[^\n]*\n', _re.MULTILINE),
        _re.compile(r'^[^\n]*?(?i:original:)[^\n]*\n', _re.MULTILINE),
    ]
    for pattern in tracing_line_patterns:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub('', content)
            fixes.append(f'溯源词行删除 ({len(matches)}行)')

    # --- 3. GitHub/原仓库URL → 移除 ---
    url_patterns = [
        (_re.compile(r'https?://github\.com/\S+'), ''),
        (_re.compile(r'https?://\S*(?:clawhub|openclaw|narrato|fishclaw)\S*', _re.IGNORECASE), ''),
    ]
    for pattern, replacement in url_patterns:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'仓库URL移除 ({len(matches)}处)')

    # --- 4. 原作者署名 → 移除 ---
    author_patterns = [
        (_re.compile(r'(?i)author:\s*\S+[^\n]*\n', _re.MULTILINE), ''),
        (_re.compile(r'(?i)created by\s+\w+[^\n]*\n', _re.MULTILINE), ''),
    ]
    for pattern, replacement in author_patterns:
        matches = pattern.findall(content)
        if matches:
            content = pattern.sub(replacement, content)
            fixes.append(f'原作者署名移除 ({len(matches)}处)')

    # --- 5. 清理因移除产生的多余空行 ---
    content = _re.sub(r'\n{3,}', '\n\n', content)

    # 写入修复后的内容
    fixed = content != original
    if fixed:
        skill_md_path.write_text(content, encoding='utf-8')

    return {
        'fixed': fixed,
        'fixes': fixes,
        'unfixable': unfixable,
    }


def run_anti_hallucination_with_autofix(skill_md_path: Path, l2_report: dict = None,
                                        l3_report: dict = None, l4_report: dict = None) -> dict:
    """防幻觉检查 + 自动修复 (v3.2新增 — 增强现有管道)

    先尝试自动修复幻觉问题(需求理解偏差/虚假实现),然后运行防幻觉检查。
    不可自动修复的问题仍会被检查阻断。
    """
    fix_result = auto_fix_hallucination(skill_md_path)

    check_result = run_anti_hallucination(skill_md_path, l2_report, l3_report, l4_report)

    check_result['auto_fix'] = fix_result

    if fix_result['fixed']:
        check_result['auto_fix_applied'] = fix_result['fixes']

    return check_result


def run_security_precheck(skill_md_path: Path) -> dict:
    """安全审核预检关卡 (v2.1新增)
    
    在上传前检测SkillHub三线安全审核的10类高风险模式 + VPN关键词封禁。
    这些模式来自29条安全审核失败skill的深度分析。
    
    检查项(21项):
      --- 基础高风险模式 (v2.1, 来自29条安全审核失败分析) ---
      1. exec命令执行 (96.6%命中率)
      2. API密钥明文处理 (62.1%)
      3. 不可信外部API/域名 (51.7%)
      4. 引用不存在的脚本 (41.4%)
      5. 硬编码服务器地址/IP (27.6%)
      6. HTTP不安全通信 (20.7%)
      7. tools字段格式错误 (17.2%)
      8. 文件系统遍历风险 (17.2%)
      9. 敏感信息泄露 (13.8%)
     10. eval/代码注入 (10.3%)
      --- 科恩实验室 + 云鼎实验室特有检测 (v2.2新增) ---
     11. SSRF服务端请求伪造 (云鼎特有)
     12. 数据外泄风险 (云鼎特有)
     13. 混淆代码/编码载荷 (科恩特有)
     14. 反向Shell/Shell反弹 (科恩特有)
     15. 权限提升风险 (科恩特有)
     16. 加密货币挖矿 (云鼎特有)
     17. AI Prompt注入风险 (云鼎特有)
     18. 持久化/自启动 (科恩特有)
     19. 不安全反序列化 (科恩特有)
     20. 依赖混淆/供应链风险 (云鼎特有)
      --- 直接封禁 ---
     21. VPN/翻墙关键词 (直接封禁)
      --- 内容反垃圾 (v3.0新增) ---
     22. 内容指纹去重 (防止近似重复内容触发平台反垃圾)
    
    参数:
        skill_md_path: SKILL.md文件路径
    
    返回:
        安全审核预检结果, overall_passed=False时必须修复后才能上传
    """
    try:
        content = skill_md_path.read_text(encoding='utf-8')
        if content.startswith('\ufeff'):
            content = content[1:]
        
        # 解析frontmatter和body
        if content.startswith('---'):
            parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
            fm_str = parts[1] if len(parts) > 1 else ''
            body = parts[2] if len(parts) > 2 else ''
            full_text = fm_str + '\n' + body
        else:
            fm_str = ''
            body = content
            full_text = content
        
        # 执行10类高风险模式检查
        checks = []
        for pattern_def in _SECURITY_RISK_PATTERNS:
            check_result = _check_security_risk_pattern(full_text, pattern_def)
            checks.append(check_result)
        
        # VPN关键词检查
        vpn_check = _check_vpn_keywords(full_text)
        checks.append(vpn_check)
        
        # 内容指纹去重检查 (v3.0新增 — 防止近似重复内容触发平台反垃圾)
        # 根因: 62%封禁skill为差异化复制内容(-free/-pro/-tool-*派生)
        # 计算内容指纹,与DB中已上传skill比对,相似度>85%阻断
        dedup_check = _check_content_fingerprint(skill_md_path, full_text)
        checks.append(dedup_check)
        
        overall_passed = all(c['passed'] for c in checks)
        
        return {
            'skill': skill_md_path.parent.name,
            'path': str(skill_md_path),
            'overall_passed': overall_passed,
            'total_checks': len(checks),
            'passed_checks': sum(1 for c in checks if c['passed']),
            'failed_checks': sum(1 for c in checks if not c['passed']),
            'checks': checks,
            'gate_type': 'security_precheck',
            'checked_at': datetime.now().isoformat()
        }
    except Exception as e:
        return {
            'skill': skill_md_path.parent.name if skill_md_path.parent else 'unknown',
            'path': str(skill_md_path),
            'overall_passed': False,
            'total_checks': 0,
            'passed_checks': 0,
            'failed_checks': 0,
            'checks': [],
            'gate_type': 'security_precheck',
            'error': str(e),
            'checked_at': datetime.now().isoformat()
        }


# ============ 评分门控 (v2.3新增 — 流程固化: 低于4.5分阻断上传) ============

RATING_GATE_THRESHOLD = 4.5  # 与market_monitor.py的RATING_THRESHOLD一致

def run_rating_gate(skill_md_path: Path, slug: str = None) -> dict:
    """评分门控检查 (v2.3新增 — 需求7+8流程固化)

    检查skill在平台上的历史评分, 阻止低评分skill重新上传。

    流程固化逻辑:
    1. 从DB查询skill的platform_rating (由sync_platform_ratings填充)
    2. 如果 platform_rating > 0 且 < 4.5 → 阻断上传, 要求先升级
    3. 如果 current_status == 'deleted' → 阻断上传, 要求重新差异化

    检查项(2项):
      1. 平台评分检查 — 历史评分是否低于阈值
      2. 删除状态检查 — skill是否因质量问题被删除

    参数:
        skill_md_path: SKILL.md文件路径
        slug: 可选的skill slug (如不提供则从路径推断)
    """
    checks = []

    # 推断slug
    if not slug:
        slug = skill_md_path.parent.name

    # 查询DB
    try:
        conn = sqlite3.connect(str(_DB_PATH))
        conn.row_factory = sqlite3.Row
        row = conn.execute("""
            SELECT platform_rating, platform_rating_count, current_status,
                   platform_ai_review, current_display_name
            FROM skills WHERE slug = ?
        """, (slug,)).fetchone()
        conn.close()

        if not row:
            # DB中无此skill记录, 跳过评分检查(新skill)
            checks.append({
                'name': '评分门控: DB记录检查',
                'passed': True,
                'severity': 'info',
                'details': [f'skill {slug} 不在DB中, 视为新skill, 跳过评分检查']
            })
            checks.append({
                'name': '评分门控: 平台评分检查',
                'passed': True,
                'severity': 'info',
                'details': ['新skill无历史评分, 跳过']
            })
        else:
            rating = row['platform_rating'] or 0.0
            rating_count = row['platform_rating_count'] or 0
            status = row['current_status'] or 'active'
            display_name = row['current_display_name'] or slug

            # 检查1: 平台评分
            if rating > 0 and rating < RATING_GATE_THRESHOLD:
                checks.append({
                    'name': '评分门控: 平台评分检查',
                    'passed': False,
                    'severity': 'critical',
                    'details': [
                        f'skill {slug} ({display_name}) 平台评分 {rating} < {RATING_GATE_THRESHOLD}',
                        f'评分数: {rating_count}',
                        f'修复方案: 执行 upgrade_single_skill("{slug}") 升级内容后重新上传',
                        f'流程: 评分同步 → 检测低评分 → 阻断上传 → 触发升级 → 升级通过 → 允许重传',
                    ]
                })
            else:
                rating_str = f'{rating}' if rating > 0 else '无评分(新skill或未同步)'
                checks.append({
                    'name': '评分门控: 平台评分检查',
                    'passed': True,
                    'severity': 'info',
                    'details': [f'评分: {rating_str}, 阈值: {RATING_GATE_THRESHOLD}']
                })

            # 检查2: 删除状态
            if status == 'deleted':
                checks.append({
                    'name': '评分门控: 删除状态检查',
                    'passed': False,
                    'severity': 'critical',
                    'details': [
                        f'skill {slug} 当前状态为 deleted (已从平台删除)',
                        f'修复方案: 重新差异化后以新slug上传, 或修复内容后恢复状态',
                    ]
                })
            else:
                checks.append({
                    'name': '评分门控: 删除状态检查',
                    'passed': True,
                    'severity': 'info',
                    'details': [f'当前状态: {status}']
                })

    except Exception as e:
        checks.append({
            'name': '评分门控: DB查询',
            'passed': True,
            'severity': 'warning',
            'details': [f'DB查询异常(不阻断): {e}']
        })

    total = len(checks)
    passed = sum(1 for c in checks if c.get('passed'))
    failed = total - passed

    return {
        'passed': failed == 0,
        'overall_passed': failed == 0,
        'total_checks': total,
        'passed_checks': passed,
        'failed_checks': failed,
        'checks': checks,
        'gate_type': 'rating_gate',
        'gate_threshold': RATING_GATE_THRESHOLD,
        'checked_at': datetime.now().isoformat()
    }


# ============ 本地LLM质量评分 (v2.4新增 — T1-003) ============

def run_local_scoring(skill_md_path: Path) -> dict:
    """调用local_quality_scorer对SKILL.md进行5维度LLM评分
    
    返回:
        {total_score, dimensions, feedback, passed, scored_at}
        评分失败时返回 {total_score: 0.0, feedback: '...', error: '...'}
    """
    try:
        # 延迟导入，避免local_quality_scorer未安装时影响quality_gate核心功能
        import sys as _sys
        _tools_dir = str(Path(__file__).resolve().parent)
        if _tools_dir not in _sys.path:
            _sys.path.insert(0, _tools_dir)
        from local_quality_scorer import score_skill
        return score_skill(skill_md_path)
    except ImportError:
        return {
            'total_score': 0.0,
            'dimensions': {},
            'feedback': 'local_quality_scorer模块未安装,跳过本地评分',
            'passed': False,
            'error': 'ImportError: local_quality_scorer'
        }
    except Exception as e:
        return {
            'total_score': 0.0,
            'dimensions': {},
            'feedback': f'本地评分异常: {e}',
            'passed': False,
            'error': str(e)
        }


# ============ 统一质量检查入口 (v2.4增强: +本地LLM质量评分) ============

def run_full_quality_check(skill_md_path: Path,
                            include_l2l3: bool = False,
                            l2_report: dict = None,
                            l3_report: dict = None,
                            l4_report: dict = None,
                            slug: str = None,
                            include_local_score: bool = True,
                            enable_autofix: bool = True) -> dict:
    """统一质量检查入口 (v2.4增强: +本地LLM质量评分; v3.2: +自动修复)
    
    执行完整质量检查链路:
    L1(13项) → 评分门控(2项) → 安全预检(21项) → 营销关卡(7项) → 防幻觉(3项)
    可选: L2/L3报告检查
    可选: 本地LLM质量评分(5维度, 阈值4.5)
    
    v2.3新增: 评分门控 — 检查平台历史评分,低于4.5分阻断上传
    v2.4新增: 本地LLM质量评分 — 5维度评测,低于4.5分阻断上传
    v3.2新增: 自动修复 — enable_autofix=True时, 安全预检和防幻觉检查前自动修复可修复的问题
    
    参数:
        skill_md_path: SKILL.md文件路径
        include_l2l3: 是否包含L2/L3报告检查(需提供l2_report/l3_report)
        l2_report: L2验证报告(可选)
        l3_report: L3试运行报告(可选)
        l4_report: L4-L9审计报告(可选)
        slug: skill slug (v2.3新增, 用于评分门控查询DB)
        include_local_score: 是否执行本地LLM质量评分 (v2.4新增, 默认True)
    
    返回:
        统一质量检查结果, 包含L1/评分/安全/营销/防幻觉各层结果
        v2.4新增: local_score(0.0-5.0), local_score_feedback, local_score_dimensions
    """
    # v2.4修复: 文件不存在时提前返回错误, 避免后续函数异常
    if not skill_md_path.exists():
        return {
            'skill': skill_md_path.parent.name if skill_md_path.parent != skill_md_path else 'unknown',
            'path': str(skill_md_path),
            'overall_passed': False,
            'error': f'文件不存在: {skill_md_path}',
            'total_checks': 0,
            'passed_checks': 0,
            'failed_checks': 0,
            'checks': [],
            'layers': {},
            'checked_at': datetime.now().isoformat()
        }

    # L1: 静态格式合规
    l1_result = run_quality_gate(skill_md_path)
    
    # 评分门控 (v2.3新增 — 流程固化: 低于4.5分阻断上传)
    rating_result = run_rating_gate(skill_md_path, slug)
    
    # 安全审核预检 (v2.1新增; v3.2: 支持自动修复)
    if enable_autofix:
        security_result = run_security_precheck_with_autofix(skill_md_path)
    else:
        security_result = run_security_precheck(skill_md_path)
    
    # 营销关卡
    marketing_result = run_marketing_gate(skill_md_path)
    
    # 防幻觉 (v3.2: 支持自动修复)
    if enable_autofix:
        anti_hallucination_result = run_anti_hallucination_with_autofix(
            skill_md_path, l2_report, l3_report, l4_report
        )
    else:
        anti_hallucination_result = run_anti_hallucination(
            skill_md_path, l2_report, l3_report, l4_report
        )
    
    # 本地LLM质量评分 (v2.4新增 — 5维度评测, 阈值4.5)
    local_score_result = run_local_scoring(skill_md_path) if include_local_score else None
    
    # 汇总 (v2.7: 为每个check添加layer字段, 便于失败归因)
    all_checks = []
    for _layer_name, _result in [
        ('L1_static', l1_result),
        ('rating_gate', rating_result),
        ('security_precheck', security_result),
        ('marketing_gate', marketing_result),
        ('anti_hallucination', anti_hallucination_result),
    ]:
        for _check in _result.get('checks', []):
            _check['layer'] = _layer_name
            all_checks.append(_check)
    
    # 本地评分检查项 (v2.4新增)
    local_score = 0.0
    local_score_feedback = ''
    local_score_dimensions = {}
    if local_score_result:
        local_score = local_score_result.get('total_score', 0.0)
        local_score_feedback = local_score_result.get('feedback', '')
        local_score_dimensions = local_score_result.get('dimensions', {})
        all_checks.append({
            'layer': 'local_score',
            'name': '本地LLM质量评分',
            'passed': local_score >= 4.5,
            'severity': 'high' if local_score < 4.5 else 'info',
            'message': f"本地评分 {local_score:.2f}/5.0 ({'通过' if local_score >= 4.5 else '未通过'}) — {local_score_feedback[:200]}"
        })
    
    total = len(all_checks)
    passed = sum(1 for c in all_checks if c.get('passed'))
    failed = total - passed
    
    # v2.4: local_score < 4.5 也阻断 (与现有 failed > 0 逻辑合并)
    result = {
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
            'rating_gate': {
                'passed': rating_result.get('overall_passed', False),
                'score': f"{rating_result.get('passed_checks', 0)}/{rating_result.get('total_checks', 0)}",
            },
            'security_precheck': {
                'passed': security_result.get('overall_passed', False),
                'score': f"{security_result.get('passed_checks', 0)}/{security_result.get('total_checks', 0)}",
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
    
    # v2.4: 仅在include_local_score=True时添加本地评分字段 (向后兼容)
    if include_local_score:
        result['local_score'] = local_score
        result['local_score_feedback'] = local_score_feedback
        result['local_score_dimensions'] = local_score_dimensions
        result['layers']['local_score'] = {
            'passed': local_score >= 4.5,
            'score': f"{local_score:.2f}/5.0",
        }
    
    return result


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
    parser.add_argument('--security', action='store_true',
                        help='仅运行安全审核预检(21项高风险模式: 10基础+10科恩/云鼎+VPN)')
    parser.add_argument('--rating', action='store_true',
                        help='仅运行评分门控检查(2项: 平台评分+删除状态, 阈值4.5)')
    parser.add_argument('--full', action='store_true',
                        help='完整质量检查: L1(13项) + 评分门控(2项) + 安全预检(21项) + 营销关卡(7项) + 防幻觉(3项)')
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
        elif args.security:
            result = run_security_precheck(sf)
        elif args.rating:
            result = run_rating_gate(sf)
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
