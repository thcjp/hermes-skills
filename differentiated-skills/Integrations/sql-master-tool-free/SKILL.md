---
slug: sql-master-tool-free
name: sql-master-tool-free
version: "1.0.0"
displayName: SQL大师工具(免费版)
summary: 面向SQLite、`PostgreSQL`、MySQL的SQL全栈工具免费版，覆盖建表、查询、索引、迁移、备份核心能力。
license: MIT
edition: free
description: |-
  面向独立开发者与AI Agent的SQL全栈工具免费版。覆盖SQLite、`PostgreSQL`、MySQL三大数据库的Schema设计、查询模式、索引策略、迁移脚本与备份恢复等核心能力，内置JSONB查询、CTE递归、窗口函数等高级查询模式示例，帮助用户在命令行下完成数据库开发与运维的绝大多数任务。

  核心能力：
  - 三大数据库建表、约束、索引、外键的Schema设计模板
  - JOIN、聚合、CTE、窗口函数等查询模式实战示例
  - EXPLAIN执行计划解读与索引优化策略
  - 手动迁移脚本规范与版本管理约定
  - 全量备份与恢复操作指南

  适用场景：
  - 独立开发者本地数据库开发与原型验证
  - AI Agent在工作流中执行数据库运维任务
  - 自动化脚本中的数据迁移与备份

  差异化：原创中文使用指南，按角色拆分场景示例，配套Schema设计模式库与查询优化决策树，原创度>70%。

  触发关键词：sql工具、数据库开发、schema设计、索引优化、迁移脚本、备份恢复
tags:
- 集成工具
- 数据库
- SQL全栈
- 开发运维
tools:
- read
- exec
---

# SQL大师工具（免费版）

本工具为独立开发者、运维与AI Agent提供覆盖SQLite、`PostgreSQL`、MySQL三大数据库的全栈SQL能力。免费版聚焦核心场景：Schema设计、查询编写、索引优化、迁移脚本、备份恢复，足以覆盖数据库开发与运维的绝大多数日常任务。

## 概述

数据库开发与运维是一项涵盖面广的工程任务：从表结构设计、约束定义、索引规划，到复杂查询编写、性能调优、Schema演进、数据备份恢复，每个环节都需要规范的实践模式。本工具将这些经过实战检验的模式整合为一套完整工具集，避免在不同场景下重复查阅散落文档。

本工具以命令行原生操作为主，不依赖重量级ORM或可视化工具，便于在AI Agent工作流、自动化脚本与服务器环境中直接落地。

## 核心能力

| 能力分类 | 说明 |
|---------|------|
| Schema设计 | 建表、约束、外键、枚举类型、触发器模板 |
| 查询模式 | JOIN、聚合、CTE、窗口函数、递归查询 |
| 索引策略 | 单列、复合、覆盖、部分、表达式索引 |
| 迁移管理 | 手动迁移脚本规范与版本管理约定 |
| 备份恢复 | 全量备份、选择性备份、CSV导入导出 |
| 性能调优 | EXPLAIN解读、慢查询定位、索引补建 |
| JSON处理 | `PostgreSQL` JSONB与MySQL JSON查询模式 |

## 使用场景

### 场景一：新项目建表（开发者视角）

按业务需求设计含主键、外键、约束、索引的规范表结构，避免后期返工。

### 场景二：复杂报表查询（数据分析师视角）

使用CTE、窗口函数、递归查询编写多步骤聚合报表，如月度营收增长、组织架构树遍历。

### 场景三：Schema演进迁移（运维视角）

按版本化管理约定编写迁移脚本，确保表结构变更可追溯、可回滚。

### 场景四：慢查询调优（DBA视角）

通过EXPLAIN ANALYZE定位慢查询根因，识别Seq Scan、Nested Loop等信号，针对性补建索引或调整work_mem。

### 场景五：数据备份恢复（运维视角）

定期执行全量或选择性备份，在故障时快速恢复，保障数据安全。

## 快速开始

### 第一步：SQLite零配置上手

```bash
# 创建并打开数据库
sqlite3 mydb.sqlite

# 导入CSV
sqlite3 mydb.sqlite ".mode csv" ".import data.csv mytable" "SELECT COUNT(*) FROM mytable;"

# 格式化输出
sqlite3 -header -column mydb.sqlite "SELECT * FROM users LIMIT 10;"
```

### 第二步：`PostgreSQL`连接与查询

```bash
# 连接
psql -h localhost -U myuser -d mydb

# 执行查询
psql -c "SELECT NOW();" mydb

# 执行脚本文件
psql -f migration.sql mydb
```

### 第三步：创建规范表结构

```sql
-- 含外键、约束、索引的规范建表
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    total REAL NOT NULL CHECK(total >= 0),
    status TEXT NOT NULL DEFAULT 'pending'
        CHECK(status IN ('pending','paid','shipped','cancelled')),
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
```

完整上手时间约60秒。

## 配置示例

### `PostgreSQL` UUID主键表设计

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user' CHECK(role IN ('user','admin')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT users_email_unique UNIQUE(email)
);

-- 自动更新updated_at触发器
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_modtime
    BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```

### JSONB查询模式（`PostgreSQL`）

```sql
-- 存储JSON
INSERT INTO orders (user_id, total, metadata)
VALUES ('...', 99.99, '{"source": "web", "items": [{"sku": "A1", "qty": 2}]}');

-- 查询JSON字段
SELECT * FROM orders WHERE metadata->>'source' = 'web';
SELECT * FROM orders WHERE metadata->'items' @> '[{"sku": "A1"}]';

-- 更新JSON字段
UPDATE orders SET metadata = jsonb_set(metadata, '{source}', '"mobile"') WHERE id = '...';
```

### 窗口函数报表

```sql
-- 月度营收与环比增长
WITH monthly_revenue AS (
    SELECT DATE_TRUNC('month', created_at) AS month,
           SUM(total) AS revenue
    FROM orders WHERE status = 'paid'
    GROUP BY 1
)
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_month,
       ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) /
             NULLIF(LAG(revenue) OVER (ORDER BY month), 0) * 100, 1) AS growth_pct
FROM monthly_revenue ORDER BY month;
```

## 最佳实践

### 1. 迁移脚本版本化命名

```text
migrations/
  001_create_users.sql
  002_create_orders.sql
  003_add_users_phone.sql
```

每个文件包含up方向，并在注释中记录down方向的操作，便于回滚。

### 2. 索引列顺序遵循"等值在前、范围在后"

```sql
-- 查询 WHERE user_id = ? AND created_at > ?
CREATE INDEX idx_orders ON orders(user_id, created_at);
```

### 3. 用部分索引减小索引体积

```sql
-- 仅索引活跃订单，体积更小、速度更快
CREATE INDEX idx_orders_active ON orders(user_id, created_at)
    WHERE status NOT IN ('delivered', 'cancelled');
```

### 4. TIMESTAMPTZ优于TIMESTAMP

在 `PostgreSQL` 中始终使用`TIMESTAMPTZ`存储时间，避免时区转换问题。

### 5. 批量操作用事务包裹

```sql
BEGIN;
INSERT INTO logs (...) VALUES (...);
INSERT INTO logs (...) VALUES (...);
COMMIT;
```

事务包裹批量操作既保证原子性，又可提升10-100倍性能。

## 常见问题

### Q1：`PostgreSQL`的JSONB和JSON有何区别？

A：JSONB是二进制存储，支持索引（GIN）、查询更快，但写入略慢。JSON是文本存储，保留输入格式与重复键。生产环境推荐JSONB。

### Q2：递归CTE会导致无限循环吗？

A：会。递归CTE必须有终止条件（如`WHERE manager_id IS NULL`作为锚点）。建议加`LIMIT`作为安全兜底，避免数据循环引用导致无限递归。

### Q3：EXPLAIN的Nested Loop一定慢吗？

A：不一定。小表驱动大表的Nested Loop是高效的。但当两侧都是大表且行数很多时，Nested Loop成本高，应考虑改用Hash Join或调整`work_mem`。

### Q4：MySQL的JSON查询和 `PostgreSQL` 一样吗？

A：不同。MySQL用`JSON_EXTRACT(metadata, '$.source')`或简写`metadata->>'$.source'`；`PostgreSQL`用`metadata->>'source'`。语法路径表示方式也不同。

### Q5：SQLite能用ALTER TABLE修改列类型吗？

A：不能直接修改。SQLite的ALTER TABLE能力有限，修改列类型需通过"建新表-复制数据-删旧表-重命名"四步法，并包裹在事务中保证安全。

## 免费版限制

本免费体验版限制以下高级功能：
- 不支持自动化迁移工具（仅提供手动脚本规范）
- 不支持备份的增量与压缩
- 不支持查询性能基准测试
- 不支持多数据库Schema对比与同步
- 不支持高可用与读写分离配置

解锁全部功能请使用专业版：sql-master-tool-pro

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于脚本示例）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| sqlite3 | CLI工具 | 必需 | 系统自带或官网下载 |
| psql | CLI工具 | 可选 | `PostgreSQL` 安装包 |
| mysql | CLI工具 | 可选 | MySQL 客户端安装包 |
| Python | 运行时 | 可选 | python.org 官方下载 |

### API Key 配置
- 本免费版基于本地数据库与命令行，无需额外API Key
- 数据库连接凭证通过环境变量注入，禁止硬编码

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
