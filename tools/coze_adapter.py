#!/usr/bin/env python3
"""
Coze平台适配器 (V95 V6)
========================
Coze(扣子)平台适配器, 提供:
1. 资格检查 — 6类标准评估skill是否符合Coze上架要求
2. 格式转换 — SKILL.md → Coze plugin.json
3. 上传接口 — 抽象上传(需官方邀请,当前返回pending)
4. 收入分成 — 70%创作者分成计算

复用已有逻辑:
- platform_ops.cmd_coze_actions() 的SkillHub状态检查
- skill_core.parser.parse_frontmatter() 的frontmatter解析
- project_config 的统一配置

依赖说明:
- 无外部依赖(标准库 + 项目内部模块)
- 不需要LLM/API Key
- upload_skill当前返回pending(Coze需官方邀请开通)
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# === 统一配置导入 ===
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, MAX_PRICE, L4_PASS_THRESHOLD  # V153 R6: 导入MAX_PRICE和L4_PASS_THRESHOLD替代硬编码

# === 复用skill_core解析层 ===
# V110 W6: Path(__file__).resolve().parent → TOOLS_DIR (统一从project_config导入)
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
from skill_core.parser import parse_frontmatter


# Coze 6类评估标准
COZE_CRITERIA = {
    "case_completeness": {
        "name": "案例完整性",
        "description": "SKILL.md包含使用案例/示例",
        "weight": 20,
    },
    "name_compliance": {
        "name": "名称规范",
        "description": "slug和displayName符合命名规范",
        "weight": 15,
    },
    "description_accuracy": {
        "name": "描述准确",
        "description": "summary准确描述功能,无夸大",
        "weight": 20,
    },
    "security_compliance": {
        "name": "安全合规",
        "description": "无硬编码密钥/无危险代码",
        "weight": 20,
    },
    "pricing_reasonable": {
        "name": "定价合理",
        "description": "定价符合市场区间(0-199.9)",
        "weight": 10,
    },
    "quality_passed": {
        "name": "质量达标",
        "description": "通过quality_gate检查",
        "weight": 15,
    },
}

# Coze收入分成比例
COZE_CREATOR_SHARE = 0.70  # 创作者70%分成


class CozeAdapter:
    """Coze平台适配器

    提供skill到Coze平台的适配能力:
    - 资格检查(复用platform_ops已有逻辑 + 6类标准)
    - 格式转换(SKILL.md → plugin.json)
    - 上传(抽象接口,需官方邀请)
    - 收入预估(70%分成)
    """

    def __init__(self):
        self.platform_name = "coze"
        self.creator_share = COZE_CREATOR_SHARE

    def check_eligibility(self, skill_data: dict) -> dict:
        """检查skill是否符合Coze上架要求

        6类标准评估(复用platform_ops已有SkillHub状态检查 + 扩展):
        1. 案例完整性 — SKILL.md包含使用案例
        2. 名称规范 — slug和displayName符合命名规范
        3. 描述准确 — summary准确描述功能
        4. 安全合规 — 无硬编码密钥
        5. 定价合理 — 定价符合市场区间
        6. 质量达标 — 通过quality_gate

        Args:
            skill_data: skill数据字典, 包含slug, skillhub状态, is_free等
                        或从upload_tracking.json读取的skill记录

        Returns:
            dict: {
                'eligible': bool,
                'category': 'paid_eligible' | 'free_eligible' | 'not_eligible',
                'criteria': {criterion_id: {'passed': bool, 'score': int, 'reason': str}},
                'total_score': int,
                'estimated_revenue': float or None,
            }
        """
        criteria_results = {}
        total_score = 0

        # 1. 案例完整性 — 检查是否有使用案例/示例
        has_case = bool(skill_data.get('description') or skill_data.get('use_case'))
        criteria_results['case_completeness'] = {
            'passed': has_case,
            'score': COZE_CRITERIA['case_completeness']['weight'] if has_case else 0,
            'reason': '有描述/案例' if has_case else '缺少使用案例',
        }

        # 2. 名称规范 — slug和displayName存在且符合规范
        slug = skill_data.get('slug', '')
        display_name = skill_data.get('displayName', skill_data.get('display_name', ''))
        name_ok = bool(slug) and len(slug) >= 3 and bool(display_name)
        criteria_results['name_compliance'] = {
            'passed': name_ok,
            'score': COZE_CRITERIA['name_compliance']['weight'] if name_ok else 0,
            'reason': f'slug={slug}, name={display_name}' if name_ok else 'slug或name缺失',
        }

        # 3. 描述准确 — summary存在且非空
        summary = skill_data.get('summary', '')
        desc_ok = bool(summary) and len(summary) >= 10
        criteria_results['description_accuracy'] = {
            'passed': desc_ok,
            'score': COZE_CRITERIA['description_accuracy']['weight'] if desc_ok else 0,
            'reason': f'summary长度={len(summary)}' if summary else 'summary缺失',
        }

        # 4. 安全合规 — 复用platform_ops的SkillHub状态检查
        sh = skill_data.get('skillhub', {})
        rs = sh.get('review_status', '')
        security_ok = rs in ('published', 'approved', 'public_published')
        criteria_results['security_compliance'] = {
            'passed': security_ok,
            'score': COZE_CRITERIA['security_compliance']['weight'] if security_ok else 0,
            'reason': f'SkillHub状态={rs}' if rs else '未在SkillHub发布',
        }

        # 5. 定价合理 — 检查定价区间
        price = skill_data.get('price_amount', 0)
        if skill_data.get('is_free'):
            pricing_ok = True
            reason = '免费skill'
        else:
            pricing_ok = 0 < price <= MAX_PRICE  # V153 R6: 使用MAX_PRICE替代硬编码199.9
            reason = f'定价={price}' if pricing_ok else f'定价异常={price}'
        criteria_results['pricing_reasonable'] = {
            'passed': pricing_ok,
            'score': COZE_CRITERIA['pricing_reasonable']['weight'] if pricing_ok else 0,
            'reason': reason,
        }

        # 6. 质量达标 — 检查是否有质量评分
        quality_score = skill_data.get('quality_score', 0)
        # V153 R7修复: 无评分时默认不通过(fail-safe),原为默认通过(fail-open)
        quality_ok = quality_score >= L4_PASS_THRESHOLD if quality_score else False  # V153 R6: 使用L4_PASS_THRESHOLD替代硬编码60
        criteria_results['quality_passed'] = {
            'passed': quality_ok,
            'score': COZE_CRITERIA['quality_passed']['weight'] if quality_ok else 0,
            'reason': f'质量评分={quality_score}' if quality_score else '无评分,默认不通过(fail-safe)',
        }

        # 汇总
        total_score = sum(c['score'] for c in criteria_results.values())
        all_passed = all(c['passed'] for c in criteria_results.values())

        # 分类
        if all_passed and security_ok:
            if skill_data.get('is_free'):
                category = 'free_eligible'
            else:
                category = 'paid_eligible'
        else:
            category = 'not_eligible'

        # 收入预估(仅对付费skill)
        estimated_revenue = None
        if category == 'paid_eligible' and not skill_data.get('is_free'):
            estimated_revenue = round(price * self.creator_share, 2)

        return {
            'eligible': all_passed,
            'category': category,
            'criteria': criteria_results,
            'total_score': total_score,
            'estimated_revenue': estimated_revenue,
        }

    def convert_format(self, skill_md_content: str) -> dict:
        """SKILL.md → Coze plugin格式

        Coze plugin.json结构:
        {
            "name": slug,
            "display_name": displayName,
            "description": summary,
            "tools": [...],
            "version": "1.0.0",
            "license": "MIT",
            "homepage": "",
            "config": {
                "price_model": "per_call",
                "price_amount": 0
            }
        }

        Args:
            skill_md_content: SKILL.md文件内容字符串

        Returns:
            dict: Coze plugin.json结构
        """
        parsed = parse_frontmatter(skill_md_content)
        fields = parsed.get('fields', {})

        # 解析tools字段(可能是字符串或列表)
        tools_raw = fields.get('tools', '')
        if isinstance(tools_raw, str):
            try:
                tools = json.loads(tools_raw)
            except (json.JSONDecodeError, ValueError):
                tools = [t.strip() for t in tools_raw.split(',') if t.strip()]
        elif isinstance(tools_raw, list):
            tools = tools_raw
        else:
            tools = []

        # price字段转换异常保护: 非数字字符串会导致崩溃
        try:
            price_amount = float(fields.get('price', 0))
        except (ValueError, TypeError):
            price_amount = 0.0
            print(f"[coze_adapter] price字段无效: '{fields.get('price')}', 默认0.0")

        plugin_json = {
            "name": fields.get('slug', ''),
            "display_name": fields.get('displayName', ''),
            "description": fields.get('summary', ''),
            "tools": tools,
            "version": fields.get('version', '1.0.0'),
            "license": fields.get('license', 'MIT'),
            "homepage": "",
            "config": {
                "price_model": fields.get('billingType', 'per_call'),
                "price_amount": price_amount,
            },
        }

        return plugin_json

    def upload_skill(self, skill_path: str, slug: str) -> dict:
        """上传skill到Coze平台

        Coze平台需要官方邀请才能上传, 当前返回pending状态。
        当获得邀请后, 此方法应实现实际的上传逻辑。

        Args:
            skill_path: skill目录路径
            slug: skill slug

        Returns:
            dict: {
                'status': 'pending',
                'reason': 'coze_invite_required',
                'slug': slug,
                'message': 'Coze平台需要官方邀请, 当前无法自动上传'
            }
        """
        return {
            'status': 'pending',
            'reason': 'coze_invite_required',
            'slug': slug,
            'message': 'Coze平台需要官方邀请, 当前无法自动上传',
            'timestamp': datetime.now().isoformat(),
        }

    def estimate_revenue(self, price: float, is_free: bool = False) -> dict:
        """预估Coze平台收入

        Coze创作者分成: 70%
        收入公式: price × 0.70

        Args:
            price: skill定价
            is_free: 是否免费skill

        Returns:
            dict: {
                'creator_revenue': float,
                'platform_revenue': float,
                'share_rate': float,
                'estimated': True
            }
        """
        if is_free or price <= 0:
            return {
                'creator_revenue': 0,
                'platform_revenue': 0,
                'share_rate': self.creator_share,
                'estimated': True,
                'note': '免费skill, 无直接收入'
            }

        creator_revenue = round(price * self.creator_share, 2)
        platform_revenue = round(price * (1 - self.creator_share), 2)

        return {
            'creator_revenue': creator_revenue,
            'platform_revenue': platform_revenue,
            'share_rate': self.creator_share,
            'estimated': True,
        }

    def batch_check_eligibility(self, skills: dict) -> dict:
        """批量检查skill的Coze资格

        复用platform_ops.cmd_coze_actions()的逻辑,
        但返回更详细的评估结果。

        Args:
            skills: {slug: skill_data} 字典

        Returns:
            dict: {
                'paid_eligible': [slug, ...],
                'free_eligible': [slug, ...],
                'not_eligible': [slug, ...],
                'details': {slug: eligibility_result}
            }
        """
        result = {
            'paid_eligible': [],
            'free_eligible': [],
            'not_eligible': [],
            'details': {},
        }

        for slug, skill_data in skills.items():
            if skill_data.get('is_source'):
                continue

            # 补充slug字段
            skill_data_with_slug = dict(skill_data)
            skill_data_with_slug['slug'] = slug

            eligibility = self.check_eligibility(skill_data_with_slug)
            result['details'][slug] = eligibility
            result[eligibility['category']].append(slug)

        return result


# CLI入口
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Coze平台适配器 (V95 V6)')
    parser.add_argument('--dry-run', action='store_true', help='试运行: 检查资格不实际上传')
    parser.add_argument('--slug', type=str, help='检查单个skill的资格')
    args = parser.parse_args()

    adapter = CozeAdapter()

    if args.slug:
        # 检查单个skill
        from daily_sync import read_upload_tracking
        tracking = read_upload_tracking()
        skill_data = tracking.get('skills', {}).get(args.slug, {})
        if not skill_data:
            print(f"skill {args.slug} 不在upload_tracking.json中")
            sys.exit(1)
        skill_data['slug'] = args.slug
        result = adapter.check_eligibility(skill_data)
        print(f"\n=== {args.slug} Coze资格检查 ===")
        print(f"分类: {result['category']}")
        print(f"总分: {result['total_score']}/100")
        if result.get('estimated_revenue'):
            print(f"预估收入: ¥{result['estimated_revenue']}")
        print(f"\n详细评估:")
        for cid, c in result['criteria'].items():
            status = '✓' if c['passed'] else '✗'
            print(f"  {status} {COZE_CRITERIA[cid]['name']}: {c['reason']}")
    elif args.dry_run:
        # 批量检查
        from daily_sync import read_upload_tracking
        tracking = read_upload_tracking()
        skills = tracking.get('skills', {})
        result = adapter.batch_check_eligibility(skills)
        print(f"\n=== Coze批量资格检查 ===")
        print(f"付费skill (可70%分成): {len(result['paid_eligible'])}个")
        print(f"免费skill (引流): {len(result['free_eligible'])}个")
        print(f"不符合: {len(result['not_eligible'])}个")
    else:
        parser.print_help()
