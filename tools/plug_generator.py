#!/usr/bin/env python3
"""
Plug 生成器 (M3.1 — 营销包装自动化)
======================================
将 A-grade skills 组合为 Plug (营销包)，为每个推荐 Bundle 生成
plug.json (pain_points / value_props / use_case) 和 SKILL.md (组合统一入口)。

依赖模块:
  - bundle_composer.find_best_bundle()  : 自动发现最佳 Bundle 组合
  - pricing_engine.calculate_price()    : 计算单个 skill 定价
  - skill_core.db.get_db()             : DB 连接 (单一来源)
  - skill_core.parser                   : frontmatter 解析

工作流:
  1. 查询 DB 获取 A-grade skills (local_quality_score >= 阈值)
  2. 按分类调用 bundle_composer.find_best_bundle() 获取推荐 Bundle
  3. 对每个推荐 Bundle 生成:
     - plug.json : pain_points (从 skill 描述提取痛点关键词)
                   value_props (pricing_engine 计算单买 vs 捆绑节省)
                   use_case    (从 tools 字段生成工作流描述)
     - SKILL.md  : 组合 skill 统一入口文档
  4. 输出到 packaged-skills/plugs/{plug-slug}/

Usage:
    python plug_generator.py --dry-run              # 预览模式 (不写文件)
    python plug_generator.py                        # 生成 Plug 文件
    python plug_generator.py --slugs a,b,c          # 指定 skill slugs
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ============================================================
# sys.path 设置 — 确保能导入 skill_core / config / bundle_composer / pricing_engine
# V117 W5: bootstrap模式, Path(__file__)在project_config导入前必须使用
# ============================================================
_TOOLS_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _TOOLS_DIR.parent
_CONFIG_DIR = _PROJECT_ROOT / "config"
for _p in [str(_TOOLS_DIR), str(_CONFIG_DIR)]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

from project_config import PACKAGED_SKILLS_DIR, A_GRADE_QUALITY_THRESHOLD, PLUGS_DIR # noqa: E402; V117 W5: 新增TOOLS_DIR+PROJECT_ROOT; V118 W3: 新增A_GRADE_QUALITY_THRESHOLD; V147 R2.1: 新增PLUGS_DIR(从project_config统一导入)
from skill_core import db as db_module                              # noqa: E402
from skill_core.parser import parse_frontmatter, find_skill_md  # noqa: E402
import bundle_composer                                         # noqa: E402
import pricing_engine                                          # noqa: E402


# ============================================================
# 常量
# ============================================================

# A-grade 质量分阈值: V118 W3 从project_config导入(与 bundle_composer/orchestrator 共享同一常量)
# Plug 输出根目录: V147 R2.1 从project_config导入PLUGS_DIR(消除本地定义,统一来源)
# 原: PLUGS_DIR = PACKAGED_SKILLS_DIR.parent / "plugs"  →  已统一到project_config

# Bundle 捆绑折扣率 (组合购买比单买节省的比例)
BUNDLE_DISCOUNT_RATE = 0.20  # 20% off

# 痛点关键词字典: pain_category -> [keywords]
# 用于从 skill 描述中提取痛点
PAIN_KEYWORD_MAP: Dict[str, List[str]] = {
    '耗时低效': ['耗时', '费时', '时间成本', '低效', '效率低', '手动', '人工',
                '繁琐', '重复', '重复劳动', '一遍又一遍', '慢', '批量处理'],
    '易出错': ['易错', '错误', '出错', '遗漏', '不准确', '偏差', '风险', '隐患',
              '不安全', '漏洞', '误操作'],
    '门槛高': ['复杂', '困难', '门槛高', '难以', '割裂', '分散', '不统一',
              '学习曲线', '专业知识', '技术壁垒', '手动配置'],
    '成本高': ['成本高', '昂贵', '付费高', '投入大', '资源消耗', '算力消耗',
              '人力成本'],
    '不透明': ['不透明', '难以追踪', '无法追溯', '黑盒', '不可见', '不可控',
              '难以监控'],
}

# 分类 -> (痛点, 方案) 映射 (用于 pain_points 和 value_props 文案生成)
CATEGORY_PAIN_SOLUTION: Dict[str, Tuple[str, str]] = {
    'Development':    ('开发效率低下重复劳动多',       '智能开发辅助与自动化'),
    'Automation':     ('日常事务繁杂难以聚焦核心',     '自动化任务编排'),
    'Other':          ('手工操作效率低易出错',         '智能化自动处理'),
    'Security':       ('安全审计手动覆盖不足',         '自动化安全扫描'),
    'Creative':       ('创作灵感与工具分散难统一',     '一站式创作工作流'),
    'Research':       ('信息检索效率低来源分散',       '智能研究聚合'),
    'Operations':     ('运维操作繁琐易出错',           '自动化运维与监控'),
    'Finance':        ('财务数据处理耗时易错',         '自动化财务流程'),
    'Productivity':   ('日常事务繁杂难以聚焦核心',     '自动化任务编排'),
    'Knowledge':      ('知识管理分散难以检索',         '统一知识中枢'),
    'Agents':         ('AI能力集成成本高',             '开箱即用AI工具链'),
    'Communication':  ('沟通渠道分散信息易遗漏',       '统一消息中枢'),
    'Integrations':   ('系统集成碎片化维护成本高',     '统一API集成层'),
    'Lifestyle':      ('生活事务分散难以高效管理',     '一站式生活助手'),
    'Data':           ('数据处理流程割裂难追溯',       '端到端数据管道'),
    'DevOps':         ('运维操作繁琐易出错',           '基础设施即代码'),
    'AI':             ('AI能力集成成本高',             '开箱即用AI工具链'),
}


# ============================================================
# 数据读取
# ============================================================

def _query_a_grade_skills(a_grade_slugs: Optional[List[str]] = None) -> List[Dict]:
    """查询 DB 获取 A-grade skills

    参数:
        a_grade_slugs: 指定 slug 列表 (None 则按质量分筛选全部 A-grade)

    返回:
        skill 字典列表，每项包含 slug / category / quality_score /
        summary / local_path / name / display_name
    """
    conn = db_module.get_db()
    c = conn.cursor()

    if a_grade_slugs:
        placeholders = ','.join('?' * len(a_grade_slugs))
        c.execute(
            f"SELECT slug, category, local_quality_score, summary, local_path, "
            f"current_name, current_display_name "
            f"FROM skills WHERE slug IN ({placeholders}) "
            f"ORDER BY local_quality_score DESC",
            a_grade_slugs
        )
    else:
        c.execute(
            "SELECT slug, category, local_quality_score, summary, local_path, "
            "current_name, current_display_name "
            "FROM skills WHERE local_quality_score >= ? "
            "ORDER BY local_quality_score DESC",
            (A_GRADE_QUALITY_THRESHOLD,)
        )

    rows = c.fetchall()
    conn.close()

    skills = []
    for row in rows:
        skills.append({
            'slug': row['slug'],
            'category': row['category'] or 'Other',
            'quality_score': row['local_quality_score'] or 0.0,
            'summary': row['summary'] or '',
            'local_path': row['local_path'] or '',
            'name': row['current_name'] or row['current_display_name'] or row['slug'],
            'display_name': row['current_display_name'] or row['current_name'] or row['slug'],
        })
    return skills


def _query_skill_summaries(slugs: List[str]) -> Dict[str, str]:
    """批量查询 skill 的 summary (从 DB)

    参数:
        slugs: slug 列表

    返回:
        {slug: summary} 映射
    """
    if not slugs:
        return {}
    conn = db_module.get_db()
    c = conn.cursor()
    placeholders = ','.join('?' * len(slugs))
    c.execute(
        f"SELECT slug, summary FROM skills WHERE slug IN ({placeholders})",
        slugs
    )
    result = {row['slug']: row['summary'] or '' for row in c.fetchall()}
    conn.close()
    return result


def _get_distinct_categories(skills: List[Dict]) -> List[str]:
    """获取 skill 列表中的去重分类 (按 skill 数量降序)"""
    cat_counts: Dict[str, int] = {}
    for s in skills:
        cat = s['category']
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    return sorted(cat_counts.keys(), key=lambda k: cat_counts[k], reverse=True)


# ============================================================
# 痛点提取 (pain_points)
# ============================================================

def _extract_pain_points(members: List[Dict]) -> List[str]:
    """从 skill 描述中提取痛点关键词

    读取每个成员 skill 的 summary (DB) 和 description (SKILL.md frontmatter)，
    基于 PAIN_KEYWORD_MAP 提取痛点，结合分类级痛点映射生成痛点列表。

    参数:
        members: Bundle 成员列表 (来自 compose_bundle 返回值)

    返回:
        去重后的痛点描述列表
    """
    pain_points: List[str] = []
    seen: set = set()

    # 批量查询所有成员的 summary
    member_slugs = [m.get('slug', '') for m in members if m.get('slug')]
    summaries = _query_skill_summaries(member_slugs)

    for member in members:
        slug = member.get('slug', '')
        category = member.get('category', 'Other')

        # 1. 分类级痛点映射
        cat_pain, _ = CATEGORY_PAIN_SOLUTION.get(
            category, CATEGORY_PAIN_SOLUTION['Other']
        )
        if cat_pain not in seen:
            pain_points.append(cat_pain)
            seen.add(cat_pain)

        # 2. 汇总该 skill 的描述文本 (DB summary + SKILL.md description)
        desc_text = summaries.get(slug, '')

        skill_md = find_skill_md(slug)
        if skill_md and skill_md.exists():
            content = skill_md.read_text(encoding='utf-8')
            fm_result = parse_frontmatter(content)
            fm_desc = fm_result['fields'].get('description', '')
            fm_summary = fm_result['fields'].get('summary', '')
            desc_text = f"{desc_text} {fm_desc} {fm_summary}"

        # 3. 提取痛点关键词
        desc_lower = desc_text.lower()
        for pain_category, keywords in PAIN_KEYWORD_MAP.items():
            for kw in keywords:
                if kw.lower() in desc_lower:
                    pain_desc = f"{slug}: 存在{pain_category}问题 ({kw})"
                    if pain_desc not in seen:
                        pain_points.append(pain_desc)
                        seen.add(pain_desc)
                    break  # 每个痛点类别只取一个关键词

    return pain_points[:10]  # 最多 10 条痛点


# ============================================================
# 价值主张计算 (value_props)
# ============================================================

def _calculate_value_props(members: List[Dict]) -> Dict:
    """使用 pricing_engine 计算单买 vs 捆绑的价格节省

    对每个成员 skill 调用 pricing_engine.calculate_price() 获取定价，
    计算单买总价、捆绑价 (折扣后) 和节省金额。

    参数:
        members: Bundle 成员列表

    返回:
        {
            'individual_prices': [{slug, name, price, tier}, ...],
            'total_individual': float,   # 单买总价
            'bundle_price': float,       # 捆绑价
            'savings': float,            # 节省金额
            'savings_percent': float,    # 节省比例
            'discount_rate': float,      # 折扣率
            'value_statement': str,      # 价值主张文案
        }
    """
    individual_prices: List[Dict] = []
    total_individual = 0.0

    for member in members:
        slug = member.get('slug', '')
        skill_md = find_skill_md(slug)

        if skill_md and skill_md.exists():
            try:
                price_result = pricing_engine.calculate_price(skill_md)
                price = price_result.get('final_price', 0.0)
                tier = price_result.get('tier', 'unknown')
            except Exception as e:  # V156: fail-safe — pricing_engine不可用时阻断而非降级为0
                raise RuntimeError(
                    f"pricing_engine.calculate_price() 失败 (slug={slug}): {e} "
                    f"— Plug生成阻断(fail-safe)"
                ) from e
        else:
            price = 0.0
            tier = 'unknown'

        individual_prices.append({
            'slug': slug,
            'name': member.get('name', slug),
            'price': round(price, 2),
            'tier': tier,
        })
        total_individual += price

    # 捆绑价 = 单买总价 × (1 - 折扣率)
    bundle_price = round(total_individual * (1 - BUNDLE_DISCOUNT_RATE), 2)
    savings = round(total_individual - bundle_price, 2)
    savings_percent = round(BUNDLE_DISCOUNT_RATE * 100, 1) if total_individual > 0 else 0.0

    # 价值主张文案
    member_count = len(members)
    if total_individual > 0:
        value_statement = (
            f"{member_count}个skill单买总价{total_individual:.1f}元，"
            f"Plug捆绑价{bundle_price:.1f}元，节省{savings:.1f}元 ({savings_percent}% off)"
        )
    else:
        value_statement = (
            f"{member_count}个skill组合为Plug，一站式解决多场景需求，"
            f"享受{BUNDLE_DISCOUNT_RATE * 100:.0f}%捆绑折扣"
        )

    return {
        'individual_prices': individual_prices,
        'total_individual': round(total_individual, 2),
        'bundle_price': bundle_price,
        'savings': savings,
        'savings_percent': savings_percent,
        'discount_rate': BUNDLE_DISCOUNT_RATE,
        'value_statement': value_statement,
    }


# ============================================================
# 用例生成 (use_case)
# ============================================================

def _generate_use_case(members: List[Dict]) -> str:
    """从 skill 的 tools 字段生成工作流描述

    读取每个成员 skill 的 SKILL.md frontmatter 中的 tools 字段，
    生成组合工作流描述。

    参数:
        members: Bundle 成员列表

    返回:
        工作流描述字符串
    """
    all_tools: List[str] = []
    member_info: List[Dict] = []

    for member in members:
        slug = member.get('slug', '')
        name = member.get('name', slug)
        category = member.get('category', 'Other')

        skill_md = find_skill_md(slug)
        tools: List[str] = []
        if skill_md and skill_md.exists():
            content = skill_md.read_text(encoding='utf-8')
            fm_result = parse_frontmatter(content)
            tools_raw = fm_result['fields'].get('tools', [])
            if isinstance(tools_raw, list):
                tools = [str(t).strip().lstrip('-').strip() for t in tools_raw if t]
            elif isinstance(tools_raw, str) and tools_raw:
                tools = [t.strip() for t in tools_raw.split(',') if t.strip()]

        all_tools.extend(tools)
        member_info.append({
            'slug': slug,
            'name': name,
            'category': category,
            'tools': tools,
        })

    # 去重工具
    unique_tools: List[str] = []
    seen_tools: set = set()
    for t in all_tools:
        if t and t not in seen_tools:
            unique_tools.append(t)
            seen_tools.add(t)

    # 生成工作流描述
    lines = [f"本Plug整合{len(members)}个互补skill，提供一站式解决方案：", ""]

    for info in member_info:
        tools_str = '、'.join(info['tools']) if info['tools'] else '通用工具'
        lines.append(f"- {info['name']} ({info['category']}): 提供 {tools_str}")

    lines.append("")
    if unique_tools:
        lines.append(f"组合工具集: {', '.join(unique_tools[:15])}")

    # 生成典型工作流
    lines.append("")
    lines.append("典型工作流:")
    workflow_steps = member_info[:5]
    for i, info in enumerate(workflow_steps, 1):
        tools_str = '、'.join(info['tools'][:3]) if info['tools'] else '数据处理'
        lines.append(f"  {i}. 使用 {info['name']} 的 {tools_str} 完成相关任务")
    lines.append(f"  {len(workflow_steps) + 1}. 整合各skill输出，形成完整解决方案")

    return '\n'.join(lines)


# ============================================================
# SKILL.md 生成
# ============================================================

def _generate_display_name(bundle: Dict, members: List[Dict]) -> str:
    """生成≤20字符的中文displayName (V150 T1)

    规则:
      - 从primary skill的name提取核心词
      - 加'组合包'后缀
      - 确保含中文字符且≤20字符

    参数:
        bundle: bundle字典
        members: 成员列表

    返回:
        ≤20字符的displayName
    """
    primary = next((m for m in members if m.get('role') == 'primary'), members[0] if members else {})
    primary_name = primary.get('name', bundle.get('bundle_name', 'plug'))

    # 提取核心词: 取name前10个字符
    core = primary_name[:10]

    # 组合displayName
    display_name = f"{core}组合包"

    # 截断到20字符
    if len(display_name) > 20:
        display_name = display_name[:20]

    return display_name


def _generate_description(bundle: Dict, members: List[Dict], pain_points: List[str],
                          value_props: Dict, categories: List[str]) -> str:
    """生成150-280字符的description (V150 T1)

    规则:
      - 避免模板话术('这是一个', '本技能', '帮助你'等)
      - 包含功能价值描述
      - 包含使用场景
      - 长度150-280字符

    参数:
        bundle: bundle字典
        members: 成员列表
        pain_points: 痛点列表
        value_props: 价值主张
        categories: 分类列表

    返回:
        150-280字符的description
    """
    member_count = len(members)
    cat_str = '、'.join(categories[:3]) if categories else '多领域'
    savings = value_props.get('savings_percent', 0)

    # 构建description, 避免模板话术
    parts = [
        f"整合{member_count}个互补skill的营销组合包，覆盖{cat_str}等领域。",
        f"组合内各skill协同工作，提供从数据输入到结果输出的端到端处理能力。",
    ]

    # 添加痛点描述 (取前2条)
    if pain_points:
        pp_str = pain_points[0] if len(pain_points) == 1 else f"{pain_points[0]}、{pain_points[1]}"
        parts.append(f"针对{pp_str}等痛点提供解决方案。")

    # 添加价值主张
    if savings > 0:
        parts.append(f"组合购买可节省{savings}%费用，相比单独购买更经济。")

    parts.append(f"包含{member_count}个经质量审核的skill，整体评分{bundle.get('overall_score', 0):.1f}分。")

    desc = ''.join(parts)

    # 确保长度在150-280之间
    if len(desc) < 150:
        # 扩展: 添加使用场景描述
        primary = next((m for m in members if m.get('role') == 'primary'), members[0] if members else {})
        primary_name = primary.get('name', '核心skill')
        parts.append(f"以{primary_name}为核心，搭配互补skill形成完整工作流。")
        desc = ''.join(parts)

    if len(desc) > 280:
        desc = desc[:277] + '...'

    return desc


def _aggregate_tools(members: List[Dict]) -> List[str]:
    """聚合成员skill的tools字段 (V150 T1)

    参数:
        members: 成员列表

    返回:
        去重后的tools列表
    """
    all_tools: List[str] = []
    seen: set = set()

    for member in members:
        slug = member.get('slug', '')
        skill_md = find_skill_md(slug)
        if skill_md and skill_md.exists():
            content = skill_md.read_text(encoding='utf-8')
            fm_result = parse_frontmatter(content)
            tools_raw = fm_result['fields'].get('tools', [])
            if isinstance(tools_raw, list):
                for t in tools_raw:
                    # V150 T3: 统一小写,避免read/Read重复
                    t_str = str(t).strip().lstrip('-').strip().lower()
                    if t_str and t_str not in seen:
                        all_tools.append(t_str)
                        seen.add(t_str)
            elif isinstance(tools_raw, str) and tools_raw:
                for t in tools_raw.split(','):
                    t_str = t.strip().lower()
                    if t_str and t_str not in seen:
                        all_tools.append(t_str)
                        seen.add(t_str)

    # 如果没有聚合到任何tools, 使用默认值
    if not all_tools:
        all_tools = ['read', 'write', 'exec']

    return all_tools


def _generate_skill_md(plug_slug: str, bundle: Dict, pain_points: List[str],
                       value_props: Dict, use_case: str) -> str:
    """生成 Plug 的 SKILL.md (组合 skill 统一入口文档)

    V150 T1: 修复质量问题
      - 添加tools字段(聚合成员skill的tools)
      - displayName限制≤20字符且含中文
      - description扩展到150-280字符且避免模板话术
      - 添加tags字段

    参数:
        plug_slug: Plug 的 slug
        bundle: compose_bundle / find_best_bundle 返回的 Bundle dict
        pain_points: 痛点列表
        value_props: 价值主张 dict
        use_case: 用例描述

    返回:
        SKILL.md 内容字符串
    """
    members = bundle.get('members', [])
    bundle_name = bundle.get('bundle_name', plug_slug)
    overall_score = bundle.get('overall_score', 0.0)
    combination_reason = bundle.get('combination_reason', '')
    categories = bundle.get('category_diversity', {}).get('categories', [])

    # V150 T1: 生成合规的displayName和description
    display_name = _generate_display_name(bundle, members)
    description = _generate_description(bundle, members, pain_points, value_props, categories)
    tools_list = _aggregate_tools(members)

    # V150 T1: 生成tags (基于分类)
    tags = ', '.join(categories[:5]) if categories else '工具, 效率, 自动化'

    # frontmatter
    member_slugs = [m['slug'] for m in members]

    # V151 T1: 生成category字段(主分类,用于平台映射)
    primary_category = categories[0] if categories else 'Other'

    # V150 T2: tools使用YAML block list格式(而非inline [a, b, c])
    # 避免被frontmatter parser解析为字符串
    fm_lines = [
        '---',
        f'slug: "{plug_slug}"',
        f'name: "{plug_slug}"',
        f'displayName: "{display_name}"',
        f'summary: "Plug组合包: {len(members)}个互补skill, 节省{value_props["savings_percent"]}%"',
        f'version: "1.0.0"',
        f'license: "Proprietary"',
        f'edition: "pro"',
        f'type: "plug"',
        f'category: "{primary_category}"',
        'tools:',
    ]
    for t in tools_list:
        fm_lines.append(f'  - {t}')
    # V156: pricing_tier 根据实际成员定价决定(非硬编码)
    # 所有成员免费(total_individual==0) → "free", 否则 → "paid"
    pricing_tier = "free" if value_props.get('total_individual', 0) == 0 else "paid"

    fm_lines.extend([
        f'tags: "{tags}"',
        f'bundle_slug: "{bundle.get("bundle_slug", "")}"',
        f'members: [{", ".join(member_slugs)}]',
        f'overall_score: {overall_score}',
        f'suggested_price: "{value_props["bundle_price"]:.2f}"',
        f'pricing_tier: "{pricing_tier}"',
        f'description: "{description}"',
        '---',
    ])

    # body
    body_lines = [
        '',
        f'# {bundle_name}',
        '',
        f'> Plug 组合包 | {len(members)} 个互补 skill | 整体评分 {overall_score}/100',
        '',
        '## 痛点 (Pain Points)',
        '',
    ]
    for pp in pain_points:
        body_lines.append(f'- {pp}')

    body_lines.extend([
        '',
        '## 价值主张 (Value Props)',
        '',
        f'- {value_props["value_statement"]}',
        f'- 单买总价: {value_props["total_individual"]} 元',
        f'- Plug 捆绑价: {value_props["bundle_price"]} 元',
        f'- 节省: {value_props["savings"]} 元 ({value_props["savings_percent"]}%)',
        '',
        '### 各 skill 定价',
        '',
        '| Skill | 价格 | 层级 |',
        '|-------|------|------|',
    ])
    for ip in value_props['individual_prices']:
        body_lines.append(f'| {ip["name"]} | {ip["price"]} 元 | {ip["tier"]} |')

    body_lines.extend([
        '',
        '## 使用场景 (Use Case)',
        '',
        use_case,
        '',
        '## 成员 skill',
        '',
        '| Slug | 名称 | 分类 | 角色 | 质量分 |',
        '|------|------|------|------|--------|',
    ])
    for m in members:
        body_lines.append(
            f'| {m["slug"]} | {m.get("name", m["slug"])} | {m.get("category", "")} | '
            f'{m.get("role", "")} | {m.get("quality_score", 0)} |'
        )

    body_lines.extend([
        '',
        '## 组合理由',
        '',
        combination_reason,
        '',
        '## 依赖说明',
        '',
        f'- 运行环境: Python 3.10+',
        f'- 依赖模块: bundle_composer, pricing_engine, skill_core',
        f'- LLM/API Key: 无需外部API (Plug为组合包,依赖成员skill各自的能力)',
        f'- 数据库: SQLite (skills.db, 存储skill元数据和质量分)',
        '',
        '---',
        f'*Generated by plug_generator.py at {datetime.now().isoformat()}*',
    ])

    return '\n'.join(fm_lines) + '\n' + '\n'.join(body_lines) + '\n'


# ============================================================
# 主函数
# ============================================================

def generate_plugs(a_grade_slugs: Optional[List[str]] = None,
                   dry_run: bool = False) -> Dict[str, Any]:
    """生成 Plug 营销包

    工作流:
      a. 查询 DB 获取 A-grade skills (或使用提供的 slug 列表)
      b. 调用 bundle_composer.find_best_bundle() 获取推荐 Bundle
      c. 对每个推荐 Bundle 生成 plug.json 和 SKILL.md
      d. 输出到 packaged-skills/plugs/{plug-slug}/

    参数:
        a_grade_slugs: 指定 skill slug 列表 (None 则查询 DB 全部 A-grade)
        dry_run: 预览模式 (True 则只输出结构不写文件)

    返回:
        {
            'plugs': [{plug_slug, bundle_slug, members, pain_points,
                       value_props, use_case, output_dir}, ...],
            'total': int,
            'dry_run': bool,
            'output_root': str,
            'generated_at': str,
        }
    """
    print(f"\n{'=' * 60}")
    print(f"Plug 生成器 {'[DRY-RUN]' if dry_run else '[WRITE]'}")
    print(f"{'=' * 60}")

    # a. 查询 A-grade skills
    print("  [1] 查询 A-grade skills...")
    a_skills = _query_a_grade_skills(a_grade_slugs)
    print(f"  [1] 找到 {len(a_skills)} 个 A-grade skills")

    if not a_skills:
        print("  [1] 无可用 A-grade skills, 退出")
        return {
            'plugs': [],
            'total': 0,
            'dry_run': dry_run,
            'output_root': str(PLUGS_DIR),
            'generated_at': datetime.now().isoformat(),
            'error': 'no_a_grade_skills',
        }

    # b. 调用 find_best_bundle() 获取推荐 Bundle
    print("  [2] 调用 bundle_composer.find_best_bundle() 获取推荐 Bundle...")
    recommended_bundles: List[Dict] = []
    seen_bundle_slugs: set = set()

    # b-1. 按分类获取推荐 Bundle
    categories = _get_distinct_categories(a_skills)
    print(f"  [2] 发现 {len(categories)} 个分类: {', '.join(categories[:8])}"
          f"{'...' if len(categories) > 8 else ''}")

    for cat in categories:
        bundle = bundle_composer.find_best_bundle(category=cat)
        bundle_slug = bundle.get('bundle_slug', '')
        members = bundle.get('members', [])

        # 跳过无效 Bundle (成员不足或出错)
        if bundle.get('error') or len(members) < bundle_composer.MIN_BUNDLE_SIZE:
            continue
        if bundle_slug in seen_bundle_slugs:
            continue

        seen_bundle_slugs.add(bundle_slug)
        recommended_bundles.append(bundle)
        print(f"  [2] 分类 {cat}: Bundle '{bundle_slug}' ({len(members)} 成员, "
              f"评分 {bundle.get('overall_score', 0):.1f})")

    # b-2. 无分类的全局最佳 Bundle (去重后追加)
    global_bundle = bundle_composer.find_best_bundle(category=None)
    global_slug = global_bundle.get('bundle_slug', '')
    if (not global_bundle.get('error')
            and global_slug not in seen_bundle_slugs
            and len(global_bundle.get('members', [])) >= bundle_composer.MIN_BUNDLE_SIZE):
        recommended_bundles.append(global_bundle)
        seen_bundle_slugs.add(global_slug)
        print(f"  [2] 全局最佳: Bundle '{global_slug}' "
              f"({len(global_bundle.get('members', []))} 成员)")

    print(f"  [2] 共 {len(recommended_bundles)} 个推荐 Bundle")

    if not recommended_bundles:
        print("  [2] 无有效推荐 Bundle, 退出")
        return {
            'plugs': [],
            'total': 0,
            'dry_run': dry_run,
            'output_root': str(PLUGS_DIR),
            'generated_at': datetime.now().isoformat(),
            'error': 'no_valid_bundles',
        }

    # c. 对每个推荐 Bundle 生成 Plug
    print("  [3] 生成 Plug 文件...")
    plugs: List[Dict] = []

    for bundle in recommended_bundles:
        bundle_slug = bundle.get('bundle_slug', 'unknown')
        members = bundle.get('members', [])
        plug_slug = f"plug-{bundle_slug}"
        plug_dir = PLUGS_DIR / plug_slug

        # c-1. 提取痛点
        pain_points = _extract_pain_points(members)

        # c-2. 计算价值主张
        value_props = _calculate_value_props(members)

        # c-3. 生成用例
        use_case = _generate_use_case(members)

        # c-4. 构建 plug.json
        plug_json = {
            'plug_slug': plug_slug,
            'bundle_slug': bundle_slug,
            'bundle_name': bundle.get('bundle_name', ''),
            'members': [
                {
                    'slug': m['slug'],
                    'name': m.get('name', ''),
                    'category': m.get('category', ''),
                    'role': m.get('role', ''),
                }
                for m in members
            ],
            'pain_points': pain_points,
            'value_props': value_props,
            'use_case': use_case,
            'overall_score': bundle.get('overall_score', 0.0),
            'combination_reason': bundle.get('combination_reason', ''),
            'generated_at': datetime.now().isoformat(),
        }

        # c-5. 生成 SKILL.md
        skill_md_content = _generate_skill_md(
            plug_slug, bundle, pain_points, value_props, use_case
        )

        plug_info = {
            'plug_slug': plug_slug,
            'bundle_slug': bundle_slug,
            'members': [m['slug'] for m in members],
            'member_count': len(members),
            'pain_points_count': len(pain_points),
            'bundle_price': value_props['bundle_price'],
            'savings': value_props['savings'],
            'output_dir': str(plug_dir),
            'plug_json': plug_json,
        }

        if dry_run:
            print(f"  [3] [DRY-RUN] Plug '{plug_slug}': "
                  f"{len(members)} 成员, {len(pain_points)} 痛点, "
                  f"捆绑价 {value_props['bundle_price']} 元")
        else:
            # d. 写入文件
            plug_dir.mkdir(parents=True, exist_ok=True)
            plug_json_path = plug_dir / "plug.json"
            plug_json_path.write_text(
                json.dumps(plug_json, ensure_ascii=False, indent=2),
                encoding='utf-8'
            )
            skill_md_path = plug_dir / "SKILL.md"
            skill_md_path.write_text(skill_md_content, encoding='utf-8')
            print(f"  [3] [WRITE] Plug '{plug_slug}': "
                  f"{len(members)} 成员 → {plug_dir}")

            # V156: L1质量门控验证 — 写入SKILL.md后验证格式合规
            try:
                from quality_gate import run_quality_gate
                l1_result = run_quality_gate(skill_md_path)
                if not l1_result.get('overall_passed', False):
                    failed_checks = [c['name'] for c in l1_result.get('checks', [])
                                     if not c.get('passed')]
                    print(f"  [3] [L1-FAIL] Plug '{plug_slug}' L1质量门控未通过: "
                          f"{failed_checks}")
                    return {
                        'plugs': plugs,
                        'total': len(plugs),
                        'dry_run': dry_run,
                        'output_root': str(PLUGS_DIR),
                        'generated_at': datetime.now().isoformat(),
                        'error': 'l1_quality_gate_failed',
                        'failed_plug': plug_slug,
                        'failed_checks': failed_checks,
                    }
                print(f"  [3] [L1-OK] Plug '{plug_slug}' L1质量门控通过 "
                      f"({l1_result.get('passed_checks', 0)}/"
                      f"{l1_result.get('total_checks', 0)})")
            except ImportError:
                # fail-safe: quality_gate模块不可用时阻断
                print(f"  [3] [L1-BLOCKED] quality_gate模块不可用 — "
                      f"Plug生成阻断(fail-safe)")
                return {
                    'plugs': plugs,
                    'total': len(plugs),
                    'dry_run': dry_run,
                    'output_root': str(PLUGS_DIR),
                    'generated_at': datetime.now().isoformat(),
                    'error': 'quality_gate_module_unavailable',
                    'failed_plug': plug_slug,
                }

        plugs.append(plug_info)

    result = {
        'plugs': plugs,
        'total': len(plugs),
        'dry_run': dry_run,
        'output_root': str(PLUGS_DIR),
        'generated_at': datetime.now().isoformat(),
    }

    print(f"\n{'=' * 60}")
    print(f"Plug 生成完成: {len(plugs)} 个 Plug "
          f"{'(dry-run, 未写文件)' if dry_run else '(已写入)'}")
    print(f"输出目录: {PLUGS_DIR}")
    print(f"{'=' * 60}\n")

    return result


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Plug 生成器: 将 A-grade skills 组合为营销 Plug 包"
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='预览模式: 输出推荐 Plug 结构, 不写文件'
    )
    parser.add_argument(
        '--slugs', type=str, default=None,
        help='指定 skill slug 列表 (逗号分隔), 不指定则查询 DB 全部 A-grade'
    )

    args = parser.parse_args()

    a_grade_slugs = None
    if args.slugs:
        a_grade_slugs = [s.strip() for s in args.slugs.split(',') if s.strip()]

    result = generate_plugs(a_grade_slugs=a_grade_slugs, dry_run=args.dry_run)

    # dry-run 模式输出完整 Plug 结构 (含 plug.json 内容)
    if args.dry_run:
        print("--- Plug 结构预览 ---")
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
