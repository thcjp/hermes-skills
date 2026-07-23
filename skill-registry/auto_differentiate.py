#!/usr/bin/env python3
"""
自动差异化系统 (流水线 Step 2 - 自动差异化)
============================================
读取 multi_source_discover.py (Step 1) 产出的 candidates_unified.json 候选 skill,
为每个候选生成差异化 SKILL.md 并写入 d:\\skills\\packaged-skills\\skillhub\\[slug]\\SKILL.md,
同时更新数据库 skills 表。

处理流程:
  1. 读取 candidates_unified.json
  2. 对每个候选:
     a. 生成 slug (kebab-case, 从 source_id 或 name 派生)
     b. 检查 slug 冲突 (查询 DB skills 表), 冲突时自动添加后缀 (-v2, -pro 等)
     c. 生成 displayName (从 name 派生, <=20字符)
     d. 生成 summary (基于 description, "痛点+方案+量化"公式, <=100字符)
     e. 生成 SKILL.md (标准 frontmatter + 核心功能 + 输入格式 + 输出格式 + 依赖说明)
     f. 设置 license: Proprietary (付费)
     g. 设置 pricing_tier: 根据内容复杂度评估 L1-L4
  3. 输出到 d:\skills\packaged-skills\skillhub\[slug]\SKILL.md
  4. 更新数据库 skills 表

用法:
  python auto_differentiate.py                         # 处理前50个候选
  python auto_differentiate.py --limit 100             # 处理前100个候选
  python auto_differentiate.py --source hermes         # 只处理hermes来源
  python auto_differentiate.py --source github          # 只处理github来源
  python auto_differentiate.py --dry-run               # 只输出计划不实际创建
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# ============================================================
# 复用 multi_source_discover.py 的 get_db() 函数
# multi_source_discover.py 从 auto_discover 导入 get_db,
# 此处采用相同来源, 保证获取同一数据库连接。
# ============================================================

_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)

from auto_discover import get_db, DB_PATH

# ============================================================
# 路径常量
# ============================================================

CANDIDATES_FILE = Path(r"d:\skills\skill-registry\discovery\candidates_unified.json")
SKILLHUB_ROOT = Path(r"d:\skills\packaged-skills\skillhub")

# slug 冲突后缀候选列表
SLUG_CONFLICT_SUFFIXES = ['-v2', '-pro', '-v3', '-plus', '-v4', '-max', '-v5', '-elite']

# 分类 -> (痛点, 方案) 映射, 用于 summary 生成
CATEGORY_PAIN_SOLUTION_MAP: Dict[str, Tuple[str, str]] = {
    'Finance':       ('财务数据处理耗时易错',         '自动化财务流程'),
    'Creative':      ('创作灵感与工具分散难统一',     '一站式创作工作流'),
    'Developer':     ('开发效率低下重复劳动多',       '智能开发辅助'),
    'Productivity':  ('日常事务繁杂难以聚焦核心',     '自动化任务编排'),
    'Data':          ('数据处理流程割裂难追溯',       '端到端数据管道'),
    'Communication': ('沟通渠道分散信息易遗漏',      '统一消息中枢'),
    'Research':      ('信息检索效率低来源分散',       '智能研究聚合'),
    'Security':      ('安全审计手动覆盖不足',         '自动化安全扫描'),
    'DevOps':        ('运维操作繁琐易出错',           '基础设施即代码'),
    'AI':            ('AI能力集成成本高',             '开箱即用AI工具链'),
    'Other':         ('手工操作效率低易出错',         '智能化自动处理'),
}

# pricing_tier -> 建议价格
TIER_PRICE_MAP: Dict[str, str] = {
    'L1-基础级': '9.9',
    'L2-进阶级': '19.9',
    'L3-专业级': '29.9',
    'L4-企业级': '49.9',
}


# ============================================================
# slug 生成与冲突检测
# ============================================================

def generate_slug(source_id: str, name: str) -> str:
    """从 source_id 或 name 生成 kebab-case slug。

    规则:
      - 优先使用 source_id, 其次使用 name
      - 转换为小写
      - 空格/下划线替换为单横杠
      - 仅保留字母数字与横杠
      - 合并连续横杠, 去除首尾横杠
      - 最长 60 字符
    """
    raw = source_id or name
    if not raw:
        raw = 'unnamed-skill'
    slug = raw.lower()
    # 空格、下划线 -> 横杠
    slug = re.sub(r'[\s_]+', '-', slug)
    # 移除特殊字符 (仅保留 a-z 0-9 -)
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # 合并连续横杠
    slug = re.sub(r'-+', '-', slug)
    # 去除首尾横杠
    slug = slug.strip('-')
    # 限制长度
    if len(slug) > 60:
        slug = slug[:60].rstrip('-')
    return slug or 'unnamed-skill'


def get_existing_slugs_from_db() -> Set[str]:
    """查询数据库 skills 表获取所有已存在的 slug。"""
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT DISTINCT slug FROM skills")
    slugs = {row[0] for row in c.fetchall() if row[0]}
    conn.close()
    return slugs


def resolve_slug_conflict(
    base_slug: str,
    existing_slugs: Set[str],
    batch_slugs: Set[str],
) -> str:
    """检测 slug 冲突, 冲突时自动添加后缀 (-v2, -pro 等)。

    检查范围包括数据库已有 slug 和当前批次已分配 slug。
    """
    all_used = existing_slugs | batch_slugs
    if base_slug not in all_used:
        return base_slug
    for suffix in SLUG_CONFLICT_SUFFIXES:
        candidate = f"{base_slug}{suffix}"
        if candidate not in all_used:
            return candidate
    # 所有预设后缀都冲突, 使用数字递增
    counter = 6
    while True:
        candidate = f"{base_slug}-v{counter}"
        if candidate not in all_used:
            return candidate
        counter += 1


# ============================================================
# displayName 生成
# ============================================================

def generate_display_name(name: str) -> str:
    """从 name 派生 displayName (<=20字符)。

    规则:
      - 移除常见的 Free/Paid/Pro 后缀
      - 去除首尾空白
      - 截断至 20 字符
    """
    display = re.sub(r'\s+(free|paid|pro)$', '', name, flags=re.IGNORECASE)
    display = display.strip()
    if len(display) > 20:
        display = display[:20]
    return display if display else name[:20]


# ============================================================
# summary 生成 (痛点+方案+量化公式)
# ============================================================

def generate_summary(name: str, description: str, category: str) -> str:
    """基于 description 生成 summary, 使用"痛点+方案+量化"公式 (<=100字符)。

    公式: [痛点]。[方案]，[主题]场景[量化指标]。
    """
    pain, solution = CATEGORY_PAIN_SOLUTION_MAP.get(
        category, CATEGORY_PAIN_SOLUTION_MAP['Other']
    )

    # 从 name 提取核心主题
    topic = name.replace('-', ' ').replace('_', ' ').strip()
    topic = re.sub(r'\s+(free|paid|pro)$', '', topic, flags=re.IGNORECASE).strip()
    if not topic:
        topic = category

    # 量化指标
    quant = '效率提升3倍'

    summary = f"{pain}。{solution}，{topic}场景{quant}。"

    # 截断至 100 字符
    if len(summary) > 100:
        summary = summary[:97] + '...'

    return summary


# ============================================================
# pricing_tier 评估 (L1-L4)
# ============================================================

def evaluate_pricing_tier(candidate: Dict[str, Any]) -> str:
    """根据内容复杂度评估 pricing_tier (L1-L4)。

    评估维度:
      - 描述与内容预览长度
      - 复杂关键词命中数
      - 分类复杂度权重
    """
    description = candidate.get('description', '')
    content_preview = candidate.get('content_preview', '')
    name = candidate.get('name', '')
    category = candidate.get('category', 'Other')

    complexity_score = 0

    # 维度1: 描述长度
    desc_len = len(description) + len(content_preview)
    if desc_len > 500:
        complexity_score += 3
    elif desc_len > 200:
        complexity_score += 2
    elif desc_len > 50:
        complexity_score += 1

    # 维度2: 复杂关键词命中
    combined_text = (description + content_preview + name).lower()
    complex_keywords = [
        'api', 'integration', 'pipeline', 'workflow', 'enterprise',
        'batch', 'automat', 'monitor', 'deploy', 'security', 'analytics',
        'dashboard', 'sync', 'webhook', 'multi', 'real-time', 'stream',
        'cluster', 'scalable', 'distributed',
    ]
    keyword_count = sum(1 for kw in complex_keywords if kw in combined_text)
    complexity_score += min(keyword_count, 4)

    # 维度3: 分类复杂度
    complex_categories = {'DevOps', 'Security', 'Data', 'AI', 'Developer'}
    if category in complex_categories:
        complexity_score += 2

    # 评估等级
    if complexity_score >= 7:
        return 'L4-企业级'
    elif complexity_score >= 5:
        return 'L3-专业级'
    elif complexity_score >= 3:
        return 'L2-进阶级'
    else:
        return 'L1-基础级'


# ============================================================
# SKILL.md 生成
# ============================================================

def generate_skill_md(
    slug: str,
    display_name: str,
    summary: str,
    description: str,
    pricing_tier: str,
    category: str,
    source: str,
    url: str,
    tools: Optional[List[str]] = None,
) -> str:
    """生成标准 SKILL.md 内容。

    包含:
      - frontmatter (slug/displayName/version/summary/license/description/tools 等)
      - ## 核心功能
      - ## 输入格式
      - ## 输出格式
      - ## 依赖说明
    """
    if tools is None:
        tools = ['read', 'exec']

    price = TIER_PRICE_MAP.get(pricing_tier, '19.9')

    # description 清理
    desc_clean = description.strip().replace('"', "'").replace('\n', ' ')
    if len(desc_clean) > 200:
        desc_clean = desc_clean[:197] + '...'

    lines: List[str] = []

    # ---- frontmatter ----
    lines.append('---')
    lines.append(f'slug: "{slug}"')
    lines.append(f'name: "{slug}"')
    lines.append('version: "1.0.0"')
    lines.append(f'displayName: "{display_name}"')
    lines.append(f'summary: "{summary}"')
    lines.append('license: "Proprietary"')
    lines.append('edition: "pro"')
    lines.append('description: |-')
    lines.append(
        f'  {desc_clean} Use when 需要{category}领域自动化处理、'
        f'数据分析和流程编排时使用。不适用于无明确需求的模糊场景。'
    )
    lines.append('tags:')
    lines.append(f'  - {category}')
    lines.append('  - automation')
    lines.append('tools:')
    for t in tools:
        lines.append(f'  - {t}')
    lines.append('homepage: "https://skillhub.cn"')
    lines.append(f'suggested_price: "{price} CNY/per_use"')
    lines.append(f'pricing_tier: "{pricing_tier}"')
    lines.append('pricing_model: "per_use"')
    lines.append('---')

    # ---- 正文 ----
    lines.append('')
    lines.append(f'# {display_name}')
    lines.append('')

    # ## 核心功能
    lines.append('## 核心功能')
    lines.append('')
    lines.append(f'### 功能1：{display_name}核心处理')
    lines.append(
        f'**解决痛点**：传统{category}场景中，手工操作效率低、容易出错、'
        f'难以规模化，缺乏统一的标准流程。'
    )
    lines.append('')
    lines.append('**专业版能力**：')
    lines.append(f'- 自动化{category}数据处理流程，减少人工干预与重复劳动')
    lines.append('- 结构化输入输出，支持批量操作与结果导出')
    lines.append('- 内置错误恢复机制，异常自动重试与降级处理')
    lines.append('- 多格式兼容，适配不同来源的数据接入与转换')
    lines.append(f'- 基于{source}来源验证，保证数据准确性与可追溯性')
    lines.append('')
    lines.append(
        f'**处理**：解析用户输入参数，执行{display_name}核心处理逻辑，'
        f'返回结构化结果与执行状态。'
    )
    lines.append('')

    # ## 输入格式
    lines.append('## 输入格式')
    lines.append('')
    lines.append('| 参数名 | 类型 | 必填 | 说明 |')
    lines.append('|--------|------|------|------|')
    lines.append(f'| content | string | 是 | {display_name}处理的内容输入 |')
    lines.append('| format | string | 否 | 输入格式, 可选值: json/text/markdown |')
    lines.append('| options | object | 否 | 高级配置参数, 如输出风格、批量大小等 |')
    lines.append('')

    # ## 输出格式
    lines.append('## 输出格式')
    lines.append('')
    lines.append('```json')
    lines.append('{')
    lines.append('  "success": true,')
    lines.append('  "data": {')
    lines.append(f'    "result": "{display_name}处理结果",')
    lines.append('    "metadata": {')
    lines.append(f'      "skill": "{slug}",')
    lines.append('      "version": "1.0.0",')
    lines.append(f'      "pricing_tier": "{pricing_tier}"')
    lines.append('    }')
    lines.append('  },')
    lines.append('  "error": null')
    lines.append('}')
    lines.append('```')
    lines.append('')

    # ## 依赖说明
    lines.append('## 依赖说明')
    lines.append('')
    lines.append('### 运行环境')
    lines.append('- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）')
    lines.append('- **操作系统**: Windows / macOS / Linux')
    lines.append('')
    lines.append('### 依赖项')
    lines.append('| 依赖项 | 类型 | 是否必需 | 获取方式 |')
    lines.append('|:-------|:-----|:---------|:---------|')
    lines.append('| LLM API | API | 必需 | 由Agent平台内置LLM提供 |')
    lines.append(f'| 数据源 | 数据 | 必需 | 来自{source}来源: {url} |')
    lines.append('')

    return '\n'.join(lines)


# ============================================================
# 数据库更新
# ============================================================

def update_database(
    slug: str,
    name: str,
    display_name: str,
    version: str,
    category: str,
    source: str,
    source_slug: str,
    source_url: str,
    local_path: str,
    pricing_tier: str,
    pricing_model: str = 'per_use',
) -> int:
    """更新数据库 skills 表, 插入或更新 skill 记录。

    返回 skill_id。
    """
    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()

    # 检查是否已存在
    c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
    existing = c.fetchone()

    if existing:
        skill_id = existing[0]
        c.execute("""
            UPDATE skills SET
                current_name = ?,
                current_display_name = ?,
                current_version = ?,
                category = ?,
                source = ?,
                source_slug = ?,
                source_url = ?,
                source_license = ?,
                local_path = ?,
                updated_at = ?,
                current_status = ?,
                is_differentiated = ?,
                differentiation_date = ?,
                pricing_model = ?,
                skill_type = ?,
                edition = ?,
                workflow_state = ?
            WHERE id = ?
        """, (
            name, display_name, version, category, source,
            source_slug, source_url, 'Proprietary',
            local_path, now, 'differentiated',
            1, now, pricing_model, 'md',
            'pro', 'step2_auto_differentiate',
            skill_id,
        ))
    else:
        c.execute("""
            INSERT INTO skills (
                slug, current_name, current_display_name, current_version,
                category, source, source_slug, source_url, source_license,
                local_path, created_at, updated_at, current_status,
                is_differentiated, differentiation_date, pricing_model,
                skill_type, edition, workflow_state
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            slug, name, display_name, version,
            category, source, source_slug, source_url, 'Proprietary',
            local_path, now, now, 'differentiated',
            1, now, pricing_model,
            'md', 'pro', 'step2_auto_differentiate',
        ))
        skill_id = c.lastrowid

    # 记录版本
    c.execute("""
        INSERT INTO versions (skill_id, version, created_at, changelog)
        VALUES (?, ?, ?, ?)
    """, (skill_id, version, now, f"Auto-differentiated {slug} v{version} ({pricing_tier})"))

    # 记录操作
    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        skill_id, 'differentiate', now, 'auto_differentiate',
        f'Auto-differentiated from source={source}, source_slug={source_slug}, tier={pricing_tier}',
        'differentiated',
    ))

    conn.commit()
    conn.close()
    return skill_id


# ============================================================
# 候选数据加载与筛选
# ============================================================

# CLI 简写 -> 实际 source 字段值 映射
# multi_source_discover.py 产出的 source 字段值: hermes / github-search / awesome-list 等
SOURCE_ALIAS_MAP: Dict[str, str] = {
    'hermes': 'hermes',
    'github': 'github-search',
    'awesome': 'awesome-list',
    'n8n': 'n8n',
    'dify': 'dify',
    'coze': 'coze',
}


def load_candidates(source_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """从 candidates_unified.json 加载候选 skill 列表。

    Args:
        source_filter: 如果指定, 只返回该来源的候选 (hermes/github/awesome 等)
                       支持简写: github -> github-search, awesome -> awesome-list
    """
    if not CANDIDATES_FILE.exists():
        print(f"[ERROR] 候选文件不存在: {CANDIDATES_FILE}")
        print("        请先运行 multi_source_discover.py 生成候选数据。")
        sys.exit(1)

    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # candidates_unified.json 结构: {generated_at, total_count, candidates: [...]}
    if isinstance(data, dict):
        candidates = data.get('candidates', [])
    elif isinstance(data, list):
        candidates = data
    else:
        candidates = []

    if source_filter:
        # 简写映射
        actual_source = SOURCE_ALIAS_MAP.get(source_filter, source_filter)
        candidates = [c for c in candidates if c.get('source') == actual_source]

    return candidates


# ============================================================
# 主处理逻辑
# ============================================================

def process_candidates(
    candidates: List[Dict[str, Any]],
    limit: int = 50,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """处理候选列表, 生成差异化 SKILL.md 并更新数据库。

    Returns:
        包含处理统计的字典
    """
    # 截取前 limit 个
    candidates = candidates[:limit]

    # 获取数据库已有 slug
    existing_slugs = get_existing_slugs_from_db()

    # 当前批次已分配 slug (用于批次内去重)
    batch_slugs: Set[str] = set()

    stats = {
        'total': len(candidates),
        'created': 0,
        'skipped': 0,
        'errors': 0,
        'details': [],
    }

    print(f"\n{'='*60}")
    print(f"自动差异化系统 - Step 2")
    print(f"{'='*60}")
    print(f"候选总数: {len(candidates)}")
    print(f"模式: {'DRY-RUN (仅输出计划)' if dry_run else 'EXECUTE (实际创建)'}")
    print(f"{'='*60}\n")

    for idx, candidate in enumerate(candidates, 1):
        source = candidate.get('source', 'unknown')
        source_id = candidate.get('source_id', '')
        name = candidate.get('name', '')
        description = candidate.get('description', '')
        category = candidate.get('category', 'Other')
        url = candidate.get('url', '')
        content_preview = candidate.get('content_preview', '')

        # a. 生成 slug
        base_slug = generate_slug(source_id, name)

        # b. 检查 slug 冲突并解决
        final_slug = resolve_slug_conflict(base_slug, existing_slugs, batch_slugs)
        batch_slugs.add(final_slug)

        # c. 生成 displayName
        display_name = generate_display_name(name)

        # d. 生成 summary
        summary = generate_summary(name, description, category)

        # e. 评估 pricing_tier
        pricing_tier = evaluate_pricing_tier(candidate)

        # f. 准备输出路径
        skill_dir = SKILLHUB_ROOT / final_slug
        skill_md_path = skill_dir / 'SKILL.md'

        # 生成 SKILL.md 内容
        skill_md_content = generate_skill_md(
            slug=final_slug,
            display_name=display_name,
            summary=summary,
            description=description,
            pricing_tier=pricing_tier,
            category=category,
            source=source,
            url=url,
        )

        # 状态标记: NEW / CONFLICT / EXISTS
        if final_slug != base_slug:
            status = f'CONFLICT ({base_slug} -> {final_slug})'
        elif final_slug in existing_slugs:
            status = 'UPDATE'
        else:
            status = 'NEW'

        print(
            f"[{idx:3d}/{len(candidates)}] {status:20s} | "
            f"slug={final_slug:40s} | "
            f"display={display_name:20s} | "
            f"tier={pricing_tier}"
        )

        detail = {
            'index': idx,
            'source': source,
            'source_id': source_id,
            'name': name,
            'slug': final_slug,
            'base_slug': base_slug,
            'display_name': display_name,
            'summary': summary,
            'pricing_tier': pricing_tier,
            'category': category,
            'status': status,
            'skill_md_path': str(skill_md_path),
        }
        stats['details'].append(detail)

        if dry_run:
            stats['skipped'] += 1
            continue

        # 实际创建
        try:
            # 创建输出目录
            skill_dir.mkdir(parents=True, exist_ok=True)

            # 写入 SKILL.md
            with open(skill_md_path, 'w', encoding='utf-8') as f:
                f.write(skill_md_content)

            # 更新数据库
            skill_id = update_database(
                slug=final_slug,
                name=name,
                display_name=display_name,
                version='1.0.0',
                category=category,
                source=source,
                source_slug=source_id,
                source_url=url,
                local_path=str(skill_md_path),
                pricing_tier=pricing_tier,
            )

            detail['skill_id'] = skill_id
            stats['created'] += 1

        except Exception as e:
            print(f"  [ERROR] {final_slug}: {e}")
            stats['errors'] += 1
            detail['error'] = str(e)

    # 输出统计
    print(f"\n{'='*60}")
    print(f"处理完成")
    print(f"{'='*60}")
    print(f"总候选数:  {stats['total']}")
    print(f"成功创建:  {stats['created']}")
    print(f"跳过(dry): {stats['skipped']}")
    print(f"错误:      {stats['errors']}")
    print(f"{'='*60}\n")

    return stats


# ============================================================
# CLI 入口
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='自动差异化系统 (流水线 Step 2) - 从候选 skill 生成差异化 SKILL.md',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python auto_differentiate.py                         # 处理前50个候选
  python auto_differentiate.py --limit 100             # 处理前100个候选
  python auto_differentiate.py --source hermes         # 只处理hermes来源
  python auto_differentiate.py --source github         # 只处理github来源
  python auto_differentiate.py --source awesome         # 只处理awesome-list来源
  python auto_differentiate.py --dry-run               # 只输出计划不实际创建
        """,
    )
    parser.add_argument(
        '--limit', type=int, default=50,
        help='只处理前N个候选 (默认: 50)',
    )
    parser.add_argument(
        '--source', type=str, default=None,
        choices=['hermes', 'github', 'awesome', 'n8n', 'dify', 'coze'],
        help='只处理指定来源的候选',
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='只输出处理计划, 不实际创建文件或更新数据库',
    )

    args = parser.parse_args()

    # 加载候选
    candidates = load_candidates(source_filter=args.source)
    print(f"加载候选: {len(candidates)} 个 (source={args.source or 'all'})")

    if not candidates:
        print("没有符合条件的候选, 退出。")
        return

    # 处理
    process_candidates(
        candidates=candidates,
        limit=args.limit,
        dry_run=args.dry_run,
    )


if __name__ == '__main__':
    main()
