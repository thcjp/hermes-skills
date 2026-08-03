#!/usr/bin/env python3
"""
通用工具函数模块 (V115 W2)
============================
统一 load_json / save_json 工具函数,
消除 clawhub_batch_uploader 和 source_security_scan 中的双重重复。

统一行为:
  - load_json: 文件不存在返回 None (调用方已有 None 检查)
  - save_json: 自动创建父目录 (更健壮, 取自 source_security_scan 版本)
"""

import json
from pathlib import Path
from typing import Optional, Any


def load_json(path) -> Optional[Any]:
    """加载 JSON 文件

    Args:
        path: 文件路径 (Path 或 str)

    Returns:
        解析后的 JSON 对象; 文件不存在时返回 None
    """
    path = Path(path) if not isinstance(path, Path) else path
    if not path.exists():
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, data: Any) -> None:
    """保存 JSON 文件

    自动创建父目录, 确保写入不会因目录缺失而失败。

    Args:
        path: 文件路径 (Path 或 str)
        data: 要序列化的数据
    """
    path = Path(path) if not isinstance(path, Path) else path
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
