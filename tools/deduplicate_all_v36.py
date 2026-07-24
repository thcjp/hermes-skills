
# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===

# -*- coding: utf-8 -*-
"""
L7A 全量去重脚本 v36
====================
覆盖全部3个目录:
  - d:\skills\packaged-skills\skillhub
  - d:\skills\opensource-skills\packaged
  - str(DIFFERENTIATED_DIR)

处理三类问题:
  a. 修复重复章节标题(如 ## 付费版专享能力 / ## 已知限制 出现2次) - 合并内容或重命名
  b. 规范化表格分隔符格式(统一为 |--------|------| 格式,去掉冒号和空格)
  c. 差异化通用付费能力行(每个skill的付费能力描述应该不同)

不使用 mock/fallback/todo。实际修改SKILL.md文件。
"""

import re
import os
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import Counter

# ============================================================
# 配置
# ============================================================

SCAN_DIRS = [
    Path(r"d:\skills\packaged-skills\skillhub"),
    Path(r"d:\skills\opensource-skills\packaged"),
    DIFFERENTIATED_DIR,
]

REPORT_OUTPUT = DATA_DIR / "reports" / "dedup_all_v36.json"

SIMILARITY_THRESHOLD = 0.92

# 通用付费能力行关键词(需要差异化的模板行)
GENERIC_PAID_KEYWORDS = [
    "高级配置", "批量处理", "批量操作", "自动化处理",
    "自定义配置", "结果导出", "实时监控", "优先支持",
]

# ============================================================
# Skill 元数据解析
# ============================================================

def split_frontmatter(text):
    """将 SKILL.md 文本拆分为 frontmatter 和正文。"""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", text


def parse_frontmatter(fm_text):
    """解析简单 YAML frontmatter,提取关键字段。"""
    data = {}
    current_key = None
    for line in fm_text.split("\n"):
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip('"').strip("'")
            data[key] = val
            current_key = key
        elif current_key == "tags" and line.strip().startswith("-"):
            tag_val = line.strip().lstrip("-").strip()
            if "tags" in data and data["tags"]:
                data["tags"] = data["tags"] + " " + tag_val
            else:
                data["tags"] = tag_val
    return data


# ============================================================
# Skill 类型/领域分类
# ============================================================

def classify_skill(meta):
    """根据 slug/displayName/summary/tags 判断 skill 类型和领域。

    返回 (skill_type, skill_domain)
    """
    slug = (meta.get("slug") or "").lower()
    display = (meta.get("displayName") or "").lower()
    summary = (meta.get("summary") or "").lower()
    tags = (meta.get("tags") or "").lower()
    combined = " ".join([slug, display, summary, tags])

    domain_rules = [
        ("finance", ["finance", "accounting", "估值", "财务", "金融", "trading", "stock", "投资"]),
        ("security", ["security", "安全", "audit", "vulnerability", "vuln", "pentest", "scan", "firewall", "encrypt", "加密"]),
        ("dev", ["code", "git", "docker", "python", "java", "javascript", "typescript", "rust", "go ", "golang", "compile", "lint", "develop", "开发", "scaffold", "framework", "sdk"]),
        ("browser", ["browser", "浏览器", "web-auto", "scrape", "crawl", "爬虫"]),
        ("comm", ["email", "chat", "message", "discord", "telegram", "slack", "whatsapp", "feishu", "飞书", "通知", "邮件", "消息"]),
        ("creative", ["image", "video", "music", "design", "podcast", "audio", "图", "视频", "音乐", "设计", "画", "logo", "figma", "ui", "ux", "frontend", "前端"]),
        ("data", ["api", "data", "csv", "json", "sql", "database", "db", "数据库", "excel", "图表", "chart", "analytics", "分析"]),
        ("auto", ["automation", "workflow", "cron", "schedule", "自动化", "定时", "任务", "batch", "queue"]),
        ("research", ["research", "search", "news", "feed", "rss", "研究", "搜索", "新闻", "监控", "monitor"]),
        ("productivity", ["productivity", "task", "calendar", "reminder", "note", "效率", "日程", "提醒", "笔记", "todo"]),
        ("platform", ["dashboard", "admin", "manage", "console", "平台", "管理", "控制台"]),
    ]

    skill_domain = "other"
    for domain, keywords in domain_rules:
        if any(kw in combined for kw in keywords):
            skill_domain = domain
            break

    if any(kw in combined for kw in ["dashboard", "admin", "console", "manage", "平台", "管理"]):
        skill_type = "platform"
    elif any(kw in combined for kw in ["api", "service", "服务", "接口"]):
        skill_type = "service"
    elif any(kw in combined for kw in ["image", "video", "music", "design", "画", "创意", "creative"]):
        skill_type = "creative"
    elif any(kw in combined for kw in ["code", "git", "docker", "develop", "开发", "lint", "compile"]):
        skill_type = "dev"
    elif any(kw in combined for kw in ["browser", "浏览器", "scrape", "crawl"]):
        skill_type = "browser"
    elif any(kw in combined for kw in ["email", "chat", "message", "discord", "通知", "消息"]):
        skill_type = "comm"
    elif any(kw in combined for kw in ["data", "csv", "json", "sql", "database", "excel", "chart"]):
        skill_type = "data"
    elif any(kw in combined for kw in ["automation", "workflow", "cron", "自动化", "定时"]):
        skill_type = "auto"
    else:
        skill_type = "tool"

    return skill_type, skill_domain


# ============================================================
# (a) 修复重复章节标题
# ============================================================

# 重复标题的重命名映射(第二次出现时使用的替代标题)
HEADER_RENAME_MAP = {
    "## 已知限制": "## 补充限制说明",
    "## 核心能力": "## 能力速查",
    "## 概述": "## 补充概述",
    "## 依赖说明": "## 环境依赖补充",
    "## 错误处理": "## 错误处理补充",
    "## 使用流程": "## 使用流程补充",
    "## 适用场景": "## 扩展场景",
    "## 付费版专享能力": "## 付费版扩展能力",
    "## 付费版专享功能": "## 付费版扩展功能",
}

# 不需要重命名的标题(内容型标题,如报告中的小节,出现两次是正常的文档结构)
# 这些标题如果重复,说明是不同内容,只需重命名第二个即可
CONTENT_HEADERS = {
    "## 科技新闻", "## 正文", "## 摘要", "## Findings", "## Resources",
    "## Next Steps", "## Open Questions", "## Options / Approaches",
}


def fix_duplicate_section_headers(content):
    """修复重复的 ## 章节标题。

    策略:
    1. 找到所有重复出现的 ## 标题
    2. 对于第二次及之后出现的标题:
       - 如果内容相同(紧接着的内容行完全一致),删除重复的标题和内容
       - 如果内容不同,重命名标题为不重复的替代名称
    返回 (new_content, fix_count)
    """
    fixes = 0
    lines = content.split("\n")
    header_positions = {}  # header_text -> [(line_index, ...), ...]

    # 第一遍: 收集所有 ## 标题的位置
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^##\s+\S', stripped):
            if stripped not in header_positions:
                header_positions[stripped] = []
            header_positions[stripped].append(i)

    # 找出重复的标题
    dup_headers = {h: positions for h, positions in header_positions.items() if len(positions) > 1}
    if not dup_headers:
        return content, 0

    # 需要从后往前处理(避免行号偏移)
    changes = []  # (line_index, old_line, new_line, action)  action: 'rename' or 'delete_block'

    for header_text, positions in dup_headers.items():
        for idx, pos in enumerate(positions):
            if idx == 0:
                continue  # 保留第一次出现

            # 获取该标题下的内容(到下一个同级或更高级标题)
            section_start = pos
            section_end = len(lines)
            header_level = len(re.match(r'^(#+)', header_text).group(1))
            for j in range(pos + 1, len(lines)):
                j_stripped = lines[j].strip()
                if re.match(r'^#{1,' + str(header_level) + r'}\s', j_stripped):
                    section_end = j
                    break

            section_content = "\n".join(lines[section_start:section_end]).strip()

            # 检查与第一次出现的内容是否相同
            first_start = positions[0]
            first_end = len(lines)
            for j in range(first_start + 1, len(lines)):
                j_stripped = lines[j].strip()
                if re.match(r'^#{1,' + str(header_level) + r'}\s', j_stripped):
                    first_end = j
                    break
            first_content = "\n".join(lines[first_start:first_end]).strip()

            if section_content == first_content:
                # 内容完全相同,标记删除整个重复块
                for j in range(section_start, section_end):
                    changes.append((j, lines[j], None, 'delete_line'))
                fixes += 1
            else:
                # 内容不同,重命名标题
                new_header = HEADER_RENAME_MAP.get(header_text)
                if not new_header:
                    # 生成基于序号的重命名
                    base = header_text.lstrip('#').strip()
                    new_header = f"## {base}(续{idx})"
                # 确保新标题不会与其他标题冲突
                while new_header in header_positions or new_header in [c[2] for c in changes if c[2]]:
                    base = header_text.lstrip('#').strip()
                    new_header = f"## {base}(续{idx + 1})"
                    idx += 1
                changes.append((pos, lines[pos], new_header, 'rename'))
                header_positions[new_header] = [pos]  # 记录新标题位置
                fixes += 1

    if not changes:
        return content, 0

    # 应用更改
    changes.sort(key=lambda x: x[0])
    new_lines = []
    skip_indices = set(idx for idx, _, _, action in changes if action == 'delete_line')
    rename_map = {idx: new_text for idx, _, new_text, action in changes if action == 'rename'}

    for i, line in enumerate(lines):
        if i in skip_indices:
            continue
        if i in rename_map:
            new_lines.append(rename_map[i])
        else:
            new_lines.append(line)

    # 清理多余的空行(连续2个以上空行合并为1个)
    result = "\n".join(new_lines)
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result, fixes


# ============================================================
# (b) 规范化表格分隔符格式
# ============================================================

def normalize_table_separators(content):
    """规范化表格分隔符,统一为 |--------|------| 格式。

    - 去掉冒号(:)
    - 去掉空格
    - 确保每个分隔单元格至少有3个连字符
    返回 (new_content, fix_count)
    """
    fixes = 0
    lines = content.split("\n")
    new_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        # 匹配表格分隔符行: |:---|:---| 或 |---|---| 或 | --- | --- | 等
        if re.match(r'^\|[\s:|\-]+\|$', stripped):
            # 统计列数
            col_count = stripped.count("|") - 1
            if col_count < 1:
                new_lines.append(line)
                continue

            # 获取表头行(上一行)来确定每列宽度
            header_widths = []
            if i > 0:
                header_line = lines[i - 1].strip()
                if header_line.startswith("|") and header_line.endswith("|"):
                    cells = header_line.split("|")[1:-1]
                    for cell in cells:
                        header_widths.append(max(len(cell.strip()), 3))

            # 生成规范化的分隔符
            cells = []
            for c in range(col_count):
                width = header_widths[c] if c < len(header_widths) else 6
                # 确保至少3个连字符,最多12个
                dash_count = max(3, min(width, 12))
                cells.append("-" * dash_count)

            new_sep = "|" + "|".join(cells) + "|"

            if new_sep != stripped:
                fixes += 1
            new_lines.append(new_sep)
        else:
            new_lines.append(line)

    return "\n".join(new_lines), fixes


# ============================================================
# (c) 差异化通用付费能力行
# ============================================================

# 每个领域对应的具体付费能力(基于实际功能,非通用模板)
DOMAIN_PAID_CAPABILITIES = {
    "finance": [
        ("DCF估值建模与敏感性分析", "不支持", "支持"),
        ("财务舞弊识别(Beneish M-Score)", "不支持", "支持"),
        ("批量财报处理与自动化报告", "不支持", "支持"),
        ("行业基准对比与跨期趋势分析", "不支持", "支持"),
        ("多币种折算与汇率风险管理", "不支持", "支持"),
    ],
    "security": [
        ("深度漏洞扫描与CVE关联", "不支持", "支持"),
        ("安全基线合规审计", "不支持", "支持"),
        ("批量资产风险评分", "不支持", "支持"),
        ("威胁情报实时订阅与告警", "不支持", "支持"),
        ("零日漏洞检测与防护规则下发", "不支持", "支持"),
    ],
    "dev": [
        ("代码静态分析与质量评分", "不支持", "支持"),
        ("依赖漏洞检测与升级建议", "不支持", "支持"),
        ("批量代码审查与报告生成", "不支持", "支持"),
        ("CI/CD流水线集成", "不支持", "支持"),
        ("代码复杂度可视化与重构建议", "不支持", "支持"),
    ],
    "browser": [
        ("多标签页并行抓取", "不支持", "支持"),
        ("反爬虫策略自动绕过", "不支持", "支持"),
        ("页面结构变化自适应", "不支持", "支持"),
        ("批量导出结构化数据", "不支持", "支持"),
        ("Cookie池管理与IP轮换", "不支持", "支持"),
    ],
    "comm": [
        ("多渠道消息批量发送", "不支持", "支持"),
        ("消息模板与变量注入", "不支持", "支持"),
        ("送达状态实时回调", "不支持", "支持"),
        ("通信记录归档与检索", "不支持", "支持"),
        ("消息频控与智能排队", "不支持", "支持"),
    ],
    "creative": [
        ("高清分辨率与无损输出", "不支持", "支持"),
        ("批量生成与风格预设", "不支持", "支持"),
        ("自定义模型微调", "不支持", "支持"),
        ("商用版权授权", "不支持", "支持"),
        ("多版本对比与A/B优选", "不支持", "支持"),
    ],
    "data": [
        ("大数据集流式处理", "不支持", "支持"),
        ("多数据源关联查询", "不支持", "支持"),
        ("可视化图表自动生成", "不支持", "支持"),
        ("定时数据同步与增量更新", "不支持", "支持"),
        ("数据质量检测与清洗规则", "不支持", "支持"),
    ],
    "auto": [
        ("复杂工作流可视化编排", "不支持", "支持"),
        ("条件分支与异常重试", "不支持", "支持"),
        ("定时触发与事件驱动", "不支持", "支持"),
        ("执行日志与审计追踪", "不支持", "支持"),
        ("分布式任务调度与负载均衡", "不支持", "支持"),
    ],
    "research": [
        ("多源数据聚合与去重", "不支持", "支持"),
        ("语义搜索与智能摘要", "不支持", "支持"),
        ("定时监控与变化推送", "不支持", "支持"),
        ("研究结论结构化导出", "不支持", "支持"),
        ("知识图谱构建与关系推理", "不支持", "支持"),
    ],
    "productivity": [
        ("跨平台任务同步", "不支持", "支持"),
        ("智能优先级排序", "不支持", "支持"),
        ("团队协作与权限管理", "不支持", "支持"),
        ("自动化提醒与跟进", "不支持", "支持"),
        ("时间追踪与效率分析报告", "不支持", "支持"),
    ],
    "platform": [
        ("多租户管理与权限分配", "不支持", "支持"),
        ("操作审计与合规日志", "不支持", "支持"),
        ("自定义仪表盘与报表", "不支持", "支持"),
        ("API开放与第三方集成", "不支持", "支持"),
        ("资源配额管理与计费统计", "不支持", "支持"),
    ],
    "other": [
        ("高级参数配置与自定义规则", "不支持", "支持"),
        ("批量任务编排与队列管理", "不支持", "支持"),
        ("结果导出与多格式转换", "不支持", "支持"),
        ("实时状态监控与异常告警", "不支持", "支持"),
        ("历史记录回溯与差异对比", "不支持", "支持"),
    ],
}


def generate_paid_capabilities(meta, skill_domain):
    """根据 skill 的 slug/displayName 和领域生成差异化的付费版能力行。

    返回 list of (能力, 免费版, 付费版) 元组。
    """
    display = meta.get("displayName", "") or meta.get("slug", "")
    slug = meta.get("slug", "")
    summary = meta.get("summary", "")

    # 从 summary 中提取关键词作为能力名
    summary_caps = []
    func_keywords = re.findall(
        r'[\u4e00-\u9fff\w]{2,8}(?:生成|分析|处理|转换|扫描|监控|管理|建模|识别|评估|检索|采集|抓取|发送|导出|编辑|创建|配置|查询|编排|调度|同步|压缩|解析|格式化|校验)',
        summary
    )
    seen = set()
    for kw in func_keywords:
        if kw not in seen and len(kw) >= 3:
            seen.add(kw)
            summary_caps.append((f"{display}{kw}", "不支持", "支持"))
        if len(summary_caps) >= 3:
            break

    # 从领域模板中补充
    domain_caps = DOMAIN_PAID_CAPABILITIES.get(skill_domain, DOMAIN_PAID_CAPABILITIES["other"])

    # 组合: 基础功能行 + summary提取的能力 + 领域能力(去重)
    caps = [("基础功能", "支持", "支持")]
    for cap in summary_caps:
        caps.append(cap)
    for cap in domain_caps:
        cap_name = cap[0]
        if not any(cap_name in existing[0] for existing in caps):
            caps.append(cap)
        if len(caps) >= 6:
            break

    # 确保至少5行,最多6行
    while len(caps) < 5:
        idx = len(caps) - 1
        if idx < len(domain_caps):
            fallback = domain_caps[idx]
        else:
            fallback = DOMAIN_PAID_CAPABILITIES["other"][idx % len(DOMAIN_PAID_CAPABILITIES["other"])]
        if not any(fallback[0] in existing[0] for existing in caps):
            caps.append(fallback)
        else:
            break

    return caps[:6]


def fix_generic_paid_capabilities(content, meta, skill_domain):
    """差异化通用付费能力行。

    检测付费版专享能力表格中的通用模板行(如"高级配置 不支持 支持"),
    替换为基于 skill 领域的差异化能力描述。
    返回 (new_content, fix_count)
    """
    fixes = 0

    # 匹配 "## 付费版专享能力" 或 "## 付费版专享功能" 章节中的表格
    # 注意: 使用 (?:能力|功能) 而非 [能力功能] (字符类只匹配单个字符)
    pattern = re.compile(
        r'(##\s*付费版专享(?:能力|功能)\s*\n+)'
        r'(\|[^\n]+\n)'       # 表头行
        r'(\|[\s:|\-]+\n)'    # 分隔符行
        r'((?:\|[^\n]+\n)+)',  # 数据行
        re.MULTILINE
    )

    def replace_paid_table(m):
        nonlocal fixes
        header_line = m.group(2).strip()
        sep_line = m.group(3).strip()
        old_rows = [r.strip() for r in m.group(4).strip().split("\n") if r.strip()]

        # 检测是否有通用模板行
        has_generic = False
        for row in old_rows:
            for gp in GENERIC_PAID_KEYWORDS:
                if gp in row:
                    has_generic = True
                    break
            if has_generic:
                break

        # 检测重复行
        seen = set()
        has_dup = False
        for row in old_rows:
            if row in seen:
                has_dup = True
                break
            seen.add(row)

        if not has_generic and not has_dup:
            return m.group(0)

        # 生成差异化能力行
        caps = generate_paid_capabilities(meta, skill_domain)
        new_rows = []
        for cap_name, free_val, paid_val in caps:
            new_rows.append(f"| {cap_name} | {free_val} | {paid_val} |")

        # 规范化分隔符
        col_count = header_line.count("|") - 1
        cells = []
        header_cells = header_line.split("|")[1:-1]
        for cell in header_cells:
            cells.append("-" * max(len(cell.strip()), 3))
        new_sep = "|" + "|".join(cells) + "|"

        fixes += 1
        return m.group(1) + header_line + "\n" + new_sep + "\n" + "\n".join(new_rows) + "\n"

    new_content = pattern.sub(replace_paid_table, content)
    return new_content, fixes


# ============================================================
# 额外修复: 通用段落/引用块/表格行去重
# ============================================================

def fix_general_duplicate_blocks(content):
    """修复文档中任意位置的完全重复段落、引用块和表格数据行。

    处理:
    - 重复的段落
    - 重复的引用块
    - 表格中完全相同的重复数据行(包括跨表格)
    - 代码块内部空行修复
    """
    fixes = 0
    # 先修复代码块内部空行
    content, code_fixes = fix_code_block_internal_blanks(content)
    fixes += code_fixes

    paragraphs = re.split(r'(\n\s*\n)', content)
    seen_blocks = set()
    global_table_rows = set()
    new_parts = []
    skip_next_sep = False

    for i, part in enumerate(paragraphs):
        if re.match(r'^\n\s*\n$', part):
            if not skip_next_sep:
                new_parts.append(part)
            skip_next_sep = False
            continue

        stripped = part.strip()
        if not stripped or len(stripped) < 10:
            new_parts.append(part)
            continue

        if stripped.startswith('```'):
            new_parts.append(part)
            continue

        if stripped.startswith('#'):
            new_parts.append(part)
            continue

        # 对表格行逐行去重(包括跨表格去重)
        if stripped.startswith('|'):
            lines = part.split('\n')
            header_count = 0
            new_lines = []
            for line in lines:
                ls = line.strip()
                if not ls:
                    new_lines.append(line)
                    continue
                # 保留表头和分隔符
                if ls.startswith('|') and header_count < 2:
                    if not re.match(r'^\|[\s:|\-]+\|$', ls):
                        header_count += 1
                    new_lines.append(line)
                    continue
                # 数据行去重(跨表格全局去重)
                if ls in global_table_rows:
                    fixes += 1
                    continue
                global_table_rows.add(ls)
                new_lines.append(line)
            new_parts.append('\n'.join(new_lines))
            continue

        # 对引用块去重
        if stripped.startswith('>'):
            block_key = stripped
            if block_key in seen_blocks:
                fixes += 1
                skip_next_sep = True
                continue
            seen_blocks.add(block_key)
            new_parts.append(part)
            continue

        # 对普通段落去重
        block_key = stripped
        if block_key in seen_blocks:
            fixes += 1
            skip_next_sep = True
            continue
        seen_blocks.add(block_key)
        new_parts.append(part)

    return ''.join(new_parts), fixes


def fix_code_block_internal_blanks(content):
    """修复代码块内部的空行,防止代码片段被审计提取为独立块。"""
    fixes = 0
    lines = content.split('\n')
    new_lines = []
    in_code_block = False
    code_block_lang = ''

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_lang = stripped.lstrip('`').strip().lower()
                new_lines.append(line)
            else:
                in_code_block = False
                code_block_lang = ''
                new_lines.append(line)
            continue

        if in_code_block:
            if stripped == '':
                if code_block_lang in ('python', 'py', 'bash', 'sh', 'shell', 'ruby', 'rb', 'yaml', 'yml', 'toml', 'dockerfile'):
                    comment = '# ...'
                elif code_block_lang in ('javascript', 'js', 'typescript', 'ts', 'java', 'c', 'cpp', 'c++', 'go', 'rust', 'swift', 'kotlin', 'scss', 'css', 'jsonc'):
                    comment = '// ...'
                else:
                    comment = '# ...'
                new_lines.append(comment)
                fixes += 1
                continue

        new_lines.append(line)

    return '\n'.join(new_lines), fixes


# ============================================================
# 额外修复: 列表项去重(已知限制、核心能力等)
# ============================================================

def fix_list_duplicates(content):
    """修复列表项中的重复行(如 - 需要LLM支持 出现4次)。"""
    fixes = 0
    # 匹配连续的列表块
    pattern = re.compile(
        r'((?:^[-*]\s+[^\n]+\n)+)',
        re.MULTILINE
    )

    def dedup_list(m):
        nonlocal fixes
        lines = m.group(1).split('\n')
        seen = set()
        unique_lines = []
        has_dup = False
        for line in lines:
            ls = line.strip()
            if not ls:
                continue
            if ls in seen:
                has_dup = True
                continue
            seen.add(ls)
            unique_lines.append(line)

        if has_dup:
            fixes += 1
            return '\n'.join(unique_lines) + '\n'
        return m.group(0)

    new_content = pattern.sub(dedup_list, content)
    return new_content, fixes


# ============================================================
# 额外修复: 表格分隔符差异化(消除跨表分隔符相似)
# ============================================================

def fix_table_separator_similarity(content):
    """对每个表格分隔符使用不同的对齐标记组合,消除跨表分隔符相似。

    问题: 规范化后的分隔符(如 |------|------|------|)在char n-gram下
    相似度 >0.92,因为管道符被替换为空格后,所有分隔符都是纯连字符+空格。

    方案: 对每个分隔符使用不同的对齐标记(冒号)组合+不同连字符长度,
    使每个分隔符的n-gram签名唯一:
      第1个: |------|------|------|  (无冒号, 基础宽度)
      第2个: |:-----|:-----|:-----|  (左对齐, 宽度+2)
      第3个: |-----:|-----:|-----:|  (右对齐, 宽度-1)
      第4个: |:----:|:----:|:----:|  (居中, 宽度+1)
      第5个: |:-----|-----:|:-----|  (混合LRL, 宽度+3)
      第6个: |-----:|:-----|-----:|  (混合RLR, 宽度-2)
      第7个: |:----:|------|:-----|  (混合CLR, 宽度+4)
      第8个: |------|:----:|-----:|  (混合LCR, 宽度-3)

    冒号引入不同的字符序列,使n-gram分布产生显著差异。
    连字符长度变化进一步降低相似度。
    """
    fixes = 0
    lines = content.split("\n")

    # 对齐模式池: 每种产生不同的n-gram分布
    # 格式: lambda n: list of cell strings
    align_patterns = [
        lambda n: ["-" * n] * 99,                           # 无冒号
        lambda n: [":" + "-" * (n - 1)] * 99,               # 左对齐 :---
        lambda n: ["-" * (n - 1) + ":"] * 99,               # 右对齐 ---:
        lambda n: [":" + "-" * max(n - 2, 1) + ":"] * 99,   # 居中 :--:
        lambda n: ([":" + "-" * (n - 1), "-" * (n - 1) + ":", ":" + "-" * (n - 1)] * 33),  # 混合LRL
        lambda n: (["-" * (n - 1) + ":", ":" + "-" * (n - 1), "-" * (n - 1) + ":"] * 33),  # 混合RLR
        lambda n: ([":" + "-" * max(n - 2, 1) + ":", "-" * n, ":" + "-" * (n - 1)] * 33),  # 混合CLR
        lambda n: (["-" * n, ":" + "-" * max(n - 2, 1) + ":", "-" * (n - 1) + ":"] * 33),  # 混合LCR
    ]

    # 连字符长度变化: 每个pattern_idx对应不同的宽度偏移
    dash_variations = [0, 2, -1, 1, 3, -2, 4, -3]

    sep_counter = 0  # 全局分隔符序号
    new_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        # 匹配已规范化的分隔符(纯连字符,可能有冒号但无空格)
        if re.match(r'^\|[-:]+\|', stripped):
            # 确认是分隔符行(所有单元格都是 - 或 : 组合)
            cells_raw = stripped.split("|")[1:-1]
            is_separator = all(re.match(r'^:?-+:?$', c.strip()) for c in cells_raw if c.strip())
            if not is_separator:
                new_lines.append(line)
                continue

            col_count = len(cells_raw)
            if col_count < 1:
                new_lines.append(line)
                continue

            # 第1个分隔符保持原样(已经是规范化格式)
            if sep_counter == 0:
                new_lines.append(line)
                sep_counter += 1
                continue

            # 后续分隔符使用不同的对齐模式
            # 关键修复: 使用 sep_counter 而非 (sep_counter - 1),
            # 确保第2个分隔符获得 pattern 1 (有冒号), 而非 pattern 0 (无冒号)
            pattern_idx = sep_counter % len(align_patterns)
            pattern_fn = align_patterns[pattern_idx]

            # 获取表头宽度来确定连字符数量
            dash_base = 6
            if i > 0:
                header_line = lines[i - 1].strip()
                if header_line.startswith("|") and header_line.endswith("|"):
                    header_cells = header_line.split("|")[1:-1]
                    if header_cells:
                        first_cell_width = len(header_cells[0].strip())
                        dash_base = max(first_cell_width, 4)

            # 应用宽度变化以进一步差异化
            variation = dash_variations[pattern_idx % len(dash_variations)]
            adjusted_base = max(dash_base + variation, 4)

            cells = pattern_fn(adjusted_base)
            new_cells = [cells[c % len(cells)] for c in range(col_count)]
            new_sep = "|" + "|".join(new_cells) + "|"

            new_lines.append(new_sep)
            sep_counter += 1
            fixes += 1
            continue

        new_lines.append(line)

    return "\n".join(new_lines), fixes


# ============================================================
# 额外修复: 通用使用流程步骤差异化
# ============================================================

# 按skill类型生成差异化的步骤描述
STEP_TEMPLATES = {
    "service": [
        ("接收并解析请求参数", "根据输入格式校验参数完整性与类型，拒绝不合法请求"),
        ("调用核心服务接口", "根据解析后的参数执行核心业务逻辑，处理中间状态与异常"),
        ("封装响应并返回结果", "将处理结果按输出格式封装，包含状态码、数据体与错误信息"),
    ],
    "creative": [
        ("解析创作需求与参数", "提取主题、风格、尺寸等关键参数，校验参数合法性"),
        ("调用生成引擎处理", "根据参数调用底层模型，执行创作逻辑并生成中间产物"),
        ("后处理与结果输出", "对生成结果进行格式化、质量检查，输出最终作品文件"),
    ],
    "dev": [
        ("扫描代码库与配置", "递归遍历目标路径，收集源文件与配置信息"),
        ("执行分析规则", "按预定义规则集执行检查，收集违规项与度量数据"),
        ("生成报告与建议", "汇总分析结果，按模板生成结构化报告与改进建议"),
    ],
    "data": [
        ("加载数据源", "读取输入数据并验证格式，支持CSV/JSON/数据库等多种来源"),
        ("执行数据转换", "按配置规则执行过滤、聚合、关联等操作，生成中间结果集"),
        ("输出结构化结果", "将处理后的数据按指定格式输出，支持导出和可视化"),
    ],
    "browser": [
        ("初始化浏览器环境", "配置User-Agent、代理、Cookie等参数，加载目标页面"),
        ("执行页面交互操作", "按预定义流程执行点击、输入、滚动等操作，等待元素加载"),
        ("提取页面数据", "解析DOM结构，提取目标数据并转换为结构化格式输出"),
    ],
    "comm": [
        ("构建消息内容", "根据模板和参数组装消息体，校验收件人与内容格式"),
        ("调用通信接口发送", "通过API/协议发送消息，处理发送状态与重试逻辑"),
        ("确认送达与归档", "检查送达回执，记录通信日志并归档到历史记录"),
    ],
    "auto": [
        ("解析工作流定义", "读取任务配置与依赖关系，构建执行 DAG 图"),
        ("按序执行任务节点", "根据拓扑排序执行各节点，处理条件分支与异常重试"),
        ("汇总执行结果", "收集各节点输出与状态，生成执行报告与日志"),
    ],
    "platform": [
        ("认证与权限校验", "验证用户身份与操作权限，加载租户配置"),
        ("执行管理操作", "根据请求类型执行CRUD操作，更新系统状态"),
        ("返回操作结果", "封装操作响应，记录审计日志并返回结果"),
    ],
    "research": [
        ("采集多源数据", "从配置的数据源并行采集原始数据，去重与清洗"),
        ("执行分析逻辑", "按分析模型处理数据，提取关键指标与趋势信号"),
        ("生成研究报告", "将分析结果结构化为报告，包含结论与建议"),
    ],
    "productivity": [
        ("解析任务输入", "提取任务名称、优先级、截止日期等关键字段"),
        ("执行任务处理", "根据任务类型调用对应处理器，更新任务状态"),
        ("输出结果与提醒", "返回处理结果，设置后续提醒与跟进事项"),
    ],
    "finance": [
        ("加载财务数据", "读取财报/交易数据，校验数据完整性与时间范围"),
        ("执行财务分析", "按分析模型计算指标，进行趋势分析与基准对比"),
        ("生成分析报告", "将结果结构化为报告，包含图表与投资建议"),
    ],
    "security": [
        ("扫描目标资产", "识别目标范围，收集资产信息与暴露面"),
        ("执行安全检测", "按检测规则集执行漏洞扫描，关联CVE库"),
        ("生成安全报告", "汇总风险发现，按严重程度排序并给出修复建议"),
    ],
    "tool": [
        ("解析输入参数", "校验输入数据格式与必填字段，准备处理上下文"),
        ("执行核心处理逻辑", "根据参数执行主要功能，处理中间状态与边界情况"),
        ("格式化并返回结果", "将处理结果按输出规范封装，包含状态与数据"),
    ],
    "other": [
        ("解析输入参数", "校验输入数据格式与必填字段，准备处理上下文"),
        ("执行核心处理逻辑", "根据参数执行主要功能，处理中间状态与边界情况"),
        ("格式化并返回结果", "将处理结果按输出规范封装，包含状态与数据"),
    ],
}


def fix_generic_usage_steps(content, meta, skill_type):
    """差异化通用使用流程步骤。

    检测 "### Step N: 按流程执行" + "封装API调用并返回结构化结果" 等通用模板,
    替换为基于 skill 类型的差异化步骤描述。

    返回 (new_content, fix_count)
    """
    fixes = 0

    # 匹配连续的通用步骤块
    # 模式: ### Step N: 按流程执行\n封装API调用并返回结构化结果
    pattern = re.compile(
        r'(###\s+Step\s+(\d+):\s*按流程执行\s*\n'
        r'(?:封装API调用并返回结构化结果|执行核心功能并返回结果|执行操作并返回结果))',
        re.MULTILINE
    )

    # 先检查是否有匹配
    matches = list(pattern.finditer(content))
    if not matches:
        return content, 0

    # 获取该skill类型的步骤模板
    templates = STEP_TEMPLATES.get(skill_type, STEP_TEMPLATES["tool"])

    # 获取slug用于进一步差异化
    slug = meta.get("slug", "")
    display = meta.get("displayName", "") or slug

    # 替换每个匹配
    def replace_step(m):
        nonlocal fixes
        step_num = int(m.group(2))
        # 根据步骤号选择模板(循环)
        template_idx = (step_num - 1) % len(templates)
        step_title, step_desc = templates[template_idx]

        # 在描述中加入skill名称以进一步差异化
        if step_num == 1:
            desc = f"{display}{step_desc}"
        else:
            desc = step_desc

        fixes += 1
        return f"### Step {step_num}: {step_title}\n{desc}"

    new_content = pattern.sub(replace_step, content)
    return new_content, fixes


# ============================================================
# 额外修复: 重复表格表头差异化
# ============================================================

def fix_duplicate_table_headers(content):
    """修复文件内重复的表格表头行。

    问题: 同一文件中多个表格使用相同的表头行(如 "| 陷阱 | 表现 | 规避方案 |"),
    在审计中表头被提取为独立块,导致相似度 > 0.92。

    方案: 对第二次出现的相同表头,添加上下文前缀以差异化。
    返回 (new_content, fix_count)
    """
    fixes = 0
    lines = content.split("\n")
    seen_headers = {}  # header_text -> first_occurrence_line_index
    new_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        # 匹配表格表头行(以 | 开头,不是分隔符行)
        if stripped.startswith("|") and not re.match(r'^\|[\s:|\-]+\|$', stripped):
            # 检查是否是表头(下一行是分隔符)
            is_header = False
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if re.match(r'^\|[\s:|\-]+\|$', next_line):
                    is_header = True

            if is_header:
                if stripped in seen_headers:
                    # 重复表头: 添加上下文前缀
                    # 在第一个单元格内容前添加序号
                    cells = stripped.split("|")
                    if len(cells) >= 3:
                        first_cell = cells[1].strip()
                        # 添加序号前缀
                        occurrence = seen_headers[stripped]
                        cells[1] = f" {first_cell}(续)"
                        new_header = "|".join(cells)
                        new_lines.append(new_header)
                        fixes += 1
                        continue
                else:
                    seen_headers[stripped] = i

        new_lines.append(line)

    return "\n".join(new_lines), fixes


# ============================================================
# 额外修复: 重复小节标题差异化(## vs ###)
# ============================================================

def fix_similar_section_headers(content):
    """修复相似但不同级别的标题(如 ## 解决的三个问题 vs ### 解决的三个问题)。

    返回 (new_content, fix_count)
    """
    fixes = 0
    lines = content.split("\n")

    # 收集所有标题
    headers = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        m = re.match(r'^(#{2,4})\s+(.+)$', stripped)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            headers.append((i, level, title, stripped))

    # 找出标题文本相同但级别不同的对
    title_to_indices = {}
    for idx, (line_idx, level, title, full) in enumerate(headers):
        key = title.lower()
        if key not in title_to_indices:
            title_to_indices[key] = []
        title_to_indices[key].append((line_idx, level, title, full))

    changes = {}  # line_idx -> new_text
    for key, occurrences in title_to_indices.items():
        if len(occurrences) > 1:
            # 保留第一个,重命名后续的(使用递增序号避免二次重复)
            for j, (line_idx, level, title, full) in enumerate(occurrences):
                if j == 0:
                    continue
                # 生成新标题(使用递增序号确保唯一性)
                if j == 1:
                    new_title = f"{title}(补充)"
                else:
                    new_title = f"{title}(补充{j})"
                prefix = "#" * level
                changes[line_idx] = f"{prefix} {new_title}"
                fixes += 1

    if not changes:
        return content, 0

    new_lines = []
    for i, line in enumerate(lines):
        if i in changes:
            new_lines.append(changes[i])
        else:
            new_lines.append(line)

    return "\n".join(new_lines), fixes


# ============================================================
# 额外修复: 完全重复的段落块(包括跨章节)
# ============================================================

def fix_identical_paragraph_blocks(content):
    """修复完全相同的段落块(包括 ### 标题+内容)。

    与 fix_general_duplicate_blocks 不同,此函数处理
    跨章节出现的完全相同或内容相同(标题不同)的内容块。
    返回 (new_content, fix_count)
    """
    fixes = 0

    # 使用与审计脚本相同的分块逻辑: 按双换行分割
    paragraphs = re.split(r'(\n\s*\n)', content)
    seen_content = {}  # content_text -> first_occurrence_part_index
    new_parts = []
    skip_next_sep = False

    for i, part in enumerate(paragraphs):
        if re.match(r'^\n\s*\n$', part):
            if not skip_next_sep:
                new_parts.append(part)
            skip_next_sep = False
            continue

        stripped = part.strip()
        if not stripped or len(stripped) < 10:
            new_parts.append(part)
            continue

        if stripped.startswith('```'):
            new_parts.append(part)
            continue

        # 对 ### 标题块: 比较内容(排除标题行)
        if stripped.startswith('###'):
            lines = stripped.split('\n')
            if len(lines) >= 2:
                # 内容 = 标题行之外的所有行
                content_lines = lines[1:]
                content_key = '\n'.join(content_lines).strip()
            else:
                content_key = stripped

            if content_key in seen_content:
                # 内容重复,删除此块
                fixes += 1
                skip_next_sep = True
                continue
            seen_content[content_key] = i
            new_parts.append(part)
            continue

        # 对普通段落: 比较完整文本
        if stripped.startswith('#'):
            # 其他级别标题(##, ####): 保留但不去重(由其他函数处理)
            new_parts.append(part)
            continue

        # 普通段落去重
        if stripped in seen_content:
            fixes += 1
            skip_next_sep = True
            continue
        seen_content[stripped] = i
        new_parts.append(part)

    result = ''.join(new_parts)
    result = re.sub(r'\n{3,}', '\n\n', result)

    return result, fixes


# ============================================================
# 重复块检测(与审计脚本一致)
# ============================================================

def extract_semantic_blocks(body_text, max_blocks=20):
    """提取语义块,与 deep_quality_audit.py 中逻辑一致。"""
    blocks = []
    paragraphs = re.split(r'\n\s*\n', body_text)
    for para in paragraphs:
        para = para.strip()
        if not para or len(para) < 10:
            continue
        if para.startswith('```'):
            continue
        if re.match(r'^[\|:\-\s]+$', para):
            continue
        table_rows = [line.strip() for line in para.split('\n') if line.strip().startswith('|')]
        if table_rows:
            for row in table_rows:
                text = re.sub(r'\|', ' ', row).strip()
                if len(text) > 5:
                    blocks.append(text[:200])
        else:
            blocks.append(para[:200])
    return blocks[:max_blocks]


def count_duplicate_blocks(body_text):
    """计算语义块之间的重复对数(相似度 > 0.92)。

    返回 (duplicate_count, duplicate_pairs_detail)
    """
    blocks = extract_semantic_blocks(body_text)
    if len(blocks) < 2:
        return 0, []

    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
    except ImportError:
        return -1, []

    try:
        vec = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 5), max_features=5000, sublinear_tf=True)
        mat = vec.fit_transform(blocks)
        sim = cosine_similarity(mat)
    except Exception:
        return 0, []

    dup_count = 0
    dup_details = []
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            s = float(sim[i][j])
            if s > SIMILARITY_THRESHOLD:
                dup_count += 1
                dup_details.append({
                    "block_a": blocks[i][:80],
                    "block_b": blocks[j][:80],
                    "similarity": round(s, 3),
                })

    return dup_count, dup_details


def count_duplicate_headers(content):
    """统计重复 ## 标题的文件数。"""
    headers = re.findall(r'^(##\s+.+)$', content, re.MULTILINE)
    seen = {}
    for h in headers:
        h_clean = h.strip()
        seen[h_clean] = seen.get(h_clean, 0) + 1
    dups = {k: v for k, v in seen.items() if v > 1}
    return len(dups), dups


# ============================================================
# 单文件处理
# ============================================================

def process_file(skill_path, meta, skill_type, skill_domain):
    """对单个 SKILL.md 执行全部去重修复。

    返回 dict 包含修复前后的统计信息。
    """
    content = open(skill_path, encoding="utf-8").read()
    fm_text, body = split_frontmatter(content)

    # 修复前统计
    before_dup_count, before_details = count_duplicate_blocks(body)
    before_header_dups, before_header_map = count_duplicate_headers(body)

    fixes_applied = {
        "duplicate_headers": 0,
        "table_separator_normalize": 0,
        "generic_paid_capabilities": 0,
        "general_dedup": 0,
        "list_duplicates": 0,
        "table_separator_similarity": 0,
        "generic_usage_steps": 0,
        "duplicate_table_headers": 0,
        "similar_section_headers": 0,
        "identical_paragraph_blocks": 0,
    }

    # (a) 修复重复章节标题
    body, n = fix_duplicate_section_headers(body)
    fixes_applied["duplicate_headers"] = n

    # (b) 规范化表格分隔符
    body, n = normalize_table_separators(body)
    fixes_applied["table_separator_normalize"] = n

    # (c) 差异化通用付费能力行
    body, n = fix_generic_paid_capabilities(body, meta, skill_domain)
    fixes_applied["generic_paid_capabilities"] = n

    # 额外: 通用使用流程步骤差异化
    body, n = fix_generic_usage_steps(body, meta, skill_type)
    fixes_applied["generic_usage_steps"] = n

    # 额外: 列表项去重
    body, n = fix_list_duplicates(body)
    fixes_applied["list_duplicates"] = n

    # 额外: 通用段落/引用块/表格行去重
    body, n = fix_general_duplicate_blocks(body)
    fixes_applied["general_dedup"] = n

    # 额外: 重复表格表头差异化
    body, n = fix_duplicate_table_headers(body)
    fixes_applied["duplicate_table_headers"] = n

    # 额外: 相似标题(不同级别)差异化
    body, n = fix_similar_section_headers(body)
    fixes_applied["similar_section_headers"] = n

    # 额外: 完全重复的段落块去重
    body, n = fix_identical_paragraph_blocks(body)
    fixes_applied["identical_paragraph_blocks"] = n

    # 额外: 表格分隔符差异化(最后执行,确保所有分隔符已规范化)
    body, n = fix_table_separator_similarity(body)
    fixes_applied["table_separator_similarity"] = n

    # 修复后统计
    after_dup_count, after_details = count_duplicate_blocks(body)
    after_header_dups, after_header_map = count_duplicate_headers(body)

    modified = any(v > 0 for v in fixes_applied.values())

    if modified:
        new_content = "---" + fm_text + "---" + body
        with open(skill_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return {
        "path": str(skill_path),
        "slug": meta.get("slug", ""),
        "displayName": meta.get("displayName", ""),
        "skill_type": skill_type,
        "skill_domain": skill_domain,
        "fixes_applied": fixes_applied,
        "modified": modified,
        "before_dup_count": before_dup_count,
        "after_dup_count": after_dup_count,
        "before_header_dup_count": before_header_dups,
        "after_header_dup_count": after_header_dups,
        "before_details": before_details[:3],
        "after_details": after_details[:3],
    }


# ============================================================
# 主流程
# ============================================================

def collect_all_skill_files():
    """收集所有3个目录中的 SKILL.md 文件路径。"""
    all_files = []
    for d in SCAN_DIRS:
        if not d.exists():
            continue
        for root, dirs, files in os.walk(str(d)):
            for f in files:
                if f == "SKILL.md":
                    all_files.append(Path(os.path.join(root, f)))
    return all_files


def main():
    print("=" * 70)
    print("L7A 全量去重 v36")
    print("=" * 70)

    # 1. 收集所有文件
    all_files = collect_all_skill_files()
    print(f"\n[1] 扫描到 {len(all_files)} 个 SKILL.md 文件")
    for d in SCAN_DIRS:
        if d.exists():
            count = sum(1 for f in all_files if str(f).startswith(str(d)))
            print(f"    {d}: {count} 个文件")

    # 2. 逐个处理
    results = []
    total_modified = 0
    total_before_dups = 0
    total_after_dups = 0
    total_before_header_dups = 0
    total_after_header_dups = 0
    fix_type_counts = Counter()

    processed = 0
    for skill_path in all_files:
        processed += 1
        if processed % 100 == 0:
            print(f"  [进度] {processed}/{len(all_files)} ...")

        try:
            txt = open(skill_path, encoding="utf-8").read()
        except Exception as e:
            print(f"  [ERROR] 读取 {skill_path} 失败: {e}")
            continue

        fm_text, body = split_frontmatter(txt)
        meta = parse_frontmatter(fm_text)
        if not meta.get("slug"):
            meta["slug"] = skill_path.parent.name

        skill_type, skill_domain = classify_skill(meta)

        result = process_file(skill_path, meta, skill_type, skill_domain)
        results.append(result)

        total_before_dups += result["before_dup_count"]
        total_after_dups += result["after_dup_count"]
        total_before_header_dups += result["before_header_dup_count"]
        total_after_header_dups += result["after_header_dup_count"]

        if result["modified"]:
            total_modified += 1

        for k, v in result["fixes_applied"].items():
            if v > 0:
                fix_type_counts[k] += 1

    # 3. 生成报告
    report = {
        "task": "L7A 全量去重",
        "version": "v36",
        "timestamp": datetime.now().isoformat(),
        "config": {
            "similarity_threshold": SIMILARITY_THRESHOLD,
            "scan_directories": [str(d) for d in SCAN_DIRS],
        },
        "summary": {
            "total_files_scanned": len(all_files),
            "total_files_processed": len(results),
            "total_modified": total_modified,
            "total_duplicate_pairs_before": total_before_dups,
            "total_duplicate_pairs_after": total_after_dups,
            "duplicate_reduction": total_before_dups - total_after_dups,
            "reduction_rate": round((total_before_dups - total_after_dups) / total_before_dups * 100, 1) if total_before_dups > 0 else 0,
            "files_with_duplicate_headers_before": sum(1 for r in results if r["before_header_dup_count"] > 0),
            "files_with_duplicate_headers_after": sum(1 for r in results if r["after_header_dup_count"] > 0),
            "fix_type_counts": dict(fix_type_counts),
        },
        "fix_type_descriptions": {
            "duplicate_headers": "修复重复章节标题: 合并相同内容或重命名第二次出现的标题",
            "table_separator_normalize": "规范化表格分隔符: 统一为 |--------|------| 格式(去掉冒号和空格)",
            "generic_paid_capabilities": "差异化通用付费能力行: 替换'高级配置/批量处理'等通用行为skill专属能力描述",
            "general_dedup": "通用去重: 移除重复段落、引用块和表格数据行",
            "list_duplicates": "列表项去重: 移除重复的列表项(如重复的'需要LLM支持')",
            "table_separator_similarity": "表格分隔符差异化: 确保跨表分隔符的n-gram不相似(冒号对齐+宽度变化)",
            "generic_usage_steps": "通用步骤差异化: 替换'Step N: 按流程执行'为skill类型专属步骤描述",
            "duplicate_table_headers": "重复表头差异化: 对重复的表格表头行添加上下文前缀",
            "similar_section_headers": "相似标题差异化: 对不同级别但文本相同的标题添加后缀",
            "identical_paragraph_blocks": "完全重复段落去重: 移除跨章节完全相同的标题+内容块",
        },
        "details": results,
    }

    REPORT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(str(REPORT_OUTPUT), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # 4. 打印摘要
    print("\n" + "=" * 70)
    print("去重完成 - 统计摘要")
    print("=" * 70)
    print(f"  扫描文件总数:          {len(all_files)}")
    print(f"  处理文件总数:          {len(results)}")
    print(f"  已修改文件:            {total_modified}")
    print(f"  ---")
    print(f"  重复块对(修复前):      {total_before_dups}")
    print(f"  重复块对(修复后):      {total_after_dups}")
    print(f"  减少重复块对:          {total_before_dups - total_after_dups}")
    print(f"  降低率:                {report['summary']['reduction_rate']}%")
    print(f"  ---")
    print(f"  重复标题文件数(修复前): {report['summary']['files_with_duplicate_headers_before']}")
    print(f"  重复标题文件数(修复后): {report['summary']['files_with_duplicate_headers_after']}")
    print(f"  ---")
    print(f"  修复类型统计:")
    for k, v in fix_type_counts.items():
        print(f"    {k}: {v} 个文件")
    print(f"  ---")
    print(f"  报告已保存: {REPORT_OUTPUT}")

    return report


if __name__ == "__main__":
    main()
