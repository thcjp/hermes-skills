---
slug: "database-admin"
name: "database-admin"
version: 2.0.1
displayName: "数据库管理专家"
summary: "表结构设计、批量数据操作、查询优化、类型处理与事务安全的全面数据库管理服务。数据库管理专家——提供全面的数据库管理功能，包括表结构创建、数据操作、查询优化、类型处理等. 核心能力包括： -"
license: "MIT"
description: |-
  数据库管理专家——提供全面的数据库管理功能，包括表结构创建、数据操作、查询优化、类型处理等.
  核心能力包括：
  - 表结构设计（主键、索引、外键约束、检查约束、NULL与默认值策略）
  - 多数据类型支持（TEXT、VARCHAR、BIGINT、UUID、JSONB、ENUM、SERIAL、DECIMAL）
  - 批量数据插入（事务优化、COPY命令、BIGINT大数处理）
  - 查询优化（JOIN、聚合统计、CTE、子查询、执行计划分析）
  - 数据库维护（CREATE/ALTER/DROP TABLE、INDEX管理、TRUNCATE、VACUUM）
  - 事务安全（ACID属性、自动提交/回滚、连接池管理）
  - 数据类型兼容性验证与主键冲突避免
tags:
  - 信息检索
  - database
  - postgresql
  - 数据处理
  - 数据分析
  - 工具
  - sql
  - create
  - stock_info
  - bigint
  - key
tools:
  - read
  - exec
  - write
  - glob
homepage: ""
category: "Research"
---
# 数据库管理专家

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 数据库管理专家处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 数据库管理专家类型处理 | 不支持 | 支持 |
| 数据库管理专家安全的全面数据库管理 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |

## 概述

本技能提供全面的数据库管理功能，包括表结构创建、数据操作、查询优化、类型处理（如 BIGINT）等。所有操作均遵循 SQL 最佳实践和事务安全原则，基于 PostgreSQL数据库 驱动 `pg` 与连接池 `pgpool` 实现.
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 表结构设计

- 自动设计最优表结构（主键、索引、约束）
- 支持多种数据类型：`TEXT`、`VARCHAR(n)`、`BIGINT`、`UUID`、`JSONB`、`ENUM`、`SERIAL`、`DECIMAL(p,s)`、`INT`、`TIMESTAMP`
- 自动创建适当的索引以提高查询性能
- 设置外键约束（`FOREIGN KEY`）和检查约束（`CHECK`）
- 处理 NULL 值和默认值策略（`NOT NULL`、`DEFAULT`）

### 数据插入
- 批量插入大量数据（使用事务优化，支持 10 万条以上记录）
- 处理 `BIGINT` 等大数类型数据（范围：-9223372036854775808 至 9223372036854775807）
- 验证数据类型兼容性
- 避免主键冲突（`ON CONFLICT`）和外键违规
- 支持 `COPY` 命令高性能批量导入

**输入**: 用户提供数据插入所需的指令和必要参数.
**输出**: 返回数据插入的处理结果,包含执行状态码、结果数据和执行日志。### 查询优化
- 编写高效的 `JOIN` 查询（INNER/LEFT/RIGHT/FULL JOIN）
- 聚合统计和分析查询（`GROUP BY`、`HAVING`、`ORDER BY`）
- 子查询和 CTE（`WITH` 子句）的使用
- 执行计划分析（`EXPLAIN ANALYZE`）和优化建议

**输入**: 用户提供查询优化所需的指令和必要参数.
**输出**: 返回查询优化的处理结果,包含执行状态码、结果数据和执行日志。### 数据库维护

| 操作 | SQL命令 | 说明 |
|:---:|:---:|:---:|
| 创建表 | `CREATE TABLE` | 定义表结构与约束 |
| 修改表 | `ALTER TABLE` | 添加/修改/删除列与约束 |
| 删除表 | `DROP TABLE` | 删除表及其数据 |
| 创建索引 | `CREATE INDEX` | 加速查询（支持 `CONCURRENTLY`） |
| 删除索引 | `DROP INDEX` | 移除索引 |
| 清空表 | `TRUNCATE` | 清空数据保留结构 |
| 分析表 | `VACUUM ANALYZE` | 回收空间并更新统计信息 |
| 备份 | `pg_dump` | 逻辑备份导出 |
| 恢复 | `pg_restore` | 从备份恢复 |

### 事务安全
- **驱动**：`pg`（PostgreSQL数据库 Node.js 驱动）
- **连接池**：`pgpool` 管理并发连接，避免连接耗尽
- **批量插入**：使用 `COPY` 或批量 `INSERT` 优化性能
- **事务控制**：自动开启 `BEGIN`/提交 `COMMIT`，异常时 `ROLLBACK`，保证 ACID 属性
- **错误处理**：捕获并报告约束违规、类型不匹配等错误

**输入**: 用户提供事务安全所需的指令和必要参数.
**输出**: 返回事务安全的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. **明确需求**：确认需要建表、插入数据、查询优化还是维护操作
2. **设计结构**：根据字段需求选择合适数据类型（`VARCHAR(100)` vs `TEXT`、`BIGINT` vs `INT`）
3. **编写SQL**：生成含约束与索引的 `CREATE TABLE` / `INSERT` / `SELECT` 语句
4. **事务执行**：在事务中执行批量操作，异常自动回滚
5. **验证结果**：通过 `EXPLAIN ANALYZE` 检查查询计划，确认索引命中

## 详细示例

### 示例1：创建库存表

```sql
CREATE TABLE stock_info (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    quantity INT DEFAULT 0,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
# ...
-- 为 product_name 创建索引
CREATE INDEX idx_stock_product_name ON stock_info(product_name);
# ...
-- 为 category 创建索引加速分组查询
CREATE INDEX idx_stock_category ON stock_info(category);
```

### 示例2：批量插入数据

```sql
-- 使用事务批量插入
BEGIN;
# ...
INSERT INTO stock_info (product_name, quantity, price, category) VALUES
    ('苹果', 100, 8.50, '水果'),
    ('香蕉', 200, 3.20, '水果'),
    ('牛肉', 50, 45.00, '肉类'),
    ('三文鱼', 30, 120.00, '海鲜');
# ...
COMMIT;
# ...
-- 大批量导入使用 COPY（10万条以上推荐）
-- COPY stock_info FROM '/path/to/data.csv' WITH (FORMAT csv, HEADER true);
```

### 示例3：查询统计

```sql
-- 计算每个类别的商品平均价格，仅统计库存>50的商品
SELECT category,
       COUNT(*) AS product_count,
       AVG(price) AS avg_price,
       SUM(quantity * price) AS total_value
FROM stock_info
WHERE quantity > 50
GROUP BY category
ORDER BY avg_price DESC;
# ...
-- 输出示例:
-- category | product_count | avg_price | total_value
-- 水果     | 2             | 5.85      | 1460.00
```

### 示例4：CTE复杂查询

```sql
-- 使用CTE查询销售额超过10万元的订单及其客户信息
WITH high_value_orders AS (
    SELECT customer_id, SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
    HAVING SUM(total_amount) > 100000
)
SELECT c.customer_name, c.email, h.total_spent
FROM high_value_orders h
JOIN customers c ON c.id = h.customer_id
ORDER BY h.total_spent DESC;
```

### 示例5：BIGINT类型处理

```sql
-- 存储超大数值ID（如雪花算法生成的ID）
CREATE TABLE event_logs (
    id BIGINT PRIMARY KEY,           -- 支持18位整数
    event_type VARCHAR(50) NOT NULL,
    payload JSONB,                   -- 存储JSON结构数据
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
# ...
-- 插入BIGINT值
INSERT INTO event_logs (id, event_type, payload) VALUES
    (1752345678901234567, 'login', '{"user_id": 12345, "ip": "192.168.1.1"}');
# ...
-- 查询JSONB字段
SELECT * FROM event_logs WHERE payload->>'user_id' = '12345';
```

### 示例6：执行计划分析

```sql
-- 分析查询执行计划
EXPLAIN ANALYZE
SELECT * FROM stock_info WHERE category = '水果' AND quantity > 50;
# ...
-- 如果出现 Seq Scan（全表扫描），说明索引未命中
-- 添加组合索引优化：
CREATE INDEX idx_stock_category_qty ON stock_info(category, quantity);
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| `BIGINT 溢出` | 数值超出 BIGINT 范围（>9223372036854775807） | 改用 `NUMERIC` 或 `DECIMAL` 类型存储超大数 |
| `主键冲突 (duplicate key)` | `INSERT` 的主键值已存在 | 使用 `INSERT ... ON CONFLICT DO NOTHING` 或 `ON CONFLICT DO UPDATE` |
| `外键违规 (foreign key violation)` | 插入的外键值在引用表中不存在 | 先插入引用表数据，或检查外键值有效性 |
| `CHECK约束违规` | 数据不满足 `CHECK` 条件 | 检查约束定义与实际数据，修正数据或调整约束 |
| `类型不匹配` | `VARCHAR` 列插入数值或反向操作 | 使用 `CAST(col AS type)` 显式转换类型 |
| `连接池耗尽` | 并发连接数超过 `pgpool` 最大连接数 | 调大连接池配置或优化查询减少长连接占用 |
| `死锁 (deadlock detected)` | 多事务以不同顺序锁定相同资源 | 统一加锁顺序，使用 `SELECT FOR UPDATE` 预锁定 |
| `VACUUM 未及时执行` | 大量删除/更新后死元组堆积导致性能下降 | 设置 `autovacuum` 参数或手动执行 `VACUUM ANALYZE` |

## 常见问题

### Q1: VARCHAR(100) 和 TEXT 有什么区别？
A: 在 PostgreSQL数据库 中两者性能几乎相同。`VARCHAR(100)` 有长度限制（100字符），`TEXT` 无限制。建议需要长度校验时用 `VARCHAR(n)`，不需要时用 `TEXT`.
### Q2: 批量插入10万条数据如何优化？
A: 三种方案：(1) 使用 `BEGIN/COMMIT` 事务包裹，避免每条自动提交；(2) 使用多值 `INSERT`（单语句插入多行）；(3) 使用 `COPY` 命令从文件直接导入，性能最高.
### Q3: BIGINT 存储雪花算法ID会溢出吗？
A: 雪花算法ID最大约 9.2×10^18，在 BIGINT 范围内（最大 9223372036854775807）。但如果ID由字符串拼接或加密生成，可能超出范围，建议改用 `NUMERIC` 或 `TEXT`.
### Q4: JSONB 和 JSON 有什么区别？
A: `JSONB` 存储为二进制格式，支持索引（如 `GIN` 索引）和高效查询（`->>` 操作符），但写入稍慢。`JSON` 存储为文本，保留原始格式但不支持索引。生产环境推荐 `JSONB`.
### Q5: 如何避免索引创建锁表？
A: PostgreSQL数据库 中使用 `CREATE INDEX CONCURRENTLY` 可在不阻塞写入的情况下创建索引。注意：`CONCURRENTLY` 不能在事务块中使用，且创建时间更长.
### Q6: EXPLAIN ANALYZE 显示 Seq Scan 怎么办？
A: 全表扫描说明索引未命中。检查：(1) `WHERE` 条件列是否有索引；(2) 是否对索引列使用了函数（如 `LOWER(col)` 会导致索引失效）；(3) 数据量过小时优化器可能主动选择 Seq Scan（正常行为）.
## 已知限制

- 不适用于实时流数据处理
- 不适用于小规模数据手动分析
- 不适用于非结构化文本情感分析
- 连接池最大连接数受数据库配置限制
- `COPY` 命令需要文件系统访问权限
