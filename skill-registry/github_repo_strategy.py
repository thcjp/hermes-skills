#!/usr/bin/env python3
"""
GitHub 仓库策略配置 (固化的策略定义)
===================================
本文件定义了项目的GitHub双仓库策略, 所有自动化脚本应引用此配置。

策略模型:
  1. hermes-skills (公开引流仓库)
     - URL: https://github.com/thcjp/hermes-skills
     - git remote: hermes-skills
     - 可见性: public
     - 推送内容: 仅免费skill (pricing=free, pricing_tier=L1/L2, license=MIT/Apache-2.0)
     - 目的: 社区影响力、品牌建设、引流到SkillHub付费版
     - 不推送: 付费skill (pricing_tier=L3/L4, license=Proprietary)

  2. origin (私有备份仓库)
     - URL: https://github.com/thcjp/-.git
     - git remote: origin
     - 可见性: private (建议在GitHub设置中改为private)
     - 推送内容: 全部skill (免费+付费) + 项目代码 + 数据库 + 脚本
     - 目的: 项目完整备份, 灾难恢复
     - 不推送: 无 (全部推送)

判定规则 (按优先级):
  1. pricing 字段 = 'free' → 免费 → 推送到hermes-skills
  2. pricing_tier in (L1-入门级, L2-标准级) → 免费 → 推送到hermes-skills
  3. license in (MIT, Apache-2.0) → 免费 → 推送到hermes-skills
  4. 以上都不满足 → 付费 → 仅推送到origin (私有备份)

使用方式:
  from github_repo_strategy import is_free_skill, PUBLIC_REMOTE, PRIVATE_REMOTE
"""

# ============================================================
# 仓库配置
# ============================================================

# 公开引流仓库
PUBLIC_REMOTE = "hermes-skills"
PUBLIC_REPO_URL = "https://github.com/thcjp/hermes-skills"
PUBLIC_REPO_VISIBILITY = "public"

# 私有备份仓库
PRIVATE_REMOTE = "origin"
PRIVATE_REPO_URL = "https://github.com/thcjp/-.git"
PRIVATE_REPO_VISIBILITY = "private"  # 建议在GitHub设置中改为private

# 分支
GITHUB_BRANCH = "main"

# ============================================================
# 免费/付费判定规则
# ============================================================

FREE_PRICING_VALUES = {"free", "Free", "FREE"}
FREE_PRICING_TIERS = {"L1-入门级", "L2-标准级"}
FREE_LICENSES = {"MIT", "Apache-2.0"}
PAID_PRICING_TIERS = {"L3-专业级", "L4-企业级"}
PAID_LICENSES = {"Proprietary", "Commercial"}


def is_free_skill(pricing: str = "", pricing_tier: str = "", license_val: str = "") -> bool:
    """判断skill是否为免费skill

    Args:
        pricing: frontmatter中的pricing字段值
        pricing_tier: frontmatter中的pricing_tier字段值
        license_val: frontmatter中的license字段值

    Returns:
        True if free skill (可以推送到公开引流仓库)
        False if paid skill (仅推送到私有备份仓库)
    """
    if pricing and pricing.lower() in FREE_PRICING_VALUES:
        return True
    if pricing_tier and pricing_tier in FREE_PRICING_TIERS:
        return True
    if license_val and license_val in FREE_LICENSES:
        return True
    return False


def get_push_strategy(pricing: str = "", pricing_tier: str = "", license_val: str = "") -> dict:
    """获取推送策略

    Returns:
        {
            'is_free': bool,
            'push_to_public': bool,  # 是否推送到hermes-skills
            'push_to_private': bool, # 是否推送到origin
            'visibility': str,       # public/private
        }
    """
    free = is_free_skill(pricing, pricing_tier, license_val)
    return {
        'is_free': free,
        'push_to_public': free,
        'push_to_private': True,  # 所有skill都推送到私有备份
        'visibility': 'public' if free else 'private',
    }


# ============================================================
# 文件判定辅助函数
# ============================================================

def is_free_skill_from_file(skill_md_path) -> bool:
    """从SKILL.md文件读取frontmatter并判断是否为免费skill"""
    import re
    from pathlib import Path

    if isinstance(skill_md_path, str):
        skill_md_path = Path(skill_md_path)

    try:
        content = skill_md_path.read_text(encoding='utf-8', errors='replace')
        if content.startswith('\ufeff'):
            content = content[1:]
        if not content.startswith('---'):
            return False

        parts = content.split('---', 2)
        if len(parts) < 3:
            return False

        fm_text = parts[1].strip()
        pricing = ""
        pricing_tier = ""
        license_val = ""

        for line in fm_text.split('\n'):
            if ':' in line and not line.startswith(' '):
                key, _, val = line.partition(':')
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key == 'pricing':
                    pricing = val
                elif key == 'pricing_tier':
                    pricing_tier = val
                elif key == 'license':
                    license_val = val

        return is_free_skill(pricing, pricing_tier, license_val)
    except Exception:
        return False


if __name__ == "__main__":
    # 自测
    print("GitHub 仓库策略配置")
    print("=" * 60)
    print(f"公开引流仓库: {PUBLIC_REPO_URL} (remote: {PUBLIC_REMOTE})")
    print(f"私有备份仓库: {PRIVATE_REPO_URL} (remote: {PRIVATE_REMOTE})")
    print(f"免费定价层: {FREE_PRICING_TIERS}")
    print(f"免费许可证: {FREE_LICENSES}")
    print()

    # 测试用例
    test_cases = [
        ("free", "L1-入门级", "MIT", True),
        ("free", "L2-标准级", "MIT", True),
        ("paid", "L3-专业级", "Proprietary", False),
        ("paid", "L4-企业级", "Proprietary", False),
        ("", "L1-入门级", "", True),
        ("", "L3-专业级", "", False),
        ("", "", "MIT", True),
        ("", "", "Proprietary", False),
    ]

    print("测试用例:")
    for pricing, tier, lic, expected in test_cases:
        result = is_free_skill(pricing, tier, lic)
        status = "PASS" if result == expected else "FAIL"
        print(f"  [{status}] pricing={pricing!r}, tier={tier!r}, license={lic!r} → free={result} (expected={expected})")
