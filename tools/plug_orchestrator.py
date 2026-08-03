#!/usr/bin/env python3
"""
Plug独立管道编排器 (V140 C1)
============================
将plug_generator + bundle_composer编排为独立管道,
不依赖skill管道(orchestrator.py / version_sync_pipeline.py)。

管道5阶段:
  1. discover  — 从DB查询A级skill + bundle_composer.find_best_bundle()
  2. compose   — 校验成员存在性 + 版本一致性 + 计算捆绑折扣价
  3. package   — 生成plug.json + SKILL.md + 营销文案(复用plug_generator)
  4. publish   — 仅上传到SkillHub(Proprietary, 不上ClawHub/GitHub)
  5. maintain — 成员skill升级时重新评估Plug组合

共享组件(与skill管道共用):
  - db_module (数据持久化)
  - pricing_engine (定价计算)
  - quality_gate (质量检查)
  - llm_bridge (LLM调用)
  - pre_upload_checks (共享预检查)

不共享组件(Plug专有):
  - plug_generator (Plug生成)
  - bundle_composer (组合发现)
  - plug_version_sync (Plug版本同步)

依赖说明:
  - 无外部依赖(标准库 + 项目内部模块)
  - plug_generator和bundle_composer已存在, 本模块编排调用
"""

from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime

# 统一配置导入
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "config"))
from project_config import TOOLS_DIR, PACKAGED_SKILLS_DIR, get_timestamp
_sys.path.insert(0, str(TOOLS_DIR))

from skill_core import db as db_module


class PlugOrchestrator:
    """Plug独立管道编排器

    管道独立于skill管道(orchestrator.py), 仅共享db_module和pre_upload_checks等基础设施。
    """

    def __init__(self):
        self.pipeline_name = "plug"
        self.phases = {}

    def run_full_pipeline(self, a_grade_slugs: List[str] = None, dry_run: bool = False) -> Dict[str, Any]:
        """运行完整Plug管道(5阶段)

        V152 R5修复: 新增dry_run参数,支持模拟测试模式
        dry_run=True时跳过实际上传,但执行所有质量检查和安全门控。
        dry_run=False时,skillhub_adapter不可用则阻断(fail-safe)。

        Args:
            a_grade_slugs: 指定参与组合的skill slug列表(None则自动发现)
            dry_run: 模拟模式,不执行实际上传

        Returns:
            管道执行结果, 含各阶段输出
        """
        result = {
            'pipeline': 'plug',
            'timestamp': get_timestamp(),
            'phases': {},
            'dry_run': dry_run,
        }

        # V151 T2: 前置企业认证校验(Plug使用Proprietary license,需企业认证)
        # 避免discover→compose→package全部完成后在publish阶段才失败
        # V152 R5修复: 非dry_run模式下skillhub_adapter不可用则阻断(fail-safe)
        # V152 R8修复: dry_run模式下认证失败也应跳过(仅警告),不阻断模拟测试
        try:
            from skillhub_adapter import check_enterprise_certification
            if not check_enterprise_certification():
                if not dry_run:
                    result['status'] = 'blocked'
                    result['error'] = (
                        'Plug需要Proprietary license, 当前账号未通过企业认证, '
                        '无法发布付费组合包(请先完成企业认证+微信支付商户绑定)'
                    )
                    print(f"[BLOCKED] {result['error']}")
                    return result
                print("[WARN] dry_run模式: 未通过企业认证,跳过(仅模拟测试,不实际上传)")
        except ImportError:
            if not dry_run:
                result['status'] = 'blocked'
                result['error'] = 'skillhub_adapter不可用且非dry_run模式,企业认证校验阻断(fail-safe)'
                print(f"[BLOCKED] {result['error']}")
                return result
            print("[WARN] skillhub_adapter不可用,dry_run模式跳过企业认证前置校验")
        except Exception as e:
            if not dry_run:
                result['status'] = 'blocked'
                result['error'] = f'企业认证校验异常,阻断(fail-safe): {e}'
                print(f"[BLOCKED] {result['error']}")
                return result
            print(f"[WARN] 企业认证校验异常(dry_run模式跳过): {e}")

        # Phase 1: discover
        result['phases']['discover'] = self.phase_discover(a_grade_slugs)
        bundle = result['phases']['discover'].get('bundle')
        if not bundle or not bundle.get('members'):
            result['status'] = 'no_bundle'
            return result

        # Phase 2: compose
        result['phases']['compose'] = self.phase_compose(bundle)
        if not result['phases']['compose'].get('valid'):
            result['status'] = 'compose_failed'
            return result

        # Phase 3: package
        result['phases']['package'] = self.phase_package(bundle)

        # Phase 4: publish (仅SkillHub)
        result['phases']['publish'] = self.phase_publish(
            result['phases']['package'],
            dry_run=dry_run
        )

        # Phase 5: maintain (记录成员关系供后续升级评估)
        result['phases']['maintain'] = self.phase_maintain(bundle)

        result['status'] = 'success'
        return result

    def phase_discover(self, a_grade_slugs: List[str] = None) -> Dict[str, Any]:
        """Phase 1: 发现 — 查询A级skill + 组合最佳bundle

        复用bundle_composer.find_best_bundle()进行自动发现。
        如果指定了a_grade_slugs, 则使用compose_bundle直接组合指定skill。

        Args:
            a_grade_slugs: 指定skill slug列表(None则自动发现)

        Returns:
            {'bundle': bundle_dict, 'discovered_at': timestamp}
        """
        if a_grade_slugs:
            # 指定slug时直接组合
            from bundle_composer import compose_bundle
            bundle = compose_bundle(skill_slugs=a_grade_slugs)
        else:
            # 自动发现最佳bundle
            from bundle_composer import find_best_bundle
            bundle = find_best_bundle()

        return {
            'bundle': bundle,
            'discovered_at': get_timestamp(),
        }

    def phase_compose(self, bundle: Dict) -> Dict[str, Any]:
        """Phase 2: 组合 — 校验成员存在性 + 版本一致性 + 捆绑定价

        Args:
            bundle: bundle_composer返回的bundle字典

        Returns:
            {'valid': bool, 'issues': list, 'individual_total': float,
             'bundle_price': float, 'discount_rate': float}
        """
        members = bundle.get('members', [])
        issues = []

        # 校验每个成员的存在性和版本
        for member in members:
            slug = member.get('slug', '')
            if not slug:
                issues.append('成员缺少slug字段')
                continue

            if not self._check_skill_exists(slug):
                issues.append(f'成员不存在于DB: {slug}')

        # 版本一致性检查: 遍历成员比较version字段
        # 不同skill可以有不同版本, 版本不一致仅记录warning不阻断
        member_versions = {}
        for member in members:
            slug = member.get('slug', '')
            # 优先使用成员自带的version字段, 缺失则从DB查询当前版本
            version = member.get('version') or self._get_skill_version(slug)
            if slug and version and version != 'unknown':
                member_versions[slug] = version
        unique_versions = set(member_versions.values())
        if len(unique_versions) > 1:
            print(f"  [WARN] 成员版本不一致: {member_versions} "
                  f"(不同skill可有不同版本, 仅记录不阻断)")

        # 捆绑折扣价计算(基于成员suggested_price)
        individual_total = 0.0
        for member in members:
            slug = member.get('slug', '')
            price = self._get_skill_price(slug)
            individual_total += price

        # 8折捆绑定价
        bundle_price = round(individual_total * 0.8, 2)

        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'individual_total': individual_total,
            'bundle_price': bundle_price,
            'discount_rate': 0.8,
            'composed_at': get_timestamp(),
        }

    def phase_package(self, bundle: Dict) -> Dict[str, Any]:
        """Phase 3: 包装 — 生成plug.json + SKILL.md(复用plug_generator)

        Args:
            bundle: bundle_composer返回的bundle字典

        Returns:
            {'plugs': list, 'bundle_slug': str, 'packaged_at': timestamp}
        """
        # 复用plug_generator.generate_plugs()
        from plug_generator import generate_plugs

        a_grade_slugs = [m.get('slug', '') for m in bundle.get('members', []) if m.get('slug')]
        plugs_result = generate_plugs(a_grade_slugs=a_grade_slugs)

        return {
            'plugs': plugs_result.get('plugs', []),
            'bundle_slug': bundle.get('bundle_slug', ''),
            'total_plugs': plugs_result.get('total', 0),
            'packaged_at': get_timestamp(),
        }

    def phase_publish(self, package_result: Dict, dry_run: bool = False) -> Dict[str, Any]:
        """Phase 4: 发布 — 仅上传到SkillHub(Proprietary license)

        Plug使用Proprietary license(捆绑包), 不上ClawHub/GitHub。
        复用enterprise_uploader.upload_skill + pre_upload_checks。

        V152 R5修复: 新增dry_run参数, dry_run=True时仅打印将要发布的
        Plug信息, 不调用enterprise_uploader.upload_skill, 不触发实际上传。
        非dry-run模式下, 调用daily_sync.check_upload_rate_limit('skillhub')
        检查速率限制, 不通过则跳过发布并记录(fail-safe)。

        Args:
            package_result: phase_package的返回结果
            dry_run: 模拟模式, 仅打印不实际上传

        Returns:
            {'results': list, 'published_at': timestamp}
        """
        # 安全导入: pre_upload_checks 和 skillhub_adapter 模块已被移除,
        # 使用 try/except 优雅降级, 避免运行时 ImportError
        try:
            from pre_upload_checks import run_pre_checks
        except ImportError:
            run_pre_checks = None
            print("[WARN] pre_upload_checks模块不可用, 跳过预检查")

        try:
            from skillhub_adapter import should_use_api
        except ImportError:
            # skillhub_adapter不可用时, 默认使用API通道(enterprise_uploader)
            should_use_api = lambda: True
            print("[WARN] skillhub_adapter模块不可用, 默认使用API通道")

        plugs = package_result.get('plugs', [])
        results = []

        for plug in plugs:
            plug_slug = plug.get('plug_slug', '')
            plug_dir = plug.get('output_dir', '')

            if not plug_slug:
                results.append({'status': 'skipped', 'reason': 'no_plug_slug'})
                continue

            # dry_run模式: 仅打印将要发布的Plug信息, 不实际上传
            if dry_run:
                print(f"  [DRY-RUN] 将发布Plug: {plug_slug} (目录: {plug_dir})")
                results.append({
                    'slug': plug_slug,
                    'status': 'dry_run',
                    'message': f'dry_run模式: 将发布Plug {plug_slug}, 不执行实际上传',
                })
                continue

            # 速率限制检查(非dry-run模式, fail-safe)
            try:
                from daily_sync import check_upload_rate_limit
                rate_check = check_upload_rate_limit('skillhub')
                if not rate_check['allowed']:
                    print(f"  [SKIP] 速率限制未通过, 跳过发布 {plug_slug}: "
                          f"{rate_check['reason']}")
                    results.append({
                        'slug': plug_slug,
                        'status': 'rate_limited',
                        'reason': rate_check['reason'],
                        'wait_seconds': rate_check.get('wait_seconds'),
                    })
                    continue
            except ImportError:
                # daily_sync不可用时阻断(fail-safe): 无法校验速率限制则不发布
                print(f"  [BLOCKED] daily_sync不可用, 无法校验速率限制, "
                      f"跳过发布 {plug_slug} (fail-safe)")
                results.append({
                    'slug': plug_slug,
                    'status': 'error',
                    'error': 'daily_sync不可用, 速率限制校验失败(fail-safe)',
                })
                continue

            # 预检查(Proprietary需要企业认证) — 模块不可用时跳过
            if run_pre_checks is not None:
                passed, msg = run_pre_checks(
                    plug_dir, 'skillhub',
                    ['dedup', 'quality_gate', 'security_scan', 'proprietary_check'],
                    slug=plug_slug
                )
                if not passed:
                    results.append({
                        'slug': plug_slug,
                        'status': 'pre_check_failed',
                        'error': msg,
                    })
                    continue

            # 上传(SkillHub API优先)
            if should_use_api():
                try:
                    from enterprise_uploader import upload_skill
                    eu_result = upload_skill(plug_slug, skip_publish=False)
                    results.append({
                        'slug': plug_slug,
                        'status': 'success' if eu_result.get('success') else 'failed',
                        'message': eu_result.get('message', ''),
                    })
                except ImportError:
                    results.append({
                        'slug': plug_slug,
                        'status': 'error',
                        'error': 'enterprise_uploader不可用',
                    })
            else:
                # CLI通道降级
                results.append({
                    'slug': plug_slug,
                    'status': 'skipped',
                    'reason': 'cli_channel_not_supported_for_plug',
                })

        return {
            'results': results,
            'published_at': get_timestamp(),
        }

    def phase_maintain(self, bundle: Dict) -> Dict[str, Any]:
        """Phase 5: 维护 — 记录Plug-成员关系到plug_members表

        Args:
            bundle: bundle_composer返回的bundle字典

        Returns:
            {'plug_slug': str, 'member_count': int, 'members': list,
             'recorded_at': timestamp}
        """
        members = bundle.get('members', [])
        bundle_slug = bundle.get('bundle_slug', '')

        conn = db_module.get_db()
        c = conn.cursor()

        # 确保plug_members表存在
        c.execute("""
            CREATE TABLE IF NOT EXISTS plug_members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plug_slug TEXT NOT NULL,
                member_slug TEXT NOT NULL,
                member_version TEXT NOT NULL DEFAULT '1.0.0',
                member_role TEXT,
                recorded_at TEXT NOT NULL,
                UNIQUE(plug_slug, member_slug)
            )
        """)

        # 记录Plug-成员关系
        for member in members:
            member_slug = member.get('slug', '')
            member_role = member.get('role', '')
            # 从DB查询成员当前版本
            member_version = self._get_skill_version(member_slug)

            try:
                c.execute("""
                    INSERT OR REPLACE INTO plug_members
                        (plug_slug, member_slug, member_version, member_role, recorded_at)
                    VALUES (?, ?, ?, ?, ?)
                """, (bundle_slug, member_slug, member_version, member_role, get_timestamp()))
            except Exception as e:
                print(f"  [WARN] 记录Plug成员关系失败: {e}")

        conn.commit()
        conn.close()

        return {
            'plug_slug': bundle_slug,
            'member_count': len(members),
            'members': [m.get('slug', '') for m in members],
            'recorded_at': get_timestamp(),
        }

    def evaluate_member_upgrade(self, plug_slug: str) -> Dict[str, Any]:
        """C3: 评估Plug成员是否需要升级

        检查Plug中每个成员skill的当前版本与记录版本是否一致,
        如果成员skill已升级, 标记Plug需要重新评估。

        Args:
            plug_slug: Plug的slug(即bundle_slug)

        Returns:
            {
                'needs_rebuild': bool,
                'upgraded_members': list,
                'current_versions': dict,
                'evaluated_at': timestamp,
            }
        """
        conn = db_module.get_db()
        c = conn.cursor()

        # 查询Plug成员
        try:
            c.execute("""
                SELECT member_slug, member_version FROM plug_members WHERE plug_slug = ?
            """, (plug_slug,))
            members = c.fetchall()
        except Exception:
            members = []

        conn.close()

        upgraded_members = []
        current_versions = {}

        for row in members:
            member_slug = row[0] if isinstance(row, tuple) else row['member_slug']
            recorded_version = row[1] if isinstance(row, tuple) else row['member_version']

            # 查询成员skill的当前版本
            current_version = self._get_skill_version(member_slug)
            current_versions[member_slug] = current_version

            if current_version != recorded_version and current_version != 'unknown':
                upgraded_members.append({
                    'slug': member_slug,
                    'recorded_version': recorded_version,
                    'current_version': current_version,
                })

        return {
            'plug_slug': plug_slug,
            'needs_rebuild': len(upgraded_members) > 0,
            'upgraded_members': upgraded_members,
            'current_versions': current_versions,
            'evaluated_at': get_timestamp(),
        }

    # ============ 内部辅助方法 ============

    def _check_skill_exists(self, slug: str) -> bool:
        """检查skill是否存在于数据库中"""
        conn = db_module.get_db()
        c = conn.cursor()
        c.execute("SELECT 1 FROM skills WHERE slug = ?", (slug,))
        result = c.fetchone() is not None
        conn.close()
        return result

    def _get_skill_version(self, slug: str) -> str:
        """获取skill的当前版本号"""
        conn = db_module.get_db()
        c = conn.cursor()
        c.execute("SELECT current_version FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        conn.close()
        if row:
            return row[0] if isinstance(row, tuple) else row['current_version']
        return 'unknown'

    def _get_skill_price(self, slug: str) -> float:
        """获取skill的建议价格"""
        conn = db_module.get_db()
        c = conn.cursor()
        c.execute("SELECT suggested_price FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        conn.close()
        if row:
            price = row[0] if isinstance(row, tuple) else row['suggested_price']
            return float(price) if price else 0.0
        return 0.0


# ============ CLI入口 ============

def main():
    """CLI入口: 运行完整Plug管道"""
    print("=" * 60)
    print("Plug独立管道 (V140 C1)")
    print("=" * 60)

    orchestrator = PlugOrchestrator()
    result = orchestrator.run_full_pipeline()

    print(f"\n状态: {result.get('status', 'unknown')}")

    for phase_name, phase_result in result.get('phases', {}).items():
        print(f"\n  [{phase_name}]")
        if isinstance(phase_result, dict):
            for k, v in phase_result.items():
                if k == 'bundle':
                    bundle = v
                    if isinstance(bundle, dict):
                        print(f"    bundle_slug: {bundle.get('bundle_slug', 'N/A')}")
                        print(f"    members: {len(bundle.get('members', []))}")
                elif k == 'plugs':
                    print(f"    plugs: {len(v) if isinstance(v, list) else v}")
                elif k == 'results':
                    print(f"    results: {len(v) if isinstance(v, list) else v}")
                elif k == 'issues':
                    if v:
                        print(f"    issues: {v}")
                elif k != 'discovered_at' and k != 'composed_at' and k != 'packaged_at' and k != 'published_at' and k != 'recorded_at':
                    print(f"    {k}: {v}")

    print(f"\n{'=' * 60}")
    print("Plug管道执行完成")


if __name__ == '__main__':
    main()
