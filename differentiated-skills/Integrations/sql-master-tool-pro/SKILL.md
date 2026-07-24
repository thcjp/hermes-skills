---
slug: "sql-master-tool-pro"
name: "sql-master-tool-pro"
version: "1.0.0"
displayName: "SQL大师工具(专业版)"
summary: "面向企业的SQL全栈专业版，含自动化迁移、增量压缩备份、Schema对比同步、高可用与读写分离配置。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队、企业与专业DBA的SQL全栈工具专业版。在免费版基础上新增自动化迁移工具、增量与压缩备份、多数据库Schema对比与同步、查询性能基准测试、高可用与读写分离配置、灾备恢复等高级能力，配套面向运维、数据工程师、DBA的多角色场景指南。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策.
tags:
  - 集成工具
  - 数据库
  - SQL全栈
  - 高级特性
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# SQL大师工具（专业版）

专业版在免费版核心能力之上，新增自动化迁移工具、增量压缩备份、多数据库Schema对比同步、性能基准测试、高可用与读写分离配置、灾备恢复等高级能力，专为团队协作、企业生产环境与高可用场景设计.
## 概述

当数据库从"单机开发"走向"企业生产"，对Schema演进管理、备份策略、多环境同步与高可用的要求显著提升：需要版本化迁移工具避免手工ALTER的混乱、需要增量压缩备份降低存储成本、需要多环境Schema对比防止结构漂移、需要主从复制与读写分离保障可用性。专业版针对这些场景提供完整解决方案，使数据库运维从"手动操作"升级为"可追溯、可恢复、可观测"的工程化能力.
同时内置多数据库Schema对比引擎，能在 `PostgreSQL`、MySQL、SQLite间自动识别结构差异并生成同步脚本，显著降低多环境维护成本.
## 核心能力

| 能力分类 | 免费版 | 专业版 |
|----|---|---|
| 迁移管理 | 手动脚本 | 自动化工具+回滚+校验 |
| 备份策略 | 手动全量 | 全量+增量+压缩+加密 |
| Schema对比 | 无 | 多库差异对比+同步脚本 |
| 性能基准 | 无 | 压测套件+回归对比 |
| 高可用 | 无 | 主从复制+读写分离+切换 |
| 灾备恢复 | 全量恢复 | 时间点恢复+断点续传 |
| 监控告警 | 无 | 慢查询+磁盘+连接池告警 |
| 优先支持 | 社区 | 工单优先响应 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置.
### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：面向企业的、SQL、全栈专业版、含自动化迁移、增量压缩备份、Schema、对比同步、高可用与读写分离、面向团队、企业与专业、DBA、全栈工具专业版、在免费版基础上新、增自动化迁移工具、增量与压缩备份、多数据库、对比与同步、查询性能基准测试、灾备恢复等高级能、配套面向运维、数据工程师、的多角色场景指南、Use、when、需要数据库操作、数据存储管理时使、不适用于数据库架、构设计决策等.
## 使用场景

### 场景一：版本化迁移管理（运维视角）

通过版本化迁移工具管理表结构演进，每次变更自动记录、可回滚，避免手动ALTER导致的混乱与数据丢失.
```python
from sql_master_tool import ProFeatures
# ...
pro = ProFeatures(db_url="postgresql://user:pass@localhost/mydb")
pro.migrations.add("005_add_orders_shipping", up_sql="""
    ALTER TABLE orders ADD COLUMN shipping_address TEXT;
    CREATE INDEX idx_orders_shipping ON orders(shipping_address);
""", down_sql="""
    DROP INDEX idx_orders_shipping;
    ALTER TABLE orders DROP COLUMN shipping_address;
""")
pro.migrations.migrate()  # 自动按版本号顺序执行
```

### 场景二：增量压缩备份（DBA视角）

采用"每周全量+每小时增量"策略，配合压缩与加密，在保障RPO<1小时的同时将存储成本降低60%以上.
```python
pro.backup_strategy(
    full_backup="weekly",
    incremental="hourly",
    retention_days=30,
    compress=True,
    encrypt_key_env="DB_ENC_KEY",
    sync_to=["s3://my-bucket/backups/"]
)
```

### 场景三：多环境Schema同步（架构师视角）

对比开发与生产环境的Schema差异，生成同步脚本，防止环境间结构漂移.
```python
diff = pro.schema_compare(
    source="postgresql://dev-host/dev_db",
    target="postgresql://prod-host/prod_db"
)
# 输出：3张表新增、1张表字段差异、2个索引缺失
diff.generate_sync_script("sync_to_prod.sql")
```

### 场景四：高可用读写分离（DBA视角）

配置主从复制与读写分离，写操作走主库，只读查询自动分流到副本，提升整体吞吐与可用性.
```python
pro.high_availability(
    master="postgresql://master-host:5432/mydb",
    replicas=["postgresql://replica-1:5432/mydb", "postgresql://replica-2:5432/mydb"],
    read_split=0.8,
    failover="auto",           # 自动故障切换
    health_check_interval=10   # 10秒健康检查
)
```

### 场景五：灾备时间点恢复（运维视角）

基于WAL日志实现时间点恢复（PITR），可将数据库恢复到任意指定时刻，RPO可达秒级.
```python
pro.pitr_recovery(
    target_time="2026-07-18 14:30:00",
    backup_base="backups/2026-07-15-full.dump",
    wal_dir="wal_archive/"
)
```

## 快速开始

### 第一步：启用专业版功能

```python
from sql_master_tool import ProFeatures
# ...
pro = ProFeatures(db_url="postgresql://user:pass@localhost/mydb")
pro.auto_backup("backups/", schedule="daily", time="02:00")
pro.enable_monitor(alert_webhook_env="OPS_WEBHOOK")
```

### 第二步：注册迁移脚本

```python
pro.migrations.add("001_init", """
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW()
    );
""")
pro.migrations.migrate()
```

### 第三步：Schema对比

```python
diff = pro.schema_compare(source="dev_url", target="prod_url")
print(diff.summary())
```

完整上手时间约120秒.
**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

### 迁移校验与回滚

```python
pro.migrations.config(
    pre_check=True,        # 迁移前语法校验
    dry_run=True,          # 演练模式，不真正执行
    auto_rollback=True,    # 失败自动回滚
    timeout=300            # 单脚本超时5分钟
)
```

### 备份3-2-1策略

```python
pro.backup_strategy(
    full_backup="daily",
    incremental="hourly",
    copies=3,                          # 至少3份副本
    media=["local", "s3", "nas"],      # 2种以上介质
    offsite=True,                      # 1份异地
    retention_days=90,
    compress_level=6,
    encrypt_key_env="DB_ENC_KEY"
)
```

### 监控告警配置

```python
pro.monitor_config(
    slow_query_threshold_ms=500,
    disk_alert_threshold=80,           # 磁盘使用率80%告警
    connection_pool_alert=0.9,         # 连接池使用率90%告警
    replication_lag_alert=10,          # 复制延迟超10秒告警
    webhook_env="OPS_WEBHOOK",
    schedule="realtime"
)
```

## 最佳实践

### 1. 迁移脚本必须包含down方向

每个迁移脚本必须有up和down两个方向，确保失败时可回滚，避免Schema进入不一致状态.
### 2. 备份遵循3-2-1原则

至少3份副本、2种存储介质、1份异地存放。专业版支持自动同步到对象存储，满足异地要求.
### 3. Schema对比纳入发布流程

每次发布前执行`pro.schema_compare`对比开发与生产环境，差异需人工确认后才同步，防止意外变更.
### 4. 故障切换需演练

高可用配置的自动故障切换需定期演练（至少每季度一次），确保切换逻辑可用且团队熟悉流程.
### 5. WAL归档保留足够时长

时间点恢复依赖WAL日志，建议归档保留至少7天，覆盖常规故障发现与响应窗口.
## 常见问题

### Q1：迁移失败后如何回滚？

A：专业版支持事务化迁移，失败自动回滚。若已部分提交，使用`pro.migrations.rollback("版本号")`回滚到指定版本。建议迁移前先用`dry_run=True`演练.
### Q2：增量备份恢复时报版本不匹配？

A：增量备份必须基于全量备份恢复，且全量备份的版本号必须与增量记录的基线一致。使用`pro.backup.validate()`校验备份链完整性.
### Q3：Schema对比显示大量差异如何处理？

A：(1) 先确认是否为预期的环境差异（如开发环境有测试表）；(2) 按变更类型分类处理：新增表→评估是否需同步、字段差异→重点审查；(3) 同步前务必备份目标库.
### Q4：读写分离后出现"写后读不到"？

A：只读副本存在复制延迟。对"写后立即读"场景使用`pro.route_to_master()`强制走主库，或配置`read_your_writes=True`.
### Q5：故障切换后原主库如何恢复？

A：原主库修复后需重新配置为副本。专业版提供`pro.rebuild_replica(old_master_url)`工具，自动从新主库同步全量数据并建立复制关系.
### Q6：时间点恢复会丢失数据吗？

A：会丢失目标时间点之后的数据。PITR是将数据库恢复到指定时刻的状态，之后的数据需要从WAL日志重放或业务层补录.
### Q7：压缩备份对性能有影响吗？

A：压缩主要消耗CPU。建议在业务低峰期执行全量压缩备份，或使用`compress_level`调低压缩级别（1-9，默认6）平衡速度与压缩率.
### Q8：多数据库Schema对比支持哪些差异？

A：支持表结构、字段类型、约束、索引、视图的差异识别。存储过程、触发器等数据库方言相关对象的对比仅在同类型数据库间支持.
### Q9：监控告警频繁触发怎么办？

A：先区分告警类型：慢查询告警→优化SQL或补建索引；磁盘告警→清理历史数据或扩容；连接池告警→调大连接数或引入缓存。建议为不同级别告警设置不同通知方式.
### Q10：专业版支持哪些数据库？

A：`PostgreSQL` 9.6+、MySQL 5.7+、SQLite 3.35+。SQL Server部分功能支持，高可用与PITR暂不支持SQL Server.
## 专业版特性

本专业版相比免费版新增以下能力：
- 自动化迁移工具：版本化迁移、自动回滚、迁移前校验、dry-run演练
- 增量压缩备份：全量+增量+压缩+加密，支持异地对象存储同步
- Schema对比同步：多数据库结构差异对比与同步脚本生成
- 性能基准测试：压测套件+回归对比+基线管理
- 高可用配置：主从复制、读写分离、自动故障切换
- 灾备恢复：时间点恢复、断点续传、异地容灾
- 监控告警：慢查询、磁盘、连接池、复制延迟监控
- 优先工单支持：工作日2小时内响应

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|:-----|:-----|:-----|:-----|
| 免费体验版 | 0元 | 核心功能+基础示例 | 个人试用 |
| 收费专业版 | 99元/月 | 全功能+高级特性+优先支持 | 团队/企业 |

专业版通过SkillHub SkillPay发布.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| psql | CLI工具 | 必需 | `PostgreSQL` 安装包 |
| mysql | CLI工具 | 可选 | MySQL 客户端安装包 |
| sqlite3 | CLI工具 | 可选 | 系统自带或官网下载 |
| Python | 运行时 | 必需 | python.org 官方下载 |
| psycopg2 | Python包 | 必需 | `pip install psycopg2` |
| boto3 | Python包 | 可选 | `pip install boto3`（S3同步） |
| cryptography | Python包 | 可选 | `pip install cryptography`（加密备份） |

### API Key 配置
- **DB_ENC_KEY**: 备份加密密钥，通过环境变量注入，禁止硬编码
- **S3凭证**: 若启用S3同步，配置AWS_ACCESS_KEY_ID与AWS_SECRET_ACCESS_KEY环境变量
- **OPS_WEBHOOK**: 监控告警Webhook地址，通过环境变量配置
- **数据库连接凭证**: 通过环境变量或配置文件注入，禁止硬编码

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "SQL大师工具(专业版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "sql master pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
