#!/usr/bin/env python3
"""
统一分类映射加载模块 (V115 W1)
================================
从 project_config.CATEGORY_MAP_FILE 加载分类映射配置,
消除 automated_review_system / clawhub_batch_uploader / enterprise_uploader 三重重复。
"""

import json
import sys as _sys
from pathlib import Path as _Path

# Phase 1: 统一配置导入
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent.parent / "config"))
from project_config import CATEGORY_MAP_FILE


def load_category_map() -> dict:
    """加载分类映射配置

    从 CATEGORY_MAP_FILE (data/category_mapping.json) 加载完整映射配置。
    文件不存在时返回空字典。

    Returns:
        dict: 完整的分类映射配置,包含:
            - local_to_skillhub_id: 本地分类→SkillHub数字ID
            - skillhub_categories: SkillHub分类信息
            - platform_categories: 平台分类键
            - local_to_platform: 本地分类→平台分类键
            - platform_to_team: 平台分类→团队分类名
            - team_categories: 团队分类信息
            - subcategory_mapping: 子分类映射
    """
    if CATEGORY_MAP_FILE.exists():
        with open(CATEGORY_MAP_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}
