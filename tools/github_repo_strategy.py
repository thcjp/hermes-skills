#!/usr/bin/env python3
"""
GitHub 仓库策略配置 (固化的策略定义)
===================================
V119 W1 (TD-142): 改为从 platform_config re-export, 消除本地硬编码副本。
V128 Y5: config/github_repo_strategy.py 是另一个向后兼容入口(无人导入)。
本文件是实际使用的入口,被version_sync_pipeline.py等模块导入。

本文件保留向后兼容的别名导出(PUBLIC_REMOTE等无GITHUB_前缀的名称),
供 version_sync_pipeline.py 等已使用这些名称的模块导入。

策略模型:
  1. hermes-skills (公开引流仓库) - 仅免费skill
  2. origin (私有备份仓库) - 全部skill + 项目代码

使用方式:
  from github_repo_strategy import is_free_skill, PUBLIC_REMOTE, PRIVATE_REMOTE
"""

# V119 W1: 从 platform_config 统一导入, 消除本地硬编码副本
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))

from platform_config import (
    GITHUB_PUBLIC_REMOTE, GITHUB_PUBLIC_REPO_URL, GITHUB_PUBLIC_VISIBILITY,
    GITHUB_PRIVATE_REMOTE, GITHUB_PRIVATE_REPO_URL, GITHUB_PRIVATE_VISIBILITY,
    is_free_skill,
    GITHUB_BRANCH,  # [V131 B1] re-export: version_sync_pipeline从此模块导入GITHUB_BRANCH
)

# ============================================================
# 向后兼容别名 (无 GITHUB_ 前缀的短名称)
# ============================================================

PUBLIC_REMOTE = GITHUB_PUBLIC_REMOTE
PUBLIC_REPO_URL = GITHUB_PUBLIC_REPO_URL
PUBLIC_REPO_VISIBILITY = GITHUB_PUBLIC_VISIBILITY

PRIVATE_REMOTE = GITHUB_PRIVATE_REMOTE
PRIVATE_REPO_URL = GITHUB_PRIVATE_REPO_URL
PRIVATE_REPO_VISIBILITY = GITHUB_PRIVATE_VISIBILITY


# ============================================================
# 文件判定辅助函数 (本文件独有, platform_config 未定义)
# ============================================================

def is_free_skill_from_file(skill_md_path) -> bool:
    """从SKILL.md文件读取frontmatter并判断是否为免费skill

    V127 X8: 使用skill_core.parser.parse_frontmatter替代手动解析(TD-197)
    """
    from pathlib import Path
    from skill_core.parser import parse_frontmatter  # V127 X8: 统一frontmatter解析

    if isinstance(skill_md_path, str):
        skill_md_path = Path(skill_md_path)

    try:
        content = skill_md_path.read_text(encoding='utf-8', errors='replace')
        result = parse_frontmatter(content)
        metadata = result['fields']

        pricing = metadata.get('pricing', '')
        pricing_tier = metadata.get('pricing_tier', '')
        license_val = metadata.get('license', '')

        return is_free_skill(pricing, pricing_tier, license_val)
    except Exception:  # [V130 A1] 宽泛捕获: 文件读取和frontmatter解析可能因编码/格式等多种原因失败
        return False


if __name__ == "__main__":
    # 自测
    print("GitHub 仓库策略配置 (re-export from platform_config)")
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
