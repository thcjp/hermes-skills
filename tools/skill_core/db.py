"""
skill_core.db - DB连接与业务函数(单一来源)

V116 W1: re-export db.py所有公共函数, 实现统一入口。
调用方可通过 `from skill_core import db as db_module` 访问全部功能,
无需再 `import db as db_module` + `from skill_core.db import get_db` 双重导入。
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
# V116 W1: 修复skill_core子目录的Phase 1路径 (需要parent.parent.parent才能到达d:\skills)
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent.parent / "config"))
from project_config import DB_PATH
# === End Phase 1 ===

# V116 W1: 添加tools目录到path, 使db.py可被re-export
_tools_dir = _Path(__file__).resolve().parent.parent
if str(_tools_dir) not in _sys.path:
    _sys.path.insert(0, str(_tools_dir))


import sqlite3
from pathlib import Path
from typing import Set

# DB路径(单一来源, 消除5模块硬编码)
# 优先使用环境变量, 其次默认路径
# DB_PATH imported from config

# V149 T1: 自动确保关键表存在 (修复upgrade_tracking表缺失导致变更检测失效)
_tables_ensured = False

def _ensure_critical_tables():
    """确保数据库中所有关键表存在 (V149 T1)

    问题: init_database()不会在get_db()时自动调用,
    导致新增表(upgrade_tracking等)在旧数据库中缺失。
    解决: 模块加载时检查并创建缺失的表。
    """
    global _tables_ensured
    if _tables_ensured:
        return

    try:
        conn = sqlite3.connect(str(DB_PATH))
        c = conn.cursor()

        # 检查upgrade_tracking表是否存在
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='upgrade_tracking'")
        if not c.fetchone():
            # 表不存在,调用db.py的init_database()创建所有缺失的表
            try:
                from db import init_database
                conn.close()
                init_database()
            except ImportError:
                conn.close()

        conn.close()
        _tables_ensured = True
    except Exception:
        _tables_ensured = True  # 避免重复尝试

# 模块加载时执行一次
_ensure_critical_tables()


def get_db(timeout: float = 5.0):
    """获取DB连接(row_factory=Row, foreign_keys=ON)

    所有模块应通过此函数获取连接, 不直接sqlite3.connect

    Args:
        timeout: 连接锁等待超时秒数(默认5.0, db.py._get_db_connection使用30)
    """
    conn = sqlite3.connect(DB_PATH, timeout=timeout)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA busy_timeout = 5000")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


def get_db_path() -> str:
    """获取DB路径(用于日志/调试)"""
    return DB_PATH


def get_existing_slugs_from_db() -> Set[str]:
    """查询数据库 skills 表获取所有已存在的 slug。

    V121 W4: 统一 auto_differentiate.py / finance_differentiate.py 的重复实现。
    """
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT DISTINCT slug FROM skills")
    slugs = {row[0] for row in c.fetchall() if row[0]}
    conn.close()
    return slugs


def get_existing_source_slugs_from_db() -> Set[str]:
    """查询数据库 skills 表获取所有已存在的 source_slug。

    V126 W4: 统一 auto_discover.py / github_scanner.py 的重复实现(TD-184)。
    """
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT source_slug FROM skills
        WHERE source_slug IS NOT NULL AND source_slug != ''
    """)
    slugs = {row[0] for row in c.fetchall()}
    conn.close()
    return slugs


def get_existing_display_names_from_db() -> Set[str]:
    """查询数据库 skills 表获取所有已存在的 display_name (小写)。

    V128 Y7: 从auto_discover.py迁移,统一display_name查询入口(TD-207)。
    """
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT current_display_name FROM skills
        WHERE current_display_name IS NOT NULL AND current_display_name != ''
    """)
    names = {row[0].lower() for row in c.fetchall()}
    conn.close()
    return names


def backup_database(reason: str = "manual") -> str:
    """备份数据库到BACKUP_DIR, 返回备份文件路径

    V94.2新增: 在任何DB修改操作前调用, 支持3层回滚方案
    """
    from project_config import BACKUP_DIR
    from datetime import datetime
    import shutil

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"skills_backup_{timestamp}_{reason}.db"
    backup_path = Path(BACKUP_DIR) / backup_name
    shutil.copy2(DB_PATH, backup_path)
    return str(backup_path)


# ============ V116 W1: Re-export db.py公共函数 ============
# 统一入口: 调用方用 `from skill_core import db as db_module` 即可访问
# get_db() + 全部业务函数(insert_skill, update_skill_fields, record_operation等)
# 消除 `import db as db_module` + `from skill_core.db import get_db` 双重导入
# [V132 C4] 垫片迁移评估: 30+文件通过skill_core.db访问, 垫片仍需保留
# 迁移条件: 需将db.py(1627行)全部函数移入skill_core/db.py, 属高风险重构(TD-27)
from db import *  # noqa: E402,F401,F403

# V122 W5: re-export sqlite3异常类型和Row, 消除4文件import sqlite3
# 调用方可通过 db_module.OperationalError / db_module.Row 直接使用
OperationalError = sqlite3.OperationalError
IntegrityError = sqlite3.IntegrityError
Row = sqlite3.Row
