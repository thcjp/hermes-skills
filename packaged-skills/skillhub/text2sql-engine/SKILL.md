---

slug: "text2sql-engine"
name: "text2sql-engine"
version: 1.0.1
displayName: "自然语言转SQL专业版"
summary: "全功能NL2SQL引擎，支持复杂多表查询、性能优化、查询解释与替代方案生成。面向数据工程师与DBA的全功能自然语言转SQL引擎，支持复杂多表关联、窗口函数、查询性能优化与执行计划分析。核心能"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  面向数据工程师与DBA的全功能自然语言转SQL引擎，支持复杂多表关联、窗口函数、查询性能优化与执行计划分析。核心能力：在免费版基础上新增多表嵌套JOIN、子查询/CTE/窗口函数、查询解释注释、替代方案对比、执行计划分析、索引优化建议、SQL安全审计等高级特性。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策.
tags:
  - 数据查询
  - SQL优化
  - 数据工程
  - 性能调优
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 写作
  - 电商
  - AI代理
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# 自然语言转SQL专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 自然语言转SQL专业版支持复杂多表查询 | 不支持 | 支持 |
| 自然语言转SQL专业版询解释与替代方案生成 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 说明 | 专业版增强 |
|:-----|:-----|:-----|
| 自然语言意图解析 | 意图到SQL子句映射 | 支持复杂嵌套意图解析 |
| Schema自动识别 | 表结构提取 | 支持视图、物化视图、分区表 |
| 多表JOIN | 表关联推导 | 无限表数，支持嵌套JOIN |
| 子查询与CTE | 复杂查询结构 | 子查询/CTE/递归CTE |
| 窗口函数 | 分析函数 | RANK/DENSE_RANK/LAG/LEAD/ROW_NUMBER |
| 查询解释 | 内联注释 | 逐子句解释+执行顺序标注 |
| 替代方案 | 多种写法对比 | 3+种方案+性能对比 |
| 执行计划分析 | EXPLAIN解析 | 索引使用/扫描类型/成本估算 |
| 索引优化建议 | 索引推荐 | 复合索引/覆盖索引/部分索引 |
| SQL安全审计 | 安全检查 | 注入风险/权限越界/敏感数据访问 |
| 多方言适配 | 方言兼容 | `关系型数据库`/MySQL/SQLite/SQL Server/Oracle |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 自然语言意图解析

针对自然语言意图,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供自然语言意图解析相关的配置参数、输入数据和处理选项.
**输出**: 返回自然语言意图解析的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`自然语言意图解析`的配置文档进行参数调优
### Schema自动识别

针对Schema自动识别,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Schema自动识别相关的配置参数、输入数据和处理选项.
**输出**: 返回Schema自动识别的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Schema自动识别`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：复杂报表生成（数据分析师视角）

某电商平台需要生成"各品类月度销售额环比增长率"报表，涉及商品表、订单表、订单明细表、品类表四张表的关联，并需要窗口函数计算环比.
向Agent描述需求：

```
查询每个品类每月的销售总额，并计算与上月的环比增长率，按品类和月份排序
```

Agent生成：

```sql
WITH monthly_sales AS (
    SELECT
        c.category_name,
        DATE_TRUNC('month', o.created_at) AS month,
        SUM(oi.quantity * oi.unit_price) AS total_sales
    FROM categories c
    INNER JOIN products p ON c.id = p.category_id
    INNER JOIN order_items oi ON p.id = oi.product_id
    INNER JOIN orders o ON oi.order_id = o.id
    WHERE o.status = 'completed'
    GROUP BY c.category_name, DATE_TRUNC('month', o.created_at)
),
sales_with_prev AS (
    SELECT
        category_name,
        month,
        total_sales,
        LAG(total_sales) OVER (
            PARTITION BY category_name
            ORDER BY month
        ) AS prev_month_sales
    FROM monthly_sales
)
SELECT
    category_name,
    month,
    total_sales,
    prev_month_sales,
    CASE
        WHEN prev_month_sales IS NULL THEN NULL
        WHEN prev_month_sales = 0 THEN NULL
        ELSE ROUND(
            (total_sales - prev_month_sales) * 100.0 / prev_month_sales, 2
        )
    END AS growth_rate_pct
FROM sales_with_prev
ORDER BY category_name, month;
```

### 场景二：慢查询优化（DBA视角）

某系统有一条查询响应时间超过30秒，DBA需要定位性能瓶颈并优化。专业版提供执行计划分析：

```sql
-- 原始查询
EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 12345 ORDER BY created_at DESC;
# ...
-- 专业版分析结果
-- Seq Scan on orders (cost=0.00..45230.00 rows=1500 width=256) (actual time=0.050..850.230)
--   Filter: (customer_id = 12345)
--   Rows Removed by Filter: 1500000
-- Sort (cost=45230.00..45233.75 rows=1500 width=256) (actual time=850.300..850.500)
--   Sort Key: created_at DESC
--   Sort Method: quicksort Memory: 256kB
# ...
-- 优化建议：
-- 1. 添加复合索引：CREATE INDEX idx_orders_customer_created ON orders(customer_id, created_at DESC);
-- 2. 避免SELECT *，只查必要字段
-- 3. 预期优化后响应时间：<50ms
```

优化后查询：

```sql
SELECT id, order_no, amount, status, created_at
FROM orders
WHERE customer_id = 12345
ORDER BY created_at DESC
LIMIT 100;
```

### 场景三：数据迁移与兼容（数据工程师视角）

某团队从MySQL迁移到 `关系型数据库`，需要将现有SQL语法进行转换。专业版支持方言间自动转换：

```sql
-- MySQL原始查询
SELECT
    user_id,
    DATE_FORMAT(created_at, '%Y-%m') AS month,
    COUNT(*) AS order_count,
    GROUP_CONCAT(product_name SEPARATOR ', ') AS products
FROM orders
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
GROUP BY user_id, DATE_FORMAT(created_at, '%Y-%m')
HAVING order_count > 5;
# ...
-- 自动转换为PostgreSQL
SELECT
    user_id,
    TO_CHAR(created_at, 'YYYY-MM') AS month,
    COUNT(*) AS order_count,
    STRING_AGG(product_name, ', ') AS products
FROM orders
WHERE created_at >= NOW() - INTERVAL '6 months'
GROUP BY user_id, TO_CHAR(created_at, 'YYYY-MM')
HAVING COUNT(*) > 5;
```

## 使用流程

### 使用流程(补充)

1. **提供完整Schema**：包括表结构、视图、索引、外键关系
2. **描述查询需求**：用自然语言描述，越详细越好
3. **选择目标方言**：指定 `关系型数据库`/MySQL/SQLite等
4. **获取SQL+解释+优化建议**：一次生成完整方案

```
数据库类型：关系型数据库
表结构：[粘贴CREATE TABLE语句]
查询需求：查询过去6个月每月新增用户数、活跃用户数、付费用户数，并计算付费转化率，按月份排序
```

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | text2sql-engine处理的内容输入 |,  |
| content | string | 否 | text2sql-engine处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "engine 相关配置参数",
    result: "engine 相关配置参数",
    result: "engine 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 问题现象 | 可能原因 | 排查步骤 | 优先级 |
|:---:|:---:|:---:|:---:|
| 生成的SQL执行报错 | Schema不完整或方言不匹配 | 核对Schema字段，确认数据库版本 | P0 |
| 查询结果不正确 | 意图解析偏差 | 细化需求描述，检查WHERE/HAVING条件 | P0 |
| 查询超时 | 缺少索引或全表扫描 | 查看执行计划，按建议添加索引 | P1 |
| 方言转换失败 | 不支持的特有语法 | 查看转换日志，手动调整不兼容部分 | P1 |
| 安全审计误报 | 规则过于严格 | 查看审计规则配置，调整白名单 | P2 |
| 替代方案性能差异大 | 数据分布不均匀 | 使用真实数据测试，参考执行计划成本 | P2 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **数据库**: `关系型数据库` 10+ / MySQL 5.7+ / SQLite 3.25+ / SQL Server 2017+ / Oracle 12c+

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| `关系型数据库` | 数据库 | 推荐 | 官方安装或云服务 |
| MySQL | 数据库 | 可选 | 官方安装或云服务 |
| pg_stat_statements | PG扩展 | 推荐 | `关系型数据库`自带 contrib 模块 |
| psql客户端 | CLI工具 | 推荐 | 随 `关系型数据库` 安装 |

### API Key 配置
- **数据库连接串**: 存储于环境变量 `DATABASE_URL`，格式 `关系型数据库://user:pass@host:port/dbname`
- **只读连接**: 建议使用只读账户进行查询验证，避免误操作
- **禁止**: 在代码或脚本中硬编码数据库密码
- **推荐**: 使用密钥管理服务（如HashiCorp Vault）管理数据库凭证

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成企业级SQL查询

## 案例展示

### 递归CTE配置（组织架构查询）

```sql
WITH RECURSIVE org_tree AS (
    -- 基础查询：优秀管理者
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
# ...
    UNION ALL
# ...
    -- 递归查询：下属员工
    SELECT e.id, e.name, e.manager_id, ot.level + 1
    FROM employees e
    INNER JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT level, COUNT(*) AS headcount, STRING_AGG(name, ', ') AS members
FROM org_tree
GROUP BY level
ORDER BY level;
```

### 窗口函数配置（用户留存分析）

```sql
SELECT
    signup_date,
    user_count,
    day1_retention,
    ROUND(day1_retention * 100.0 / user_count, 2) AS day1_rate,
    day7_retention,
    ROUND(day7_retention * 100.0 / user_count, 2) AS day7_rate
FROM (
    SELECT
        signup_date,
        COUNT(DISTINCT user_id) AS user_count,
        COUNT(DISTINCT CASE WHEN last_active >= signup_date + INTERVAL '1 day'
            THEN user_id END) AS day1_retention,
        COUNT(DISTINCT CASE WHEN last_active >= signup_date + INTERVAL '7 days'
            THEN user_id END) AS day7_retention
    FROM user_activity
    GROUP BY signup_date
) t
ORDER BY signup_date;
```

### 索引优化建议模板

```sql
-- 专业版自动生成的索引建议
-- 查询模式：WHERE status = 'active' AND created_at > '2024-01-01'
-- 当前问题：Seq Scan，扫描全表500万行
# ...
-- 建议索引1：复合索引（覆盖查询条件）
CREATE INDEX CONCURRENTLY idx_orders_status_created
    ON orders(status, created_at DESC)
    WHERE status = 'active';  -- 部分索引，减小体积
# ...
-- 建议索引2：覆盖索引（包含查询字段）
CREATE INDEX CONCURRENTLY idx_orders_covering
    ON orders(status, created_at DESC)
    INCLUDE (order_no, amount, customer_id);
# ...
-- 预期效果：
-- Seq Scan -> Index Only Scan
-- 扫描行数：500万 -> 约2000
-- 响应时间：2.5s -> <10ms
```

## 常见问题

### Q1：专业版支持多少张表的JOIN？

A：无限制。专业版支持任意数量的表关联，自动推导JOIN关系。对于超过5张表的复杂查询，会生成可视化的关系图帮助理解.
### Q2：执行计划分析支持哪些数据库？

A：支持 `关系型数据库`（EXPLAIN ANALYZE）、MySQL（EXPLAIN FORMAT=JSON）、SQLite（EXPLAIN QUERY PLAN）。分析结果包括扫描类型、索引使用、成本估算、实际耗时等.
### Q3：索引优化建议是否自动执行？

A：不会自动执行。专业版只生成建议（CREATE INDEX语句），需DBA审核后手动执行。建议使用 `CONCURRENTLY` 选项避免锁表.
### Q4：SQL安全审计能检测哪些风险？

A：覆盖6类安全风险：SQL注入、权限越界、敏感数据暴露、危险操作（全表删除/更新）、笛卡尔积、资源消耗过大。审计结果按严重程度分级.
### Q5：方言转换的准确率如何？

A：对于标准SQL语法，转换准确率>95%。部分数据库特有语法（如Oracle的CONNECT BY）会转换为标准CTE等价写法，并标注转换说明.
### Q6：如何处理超大型表的查询？

A：专业版建议使用分区策略：(1) 按时间范围分区（时序数据）；(2) 按Hash分区（均匀分布）；(3) 使用物化视图预聚合。同时生成对应的分区DDL语句.
### Q7：窗口函数和GROUP BY有什么区别？

A：GROUP BY会折叠行（每组一行），窗口函数保留原始行并添加聚合值。窗口函数适合需要在明细数据旁边展示聚合值的场景，如"每个员工薪资与部门平均薪资的差值".
### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

A：数据库层面有限制（`关系型数据库`默认100层），可在查询中设置 `SET max_recursion_depth = N`。专业版会检测递归深度并在接近限制时发出警告.
### Q9：专业版是否支持NoSQL查询转换？

A：当前版本不支持。专业版专注于关系型SQL。如需MongoDB/ES等NoSQL查询，请关注后续版本更新.
### Q10：如何获取优先技术支持？

A：专业版用户提供7x24小时优先支持通道，可通过专属工单系统提交问题，平均响应时间<4小时，关键问题<1小时.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 依赖Agent平台的LLM能力与运行环境配置
- 免费版功能受限，高级能力需升级专业版
