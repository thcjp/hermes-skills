---
slug: "sqlite-manager"
name: "sqlite-manager"
version: 1.0.1
displayName: "SQLite管理(专业版)"
summary: "面向企业的SQLite管理专业版，含自动备份、连接池监控、Schema迁移、DuckDB集成、灾备恢复与优先支持。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队、企业与专业开发者的SQLite全功能管理专业版。在免费版基础上新增自动定时备份、连接池监控与告警、Schema版本化迁移、DuckDB分析引擎集成、增量备份与时间点恢复、多租户管理与透明数据加密等高级能力，配套面向运维、数据工程师、Agent架构师的多角色场景指南。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修.
tags:
  - 集成工具
  - 本地存储
  - 数据库
  - 高级特性
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 运维
  - 监控
  - 写作
  - python
  - pro
  - sqlite
  - duckdb
  - 加密
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# SQLite管理(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| SQLite管理(专业版)业的SQLite管理 | 不支持 | 支持 |
| SQLite管理(专业版)连接池监控 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 备份策略 | 手动 | 手动+定时+增量+加密 |
| 连接池监控 | 无 | 实时指标+告警 |
| Schema迁移 | 手动SQL | 自动版本迁移+回滚 |
| 分析查询 | 原生SQLite | 集成DuckDB引擎 |
| 灾备恢复 | 全量恢复 | 时间点恢复+断点续传 |
| 多租户 | 无 | 租户隔离+资源配额 |
| 数据加密 | 无 | 透明数据加密(TDE) |
| 优先支持 | 社区 | 工单优先响应 |
### 能力分类

针对能力分类,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力分类相关的配置参数、输入数据和处理选项.
**输出**: 返回能力分类的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力分类`的配置文档进行参数调优
### 备份策略

针对备份策略,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供备份策略相关的配置参数、输入数据和处理选项.
**输出**: 返回备份策略的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`备份策略`的配置文档进行参数调优
### 连接池监控

针对连接池,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供连接池监控相关的配置参数、输入数据和处理选项.
**输出**: 返回连接池监控的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`连接池监控`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：多租户Agent平台（运维视角）

为每个租户分配独立SQLite文件，通过连接池统一管理，监控每个租户的连接数、慢查询、磁盘占用，超阈值自动告警.
```python
from sqlite_manager import MultiTenantManager
# ...
manager = MultiTenantManager(base_dir="/data/tenants")
manager.register_tenant("tenant_a", max_connections=10, quota_gb=5)
manager.register_tenant("tenant_b", max_connections=20, quota_gb=10)
manager.monitor.start()  # 启动监控指标采集
```

### 场景二：日志归档与离线分析（数据工程师视角）

每日将生产日志归档至SQLite，使用DuckDB执行亿级聚合分析，无需迁移到ClickHouse等独立OLAP系统.
```python
import duckdb
# ...
conn = duckdb.connect(":memory:")
conn.execute("ATTACH 'agent_data.db' AS sqlite_db (TYPE sqlite)")
# ...
result = conn.execute("""
    SELECT agent, COUNT(*) AS call_cnt, AVG(latency_ms) AS avg_lat
    FROM sqlite_db.session_logs
    WHERE created_at >= '2026-01-01'
    GROUP BY agent
    ORDER BY call_cnt DESC
""").fetchall()
```

### 场景三：高可用本地存储（架构师视角）

通过WAL+增量备份+时间点恢复构建RPO<5分钟的本地数据高可用方案，适用于边缘节点与离线环境.
```python
pro.high_availability(
    wal_checkpoint="passive",
    incremental_backup="5min",
    pitr_wal_retention="7d",
    auto_restore_on_corruption=True
)
```

### 场景四：Schema平滑升级（开发者视角）

通过版本化迁移脚本管理表结构演进，避免手动ALTER导致的锁表与数据丢失.
```python
pro.migrations.add("003_add_index", up_sql="""
    CREATE INDEX idx_logs_session ON logs(session_id);
""", down_sql="""
    DROP INDEX idx_logs_session;
""")
pro.migrations.migrate()
```

### 场景五：敏感数据加密（安全视角）

对存储敏感信息的SQLite文件启用透明数据加密，密钥通过环境变量注入，落盘数据全部加密.
```python
pro.enable_tde(key_env="DB_ENC_KEY")
# 此后所有写入自动加密，读取自动解密，应用层无感
```

## 使用流程

### 优秀步：启用专业版功能

```python
from sqlite_manager import SQLiteDB, ProFeatures
# ...
db = SQLiteDB("agent_data.db", edition="pro")
pro = ProFeatures(db)
# ...
pro.auto_backup("backups/", schedule="daily", time="02:00")
pro.enable_pool_monitor(alert_threshold=0.8)
```

### 第二步：注册Schema迁移

```python
pro.migrations.add("001_init", """
    CREATE TABLE memos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        tags TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    CREATE INDEX idx_memos_tags ON memos(tags);
""")
pro.migrations.migrate()
```

### 第三步：接入DuckDB分析

```python
pro.analytics.attach_duckdb()
df = pro.analytics.query("SELECT tags, COUNT(*) FROM memos GROUP BY tags")
```

完整上手时间约120秒.
#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "manager 相关配置参数",
    result: "manager 相关配置参数"
  },
  "error": null
}
```

## 异常处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| sqlite3 | CLI工具 | 必需 | 系统自带或官网下载 |
| sqlite3 | Python模块 | 必需 | Python标准库自带 |
| Python | 运行时 | 必需 | python.org 官方下载 |
| duckdb | Python包 | 可选 | `pip install duckdb` |
| boto3 | Python包 | 可选 | `pip install boto3`（S3同步） |
| cryptography | Python包 | 可选 | `pip install cryptography`（TDE加密） |

### API Key 配置
- **DB_ENC_KEY**: 备份加密与TDE密钥，通过环境变量注入，禁止硬编码
- **S3凭证**: 若启用S3同步，配置AWS_ACCESS_KEY_ID与AWS_SECRET_ACCESS_KEY环境变量
- **告警Webhook**: 通过环境变量ALERT_WEBHOOK_URL配置告警通知地址

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 连接池调优

```python
from sqlite_manager import ConnectionPool
# ...
pool = ConnectionPool(
    "agent_data.db",
    max_connections=20,
    timeout=10.0,
    idle_timeout=300,
    health_check=True,
    metrics=True
)
print(pool.metrics.summary())
# 活跃连接: 8/20 | 等待数: 0 | 命中率: 98.5% | 平均等待: 2ms
```

### 增量备份策略

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

### 多租户资源配额

```python
manager.set_quota("tenant_a",
    max_connections=10,
    max_storage_gb=5,
    max_qps=100,
    backup_schedule="daily"
)
manager.alert_on_quota_exceed(webhook_env="OPS_WEBHOOK")
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 本地运行，不支持多设备同步
- 监控精度受限于系统采样频率
- 免费版不支持远程监控与多设备管理
- 长时间监控可能占用较多存储空间

## 常见问题

**Q: 如何处理异常输入?**
A: 系统会自动检测并返回错误提示, 同时提供修复建议.
**Q: 支持哪些输入格式?**
A: 支持标准文本、JSON、CSV等常见格式.