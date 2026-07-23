---
slug: "pg-mcp-skills"
name: "pg-mcp-skills"
version: "1.0.0"
displayName: "PG-MCP助手(专业版)"
summary: "企业级`PostgreSQL`数据库管理方案，支持自动化调优、迁移升级、多实例管理与高可用监控。"
license: "Proprietary"
edition: "pro"
description: |-
  PG-MCP助手专业版是一套面向中大型团队与企业级场景的 `PostgreSQL` 数据库管理解决方案，在免费版基础上扩展出自动化性能调优、智能索引推荐、数据库迁移与版本升级、多实例统一管理、高可用与故障转移监控等能力。核心能力：提供基于执行计划的自动索引推荐、冗余索引清理流程、大版本升级迁移方案、多实例配置中心化管 理、主备切换与故障转移监控、慢查询自动归档与分析报告
tags:
  - 数据库
  - 集成工具
  - MCP工具
  - 企业级
  - 专业版
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# PG-MCP助手(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| PG-MCP助手(专业版)数据库管理 | 不支持 | 支持 |
| PG-MCP助手(专业版)多实例管理 | 不支持 | 支持 |
| PG-MCP助手(专业版)与高可用监控 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |

## 核心能力

### 能力一：自动化性能调优
通过 MCP工具采集执行计划、锁等待、缓存命中率、死元组比例等多维度指标，结合内置规则库自动识别性能瓶颈并给出调优建议.
| 调优维度 | 采集指标 | 自动建议 |
|:-----|:-----|:-----|
| 慢查询 | 平均执行时长、调用次数 | 索引建议、SQL 重写建议 |
| 锁等待 | lock_wait_time、deadlock_count | 锁顺序优化、事务拆分 |
| 缓存命中率 | cache_hit_ratio | shared_buffers 调整、热点表识别 |
| 死元组 | dead_tuple_ratio | VACUUM 频率调整、长事务排查 |
| 连接数 | active_connections | 连接池配置、慢会话清理 |

**输入**: 用户提供能力一：自动化性能调优所需的指令和必要参数.
**输出**: 返回能力一：自动化性能调优的处理结果,包含执行状态码、结果数据和执行日志。### 能力二：智能索引推荐

基于 `pg_stat_statements` 与执行计划分析，自动识别高频查询的缺失索引、冗余索引、未使用索引，生成索引优化建议清单.
### 能力三：数据库迁移与版本升级
提供 `PostgreSQL` 大版本升级（如 13→16）的完整方案，包括兼容性检查、升级方式选择（pg_upgrade / 逻辑复制 / dump-restore）、停机窗口规划、回滚预案.
**输出**: 返回能力三：数据库迁移与版本升级的处理结果,包含执行状态码、结果数据和执行日志.
### 能力四：多实例统一管理
通过配置中心化管理多个数据库实例的连接信息、监控指标、告警规则。支持一键切换目标实例、批量执行诊断命令.
**输入**: 用户提供能力四：多实例统一管理所需的指令和必要参数.
**输出**: 返回能力四：多实例统一管理的处理结果,包含执行状态码、结果数据和执行日志。### 能力五：高可用与故障转移监控
提供主备复制状态监控、复制延迟告警、自动故障转移方案（基于 Patroni 或 repmgr）、脑裂检测与恢复流程.
**处理**: 解析能力五：高可用与故障转移监控的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力五：高可用与故障转移监控的处理结果,包含执行状态码、结果数据和执行日志。### 能力六：慢查询自动归档与分析报告
自动归档超过阈值的慢查询，按周生成分析报告，包含 Top 10 慢查询、趋势变化、优化建议.
**输入**: 用户提供能力六：慢查询自动归档与分析报告所需的指令和必要参数。- 验证返回数据的完整性和格式正确性
- 参考`能力四：多实例统一管理`的配置文档进行参数调优
#
## 适用场景

### 场景一：生产数据库性能调优

DBA 定期通过"自动化性能调优"意图执行全维度扫描，识别性能瓶颈并获取调优建议。关键告警自动推送到企业微信.
### 场景二：跨版本升级迁移

业务需要从 `PostgreSQL` 13 升级到 16 以使用新特性。通过"数据库迁移"意图生成升级方案，包括兼容性检查、停机窗口规划、回滚预案.
### 场景三：多团队数据库平台

公司内多个业务线共享数据库基础设施。通过"多实例管理"意图统一管理所有实例，按租户隔离配置与告警.
### 场景四：金融级高可用部署

核心业务数据库要求 99.99% 可用性。通过"高可用监控"意图部署主备复制、自动故障转移、脑裂检测，保障业务连续性.
### 场景五：合规审计与性能报告

季度审计需要提供数据库性能报告。通过"慢查询分析报告"意图自动生成包含 Top 慢查询、趋势分析、优化建议的结构化报告.
## 使用流程

本助手需要配合 MCP工具使用。请确保已安装并配置 postgres 相关的 MCP工具，且具备专业版授权.
**典型提问模板**：

```
帮我扫描生产库的性能瓶颈，给出调优建议
```

```
我们需要从 PostgreSQL 13 升级到 16，帮我规划升级方案与停机窗口
```

```
管理 5 个数据库实例，统一配置监控与告警
```

Agent 会根据输入识别意图，调用对应的 MCP工具，并返回结构化的方案与建议.
**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | pg-mcp-skills处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 症状 | 可能原因 | 排查方法 | 对策 |
|:---:|:---:|:---:|:---:|
| 数据库响应变慢 | 多种可能 | 执行全维度性能扫描 | 按建议清单逐项优化 |
| 升级后兼容性报错 | 废弃特性或扩展 | 查看错误日志 | 适配代码或回滚版本 |
| 主备复制中断 | 网络或 WAL 堆积 | 查看 pg_stat_replication | 修复网络或扩大 wal_keep_size |
| 脑裂告警 | 双主同时写入 | 检查心跳与仲裁 | 立即下线次要主库 |
| 索引创建卡住 | 长事务阻塞 | 查看 pg_locks | 终止阻塞会话或等待 |
| 慢查询数量激增 | 统计信息陈旧 | 查看 ANALYZE 时间 | 手动 ANALYZE 或调整 autovacuum |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md与 MCP工具的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **数据库**: `PostgreSQL` 13+（推荐 16+，需支持 pg_stat_statements）
- **监控栈**: Prometheus + Grafana + postgres-exporter（推荐）
- **高可用组件**: Patroni 或 repmgr（可选）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| postgres MCP server | 服务 | 必需 | 通过 /setup-postgres-mcp 部署 |
| `PostgreSQL` 客户端 | 工具 | 必需 | psql / pgAdmin / DBeaver 等 |
| pg_stat_statements | 扩展 | 必需 | `PostgreSQL` 内置 contrib |
| Patroni / repmgr | 高可用 | 可选 | 官方仓库或包管理器安装 |
| 配置中心 | 服务 | 可选 | etcd / Consul / ZooKeeper |

### API Key 配置
- 本专业版为知识库型 Skill，自身不需要 API Key
- 数据库连接凭据由 MCP server 配置文件管理，应存储于密钥管理服务中
- 配置中心访问凭据同样需要密钥管理
- 禁止在 SKILL.md 或脚本中硬编码数据库凭据或 API Token

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent调用MCP工具完成企业级数据库管理

## 案例展示

### 自动化性能调优扫描

```text
扫描流程：
1. 调用 get_database_health 获取基础指标
2. 查询 pg_stat_statements 获取慢查询 Top 20
3. 查询 pg_stat_activity 获取锁等待情况
4. 查询 pg_stat_user_tables 获取死元组比例
5. 综合分析，输出调优建议清单
# ...
输出格式：
| 维度 | 当前值 | 建议值 | 优化动作 |
```

### 智能索引推荐

```sql
-- 识别高频查询的缺失索引
SELECT
    query,
    calls,
    mean_exec_time,
    rows
FROM pg_stat_statements
WHERE mean_exec_time > 100  -- 平均执行超过 100ms
ORDER BY calls DESC
LIMIT 20;
# ...
-- 识别未使用的索引
SELECT
    schemaname,
    relname,
    indexrelname,
    idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND schemaname NOT IN ('pg_catalog', 'information_schema');
```

### 大版本升级方案模板

```text
升级方案：PostgreSQL 13 → 16
# ...
阶段一：兼容性检查（1 天）
- 检查废弃特性使用情况
- 检查扩展兼容性
- 检查自定义函数与存储过程
# ...
阶段二：升级方式选择
- pg_upgrade：停机 30 分钟，原地升级
- 逻辑复制：停机 < 1 分钟，需双倍存储
- dump-restore：停机数小时，最安全
# ...
阶段三：停机窗口规划
- 选择业务低峰期（如凌晨 2-4 点）
- 提前 1 周通知业务方
- 准备回滚快照
# ...
阶段四：回滚预案
- 升级前全量备份
- 保留旧版本数据目录
- 验证失败时 15 分钟内回滚
```

### 多实例配置中心

```yaml
# instances.yaml
instances:
  - name: prod-core
    host: 10.0.1.10
    port: 5432
    database: core
    role: primary
    monitoring: true
    alert_rules:
      - connection_count > 80
      - replication_lag > 5s
# ...
  - name: prod-report
    host: 10.0.1.11
    port: 5432
    database: report
    role: replica
    monitoring: true
    alert_rules:
      - replication_lag > 10s
```

### 高可用监控指标

```sql
-- 主备复制状态
SELECT
    client_addr,
    state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn,
    (sent_lsn - replay_lsn) AS replication_lag_bytes
FROM pg_stat_replication;
# ...
-- 脑裂检测
SELECT
    CASE
        WHEN count(*) > 1 THEN 'SPLIT_BRAIN_ALERT'
        ELSE 'OK'
    END AS status
FROM pg_stat_replication;
```

## 常见问题

### Q1：自动化调优会自动执行优化动作吗？

不会。本助手只提供建议，所有优化动作（如创建索引、调整参数）需人工确认后执行。生产环境的自动化操作需要额外审批流程.
### Q2：索引推荐准确率如何？

基于执行计划与统计信息的推荐准确率约 85%。最终是否采纳需结合业务场景判断，如查询频率、写入压力、存储成本等.
### Q3：版本升级停机窗口多久？

取决于数据量与升级方式。pg_upgrade 通常 30 分钟以内；逻辑复制可做到秒级切换但需双倍存储；dump-restore 适用于小库，大库耗时数小时.
### Q4：多实例管理如何保证配置一致性？

使用配置中心（如 etcd / Consul）存储实例配置，通过模板渲染生成各实例的 postgresql.conf。变更时批量推送并验证.
### Q5：高可用方案选 Patroni 还是 repmgr？

Patroni 更现代化，支持自动故障转移与 Kubernetes 部署，适合云原生场景；repmgr 更轻量，适合传统物理机部署。根据基础设施选择.
### Q6：慢查询报告如何分发？

建议按周生成，通过邮件或企业微信推送给 DBA 与开发负责人。关键慢查询（执行时长超过阈值 2 倍）触发即时告警.
### Q7：性能调优后如何验证效果？

调优前后使用相同工作负载压测，对比平均响应时间、P95 延迟、吞吐量等指标。生产环境可通过 A/B 流量对比验证.
### Q8：多实例管理的安全风险？

主要风险是配置泄露与误操作。建议连接凭据存储于密钥管理服务，所有操作记录审计日志，写操作需二次确认.
### Q9：高可用方案的 RPO 与 RTO？

基于同步复制的方案 RPO=0（无数据丢失），RTO<30 秒；基于异步复制的方案 RPO>0（可能丢失少量数据），RTO<10 秒。根据业务 SLA 选择.
### Q10：版本升级失败如何回滚？

pg_upgrade 保留旧版本数据目录，回滚只需切换回旧版本二进制并启动旧目录；逻辑复制方案回滚只需切换应用连接到旧主库.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

