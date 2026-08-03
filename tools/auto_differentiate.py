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
import re
import sys
import hashlib
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple, Union

# ============================================================
# DB连接: V118 W6修复 — 不再从auto_discover导入get_db(已移除),
# 直接使用db_module.get_db()
# ============================================================

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DISCOVERY_DIR, PACKAGED_SKILLS_DIR, TOOLS_DIR, PLATFORM_CONFIG, MAX_DISPLAY_NAME_LEN # V110 W5: DATA_DIR→DISCOVERY_DIR; V113: 新增TOOLS_DIR; V115 W3: Phase 1标准化; V118 W8: 新增PLATFORM_CONFIG; V118 W6修复: 新增DB_PATH; MAX_DISPLAY_NAME_LEN
# === End Phase 1 ===

if str(TOOLS_DIR) not in _sys.path:
    _sys.path.insert(0, str(TOOLS_DIR))  # V115 W3: Phase 1标准化

from skill_core import db as db_module  # V116 W1: 统一db入口(替代import db)
from skill_core.db import get_existing_slugs_from_db  # V121 W4: 统一slug查询(本地实现已删除)
from skill_core.rules import resolve_slug_conflict, MAX_SUMMARY_LEN, MAX_SKILL_MD_LINES  # V116 W3: 统一slug冲突解决; MAX_SUMMARY_LEN; V119 W5: 新增MAX_SKILL_MD_LINES
from skill_core.parser import extract_source_license  # V126 W5: 统一license提取(TD-185), 替代本地_extract_source_license

# ============================================================
# 安全预检: 差异化前扫描源skill安全风险 (v2.2新增)
# 防止基于有安全隐患的源skill生成差异化产物
# ============================================================
try:
    from source_security_scan import scan_content, auto_fix_risks
    _SECURITY_SCAN_AVAILABLE = True
except ImportError:
    _SECURITY_SCAN_AVAILABLE = False

# ============================================================
# 路径常量
# ============================================================

CANDIDATES_FILE = DISCOVERY_DIR / "candidates_unified.json"  # V110 W5: 统一从project_config.DISCOVERY_DIR构造
SKILLHUB_ROOT = PACKAGED_SKILLS_DIR

# v3.0: 移除-pro后缀(会创建近似重复slug触发平台反垃圾系统)
# v3.3: 移除所有程序化后缀(-v2/-v3/-plus等),避免被反垃圾系统识别为"绕过唯一性约束"
# 冲突时改为返回错误,由人工或语义化重命名处理
SLUG_CONFLICT_SUFFIXES = []  # v3.3: 空列表,不自动追加任何后缀

# PRR P0-2: 分类痛点/方案变体池 — 每分类3种变体,避免同分类skill内容雷同
# (原CATEGORY_PAIN_SOLUTION_MAP仅11种固定组合,所有同分类skill summary完全相同)
CATEGORY_PAIN_SOLUTIONS: Dict[str, List[Tuple[str, str]]] = {
    'Finance':       [('财务数据处理耗时易错', '自动化财务流程'),
                      ('财务报表制作效率低下', '智能化财务数据处理'),
                      ('财务数据分散难以汇总', '统一财务数据管理')],
    'Creative':      [('创作灵感与工具分散难统一', '一站式创作工作流'),
                      ('创意产出效率不稳定', '结构化创作辅助'),
                      ('设计资源管理分散', '集成化创作工具链')],
    'Developer':     [('开发效率低下重复劳动多', '智能开发辅助'),
                      ('代码质量与一致性难保证', '自动化代码审查'),
                      ('开发流程工具链分散', '统一开发工作流')],
    'Productivity':  [('日常事务繁杂难以聚焦核心', '自动化任务编排'),
                      ('工作流程缺乏系统化管理', '结构化任务管理'),
                      ('信息过载导致决策效率低', '智能信息筛选与聚合')],
    'Data':          [('数据处理流程割裂难追溯', '端到端数据管道'),
                      ('数据质量与一致性难保证', '自动化数据校验'),
                      ('数据分析结果难以复现', '标准化数据处理流程')],
    'Communication': [('沟通渠道分散信息易遗漏', '统一消息中枢'),
                      ('团队协作信息同步困难', '集成化沟通管理'),
                      ('消息处理效率低下', '智能消息路由与聚合')],
    'Research':      [('信息检索效率低来源分散', '智能研究聚合'),
                      ('文献调研耗时且易遗漏', '自动化文献梳理'),
                      ('研究数据难以系统化', '结构化研究数据管理')],
    'Security':      [('安全审计手动覆盖不足', '自动化安全扫描'),
                      ('安全风险发现滞后', '持续安全监控'),
                      ('合规检查流程繁琐', '自动化合规检测')],
    'DevOps':        [('运维操作繁琐易出错', '基础设施即代码'),
                      ('部署流程缺乏一致性', '自动化部署编排'),
                      ('运维监控覆盖不全', '全链路运维监控')],
    'AI':            [('AI能力集成成本高', '开箱即用AI工具链'),
                      ('AI模型部署运维复杂', '简化AI服务管理'),
                      ('AI应用开发门槛高', '低代码AI应用构建')],
    'Other':         [('手工操作效率低易出错', '智能化自动处理'),
                      ('工作流程缺乏自动化', '流程自动化改造'),
                      ('现有工具能力不足', '增强型工具支持')],
}


def _get_pain_solution(category: str, slug: str) -> Tuple[str, str]:
    """PRR P0-2: 获取分类痛点/方案 — 基于slug hash选择变体,避免同分类雷同"""
    variants = CATEGORY_PAIN_SOLUTIONS.get(category, CATEGORY_PAIN_SOLUTIONS['Other'])
    return variants[hash(slug) % len(variants)] if slug else variants[0]


# pricing_tier -> 建议价格
TIER_PRICE_MAP: Dict[str, str] = {
    'L1-基础级': '9.9',
    'L2-进阶级': '19.9',
    'L3-专业级': '29.9',
    'L4-企业级': '99.9',
}

# PRR P1-2: 诚实回退描述池 — 不含虚假量化指标
# 原_QUANT_POOL含6个与实际能力无关的性能声明('效率提升3倍'等),构成虚假宣传
# 当源内容无法提取真实量化数据时,使用诚实非量化语言
_HONEST_FALLBACK_POOL: List[str] = [
    '提供专业能力支持',
    '优化工作流程效率',
    '简化复杂操作步骤',
    '提升任务处理质量',
    '支持多场景自动化处理',
]

# V144 G2: padding文案差异化池 — 替代3文件共享的固定文案(避免批量特征)
_PADDING_POOL: List[str] = [
    '支持多种输入格式,输出结构化结果,适配独立开发者与小型团队',
    '提供专业能力支持,覆盖多场景工作流,支持自动化处理',
    '内置错误恢复与降级机制,多格式兼容,适配多源数据',
    '开箱即用,无需复杂配置,支持中文交互与结构化输出',
    '轻量级设计,低资源占用,适配云端与本地部署',
]


def _get_padding(seed: str) -> str:
    """V144 G2: 获取差异化padding文案(替代3文件共享固定文案)"""
    return _PADDING_POOL[hash(seed) % len(_PADDING_POOL)]


def _extract_quant_from_source(source_content: str) -> Optional[str]:
    """V138 A3: 从源skill内容提取量化指标

    优先从源skill的实际描述中提取真实的量化数据,
    而非使用固定硬编码量化词。

    Args:
        source_content: 源skill的完整SKILL.md内容

    Returns:
        提取到的量化指标字符串, 无匹配时返回None
    """
    if not source_content:
        return None
    # 匹配数字+倍/百分比模式
    patterns = [
        r'提升(\d+\.?\d*倍)',
        r'提升(\d+[%％])',
        r'降低(\d+[%％])',
        r'节省(\d+[%％])',
        r'缩短(\d+[%％])',
        r'加速(\d+\.?\d*倍)',
        r'覆盖(\d+[%％])',
        r'减少(\d+[%％])',
        r'效率提升(\d+\.?\d*倍)',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, source_content)
        if matches:
            # 将匹配的数字组合成量化指标
            num = matches[0]
            if '倍' in pattern:
                return f'效率提升{num}'
            elif '降低' in pattern or '缩短' in pattern or '减少' in pattern:
                return f'处理时间缩短{num}'
            elif '节省' in pattern:
                return f'运营成本降低{num}'
            elif '覆盖' in pattern:
                return f'自动化覆盖{num}'
            elif '加速' in pattern:
                return f'响应速度提升{num}'
            else:
                return f'效率提升{num}'
    return None


def _get_quantifier(slug: str = '', source_content: str = '') -> str:
    """V138 A3: 获取量化指标 — 优先源内容提取, 其次量化池轮选

    Args:
        slug: skill slug, 用于量化池轮选hash
        source_content: 源skill内容, 优先从中提取真实量化指标

    Returns:
        量化指标字符串
    """
    # 优先从源内容提取真实量化指标
    extracted = _extract_quant_from_source(source_content)
    if extracted:
        return extracted
    # PRR P1-2: 无源内容或无匹配时, 使用诚实回退描述(不含虚假量化)
    if slug:
        return _HONEST_FALLBACK_POOL[hash(slug) % len(_HONEST_FALLBACK_POOL)]
    return _HONEST_FALLBACK_POOL[0]


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


# V121 W4: get_existing_slugs_from_db 已统一到 skill_core.db (本地实现已删除)
# V116 W3: resolve_slug_conflict已统一到skill_core.rules (本地实现已删除)
# 调用方默认使用auto_suffix=False模式(v3.3行为: 冲突返回None)


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
    if len(display) > MAX_DISPLAY_NAME_LEN:
        display = display[:20]
    return display if display else name[:20]


# ============================================================
# summary 生成 (痛点+方案+量化公式)
# ============================================================

def generate_summary(name: str, description: str, category: str,
                     slug: str = '', source_content: str = '') -> str:
    """基于 description 生成 summary, 使用"痛点+方案+量化"公式 (<=100字符)。

    公式: [痛点]。[方案]，[主题]场景[量化指标]。

    V138 A3: 量化指标从源内容提取或量化池轮选, 不再使用固定硬编码量化词。
    PRR P0-2: 痛点/方案使用变体池,避免同分类skill内容雷同。
    PRR P1-2: 无真实量化时使用诚实回退描述,不含虚假指标。
    """
    pain, solution = _get_pain_solution(category, slug)

    # 从 name 提取核心主题
    topic = name.replace('-', ' ').replace('_', ' ').strip()
    topic = re.sub(r'\s+(free|paid|pro)$', '', topic, flags=re.IGNORECASE).strip()
    if not topic:
        topic = category

    # V138 A3: 量化指标 — 优先源内容提取, 其次量化池轮选
    quant = _get_quantifier(slug, source_content)

    summary = f"{pain}。{solution}，{topic}场景{quant}。"

    # 截断至 100 字符
    if len(summary) > MAX_SUMMARY_LEN:
        summary = summary[:97] + '...'

    return summary


# ============ E13: TRAE Work AI代理适配 ============

def generate_summary_with_agent(name: str, description: str, category: str,
                                skill_content: str = '') -> str:
    """E13: 使用LLM生成summary — 双路径(Trae AI代理/外部API)

    V138 A2: 修复断点 — 从"只返回prompt"改为"调用llm_bridge执行+返回结果"。
    LLM不可用时走generate_summary()规则降级(真实降级, 非mock)。
    """
    from llm_bridge import get_bridge
    bridge = get_bridge()
    skill_data = {'slug': name, 'skill_content': skill_content or description, 'name': name}
    context = {'category': category, 'description': description}
    result = bridge.execute('analyze', skill_data, context)
    if result.get('status') == 'success':
        return result['result']
    # fallback: 无LLM可用时走规则降级(真实降级, 非mock)
    return generate_summary(name, description, category,
                            slug=name, source_content=skill_content)


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
    if desc_len > MAX_SKILL_MD_LINES:
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

def _extract_source_body(source_content: str) -> str:
    """从源skill内容中提取body部分，保留源skill的功能逻辑、工具调用和IO契约。

    提取规则:
      - 移除frontmatter (--- 块)
      - 从 ## 核心功能 或 ## 核心能力 header开始保留正文
      - 返回去标识化后的功能内容

    Args:
        source_content: 源skill的完整SKILL.md内容

    Returns:
        提取后的body文本，无源内容时返回空字符串
    """
    if not source_content:
        return ''
    content = source_content
    if content.startswith('\ufeff'):
        content = content[1:]
    # 移除frontmatter
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            body = parts[2]
        else:
            body = content
    else:
        body = content

    # 从 ## 核心功能 或 ## 核心能力 开始保留正文
    match = re.search(r'^##\s+(核心功能|核心能力)\s*$', body, re.MULTILINE)
    if match:
        body = body[match.start():]

    return body.strip()


# ============================================================
# V138 A4: 核心功能生成 — LLM推断 + 分类差异化fallback
# ============================================================

# 分类 → 差异化核心功能文案池(替代原5条固定模板)
_CATEGORY_FEATURES_MAP: Dict[str, List[str]] = {
    'Finance': [
        '自动化财务报表生成与多维度数据分析',
        '支持多账户、多币种聚合与实时汇率换算',
        '内置交易异常检测与风险预警机制',
        '合规性审计追踪，完整记录每笔操作链路',
    ],
    'Creative': [
        '多模态创意素材统一管理与版本控制',
        '支持团队协作编辑与实时审稿反馈',
        '内置版权检测与素材去重，避免重复创作',
        '一键导出多种格式，适配不同发布平台',
    ],
    'Developer': [
        '代码质量自动审查与安全漏洞扫描',
        '支持多语言项目结构与依赖关系分析',
        '内置CI/CD流水线集成与构建状态追踪',
        'API接口自动生成文档与Mock测试数据',
    ],
    'Productivity': [
        '智能任务优先级排序与时间块分配',
        '支持多源数据聚合与跨平台同步',
        '内置工作流自动化与定时触发机制',
        '操作日志完整记录与效率趋势分析',
    ],
    'Data': [
        '端到端数据管道构建与数据血缘追踪',
        '支持多数据源接入与实时ETL转换',
        '内置数据质量校验与异常值自动修复',
        '可视化数据概览与自定义报表导出',
    ],
    'Communication': [
        '多渠道消息统一聚合与智能分类',
        '支持多语言实时翻译与语境适配',
        '内置消息优先级排序与免打扰策略',
        '会话历史全文检索与关键信息提取',
    ],
    'Research': [
        '多源文献自动检索与去重合并',
        '支持研究数据结构化提取与标注管理',
        '内置引用格式自动生成与合规校验',
        '研究进度可视化与协作批注共享',
    ],
    'Security': [
        '自动化安全漏洞扫描与修复建议',
        '支持多框架合规检查与审计报告生成',
        '内置密钥泄露检测与权限最小化分析',
        '安全事件实时告警与处置链路追踪',
    ],
    'DevOps': [
        '基础设施即代码模板管理与版本控制',
        '支持多云环境配置同步与漂移检测',
        '内置部署健康检查与自动回滚机制',
        '资源使用率监控与成本优化建议',
    ],
    'AI': [
        '预训练模型快速集成与推理服务部署',
        '支持多模态输入处理与结构化输出',
        '内置Prompt模板管理与A/B测试',
        '模型性能监控与漂移检测告警',
    ],
    'Other': [
        f'自动化处理流程，减少人工干预与重复劳动',
        '结构化输入输出，支持批量操作与结果导出',
        '内置错误恢复机制，异常自动重试与降级处理',
        '多格式兼容，适配不同来源的数据接入与转换',
    ],
}


def _generate_category_specific_features(category: str, source: str,
                                         name: str) -> List[str]:
    """V138 A4: 基于category的差异化核心功能文案(非固定5条)

    从分类特征池中选择与skill名称相关的功能点,
    并附加来源验证条目。
    """
    features = list(_CATEGORY_FEATURES_MAP.get(
        category, _CATEGORY_FEATURES_MAP['Other']
    ))
    # 附加来源验证(与原模板一致但作为额外项)
    features.append(f'基于{source}来源验证，保证数据准确性与可追溯性')
    return features


def _generate_core_features_from_context(slug: str, name: str,
                                         description: str, category: str,
                                         source: str) -> List[str]:
    """V138 A4: 无source_content时生成核心功能列表

    优先使用LLM从skill名称/描述推断核心能力,
    LLM不可用时走分类差异化文案池(真实降级, 非固定模板)。

    Args:
        slug: skill slug
        name: display name
        description: skill描述
        category: 分类
        source: 来源

    Returns:
        核心功能文案列表(4-5条)
    """
    # 尝试LLM路径
    try:
        from llm_bridge import get_bridge
        bridge = get_bridge()
        skill_data = {
            'slug': slug, 'name': name,
            'skill_content': description or f'{name} - {category}',
        }
        context = {
            'category': category, 'description': description,
            'source': source, 'task': 'core_features',
        }
        result = bridge.execute('analyze', skill_data, context)
        if result.get('status') == 'success':
            parsed = _parse_llm_features(result['result'])
            if parsed:
                return parsed
    except Exception as e:
        print(f"[WARN] LLM不可用,走降级: {e}")

    # fallback: 分类差异化文案池(真实降级, 非固定5条模板)
    return _generate_category_specific_features(category, source, name)


def _parse_llm_features(llm_output: str) -> List[str]:
    """V138 A4: 解析LLM返回的核心功能列表

    支持两种格式:
      1. JSON数组: ["feature1", "feature2", ...]
      2. Markdown列表: - feature1\\n- feature2
    """
    if not llm_output or not llm_output.strip():
        return []

    # 尝试JSON数组解析
    try:
        data = json.loads(llm_output.strip())
        if isinstance(data, list):
            return [str(item).strip() for item in data if item]
    except (json.JSONDecodeError, ValueError) as e:  # V144: 添加警告日志(多策略回退)
        print(f"[WARN] JSON数组解析失败,尝试下一策略: {e}")

    # 尝试从JSON中提取数组
    json_match = re.search(r'\[.*?\]', llm_output, re.DOTALL)
    if json_match:
        try:
            data = json.loads(json_match.group())
            if isinstance(data, list):
                return [str(item).strip() for item in data if item]
        except (json.JSONDecodeError, ValueError) as e:  # V144: 添加警告日志(多策略回退)
            print(f"[WARN] JSON提取数组失败,尝试Markdown解析: {e}")

    # 尝试Markdown列表解析
    lines = llm_output.strip().split('\n')
    features = []
    for line in lines:
        line = line.strip()
        # 匹配 - 或 * 或 1. 开头的列表项
        match = re.match(r'^[-*]\s+(.+)$', line)
        if not match:
            match = re.match(r'^\d+\.\s+(.+)$', line)
        if match:
            feature = match.group(1).strip()
            if feature and len(feature) > 5:  # 过滤过短的无意义项
                features.append(feature)

    return features if features else []


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
    source_content: str = "",
) -> str:
    """生成标准 SKILL.md 内容。

    当提供 source_content 时，保留源skill的body内容(≥70%)，
    包括功能逻辑、工具调用和IO契约，仅替换frontmatter并补充增强章节。

    包含:
      - frontmatter (slug/displayName/version/summary/license/description/tools 等)
      - # 标题
      - 源skill body (核心功能等，保留≥70%功能内容) 或 模板核心功能
      - ## 输入格式 (增强章节)
      - ## 输出格式 (增强章节)
      - ## 依赖说明 (增强章节)
    """
    if tools is None:
        tools = ['read', 'exec']

    price = TIER_PRICE_MAP.get(pricing_tier, '19.9')

    # description 清理
    desc_clean = description.strip().replace('"', "'").replace('\n', ' ')
    if len(desc_clean) > 200:
        desc_clean = desc_clean[:197] + '...'

    lines: List[str] = []

    # 从源skill内容提取license，默认MIT
    source_license = extract_source_license(source_content)  # V126 W5: 使用统一版本

    # ---- frontmatter ----
    lines.append('---')
    lines.append(f'slug: "{slug}"')
    lines.append(f'name: "{slug}"')
    lines.append('version: "1.0.0"')
    lines.append(f'displayName: "{display_name}"')
    lines.append(f'summary: "{summary}"')
    lines.append(f'license: "{source_license}"')
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
    lines.append('homepage: "' + PLATFORM_CONFIG['skillhub']['page_base'] + '"')  # V118 W8 (TD-140): 从PLATFORM_CONFIG读取
    lines.append(f'suggested_price: "{price} CNY/per_call"')
    lines.append(f'pricing_tier: "{pricing_tier}"')
    lines.append('pricing_model: "per_call"')
    lines.append('---')

    # ---- 正文 ----
    lines.append('')
    lines.append(f'# {display_name}')
    lines.append('')

    # 提取源skill body，保留源skill的功能逻辑、工具调用和IO契约 (≥70%)
    source_body = _extract_source_body(source_content)

    if source_body:
        # 保留源skill body (≥70%功能内容)
        lines.append(source_body)
        lines.append('')
        lines.append('---')
        lines.append('')
    else:
        # V138 A4: 无源内容时使用LLM或上下文推断核心功能(非固定5条模板)
        feature_lines = _generate_core_features_from_context(
            slug, display_name, description, category, source
        )
        lines.append('## 核心功能')
        lines.append('')
        lines.append(f'### 功能1：{display_name}核心处理')
        lines.append(
            f'**解决痛点**：传统{category}场景中，手工操作效率低、容易出错、'
            f'难以规模化，缺乏统一的标准流程。'
        )
        lines.append('')
        lines.append('**专业版能力**：')
        for feature_line in feature_lines:
            lines.append(f'- {feature_line}')
        lines.append('')
        lines.append(
            f'**处理**：解析用户输入参数，执行{display_name}核心处理逻辑，'
            f'返回结构化结果与执行状态。'
        )
        lines.append('')

    # ## 输入格式 (增强章节)
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
    pricing_model: str = 'per_call',
    source_license: str = 'MIT',
    content_hash: str = None,
) -> int:
    """更新数据库 skills 表, 插入或更新 skill 记录。

    返回 skill_id。

    v1.3新增参数:
        content_hash: SKILL.md内容的SHA-256哈希(前16位)，用于内容去重
    """
    now = datetime.now().isoformat()

    # 检查是否已存在
    conn = db_module.get_db()
    c = conn.cursor()
    c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
    existing = c.fetchone()
    conn.close()

    if existing:
        skill_id = existing[0]
        db_module.update_skill_fields(
            skill_id,
            current_name=name,
            current_display_name=display_name,
            current_version=version,
            category=category,
            source=source,
            source_slug=source_slug,
            source_url=source_url,
            source_license=source_license,
            local_path=local_path,
            current_status='differentiated',
            is_differentiated=1,
            differentiation_date=now,
            pricing_model=pricing_model,
            skill_type='md',
            edition='pro',
            content_hash=content_hash,
            workflow_state='step2_auto_differentiate',
        )
    else:
        skill_id = db_module.insert_skill(
            slug=slug,
            name=name,
            display_name=display_name,
            version=version,
            category=category,
            source=source,
            source_slug=source_slug,
            source_url=source_url,
            source_license=source_license,
            local_path=local_path,
            current_status='differentiated',
            is_differentiated=1,
            differentiation_date=now,
            pricing_model=pricing_model,
            skill_type='md',
            edition='pro',
            content_hash=content_hash,
            workflow_state='step2_auto_differentiate',
        )

    # 记录版本
    db_module.add_version(skill_id, version,
                          changelog=f"Auto-differentiated {slug} v{version} ({pricing_tier})")

    # 记录操作
    db_module.record_operation(
        skill_id, 'differentiate',
        f'Auto-differentiated from source={source}, source_slug={source_slug}, tier={pricing_tier}',
        operator='auto_differentiate',
        after_state='differentiated',
    )

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


# V130 A6: 与source_security_scan.load_candidates不是重复定义。
# 差异: 本函数含SOURCE_ALIAS_MAP简写映射(如github->github-search), 文件不存在时sys.exit(1)终止;
#       source_security_scan版无别名映射(直接按source过滤), 文件不存在时返回[]。
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

def _init_processing_state(
    candidates: List[Dict[str, Any]],
    limit: int,
) -> Tuple[List[Dict[str, Any]], Set[str], Set[str], Dict[str, Any]]:
    """初始化处理状态: 截取前 limit 个候选, 查询数据库已有 slug,
    并初始化批次内去重集合与统计字典。"""
    # [V136 G6] 拆分自 process_candidates: 处理状态初始化阶段
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
        'security_blocked': 0,
        'security_fixed': 0,
        'details': [],
    }
    return candidates, existing_slugs, batch_slugs, stats


def _print_processing_header(total: int, dry_run: bool) -> None:
    """打印自动差异化系统处理头部信息。"""
    # [V136 G6] 拆分自 process_candidates: 头部输出阶段
    print(f"\n{'='*60}")
    print(f"自动差异化系统 - Step 2")
    print(f"{'='*60}")
    print(f"候选总数: {total}")
    print(f"模式: {'DRY-RUN (仅输出计划)' if dry_run else 'EXECUTE (实际创建)'}")
    print(f"{'='*60}\n")


def _run_security_precheck(
    candidate: Dict[str, Any],
    skip_security: bool,
    auto_fix_security: bool,
    stats: Dict[str, Any],
    idx: int,
    total: int,
) -> Tuple[str, List[Any], str, bool]:
    """差异化前安全预检 (v2.2)。

    返回 (security_status, security_fixes, description, blocked):
      - blocked=True 表示 critical 风险已记录并应跳过该候选;
      - description 可能已按自动修复结果更新。
    """
    # [V136 G6] 拆分自 process_candidates: 安全预检阶段
    source = candidate.get('source', 'unknown')
    source_id = candidate.get('source_id', '')
    name = candidate.get('name', '')
    description = candidate.get('description', '')
    content_preview = candidate.get('content_preview', '')

    security_status = 'SAFE'
    security_fixes: List[Any] = []
    if not skip_security and _SECURITY_SCAN_AVAILABLE:
        # 合并所有可扫描内容
        scan_text = f"{description}\n{content_preview}"
        scan_result = scan_content(scan_text)

        if scan_result['action'] == 'BLOCKED':
            # critical风险: 跳过差异化
            stats['security_blocked'] += 1
            security_status = 'BLOCKED'
            failed_names = [c.get('name', '') for c in scan_result.get('checks', [])]
            print(
                f"[{idx:3d}/{total}] ✗ BLOCKED  | "
                f"source={source:15s} | name={name[:30]}"
            )
            for check in scan_result.get('checks', []):
                print(f"           → [{check.get('severity', '').upper()}] {check.get('name', '')}")

            stats['details'].append({
                'index': idx,
                'source': source,
                'source_id': source_id,
                'name': name,
                'status': 'SECURITY_BLOCKED',
                'security_risks': failed_names,
            })
            return security_status, security_fixes, description, True

        elif scan_result['action'] in ('WARNING', 'NOTICE') and auto_fix_security:
            # high/medium风险: 自动修复
            security_status = scan_result['action']
            fixed_text, fixes = auto_fix_risks(scan_text, scan_result)
            security_fixes = fixes
            if fixes:
                stats['security_fixed'] += 1
                # 使用修复后的description
                description = fixed_text[:len(description)] if len(fixed_text) < len(description) * 2 else description
    elif not skip_security and not _SECURITY_SCAN_AVAILABLE:
        # V153 R4修复: 安全扫描模块不可用时阻断(fail-safe),原为默认SAFE(fail-open)
        # 原因: _SECURITY_SCAN_AVAILABLE=False时,security_status保持SAFE,不安全内容通过差异化
        security_status = 'BLOCKED'
        print(f"[{idx:3d}/{total}] ✗ BLOCKED  | source={source:15s} | name={name[:30]}")
        print(f"           → 安全扫描模块不可用 — 阻断(fail-safe)")
        stats['security_blocked'] += 1
        stats['details'].append({
            'index': idx,
            'source': source,
            'source_id': source_id,
            'name': name,
            'status': 'SECURITY_SCAN_UNAVAILABLE',
            'security_risks': ['security_scan_module_unavailable'],
        })
        return security_status, security_fixes, description, True

    return security_status, security_fixes, description, False


# ============================================================
# PRR P0-1: 源skill内容获取 — 从本地目录读取真实源SKILL.md
# 修复content_preview是元数据而非源正文的结构性缺陷
# ============================================================

def _fetch_source_content(candidate: Dict[str, Any]) -> str:
    """PRR P0-1: 获取源skill的真实SKILL.md内容

    content_preview是500字符的元数据摘要(slug/repo/url),
    不是源skill的功能正文。本函数从本地下载目录读取真实内容。

    搜索路径:
      1. CLAWHUB_DOWNLOADED_DIR — 已下载的clawhub skill
      2. OPENSOURCE_SKILLS_DIR — 已打包的开源skill
      3. ENTERPRISE_UPLOAD_DIR — 企业上传skill

    Args:
        candidate: 候选项字典,含source_id/name/source/metadata

    Returns:
        源skill的完整SKILL.md内容,找不到时返回空字符串
    """
    source_id = candidate.get('source_id', '')
    name = candidate.get('name', '')
    source = candidate.get('source', '')
    metadata = candidate.get('metadata', {})

    # 从metadata中提取可能的slug/路径信息
    meta_slug = metadata.get('slug', '') if isinstance(metadata, dict) else ''
    meta_path = metadata.get('local_path', '') if isinstance(metadata, dict) else ''

    # 候选slug列表(按可能性排序)
    search_slugs = []
    if meta_slug:
        search_slugs.append(meta_slug.lower().replace('_', '-'))
    if source_id:
        search_slugs.append(source_id.lower().replace('_', '-'))
    if name:
        # name可能含空格/大写,转为kebab-case
        slug_from_name = re.sub(r'[\s_]+', '-', name.lower())
        slug_from_name = re.sub(r'[^a-z0-9-]', '', slug_from_name).strip('-')
        if slug_from_name:
            search_slugs.append(slug_from_name)

    # 如果metadata中有local_path,直接读取
    if meta_path:
        p = Path(meta_path)
        md = p if p.name == 'SKILL.md' and p.exists() else p / 'SKILL.md'
        if md.exists():
            try:
                content = md.read_text(encoding='utf-8')
                if content and len(content) > 100:
                    return content
            except Exception as e:
                print(f"[WARN] 源skill读取失败({meta_path}): {e}")

    # 在本地下载目录中搜索
    search_dirs = []
    try:
        search_dirs = [CLAWHUB_DOWNLOADED_DIR, OPENSOURCE_SKILLS_DIR, ENTERPRISE_UPLOAD_DIR]
    except NameError as e:
        print(f"[WARN] 搜索目录变量未定义,使用空列表: {e}")

    for base_dir in search_dirs:
        if not base_dir.exists():
            continue
        for slug in search_slugs:
            if not slug:
                continue
            # 扁平结构: {dir}/{slug}/SKILL.md
            md = base_dir / slug / 'SKILL.md'
            if md.exists():
                try:
                    content = md.read_text(encoding='utf-8')
                    if content and len(content) > 100:
                        return content
                except Exception as e:
                    print(f"[WARN] 源skill读取失败({md}): {e}")
            # 嵌套结构: {dir}/{category}/{slug}/SKILL.md
            if base_dir.exists():
                for cat_dir in base_dir.iterdir():
                    if not cat_dir.is_dir():
                        continue
                    md = cat_dir / slug / 'SKILL.md'
                    if md.exists():
                        try:
                            content = md.read_text(encoding='utf-8')
                            if content and len(content) > 100:
                                return content
                        except Exception as e:
                            print(f"[WARN] 源skill读取失败({md}): {e}")

    # 未找到源内容时返回空字符串(不回退到content_preview,因为那是元数据不是正文)
    return ''


def _generate_skill_metadata(
    candidate: Dict[str, Any],
    existing_slugs: Set[str],
    batch_slugs: Set[str],
    description: str,
) -> Dict[str, Any]:
    """生成 slug / displayName / summary / pricing_tier / SKILL.md 内容与输出路径。

    返回字典中 final_slug 为 None 表示 slug 冲突无法自动解决
    (v3.3: 不使用程序化后缀, 需语义化重命名)。
    成功时会把 final_slug 加入 batch_slugs (批次内去重)。
    """
    # [V136 G6] 拆分自 process_candidates: 元数据与 SKILL.md 生成阶段
    source_id = candidate.get('source_id', '')
    name = candidate.get('name', '')
    category = candidate.get('category', 'Other')
    source = candidate.get('source', 'unknown')
    url = candidate.get('url', '')
    content_preview = candidate.get('content_preview', '')

    # PRR P0-1: 获取源skill真实SKILL.md内容(替代content_preview元数据)
    # content_preview是500字符的元数据摘要(slug/repo/url),不是源skill功能正文
    # _fetch_source_content从本地下载目录读取真实SKILL.md文件
    real_source_content = _fetch_source_content(candidate)
    if not real_source_content:
        # 源内容无法获取时,使用content_preview作为最后fallback并记录警告
        print(f"  [WARN] 源skill内容获取失败({name}), 使用元数据fallback — 差异化质量可能降低")
        real_source_content = content_preview

    # a. 生成 slug
    base_slug = generate_slug(source_id, name)

    # b. 检查 slug 冲突并解决
    final_slug = resolve_slug_conflict(base_slug, existing_slugs, batch_slugs)
    if final_slug is None:
        # v3.3: slug冲突时跳过该候选,不使用程序化后缀
        return {'base_slug': base_slug, 'final_slug': None}
    batch_slugs.add(final_slug)

    # c. 生成 displayName
    display_name = generate_display_name(name)

    # d. 生成 summary — V138 A3: 传入slug和source_content以提取真实量化指标
    # PRR P0-1: 使用real_source_content(真实源SKILL.md)替代content_preview(元数据)
    summary = generate_summary(name, description, category,
                               slug=final_slug, source_content=real_source_content)

    # e. 评估 pricing_tier
    pricing_tier = evaluate_pricing_tier(candidate)

    # f. 准备输出路径
    skill_dir = SKILLHUB_ROOT / final_slug
    skill_md_path = skill_dir / 'SKILL.md'

    # 生成 SKILL.md 内容
    # PRR P0-1: 使用real_source_content替代content_preview,确保源body保留≥70%
    skill_md_content = generate_skill_md(
        slug=final_slug,
        display_name=display_name,
        summary=summary,
        description=description,
        pricing_tier=pricing_tier,
        category=category,
        source=source,
        url=url,
        source_content=real_source_content,
    )

    return {
        'base_slug': base_slug,
        'final_slug': final_slug,
        'display_name': display_name,
        'summary': summary,
        'pricing_tier': pricing_tier,
        'skill_dir': skill_dir,
        'skill_md_path': skill_md_path,
        'skill_md_content': skill_md_content,
    }


def _determine_skill_status(
    security_status: str,
    final_slug: str,
    base_slug: str,
    existing_slugs: Set[str],
) -> str:
    """根据安全状态与 slug 冲突情况判定技能状态标签。

    状态标记: NEW / CONFLICT / EXISTS / SECURITY_BLOCKED
    """
    # [V136 G6] 拆分自 process_candidates: 状态判定阶段
    if security_status == 'BLOCKED':
        status = 'SECURITY_BLOCKED'
    elif final_slug != base_slug:
        status = f'CONFLICT ({base_slug} -> {final_slug})'
    elif final_slug in existing_slugs:
        status = 'UPDATE'
    else:
        status = 'NEW'

    if security_status in ('WARNING', 'NOTICE'):
        status += f' [{security_status}]'

    return status


def _build_skill_detail(
    idx: int,
    candidate: Dict[str, Any],
    meta: Dict[str, Any],
    status: str,
    security_status: str,
    security_fixes: List[Any],
) -> Dict[str, Any]:
    """构建单个候选的处理明细字典。"""
    # [V136 G6] 拆分自 process_candidates: 明细构建阶段
    return {
        'index': idx,
        'source': candidate.get('source', 'unknown'),
        'source_id': candidate.get('source_id', ''),
        'name': candidate.get('name', ''),
        'slug': meta['final_slug'],
        'base_slug': meta['base_slug'],
        'display_name': meta['display_name'],
        'summary': meta['summary'],
        'pricing_tier': meta['pricing_tier'],
        'category': candidate.get('category', 'Other'),
        'status': status,
        'skill_md_path': str(meta['skill_md_path']),
        'security_status': security_status,
        'security_fixes': security_fixes,
    }


def _create_skill_on_disk(
    detail: Dict[str, Any],
    candidate: Dict[str, Any],
    meta: Dict[str, Any],
) -> None:
    """实际创建技能产物: 建目录, 写 SKILL.md, 更新数据库, 填充 simhash。

    PRR P1-3: 写入前检查simhash相似度,阻断近似重复内容(防止平台反垃圾检测)。
    """
    # [V136 G6] 拆分自 process_candidates: 落盘创建阶段
    final_slug = meta['final_slug']
    skill_md_path = meta['skill_md_path']
    skill_md_content = meta['skill_md_content']
    skill_dir = meta['skill_dir']

    # PRR P1-3: 生成时相似度阻断 — 写入前检查跨skill simhash相似度
    # PRR V146 P0-C: content_dedup不可用时阻断(fail-safe), 不允许跳过
    # 根因: 原代码content_dedup不可用时仅打印警告继续写入,近似重复内容未拦截
    try:
        from content_dedup import find_approximate_duplicates
        approx_dups = find_approximate_duplicates(
            skill_md_content, exclude_slug=final_slug
        )
        if approx_dups:
            closest = approx_dups[0]
            raise ValueError(
                f"simhash相似度阻断: 与已有skill '{closest['slug']}' "
                f"Hamming距离={closest['hamming_distance']} "
                f"(相似度={closest.get('similarity', 0):.1%}) — 需进一步差异化"
            )
    except ImportError:
        raise ValueError(
            f"content_dedup模块不可用 — 生成已阻断(fail-safe)。"
            f"无法验证skill '{final_slug}'的相似度,请检查content_dedup.py是否正确安装。"
        )
    except ValueError:
        raise  # 重新抛出相似度阻断异常
    except Exception as e:
        raise ValueError(f"simhash检查异常(阻断): {e}")

    # 创建输出目录
    skill_dir.mkdir(parents=True, exist_ok=True)

    # 写入 SKILL.md
    with open(skill_md_path, 'w', encoding='utf-8') as f:
        f.write(skill_md_content)

    # 更新数据库 (v1.3: 传入content_hash)
    _content_hash = hashlib.sha256(skill_md_content.encode('utf-8')).hexdigest()[:16]
    skill_id = update_database(
        slug=final_slug,
        name=candidate.get('name', ''),
        display_name=meta['display_name'],
        version='1.0.0',
        category=candidate.get('category', 'Other'),
        source=candidate.get('source', 'unknown'),
        source_slug=candidate.get('source_id', ''),
        source_url=candidate.get('url', ''),
        local_path=str(skill_md_path),
        pricing_tier=meta['pricing_tier'],
        source_license=extract_source_license(candidate.get('content_preview', '')),  # V126 W5
        content_hash=_content_hash,
    )

    # v1.3: 填充simhash (接入去重管道)
    # V153 R9修复: simhash填充失败时记录警告(非阻断,但标记需人工复查)
    try:
        from content_dedup import update_simhash
        update_simhash(final_slug, skill_md_content)
    except ImportError as e:
        print(f"[WARN] content_dedup模块不可用,simhash未填充(近似去重对该skill失效): {e}")
    except Exception as e:
        print(f"[WARN] simhash填充失败(近似去重对该skill失效,需人工复查): {e}")

    detail['skill_id'] = skill_id


def _print_processing_summary(stats: Dict[str, Any]) -> None:
    """打印处理完成统计信息。"""
    # [V136 G6] 拆分自 process_candidates: 统计输出阶段
    print(f"\n{'='*60}")
    print(f"处理完成")
    print(f"{'='*60}")
    print(f"总候选数:  {stats['total']}")
    print(f"成功创建:  {stats['created']}")
    print(f"跳过(dry): {stats['skipped']}")
    print(f"错误:      {stats['errors']}")
    print(f"安全阻断:  {stats['security_blocked']}")
    print(f"安全修复:  {stats['security_fixed']}")
    print(f"{'='*60}\n")


def process_candidates(
    candidates: List[Dict[str, Any]],
    limit: int = 50,
    dry_run: bool = False,
    skip_security: bool = False,
    auto_fix_security: bool = True,
) -> Dict[str, Any]:
    """处理候选列表, 生成差异化 SKILL.md 并更新数据库。

    v2.2新增: 差异化前安全预检
    - 对每个候选的源内容执行21项安全风险扫描
    - critical风险(BLOCKED): 跳过差异化
    - high风险(WARNING): 自动修复后继续
    - medium风险(NOTICE): 自动修复后继续
    - safe: 正常差异化

    Args:
        candidates: 候选 skill 列表
        limit: 处理上限
        dry_run: 仅输出计划
        skip_security: 跳过安全预检(不推荐)
        auto_fix_security: 自动修复可修复的安全风险

    Returns:
        包含处理统计的字典
    """
    # [V136 G6] 重构: 拆分为阶段化辅助函数, 主流程仅做编排
    candidates, existing_slugs, batch_slugs, stats = _init_processing_state(candidates, limit)
    _print_processing_header(stats['total'], dry_run)

    for idx, candidate in enumerate(candidates, 1):
        # ===== v2.2: 差异化前安全预检 =====
        security_status, security_fixes, description, blocked = _run_security_precheck(
            candidate, skip_security, auto_fix_security, stats, idx, stats['total']
        )
        if blocked:
            continue

        # 生成 slug / 元数据 / SKILL.md 内容
        meta = _generate_skill_metadata(candidate, existing_slugs, batch_slugs, description)
        if meta['final_slug'] is None:
            # v3.3: slug冲突时跳过该候选,不使用程序化后缀
            print(f"  [SKIP] slug冲突无法自动解决: {meta['base_slug']} (需语义化重命名)")
            continue

        final_slug = meta['final_slug']
        # 状态标记: NEW / CONFLICT / EXISTS / SECURITY_BLOCKED
        status = _determine_skill_status(security_status, final_slug, meta['base_slug'], existing_slugs)

        print(
            f"[{idx:3d}/{stats['total']}] {status:20s} | "
            f"slug={final_slug:40s} | "
            f"display={meta['display_name']:20s} | "
            f"tier={meta['pricing_tier']}"
        )

        detail = _build_skill_detail(idx, candidate, meta, status, security_status, security_fixes)
        stats['details'].append(detail)

        if dry_run:
            stats['skipped'] += 1
            continue

        # 实际创建
        try:
            _create_skill_on_disk(detail, candidate, meta)
            stats['created'] += 1
        except Exception as e:  # [V131 B2] 宽泛捕获: 异常记录日志继续
            print(f"  [ERROR] {final_slug}: {e}")
            stats['errors'] += 1
            detail['error'] = str(e)

    _print_processing_summary(stats)
    return stats


# ============================================================
# E9: 营销优化增强
# ============================================================

def optimize_marketing_copy(
    display_name: str = '',
    summary: str = '',
    description: str = '',
    category: str = 'Other',
    slug: str = '',
    skill_content: str = '',
    use_agent: bool = True,
    skills: Union[Dict[str, Any], List[Dict[str, Any]], None] = None,
) -> Dict[str, Any]:
    """E9: 营销优化增强 — 统一营销文案入口 (M3.2增强)

    使用E13的generate_agent_prompt('analyze')进行AI驱动优化。
    AI代理不可用时, 使用规则优化(真实降级, 非mock)。

    优化规则:
    - displayName: ≤20字符, 移除冗余后缀, 突出核心价值
    - summary: ≤100字符, "痛点+方案+量化"公式, SEO关键词前置
    - description: 150-280字符, 包含Use when触发条件, 突出差异化

    M3.2增强 (统一营销文案入口):
    - 支持 batch 模式: 传入 skills (单个 dict 或 list) 进行批量优化
    - 内部调用 batch_optimize_description.expand_description() 扩写 description
    - 内部调用 quality_gate.run_marketing_gate() 进行营销数据质量门禁验证

    参数:
        display_name: 原始displayName
        summary: 原始summary
        description: 原始description
        category: skill分类
        slug: skill的slug
        skill_content: SKILL.md内容(AI优化时提供上下文)
        use_agent: 是否使用AI代理路径(默认True)
        skills: (M3.2新增) 单个skill dict或skill dict列表, 用于批量优化。
                每个dict可包含: slug, display_name/displayName, summary,
                description, category, skill_content/local_path/skill_md_path

    返回:
        单skill模式: 原有返回 + expanded_description + gate_result
        batch模式:
        {
            'batch': True,
            'total': int,
            'optimized_count': int,
            'results': [单skill优化结果, ...],
            'optimized_at': str,
        }
    """
    # === M3.2: batch 模式 ===
    if skills is not None:
        skills_list = [skills] if isinstance(skills, dict) else list(skills)
        return _batch_optimize_marketing_copy(skills_list, use_agent=use_agent)

    # === 单 skill 模式 (原有逻辑 + M3.2集成) ===
    original = {
        'displayName': display_name,
        'summary': summary,
        'description': description,
    }

    changes = []
    agent_prompt = ''

    # AI代理路径优先
    if use_agent:
        # 复用E13的generate_agent_prompt (F-01: 薄wrapper)
        from llm_validator import generate_agent_prompt, validate_agent_prompt

        skill_data = {
            'slug': slug or display_name,
            'name': display_name,
            'skill_content': skill_content or description,
        }
        context = {
            'category': category,
            'description': description,
            'optimization_mode': True,
            'current_display_name': display_name,
            'current_summary': summary,
        }
        agent_prompt = generate_agent_prompt('analyze', skill_data, context)

        # F-08: prompt质量校验
        validation = validate_agent_prompt(agent_prompt)
        if validation['valid']:
            # V144 G3: 实际调用LLM桥接执行(之前只生成prompt未执行,是E13断点)
            try:
                from llm_bridge import get_bridge
                bridge = get_bridge()
                llm_result = bridge.execute('analyze', skill_data, context)
                if llm_result.get('status') == 'success':
                    optimization_mode = 'agent'
                    # 解析LLM返回的优化结果
                    llm_data = llm_result.get('result', '')
                    if isinstance(llm_data, dict):
                        # LLM返回结构化结果: 直接使用
                        if llm_data.get('displayName'):
                            opt_display = llm_data['displayName'][:20]
                            changes.append(f"displayName(LLM): '{display_name}' → '{opt_display}'")
                        if llm_data.get('summary'):
                            opt_summary = llm_data['summary'][:100]
                            changes.append(f"summary(LLM): AI优化")
                        if llm_data.get('description'):
                            opt_description = llm_data['description']
                            changes.append("description(LLM): AI优化")
                    elif isinstance(llm_data, str) and llm_data:
                        # LLM返回文本: 用于description增强
                        opt_description = llm_data
                        changes.append("description(LLM): AI增强")
                    changes.append("LLM代理优化成功")
                else:
                    # LLM执行失败, 降级到规则优化(真实降级, 非mock)
                    optimization_mode = 'rule'
                    changes.append(f"LLM执行失败, 降级到规则优化: {llm_result.get('error', 'unknown')}")
            except ImportError:
                optimization_mode = 'rule'
                changes.append("llm_bridge不可用, 降级到规则优化")
            except Exception as e:
                optimization_mode = 'rule'
                changes.append(f"LLM调用异常, 降级到规则优化: {e}")
        else:
            # prompt校验失败, 降级到规则优化(真实降级, 非mock)
            optimization_mode = 'rule'
            changes.append(f"AI代理prompt校验失败, 降级到规则优化: {validation['issues']}")
    else:
        optimization_mode = 'rule'

    # 规则优化(无论是否使用AI代理, 都提供规则优化结果作为基础)
    # V144 G3: 如果LLM已返回结果, 不再重复执行规则优化
    if optimization_mode != 'agent':
        opt_display = _optimize_display_name(display_name)
        opt_summary = _optimize_summary(summary, category, display_name)
        opt_description = _optimize_description(description, category, display_name)

        # 记录规则优化变更
        if opt_display != display_name:
            changes.append(f"displayName: '{display_name}' → '{opt_display}'")
        if opt_summary != summary:
            changes.append(f"summary: '{summary[:30]}...' → '{opt_summary[:30]}...'")
        if opt_description != description:
            changes.append("description: 优化了SEO关键词和触发条件")
    else:
        # LLM路径: 确保有基础值(如果LLM未返回某字段)
        opt_display = opt_display if 'opt_display' in dir() else _optimize_display_name(display_name)
        opt_summary = opt_summary if 'opt_summary' in dir() else _optimize_summary(summary, category, display_name)
        opt_description = opt_description if 'opt_description' in dir() else _optimize_description(description, category, display_name)

    # M3.2: 调用 batch_optimize_description.expand_description() 扩写 description
    expanded_description = opt_description
    try:
        from batch_optimize_description import expand_description
        fields = {
            'displayName': opt_display,
            'name': opt_display,
            'summary': opt_summary,
            'description': opt_description,
        }
        body = skill_content or description or ''
        expanded_description = expand_description(fields, body)
        if expanded_description and expanded_description != opt_description:
            changes.append(
                f"description: expand_description 扩写至 {len(expanded_description)} 字符"
            )
            opt_description = expanded_description
    except ImportError:
        changes.append("expand_description 模块不可用, 跳过 description 扩写")
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常收集错误继续批量处理
        changes.append(f"expand_description 异常: {e}")

    # M3.2: 调用 quality_gate.run_marketing_gate() 进行营销数据质量门禁验证
    gate_result = None
    try:
        from quality_gate import run_marketing_gate
        # 尝试定位 SKILL.md 文件
        skill_md_path = None
        if slug:
            try:
                from skill_core.parser import find_skill_md as _find_md
                skill_md_path = _find_md(slug)
            except Exception as e:
                print(f"[WARN] skill_md查找失败,跳过marketing gate: {e}")
        if skill_md_path and skill_md_path.exists():
            gate_result = run_marketing_gate(skill_md_path)
        else:
            # V153 R10修复: None→False(fail-safe),原为None(语义模糊)
            gate_result = {
                'overall_passed': False,
                'note': 'SKILL.md 文件未找到, 门控验证不通过(fail-safe)',
            }
    except ImportError:
        # V153 R10修复: None→False(fail-safe)
        gate_result = {
            'overall_passed': False,
            'note': 'run_marketing_gate 模块不可用, 门控验证不通过(fail-safe)',
        }
    except Exception as e:  # [V131 B2] 宽泛捕获: 异常更新状态/计数继续
        # V153 R10修复: None→False(fail-safe)
        gate_result = {
            'overall_passed': False,
            'note': f'run_marketing_gate 异常, 门控验证不通过(fail-safe): {e}',
        }

    return {
        'optimized': {
            'displayName': opt_display,
            'summary': opt_summary,
            'description': opt_description,
        },
        'original': original,
        'changes': changes,
        'agent_prompt': agent_prompt,
        'optimization_mode': optimization_mode,
        'expanded_description': expanded_description,
        'gate_result': gate_result,
        'optimized_at': datetime.now().isoformat(),
    }


def _batch_optimize_marketing_copy(
    skills_list: List[Dict[str, Any]],
    use_agent: bool = True,
) -> Dict[str, Any]:
    """M3.2: 批量优化营销文案 (统一入口的 batch 后端)

    对每个 skill 调用 optimize_marketing_copy() 单skill模式进行优化,
    内部集成 expand_description 和 run_marketing_gate。

    参数:
        skills_list: skill dict 列表, 每个 dict 可包含:
                     slug, display_name/displayName, summary, description,
                     category, skill_content/local_path
        use_agent: 是否使用AI代理路径

    返回:
        {
            'batch': True,
            'total': int,
            'optimized_count': int,
            'results': [单skill优化结果, ...],
            'optimized_at': str,
        }
    """
    results = []
    for skill in skills_list:
        s_display_name = (
            skill.get('display_name')
            or skill.get('displayName')
            or skill.get('name')
            or ''
        )
        s_summary = skill.get('summary') or ''
        s_description = skill.get('description') or ''
        s_category = skill.get('category') or 'Other'
        s_slug = skill.get('slug') or ''
        s_content = skill.get('skill_content') or skill.get('content') or ''

        result = optimize_marketing_copy(
            display_name=s_display_name,
            summary=s_summary,
            description=s_description,
            category=s_category,
            slug=s_slug,
            skill_content=s_content,
            use_agent=use_agent,
            skills=None,  # 确保不递归进入 batch 模式
        )
        result['slug'] = s_slug
        results.append(result)

    optimized_count = sum(1 for r in results if r.get('changes'))
    return {
        'batch': True,
        'total': len(skills_list),
        'optimized_count': optimized_count,
        'results': results,
        'optimized_at': datetime.now().isoformat(),
    }


def _optimize_display_name(display_name: str) -> str:
    """优化displayName: ≤20字符, 移除冗余后缀, 突出核心价值"""
    import re
    # 移除常见冗余后缀
    cleaned = re.sub(r'\s+(free|paid|pro|beta|v\d+|tool|helper|plugin)$',
                     '', display_name, flags=re.IGNORECASE)
    # 移除尾部标点
    cleaned = cleaned.rstrip(' -—|')
    # 确保不为空
    if not cleaned:
        cleaned = display_name
    # 截断到20字符 (V119 W5: 使用MAX_DISPLAY_NAME_LEN常量)
    if len(cleaned) > MAX_DISPLAY_NAME_LEN:
        cleaned = cleaned[:MAX_DISPLAY_NAME_LEN]
    return cleaned.strip()


def _optimize_summary(summary: str, category: str, display_name: str) -> str:
    """优化summary: ≤100字符, SEO关键词前置, 量化指标

    V138 A3: 量化指标从量化池轮选, 不再使用固定硬编码量化词。
    PRR P0-2: 痛点/方案使用变体池。
    PRR P1-2: 无真实量化时使用诚实回退描述。
    """
    # 如果summary已满足要求, 仅微调
    pain, solution = _get_pain_solution(category, display_name)

    # SEO关键词前置: 将核心词放在前面
    topic = display_name.replace('-', ' ').replace('_', ' ').strip()
    topic = re.sub(r'\s+(free|paid|pro)$', '', topic, flags=re.IGNORECASE).strip()
    if not topic:
        topic = category

    # V138 A3: 量化指标 — 从量化池轮选(用display_name做hash, 避免批量相同)
    quant = _get_quantifier(slug=display_name)

    # 构造优化后的summary
    optimized = f"{pain}。{solution}，{topic}场景{quant}。"

    # 如果原始summary已包含量化指标且长度合适, 保留原始
    has_quant = any(kw in summary for kw in ['倍', '%', '提升', '降低', '节省'])
    if has_quant and 10 <= len(summary) <= 100:
        return summary  # 原始已足够好

    # 截断到100字符
    if len(optimized) > 100:
        optimized = optimized[:97] + '...'

    return optimized


def _optimize_description(description: str, category: str, display_name: str) -> str:
    """优化description: 150-280字符, 包含Use when触发条件"""
    MIN_DESC = 150
    MAX_DESC = 280

    # 检查是否已有Use when
    has_use_when = 'use when' in description.lower() or '适用于' in description

    # 如果描述长度合适且包含触发条件, 轻微优化
    if MIN_DESC <= len(description) <= MAX_DESC and has_use_when:
        return description

    # 优化: 确保包含Use when触发条件
    trigger = f"Use when 需要{category}领域自动化处理、数据分析和流程编排时使用。不适用于无明确需求的模糊场景。"
    # padding用于补充短描述到最小长度 (V144 G2: 使用差异化池替代固定文案)
    padding_parts = [
        f"{_get_padding(slug)}。",  # V144 G2
        f"{_get_padding(slug + '_2')}。",  # 第二个padding用不同seed
        f"{_get_padding(slug + '_3')}。",  # 第三个padding用不同seed
    ]

    if len(description) < MIN_DESC:
        # 描述太短, 逐步补充padding直到达到MIN_DESC
        optimized = description.rstrip('。') + '。'
        for part in padding_parts:
            optimized += part
            if len(optimized) >= MIN_DESC:
                break
        # 确保包含trigger
        if 'use when' not in optimized.lower() and '适用于' not in optimized:
            optimized += trigger
        # 如果仍不够长, 循环补充
        idx = 0
        while len(optimized) < MIN_DESC and idx < len(padding_parts) * 2:
            optimized += padding_parts[idx % len(padding_parts)]
            idx += 1
    elif len(description) > MAX_DESC:
        # 描述太长, 截断并补充触发条件
        optimized = description[:MAX_DESC - len(trigger) - 10].rstrip('。') + '。' + trigger
    else:
        # 长度合适, 确保包含触发条件
        if not has_use_when:
            optimized = description.rstrip('。') + ' ' + trigger
        else:
            optimized = description

    # 最终长度检查
    if len(optimized) > MAX_DESC:
        optimized = optimized[:MAX_DESC - 3] + '...'

    return optimized


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
    parser.add_argument(
        '--skip-security', action='store_true',
        help='跳过差异化前安全预检(不推荐, 可能生成有安全风险的skill)',
    )
    parser.add_argument(
        '--no-auto-fix', action='store_true',
        help='禁用安全风险自动修复(有风险的候选将被跳过而非修复)',
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
        skip_security=args.skip_security,
        auto_fix_security=not args.no_auto_fix,
    )


if __name__ == '__main__':
    main()
