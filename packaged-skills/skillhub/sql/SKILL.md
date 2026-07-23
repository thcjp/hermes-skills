---
slug: "sql"
name: "sql"
version: "1.0.0"
displayName: "SQL查询引擎"
summary: "SQL查询编写、性能优化、索引策略、Schema设计与事务管理的全栈指导。"
license: "Proprietary"
description: |-
  SQL全栈能力引擎，覆盖查询编写、性能优化、索引策略、Schema设计、事务管理与
  数据库运维。支持PostgreSQL、MySQL、SQLite等主流数据库。核心能力：
  - SQL查询编写与优化（EXPLAIN ANALYZE分析、N+1问题修复）
  - 索引策略（B-Tree/GIN/GiST/部分索引/表达式索引）
  - Schema设计与规范化（1NF-3NF、反规范化策略）
  - 事务与并发控制（隔离级别、死锁处理、乐观锁）
  - 窗口函数与CTE高级查询
  - 数据库运维（VACUUM/备份/复制/分区）
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 数据存储
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# SQL查询引擎

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
## 核心能力

### 1. 查询编写与优化
```sql
-- EXPLAIN ANALYZE 分析查询计划
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 42;

-- N+1查询问题修复：子查询改为JOIN
-- 问题：循环中执行N次查询
-- 修复：单次JOIN查询
SELECT u.name, o.order_date, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.id IN (1, 2, 3, 4, 5);

-- 窗口函数：排名/累计/分桶
SELECT
  product_name,
  category,
  price,
  RANK() OVER (PARTITION BY category ORDER BY price DESC) AS rank_in_category,
  SUM(price) OVER (PARTITION BY category) AS category_total,
  PERCENT_RANK() OVER (ORDER BY price) AS price_percentile
FROM products;

-- CTE递归查询：组织架构树
WITH RECURSIVE org_tree AS (
  SELECT id, name, parent_id, 1 AS level
  FROM departments WHERE parent_id IS NULL
  UNION ALL
  SELECT d.id, d.name, d.parent_id, ot.level + 1
  FROM departments d
  JOIN org_tree ot ON d.parent_id = ot.id
)
SELECT * FROM org_tree ORDER BY level, name;
```- 验证执行结果，确认输出符合预期格式
- 参考`数据库运维`相关配置参数进行设置- 验证执行结果，确认输出符合预期格式
- 参考`高级查询模式`相关配置参数进行设置- 验证执行结果，确认输出符合预期格式
- 参考`Schema设计与规范化`相关配置参数进行设置- 验证执行结果，确认输出符合预期格式
- 参考`索引策略`相关配置参数进行设置- 验证执行结果，确认输出符合预期格式
- 参考`查询编写与优化`相关配置参数进行设置
### 2. 索引策略
```sql
-- B-Tree索引（默认，适合等值和范围查询）
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- 复合索引（注意列顺序：等值→范围）
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- 部分索引（仅索引满足条件的行，减少索引体积）
CREATE INDEX idx_orders_active ON orders(user_id) WHERE status = 'active';

-- 表达式索引（解决函数导致索引失效）
CREATE INDEX idx_users_lower_email ON users(LOWER(email));
-- 现在可以使用：SELECT * FROM users WHERE LOWER(email) = 'test@example.com'

-- GIN索引（PostgreSQL，适合JSONB/全文检索/数组）
CREATE INDEX idx_products_attrs ON products USING GIN(attributes);
SELECT * FROM products WHERE attributes @> '{"color": "red"}';
```

**处理**: 按照skill规范执行索引策略操作,遵循单一意图原则。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `索引策略` 选项
- 处理流程: 接收输入 -> 执行索引策略 -> 返回结果
- 输入: 用户提供索引策略所需的参数和指令
- 输出: 返回索引策略的执行结果,包含操作状态和输出数据

### 3. Schema设计与规范化
```sql
-- 1NF：消除重复组（每列原子值）
-- 2NF：消除部分依赖（非主键列依赖完整主键）
-- 3NF：消除传递依赖（非主键列不依赖其他非主键列）

-- 反规范化策略：读多写少场景适当冗余
-- 订单表冗余存储用户名（避免每次JOIN users表）
CREATE TABLE orders (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT NOT NULL REFERENCES users(id),
  user_name VARCHAR(100) NOT NULL,  -- 冗余字段
  total DECIMAL(10,2) NOT NULL CHECK (total >= 0),
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  CONSTRAINT chk_status CHECK (status IN ('pending','paid','shipped','delivered','cancelled'))
);

-- 分区表（按时间分区大表）
CREATE TABLE events (
  id BIGSERIAL,
  event_time TIMESTAMPTZ NOT NULL,
  event_data JSONB
) PARTITION BY RANGE (event_time);

CREATE TABLE events_2026_01 PARTITION OF events
  FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');
```

**处理**: 按照skill规范执行Schema设计与规范化操作,遵循单一意图原则。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `schema设计与规范化` 选项
- 处理流程: 接收输入 -> 执行Schema设计与规范化 -> 返回结果
- 输入: 用户提供Schema设计与规范化所需的参数和指令
- 输出: 返回Schema设计与规范化的执行结果,包含操作状态和输出数据

### 4. 事务与并发控制
```sql
-- 隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;   -- PostgreSQL默认
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;     -- 最高隔离，防幻读

-- 乐观锁（版本号控制）
UPDATE products SET stock = stock - 1, version = version + 1
WHERE id = 42 AND version = 5;
-- 若affected_rows = 0，说明已被其他事务修改，需重试

-- 悲观锁（SELECT FOR UPDATE）
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- 业务逻辑
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- 死锁避免：固定加锁顺序
-- 事务A: 先锁account 1 再锁account 2
-- 事务B: 先锁account 1 再锁account 2（而非先2后1）
```

**输入**: 用户提供事务与并发控制所需的指令和必要参数。
**处理**: 按照skill规范执行事务与并发控制操作,遵循单一意图原则。
**输出**: 返回事务与并发控制的执行结果,包含操作状态和输出数据。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `事务与并发控制` 选项

### 5. 高级查询模式
```sql
-- UPSERT（存在则更新，不存在则插入）
INSERT INTO users (email, name, updated_at)
VALUES ('test@example.com', 'Test', NOW())
ON CONFLICT (email) DO UPDATE
SET name = EXCLUDED.name, updated_at = NOW();

-- LATERAL JOIN（子查询引用外层表）
SELECT u.name, recent_orders.*
FROM users u
LEFT JOIN LATERAL (
  SELECT * FROM orders
  WHERE orders.user_id = u.id
  ORDER BY created_at DESC
  LIMIT 3
) recent_orders ON true;

-- 交叉表（行转列）
SELECT user_id,
  SUM(CASE WHEN month = 1 THEN amount ELSE 0 END) AS jan,
  SUM(CASE WHEN month = 2 THEN amount ELSE 0 END) AS feb,
  SUM(CASE WHEN month = 3 THEN amount ELSE 0 END) AS mar
FROM monthly_spending
GROUP BY user_id;
```

**处理**: 按照skill规范执行高级查询模式操作,遵循单一意图原则。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `高级查询模式` 选项
- 处理流程: 接收输入 -> 执行高级查询模式 -> 返回结果
- 输入: 用户提供高级查询模式所需的参数和指令
- 输出: 返回高级查询模式的执行结果,包含操作状态和输出数据

### 6. 数据库运维
```sql
-- VACUUM ANALYZE（回收空间+更新统计信息）
VACUUM ANALYZE orders;

-- 查看表大小和索引大小
SELECT
  relname AS table_name,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
  pg_size_pretty(pg_relation_size(relid)) AS table_size,
  pg_size_pretty(pg_indexes_size(relid)) AS index_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

-- 慢查询日志配置
ALTER SYSTEM SET log_min_duration_statement = 1000;  -- 记录>1秒的查询
ALTER SYSTEM SET shared_buffers = '256MB';
ALTER SYSTEM SET work_mem = '4MB';
SELECT pg_reload_conf();
```

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 查询优化 | 慢SQL+表结构 | EXPLAIN分析+优化建议+改写SQL |
| 索引设计 | 表结构+查询模式 | 索引创建方案+预期效果分析 |
| Schema设计 | 业务需求+数据关系 | 建表语句+约束+索引+分区策略 |
| 事务设计 | 并发场景+一致性需求 | 隔离级别选择+锁策略+死锁预防 |
| 数据迁移 | 源表+目标表 | 迁移SQL+数据校验+回滚方案 |

**不适用于**：NoSQL数据库设计、NewSQL分布式事务、数据库内核开发。

## 使用流程

1. 确认数据库类型（PostgreSQL/MySQL/SQLite）
2. 分析表结构和数据量
3. 使用 `EXPLAIN ANALYZE` 诊断查询性能
4. 根据诊断结果选择优化策略（索引/重写/分区/反规范化）
5. 验证优化效果并评估副作用

#
## 示例

### 示例1：慢查询优化
```
输入: SELECT * FROM orders WHERE DATE(created_at) = '2026-07-21' （慢查询5秒）
诊断: DATE()函数导致created_at索引失效，全表扫描
优化: SELECT * FROM orders WHERE created_at >= '2026-07-21' AND created_at < '2026-07-22'
效果: 使用idx_orders_created_at索引，查询时间从5s降至12ms
```

### 示例2：索引策略
```
输入: 频繁查询 SELECT * FROM products WHERE category = 'electronics' AND price < 1000
分析: 两个条件都需要索引，category等值+price范围
方案: CREATE INDEX idx_products_cat_price ON products(category, price)
说明: 等值列在前，范围列在后，充分利用复合索引
```

### 示例3：N+1问题修复
```
输入: ORM生成100个用户各自查询订单（100+1次查询）
修复: SELECT u.*, o.* FROM users u LEFT JOIN orders o ON u.id = o.user_id WHERE u.id IN (...)
效果: 101次查询合并为1次，响应时间从2s降至80ms
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `EXPLAIN ANALYZE` 显示Seq Scan而非Index Scan | 查询条件导致索引失效（函数包裹列/类型不匹配/OR条件） | 移除列上的函数（`DATE(col)`→范围查询），确保比较类型一致，OR改为UNION ALL |
| `INSERT` 报 deadlock detected | 两个事务以不同顺序锁定相同资源 | 统一加锁顺序（按主键排序后加锁），缩小事务范围，使用`ON CONFLICT`替代先查后插 |
| 查询使用 `LIKE '%keyword%'` 全表扫描 | 前缀通配符无法使用B-Tree索引 | 使用全文检索（`tsvector`+`GIN`索引）或trigram索引（`pg_trgm`扩展） |
| 索引存在但未使用 | 统计信息过期或数据分布倾斜 | 执行 `VACUUM ANALYZE tablename` 更新统计信息，检查 `pg_stats` 查看数据分布 |
| `SERIALIZABLE` 隔离级别下频繁序列化失败 | 并发冲突率高，风暴 | 降级为`READ COMMITTED`+应用层乐观锁，或使用 advisory lock 减少冲突范围 |
| 连接池耗尽 "too many connections" | 连接泄漏或并发过高 | 检查应用是否正确释放连接，配置连接池上限（如PgBouncer `max_client_conn=100`），使用 `pg_stat_activity` 排查长事务 |

## 常见问题

### Q1: `EXPLAIN ANALYZE` 和 `EXPLAIN` 有什么区别？
`EXPLAIN` 仅显示查询计划（预估成本），不实际执行查询。`EXPLAIN ANALYZE` 实际执行查询并显示实际耗时和行数。生产环境慎用 `EXPLAIN ANALYZE` 执行UPDATE/DELETE（会真实修改数据），可包裹在事务中回滚：`BEGIN; EXPLAIN ANALYZE UPDATE...; ROLLBACK;`。分析SELECT时优先用 `EXPLAIN ANALYZE`，因为它显示预估与实际的偏差。

### Q2: 复合索引的列顺序如何决定？
列顺序遵循"等值在前，范围在后"原则。例如 `WHERE category = 'A' AND price > 100`，索引应为 `(category, price)`——等值条件category先定位到匹配行，再在子集上用price范围扫描。如果反过来 `(price, category)`，price的范围扫描后还需逐行检查category，效率更低。通用规则：等值列→排序列→范围列。

### Q3: 什么时候应该反规范化？
反规范化适用于读多写少、查询性能优先于写入一致性的场景。典型场景：1)频繁JOIN的读路径（冗余存储关联字段）；2)实时统计需求（预计算聚合表）；3)历史快照（订单冗余存储下单时的商品价格）。反规范化的代价是写入时需同步更新冗余字段（可能需要触发器或应用层保证一致性），以及存储空间增加。

### Q4: 乐观锁和悲观锁如何选择？
乐观锁适用于读多写少、冲突概率低的场景——通过版本号`version`字段实现，更新时检查版本，失败则重试。优势是无锁等待、高并发友好。悲观锁（`SELECT FOR UPDATE`）适用于写多、冲突概率高、一致性要求严格的场景——直接锁定行，其他事务等待。劣势是降低并发度、可能死锁。资金扣减等关键操作通常用悲观锁，用户信息更新等低冲突场景用乐观锁。

### Q5: PostgreSQL的MVCC如何影响VACUUM？
PostgreSQL的MVCC（多版本并发控制）中，UPDATE/DELETE不立即删除旧数据，而是标记为"死元组"。这些死元组占据磁盘空间，需要VACUUM回收。`VACUUM` 标记空间可重用，`VACUUM FULL` 物理回收空间（需排他锁）。配置 `autovacuum` 自动执行。高写入表需要更频繁的VACUUM，可通过 `ALTER TABLE tablename SET (autovacuum_vacuum_scale_factor = 0.05)` 调整触发阈值。

### Q6: 分区表什么时候用？用什么分区策略？
分区表适用于单表数据量超过1000万行、且查询通常只涉及部分数据的场景。分区策略：1)范围分区（按时间，适合日志/订单等时序数据）；2)列表分区（按地区/类别，适合有明显分类的数据）；3)哈希分区（均匀分布，适合无明显查询模式的超大表）。分区裁剪（partition pruning）确保查询只扫描相关分区，是性能提升的关键。注意：分区键必须是主键的一部分，跨分区查询有额外开销。

## 已知限制

- 语法以PostgreSQL为主，MySQL/SQLite有差异
- 无法连接实际数据库执行验证
- 性能优化建议基于通用模式，实际效果需在真实环境验证
- 分布式数据库（CockroachDB/TiDB）有额外限制
- 存储过程和触发器的深度调试需数据库管理员介入
