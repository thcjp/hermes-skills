---
slug: "sql-toolkit"
name: "sql-toolkit"
version: "1.0.0"
displayName: "SQL Toolkit"
summary: "关系型数据库操作工具箱，覆盖SQLite/PostgreSQL/MySQL的查询、设计、迁移与优化"
license: "Proprietary"
description: |-
  SQL Toolkit 是关系型数据库命令行操作的完整工具箱，覆盖 SQLite、PostgreSQL、MySQL 三大数据库。
  核心能力包括 Schema Operations（表结构创建与修改）、Quick Start（零配置快速上手）、
  查询模式（Joins、Aggregations、CTEs、窗口函数）、数据库迁移、查询优化（EXPLAIN、索引策略）、
  备份与恢复。适用于数据库开发、数据探索、性能调优场景。
tags:
  - 需求设计
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
---
# SQL Toolkit

关系型数据库命令行操作工具箱，覆盖 SQLite、PostgreSQL、MySQL，提供 Schema 设计、查询编写、迁移脚本、索引优化、备份恢复的完整模式。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | SQL Toolkit处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| SQL ToolkitMySQL的查询 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

### Quick Start（SQLite 零配置快速上手）

SQLite 内置于 Python，无需安装服务，适合本地数据探索和原型开发。支持 CSV 导入、快速查询、格式化输出。

```bash
sqlite3 mydb.sqlite
sqlite3 mydb.sqlite ".mode csv" ".import data.csv mytable" "SELECT COUNT(*) FROM mytable;"
sqlite3 mydb.sqlite "SELECT * FROM users WHERE created_at > '2026-01-01' LIMIT 10;"
sqlite3 -header -csv mydb.sqlite "SELECT * FROM orders;" > orders.csv
sqlite3 -header -column mydb.sqlite
```

快速导入 CSV 进行临时分析：`sqlite3 :memory: ".mode csv" ".import file.csv t" "SELECT ..."`

### Schema Operations（表结构创建与修改）

创建带外键约束和检查约束的表结构，支持 ALTER TABLE 增删列、CREATE INDEX 创建索引：

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);
# ...
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    total REAL NOT NULL CHECK(total >= 0),
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','paid','shipped','cancelled'))
);
# ...
ALTER TABLE users ADD COLUMN phone TEXT;
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE UNIQUE INDEX idx_users_email ON users(email);
```

PostgreSQL 额外支持：UUID 主键（`uuid_generate_v4()`）、`TIMESTAMPTZ` 时间戳、ENUM 类型、`JSONB` 字段、触发器自动更新 `updated_at`、部分索引（Partial Index）、GIN 索引。

### Query Patterns（查询模式：Joins / Aggregations / CTEs）

**Joins**：`INNER JOIN` 取交集、`LEFT JOIN` 保留左表全量、`SELF JOIN` 做同表关联（如查找同邮箱域名的用户）。

**Aggregations**：`GROUP BY` + `HAVING` 过滤分组、窗口函数实现运行总计（`SUM() OVER`）、组内排名（`RANK() OVER PARTITION BY`）、移动平均（`AVG() OVER ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`）。

**CTEs（Common Table Expressions）**：用 `WITH` 子句拆解多步查询，支持递归 CTE 实现树形遍历（如组织架构图 `WITH RECURSIVE org_tree AS ...`）。

```sql
WITH monthly_revenue AS (
    SELECT DATE_TRUNC('month', created_at) AS month, SUM(total) AS revenue
    FROM orders WHERE status = 'paid' GROUP BY 1
)
SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue FROM monthly_revenue;
```

### Migrations（数据库迁移脚本模式）

迁移文件命名约定：`migrations/001_create_users.sql`、`002_create_orders.sql`，配合 `schema_migrations` 版本表追踪已应用版本。脚本自动跳过已执行迁移，失败时中断并报错。

### Query Optimization（EXPLAIN 与索引策略）
使用 `EXPLAIN (ANALYZE, BUFFERS)` 查看 PostgreSQL 执行计划，关注：
- `Seq Scan` 全表扫描 → 需要加索引
- `Nested Loop` 大数据量 → 考虑 `Hash Join`，可能需增大 `work_mem`
- `Rows Removed by Filter` 过高 → 索引未覆盖过滤条件
- 预估行数偏差大 → 执行 `ANALYZE tablename` 更新统计

索引策略：单列索引、复合索引（等值过滤在前、范围过滤在后）、覆盖索引（`INCLUDE` 避免回表）、部分索引（`WHERE` 条件缩小体积）、GIN 索引（JSONB 查询）。SQLite 用 `EXPLAIN QUERY PLAN` 检查 SCAN vs SEARCH USING INDEX。

**输入**: 用户提供Query Optimization（EXPLAIN 与索引策略）所需的指令和必要参数。
**输出**: 返回Query Optimization（EXPLAIN 与索引策略）的处理结果,包含执行状态码、结果数据和执行日志。### Backup & Restore（备份与恢复）
```bash
# PostgreSQL
pg_dump -Fc -h localhost -U myuser mydb > backup.dump
pg_restore -h localhost -U myuser -d mydb --clean --if-exists backup.dump
# ...
# SQLite
sqlite3 mydb.sqlite ".backup backup.sqlite"
sqlite3 mydb.sqlite .dump > backup.sql
# ...
# MySQL
mysqldump -h localhost -u root -p mydb > backup.sql
mysql -h localhost -u root -p mydb < backup.sql
```

**处理**: 解析Backup & Restore（备份与恢复）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回Backup & Restore（备份与恢复）的处理结果,包含执行状态码、结果数据和执行日志。

#
## 示例

### 基本用法

向Agent发送指令:

```
使用 SQL Toolkit 处理以下任务:
[具体任务描述]
```

### 输出说明

Agent将根据指令调用对应能力,返回响应数据。响应格式取决于具体能力点的输出定义。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 连接被拒绝 | 数据库服务未启动或端口错误 | 检查数据库服务状态，确认主机和端口配置 |
| 认证失败 | 用户名/密码错误或权限不足 | 核对凭据，确认用户对目标数据库有访问权限 |
| SQL 语法错误 | 关键字拼写错误或语法不符合方言 | 检查 SQL 方言差异（如 SQLite 无 TIMESTAMPTZ），参考对应数据库文档 |
| 外键约束冲突 | 插入或删除违反外键引用完整性 | 先操作被引用表或使用 ON DELETE CASCADE，检查引用关系 |
| 索引创建失败 | 索引名重复或字段不存在 | 确认字段名拼写，使用 DROP INDEX IF EXISTS 清理旧索引 |
| 迁移脚本执行失败 | SQL 文件中有语法错误或依赖顺序错误 | 检查迁移文件命名顺序，确认前序迁移已执行，查看具体错误行号 |
| 查询超时 | 全表扫描大数据量或锁等待 | 使用 EXPLAIN 分析执行计划，添加索引或优化查询条件 |
| 锁冲突 | 并发事务互相阻塞 | 设置合理的 lock_timeout，按固定顺序访问表减少死锁 |

## 常见问题

### Q1: SQLite 和 PostgreSQL 的 SQL 语法有什么主要区别？
A: SQLite 使用 `AUTOINCREMENT`、`TEXT` 类型、`datetime('now')` 函数；PostgreSQL 使用 `SERIAL`/`UUID`、`TIMESTAMPTZ`、`NOW()` 函数，还支持 `JSONB`、`ENUM`、部分索引等高级特性。

### Q2: 如何选择索引类型？
A: 单列索引用于单字段过滤；复合索引注意列顺序（等值在前、范围在后）；覆盖索引用 `INCLUDE` 避免回表；部分索引用 `WHERE` 缩小体积；JSONB 查询用 GIN 索引。

### Q3: 迁移脚本如何保证幂等性？
A: 使用 `CREATE TABLE IF NOT EXISTS`、`DROP INDEX IF EXISTS` 等条件语句，配合 `schema_migrations` 版本表追踪已执行迁移，避免重复执行。

## 已知限制

- 不适用于 NoSQL 数据库（MongoDB、Redis 等）
- 无法自动修复数据损坏，需手动恢复备份
- 查询性能受数据库服务器配置和硬件影响
- 复杂的分布式数据库场景需额外工具支持
