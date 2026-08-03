"""
Skill项目版本管理SQLite数据库
位置：d:\skills\skill-registry.db

管理内容：
1. skills - 每个skill的基本信息（slug、名称、版本、分类、来源、当前状态）
2. versions - 版本历史（每次修改记录）
3. operations - 操作历史（修改、上传、撤回等）
4. platforms - 平台上传状态（clawhub、skillhub）
5. pricing - 收费策略（免费体验版/收费专业版）
6. sources - 来源信息（clawhub下载、原创、开源修改）
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH
# === End Phase 1 ===


import sqlite3
import json
from pathlib import Path
from datetime import datetime
import hashlib

# DB_PATH imported from config

# v2.4: 设置WAL模式提升并发性能 (持久化,只需设置一次)
# 解决多进程同时写入时"database is locked"问题
try:
    _wal_init_conn = sqlite3.connect(DB_PATH, timeout=30)
    _wal_init_conn.execute("PRAGMA journal_mode = WAL")
    _wal_init_conn.execute("PRAGMA busy_timeout = 5000")
    _wal_init_conn.close()
except Exception as e:
    print(f"[WARN] WAL初始化失败(可能其他进程正在初始化): {e}")

# v2.4: 带重试的连接辅助函数 (强化已有流程,不创建碎片化代码)
def _get_db_connection(timeout=30):
    """创建带WAL+busy_timeout的数据库连接,解决并发锁问题

    V121 W1: 对齐 skill_core.db.get_db() 的全部PRAGMA设置
    (row_factory, foreign_keys, busy_timeout, journal_mode=WAL)
    R75.2 统一化: 委托 skill_core.db.get_db() 消除并行DB连接实现
    """
    from skill_core.db import get_db
    return get_db(timeout=timeout)


# v1.3: Schema版本管理常量
SCHEMA_VERSION_BASELINE = 1  # 基线版本(含25个ALTER TABLE合并)


def _column_exists(cursor, table_name, column_name):
    """检查表中是否存在指定列 (v1.3: 显式检查替代try/except模式)

    参数:
        cursor: 数据库游标
        table_name: 表名
        column_name: 列名

    返回:
        bool: 列是否存在
    """
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]
    return column_name in columns


def _add_column_if_missing(cursor, table_name, column_name, column_def):
    """安全添加列 (v1.3: 显式检查替代try/except, 统一迁移模式)

    参数:
        cursor: 数据库游标
        table_name: 表名
        column_name: 列名
        column_def: 列定义 (如 "TEXT DEFAULT 'unknown'")
    """
    if not _column_exists(cursor, table_name, column_name):
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_def}")


def migrate_schema(target_version=None):
    """数据库schema迁移框架 (v1.3)

    当前仅记录版本,不执行新迁移。
    未来版本可通过在此函数中添加迁移步骤实现版本化schema升级。

    参数:
        target_version: 目标版本号 (None则迁移到最新)

    返回:
        current_version: 当前数据库schema版本
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()

    # 确保schema_version表存在
    c.execute("""
        CREATE TABLE IF NOT EXISTS schema_version (
            version INTEGER PRIMARY KEY,
            applied_at TEXT NOT NULL,
            description TEXT
        )
    """)

    # 获取当前版本
    c.execute("SELECT MAX(version) FROM schema_version")
    row = c.fetchone()
    current_version = row[0] if row and row[0] else 0

    if target_version is None:
        target_version = SCHEMA_VERSION_BASELINE

    if current_version >= target_version:
        conn.close()
        return current_version

    # 未来迁移步骤在此添加:
    # if current_version < 2:
    #     ... migration to v2 ...
    #     c.execute("INSERT INTO schema_version (version, applied_at, description) VALUES (2, ?, 'description')",
    #               (datetime.now().isoformat(),))

    conn.commit()
    conn.close()
    return target_version


def _create_schema_version_table(c):
    """创建schema_version表并记录基线版本"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS schema_version (
            version INTEGER PRIMARY KEY,
            applied_at TEXT NOT NULL,
            description TEXT
        )
    """)
    c.execute(
        "INSERT OR IGNORE INTO schema_version (version, applied_at, description) VALUES (?, ?, ?)",
        (SCHEMA_VERSION_BASELINE, datetime.now().isoformat(),
         "baseline: 25 ALTER TABLEs consolidated to explicit column checks + simhash column added")
    )


def _create_skills_table(c):
    """创建skills主表并执行列迁移"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT UNIQUE NOT NULL,
            current_name TEXT,
            current_display_name TEXT,
            current_version TEXT NOT NULL,
            category TEXT,
            source TEXT NOT NULL,
            source_slug TEXT,
            source_url TEXT,
            source_author TEXT,
            source_license TEXT,
            local_path TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            current_status TEXT NOT NULL,
            is_differentiated INTEGER DEFAULT 0,
            differentiation_date TEXT,
            pricing_model TEXT,
            skill_type TEXT,
            notes TEXT,
            edition TEXT,
            parent_slug TEXT,
            current_score INTEGER DEFAULT 0,
            workflow_state TEXT DEFAULT 'step1_read_original',
            suggested_price REAL,
            pricing_category TEXT,
            pricing_rationale TEXT,
            pricing_tier TEXT,
            is_paid INTEGER DEFAULT 0,
            simhash INTEGER DEFAULT 0
        )
    """)
    # v1.3: 迁移 - 为已存在的数据库添加新列 (显式检查替代try/except)
    _add_column_if_missing(c, "skills", "edition", "TEXT")
    _add_column_if_missing(c, "skills", "parent_slug", "TEXT")
    _add_column_if_missing(c, "skills", "current_score", "INTEGER DEFAULT 0")
    _add_column_if_missing(c, "skills", "workflow_state", "TEXT DEFAULT 'step1_read_original'")
    _add_column_if_missing(c, "skills", "suggested_price", "REAL")
    _add_column_if_missing(c, "skills", "pricing_category", "TEXT")
    _add_column_if_missing(c, "skills", "pricing_rationale", "TEXT")
    _add_column_if_missing(c, "skills", "pricing_tier", "TEXT")
    _add_column_if_missing(c, "skills", "is_paid", "INTEGER DEFAULT 0")
    # v1.4: 三轨关联字段
    _add_column_if_missing(c, "skills", "summary", "TEXT")
    _add_column_if_missing(c, "skills", "free_slug", "TEXT")
    _add_column_if_missing(c, "skills", "paid_slug", "TEXT")
    # v1.5: 四平台同步状态字段 (P0-3a)
    _add_column_if_missing(c, "skills", "skillhub_sync_status", "TEXT DEFAULT 'unknown'")
    _add_column_if_missing(c, "skills", "clawhub_sync_status", "TEXT DEFAULT 'unknown'")
    _add_column_if_missing(c, "skills", "github_public_sync_status", "TEXT DEFAULT 'unknown'")
    _add_column_if_missing(c, "skills", "github_private_sync_status", "TEXT DEFAULT 'unknown'")
    _add_column_if_missing(c, "skills", "last_sync_at", "TEXT")
    # v1.6: 本地LLM质量评分字段 (T1-004)
    _add_column_if_missing(c, "skills", "local_quality_score", "REAL DEFAULT 0.0")
    _add_column_if_missing(c, "skills", "local_score_feedback", "TEXT DEFAULT ''")
    _add_column_if_missing(c, "skills", "local_score_at", "TEXT")
    # v3.0: 内容指纹字段 (用于防重复内容检测)
    _add_column_if_missing(c, "skills", "content_hash", "TEXT")
    # v1.3: SimHash指纹列 (原由content_dedup.py动态添加,现纳入正式schema)
    _add_column_if_missing(c, "skills", "simhash", "INTEGER DEFAULT 0")


def _create_versions_table(c):
    """创建versions版本历史表"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS versions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            version TEXT NOT NULL,
            created_at TEXT NOT NULL,
            changelog TEXT,
            content_hash TEXT,
            file_size INTEGER,
            line_count INTEGER,
            changes_summary TEXT,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)


def _create_operations_table(c):
    """创建operations操作历史表"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            operation_type TEXT NOT NULL,
            operation_date TEXT NOT NULL,
            operator TEXT,
            details TEXT,
            before_state TEXT,
            after_state TEXT,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)


def _create_platform_uploads_table(c):
    """创建platform_uploads表并执行列迁移"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS platform_uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            version TEXT NOT NULL,
            platform TEXT NOT NULL,
            platform_slug TEXT,
            upload_date TEXT NOT NULL,
            upload_status TEXT NOT NULL,
            http_status INTEGER,
            error_message TEXT,
            visibility TEXT,
            pricing_on_platform TEXT,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)
    _add_column_if_missing(c, "platform_uploads", "community_published", "INTEGER DEFAULT 0")
    _add_column_if_missing(c, "platform_uploads", "download_ready", "TEXT")


def _create_pricing_tables(c):
    """创建pricing和pricing_history表"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS pricing (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            edition TEXT NOT NULL,
            price_model TEXT,
            price_amount REAL,
            price_currency TEXT,
            trial_limits TEXT,
            pro_features TEXT,
            effective_date TEXT NOT NULL,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS pricing_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL,
            platform TEXT,
            old_price REAL,
            new_price REAL,
            old_model TEXT,
            new_model TEXT,
            changed_at TEXT NOT NULL,
            changed_by TEXT,
            change_reason TEXT
        )
    """)


def _create_sources_table(c):
    """创建sources表并执行列迁移和索引"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT NOT NULL,
            source_name TEXT,
            source_url TEXT,
            source_author TEXT,
            source_license TEXT,
            source_version TEXT,
            download_date TEXT,
            original_slug TEXT,
            notes TEXT,
            skill_id INTEGER,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)
    _add_column_if_missing(c, "sources", "skill_id", "INTEGER")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sources_skill ON sources(skill_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sources_original_slug ON sources(original_slug)")


def _create_dependencies_table(c):
    """创建dependencies依赖关系表"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS dependencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            depends_on_skill_id INTEGER,
            depends_on_external TEXT,
            dependency_type TEXT,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)


def _create_scores_table(c):
    """创建scores评分表并执行列迁移和索引"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            scored_at TEXT NOT NULL,
            score_type TEXT NOT NULL,
            quality_score INTEGER NOT NULL DEFAULT 0,
            practicality_score INTEGER NOT NULL DEFAULT 0,
            simplicity_score INTEGER NOT NULL DEFAULT 0,
            cost_score INTEGER NOT NULL DEFAULT 0,
            performance_score INTEGER NOT NULL DEFAULT 0,
            debranding_score INTEGER NOT NULL DEFAULT 0,
            compliance_score INTEGER NOT NULL DEFAULT 0,
            differentiation_score INTEGER NOT NULL DEFAULT 0,
            total_score INTEGER NOT NULL DEFAULT 0,
            pass_threshold INTEGER NOT NULL DEFAULT 40,
            is_pass INTEGER NOT NULL DEFAULT 0,
            reviewer TEXT,
            notes TEXT,
            is_current INTEGER DEFAULT 1,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)
    _add_column_if_missing(c, "scores", "is_current", "INTEGER DEFAULT 1")
    c.execute("CREATE INDEX IF NOT EXISTS idx_scores_current ON scores(skill_id, score_type, is_current)")


def _create_workflow_states_table(c):
    """创建workflow_states工作流状态表"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS workflow_states (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            step_number INTEGER NOT NULL,
            step_name TEXT NOT NULL,
            started_at TEXT,
            completed_at TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            result_data TEXT,
            retry_count INTEGER DEFAULT 0,
            notes TEXT,
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)


def _create_plug_members_table(c):
    """创建plug_members表 (V140 C1: Plug-成员关系跟踪)"""
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
    c.execute("""
        CREATE INDEX IF NOT EXISTS idx_plug_members_plug
        ON plug_members(plug_slug)
    """)
    c.execute("""
        CREATE INDEX IF NOT EXISTS idx_plug_members_member
        ON plug_members(member_slug)
    """)


def _create_upgrade_tracking_table(c):
    """创建upgrade_tracking表 (V141 D2: 替代JSON存储, SQLite权威源)"""
    c.execute("""
        CREATE TABLE IF NOT EXISTS upgrade_tracking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_id INTEGER NOT NULL,
            slug TEXT NOT NULL,
            source_version TEXT,
            local_version TEXT,
            content_hash TEXT,
            needs_upgrade INTEGER DEFAULT 0,
            upgrade_reason TEXT,
            last_checked TEXT,
            last_upgraded TEXT,
            FOREIGN KEY (skill_id) REFERENCES skills(id),
            UNIQUE(slug)
        )
    """)
    c.execute("""
        CREATE INDEX IF NOT EXISTS idx_upgrade_tracking_slug
        ON upgrade_tracking(slug)
    """)
    c.execute("""
        CREATE INDEX IF NOT EXISTS idx_upgrade_needs_upgrade
        ON upgrade_tracking(needs_upgrade)
    """)


def _create_fts_table(c):
    """创建skills_fts全文搜索虚拟表"""
    c.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS skills_fts USING fts5(
            slug, name, display_name, description, tags, category
        )
    """)


def _create_all_indexes(c):
    """创建所有索引"""
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_slug ON skills(slug)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_status ON skills(current_status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_source ON skills(source)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_category ON skills(category)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_versions_skill ON versions(skill_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_operations_skill ON operations(skill_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_uploads_skill ON platform_uploads(skill_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_uploads_platform ON platform_uploads(platform)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_scores_skill ON scores(skill_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_scores_pass ON scores(is_pass)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_workflow_skill ON workflow_states(skill_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_workflow_status ON workflow_states(status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_edition ON skills(edition)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_parent_slug ON skills(parent_slug)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_free_slug ON skills(free_slug)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_paid_slug ON skills(paid_slug)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_skillhub_sync ON skills(skillhub_sync_status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_clawhub_sync ON skills(clawhub_sync_status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_gh_public_sync ON skills(github_public_sync_status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_gh_private_sync ON skills(github_private_sync_status)")


def _create_views(c):
    """创建v_skill_lifecycle和v_three_track_overview视图"""
    c.execute("DROP VIEW IF EXISTS v_skill_lifecycle")
    c.execute("""
        CREATE VIEW v_skill_lifecycle AS
        WITH latest_uploads AS (
            SELECT
                skill_id, platform, upload_status, visibility,
                ROW_NUMBER() OVER (PARTITION BY skill_id, platform ORDER BY upload_date DESC) as rn
            FROM platform_uploads
        )
        SELECT
            s.slug,
            s.current_display_name as display_name,
            s.skill_type,
            s.source_slug,
            s.free_slug,
            s.paid_slug,
            s.current_version as version,
            s.current_status as status,
            s.pricing_tier,
            s.edition,
            s.is_paid,
            s.category,
            s.source,
            s.skillhub_sync_status,
            s.clawhub_sync_status,
            s.github_public_sync_status,
            s.github_private_sync_status,
            s.last_sync_at,
            sh.upload_status as skillhub_upload_status,
            ch.upload_status as clawhub_upload_status,
            gh_pub.upload_status as github_public_upload_status,
            gh_pri.upload_status as github_private_upload_status,
            s.updated_at as last_updated
        FROM skills s
        LEFT JOIN latest_uploads sh ON sh.skill_id = s.id AND sh.platform = 'skillhub' AND sh.rn = 1
        LEFT JOIN latest_uploads ch ON ch.skill_id = s.id AND ch.platform = 'clawhub' AND ch.rn = 1
        LEFT JOIN latest_uploads gh_pub ON gh_pub.skill_id = s.id AND gh.platform = 'github_public' AND gh.rn = 1
        LEFT JOIN latest_uploads gh_pri ON gh_pri.skill_id = s.id AND gh_pri.platform = 'github_private' AND gh_pri.rn = 1
        WHERE s.current_status IN ('synced_from_skillhub', 'local_only', 'deleted_on_skillhub', 'active', 'updated', 'stale')
    """)
    c.execute("DROP VIEW IF EXISTS v_three_track_overview")
    c.execute("""
        CREATE VIEW v_three_track_overview AS
        SELECT
            s.slug,
            s.current_display_name as display_name,
            s.category,
            s.pricing_tier,
            s.edition,
            s.is_paid,
            s.source_slug,
            s.free_slug,
            s.paid_slug,
            CASE
                WHEN s.skill_type = 'source' THEN '源skill'
                WHEN s.skill_type = 'free' THEN '免费版'
                WHEN s.skill_type = 'paid' THEN '付费版'
                WHEN s.skill_type = 'tool' THEN '工具'
                ELSE '未分类'
            END as track_name,
            s.current_status as status,
            s.updated_at as last_updated
        FROM skills s
        WHERE s.current_status IN ('synced_from_skillhub', 'local_only', 'deleted_on_skillhub', 'active', 'updated', 'stale')
        ORDER BY s.source_slug, s.skill_type
    """)


def init_database():
    """初始化数据库，创建所有表

    [V133 D2] 重构: 370行→~30行, 拆分为13个_helper函数(TD-244)
    """
    conn = _get_db_connection()
    c = conn.cursor()

    _create_schema_version_table(c)
    _create_skills_table(c)
    _create_versions_table(c)
    _create_operations_table(c)
    _create_platform_uploads_table(c)
    _create_pricing_tables(c)
    _create_sources_table(c)
    _create_dependencies_table(c)
    _create_scores_table(c)
    _create_workflow_states_table(c)
    _create_plug_members_table(c)
    _create_upgrade_tracking_table(c)
    _create_fts_table(c)
    _create_all_indexes(c)
    _create_views(c)

    # D3: 回填 sources.skill_id
    backfill_source_skill_id(c)

    conn.commit()
    conn.close()
    print(f"Database initialized: {DB_PATH}")


def backfill_source_skill_id(c):
    """D3修复: 回填 sources.skill_id

    将 sources 表中 skill_id 为 NULL 的记录，通过 original_slug 关联到 skills 表。
    匹配策略（按优先级）:
      1. skills.source_slug = sources.original_slug
      2. skills.slug = sources.original_slug (直接匹配)
      3. skills.slug = sources.original_slug + '-free' (免费版)
      4. skills.slug = sources.original_slug + '-pro' (付费版)

    使用 UPDATE 而非 DELETE+INSERT，保护历史数据。
    """
    c.execute("""
        UPDATE sources
        SET skill_id = (
            SELECT s.id FROM skills s
            WHERE s.source_slug = sources.original_slug
            LIMIT 1
        )
        WHERE skill_id IS NULL
        AND EXISTS (
            SELECT 1 FROM skills s WHERE s.source_slug = sources.original_slug
        )
    """)
    matched_source_slug = c.rowcount

    c.execute("""
        UPDATE sources
        SET skill_id = (
            SELECT s.id FROM skills s
            WHERE s.slug = sources.original_slug
            LIMIT 1
        )
        WHERE skill_id IS NULL
        AND EXISTS (
            SELECT 1 FROM skills s WHERE s.slug = sources.original_slug
        )
    """)
    matched_slug = c.rowcount

    c.execute("""
        UPDATE sources
        SET skill_id = (
            SELECT s.id FROM skills s
            WHERE s.slug = sources.original_slug || '-free'
            LIMIT 1
        )
        WHERE skill_id IS NULL
        AND EXISTS (
            SELECT 1 FROM skills s WHERE s.slug = sources.original_slug || '-free'
        )
    """)
    matched_free = c.rowcount

    c.execute("""
        UPDATE sources
        SET skill_id = (
            SELECT s.id FROM skills s
            WHERE s.slug = sources.original_slug || '-pro'
            LIMIT 1
        )
        WHERE skill_id IS NULL
        AND EXISTS (
            SELECT 1 FROM skills s WHERE s.slug = sources.original_slug || '-pro'
        )
    """)
    matched_pro = c.rowcount

    total_matched = matched_source_slug + matched_slug + matched_free + matched_pro

    # 第5级匹配: "owner/repo"格式归一化 (awesome-list/github-search源)
    # 将"owner/repo"转为kebab-case repo名后再匹配
    import re as _re
    c.execute("SELECT id, original_slug FROM sources WHERE skill_id IS NULL")
    unlinked = c.fetchall()
    matched_normalized = 0
    for source_id, original_slug in unlinked:
        if not original_slug or '/' not in original_slug:
            continue
        # 提取repo名并转kebab-case
        repo = original_slug.split('/')[-1]
        s = _re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', repo)
        s = s.replace('_', '-').lower()
        s = _re.sub(r'[^a-z0-9-]', '', s)
        s = _re.sub(r'-+', '-', s).strip('-')
        if not s:
            continue
        # 尝试匹配
        for candidate in [s, s + '-free', s + '-pro']:
            c.execute("SELECT id FROM skills WHERE slug = ? LIMIT 1", (candidate,))
            row = c.fetchone()
            if row:
                c.execute("UPDATE sources SET skill_id = ? WHERE id = ?", (row[0], source_id))
                matched_normalized += 1
                break

    total_matched += matched_normalized
    if total_matched > 0:
        print(f"  [backfill] sources.skill_id 回填 {total_matched} 条 (source_slug:{matched_source_slug} slug:{matched_slug} -free:{matched_free} -pro:{matched_pro} normalized:{matched_normalized})")


def compute_file_hash(file_path: Path) -> str:
    """计算文件SHA256 (V105 W2: 统一签名,其他文件import此实现)"""
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def parse_skill_md(skill_md_path):
    """解析SKILL.md的frontmatter (v1.3: 内部统一调用skill_core.parser.parse_frontmatter_from_file)

    返回: (metadata_dict, body_str)

    V128 Y3: 此函数与l2_capability_checker.parse_skill_md_content和
    skill_batch_upgrader_v2.parse_skill_md_tuple不是重复定义。
    三者均委托skill_core.parser,但签名/返回类型不同:
    - 本函数: 路径输入→(dict, body), 用于DB操作
    - parse_skill_md_content: 内容输入→Dict含chapters, 用于L2检查
    - parse_skill_md_tuple: 内容输入→(raw_str, body_str), 用于批量升级
    """
    from skill_core.parser import parse_frontmatter_from_file
    result = parse_frontmatter_from_file(Path(skill_md_path))
    return result['fields'], result['body']


def register_skill(slug, name, display_name, version, category, source, local_path,
                   source_slug=None, source_url=None, source_author=None,
                   source_license=None, skill_type=None, pricing_model=None,
                   is_differentiated=0, notes=None, edition=None, parent_slug=None,
                   content_hash=None, workflow_state=None):
    """注册或更新一个skill

    v1.1新增参数：
        edition: 版本类型 'free' 或 'pro'
        parent_slug: 关联的父skill slug（免费版和专业版共享）
    v1.2新增参数：
        workflow_state: 工作流状态 (默认'step1_read_original')
                       可选值: step1_read_original...completed, deprecated
    v1.3新增参数：
        content_hash: SKILL.md内容的SHA-256哈希(前16位)，用于内容去重
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)

    now = datetime.now().isoformat()
    wf_state = workflow_state or 'step1_read_original'
    # v1.3: pricing_model默认为'per_call' (防止NULL值)
    if pricing_model is None:
        pricing_model = 'per_call'

    # 检查是否已存在
    c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
    existing = c.fetchone()

    if existing:
        skill_id = existing[0]
        c.execute("""
            UPDATE skills SET
                current_name = ?, current_display_name = ?, current_version = ?,
                category = ?, source = ?, local_path = ?,
                source_slug = ?, source_url = ?, source_author = ?, source_license = ?,
                skill_type = ?, pricing_model = ?, is_differentiated = ?,
                edition = ?, parent_slug = ?,
                content_hash = ?,
                workflow_state = ?,
                updated_at = ?, notes = ?
            WHERE id = ?
        """, (name, display_name, version, category, source, local_path,
              source_slug, source_url, source_author, source_license,
              skill_type, pricing_model, is_differentiated,
              edition, parent_slug, content_hash, wf_state, now, notes, skill_id))
    else:
        c.execute("""
            INSERT INTO skills (
                slug, current_name, current_display_name, current_version,
                category, source, source_slug, source_url, source_author, source_license,
                local_path, created_at, updated_at, current_status,
                is_differentiated, pricing_model, skill_type, notes,
                edition, parent_slug, content_hash, workflow_state
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (slug, name, display_name, version, category, source,
              source_slug, source_url, source_author, source_license,
              local_path, now, now, 'registered', is_differentiated,
              pricing_model, skill_type, notes, edition, parent_slug, content_hash, wf_state))
        skill_id = c.lastrowid

    # 记录版本
    c.execute("""
        INSERT INTO versions (skill_id, version, created_at, changelog)
        VALUES (?, ?, ?, ?)
    """, (skill_id, version, now, f"Registered skill {slug} v{version}"))

    # 记录操作
    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (skill_id, 'register', now, 'system', f'Registered {slug} v{version} (edition={edition})', 'registered'))

    conn.commit()
    conn.close()
    return skill_id


def record_score(skill_id, score_type, quality, practicality, simplicity, cost,
                 performance, debranding, compliance, differentiation,
                 reviewer='system', notes=None):
    """记录八大维度评分（v1.3: 改为save_score的兼容wrapper）

    保留向后兼容: 内部调用save_score, 补充is_current历史保护。
    新代码应直接调用save_score()。

    参数：
        skill_id: skill ID
        score_type: 'baseline'（改造前基线）或 'final'（改造后最终）
        quality..differentiation: 八大维度分数（0-6分）
    """
    total = quality + practicality + simplicity + cost + performance + debranding + compliance + differentiation
    return save_score(
        skill_id=skill_id,
        score_type=score_type,
        total_score=total,
        quality=quality, practicality=practicality, simplicity=simplicity,
        cost=cost, performance=performance, debranding=debranding,
        compliance=compliance, differentiation=differentiation,
        reviewer=reviewer, notes=notes,
    )


def save_score(skill_id, score_type, total_score,
               quality=0, practicality=0, simplicity=0,
               performance=0, debranding=0, differentiation=0,
               compliance=0, cost=0,
               reviewer='system', notes=None, is_pass=None,
               pass_threshold=40, grade=None):
    """保存评分记录（支持is_current历史保护机制）

    D5修复延续: 标记同类型旧记录为is_current=0，插入新记录is_current=1。
    替代: 各模块中的 UPDATE scores SET is_current=0 + INSERT INTO scores 裸SQL。

    V153 R1修复: 新增grade参数, 支持持久化评分等级(A/B/C/D)到skills表。

    参数：
        skill_id: skill ID
        score_type: 评分类型 ('trace_llm', 'agent_trial', 'baseline', 'final' 等)
        total_score: 总分
        quality..cost: 八大维度分数
        reviewer: 评分者标识
        notes: 评分备注（JSON字符串或普通文本）
        is_pass: 是否通过（None则自动按pass_threshold判定）
        pass_threshold: 通过阈值（默认40）
        grade: 评分等级(A/B/C/D), 提供时写入skills表grade列
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)

    now = datetime.now().isoformat()

    # 标记同类型旧记录为非当前
    c.execute(
        "UPDATE scores SET is_current = 0 WHERE skill_id = ? AND score_type = ? AND is_current = 1",
        (skill_id, score_type)
    )

    # 自动判定是否通过
    if is_pass is None:
        is_pass = 1 if total_score >= pass_threshold else 0

    # 插入新记录，is_current=1
    c.execute("""
        INSERT INTO scores (skill_id, score_type, total_score,
            quality_score, practicality_score, simplicity_score,
            performance_score, debranding_score, differentiation_score,
            compliance_score, cost_score, scored_at, reviewer, notes, is_pass, pass_threshold, is_current)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
    """, (skill_id, score_type, total_score,
          quality, practicality, simplicity,
          performance, debranding, differentiation,
          compliance, cost,
          now, reviewer, notes, is_pass, pass_threshold))

    # 更新skills表的current_score
    c.execute("UPDATE skills SET current_score = ?, updated_at = ? WHERE id = ?",
              (total_score, now, skill_id))

    # V153 R1: 持久化grade到skills表(如果调用方提供了grade)
    # 自动检查skills表是否有grade列, 缺失则ALTER TABLE添加(fail-safe)
    if grade is not None:
        c.execute("PRAGMA table_info(skills)")
        existing_columns = [row[1] for row in c.fetchall()]
        if 'grade' not in existing_columns:
            c.execute("ALTER TABLE skills ADD COLUMN grade TEXT")
        c.execute("UPDATE skills SET grade = ?, updated_at = ? WHERE id = ?",
                  (grade, now, skill_id))

    conn.commit()
    conn.close()
    return total_score, is_pass


def update_workflow_state(skill_id, step_number, step_name, status, result_data=None, notes=None):
    """更新10步工作流状态（v1.1新增，修复工作流无状态机问题）

    参数：
        skill_id: skill ID
        step_number: 步骤号 1-10
        step_name: 步骤名称
        status: 'pending', 'in_progress', 'completed', 'failed', 'retry'
        result_data: 步骤结果数据（JSON字符串）
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)

    now = datetime.now().isoformat()

    # 检查是否已有该步骤记录
    c.execute("SELECT id, retry_count FROM workflow_states WHERE skill_id = ? AND step_number = ?",
              (skill_id, step_number))
    existing = c.fetchone()

    if existing:
        record_id = existing[0]
        retry_count = existing[1] or 0
        if status == 'retry':
            retry_count += 1

        if status in ('in_progress',):
            c.execute("""
                UPDATE workflow_states SET started_at = ?, status = ?, notes = ?
                WHERE id = ?
            """, (now, status, notes, record_id))
        elif status in ('completed', 'failed', 'retry'):
            c.execute("""
                UPDATE workflow_states SET completed_at = ?, status = ?,
                result_data = ?, retry_count = ?, notes = ?
                WHERE id = ?
            """, (now, status, result_data, retry_count, notes, record_id))
    else:
        retry_count = 1 if status == 'retry' else 0
        c.execute("""
            INSERT INTO workflow_states (
                skill_id, step_number, step_name, started_at, completed_at,
                status, result_data, retry_count, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (skill_id, step_number, step_name,
              now if status == 'in_progress' else None,
              now if status in ('completed', 'failed', 'retry') else None,
              status, result_data, retry_count, notes))

    # 更新skills表的workflow_state
    c.execute("UPDATE skills SET workflow_state = ?, updated_at = ? WHERE id = ?",
              (f'step{step_number}_{step_name}', now, skill_id))

    conn.commit()
    conn.close()


# ============ v1.3: workflow_state标准化 ============

# 非标准workflow_state值 → 标准workflow_state值 映射表
_WORKFLOW_STATE_MAPPING = {
    'unknown': 'step1_read_original',          # 未开始
    'deleted_by_sync': 'deprecated',            # 已同步删除
    'local_file_missing_clawhub': 'step1_read_original',  # 需重新读取
    'uploaded_approved': 'step10_completed',    # 已上传已审核=完成
    'completed': 'step10_completed',            # 完成
    'quality_passed': 'step7_validate',        # 质检通过=验证完成
    'plug_registered': 'step6_phase_package',   # Plug已注册=包装完成
    'uploaded': 'step9_platform_upload',        # 已上传
}

# 标准workflow_state值集合
STANDARD_WORKFLOW_STATES = frozenset([
    'step1_read_original', 'step2_auto_differentiate', 'step3_auto_dedup',
    'step4_auto_price', 'step5_add_deps', 'step6_phase_package',
    'step7_validate', 'step8_optimize', 'step9_platform_upload',
    'step10_completed', 'deprecated',
])


def normalize_workflow_state(state: str) -> str:
    """将非标准workflow_state值映射为标准值 (v1.3新增)

    参数:
        state: 原始workflow_state值

    返回:
        标准化的workflow_state值 (如果已是标准值则原样返回)
    """
    if not state:
        return 'step1_read_original'
    if state in STANDARD_WORKFLOW_STATES:
        return state
    return _WORKFLOW_STATE_MAPPING.get(state, 'step1_read_original')


def backfill_workflow_states() -> dict:
    """批量回填非标准workflow_state值 (v1.3新增)

    将所有非标准workflow_state值映射为标准值。

    返回:
        {'total_updated': int, 'details': {old_state: count, ...}}
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()

    # 查询非标准值
    c.execute("SELECT workflow_state, COUNT(*) FROM skills GROUP BY workflow_state")
    state_counts = {row[0]: row[1] for row in c.fetchall()}

    details = {}
    total_updated = 0

    for old_state, count in state_counts.items():
        new_state = normalize_workflow_state(old_state)
        if new_state != old_state:
            c.execute(
                "UPDATE skills SET workflow_state = ?, updated_at = ? WHERE workflow_state = ?",
                (new_state, datetime.now().isoformat(), old_state)
            )
            details[old_state] = {'new_state': new_state, 'count': count}
            total_updated += count

    conn.commit()
    conn.close()

    return {'total_updated': total_updated, 'details': details}


def record_upload(skill_id, version, platform, platform_slug, upload_status,
                  http_status=None, error_message=None, visibility=None,
                  pricing_on_platform=None, community_published=0,
                  download_ready=None):
    """记录上传到平台

    v1.3新增参数：
        community_published: 是否已发布到社区 (0=未发布, 1=已发布, 默认0)
        download_ready: 下载就绪时间戳 (ISO格式字符串, None表示尚未就绪)
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO platform_uploads (
            skill_id, version, platform, platform_slug, upload_date,
            upload_status, http_status, error_message, visibility, pricing_on_platform,
            community_published, download_ready
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, version, platform, platform_slug, now, upload_status,
          http_status, error_message, visibility, pricing_on_platform,
          community_published, download_ready))

    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (skill_id, f'upload_{platform}', now, 'system',
          f'Uploaded {version} to {platform}: {upload_status}', upload_status))

    conn.commit()
    conn.close()


def record_source(source_type, source_name, source_url, source_author,
                   source_license, source_version, original_slug, notes, skill_id=None):
    """记录技能来源信息到sources表

    参数：
        source_type: 来源类型（如 'github', 'clawhub', 'original'）
        source_name: 来源名称
        source_url: 来源URL
        source_author: 来源作者
        source_license: 来源许可证
        source_version: 来源版本
        original_slug: 原始slug
        notes: 备注（JSON字符串或文本）
        skill_id: 关联的skill ID（可选，D3修复后支持外键关联）
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO sources (
            source_type, source_name, source_url, source_author,
            source_license, source_version, download_date, original_slug, notes, skill_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (source_type, source_name, source_url, source_author,
          source_license, source_version, now, original_slug, notes, skill_id))

    conn.commit()
    conn.close()


def record_operation(skill_id, operation_type, details, before_state=None, after_state=None,
                     operator='system'):
    """记录操作

    参数：
        skill_id: skill ID
        operation_type: 操作类型（如 'register', 'import', 'version_sync', 'naming_governance'）
        details: 操作详情描述
        before_state: 操作前状态
        after_state: 操作后状态
        operator: 操作者标识（默认 'system'，多平台同步等场景可传 'version_sync_pipeline'）
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, before_state, after_state)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, operation_type, now, operator, details, before_state, after_state))

    conn.commit()
    conn.close()


def insert_skill(slug, name, display_name, version, category, source, local_path,
                 current_status='registered', source_slug=None, source_url=None,
                 source_author=None, source_license=None, skill_type=None,
                 pricing_model=None, is_differentiated=0, differentiation_date=None,
                 notes=None, edition=None, parent_slug=None,
                 content_hash=None, workflow_state=None):
    """仅插入skill记录（不含版本和操作记录）

    用于基线导入、自动差异化等需要单独控制版本记录内容（如content_hash）的场景。
    替代: INSERT INTO skills
    返回: skill_id

    v1.3新增参数：
        content_hash: SKILL.md内容的SHA-256哈希(前16位)，用于内容去重
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()
    wf_state = workflow_state or 'step1_read_original'
    # v1.3: pricing_model默认为'per_call' (防止NULL值)
    if pricing_model is None:
        pricing_model = 'per_call'
    c.execute("""
        INSERT INTO skills (
            slug, current_name, current_display_name, current_version,
            category, source, source_slug, source_url, source_author, source_license,
            local_path, created_at, updated_at, current_status,
            is_differentiated, differentiation_date, pricing_model, skill_type, notes,
            edition, parent_slug, content_hash, workflow_state
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (slug, name, display_name, version, category, source,
          source_slug, source_url, source_author, source_license,
          local_path, now, now, current_status,
          is_differentiated, differentiation_date, pricing_model, skill_type, notes,
          edition, parent_slug, content_hash, wf_state))
    conn.commit()
    skill_id = c.lastrowid
    conn.close()
    return skill_id


def add_version(skill_id, version, changelog=None, content_hash=None,
                file_size=None, line_count=None, changes_summary=None):
    """添加版本记录（含content_hash基线）

    用于基线导入、版本同步等需要记录content_hash的场景。
    替代: INSERT INTO versions
    返回: version_id
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()
    c.execute("""
        INSERT INTO versions (skill_id, version, created_at, changelog, content_hash,
                             file_size, line_count, changes_summary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, version, now, changelog, content_hash, file_size, line_count, changes_summary))
    conn.commit()
    version_id = c.lastrowid
    conn.close()
    return version_id


def update_version_hash(version_id, content_hash):
    """更新版本记录的content_hash

    用于回填hash基线（update_baseline_hashes场景）。
    替代: UPDATE versions SET content_hash WHERE id = ?
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    c.execute("UPDATE versions SET content_hash = ? WHERE id = ?",
              (content_hash, version_id))
    conn.commit()
    conn.close()


# update_skill_fields 允许更新的字段白名单
_SKILL_FIELD_WHITELIST = frozenset({
    'slug', 'current_name', 'current_display_name', 'current_version',
    'category', 'source', 'source_slug', 'source_url', 'source_author',
    'source_license', 'local_path', 'current_status', 'is_differentiated',
    'differentiation_date', 'pricing_model', 'skill_type', 'notes',
    'edition', 'parent_slug', 'workflow_state', 'pricing_category',
    'pricing_rationale', 'pricing_tier', 'is_paid', 'suggested_price',
    'content_hash',  # v1.3: 内容指纹(用于防重复内容检测)
    'simhash',  # v1.3: SimHash指纹(内容近似去重)
    # v1.6: 本地LLM质量评分字段 (T1-005)
    'local_quality_score', 'local_score_feedback', 'local_score_at',
})


def update_skill_fields(skill_id, **fields):
    """更新skill的指定字段

    用于命名治理、版本同步、自动差异化等需要部分更新skill记录的场景。
    替代: UPDATE skills SET ... WHERE id = ?
    仅允许更新白名单字段（_SKILL_FIELD_WHITELIST），防止SQL注入。自动更新 updated_at。
    """
    updates = {k: v for k, v in fields.items() if k in _SKILL_FIELD_WHITELIST}
    if not updates:
        return
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()
    updates['updated_at'] = now
    set_clause = ', '.join(f'{k} = ?' for k in updates.keys())
    values = list(updates.values()) + [skill_id]
    c.execute(f"UPDATE skills SET {set_clause} WHERE id = ?", values)
    conn.commit()
    conn.close()


def record_platform_upload(skill_id, version, platform, platform_slug, upload_status,
                           http_status=None, error_message=None, visibility=None,
                           pricing_on_platform=None, operator='system',
                           operation_type=None, operation_details=None):
    """记录平台上传（可自定义操作者和操作类型）

    用于版本同步流水线等多平台同步场景，需要自定义操作记录中的operator和operation_type。
    替代: INSERT INTO platform_uploads + INSERT INTO operations

    V129 Z4 (TD-213): 本函数为【唯一 DB 写入实现】(canonical)。
    version_sync_pipeline.record_platform_upload 是对本函数的委托适配器(参数名映射 + 上下文注入),
    实际写入逻辑全部在此处, 不要在别处复制 DB 写入代码。
    """
    import time as _time
    for attempt in range(3):
        try:
            conn = _get_db_connection(timeout=30)
            c = conn.cursor()
            now = datetime.now().isoformat()
            c.execute("""
                INSERT INTO platform_uploads (
                    skill_id, version, platform, platform_slug, upload_date,
                    upload_status, http_status, error_message, visibility, pricing_on_platform,
                    community_published, download_ready
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (skill_id, version, platform, platform_slug, now, upload_status,
                  http_status, error_message, visibility, pricing_on_platform,
                  0, None))
            op_type = operation_type or f'upload_{platform}'
            op_details = operation_details or f'Uploaded {version} to {platform}: {upload_status}'
            c.execute("""
                INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (skill_id, op_type, now, operator, op_details, upload_status))
            conn.commit()
            conn.close()
            break
        except sqlite3.OperationalError as e:
            try:
                conn.close()
            except Exception as e:
                print(f"[WARN] 数据库连接关闭失败(不影响重试): {e}")
            if "locked" in str(e) and attempt < 2:
                _time.sleep(1)
                continue
            raise


def set_pricing(skill_id, edition, price_model, price_amount, price_currency,
                trial_limits, pro_features):
    """设置收费策略（新建记录）"""
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO pricing (skill_id, edition, price_model, price_amount, price_currency,
                            trial_limits, pro_features, effective_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, edition, price_model, price_amount, price_currency,
          trial_limits, pro_features, now))

    conn.commit()
    conn.close()


def update_pricing(skill_id, edition, price_model, price_amount, price_currency='CNY'):
    """更新收费策略（已存在记录）"""
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)

    c.execute("""
        UPDATE pricing
        SET edition = ?, price_model = ?, price_amount = ?, price_currency = ?
        WHERE skill_id = ?
    """, (edition, price_model, price_amount, price_currency, skill_id))

    conn.commit()
    conn.close()


def get_skill_status(slug):
    """获取skill状态"""
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    c = conn.cursor()

    c.execute("SELECT * FROM skills WHERE slug = ?", (slug,))
    skill = c.fetchone()

    if skill:
        skill_id = skill['id']
        c.execute("SELECT * FROM versions WHERE skill_id = ? ORDER BY created_at DESC", (skill_id,))
        versions = c.fetchall()

        c.execute("SELECT * FROM operations WHERE skill_id = ? ORDER BY operation_date DESC", (skill_id,))
        operations = c.fetchall()

        c.execute("SELECT * FROM platform_uploads WHERE skill_id = ? ORDER BY upload_date DESC", (skill_id,))
        uploads = c.fetchall()

        c.execute("SELECT * FROM pricing WHERE skill_id = ?", (skill_id,))
        pricing = c.fetchall()

        conn.close()
        return {
            'skill': dict(skill),
            'versions': [dict(v) for v in versions],
            'operations': [dict(o) for o in operations],
            'uploads': [dict(u) for u in uploads],
            'pricing': [dict(p) for p in pricing]
        }

    conn.close()
    return None


def list_all_skills():
    """列出所有skill"""
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    c = conn.cursor()

    c.execute("""
        SELECT s.*,
            (SELECT COUNT(*) FROM platform_uploads WHERE skill_id = s.id AND upload_status = 'success') as upload_count,
            (SELECT MAX(upload_date) FROM platform_uploads WHERE skill_id = s.id) as last_upload,
            (SELECT GROUP_CONCAT(DISTINCT platform) FROM platform_uploads WHERE skill_id = s.id AND upload_status = 'success') as platforms_uploaded
        FROM skills s
        ORDER BY s.category, s.slug
    """)

    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results


def get_skills_needing_work():
    """获取需要优化或上传的skill"""
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    c = conn.cursor()

    # 未差异化的
    c.execute("""
        SELECT * FROM skills
        WHERE is_differentiated = 0 OR current_status IN ('registered', 'pending_optimization')
        ORDER BY category, slug
    """)
    needs_optimization = [dict(r) for r in c.fetchall()]

    # 已优化但未上传到某平台的
    c.execute("""
        SELECT s.* FROM skills s
        WHERE s.is_differentiated = 1 AND s.current_status = 'optimized'
        AND s.id NOT IN (SELECT skill_id FROM platform_uploads WHERE upload_status = 'success')
        ORDER BY s.category, s.slug
    """)
    needs_upload = [dict(r) for r in c.fetchall()]

    conn.close()
    return {'needs_optimization': needs_optimization, 'needs_upload': needs_upload}


# ============================================================
# v1.5: 四平台同步机制函数 (P0-3b/c/d, P1-3)
# ============================================================

def _backfill_skillhub_status(c):
    """SkillHub同步状态回填 (阶段1+2+5) — 返回计数dict"""
    # ====== 阶段1: 从 platform_uploads 回填 skillhub_sync_status ======
    c.execute("""
        UPDATE skills SET skillhub_sync_status = CASE
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform = 'skillhub' AND upload_status = 'success'
            ) THEN 'synced'
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform = 'skillhub' AND upload_status = 'failed'
            ) THEN 'failed'
            WHEN skill_type = 'source' THEN 'not_applicable'
            ELSE 'unknown'
        END
    """)

    # ====== 阶段2: 从 upload_tracking.json 回填 skillhub ======
    # V95 V5: 统一入口, 委托daily_sync (消除直接json.load)
    from daily_sync import read_upload_tracking
    tracking = read_upload_tracking()
    json_synced_sh = 0

    if tracking:
        # JSON结构: {"metadata": {...}, "stats": {...}, "skills": {slug: {...}}, "last_updated": "..."}
        skills_data = tracking.get('skills', tracking)

        for slug, data in skills_data.items():
            if not isinstance(data, dict):
                continue
            if data.get('is_source'):
                continue

            c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
            row = c.fetchone()
            if not row:
                continue
            skill_id = row[0]

            # SkillHub: JSON中review_status=published/approved/public_published → synced
            sh = data.get('skillhub', {})
            sh_rs = sh.get('review_status', '')
            if sh_rs in ('published', 'approved', 'public_published'):
                c.execute("UPDATE skills SET skillhub_sync_status = 'synced' WHERE id = ? AND skillhub_sync_status = 'unknown'", (skill_id,))
                if c.rowcount > 0:
                    json_synced_sh += 1
            elif sh_rs == 'rejected':
                c.execute("UPDATE skills SET skillhub_sync_status = 'failed' WHERE id = ? AND skillhub_sync_status = 'unknown'", (skill_id,))
            elif sh_rs == 'deleted':
                c.execute("UPDATE skills SET skillhub_sync_status = 'not_applicable' WHERE id = ? AND skillhub_sync_status = 'unknown'", (skill_id,))

    # ====== 阶段5: SkillHub消缺 — 仅基于实际platform_uploads记录标记 (C3修复) ======
    # 之前基于目录路径(local_path LIKE '%packaged-skills%skillhub%')乐观假设已上传,
    # 导致912个无实际上传记录的skill被标记为synced, 扩大了check_banned_skills的误判范围。
    # 修复: 仅当platform_uploads表中存在success记录时才标记为synced
    c.execute("""
        UPDATE skills SET skillhub_sync_status = 'synced'
        WHERE skillhub_sync_status = 'unknown'
        AND EXISTS (
            SELECT 1 FROM platform_uploads
            WHERE skill_id = skills.id
            AND platform = 'skillhub'
            AND upload_status = 'success'
        )
    """)
    sh_synced_from_uploads = c.rowcount

    # 未有上传记录但本地文件存在的, 标记为pending_upload (需上传)
    c.execute("""
        UPDATE skills SET skillhub_sync_status = 'pending_upload'
        WHERE skillhub_sync_status = 'unknown'
        AND local_path IS NOT NULL AND local_path != ''
        AND (skill_type != 'source' OR skill_type IS NULL)
        AND NOT EXISTS (
            SELECT 1 FROM platform_uploads
            WHERE skill_id = skills.id
            AND platform = 'skillhub'
            AND upload_status = 'success'
        )
    """)
    sh_pending_count = c.rowcount

    return {'json_synced_sh': json_synced_sh}


def _backfill_clawhub_status(c):
    """ClawHub同步状态回填 (阶段1+2+6) — 返回计数dict"""
    # ====== 阶段1: 从 platform_uploads 回填 clawhub_sync_status ======
    c.execute("""
        UPDATE skills SET clawhub_sync_status = CASE
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform = 'clawhub' AND upload_status = 'success'
            ) THEN 'synced'
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform = 'clawhub' AND upload_status = 'failed'
            ) THEN 'failed'
            WHEN skill_type = 'source' THEN 'not_applicable'
            WHEN is_paid = 1 THEN 'not_applicable'
            ELSE 'unknown'
        END
    """)

    # ====== 阶段2: 从 upload_tracking.json 回填 clawhub ======
    # V95 V5: 统一入口, 委托daily_sync (消除直接json.load)
    from daily_sync import read_upload_tracking
    tracking = read_upload_tracking()
    json_synced_ch = 0

    if tracking:
        # JSON结构: {"metadata": {...}, "stats": {...}, "skills": {slug: {...}}, "last_updated": "..."}
        skills_data = tracking.get('skills', tracking)

        for slug, data in skills_data.items():
            if not isinstance(data, dict):
                continue
            if data.get('is_source'):
                continue

            c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
            row = c.fetchone()
            if not row:
                continue
            skill_id = row[0]

            # ClawHub: JSON中clawhub.status=published → synced
            ch = data.get('clawhub', {})
            ch_st = ch.get('status', '')
            if ch_st == 'published':
                c.execute("UPDATE skills SET clawhub_sync_status = 'synced' WHERE id = ? AND clawhub_sync_status = 'unknown'", (skill_id,))
                if c.rowcount > 0:
                    json_synced_ch += 1
            elif ch_st in ('withdrawn', 'not_eligible', 'not_applicable'):
                c.execute("UPDATE skills SET clawhub_sync_status = 'not_applicable' WHERE id = ? AND clawhub_sync_status = 'unknown'", (skill_id,))

    # ====== 阶段6: ClawHub消缺 — 未上传的free skill标记为pending ======
    # ClawHub只上传free skill，未上传的标记为pending(待上传)
    c.execute("""
        UPDATE skills SET clawhub_sync_status = 'pending'
        WHERE clawhub_sync_status = 'unknown'
        AND (skill_type != 'source' OR skill_type IS NULL)
        AND (is_paid = 0 OR is_paid IS NULL)
        AND local_path IS NOT NULL AND local_path != ''
    """)
    ch_pending_count = c.rowcount

    return {'json_synced_ch': json_synced_ch}


def _backfill_github_public_status(c):
    """GitHub公开同步状态回填 (阶段1+2+4) — 返回计数dict"""
    # ====== 阶段1: 从 platform_uploads 回填 github_public_sync_status (hermes-skills 公开引流) ======
    c.execute("""
        UPDATE skills SET github_public_sync_status = CASE
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform IN ('github_public', 'github') AND upload_status = 'success'
            ) THEN 'synced'
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform IN ('github_public', 'github') AND upload_status = 'failed'
            ) THEN 'failed'
            WHEN skill_type = 'source' THEN 'not_applicable'
            ELSE 'unknown'
        END
    """)

    # ====== 阶段2: 从 upload_tracking.json 回填 github_public ======
    # V95 V5: 统一入口, 委托daily_sync (消除直接json.load)
    from daily_sync import read_upload_tracking
    tracking = read_upload_tracking()
    json_synced_gh_pub = 0

    if tracking:
        # JSON结构: {"metadata": {...}, "stats": {...}, "skills": {slug: {...}}, "last_updated": "..."}
        skills_data = tracking.get('skills', tracking)

        for slug, data in skills_data.items():
            if not isinstance(data, dict):
                continue
            if data.get('is_source'):
                continue

            c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
            row = c.fetchone()
            if not row:
                continue
            skill_id = row[0]

            # GitHub公开: JSON中hermes.github_published=true → synced
            hermes = data.get('hermes', {})
            if hermes.get('github_published'):
                c.execute("UPDATE skills SET github_public_sync_status = 'synced' WHERE id = ? AND github_public_sync_status = 'unknown'", (skill_id,))
                if c.rowcount > 0:
                    json_synced_gh_pub += 1

    # ====== 阶段4: GitHub公开消缺 — 所有非source skill都在hermes-skills仓库中 ======
    # hermes-skills推送所有skill(免费+付费)，因此所有非source skill的
    # github_public_sync_status也应该是synced (与github_private相同逻辑)
    c.execute("""
        UPDATE skills SET github_public_sync_status = 'synced'
        WHERE github_public_sync_status = 'unknown'
        AND (skill_type != 'source' OR skill_type IS NULL)
        AND local_path IS NOT NULL AND local_path != ''
    """)
    gh_public_synced_from_local = c.rowcount

    return {'json_synced_gh_pub': json_synced_gh_pub}


def _backfill_github_private_status(c):
    """GitHub私有同步状态回填 (阶段1+3) — 返回计数dict"""
    # ====== 阶段1: 从 platform_uploads 回填 github_private_sync_status (origin 私有备份) ======
    c.execute("""
        UPDATE skills SET github_private_sync_status = CASE
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform = 'github_private' AND upload_status = 'success'
            ) THEN 'synced'
            WHEN EXISTS(
                SELECT 1 FROM platform_uploads
                WHERE skill_id = skills.id AND platform = 'github_private' AND upload_status = 'failed'
            ) THEN 'failed'
            WHEN skill_type = 'source' THEN 'not_applicable'
            ELSE 'unknown'
        END
    """)

    # ====== 阶段3: GitHub私有消缺 — 所有非source skill都在origin仓库中 ======
    # origin仓库是项目主仓库，所有skill文件都push到origin
    # 因此所有非source skill的github_private_sync_status应该是synced
    c.execute("""
        UPDATE skills SET github_private_sync_status = 'synced'
        WHERE github_private_sync_status = 'unknown'
        AND (skill_type != 'source' OR skill_type IS NULL)
        AND local_path IS NOT NULL AND local_path != ''
    """)
    gh_private_synced = c.rowcount

    return {'gh_private_synced': gh_private_synced}


def _backfill_source_skill_cleanup(c):
    """源skill目录+源skill全平台消缺 (阶段6b + source cleanup) — 返回计数dict"""
    # ====== 阶段6b: 源skill目录消缺 — clawhub-skills/downloaded/中的是源skill ======
    # local_path在clawhub-skills/downloaded/目录下的skill是源skill(从ClawHub下载)
    # 即使skill_type不是'source'，也应标记为not_applicable
    c.execute("""
        UPDATE skills SET
            skillhub_sync_status = 'not_applicable',
            clawhub_sync_status = 'not_applicable',
            github_public_sync_status = 'not_applicable',
            github_private_sync_status = 'not_applicable'
        WHERE (skillhub_sync_status = 'unknown' OR clawhub_sync_status = 'unknown'
             OR github_public_sync_status = 'unknown' OR github_private_sync_status = 'unknown')
        AND local_path LIKE '%clawhub-skills%downloaded%'
    """)
    source_dir_na = c.rowcount

    # 对于source skill，确保所有平台都是not_applicable
    c.execute("""
        UPDATE skills SET
            skillhub_sync_status = 'not_applicable',
            clawhub_sync_status = 'not_applicable',
            github_public_sync_status = 'not_applicable',
            github_private_sync_status = 'not_applicable'
        WHERE skill_type = 'source'
        AND (skillhub_sync_status = 'unknown' OR clawhub_sync_status = 'unknown'
             OR github_public_sync_status = 'unknown' OR github_private_sync_status = 'unknown')
    """)
    source_na = c.rowcount

    return {'source_dir_na': source_dir_na, 'source_na': source_na}


def backfill_sync_status():
    """P0-3b + P0-4: 从 platform_uploads + upload_tracking.json 回填四平台同步状态 [V134 E5]

    两阶段回填:
    阶段1 (P0-3b): 从 platform_uploads 表回填 (已有逻辑)
    阶段2 (P0-4): 从 upload_tracking.json 直接回填 sync_status (消除unknown)

    幂等操作：可重复执行，每次都基于最新数据重新计算。
    同步状态值: synced / failed / not_applicable / unknown

    [V134 E5] 拆分为5个helper函数 + 主函数:
      _backfill_skillhub_status / _backfill_clawhub_status
      _backfill_github_public_status / _backfill_github_private_status
      _backfill_source_skill_cleanup
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    now = datetime.now().isoformat()

    # ====== 调用5个平台helper ======
    sh_counts = _backfill_skillhub_status(c)
    ch_counts = _backfill_clawhub_status(c)
    gh_pub_counts = _backfill_github_public_status(c)
    gh_pri_counts = _backfill_github_private_status(c)
    src_counts = _backfill_source_skill_cleanup(c)

    # 更新 last_sync_at
    c.execute("""
        UPDATE skills SET last_sync_at = ?
        WHERE EXISTS(SELECT 1 FROM platform_uploads WHERE skill_id = skills.id)
    """, (now,))

    # 统计结果
    c.execute("""
        SELECT
            SUM(CASE WHEN skillhub_sync_status = 'synced' THEN 1 ELSE 0 END) as sh_synced,
            SUM(CASE WHEN skillhub_sync_status = 'unknown' THEN 1 ELSE 0 END) as sh_unknown,
            SUM(CASE WHEN clawhub_sync_status = 'synced' THEN 1 ELSE 0 END) as ch_synced,
            SUM(CASE WHEN clawhub_sync_status = 'unknown' THEN 1 ELSE 0 END) as ch_unknown,
            SUM(CASE WHEN github_public_sync_status = 'synced' THEN 1 ELSE 0 END) as gh_pub_synced,
            SUM(CASE WHEN github_public_sync_status = 'unknown' THEN 1 ELSE 0 END) as gh_pub_unknown,
            SUM(CASE WHEN github_private_sync_status = 'synced' THEN 1 ELSE 0 END) as gh_pri_synced,
            SUM(CASE WHEN github_private_sync_status = 'unknown' THEN 1 ELSE 0 END) as gh_pri_unknown
        FROM skills
    """)
    row = c.fetchone()
    conn.commit()
    conn.close()

    result = {
        'skillhub_synced': row[0],
        'skillhub_unknown': row[1],
        'clawhub_synced': row[2],
        'clawhub_unknown': row[3],
        'github_public_synced': row[4],
        'github_public_unknown': row[5],
        'github_private_synced': row[6],
        'github_private_unknown': row[7],
        'json_synced_sh': sh_counts['json_synced_sh'],
        'json_synced_ch': ch_counts['json_synced_ch'],
        'json_synced_gh_pub': gh_pub_counts['json_synced_gh_pub'],
        'gh_private_synced': gh_pri_counts['gh_private_synced'],
        'source_na': src_counts['source_na'],
        'source_dir_na': src_counts['source_dir_na'],
    }
    print(f"backfill_sync_status 完成: {result}")
    return result


def migrate_github_to_dual_repo():
    """P0-3c: 迁移 platform_uploads 中的 github 记录为 github_public

    历史记录使用 'github' 值，现在需要区分 github_public (hermes-skills公开) 和 github_private (origin私有)。
    所有历史 'github' 记录均为 hermes-skills 公开仓库推送，因此迁移为 'github_public'。

    幂等操作：仅更新 platform='github' 的记录，已迁移的记录不受影响。
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)

    # 统计迁移前
    c.execute("SELECT COUNT(*) FROM platform_uploads WHERE platform = 'github'")
    before_count = c.fetchone()[0]

    if before_count == 0:
        conn.close()
        print("migrate_github_to_dual_repo: 无需迁移 (已无 'github' 记录)")
        return {'migrated': 0, 'already_done': True}

    # 执行迁移
    c.execute("""
        UPDATE platform_uploads SET platform = 'github_public'
        WHERE platform = 'github'
    """)
    migrated = c.rowcount

    # 统计迁移后
    c.execute("SELECT platform, COUNT(*) FROM platform_uploads GROUP BY platform ORDER BY platform")
    after_dist = {row[0]: row[1] for row in c.fetchall()}

    conn.commit()
    conn.close()

    result = {'migrated': migrated, 'after_distribution': after_dist}
    print(f"migrate_github_to_dual_repo 完成: 迁移 {migrated} 条记录, 平台分布: {after_dist}")
    return result


def sync_hermes_from_json():
    """P0-3d: 从 upload_tracking.json 同步 hermes (GitHub公开) 状态到 DB

    upload_tracking.json 中每个 skill 的 'hermes' 对象包含:
    - github_published: 是否已推送到 hermes-skills 仓库
    - github_repo: 仓库URL
    - github_pushed_at: 推送时间

    将这些状态同步到 platform_uploads 表（platform='github_public'），
    消除双数据源不一致问题。

    幂等操作：先检查是否已有记录，避免重复插入。
    """
    # V95 V5: 统一入口, 委托daily_sync (消除直接json.load)
    from daily_sync import read_upload_tracking
    tracking = read_upload_tracking()
    if not tracking or not tracking.get('skills'):
        print(f"sync_hermes_from_json: upload_tracking.json为空或不存在")
        return {'synced': 0, 'error': 'json_not_found'}

    # JSON结构: {"metadata": {...}, "stats": {...}, "skills": {slug: {...}}, "last_updated": "..."}
    skills_data = tracking.get('skills', tracking)

    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)

    synced_count = 0
    skipped_count = 0
    now = datetime.now().isoformat()

    for slug, data in skills_data.items():
        if not isinstance(data, dict):
            continue

        # 获取 skill_id
        c.execute("SELECT id, current_version FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        if not row:
            skipped_count += 1
            continue
        skill_id, version = row

        # 检查 hermes 数据
        hermes = data.get('hermes', {})
        if not hermes:
            skipped_count += 1
            continue

        github_published = hermes.get('github_published', False)
        github_pushed_at = hermes.get('github_pushed_at')

        if not github_published:
            skipped_count += 1
            continue

        # 检查是否已有 github_public 记录（幂等）
        c.execute("""
            SELECT id FROM platform_uploads
            WHERE skill_id = ? AND platform = 'github_public' AND upload_status = 'success'
        """, (skill_id,))
        existing = c.fetchone()

        if existing:
            skipped_count += 1
            continue

        # 插入 github_public 记录
        upload_date = github_pushed_at or hermes.get('converted_at') or now
        c.execute("""
            INSERT INTO platform_uploads (
                skill_id, version, platform, platform_slug, upload_date,
                upload_status, http_status, error_message, visibility, pricing_on_platform,
                community_published, download_ready
            ) VALUES (?, ?, 'github_public', ?, ?, 'success', 200, NULL, 'public', NULL, 0, NULL)
        """, (skill_id, version or '1.0.0', slug, upload_date))

        # 记录操作
        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
            VALUES (?, 'sync_hermes_from_json', ?, 'system', ?, 'success')
        """, (skill_id, now, f'Synced hermes status from JSON: github_published=True'))

        synced_count += 1

    conn.commit()
    conn.close()

    result = {'synced': synced_count, 'skipped': skipped_count}
    print(f"sync_hermes_from_json 完成: 同步 {synced_count} 条, 跳过 {skipped_count} 条")
    return result


def backfill_three_track_association():
    """P1-3: 回填 free_slug / paid_slug 三轨关联字段

    策略:
    1. 付费版 skill (edition in pro/paid): 通过 parent_slug 或命名规则找到对应免费版
    2. 免费版 skill (edition=free): 通过 pair_slug (JSON) 或命名规则找到对应付费版
    3. 源 skill: 不需要关联

    命名规则:
    - 免费版: {base_slug}-free 或 {base_slug}
    - 付费版: {base_slug}-pro, {base_slug}-paid, 或 {base_slug}

    幂等操作：仅更新 free_slug/paid_slug 为 NULL 的记录。
    """
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    c = conn.cursor()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)

    # 1. 通过 parent_slug 回填
    # 付费版 → 免费版: free_slug = parent_slug (如果 parent_slug 指向一个免费版)
    c.execute("""
        UPDATE skills SET free_slug = parent_slug
        WHERE free_slug IS NULL
        AND parent_slug IS NOT NULL
        AND edition IN ('pro', 'paid')
        AND parent_slug IN (SELECT slug FROM skills WHERE edition = 'free')
    """)
    free_via_parent = c.rowcount

    # 免费版 → 付费版: paid_slug = parent_slug (如果 parent_slug 指向一个付费版)
    c.execute("""
        UPDATE skills SET paid_slug = parent_slug
        WHERE paid_slug IS NULL
        AND parent_slug IS NOT NULL
        AND edition = 'free'
        AND parent_slug IN (SELECT slug FROM skills WHERE edition IN ('pro', 'paid'))
    """)
    paid_via_parent = c.rowcount

    # 2. 反向回填: 如果 A.free_slug = B, 则 B.paid_slug = A
    c.execute("""
        UPDATE skills SET paid_slug = (
            SELECT s2.slug FROM skills s2
            WHERE s2.free_slug = skills.slug AND s2.free_slug IS NOT NULL
            LIMIT 1
        )
        WHERE paid_slug IS NULL
        AND EXISTS (
            SELECT 1 FROM skills s2 WHERE s2.free_slug = skills.slug AND s2.free_slug IS NOT NULL
        )
    """)
    paid_via_reverse = c.rowcount

    # 3. 反向回填: 如果 A.paid_slug = B, 则 B.free_slug = A
    c.execute("""
        UPDATE skills SET free_slug = (
            SELECT s2.slug FROM skills s2
            WHERE s2.paid_slug = skills.slug AND s2.paid_slug IS NOT NULL
            LIMIT 1
        )
        WHERE free_slug IS NULL
        AND EXISTS (
            SELECT 1 FROM skills s2 WHERE s2.paid_slug = skills.slug AND s2.paid_slug IS NOT NULL
        )
    """)
    free_via_reverse = c.rowcount

    # 4. 命名规则回填: {base}-free → {base}-pro
    # 查找所有 -free 结尾的skill，尝试匹配 -pro 结尾的skill
    c.execute("""
        UPDATE skills SET paid_slug = REPLACE(slug, '-free', '-pro')
        WHERE paid_slug IS NULL
        AND slug LIKE '%-free'
        AND REPLACE(slug, '-free', '-pro') IN (SELECT slug FROM skills WHERE edition IN ('pro', 'paid'))
    """)
    paid_via_naming = c.rowcount

    # 反向: {base}-pro → {base}-free
    c.execute("""
        UPDATE skills SET free_slug = REPLACE(slug, '-pro', '-free')
        WHERE free_slug IS NULL
        AND slug LIKE '%-pro'
        AND REPLACE(slug, '-pro', '-free') IN (SELECT slug FROM skills WHERE edition = 'free')
    """)
    free_via_naming = c.rowcount

    # 5. 从 upload_tracking.json 的 pair_slug 回填
    # V95 V5: 统一入口, 委托daily_sync (消除直接json.load)
    from daily_sync import read_upload_tracking
    tracking = read_upload_tracking()
    json_synced = 0
    if tracking:
        # JSON结构: {"metadata": {...}, "stats": {...}, "skills": {slug: {...}}, "last_updated": "..."}
        skills_data = tracking.get('skills', tracking)

        for slug, data in skills_data.items():
            if not isinstance(data, dict):
                continue
            pair_slug = data.get('pair_slug')
            if not pair_slug:
                continue

            is_free = data.get('is_free', False)
            c.execute("SELECT id FROM skills WHERE slug = ? AND (free_slug IS NULL OR paid_slug IS NULL)", (slug,))
            row = c.fetchone()
            if not row:
                continue
            skill_id = row[0]

            if is_free:
                # 免费版 → 付费版
                c.execute("UPDATE skills SET paid_slug = ? WHERE id = ? AND paid_slug IS NULL", (pair_slug, skill_id))
            else:
                # 付费版 → 免费版
                c.execute("UPDATE skills SET free_slug = ? WHERE id = ? AND free_slug IS NULL", (pair_slug, skill_id))
            json_synced += c.rowcount

    # 统计结果
    c.execute("SELECT COUNT(*) FROM skills WHERE free_slug IS NOT NULL")
    free_total = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM skills WHERE paid_slug IS NOT NULL")
    paid_total = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM skills")
    total = c.fetchone()[0]

    conn.commit()
    conn.close()

    result = {
        'free_slug_filled': free_total,
        'paid_slug_filled': paid_total,
        'total': total,
        'free_pct': f"{free_total*100//total}%",
        'paid_pct': f"{paid_total*100//total}%",
    }
    print(f"backfill_three_track_association 完成: {result}")
    return result


def get_sync_status_summary():
    """查询四平台同步状态概览"""
    conn = _get_db_connection()  # V121 W1: sqlite3.connect→_get_db_connection()
    # V122 W1: 冗余PRAGMA已清理(_get_db_connection已设置)
    c = conn.cursor()

    c.execute("""
        SELECT
            skillhub_sync_status,
            clawhub_sync_status,
            github_public_sync_status,
            github_private_sync_status,
            COUNT(*) as count
        FROM skills
        GROUP BY skillhub_sync_status, clawhub_sync_status, github_public_sync_status, github_private_sync_status
        ORDER BY count DESC
        LIMIT 20
    """)
    rows = [dict(r) for r in c.fetchall()]

    c.execute("""
        SELECT
            SUM(CASE WHEN skillhub_sync_status = 'synced' THEN 1 ELSE 0 END) as sh,
            SUM(CASE WHEN clawhub_sync_status = 'synced' THEN 1 ELSE 0 END) as ch,
            SUM(CASE WHEN github_public_sync_status = 'synced' THEN 1 ELSE 0 END) as gh_pub,
            SUM(CASE WHEN github_private_sync_status = 'synced' THEN 1 ELSE 0 END) as gh_pri,
            COUNT(*) as total
        FROM skills
    """)
    summary = dict(c.fetchone())

    conn.close()
    return {'summary': summary, 'distribution': rows}


if __name__ == '__main__':
    init_database()
    migrate_schema()  # v1.3: 执行schema迁移检查
    print("Database schema created successfully.")
    print(f"Location: {DB_PATH}")
