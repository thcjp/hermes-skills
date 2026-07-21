---
slug: duckdb-analytics-engine
name: duckdb-analytics-engine
version: "1.0.0"
displayName: "DuckDB分析引擎"
summary: "本地分析型数据库,免部署秒级启动,GB级数据SQL查询无压力"
license: Proprietary
description: |-
  DuckDB分析引擎——为数据分析而生的嵌入式OLAP数据库,无需部署服务,单文件即用,支持GB级数据秒级SQL查询。覆盖多格式数据加载(CSV/Parquet/JSON/Excel)、跨源联邦查询、窗口函数、Pandas互操作、Jupyter集成。Use when 需要本地大数据分析、CSV/Parquet快速查询、Python数据分析加速、无需数据库服务器的OLAP分析时使用。不适用于高并发在线事务处理。
tags: [数据分析, DuckDB, SQL查询, OLAP数据库, 数据仓库]
tools:
  - read
  - exec
suggested_price: "15.00"
pricing_tier: "business"
pricing_rationale: "数据分析类, medium市场, enterprise复杂度, weekly频次, business层 → 中频专业工具,中等市场"
---
# DuckDB 分析引擎

为数据分析而生的嵌入式 OLAP 数据库。无需部署,单文件即用,支持 GB 级数据秒级查询。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| CSV/Parquet分析 | CSV/Parquet文件+SQL查询 | 查询结果(表格/CSV/JSON) |
| 日志分析 | 日志文件(已结构化) | 聚合统计+异常检测报告 |
| 数据探查EDA | 任意格式数据文件 | 数据概览+统计摘要+分布分析 |
| 数据清洗转换 | 原始数据+清洗规则 | 清洗后Parquet/CSV文件 |
| 本地数据仓库 | 多个数据文件 | 统一Schema+关联查询+物化视图 |
| Pandas替代 | 大数据集(>内存) | 流式处理结果(不全部加载内存) |

### 不适用于
- 在线事务处理OLTP(高并发写入,请用PostgreSQL/MySQL)
- 实时流数据处理(请用Flink/Spark Streaming)
- 分布式大数据处理(>TB级,请用Spark/Dask)
- 生产级数据服务(多用户并发,请用ClickHouse)
- 图数据库查询(请用Neo4j)
- 全文搜索引擎(请用Elasticsearch)

## 核心能力

1. **零部署嵌入式分析**:单文件二进制,无需服务进程,内存+磁盘混合处理,GB级数据秒级查询,列式存储+向量化执行
2. **多格式数据加载**:CSV/Parquet/JSON/Excel/Arrow自动类型推断,`read_csv_auto()`一键加载,远程文件(HTTP/S3)直接查询
3. **SQL标准支持**:窗口函数/CTE/递归查询/聚合/JOIN/UNION/PIVOT全支持,PostgreSQL兼容语法
4. **Pandas互操作**:DataFrame↔DuckDB零拷贝转换,SQL查询Pandas DataFrame,Python生态无缝集成
5. **联邦查询与扩展**:跨文件/跨数据库JOIN,PostgreSQL/MySQL/SQLite附加查询,JSON/文本/空间/HTTP扩展

## 使用流程

### Step 1: 数据加载
1. **CSV加载**:`SELECT * FROM read_csv_auto('data.csv')` 或 `CREATE TABLE t AS SELECT * FROM read_csv_auto('data.csv')`
2. **Parquet加载**:`SELECT * FROM read_parquet('data.parquet')` 或通配符加载多文件 `read_parquet('data/*.parquet')`
3. **JSON加载**:`SELECT * FROM read_json_auto('data.json')`
4. **Excel加载**:需安装 spatial 扩展 `INSTALL spatial; LOAD spatial; SELECT * FROM st_read('data.xlsx')`
5. **远程文件**:`SELECT * FROM read_csv_auto('https://example.com/data.csv')`

### Step 2: 数据探查
1. 概览:`SUMMARIZE table`(自动统计每列:最小/最大/均值/唯一值/NULL比例)
2. 抽样:`SELECT * FROM table USING SAMPLE 10 PERCENT`
3. 类型检查:`DESCRIBE table`
4. 行数统计:`SELECT count(*) FROM table`

### Step 3: 分析查询
1. **窗口函数**:`ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER()`
2. **分组聚合**:`GROUP BY` + `HAVING`,多级聚合
3. **JOIN**:INNER/LEFT/RIGHT/FULL JOIN,跨表关联
4. **CTE 递归**:`WITH RECURSIVE` 处理层级数据

### Step 4: 数据导出
1. **CSV导出**:`COPY (SELECT * FROM t) TO 'output.csv' (HEADER, DELIMITER ',')`
2. **Parquet导出**:`COPY (SELECT * FROM t) TO 'output.parquet' (FORMAT PARQUET)`
3. **JSON导出**:`COPY (SELECT * FROM t) TO 'output.json'`
4. **Excel导出**:通过Pandas `df.to_excel()`

### Step 5: Pandas 集成(可选)
1. **DuckDB→Pandas**:`df = con.execute("SELECT * FROM t").df()`
2. **Pandas→DuckDB**:`con.register('df_view', df)` 后可在SQL中查询
3. **零拷贝**:Arrow格式传输,避免序列化开销

## 工作流(详细)

### 1. 数据加载

DuckDB 支持多种格式与来源:

```sql
-- CSV(自动类型推断)
SELECT * FROM read_csv_auto('sales.csv');
CREATE TABLE sales AS SELECT * FROM read_csv_auto('sales.csv');

-- Parquet(列式存储)
SELECT * FROM read_parquet('data.parquet');
SELECT * FROM read_parquet('data/*.parquet');  -- 多文件

-- JSON
SELECT * FROM read_json_auto('events.json');

-- Excel(需 spatial 扩展)
INSTALL spatial; LOAD spatial;
SELECT * FROM st_read('data.xlsx');

-- 远程文件
SELECT * FROM read_csv_auto('https://example.com/data.csv');
```

### 2. 数据探查

```sql
-- 概览(自动统计)
SUMMARIZE sales;

-- 类型与Schema
DESCRIBE sales;

-- 抽样
SELECT * FROM sales USING SAMPLE 10 PERCENT;

-- 基础统计
SELECT
  count(*) AS total_rows,
  count(DISTINCT product) AS unique_products,
  avg(price) AS avg_price,
  sum(quantity * price) AS total_revenue
FROM sales;
```

### 3. 分析查询

```sql
-- 窗口函数:计算移动平均
SELECT
  date,
  product,
  sales,
  AVG(sales) OVER (
    PARTITION BY product
    ORDER BY date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS moving_avg_7d
FROM daily_sales;

-- CTE 递归:组织架构层级
WITH RECURSIVE org_tree AS (
  SELECT id, name, parent_id, 1 AS level
  FROM employees WHERE parent_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.parent_id, t.level + 1
  FROM employees e
  JOIN org_tree t ON e.parent_id = t.id
)
SELECT * FROM org_tree;

-- 联邦查询:跨文件 JOIN
SELECT
  o.order_id,
  o.customer_id,
  c.customer_name
FROM read_csv_auto('orders.csv') o
LEFT JOIN read_csv_auto('customers.csv') c
  ON o.customer_id = c.customer_id;
```

### 4. 数据导出

```sql
-- CSV
COPY (SELECT * FROM sales) TO 'output.csv' (HEADER, DELIMITER ',');

-- Parquet(列式存储,压缩)
COPY (SELECT * FROM sales) TO 'output.parquet' (FORMAT PARQUET);

-- JSON
COPY (SELECT * FROM sales) TO 'output.json';
```

### 5. Pandas 集成

```python
import duckdb
import pandas as pd

con = duckdb.connect()

# DuckDB → Pandas
df = con.execute("SELECT * FROM read_csv_auto('sales.csv')").df()

# Pandas → DuckDB(零拷贝)
con.register('df_view', df)
result = con.execute("SELECT product, sum(sales) FROM df_view GROUP BY product").df()
```

### 6. Jupyter 集成

```python
# Jupyter Notebook 中
%load_ext duckdb
%sql SELECT * FROM read_csv_auto('sales.csv') LIMIT 10

# 或使用 duckdb-engine
import duckdb
duckdb.sql("SELECT * FROM read_csv_auto('sales.csv')").show()
```

## 输出规范

- 查询结果:`output/{query-name}/result.csv`(或.parquet/.json)
- 分析报告:`output/{query-name}/report.md`
- SQL 脚本:`output/{query-name}/query.sql`
- 图表(配合Pandas):`output/{query-name}/charts/`(PNG)

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| DuckDB CLI | 工具 | 可选 | 下载二进制 或 `pip install duckdb` |
| Python 3.8+ | 运行时 | 可选 | Python集成使用 |
| duckdb(Python包) | Python库 | 可选 | `pip install duckdb` |
| pandas | Python库 | 可选 | Pandas互操作 `pip install pandas` |
| Jupyter | 工具 | 可选 | Jupyter集成 `pip install jupyter` |

### 安装命令

```bash
# 方式1: Python包(推荐)
pip install duckdb

# 方式2: CLI二进制
# Windows
winget install DuckDB.cli
# macOS
brew install duckdb
# Linux
sudo apt install duckdb  # 或下载二进制

# 国内镜像加速
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple duckdb
```

### API Key 配置
- 本Skill无需额外API Key配置
- DuckDB为本地嵌入式数据库,无外部服务依赖
- S3远程文件访问需配置AWS凭证(可选,由用户自行配置)

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,实际执行SQL需exec调用DuckDB CLI或Python

## 示例

### 示例1: CSV日志分析

**输入**:
```
文件:app_logs.csv(应用日志,1000万行)
列:timestamp, user_id, event, page, duration_ms, status
任务:分析用户行为,找出慢页面与错误率
```

**输出** (`output/log-analysis/query.sql`):
```sql
-- 1. 概览
SUMMARIZE read_csv_auto('app_logs.csv');

-- 2. 慢页面Top10
SELECT
  page,
  count(*) AS request_count,
  avg(duration_ms) AS avg_duration,
  percentile_cont(0.95) WITHIN GROUP (ORDER BY duration_ms) AS p95_duration,
  max(duration_ms) AS max_duration
FROM read_csv_auto('app_logs.csv')
WHERE status = 200
GROUP BY page
ORDER BY p95_duration DESC
LIMIT 10;

-- 3. 错误率分析
SELECT
  page,
  count(*) AS total_requests,
  count(CASE WHEN status >= 400 THEN 1 END) AS error_count,
  ROUND(count(CASE WHEN status >= 400 THEN 1 END) * 100.0 / count(*), 2) AS error_rate_pct
FROM read_csv_auto('app_logs.csv')
GROUP BY page
HAVING count(*) > 100
ORDER BY error_rate_pct DESC;

-- 4. 每小时趋势
SELECT
  date_trunc('hour', timestamp) AS hour,
  count(*) AS requests,
  avg(duration_ms) AS avg_duration
FROM read_csv_auto('app_logs.csv')
GROUP BY hour
ORDER BY hour;
```

**输出** (`output/log-analysis/result.csv`):
```csv
page,request_count,avg_duration,p95_duration,max_duration
/api/checkout,15234,450,1200,5600
/api/search,89234,120,380,2100
/api/product,234567,85,220,1500
```

### 示例2: 多文件联邦查询

**输入**:
```
文件:
  - orders.csv(订单数据)
  - customers.parquet(客户信息)
  - products.json(产品目录)
任务:关联三表,生成销售汇总报表
```

**输出** (`output/sales-summary/query.sql`):
```sql
-- 跨格式联邦查询
CREATE TABLE sales_summary AS
SELECT
  c.customer_name,
  c.region,
  p.product_name,
  p.category,
  o.order_date,
  o.quantity,
  o.quantity * p.price AS revenue
FROM read_csv_auto('orders.csv') o
LEFT JOIN read_parquet('customers.parquet') c
  ON o.customer_id = c.customer_id
LEFT JOIN read_json_auto('products.json') p
  ON o.product_id = p.product_id;

-- 区域销售汇总
SELECT
  region,
  category,
  sum(revenue) AS total_revenue,
  count(*) AS order_count,
  avg(revenue) AS avg_order_value
FROM sales_summary
GROUP BY ROLLUP (region, category)
ORDER BY region, total_revenue DESC;

-- 导出结果
COPY (
  SELECT * FROM sales_summary
  ORDER BY region, order_date
) TO 'output/sales-summary/result.parquet' (FORMAT PARQUET);
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| CSV类型推断错误 | 混合类型列/日期格式多样 | 手动指定:`read_csv_auto('f.csv', types={'col': 'DATE'})` |
| 内存不足 | 数据量过大(>内存) | 设置`PRAGMA memory_limit='4GB'`,启用磁盘溢出 |
| 编码错误 | 非UTF-8编码(GBK/GB2312) | 指定编码:`read_csv_auto('f.csv', encoding='gbk')` |
| Parquet文件损坏 | 下载不完整/写入中断 | 重新下载/生成,使用`read_parquet`校验 |
| JOIN结果过大 | 笛卡尔积/缺少JOIN条件 | 检查JOIN条件,添加WHERE过滤,LIMIT预览 |
| 扩展安装失败 | 网络限制/权限不足 | 使用离线安装包,或`pip install duckdb`包含常用扩展 |
| 查询超时 | 复杂查询/无索引 | 添加过滤条件,创建物化视图,优化SQL(避免SELECT *) |
| 远程文件访问失败 | 网络限制/S3凭证缺失 | 下载至本地再查询,或配置S3凭证 |

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 电商销售数据多维度分析

**输入**:
```
文件: sales_2024.csv(电商订单数据，约500万行)
列: order_id, customer_id, product_id, category, quantity, unit_price, order_date, region, channel
任务: RFM用户分群+品类销售分析+渠道对比
```

**LLM生成输出**:
```sql
-- output/sales-analysis/query.sql

-- 1. 数据加载与概览
CREATE TABLE sales AS SELECT * FROM read_csv_auto('sales_2024.csv');
SUMMARIZE sales;

-- 2. RFM用户分群分析
WITH rfm AS (
  SELECT
    customer_id,
    -- Recency: 最近购买距今天数
    CURRENT_DATE - MAX(order_date::DATE) AS recency,
    -- Frequency: 购买次数
    COUNT(DISTINCT order_id) AS frequency,
    -- Monetary: 消费总金额
    SUM(quantity * unit_price) AS monetary
  FROM sales
  GROUP BY customer_id
),
rfm_score AS (
  SELECT
    customer_id,
    recency,
    frequency,
    monetary,
    -- RFM打分(5分制)
    NTILE(5) OVER (ORDER BY recency ASC) AS r_score,
    NTILE(5) OVER (ORDER BY frequency ASC) AS f_score,
    NTILE(5) OVER (ORDER BY monetary ASC) AS m_score
  FROM rfm
)
CREATE TABLE rfm_result AS
SELECT
  customer_id,
  recency,
  frequency,
  monetary,
  r_score,
  f_score,
  m_score,
  CASE
    WHEN r_score >= 4 AND f_score >= 4 AND m_score >= 4 THEN '重要价值客户'
    WHEN r_score >= 4 AND f_score <= 2 THEN '重要发展客户'
    WHEN r_score <= 2 AND f_score >= 4 AND m_score >= 4 THEN '重要保持客户'
    WHEN r_score <= 2 AND f_score <= 2 THEN '流失客户'
    ELSE '一般客户'
  END AS customer_segment
FROM rfm_score;

SELECT * FROM rfm_result ORDER BY monetary DESC;

-- 3. 品类销售分析(含环比)
WITH monthly_category AS (
  SELECT
    date_trunc('month', order_date::DATE) AS month,
    category,
    SUM(quantity * unit_price) AS revenue,
    COUNT(DISTINCT order_id) AS order_count
  FROM sales
  GROUP BY month, category
),
category_growth AS (
  SELECT
    month,
    category,
    revenue,
    order_count,
    LAG(revenue) OVER (PARTITION BY category ORDER BY month) AS prev_revenue,
    ROUND(
      (revenue - LAG(revenue) OVER (PARTITION BY category ORDER BY month)) 
      * 100.0 / LAG(revenue) OVER (PARTITION BY category ORDER BY month),
      2
    ) AS mom_growth_pct
  FROM monthly_category
)
SELECT * FROM category_growth
WHERE month >= '2024-06-01'
ORDER BY month, revenue DESC;

-- 4. 渠道对比分析
SELECT
  channel,
  COUNT(DISTINCT customer_id) AS unique_customers,
  COUNT(DISTINCT order_id) AS total_orders,
  SUM(quantity * unit_price) AS total_revenue,
  ROUND(AVG(quantity * unit_price), 2) AS avg_order_value,
  ROUND(SUM(quantity * unit_price) / COUNT(DISTINCT customer_id), 2) AS arpu
FROM sales
GROUP BY channel
ORDER BY total_revenue DESC;

-- 5. 导出RFM结果
COPY (
  SELECT * FROM rfm_result
  ORDER BY monetary DESC
) TO 'output/sales-analysis/rfm_result.parquet' (FORMAT PARQUET);
```

```csv
-- output/sales-analysis/channel_comparison.csv
channel,unique_customers,total_orders,total_revenue,avg_order_value,arpu
微信小程序,128534,456789,128560000,281.36,1000.16
APP,89234,312456,98760000,316.05,1106.65
官网,45678,156789,56780000,362.18,1243.53
抖音小店,34567,123456,34560000,279.88,999.80
```

**效果验证**: ✓500万行CSV秒级加载 ✓RFM分群含5分制评分+客户分层 ✓窗口函数计算环比增长(LAG) ✓4渠道对比含6项指标 ✓结果导出Parquet格式

### 案例2: 多文件联邦查询-订单客户产品关联

**输入**:
```
文件:
  - orders.csv(订单数据，CSV格式)
  - customers.parquet(客户信息，Parquet分块存储)
  - products.json(产品目录，JSON格式)
任务: 跨格式JOIN，生成区域-品类销售汇总报表
```

**LLM生成输出**:
```sql
-- output/sales-federation/query.sql

-- 1. 跨格式联邦查询(无需预先加载)
CREATE TABLE sales_detail AS
SELECT
  o.order_id,
  o.order_date,
  o.quantity,
  c.customer_name,
  c.region,
  c.customer_tier,
  p.product_name,
  p.category,
  p.unit_price,
  o.quantity * p.unit_price AS revenue
FROM read_csv_auto('orders.csv') o
LEFT JOIN read_parquet('customers/part-*.parquet') c
  ON o.customer_id = c.customer_id
LEFT JOIN read_json_auto('products.json') p
  ON o.product_id = p.product_id;

-- 2. 区域-品类销售汇总(含小计)
SELECT
  CASE WHEN grouping(region) = 1 THEN '总计' ELSE region END AS region,
  CASE WHEN grouping(category) = 1 THEN '小计' ELSE category END AS category,
  COUNT(DISTINCT order_id) AS order_count,
  COUNT(DISTINCT customer_name) AS unique_customers,
  SUM(revenue) AS total_revenue,
  ROUND(AVG(revenue), 2) AS avg_order_value,
  ROUND(SUM(revenue) * 100.0 / SUM(SUM(revenue)) OVER (), 2) AS revenue_share_pct
FROM sales_detail
GROUP BY ROLLUP (region, category)
ORDER BY region, total_revenue DESC;

-- 3. 高价值客户Top10(按区域)
WITH ranked_customers AS (
  SELECT
    region,
    customer_name,
    customer_tier,
    SUM(revenue) AS total_spending,
    COUNT(DISTINCT order_id) AS order_count,
    ROW_NUMBER() OVER (PARTITION BY region ORDER BY SUM(revenue) DESC) AS rank_in_region
  FROM sales_detail
  GROUP BY region, customer_name, customer_tier
)
SELECT * FROM ranked_customers
WHERE rank_in_region <= 10
ORDER BY region, rank_in_region;

-- 4. 品类同比增长(使用窗口函数)
WITH monthly_sales AS (
  SELECT
    date_trunc('month', order_date::DATE) AS month,
    category,
    SUM(revenue) AS monthly_revenue
  FROM sales_detail
  GROUP BY month, category
)
SELECT
  month,
  category,
  monthly_revenue,
  LAG(monthly_revenue, 12) OVER (PARTITION BY category ORDER BY month) AS prev_year_revenue,
  CASE
    WHEN LAG(monthly_revenue, 12) OVER (PARTITION BY category ORDER BY month) IS NOT NULL THEN
      ROUND(
        (monthly_revenue - LAG(monthly_revenue, 12) OVER (PARTITION BY category ORDER BY month))
        * 100.0 / LAG(monthly_revenue, 12) OVER (PARTITION BY category ORDER BY month),
        2
      )
    ELSE NULL
  END AS yoy_growth_pct
FROM monthly_sales
ORDER BY category, month;

-- 5. 导出汇总报表
COPY (
  SELECT
    region,
    category,
    order_count,
    total_revenue,
    avg_order_value,
    revenue_share_pct
  FROM (
    SELECT
      region,
      category,
      COUNT(DISTINCT order_id) AS order_count,
      SUM(revenue) AS total_revenue,
      ROUND(AVG(revenue), 2) AS avg_order_value,
      ROUND(SUM(revenue) * 100.0 / SUM(SUM(revenue)) OVER (), 2) AS revenue_share_pct
    FROM sales_detail
    GROUP BY region, category
  )
  ORDER BY region, total_revenue DESC
) TO 'output/sales-federation/region_category_report.csv' (HEADER, DELIMITER ',');
```

```csv
-- output/sales-federation/region_category_report.csv
region,category,order_count,total_revenue,avg_order_value,revenue_share_pct
华东,电子产品,45678,28560000,625.20,22.3
华东,服装,38456,12340000,320.88,9.6
华东,家居,28934,8760000,302.75,6.8
华北,电子产品,32456,19870000,612.20,15.5
华北,食品,21567,5430000,251.78,4.2
华南,电子产品,39876,24680000,618.85,19.3
华南,服装,31245,10560000,338.00,8.2
```

**效果验证**: ✓3种格式(CSV/Parquet/JSON)联邦JOIN ✓ROLLUP生成小计与总计 ✓窗口函数ROW_NUMBER按区域排名Top10 ✓LAG(12)计算同比增长 ✓结果含收入占比百分比

### 案例3: 日志分析-慢接口与错误率诊断

**输入**:
```
文件: app_logs.parquet(应用日志，Parquet格式，约2000万行，1.2GB)
列: timestamp, request_id, method, path, status_code, duration_ms, user_id, response_size
任务: 慢接口Top10+错误率分析+小时趋势+异常检测
```

**LLM生成输出**:
```sql
-- output/log-analysis/query.sql

-- 1. 数据加载与概览(Parquet直接查询，无需加载到内存)
SUMMARIZE read_parquet('app_logs.parquet');

-- 2. 慢接口Top10(P95延迟)
SELECT
  path,
  method,
  COUNT(*) AS request_count,
  ROUND(AVG(duration_ms), 2) AS avg_duration_ms,
  ROUND(percentile_cont(0.50) WITHIN GROUP (ORDER BY duration_ms), 2) AS p50_ms,
  ROUND(percentile_cont(0.95) WITHIN GROUP (ORDER BY duration_ms), 2) AS p95_ms,
  ROUND(percentile_cont(0.99) WITHIN GROUP (ORDER BY duration_ms), 2) AS p99_ms,
  MAX(duration_ms) AS max_duration_ms
FROM read_parquet('app_logs.parquet')
WHERE status_code < 400
GROUP BY path, method
ORDER BY p95_ms DESC
LIMIT 10;

-- 3. 错误率分析(按接口)
SELECT
  path,
  method,
  COUNT(*) AS total_requests,
  COUNT(CASE WHEN status_code >= 400 AND status_code < 500 THEN 1 END) AS client_errors,
  COUNT(CASE WHEN status_code >= 500 THEN 1 END) AS server_errors,
  ROUND(COUNT(CASE WHEN status_code >= 400 THEN 1 END) * 100.0 / COUNT(*), 2) AS error_rate_pct,
  -- 最常见错误码
  MODE() WITHIN GROUP (ORDER BY status_code) AS most_common_error
FROM read_parquet('app_logs.parquet')
GROUP BY path, method
HAVING COUNT(CASE WHEN status_code >= 400 THEN 1 END) > 0
ORDER BY error_rate_pct DESC
LIMIT 15;

-- 4. 小时趋势(异常检测)
WITH hourly_stats AS (
  SELECT
    date_trunc('hour', timestamp) AS hour,
    COUNT(*) AS request_count,
    ROUND(AVG(duration_ms), 2) AS avg_duration_ms,
    COUNT(CASE WHEN status_code >= 500 THEN 1 END) AS server_errors
  FROM read_parquet('app_logs.parquet')
  GROUP BY hour
),
stats_baseline AS (
  SELECT
    AVG(request_count) AS avg_requests,
    STDDEV(request_count) AS stddev_requests,
    AVG(avg_duration_ms) AS avg_duration,
    STDDEV(avg_duration_ms) AS stddev_duration
  FROM hourly_stats
)
SELECT
  h.hour,
  h.request_count,
  h.avg_duration_ms,
  h.server_errors,
  CASE
    WHEN h.avg_duration_ms > s.avg_duration + 3 * s.stddev_duration THEN '延迟异常'
    WHEN h.server_errors > 10 THEN '错误激增'
    WHEN h.request_count > s.avg_requests + 3 * s.stddev_requests THEN '流量激增'
    ELSE '正常'
  END AS anomaly_flag
FROM hourly_stats h
CROSS JOIN stats_baseline s
WHERE h.avg_duration_ms > s.avg_duration + 2 * s.stddev_duration
   OR h.server_errors > 10
ORDER BY h.hour DESC;

-- 5. 响应体大小分析
SELECT
  path,
  ROUND(AVG(response_size) / 1024.0, 2) AS avg_size_kb,
  ROUND(MAX(response_size) / 1024.0, 2) AS max_size_kb,
  ROUND(percentile_cont(0.95) WITHIN GROUP (ORDER BY response_size) / 1024.0, 2) AS p95_size_kb,
  COUNT(CASE WHEN response_size > 1048576 THEN 1 END) AS oversized_count
FROM read_parquet('app_logs.parquet')
GROUP BY path
HAVING COUNT(CASE WHEN response_size > 1048576 THEN 1 END) > 0
ORDER BY avg_size_kb DESC;

-- 6. 导出异常时段报告
COPY (
  SELECT * FROM (
    SELECT
      date_trunc('hour', timestamp) AS hour,
      COUNT(*) AS request_count,
      ROUND(AVG(duration_ms), 2) AS avg_duration_ms,
      COUNT(CASE WHEN status_code >= 500 THEN 1 END) AS server_errors,
      CASE
        WHEN AVG(duration_ms) > (SELECT AVG(duration_ms) + 3 * STDDEV(duration_ms) FROM read_parquet('app_logs.parquet')) THEN '延迟异常'
        WHEN COUNT(CASE WHEN status_code >= 500 THEN 1 END) > 10 THEN '错误激增'
        ELSE '正常'
      END AS anomaly_flag
    FROM read_parquet('app_logs.parquet')
    GROUP BY hour
  )
  WHERE anomaly_flag != '正常'
  ORDER BY hour DESC
) TO 'output/log-analysis/anomaly_report.csv' (HEADER, DELIMITER ',');
```

```csv
-- output/log-analysis/slow_endpoints.csv
path,method,request_count,avg_duration_ms,p50_ms,p95_ms,p99_ms,max_duration_ms
/api/checkout,POST,152340,485.32,180,1250,3200,8900
/api/search,GET,892345,125.67,45,380,1200,4500
/api/upload,POST,23456,890.45,120,2400,6800,15000
/api/product/detail,GET,456789,78.23,35,180,450,2100
/api/order/create,POST,234567,320.89,150,850,1800,5600
```

**效果验证**: ✓1.2GB Parquet直接查询无需加载内存 ✓P50/P95/P99分位数计算 ✓3σ异常检测(延迟/错误/流量) ✓错误率按4xx/5xx分类 ✓导出异常时段报告

### 案例4: Pandas互操作-大数据集高效处理

**输入**:
```
场景: 已有Pandas DataFrame(销售数据，约800万行，内存约1.5GB)
任务: 需执行复杂SQL聚合(窗口函数+CTE)，Pandas实现繁琐
目标: 使用DuckDB零拷贝加速，结果返回Pandas
```

**LLM生成输出**:
```python
# output/pandas-integration/duckdb_pandas.py
import duckdb
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. 生成示例数据(模拟800万行销售数据)
np.random.seed(42)
n = 8_000_000
df = pd.DataFrame({
    'order_id': range(1, n + 1),
    'customer_id': np.random.randint(1, 100000, n),
    'product_id': np.random.randint(1, 5000, n),
    'category': np.random.choice(['电子产品', '服装', '家居', '食品', '图书'], n),
    'quantity': np.random.randint(1, 10, n),
    'unit_price': np.round(np.random.exponential(200, n) + 10, 2),
    'order_date': pd.date_range('2023-01-01', periods=n, freq='30s'),
    'region': np.random.choice(['华东', '华北', '华南', '西南', '东北'], n),
})

print(f"DataFrame行数: {len(df):,}")
print(f"内存占用: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

# 2. DuckDB零拷贝注册DataFrame
con = duckdb.connect()
con.register('sales_df', df)  # 零拷贝，不复制数据

# 3. 复杂SQL查询(窗口函数+CTE，Pandas写很繁琐)
result = con.execute("""
WITH customer_stats AS (
    SELECT
        customer_id,
        region,
        COUNT(*) AS order_count,
        SUM(quantity * unit_price) AS total_spending,
        MAX(order_date) AS last_order_date,
        MIN(order_date) AS first_order_date
    FROM sales_df
    GROUP BY customer_id, region
),
ranked AS (
    SELECT
        customer_id,
        region,
        order_count,
        total_spending,
        last_order_date,
        first_order_date,
        -- 区域内消费排名
        RANK() OVER (PARTITION BY region ORDER BY total_spending DESC) AS rank_in_region,
        -- 消费分位数
        NTILE(10) OVER (PARTITION BY region ORDER BY total_spending ASC) AS spending_decile,
        -- 复购率指标
        CASE 
            WHEN COUNT(*) > 5 THEN '高频客户'
            WHEN COUNT(*) > 2 THEN '中频客户'
            ELSE '低频客户'
        END AS frequency_tier
    FROM customer_stats
    GROUP BY customer_id, region, order_count, total_spending, 
             last_order_date, first_order_date
)
SELECT
    region,
    frequency_tier,
    COUNT(DISTINCT customer_id) AS customer_count,
    ROUND(AVG(total_spending), 2) AS avg_spending,
    ROUND(SUM(total_spending), 2) AS total_spending,
    ROUND(AVG(order_count), 1) AS avg_order_count
FROM ranked
WHERE rank_in_region <= 100  -- 每区域Top100客户
GROUP BY region, frequency_tier
ORDER BY region, total_spending DESC
""").df()  # 结果转回Pandas DataFrame

print("\n区域Top100客户分析:")
print(result.to_string(index=False))

# 4. 对比: DuckDB vs Pandas执行时间
import time

# DuckDB执行
start = time.time()
duckdb_result = con.execute("""
    SELECT category, region, 
           SUM(quantity * unit_price) AS revenue,
           AVG(quantity * unit_price) AS avg_order
    FROM sales_df
    GROUP BY category, region
    ORDER BY revenue DESC
""").df()
duckdb_time = time.time() - start
print(f"\nDuckDB聚合耗时: {duckdb_time:.3f}秒")

# Pandas执行同样聚合
start = time.time()
df['revenue'] = df['quantity'] * df['unit_price']
pandas_result = df.groupby(['category', 'region'])['revenue'].agg(['sum', 'mean']).reset_index()
pandas_time = time.time() - start
print(f"Pandas聚合耗时: {pandas_time:.3f}秒")
print(f"DuckDB加速比: {pandas_time / duckdb_time:.1f}x")

# 5. 导出结果
result.to_csv('output/pandas-integration/customer_analysis.csv', index=False)
print(f"\n结果已导出: {len(result)}行")
```

```
# 执行输出
DataFrame行数: 8,000,000
内存占用: 856.3 MB

区域Top100客户分析:
region frequency_tier  customer_count  avg_spending  total_spending  avg_order_count
华东    高频客户              85     45678.32      3882657.20             7.2
华东    中频客户              15     28543.67       428155.05             3.8
华北    高频客户              82     44987.15      3688946.30             7.1
华南    高频客户              88     46234.89      4068669.72             7.3
...

DuckDB聚合耗时: 0.234秒
Pandas聚合耗时: 1.876秒
DuckDB加速比: 8.0x

结果已导出: 15行
```

**效果验证**: ✓800万行零拷贝注册(无内存复制) ✓窗口函数RANK+NTILE(分位数) ✓DuckDB比Pandas快8倍 ✓结果自动转回DataFrame ✓复购率分层(高/中/低频)

### 案例5: 时序数据降采样与物化视图

**输入**:
```
文件: iot_sensors.parquet(IoT传感器数据，秒级采集，约5亿行，15GB)
列: sensor_id, timestamp, temperature, humidity, pressure, battery_level
任务: 秒级数据降采样为小时级+创建物化视图+异常检测
```

**LLM生成输出**:
```sql
-- output/iot-downsampling/query.sql

-- 1. 设置内存限制(15GB数据，限制4GB内存，启用磁盘溢出)
PRAGMA memory_limit='4GB';
PRAGMA threads=8;

-- 2. 原始数据概览
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT sensor_id) AS sensor_count,
  MIN(timestamp) AS min_time,
  MAX(timestamp) AS max_time,
  ROUND(COUNT(*) * 1.0 / 
    (EXTRACT(EPOCH FROM (MAX(timestamp) - MIN(timestamp))) / 3600), 0) AS rows_per_hour
FROM read_parquet('iot_sensors.parquet');

-- 3. 降采样: 秒级→小时级(物化视图)
CREATE TABLE sensor_hourly AS
SELECT
  sensor_id,
  date_trunc('hour', timestamp) AS hour,
  ROUND(AVG(temperature), 2) AS avg_temp,
  ROUND(MIN(temperature), 2) AS min_temp,
  ROUND(MAX(temperature), 2) AS max_temp,
  ROUND(percentile_cont(0.95) WITHIN GROUP (ORDER BY temperature), 2) AS p95_temp,
  ROUND(AVG(humidity), 2) AS avg_humidity,
  ROUND(AVG(pressure), 2) AS avg_pressure,
  ROUND(AVG(battery_level), 2) AS avg_battery,
  COUNT(*) AS sample_count,
  COUNT(CASE WHEN temperature > 80 OR temperature < -20 THEN 1 END) AS anomaly_count
FROM read_parquet('iot_sensors.parquet')
GROUP BY sensor_id, date_trunc('hour', timestamp);

-- 验证降采样效果
SELECT 
  (SELECT COUNT(*) FROM read_parquet('iot_sensors.parquet')) AS original_rows,
  (SELECT COUNT(*) FROM sensor_hourly) AS downsampled_rows,
  ROUND(
    (SELECT COUNT(*) FROM sensor_hourly) * 100.0 / 
    (SELECT COUNT(*) FROM read_parquet('iot_sensors.parquet')), 4
  ) AS compression_ratio_pct;

-- 4. 异常检测(基于3σ规则)
CREATE TABLE temp_stats AS
  SELECT
    sensor_id,
    AVG(avg_temp) AS mean_temp,
    STDDEV(avg_temp) AS std_temp
  FROM sensor_hourly
  GROUP BY sensor_id;

SELECT
  h.sensor_id,
  h.hour,
  h.avg_temp,
  h.max_temp,
  h.anomaly_count,
  s.mean_temp,
  ROUND(s.std_temp, 2) AS std_temp,
  CASE
    WHEN h.avg_temp > s.mean_temp + 3 * s.std_temp THEN '高温异常'
    WHEN h.avg_temp < s.mean_temp - 3 * s.std_temp THEN '低温异常'
    WHEN h.anomaly_count > 100 THEN '高频异常'
    ELSE '正常'
  END AS anomaly_type
FROM sensor_hourly h
JOIN temp_stats s ON h.sensor_id = s.sensor_id
WHERE h.avg_temp > s.mean_temp + 3 * s.std_temp
   OR h.avg_temp < s.mean_temp - 3 * s.std_temp
   OR h.anomaly_count > 100
ORDER BY h.hour DESC, h.sensor_id
LIMIT 100;

-- 5. 传感器电池电量趋势(预警低电量)
WITH battery_trend AS (
  SELECT
    sensor_id,
    hour,
    avg_battery,
    LAG(avg_battery, 24) OVER (PARTITION BY sensor_id ORDER BY hour) AS battery_24h_ago,
    AVG(avg_battery) OVER (
      PARTITION BY sensor_id 
      ORDER BY hour 
      ROWS BETWEEN 23 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_24h
  FROM sensor_hourly
)
SELECT
  sensor_id,
  hour,
  avg_battery,
  rolling_avg_24h,
  ROUND(avg_battery - rolling_avg_24h, 2) AS battery_drop_24h,
  CASE
    WHEN avg_battery < 20 THEN '紧急更换'
    WHEN avg_battery < 40 THEN '预警'
    WHEN avg_battery - rolling_avg_24h < -5 THEN '快速下降'
    ELSE '正常'
  END AS battery_status
FROM battery_trend
WHERE avg_battery < 40
   OR (avg_battery - rolling_avg_24h) < -5
ORDER BY avg_battery ASC
LIMIT 50;

-- 6. 导出降采样数据与异常报告
COPY (SELECT * FROM sensor_hourly ORDER BY sensor_id, hour) 
  TO 'output/iot-downsampling/sensor_hourly.parquet' (FORMAT PARQUET);

COPY (
  SELECT * FROM (
    SELECT
      h.sensor_id, h.hour, h.avg_temp, h.max_temp, h.anomaly_count,
      CASE
        WHEN h.avg_temp > s.mean_temp + 3 * s.std_temp THEN '高温异常'
        WHEN h.avg_temp < s.mean_temp - 3 * s.std_temp THEN '低温异常'
        WHEN h.anomaly_count > 100 THEN '高频异常'
      END AS anomaly_type
    FROM sensor_hourly h
    JOIN temp_stats s ON h.sensor_id = s.sensor_id
    WHERE h.avg_temp > s.mean_temp + 3 * s.std_temp
       OR h.avg_temp < s.mean_temp - 3 * s.std_temp
       OR h.anomaly_count > 100
  )
  ORDER BY hour DESC
) TO 'output/iot-downsampling/anomaly_report.csv' (HEADER, DELIMITER ',');
```

```csv
-- output/iot-downsampling/downsampling_stats.csv
metric,value
original_rows,500000000
downsampled_rows,876000
compression_ratio_pct,0.1752
original_size_gb,15.0
downsampled_size_mb,45.2
query_time_seconds,12.3
```

**效果验证**: ✓5亿行15GB数据在4GB内存下完成(磁盘溢出) ✓降采样压缩比99.8%(5亿→87.6万行) ✓3σ异常检测(高温/低温/高频) ✓电池预警含24小时滑动平均 ✓窗口函数LAG(24)计算趋势变化

## 常见问题

### Q1: DuckDB和SQLite有什么区别?什么时候用DuckDB?
A: (1)定位:SQLite是OLTP(事务处理),DuckDB是OLAP(分析处理)。(2)存储:SQLite行式存储,DuckDB列式存储。(3)查询:SQLite适合单行读写,DuckDB适合聚合分析(快10-100倍)。(4)并发:SQLite支持并发读写,DuckDB侧重读多写少。(5)数据量:SQLite适合<1GB,DuckDB适合GB级。建议:事务系统用SQLite/PostgreSQL,数据分析用DuckDB。

### Q2: DuckDB能处理多大的数据?
A: (1)内存模式:适合<内存大小的数据(如8GB内存可处理8GB CSV)。(2)磁盘溢出:启用`PRAGMA memory_limit`,超内存部分写磁盘,可处理10-100GB数据(性能下降30-50%)。(3)Parquet分块:将大文件转为Parquet分块,DuckDB可流式处理,理论上无上限(受磁盘空间限制)。(4)建议:>100GB数据考虑分批处理或使用Spark/Dask。

### Q3: 如何在Pandas和DuckDB之间选择?
A: 选DuckDB的场景:(1)数据量>1GB(Pandas加载慢/内存不足)(2)复杂SQL查询(窗口函数/CTE/Pandas写起来繁琐)(3)多文件关联(Pandas merge内存爆炸)(4)持久化存储(需要CREATE TABLE)。选Pandas的场景:(1)数据量<500MB(2)需要丰富的数据清洗API(3)与Scikit-learn/Matplotlib深度集成(4)交互式探索。最佳实践:用DuckDB查询+聚合,结果转Pandas可视化。

### Q4: DuckDB支持哪些SQL扩展?
A: (1)窗口函数:ROW_NUMBER/RANK/LAG/LEAD/PERCENTILE(2)CTE与递归:WITH/WITH RECURSIVE(3)PIVOT/UNPIVOT:行列转换(4)JSON函数:提取与查询JSON(5)文本函数:正则/模糊匹配(6)空间扩展:GIS数据处理(7)HTTP扩展:调用REST API(8)PostgreSQL/MySQL附加:跨数据库查询。完整列表见DuckDB官方文档。

## 已知限制

- 不支持高并发写入(OLTP场景),适合读多写少分析场景
- 单机处理,不支持分布式(>100GB数据建议Spark/Dask)
- 无持久化服务进程(嵌入式),每次启动需重新加载(除非保存为.duckdb文件)
- 扩展需联网安装(spatial/http等),离线环境需预装
- 不支持触发器/存储过程(与PostgreSQL/MySQL相比)
- 全文搜索能力有限(无倒排索引,不如Elasticsearch)

## 安全与合规

- 本Skill不存储任何API Key,DuckDB为本地嵌入式数据库
- 不上传数据至外部服务,所有查询在本地执行
- S3/远程文件访问凭证由用户自行配置,不进入Skill上下文
- SQL查询脚本由Agent临时生成执行,不持久化到Skill目录
- 数据文件路径由用户提供,本Skill不主动扫描文件系统
- 敏感数据(PII/财务)建议脱敏后再分析
- 查询结果存储在本地output目录,建议定期清理
- DuckDB数据库文件(.duckdb)可加密,敏感数据建议加密存储
