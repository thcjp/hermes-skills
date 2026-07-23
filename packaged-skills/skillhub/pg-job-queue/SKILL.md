---
slug: "pg-job-queue"
name: "pg-job-queue"
version: "1.0.0"
displayName: "PG任务队列(专业版)"
summary: "基于`PostgreSQL`的企业级任务队列，支持DAG编排、分片扩展、死信队列与高可用方案。"
license: "Proprietary"
edition: "pro"
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
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# PG任务队列(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 环境配置与依赖管理
**输入**: 用户提供依赖说明所需的指令和必要参数。
**处理**: 解析依赖说明的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回依赖说明的处理结果,包含执行状态码、结果数据和执行日志。### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **数据库**: `PostgreSQL` 11+（需支持 SKIP LOCKED、JSONB、表继承、PL/pgSQL）
- **监控栈**: Prometheus + Grafana + postgres-exporter（可选但推荐）

**输入**: 用户提供运行环境所需的指令和必要参数。
**处理**: 解析运行环境的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| `PostgreSQL` 客户端 | 工具 | 必需 | psql / pgAdmin / DBeaver 等 |
| 数据库驱动 | 库 | 必需 | pgx (Go) / psycopg (Python) / node-postgres (Node.js) |
| Prometheus | 监控 | 推荐 | 官方下载或 Helm 部署 |
| Grafana | 可视化 | 推荐 | 官方下载或 Helm 部署 |
| 告警通知 | 服务 | 可选 | Slack / 钉钉 / 企业微信 Webhook |

**处理**: 解析第三方依赖的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回第三方依赖的处理结果,包含执行状态码、结果数据和执行日志。### API Key 配置
- 本专业版为知识库型 Skill，自身不需要 API Key
- 若 Agent 需要连接实际数据库执行命令，相关凭据由用户自行配置于环境变量中
- 监控告警 Webhook URL 等敏感配置应存储于密钥管理服务中
- 禁止在 SKILL.md 或脚本中硬编码数据库凭据或 API Token

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分诊断功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent输出企业级队列架构方案

**输入**: 用户提供可用性分类所需的指令和必要参数。
### 依赖项

针对依赖项,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供依赖项相关的配置参数、输入数据和处理选项。

**输出**: 返回依赖项的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`依赖项`的配置文档进行参数调优
#
## 适用场景

### 场景一：金融级批处理

每日凌晨的对账任务，涉及数据同步、对账计算、差异报告、告警通知四个阶段，任一阶段失败需人工介入。使用 DAG 编排 + 死信队列 + 全链路监控。

### 场景二：电商大促任务洪峰

双 11 期间任务量激增 10 倍，单表无法承载。按 `job_type` 分片到 4 张子表，每张表独立 Worker 池，整体吞吐提升 4 倍。

### 场景三：多团队共享队列平台

公司内多个业务线共用一套队列基础设施。通过命名空间隔离、配额管理、优先级抢占机制，保障关键业务不被低优先级任务挤占。

### 场景四：跨集群任务迁移

集群迁移期间，新旧集群并行运行，任务需逐步从旧集群切到新集群。通过灰度发布机制，按比例将任务路由到新集群，异常时一键回滚。

## 使用流程

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

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | pg-job-queue处理的内容输入 |,  |
| content | string | 否 | pg-job-queue处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "queue 相关配置参数",
    result: "queue 相关配置参数",
    result: "queue 相关配置参数",
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

| 错误场景 | 可能原因 | 排查方法 | 处理方式 |
|:-----|:---------|:---------|:-----|
| DAG 任务卡住不执行 | 依赖任务未完成 | 查询 job_dependencies 表 | 修复依赖任务或人工标记完成 |
| 分片后吞吐未提升 | 分片不均或 Worker 未独立 | 查看各分片任务量与 Worker 配置 | 调整分片键或增加 Worker |
| 死信队列堆积 | 失败任务未处理 | 查看死信队列表与告警 | 分配值班人员处理 |
| 灰度发布后失败率上升 | 新版本逻辑缺陷 | 查看新 Worker 日志 | 一键回滚到旧版本 |
| 主备切换后任务丢失 | 切换期间未回收超时任务 | 查询超时任务 | 执行回收并补发丢失任务 |
| 监控指标缺失 | 视图未创建或权限不足 | 检查视图与 exporter 配置 | 创建视图并授予监控账号 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 无需API Key(本地LLM);如使用云端LLM,通过对应平台官网注册获取,配置为环境变量 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding
### 运行环境与依赖
- **运行环境**: Windows/macOS/Linux,Agent平台环境
- **可用性分类**: MD(纯Markdown指令) + EXEC(需要命令行执行)


## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

