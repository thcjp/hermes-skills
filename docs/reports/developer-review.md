# Skill生产规范v1.1 — 第4轮开发者代码审核报告

**审核轮次**: 第4轮（开发者代码审核）
**审核日期**: 2026-07-18
**审核范围**: db.py / check_debranding.py / 改造文件SKILL.md / 脚本一致性 / 可扩展性
**总体评分**: **68 / 100**

---

## 评分明细

| 维度 | 满分 | 得分 | 说明 |
|------|------|------|------|
| 数据库代码质量 (db.py) | 25 | 14 | 缺edition/parent_slug列、外键未启用、无事务边界、N+1查询、versions表未填充 |
| 检测脚本质量 (check_debranding.py) | 25 | 13 | `\b`正则中文失效(P0新发现)、反引号计数误判、绕过db.py抽象层、ALLOWED_CONTEXTS不完整 |
| 改造文件代码质量 | 20 | 14 | aws-agent-orchestrator-pro MCP处理正确；memory-fortress-pro 46.8%内容重叠 |
| 脚本一致性 | 15 | 10 | 步骤9代码可执行但缺edition/parent_slug；规范自述与实现矛盾 |
| 可扩展性 | 15 | 9 | list_all_skills无分页、代码块检测O(n²)、无连接池、660+规模存在瓶颈 |
| **合计** | **100** | **68** | |

---

## 一、代码问题清单

### P0 问题（5项 — 阻断级，必须立即修复）

---

#### P0-1: skills表缺少edition列（第3轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 28-51 (init_database建表语句)
- **问题描述**: skills表没有`edition`列。规范第2.1节（行139）明确声明"v1.1不再使用`-pro`/`-free`后缀，改用`edition`字段区分"，第5.2节（行365-374）再次强调edition字段，但数据库表结构中完全缺失此列。pricing表有edition列（行107），但skills主表没有，导致无法在主表层面追踪skill版本类型。
- **影响**: 无法通过数据库查询区分free/pro版本，只能依赖slug后缀（`-free`/`-pro`）做字符串匹配，违背了规范的设计意图。
- **验证方法**: `PRAGMA table_info(skills)` 确认无edition列。

**修复代码**:
```sql
-- db.py init_database() 中 skills 表建表语句补充
-- 在 skill_type TEXT, 后面添加:
edition TEXT DEFAULT 'standard',  -- free / pro / standard
parent_slug TEXT,                 -- 关联的母版slug（free和pro共享同一parent_slug）
```

```python
# db.py init_database() 中添加迁移逻辑（兼容已有数据库）
def init_database():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # ... 建表语句 ...

    # v1.1 迁移：为已有数据库添加 edition 和 parent_slug 列
    c.execute("PRAGMA table_info(skills)")
    existing_cols = [row[1] for row in c.fetchall()]
    if 'edition' not in existing_cols:
        c.execute("ALTER TABLE skills ADD COLUMN edition TEXT DEFAULT 'standard'")
    if 'parent_slug' not in existing_cols:
        c.execute("ALTER TABLE skills ADD COLUMN parent_slug TEXT")

    # 为已有数据回填 edition（根据slug后缀推断）
    c.execute("UPDATE skills SET edition = 'free' WHERE slug LIKE '%-free' AND edition = 'standard'")
    c.execute("UPDATE skills SET edition = 'pro' WHERE slug LIKE '%-pro' AND edition = 'standard'")

    conn.commit()
    conn.close()
```

---

#### P0-2: skills表缺少parent_slug列（第3轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 28-51
- **问题描述**: skills表没有`parent_slug`列。规范第2.1节（行156）明确说明"edition字段用于数据库追踪关联（两版本共享parent_slug）"，但数据库和代码均未实现。
- **影响**: free和pro版本之间无法建立数据库层面的关联关系，无法查询"某个skill的所有版本"。
- **修复代码**: 见P0-1修复代码中的ALTER TABLE语句。

---

#### P0-3: `\b`正则在中文上下文中完全失效（新发现）

- **文件**: `d:\skills\skill-registry\check_debranding.py`
- **行号**: 15-24 (FORBIDDEN_PATTERNS定义), 70 (re.finditer调用)
- **问题描述**: Python 3中`\w`默认匹配Unicode字符（含中文），因此`\b`在中文字符与英文字符之间**不产生边界匹配**。所有使用`\b`的禁止模式（clawhub、PostgreSQL、MCP、tenant等）在中文文本中将**完全无法检测**。
- **验证结果**:
  ```
  re.finditer(r'\b(clawhub)\b', "上传到clawhub平台")  → 0个匹配（应匹配1个）
  re.finditer(r'\bPostgreSQL\b', "支持PostgreSQL数据源")  → 0个匹配（应匹配1个）
  re.finditer(r'\b(clawhub)\b', " clawhub ")  → 1个匹配（英文上下文正常）
  ```
- **影响**: 检测脚本对中文SKILL.md中的品牌词检测存在严重盲区。攻击者只需在品牌词前后紧邻中文字符即可绕过所有检测。这是**安全合规层面的重大漏洞**。
- **根因**: Python 3 `re`模块默认Unicode模式下，`\w` = `[a-zA-Z0-9_]` + Unicode字母（含中文），`\b`仅在`\w`与非`\w`之间匹配。中文字符属于`\w`，因此"到clawhub"之间无`\b`。

**修复代码**:
```python
# check_debranding.py 第15-24行修改
# 方案：所有 \b 改为 (?<![a-zA-Z]) 和 (?![a-zA-Z]) 环视断言
# 或在编译时使用 re.ASCII 标志

FORBIDDEN_PATTERNS = [
    # 使用 (?<!\w) 和 (?!\w) 替代 \b，并指定 re.ASCII
    # 或更精确地使用 (?<![a-zA-Z]) 前向否定环视
    (r'(?<![a-zA-Z])(clawhub|clawsec|clawdbot|openclaw)(?![a-zA-Z])', '平台烙印词', 'high'),
    (r'(?<![a-zA-Z])(clawhut|clawhob|clawhvb)(?![a-zA-Z])', '平台烙印词变体', 'high'),
    (r'(?<![a-zA-Z])(fishclaw|narrato|dailyhot|novel_bridge|totalreclaw|kyaukyuai)(?![a-zA-Z])', '项目烙印词', 'high'),
    (r'(?<![a-zA-Z])PostgreSQL(?![a-zA-Z])', '内部系统词-PostgreSQL', 'high'),
    (r'(?<![a-zA-Z])MCP(?![a-zA-Z])', '内部系统词-MCP', 'medium'),
    (r'(?<![a-zA-Z])tenant(?![a-zA-Z])', '内部系统词-tenant', 'high'),
    # ... 其余模式不变（xianyu、老田和小甜甜、溯源词等不含\b的无需修改）
]
```

---

#### P0-4: 八大维度评分无持久化（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 22-164 (init_database全函数)
- **问题描述**: 规范定义了8大改造维度的0/2/4/6分量化评分体系（总分48分，低于30分不得上架），但数据库中**没有评分表**。评分结果仅在SKILL.md frontmatter中以YAML记录，无法通过SQL查询进行批量筛选、趋势分析或跨skill对比。
- **影响**: 无法回答"哪些skill评分低于30分？"、"哪个维度平均分最低？"等关键管理问题。
- **验证方法**: `SELECT name FROM sqlite_master WHERE type='table'` 确认无`skill_scores`表。

**修复代码**:
```python
# db.py init_database() 中添加
# 9. skill_scores - 八大维度评分表
c.execute("""
    CREATE TABLE IF NOT EXISTS skill_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skill_id INTEGER NOT NULL,
        version TEXT NOT NULL,
        scored_at TEXT NOT NULL,
        scorer TEXT,
        -- 八大维度评分（0/2/4/6分制）
        score_debranding INTEGER DEFAULT 0,        -- 去除标识
        score_differentiation INTEGER DEFAULT 0,    -- 差异化改造
        score_pricing INTEGER DEFAULT 0,            -- 收费策略
        score_version INTEGER DEFAULT 0,            -- 版本管理
        score_compliance INTEGER DEFAULT 0,         -- 双平台合规
        score_license INTEGER DEFAULT 0,            -- License合规
        score_documentation INTEGER DEFAULT 0,      -- 文档质量
        score_testing INTEGER DEFAULT 0,            -- 测试验证
        total_score INTEGER DEFAULT 0,              -- 总分（满分48）
        pass_threshold INTEGER DEFAULT 30,          -- 及格线
        is_passed INTEGER DEFAULT 0,                -- 是否通过
        notes TEXT,
        FOREIGN KEY (skill_id) REFERENCES skills(id)
    )
""")

c.execute("CREATE INDEX IF NOT EXISTS idx_scores_skill ON skill_scores(skill_id)")
c.execute("CREATE INDEX IF NOT EXISTS idx_scores_passed ON skill_scores(is_passed)")
c.execute("CREATE INDEX IF NOT EXISTS idx_scores_total ON skill_scores(total_score)")
```

---

#### P0-5: 10步工作流无状态机持久化（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 22-164 (init_database全函数)
- **问题描述**: 规范定义了10步工作流（下载→去标识→差异化→评分→版本→收费→License→合规→登记→上架），但数据库中**没有工作流状态表**。current_status字段是一个自由文本字段，无值域约束，无法追踪每个步骤的完成时间和操作人。
- **影响**: 无法回答"某个skill卡在哪一步？"、"步骤5平均耗时多少？"等流程管理问题。工作流可追溯性为零。
- **验证方法**: `SELECT name FROM sqlite_master WHERE type='table'` 确认无`workflow_state`表。

**修复代码**:
```python
# db.py init_database() 中添加
# 10. workflow_state - 工作流状态机表
c.execute("""
    CREATE TABLE IF NOT EXISTS workflow_state (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skill_id INTEGER NOT NULL,
        current_step INTEGER NOT NULL,           -- 当前步骤（1-10）
        step_name TEXT NOT NULL,                 -- 步骤名称
        step_status TEXT DEFAULT 'pending',      -- pending / in_progress / completed / failed / skipped
        started_at TEXT,
        completed_at TEXT,
        operator TEXT,
        notes TEXT,
        FOREIGN KEY (skill_id) REFERENCES skills(id)
    )
""")

c.execute("CREATE INDEX IF NOT EXISTS idx_workflow_skill ON workflow_state(skill_id)")
c.execute("CREATE INDEX IF NOT EXISTS idx_workflow_step ON workflow_state(current_step, step_status)")
```

---

### P1 问题（13项 — 严重级，需在版本发布前修复）

---

#### P1-1: 规范自身frontmatter缺edition字段（第3轮未修复）

- **文件**: `d:\skills\differentiated-skills\Agents\skill-production-standards\SKILL.md`
- **行号**: 1-20 (frontmatter)
- **问题描述**: 规范自身声明"使用edition字段区分版本"（行139），但自身的frontmatter中没有`edition`字段。规范不遵守自己的规范。
- **修复代码**:
```yaml
# 在 frontmatter 中添加
edition: standard  # 规范本身是标准版
```

---

#### P1-2: 外键约束未启用（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 24 (sqlite3.connect后)
- **问题描述**: 虽然表定义中声明了`FOREIGN KEY`，但SQLite默认不启用外键约束检查。需要在每次连接后执行`PRAGMA foreign_keys = ON`。当前代码在所有`sqlite3.connect()`调用后均未执行此pragma。
- **验证结果**: `PRAGMA foreign_keys` 返回 `0` (OFF)。
- **影响**: 可以插入指向不存在skill_id的versions/operations/pricing记录，数据完整性无法保证。

**修复代码**:
```python
# db.py 所有函数中，在 sqlite3.connect() 后添加：
conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON")  # 启用外键约束
c = conn.cursor()

# 更好的方案：封装为上下文管理器
import contextlib

@contextlib.contextmanager
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()
```

---

#### P1-3: 三张死表（第1轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 118-151 (sources/dependencies/skills_fts建表)
- **问题描述**: `sources`(行120-131)、`dependencies`(行135-143)、`skills_fts`(行148-151)三张表已创建但从未被任何代码写入或查询。数据库验证显示三张表均为0行。
- **影响**: 代码膨胀，维护成本增加，给开发者造成"功能已实现"的错觉。

**修复方案**:
```python
# 方案A：删除死表（如果短期不使用）
# 删除 init_database() 中 sources、dependencies、skills_fts 的建表语句

# 方案B：实现写入逻辑
# 在 register_skill() 中，同时写入 sources 表：
c.execute("""
    INSERT INTO sources (source_type, source_name, source_url, source_author,
                         source_license, download_date, original_slug)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", (source, source, source_url, source_author, source_license, now, source_slug))

# 在 register_skill() 中，同时更新 skills_fts：
c.execute("""
    INSERT INTO skills_fts (slug, name, display_name, description, tags, category)
    VALUES (?, ?, ?, ?, ?, ?)
""", (slug, name, display_name, notes, '', category))
```

---

#### P1-4: 反引号计数逻辑错误 — triple backticks误判为内联代码（第1轮P2-5升级）

- **文件**: `d:\skills\skill-registry\check_debranding.py`
- **行号**: 81-85
- **问题描述**: 反引号检测使用`before.count('`')`统计匹配位置之前的所有反引号数量，通过奇偶性判断是否在内联代码中。但此逻辑将代码块的` ``` `（3个反引号）也计入统计，导致3个反引号=奇数=误判为"在内联代码中"，从而错误跳过代码块内的品牌词检测。
- **验证结果**:
  ```
  内容: "# Test\n```bash\nclawhub upload\n```\n"
  before.count('`') = 3 (代码块开头的三个反引号)
  3 % 2 == 1 → True → 误判为内联代码 → 跳过clawhub检测
  ```
- **影响**: 代码块内的clawhub/项目烙印词等**不会被检测到**（虽然代码块内的MCP/tenant/PostgreSQL有独立的allowlist跳过逻辑，但代码块内的clawhub应该被检测却没有被检测）。

**修复代码**:
```python
# check_debranding.py 第81-85行修改
# 方案：先排除代码块的反引号，再统计内联反引号

# 替换原来的反引号检测逻辑：
if '`' in context:
    before = content[:m.start()]
    # 排除代码块的 triple backticks，只统计内联反引号
    before_no_codeblocks = re.sub(r'```.*?```', '', before, flags=re.DOTALL)
    # 同时排除未闭合的代码块开头
    before_no_codeblocks = re.sub(r'```[^\n]*\n', '', before_no_codeblocks)
    backtick_count_before = before_no_codeblocks.count('`')
    if backtick_count_before % 2 == 1:
        continue
```

---

#### P1-5: check_debranding.py绕过db.py抽象层（第1轮未修复）

- **文件**: `d:\skills\skill-registry\check_debranding.py`
- **行号**: 166-201 (update_database_with_check_results函数)
- **问题描述**: `update_database_with_check_results()`直接使用`sqlite3.connect()`操作数据库，绕过了db.py的抽象层。直接SQL操作与db.py的`record_operation()`功能重复。
- **影响**: 如果db.py的表结构变更（如P0-1/P0-2添加edition/parent_slug列），check_debranding.py不会自动适配，需要同步修改两处代码。

**修复代码**:
```python
# check_debranding.py 第166-201行重写
from db import record_operation  # 导入db.py的抽象层

def update_database_with_check_results(results):
    """将检测结果更新到数据库（通过db.py抽象层）"""
    debranding_pass_count = 0
    debranding_fail_count = 0

    for file_path, result in results.items():
        issues = result.get('issues', [])
        slug = Path(file_path).parent.name

        # 通过 db.py 查询 skill_id（而非直接SQL）
        from db import get_skill_status
        skill_data = get_skill_status(slug)
        if not skill_data:
            continue

        skill_id = skill_data['skill']['id']
        status = 'pass' if not issues else 'fail'

        if status == 'pass':
            debranding_pass_count += 1
        else:
            debranding_fail_count += 1

        # 通过 db.py 记录操作（而非直接SQL）
        issue_summary = '; '.join(f"{i['description']}:{i['match']}" for i in issues[:5])
        record_operation(
            skill_id=skill_id,
            operation_type='debranding_check',
            details=f'Found {len(issues)} issues' + (f': {issue_summary}' if issues else ''),
            before_state='unchecked',
            after_state=status
        )

    print(f"\nDatabase updated:")
    print(f"  Debranding pass: {debranding_pass_count}")
    print(f"  Debranding fail: {debranding_fail_count}")
```

---

#### P1-6: update_database_with_check_results不更新current_status（第1轮未修复）

- **文件**: `d:\skills\skill-registry\check_debranding.py`
- **行号**: 166-201
- **问题描述**: 检测完成后仅在operations表记录操作历史，但**不更新skills表的current_status字段**。通过检测的skill其current_status仍为旧值（如'registered'），不会变为'debranding_passed'。
- **影响**: 工作流状态不连贯，`get_skills_needing_work()`无法正确筛选已完成去标识的skill。

**修复代码**:
```python
# 在 update_database_with_check_results() 中添加状态更新
from db import record_operation
import sqlite3
from datetime import datetime

def update_database_with_check_results(results):
    from db import DB_PATH, record_operation, get_skill_status
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    now = datetime.now().isoformat()

    debranding_pass_count = 0
    debranding_fail_count = 0

    for file_path, result in results.items():
        issues = result.get('issues', [])
        slug = Path(file_path).parent.name

        c.execute("SELECT id FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        if not row:
            continue

        skill_id = row[0]
        status = 'pass' if not issues else 'fail'
        new_db_status = 'debranding_passed' if not issues else 'debranding_failed'

        # 更新 skills 表的 current_status
        c.execute("UPDATE skills SET current_status = ?, updated_at = ? WHERE id = ?",
                  (new_db_status, now, skill_id))

        if status == 'pass':
            debranding_pass_count += 1
        else:
            debranding_fail_count += 1

        # 记录操作
        issue_summary = '; '.join(f"{i['description']}:{i['match']}" for i in issues[:5])
        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, before_state, after_state)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (skill_id, 'debranding_check', now, 'script',
              f'Found {len(issues)} issues' + (f': {issue_summary}' if issues else ''),
              'unchecked', new_db_status))

    conn.commit()
    conn.close()

    print(f"\nDatabase updated:")
    print(f"  Debranding pass: {debranding_pass_count}")
    print(f"  Debranding fail: {debranding_fail_count}")
```

---

#### P1-7: ALLOWED_CONTEXTS不完整 — clawhub和PostgreSQL缺失（第1轮未修复）

- **文件**: `d:\skills\skill-registry\check_debranding.py`
- **行号**: 46-54
- **问题描述**: `ALLOWED_CONTEXTS`列表仅包含7项（SkillHub/skillhub.cn/SkillPay/工具协议/Agent工具协议/transport/Transport）。规范第1轮QA已指出clawhub和PostgreSQL在某些合法上下文中应被允许，但未被加入。但需注意：clawhub本身是平台烙印词，不应加入ALLOWED_CONTEXTS（应通过代码块/反引号机制跳过，而非上下文白名单）；PostgreSQL作为数据库技术术语，在描述外部数据源时是合法的。
- **修复建议**: PostgreSQL应加入ALLOWED_CONTEXTS（或作为技术术语allowlist处理），clawhub不应加入（它是要检测的烙印词，应通过修复P0-3和P1-4使其在代码块中也能被正确检测）。

**修复代码**:
```python
# check_debranding.py 第46-54行修改
ALLOWED_CONTEXTS = [
    'SkillHub',
    'skillhub.cn',
    'SkillPay',
    '工具协议',
    'Agent工具协议',
    'transport',
    'Transport',
    # 新增：PostgreSQL作为标准数据库技术术语
    'PostgreSQL',      # PostgreSQL作为外部数据源描述时合法
    'database',
    '数据源',
    '数据库',
]

# 在 check_skill_md() 中，为PostgreSQL添加上下文白名单跳过
# 第87-92行代码块检测后添加：
if 'PostgreSQL' in pattern and any(kw in context for kw in ['数据源', '数据库', 'database', 'PostgreSQL']):
    continue
```

---

#### P1-8: 无事务边界（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 226-281 (register_skill), 284-307 (record_upload), 310-322 (record_operation), 325-340 (set_pricing)
- **问题描述**: 每个函数内部有多个INSERT/UPDATE操作（如register_skill同时操作skills表、versions表、operations表），但使用的是简单的`conn.commit()`。如果中间某步失败，前面的操作已提交，后面的未提交，导致数据不一致。没有使用`BEGIN TRANSACTION`/`COMMIT`/`ROLLBACK`事务边界。
- **影响**: 并发写入或异常时数据一致性无法保证。

**修复代码**:
```python
# db.py register_skill() 重构示例（其他函数同理）
def register_skill(slug, name, display_name, version, category, source, local_path,
                   source_slug=None, source_url=None, source_author=None,
                   source_license=None, skill_type=None, pricing_model=None,
                   is_differentiated=0, notes=None, edition='standard', parent_slug=None):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    now = datetime.now().isoformat()

    try:
        conn.execute("BEGIN TRANSACTION")  # 显式事务

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
                    updated_at = ?, notes = ?
                WHERE id = ?
            """, (name, display_name, version, category, source, local_path,
                  source_slug, source_url, source_author, source_license,
                  skill_type, pricing_model, is_differentiated,
                  edition, parent_slug, now, notes, skill_id))
        else:
            c.execute("""
                INSERT INTO skills (
                    slug, current_name, current_display_name, current_version,
                    category, source, source_slug, source_url, source_author, source_license,
                    local_path, created_at, updated_at, current_status,
                    is_differentiated, pricing_model, skill_type, notes, edition, parent_slug
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (slug, name, display_name, version, category, source,
                  source_slug, source_url, source_author, source_license,
                  local_path, now, now, 'registered', is_differentiated,
                  pricing_model, skill_type, notes, edition, parent_slug))
            skill_id = c.lastrowid

        c.execute("""
            INSERT INTO versions (skill_id, version, created_at, changelog)
            VALUES (?, ?, ?, ?)
        """, (skill_id, version, now, f"Registered skill {slug} v{version}"))

        c.execute("""
            INSERT INTO operations (skill_id, operation_type, operation_date, operator, details, after_state)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (skill_id, 'register', now, 'system', f'Registered {slug} v{version}', 'registered'))

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        raise e
    finally:
        conn.close()
    return skill_id
```

---

#### P1-9: list_all_skills() N+1查询（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 379-396
- **问题描述**: `list_all_skills()`使用了3个关联子查询（upload_count、last_upload、platforms_uploaded），每行skill都要执行3次子查询。当前660+skill时，相当于660×3=1980次子查询。
- **影响**: 大规模数据下查询性能严重下降。

**修复代码**:
```python
# db.py list_all_skills() 重写为JOIN聚合
def list_all_skills():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("""
        SELECT s.*,
            COALESCE(uc.upload_count, 0) as upload_count,
            uc.last_upload,
            uc.platforms_uploaded
        FROM skills s
        LEFT JOIN (
            SELECT skill_id,
                   COUNT(*) FILTER (WHERE upload_status = 'success') as upload_count,
                   MAX(upload_date) as last_upload,
                   GROUP_CONCAT(DISTINCT platform) FILTER (WHERE upload_status = 'success') as platforms_uploaded
            FROM platform_uploads
            GROUP BY skill_id
        ) uc ON s.id = uc.skill_id
        ORDER BY s.category, s.slug
    """)

    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results
```

> 注：SQLite 3.30+支持`FILTER`子句。如果版本不支持，可用`SUM(CASE WHEN ... THEN 1 ELSE 0 END)`替代。

---

#### P1-10: versions表content_hash/file_size/line_count未填充（第1轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 267-271 (register_skill中versions插入)
- **问题描述**: versions表有content_hash/file_size/line_count字段（行61-63），但register_skill在插入versions记录时（行268-271）只填了skill_id/version/created_at/changelog，**未计算和填充hash/size/行数**。数据库验证显示1322条versions记录中content_hash全部为NULL。
- **影响**: 无法检测文件内容变更（只能靠版本号），无法做增量同步，版本去重失效。

**修复代码**:
```python
# db.py register_skill() 中 versions 插入修改
# 在插入 versions 之前计算 hash 和文件信息
import hashlib, os

def compute_file_info(file_path):
    """计算文件的hash、大小、行数"""
    if not file_path or not os.path.exists(file_path):
        return None, None, None
    with open(file_path, 'rb') as f:
        content = f.read()
    content_hash = hashlib.sha256(content).hexdigest()
    file_size = len(content)
    line_count = len(content.decode('utf-8', errors='replace').split('\n'))
    return content_hash, file_size, line_count

# 在 register_skill() 中：
skill_md_path = os.path.join(local_path, 'SKILL.md')
content_hash, file_size, line_count = compute_file_info(skill_md_path)

c.execute("""
    INSERT INTO versions (skill_id, version, created_at, changelog, content_hash, file_size, line_count)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", (skill_id, version, now, f"Registered skill {slug} v{version}",
      content_hash, file_size, line_count))
```

---

#### P1-11: pricing表缺end_date/is_active（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 102-116 (pricing建表)
- **问题描述**: pricing表只有`effective_date`（生效日期），没有`end_date`（失效日期）和`is_active`（是否当前生效）字段。每次调用set_pricing都会插入新行，但无法标记旧行失效，也无法查询"当前生效的定价"。
- **影响**: 无法管理定价历史，无法回答"某个skill当前的定价是多少？"（只能查最新插入的，但这不一定是当前生效的）。

**修复代码**:
```python
# db.py init_database() 中 pricing 表修改
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
        end_date TEXT,                    -- 新增：失效日期
        is_active INTEGER DEFAULT 1,      -- 新增：是否当前生效（1=生效, 0=已失效）
        FOREIGN KEY (skill_id) REFERENCES skills(id)
    )
""")

# db.py set_pricing() 修改：先失效旧定价，再插入新定价
def set_pricing(skill_id, edition, price_model, price_amount, price_currency,
                trial_limits, pro_features):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    now = datetime.now().isoformat()

    try:
        conn.execute("BEGIN TRANSACTION")
        # 失效同一skill同一edition的旧定价
        c.execute("""
            UPDATE pricing SET is_active = 0, end_date = ?
            WHERE skill_id = ? AND edition = ? AND is_active = 1
        """, (now, skill_id, edition))

        # 插入新定价
        c.execute("""
            INSERT INTO pricing (skill_id, edition, price_model, price_amount, price_currency,
                                trial_limits, pro_features, effective_date, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (skill_id, edition, price_model, price_amount, price_currency,
              trial_limits, pro_features, now))

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        raise e
    finally:
        conn.close()
```

---

#### P1-12: memory-fortress-pro 46.8%内容与free版完全重叠（第3轮量化验证）

- **文件**: `d:\skills\differentiated-skills\Agents\memory-fortress-pro\SKILL.md`
- **行号**: 全文854行
- **问题描述**: 第3轮PM指出"换皮"嫌疑（新增内容占比约30%），经代码层面逐行对比验证，实际数据如下：
  - 专业版总非空行数: 558行
  - 与免费版完全重叠行数: 261行（46.8%）
  - 专业版独有行数: 297行（53.2%）
  - 7个章节为100%复制（六层记忆架构/当前任务/关键上下文/待办事项/快速开始，均为2-7行的短章节）
  - 5个章节为专业版独有新增（多角色场景指南/性能优化策略/多平台集成示例/版本升级迁移指南/推荐文件结构）
- **评估**: PM的30%估计偏低，实际新增内容占53.2%。但46.8%的重叠中，核心架构章节（架构总览76.9%重叠、Agent指令70.8%重叠、WAL协议27.3%重叠）的复制是合理的（共享底层架构），问题在于"当前任务/关键上下文/待办事项"等运行时状态章节也100%复制，这些应按版本定制。六层架构完整性检查通过（六层均在两版本中存在）。
- **严重度**: P1（不阻断发布，但影响专业版价值感）

**修复建议**:
```markdown
# memory-fortress-pro/SKILL.md 需差异化的章节：
# 1. "当前任务" — 应反映专业版独有的任务（如向量索引重建、Mem0模型调优）
# 2. "关键上下文" — 应包含专业版独有的上下文（如云同步状态、成本预算）
# 3. "待办事项" — 应包含专业版独有的待办（如多平台集成测试）
# 4. "快速开始" — 应增加专业版独有的启动步骤（向量DB初始化、Mem0配置）
# 5. "六层记忆架构" — 应在每层标注"✅ 专业版增强：..."说明差异点
```

---

#### P1-13: 规范步骤9代码缺edition/parent_slug参数（新发现）

- **文件**: `d:\skills\differentiated-skills\Agents\skill-production-standards\SKILL.md`
- **行号**: 步骤9数据库登记代码段
- **问题描述**: 规范步骤9的register_skill调用示例未传递edition和parent_slug参数。规范第2.1节（行156）明确说"两版本共享parent_slug"，但步骤9的代码示例中：
  - register_skill的参数列表中没有edition和parent_slug
  - 同时db.py的register_skill函数签名（行226-229）也不接受这两个参数
- **影响**: 规范描述的edition/parent_slug机制在代码层面完全未实现，步骤9代码可执行但无法完成规范要求的功能。

**修复代码**:
```python
# 规范步骤9代码应修改为：
from db import register_skill, record_operation, set_pricing

# 注册免费版
free_skill_id = register_skill(
    slug='new-skill-free',
    name='new-skill-free',
    display_name='新名称(免费版)',
    version='1.0.0',
    category='Agents',
    source='clawhub_download',
    local_path=r'd:\skills\differentiated-skills\Agents\new-skill-free',
    source_slug='original-slug',
    source_license='MIT',
    skill_type='differentiated',
    pricing_model='free',
    is_differentiated=1,
    edition='free',           # 新增
    parent_slug='new-skill'   # 新增：两版本共享的母版slug
)

# 注册专业版
pro_skill_id = register_skill(
    slug='new-skill-pro',
    name='new-skill-pro',
    display_name='新名称(专业版)',
    version='1.0.0',
    category='Agents',
    source='clawhub_download',
    local_path=r'd:\skills\differentiated-skills\Agents\new-skill-pro',
    source_slug='original-slug',
    source_license='MIT',
    skill_type='differentiated',
    pricing_model='paid',
    is_differentiated=1,
    edition='pro',            # 新增
    parent_slug='new-skill'   # 新增：与免费版共享同一parent_slug
)
```

---

### P2 问题（12项 — 改进级，建议修复）

---

#### P2-1: exclude_dirs使用子串匹配（第1轮未修复）

- **文件**: `d:\skills\skill-registry\check_debranding.py`
- **行号**: 112
- **问题描述**: `any(excluded in str(skill_md) for excluded in exclude_dirs)`使用子串匹配，`'skill-production-standards'`会同时匹配`'skill-production-standards-v2'`等目录。
- **修复代码**:
```python
# 改为路径组件精确匹配
skill_path = Path(skill_md)
if any(excluded in skill_path.parts for excluded in exclude_dirs):
    continue
```

---

#### P2-2: 代码块检测O(n²)性能问题（第1轮未修复）

- **文件**: `d:\skills\skill-registry\check_debranding.py`
- **行号**: 88
- **问题描述**: `list(re.finditer(r'```', content[:m.start()]))`对每个匹配位置都重新扫描从文件开头到当前位置的所有` ``` `，时间复杂度O(n²)。660+skill×每个文件多个匹配=大量重复扫描。
- **修复代码**:
```python
# 预计算代码块区域，避免重复扫描
def find_codeblock_regions(content):
    """预计算所有代码块区域的(start, end)列表"""
    regions = []
    in_block = False
    block_start = 0
    for m in re.finditer(r'```', content):
        if not in_block:
            block_start = m.start()
            in_block = True
        else:
            regions.append((block_start, m.end()))
            in_block = False
    if in_block:  # 未闭合的代码块
        regions.append((block_start, len(content)))
    return regions

def is_in_codeblock(pos, regions):
    """检查位置是否在代码块内"""
    for start, end in regions:
        if start <= pos <= end:
            return True
    return False

# 在 check_skill_md() 中预计算一次
codeblock_regions = find_codeblock_regions(content)
# 然后在循环中使用：
if is_in_codeblock(m.start(), codeblock_regions):
    if 'tenant' in pattern.lower() or 'MCP' in pattern or 'PostgreSQL' in pattern:
        continue
```

---

#### P2-3: parse_skill_md未集成到register_skill（第1轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 177-224 (parse_skill_md), 226-281 (register_skill)
- **问题描述**: `parse_skill_md()`函数（行177）已实现从SKILL.md解析frontmatter的能力，但`register_skill()`（行226）不调用它，所有字段需调用方手动传入。
- **修复代码**:
```python
# db.py 添加便捷函数
def register_skill_from_md(skill_md_path, source='local', **overrides):
    """从SKILL.md文件自动解析并注册"""
    parsed = parse_skill_md(skill_md_path)
    if not parsed:
        return None

    fm = parsed.get('frontmatter', {})
    return register_skill(
        slug=fm.get('slug', Path(skill_md_path).parent.name),
        name=fm.get('name', ''),
        display_name=fm.get('display_name', fm.get('name', '')),
        version=fm.get('version', '1.0.0'),
        category=fm.get('category', 'uncategorized'),
        source=source,
        local_path=str(Path(skill_md_path).parent),
        edition=fm.get('edition', 'standard'),
        parent_slug=fm.get('parent_slug'),
        **overrides
    )
```

---

#### P2-4: register_skill必填参数与规范不一致（第1轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 226-229
- **问题描述**: register_skill有7个必填参数（slug/name/display_name/version/category/source/local_path），但规范步骤9的调用示例中display_name和version可能是可选的（从SKILL.md自动解析）。
- **修复建议**: 提供从SKILL.md自动注册的便捷函数（见P2-3），减少手动参数。

---

#### P2-5: set_pricing必填参数过多（第1轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 325-326
- **问题描述**: set_pricing有7个必填参数，但某些场景下trial_limits和pro_features可能不适用（如免费版不需要设置定价）。
- **修复代码**:
```python
def set_pricing(skill_id, edition, price_model='free', price_amount=0,
                price_currency='CNY', trial_limits=None, pro_features=None):
    # 将非edition参数设为可选，提供默认值
```

---

#### P2-6: pricing_model无值域校验（第1轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 47 (pricing_model TEXT)
- **问题描述**: pricing_model是自由文本字段，无值域约束。可能存储'free'/'paid'/'subscription'/'freemium'等不一致的值。
- **修复代码**:
```python
# 在 register_skill() 中添加校验
VALID_PRICING_MODELS = {'free', 'paid', 'subscription', 'freemium', 'one-time'}
if pricing_model and pricing_model not in VALID_PRICING_MODELS:
    raise ValueError(f"Invalid pricing_model: {pricing_model}. Must be one of {VALID_PRICING_MODELS}")
```

---

#### P2-7: SLUG_MAPPING硬编码（第2轮未修复）

- **文件**: `d:\skills\skill-registry\scan_and_import.py`
- **问题描述**: SLUG_MAPPING字典硬编码了slug映射关系，新增skill需要手动修改代码。
- **修复建议**: 将映射关系存储到数据库的sources表或配置文件中。

---

#### P2-8: 无WAL模式（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 24 (init_database中)
- **问题描述**: 未启用WAL（Write-Ahead Logging）模式，并发读写时性能差。
- **修复代码**:
```python
# init_database() 中添加
c.execute("PRAGMA journal_mode = WAL")
c.execute("PRAGMA synchronous = NORMAL")
```

---

#### P2-9: 无Schema迁移版本管理（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 22 (init_database)
- **问题描述**: 使用`CREATE TABLE IF NOT EXISTS`，无法做Schema升级迁移。添加新列需要手动ALTER TABLE。
- **修复建议**: 添加schema_version表记录版本号，实现迁移逻辑。

---

#### P2-10: 无连接池（第2轮未修复）

- **文件**: `d:\skills\skill-registry\db.py`
- **问题描述**: 每个函数都创建新连接，频繁连接/断开开销大。
- **修复建议**: 使用连接池或上下文管理器复用连接。

---

#### P2-11: list_all_skills()无分页（新发现）

- **文件**: `d:\skills\skill-registry\db.py`
- **行号**: 379-396
- **问题描述**: `list_all_skills()`返回所有skill记录，无LIMIT/OFFSET分页。660+skill时返回大量数据，内存占用高。
- **修复代码**:
```python
def list_all_skills(limit=None, offset=0, category=None):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    query = """
        SELECT s.*, ...
        FROM skills s
        LEFT JOIN (...) uc ON s.id = uc.skill_id
    """
    params = []
    if category:
        query += " WHERE s.category = ?"
        params.append(category)
    query += " ORDER BY s.category, s.slug"
    if limit:
        query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])

    c.execute(query, params)
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results
```

---

#### P2-12: analyze_status.py中f-string SQL拼接（新发现）

- **文件**: `d:\skills\skill-registry\analyze_status.py`
- **行号**: 174
- **问题描述**: `query += f" LIMIT {limit}"`使用f-string拼接SQL。虽然limit参数通常为整数，但如果传入恶意字符串会导致SQL注入。
- **修复代码**:
```python
# 改为参数化查询
if limit:
    query += " LIMIT ?"
    c.execute(query, (limit,))
else:
    c.execute(query)
```

---

## 二、修复方案汇总（优先级排序）

### 第一优先级：P0修复（5项）

| 编号 | 修复内容 | 涉及文件 | 预计工时 |
|------|----------|----------|----------|
| P0-1 | skills表添加edition列 | db.py | 0.5h |
| P0-2 | skills表添加parent_slug列 | db.py | 0.5h |
| P0-3 | `\b`正则改为`(?<![a-zA-Z])`环视 | check_debranding.py | 1h |
| P0-4 | 添加skill_scores评分表 | db.py | 1h |
| P0-5 | 添加workflow_state状态表 | db.py | 1h |

### 第二优先级：P1修复（13项）

| 编号 | 修复内容 | 涉及文件 | 预计工时 |
|------|----------|----------|----------|
| P1-1 | 规范frontmatter添加edition | SKILL.md(规范) | 0.1h |
| P1-2 | 启用外键约束 | db.py | 0.5h |
| P1-3 | 处理三张死表 | db.py | 1h |
| P1-4 | 修复反引号计数逻辑 | check_debranding.py | 1h |
| P1-5 | check_debranding改用db.py抽象层 | check_debranding.py | 1h |
| P1-6 | 更新current_status字段 | check_debranding.py | 0.5h |
| P1-7 | 完善ALLOWED_CONTEXTS | check_debranding.py | 0.5h |
| P1-8 | 添加事务边界 | db.py | 2h |
| P1-9 | 重写list_all_skills为JOIN | db.py | 1h |
| P1-10 | 填充versions表hash/size/lines | db.py | 1h |
| P1-11 | pricing表添加end_date/is_active | db.py | 1h |
| P1-12 | 差异化memory-fortress-pro运行时章节 | SKILL.md(pro) | 2h |
| P1-13 | 规范步骤9代码补edition/parent_slug | SKILL.md(规范) | 0.5h |

---

## 三、通过项清单

以下代码经审核确认正确实现：

### 数据库代码 (db.py)

1. **参数化查询**: 所有SQL查询均使用`?`占位符，无SQL注入风险（db.py全函数）
2. **register_skill幂等性**: 支持已存在skill的更新（先SELECT再INSERT/UPDATE，行237-265）
3. **record_upload上传记录**: 正确记录上传状态和错误信息（行284-307）
4. **record_operation操作历史**: before_state/after_state参数设计合理，支持状态追踪（行310-322）
5. **set_pricing定价设置**: edition参数有效，INSERT语句正确（行325-340）
6. **get_skill_status关联查询**: 正确查询skill及其versions/operations/uploads/pricing（行343-376）
7. **get_skills_needing_work返回结构**: 返回dict区分needs_optimization和needs_upload，结构合理（行399-423）
8. **索引设计**: 为slug/status/source/category/skill_id等高频查询字段创建了索引（行153-161）

### 检测脚本 (check_debranding.py)

9. **FORBIDDEN_PATTERNS覆盖度**: 6大类检测模式覆盖平台烙印/项目烙印/内部系统词/溯源词/GitHub URL/原作者署名（行13-43）
10. **嵌套循环bug已修复**: v1.1已将外层for match + 内层finditer改为直接finditer遍历，消除了重复报告（行68-70）
11. **代码块技术术语allowlist**: 代码块中的MCP/tenant/PostgreSQL被正确跳过（行87-92）
12. **aws-agent-orchestrator-pro MCP处理**: 8处MCP引用全部正确处理（2处代码块内、4处反引号内、2处transport上下文），0误报
13. **CLI命令速查表完整**: aws-agent-orchestrator-pro的CLI命令表保留完整（行134起，含8条命令及专业版增强说明）
14. **报告生成功能**: generate_report正确生成Markdown格式报告，含统计摘要和问题详情（行126-163）

### 改造文件

15. **memory-fortress-pro六层架构完整**: 第一层至第六层均完整保留（免费版和专业版均含）
16. **memory-fortress-pro新增内容**: 专业版有5个全新章节（多角色场景指南/性能优化策略/多平台集成示例/版本升级迁移指南/推荐文件结构），新增内容占53.2%
17. **aws-agent-orchestrator-pro Transport矩阵**: Lambda/REST/MCP三transport正确保留，MCP作为transport类型合法引用

---

## 四、可扩展性代码评估

### 4.1 660+ skill批量处理能力评估

| 组件 | 当前能力 | 660+规模瓶颈 | 严重度 |
|------|----------|-------------|--------|
| register_skill | 单条注册，每次开关连接 | 批量注册660次连接/断开，约3-5分钟 | 中 |
| list_all_skills | 无分页，3个关联子查询 | 660行×3子查询=1980次查询，约2-5秒 | 高 |
| check_skill_md | O(n²)代码块检测 | 每文件多匹配×全量扫描，大文件可能数秒 | 高 |
| check_all_skills | 串行遍历所有SKILL.md | 660文件串行检测，约10-30分钟 | 中 |
| update_database_with_check_results | 逐条更新 | 660次单独INSERT，约1-2分钟 | 低 |

### 4.2 批量注册脚本优化建议

```python
# scan_and_import.py 优化建议
def batch_register_skills(skills_list):
    """批量注册skill，使用单连接+事务"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    c = conn.cursor()

    try:
        conn.execute("BEGIN TRANSACTION")
        for skill in skills_list:
            # 批量INSERT（使用executemany或循环INSERT）
            c.execute("INSERT INTO skills (...) VALUES (...)", (...))
        conn.execute("COMMIT")
    except:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
```

### 4.3 检测脚本性能优化建议

```python
# check_debranding.py 并行化建议
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_all_skills_parallel(directory, exclude_dirs=None, max_workers=4):
    """并行检测所有SKILL.md"""
    results = {}
    exclude_dirs = exclude_dirs or []

    skill_files = [
        f for f in Path(directory).rglob('SKILL.md')
        if not any(excluded in f.parts for excluded in exclude_dirs)
    ]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_skill_md, f): f for f in skill_files}
        for future in as_completed(futures):
            file_path = futures[future]
            issues, error = future.result()
            results[str(file_path)] = {'issues': issues} if not error else {'error': error}

    return results
```

---

## 五、脚本一致性验证

### 5.1 规范描述 vs 实际代码

| 验证项 | 规范描述 | 实际代码 | 一致性 |
|--------|----------|----------|--------|
| register_skill参数 | 应支持edition/parent_slug | 不支持 | **不一致** |
| set_pricing参数 | edition/price_model/price_amount/... | 完全匹配 | 一致 |
| record_operation参数 | skill_id/operation_type/details/before_state/after_state | 完全匹配 | 一致 |
| 步骤9代码可执行性 | 应能直接运行 | 可运行但缺edition/parent_slug | **部分一致** |
| 检测脚本6项检测 | 6大类禁止模式 | 实际6大类+变体=15条正则 | 一致（超额完成） |
| 技术术语allowlist | MCP/tenant/PostgreSQL在代码块中跳过 | 正确实现 | 一致 |
| edition字段替代后缀 | 使用edition字段，不使用-pro/-free后缀 | 实际目录仍用-pro/-free后缀 | **不一致** |

### 5.2 规范自相矛盾

规范第2.1节（行139）声明"v1.1不再使用`-pro`/`-free`后缀"，但：
1. 规范自身的frontmatter没有edition字段（P1-1）
2. 实际skill目录命名为`memory-fortress-free`/`memory-fortress-pro`/`aws-agent-orchestrator-pro`
3. 规范步骤9代码中slug仍使用`-free`/`-pro`后缀（行143-150的YAML示例也用了后缀）
4. db.py不支持edition/parent_slug字段

**结论**: 规范的edition字段设计仅停留在文档层面，代码实现完全未跟进。

---

## 六、给第5轮（安全合规）的传递注意事项

### 6.1 必须重点验证的安全问题

1. **P0-3（最高优先级）**: `\b`正则在中文上下文中完全失效 — 这是安全合规层面的重大漏洞。所有使用`\b`的禁止模式（clawhub/PostgreSQL/MCP/tenant等）在中文SKILL.md中无法检测。攻击者只需在品牌词前后紧邻中文字符即可绕过所有检测。第5轮必须验证修复后的正则是否能正确检测中文上下文中的品牌词。

2. **P1-4**: 反引号计数逻辑错误导致代码块内品牌词不被检测 — 代码块内的`clawhub`等烙印词因triple backticks误判而被跳过。第5轮需验证代码块内是否仍有未检测的烙印词。

3. **P1-7**: ALLOWED_CONTEXTS不完整 — PostgreSQL在正文中的误报/漏报需确认。clawhub是否应加入ALLOWED_CONTEXTS需要安全合规角度的判断（建议不加，clawhub是平台烙印词，应通过修复正则来检测而非白名单跳过）。

### 6.2 数据安全相关

4. **外键约束未启用（P1-2）**: 可能导致孤儿记录，影响数据完整性审计。
5. **无事务边界（P1-8）**: 并发写入时数据一致性无法保证，审计追踪可能不完整。
6. **versions表未填充content_hash（P1-10）**: 无法验证文件内容是否被篡改，影响版本完整性审计。
7. **analyze_status.py:174 f-string SQL拼接（P2-12）**: 虽然当前非 exploitable，但从安全合规角度应修复。

### 6.3 合规相关

8. **GitHub URL检测（行37）**: `r'https?://github\.com/\S+'`会匹配所有GitHub URL。需确认是否有合法的GitHub URL引用（如License链接、参考实现链接）被误报。
9. **原作者署名检测（行41-42）**: `author:\s*\S+`和`created by\s+\w+`的正则较宽泛，可能误报合法的"author"字段（如配置文件中的author属性）。第5轮需验证是否有误报。
10. **License合规审核**: 规范步骤7要求License审核，但代码层面无License信息校验逻辑。需确认License审核是否完全依赖人工流程。
11. **memory-fortress-pro的License与版权声明章节**: 需验证专业版的License信息是否与免费版一致，是否有合规风险。

### 6.4 第5轮需额外检查的代码路径

- `d:\skills\skill-registry\db.py` — 数据存储安全性
- `d:\skills\skill-registry\check_debranding.py` — 检测绕过风险
- `d:\skills\skill-registry\scan_and_import.py` — 导入过程安全性（行164: `f"https://clawhub.ai/{original_slug}"` 硬编码了原平台URL）
- 各SKILL.md中的License章节 — 合规性
- 各SKILL.md中的GitHub URL — 是否有应去除的原仓库链接

---

## 附录：审核方法论

### 审核工具
1. 静态代码审查：逐行阅读db.py（429行）、check_debranding.py（220行）全部代码
2. 动态验证：编写4个验证脚本，实际运行检测正则、数据库状态、内容重叠度、代码一致性
3. 交叉验证：对比规范文档描述与实际代码实现，识别矛盾点

### 验证脚本清单
| 脚本 | 用途 | 关键发现 |
|------|------|----------|
| verify_db.py | 数据库实际状态验证 | 确认edition/parent_slug缺失、3张死表、外键未启用 |
| verify_debranding.py | 检测脚本误报验证 | 发现`\b`正则在中文上下文失效 |
| debug_regex.py | 正则表达式深入调试 | 确认`\w`匹配中文导致`\b`失效，re.ASCII可修复 |
| compare_memory.py | free vs pro内容重叠度分析 | 量化重叠率46.8%，新增内容53.2% |
| verify_consistency.py | 规范步骤9代码一致性验证 | 确认register_skill缺edition/parent_slug参数 |

### 审核覆盖度
- db.py: 10/10函数全部审核
- check_debranding.py: 5/5函数全部审核 + 15条正则全部验证
- aws-agent-orchestrator-pro/SKILL.md: MCP引用(8处)+CLI命令表 完整审核
- memory-fortress-pro/SKILL.md: 26章节逐行对比 + 六层架构完整性检查
- 规范步骤9代码: 3个函数调用与db.py签名逐一比对
