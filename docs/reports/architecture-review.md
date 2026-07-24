# Skill生产规范v1.1改造效果 — 第2轮架构审核报告

> **审核角色**：资深系统架构师
> **审核轮次**：第2轮（共5轮串联审核）
> **前置输入**：第1轮QA工程师审核报告（70/100）
> **审核日期**：2026-07-18
> **审核范围**：数据库架构、数据流架构、规范自身一致性、改造效果架构评估、可扩展性分析

---

## 一、总体评分

### 架构评分：65 / 100

| 维度 | 满分 | 得分 | 说明 |
|------|------|------|------|
| 数据库表结构设计 | 20 | 12 | 8表分离合理，但3张死表浪费、edition/parent_slug缺失、外键未启用 |
| 数据流完整性 | 20 | 11 | 核心CRUD可用，但评分无持久化、状态机断裂、无事务边界 |
| 规范与实现一致性 | 20 | 10 | 规范声称的edition/parent_slug在DB完全未落地，10步工作流仅3步有DB操作 |
| 改造文件架构合理性 | 20 | 16 | 双版本结构清晰、edition字段已用，但parent_slug在文件层也缺失 |
| 可扩展性 | 20 | 16 | SQLite可支撑660+skill，但批量脚本效率低、N+1查询、无WAL模式 |
| **合计** | **100** | **65** | |

### 与第1轮QA评分对比

| 轮次 | 评分 | 核心发现 |
|------|------|----------|
| 第1轮 QA | 70/100 | 2项P0 + 12项P1，聚焦字段缺失与文档不一致 |
| 第2轮 架构 | 65/100 | 确认P0升级影响范围，新增3项架构级P0（评分无持久化、状态机断裂、事务无边界） |

> **评分下降原因**：QA工程师从"字段是否存在"角度审核，架构师从"系统是否能运转"角度审核。架构审核发现v1.1的核心价值主张（edition区分双版本、8大维度评分卡、10步含回流工作流）在数据库层面几乎完全未落地，这是比字段缺失更严重的架构级问题。

---

## 二、架构问题清单（P0/P1/P2分级）

### P0问题（必须修复，阻断发布）

#### P0-1：`skills`主表缺失`edition`列 — v1.1核心特性未落地

**严重度**：阻断
**影响范围**：全部双版本skill的数据库追踪

**现状**：
- 规范第2.1节明确声明"使用edition字段区分free/pro"
- 规范第9.2节映射表写明"双版本生成 → skills (edition字段) → 区分free/pro"
- 但`db.py`第28-51行`skills`表CREATE语句中**无`edition`列**
- `register_skill()`函数签名（第226-229行）**不接受`edition`参数**
- 唯一有`edition`列的是`pricing`表（第107行），但pricing表是定价记录，不是skill主属性

**架构影响**：
```
规范声称：skills.edition = 'free' | 'pro'  ← 区分双版本
实际实现：skills表无edition列             ← 无法区分
         pricing表有edition列             ← 但pricing是可选的，且1:N关系
```
无法执行`SELECT * FROM skills WHERE edition = 'pro'`这样的基础查询。要查专业版skill必须JOIN pricing表，这违反了"主属性应在主表"的设计原则。

#### P0-2：`parent_slug`字段完全缺失 — 双版本在DB中孤立

**严重度**：阻断
**影响范围**：免费版与专业版的关联关系

**现状**：
- 规范第2.1节明确声明"edition字段用于数据库追踪关联（两版本共享parent_slug）"
- `skills`表中**无`parent_slug`列**
- `source_slug`字段存在（第37行），但语义不同：`source_slug`指向**原始下载的skill**，不是**同一skill的另一个edition**
- 数据流中免费版和专业版作为两条独立记录插入，无任何外键或字段关联

**架构影响**：
```
aws-agent-orchestrator-free (skill_id=101, source_slug=aws-agentcore-langgraph)
aws-agent-orchestrator-pro  (skill_id=102, source_slug=aws-agentcore-langgraph)
                              ↑ 两条记录仅通过source_slug间接关联到同一原始skill
                                无法直接查询"skill 101的专业版是哪个"
```
无法执行`SELECT * FROM skills WHERE parent_slug = 'aws-agent-orchestrator'`来获取一个skill的免费版+专业版对。

#### P0-3：8大维度评分无持久化层 — 质量门禁形同虚设

**严重度**：阻断
**影响范围**：整个质量管控体系

**现状**：
- 规范第一章定义了8大维度评分（0/2/4/6分制，总分48分），评分门槛≥40分通过
- 规范第7节步骤3（改造前评分）和步骤8（改造后评分）是核心质量门禁
- 但数据库中**无`scores`表，`skills`表中也无评分字段**
- `operations`表虽可记录评分操作，但`details`是TEXT字段，评分数据无法结构化查询
- 无法执行`SELECT * FROM skills WHERE score_total >= 40`这样的门禁查询

**架构影响**：
质量门禁（<30分返工、30-39分复审、≥40分通过）完全依赖人工记忆，无数据库支撑。改造前/后评分对比、维度级短板分析、批量质量统计均无法实现。这使规范的核心价值（量化评分卡）在生产环境中无法运转。

#### P0-4：10步工作流无状态机持久化 — 回流机制无法追踪

**严重度**：阻断
**影响范围**：工作流管理与批量进度追踪

**现状**：
- 规范第7节定义了10步工作流，含3条回流路径（6→5、8→5、7.5→5）
- `skills.current_status`字段存在，但其值（`registered`/`optimized`/`pending_optimization`）与10步工作流的步骤**无映射关系**
- 无`current_step`字段记录当前处于哪一步
- 无`reflow_count`字段记录回流次数
- `operations`表记录了操作历史，但无法回答"这个skill现在卡在第几步"

**架构影响**：
```
规范工作流：步骤1→2→3→4→5→6→7→8→9→10（含3条回流）
DB状态机：  registered → optimized（仅2个状态，无步骤级追踪）
```
无法实现"查询所有卡在步骤6（去标识检测失败）的skill"这样的关键运维查询。回流机制（6→5、8→5）的发生次数、原因、耗时均无法统计。

### P1问题（重点修复，影响生产质量）

#### P1-1：规范自身frontmatter缺`edition`字段

**文件**：`d:\skills\differentiated-skills\Agents\skill-production-standards\SKILL.md` 第1-26行
**现状**：frontmatter包含slug/name/version/displayName/summary/license/description/tags/tools，但**无`edition`字段**
**违反**：规范第8.1节检查清单明确要求"edition字段（free/pro）已设置"
**影响**：规范自身不遵守自家规则，降低规范权威性

#### P1-2：check_debranding.py实现18个pattern但规范仅文档化6个

**文件**：`d:\skills\skill-registry\check_debranding.py` 第13-43行
**现状**：
- 规范第3.1节文档化6项自动化检测
- 实际代码实现18个正则模式（含平台烙印变体、内部系统词、xianyu、老田和小甜甜等）
- **更严重**：`PostgreSQL`被标记为`'high'`严重度（第22行），但规范第3.3节Allowlist明确声明PostgreSQL是合法主流数据库术语
- **更严重**：`clawhub`在FORBIDDEN_PATTERNS中（第15行），但ALLOWED_CONTEXTS中**只有`SkillHub`没有`clawhub`**，导致规范自身允许的"上传到clawhub"会被误报

**代码证据**：
```python
# check_debranding.py 第15行 - clawhub被禁止
(r'\b(clawhub|clawsec|clawdbot|openclaw)\b', '平台烙印词', 'high'),

# check_debranding.py 第22行 - PostgreSQL被禁止
(r'\bPostgreSQL\b', '内部系统词-PostgreSQL', 'high'),

# check_debranding.py 第46-54行 - ALLOWED_CONTEXTS不含clawhub和PostgreSQL
ALLOWED_CONTEXTS = [
    'SkillHub', 'skillhub.cn', 'SkillPay',
    '工具协议', 'Agent工具协议', 'transport', 'Transport',
]
```

#### P1-3：3张死表（skills_fts / sources / dependencies）

**现状**：
- `skills_fts`（第147-151行）：FTS5虚拟表已创建，但全代码库中**无任何INSERT语句**向其写入数据。全文搜索功能完全不可用。
- `sources`（第119-132行）：来源信息表已创建，但`register_skill()`将来源信息直接写入`skills.source_*`字段，**从不写入`sources`表**。该表永远为空。
- `dependencies`（第134-144行）：依赖关系表已创建，但**无任何代码**向其写入。skill间依赖关系完全未追踪。

**架构建议**：
- `sources`表与`skills.source_*`字段功能重叠，违反DRY原则。建议删除`sources`表，或反过来将来源信息规范化到`sources`表并在`skills`中仅保留外键。
- `skills_fts`应通过触发器或应用层同步数据，否则删除。
- `dependencies`表若要启用，需在`register_skill()`中增加依赖参数。

#### P1-4：SQLite外键约束未启用

**现状**：
- `db.py`中所有子表都声明了`FOREIGN KEY (skill_id) REFERENCES skills(id)`
- 但**从未执行`PRAGMA foreign_keys = ON`**
- SQLite默认外键约束为OFF，因此所有FOREIGN KEY声明均为**无效装饰**
- 删除skill时不会级联删除versions/operations/pricing等子表记录，产生孤儿数据

**代码证据**：
```python
# db.py 第24行 - 连接后直接创建表，未执行PRAGMA
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
# 缺少：c.execute("PRAGMA foreign_keys = ON")
```

#### P1-5：无事务边界 — register_skill/set_pricing/record_operation各自独立提交

**现状**：
- `register_skill()`（第226-281行）：打开连接→INSERT skill→INSERT version→INSERT operation→commit→关闭
- `set_pricing()`（第325-340行）：打开连接→INSERT pricing→commit→关闭
- `record_operation()`（第310-322行）：打开连接→INSERT operation→commit→关闭
- 规范步骤9要求三个函数依次调用形成"注册免费版→注册专业版→设置定价→记录操作"的完整事务
- 但如果`set_pricing()`在`register_skill()`后失败，**已注册的skill无定价记录，且无法回滚**

**架构影响**：
```
规范步骤9调用链：
  register_skill(free) → 成功commit
  register_skill(pro)  → 成功commit
  set_pricing(pro)     → 失败（异常）
  record_operation()   → 未执行
  
结果：专业版skill已注册但无定价，无操作记录，数据不一致
```

#### P1-6：`current_status`值域与10步工作流无映射

**现状**：
- `current_status`的已知值：`registered`、`optimized`、`pending_optimization`
- 10步工作流的步骤：1(分析)→2(研究)→3(评分)→4(设计)→5(重写)→6(去标识)→7(License)→8(评分)→9(登记)→10(上传)
- 两者之间**无映射关系**，无法从`current_status`判断skill处于工作流哪一步

#### P1-7：`versions`表关键字段未填充

**现状**：
- `versions`表有`content_hash`、`file_size`、`line_count`、`changes_summary`字段（第58-61行）
- 但`register_skill()`的INSERT语句（第268-271行）**仅填充`skill_id`、`version`、`created_at`、`changelog`**
- `compute_file_hash()`函数（第168-174行）存在但**未在register_skill中调用**
- `scan_and_import.py`计算了file_hash但存入`notes`字段而非`versions`表

#### P1-8：`pricing`表无法追踪定价历史

**现状**：
- `pricing`表有`effective_date`但**无`end_date`或`is_active`字段**
- 每次调用`set_pricing()`都INSERT新记录，但无法标记旧记录为"已失效"
- 无法查询"某skill在2026年3月的价格"，无法追踪免费→付费转化时间线
- 无法执行`SELECT * FROM pricing WHERE skill_id = ? AND is_active = 1`查当前有效定价

#### P1-9：索引设计不充分

**缺失索引**：
| 缺失索引 | 影响查询 | 预期性能影响 |
|----------|----------|-------------|
| `pricing(skill_id)` | `get_skill_status()`查定价 | 全表扫描 |
| `skills(is_differentiated)` | `get_skills_needing_work()`查未差异化 | 全表扫描 |
| `skills(skill_type)` | 按类型筛选skill | 全表扫描 |
| `skills(pricing_model)` | 按定价模型筛选 | 全表扫描 |
| `skills(edition)` (待添加) | 按免费/专业版筛选 | 全表扫描 |
| `skills(parent_slug)` (待添加) | 查双版本关联 | 全表扫描 |

#### P1-10：`list_all_skills()`存在N+1查询问题

**现状**（第385-392行）：
```sql
SELECT s.*,
    (SELECT COUNT(*) FROM platform_uploads WHERE skill_id = s.id AND upload_status = 'success') as upload_count,
    (SELECT MAX(upload_date) FROM platform_uploads WHERE skill_id = s.id) as last_upload,
    (SELECT GROUP_CONCAT(DISTINCT platform) FROM platform_uploads WHERE skill_id = s.id AND upload_status = 'success') as platforms_uploaded
FROM skills s
ORDER BY s.category, s.slug
```
每行3个相关子查询。660个skill = 1980次子查询执行。应改为LEFT JOIN + GROUP BY。

#### P1-11：去标识检测结果未更新`skills.current_status`

**现状**：
- `check_debranding.py`的`update_database_with_check_results()`（第166-205行）向`operations`表写入检测结果
- 但**不更新`skills.current_status`**
- 检测失败的skill状态仍为`optimized`，不会被标记为`debranding_failed`
- 工作流步骤6（去标识检测）的通过/失败结果无法从`skills`表直接查询

#### P1-12：License审核结果无结构化存储

**现状**：
- 规范第四章定义了License审核流程（MIT/BSD/Apache兼容，GPL/AGPL不兼容）
- `skills.source_license`字段存储原始license（第40行）
- 但**License审核结果（兼容/不兼容/跳过）无专门字段或表存储**
- 无法查询"哪些skill因GPL license被跳过"

### P2问题（建议优化）

#### P2-1：SLUG_MAPPING硬编码在脚本中

**文件**：`d:\skills\skill-registry\scan_and_import.py` 第47-105行
**现状**：64个slug映射关系硬编码在Python字典中
**问题**：新增skill需修改代码而非数据，违反开闭原则。应迁移到数据库表或配置文件。

#### P2-2：无WAL模式，并发读写受限

**现状**：未设置`PRAGMA journal_mode=WAL`
**影响**：批量改造时若同时查询数据库（如`list_all_skills()`），写入操作会阻塞读取。

#### P2-3：无数据库Schema迁移版本管理

**现状**：`init_database()`使用`CREATE TABLE IF NOT EXISTS`，无法做Schema升级
**影响**：添加edition/parent_slug等列需要手动ALTER TABLE，无迁移脚本管理。

#### P2-4：免费版/专业版在文件层无显式parent_slug

**现状**：
- `aws-agent-orchestrator-pro/SKILL.md` frontmatter有`edition: pro`但无`parent_slug`字段
- `local-vector-memory-pro/SKILL.md` frontmatter有`edition: pro`但无`parent_slug`字段
- 双版本关联仅依赖目录命名约定（`-free`/`-pro`后缀），无显式关联字段
- 若文件被重命名，关联关系即丢失

#### P2-5：`compute_file_hash()`未被版本管理调用

**现状**：函数存在于`db.py`但仅被`scan_and_import.py`调用，结果存入`notes`字段。`register_skill()`未调用它来填充`versions.content_hash`。

#### P2-6：无连接池/上下文管理器模式

**现状**：每个函数独立`sqlite3.connect()` + `close()`，无连接复用。批量处理660个skill时频繁创建/销毁连接。

---

## 三、数据库架构改进方案（具体SQL迁移语句）

### 3.1 P0修复：添加edition和parent_slug列

```sql
-- ============ P0-1: 添加edition列 ============
ALTER TABLE skills ADD COLUMN edition TEXT DEFAULT 'free';
-- 填充已有数据：根据slug后缀推断edition
UPDATE skills SET edition = 'pro' WHERE slug LIKE '%-pro';
UPDATE skills SET edition = 'free' WHERE slug LIKE '%-free' OR slug NOT LIKE '%-pro';
-- 添加索引
CREATE INDEX IF NOT EXISTS idx_skills_edition ON skills(edition);

-- ============ P0-2: 添加parent_slug列 ============
ALTER TABLE skills ADD COLUMN parent_slug TEXT;
-- 填充已有数据：从slug推断parent_slug
UPDATE skills SET parent_slug = REPLACE(REPLACE(slug, '-pro', ''), '-free', '')
WHERE slug LIKE '%-pro' OR slug LIKE '%-free';
-- 添加索引
CREATE INDEX IF NOT EXISTS idx_skills_parent_slug ON skills(parent_slug);
```

### 3.2 P0修复：评分持久化表

```sql
-- ============ P0-3: 创建评分表 ============
CREATE TABLE IF NOT EXISTS skill_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id INTEGER NOT NULL,
    score_type TEXT NOT NULL,  -- 'pre' (改造前) 或 'post' (改造后)
    dimension TEXT NOT NULL,   -- 'quality'/'practicality'/'simplicity'/'cost'/'performance'/'debranding'/'compliance'/'differentiation'
    score INTEGER NOT NULL,    -- 0/2/4/6
    max_score INTEGER DEFAULT 6,
    scored_at TEXT NOT NULL,
    scored_by TEXT,            -- 'architect'/'qa'/'automated'
    notes TEXT,
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);

-- 评分汇总视图（便于门禁查询）
CREATE VIEW IF NOT EXISTS v_skill_score_summary AS
SELECT 
    skill_id,
    score_type,
    SUM(score) as total_score,
    SUM(max_score) as max_total,
    ROUND(CAST(SUM(score) AS FLOAT) / SUM(max_score) * 100, 1) as pass_percentage,
    CASE 
        WHEN SUM(score) >= 40 THEN 'pass'
        WHEN SUM(score) >= 30 THEN 'review'
        ELSE 'fail'
    END as gate_status
FROM skill_scores
GROUP BY skill_id, score_type;

-- 索引
CREATE INDEX IF NOT EXISTS idx_scores_skill ON skill_scores(skill_id);
CREATE INDEX IF NOT EXISTS idx_scores_type ON skill_scores(score_type);
```

### 3.3 P0修复：工作流状态机表

```sql
-- ============ P0-4: 创建工作流状态追踪表 ============
CREATE TABLE IF NOT EXISTS workflow_state (
    skill_id INTEGER PRIMARY KEY,
    current_step INTEGER NOT NULL DEFAULT 1,  -- 1-10 对应规范10步
    current_status TEXT NOT NULL DEFAULT 'pending',  -- pending/in_progress/passed/failed/skipped
    reflow_count INTEGER DEFAULT 0,
    last_step_change_at TEXT NOT NULL,
    last_reflow_from_step INTEGER,
    last_reflow_reason TEXT,
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);

-- 步骤状态明细表（记录每一步的执行历史）
CREATE TABLE IF NOT EXISTS workflow_step_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id INTEGER NOT NULL,
    step_number INTEGER NOT NULL,
    step_name TEXT NOT NULL,
    started_at TEXT,
    completed_at TEXT,
    status TEXT NOT NULL,  -- pending/in_progress/passed/failed/reflowed/skipped
    details TEXT,
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);

CREATE INDEX IF NOT EXISTS idx_workflow_status ON workflow_state(current_status);
CREATE INDEX IF NOT EXISTS idx_workflow_step ON workflow_state(current_step);
CREATE INDEX IF NOT EXISTS idx_step_history_skill ON workflow_step_history(skill_id);
```

### 3.4 P1修复：外键约束启用 + 定价历史

```sql
-- ============ P1-4: 启用外键约束（需在每次连接时执行） ============
-- 注意：SQLite的PRAGMA foreign_keys是连接级设置，需在代码中修改
-- db.py中所有sqlite3.connect()后应添加：
--   c.execute("PRAGMA foreign_keys = ON")
-- 或在init_database()中设置并使用连接池统一管理

-- ============ P1-8: pricing表添加历史追踪字段 ============
ALTER TABLE pricing ADD COLUMN end_date TEXT;
ALTER TABLE pricing ADD COLUMN is_active INTEGER DEFAULT 1;
CREATE INDEX IF NOT EXISTS idx_pricing_skill ON pricing(skill_id);
CREATE INDEX IF NOT EXISTS idx_pricing_active ON pricing(is_active);

-- 当设置新定价时，旧定价自动失效（需在set_pricing()代码中实现）
-- UPDATE pricing SET is_active = 0, end_date = ? WHERE skill_id = ? AND is_active = 1;
```

### 3.5 P1修复：补充缺失索引

```sql
-- ============ P1-9: 补充缺失索引 ============
CREATE INDEX IF NOT EXISTS idx_skills_is_differentiated ON skills(is_differentiated);
CREATE INDEX IF NOT EXISTS idx_skills_skill_type ON skills(skill_type);
CREATE INDEX IF NOT EXISTS idx_skills_pricing_model ON skills(pricing_model);
-- idx_skills_edition 和 idx_skills_parent_slug 已在3.1中创建
```

### 3.6 P1修复：死表处理

```sql
-- ============ P1-3: 死表处理 ============

-- 方案A：删除死表（推荐，当前完全未使用）
-- DROP TABLE IF EXISTS skills_fts;
-- DROP TABLE IF EXISTS sources;
-- DROP TABLE IF EXISTS dependencies;

-- 方案B：激活使用（若计划未来使用）

-- skills_fts激活：通过触发器自动同步
CREATE TRIGGER IF NOT EXISTS trg_skills_ai_fts AFTER INSERT ON skills BEGIN
    INSERT INTO skills_fts(slug, name, display_name, description, tags, category)
    VALUES (NEW.slug, NEW.current_name, NEW.current_display_name, NEW.notes, '', NEW.category);
END;

CREATE TRIGGER IF NOT EXISTS trg_skills_ad_fts AFTER DELETE ON skills BEGIN
    DELETE FROM skills_fts WHERE slug = OLD.slug;
END;

-- sources激活：将skills表中的source_*字段规范化到sources表
-- （需要数据迁移脚本，将skills.source_*复制到sources表，skills中改为source_id外键）

-- dependencies激活：在register_skill()中增加depends_on参数
```

### 3.7 P1修复：N+1查询优化

```sql
-- ============ P1-10: list_all_skills()查询优化 ============
-- 原SQL（3个相关子查询/行）改为JOIN+GROUP BY：

CREATE VIEW IF NOT EXISTS v_skills_with_uploads AS
SELECT 
    s.*,
    COALESCE(uc.upload_count, 0) as upload_count,
    uc.last_upload,
    uc.platforms_uploaded
FROM skills s
LEFT JOIN (
    SELECT 
        skill_id,
        SUM(CASE WHEN upload_status = 'success' THEN 1 ELSE 0 END) as upload_count,
        MAX(upload_date) as last_upload,
        GROUP_CONCAT(DISTINCT CASE WHEN upload_status = 'success' THEN platform END) as platforms_uploaded
    FROM platform_uploads
    GROUP BY skill_id
) uc ON s.id = uc.skill_id
ORDER BY s.category, s.slug;
```

### 3.8 完整迁移脚本框架

```python
# migrate_v1_1.py — Schema迁移脚本
"""
Skill Registry Database v1.1 Migration
执行所有P0/P1级别的Schema修复
"""
import sqlite3

DB_PATH = r"d:\skills\skill-registry.db"

def migrate():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 启用外键
    c.execute("PRAGMA foreign_keys = ON")
    
    # 1. 添加edition列
    try:
        c.execute("ALTER TABLE skills ADD COLUMN edition TEXT DEFAULT 'free'")
        print("[OK] Added edition column")
    except sqlite3.OperationalError:
        print("[SKIP] edition column already exists")
    
    # 2. 添加parent_slug列
    try:
        c.execute("ALTER TABLE skills ADD COLUMN parent_slug TEXT")
        print("[OK] Added parent_slug column")
    except sqlite3.OperationalError:
        print("[SKIP] parent_slug column already exists")
    
    # 3. 填充edition数据
    c.execute("UPDATE skills SET edition = 'pro' WHERE slug LIKE '%-pro' AND edition = 'free'")
    c.execute("UPDATE skills SET edition = 'free' WHERE slug LIKE '%-free'")
    print(f"[OK] Updated edition data: {c.rowcount} rows")
    
    # 4. 填充parent_slug数据
    c.execute("""
        UPDATE skills SET parent_slug = REPLACE(REPLACE(slug, '-pro', ''), '-free', '')
        WHERE (slug LIKE '%-pro' OR slug LIKE '%-free') AND parent_slug IS NULL
    """)
    print(f"[OK] Updated parent_slug data: {c.rowcount} rows")
    
    # 5. 创建评分表
    c.execute("""...""")  # 见3.2
    
    # 6. 创建工作流状态表
    c.execute("""...""")  # 见3.3
    
    # 7. 补充索引
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_edition ON skills(edition)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_parent_slug ON skills(parent_slug)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_is_differentiated ON skills(is_differentiated)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_skills_skill_type ON skills(skill_type)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_pricing_skill ON pricing(skill_id)")
    
    # 8. pricing表添加历史字段
    try:
        c.execute("ALTER TABLE pricing ADD COLUMN end_date TEXT")
        c.execute("ALTER TABLE pricing ADD COLUMN is_active INTEGER DEFAULT 1")
        print("[OK] Added pricing history columns")
    except sqlite3.OperationalError:
        print("[SKIP] pricing columns already exist")
    
    conn.commit()
    conn.close()
    print("Migration complete.")

if __name__ == '__main__':
    migrate()
```

---

## 四、通过项清单

以下架构设计经审核确认合理，应保持：

| 序号 | 通过项 | 验证结论 |
|------|--------|----------|
| 1 | 8表分离的总体设计 | skills/versions/operations/platform_uploads/pricing的职责分离合理，符合关注点分离原则 |
| 2 | `pricing`表包含`edition`字段 | 虽然主表缺失，但pricing表已有edition列，set_pricing()函数签名正确接受edition参数 |
| 3 | `set_pricing()`函数设计 | 参数完整（edition/price_model/price_amount/price_currency/trial_limits/pro_features），调用方式与规范步骤9示例匹配 |
| 4 | `record_operation()`支持before_state/after_state | 可记录操作前后的状态变化，为工作流追踪提供基础 |
| 5 | `get_skill_status()`一站式查询 | 一次调用返回skill+versions+operations+uploads+pricing完整信息，API设计友好 |
| 6 | `get_skills_needing_work()`分流查询 | 分别返回needs_optimization和needs_upload，支持工作流分流 |
| 7 | check_debranding.py的ALLOWED_CONTEXTS机制 | 上下文感知检测的设计方向正确（虽列表不完整） |
| 8 | check_debranding.py的代码块排除逻辑 | 反引号包裹的命令行参数和三反引号代码块中的技术术语被正确跳过 |
| 9 | check_debranding.py的exclude_dirs机制 | 排除skill-production-standards自身，避免规范文档中的检测规则示例被误报 |
| 10 | check_debranding.py的update_database_with_check_results() | 检测结果写入operations表，实现了检测→DB的集成（虽不完整） |
| 11 | 改造后skill文件的edition字段 | aws-agent-orchestrator-pro和local-vector-memory-pro的frontmatter均正确设置`edition: pro` |
| 12 | 改造后skill文件的双版本结构 | 免费版有"免费版限制"章节、专业版有"专业版特性"+"定价"章节，符合规范2.2/2.3 |
| 13 | 改造后skill文件的License声明 | 两个专业版均包含"License与版权声明"章节，保留原始作品/license/改进license，符合规范4.2 |
| 14 | 改造后skill文件的references分层 | aws-agent-orchestrator-pro使用references/子目录分层加载，符合规范维度4（LLM成本）按需加载 |
| 15 | 规范的回流机制设计 | 步骤6→5、8→5、7.5→5的回流路径在流程图中正确标注（虽DB未落地） |
| 16 | 规范的0/2/4/6评分制设计 | 相比0/3/5制避免激励扭曲，设计理由充分 |
| 17 | scan_and_import.py的多目录扫描 | 支持4种来源目录（clawhub下载/差异化/开源改造/原创），source字段区分 |
| 18 | 规范的API Token安全处理 | 第6.3节明确禁止硬编码Token，要求存储在gitignore目录，安全意识到位 |
| 19 | 目录结构按category组织 | Agents/Automation分类清晰，skill以slug为目录名，扁平化便于管理 |
| 20 | compute_file_hash()使用SHA256 | 文件哈希算法选择正确，8192字节分块读取避免大文件内存溢出 |

---

## 五、给后续3轮（PM/开发者/安全合规）的传递注意事项

### 5.1 传递给第3轮PM（产品经理）的注意事项

1. **edition字段缺失的业务影响**：PM需评估"免费版/专业版在数据库中无法直接区分"对商业化运营报表的影响。当前要统计专业版skill数量必须JOIN pricing表，且pricing表可能为空（未调用set_pricing的skill）。

2. **评分无持久化的产品影响**：PM定义的8大维度评分卡（规范核心卖点）在DB中无法存储。PM需决定：(a) 评分是否需要持久化？(b) 评分历史是否需要留存供改进对比？(c) 评分是否作为上架门禁的硬性条件（需要DB查询支撑）？

3. **parent_slug缺失的转化追踪影响**：PM需评估"无法从DB查询免费版→专业版的转化率"是否影响运营。当前无法执行"查询所有有免费版但无专业版的skill"这样的转化漏斗分析。

4. **定价历史缺失的影响**：pricing表无end_date/is_active，PM需决定是否需要追踪定价变更历史（如促销价→正价→降价）。

5. **工作流状态不可查询的影响**：PM需评估"无法查看660+skill各自处于改造流程哪一步"是否影响项目管理可视化。当前仅能区分"已差异化/未差异化"两个粗粒度状态。

6. **死表的产品决策**：PM需决定sources/dependencies/skills_fts三张表是删除还是激活。如果激活，需排期开发对应的数据写入逻辑。

### 5.2 传递给第4轮开发者（Developer）的注意事项

1. **register_skill()签名需扩展**：必须增加`edition`和`parent_slug`参数。修改后需同步更新scan_and_import.py和update_v2_and_report.py中的调用。

2. **事务边界需重构**：建议引入`@contextmanager`或连接池模式，将register_skill+set_pricing+record_operation包装在单个事务中。示例：
   ```python
   with db_transaction() as conn:
       free_id = register_skill(conn=conn, ...)
       pro_id = register_skill(conn=conn, ...)
       set_pricing(conn=conn, skill_id=pro_id, ...)
       record_operation(conn=conn, skill_id=free_id, ...)
   ```

3. **PRAGMA foreign_keys = ON**：必须在每个`sqlite3.connect()`后执行。建议封装`get_connection()`工具函数统一处理。

4. **check_debranding.py需修复ALLOWED_CONTEXTS**：
   - 添加`'clawhub'`到ALLOWED_CONTEXTS（规范3.3明确允许作为目标平台名）
   - 添加PostgreSQL的合法上下文（如`'数据库'`、`'data source'`、`'数据源'`）
   - 或者将PostgreSQL从FORBIDDEN_PATTERNS移除，改为仅在特定上下文检测

5. **versions表需完整填充**：register_skill()中应调用compute_file_hash()并填充content_hash/file_size/line_count字段。

6. **list_all_skills()需重构**：从相关子查询改为LEFT JOIN（见3.7），避免660+skill时的N+1性能问题。

7. **check_debranding.py需更新skills.current_status**：检测失败时应将status设为`debranding_failed`，检测通过时设为`debranding_passed`。

8. **需创建migrate_v1_1.py迁移脚本**：按第三节SQL语句编写，确保现有数据不丢失。

### 5.3 传递给第5轮安全合规（Security & Compliance）的注意事项

1. **外键约束未启用的数据完整性风险**：FK未启用意味着可向versions/operations/pricing插入不存在的skill_id，产生孤儿数据。安全合规需评估这是否构成数据完整性风险。

2. **API Token存储路径**：规范第6.3节要求Token存储在`d:\skills\.skillhub-credentials\`和`d:\skills\.clawhub-credentials\`。安全合规需验证：(a) 这些目录是否已gitignore？(b) 文件权限是否限制为当前用户？(c) 是否有日志泄露风险？

3. **check_debranding.py的误报风险**：PostgreSQL和clawhub被误报为禁止词，可能导致开发者为了通过检测而删除合法的技术引用，影响skill质量。安全合规需评估误报对合规检测可信度的影响。

4. **License审核结果未存储**：source_license字段存储了原始license，但审核结果（兼容/不兼容/跳过）无记录。安全合规需决定是否需要审计追踪License审核决策。

5. **去标识检测的18个pattern中有内部代号**：`'老田和小甜甜'`、`'xianyu'`等内部代号出现在检测脚本中。安全合规需评估这些代号本身是否构成信息泄露（虽在本地脚本中，但若仓库公开则有风险）。

6. **SLUG_MAPPING硬编码64个映射**：包含原始slug信息（如`'totalreclaw'`、`'kyaukyuai-linear-cli'`），这些是去标识应清除的原始标识。安全合规需评估此映射表是否应从代码中移至gitignore的配置文件。

7. **数据库文件无加密**：`skill-registry.db`为明文SQLite文件，包含所有skill的元数据。安全合规需评估是否需要加密或限制文件访问权限。

---

## 六、可扩展性评估报告

### 6.1 当前架构对660+skill批量改造的支撑能力

| 评估维度 | 当前能力 | 660+skill需求 | 差距 | 风险等级 |
|----------|----------|---------------|------|----------|
| 数据存储容量 | SQLite单文件 | 660条skill + 版本/操作/上传记录 | SQLite轻松支撑百万级记录，无容量风险 | 低 |
| 批量导入性能 | 每skill 2次连接+2次commit | 660×2=1320次连接/提交 | 预计耗时5-10分钟，可接受但需优化 | 中 |
| 查询性能 | list_all_skills有N+1问题 | 660行×3子查询=1980次 | 预计3-5秒，需优化为JOIN | 中 |
| 去标识检测 | 串行扫描所有SKILL.md | 660个文件×18正则 | 预计30-60秒，可接受 | 低 |
| 状态追踪 | 仅2个粗粒度状态 | 需10步工作流级追踪 | 完全无法支撑批量进度管理 | 高 |
| 评分统计 | 无评分持久化 | 需按维度/总分统计 | 完全无法支撑质量统计 | 高 |
| 并发写入 | SQLite单写入锁 | 批量改造可能多进程 | 需WAL模式或串行化 | 中 |

### 6.2 数据库性能瓶颈分析

**瓶颈1：连接管理（中风险）**
```
当前：每个register_skill()调用 = 1次connect + 3次INSERT + 1次commit + 1次close
660个skill = 660次完整连接生命周期
优化：使用连接池 + 批量commit（每50个skill提交一次）
预期：耗时从5-10分钟降至30-60秒
```

**瓶颈2：N+1查询（中风险）**
```
当前：list_all_skills() = 1次主查询 + 660×3次子查询 = 1981次查询
优化：改为LEFT JOIN + GROUP BY = 1次查询
预期：耗时从3-5秒降至<0.5秒
```

**瓶颈3：去标识检测串行（低风险）**
```
当前：check_all_skills()串行扫描660个文件
优化：可并行化（multiprocessing.Pool），但660个文件30-60秒可接受
```

**瓶颈4：WAL模式缺失（中风险）**
```
当前：默认journal_mode=DELETE，写入时阻塞读取
660+skill批量导入时，若同时查询状态会导致"database is locked"错误
优化：PRAGMA journal_mode=WAL（允许并发读+单写）
```

### 6.3 批量处理脚本优化建议

**1. scan_and_import.py优化**
```python
def import_skills_to_db_batch(skills, batch_size=50):
    """批量导入：使用单连接+批量提交"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode=WAL")
    c = conn.cursor()
    
    for i, skill in enumerate(skills):
        # 单条INSERT，但不立即commit
        _register_skill_with_conn(c, skill)
        
        # 每batch_size条提交一次
        if (i + 1) % batch_size == 0:
            conn.commit()
            print(f"  Committed batch {(i+1)//batch_size}: {i+1} skills")
    
    conn.commit()  # 提交剩余记录
    conn.close()
```

**2. register_skill()支持连接注入**
```python
def register_skill(slug, name, ..., conn=None):
    """支持外部注入连接，实现事务复用"""
    own_connection = conn is None
    if own_connection:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    
    # ... 业务逻辑 ...
    
    if own_connection:
        conn.commit()
        conn.close()
    # 若conn由外部传入，由外部决定commit/close
```

**3. check_debranding.py并行化**
```python
from multiprocessing import Pool, cpu_count

def check_all_skills_parallel(directory, exclude_dirs=None):
    """并行扫描所有SKILL.md"""
    files = list(Path(directory).rglob('SKILL.md'))
    if exclude_dirs:
        files = [f for f in files if not any(ex in str(f) for ex in exclude_dirs)]
    
    with Pool(min(cpu_count(), 8)) as pool:
        results_list = pool.map(check_single_file_wrapper, files)
    
    return dict(zip([str(f) for f in files], results_list))
```

### 6.4 可扩展性综合结论

**结论：当前架构在存储层面可支撑660+skill，但在管理层面存在严重缺口。**

| 层面 | 评估 | 说明 |
|------|------|------|
| 存储容量 | 通过 | SQLite轻松支撑660+skill及其历史记录 |
| 导入性能 | 需优化 | 连接管理+批量提交可将5-10分钟降至<1分钟 |
| 查询性能 | 需优化 | N+1查询需改为JOIN，添加缺失索引 |
| 状态管理 | 不通过 | 10步工作流无状态机，660个skill的进度无法追踪 |
| 质量统计 | 不通过 | 评分无持久化，无法统计660个skill的质量分布 |
| 并发支持 | 需优化 | 需启用WAL模式支持批量写入时的并发读取 |
| 检测性能 | 通过 | 串行扫描660个文件30-60秒可接受，可进一步并行化 |

**关键风险**：若不修复P0-3（评分持久化）和P0-4（工作流状态机），660+skill的批量改造将无法进行进度管理和质量门禁统计，相当于"盲飞"。

---

## 七、规范与实现一致性验证明细

### 7.1 数据库函数签名对照表

| 规范描述（第9.1节） | 实际签名 | 一致性 | 问题 |
|---------------------|----------|--------|------|
| `register_skill()`必填: slug, name, version, category, source, local_path | `register_skill(slug, name, display_name, version, category, source, local_path, ...)` | 不一致 | `display_name`为必填但规范未列出 |
| `record_upload()`必填: skill_id, version, platform, platform_slug, upload_status | `record_upload(skill_id, version, platform, platform_slug, upload_status, ...)` | 一致 | - |
| `record_operation()`必填: skill_id, operation_type, details | `record_operation(skill_id, operation_type, details, ...)` | 一致 | - |
| `set_pricing()`必填: skill_id, edition, price_model, price_amount | `set_pricing(skill_id, edition, price_model, price_amount, ...)` | 一致 | - |
| 规范步骤9示例调用`register_skill(source_license='MIT')` | 实际支持`source_license`参数 | 一致 | - |
| 规范声称`register_skill()`应支持edition | 实际**不支持**edition参数 | **不一致** | P0-1 |
| 规范声称应支持parent_slug关联 | 实际**不支持**parent_slug参数 | **不一致** | P0-2 |

### 7.2 10步工作流DB操作映射表

| 步骤 | 步骤名称 | 规范描述 | DB操作 | 状态 | 问题 |
|------|----------|----------|--------|------|------|
| 1 | 原始内容分析 | 读取原始SKILL.md | 无 | 缺失 | 无操作记录 |
| 2 | 痛点研究 | WebSearch痛点 | 无 | 缺失 | 无操作记录 |
| 3 | 改造前评分 | 8大维度基线评分 | 无 | **缺失** | P0-3：评分无持久化 |
| 4 | 差异化设计 | 设计改进方案 | 无 | 缺失 | 无操作记录 |
| 5 | 内容重写 | 重写SKILL.md | 无 | 缺失 | 无操作记录 |
| 6 | 去标识检测 | check_debranding.py | operations表INSERT | **部分** | P1-11：未更新current_status |
| 7 | License审核 | 查兼容性矩阵 | 无 | **缺失** | P1-12：审核结果无存储 |
| 8 | 改造后评分 | 8大维度评分 | 无 | **缺失** | P0-3：评分无持久化 |
| 9 | 数据库登记 | register_skill+set_pricing+record_operation | skills+versions+operations+pricing表INSERT | 通过 | P1-5：无事务边界 |
| 10 | 双平台上传 | record_upload | platform_uploads+operations表INSERT | 通过 | - |
| 10.5 | 上传失败重试 | 等待重试 | 无 | 缺失 | 重试结果未记录 |

**10步中仅3步有完整DB操作（步骤6部分、9、10），4步完全无DB操作（步骤1/2/4/5），3步有重大缺失（步骤3/7/8）。工作流DB覆盖率为30%。**

### 7.3 回流机制DB状态追踪验证

| 回流路径 | 规范描述 | DB追踪 | 状态 |
|----------|----------|--------|------|
| 步骤6→5（去标识检测失败→重写） | "检测失败：返回步骤5，修复后重新检测" | 无reflow_count字段 | **未实现** |
| 步骤8→5（评分<30分→重写） | "<30分：返回步骤5" | 无评分记录、无reflow记录 | **未实现** |
| 步骤7.5→5（评分30-39分→复审改进→重写） | "30-39分：进入步骤7.5复审" | 无复审记录、无reflow记录 | **未实现** |

**结论：3条回流路径在DB层面完全未实现，无法追踪回流次数、原因和耗时。**

---

## 八、改造后文件架构评估

### 8.1 aws-agent-orchestrator-pro 架构评估

**文件**：`d:\skills\differentiated-skills\Agents\aws-agent-orchestrator-pro\SKILL.md`

| 检查项 | 规范要求 | 实际情况 | 结论 |
|--------|----------|----------|------|
| edition字段 | frontmatter含edition: pro | 第29行 `edition: pro` | 通过 |
| 专业版特性章节 | "## 专业版特性" | 第520行 "## 十三、专业版特性" | 通过 |
| 定价章节 | 含定价表 | 第531行 "## 十四、定价" + 表格 | 通过 |
| License声明 | 保留原始版权 | 第542行 "## License与版权声明" | 通过 |
| 免费版引用 | 引导使用免费版 | 第19行 "免费试用请使用 aws-agent-orchestrator-free" | 通过 |
| references分层 | 按需加载 | 第478行 references/子目录6个文件 | 通过 |
| FAQ数量 | ≥10问 | 12问（Q1-Q12） | 通过 |
| 故障排查表 | ≥5项 | 12项 | 通过 |
| parent_slug字段 | 规范声称共享parent_slug | **frontmatter无parent_slug字段** | **缺失** |
| 与免费版的显式关联 | DB层面parent_slug关联 | **仅靠目录命名-implies关联** | **弱关联** |

### 8.2 local-vector-memory-pro 架构评估

**文件**：`d:\skills\differentiated-skills\Agents\local-vector-memory-pro\SKILL.md`

| 检查项 | 规范要求 | 实际情况 | 结论 |
|--------|----------|----------|------|
| edition字段 | frontmatter含edition: pro | 第8行 `edition: pro` | 通过 |
| 专业版特性章节 | "## 专业版特性" | 第203行 "## 专业版特性" | 通过 |
| 定价章节 | 含定价表 | 第571行 "## 定价" + 表格 | 通过 |
| License声明 | 保留原始版权 | 第644行 "## License 与版权声明" | 通过 |
| 免费版引用 | 引导使用免费版 | FAQ Q1/Q7引用免费版 | 通过 |
| FAQ数量 | ≥10问 | 12问 | 通过 |
| 故障排查表 | ≥5项 | 12项 | 通过 |
| 版本升级迁移指南 | 专业版应含 | 第582行 "## 版本升级迁移指南" | 通过（超出规范要求） |
| parent_slug字段 | 规范声称共享parent_slug | **frontmatter无parent_slug字段** | **缺失** |
| 与免费版的显式关联 | DB层面parent_slug关联 | **仅靠目录命名implies关联** | **弱关联** |

### 8.3 文件目录结构评估

**当前结构**：
```
d:\skills\differentiated-skills\
  Agents\
    aws-agent-orchestrator-free\    ← 免费版
      SKILL.md
    aws-agent-orchestrator-pro\     ← 专业版（兄弟目录）
      SKILL.md
      references\
    local-vector-memory-free\
      SKILL.md
    local-vector-memory-pro\
      SKILL.md
```

**评估结论**：
- **优点**：扁平化结构简单，以slug为目录名，无需嵌套。免费版和专业版作为兄弟目录，命名约定清晰。
- **问题1**：免费版和专业版之间无显式关联机制。若有人重命名目录（如`aws-agent-orchestrator-pro` → `aws-multi-agent-pro`），关联即断裂。
- **问题2**：无"原始skill"目录的对应关系。原始skill在`clawhub-skills/downloaded/`，改造后在`differentiated-skills/`，两者关联仅在`scan_and_import.py`的`SLUG_MAPPING`硬编码字典中。
- **建议**：在SKILL.md frontmatter中增加`parent_slug`字段，作为双版本关联的显式声明：
  ```yaml
  # aws-agent-orchestrator-pro/SKILL.md
  slug: aws-agent-orchestrator-pro
  edition: pro
  parent_slug: aws-agent-orchestrator  # 显式声明父skill
  ```

---

## 九、总结与优先级建议

### 修复优先级排序

| 优先级 | 问题编号 | 问题描述 | 修复工作量 | 建议负责方 |
|--------|----------|----------|------------|------------|
| P0 | P0-1 | skills表缺edition列 | 0.5天 | 开发者 |
| P0 | P0-2 | skills表缺parent_slug列 | 0.5天 | 开发者 |
| P0 | P0-3 | 评分无持久化表 | 1天 | 开发者+PM确认需求 |
| P0 | P0-4 | 工作流状态机无持久化 | 1天 | 开发者+PM确认状态定义 |
| P1 | P1-4 | 外键约束未启用 | 0.5天 | 开发者 |
| P1 | P1-5 | 无事务边界 | 1天 | 开发者 |
| P1 | P1-2 | check_debranding误报clawhub/PostgreSQL | 0.5天 | 开发者 |
| P1 | P1-3 | 3张死表处理 | 0.5天 | PM决策+开发者执行 |
| P1 | P1-11 | 去标识检测未更新status | 0.5天 | 开发者 |
| P1 | P1-9 | 缺失索引补充 | 0.5天 | 开发者 |
| P1 | P1-10 | N+1查询优化 | 0.5天 | 开发者 |
| P1 | P1-1 | 规范frontmatter缺edition | 0.1天 | 任何人 |
| P1 | P1-7 | versions表字段未填充 | 0.5天 | 开发者 |
| P1 | P1-8 | pricing表缺历史追踪 | 0.5天 | 开发者 |
| P1 | P1-6 | current_status与工作流无映射 | 0.5天 | 开发者+PM确认 |
| P1 | P1-12 | License审核结果无存储 | 0.5天 | 开发者 |
| P2 | P2-1~6 | 各项优化 | 2天 | 开发者 |

**总修复工作量估算**：约10-12个工作日

### 核心结论

Skill生产规范v1.1的**文档设计质量高**（8大维度评分卡、10步含回流工作流、双版本edition机制、License合规审核），但**数据库实现严重滞后于规范设计**。v1.1的四大核心特性中：

| 核心特性 | 规范设计 | DB实现 | 落地率 |
|----------|----------|--------|--------|
| edition区分双版本 | 完善 | 主表缺失edition列 | 0% |
| parent_slug关联双版本 | 声明存在 | 完全缺失 | 0% |
| 8大维度评分卡 | 完善 | 无持久化层 | 0% |
| 10步含回流工作流 | 完善 | 无状态机 | 30%（仅步骤6/9/10部分落地） |

**架构师建议**：在启动660+skill批量改造前，必须先完成P0修复（约3个工作日），否则批量改造将无法进行进度管理和质量门禁统计。P1修复可与第一批改造并行推进。

---

*审核人：资深系统架构师 | 审核日期：2026-07-18 | 报告版本：v2.0*
