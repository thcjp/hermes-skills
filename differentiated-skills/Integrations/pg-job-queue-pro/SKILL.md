---
slug: pg-job-queue-pro
name: pg-job-queue-pro
version: "1.0.0"
displayName: PG任务队列(专业版)
summary: 基于`PostgreSQL`的企业级任务队列，支持DAG编排、分片扩展、死信队列与高可用方案。
license: Proprietary
edition: pro
description: |-
  PG任务队列专业版是一套面向中大型团队与企业级场景的 `PostgreSQL` 任务队列解决方案，在免费版基础上扩展出任务依赖图编排、多队列分片、死信队列、高可用部署、灰度发布与高级监控等能力。核心能力：提供 DAG 任务编排模型、按 job_type 水平分片方案、死信队列与人工补偿流程、主备切换与故障转移设计、灰度发布与版本回滚策略、Prometheus 指标体系与告警规则模板
tags:
- 数据库
- 集成工具
- 任务队列
- 企业级
- 专业版
tools:
  - - read
- exec
---
# PG任务队列（专业版）

## 概述

当任务量从日均万级增长到百万级，当任务之间存在复杂依赖关系，当业务对可靠性提出金融级要求时，简单的单表队列已无法满足需求。本专业版在免费版基础上，系统性地扩展出企业级队列所需的全部高级能力。

专业版聚焦于**中大型团队与企业级场景的核心痛点**：任务编排复杂度上升、单表吞吐瓶颈、失败任务堆积、故障切换中断、版本上线风险、监控盲区。每种能力均提供架构设计、配置示例、容量规划与上线检查清单。

## 核心能力

### 依赖说明

复杂业务场景中，任务往往存在依赖关系（如"报表生成依赖数据同步完成"）。本助手提供基于依赖表与拓扑排序的 DAG 编排方案，支持串行、并行、扇出、扇入四种基础模式。

| 编排模式 | 适用场景 | 实现要点 |
|:---------|:---------|:---------|
| 串行 | A 完成后才能执行 B | depends_on 字段 + 完成回调检查 |
| 并行 | A 与 B 互不依赖可同时执行 | 独立 job_type + 各自 Worker |
| 扇出 | A 完成后触发 B、C、D | A 完成时批量插入 B/C/D |
| 扇入 | B、C、D 全部完成后触发 E | depends_on 数组 + 全完成检查 |

### 能力二：多队列水平分片

单表吞吐瓶颈约在 1000 任务/秒。超过此量级时，按 `job_type` 分表是最低成本的扩展方案。本助手提供分片策略设计、跨分片查询方案、分片扩容流程。

### 能力三：死信队列与人工补偿

重试 `max_attempts` 次后仍失败的任务进入死信队列，由人工审核后决定重试、丢弃或修复。本助手提供死信队列表设计、告警通知方案、补偿流程模板。

### 能力四：高可用与故障转移

队列服务自身也需要高可用。本助手提供主备 Worker 部署方案、数据库主备切换流程、Worker 健康检查与自动重启机制。

### 能力五：灰度发布与版本回滚

任务逻辑变更时，如何在不中断现有任务的前提下灰度发布新版本？本助手提供基于 Worker 版本标签的灰度方案与一键回滚流程。

### 能力六：高级监控告警体系

提供 Prometheus 指标采集模板、Grafana 仪表盘 JSON、告警规则模板（pending 堆积、失败率飙升、Worker 离线、执行时长异常等）。

## 使用场景

### 场景一：金融级批处理

每日凌晨的对账任务，涉及数据同步、对账计算、差异报告、告警通知四个阶段，任一阶段失败需人工介入。使用 DAG 编排 + 死信队列 + 全链路监控。

### 场景二：电商大促任务洪峰

双 11 期间任务量激增 10 倍，单表无法承载。按 `job_type` 分片到 4 张子表，每张表独立 Worker 池，整体吞吐提升 4 倍。

### 场景三：多团队共享队列平台

公司内多个业务线共用一套队列基础设施。通过命名空间隔离、配额管理、优先级抢占机制，保障关键业务不被低优先级任务挤占。

### 场景四：跨集群任务迁移

集群迁移期间，新旧集群并行运行，任务需逐步从旧集群切到新集群。通过灰度发布机制，按比例将任务路由到新集群，异常时一键回滚。

## 不适用场景

以下场景PG任务队列(专业版)不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析


## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求。


## 快速开始

本助手为知识库型 Skill，无需安装额外依赖。直接在 Agent 对话中描述你的企业级队列需求即可获取方案。

**典型提问模板**：

```
我的对账任务涉及 4 个阶段，每个阶段失败处理方式不同，如何用 PostgreSQL 实现依赖编排？
```

```
日均任务量 50 万，单表已经出现领取延迟，如何分片扩展？
```

```
需要保障队列在主库故障时不中断，如何设计高可用方案？
```

Agent 会根据问题匹配对应的知识条目，输出"架构设计 → 配置示例 → 容量规划 → 上线检查 → 运维监控"五段式方案。

## 示例

### DAG 依赖表设计

```sql
CREATE TABLE job_dependencies (
    job_id UUID NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    depends_on_job_id UUID NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (job_id, depends_on_job_id)
);

CREATE INDEX idx_deps_on ON job_dependencies (depends_on_job_id);

-- 扇入检查函数：判断某任务的所有依赖是否已完成
CREATE OR REPLACE FUNCTION all_deps_completed(p_job_id UUID)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN NOT EXISTS (
        SELECT 1 FROM job_dependencies d
        JOIN jobs j ON j.id = d.depends_on_job_id
        WHERE d.job_id = p_job_id
          AND j.status != 'completed'
    );
END;
$$ LANGUAGE plpgsql;
```

### 多队列分片策略

```sql
-- 按 job_type 分表
CREATE TABLE jobs_email (...) INHERITS (jobs);
CREATE TABLE jobs_report (...) INHERITS (jobs);
CREATE TABLE jobs_cleanup (...) INHERITS (jobs);

-- 路由触发器
CREATE OR REPLACE FUNCTION route_job_by_type()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.job_type LIKE 'email_%' THEN
        INSERT INTO jobs_email VALUES (NEW.*);
    ELSIF NEW.job_type LIKE 'report_%' THEN
        INSERT INTO jobs_report VALUES (NEW.*);
    ELSIF NEW.job_type LIKE 'cleanup_%' THEN
        INSERT INTO jobs_cleanup VALUES (NEW.*);
    ELSE
        RETURN NEW;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_route_job
    BEFORE INSERT ON jobs
    FOR EACH ROW EXECUTE FUNCTION route_job_by_type();
```

### 死信队列表

```sql
CREATE TABLE dead_letter_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    original_job_id UUID NOT NULL,
    job_type VARCHAR(50) NOT NULL,
    data JSONB NOT NULL,
    attempts INT NOT NULL,
    last_error TEXT NOT NULL,
    failed_at TIMESTAMPTZ DEFAULT NOW(),
    reviewed_by VARCHAR(100),
    reviewed_at TIMESTAMPTZ,
    review_action VARCHAR(20),  -- 'retry' / 'discard' / 'fixed'
    review_note TEXT
);

-- 超过重试次数的任务自动转入死信队列
CREATE OR REPLACE FUNCTION move_to_dead_letter(p_job_id UUID)
RETURNS VOID AS $$
BEGIN
    INSERT INTO dead_letter_jobs (original_job_id, job_type, data, attempts, last_error)
    SELECT id, job_type, data, attempts, last_error
    FROM jobs WHERE id = p_job_id;

    DELETE FROM jobs WHERE id = p_job_id;
END;
$$ LANGUAGE plpgsql;
```

### Prometheus 监控指标

```sql
-- 暴露给 prometheus-postgres-exporter 的监控视图
CREATE VIEW queue_metrics AS
SELECT
    job_type,
    SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) AS pending_count,
    SUM(CASE WHEN status IN ('claimed', 'running') THEN 1 ELSE 0 END) AS running_count,
    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) AS failed_count,
    AVG(CASE WHEN status = 'completed'
        THEN EXTRACT(EPOCH FROM (completed_at - started_at))
        ELSE NULL END) AS avg_duration_sec,
    MAX(CASE WHEN status = 'pending'
        THEN EXTRACT(EPOCH FROM (NOW() - created_at))
        ELSE 0 END) AS oldest_pending_age_sec
FROM jobs
GROUP BY job_type;
```

## 最佳实践

### 实践一：DAG 编排避免循环依赖

任务依赖图必须是无环 DAG。在插入依赖关系时，应通过拓扑排序校验无环。建议在应用层实现环检测，避免死锁。

### 实践二：分片键选择遵循热点隔离

按 `job_type` 分片时，确保高吞吐的 `job_type` 独立成片，避免热点任务拖累其他任务。若某 `job_type` 仍超出单表承载，可按 `user_id` 哈希二次分片。

### 实践三：死信队列必须有人值守

死信队列不是垃圾箱，必须有明确的处理 SLA。建议配置告警，死信任务超过 10 条或 1 小时未处理即通知值班人员。

### 实践四：灰度发布按 Worker 版本标签路由

为新版本 Worker 打上版本标签（如 `v2`），通过 `claim_job_batch` 的 `p_worker_id` 参数控制路由。初期只让 10% 任务进入 v2 Worker，观察无异常后逐步放量。

### 实践五：主备切换需配合应用层重连

数据库主备切换时，应用层会经历短暂连接中断。Worker 需实现指数退避重连逻辑，并在重连后先执行超时回收，再恢复领取。

### 实践六：监控指标采集频率不低于 30 秒

队列状态变化快，30 秒以上的采集间隔可能漏掉短时尖峰。建议 Prometheus 采集间隔设为 15-30 秒，关键告警规则窗口设为 1-2 分钟。

### 实践七：容量规划预留 3 倍余量

按峰值任务量 × 3 规划数据库与 Worker 资源。大促、故障恢复等场景任务量可能瞬间飙升，3 倍余量是经过验证的安全水位。

## 错误处理

| 症状 | 可能原因 | 排查方法 | 对策 |
|:-----|:---------|:---------|:-----|
| DAG 任务卡住不执行 | 依赖任务未完成 | 查询 job_dependencies 表 | 修复依赖任务或人工标记完成 |
| 分片后吞吐未提升 | 分片不均或 Worker 未独立 | 查看各分片任务量与 Worker 配置 | 调整分片键或增加 Worker |
| 死信队列堆积 | 失败任务未处理 | 查看死信队列表与告警 | 分配值班人员处理 |
| 灰度发布后失败率上升 | 新版本逻辑缺陷 | 查看新 Worker 日志 | 一键回滚到旧版本 |
| 主备切换后任务丢失 | 切换期间未回收超时任务 | 查询超时任务 | 执行回收并补发丢失任务 |
| 监控指标缺失 | 视图未创建或权限不足 | 检查视图与 exporter 配置 | 创建视图并授予监控账号 |

## 常见问题

### Q1：DAG 编排如何处理条件分支？

条件分支建议在 Worker 业务逻辑中实现，而非在依赖图中硬编码。Worker 完成任务后根据结果决定插入哪些后续任务，依赖表只记录实际产生的依赖关系。

### Q2：分片后如何跨分片查询？

跨分片查询使用 `UNION ALL` 或父表查询（继承场景下父表自动包含所有子表数据）。但跨分片 JOIN 性能较差，建议尽量避免，或在应用层聚合。

### Q3：死信任务修复后如何重新入队？

在死信队列表中标记 `review_action = 'retry'`，由补偿任务将原任务数据重新插入 `jobs` 表，状态设为 `pending`，`attempts` 重置为 0。

### Q4：高可用方案中主备 Worker 如何避免重复领取？

主备 Worker 共享同一 `jobs` 表，依赖 `SKIP LOCKED` 保证不重复领取。主 Worker 故障后，备 Worker 自动接管，无需数据同步。

### Q5：灰度发布如何快速回滚？

将 `claim_job_batch` 的 `p_worker_id` 参数恢复为旧版本标签即可。已在执行中的新版本任务会继续完成，新领取的任务全部回到旧版本。

### Q6：监控告警阈值如何设置？

参考阈值：pending 堆积超过 1000、失败率超过 5%、Worker 离线超过 1 分钟、平均执行时长超过历史 P95 的 2 倍。具体阈值需结合业务 SLA 调整。

### Q7：容量规划如何评估数据库资源？

按"峰值任务量 × 平均负载大小 × 保留天数"估算存储空间。CPU 与内存按"峰值 QPS × 单任务平均耗时"估算并发连接数，再换算为实例规格。

### Q8：多团队共享队列如何隔离资源？

通过 `tenant_id` 字段逻辑隔离，配合配额表限制每个租户的最大并发数与日任务量。物理隔离可按租户分库，但运维成本更高。

### Q9：任务幂等性如何保障？

任务执行逻辑必须设计为幂等的，即重复执行不产生副作用。常见手段：唯一键去重、状态机校验、乐观锁更新。非幂等任务建议 `max_attempts = 1`。

### Q10：如何评估队列方案的性价比？

对比"单表队列 + 垂直扩展"与"分片队列 + 水平扩展"的总成本（数据库实例费 + Worker 实例费 + 运维人力费）。通常任务量 5000/秒是分水岭，低于此值单表更经济。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **数据库**: `PostgreSQL` 11+（需支持 SKIP LOCKED、JSONB、表继承、PL/pgSQL）
- **监控栈**: Prometheus + Grafana + postgres-exporter（可选但推荐）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| `PostgreSQL` 客户端 | 工具 | 必需 | psql / pgAdmin / DBeaver 等 |
| 数据库驱动 | 库 | 必需 | pgx (Go) / psycopg (Python) / node-postgres (Node.js) |
| Prometheus | 监控 | 推荐 | 官方下载或 Helm 部署 |
| Grafana | 可视化 | 推荐 | 官方下载或 Helm 部署 |
| 告警通知 | 服务 | 可选 | Slack / 钉钉 / 企业微信 Webhook |

### API Key 配置
- 本专业版为知识库型 Skill，自身不需要 API Key
- 若 Agent 需要连接实际数据库执行命令，相关凭据由用户自行配置于环境变量中
- 监控告警 Webhook URL 等敏感配置应存储于密钥管理服务中
- 禁止在 SKILL.md 或脚本中硬编码数据库凭据或 API Token

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分诊断功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent输出企业级队列架构方案

## 专业版特性

本专业版相比免费版新增以下能力：
- DAG 任务依赖编排：支持串行、并行、扇出、扇入四种模式，解决复杂任务编排难题
- 多队列水平分片：按 `job_type` 分表扩展，突破单表吞吐瓶颈
- 死信队列与人工补偿：失败任务自动归档，提供审核与重试流程
- 高可用与故障转移：主备 Worker 部署、数据库主备切换、自动恢复机制
- 灰度发布与版本回滚：基于 Worker 版本标签的灰度方案，一键回滚
- 高级监控告警体系：Prometheus 指标模板、Grafana 仪表盘、告警规则

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心队列设计 + 基础示例 | 个人试用、小型项目 |
| 收费专业版 | ¥49.9/月 | 全功能 + 企业级架构 + 优先支持 | 团队、企业级生产环境 |

专业版通过 SkillHub SkillPay 发布，享受 7×24 优先技术支持与季度架构评审服务。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
