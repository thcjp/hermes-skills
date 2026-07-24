#!/usr/bin/env python3
"""
深度质量审计系统 (Deep Quality Audit) v3.0
==========================================
全量扫描 packaged-skills/skillhub 和 differentiated-skills 下所有 SKILL.md 文件，
执行八层质量检查:

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

Layer 8 (安全审计 Security Audit):
  - EXTERNAL_URL: 外部商业URL或第三方API端点
  - INJECTED_MARKETING_TEXT: 注入的无关营销模板文本
  - API_KEY_EXPOSURE: API密钥格式和Authorization头模式
  - SLUG_CONTENT_MISMATCH: slug与内容不匹配
  - DUPLICATE_YAML_FIELDS: frontmatter重复字段
  - TAG_MISMATCH: tags与内容不匹配
  - GARBLED_TEXT: 乱码/编码错误文本
  - DEPENDENCY_CONTRADICTION: 依赖说明与已知限制矛盾
  评级: A(90+) / B(70+) / C(50+) / D(30+) / F(<30)

使用方式:
    python deep_quality_audit.py              # 执行审计
    python deep_quality_audit.py --fix        # 审计并自动修复 warning 级别问题
    python deep_quality_audit.py --fix-all    # 审计并自动修复 warning + info 级别问题
    python deep_quality_audit.py --no-layer8  # 关闭L8安全审计

输出:
    - JSON 报告: deep_quality_audit_report.json
    - 控制台汇总统计 (含功能质量+可销售性)
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===


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
# DIFFERENTIATED_DIR imported from config
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
        elif line.startswith('- ') and current_key:
            val = line[2:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
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


def check_skill(skill_path: Path, source: str, enable_l7: bool = True, enable_l7b: bool = True, enable_l8: bool = True):
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

    # === semantic 检查 (Layer 7a) ===
    l7_result = check_semantic_quality(body_text, enable_l7a=enable_l7)

    # === LLM 可执行性检查 (Layer 7b) ===
    l7b_result = check_llm_executability(body_text, skill_slug=slug, enable_l7b=enable_l7b, skill_path=skill_path)

    # === 安全审计 (Layer 8) ===
    if enable_l8:
        fm_text_raw, _ = split_frontmatter_body(content)
        l8_result = check_security_quality(
            content=content, fm=fm, fm_text=fm_text_raw,
            body_text=body_text, slug=slug, dir_name=dir_name
        )
    else:
        l8_result = {
            "issues": [], "score": -1, "grade": "N/A",
            "passed": False, "category_counts": {},
        }

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
        "semantic": {
            "l7a_available": l7_result["l7a_available"],
            "l7a_score": l7_result["l7a_score"],
            "l7a_grade": l7_result["l7a_grade"],
            "template_block_count": l7_result["template_block_count"],
            "template_blocks": l7_result["template_blocks"][:10],
            "similarity_scores": l7_result["similarity_scores"][:20],
            "issues": l7_result["issues"],
            "model_error": l7_result["model_error"],
        },
        "executability": {
            "l7b_enabled": l7b_result["l7b_enabled"],
            "l7b_score": l7b_result["l7b_score"],
            "l7b_grade": l7b_result["l7b_grade"],
            "executable": l7b_result["executable"],
            "checks_passed": l7b_result["checks_passed"],
            "checks_failed": l7b_result["checks_failed"],
            "issues": l7b_result["issues"],
        },
        "security": {
            "l8_enabled": enable_l8,
            "l8_score": l8_result["score"],
            "l8_grade": l8_result["grade"],
            "l8_passed": l8_result["passed"],
            "category_counts": l8_result["category_counts"],
            "issues": l8_result["issues"],
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
# TODO/FIXME仅在行首(可带注释符号)匹配，避免误报函数名/状态名/命令中的"todo"
REAL_PLACEHOLDER_PATTERNS = [
    (r"(?m)^[\s/#*;]*TODO[:\s]", "TODO标记"),
    (r"(?m)^[\s/#*;]*FIXME[:\s]", "FIXME标记"),
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
    # 指令性内容包括: 步骤关键词、序号列表、输入/处理/输出模式、操作动词
    if re.search(
        r'步骤|Step\s*[1-9]|首先|然后|接下来|用法|Usage'
        r'|输入|处理|输出'           # 输入/处理/输出指令模式
        r'|安装|配置|运行|执行|部署'   # 操作动词
        r'|Install|Run|Execute|Config|Deploy|Setup',  # 英文操作动词
        body_text, re.IGNORECASE
    ):
        score += 15
    else:
        issues.append("NO_INSTRUCTIONS: 无步骤/用法指令性内容")

    # 使用指南section: 扩大匹配范围，涵盖功能说明/核心能力/快速开始/入门等常见section
    if re.search(
        r'##\s*(使用|用法|Usage|How to|步骤|Steps|Guide'
        r'|快速开始|快速上手|入门|操作|功能|核心能力|核心功能|功能说明'
        r'|Capabilities|Overview|Quick Start|Getting Started'
        r'|Introduction|简介|说明)',
        body_text, re.IGNORECASE
    ):
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
    if re.search(r'##\s*(功能|Features|核心能力|Capabilities|能力|任务定义)', body_text, re.IGNORECASE):
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

    # 扣分项: 真实placeholder (TODO/FIXME大小写敏感，待补充等中文不敏感)
    for pattern, desc in REAL_PLACEHOLDER_PATTERNS:
        if re.search(pattern, body_text):
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
# 注意: ## header 后面跟 ### sub-header 是正常结构，不算空段落
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

# 截断文本检测 (单词在中间断开 - camelCase在非代码上下文)
# 需要排除: 代码块(```...```), 行内代码(`...`), URL(http/https), 文件路径
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
    # 改进: 排除 ## 后面跟 ### 子标题的正常结构
    # 只有当 ## header 后面直接跟另一个 ## header (同级) 且中间没有内容时才算空
    empty_sections_found = EMPTY_SECTION_REGEX.findall(body_text)
    # 过滤: 只保留真正空的段落 (标题文字<30字符 且 后面确实无内容)
    # 排除有 ### 子标题的段落、排除正常的短标题段落
    meaningful_empty = []
    for sec_title in empty_sections_found:
        title = sec_title.strip()
        if not title or len(title) >= 30:
            continue
        if title in ('依赖说明', '概述', '简介', 'Introduction', 'Overview'):
            continue
        # 检查这个 ## 标题后面是否有 ### 子标题
        # 如果有子标题，说明这个section有内容(通过子标题体现)，不算空
        pattern = re.compile(
            r'##\s+' + re.escape(title) + r'\s*\n(.*?)(?=\n##\s+|\Z)',
            re.DOTALL
        )
        match = pattern.search(body_text)
        if match:
            section_content = match.group(1).strip()
            # 有 ### 子标题或有实际内容(>20字符非空行)则不算空
            has_subsection = bool(re.search(r'^###\s+', section_content, re.MULTILINE))
            has_content = len(section_content) > 20
            if not has_subsection and not has_content:
                meaningful_empty.append(title)
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
    # 移除代码块(```...```), 行内代码(`...`), URL, 文件路径
    prose_text = re.sub(r'```[\s\S]*?```', '', body_text)  # 代码块
    prose_text = re.sub(r'`[^`]+`', '', prose_text)  # 行内代码
    prose_text = re.sub(r'https?://[^\s)]+', '', prose_text)  # URL
    prose_text = re.sub(r'[a-zA-Z]:\\[^\s]+', '', prose_text)  # Windows路径
    prose_text = re.sub(r'/[a-zA-Z][^\s)]*', '', prose_text)  # Unix路径
    truncated = TRUNCATED_TEXT_REGEX.findall(prose_text)
    # 仅当截断检测命中50+次时才报告 (技术术语camelCase会产生大量误报)
    if len(truncated) >= 50:
        issues.append(f"TRUNCATED_TEXT: 检测到{len(truncated)}处可能截断的文本")

    # 计算真实性得分
    # 基础分100, 每个模板填充扣5分, 每个空段落扣3分, 截断扣10分(仅当>=50才扣分)
    truncated_penalty = len(truncated) * 10 if len(truncated) >= 50 else 0
    penalty = template_count * 5 + empty_count * 3 + truncated_penalty
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


# ============ 语义审计 (Layer 7: Semantic Audit) ============
# L7a: TF-IDF 语义模板检测 - 使用 scikit-learn TF-IDF 向量化文本块,
# 与已知模板模式进行余弦相似度比较,检测 regex (Layer 6) 无法覆盖的语义级模板填充
# 设计支持两种后端: sklearn TF-IDF (默认,轻量) 和 sentence-transformers (可选,深度语义)
# L7b: LLM 深度审查 (预留接口, 未来实现)

# 已知模板填充模式的代表性文本 (用于语义比较)
_TEMPLATE_PATTERNS = [
    "按照skill规范执行操作",
    "用户提供所需的参数和指令",
    "返回操作结果,包含操作状态和输出数据",
    "验证执行结果,确认输出符合预期格式",
    "参考相关配置参数进行设置",
    "执行ping命令测试网络连通性,检查防火墙和代理设置",
    "本技能不做以下内容",
    "需要人工判断的复杂决策场景",
    "确认运行环境满足依赖说明中的要求",
    "根据适用场景选择合适的使用方式",
    "如遇错误,参考错误处理章节",
    "基础使用 用户请求 处理结果",
    "相关说明, 默认: 全部维度",
    "审查严格度, 可选: strict/normal/loose, 默认: normal",
]

# 向量化模型缓存
_vectorizer = None
_model_loaded = False
_model_load_error = None


def _load_embedding_model():
    """加载文本向量化模型 (懒加载)

    优先使用 sentence-transformers (深度语义), 降级到 sklearn TF-IDF (轻量词频)
    """
    global _vectorizer, _model_loaded, _model_load_error
    if _model_loaded:
        return _vectorizer, _model_load_error
    _model_loaded = True
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine
        # 使用 sklearn TF-IDF 向量化器 (支持中文字符级 n-gram)
        _vectorizer = {
            "type": "sklearn_tfidf",
            "model": TfidfVectorizer(
                analyzer='char_wb',
                ngram_range=(2, 5),
                max_features=5000,
                sublinear_tf=True,
            ),
            "cosine_fn": sklearn_cosine,
        }
    except ImportError:
        _model_load_error = "scikit-learn not installed (pip install scikit-learn)"
    except Exception as e:
        _model_load_error = f"model load error: {e}"
    return _vectorizer, _model_load_error


def _extract_semantic_blocks(body_text: str, max_blocks: int = 20) -> list:
    """从SKILL.md正文中提取语义块(段落/表格行/列表项)用于嵌入比较"""
    blocks = []
    # 按双换行分段
    paragraphs = re.split(r'\n\s*\n', body_text)
    for para in paragraphs:
        para = para.strip()
        if not para or len(para) < 10:
            continue
        # 跳过代码块
        if para.startswith('```'):
            continue
        # 跳过纯表格分隔符行
        if re.match(r'^[\|:\-\s]+$', para):
            continue
        # 提取表格行作为单独块
        table_rows = [line.strip() for line in para.split('\n') if line.strip().startswith('|')]
        if table_rows:
            for row in table_rows:
                # 去掉表格格式符,只保留文本
                text = re.sub(r'\|', ' ', row).strip()
                if len(text) > 5:
                    blocks.append(text[:200])  # 截断防止过长
        else:
            blocks.append(para[:200])

    return blocks[:max_blocks]


def _cosine_similarity(vec1, vec2):
    """计算两个向量的余弦相似度"""
    import math
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


def check_semantic_quality(body_text: str, enable_l7a: bool = True) -> dict:
    """Layer 7: 语义审计

    L7a: 嵌入向量模板检测
    - 提取正文语义块,计算嵌入向量
    - 与已知模板模式比较余弦相似度
    - 相似度 > 0.85 的块标记为疑似模板填充

    Returns:
        dict: {
            l7a_available: bool,     # 模型是否可用
            l7a_score: int,          # 0-100, 越高越好
            l7a_grade: str,          # A/B/C/D/F
            template_blocks: list,   # 疑似模板块列表
            template_block_count: int,
            similarity_scores: list, # 各块的最高相似度
            issues: list,            # 问题描述
            model_error: str,        # 模型加载错误(如有)
        }
    """
    result = {
        "l7a_available": False,
        "l7a_score": 100,
        "l7a_grade": "A",
        "template_blocks": [],
        "template_block_count": 0,
        "similarity_scores": [],
        "issues": [],
        "model_error": None,
    }

    if not enable_l7a:
        result["issues"].append("L7A_DISABLED: Layer 7a 未启用")
        return result

    # 加载模型
    model, error = _load_embedding_model()
    if error:
        result["model_error"] = error
        result["issues"].append(f"L7A_MODEL_UNAVAILABLE: {error}")
        # 模型不可用时给中性分数,不惩罚skill
        result["l7a_score"] = -1
        result["l7a_grade"] = "N/A"
        return result

    result["l7a_available"] = True

    # 提取语义块
    blocks = _extract_semantic_blocks(body_text)
    if not blocks:
        result["issues"].append("L7A_NO_BLOCKS: 无法提取语义块,内容可能过短")
        result["l7a_score"] = 50
        result["l7a_grade"] = "C"
        return result

    # 使用 TF-IDF 向量化文本块和模板模式
    import numpy as np
    from scipy.sparse import vstack

    vectorizer = model["model"]
    cosine_fn = model["cosine_fn"]

    # 合并模板模式和文本块进行 fit_transform,确保特征空间一致
    all_texts = _TEMPLATE_PATTERNS + blocks
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # 模板模式向量 (前 len(_TEMPLATE_PATTERNS) 行)
    template_matrix = tfidf_matrix[:len(_TEMPLATE_PATTERNS)]
    # 文本块向量 (后 len(blocks) 行)
    block_matrix = tfidf_matrix[len(_TEMPLATE_PATTERNS):]

    # 计算每个块与所有模板模式的余弦相似度
    sim_matrix = cosine_fn(block_matrix, template_matrix)

    # 对每个块,找出与模板模式的最高相似度
    template_blocks = []
    similarity_scores = []

    for i in range(sim_matrix.shape[0]):
        sim_row = sim_matrix[i]
        max_sim = float(sim_row.max())
        best_pattern_idx = int(sim_row.argmax())

        similarity_scores.append(round(max_sim, 3))

        # 相似度 > 0.85 标记为疑似模板填充
        if max_sim > 0.85:
            template_blocks.append({
                "block_text": blocks[i][:100],
                "similarity": round(float(max_sim), 3),
                "matched_pattern": _TEMPLATE_PATTERNS[best_pattern_idx][:60],
            })

    result["template_blocks"] = template_blocks
    result["template_block_count"] = len(template_blocks)
    result["similarity_scores"] = similarity_scores

    # 评分: 模板块占比越低越好
    template_ratio = len(template_blocks) / len(blocks) if blocks else 0
    if template_ratio == 0:
        result["l7a_score"] = 100
        result["l7a_grade"] = "A"
    elif template_ratio < 0.1:
        result["l7a_score"] = 85
        result["l7a_grade"] = "B"
    elif template_ratio < 0.2:
        result["l7a_score"] = 65
        result["l7a_grade"] = "C"
    elif template_ratio < 0.4:
        result["l7a_score"] = 40
        result["l7a_grade"] = "D"
    else:
        result["l7a_score"] = 15
        result["l7a_grade"] = "F"

    if template_blocks:
        result["issues"].append(
            f"L7A_TEMPLATE_DETECTED: 检测到 {len(template_blocks)} 个疑似模板填充块 "
            f"(占比 {template_ratio*100:.1f}%), 最高相似度 {max(s[1] for s in [(b['block_text'], b['similarity']) for b in template_blocks]):.3f}"
        )

    # 检测高重复块 (语义块之间的相似度,使用 TF-IDF 矩阵)
    if len(blocks) > 3:
        block_sim_matrix = cosine_fn(block_matrix)
        duplicate_count = 0
        for i in range(block_sim_matrix.shape[0]):
            for j in range(i + 1, block_sim_matrix.shape[0]):
                sim = float(block_sim_matrix[i, j])
                if sim > 0.92:
                    # 跳过表格分隔符行(------ ------ 等)造成的假重复
                    # 这些是Markdown表格结构,不是内容重复
                    if re.match(r'^[\-:\s]+$', blocks[i]) and re.match(r'^[\-:\s]+$', blocks[j]):
                        continue
                    duplicate_count += 1
        if duplicate_count > 0:
            result["issues"].append(
                f"L7A_DUPLICATE_BLOCKS: 检测到 {duplicate_count} 对高度相似的内容块 "
                f"(相似度 > 0.92), 可能存在内容重复"
            )
            # 重复内容降低评分
            result["l7a_score"] = max(0, result["l7a_score"] - 15)
            if result["l7a_score"] < 65 and result["l7a_grade"] == "A":
                result["l7a_grade"] = "B"

    return result


# ============ Layer 7b: LLM 深度审查 (可执行性验证) ============
# L7b: 使用 LLM 模拟执行 skill 任务,检测"声称能做但实际无法完成"的问题
# 接口设计: 接收 skill 正文文本,返回可执行性评估结果

def check_llm_executability(body_text: str, skill_slug: str = "", enable_l7b: bool = True, skill_path: Path = None) -> dict:
    """Layer 7b: LLM 深度审查 - 可执行性验证

    分析 SKILL.md 正文,检测以下问题:
    - L7B_NO_CODE: 声称有脚本但实际无代码块
    - L7B_BROKEN_REF: 引用了不存在的脚本/文件
    - L7B_VAGUE_TASK: 任务描述过于模糊,无法执行
    - L7B_MISSING_INPUT: 缺少必要的输入参数说明
    - L7B_NO_OUTPUT: 缺少输出格式说明
    - L7BContradiction: 内容自相矛盾

    Args:
        body_text: SKILL.md 正文 (不含 frontmatter)
        skill_slug: skill 的 slug (用于日志)
        enable_l7b: 是否启用 L7b (默认启用,可通过 --no-layer7b 关闭)
        skill_path: SKILL.md 文件路径或 skill 目录路径 (用于检查脚本引用是否存在,
                    为 None 时跳过文件存在性检查)

    Returns:
        dict: {
            l7b_enabled: bool,
            l7b_score: int,          # 0-100
            l7b_grade: str,          # A/B/C/D/F/N/A
            issues: list,            # 问题描述
            checks_passed: int,
            checks_failed: int,
            executable: bool,        # 是否可执行
        }
    """
    result = {
        "l7b_enabled": enable_l7b,
        "l7b_score": 100,
        "l7b_grade": "A",
        "issues": [],
        "checks_passed": 0,
        "checks_failed": 0,
        "executable": True,
    }

    if not enable_l7b:
        result["l7b_score"] = -1
        result["l7b_grade"] = "N/A"
        return result

    # === 静态可执行性检查 (不依赖 LLM,基于规则) ===

    # 检查1: 是否有代码块
    code_blocks = re.findall(r'```(\w+)?', body_text)
    has_code = len(code_blocks) > 0
    if has_code:
        result["checks_passed"] += 1
    else:
        # 没有代码块但声称有脚本
        if re.search(r'scripts?/', body_text) or re.search(r'执行.*脚本', body_text):
            result["issues"].append("L7B_NO_CODE: 声称有脚本但正文中无代码块")
            result["checks_failed"] += 1
            result["executable"] = False
        else:
            result["checks_passed"] += 1  # 纯描述性skill也可以

    # 检查2: 脚本引用是否存在 (L7B_BROKEN_REF)
    # 提取所有脚本/文件路径引用: scripts/xxx.py, bin/xxx, ./xxx.sh
    # 以及代码块中 python scripts/xxx.py 或 ./bin/xxx 形式的引用
    # 先去除 shebang 行 (#!/usr/bin/env, #!/bin/bash 等),避免误报 bin/env 等系统路径
    body_for_refs = re.sub(r'(?m)^[\s]*#!.*$', '', body_text)
    ref_patterns = [
        r'(?:\./)?(?:scripts?|bin)/[\w./-]+',  # scripts/ 或 bin/ 路径
        r'\./[\w-]+\.sh',                       # ./xxx.sh
    ]
    script_refs = set()
    for pattern in ref_patterns:
        for m in re.finditer(pattern, body_for_refs):
            ref = m.group(0)
            # 标准化: 去除 ./
            if ref.startswith('./'):
                ref = ref[2:]
            # 去除尾部 . 或 /
            ref = ref.rstrip('./')
            if ref:
                script_refs.add(ref)

    if not script_refs:
        # 没有引用任何脚本,不是错误
        result["checks_passed"] += 1
    else:
        # 检查引用的脚本/文件是否实际存在于 skill 目录中
        broken_refs = []
        skill_dir = None
        if skill_path is not None:
            # skill_path 可能是 SKILL.md 文件路径或 skill 目录路径
            try:
                if skill_path.is_file():
                    skill_dir = skill_path.parent
                elif skill_path.is_dir():
                    skill_dir = skill_path
                else:
                    # 路径不存在: 如果以 .md 结尾则视为文件路径,取父目录
                    skill_dir = skill_path.parent if skill_path.suffix == '.md' else skill_path
            except Exception:
                skill_dir = None

        if skill_dir is not None:
            for ref in sorted(script_refs):
                expected_path = skill_dir / ref
                if not expected_path.exists():
                    broken_refs.append((ref, expected_path))

        if broken_refs:
            for ref, expected_path in broken_refs:
                result["issues"].append({
                    "code": "L7B_BROKEN_REF",
                    "message": f"引用了不存在的脚本/文件: {ref} (路径: {expected_path})"
                })
            result["checks_failed"] += 1
        else:
            # 所有引用的脚本都存在 (或无法验证文件系统时跳过)
            result["checks_passed"] += 1

    # 检查3: 任务描述是否具体
    vague_patterns = [
        r'按照skill规范执行.*操作',
        r'处理用户输入并返回结果',
        r'执行.*操作.*处理.*结果',
    ]
    vague_count = 0
    for pattern in vague_patterns:
        vague_count += len(re.findall(pattern, body_text))
    if vague_count > 3:
        result["issues"].append(f"L7B_VAGUE_TASK: 检测到 {vague_count} 处模糊任务描述")
        result["checks_failed"] += 1
    else:
        result["checks_passed"] += 1

    # 检查4: 输入参数说明
    has_input_section = bool(re.search(r'##\s*(?:输入|参数|输入格式|参数说明)', body_text))
    has_input_table = bool(re.search(r'\|\s*参数名?\s*\|.*\|\s*类型\s*\|.*\|\s*必填', body_text))
    if has_input_section or has_input_table:
        result["checks_passed"] += 1
    else:
        # 如果有代码块,检查是否有参数说明
        if has_code:
            result["issues"].append("L7B_MISSING_INPUT: 有代码但缺少输入参数说明")
            result["checks_failed"] += 1
        else:
            result["checks_passed"] += 1

    # 检查5: 输出格式说明
    has_output_section = bool(re.search(r'##\s*(?:输出|输出格式|返回值|返回结果)', body_text))
    has_output_example = bool(re.search(r'(?:输出|返回|结果).*[:：]\s*\n', body_text))
    if has_output_section or has_output_example:
        result["checks_passed"] += 1
    else:
        if has_code:
            result["issues"].append("L7B_NO_OUTPUT: 有代码但缺少输出格式说明")
            result["checks_failed"] += 1
        else:
            result["checks_passed"] += 1

    # 检查6: 内容自相矛盾检测
    # 检查是否同时声称"免费"和"付费"
    has_free_claim = bool(re.search(r'永久免费|完全免费|免费使用', body_text))
    has_paid_claim = bool(re.search(r'付费版|Proprietary|suggested_price', body_text))
    if has_free_claim and has_paid_claim:
        result["issues"].append("L7B_CONTRADICTION: 同时存在免费和付费表述,内容自相矛盾")
        result["checks_failed"] += 1
    else:
        result["checks_passed"] += 1

    # === 评分 ===
    total_checks = result["checks_passed"] + result["checks_failed"]
    if total_checks > 0:
        pass_rate = result["checks_passed"] / total_checks
    else:
        pass_rate = 1.0

    if not result["executable"]:
        result["l7b_score"] = 20
        result["l7b_grade"] = "F"
    elif pass_rate == 1.0:
        result["l7b_score"] = 100
        result["l7b_grade"] = "A"
    elif pass_rate >= 0.8:
        result["l7b_score"] = 80
        result["l7b_grade"] = "B"
    elif pass_rate >= 0.6:
        result["l7b_score"] = 60
        result["l7b_grade"] = "C"
    elif pass_rate >= 0.4:
        result["l7b_score"] = 40
        result["l7b_grade"] = "D"
    else:
        result["l7b_score"] = 15
        result["l7b_grade"] = "F"

    return result


# ============ 安全审计 (Layer 8: Security Audit) ============
# L8: 安全审计 - 基于 skillhub_review_analysis_v36.json 的8类安全审核失败模式
# 检测外部URL、注入营销文本、API密钥暴露、slug内容不匹配、重复YAML字段、
# 标签不匹配、乱码文本、依赖矛盾

# 外部URL白名单域名 (允许的文档/开发站点)
_EXTERNAL_URL_ALLOWLIST = frozenset({
    "skillhub.cn", "www.skillhub.cn",
    "skillhub.ai", "www.skillhub.ai",
    "clawhub.ai", "www.clawhub.ai",
    "github.com", "raw.githubusercontent.com", "gist.github.com",
    "npmjs.com", "www.npmjs.com",
    "pypi.org", "www.pypi.org",
    "python.org", "docs.python.org", "www.python.org",
    "nodejs.org", "www.nodejs.org",
    "developer.mozilla.org", "learn.microsoft.com",
    "json.org", "www.json.org",
    "schema.org", "www.schema.org",
    "w3.org", "www.w3.org",
    "example.com", "www.example.com",
    "localhost", "127.0.0.1",
    "unicode.org", "www.unicode.org",
    "opensource.org",
    "creativecommons.org",
    "tools.ietf.org",
    "datatracker.ietf.org",
    "semver.org",
    "yaml.org",
    "httpstatus.io",
    "google.com", "www.google.com",
    "swagger.io", "www.swagger.io",
    "openai.com", "www.openai.com",
    "anthropic.com", "www.anthropic.com",
})

# slug关键词停用词 (不参与slug-content匹配的通用词)
_SLUG_STOPWORDS = frozenset({
    "and", "the", "for", "pro", "free", "tool", "tools", "api", "new",
    "all", "gen", "skill", "paid", "hub", "app", "plus", "lite", "max",
    "with", "your", "use", "via", "using", "from", "into",
})

# 注入营销文本模式 (差异化处理脚本注入的无关模板文本)
# 注意: "海报制作"单独出现是合法词汇,只匹配完整营销模板序列
_INJECTED_MARKETING_PATTERNS = [
    (r'需要营销推广[、，。]|广告投放[、，。][^。]*获客转化|增长裂变', "营销推广模板注入"),
    (r'需要设计创作[、，。][^。]*海报制作', "设计创作模板注入"),
    (r'不适用于非法营销手段', "非法营销免责声明模板"),
    (r'适用于独立开发者[、，]企业团队和自动化工作流场景', "适用场景模板注入"),
]

# API密钥暴露模式
_API_KEY_EXPOSURE_PATTERNS = [
    # 占位符密钥: 至少12个x, 且前后有引号/等号/冒号等上下文 (排除普通文本中的xxx)
    (r'(?<=["\':= ])x{12,}(?=["\':= \n])', "占位符密钥(xxxxxxxxxxxx模式)"),
    (r'Authorization:\s*Bearer\s+YOUR_API_KEY', "Bearer YOUR_API_KEY模式"),
    (r'sk-xxxx', "sk-xxxx密钥格式"),
    # 排除YOUR_PUBLIC_KEY/YOUR_SECRET_KEY等安全占位符
    (r'stream-public-key:\s*(?!YOUR_|your_)[A-Z_]{4,}', "stream-public-key请求头模式"),
    (r'stream-secret-key:\s*(?!YOUR_|your_)[A-Z_]{4,}', "stream-secret-key请求头模式"),
    (r'taro_[a-z_]{4,}\.[a-z_]{4,}', "taro_密钥格式"),
    (r'AKIA[0-9A-Z]{16}', "AWS AKIA密钥格式"),
    (r'ghp_[a-zA-Z0-9]{36}', "GitHub Token格式"),
]

# 乱码/编码错误模式 (UTF-8被错误解码为Latin-1的mojibake)
_GARBLED_TEXT_PATTERNS = [
    (r'æ[\xb0-\xff]{2,5}å[\xe6-\xff]{1,5}', "UTF-8 mojibake (æ°å模式)"),
    (r'[æåçèéêëìíîïðñòóôõöøùúûüýþÿ]{4,}', "连续Latin-1扩展字符(mojibake)"),
    (r'Ã[\x80-\xbf]', "UTF-8双字节mojibake (Ã模式)"),
    (r'Â[\xa6-\xbf]', "Latin-1符号mojibake (Â模式)"),
]

# URL提取正则
_URL_DOMAIN_REGEX = re.compile(
    r'https?://([a-zA-Z0-9][-a-zA-Z0-9.]*\.[a-zA-Z]{2,}|localhost|127\.0\.0\.1)'
)


def check_security_quality(content: str, fm: dict, fm_text: str, body_text: str,
                           slug: str, dir_name: str) -> dict:
    """Layer 8: 安全审计 - 检测8类安全审核失败模式

    基于 skillhub_review_analysis_v36.json 的失败类别:
    1. EXTERNAL_URL - 外部商业URL或第三方API端点
    2. INJECTED_MARKETING_TEXT - 注入的无关营销模板文本
    3. API_KEY_EXPOSURE - API密钥格式和Authorization头模式
    4. SLUG_CONTENT_MISMATCH - slug与内容不匹配
    5. DUPLICATE_YAML_FIELDS - frontmatter重复字段
    6. TAG_MISMATCH - tags与内容不匹配
    7. GARBLED_TEXT - 乱码/编码错误
    8. DEPENDENCY_CONTRADICTION - 依赖说明与限制矛盾

    Args:
        content: 完整文件内容 (frontmatter + body)
        fm: 解析后的frontmatter字典
        fm_text: frontmatter原始文本
        body_text: 正文文本 (不含frontmatter)
        slug: skill slug
        dir_name: 目录名

    Returns:
        dict: {
            issues: list,          # 问题描述列表 [{category, severity, message, evidence}]
            score: int,            # 0-100
            grade: str,            # A/B/C/D/F
            passed: bool,          # 是否通过安全审计
            category_counts: dict, # 各类别问题数量
        }
    """
    issues = []
    category_counts = {
        "EXTERNAL_URL": 0,
        "INJECTED_MARKETING_TEXT": 0,
        "API_KEY_EXPOSURE": 0,
        "SLUG_CONTENT_MISMATCH": 0,
        "DUPLICATE_YAML_FIELDS": 0,
        "TAG_MISMATCH": 0,
        "GARBLED_TEXT": 0,
        "DEPENDENCY_CONTRADICTION": 0,
    }

    # === 1. EXTERNAL_URL 检查 ===
    # 只检查frontmatter中的URL (body中的API端点文档是合法的)
    url_domains = _URL_DOMAIN_REGEX.findall(fm_text)
    external_urls = []
    for domain in url_domains:
        domain_lower = domain.lower()
        is_allowed = any(
            domain_lower == a or domain_lower.endswith('.' + a)
            for a in _EXTERNAL_URL_ALLOWLIST
        )
        if not is_allowed and domain not in external_urls:
            external_urls.append(domain)
    if external_urls:
        category_counts["EXTERNAL_URL"] = len(external_urls)
        issues.append({
            "category": "EXTERNAL_URL",
            "severity": "high",
            "message": f"frontmatter中发现 {len(external_urls)} 个外部URL域名 (非白名单)",
            "evidence": ", ".join(external_urls[:5]),
        })

    # === 2. INJECTED_MARKETING_TEXT 检查 ===
    marketing_hits = []
    for pattern, desc in _INJECTED_MARKETING_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            marketing_hits.append(desc)
            category_counts["INJECTED_MARKETING_TEXT"] += len(matches)
    if marketing_hits:
        issues.append({
            "category": "INJECTED_MARKETING_TEXT",
            "severity": "high",
            "message": f"发现注入营销模板文本: {'; '.join(marketing_hits)}",
            "evidence": marketing_hits[0],
        })

    # === 3. API_KEY_EXPOSURE 检查 ===
    # 安全类skill合法地讨论密钥模式作为功能文档,加入白名单豁免
    _API_KEY_WHITELIST = {
        "security-audit",  # 安全审计skill合法文档化AKIA等密钥检测模式
    }
    api_key_hits = []
    if slug not in _API_KEY_WHITELIST:
        for pattern, desc in _API_KEY_EXPOSURE_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                api_key_hits.append(desc)
                category_counts["API_KEY_EXPOSURE"] += len(matches)
    if api_key_hits:
        issues.append({
            "category": "API_KEY_EXPOSURE",
            "severity": "medium",
            "message": f"发现API密钥暴露模式: {'; '.join(api_key_hits)}",
            "evidence": api_key_hits[0],
        })

    # === 4. SLUG_CONTENT_MISMATCH 检查 ===
    # 启发式: slug关键词应出现在description/body/name/displayName中
    # 过滤停用词,避免对通用词(and/free/pro等)的误报
    description = str(fm.get('description', '')).strip()
    if slug and description and len(slug) > 3:
        slug_words = [w for w in slug.split('-')
                      if len(w) > 2 and w.lower() not in _SLUG_STOPWORDS]
        if slug_words:
            # 在description, body_text, name, displayName中搜索
            name_val = str(fm.get('name', '')).lower()
            display_val = str(fm.get('displayName', '')).lower()
            search_text = (description + ' ' + body_text[:3000] +
                           ' ' + name_val + ' ' + display_val).lower()
            matched_words = [w for w in slug_words if w.lower() in search_text]
            # 如果没有任何slug关键词出现在搜索文本中,标记为不匹配
            if not matched_words:
                category_counts["SLUG_CONTENT_MISMATCH"] = 1
                issues.append({
                    "category": "SLUG_CONTENT_MISMATCH",
                    "severity": "medium",
                    "message": f"slug关键词 {slug_words} 均未出现在description/body中",
                    "evidence": f"slug='{slug}', desc前50字符='{description[:50]}'",
                })

    # === 5. DUPLICATE_YAML_FIELDS 检查 ===
    # 检查frontmatter原始文本中的重复顶层键
    if fm_text:
        # 匹配行首的 key: 模式 (非缩进行)
        fm_keys = re.findall(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*:', fm_text, re.MULTILINE)
        key_counts = {}
        for key in fm_keys:
            key_counts[key] = key_counts.get(key, 0) + 1
        duplicates = {k: v for k, v in key_counts.items() if v > 1}
        if duplicates:
            dup_count = sum(duplicates.values())
            category_counts["DUPLICATE_YAML_FIELDS"] = dup_count
            issues.append({
                "category": "DUPLICATE_YAML_FIELDS",
                "severity": "medium",
                "message": f"frontmatter存在重复字段: {dict(duplicates)}",
                "evidence": f"重复字段: {', '.join(f'{k}({v}次)' for k, v in duplicates.items())}",
            })

    # === 6. TAG_MISMATCH 检查 ===
    # 启发式: tags为逗号分隔字符串时,检查是否与内容相关
    tags_val = fm.get('tags', None)
    if tags_val and isinstance(tags_val, str):
        tag_words = [t.strip().strip("'\"") for t in tags_val.split(',') if t.strip()]
        tag_words = [t for t in tag_words if len(t) > 1]
        if tag_words:
            search_text = (description + ' ' + body_text[:2000]).lower()
            matched_tags = [t for t in tag_words if t.lower() in search_text]
            # 如果超过一半的tag词未在内容中出现,标记为不匹配
            unmatched = len(tag_words) - len(matched_tags)
            if unmatched > len(tag_words) / 2:
                category_counts["TAG_MISMATCH"] = 1
                issues.append({
                    "category": "TAG_MISMATCH",
                    "severity": "low",
                    "message": f"tags字段与内容不匹配: {tag_words} (匹配{len(matched_tags)}/{len(tag_words)})",
                    "evidence": f"未匹配tags: {[t for t in tag_words if t.lower() not in search_text]}",
                })

    # === 7. GARBLED_TEXT 检查 ===
    garbled_hits = []
    for pattern, desc in _GARBLED_TEXT_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            garbled_hits.append(desc)
            category_counts["GARBLED_TEXT"] += len(matches)
    if garbled_hits:
        issues.append({
            "category": "GARBLED_TEXT",
            "severity": "low",
            "message": f"发现乱码/编码错误文本: {'; '.join(garbled_hits)}",
            "evidence": garbled_hits[0],
        })

    # === 8. DEPENDENCY_CONTRADICTION 检查 ===
    # 检查"需要API Key"和"无需API Key"同时出现
    # 使用负向后顾(?<![无不])排除"无需"中的"需"导致的误报
    # 使用负向后顾(?<!非)排除"非API Key"的否定表述
    # 使用[^。；\n]避免跨句匹配,排除"回报要求...API密钥"等误报
    # 排除可选/高级功能场景(如需/若需/可选/专业版/外部/脚本等)以减少误报
    # 使用负向前瞻(?!\s*[吗呢])排除FAQ问句"需要API Key吗？"的误报
    _OPTIONAL_INDICATORS = re.compile(
        r'(?:如需|若需|可选|专业版|高级功能|额外配置|云端|云服务|外部服务|外部API|外部|批量|企业版|付费|Pro版|增强|升级|对应服务|对应|各自平台|各自|自定义|CDN|短信|推送|更高|专业|批量扫描|官方API|兼容API|外部写作|TTS|图像生成|云向量|云浏览器|OpenAI|Deepgram|ElevenLabs|百度|模型|目标API|脚本|被守护|可能|如使用|若使用)',
        re.IGNORECASE
    )
    # FAQ问句行模式: 以Q/### Q/问开头,或包含问号
    _QA_LINE_PATTERN = re.compile(r'^(?:#{1,6}\s*)?(?:Q\d*[：:]|问[：:]|.*？\s*$)', re.MULTILINE)
    needs_api_key = False
    for m in re.finditer(
        r'(?<![无不])(?:需要|需|要求)[^。；\n]{0,10}(?<!非)(?:API\s*Key|API密钥|API\s*key|api[_-]?key)(?!\s*[吗呢])',
        body_text, re.IGNORECASE
    ):
        # 排除FAQ问句行: 如果匹配所在行是Q&A问句,跳过
        line_start = body_text.rfind('\n', 0, m.start()) + 1
        line_end = body_text.find('\n', m.end())
        if line_end == -1:
            line_end = len(body_text)
        line_text = body_text[line_start:line_end]
        if _QA_LINE_PATTERN.match(line_text.strip()):
            continue
        # 检查匹配前的50字符上下文和匹配文本本身是否包含可选/外部功能指示词
        context_start = max(0, m.start() - 50)
        context = body_text[context_start:m.end()]
        if not _OPTIONAL_INDICATORS.search(context):
            needs_api_key = True
            break
    no_api_key = bool(re.search(
        r'(?:无需|不需要|无须|无需额外).{0,10}(?:API|密钥|API\s*Key)',
        body_text, re.IGNORECASE
    ))
    if needs_api_key and no_api_key:
        category_counts["DEPENDENCY_CONTRADICTION"] = 1
        issues.append({
            "category": "DEPENDENCY_CONTRADICTION",
            "severity": "low",
            "message": "依赖说明与已知限制矛盾: 同时出现'需要API Key'和'无需API Key'表述",
            "evidence": "body中同时存在需要/无需API Key的矛盾表述",
        })

    # === 评分 ===
    # 基础分100, 每个high问题扣25, medium扣15, low扣10
    penalty = 0
    for issue in issues:
        sev = issue["severity"]
        if sev == "high":
            penalty += 25
        elif sev == "medium":
            penalty += 15
        elif sev == "low":
            penalty += 10
    score = max(0, 100 - penalty)

    # 评级
    if score >= 90:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 30:
        grade = "D"
    else:
        grade = "F"

    passed = len(issues) == 0

    return {
        "issues": issues,
        "score": score,
        "grade": grade,
        "passed": passed,
        "category_counts": category_counts,
    }


def run_audit(fix_mode: bool = False, fix_all: bool = False, enable_l7: bool = True, enable_l7b: bool = True, enable_l8: bool = True):
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
    if enable_l7:
        print("[Layer 7a] 语义审计已启用 (L7a TF-IDF模板检测)")
    if enable_l7b:
        print("[Layer 7b] 可执行性审计已启用 (L7b 静态可执行性检查)")
    if enable_l8:
        print("[Layer 8] 安全审计已启用 (L8 8类安全审核检查)")
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
        result = check_skill(skill_path, source, enable_l7=enable_l7, enable_l7b=enable_l7b, enable_l8=enable_l8)
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
    sell_grade_b = []  # B级可销售性(可提升至A)
    func_score_sum = 0
    sell_score_sum = 0

    # Layer 6 统计
    auth_grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    auth_issues_list = []
    auth_score_sum = 0
    auth_template_total = 0

    # Layer 7 统计
    l7_grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    l7_issues_list = []
    l7_score_sum = 0
    l7_template_block_total = 0
    l7_available_count = 0

    # Layer 7b (可执行性) 统计
    l7b_grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    l7b_issues_list = []
    l7b_score_sum = 0
    l7b_available_count = 0
    l7b_executable_count = 0
    # 6项检查触发分布
    l7b_check_distribution = {
        "L7B_NO_CODE": 0,
        "L7B_BROKEN_REF": 0,
        "L7B_VAGUE_TASK": 0,
        "L7B_MISSING_INPUT": 0,
        "L7B_NO_OUTPUT": 0,
        "L7B_CONTRADICTION": 0,
    }

    # Layer 8 (安全审计) 统计
    l8_grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    l8_issues_list = []
    l8_score_sum = 0
    l8_available_count = 0
    l8_passed_count = 0
    l8_failed_count = 0
    # 8类安全问题触发分布
    l8_category_distribution = {
        "EXTERNAL_URL": 0,
        "INJECTED_MARKETING_TEXT": 0,
        "API_KEY_EXPOSURE": 0,
        "SLUG_CONTENT_MISMATCH": 0,
        "DUPLICATE_YAML_FIELDS": 0,
        "TAG_MISMATCH": 0,
        "GARBLED_TEXT": 0,
        "DEPENDENCY_CONTRADICTION": 0,
    }

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
        elif sell_grade == "B":
            sell_grade_b.append({
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

        # 收集语义审计统计 (Layer 7)
        sem = result.get("semantic", {})
        l7_grade = sem.get("l7a_grade", "N/A")
        l7_score = sem.get("l7a_score", -1)
        if l7_grade not in l7_grades:
            l7_grades[l7_grade] = 0
        l7_grades[l7_grade] += 1
        if l7_score >= 0:
            l7_score_sum += l7_score
            l7_available_count += 1
        l7_template_block_total += sem.get("template_block_count", 0)
        if sem.get("issues"):
            l7_issues_list.append({
                "slug": result["slug"],
                "source": result["source"],
                "grade": l7_grade,
                "score": l7_score,
                "template_block_count": sem.get("template_block_count", 0),
                "issues": sem["issues"],
            })

        # 收集可执行性审计统计 (Layer 7b)
        exe = result.get("executability", {})
        l7b_grade = exe.get("l7b_grade", "N/A")
        l7b_score = exe.get("l7b_score", -1)
        if l7b_grade not in l7b_grades:
            l7b_grades[l7b_grade] = 0
        l7b_grades[l7b_grade] += 1
        if l7b_score >= 0:
            l7b_score_sum += l7b_score
            l7b_available_count += 1
        if exe.get("executable"):
            l7b_executable_count += 1
        # 统计6项检查触发分布
        for issue in exe.get("issues", []):
            issue_code = None
            if isinstance(issue, dict):
                issue_code = issue.get("code")
            elif isinstance(issue, str):
                # 形如 "L7B_NO_CODE: ..." 
                m = re.match(r'(L7B_\w+)', issue)
                issue_code = m.group(1) if m else None
            if issue_code and issue_code in l7b_check_distribution:
                l7b_check_distribution[issue_code] += 1
        if exe.get("issues"):
            l7b_issues_list.append({
                "slug": result["slug"],
                "source": result["source"],
                "grade": l7b_grade,
                "score": l7b_score,
                "executable": exe.get("executable"),
                "checks_passed": exe.get("checks_passed", 0),
                "checks_failed": exe.get("checks_failed", 0),
                "issues": exe["issues"],
            })

        # 收集安全审计统计 (Layer 8)
        sec = result.get("security", {})
        l8_grade = sec.get("l8_grade", "N/A")
        l8_score = sec.get("l8_score", -1)
        if l8_grade not in l8_grades:
            l8_grades[l8_grade] = 0
        l8_grades[l8_grade] += 1
        if l8_score >= 0:
            l8_score_sum += l8_score
            l8_available_count += 1
        if sec.get("l8_passed"):
            l8_passed_count += 1
        else:
            l8_failed_count += 1
        # 统计8类安全问题触发分布
        for cat, cnt in sec.get("category_counts", {}).items():
            if cnt > 0 and cat in l8_category_distribution:
                l8_category_distribution[cat] += 1
        if sec.get("issues"):
            l8_issues_list.append({
                "slug": result["slug"],
                "source": result["source"],
                "grade": l8_grade,
                "score": l8_score,
                "passed": sec.get("l8_passed"),
                "category_counts": sec.get("category_counts", {}),
                "issues": sec["issues"],
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
            "semantic_grade": sem.get("l7a_grade", "N/A") if 'sem' in dir() else "N/A",
            "semantic_score": sem.get("l7a_score", -1) if 'sem' in dir() else -1,
            "executability_grade": l7b_grade,
            "executability_score": l7b_score,
            "executable": exe.get("executable"),
            "security_grade": l8_grade,
            "security_score": l8_score,
            "security_passed": sec.get("l8_passed"),
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
            "total_b_grade": len(sell_grade_b),
            "b_grade_detail": sell_grade_b[:100],
        },
        "content_authenticity": {
            "grade_distribution": auth_grades,
            "avg_score": round(auth_avg, 1),
            "total_with_issues": len(auth_issues_list),
            "total_template_fills": auth_template_total,
            "issues_detail": auth_issues_list[:200],
        },
        "semantic_audit": {
            "enabled": enable_l7,
            "l7a_available_count": l7_available_count,
            "grade_distribution": l7_grades,
            "avg_score": round(l7_score_sum / l7_available_count, 1) if l7_available_count else 0,
            "total_template_blocks": l7_template_block_total,
            "total_with_issues": len(l7_issues_list),
            "issues_detail": l7_issues_list[:100],
        },
        "executability_audit": {
            "enabled": enable_l7b,
            "l7b_available_count": l7b_available_count,
            "grade_distribution": l7b_grades,
            "avg_score": round(l7b_score_sum / l7b_available_count, 1) if l7b_available_count else 0,
            "executable_count": l7b_executable_count,
            "pass_rate": f"{l7b_executable_count * 100 // total}%" if total else "0%",
            "check_distribution": l7b_check_distribution,
            "total_with_issues": len(l7b_issues_list),
            "issues_detail": l7b_issues_list,
        },
        "security_audit": {
            "enabled": enable_l8,
            "l8_available_count": l8_available_count,
            "grade_distribution": l8_grades,
            "avg_score": round(l8_score_sum / l8_available_count, 1) if l8_available_count else 0,
            "passed_count": l8_passed_count,
            "failed_count": l8_failed_count,
            "pass_rate": f"{l8_passed_count * 100 // total}%" if total else "0%",
            "category_distribution": l8_category_distribution,
            "total_with_issues": len(l8_issues_list),
            "issues_detail": l8_issues_list,
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
    if sell_grade_b:
        print(f"  B级 (可提升至A): {len(sell_grade_b)} 个 skill")
        for item in sell_grade_b[:30]:
            factors_str = ', '.join(item.get('factors', [])) if item.get('factors') else '无'
            print(f"    [{item['grade']}] {item['slug']} (分:{item['score']}): {factors_str}")
        if len(sell_grade_b) > 30:
            print(f"    ... 还有 {len(sell_grade_b) - 30} 个")

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

    # Layer 7: 语义审计统计
    if enable_l7:
        print()
        print("─" * 60)
        print("语义审计 (Layer 7: Semantic Audit - L7a 嵌入向量模板检测):")
        if l7_available_count > 0:
            l7_avg = l7_score_sum / l7_available_count
            print(f"  模型可用: {l7_available_count} / {total} 个 skill 已分析")
            print(f"  平均分: {l7_avg:.1f} / 100")
            print(f"  等级分布: A={l7_grades.get('A',0)}  B={l7_grades.get('B',0)}  "
                  f"C={l7_grades.get('C',0)}  D={l7_grades.get('D',0)}  "
                  f"F={l7_grades.get('F',0)}  N/A={l7_grades.get('N/A',0)}")
            l7_a_b = l7_grades.get('A', 0) + l7_grades.get('B', 0)
            print(f"  A+B级 (语义合格): {l7_a_b} / {l7_available_count} ({l7_a_b*100//l7_available_count if l7_available_count else 0}%)")
            print(f"  疑似模板块总数: {l7_template_block_total}")
            print(f"  有问题skill: {len(l7_issues_list)} 个")
            if l7_issues_list:
                severe_l7 = [item for item in l7_issues_list if item['grade'] in ('C', 'D', 'F')]
                if severe_l7:
                    print(f"  C+D+F级 (严重语义问题): {len(severe_l7)} 个")
                    for item in severe_l7[:15]:
                        issues_str = '; '.join(item['issues'][:2])
                        print(f"    [{item['grade']}] {item['slug']} (分:{item['score']}, 模板块:{item['template_block_count']}): {issues_str}")
                    if len(severe_l7) > 15:
                        print(f"    ... 还有 {len(severe_l7) - 15} 个")
        else:
            na_count = l7_grades.get('N/A', 0)
            print(f"  模型不可用: {na_count} 个 skill 跳过 L7a 分析")
            print(f"  安装 sentence-transformers 以启用: pip install sentence-transformers")

    # Layer 7b: 可执行性审计统计
    if enable_l7b:
        print()
        print("─" * 60)
        print("可执行性审计 (Layer 7b: Executability Audit - L7b 静态可执行性检查):")
        if l7b_available_count > 0:
            l7b_avg = l7b_score_sum / l7b_available_count
            print(f"  已分析: {l7b_available_count} / {total} 个 skill")
            print(f"  平均分: {l7b_avg:.1f} / 100")
            print(f"  等级分布: A={l7b_grades.get('A',0)}  B={l7b_grades.get('B',0)}  "
                  f"C={l7b_grades.get('C',0)}  D={l7b_grades.get('D',0)}  "
                  f"F={l7b_grades.get('F',0)}  N/A={l7b_grades.get('N/A',0)}")
            print(f"  可执行: {l7b_executable_count} / {total} ({l7b_executable_count*100//total if total else 0}%)")
            print(f"  6项检查触发分布:")
            for code, cnt in l7b_check_distribution.items():
                print(f"    {code}: {cnt}")
            print(f"  有问题skill: {len(l7b_issues_list)} 个")
            if l7b_issues_list:
                severe_l7b = [item for item in l7b_issues_list if item['grade'] in ('C', 'D', 'F')]
                if severe_l7b:
                    print(f"  C+D+F级 (严重可执行性问题): {len(severe_l7b)} 个")
                    for item in severe_l7b[:20]:
                        issues_str = '; '.join(
                            (i if isinstance(i, str) else i.get('message', str(i))) for i in item['issues'][:2]
                        )
                        print(f"    [{item['grade']}] {item['slug']} (分:{item['score']}): {issues_str}")
                    if len(severe_l7b) > 20:
                        print(f"    ... 还有 {len(severe_l7b) - 20} 个")

    # Layer 8: 安全审计统计
    if enable_l8:
        print()
        print("─" * 60)
        print("安全审计 (Layer 8: Security Audit - L8 8类安全审核检查):")
        if l8_available_count > 0:
            l8_avg = l8_score_sum / l8_available_count
            print(f"  已分析: {l8_available_count} / {total} 个 skill")
            print(f"  平均分: {l8_avg:.1f} / 100")
            print(f"  等级分布: A={l8_grades.get('A',0)}  B={l8_grades.get('B',0)}  "
                  f"C={l8_grades.get('C',0)}  D={l8_grades.get('D',0)}  "
                  f"F={l8_grades.get('F',0)}  N/A={l8_grades.get('N/A',0)}")
            print(f"  安全通过: {l8_passed_count} / {total} ({l8_passed_count*100//total if total else 0}%)")
            print(f"  安全失败: {l8_failed_count} / {total} ({l8_failed_count*100//total if total else 0}%)")
            print(f"  8类安全问题触发分布:")
            for cat, cnt in l8_category_distribution.items():
                print(f"    {cat}: {cnt}")
            print(f"  有问题skill: {len(l8_issues_list)} 个")
            if l8_issues_list:
                severe_l8 = [item for item in l8_issues_list if item['grade'] in ('C', 'D', 'F')]
                if severe_l8:
                    print(f"  C+D+F级 (严重安全问题): {len(severe_l8)} 个")
                    for item in severe_l8[:25]:
                        issues_str = '; '.join(
                            (i.get('message', str(i)) if isinstance(i, dict) else str(i))
                            for i in item['issues'][:3]
                        )
                        print(f"    [{item['grade']}] {item['slug']} (分:{item['score']}): {issues_str}")
                    if len(severe_l8) > 25:
                        print(f"    ... 还有 {len(severe_l8) - 25} 个")

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
    # L7a 使用轻量级 sklearn TF-IDF 后端, 默认启用; 可通过 --no-layer7 关闭
    enable_l7 = "--no-layer7" not in sys.argv
    # L7b 可执行性审计默认启用; 可通过 --no-layer7b 关闭 (与L7a/L8保持一致的opt-out模式)
    enable_l7b = "--no-layer7b" not in sys.argv
    # L8 安全审计默认启用; 可通过 --no-layer8 关闭
    enable_l8 = "--no-layer8" not in sys.argv

    passed = run_audit(fix_mode=fix_mode, fix_all=fix_all, enable_l7=enable_l7, enable_l7b=enable_l7b, enable_l8=enable_l8)

    # 如果存在 critical 问题，返回非零退出码
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
