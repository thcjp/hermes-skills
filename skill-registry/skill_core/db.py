"""
skill_core.db - DB连接(单一来源)

轻量封装, 提供DB路径和连接函数
完整的register_skill等业务函数仍在主db.py中(避免大规模迁移风险)
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
# === End Phase 1 ===


import sqlite3
from pathlib import Path

# DB路径(单一来源, 消除5模块硬编码)
# 优先使用环境变量, 其次默认路径
import os
# DB_PATH imported from config


def get_db():
    """获取DB连接(row_factory=Row, foreign_keys=ON)

    所有模块应通过此函数获取连接, 不直接sqlite3.connect
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def get_db_path() -> str:
    """获取DB路径(用于日志/调试)"""
    return DB_PATH
