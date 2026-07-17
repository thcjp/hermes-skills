---
slug: duckdb-analytics-engine
name: duckdb-analytics-engine
version: "1.0.0"
displayName: "DuckDB分析引擎"
summary: "无需服务器,直接SQL查询CSV/Parquet/JSON,嵌入式OLAP秒级分析"
license: MIT
description: |-
  DuckDB分析引擎——无需服务器,进程内运行的嵌入式列式OLAP数据库。直接SQL查询CSV/Parquet/JSON如同查询数据库表,零部署成本,秒级出结果,让数据分析像查数据库一样简单。

  核心能力:
  - 文件直接查询:CSV/Parquet/JSON无需导入,SQL直接查
  - 多源联合分析:CSV JOIN Parquet JOIN JSON跨格式关联
  - SQL聚合与窗口:完整SQL支持,聚合/窗口/CTE/复杂查询
  - Python/Node集成:嵌入式调用,替代Pandas大数据处理
  - Schema推断:自动识别列类型,零配置上手
  - ETL处理:读取→转换→写入,数据管道一站式

  适用场景:
  - 独立创业者数据分析:本地CSV秒级分析,无需搭建数据库
  - 副业达人日志分析:服务器日志解析+聚合+过滤
  - 一人公司报表生成:SQL聚合→CSV/Excel输出
  - 数据工程师ETL:替代Pandas处理大数据,列式存储+向量化

  差异化:不是需要部署的数据库服务,而是进程内嵌入式OLAP引擎,零服务器成本直接查询文件数据,让个人开发者也能拥有大数据分析能力。

  触发关键词:DuckDB、OLAP、分析数据库、嵌入式数据库、CSV查询、Parquet、数据分析、ETL、数据探索、报表
tags: [数据分析, DuckDB, OLAP, 数据探索, SQL查询]
tools: [read, exec]
---

# DuckDB分析引擎

使用 DuckDB 嵌入式列式数据库,直接对文件数据进行高性能SQL分析。无需服务器,进程内运行,查询CSV/Parquet/JSON如同查询数据库表。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| CSV分析 | 有CSV文件需要分析 | 直接SQL查询,无需导入数据库 |
| 日志分析 | 服务器日志文件 | 解析+聚合+过滤 |
| 数据探索 | 快速了解数据集 | Schema推断+统计+采样 |
| ETL处理 | 数据转换与清洗 | 读取→转换→写入 |
| 多源关联 | 多文件/多格式关联 | CSV JOIN Parquet JOIN JSON |
| 报表生成 | 定期报表 | SQL聚合→CSV/Excel输出 |
| 数据管道 | 替代Pandas大数据处理 | 列式存储+向量化执行 |

## 工作流

### 1. 数据加载

1. **CSV 直接查询**
   - `SELECT * FROM 'data.csv'`:自动推断Schema
   - 支持分隔符/标题行/引号/转义
   - 大文件流式读取(不全部加载内存)
   - 类型推断(整数/浮点/日期/字符串)
2. **Parquet 查询**
   - `SELECT * FROM 'data.parquet'`:直接读取
   - 列式存储,只读需要的列
   - 谓词下推(filter pushdown)
   - 多文件:`SELECT * FROM 'data/*.parquet'`
3. **JSON 查询**
   - `SELECT * FROM 'data.json'`:JSON数组
   - `SELECT unnest(json_data) FROM ...`:展开嵌套
   - JSON函数:`json_extract()`, `json_array_length()`
4. **多源关联**
   - CSV JOIN Parquet:`SELECT * FROM 'a.csv' a JOIN 'b.parquet' b ON a.id = b.id`
   - 混合格式查询:不同格式表统一SQL

### 2. SQL 分析

1. **聚合分析**
   - 基本聚合:`SUM/AVG/COUNT/MIN/MAX`
   - 分组:`GROUP BY` + `HAVING`
   - 去重计数:`COUNT(DISTINCT)`
   - 近似计数:`approx_count_distinct()`
2. **窗口函数**
   - 排名:`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`
   - 累计:`SUM() OVER (ORDER BY ...)`
   - 移动平均:`AVG() OVER (ROWS BETWEEN ...)`
   - LAG/LEAD:前一行/后一行
3. **时间序列**
   - 日期函数:`date_trunc()`, `date_diff()`
   - 时间窗口:`WINDOW` + `PARTITION BY`
   - 趋势分析:同比/环比
4. **统计函数**
   - 描述统计:`mean()`, `stddev()`, `median()`, `quantile()`
   - 相关性:`corr()`, `covar_pop()`
   - 回归:`regr_slope()`, `regr_intercept()`

### 3. 数据转换

1. **清洗**
   - 去重:`SELECT DISTINCT`
   - 空值处理:`COALESCE()`, `NULLIF()`
   - 类型转换:`CAST()`, `::type`
   - 字符串处理:`trim()`, `regexp_replace()`
2. **重塑**
   - 长转宽:`PIVOT`
   - 宽转长:`UNPIVOT`
   - 行转列:`CASE WHEN`
   - 嵌套展开:`UNNEST()`, `STRUCT`
3. **输出**
   - 写入CSV:`COPY (SELECT ...) TO 'output.csv'`
   - 写入Parquet:`COPY (SELECT ...) TO 'output.parquet' (FORMAT PARQUET)`
   - 写入JSON:`COPY (SELECT ...) TO 'output.json' (FORMAT JSON)`

### 4. Python 集成

1. **Pandas 替代**
   ```python
   import duckdb
   # 直接查询CSV(比Pandas快10-100x)
   result = duckdb.sql("SELECT * FROM 'data.csv' WHERE amount > 100").df()
   ```
2. **Pandas 互操作**
   ```python
   import pandas as pd
   df = pd.read_csv('data.csv')
   # 直接对DataFrame执行SQL
   result = duckdb.sql("SELECT category, SUM(amount) FROM df GROUP BY 1").df()
   ```
3. **大数据处理**
   - 流式处理:逐块读取处理
   - 并行执行:多线程
   - 内存映射:不全部加载内存

### 5. Node.js 集成

1. **基础使用**
   ```javascript
   const duckdb = require('duckdb');
   const db = new duckdb.Database(':memory:');
   db.all("SELECT * FROM 'data.csv' LIMIT 10", (err, rows) => { ... });
   ```
2. **异步查询**
   ```javascript
   const conn = db.connect();
   const result = await conn.all("SELECT COUNT(*) FROM 'data.parquet'");
   ```

## 依赖说明

| 依赖类型 | 要求 | 说明 |
|:---------|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| 运行环境 | Python 3.8+ 或 Node.js 16+ | DuckDB 嵌入式运行 |
| 安装 | `pip install duckdb` 或 `npm install duckdb` | 单一依赖,无外部服务 |
| 数据 | CSV/Parquet/JSON 文件 | 本地或远程(HTTP/S3) |
| 可选 | Pandas | Python数据分析集成 |
| 可选 | S3/GCS 访问凭证 | 远程文件查询 |

## 异常处理

| 异常场景 | 处理方式 |
|:---------|:---------|
| CSV格式异常 | 指定分隔符/引号/转义参数 |
| 内存不足 | 使用流式读取,分块处理 |
| 类型推断错误 | 手动指定列类型:`read_csv_auto()` → `read_csv()` |
| 大文件慢 | 转换为Parquet(列式+压缩),再查询 |
| 编码问题 | 指定编码:`COPY ... (ENCODING 'UTF-8')` |
| 远程文件超时 | 设置超时,下载到本地再查询 |

## 示例

### 输入:销售数据分析

```
用户请求:分析sales.csv中的销售数据,按月统计销售额和订单量

输出SQL:
WITH monthly AS (
  SELECT
    date_trunc('month', order_date) AS month,
    SUM(amount) AS revenue,
    COUNT(*) AS orders,
    COUNT(DISTINCT customer_id) AS unique_customers
  FROM 'sales.csv'
  GROUP BY 1
)
SELECT
  month,
  revenue,
  orders,
  unique_customers,
  revenue / orders AS avg_order_value,
  revenue / unique_customers AS revenue_per_customer,
  LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
  (revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month) * 100 AS mom_growth_pct
FROM monthly
ORDER BY month;
```

### 输入:多文件关联分析

```
用户请求:关联orders.parquet和customers.csv,分析客户分群

输出SQL:
WITH customer_stats AS (
  SELECT
    c.customer_id,
    c.name,
    c.signup_date,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_spent,
    AVG(o.amount) AS avg_order_value,
    MAX(o.order_date) AS last_order_date,
    date_diff('day', MAX(o.order_date), CURRENT_DATE) AS days_since_last_order
  FROM 'customers.csv' c
  LEFT JOIN 'orders/*.parquet' o ON c.customer_id = o.customer_id
  GROUP BY 1, 2, 3
)
SELECT
  customer_id,
  name,
  total_orders,
  total_spent,
  CASE
    WHEN days_since_last_order < 30 THEN '活跃'
    WHEN days_since_last_order < 90 THEN '沉默'
    ELSE '流失'
  END AS customer_status,
  CASE
    WHEN total_spent > 10000 THEN '高价值'
    WHEN total_spent > 1000 THEN '中价值'
    ELSE '低价值'
  END AS value_segment
FROM customer_stats
ORDER BY total_spent DESC;
```
