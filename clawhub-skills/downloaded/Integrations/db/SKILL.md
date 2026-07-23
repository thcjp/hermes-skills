---
slug: db
name: db
version: "1.0.0"
displayName: Database
summary: "设计运营数据库,规避扩展/可靠性/数据完整性陷阱"
  integrity traps.
license: MIT
description: |-
  Design and operate databases avoiding common scaling, reliability, and
  data integrity traps。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据...
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Database

## Connection Traps

* Connection pools exhausted = app hangs silently — set max connections, monitor pool usage
* Each Lambda/serverless invocation may open new connection — use connection pooling proxy (RDS Proxy, PgBouncer)
* Connections left open block schema changes — `ALTER TABLE` waits for all transactions
* Idle connections consume memory — set connection timeout, kill idle connections

## Transaction Gotchas

* Long transactions hold locks and bloat MVCC — keep transactions short
* Read-only transactions still take snapshots — can block vacuum/cleanup in Postgres
* Implicit autocommit varies by database — explicit BEGIN/COMMIT is safer
* Deadlocks from inconsistent lock ordering — always lock tables/rows in same order
* Lost updates from read-modify-write without locking — use SELECT FOR UPDATE or optimistic locking

## Schema Changes

* Adding column with default rewrites entire table in old MySQL/Postgres — use NULL default, backfill, then alter
* Index creation locks writes in some databases — use CONCURRENTLY in Postgres, ONLINE in MySQL 8+
* Renaming column breaks running application — add new column, migrate, drop old
* Dropping column with active queries causes errors — deploy code change first, then schema change
* Foreign key checks slow bulk inserts — disable constraints, insert, re-enable

## Backup and Recovery

* Logical backups (pg_dump, mysqldump) lock tables or miss concurrent writes — use consistent snapshot
* Point-in-time recovery requires WAL/binlog retention — configure before you need it
* Backup verification: restore regularly — backups that can't restore aren't backups
* Replication lag during backup can cause inconsistency — backup from replica, verify consistency

## Replication Traps

* Replication lag means stale reads — check lag before trusting replica data
* Writes to replica corrupt replication — make replicas read-only
* Schema changes can break replication — replicate schema changes, don't apply separately
* Split-brain after failover loses writes — use fencing/STONITH to prevent
* Promoting replica doesn't redirect connections — application must reconnect to new primary

## Query Patterns

* N+1 queries from ORM lazy loading — eager load relationships or batch queries
* Missing indexes on foreign keys slows joins and cascading deletes
* Large IN clauses become slow — batch into multiple queries or use temp table
* COUNT(*) on large tables is slow — use approximate counts or cache
* SELECT without LIMIT on unbounded data risks OOM

## Data Integrity

* Application-level unique checks have race conditions — use database constraints
* Check constraints often disabled for "flexibility" then data corrupts — keep them on
* Orphan rows from missing foreign keys — add constraints retroactively, clean up first
* Timezone confusion: store UTC, convert on display — never store local time without zone
* Floating point for money causes rounding errors — use DECIMAL or integer cents

## Scaling Limits

* Single table over 100M rows needs sharding strategy — plan before you hit it
* Autovacuum falling behind causes table bloat — monitor dead tuple ratio
* Query planner statistics stale after bulk changes — ANALYZE after large imports
* Connection count doesn't scale linearly — more connections = more lock contention
* Disk IOPS often bottleneck before CPU — monitor I/O wait

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

- Design and operate databases avoiding common scaling, reliability, and
  data integrity traps
- 触发关键词: common, databases, operate, design, avoiding, database

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

### Q1: 如何开始使用Database？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Database有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
