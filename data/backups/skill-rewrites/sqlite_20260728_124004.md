---
slug: sqlite
name: sqlite
version: "1.0.0"
displayName: SQLite
summary: "正确用SQLite,并发/pragmas/类型处理得当(社区下载版)"
license: MIT
description: |-
  Use SQLite correctly with proper concurrency, pragmas, and type handling。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# SQLite

## Concurrency (Biggest Gotcha)

* Only one writer at a time—concurrent writes queue or fail; not for high-write workloads
* Enable WAL mode: `PRAGMA journal_mode=WAL`—allows reads during writes, huge improvement
* Set busy timeout: `PRAGMA busy_timeout=5000`—waits 5s before SQLITE_BUSY instead of failing immediately
* WAL needs `-wal` and `-shm` files—don't forget to copy them with main database
* `BEGIN IMMEDIATE` to grab write lock early—prevents deadlocks in read-then-write patterns

## Foreign Keys (Off by Default!)

* `PRAGMA foreign_keys=ON` required per connection—not persisted in database
* Without it, foreign key constraints silently ignored—data integrity broken
* Check before relying: `PRAGMA foreign_keys` returns 0 or 1
* ON DELETE CASCADE only works if foreign_keys is ON

## Type System

* Type affinity, not strict types—INTEGER column accepts "hello" without error
* `STRICT` tables enforce types—but only SQLite 3.37+ (2021)
* No native DATE/TIME—use TEXT as ISO8601 or INTEGER as Unix timestamp
* BOOLEAN doesn't exist—use INTEGER 0/1; TRUE/FALSE are just aliases
* REAL is 8-byte float—same precision issues as any float

## Schema Changes

* `ALTER TABLE` very limited—can add column, rename table/column; that's mostly it
* Can't change column type, add constraints, or drop columns (until 3.35)
* Workaround: create new table, copy data, drop old, rename—wrap in transaction
* `ALTER TABLE ADD COLUMN` can't have PRIMARY KEY, UNIQUE, or NOT NULL without default

## Performance Pragmas

* `PRAGMA optimize` before closing long-running connections—updates query planner stats
* `PRAGMA cache_size=-64000` for 64MB cache—negative = KB; default very small
* `PRAGMA synchronous=NORMAL` with WAL—good balance of safety and speed
* `PRAGMA temp_store=MEMORY` for temp tables in RAM—faster sorts and temp results

## Vacuum & Maintenance

* Deleted data doesn't shrink file—`VACUUM` rewrites entire database, reclaims space
* `VACUUM` needs 2x disk space temporarily—ensure enough room
* `PRAGMA auto_vacuum=INCREMENTAL` with `PRAGMA incremental_vacuum`—partial reclaim without full rewrite
* After bulk deletes, always vacuum or file stays bloated

## Backup Safety

* Never copy database file while open—corrupts if write in progress
* Use `.backup` command in sqlite3—or `sqlite3_backup_*` API
* WAL mode: `-wal` and `-shm` must be copied atomically with main file
* `VACUUM INTO 'backup.db'` creates standalone copy (3.27+)

## Indexing

* Covering indexes work—add extra columns to avoid table lookup
* Partial indexes supported (3.8+): `CREATE INDEX ... WHERE condition`
* Expression indexes (3.9+): `CREATE INDEX ON t(lower(name))`
* `EXPLAIN QUERY PLAN` shows index usage—simpler than PostgreSQL EXPLAIN

## Transactions

* Autocommit by default—each statement is own transaction; slow for bulk inserts
* Batch inserts: `BEGIN; INSERT...; INSERT...; COMMIT`—10-100x faster
* `BEGIN EXCLUSIVE` for exclusive lock—blocks all other connections
* Nested transactions via `SAVEPOINT name` / `RELEASE name` / `ROLLBACK TO name`

## Common Mistakes

* Using SQLite for web app with concurrent users—one writer blocks all; use PostgreSQL
* Assuming ROWID is stable—`VACUUM` can change ROWIDs; use explicit INTEGER PRIMARY KEY
* Not setting busy_timeout—random SQLITE_BUSY errors under any concurrency
* In-memory database `':memory:'`—each connection gets different database; use `file::memory:?cache=shared` for shared

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Use SQLite correctly with proper concurrency, pragmas, and type handling
- 触发关键词: sqlite, proper, concurrency, correctly

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用SQLite？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: SQLite有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
