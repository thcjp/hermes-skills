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
            workflow_state TEXT DEFAULT 'step1_read_original'
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
            notes TEXT
        )
    """)

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
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )
    """)

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

    conn.commit()
    conn.close()
    print(f"Database initialized: {DB_PATH}")


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
                  pricing_on_platform=None):
    """记录上传到平台"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO platform_uploads (
            skill_id, version, platform, platform_slug, upload_date,
            upload_status, http_status, error_message, visibility, pricing_on_platform
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, version, platform, platform_slug, now, upload_status,
          http_status, error_message, visibility, pricing_on_platform))

    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (skill_id, f'upload_{platform}', now, 'system',
          f'Uploaded {version} to {platform}: {upload_status}', upload_status))

    conn.commit()
    conn.close()


def record_operation(skill_id, operation_type, details, before_state=None, after_state=None):
    """记录操作"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, before_state, after_state)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, operation_type, now, 'system', details, before_state, after_state))

    conn.commit()
    conn.close()


def set_pricing(skill_id, edition, price_model, price_amount, price_currency,
                trial_limits, pro_features):
    """设置收费策略"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()

    c.execute("""
        INSERT INTO pricing (skill_id, edition, price_model, price_amount, price_currency,
                            trial_limits, pro_features, effective_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (skill_id, edition, price_model, price_amount, price_currency,
          trial_limits, pro_features, now))

    conn.commit()
    conn.close()


def get_skill_status(slug):
    """获取skill状态"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
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
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
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
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
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


if __name__ == '__main__':
    init_database()
    print("Database schema created successfully.")
    print(f"Location: {DB_PATH}")
