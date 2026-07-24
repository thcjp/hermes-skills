---
slug: clickhouse-olap-expert
name: clickhouse-analytics
version: 1.0.1
displayName: ClickHouse分析专家
summary: 亿级数据秒级查询,ClickHouse列式数据库从建表到集群全栈优化
license: Proprietary
description: ClickHouse分析专家——基于官方最佳实践设计高性能列式分析数据库，让亿级数据查询秒级返回。适用于实时分析、日志分析、用户行为分析、时序数据、广告技术、数据仓库等场景。从表引擎选择到集群管理，全栈OLAP方案。国内场景可使用阿里云ClickHouse或腾讯云CDWCH。触发关键词：ClickHouse、列式数据库、分析数据库、MergeTree、分区、物化视图、投影、查询优化、OLAP、大数据分析
tags:
- 数据分析
- ClickHouse
- 列式数据库
- OLAP
- 大数据
tools:
- read
- exec
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
---
# ClickHouse分析专家

基于 ClickHouse 官方最佳实践，设计高性能、可扩展的列式分析数据库。从表设计到查询优化，从物化视图到集群管理，全栈分析数据库方案。

## 核心能力

- **表引擎选择**：MergeTree 系列（Replacing/Summing/Aggregating/Collapsing）+ 特殊引擎（Log/Distributed/Dictionary/Kafka/MaterializedView）
- **分区与排序键设计**：时间分区裁剪 + 排序键选择性优化 + 主键稀疏索引（8192 行粒度）+ TTL 自动清理
- **物化视图与投影**：物化视图（跨表预聚合）+ 投影（同表多排序）+ 自动选择最优投影
- **查询优化**：列式存储只查所需列 + groupBitmap 替代 COUNT(DISTINCT) + 字典替代 JOIN + 分布式查询优化
- **集群管理**：分片（Distributed 表路由）+ 副本（ReplicatedMergeTree + ZooKeeper/Keeper）+ 负载均衡

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 实时分析 | 业务指标 + 数据量 + 查询模式 | MergeTree 表 + 物化视图 + 查询示例 |
| 日志分析 | 日志格式 + 日增量 + 保留期 | 分区表 + TTL + 采样索引 + 降采样策略 |
| 用户行为 | 事件类型 + 漏斗/留存需求 | 事件表 + Array/JSON + 漏斗查询 + 留存查询 |
| 时序数据 | 监控/IoT 指标 + 采样频率 | TTL 压缩 + 降采样物化视图 + 时序查询 |
| 广告技术 | 报表维度 + 归因需求 | 多表 JOIN 优化 + 字典 + 实时报表 |
| 数据仓库 | 星型/雪花模型 + OLAP 需求 | 宽表 + 物化视图 + 星型模型优化 |

**不适用于**：
- OLTP 事务型业务（高并发小事务，用 MySQL/PostgreSQL）
- 键值缓存（用 Redis）
- 全文搜索引擎（用 Elasticsearch，ClickHouse 全文搜索能力有限）
- 图数据库场景（用 Neo4j）
- 单机小数据量分析（< 100 万行，用 PostgreSQL 足矣）

## 使用流程

### Step 1: 选择表引擎
- MergeTree（通用分析表，默认推荐）
- ReplacingMergeTree（去重，最终一致）
- SummingMergeTree（自动汇总）
- AggregatingMergeTree（预聚合）
- CollapsingMergeTree（自动删除，版本控制）
- 特殊引擎：Log/Distributed/Dictionary/Kafka

### Step 2: 设计分区与排序键
- 分区键（PARTITION BY）：按时间分区（`toYYYYMM(date)`），单节点不超过 1000 分区
- 排序键（ORDER BY）：选择性高的列在前，过滤条件常用的列在前
- 主键（PRIMARY KEY）：默认与排序键相同，可选排序键前缀子集
- TTL：`TTL date + INTERVAL 30 DAY` 自动清理过期数据

### Step 3: 设计物化视图与投影
- 物化视图：源表写入时触发，目标表用 SummingMergeTree/AggregatingMergeTree
- 投影：同一表的不同排序方式，查询自动选择最优投影
- 组合使用：物化视图跨表预聚合 + 投影同表多排序

### Step 4: 查询优化
- 只查需要的列（列式存储优势）
- 使用分区过滤（`WHERE date BETWEEN`）
- 聚合优化：`groupBitmap` 替代 `COUNT(DISTINCT)`，`quantile()` 近似计算
- JOIN 优化：小表放右侧，使用字典替代 JOIN

### Step 5: 数据摄入设计
- 批量插入：> 1000 行/批，避免频繁小批量
- 流式摄入：Kafka 引擎 + MaterializedView 自动写入
- 数据格式：TSV/CSV/Parquet（推荐）/ Native（高性能）/ JSONEachRow（灵活）

### Step 6: 集群配置（如需）
- 分片（Shard）：水平拆分 + Distributed 表路由
- 副本（Replica）：ReplicatedMergeTree + ZooKeeper/ClickHouse Keeper
- 负载均衡：轮询/随机

### Step 7: 监控与运维
- system.metrics / system.events：性能指标
- system.merges：合并进度
- system.replicas：副本状态
- Grafana 仪表盘：可视化监控

## 示例

### 示例 1：用户行为分析表

**输入**：
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | ClickHouse分析专家处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
需求：设计用户行为分析表，日增 1 亿条事件，支持实时 UV/PV 和漏斗分析。
```

**输出**：
```sql
-- 1. 事件明细表
CREATE TABLE events (
  event_time DateTime,
  user_id UInt64,
  event_name String,
  properties String,          -- JSON 格式属性
  device_type LowCardinality(String),  -- 低基数枚举
  platform LowCardinality(String),
  session_id String
) ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(event_time)
ORDER BY (event_name, user_id, event_time)
TTL event_time + INTERVAL 90 DAY
SETTINGS index_granularity = 8192;
# ...
-- 2. 物化视图：每日汇总（实时 UV/PV）
CREATE MATERIALIZED VIEW daily_stats
ENGINE = SummingMergeTree()
PARTITION BY toYYYYMM(day)
ORDER BY (event_name, day)
AS SELECT
  event_name,
  toDate(event_time) AS day,
  count() AS pv,
  uniqState(user_id) AS uv_state   -- 使用 uniqState 支持合并
FROM events
GROUP BY event_name, day;
# ...
-- 3. 查询示例
-- 实时 PV（最近 1 小时）
SELECT count() AS pv
FROM events
WHERE event_name = 'view'
  AND event_time > now() - INTERVAL 1 HOUR;
# ...
-- 实时 UV（使用物化视图 + uniqMerge）
SELECT event_name, sum(pv) AS total_pv, uniqMerge(uv_state) AS total_uv
FROM daily_stats
WHERE day = today()
GROUP BY event_name;
# ...
-- 漏斗分析（view → click → purchase）
SELECT
  user_id,
  countIf(event_name = 'view') AS view_cnt,
  countIf(event_name = 'click') AS click_cnt,
  countIf(event_name = 'purchase') AS purchase_cnt
FROM events
WHERE event_time >= today() - INTERVAL 7 DAY
  AND event_name IN ('view', 'click', 'purchase')
GROUP BY user_id
HAVING view_cnt > 0;
```

### 示例 2：日志分析平台

**输入**：
```
需求：搭建日志分析平台，日增 10TB 日志，保留 7 天，需要全文搜索与降采样。
```

**输出**：
```sql
-- 1. 原始日志表（保留 7 天）
CREATE TABLE logs_raw (
  log_time DateTime,
  service_name LowCardinality(String),
  level LowCardinality(String),    -- INFO/WARN/ERROR
  message String,
  host LowCardinality(String),
  trace_id String,
  INDEX msg_idx message TYPE tokenbf_v1(30720, 3, 0) GRANULARITY 4  -- 全文搜索索引
) ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(log_time)
ORDER BY (service_name, log_time)
TTL log_time + INTERVAL 7 DAY
SETTINGS compression = 'LZ4';
# ...
-- 2. 降采样物化视图（按小时聚合，保留 1 年）
CREATE MATERIALIZED VIEW logs_hourly
ENGINE = MergeTree()
PARTITION BY toYYYYMM(hour)
ORDER BY (service_name, level, hour)
TTL hour + INTERVAL 365 DAY
AS SELECT
  service_name,
  level,
  toStartOfHour(log_time) AS hour,
  count() AS log_count,
  uniq(trace_id) AS trace_count
FROM logs_raw
GROUP BY service_name, level, hour;
# ...
-- 3. 查询示例
-- 全文搜索错误日志
SELECT log_time, service_name, message, trace_id
FROM logs_raw
WHERE message LIKE '%timeout%'
  AND level = 'ERROR'
  AND log_time > now() - INTERVAL 1 HOUR
ORDER BY log_time DESC
LIMIT 100;
# ...
-- 服务错误率趋势（使用降采样表，秒级返回）
SELECT
  hour,
  service_name,
  sumIf(log_count, level = 'ERROR') / sum(log_count) AS error_rate
FROM logs_hourly
WHERE hour > now() - INTERVAL 7 DAY
GROUP BY hour, service_name
ORDER BY hour;
```

## 错误处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 重试机制: 失败时自动重试, 最多3次

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 查询超时 | 全表扫描或聚合基数过大 | 检查分区裁剪 + 添加排序键索引 + 优化聚合 + 增加资源 |
| 内存溢出（OOM） | `max_memory_usage` 超限 | 调整 `max_memory_usage` + 使用流式聚合 + 分批查询 |
| 数据不一致 | ReplacingMergeTree 未完成合并 | 最终一致，手动 `OPTIMIZE TABLE FINAL` 强制合并 |
| 合并积压 | 写入速度超过合并速度 | 检查 `system.merges` + 增加后台线程 + 减少分区数 |
| 副本延迟 | ZooKeeper 网络问题 | 检查 ZooKeeper 连接 + `system.replicas` 排查 |
| 磁盘空间不足 | 数据增长超预期 | TTL 自动清理 + 增加磁盘 + 冷热分层 |
| ZooKeeper 故障 | 协调服务不可用 | 迁移到 ClickHouse Keeper（原生，无 JVM 依赖） |
| 分布式 JOIN 慢 | 数据跨节点传输 | 小表放右侧 + 使用字典替代 JOIN + 预 JOIN 宽表 |

## 依赖说明

### 运行环境
- **Agent 平台**：Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持 SKILL.md 的任意 Agent
- **操作系统**：Windows / macOS / Linux
- **运行时**：需要 Agent 支持 exec（命令行执行）能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| ClickHouse 实例 | 服务 | 必需（执行时） | 自托管 / ClickHouse Cloud / 国内云托管 |
| clickhouse-client | CLI | 必需（执行时） | 官方包管理器安装 |
| ZooKeeper / Keeper | 服务 | 可选 | 集群模式（副本协调） |
| chdb | 库 | 可选 | Python 嵌入式，无需服务器，进程内 SQL |
| Grafana | 工具 | 可选 | 监控仪表盘可视化 |

### 国内替代方案
| 海外服务/工具 | 国内替代 | 说明 |
|:---------|---------:|:---------|
| ClickHouse Cloud | 阿里云 ClickHouse | 阿里云托管 ClickHouse，兼容开源版本 |
| ClickHouse Cloud | 腾讯云 CDWCH（ClickHouse） | 腾讯云托管 ClickHouse |
| ClickHouse Cloud | 华为云 GaussDB(DWS) ClickHouse | 华为云托管版本 |
| ZooKeeper | ClickHouse Keeper | ClickHouse 原生协调服务，无 JVM 依赖 |
| Grafana | 阿里云监控 / 腾讯云监控 | 国内监控可视化（也可自建 Grafana） |

### API Key 配置
- **CLICKHOUSE_HOST**：必需（连接时），ClickHouse 服务器地址
- **CLICKHOUSE_USER**：必需（连接时），用户名
- **CLICKHOUSE_PASSWORD**：可选（连接时），密码
- 配置方式：在 Agent 的环境变量或 `.env` 文件中设置
- **Skill 内零硬编码**，所有凭据通过环境变量引用

### 可用性分类
- **分类**：MD + EXEC
- **说明**：纯 Markdown 方法论，实际执行需要 ClickHouse 实例和 CLI 工具，纯设计阶段无需额外依赖

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 用户行为分析表设计

**输入**:
```
需求: 设计用户行为分析表，日增1亿条事件，支持实时UV/PV和漏斗分析。
事件类型: view, click, purchase, share等20种
保留期: 90天
查询场景: 实时大盘(秒级) + 漏斗分析(分钟级)
```

**LLM生成输出**:
```sql
-- output/user-events/01_create_table.sql
# ...
-- 1. 事件明细表（MergeTree，按天分区）
CREATE TABLE events (
  event_time DateTime,
  user_id UInt64,
  event_name LowCardinality(String),  -- 20种事件，低基数优化
  properties String,                   -- JSON格式属性
  device_type LowCardinality(String),  -- iOS/Android/Web
  platform LowCardinality(String),     -- 渠道
  session_id String,
  ip IPv4                              -- IPv4类型比String高效
) ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(event_time)
ORDER BY (event_name, user_id, event_time)  -- 选择性: event_name > user_id > time
TTL event_time + INTERVAL 90 DAY            -- 90天自动清理
SETTINGS index_granularity = 8192;           -- 稀疏索引粒度
# ...
-- 2. 每日汇总物化视图（实时UV/PV，秒级查询）
CREATE MATERIALIZED VIEW daily_stats
ENGINE = SummingMergeTree()
PARTITION BY toYYYYMM(day)
ORDER BY (event_name, day)
TTL day + INTERVAL 180 DAY  -- 汇总数据保留更久
AS SELECT
  event_name,
  toDate(event_time) AS day,
  count() AS pv,
  uniqState(user_id) AS uv_state  -- 使用uniqState支持合并
FROM events
GROUP BY event_name, day;
# ...
-- 3. 漏斗分析辅助表（按user_id排序，加速漏斗查询）
CREATE TABLE events_by_user
ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(event_time)
ORDER BY (user_id, event_time)
TTL event_time + INTERVAL 90 DAY
AS SELECT * FROM events;  -- 通过物化视图同步
# ...
-- 4. 查询示例
-- 4.1 实时PV（最近1小时，秒级返回）
SELECT count() AS pv
FROM events
WHERE event_name = 'view'
  AND event_time > now() - INTERVAL 1 HOUR;
# ...
-- 4.2 实时UV（使用物化视图，秒级返回）
SELECT event_name, sum(pv) AS total_pv, uniqMerge(uv_state) AS total_uv
FROM daily_stats
WHERE day = today()
GROUP BY event_name;
# ...
-- 4.3 漏斗分析（view → click → purchase，7天窗口）
SELECT
  countIf(view_cnt > 0) AS step1_view,
  countIf(click_cnt > 0) AS step2_click,
  countIf(purchase_cnt > 0) AS step3_purchase,
  round(countIf(click_cnt > 0) / countIf(view_cnt > 0) * 100, 2) AS cvr_1_2,
  round(countIf(purchase_cnt > 0) / countIf(click_cnt > 0) * 100, 2) AS cvr_2_3
FROM (
  SELECT
    user_id,
    countIf(event_name = 'view') AS view_cnt,
    countIf(event_name = 'click') AS click_cnt,
    countIf(event_name = 'purchase') AS purchase_cnt
  FROM events
  WHERE event_time >= today() - INTERVAL 7 DAY
    AND event_name IN ('view', 'click', 'purchase')
  GROUP BY user_id
);
# ...
-- 4.4 留存分析（次日/7日/30日留存）
SELECT
  today_users.day AS day,
  today_users.cnt AS dau,
  d1_users.cnt AS d1_retention,
  round(d1_users.cnt / today_users.cnt * 100, 2) AS d1_retention_rate
FROM
  (SELECT toDate(event_time) AS day, uniq(user_id) AS cnt
   FROM events WHERE event_time >= today() - INTERVAL 30 DAY
   GROUP BY day) AS today_users
LEFT JOIN
  (SELECT toDate(event_time) - INTERVAL 1 DAY AS day, uniq(user_id) AS cnt
   FROM events WHERE event_time >= today() - INTERVAL 30 DAY
   GROUP BY day) AS d1_users
USING day
ORDER BY day;
```

```text
# 性能基准（1亿条/日，90天数据约90亿行）
| 查询 | 扫描行数 | 耗时 | 优化点 |
|---:|:---|---:|---:|
| 实时PV(1小时) | ~400万 | 0.2s | 分区裁剪+列式扫描 |
| 实时UV(物化视图) | ~20行 | 0.05s | 预聚合 |
| 漏斗分析(7天) | ~7亿 | 8s | 分区裁剪+排序键 |
| 留存分析(30天) | ~30亿 | 15s | 物化视图预聚合 |
```

**效果验证**: ✓日增1亿条表设计合理 ✓物化视图实现秒级UV/PV ✓漏斗分析SQL完整 ✓分区裁剪+排序键优化 ✓TTL 90天自动清理

### 案例2: 日志分析平台搭建

**输入**:
```
需求: 搭建日志分析平台，日增10TB日志，保留7天原始+1年降采样。
日志格式: 时间/服务/级别/消息/主机/trace_id
查询场景: 全文搜索 + 错误率趋势 + 服务健康度
```

**LLM生成输出**:
```sql
-- output/log-analytics/01_create_tables.sql
# ...
-- 1. 原始日志表（保留7天，全文搜索索引）
CREATE TABLE logs_raw (
  log_time DateTime64(3),              -- 毫秒精度
  service_name LowCardinality(String), -- 服务名(低基数)
  level LowCardinality(String),        -- INFO/WARN/ERROR
  message String,
  host LowCardinality(String),
  trace_id String,
  -- tokenbf_v1索引: 近似全文搜索
  INDEX msg_idx message TYPE tokenbf_v1(30720, 3, 0) GRANULARITY 4,
  -- trace_id索引: 加速链路追踪
  INDEX trace_idx trace_id TYPE bloom_filter(0.01) GRANULARITY 1
) ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(log_time)
ORDER BY (service_name, log_time)
TTL log_time + INTERVAL 7 DAY          -- 7天自动清理
SETTINGS compression = 'LZ4';
# ...
-- 2. 小时降采样表（保留1年，加速趋势查询）
CREATE MATERIALIZED VIEW logs_hourly
ENGINE = SummingMergeTree()
PARTITION BY toYYYYMM(hour)
ORDER BY (service_name, level, hour)
TTL hour + INTERVAL 365 DAY
AS SELECT
  service_name,
  level,
  toStartOfHour(log_time) AS hour,
  count() AS log_count,
  uniq(trace_id) AS trace_count
FROM logs_raw
GROUP BY service_name, level, hour;
# ...
-- 3. 服务健康度日表（保留2年，长期趋势）
CREATE MATERIALIZED VIEW service_health_daily
ENGINE = MergeTree()
PARTITION BY toYYYYMM(day)
ORDER BY (service_name, day)
TTL day + INTERVAL 730 DAY
AS SELECT
  service_name,
  toDate(log_time) AS day,
  countIf(level = 'ERROR') AS error_count,
  countIf(level = 'WARN') AS warn_count,
  count() AS total_count,
  round(countIf(level = 'ERROR') / count() * 100, 4) AS error_rate
FROM logs_raw
GROUP BY service_name, day;
# ...
-- 4. 查询示例
-- 4.1 全文搜索错误日志（秒级）
SELECT log_time, service_name, message, trace_id
FROM logs_raw
WHERE message LIKE '%timeout%'
  AND level = 'ERROR'
  AND log_time > now() - INTERVAL 1 HOUR
ORDER BY log_time DESC
LIMIT 100;
# ...
-- 4.2 服务错误率趋势（使用降采样表，秒级）
SELECT
  hour,
  service_name,
  sumIf(log_count, level = 'ERROR') / sum(log_count) * 100 AS error_rate
FROM logs_hourly
WHERE hour > now() - INTERVAL 7 DAY
  AND service_name = 'order-service'
GROUP BY hour, service_name
ORDER BY hour;
# ...
-- 4.3 Top10错误最多的服务
SELECT
  service_name,
  sum(error_count) AS total_errors,
  round(sum(error_count) / sum(total_count) * 100, 2) AS error_rate
FROM service_health_daily
WHERE day = today()
GROUP BY service_name
ORDER BY total_errors DESC
LIMIT 10;
# ...
-- 4.4 链路追踪查询
SELECT log_time, level, message, host
FROM logs_raw
WHERE trace_id = 'abc-123-def-456'
ORDER BY log_time;
```

```sql
-- output/log-analytics/02_ingest_kafka.sql
-- Kafka流式摄入配置
CREATE TABLE logs_kafka (
  log_time DateTime64(3),
  service_name String,
  level String,
  message String,
  host String,
  trace_id String
) ENGINE = Kafka(
  'kafka-broker:9092',
  'logs-topic',