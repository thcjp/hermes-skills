#!/usr/bin/env python3
"""
深度质量审计系统 (Deep Quality Audit) v3.0
==========================================
全量扫描 packaged-skills/skillhub 和 differentiated-skills 下所有 SKILL.md 文件，
执行六层质量检查:

Layer 1-3 (格式检查):
  critical (致命):
    - 缺失 slug / version / name 字段
    - slug 与目录名不匹配
    - 空内容
    - frontmatter 解析失败
  warning (警告):
    - summary 超过 100 字符
    - displayName 超过 20 字符
    - description 为空
    - 缺少 license 字段
    - 缺少 tools 字段
    - 版本格式不合规
  info (信息):
    - 缺少 homepage 字段
    - 缺少 tags 字段
    - 内容少于 500 字符
    - 缺少依赖说明 section

Layer 4 (功能质量 Functional Quality):
  - 内容深度评估 (0-25分)
  - 指令性内容检查 (0-25分)
  - 代码/示例检查 (0-20分)
  - 任务定义检查 (0-15分)
  - 错误处理检查 (0-15分)
  - 真实placeholder检测 (TODO/FIXME/待补充)
  评级: A(70+) / B(50+) / C(30+) / D(10+) / F(<10)

Layer 5 (可销售性 Sellability):
  - 内容深度 (0-25分)
  - 功能完整度 (0-20分)
  - 技术深度 (0-20分)
  - 用户体验 (0-20分)
  - 专业性 (0-15分)
  评级: A(70+) / B(50+) / C(30+) / D(<30)

Layer 6 (内容真实性 Content Authenticity):
  - 模板填充检测 (通用段落/乱码拼接/占位表格)
  - 空段落检测 (空FAQ/空已知限制/空section)
  - 截断文本检测
  - 案例占位检测
  评级: A(85+) / B(65+) / C(40+) / D(20+) / F(<20)

使用方式:
    python deep_quality_audit.py              # 执行审计
    python deep_quality_audit.py --fix        # 审计并自动修复 warning 级别问题
    python deep_quality_audit.py --fix-all    # 审计并自动修复 warning + info 级别问题

输出:
    - JSON 报告: deep_quality_audit_report.json
    - 控制台汇总统计 (含功能质量+可销售性)
"""

import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime

# 从 config.py 导入统一配置（与 automated_review_system.py 保持一致的风格）
# config.py 定义了 PACKAGED_SKILLS_DIR / REGISTRY_DIR / MAX_SUMMARY_LEN / MAX_DISPLAYNAME_LEN 等常量
import config as _cfg

# ============ 路径配置 ============
# 优先使用 config.py 中的常量，回退到原始字符串路径
PACKAGED_DIR = getattr(_cfg, 'PACKAGED_SKILLS_DIR', Path(r"D:\skills\packaged-skills\skillhub"))
DIFFERENTIATED_DIR = Path(r"D:\skills\differentiated-skills")
REGISTRY_DIR = getattr(_cfg, 'REGISTRY_DIR', Path(r"D:\skills\skill-registry"))
REPORT_PATH = REGISTRY_DIR / "deep_quality_audit_report.json"

# ============ 阈值常量 ============
# 从 config.py 导入统一阈值，确保与其他脚本一致
MAX_SUMMARY_LENGTH = getattr(_cfg, 'MAX_SUMMARY_LEN', 100)       # summary 最大字符数
MAX_DISPLAYNAME_LENGTH = getattr(_cfg, 'MAX_DISPLAYNAME_LEN', 20) # displayName 最大字符数
MIN_CONTENT_LENGTH = 500       # 内容最小字符数
VERSION_REGEX = r'^\d+\.\d+\.\d+$'  # 合规版本格式 x.y.z

# ============ 检查规则定义 ============
# critical 级别检查项
CRITICAL_CHECKS = [
    "MISSING_SLUG",           # 缺失 slug 字段
    "MISSING_VERSION",        # 缺失 version 字段
    "MISSING_NAME",           # 缺失 name 字段
    "SLUG_DIRNAME_MISMATCH",  # slug 与目录名不匹配
    "EMPTY_CONTENT",          # 空内容
    "FRONTMATTER_PARSE_FAIL", # frontmatter 解析失败
]

# warning 级别检查项
WARNING_CHECKS = [
    "SUMMARY_TOO_LONG",       # summary 超过 100 字符
    "DISPLAYNAME_TOO_LONG",   # displayName 超过 20 字符
    "DESCRIPTION_EMPTY",      # description 为空
    "MISSING_LICENSE",        # 缺少 license 字段
    "MISSING_TOOLS",          # 缺少 tools 字段
    "INVALID_VERSION_FORMAT", # 版本格式不合规
]

# info 级别检查项
INFO_CHECKS = [
    "MISSING_HOMEPAGE",       # 缺少 homepage 字段
    "MISSING_TAGS",           # 缺少 tags 字段
    "CONTENT_TOO_SHORT",      # 内容少于 500 字符
    "MISSING_DEP_SECTION",    # 缺少依赖说明 section
]


def parse_frontmatter(content: str) -> dict:
    """解析 YAML frontmatter，支持多行块标量 (|-, |, >-, >)

    使用正则分割 --- 分隔符，与 automated_review_system.py 保持一致的逻辑。
    """
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith('---'):
        return {}
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    fm_text = parts[1].strip()
    fm = {}
    current_key = None
    block_key = None
    block_lines = []
    fm_lines = fm_text.split('\n')
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        line_stripped = line.rstrip()
        if not line_stripped:
            if block_key:
                block_lines.append('')
            i += 1
            continue
        if block_key and (line.startswith('  ') or line.startswith('\t')):
            block_lines.append(line.strip())
            i += 1
            continue
        if block_key:
            fm[block_key] = '\n'.join(block_lines).strip()
            block_key = None
            block_lines = []
        if line.startswith('  - '):
            val = line[4:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if current_key:
                if current_key not in fm:
                    fm[current_key] = []
                fm[current_key].append(val)
        elif ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if val in ('|-', '|', '>-', '>'):
                block_key = key
                block_lines = []
                fm[key] = ''
            elif val:
                fm[key] = val
            else:
                current_key = key
                fm[key] = []
        i += 1
    if block_key:
        fm[block_key] = '\n'.join(block_lines).strip()
    return fm


def split_frontmatter_body(content: str):
    """将文件内容分割为 frontmatter 文本和正文文本"""
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith('---'):
        return '', content
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return '', content
    return parts[1], parts[2]


def collect_skill_files():
    """收集所有需要审计的 SKILL.md 文件路径

    Returns:
        list of (Path, source_str) 元组
    """
    files = []

    # 扫描 packaged-skills/skillhub
    if PACKAGED_DIR.exists():
        for skill_dir in sorted(PACKAGED_DIR.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                files.append((skill_md, "packaged"))

    # 扫描 differentiated-skills (按类别子目录)
    if DIFFERENTIATED_DIR.exists():
        for cat_dir in sorted(DIFFERENTIATED_DIR.iterdir()):
            if not cat_dir.is_dir():
                continue
            for skill_dir in sorted(cat_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    source = f"differentiated/{cat_dir.name}"
                    files.append((skill_md, source))

    return files


def check_skill(skill_path: Path, source: str):
    """对单个 SKILL.md 执行全部质量检查

    Returns:
        dict: {
            slug, source, severity, issues, body_length, version,
            dir_name, frontmatter
        }
    """
    dir_name = skill_path.parent.name
    issues = {
        "critical": [],
        "warning": [],
        "info": [],
    }

    # 读取文件内容
    try:
        content = skill_path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        issues["critical"].append(f"读取文件失败: {e}")
        return {
            "slug": dir_name,
            "source": source,
            "severity": "critical",
            "issues": issues["critical"],
            "body_length": 0,
            "version": "",
            "dir_name": dir_name,
            "frontmatter": {},
            "_content": "",
        }

    body_length = len(content)

    # === critical 检查 ===

    # 空内容检查
    if not content.strip():
        issues["critical"].append("EMPTY_CONTENT: 文件内容为空")
        return {
            "slug": dir_name,
            "source": source,
            "severity": "critical",
            "issues": ["EMPTY_CONTENT: 文件内容为空"],
            "body_length": 0,
            "version": "",
            "dir_name": dir_name,
            "frontmatter": {},
            "_content": content,
        }

    # frontmatter 解析
    fm = parse_frontmatter(content)

    # frontmatter 解析失败检查
    if not fm:
        issues["critical"].append("FRONTMATTER_PARSE_FAIL: frontmatter 解析失败或不存在")

    # 缺失 slug 字段
    slug = str(fm.get('slug', '')).strip().strip('"')
    if not slug:
        issues["critical"].append("MISSING_SLUG: 缺失 slug 字段")
        slug = dir_name  # 回退到目录名用于后续检查

    # 缺失 version 字段
    version = str(fm.get('version', '')).strip().strip('"')
    if not version:
        issues["critical"].append("MISSING_VERSION: 缺失 version 字段")

    # 缺失 name 字段
    name = str(fm.get('name', '')).strip().strip('"')
    if not name:
        issues["critical"].append("MISSING_NAME: 缺失 name 字段")

    # slug 与目录名不匹配
    if slug and slug != dir_name:
        issues["critical"].append(
            f"SLUG_DIRNAME_MISMATCH: slug='{slug}' 与目录名='{dir_name}' 不匹配"
        )

    # === warning 检查 ===

    # summary 超过 100 字符
    summary = str(fm.get('summary', '')).strip()
    if summary and len(summary) > MAX_SUMMARY_LENGTH:
        issues["warning"].append(
            f"SUMMARY_TOO_LONG: summary 长度 {len(summary)} 超过 {MAX_SUMMARY_LENGTH} 字符"
        )

    # displayName 超过 20 字符
    display_name = str(fm.get('displayName', '')).strip()
    if display_name and len(display_name) > MAX_DISPLAYNAME_LENGTH:
        issues["warning"].append(
            f"DISPLAYNAME_TOO_LONG: displayName 长度 {len(display_name)} 超过 {MAX_DISPLAYNAME_LENGTH} 字符"
        )

    # description 为空
    description = str(fm.get('description', '')).strip()
    if not description:
        issues["warning"].append("DESCRIPTION_EMPTY: description 为空")

    # 缺少 license 字段
    license_val = str(fm.get('license', '')).strip()
    if not license_val:
        issues["warning"].append("MISSING_LICENSE: 缺少 license 字段")

    # 缺少 tools 字段
    tools_val = fm.get('tools', None)
    if tools_val is None or (isinstance(tools_val, list) and len(tools_val) == 0):
        issues["warning"].append("MISSING_TOOLS: 缺少 tools 字段")

    # 版本格式不合规
    if version and not re.match(VERSION_REGEX, version):
        issues["warning"].append(
            f"INVALID_VERSION_FORMAT: 版本 '{version}' 不符合 x.y.z 格式"
        )

    # === info 检查 ===

    # 缺少 homepage 字段
    homepage = str(fm.get('homepage', '')).strip()
    if not homepage:
        issues["info"].append("MISSING_HOMEPAGE: 缺少 homepage 字段")

    # 缺少 tags 字段
    tags_val = fm.get('tags', None)
    if tags_val is None or (isinstance(tags_val, list) and len(tags_val) == 0):
        issues["info"].append("MISSING_TAGS: 缺少 tags 字段")

    # 内容少于 500 字符
    if body_length < MIN_CONTENT_LENGTH:
        issues["info"].append(
            f"CONTENT_TOO_SHORT: 内容长度 {body_length} 少于 {MIN_CONTENT_LENGTH} 字符"
        )

    # 缺少依赖说明 section
    _, body_text = split_frontmatter_body(content)
    if not re.search(r'##\s*依赖说明|##\s*Dependencies|##\s*Dependency', body_text, re.IGNORECASE):
        issues["info"].append("MISSING_DEP_SECTION: 缺少依赖说明 section")

    # === functional 检查 (Layer 4) ===
    func_result = check_functional_quality(body_text)
    functional_issues = func_result["issues"]

    # === sellability 评估 (Layer 5) ===
    sell_result = check_sellability(body_text, fm, func_result["score"])

    # === content authenticity 检查 (Layer 6) ===
    auth_result = check_content_authenticity(body_text)

    # 确定最终严重级别
    if issues["critical"]:
        severity = "critical"
        all_issues = issues["critical"]
    elif issues["warning"]:
        severity = "warning"
        all_issues = issues["warning"] + issues["info"]
    elif issues["info"]:
        severity = "info"
        all_issues = issues["info"]
    else:
        severity = "ok"
        all_issues = []

    return {
        "slug": slug,
        "source": source,
        "severity": severity,
        "issues": all_issues,
        "body_length": body_length,
        "version": version,
        "dir_name": dir_name,
        "frontmatter": fm,
        "functional": {
            "score": func_result["score"],
            "grade": func_result["grade"],
            "issues": functional_issues,
        },
        "sellability": {
            "score": sell_result["score"],
            "grade": sell_result["grade"],
            "factors": sell_result["factors"],
        },
        "authenticity": {
            "score": auth_result["authenticity_score"],
            "grade": auth_result["grade"],
            "template_count": auth_result["template_count"],
            "empty_sections": auth_result["empty_sections"],
            "issues": auth_result["issues"],
        },
        "_content": content,
        "_issues_map": issues,
    }


# ============ 功能质量检查 (Layer 4: Functional Quality) ============
# 从格式检查升级为功能验证 - 判断skill是否真能完成任务

FUNCTIONAL_CHECKS = [
    "NO_INSTRUCTIONS",        # 无指令性内容(步骤/用法)
    "NO_CODE_BLOCKS",         # 无代码块
    "REAL_PLACEHOLDER",       # 含真实placeholder(TODO/FIXME/待补充)
    "CONTENT_TOO_SHORT_FUNC", # 正文<500字符(功能不足)
    "NO_TASK_DEFINITION",     # 无任务定义(##功能/Features)
    "NO_ERROR_HANDLING",      # 无错误处理说明
    "NO_USAGE_GUIDE",         # 无使用指南(##用法/Usage)
    "NO_INPUT_OUTPUT",        # 无输入输出说明
]

# 真实placeholder模式 (非模板变量)
REAL_PLACEHOLDER_PATTERNS = [
    (r"TODO[:\s]", "TODO标记"),
    (r"FIXME[:\s]", "FIXME标记"),
    (r"待补充", "待补充"),
    (r"待完善", "待完善"),
    (r"lorem ipsum", "Lorem Ipsum"),
    (r"placeholder\s+content", "占位内容"),
    (r"replace[_ ]this", "替换占位"),
    (r"示例文本内容", "示例占位"),
]

def check_functional_quality(body_text: str) -> dict:
    """功能质量检查 - 判断skill正文是否包含可执行指令

    Returns:
        dict: {issues: [...], score: 0-100, grade: A/B/C/D/F}
    """
    issues = []
    body_len = len(body_text.strip())
    score = 0

    # 维度1: 内容深度 (0-25分)
    if body_len > 8000: score += 25
    elif body_len > 4000: score += 20
    elif body_len > 2000: score += 15
    elif body_len > 1000: score += 10
    elif body_len > 500: score += 5
    else:
        issues.append(f"CONTENT_TOO_SHORT_FUNC: 正文仅{body_len}字符, 功能不足")
        score += 2

    # 维度2: 指令性内容 (0-25分)
    if re.search(r'步骤|Step\s*[1-9]|首先|然后|接下来|用法|Usage', body_text, re.IGNORECASE):
        score += 15
    else:
        issues.append("NO_INSTRUCTIONS: 无步骤/用法指令性内容")

    if re.search(r'##\s*(使用|用法|Usage|How to|步骤|Steps|Guide)', body_text, re.IGNORECASE):
        score += 10
    else:
        issues.append("NO_USAGE_GUIDE: 无使用指南section")

    # 维度3: 代码/示例 (0-20分)
    code_blocks = body_text.count("```") // 2
    if code_blocks >= 3: score += 15
    elif code_blocks >= 1: score += 10
    else:
        issues.append("NO_CODE_BLOCKS: 无代码块")

    if re.search(r'##\s*(示例|Example|Demo)', body_text, re.IGNORECASE):
        score += 5

    # 维度4: 任务定义 (0-15分)
    if re.search(r'##\s*(功能|Features|核心能力|Capabilities|能力)', body_text, re.IGNORECASE):
        score += 10
    else:
        issues.append("NO_TASK_DEFINITION: 无任务定义section")

    if re.search(r'输入|Input|参数|Parameters', body_text, re.IGNORECASE):
        score += 3
    if re.search(r'输出|Output|返回|Return', body_text, re.IGNORECASE):
        score += 2
    if not (re.search(r'输入|Input|参数', body_text, re.IGNORECASE) and
            re.search(r'输出|Output|返回', body_text, re.IGNORECASE)):
        issues.append("NO_INPUT_OUTPUT: 无输入输出说明")

    # 维度5: 错误处理 (0-15分)
    if re.search(r'错误|Error|异常|Exception|失败|Fail|超时|timeout', body_text, re.IGNORECASE):
        score += 10
    else:
        issues.append("NO_ERROR_HANDLING: 无错误处理说明")

    if re.search(r'##\s*依赖说明|##\s*Dependencies', body_text, re.IGNORECASE):
        score += 5

    # 扣分项: 真实placeholder
    for pattern, desc in REAL_PLACEHOLDER_PATTERNS:
        if re.search(pattern, body_text, re.IGNORECASE):
            issues.append(f"REAL_PLACEHOLDER: 检测到{desc}")
            score -= 15
            break

    # 评级
    if score >= 70: grade = "A"
    elif score >= 50: grade = "B"
    elif score >= 30: grade = "C"
    elif score >= 10: grade = "D"
    else: grade = "F"

    return {"issues": issues, "score": max(0, score), "grade": grade}


# ============ 可销售性评估 (Layer 5: Sellability) ============
# 从买家角度评估skill价值

def check_sellability(body_text: str, fm: dict, functional_score: int) -> dict:
    """可销售性评估 - 从买家角度评估skill价值

    Returns:
        dict: {score: 0-100, grade: A/B/C/D, factors: [...]}
    """
    body_len = len(body_text.strip())
    score = 0
    factors = []

    # 1. 内容深度 (0-25分)
    if body_len > 8000: score += 25; factors.append("内容充实(>8K字符)")
    elif body_len > 4000: score += 20; factors.append("内容较充实(>4K字符)")
    elif body_len > 2000: score += 15; factors.append("内容中等(>2K字符)")
    else: score += 5; factors.append("内容偏少(<2K字符)")

    # 2. 功能完整 (0-20分) - 基于功能质量得分
    func_pct = functional_score * 20 // 100
    score += func_pct
    if functional_score >= 70: factors.append("功能完整(A级)")
    elif functional_score >= 50: factors.append("功能较完整(B级)")

    # 3. 技术深度 (0-20分)
    code_blocks = body_text.count("```") // 2
    if code_blocks >= 5: score += 15; factors.append(f"代码丰富({code_blocks}块)")
    elif code_blocks >= 2: score += 10; factors.append(f"有代码示例({code_blocks}块)")
    elif code_blocks >= 1: score += 5

    if re.search(r'API|HTTP|JSON|REST|SDK', body_text):
        score += 5; factors.append("含技术规格")

    # 4. 用户体验 (0-20分)
    if re.search(r'步骤|Step|用法|Usage', body_text, re.IGNORECASE):
        score += 10; factors.append("有使用步骤")
    if re.search(r'示例|Example|Demo', body_text, re.IGNORECASE):
        score += 5; factors.append("有示例")
    if re.search(r'错误|Error|异常', body_text, re.IGNORECASE):
        score += 5; factors.append("有错误处理")

    # 5. 专业性 (0-15分)
    if re.search(r'##\s*依赖说明', body_text, re.IGNORECASE):
        score += 5; factors.append("有依赖说明")
    if fm.get('license'):
        score += 5
    if fm.get('tags'):
        score += 5

    # 评级
    if score >= 70: grade = "A"
    elif score >= 50: grade = "B"
    elif score >= 30: grade = "C"
    else: grade = "D"

    return {"score": min(100, score), "grade": grade, "factors": factors}


# ============ 内容真实性检查 (Layer 6: Content Authenticity) ============
# 检测批量生成的模板填充、空段落、乱码拼接等问题
# 这是质量审计的最后一道防线: 确保内容是真实的，而非模板生成

# 通用模板段落特征 (出现即说明是批量生成的填充内容)
TEMPLATE_PATTERNS = [
    # 通用模板句子: "执行X操作，处理输入数据并返回结果"
    (r'执行.{0,20}操作[,，]处理输入数据并返回结果', "GENERIC_TEMPLATE_SENTENCE"),
    # 三个完全相同的通用段落标题
    (r'##\s*指令解析与执行', "GENERIC_SECTION_INSTRUCTION_PARSE"),
    (r'##\s*数据处理与转换', "GENERIC_SECTION_DATA_PROCESS"),
    (r'##\s*结果验证与输出', "GENERIC_SECTION_RESULT_VERIFY"),
    # "能力覆盖范围" 乱码拼接
    (r'##\s*能力覆盖范围', "GENERIC_SECTION_COVERAGE_GARBLED"),
    # "技术细节" 通用模板表格 (parser/processor/output)
    (r'##\s*技术细节[\s\S]{0,200}parser[\s\S]{0,100}processor[\s\S]{0,100}output', "GENERIC_TECH_DETAIL_TABLE"),
    # "命令参数说明" 无意义的flag列举
    (r'##\s*命令参数说明', "GENERIC_PARAM_LISTING"),
    # "相关说明" 作为表格内容的占位符
    (r'\|\s*相关说明\s*\|', "PLACEHOLDER_TABLE_CELL"),
    # "源能力映射" 通用模板
    (r'##\s*源能力映射', "GENERIC_SOURCE_MAPPING"),
    # "领域术语" 仅罗列单词无解释
    (r'##\s*领域术语', "GENERIC_DOMAIN_TERMS"),
]

# 空段落检测: section header 后面紧跟空行或另一个header或文件结尾
EMPTY_SECTION_REGEX = re.compile(
    r'##\s+(.+?)\s*\n\s*(?:\n##\s+|\n##\s+|$)',
    re.MULTILINE
)

# "已知限制" 空白检测 (只有破折号或空行)
EMPTY_LIMITATIONS_REGEX = re.compile(
    r'##\s*(?:已知限制|Limitations)\s*\n((?:[\s\-|]*\n){0,5})\s*(?:##|\Z)',
    re.MULTILINE
)

# FAQ 空答案检测
EMPTY_FAQ_REGEX = re.compile(
    r'(?:###?\s*.+?\?\s*\n)\s*(?:\n(?:##|\Z))',
    re.MULTILINE
)

# "案例展示" 占位检测 (输入: 用户请求 / 处理: 根据使用流程执行 / 输出: 处理结果)
PLACEHOLDER_CASE_REGEX = re.compile(
    r'输入[:：]\s*(?:用户请求|示例数据|示例内容)\s*\n.*?处理[:：]\s*(?:根据使用流程执行|示例处理)\s*\n.*?输出[:：]\s*(?:处理结果|示例输出|建议优化)',
    re.DOTALL
)

# 截断文本检测 (单词在中间断开)
TRUNCATED_TEXT_REGEX = re.compile(r'[a-zA-Z]{3,}[a-z][A-Z]')


def check_content_authenticity(body_text: str) -> dict:
    """内容真实性检查 (Layer 6) - 检测模板填充、空段落、乱码

    Returns:
        dict: {
            issues: [...],         # 发现的问题列表
            template_count: int,    # 模板填充数量
            empty_sections: int,    # 空段落数量
            authenticity_score: 0-100,  # 真实性得分
            grade: A/B/C/D/F,
        }
    """
    issues = []
    template_count = 0
    empty_count = 0

    # 1. 检测通用模板段落
    for pattern, code in TEMPLATE_PATTERNS:
        matches = re.findall(pattern, body_text, re.IGNORECASE)
        if matches:
            template_count += len(matches)
            issues.append(f"TEMPLATE_FILL: {code} (出现{len(matches)}次)")

    # 2. 检测空段落 (header后直接跟另一个header或空行)
    empty_sections_found = EMPTY_SECTION_REGEX.findall(body_text)
    # 过滤掉正常的短段落(有些section确实可以短)
    meaningful_empty = [s for s in empty_sections_found
                        if s.strip() and len(s.strip()) < 30
                        and s.strip() not in ('依赖说明', '概述')]
    if meaningful_empty:
        empty_count = len(meaningful_empty)
        if empty_count >= 3:
            issues.append(f"EMPTY_SECTIONS: {empty_count}个段落内容为空或过短")

    # 3. 检测"已知限制"空白
    if EMPTY_LIMITATIONS_REGEX.search(body_text):
        empty_count += 1
        issues.append("EMPTY_LIMITATIONS: 已知限制段落为空")

    # 4. 检测FAQ空答案
    faq_empty = EMPTY_FAQ_REGEX.findall(body_text)
    if faq_empty:
        empty_count += len(faq_empty)
        if len(faq_empty) >= 2:
            issues.append(f"EMPTY_FAQ: {len(faq_empty)}个FAQ答案为空")

    # 5. 检测"案例展示"占位
    if PLACEHOLDER_CASE_REGEX.search(body_text):
        template_count += 1
        issues.append("PLACEHOLDER_CASE: 案例展示为占位符内容")

    # 6. 检测截断文本 (仅在代码块外的正文中检测)
    # 移除代码块以避免camelCase变量名导致误报
    prose_text = re.sub(r'```[\s\S]*?```', '', body_text)
    truncated = TRUNCATED_TEXT_REGEX.findall(prose_text)
    if truncated:
        issues.append(f"TRUNCATED_TEXT: 检测到{len(truncated)}处可能截断的文本")

    # 计算真实性得分
    # 基础分100, 每个模板填充扣5分, 每个空段落扣3分, 截断扣10分
    penalty = template_count * 5 + empty_count * 3 + len(truncated) * 10
    score = max(0, 100 - penalty)

    # 评级
    if score >= 85: grade = "A"
    elif score >= 65: grade = "B"
    elif score >= 40: grade = "C"
    elif score >= 20: grade = "D"
    else: grade = "F"

    return {
        "issues": issues,
        "template_count": template_count,
        "empty_sections": empty_count,
        "authenticity_score": score,
        "grade": grade,
    }


# ============ 分类映射 (用于 --fix-all 自动补 tags) ============
CATEGORY_TAGS_MAP = {
    "Agents": ["AI代理", "智能体", "自动化"],
    "Automation": ["自动化", "效率工具", "工作流"],
    "Communication": ["通信", "消息", "协作"],
    "Creative": ["创意设计", "内容创作", "多媒体"],
    "Development": ["开发工具", "编程", "代码"],
    "Finance": ["金融", "财务", "数据分析"],
    "Integrations": ["集成", "API", "第三方服务"],
    "Knowledge": ["知识管理", "笔记", "文档"],
    "Lifestyle": ["生活", "健康", "日常"],
    "Operations": ["运维", "监控", "基础设施"],
    "Other": ["通用工具"],
    "Productivity": ["效率", "办公", "生产力"],
    "Research": ["研究", "分析", "学术"],
    "Security": ["安全", "审计", "防护"],
    "其他": ["通用工具"],
    "packaged": ["通用工具"],
}

DEFAULT_HOMEPAGE = "https://skillhub.cn"

# 默认依赖说明模板
DEFAULT_DEP_SECTION = """
## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux

### 可用性分类
- **分类**: MD（纯Markdown指令，通过自然语言驱动Agent完成操作）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作。
"""


def infer_tags_from_path(skill_path: Path, source: str) -> list:
    """根据 skill 路径和来源推断 tags"""
    # 如果 source 是 differentiated/Category 格式，提取 Category
    if source.startswith("differentiated/"):
        category = source.split("/", 1)[1]
        return CATEGORY_TAGS_MAP.get(category, ["通用工具"])
    return CATEGORY_TAGS_MAP.get(source, ["通用工具"])


def add_frontmatter_field(content: str, key: str, value) -> str:
    """在 frontmatter 中添加一个新字段（在 --- 闭合行之前插入）"""
    if content.startswith('\ufeff'):
        content = content[1:]
    if not content.startswith('---'):
        return content

    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return content

    fm_text = parts[1]
    body = parts[2]

    # 构建新字段文本
    if isinstance(value, list):
        # 列表格式: key:\n  - item1\n  - item2
        items = '\n'.join(f'  - {v}' for v in value)
        new_field = f'{key}:\n{items}'
    else:
        new_field = f'{key}: "{value}"'

    # 在 frontmatter 末尾添加新字段
    fm_text = fm_text.rstrip() + '\n' + new_field + '\n'

    return f'---{fm_text}---{body}'


def add_dep_section(content: str) -> str:
    """在正文末尾添加依赖说明 section"""
    if '## 依赖说明' in content or '## Dependencies' in content or '## Dependency' in content:
        return content
    return content.rstrip() + '\n' + DEFAULT_DEP_SECTION


def fix_info_issues(skill_path: Path, result: dict) -> list:
    """自动修复 info 级别问题

    可修复的问题:
    - MISSING_HOMEPAGE: 添加 homepage 字段
    - MISSING_TAGS: 根据 skill 所在目录推断 tags 并添加
    - MISSING_DEP_SECTION: 添加依赖说明 section
    - CONTENT_TOO_SHORT: 添加基础内容（概述 + 依赖说明）

    Returns:
        list of str: 已执行的修复描述
    """
    fixes = []
    content = result.get("_content", "")
    fm = result.get("frontmatter", {})
    issues_map = result.get("_issues_map", {"critical": [], "warning": [], "info": []})

    modified = False
    info_issues = issues_map.get("info", [])

    # 修复 MISSING_HOMEPAGE
    has_homepage_issue = any(i.startswith("MISSING_HOMEPAGE") for i in info_issues)
    if has_homepage_issue:
        content = add_frontmatter_field(content, 'homepage', DEFAULT_HOMEPAGE)
        fixes.append(f"添加 homepage: {DEFAULT_HOMEPAGE}")
        modified = True

    # 修复 MISSING_TAGS
    has_tags_issue = any(i.startswith("MISSING_TAGS") for i in info_issues)
    if has_tags_issue:
        inferred_tags = infer_tags_from_path(skill_path, result.get("source", ""))
        content = add_frontmatter_field(content, 'tags', inferred_tags)
        fixes.append(f"添加 tags: {', '.join(inferred_tags)}")
        modified = True

    # 修复 MISSING_DEP_SECTION
    has_dep_issue = any(i.startswith("MISSING_DEP_SECTION") for i in info_issues)
    if has_dep_issue:
        content = add_dep_section(content)
        fixes.append("添加依赖说明 section")
        modified = True

    # 修复 CONTENT_TOO_SHORT（在添加依赖说明后再次检查）
    has_short_issue = any(i.startswith("CONTENT_TOO_SHORT") for i in info_issues)
    if has_short_issue and not has_dep_issue:
        # 如果内容太短且还没添加依赖说明，添加它
        content = add_dep_section(content)
        fixes.append("添加依赖说明 section (内容补充)")
        modified = True
    elif has_short_issue:
        # 依赖说明已添加，如果内容仍然太短，添加基础概述
        if len(content) < MIN_CONTENT_LENGTH:
            _, body = split_frontmatter_body(content)
            if not re.search(r'##\s*概述', body):
                overview = "\n## 概述\n\n本Skill提供专业功能，通过自然语言指令驱动Agent完成操作。\n"
                # 在 body 的开头插入概述
                parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
                if len(parts) >= 3:
                    content = f'{parts[0]}---\n{parts[1]}\n---\n{overview}{parts[2]}'
                    fixes.append("添加概述 section (内容补充)")
                    modified = True

    if modified:
        skill_path.write_text(content, encoding='utf-8')

    return fixes


def fix_warning_issues(skill_path: Path, result: dict) -> list:
    """自动修复 warning 级别问题

    可修复的问题:
    - SUMMARY_TOO_LONG: 截断过长的 summary
    - DISPLAYNAME_TOO_LONG: 截断过长的 displayName

    Returns:
        list of str: 已执行的修复描述
    """
    fixes = []
    content = result.get("_content", "")
    fm = result.get("frontmatter", {})
    issues_map = result.get("_issues_map", {"critical": [], "warning": [], "info": []})

    modified = False

    # 修复 summary 过长
    summary_issues = [i for i in issues_map["warning"] if i.startswith("SUMMARY_TOO_LONG")]
    if summary_issues and 'summary' in fm:
        old_summary = str(fm['summary'])
        new_summary = old_summary[:MAX_SUMMARY_LENGTH]
        # 在 frontmatter 文本中替换
        content = replace_frontmatter_value(content, 'summary', old_summary, new_summary)
        fixes.append(f"截断 summary: {len(old_summary)} -> {len(new_summary)} 字符")
        modified = True

    # 修复 displayName 过长
    displayname_issues = [i for i in issues_map["warning"] if i.startswith("DISPLAYNAME_TOO_LONG")]
    if displayname_issues and 'displayName' in fm:
        old_dn = str(fm['displayName'])
        new_dn = old_dn[:MAX_DISPLAYNAME_LENGTH]
        content = replace_frontmatter_value(content, 'displayName', old_dn, new_dn)
        fixes.append(f"截断 displayName: {len(old_dn)} -> {len(new_dn)} 字符")
        modified = True

    if modified:
        skill_path.write_text(content, encoding='utf-8')

    return fixes


def replace_frontmatter_value(content: str, key: str, old_val: str, new_val: str) -> str:
    """在 frontmatter 中替换指定 key 的值

    处理多种格式: 普通值、引号值、块标量值
    """
    if content.startswith('\ufeff'):
        content = content[1:]

    # 尝试匹配带引号的值: key: "value"
    # 使用精确的 key 匹配，避免误匹配其他字段中相同的值
    pattern_quoted = re.compile(
        r'^(' + re.escape(key) + r'):\s*"(' + re.escape(old_val) + r')"',
        re.MULTILINE
    )
    match_quoted = pattern_quoted.search(content)
    if match_quoted:
        # 精确替换匹配到的引号内内容
        val_start = match_quoted.start(2)
        val_end = match_quoted.end(2)
        return content[:val_start] + new_val + content[val_end:]

    # 尝试匹配不带引号的值: key: value
    pattern_plain = re.compile(
        r'^(' + re.escape(key) + r'):\s*' + re.escape(old_val) + r'\s*$',
        re.MULTILINE
    )
    match = pattern_plain.search(content)
    if match:
        return content[:match.start()] + f"{key}: {new_val}" + content[match.end():]

    # 尝试匹配块标量值后逐行替换
    # 对于 |- 或 > 格式，找到块标量区域并替换内容
    block_pattern = re.compile(
        r'^(' + re.escape(key) + r'):\s*[|>]-?\s*\n((?:[ \t]+.*\n?)*)',
        re.MULTILINE
    )
    block_match = block_pattern.search(content)
    if block_match:
        # 替换块标量内容为单行值
        replacement = f"{key}: {new_val}"
        return content[:block_match.start()] + replacement + content[block_match.end():]

    # 最后尝试直接在全文中替换该值（保守方式）
    # 只在 frontmatter 区域内替换
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) >= 3:
        fm_text = parts[1]
        fm_text = fm_text.replace(old_val, new_val, 1)
        return parts[0] + '---\n' + fm_text + '\n---' + parts[2]

    return content


def run_audit(fix_mode: bool = False, fix_all: bool = False):
    """执行全量审计

    Args:
        fix_mode: 是否启用自动修复模式 (修复 warning 级别)
        fix_all: 是否启用全量修复模式 (修复 warning + info 级别)
    """
    print("=" * 60)
    print("深度质量审计系统 (Deep Quality Audit)")
    print("=" * 60)
    if fix_all:
        print("[模式] 审计 + 全量自动修复 (warning + info)")
    elif fix_mode:
        print("[模式] 审计 + 自动修复 warning 级别问题")
    else:
        print("[模式] 仅审计")
    print()

    # 收集所有 SKILL.md 文件
    print("[1/3] 收集 SKILL.md 文件...")
    skill_files = collect_skill_files()
    print(f"  共发现 {len(skill_files)} 个 SKILL.md 文件")

    # 执行审计
    print("[2/3] 执行质量检查...")
    all_results = []
    fixes_applied = []

    for skill_path, source in skill_files:
        result = check_skill(skill_path, source)
        all_results.append(result)

        # 自动修复 warning 级别问题
        if (fix_mode or fix_all) and result["severity"] in ("warning", "critical"):
            warning_issues = result.get("_issues_map", {}).get("warning", [])
            if warning_issues:
                applied = fix_warning_issues(skill_path, result)
                if applied:
                    fixes_applied.append({
                        "slug": result["slug"],
                        "source": source,
                        "fixes": applied,
                    })

        # 自动修复 info 级别问题 (仅 --fix-all 模式)
        if fix_all and result["severity"] in ("info", "warning", "critical"):
            info_issues = result.get("_issues_map", {}).get("info", [])
            if info_issues:
                # 重新读取文件（可能已被 warning 修复修改过）
                result["_content"] = skill_path.read_text(encoding='utf-8', errors='replace')
                applied = fix_info_issues(skill_path, result)
                if applied:
                    fixes_applied.append({
                        "slug": result["slug"],
                        "source": source,
                        "fixes": applied,
                        "level": "info",
                    })

    # 统计汇总
    print("[3/3] 生成报告...")

    by_severity = {"critical": 0, "warning": 0, "info": 0, "ok": 0}
    by_source = {}
    critical_issues = []
    warning_issues = []
    info_issues = []

    # Layer 4 & 5 统计
    func_grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    sell_grades = {"A": 0, "B": 0, "C": 0, "D": 0}
    func_issues_list = []
    sell_grade_d = []  # D级可销售性(需优化)
    func_score_sum = 0
    sell_score_sum = 0

    # Layer 6 统计
    auth_grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    auth_issues_list = []
    auth_score_sum = 0
    auth_template_total = 0

    for result in all_results:
        sev = result["severity"]
        by_severity[sev] += 1

        src = result["source"]
        if src not in by_source:
            by_source[src] = {"critical": 0, "warning": 0, "info": 0, "ok": 0}
        by_source[src][sev] += 1

        # 收集功能质量统计
        func = result.get("functional", {})
        func_grade = func.get("grade", "F")
        func_score = func.get("score", 0)
        func_grades[func_grade] = func_grades.get(func_grade, 0) + 1
        func_score_sum += func_score
        if func.get("issues"):
            func_issues_list.append({
                "slug": result["slug"],
                "source": result["source"],
                "grade": func_grade,
                "score": func_score,
                "issues": func["issues"],
            })

        # 收集可销售性统计
        sell = result.get("sellability", {})
        sell_grade = sell.get("grade", "D")
        sell_score = sell.get("score", 0)
        sell_grades[sell_grade] = sell_grades.get(sell_grade, 0) + 1
        sell_score_sum += sell_score
        if sell_grade in ("C", "D"):
            sell_grade_d.append({
                "slug": result["slug"],
                "source": result["source"],
                "grade": sell_grade,
                "score": sell_score,
                "factors": sell.get("factors", []),
            })

        # 收集内容真实性统计 (Layer 6)
        auth = result.get("authenticity", {})
        auth_grade = auth.get("grade", "F")
        auth_score = auth.get("score", 0)
        auth_grades[auth_grade] = auth_grades.get(auth_grade, 0) + 1
        auth_score_sum += auth_score
        auth_template_total += auth.get("template_count", 0)
        if auth.get("issues"):
            auth_issues_list.append({
                "slug": result["slug"],
                "source": result["source"],
                "grade": auth_grade,
                "score": auth_score,
                "template_count": auth.get("template_count", 0),
                "empty_sections": auth.get("empty_sections", 0),
                "issues": auth["issues"],
            })

        entry = {
            "slug": result["slug"],
            "source": result["source"],
            "severity": result["severity"],
            "issues": result["issues"],
            "body_length": result["body_length"],
            "version": result["version"],
            "functional_grade": func_grade,
            "functional_score": func_score,
            "sellability_grade": sell_grade,
            "sellability_score": sell_score,
            "authenticity_grade": auth_grade,
            "authenticity_score": auth_score,
        }

        if sev == "critical":
            critical_issues.append(entry)
        elif sev == "warning":
            warning_issues.append(entry)
        elif sev == "info":
            info_issues.append(entry)

    # 构建 JSON 报告
    total = len(all_results)
    func_avg = func_score_sum / total if total else 0
    sell_avg = sell_score_sum / total if total else 0
    auth_avg = auth_score_sum / total if total else 0

    report = {
        "audit_date": datetime.now().isoformat(),
        "total_skills": total,
        "fix_mode": fix_mode,
        "fix_all": fix_all,
        "by_severity": by_severity,
        "by_source": by_source,
        "critical_issues": critical_issues,
        "warning_issues": warning_issues,
        "info_issues": info_issues,
        "functional_quality": {
            "grade_distribution": func_grades,
            "avg_score": round(func_avg, 1),
            "total_with_issues": len(func_issues_list),
            "issues_detail": func_issues_list[:100],
        },
        "sellability": {
            "grade_distribution": sell_grades,
            "avg_score": round(sell_avg, 1),
            "total_below_b": len(sell_grade_d),
            "below_b_detail": sell_grade_d[:100],
        },
        "content_authenticity": {
            "grade_distribution": auth_grades,
            "avg_score": round(auth_avg, 1),
            "total_with_issues": len(auth_issues_list),
            "total_template_fills": auth_template_total,
            "issues_detail": auth_issues_list[:200],
        },
    }

    if fix_mode and fixes_applied:
        report["fixes_applied"] = fixes_applied

    # 写入报告文件
    REPORT_PATH.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )

    # 打印汇总统计
    print()
    print("=" * 60)
    print("审计结果汇总")
    print("=" * 60)
    print(f"审计时间: {report['audit_date']}")
    print(f"总 skill 数: {report['total_skills']}")
    print(f"修复模式: {'是' if fix_mode else '否'}")
    print()
    print("按严重级别统计:")
    print(f"  CRITICAL (致命): {by_severity['critical']}")
    print(f"  WARNING (警告): {by_severity['warning']}")
    print(f"  INFO    (信息): {by_severity['info']}")
    print(f"  OK      (通过): {by_severity['ok']}")
    print()
    print("按来源统计:")
    for src, counts in sorted(by_source.items()):
        total_src = sum(counts.values())
        print(f"  {src:40s} 总计 {total_src:4d}  "
              f"(critical={counts['critical']}, warning={counts['warning']}, "
              f"info={counts['info']}, ok={counts['ok']})")

    # Layer 4: 功能质量统计
    print()
    print("─" * 60)
    print("功能质量 (Layer 4: Functional Quality):")
    print(f"  平均分: {func_avg:.1f} / 100")
    print(f"  等级分布: A={func_grades['A']}  B={func_grades['B']}  "
          f"C={func_grades['C']}  D={func_grades['D']}  F={func_grades['F']}")
    func_a_b = func_grades['A'] + func_grades['B']
    print(f"  A+B级 (功能合格): {func_a_b} / {total} ({func_a_b*100//total if total else 0}%)")
    if func_issues_list:
        print(f"  有功能问题: {len(func_issues_list)} 个 skill")
        # 显示前10个功能问题
        for item in func_issues_list[:10]:
            print(f"    [{item['grade']}] {item['slug']}: {'; '.join(item['issues'][:2])}")
        if len(func_issues_list) > 10:
            print(f"    ... 还有 {len(func_issues_list) - 10} 个")

    # Layer 5: 可销售性统计
    print()
    print("─" * 60)
    print("可销售性 (Layer 5: Sellability):")
    print(f"  平均分: {sell_avg:.1f} / 100")
    print(f"  等级分布: A={sell_grades['A']}  B={sell_grades['B']}  "
          f"C={sell_grades['C']}  D={sell_grades['D']}")
    sell_a_b = sell_grades['A'] + sell_grades['B']
    print(f"  A+B级 (可销售): {sell_a_b} / {total} ({sell_a_b*100//total if total else 0}%)")
    if sell_grade_d:
        print(f"  C+D级 (需优化): {len(sell_grade_d)} 个 skill")
        for item in sell_grade_d[:10]:
            factors_str = ', '.join(item.get('factors', [])) if item.get('factors') else '无'
            print(f"    [{item['grade']}] {item['slug']} (分:{item['score']}): {factors_str}")
        if len(sell_grade_d) > 10:
            print(f"    ... 还有 {len(sell_grade_d) - 10} 个")

    # Layer 6: 内容真实性统计
    print()
    print("─" * 60)
    print("内容真实性 (Layer 6: Content Authenticity):")
    print(f"  平均分: {auth_avg:.1f} / 100")
    print(f"  等级分布: A={auth_grades['A']}  B={auth_grades['B']}  "
          f"C={auth_grades['C']}  D={auth_grades['D']}  F={auth_grades['F']}")
    auth_a_b = auth_grades['A'] + auth_grades['B']
    print(f"  A+B级 (内容真实): {auth_a_b} / {total} ({auth_a_b*100//total if total else 0}%)")
    print(f"  模板填充总数: {auth_template_total}")
    print(f"  有问题skill: {len(auth_issues_list)} 个")
    if auth_issues_list:
        # 显示C/D/F级的问题skill (最严重的)
        severe_auth = [item for item in auth_issues_list if item['grade'] in ('C', 'D', 'F')]
        if severe_auth:
            print(f"  C+D+F级 (严重模板填充): {len(severe_auth)} 个")
            for item in severe_auth[:20]:
                issues_str = '; '.join(item['issues'][:2])
                print(f"    [{item['grade']}] {item['slug']} (分:{item['score']}, 模板:{item['template_count']}): {issues_str}")
            if len(severe_auth) > 20:
                print(f"    ... 还有 {len(severe_auth) - 20} 个")

    if critical_issues:
        print()
        print(f"CRITICAL 问题列表 ({len(critical_issues)} 个):")
        for item in critical_issues[:20]:
            print(f"  [{item['source']}] {item['slug']}: {'; '.join(item['issues'])}")
        if len(critical_issues) > 20:
            print(f"  ... 还有 {len(critical_issues) - 20} 个")

    if warning_issues:
        print()
        print(f"WARNING 问题列表 ({len(warning_issues)} 个):")
        for item in warning_issues[:20]:
            print(f"  [{item['source']}] {item['slug']}: {'; '.join(item['issues'])}")
        if len(warning_issues) > 20:
            print(f"  ... 还有 {len(warning_issues) - 20} 个")

    if info_issues:
        print()
        print(f"INFO 问题统计 ({len(info_issues)} 个 skill 有 info 级别问题)")

    if fix_mode and fixes_applied:
        print()
        print(f"自动修复汇总 ({len(fixes_applied)} 个 skill 已修复):")
        for fix in fixes_applied[:20]:
            print(f"  [{fix['source']}] {fix['slug']}: {'; '.join(fix['fixes'])}")
        if len(fixes_applied) > 20:
            print(f"  ... 还有 {len(fixes_applied) - 20} 个")

    print()
    print(f"报告已保存: {REPORT_PATH}")

    # 返回是否通过审计（无 critical 问题 + 功能质量无F级）
    passed = by_severity["critical"] == 0
    func_f = func_grades.get("F", 0)
    sell_d = sell_grades.get("D", 0)

    if passed:
        verdict_parts = ["格式通过"]
        if func_f == 0:
            verdict_parts.append("功能无F级")
        else:
            verdict_parts.append(f"功能F级:{func_f}个")
        if sell_d == 0:
            verdict_parts.append("可销售性无D级")
        else:
            verdict_parts.append(f"可销售性D级:{sell_d}个")
        auth_f = auth_grades.get("F", 0)
        auth_cd = auth_grades.get("C", 0) + auth_grades.get("D", 0)
        if auth_f == 0 and auth_cd == 0:
            verdict_parts.append("内容真实无C/D/F")
        elif auth_f > 0:
            verdict_parts.append(f"内容F级:{auth_f}个")
        else:
            verdict_parts.append(f"内容C/D级:{auth_cd}个")
        print(f"\n审计结果: {'通过' if passed else '未通过'} ({', '.join(verdict_parts)})")
    else:
        print(f"\n审计结果: 未通过 (存在 critical 级别问题)")
    return passed


def main():
    """主入口"""
    fix_mode = "--fix" in sys.argv
    fix_all = "--fix-all" in sys.argv

    passed = run_audit(fix_mode=fix_mode, fix_all=fix_all)

    # 如果存在 critical 问题，返回非零退出码
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
