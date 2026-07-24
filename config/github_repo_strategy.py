#!/usr/bin/env python3
"""
GitHub 仓库策略配置 (已迁移到 platform_config.py)
==================================================
此文件保留为向后兼容入口，实际定义在 platform_config.py 中。

策略模型:
  1. hermes-skills (公开引流仓库)
     - URL: https://github.com/thcjp/hermes-skills
     - git remote: hermes-skills
     - 可见性: public
     - 推送内容: 仅免费skill (pricing=free, pricing_tier=L1/L2, license=MIT/Apache-2.0)
     - 目的: 社区影响力、品牌建设、引流到SkillHub付费版

  2. origin (私有备份仓库)
     - URL: https://github.com/thcjp/-.git
     - git remote: origin
     - 可见性: private
     - 推送内容: 全部skill (免费+付费) + 项目代码 + 数据库 + 脚本
     - 目的: 项目完整备份, 灾难恢复
"""

# 从 platform_config 重新导出所有策略
from platform_config import (
    GITHUB_PUBLIC_REMOTE as PUBLIC_REMOTE,
    GITHUB_PUBLIC_REPO_URL as PUBLIC_REPO_URL,
    GITHUB_PUBLIC_VISIBILITY as PUBLIC_REPO_VISIBILITY,
    GITHUB_PRIVATE_REMOTE as PRIVATE_REMOTE,
    GITHUB_PRIVATE_REPO_URL as PRIVATE_REPO_URL,
    GITHUB_PRIVATE_VISIBILITY as PRIVATE_REPO_VISIBILITY,
    GITHUB_BRANCH,
    FREE_PRICING_VALUES,
    FREE_PRICING_TIERS,
    FREE_LICENSES,
    PAID_PRICING_TIERS,
    PAID_LICENSES,
    is_free_skill,
    get_push_strategy,
)

__all__ = [
    'PUBLIC_REMOTE', 'PUBLIC_REPO_URL', 'PUBLIC_REPO_VISIBILITY',
    'PRIVATE_REMOTE', 'PRIVATE_REPO_URL', 'PRIVATE_REPO_VISIBILITY',
    'GITHUB_BRANCH',
    'FREE_PRICING_VALUES', 'FREE_PRICING_TIERS', 'FREE_LICENSES',
    'PAID_PRICING_TIERS', 'PAID_LICENSES',
    'is_free_skill', 'get_push_strategy',
]
