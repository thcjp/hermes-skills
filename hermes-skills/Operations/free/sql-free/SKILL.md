---
name: "sql-free"
description: "多数据库SQL查询、优化、schema设计与数据分析，支持MySQL/PostgreSQL/SQLite/SQLServer。免费版"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "SQL查询助手(免费版)"
  version: "1.0.0"
  summary: "多数据库SQL查询、优化、schema设计与数据分析，支持MySQL/PostgreSQL/SQLite/SQLServer。免费版"
  tags:
    - "数据存储"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# SQL查询助手(免费版)

SQL查询与数据库操作辅助引擎，支持MySQL、PostgreSQL、SQLite、SQLServer，覆盖自然语言转SQL、性能优化与Schema设计。

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

### 1. 自然语言转SQL
将自然语言问题转换为SQL查询，自动适配目标数据库方言：

```sql
-- MySQL: 查找过去30天消费超1000的VIP用户
SELECT u.user_id, u.name, SUM(o.amount) AS total_spent
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE u.is_vip = 1
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY u.user_id, u.name
HAVING total_spent > 1000;
```

支持的方言差异自动处理：
- 日期函数：`NOW()`/`CURRENT_TIMESTAMP`/`GETDATE()`
- 分页：`LIMIT OFFSET`/`FETCH NEXT`
- 字符串拼接：`CONCAT()`/`||`/`+`
- 自增主键：`AUTO_INCREMENT`/`SERIAL`/`IDENTITY`

### 2. 查询性能优化
分析SQL查询性能并提供优化建议：
- **EXPLAIN分析**：解读执行计划，识别全表扫描、临时表、文件排序
- **索引建议**：基于WHERE/JOIN/ORDER BY子句推荐索引
- **查询重写**：子查询转JOIN、避免SELECT *、减少嵌套层级
- **N+1问题检测**：识别ORM生成的低效查询模式

### 3. 数据库Schema设计
- **表结构设计**：字段类型选择、约束设计、范式化/反范式化权衡
- **索引策略**：主键/唯一索引/联合索引/覆盖索引设计
- **ER图生成**：表关系可视化（Mermaid格式）
- **迁移脚本**：DDL生成与版本管理

**输入**: 用户提供数据库Schema设计所需的指令和必要参数。
**处理**: 按照skill规范执行数据库Schema设计操作,遵循单一意图原则。

### 4. 复杂分析查询
- **窗口函数**：`ROW_NUMBER()`/`RANK()`/`LAG()`/`LEAD()`/`SUM() OVER()`
- **CTE递归**：层级数据查询（组织架构/评论树/目录树）
- **聚合分析**：`GROUP BY`/`HAVING`/`ROLLUP`/`CUBE`
- **时间序列**：同比/环比/移动平均/累计求和

**输入**: 用户提供复杂分析查询所需的指令和必要参数。
**输出**: 返回复杂分析查询的执行结果,包含操作状态和输出数据。

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 查询生成 | 自然语言问题+表结构 | 可执行SQL+方言适配 |
| 性能调优 | 慢查询SQL+表数据量 | EXPLAIN分析+优化建议+重写SQL |
| Schema设计 | 业务需求描述 | 表结构DDL+索引策略+ER图 |
| 数据分析 | 分析维度+指标 | 窗口函数/CTE查询+结果解读 |

**不适用于**：数据库运维（备份/主从配置）、NoSQL查询、数据库安全审计。

## 使用流程

1. 确定目标数据库类型（MySQL/PostgreSQL/SQLite/SQLServer）
2. 提供表结构（CREATE TABLE语句或schema描述）
3. 描述查询需求（自然语言或SQL片段）
4. 生成/优化SQL并标注方言差异
5. 可选：执行验证并解读结果

## 示例

### 示例1：复杂分析查询
```sql
-- PostgreSQL: 计算每个用户消费的环比增长率
WITH monthly_spending AS (
  SELECT
    user_id,
    DATE_TRUNC('month', created_at) AS month,
    SUM(amount) AS total
  FROM orders
  WHERE created_at >= NOW() - INTERVAL '6 months'
  GROUP BY user_id, month
)
SELECT
  user_id,
  month,
  total,
  LAG(total) OVER (PARTITION BY user_id ORDER BY month) AS prev_month,
  ROUND(
    (total - LAG(total) OVER (PARTITION BY user_id ORDER BY month))
    / LAG(total) OVER (PARTITION BY user_id ORDER BY month) * 100,
    2
  ) AS growth_rate_pct
FROM monthly_spending
ORDER BY user_id, month;
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `ERROR 1146: Table doesn't exist` | 表名拼写错误或未选择数据库 | 检查表名大小写（Linux下MySQL区分大小写），执行 `SHOW TABLES;` 确认表存在，执行 `USE database_name;` 选择数据库 |
| `ERROR 1052: Column 'id' in field list is ambiguous` | JOIN多表存在同名字段未指定表前缀 | 为所有字段添加表别名前缀，如 `SELECT u.id, o.id FROM users u JOIN orders o` |
| 查询超时或极慢 | 缺少索引或全表扫描大数据量 | 执行 `EXPLAIN` 检查执行计划，为WHERE/JOIN条件添加索引，避免 `SELECT *`，考虑分页查询 |
| `ERROR 1064: Syntax error` | SQL语法错误或方言不兼容 | 根据目标数据库方言调整语法，如MySQL用反引号 `` ` `` 包裹保留字，PostgreSQL用双引号 `"` |

## 常见问题

### Q1: 如何选择数据库方言？生成的SQL如何适配不同数据库？
开始查询前明确目标数据库类型。引擎自动处理方言差异：日期函数（MySQL `DATE_SUB()` vs PostgreSQL `INTERVAL`）、分页（MySQL `LIMIT offset, count` vs SQLServer `OFFSET FETCH`）、字符串函数（`CONCAT()` vs `||`）。如果不确定目标数据库，默认生成标准SQL，标注需要按方言调整的部分。

### Q2: EXPLAIN执行计划中哪些指标最关键？
重点关注：`type`（访问类型，`ALL`为全表扫描需优化，`ref`/`eq_ref`为索引查找）、`key`（实际使用的索引，`NULL`表示未用索引）、`rows`（预估扫描行数，越少越好）、`Extra`（`Using filesort`和`Using temporary`表示需要额外排序/临时表，通常需优化）。优化目标是将`type`从`ALL`提升到`ref`或更高，减少`rows`。

### Q3: 联合索引的最左前缀原则是什么？
联合索引`(a, b, c)`仅支持以下查询前缀：`a`、`a,b`、`a,b,c`。单独查询`b`或`c`无法使用该索引。设计联合索引时，将选择性最高的列放最前面（如`WHERE status='active'`比`WHERE created_at>'2024-01-01'`选择性高），范围查询列放最后（范围查询后的列无法走索引）。

## 已知限制

- 无法直接连接数据库执行查询（需用户提供数据库客户端或连接）
- 生成的SQL需用户自行验证执行结果
- 性能优化建议基于执行计划分析，实际效果受数据分布影响


## 升级提示

本免费版提供基础功能。升级到完整版 sql 获取全部能力和高级特性。
