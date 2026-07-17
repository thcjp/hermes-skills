---
slug: sql
name: sql
version: "1.0.1"
displayName: SQL
summary: Master relational databases with SQL. Schema design, queries, performance,
  migrations for Postgre...
license: MIT
description: |-
  Master relational databases with SQL. Schema design, queries, performance,
  migrations for Postgre...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: master, databases, relational, sql, schema
tags:
- Integrations
tools:
- read
- exec
---

# SQL

Master relational databases from the command line. Covers SQLite, PostgreSQL, MySQL, and SQL Server with battle-tested patterns for schema design, querying, migrations, and operations.

## When to Use

Working with relational databases—designing schemas, writing queries, building migrations, optimizing performance, or managing backups. Applies to SQLite, PostgreSQL, MySQL, and SQL Server.

## Quick Reference

| Topic | File |
| --- | --- |
| Query patterns | `patterns.md` |
| Schema design | `schemas.md` |
| Operations | `operations.md` |

## Core Rules

### 1. Choose the Right Database

| Use Case | Database | Why |
| --- | --- | --- |
| Local/embedded | SQLite | Zero setup, single file |
| General production | PostgreSQL | Best standards, JSONB, extensions |
| Legacy/hosting | MySQL | Wide hosting support |
| Enterprise/.NET | SQL Server | Windows integration |

### 2. Always Parameterize Queries

```python
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### 3. Index Your Filters

Any column in WHERE, JOIN ON, or ORDER BY on large tables needs an index.

### 4. Use Transactions

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 5. Prefer EXISTS Over IN

```sql
-- ✅ Faster (stops at first match)
SELECT * FROM orders o WHERE EXISTS (
  SELECT 1 FROM users u WHERE u.id = o.user_id AND u.active
);
```

---

## Quick Start

### SQLite

```bash
sqlite3 mydb.sqlite                              # Create/open
sqlite3 mydb.sqlite "SELECT * FROM users;"       # Query
sqlite3 -header -csv mydb.sqlite "SELECT *..." > out.csv
sqlite3 mydb.sqlite "PRAGMA journal_mode=WAL;"   # Better concurrency
```

### PostgreSQL

```bash
psql -h localhost -U myuser -d mydb              # Connect
psql -c "SELECT NOW();" mydb                     # Query
psql -f migration.sql mydb                       # Run file
\dt  \d+ users  \di+                             # List tables/indexes
```

### MySQL

```bash
mysql -h localhost -u root -p mydb               # Connect
mysql -e "SELECT NOW();" mydb                    # Query
```

### SQL Server

```bash
sqlcmd -S localhost -U myuser -d mydb            # Connect
sqlcmd -Q "SELECT GETDATE()"                     # Query
sqlcmd -S localhost -d mydb -E                   # Windows auth
```

---

## Common Traps

### NULL Traps

* `NOT IN (subquery)` returns empty if subquery has NULL → use `NOT EXISTS`
* `NULL = NULL` is NULL, not true → use `IS NULL`
* `COUNT(column)` excludes NULLs, `COUNT(*)` counts all

### Index Killers

* Functions on columns → `WHERE YEAR(date) = 2024` scans full table
* Type conversion → `WHERE varchar_col = 123` skips index
* `LIKE '%term'` can't use index → only `LIKE 'term%'` works
* Composite `(a, b)` won't help filtering only on `b`

### Join Traps

* LEFT JOIN with WHERE on right table becomes INNER JOIN
* Missing JOIN condition = Cartesian product
* Multiple LEFT JOINs can multiply rows

---

## EXPLAIN

```sql
-- PostgreSQL
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM orders WHERE user_id = 5;

-- SQLite
EXPLAIN QUERY PLAN SELECT * FROM orders WHERE user_id = 5;
```

**Red flags:**

* `Seq Scan` on large tables → needs index
* `Rows Removed by Filter` high → index doesn't cover filter
* Actual vs estimated rows differ → run `ANALYZE tablename;`

---

## Index Strategy

```sql
-- Composite index (equality first, range last)
CREATE INDEX idx_orders ON orders(user_id, status);

-- Covering index (avoids table lookup)
CREATE INDEX idx_orders ON orders(user_id) INCLUDE (total);

-- Partial index (smaller, faster)
CREATE INDEX idx_pending ON orders(user_id) WHERE status = 'pending';
```

---

## Portability

| Feature | PostgreSQL | MySQL | SQLite | SQL Server |
| --- | --- | --- | --- | --- |
| LIMIT | LIMIT n | LIMIT n | LIMIT n | TOP n |
| UPSERT | ON CONFLICT | ON DUPLICATE KEY | ON CONFLICT | MERGE |
| Boolean | true/false | 1/0 | 1/0 | 1/0 |
| Concat | || | CONCAT() | || | + |

---

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `prisma` — Node.js ORM
* `sqlite` — SQLite-specific patterns
* `analytics` — data analysis queries

## Feedback

* If useful: `
* Stay updated: `

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
