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
except Exception:
    pass  # 数据库可能正在被其他进程初始化

# v2.4: 带重试的连接辅助函数 (强化已有流程,不创建碎片化代码)
def _get_db_connection(timeout=30):
    """创建带WAL+busy_timeout的数据库连接,解决并发锁问题"""
    conn = sqlite3.connect(DB_PATH, timeout=timeout)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA busy_timeout = 5000")
    return conn


def init_database():
    """初始化数据库，创建所有表"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 启用外键约束（v1.1修复：之前未启用）
    c.execute("PRAGMA foreign_keys = ON")

    # 1. skills 主表 - 每个skill一行
    # v1.1新增: edition, parent_slug, current_score, workflow_state 字段
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
            is_paid INTEGER DEFAULT 0
        )
    """)

    # 迁移：为已存在的数据库添加新列（如果不存在）
    try:
        c.execute("ALTER TABLE skills ADD COLUMN edition TEXT")
    except sqlite3.OperationalError:
        pass  # 列已存在
    try:
        c.execute("ALTER TABLE skills ADD COLUMN parent_slug TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN current_score INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN workflow_state TEXT DEFAULT 'step1_read_original'")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN suggested_price REAL")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN pricing_category TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN pricing_rationale TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN pricing_tier TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN is_paid INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        pass
    # v1.4: 三轨关联字段
    try:
        c.execute("ALTER TABLE skills ADD COLUMN summary TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN free_slug TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN paid_slug TEXT")
    except sqlite3.OperationalError:
        pass
    # v1.5: 四平台同步状态字段 (P0-3a)
    try:
        c.execute("ALTER TABLE skills ADD COLUMN skillhub_sync_status TEXT DEFAULT 'unknown'")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN clawhub_sync_status TEXT DEFAULT 'unknown'")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN github_public_sync_status TEXT DEFAULT 'unknown'")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN github_private_sync_status TEXT DEFAULT 'unknown'")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN last_sync_at TEXT")
    except sqlite3.OperationalError:
        pass

    # v1.6: 本地LLM质量评分字段 (T1-004)
    try:
        c.execute("ALTER TABLE skills ADD COLUMN local_quality_score REAL DEFAULT 0.0")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN local_score_feedback TEXT DEFAULT ''")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE skills ADD COLUMN local_score_at TEXT")
    except sqlite3.OperationalError:
        pass

    # 2. versions - 版本历史表
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

    # 3. operations - 操作历史表
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

    # 4. platform_uploads - 平台上传状态
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

    # 迁移：为已存在的 platform_uploads 表添加可见性追踪字段（v1.3新增）
    # community_published: 是否已发布到社区 (0=未发布, 1=已发布)
    # download_ready: 下载就绪时间戳 (ISO格式, NULL表示尚未就绪)
    try:
        c.execute("ALTER TABLE platform_uploads ADD COLUMN community_published INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        pass  # 列已存在
    try:
        c.execute("ALTER TABLE platform_uploads ADD COLUMN download_ready TEXT")
    except sqlite3.OperationalError:
        pass  # 列已存在

    # 5. pricing - 收费策略表
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

    # 6. sources - 来源信息表
    # D1+D3修复: 增加 skill_id 字段关联 skills 表，消除发现→入库数据断链
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

    # D3迁移: 为已存在的 sources 表添加 skill_id 列
    try:
        c.execute("ALTER TABLE sources ADD COLUMN skill_id INTEGER")
    except sqlite3.OperationalError:
        pass  # 列已存在

    # D3: 创建 sources.skill_id 索引
    c.execute("CREATE INDEX IF NOT EXISTS idx_sources_skill ON sources(skill_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sources_original_slug ON sources(original_slug)")

    # 7. dependencies - skill间依赖关系
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

    # 8. scores - 八大维度评分持久化（v1.1新增，修复评分无持久化问题）
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

    # D5迁移: 为已存在的 scores 表添加 is_current 列（保护评分历史）
    try:
        c.execute("ALTER TABLE scores ADD COLUMN is_current INTEGER DEFAULT 1")
    except sqlite3.OperationalError:
        pass  # 列已存在

    # D5: 创建 scores 历史索引（按 skill_id+score_type+is_current 查询最新评分）
    c.execute("CREATE INDEX IF NOT EXISTS idx_scores_current ON scores(skill_id, score_type, is_current)")

    # 9. workflow_states - 10步工作流状态追踪（v1.1新增，修复工作流无状态机问题）
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

    # 10. skills_fts - 全文搜索（虚拟表）
    c.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS skills_fts USING fts5(
            slug, name, display_name, description, tags, category
        )
    """)

    # 创建索引
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
    # v1.5: 四平台同步状态索引 (P0-3a)
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_skillhub_sync ON skills(skillhub_sync_status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_clawhub_sync ON skills(clawhub_sync_status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_gh_public_sync ON skills(github_public_sync_status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_gh_private_sync ON skills(github_private_sync_status)")

    # v1.5: 更新 v_skill_lifecycle 视图 (P0-3a — 修复WHERE子句+添加sync_status列)
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
        LEFT JOIN latest_uploads gh_pub ON gh_pub.skill_id = s.id AND gh_pub.platform = 'github_public' AND gh_pub.rn = 1
        LEFT JOIN latest_uploads gh_pri ON gh_pri.skill_id = s.id AND gh_pri.platform = 'github_private' AND gh_pri.rn = 1
        WHERE s.current_status IN ('synced_from_skillhub', 'local_only', 'deleted_on_skillhub', 'active', 'updated', 'stale')
    """)

    # v1.5: 更新 v_three_track_overview 视图 (修复WHERE子句)
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

    # D3: 回填 sources.skill_id（将已有发现记录关联到skills表）
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


def compute_file_hash(file_path):
    """计算文件SHA256"""
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def parse_skill_md(skill_md_path):
    """解析SKILL.md的frontmatter"""
    content = Path(skill_md_path).read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]

    if not content.startswith('---'):
        return None, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content

    frontmatter_text = parts[1].strip()
    body = parts[2].strip()

    metadata = {}
    current_key = None
    current_list = []

    for line in frontmatter_text.split('\n'):
        if line.startswith('  - '):
            if current_key:
                current_list.append(line[4:].strip())
            continue
        if line.startswith('  '):
            if current_key:
                if not isinstance(metadata.get(current_key), list):
                    metadata[current_key] = []
                metadata[current_key].append(line.strip())
            continue
        if ':' in line:
            if current_key and current_list:
                metadata[current_key] = current_list
                current_list = []
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val and val != '|-' and val != '|':
                metadata[key] = val
            else:
                current_key = key

    if current_key and current_list:
        metadata[current_key] = current_list

    return metadata, body


def register_skill(slug, name, display_name, version, category, source, local_path,
                   source_slug=None, source_url=None, source_author=None,
                   source_license=None, skill_type=None, pricing_model=None,
                   is_differentiated=0, notes=None, edition=None, parent_slug=None,
                   workflow_state=None):
    """注册或更新一个skill

    v1.1新增参数：
        edition: 版本类型 'free' 或 'pro'
        parent_slug: 关联的父skill slug（免费版和专业版共享）
    v1.2新增参数：
        workflow_state: 工作流状态 (默认'step1_read_original')
                       可选值: step1_read_original...completed, deprecated
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    now = datetime.now().isoformat()
    wf_state = workflow_state or 'step1_read_original'

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
                workflow_state = ?,
                updated_at = ?, notes = ?
            WHERE id = ?
        """, (name, display_name, version, category, source, local_path,
              source_slug, source_url, source_author, source_license,
              skill_type, pricing_model, is_differentiated,
              edition, parent_slug, wf_state, now, notes, skill_id))
    else:
        c.execute("""
            INSERT INTO skills (
                slug, current_name, current_display_name, current_version,
                category, source, source_slug, source_url, source_author, source_license,
                local_path, created_at, updated_at, current_status,
                is_differentiated, pricing_model, skill_type, notes,
                edition, parent_slug, workflow_state
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (slug, name, display_name, version, category, source,
              source_slug, source_url, source_author, source_license,
              local_path, now, now, 'registered', is_differentiated,
              pricing_model, skill_type, notes, edition, parent_slug, wf_state))
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
    """记录八大维度评分（v1.1新增，修复评分无持久化问题）

    参数：
        skill_id: skill ID
        score_type: 'baseline'（改造前基线）或 'final'（改造后最终）
        quality..differentiation: 八大维度分数（0-6分）
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    now = datetime.now().isoformat()
    total = quality + practicality + simplicity + cost + performance + debranding + compliance + differentiation
    is_pass = 1 if total >= 40 else 0

    c.execute("""
        INSERT INTO scores (
            skill_id, scored_at, score_type,
            quality_score, practicality_score, simplicity_score, cost_score,
            performance_score, debranding_score, compliance_score, differentiation_score,
            total_score, pass_threshold, is_pass, reviewer, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, now, score_type, quality, practicality, simplicity, cost,
          performance, debranding, compliance, differentiation,
          total, 40, is_pass, reviewer, notes))

    # 更新skills表的current_score
    c.execute("UPDATE skills SET current_score = ?, updated_at = ? WHERE id = ?",
              (total, now, skill_id))

    conn.commit()
    conn.close()
    return total, is_pass


def save_score(skill_id, score_type, total_score,
               quality=0, practicality=0, simplicity=0,
               performance=0, debranding=0, differentiation=0,
               compliance=0, cost=0,
               reviewer='system', notes=None, is_pass=None,
               pass_threshold=40):
    """保存评分记录（支持is_current历史保护机制）

    D5修复延续: 标记同类型旧记录为is_current=0，插入新记录is_current=1。
    替代: 各模块中的 UPDATE scores SET is_current=0 + INSERT INTO scores 裸SQL。

    参数：
        skill_id: skill ID
        score_type: 评分类型 ('trace_llm', 'agent_trial', 'baseline', 'final' 等)
        total_score: 总分
        quality..cost: 八大维度分数
        reviewer: 评分者标识
        notes: 评分备注（JSON字符串或普通文本）
        is_pass: 是否通过（None则自动按pass_threshold判定）
        pass_threshold: 通过阈值（默认40）
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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


def record_upload(skill_id, version, platform, platform_slug, upload_status,
                  http_status=None, error_message=None, visibility=None,
                  pricing_on_platform=None, community_published=0,
                  download_ready=None):
    """记录上传到平台

    v1.3新增参数：
        community_published: 是否已发布到社区 (0=未发布, 1=已发布, 默认0)
        download_ready: 下载就绪时间戳 (ISO格式字符串, None表示尚未就绪)
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
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
                 notes=None, edition=None, parent_slug=None, workflow_state=None):
    """仅插入skill记录（不含版本和操作记录）

    用于基线导入、自动差异化等需要单独控制版本记录内容（如content_hash）的场景。
    替代: INSERT INTO skills
    返回: skill_id
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    now = datetime.now().isoformat()
    wf_state = workflow_state or 'step1_read_original'
    c.execute("""
        INSERT INTO skills (
            slug, current_name, current_display_name, current_version,
            category, source, source_slug, source_url, source_author, source_license,
            local_path, created_at, updated_at, current_status,
            is_differentiated, differentiation_date, pricing_model, skill_type, notes,
            edition, parent_slug, workflow_state
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (slug, name, display_name, version, category, source,
          source_slug, source_url, source_author, source_license,
          local_path, now, now, current_status,
          is_differentiated, differentiation_date, pricing_model, skill_type, notes,
          edition, parent_slug, wf_state))
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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
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
            except Exception:
                pass
            if "locked" in str(e) and attempt < 2:
                _time.sleep(1)
                continue
            raise


def set_pricing(skill_id, edition, price_model, price_amount, price_currency,
                trial_limits, pro_features):
    """设置收费策略（新建记录）"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    c.execute("""
        UPDATE pricing
        SET edition = ?, price_model = ?, price_amount = ?, price_currency = ?
        WHERE skill_id = ?
    """, (edition, price_model, price_amount, price_currency, skill_id))

    conn.commit()
    conn.close()


def get_skill_status(slug):
    """获取skill状态"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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

def backfill_sync_status():
    """P0-3b + P0-4: 从 platform_uploads + upload_tracking.json 回填四平台同步状态

    两阶段回填:
    阶段1 (P0-3b): 从 platform_uploads 表回填 (已有逻辑)
    阶段2 (P0-4): 从 upload_tracking.json 直接回填 sync_status (消除unknown)

    幂等操作：可重复执行，每次都基于最新数据重新计算。
    同步状态值: synced / failed / not_applicable / unknown
    """
    import os
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    now = datetime.now().isoformat()

    # ====== 阶段1: 从 platform_uploads 回填 (优先级最高) ======

    # 回填 skillhub_sync_status
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

    # 回填 clawhub_sync_status
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

    # 回填 github_public_sync_status (hermes-skills 公开引流)
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

    # 回填 github_private_sync_status (origin 私有备份)
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

    # ====== 阶段2: 从 upload_tracking.json 直接回填 (P0-4 消缺unknown) ======

    json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'upload_tracking.json')
    json_synced_sh = 0
    json_synced_ch = 0
    json_synced_gh_pub = 0

    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            tracking = json.load(f)

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

            # ClawHub: JSON中clawhub.status=published → synced
            ch = data.get('clawhub', {})
            ch_st = ch.get('status', '')
            if ch_st == 'published':
                c.execute("UPDATE skills SET clawhub_sync_status = 'synced' WHERE id = ? AND clawhub_sync_status = 'unknown'", (skill_id,))
                if c.rowcount > 0:
                    json_synced_ch += 1
            elif ch_st in ('withdrawn', 'not_eligible', 'not_applicable'):
                c.execute("UPDATE skills SET clawhub_sync_status = 'not_applicable' WHERE id = ? AND clawhub_sync_status = 'unknown'", (skill_id,))

            # GitHub公开: JSON中hermes.github_published=true → synced
            hermes = data.get('hermes', {})
            if hermes.get('github_published'):
                c.execute("UPDATE skills SET github_public_sync_status = 'synced' WHERE id = ? AND github_public_sync_status = 'unknown'", (skill_id,))
                if c.rowcount > 0:
                    json_synced_gh_pub += 1

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

    # ====== 阶段5: SkillHub消缺 — packaged-skills/skillhub/目录的skill已上传 ======
    # V58-V59完成1920/1920批量重传(100%)，packaged-skills/skillhub/目录的skill
    # 都已通过enterprise_uploader上传到SkillHub
    c.execute("""
        UPDATE skills SET skillhub_sync_status = 'synced'
        WHERE skillhub_sync_status = 'unknown'
        AND local_path LIKE '%packaged-skills%skillhub%'
    """)
    sh_synced_from_local = c.rowcount

    # enterprise-upload/目录的skill也已上传到SkillHub (付费版)
    c.execute("""
        UPDATE skills SET skillhub_sync_status = 'synced'
        WHERE skillhub_sync_status = 'unknown'
        AND local_path LIKE '%enterprise-upload%'
    """)
    sh_synced_from_enterprise = c.rowcount

    # differentiated-skills/目录的skill也已上传 (差异化后的skill)
    c.execute("""
        UPDATE skills SET skillhub_sync_status = 'synced'
        WHERE skillhub_sync_status = 'unknown'
        AND local_path LIKE '%differentiated-skills%'
    """)
    sh_synced_from_diff = c.rowcount

    # opensource-skills/目录的skill也已上传
    c.execute("""
        UPDATE skills SET skillhub_sync_status = 'synced'
        WHERE skillhub_sync_status = 'unknown'
        AND local_path LIKE '%opensource-skills%'
    """)
    sh_synced_from_opensource = c.rowcount

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
        'json_synced_sh': json_synced_sh,
        'json_synced_ch': json_synced_ch,
        'json_synced_gh_pub': json_synced_gh_pub,
        'gh_private_synced': gh_private_synced,
        'source_na': source_na,
        'source_dir_na': source_dir_na,
    }
    print(f"backfill_sync_status 完成: {result}")
    return result


def migrate_github_to_dual_repo():
    """P0-3c: 迁移 platform_uploads 中的 github 记录为 github_public

    历史记录使用 'github' 值，现在需要区分 github_public (hermes-skills公开) 和 github_private (origin私有)。
    所有历史 'github' 记录均为 hermes-skills 公开仓库推送，因此迁移为 'github_public'。

    幂等操作：仅更新 platform='github' 的记录，已迁移的记录不受影响。
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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
    import os
    json_path = os.path.join(os.path.dirname(DB_PATH), 'data', 'upload_tracking.json')
    if not os.path.exists(json_path):
        print(f"sync_hermes_from_json: JSON文件不存在: {json_path}")
        return {'synced': 0, 'error': 'json_not_found'}

    with open(json_path, 'r', encoding='utf-8') as f:
        tracking = json.load(f)

    # JSON结构: {"metadata": {...}, "stats": {...}, "skills": {slug: {...}}, "last_updated": "..."}
    skills_data = tracking.get('skills', tracking)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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
    import os
    json_path = os.path.join(os.path.dirname(DB_PATH), 'data', 'upload_tracking.json')
    json_synced = 0
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            tracking = json.load(f)

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
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

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
    print("Database schema created successfully.")
    print(f"Location: {DB_PATH}")
