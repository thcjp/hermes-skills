#!/usr/bin/env python3
"""
Skill Bundle 组合器 (v1.0 — E4实现)
==================================
分析skill关系，组合互补skill为Bundle，提升整体价值和用户体验。

核心功能:
  1. compose_bundle(): 从DB读取skill列表，分析互补性，组合为Bundle
  2. score_bundle(): 评估Bundle整体质量（E8的预实现）

互补性分析策略:
  - SimHash距离(E3): 距离越大内容差异越大，互补性越高
  - 分类多样性: 不同分类的skill覆盖更广的使用场景
  - 质量均衡: 成员质量应均衡，避免短板效应

注: E15的Skill关系图谱在Phase 5实现，当前用分类+SimHash距离替代。

Usage:
    python bundle_composer.py compose --category Development    # 按分类组合
    python bundle_composer.py compose --slugs slug1,slug2,slug3 # 指定skill
    python bundle_composer.py score --bundle bundle.json        # 评分已有Bundle
    python bundle_composer.py compose --auto                    # 自动发现最佳组合
"""

import json
import sys
from pathlib import Path
from typing import List, Dict
from datetime import datetime

# 导入统一配置
# V111 W2: chicken-and-egg修复(类似batch_optimize_description.py) — 先导入project_config
_config_dir = str(Path(__file__).resolve().parent.parent / "config")
if _config_dir not in sys.path:
    sys.path.insert(0, _config_dir)
from project_config import DB_PATH, TOOLS_DIR, A_GRADE_QUALITY_THRESHOLD, LOCAL_QUALITY_GRADE_C # V111 W2: 新增PROJECT_ROOT+TOOLS_DIR; V118 W3: 新增A_GRADE_QUALITY_THRESHOLD; V156: 新增LOCAL_QUALITY_GRADE_C用于B级降级筛选
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
from content_dedup import hamming_distance, simhash_similarity
from skill_core import db as db_module

# ============ 常量配置 ============

# Bundle大小限制
MIN_BUNDLE_SIZE = 2
MAX_BUNDLE_SIZE = 7
OPTIMAL_BUNDLE_SIZE = 4

# SimHash距离阈值（用于互补性判断）
COMPLEMENTARY_DISTANCE_MIN = 10    # 距离≥10视为互补（内容差异大）
REDUNDANT_DISTANCE_MAX = 3         # 距离≤3视为冗余（内容太相似）
SIMHASH_BITS = 64

# 评分权重
SCORE_WEIGHTS = {
    'quality': 0.35,          # 成员平均质量
    'complementarity': 0.30,  # 互补性
    'coverage': 0.25,         # 覆盖度
    'size_fit': 0.10,         # 大小适配
}

# 质量分阈值: V118 W3 从project_config导入(与plug_generator/orchestrator共享同一常量)
MIN_MEMBER_SCORE = A_GRADE_QUALITY_THRESHOLD


# ============ 数据读取 ============

def _load_skills_from_db(
    slugs: List[str] = None,
    category: str = None,
    db_path: str = None,
    limit: int = 50
) -> List[Dict]:
    """从DB读取skill列表

    TD-22修复: 当slugs指定时, 跳过simhash过滤条件, 允许查询任意指定skill。
    仅当使用category筛选(自动发现模式)时, 保留simhash过滤(用于互补性分析)。

    参数:
        slugs: 指定slug列表（None则不限）
        category: 指定分类（None则不限）
        db_path: 数据库路径
        limit: 最大返回数量

    返回:
        skill字典列表，每项包含:
        {
            'slug': str,
            'category': str,
            'local_quality_score': float,
            'simhash': int,
            'current_name': str,
            'summary': str,
            'local_path': str,
        }
    """
    if db_path is None:
        db_path = DB_PATH

    conn = db_module.get_db()
    c = conn.cursor()

    query = """
        SELECT slug, category, local_quality_score, simhash,
               current_name, current_display_name, summary, local_path
        FROM skills
        WHERE 1=1
    """
    params = []

    if slugs:
        # TD-22: 指定slugs时不过滤simhash, 允许查询任意skill
        placeholders = ','.join('?' * len(slugs))
        query += f" AND slug IN ({placeholders})"
        params.extend(slugs)
    elif category:
        # 自动发现模式: 保留simhash过滤(互补性分析需要)
        query += " AND simhash IS NOT NULL AND simhash != 0"
        query += " AND category = ?"
        params.append(category)
    else:
        # 无指定时: 保留simhash过滤(自动发现场景)
        query += " AND simhash IS NOT NULL AND simhash != 0"

    query += " ORDER BY local_quality_score DESC LIMIT ?"
    params.append(limit)

    c.execute(query, params)
    rows = c.fetchall()
    conn.close()

    skills = []
    for row in rows:
        skills.append({
            'slug': row['slug'],
            'category': row['category'] or 'Other',
            'quality_score': row['local_quality_score'] or 0.0,
            'simhash': row['simhash'] or 0,
            'name': row['current_name'] or row['current_display_name'] or row['slug'],
            'summary': row['summary'] or '',
            'local_path': row['local_path'] or '',
        })

    return skills


def _load_skill_content(local_path: str) -> str:
    """读取skill的SKILL.md内容

    参数:
        local_path: skill本地路径

    返回:
        SKILL.md内容字符串，读取失败返回空字符串
    """
    skill_path = Path(local_path)
    if skill_path.is_file() and skill_path.name == 'SKILL.md':
        return skill_path.read_text(encoding='utf-8')
    elif skill_path.is_dir():
        skill_md = skill_path / "SKILL.md"
        if skill_md.exists():
            return skill_md.read_text(encoding='utf-8')
    return ''


# ============ 互补性分析 ============

def _compute_pairwise_complementarity(skills: List[Dict]) -> Dict[str, Dict]:
    """计算skill两两之间的互补性

    使用SimHash距离衡量内容差异：
    - 距离越大 → 内容差异越大 → 互补性越高
    - 距离越小 → 内容越相似 → 冗余性越高

    参数:
        skills: skill列表

    返回:
        {
            'slug1_slug2': {
                'simhash_distance': int,
                'similarity': float,
                'complementary': bool,
                'redundant': bool,
            }
        }
    """
    pairs = {}
    for i, s1 in enumerate(skills):
        for j, s2 in enumerate(skills):
            if i >= j:
                continue
            if s1['simhash'] == 0 or s2['simhash'] == 0:
                continue

            dist = hamming_distance(s1['simhash'], s2['simhash'])
            sim = simhash_similarity(s1['simhash'], s2['simhash'])
            key = f"{s1['slug']}_{s2['slug']}"

            pairs[key] = {
                'simhash_distance': dist,
                'similarity': round(sim, 4),
                'complementary': dist >= COMPLEMENTARY_DISTANCE_MIN,
                'redundant': dist <= REDUNDANT_DISTANCE_MAX,
            }

    return pairs


def _analyze_category_diversity(skills: List[Dict]) -> Dict:
    """分析skill分类多样性

    参数:
        skills: skill列表

    返回:
        {
            'categories': set of categories,
            'unique_categories': int,
            'category_distribution': {category: count},
        }
    """
    categories = [s['category'] for s in skills]
    unique_cats = set(categories)
    distribution = {}
    for cat in categories:
        distribution[cat] = distribution.get(cat, 0) + 1

    return {
        'categories': list(unique_cats),
        'unique_categories': len(unique_cats),
        'category_distribution': distribution,
    }


def _determine_skill_role(skill: Dict, all_skills: List[Dict], pairs: Dict) -> str:
    """确定skill在Bundle中的角色

    角色类型:
    - primary: 质量最高的核心skill
    - complementary: 与核心skill互补的skill
    - supporting: 填补覆盖空白的skill

    参数:
        skill: 当前skill
        all_skills: Bundle中所有skill
        pairs: 互补性分析结果

    返回:
        角色字符串
    """
    # 质量最高的skill为primary
    max_score = max(s['quality_score'] for s in all_skills)
    if skill['quality_score'] >= max_score - 0.1:
        return 'primary'

    # 检查与其他skill的互补性
    complementary_count = 0
    redundant_count = 0
    for other in all_skills:
        if other['slug'] == skill['slug']:
            continue
        key = f"{skill['slug']}_{other['slug']}" if f"{skill['slug']}_{other['slug']}" in pairs \
            else f"{other['slug']}_{skill['slug']}"
        pair_info = pairs.get(key, {})
        if pair_info.get('complementary'):
            complementary_count += 1
        if pair_info.get('redundant'):
            redundant_count += 1

    if redundant_count > complementary_count:
        return 'redundant'
    elif complementary_count >= len(all_skills) // 2:
        return 'complementary'
    else:
        return 'supporting'


# ============ Bundle组合 ============

def compose_bundle(
    skill_slugs: List[str] = None,
    category: str = None,
    max_bundle_size: int = MAX_BUNDLE_SIZE,
    min_bundle_size: int = MIN_BUNDLE_SIZE,
    min_quality: float = MIN_MEMBER_SCORE,
    db_path: str = None
) -> Dict:
    """组合互补skill为Bundle (E4核心函数)

    从DB读取skill列表，分析互补性，组合为高质量Bundle。
    互补性判断基于SimHash距离(E3)和分类多样性。

    数据流依赖:
        本函数的输出可供 score_bundle()(E8) 和 integrate_bundle_scoring()(E8) 使用,
        作为它们评估Bundle整体质量的输入参数。E4→E8为数据流依赖关系。

    参数:
        skill_slugs: 指定skill slug列表（None则从DB按分类读取）
        category: 指定分类（None则不限分类，当skill_slugs为None时生效）
        max_bundle_size: Bundle最大成员数
        min_bundle_size: Bundle最小成员数
        min_quality: 成员最低质量分
        db_path: 数据库路径

    返回:
        {
            'bundle_name': str,           # Bundle名称
            'bundle_slug': str,           # Bundle的slug
            'members': [                   # 成员列表
                {
                    'slug': str,
                    'name': str,
                    'category': str,
                    'quality_score': float,
                    'role': str,          # primary/complementary/supporting
                }
            ],
            'complementarity_score': float,
            'coverage_score': float,
            'quality_score': float,
            'overall_score': float,
            'combination_reason': str,    # 组合理由
            'pairwise_analysis': dict,     # 两两分析详情
            'category_diversity': dict,    # 分类多样性
            'created_at': str,            # 创建时间
        }
    """
    # 1. 加载skill列表
    if skill_slugs:
        skills = _load_skills_from_db(slugs=skill_slugs, db_path=db_path)
    else:
        skills = _load_skills_from_db(category=category, db_path=db_path, limit=30)

    if len(skills) < min_bundle_size:
        return {
            'bundle_name': '',
            'bundle_slug': '',
            'members': [],
            'overall_score': 0.0,
            'combination_reason': f'可用skill不足: {len(skills)} < {min_bundle_size}',
            'error': 'insufficient_skills',
        }

    # 2. 过滤低质量skill
    qualified = [s for s in skills if s['quality_score'] >= min_quality]
    if len(qualified) < min_bundle_size:
        # A级skill不足时,降级筛选B级及以上(quality_score >= LOCAL_QUALITY_GRADE_C)
        qualified = [s for s in skills if s['quality_score'] >= LOCAL_QUALITY_GRADE_C]
        if len(qualified) < min_bundle_size:
            # B级及以上仍不足,不生成低质量Bundle(fail-safe)
            print(f"[bundle_composer] B级及以上skill不足: {len(qualified)} < {min_bundle_size}, 不生成Bundle(fail-safe)")
            return {
                'bundle_name': '',
                'bundle_slug': '',
                'members': [],
                'overall_score': 0.0,
                'combination_reason': f'B级及以上skill不足: {len(qualified)} < {min_bundle_size}',
                'error': 'insufficient_qualified_skills',
            }

    # 3. 限制Bundle大小
    if len(qualified) > max_bundle_size:
        # 按质量分排序，取前max_bundle_size个
        qualified.sort(key=lambda s: s['quality_score'], reverse=True)
        qualified = qualified[:max_bundle_size]

    # 4. 计算两两互补性
    pairs = _compute_pairwise_complementarity(qualified)

    # 5. 分析分类多样性
    cat_diversity = _analyze_category_diversity(qualified)

    # 6. 确定每个skill的角色
    for skill in qualified:
        skill['role'] = _determine_skill_role(skill, qualified, pairs)

    # 7. 评分
    score_result = score_bundle({
        'members': qualified,
        'pairwise_analysis': pairs,
        'category_diversity': cat_diversity,
    })

    # 8. 生成Bundle名称和slug
    primary = next((s for s in qualified if s['role'] == 'primary'), qualified[0])
    categories_in_bundle = list(cat_diversity['categories'])
    if len(categories_in_bundle) == 1:
        bundle_name = f"{categories_in_bundle[0]} Bundle: {primary['name']}"
    else:
        bundle_name = f"Cross-Domain Bundle: {primary['name']}"

    bundle_slug = f"bundle-{primary['slug']}"[:50]

    # 9. 生成组合理由
    complementary_count = sum(1 for s in qualified if s['role'] == 'complementary')
    redundant_count = sum(1 for s in qualified if s['role'] == 'redundant')
    reason_parts = [
        f"{len(qualified)}个skill组合",
        f"覆盖{cat_diversity['unique_categories']}个分类",
        f"{complementary_count}个互补",
    ]
    if redundant_count > 0:
        reason_parts.append(f"{redundant_count}个冗余(建议剔除)")
    reason_parts.append(f"整体评分{score_result['overall_score']:.1f}/100")

    return {
        'bundle_name': bundle_name,
        'bundle_slug': bundle_slug,
        'members': [
            {
                'slug': s['slug'],
                'name': s['name'],
                'category': s['category'],
                'quality_score': s['quality_score'],
                'role': s['role'],
            }
            for s in qualified
        ],
        'complementarity_score': score_result['complementarity_score'],
        'coverage_score': score_result['coverage_score'],
        'quality_score': score_result['quality_score'],
        'overall_score': score_result['overall_score'],
        'combination_reason': ' | '.join(reason_parts),
        'pairwise_analysis': pairs,
        'category_diversity': cat_diversity,
        'created_at': datetime.now().isoformat(),
    }


# ============ Bundle评分 (E8预实现) ============

def score_bundle(bundle: Dict) -> Dict:
    """评估Bundle整体质量 (E8预实现)

    评分维度:
    1. 质量分(35%): 成员skill的平均质量分
    2. 互补性分(30%): 基于SimHash距离的成员间内容差异
    3. 覆盖度分(25%): 分类多样性和话题覆盖
    4. 大小适配分(10%): Bundle大小是否合理

    数据流依赖(E4→E8):
        本函数接收 compose_bundle()(E4) 的输出作为输入参数,
        评估E4组合的Bundle的整体质量。E4→E8为数据流依赖关系(非代码级调用)。

    参数:
        bundle: compose_bundle()返回的dict，或包含members的dict

    返回:
        {
            'overall_score': float,         # 0-100综合评分
            'quality_score': float,         # 0-100质量分
            'complementarity_score': float, # 0-100互补性分
            'coverage_score': float,       # 0-100覆盖度分
            'size_fit_score': float,       # 0-100大小适配分
            'reason': str,                 # 评分理由
        }
    """
    members = bundle.get('members', [])
    if not members:
        return {
            'overall_score': 0.0,
            'quality_score': 0.0,
            'complementarity_score': 0.0,
            'coverage_score': 0.0,
            'size_fit_score': 0.0,
            'reason': 'Bundle为空',
        }

    pairs = bundle.get('pairwise_analysis', {})
    cat_diversity = bundle.get('category_diversity', {})

    # === 1. 质量分 (35%) ===
    # 成员平均质量分（0-5 → 0-100）
    avg_quality = sum(m.get('quality_score', 0) for m in members) / len(members)
    quality_score = min(avg_quality / 5.0 * 100, 100)

    # 质量均衡度：标准差越小越好
    if len(members) > 1:
        variance = sum((m.get('quality_score', 0) - avg_quality) ** 2 for m in members) / len(members)
        std_dev = variance ** 0.5
        balance_factor = max(0, 1 - std_dev / 2.0)  # std_dev=0时1.0，std_dev=2时0.0
    else:
        balance_factor = 0.5

    quality_final = quality_score * (0.7 + 0.3 * balance_factor)

    # === 2. 互补性分 (30%) ===
    # 基于SimHash距离的平均值
    if pairs:
        distances = [p['simhash_distance'] for p in pairs.values()]
        avg_distance = sum(distances) / len(distances)
        # 距离越大互补性越高：距离0→0分，距离32+→100分
        complementarity_raw = min(avg_distance / (SIMHASH_BITS // 2) * 100, 100)

        # 冗余惩罚：有冗余对则扣分
        redundant_count = sum(1 for p in pairs.values() if p.get('redundant'))
        redundant_penalty = redundant_count * 15
        complementarity_final = max(0, complementarity_raw - redundant_penalty)
    else:
        complementarity_final = 50.0  # 无配对信息时给中等分

    # === 3. 覆盖度分 (25%) ===
    unique_cats = cat_diversity.get('unique_categories', 1)
    # 分类数越多覆盖越好：1分类→40分，2分类→70分，3+分类→100分
    if unique_cats == 1:
        coverage_score = 40.0
    elif unique_cats == 2:
        coverage_score = 70.0
    else:
        coverage_score = min(100.0, 70.0 + (unique_cats - 2) * 15)

    # === 4. 大小适配分 (10%) ===
    bundle_size = len(members)
    if bundle_size == OPTIMAL_BUNDLE_SIZE:
        size_fit_score = 100.0
    elif MIN_BUNDLE_SIZE <= bundle_size <= MAX_BUNDLE_SIZE:
        # 偏离最优大小的惩罚
        deviation = abs(bundle_size - OPTIMAL_BUNDLE_SIZE)
        size_fit_score = max(60.0, 100.0 - deviation * 15)
    else:
        size_fit_score = 30.0

    # === 综合评分 ===
    overall = (
        quality_final * SCORE_WEIGHTS['quality'] +
        complementarity_final * SCORE_WEIGHTS['complementarity'] +
        coverage_score * SCORE_WEIGHTS['coverage'] +
        size_fit_score * SCORE_WEIGHTS['size_fit']
    )

    # 生成评分理由
    reason_parts = [
        f"质量{quality_final:.0f}({'均衡' if balance_factor > 0.7 else '不均衡'})",
        f"互补{complementarity_final:.0f}",
        f"覆盖{coverage_score:.0f}({unique_cats}分类)",
        f"大小{size_fit_score:.0f}({bundle_size}个)",
    ]

    return {
        'overall_score': round(overall, 1),
        'quality_score': round(quality_final, 1),
        'complementarity_score': round(complementarity_final, 1),
        'coverage_score': round(coverage_score, 1),
        'size_fit_score': round(size_fit_score, 1),
        'reason': ' | '.join(reason_parts),
    }


# ============ 自动发现最佳组合 ============

def find_best_bundle(
    category: str = None,
    candidate_limit: int = 20,
    db_path: str = None
) -> Dict:
    """自动发现最佳Bundle组合

    从候选skill中尝试不同组合，找到评分最高的Bundle。

    参数:
        category: 限定分类（None则不限）
        candidate_limit: 候选skill数量上限
        db_path: 数据库路径

    返回:
        最佳Bundle的compose_bundle()结果
    """
    # 加载候选skill
    skills = _load_skills_from_db(category=category, db_path=db_path, limit=candidate_limit)

    if len(skills) < MIN_BUNDLE_SIZE:
        return compose_bundle(skill_slugs=[s['slug'] for s in skills], db_path=db_path)

    # 策略：取质量最高的skill作为primary，然后贪心添加互补性最高的skill
    skills.sort(key=lambda s: s['quality_score'], reverse=True)

    # 以质量最高的skill为起点
    primary = skills[0]
    selected = [primary]
    remaining = skills[1:]

    # 贪心添加：每次选择与已选skill互补性最高的skill
    while len(selected) < OPTIMAL_BUNDLE_SIZE and remaining:
        best_candidate = None
        best_score = -1

        for candidate in remaining:
            # 计算candidate与已选skill的平均SimHash距离
            distances = []
            for s in selected:
                if candidate['simhash'] and s['simhash']:
                    dist = hamming_distance(candidate['simhash'], s['simhash'])
                    distances.append(dist)

            if distances:
                avg_dist = sum(distances) / len(distances)
                # 互补性得分：距离越远越好，但不能太远（相关领域）
                complement_score = avg_dist
                # 质量加分
                total_score = complement_score + candidate['quality_score']

                if total_score > best_score:
                    best_score = total_score
                    best_candidate = candidate

        if best_candidate:
            selected.append(best_candidate)
            remaining.remove(best_candidate)
        else:
            break

    # 用选定的skill组合Bundle
    return compose_bundle(
        skill_slugs=[s['slug'] for s in selected],
        db_path=db_path
    )


# ============ E8: Bundle评分集成到上传管道 ============

# Bundle上传门控阈值（总分<60则阻止上传）
BUNDLE_UPLOAD_THRESHOLD = 60


def integrate_bundle_scoring(
    bundle: Dict,
    check_members: bool = True,
    db_path: str = None,
) -> Dict:
    """E8: 将Bundle评分集成到上传管道

    对Bundle执行双重验证:
    1. 成员门控: 调用upload_gate的run_gate_check_with_dedup验证每个成员skill
    2. Bundle评分: 调用score_bundle()评估Bundle整体质量

    Bundle整体评分<BUNDLE_UPLOAD_THRESHOLD则阻止上传。

    数据流依赖(E4→E8):
        本函数接收 compose_bundle()(E4) 的输出作为输入参数,
        对E4组合的Bundle执行上传门控和整体评分。E4→E8为数据流依赖关系(非代码级调用)。

    参数:
        bundle: compose_bundle()返回的dict, 或包含'members'的dict
        check_members: 是否执行成员门控检查(默认True)
        db_path: 数据库路径(传递给成员检查)

    返回:
        {
            'bundle_slug': str,           # Bundle标识
            'passed': bool,               # 是否通过上传门控
            'bundle_score': float,        # Bundle整体评分(0-100)
            'score_detail': dict,         # 评分详情(来自score_bundle)
            'member_gates': list,         # 各成员门控结果
            'blocked_reasons': list,      # 阻止原因列表
            'summary': str,               # 摘要文本
            'checked_at': str,            # 检查时间(ISO)
        }
    """
    members = bundle.get('members', [])
    bundle_slug = bundle.get('bundle_slug', bundle.get('bundle_name', 'unknown'))
    blocked_reasons = []

    # 1. 成员门控检查
    member_gates = []
    if check_members and members:
        # 延迟导入upload_gate, 避免循环依赖
        try:
            from upload_gate import run_gate_check_with_dedup
            _gate_available = True
        except ImportError:
            _gate_available = False

        # V153 R5修复: upload_gate不可用时阻断(fail-safe),原为跳过检查(fail-open)
        # V155 R5修复: 移除不可达的else分支(原dead code,与fail-safe逻辑矛盾)
        if not _gate_available:
            blocked_reasons.append(
                "upload_gate模块不可用 — 成员门控检查阻断(fail-safe)"
            )
        else:
            for member in members:
                slug = member.get('slug', '') if isinstance(member, dict) else str(member)
                local_path = member.get('local_path', '') if isinstance(member, dict) else ''

                # 优先使用local_path, 否则尝试从DB查找
                check_path = local_path
                if not check_path:
                    check_path = _find_skill_dir_by_slug(slug, db_path)

                if check_path:
                    gate_result = run_gate_check_with_dedup(check_path)
                    member_gates.append({
                        'slug': slug,
                        'passed': gate_result.get('passed', False),
                        'issues': gate_result.get('issues', []),
                        'summary': gate_result.get('summary', ''),
                    })
                    if not gate_result.get('passed', False):
                        blocked_reasons.append(
                            f"成员'{slug}'未通过上传门控: {gate_result.get('summary', '未知原因')}"
                        )
                else:
                    member_gates.append({
                        'slug': slug,
                        'passed': False,
                        'issues': [],
                        'summary': f'未找到skill目录: {slug}',
                    })
                    blocked_reasons.append(f"成员'{slug}'目录未找到")
    else:
        # 无成员或check_members=False
        member_gates = []

    # 2. Bundle评分(复用E4的score_bundle)
    score_detail = score_bundle(bundle)
    bundle_score = score_detail.get('overall_score', 0.0)

    # 3. Bundle门控: 评分<阈值则阻止
    if bundle_score < BUNDLE_UPLOAD_THRESHOLD:
        blocked_reasons.append(
            f"Bundle整体评分{bundle_score:.1f}低于阈值{BUNDLE_UPLOAD_THRESHOLD}"
        )

    # 4. 成员门控失败也阻止
    failed_members = [g for g in member_gates if g.get('passed') is False]
    if failed_members:
        blocked_reasons.append(
            f"{len(failed_members)}个成员未通过门控检查"
        )

    # 5. 综合判定
    passed = len(blocked_reasons) == 0

    # 6. 生成摘要
    passed_count = sum(1 for g in member_gates if g.get('passed') is True)
    total_count = len(member_gates)
    summary_parts = [
        f"Bundle评分: {bundle_score:.1f}/100",
        f"成员门控: {passed_count}/{total_count}通过",
    ]
    if passed:
        summary_parts.append("状态: 通过")
    else:
        summary_parts.append(f"状态: 阻止({len(blocked_reasons)}个原因)")

    return {
        'bundle_slug': bundle_slug,
        'passed': passed,
        'bundle_score': bundle_score,
        'score_detail': score_detail,
        'member_gates': member_gates,
        'blocked_reasons': blocked_reasons,
        'summary': ' | '.join(summary_parts),
        'checked_at': datetime.now().isoformat(),
    }


def _find_skill_dir_by_slug(slug: str, db_path: str = None) -> str:
    """从DB查找skill的本地目录路径

    参数:
        slug: skill的slug
        db_path: 数据库路径

    返回:
        skill目录路径字符串, 未找到返回空字符串
    """
    if db_path is None:
        db_path = DB_PATH

    try:
        conn = db_module.get_db()
        c = conn.cursor()
        c.execute("SELECT local_path FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        conn.close()
        if row and row['local_path']:
            return row['local_path']
    except Exception as e:
        print(f"[WARN] DB查询失败,返回空路径: {e}")
    return ''


# ============ CLI ============

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == 'compose':
        # 解析参数
        category = None
        slugs = None
        max_size = MAX_BUNDLE_SIZE

        for i, arg in enumerate(sys.argv[2:], 2):
            if arg == '--category' and i + 1 < len(sys.argv):
                category = sys.argv[i + 1]
            elif arg == '--slugs' and i + 1 < len(sys.argv):
                slugs = sys.argv[i + 1].split(',')
            elif arg == '--max-size' and i + 1 < len(sys.argv):
                max_size = int(sys.argv[i + 1])

        if slugs:
            result = compose_bundle(skill_slugs=slugs, max_bundle_size=max_size)
        else:
            result = compose_bundle(category=category, max_bundle_size=max_size)

        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif cmd == 'score':
        # 评分已有Bundle
        if len(sys.argv) < 3:
            print("用法: python bundle_composer.py score --bundle <bundle.json>")
            return

        bundle_file = sys.argv[2]
        if not Path(bundle_file).exists():
            print(f"文件不存在: {bundle_file}")
            return

        with open(bundle_file, 'r', encoding='utf-8') as f:
            bundle = json.load(f)

        result = score_bundle(bundle)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif cmd == 'auto':
        # 自动发现最佳组合
        category = None
        for i, arg in enumerate(sys.argv[2:], 2):
            if arg == '--category' and i + 1 < len(sys.argv):
                category = sys.argv[i + 1]

        result = find_best_bundle(category=category)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    else:
        print(__doc__)


if __name__ == '__main__':
    main()
