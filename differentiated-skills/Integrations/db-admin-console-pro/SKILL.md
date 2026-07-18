---
slug: db-admin-console-pro
name: db-admin-console-pro
version: "1.0.0"
displayName: 数据库管理台(专业版)
summary: 全功能数据库管理平台,支持大规模批量操作、分区表、性能基线、定时备份与多实例管理。
license: MIT
edition: pro
description: |-
  数据库管理台专业版面向专业 DBA、后端架构师与运维团队,提供完整的数据库设计、批量操作、性能优化与运维自动化能力。

  核心能力:
  - 涵盖免费版全部能力,无单表大小与操作规模限制
  - 大规模批量操作:COPY 命令、批量 INSERT 10 万级、事务优化与检查点
  - 分区表与表空间:按时间/范围/列表分区,空间管理
  - 存储过程与触发器:自动化业务逻辑封装
  - 查询性能基线:SQL 性能回归检测、慢查询追踪、自动索引建议
  - 定时备份与恢复:增量/全量备份、PITR 时间点恢复
  - 多实例管理:读写分离、连接池、主从同步
  - Schema 迁移版本管理:迁移脚本版本化、回滚、审计
  - 跨数据库同步:`PostgreSQL` ↔ MySQL ↔ ClickHouse
  - 安全与审计:权限管理、数据脱敏、操作审计

  适用场景:
  - 企业级数据库设计与运维
  - 高并发业务批量数据处理
  - 数据仓库 ETL 与同步
  - 多数据库实例统一管理

  差异化:相比免费版,专业版补齐"批量、分区、性能基线、自动化运维、多实例"五大短板,形成完整的数据库管理生产线。

  触发关键词:批量操作、分区表、性能基线、定时备份、多实例、Schema迁移、`PostgreSQL`、数据同步
tags:
  - 数据库管理
  - 性能优化
  - 自动化运维
  - 集成工具
tools:
  - read
  - exec
---

# 数据库管理台 专业版

## 一、概述

数据库管理台专业版在免费版的日常管理能力之上,补齐"大规模批量操作、分区表、性能基线、定时备份、多实例管理"五大短板,形成完整的数据库管理生产线。面向专业 DBA、后端架构师、运维团队与数据工程师,适合需要处理大规模数据、跨实例协同与自动化运维的团队场景。

专业版支持 10 万级批量插入与 COPY 命令、按时间/范围/列表的分区表、SQL 性能基线与回归检测、定时备份与 PITR 时间点恢复、多实例读写分离与主从同步、Schema 迁移版本管理,以及跨数据库同步与安全审计。

## 二、核心能力

### 2.1 表结构设计(完整版)

| 能力 | 说明 |
|------|------|
| 主键策略 | SERIAL/BIGSERIAL/UUID/复合主键 |
| 分区表 | RANGE/LIST/HASH 分区,自动分区维护 |
| 表空间 | 数据/索引分离存储,IO 优化 |
| 约束 | NOT NULL/UNIQUE/CHECK/EXCLUDE/外键 |
| 默认值 | 静态/动态(CURRENT_TIMESTAMP/序列) |
| 数据类型 | 全类型覆盖,含 JSONB/ARRAY/ENUM/RANGE |

### 2.2 大规模批量操作

- **COPY 命令**:`PostgreSQL` 高速批量导入(比 INSERT 快 10 倍+)
- **批量 INSERT**:10 万级数据分批提交
- **事务优化**:大事务切分为小事务,避免锁表
- **检查点策略**:每 N 行提交一次,失败可断点续传
- **幂等保证**:`ON CONFLICT DO UPDATE` 实现幂等
- **类型校验**:批量插入前预校验,失败项隔离

### 2.3 分区表与表空间

```sql
-- 按时间范围分区
CREATE TABLE events (
    id          BIGSERIAL,
    created_at  TIMESTAMPTZ NOT NULL,
    data        JSONB
) PARTITION BY RANGE (created_at);

CREATE TABLE events_2024_01 PARTITION OF events
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE events_2024_02 PARTITION OF events
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

-- 自动分区维护(通过 pg_partman 扩展)
```

### 2.4 存储过程与触发器

- **存储过程**:封装复杂业务逻辑,降低应用层复杂度
- **触发器**:BEFORE/AFTER INSERT/UPDATE/DELETE 触发
- **事件触发器**:DDL 操作触发,如审计日志
- **事务内调用**:支持事务回滚与异常处理

### 2.5 查询性能基线

- **SQL 性能基线**:为每条关键 SQL 记录执行时间基线
- **回归检测**:SQL 改动后与基线对比,自动告警
- **慢查询追踪**:`pg_stat_statements` 自动收集慢查询
- **自动索引建议**:基于查询模式给出索引建议
- **执行计划对比**:新旧执行计划 diff,定位性能变化

### 2.6 定时备份与恢复

| 备份类型 | 命令 | 频率 | 恢复粒度 |
|----------|------|------|----------|
| 全量备份 | `pg_dump` | 每日 | 库/表/模式 |
| 增量备份 | WAL 归档 | 持续 | 任意时间点 |
| 逻辑备份 | `pg_dump` | 按需 | 表/行级 |
| PITR | WAL + 全量 | 按需 | 时间点恢复 |

- **自动化调度**:cron 定时触发备份任务
- **异地备份**:支持同步到 OSS/S3
- **恢复演练**:定期恢复测试,验证可用性

### 2.7 多实例管理

- **读写分离**:写主库,读从库,自动路由
- **连接池**:`pgbouncer` / `pgpool-II` 管理并发连接
- **主从同步**:流复制(同步/异步)
- **故障切换**:主库故障自动切换从库
- **多租户**:Schema 级隔离与配额管理

### 2.8 Schema 迁移版本管理

- **迁移脚本**:每个变更一个版本号文件
- **版本追踪**:数据库表记录当前版本
- **回滚支持**:每个迁移配套回滚脚本
- **审计日志**:谁在何时执行了什么迁移
- **CI/CD 集成**:迁移脚本走代码评审与自动化执行

### 2.9 跨数据库同步

- **`PostgreSQL` ↔ MySQL**:基于触发器或 CDC
- **`PostgreSQL` ↔ ClickHouse**:OLTP → OLAP 同步
- **批量同步**:定时全量或增量同步
- **数据校验**:同步后行数与字段一致性校验
- **冲突处理**:同一记录多处变更的解决策略

### 2.10 安全与审计

- **权限管理**:角色级权限,最小权限原则
- **数据脱敏**:敏感字段查询时自动脱敏
- **操作审计**:DDL/DML 操作完整记录
- **登录审计**:登录成功/失败日志
- **数据加密**:传输层 SSL,存储层 TDE

## 三、使用场景

### 3.1 按角色场景矩阵

| 角色 | 场景 | 关键能力 | 输出形态 |
|------|------|----------|----------|
| DBA | 大规模数据迁移 | 批量操作 + 检查点 | 迁移报告 + 校验结果 |
| 后端架构师 | 性能优化 | 性能基线 + 索引建议 | 优化方案 + 执行计划对比 |
| 运维工程师 | 自动化备份 | 定时备份 + PITR | 备份文件 + 恢复演练报告 |
| 数据工程师 | 跨库同步 | CDC + 数据校验 | 同步任务 + 一致性报告 |

### 3.2 典型工作流

```text
1. 业务方提出新需求:订单表需支持 10 亿行
2. DBA 设计分区表(按月分区)
3. 编写迁移脚本(版本化)
4. CI/CD 自动执行迁移
5. 验证性能基线,与旧表对比
6. 配置自动分区维护任务
7. 设置慢查询监控与告警
8. 定时备份与恢复演练
```

## 四、快速开始

预计上手时间:**< 120 秒**(数据库连接需配置凭证)。

### 4.1 大规模批量导入

```text
请把 sales.csv(约 1000 万行)导入到 sales 表:
- 数据库: PostgreSQL(凭证从环境变量读取)
- 表: sales(已存在,按月分区)
- 方式: COPY 命令
- 检查点: 每 100 万行提交一次
- 失败处理: 隔离失败行,继续处理
- 完成后: 输出导入报告与失败行清单
```

### 4.2 性能优化

```text
请优化这条慢查询:
- SQL: SELECT ... FROM orders WHERE ...
- 当前耗时: 8.5s
- 目标: <500ms
- 要求: 给出索引建议 + 改写 SQL + 执行计划对比
- 与性能基线对比,验证优化效果
```

### 4.3 定时备份配置

```text
请配置定时备份任务:
- 数据库: PostgreSQL(凭证从环境变量读取)
- 全量备份: 每日凌晨 02:00
- 增量备份: WAL 持续归档
- 异地备份: 同步到 OSS(bucket: db-backups)
- 恢复演练: 每周一次
- 保留策略: 全量 30 天,WAL 7 天
```

### 4.4 Schema 迁移

```text
请为以下变更创建迁移脚本:
- 新增字段: orders.shipping_address JSONB
- 新增索引: idx_orders_shipping_status
- 数据回填: 已有订单的 shipping_address 默认 null
- 迁移版本: 2024_12_15_add_shipping
- 配套回滚脚本
```

## 五、配置示例

### 5.1 多实例配置

```yaml
instances:
  primary:
    type: postgres
    host: ${DB_PRIMARY_HOST}
    port: ${DB_PRIMARY_PORT}
    user: ${DB_PRIMARY_USER}
    password: ${DB_PRIMARY_PASSWORD}
    database: ${DB_PRIMARY_NAME}
    role: write
    pool_size: 20
  replicas:
    - host: ${DB_REPLICA1_HOST}
      role: read
      pool_size: 10
    - host: ${DB_REPLICA2_HOST}
      role: read
      pool_size: 10
```

### 5.2 批量导入脚本

```python
import os
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_NAME']
)

# COPY 命令高速导入
with open('sales.csv', 'r', encoding='utf-8') as f:
    with conn.cursor() as cur:
        cur.copy_expert(
            "COPY sales FROM STDIN WITH (FORMAT csv, HEADER true, "
            "DELIMITER ',', NULL '\\N')",
            f
        )
    conn.commit()
```

### 5.3 分区表自动维护

```sql
-- 使用 pg_partman 扩展自动维护分区
CREATE EXTENSION IF NOT EXISTS pg_partman;

SELECT partman.create_parent(
    parent_table => 'public.events',
    control => 'created_at',
    type => 'range',
    interval => 'monthly',
    premake => 6  -- 预创建未来 6 个月的分区
);

-- 定期运行维护函数(通过 cron)
SELECT partman.run_maintenance();
```

### 5.4 性能基线配置

```yaml
performance:
  baseline:
    enabled: true
    sample_size: 100
    threshold: 1.5    # 1.5 倍基线触发告警
    key_queries:
      - id: top_orders_by_user
        sql: "SELECT * FROM orders WHERE user_id = $1 ORDER BY created_at DESC LIMIT 50"
        max_ms: 100
      - id: daily_sales_summary
        sql: "SELECT date, SUM(amount) FROM sales GROUP BY date"
        max_ms: 500
  slow_query:
    threshold_ms: 1000
    sample_rate: 1.0
```

### 5.5 备份配置

```yaml
backup:
  full:
    schedule: "0 2 * * *"  # 每日 02:00
    command: "pg_dump"
    compress: gzip
    target: local
    retention_days: 30
  wal:
    archive: true
    target: oss
    oss_bucket: db-backups
    retention_days: 7
  recovery_test:
    schedule: "0 4 * * 1"  # 每周一 04:00
    target_db: recovery_test
```

### 5.6 Schema 迁移版本管理

```yaml
migrations:
  dir: ./migrations
  table: schema_migrations
  naming: "{date}_{seq}_{description}.sql"
  audit: true
  rollback: true
  ci_cd:
    auto_apply: false
    review_required: true
```

## 六、最佳实践

- **分区优先**:大表(>1000 万行)优先考虑分区,按时间或热点字段
- **批量提交**:大批量操作分批提交,避免长事务持锁
- **COPY 命令**:大批量导入用 COPY,比 INSERT 快 10 倍+
- **性能基线**:关键 SQL 建立基线,变更后回归检测
- **索引策略**:WHERE/JOIN/ORDER BY 字段建索引,低选择性字段不单独建
- **连接池**:高并发场景用 `pgbouncer` 管理连接
- **读写分离**:读多写少场景分离主从,降低主库压力
- **定期维护**:VACUUM ANALYZE、REINDEX、统计信息更新
- **备份演练**:定期恢复测试,验证备份可用性
- **迁移版本化**:DDL 变更走版本化迁移脚本,支持回滚
- **凭证安全**:数据库密码一律走环境变量,**禁止**硬编码
- **权限最小化**:角色级权限,最小权限原则

## 七、常见问题

### Q1: 专业版支持多大的表?

A: 单表支持 10 亿行级别(分区表)。批量操作支持千万级数据导入,通过 COPY 命令与分批提交优化性能。

### Q2: 分区表如何选择分区策略?

A: 时间序列数据用 RANGE 分区(按月/日);枚举值固定用 LIST 分区(按地区);均匀分布用 HASH 分区。

### Q3: COPY 命令与 INSERT 哪个更快?

A: COPY 比 INSERT 快 10 倍以上,适合大批量导入。COPY 走二进制协议,绕过 SQL 解析,且支持并行。

### Q4: 性能基线如何建立?

A: 为每条关键 SQL 采样多次执行时间,取 P95 作为基线。变更后再次采样,与基线对比,超出阈值(如 1.5 倍)告警。

### Q5: PITR 时间点恢复如何工作?

A: 基于全量备份 + WAL 归档,可恢复到任意时间点。流程:恢复全量 → 回放 WAL 到目标时间点 → 完成恢复。

### Q6: 多实例读写分离如何实现?

A: 主库负责写,从库负责读。应用层通过连接池(`pgbouncer`)路由,读请求自动分发到从库。同步延迟需监控。

### Q7: Schema 迁移如何回滚?

A: 每个迁移脚本配套回滚脚本。版本表记录当前版本,回滚时按逆序执行回滚脚本。

### Q8: 跨数据库同步如何处理类型差异?

A: 通过类型映射表统一处理。如 `PostgreSQL` 的 JSONB ↔ MySQL 的 JSON,`PostgreSQL` 的 BIGSERIAL ↔ MySQL 的 BIGINT AUTO_INCREMENT。

### Q9: 是否支持 MCP工具扩展?

A: 专业版支持通过 MCP工具协议接入外部数据库与运维工具,可在 `mcp_servers` 配置块中注册 MCP server 与 MCP端点,融入 MCP生态共享数据库管理能力。

### Q10: 凭证如何安全存储?

A: **必须**通过环境变量传入,**禁止**硬编码;推荐存放于 `d:\skills\.skill-credentials\` 目录(已 gitignore)。多实例可分别配置不同凭证。

## 八、专业版特性

本专业版相比免费版新增以下能力:

- 大规模批量操作:COPY 命令、批量 INSERT 10 万级、检查点、幂等保证
- 分区表与表空间:RANGE/LIST/HASH 分区、自动维护、IO 优化
- 存储过程与触发器:业务逻辑封装、事件触发
- 查询性能基线:回归检测、慢查询追踪、自动索引建议
- 定时备份与恢复:全量/增量/WAL/PITR、异地备份、恢复演练
- 多实例管理:读写分离、连接池、主从同步、故障切换
- Schema 迁移版本管理:版本化、回滚、审计、CI/CD 集成
- 跨数据库同步:`PostgreSQL` ↔ MySQL ↔ ClickHouse
- 安全与审计:权限管理、数据脱敏、操作审计、加密
- MCP工具集成:通过 MCP server 接入外部能力,融入 MCP生态

## 九、定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 基础 DDL/DML + 查询优化 + 事务安全 | 个人/小项目 |
| 收费专业版 | ¥299/月 | 全功能 + 批量 + 分区 + 自动化运维 + 多实例 | 团队/企业 |

专业版通过 SkillHub SkillPay 发布。

## 十、依赖说明

### 运行环境

- **Agent 平台**: 任意支持 SKILL.md 的 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **数据库**: `PostgreSQL` 13+(推荐)/ MySQL 8+ / ClickHouse 22+
- **Python**: 3.9+(运维脚本需要)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| psycopg2 | Python 库 | 必需 | `pip install psycopg2-binary`(`PostgreSQL`) |
| mysql-connector | Python 库 | 可选 | `pip install mysql-connector-python`(MySQL) |
| clickhouse-driver | Python 库 | 可选 | `pip install clickhouse-driver`(ClickHouse) |
| SQLAlchemy | Python 库 | 必需 | `pip install sqlalchemy`(ORM) |
| alembic | Python 库 | 可选 | `pip install alembic`(Schema 迁移) |
| redis | Python 库 | 可选 | `pip install redis`(连接池/缓存) |
| boto3 | Python 库 | 可选 | `pip install boto3`(OSS/S3 异地备份) |
| pg_partman | PG 扩展 | 可选 | 通过 `CREATE EXTENSION` 安装 |
| pgbouncer | 中间件 | 可选 | 系统包管理器安装(连接池) |

### API Key 配置

- **主库凭证**: 通过 `DB_PRIMARY_HOST`/`DB_PRIMARY_USER`/`DB_PRIMARY_PASSWORD` 等环境变量传入
- **从库凭证**: 通过 `DB_REPLICA1_HOST` 等环境变量传入
- **对象存储**: 通过 `OSS_ACCESS_KEY`/`OSS_SECRET_KEY` 等环境变量传入
- **禁止**: 在 SKILL.md、脚本、配置文件中硬编码任何凭证
- **推荐路径**: 凭证统一存放在 `d:\skills\.skill-credentials\` 目录(已 gitignore)

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言驱动的 AI Skill,集成批量操作、分区表、性能基线与自动化运维的完整生产线
