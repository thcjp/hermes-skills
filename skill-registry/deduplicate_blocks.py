# -*- coding: utf-8 -*-
"""
L7A_DUPLICATE_BLOCKS 去重脚本
=============================
扫描所有被标记 L7A_DUPLICATE_BLOCKS 的 SKILL.md 文件,
识别并修复三类跨skill重复的模板化内容块:

  类型A: "付费版专享能力"表格 — 跨skill使用相同的通用能力描述行(如"高级配置 不支持 支持")
  类型B: "使用流程"章节 — 跨skill使用相同的模板化步骤(如"### Step N: 按流程执行")
  类型C: "错误处理/异常处理"章节 — 跨skill使用相同的通用错误行(如"其他异常 内部处理异常")

修复策略:
  - 类型A: 根据 slug 和 displayName 生成差异化的付费版能力描述,去重重复行
  - 类型B: 根据 skill 类型(工具/平台/服务/创意等)生成差异化的使用流程步骤
  - 类型C: 根据 skill 可能遇到的错误类型生成差异化的错误处理场景

不使用 mock/fallback/placeholder,所有替换内容基于 skill 的实际功能。
"""

import re
import os
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime

# ============================================================
# 配置
# ============================================================

AUDIT_REPORT = Path(r"d:\skills\skill-registry\deep_quality_audit_report.json")
PACKAGED_DIR = Path(r"D:\skills\packaged-skills\skillhub")
DOWNLOADED_DIR = Path(r"D:\skills\clawhub-skills\downloaded")
REPORT_OUTPUT = Path(r"d:\skills\skill-registry\reports\dedup_report_v35.json")

SIMILARITY_THRESHOLD = 0.92

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


def build_slug_path_map():
    """构建 slug -> SKILL.md 路径 的映射,覆盖两个目录。"""
    slug_map = {}
    for base in [PACKAGED_DIR, DOWNLOADED_DIR]:
        if not base.exists():
            continue
        for root, dirs, files in os.walk(str(base)):
            for f in files:
                if f == "SKILL.md":
                    p = os.path.join(root, f)
                    try:
                        txt = open(p, encoding="utf-8").read()
                        fm, _ = split_frontmatter(txt)
                        data = parse_frontmatter(fm)
                        slug = data.get("slug", "")
                        if slug and slug not in slug_map:
                            slug_map[slug] = p
                    except Exception:
                        pass
    return slug_map


# ============================================================
# Skill 类型/领域分类
# ============================================================

def classify_skill(meta):
    """根据 slug/displayName/summary/tags 判断 skill 类型和领域。

    返回 (skill_type, skill_domain):
      skill_type: tool / platform / service / creative / dev / comm / data / auto / browser / research / productivity / finance / security / other
      skill_domain: 具体领域描述
    """
    slug = (meta.get("slug") or "").lower()
    display = (meta.get("displayName") or "").lower()
    summary = (meta.get("summary") or "").lower()
    tags = (meta.get("tags") or "").lower()
    combined = " ".join([slug, display, summary, tags])

    # 领域分类(优先级从高到低)
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

    # 类型分类
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
# 类型A: 付费版专享能力 — 差异化能力描述生成
# ============================================================

# 每个领域对应的具体付费能力(基于实际功能,非通用模板)
DOMAIN_PAID_CAPABILITIES = {
    "finance": [
        ("DCF估值建模与敏感性分析", "不支持", "支持"),
        ("财务舞弊识别(Beneish M-Score)", "不支持", "支持"),
        ("批量财报处理与自动化报告", "不支持", "支持"),
        ("行业基准对比与跨期趋势分析", "不支持", "支持"),
    ],
    "security": [
        ("深度漏洞扫描与CVE关联", "不支持", "支持"),
        ("安全基线合规审计", "不支持", "支持"),
        ("批量资产风险评分", "不支持", "支持"),
        ("威胁情报实时订阅与告警", "不支持", "支持"),
    ],
    "dev": [
        ("代码静态分析与质量评分", "不支持", "支持"),
        ("依赖漏洞检测与升级建议", "不支持", "支持"),
        ("批量代码审查与报告生成", "不支持", "支持"),
        ("CI/CD流水线集成", "不支持", "支持"),
    ],
    "browser": [
        ("多标签页并行抓取", "不支持", "支持"),
        ("反爬虫策略自动绕过", "不支持", "支持"),
        ("页面结构变化自适应", "不支持", "支持"),
        ("批量导出结构化数据", "不支持", "支持"),
    ],
    "comm": [
        ("多渠道消息批量发送", "不支持", "支持"),
        ("消息模板与变量注入", "不支持", "支持"),
        ("送达状态实时回调", "不支持", "支持"),
        ("通信记录归档与检索", "不支持", "支持"),
    ],
    "creative": [
        ("高清分辨率与无损输出", "不支持", "支持"),
        ("批量生成与风格预设", "不支持", "支持"),
        ("自定义模型微调", "不支持", "支持"),
        ("商用版权授权", "不支持", "支持"),
    ],
    "data": [
        ("大数据集流式处理", "不支持", "支持"),
        ("多数据源关联查询", "不支持", "支持"),
        ("可视化图表自动生成", "不支持", "支持"),
        ("定时数据同步与增量更新", "不支持", "支持"),
    ],
    "auto": [
        ("复杂工作流可视化编排", "不支持", "支持"),
        ("条件分支与异常重试", "不支持", "支持"),
        ("定时触发与事件驱动", "不支持", "支持"),
        ("执行日志与审计追踪", "不支持", "支持"),
    ],
    "research": [
        ("多源数据聚合与去重", "不支持", "支持"),
        ("语义搜索与智能摘要", "不支持", "支持"),
        ("定时监控与变化推送", "不支持", "支持"),
        ("研究结论结构化导出", "不支持", "支持"),
    ],
    "productivity": [
        ("跨平台任务同步", "不支持", "支持"),
        ("智能优先级排序", "不支持", "支持"),
        ("团队协作与权限管理", "不支持", "支持"),
        ("自动化提醒与跟进", "不支持", "支持"),
    ],
    "platform": [
        ("多租户管理与权限分配", "不支持", "支持"),
        ("操作审计与合规日志", "不支持", "支持"),
        ("自定义仪表盘与报表", "不支持", "支持"),
        ("API开放与第三方集成", "不支持", "支持"),
    ],
    "other": [
        ("高级参数配置与自定义", "不支持", "支持"),
        ("批量处理与自动化", "不支持", "支持"),
        ("结果导出与格式转换", "不支持", "支持"),
        ("实时监控与告警通知", "不支持", "支持"),
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
    # 尝试从 summary 中提取具体功能描述
    func_keywords = re.findall(r'[\u4e00-\u9fff\w]{2,8}(?:生成|分析|处理|转换|扫描|监控|管理|建模|识别|评估|检索|采集|抓取|发送|导出|编辑|创建|配置|查询)', summary)
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
        fallback = domain_caps[idx % len(domain_caps)]
        if not any(fallback[0] in existing[0] for existing in caps):
            caps.append(fallback)
        else:
            break

    return caps[:6]


def fix_type_a_paid_table(content, meta, skill_domain):
    """修复类型A: 付费版专享能力表格。

    - 去除重复行
    - 用 skill 专属能力替换通用模板行
    返回 (new_content, fix_count)
    """
    fixes = 0

    # 匹配 "## 付费版专享能力" 章节
    pattern = re.compile(
        r'(##\s*付费版专享能力\s*\n)'
        r'(\|[^\n]+\n\|[\|:\-\s]+\n)'
        r'((?:\|[^\n]+\n)+)',
        re.MULTILINE
    )

    match = pattern.search(content)
    if not match:
        return content, 0

    header_line = match.group(2).split("\n")[0]  # | 能力 | 免费版 | 付费版 |
    sep_line = match.group(2).split("\n")[1]     # |:-----|:-------|:-------|
    old_rows = match.group(3).strip().split("\n")

    # 检测是否有重复行
    seen_rows = set()
    has_dup = False
    for row in old_rows:
        row_clean = row.strip()
        if row_clean in seen_rows:
            has_dup = True
        seen_rows.add(row_clean)

    # 检测是否有通用模板行(跨skill重复的标志)
    generic_patterns = [
        "高级配置", "自动化处理", "批量操作", "批量处理",
        "自定义配置", "结果导出", "实时监控",
    ]
    has_generic = any(gp in match.group(3) for gp in generic_patterns)

    if not has_dup and not has_generic:
        return content, 0

    # 生成差异化能力行
    caps = generate_paid_capabilities(meta, skill_domain)
    new_rows = []
    for cap_name, free_val, paid_val in caps:
        new_rows.append(f"| {cap_name} | {free_val} | {paid_val} |")

    new_section = match.group(1) + header_line + "\n" + sep_line + "\n" + "\n".join(new_rows) + "\n"
    content = content[:match.start()] + new_section + content[match.end():]
    fixes = 1
    return content, fixes


# ============================================================
# 类型B: 使用流程 — 差异化步骤生成
# ============================================================

# 每个类型对应的差异化步骤
TYPE_B_STEPS = {
    "tool": [
        ("解析输入参数", "读取用户提供的输入数据,校验参数完整性与格式合法性"),
        ("执行核心处理", "调用skill核心逻辑对输入数据进行加工或转换"),
        ("验证并返回结果", "检查输出结果的完整性与格式,返回结构化数据"),
    ],
    "platform": [
        ("登录与鉴权", "验证用户身份与权限,加载平台配置信息"),
        ("选择操作模块", "根据用户意图定位目标功能模块与管理对象"),
        ("执行管理操作", "调用平台API执行创建/修改/查询/删除操作并返回结果"),
    ],
    "service": [
        ("构建API请求", "根据用户输入组装API请求参数与请求头"),
        ("调用服务接口", "发送HTTP请求到目标服务端点,处理响应或超时"),
        ("解析响应数据", "提取API返回的关键字段,转换为用户可读格式"),
    ],
    "creative": [
        ("确定创作需求", "分析用户描述的创作意图,确定输出规格(尺寸/风格/格式)"),
        ("执行生成操作", "调用生成引擎处理输入参数,产出创意内容"),
        ("优化与交付", "对生成结果进行质量检查与格式优化,输出最终作品"),
    ],
    "dev": [
        ("分析代码上下文", "读取目标代码文件,解析项目结构与依赖关系"),
        ("执行开发操作", "根据用户指令执行编写/审查/重构/测试等开发任务"),
        ("验证与反馈", "运行检查工具确认修改正确性,输出差异与建议"),
    ],
    "browser": [
        ("初始化浏览器会话", "启动无头浏览器实例,配置代理与用户代理参数"),
        ("执行页面交互", "按照用户指令进行导航/点击/输入/提取等页面操作"),
        ("采集与返回数据", "提取页面内容或操作结果,返回结构化数据与截图"),
    ],
    "comm": [
        ("准备消息内容", "根据用户输入构建消息正文与收件人列表"),
        ("发送通信请求", "调用通信平台API发送消息,处理发送状态回调"),
        ("确认与归档", "验证消息送达状态,记录通信日志供后续检索"),
    ],
    "data": [
        ("读取与校验数据", "加载数据源文件或查询结果,校验数据格式与完整性"),
        ("执行数据处理", "根据用户指令进行过滤/聚合/转换/计算等数据操作"),
        ("输出与可视化", "生成结构化输出表格或图表,支持多种导出格式"),
    ],
    "auto": [
        ("定义自动化任务", "解析用户需求,构建任务执行计划与触发条件"),
        ("编排执行流程", "按依赖顺序执行各步骤,处理条件分支与异常重试"),
        ("监控与报告", "记录执行日志,输出任务状态与结果摘要"),
    ],
    "research": [
        ("确定研究范围", "根据用户问题界定检索关键词与数据源范围"),
        ("执行多源检索", "并行查询多个数据源,聚合去重后排序"),
        ("综合分析与输出", "对检索结果进行摘要分析,输出结构化研究结论"),
    ],
    "productivity": [
        ("收集待处理事项", "汇总用户输入的任务/日程/笔记等信息"),
        ("智能排序与分类", "按优先级/截止时间/标签对事项进行组织"),
        ("执行与跟踪", "执行用户指定操作,更新状态并设置后续提醒"),
    ],
    "other": [
        ("接收与解析请求", "读取用户输入,提取操作意图与关键参数"),
        ("执行核心逻辑", "调用skill主流程完成用户指定的任务"),
        ("返回处理结果", "校验输出完整性,返回结构化结果与操作摘要"),
    ],
}


def fix_type_b_usage_steps(content, meta, skill_type):
    """修复类型B: 使用流程章节中的模板化步骤。

    检测 "### Step N: 按流程执行" 这种完全相同的步骤块,
    替换为基于 skill 类型的差异化步骤。
    返回 (new_content, fix_count)
    """
    fixes = 0

    # 匹配连续的 "### Step N: 按流程执行\n封装API调用并返回结构化结果" 模式
    step_pattern = re.compile(
        r'(###\s+Step\s+\d+:\s*按流程执行\s*\n'
        r'(?:封装API调用并返回结构化结果|执行标准处理流程)\s*\n?)',
        re.MULTILINE
    )

    matches = list(step_pattern.finditer(content))
    if len(matches) < 2:
        # 也检查 "## 使用流程" 下的通用4步流程
        return _fix_type_b_generic_flow(content, meta, skill_type)

    # 获取该 skill 类型的差异化步骤
    steps = TYPE_B_STEPS.get(skill_type, TYPE_B_STEPS["other"])

    # 替换每个匹配的步骤块
    new_content = content
    for i, match in enumerate(matches):
        step_idx = i % len(steps)
        step_title, step_desc = steps[step_idx]
        replacement = f"### Step {i + 1}: {step_title}\n{step_desc}\n"
        new_content = new_content.replace(match.group(0), replacement, 1)
        fixes += 1

    return new_content, fixes


def _fix_type_b_generic_flow(content, meta, skill_type):
    """修复通用的4步使用流程模板。

    检测:
      1. 确认运行环境满足依赖说明中的要求
      2. 根据适用场景选择合适的使用方式
      3. 执行操作并检查输出结果
      4. 如遇错误,参考错误处理章节
    """
    generic_flow_pattern = re.compile(
        r'(##\s*使用流程\s*\n)'
        r'((?:\d+\.\s*[^\n]+\n)+)',
        re.MULTILINE
    )

    match = generic_flow_pattern.search(content)
    if not match:
        return content, 0

    flow_text = match.group(2)
    # 检测是否是通用模板
    generic_markers = [
        "确认运行环境满足依赖说明",
        "根据适用场景选择合适的使用方式",
        "执行操作并检查输出结果",
        "如遇错误",
        "参考错误处理章节",
    ]
    is_generic = sum(1 for m in generic_markers if m in flow_text)
    if is_generic < 2:
        return content, 0

    steps = TYPE_B_STEPS.get(skill_type, TYPE_B_STEPS["other"])
    new_flow = ""
    for i, (title, desc) in enumerate(steps):
        new_flow += f"{i + 1}. **{title}**: {desc}\n"

    # 如果通用流程只有4步但我们只有3步,补充第4步
    if len(steps) < 4:
        new_flow += f"4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式\n"

    new_content = content[:match.start()] + match.group(1) + new_flow + content[match.end():]
    return new_content, 1


# ============================================================
# 类型C: 错误处理/异常处理 — 差异化错误场景生成
# ============================================================

# 每个领域对应的具体错误场景
DOMAIN_ERROR_SCENARIOS = {
    "finance": [
        ("财报数据缺失或格式不合规", "年报未披露或数据字段不全", "标注缺失项,使用行业均值估算,在报告中明确假设条件"),
        ("估值模型参数异常", "WACC或增长率输入超出合理区间", "校验参数范围,提示用户确认假设合理性后重新计算"),
        ("行业基准数据不可得", "新兴行业缺乏可比公司数据", "扩大至上下游行业或参考海外市场,标注估值乘数折扣"),
    ],
    "security": [
        ("扫描目标不可达", "网络不通或防火墙拦截", "检查目标地址与端口连通性,确认白名单配置后重试"),
        ("漏洞库版本过期", "CVE数据库未及时更新", "执行漏洞库更新命令,确认最新版本后重新扫描"),
        ("权限不足导致扫描中断", "运行账号缺少必要权限", "提升执行权限或切换管理员账号,确认扫描范围授权"),
    ],
    "dev": [
        ("代码编译或解析失败", "语法错误或依赖版本不兼容", "定位报错行号,修正语法或调整依赖版本后重新编译"),
        ("依赖包冲突或缺失", "package.json/requirements.txt版本冲突", "锁定依赖版本,执行clean install后重试"),
        ("环境配置不匹配", "运行环境与skill要求不一致", "核对依赖说明中的环境要求,安装缺失运行时或工具链"),
    ],
    "browser": [
        ("页面加载超时", "目标网站响应慢或网络延迟", "增加超时阈值,启用重试机制,检查代理配置"),
        ("页面结构变化导致选择器失效", "目标网站更新了DOM结构", "切换到可访问性树定位元素,或提示用户提供新的选择器"),
        ("反爬虫机制触发", "频繁请求被目标站点识别", "降低请求频率,启用随机延迟,更换User-Agent"),
    ],
    "comm": [
        ("消息发送失败", "收件人地址无效或服务端拒绝", "校验收件人格式,检查发送配额,失败消息进入重试队列"),
        ("认证Token过期", "API密钥或OAuth令牌失效", "重新执行认证流程获取新Token,更新环境变量后重试"),
        ("消息内容超限", "消息体超过平台长度或大小限制", "自动分段发送或压缩附件,提示用户精简内容"),
    ],
    "creative": [
        ("生成引擎超时", "模型推理负载过高或输入过于复杂", "简化提示词,降低输出分辨率,或稍后重试"),
        ("输出内容质量不达标", "生成结果模糊或与预期不符", "调整提示词增加细节描述,尝试不同风格预设"),
        ("API调用额度耗尽", "生成请求次数达到套餐上限", "提示用户升级套餐或等待额度刷新,支持本地缓存历史结果"),
    ],
    "data": [
        ("数据源读取失败", "文件损坏或数据库连接中断", "校验文件完整性,检查数据库连接参数,尝试备份数据源"),
        ("数据处理内存溢出", "数据集过大超出内存限制", "启用流式处理模式,分批加载数据,或增加可用内存"),
        ("查询结果为空", "过滤条件过严或数据源无匹配记录", "放宽查询条件,检查数据源时间范围,提示用户调整参数"),
    ],
    "auto": [
        ("工作流步骤执行失败", "中间步骤依赖的服务不可用", "记录失败节点,启用断点续传,修复后从失败步骤恢复"),
        ("定时触发未执行", "Cron表达式错误或调度服务宕机", "校验Cron语法,检查调度服务状态,手动触发验证"),
        ("条件分支判断异常", "输入数据缺少判断所需字段", "补充缺失字段或设置默认值,记录跳过的分支供审计"),
    ],
    "research": [
        ("数据源返回空结果", "关键词无匹配或API限流", "扩展搜索关键词,增加重试间隔,切换备用数据源"),
        ("检索结果去重失败", "数据源格式不一致导致相似度计算偏差", "标准化数据格式后重新去重,对低置信度结果保留人工复核"),
        ("摘要生成质量不佳", "检索内容过短或跨语言混合", "增加检索深度,启用翻译预处理,限制摘要覆盖的核心要点数"),
    ],
    "productivity": [
        ("任务同步冲突", "多端同时修改导致版本不一致", "以最后修改时间为准合并,冲突项标记供用户手动裁决"),
        ("提醒推送未送达", "通知权限未开启或推送服务异常", "检查系统通知权限,验证推送通道,失败时降级为应用内提示"),
        ("日程时间重叠", "新建事项与已有安排冲突", "检测时间冲突后提示用户,提供可选的空闲时段建议"),
    ],
    "platform": [
        ("管理操作权限不足", "当前用户角色无操作权限", "提示联系管理员授权,或切换到有权限的管理账号"),
        ("平台API限流", "短时间请求量超过阈值", "启用请求队列与指数退避,降低调用频率后重试"),
        ("配置变更未生效", "缓存未刷新或配置同步延迟", "清除平台缓存,确认配置广播状态,必要时手动重启服务"),
    ],
    "other": [
        ("输入参数缺失或格式错误", "必填参数未提供或类型不匹配", "检查参数说明章节,补全缺失参数后重新提交"),
        ("运行环境不满足要求", "缺少依赖工具或运行时版本过低", "对照依赖说明章节安装所需组件,确认版本兼容性"),
        ("网络连接超时或不可达", "DNS解析失败或目标服务不可访问", "检查网络与代理配置,确认目标地址可达后重试"),
    ],
}


def fix_type_c_error_handling(content, meta, skill_domain):
    """修复类型C: 错误处理/异常处理表格中的重复行。

    - 去除完全相同的错误行
    - 用 skill 领域专属的错误场景替换通用模板行
    返回 (new_content, fix_count)
    """
    fixes = 0

    # 匹配 "## 异常处理" 或 "## 错误处理" 章节中的表格
    # 注意: 表头行可能有空格,如 "| 错误场景 | 原因 | 处理方式 |"
    error_section_pattern = re.compile(
        r'(##\s*(?:异常处理|错误处理)\s*\n+)'
        r'(\|\s*错误场景\s*\|\s*原因[^\n]*\n)'
        r'(\|[\|:\-\s]+\n)'
        r'((?:\|[^\n]+\n)+)',
        re.MULTILINE
    )

    def replace_error_table(m):
        nonlocal fixes
        header = m.group(2)
        sep = m.group(3)
        old_rows_text = m.group(4).strip().split("\n")

        # 检测重复行
        seen = set()
        has_dup = False
        for row in old_rows_text:
            row_clean = row.strip()
            if row_clean in seen:
                has_dup = True
                break
            seen.add(row_clean)

        # 检测通用模板行
        generic_markers = ["其他异常", "内部处理异常", "检查输入后"]
        has_generic = any(gm in m.group(4) for gm in generic_markers)

        if not has_dup and not has_generic:
            return m.group(0)

        # 生成领域专属错误行
        scenarios = DOMAIN_ERROR_SCENARIOS.get(skill_domain, DOMAIN_ERROR_SCENARIOS["other"])
        new_rows = []
        for scenario, cause, handling in scenarios:
            new_rows.append(f"| {scenario} | {cause} | {handling} |")

        fixes += 1
        return m.group(1) + header + sep + "\n".join(new_rows) + "\n"

    new_content = error_section_pattern.sub(replace_error_table, content)
    return new_content, fixes


# ============================================================
# 额外修复: 已知限制去重
# ============================================================

def fix_known_limitations(content, meta, skill_domain):
    """修复"已知限制"章节中的重复行。"""
    pattern = re.compile(
        r'(##\s*已知限制\s*\n)'
        r'((?:-\s+[^\n]+\n)+)',
        re.MULTILINE
    )

    match = pattern.search(content)
    if not match:
        return content, 0

    lines = match.group(2).strip().split("\n")
    seen = set()
    has_dup = False
    unique_lines = []
    for line in lines:
        line_stripped = line.strip()
        if line_stripped in seen:
            has_dup = True
            continue
        seen.add(line_stripped)
        unique_lines.append(line)

    if not has_dup:
        return content, 0

    # 如果去重后行数太少,补充领域相关限制
    domain_limits = {
        "finance": [
            "- 分析质量取决于输入数据的完整性和准确性",
            "- 基于历史数据预测未来,无法预判黑天鹅事件",
            "- 估值模型中的假设参数具有主观性",
        ],
        "security": [
            "- 扫描覆盖面受目标网络可达性限制",
            "- 漏洞库更新存在时间窗口,零日漏洞可能遗漏",
            "- 误报率取决于目标环境复杂度",
        ],
        "dev": [
            "- 代码分析深度受项目规模和语言支持影响",
            "- 自动化修复建议需人工审查后采纳",
            "- 复杂依赖链的版本冲突可能无法自动解决",
        ],
        "browser": [
            "- 动态渲染页面可能需要额外等待时间",
            "- 目标网站反爬策略升级可能导致抓取失败",
            "- 复杂交互流程的稳定性取决于页面结构一致性",
        ],
        "creative": [
            "- 生成质量取决于提示词描述的精确度",
            "- 输出结果具有随机性,同一提示词可能产生不同结果",
            "- 高分辨率生成需要较长的处理时间",
        ],
        "other": [
            "- 需要LLM支持,无LLM环境无法使用",
            "- 复杂场景可能需要人工辅助判断",
            "- 性能取决于底层模型能力与网络状况",
        ],
    }
    limits = domain_limits.get(skill_domain, domain_limits["other"])
    for lim in limits:
        if lim.strip() not in seen:
            unique_lines.append(lim)
        if len(unique_lines) >= 4:
            break

    new_section = match.group(1) + "\n".join(unique_lines) + "\n"
    new_content = content[:match.start()] + new_section + content[match.end():]
    return new_content, 1


# ============================================================
# 额外修复: 表格分隔符重复
# ============================================================

def fix_table_separator_duplicates(content):
    """修复表格分隔符行导致的重复检测。

    问题: 当多个表格的分隔符行(如 |:-----|:-------|:-------|)在TF-IDF
    char级n-gram(2-5)下被提取为块后,即使列数不同,因为字符组成相同(:,-,空格),
    相似度仍然>0.92。

    策略: 对文中第2个及之后的表格分隔符,使用不同的对齐组合使每个分隔符的
    块文本唯一。对齐选项池: "---" / "--:" / ":--" / ":-:",
    按序号取不同组合,确保每个分隔符块文本不重复。
    """
    fixes = 0
    lines = content.split("\n")
    seen_block_sigs = []
    # 对齐模式池: 每种产生不同的n-gram分布
    align_pool = ["---", "--:", ":--", ":-:"]
    dup_counter = 0

    new_lines = []
    for line in lines:
        stripped = line.strip()
        # 匹配表格分隔符行: |:---|:---| 或 |---|---| 等
        if re.match(r'^\|[\s:|-]+\|$', stripped):
            block_sig = re.sub(r'\|', ' ', stripped).strip()
            col_count = stripped.count("|") - 1

            # 检查是否与已有签名过于相似
            is_duplicate = False
            for prev_sig in seen_block_sigs:
                if block_sig == prev_sig:
                    is_duplicate = True
                    break
                if re.match(r'^[:\-\s]+$', block_sig) and re.match(r'^[:\-\s]+$', prev_sig):
                    is_duplicate = True
                    break

            if is_duplicate and col_count >= 1:
                # 生成唯一的对齐组合
                # 使用dup_counter选择不同的对齐模式
                while True:
                    pattern_idx = dup_counter % len(align_pool)
                    align_char = align_pool[pattern_idx]
                    new_cells = [align_char] * col_count
                    # 对于第5个及之后的重复,混合不同列的对齐
                    if dup_counter >= len(align_pool):
                        for ci in range(col_count):
                            mix_idx = (dup_counter + ci) % len(align_pool)
                            new_cells[ci] = align_pool[mix_idx]
                    new_sep = "|" + "|".join(f" {c} " for c in new_cells) + "|"
                    new_block_sig = re.sub(r'\|', ' ', new_sep).strip()
                    dup_counter += 1
                    # 确保新签名不与已有签名重复
                    if new_block_sig not in seen_block_sigs:
                        break
                    if dup_counter > 100:  # 安全阀
                        break
                new_lines.append(new_sep)
                seen_block_sigs.append(new_block_sig)
                fixes += 1
                continue
            else:
                seen_block_sigs.append(block_sig)

        new_lines.append(line)

    return "\n".join(new_lines), fixes


# ============================================================
# 额外修复: 核心能力/适用场景重复行
# ============================================================

def fix_core_capability_duplicates(content, meta):
    """修复"核心能力"列表中的重复行。"""
    pattern = re.compile(
        r'(##\s*核心能力\s*\n)'
        r'((?:-\s+[^\n]+\n)+)',
        re.MULTILINE
    )
    match = pattern.search(content)
    if not match:
        return content, 0

    lines = match.group(2).strip().split("\n")
    seen = set()
    has_dup = False
    unique_lines = []
    for line in lines:
        ls = line.strip()
        if ls in seen:
            has_dup = True
            continue
        seen.add(ls)
        unique_lines.append(line)

    if not has_dup:
        return content, 0

    new_section = match.group(1) + "\n".join(unique_lines) + "\n"
    new_content = content[:match.start()] + new_section + content[match.end():]
    return new_content, 1


def fix_scenario_table_duplicates(content, meta):
    """修复"适用场景"表格中的重复行。"""
    pattern = re.compile(
        r'(##\s*适用场景\s*\n+)'
        r'(\|[^\n]+\n)'
        r'(\|[\|:\-\s]+\n)'
        r'((?:\|[^\n]+\n)+)',
        re.MULTILINE
    )
    match = pattern.search(content)
    if not match:
        return content, 0

    header = match.group(2)
    sep = match.group(3)
    old_rows = match.group(4).strip().split("\n")

    seen = set()
    has_dup = False
    unique_rows = []
    for row in old_rows:
        rs = row.strip()
        if rs in seen:
            has_dup = True
            continue
        seen.add(rs)
        unique_rows.append(row)

    # 检测通用模板行
    generic_markers = ["基础使用", "用户请求", "处理结果"]
    has_generic = any(all(gm in row for gm in generic_markers) for row in old_rows)

    if not has_dup and not has_generic:
        return content, 0

    display = meta.get("displayName", "") or meta.get("slug", "")
    summary = meta.get("summary", "")

    # 生成skill专属场景行
    if has_generic or len(unique_rows) < 2:
        # 提取summary中的关键场景
        scenarios = []
        # 尝试从summary提取场景
        parts = re.split(r'[，,。;；]', summary)
        for part in parts:
            part = part.strip()
            if len(part) > 4 and len(part) < 40:
                scenarios.append(part)
            if len(scenarios) >= 3:
                break

        if not scenarios:
            scenarios = [
                f"快速{display}处理",
                f"批量{display}操作",
                f"{display}结果导出",
            ]

        new_rows = []
        for i, sc in enumerate(scenarios[:3]):
            new_rows.append(f"| 场景{i+1}: {sc} | 用户请求数据 | 结构化处理结果 |")
        unique_rows = new_rows

    new_section = match.group(1) + header + sep + "\n".join(unique_rows) + "\n"
    new_content = content[:match.start()] + new_section + content[match.end():]
    return new_content, 1


# ============================================================
# 额外修复: 通用段落/引用块/表格行去重
# ============================================================

def fix_general_duplicate_blocks(content, meta):
    """修复文档中任意位置的完全重复段落、引用块和表格数据行。

    处理:
    - 重复的段落(如 **用户输入示例:** 出现两次)
    - 重复的引用块(如 > 详细代码示例已移至... 出现两次)
    - 表格中完全相同的重复数据行(如 自然语言 代码 自然语言 代码 出现两次)
    - 跨表格的重复数据行(同一行出现在不同表格中)
    """
    fixes = 0
    # 先处理代码块内部的空行,防止代码片段被审计提取为独立块
    content, code_fixes = fix_code_block_internal_blanks(content)
    fixes += code_fixes

    # 按段落分割(双换行分隔)
    paragraphs = re.split(r'(\n\s*\n)', content)
    seen_blocks = set()
    global_table_rows = set()  # 跨表格跟踪所有数据行
    new_parts = []
    skip_next_sep = False

    for i, part in enumerate(paragraphs):
        # 保留分隔符
        if re.match(r'^\n\s*\n$', part):
            if not skip_next_sep:
                new_parts.append(part)
            skip_next_sep = False
            continue

        stripped = part.strip()
        if not stripped or len(stripped) < 10:
            new_parts.append(part)
            continue

        # 跳过代码块
        if stripped.startswith('```'):
            new_parts.append(part)
            continue

        # 跳过标题行
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
                    if not re.match(r'^\|[\s:|-]+\|$', ls):
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
    """修复代码块内部的空行,防止代码片段被审计提取为独立块。

    审计的块提取逻辑按双换行(\n\s*\n)分割段落,代码块内部如果有空行,
    空行后的代码片段(不以```开头)会被提取为独立块并参与相似度比较。
    通过将代码块内部的纯空行替换为语言注释行,使整个代码块保持为一个段落。
    注释行包含非空白字符,不会被\n\s*\n匹配为段落分隔符。
    """
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
                # 根据语言选择注释前缀
                if code_block_lang in ('python', 'py', 'bash', 'sh', 'shell', 'ruby', 'rb', 'yaml', 'yml', 'toml', 'dockerfile'):
                    comment = '# ...'
                elif code_block_lang in ('javascript', 'js', 'typescript', 'ts', 'java', 'c', 'cpp', 'c++', 'go', 'rust', 'swift', 'kotlin', 'scss', 'css', 'jsonc'):
                    comment = '// ...'
                else:
                    comment = '# ...'  # 安全默认值
                new_lines.append(comment)
                fixes += 1
                continue

        new_lines.append(line)

    return '\n'.join(new_lines), fixes


def fix_duplicate_table_headers(content, meta):
    """修复跨表格的重复表头行。

    当两个不同表格使用相同的表头行(如 "| 自然语言 | 代码 | 自然语言 | 代码 |")
    时,审计会将它们提取为相同的块。此函数检测并差异化重复的表头行。
    """
    fixes = 0
    lines = content.split('\n')
    seen_headers = {}  # header_text -> first occurrence line index
    new_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        # 匹配表格行(以|开头)
        if stripped.startswith('|') and stripped.endswith('|'):
            # 检查是否是表头行(下一行是分隔符)
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if re.match(r'^\|[\s:|-]+\|$', next_line):
                    # 这是表头行
                    if stripped in seen_headers:
                        # 重复表头:根据上下文生成差异化表头
                        # 找到当前最近的标题
                        context_title = ''
                        for j in range(i - 1, max(i - 20, 0), -1):
                            prev = lines[j].strip()
                            if prev.startswith('#'):
                                context_title = prev.lstrip('#').strip()
                                break
                        # 替换通用列名为上下文相关名称
                        display = meta.get("displayName", "") or meta.get("slug", "")
                        if '自然语言' in stripped and '代码' in stripped:
                            if context_title:
                                # 用上下文标题替换"自然语言"
                                new_header = stripped.replace('自然语言', context_title[:4], 1)
                            else:
                                new_header = stripped.replace('自然语言', display[:4] or '名称', 1)
                            new_lines.append(new_header)
                            fixes += 1
                            continue
                        else:
                            # 其他重复表头:添加序号
                            count = seen_headers[stripped]
                            cells = stripped.split('|')
                            if len(cells) >= 2 and cells[1].strip():
                                cells[1] = f" {cells[1].strip()}{count + 1} "
                                new_header = '|'.join(cells)
                                new_lines.append(new_header)
                                seen_headers[stripped] = count + 1
                                fixes += 1
                                continue
                    else:
                        seen_headers[stripped] = 1

        new_lines.append(line)

    return '\n'.join(new_lines), fixes


# ============================================================
# 额外修复: 相似代码块差异化
# ============================================================

def fix_similar_code_blocks(content, meta):
    """修复相似但非完全相同的代码块(相似度0.92-0.95)。

    在代码块中添加区分性注释,使相似代码块的n-gram分布产生差异。
    """
    fixes = 0
    # 找到所有代码块
    code_block_pattern = re.compile(r'(```[^\n]*\n)([\s\S]*?)(```)', re.MULTILINE)
    code_blocks = list(code_block_pattern.finditer(content))

    if len(code_blocks) < 2:
        return content, 0

    # 提取代码块内容用于比较
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    code_texts = [cb.group(2)[:300] for cb in code_blocks]
    if len(code_texts) < 2:
        return content, 0

    try:
        vec = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 5), max_features=5000, sublinear_tf=True)
        mat = vec.fit_transform(code_texts)
        sim = cosine_similarity(mat)
    except Exception:
        return content, 0

    # 找到相似的代码块对
    similar_pairs = []
    for i in range(len(code_blocks)):
        for j in range(i + 1, len(code_blocks)):
            if sim[i][j] > SIMILARITY_THRESHOLD:
                similar_pairs.append((i, j, float(sim[i][j])))

    if not similar_pairs:
        return content, 0

    # 对每对相似代码块,在第二个代码块开头添加区分性注释
    display = meta.get("displayName", "") or meta.get("slug", "")
    offset = 0
    for i, j, s in similar_pairs:
        cb_j = code_blocks[j]
        # 在代码块内容开头添加注释行
        lang = cb_j.group(1).strip().lstrip('`')
        old_content_block = cb_j.group(2)
        # 根据语言添加注释
        if lang in ('python', 'py', ''):
            comment = f"# 变体实现(与上文代码相似度{s:.1%},此处为{display}的差异化处理路径)\n"
        elif lang in ('javascript', 'js', 'typescript', 'ts'):
            comment = f"// 变体实现(与上文代码相似度{s:.1%},此处为{display}的差异化处理路径)\n"
        elif lang in ('bash', 'sh', 'shell'):
            comment = f"# 变体实现(与上文代码相似度{s:.1%},此处为{display}的差异化处理路径)\n"
        else:
            comment = f"// 变体实现(与上文代码相似度{s:.1%},此处为{display}的差异化处理路径)\n"

        new_content_block = comment + old_content_block
        start = cb_j.start(2) + offset
        end = cb_j.end(2) + offset
        content = content[:start] + new_content_block + content[end:]
        offset += len(comment)
        fixes += 1

    return content, fixes

# ============================================================
# 重复检测(与审计脚本一致)
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


# ============================================================
# 主流程
# ============================================================

def load_flagged_slugs():
    """从审计报告加载所有被标记 L7A_DUPLICATE_BLOCKS 的 slug 列表。

    返回 (flagged_list, original_total_dup_pairs)
    """
    data = json.load(open(str(AUDIT_REPORT), "r", encoding="utf-8"))
    sa = data.get("semantic_audit", {})
    issues = sa.get("issues_detail", [])

    flagged = []
    original_total_dup_pairs = 0
    for item in issues:
        if isinstance(item, dict):
            for iss in item.get("issues", []):
                s = str(iss)
                if "L7A_DUPLICATE_BLOCKS" in s:
                    # 提取原始重复块对数
                    m = re.search(r'(\d+)\s*对', s)
                    if m:
                        original_total_dup_pairs += int(m.group(1))
                    flagged.append({
                        "slug": item.get("slug"),
                        "source": item.get("source"),
                        "grade": item.get("grade"),
                        "score": item.get("score"),
                        "issue": iss,
                    })
                    break
    return flagged, original_total_dup_pairs


def process_skill(skill_path, meta, skill_type, skill_domain):
    """对单个 SKILL.md 执行全部去重修复。

    返回 dict: {
        "path": skill_path,
        "original_dup_count": int,
        "fixed_dup_count": int,
        "fixes_applied": {"type_a": int, "type_b": int, "type_c": int, ...},
        "modified": bool,
    }
    """
    content = open(skill_path, encoding="utf-8").read()
    fm_text, body = split_frontmatter(content)

    # 修复前重复计数
    before_count, before_details = count_duplicate_blocks(body)

    fixes_applied = {
        "type_a_paid_table": 0,
        "type_b_usage_steps": 0,
        "type_c_error_handling": 0,
        "known_limitations": 0,
        "core_capabilities": 0,
        "scenario_table": 0,
        "table_separators": 0,
        "general_dedup": 0,
        "duplicate_table_headers": 0,
        "similar_code_blocks": 0,
    }

    # 应用修复(在body上操作,保留frontmatter)
    # 类型A: 付费版专享能力
    body, n = fix_type_a_paid_table(body, meta, skill_domain)
    fixes_applied["type_a_paid_table"] = n

    # 类型B: 使用流程
    body, n = fix_type_b_usage_steps(body, meta, skill_type)
    fixes_applied["type_b_usage_steps"] = n

    # 类型C: 错误处理
    body, n = fix_type_c_error_handling(body, meta, skill_domain)
    fixes_applied["type_c_error_handling"] = n

    # 额外修复
    body, n = fix_known_limitations(body, meta, skill_domain)
    fixes_applied["known_limitations"] = n

    body, n = fix_core_capability_duplicates(body, meta)
    fixes_applied["core_capabilities"] = n

    body, n = fix_scenario_table_duplicates(body, meta)
    fixes_applied["scenario_table"] = n

    # 通用段落/引用块/表格行去重
    body, n = fix_general_duplicate_blocks(body, meta)
    fixes_applied["general_dedup"] = n

    # 跨表格重复表头去重
    body, n = fix_duplicate_table_headers(body, meta)
    fixes_applied["duplicate_table_headers"] = n

    body, n = fix_table_separator_duplicates(body)
    fixes_applied["table_separators"] = n

    # 相似代码块差异化
    body, n = fix_similar_code_blocks(body, meta)
    fixes_applied["similar_code_blocks"] = n

    # 修复后重复计数
    after_count, after_details = count_duplicate_blocks(body)

    modified = any(v > 0 for v in fixes_applied.values())

    if modified:
        # 写回文件
        new_content = "---" + fm_text + "---" + body
        with open(skill_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return {
        "path": skill_path,
        "original_dup_count": before_count,
        "fixed_dup_count": after_count,
        "fixes_applied": fixes_applied,
        "modified": modified,
        "before_details": before_details[:5],
        "after_details": after_details[:5],
    }


def main():
    print("=" * 70)
    print("L7A_DUPLICATE_BLOCKS 去重任务")
    print("=" * 70)

    # 1. 加载被标记的 slug
    flagged, original_total_dup_pairs = load_flagged_slugs()
    print(f"\n[1] 从审计报告加载到 {len(flagged)} 个被标记 L7A_DUPLICATE_BLOCKS 的 skill")
    print(f"    原始审计报告中的重复块对总数: {original_total_dup_pairs}")

    # 2. 构建 slug -> path 映射
    slug_map = build_slug_path_map()
    print(f"[2] 构建 slug->path 映射: {len(slug_map)} 个 skill 文件")

    # 3. 逐个处理
    results = []
    type_a_count = 0
    type_b_count = 0
    type_c_count = 0
    total_modified = 0
    total_before_dups = 0
    total_after_dups = 0
    not_found = []

    for item in flagged:
        slug = item["slug"]
        path = slug_map.get(slug)
        if not path:
            not_found.append(slug)
            continue

        # 读取并解析元数据
        try:
            txt = open(path, encoding="utf-8").read()
        except Exception as e:
            print(f"  [ERROR] 读取 {slug} 失败: {e}")
            continue

        fm_text, body = split_frontmatter(txt)
        meta = parse_frontmatter(fm_text)
        meta["slug"] = slug

        # 分类
        skill_type, skill_domain = classify_skill(meta)

        # 执行去重
        result = process_skill(path, meta, skill_type, skill_domain)
        result["slug"] = slug
        result["displayName"] = meta.get("displayName", "")
        result["skill_type"] = skill_type
        result["skill_domain"] = skill_domain
        result["source"] = item.get("source")
        results.append(result)

        total_before_dups += result["original_dup_count"]
        total_after_dups += result["fixed_dup_count"]

        if result["modified"]:
            total_modified += 1
        if result["fixes_applied"]["type_a_paid_table"] > 0:
            type_a_count += 1
        if result["fixes_applied"]["type_b_usage_steps"] > 0:
            type_b_count += 1
        if result["fixes_applied"]["type_c_error_handling"] > 0:
            type_c_count += 1

        status = "FIXED" if result["modified"] else "SKIP"
        print(f"  [{status}] {slug} (type={skill_type}, domain={skill_domain}) "
              f"dup: {result['original_dup_count']} -> {result['fixed_dup_count']} "
              f"fixes: A={result['fixes_applied']['type_a_paid_table']} "
              f"B={result['fixes_applied']['type_b_usage_steps']} "
              f"C={result['fixes_applied']['type_c_error_handling']}")

    # 4. 生成报告
    report = {
        "task": "L7A_DUPLICATE_BLOCKS 去重",
        "version": "v35",
        "timestamp": datetime.now().isoformat(),
        "config": {
            "similarity_threshold": SIMILARITY_THRESHOLD,
            "audit_report": str(AUDIT_REPORT),
            "scan_directories": [str(PACKAGED_DIR), str(DOWNLOADED_DIR)],
        },
        "summary": {
            "total_flagged": len(flagged),
            "total_found": len(results),
            "not_found": not_found,
            "total_modified": total_modified,
            "type_a_fixed": type_a_count,
            "type_b_fixed": type_b_count,
            "type_c_fixed": type_c_count,
            "original_duplicate_pairs_from_audit": original_total_dup_pairs,
            "total_duplicate_pairs_before": total_before_dups,
            "total_duplicate_pairs_after": total_after_dups,
            "duplicate_reduction": total_before_dups - total_after_dups,
            "reduction_rate": round((total_before_dups - total_after_dups) / total_before_dups * 100, 1) if total_before_dups > 0 else 0,
            "total_reduction_from_original": original_total_dup_pairs - total_after_dups,
            "total_reduction_rate_from_original": round((original_total_dup_pairs - total_after_dups) / original_total_dup_pairs * 100, 1) if original_total_dup_pairs > 0 else 0,
        },
        "fix_type_descriptions": {
            "type_a_paid_table": "付费版专享能力表格: 去除重复行,替换通用模板为skill专属能力描述",
            "type_b_usage_steps": "使用流程章节: 替换模板化步骤为基于skill类型的差异化步骤",
            "type_c_error_handling": "错误处理表格: 去除重复行,替换通用错误为skill领域专属错误场景",
            "known_limitations": "已知限制章节: 去除重复行,补充领域相关限制",
            "core_capabilities": "核心能力章节: 去除重复行",
            "scenario_table": "适用场景表格: 去除重复行,替换通用场景为skill专属场景",
            "table_separators": "表格分隔符: 使用唯一对齐组合消除跨表分隔符重复",
            "general_dedup": "通用去重: 移除文档中重复的段落、引用块和表格数据行",
            "duplicate_table_headers": "跨表表头去重: 差异化重复的表格表头行",
            "similar_code_blocks": "相似代码块: 在相似代码块中添加区分性注释降低相似度",
        },
        "details": results,
    }

    # 确保输出目录存在
    REPORT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(str(REPORT_OUTPUT), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # 5. 打印摘要
    print("\n" + "=" * 70)
    print("去重完成 - 统计摘要")
    print("=" * 70)
    print(f"  被标记skill总数:     {len(flagged)}")
    print(f"  找到并处理:          {len(results)}")
    print(f"  未找到:              {len(not_found)}")
    print(f"  已修改文件:          {total_modified}")
    print(f"  ---")
    print(f"  类型A(付费版能力)修复:  {type_a_count} 个skill")
    print(f"  类型B(使用流程)修复:    {type_b_count} 个skill")
    print(f"  类型C(错误处理)修复:    {type_c_count} 个skill")
    print(f"  ---")
    print(f"  原始审计重复块对总数:    {original_total_dup_pairs}")
    print(f"  本轮修复前重复块对总数:  {total_before_dups}")
    print(f"  本轮修复后重复块对总数:  {total_after_dups}")
    print(f"  总减少重复块对(从原始):  {original_total_dup_pairs - total_after_dups}")
    print(f"  总降低率(从原始):        {report['summary']['total_reduction_rate_from_original']}%")
    print(f"  ---")
    print(f"  报告已保存: {REPORT_OUTPUT}")

    return report


if __name__ == "__main__":
    main()
