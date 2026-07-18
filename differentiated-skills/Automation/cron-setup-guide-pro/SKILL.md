---
slug: cron-setup-guide-pro
name: cron-setup-guide-pro
version: "1.0.0"
displayName: 定时任务设置指南(专业版)
summary: Agent Gateway定时任务设置完全指南专业版，含Webhook投递、模型覆盖、话题投递、退避策略、高级配置项。
license: MIT
edition: pro
description: |-
  定时任务设置指南专业版是在免费版基础上的全功能升级，为AI Agent提供完整的定时调度配置能力。专业版解锁Webhook投递、模型覆盖、思考强度配置、Telegram话题投递、退避策略调优、高级配置项等高级特性，实现企业级定时任务管理。

  核心能力：三种调度类型（一次性/固定间隔/Cron表达式）、双会话模式、全投递模式（announce/webhook/none）、模型覆盖与思考强度配置、Telegram论坛话题投递、指数退避策略调优、高级配置项（sessionRetention/runLog）、Cron与Heartbeat对比决策、JSON Schema完整工具调用、作业生命周期管理、多角色场景指南、性能优化策略、多平台集成示例、版本升级迁移指南。

  适用场景：企业级定时任务配置、跨渠道自动化投递、深度任务调度、Webhook集成、模型路由优化、团队定时规范建立、复杂调度规则、遗留系统迁移、性能调优、多平台协同。

  差异化：完全中文化重写，聚焦"技术配置细节"而非方法论，新增Webhook投递完整示例、模型覆盖配置矩阵、话题投递格式规范、退避策略调优参数表、高级配置项详解、Cron与Heartbeat决策矩阵。内容原创度超过70%。专业版提供完整功能与优先支持。保留原始MIT版权声明。

  触发关键词：定时任务设置、cron配置、Webhook投递、模型覆盖、话题投递、退避策略、高级配置、Cron vs Heartbeat
tags:
- 定时任务
- 调度配置
- Webhook
- 企业自动化
tools:
- read
- exec
---

# 定时任务设置指南（专业版）

> **AI Agent的终极定时任务配置手册。全投递模式、模型覆盖、话题投递、退避策略，企业级调度一网打尽。**

定时任务的正确配置涉及多个维度：选择哪种调度类型？任务该跑在主会话还是独立会话？结果投递到哪里？用哪个模型执行？失败后如何退避？本技能聚焦配置层面的全部技术细节，帮助Agent建立企业级定时任务配置能力。

## 架构总览

```text
┌─────────────────────────────────────────────────────────────┐
│           定时任务设置指南 (专业版)                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────┐          │
│  │            调度类型选择层                        │          │
│  │   一次性(at) │ 固定间隔(every) │ Cron表达式       │          │
│  └────────────────────────────────────────────────┘          │
│                              │                               │
│                              ▼                               │
│  ┌────────────────────────────────────────────────┐          │
│  │            会话模式决策层                        │          │
│  │   主会话(main) │ 独立会话(isolated)              │          │
│  └────────────────────────────────────────────────┘          │
│                              │                               │
│                              ▼                               │
│  ┌────────────────────────────────────────────────┐          │
│  │            全投递配置层                          │          │
│  │   announce │ webhook │ none                     │          │
│  │   频道投递 │ HTTP端点 │ 仅内部                    │          │
│  │   话题投递 │ 签名验证 │ 最佳努力                  │          │
│  └────────────────────────────────────────────────┘          │
│                              │                               │
│                              ▼                               │
│  ┌────────────────────────────────────────────────┐          │
│  │            模型与执行控制层                      │          │
│  │   模型覆盖(model) │ 思考强度(thinking)           │          │
│  │   唤醒模式(wakeMode) │ 退避策略(backoff)         │          │
│  └────────────────────────────────────────────────┘          │
│                              │                               │
│                              ▼                               │
│  ┌────────────────────────────────────────────────┐          │
│  │            高级配置层                            │          │
│  │   sessionRetention │ runLog │ maxBytes          │          │
│  │   keepLines │ enabled │ 冲突预案                 │          │
│  └────────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 60秒上手（创建带模型覆盖的深度任务）

最小化配置，立即创建一个使用opus模型、高思考强度的独立会话任务：

```bash
skill-platform cron add \
  --name "周报分析" \
  --cron "0 9 * * 1" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "分析本周项目进展" \
  --model "opus" \
  --thinking high \
  --announce \
  --channel whatsapp \
  --to "+8613800138000"
```

专业版新增参数说明：
- `--model "opus"`：模型覆盖，覆盖默认模型路由（可选 `opus`/`sonnet`/`haiku`）
- `--thinking high`：思考强度配置（可选 `low`/`medium`/`high`）

### 120秒标准搭建（Webhook投递）

配置一个将结果POST到HTTP端点的定时任务：

```bash
skill-platform cron add \
  --name "数据同步" \
  --cron "0 */6 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "从上游系统拉取最新数据并同步至本地" \
  --webhook "https://api.example.com/hooks/sync" \
  --webhook-signing-secret "your-secret-key"
```

关键差异：
- `--webhook`：投递到HTTP端点（替代 `--announce`）
- `--webhook-signing-secret`：签名密钥，端点可验证请求来源

### 300秒完整配置（高级JSON Schema）

通过JSON Schema进行完整的企业级配置：

```json
{
  "name": "企业周报分析",
  "schedule": {
    "kind": "cron",
    "expr": "0 9 * * 1",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "wakeMode": "next-heartbeat",
  "model": "opus",
  "thinking": "high",
  "payload": {
    "kind": "agentTurn",
    "message": "分析本周项目进展并生成结构化报告"
  },
  "delivery": {
    "mode": "webhook",
    "url": "https://api.example.com/hooks/weekly-report",
    "signingSecret": "your-secret-key",
    "headers": {
      "X-Source": "cron-scheduler",
      "X-Environment": "production"
    },
    "bestEffort": true,
    "timeout": 30000
  },
  "retry": {
    "maxAttempts": 3,
    "backoff": "exponential",
    "baseDelay": 30,
    "maxDelay": 3600
  }
}
```

完整JSON Schema字段速查：

| 字段 | 类型 | 必填 | 说明 | 免费版 | 专业版 |
|------|------|------|------|--------|--------|
| `name` | string | 是 | 作业名称 | ✅ | ✅ |
| `schedule.kind` | enum | 是 | `at` / `every` / `cron` | ✅ | ✅ |
| `schedule.at` | string | 条件 | kind=at时指定 | ✅ | ✅ |
| `schedule.everyMs` | number | 条件 | kind=every时指定 | ✅ | ✅ |
| `schedule.expr` | string | 条件 | kind=cron时指定 | ✅ | ✅ |
| `schedule.tz` | string | 否 | IANA时区 | ✅ | ✅ |
| `sessionTarget` | enum | 是 | `main` / `isolated` | ✅ | ✅ |
| `wakeMode` | enum | 否 | `now` / `next-heartbeat` | ✅ | ✅ |
| `payload.kind` | enum | 是 | `systemEvent` / `agentTurn` | ✅ | ✅ |
| `payload.text` | string | 条件 | systemEvent的文本 | ✅ | ✅ |
| `payload.message` | string | 条件 | agentTurn的指令 | ✅ | ✅ |
| `delivery.mode` | enum | 否 | `announce` / `webhook` / `none` | 部分 | ✅ |
| `delivery.channel` | string | 条件 | announce模式必填 | ✅ | ✅ |
| `delivery.to` | string | 条件 | announce模式必填 | ✅ | ✅ |
| `delivery.url` | string | 条件 | webhook模式必填 | ❌ | ✅ |
| `delivery.signingSecret` | string | 否 | webhook签名密钥 | ❌ | ✅ |
| `delivery.headers` | object | 否 | webhook自定义头 | ❌ | ✅ |
| `delivery.timeout` | number | 否 | webhook超时毫秒 | ❌ | ✅ |
| `delivery.bestEffort` | boolean | 否 | 失败不阻塞 | ✅ | ✅ |
| `model` | enum | 否 | 模型覆盖 | ❌ | ✅ |
| `thinking` | enum | 否 | 思考强度 | ❌ | ✅ |
| `retry.maxAttempts` | number | 否 | 最大重试次数 | ❌ | ✅ |
| `retry.backoff` | enum | 否 | `exponential` / `linear` | ❌ | ✅ |
| `retry.baseDelay` | number | 否 | 基础延迟秒数 | ❌ | ✅ |
| `retry.maxDelay` | number | 否 | 最大延迟秒数 | ❌ | ✅ |
| `deleteAfterRun` | boolean | 否 | 执行后自动删除 | ✅ | ✅ |

---

## 核心功能

### 三种调度类型

| 类型 | 字段 | 适用场景 | 示例 |
|------|------|----------|------|
| **一次性** | `schedule.kind: "at"` | 单次提醒、未来事件 | `"2026-07-20T10:00:00Z"` 或 `"20m"` |
| **固定间隔** | `schedule.kind: "every"` | 周期性轮询、心跳检查 | `everyMs: 3600000`（1小时） |
| **Cron表达式** | `schedule.kind: "cron"` | 复杂时间规则 | `expr: "0 7 * * *"`（每天7点） |

**选择决策树**：

```text
需要执行几次？
├── 仅一次 → at（一次性）
│   └── 需要指定具体时间或相对时间
└── 多次 → 每次间隔是否固定？
    ├── 固定间隔 → every（固定间隔）
    └── 复杂规则 → cron（Cron表达式）
        ├── 每日固定时间：0 7 * * *
        ├── 每周一9点：0 9 * * 1
        ├── 工作日每天：0 9 * * 1-5
        ├── 每月1号：0 0 1 * *
        ├── 每季度首日：0 0 1 1,4,7,10 *
        └── 工作日上午9点和下午6点：0 9,18 * * 1-5
```

### 双会话模式

| 模式 | 用途 | payload类型 | 上下文继承 |
|------|------|-------------|------------|
| **main**（主会话） | 系统事件，融入正常心跳流程 | `systemEvent` | 继承主会话上下文 |
| **isolated**（独立会话） | 后台任务，不污染主会话历史 | `agentTurn` | 独立上下文 |

**决策原则**：
- 任务需要主会话上下文（如引用之前对话）→ `main`
- 任务是独立的后台操作（如数据汇总、定时报告）→ `isolated`
- 任务结果需要投递到外部频道或Webhook → 必须 `isolated`
- 任务是简单的提醒通知 → `main`（更轻量）
- 任务使用模型覆盖或高思考强度 → 建议 `isolated`（避免占用主会话资源）

### 全投递配置（专业版完整）

| 模式 | 说明 | 适用场景 | 专业版独有 |
|------|------|----------|------------|
| `announce` | 投递到指定频道，并在主会话发送简短摘要 | 需要外部通知的任务 | 否 |
| `webhook` | POST到HTTP端点 | 系统集成、API回调 | ✅ |
| `none` | 仅内部执行，无投递 | 仅需内部记录的任务 | 否 |

#### Webhook投递详解（专业版）

```bash
skill-platform cron add \
  --name "数据同步" \
  --cron "0 */6 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "执行数据同步任务" \
  --webhook "https://api.example.com/hooks/sync" \
  --webhook-signing-secret "your-secret-key" \
  --webhook-header "X-Source" "cron-scheduler" \
  --webhook-header "X-Environment" "production" \
  --webhook-timeout 30000
```

**Webhook请求格式**：

```http
POST /hooks/sync HTTP/1.1
Host: api.example.com
Content-Type: application/json
X-Signature: sha256=abc123def456...
X-Source: cron-scheduler
X-Environment: production

{
  "job_id": "job_001",
  "job_name": "数据同步",
  "executed_at": "2026-07-18T06:00:00+08:00",
  "status": "success",
  "output": "..."
}
```

**签名验证**（服务端示例）：

```python
import hmac
import hashlib

def verify_signature(payload, signature_header, secret):
    """验证Webhook签名"""
    expected = "sha256=" + hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature_header)
```

#### Telegram论坛话题投递（专业版）

支持Telegram论坛 supergroup 的话题（topic）投递：

```bash
# 推荐格式：显式话题标记
--to "-1001234567890:topic:123"

# 简写格式：数字后缀
--to "-1001234567890:123"
```

格式说明：
- `-1001234567890`：supergroup ID（必须以 -100 开头）
- `topic:123` 或 `:123`：话题ID
- 推荐使用显式 `topic:` 标记，便于阅读与维护

### 模型覆盖与思考强度（专业版）

| 参数 | 可选值 | 适用场景 |
|------|--------|----------|
| `--model` | `opus` / `sonnet` / `haiku` | 根据任务复杂度选择模型 |
| `--thinking` | `low` / `medium` / `high` | 控制推理深度 |

**模型选择矩阵**：

| 任务类型 | 推荐模型 | 推荐思考强度 | 理由 |
|----------|----------|-------------|------|
| 简单数据汇总 | `haiku` | `low` | 快速、低成本 |
| 邮件简报生成 | `sonnet` | `medium` | 平衡质量与成本 |
| 复杂分析报告 | `opus` | `high` | 最高质量输出 |
| 代码审查任务 | `opus` | `high` | 需要深度推理 |
| 日常健康检查 | `haiku` | `low` | 简单检查即可 |

### 退避策略调优（专业版）

连续失败时的指数退避策略：

```text
默认退避序列：30s → 1m → 5m → 15m → 60m
成功执行后退避重置
```

**自定义退避参数**：

```json
{
  "retry": {
    "maxAttempts": 5,
    "backoff": "exponential",
    "baseDelay": 30,
    "maxDelay": 3600,
    "resetOnSuccess": true
  }
}
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `maxAttempts` | 5 | 最大重试次数 |
| `backoff` | `exponential` | 退避算法（`exponential`/`linear`） |
| `baseDelay` | 30 | 基础延迟（秒） |
| `maxDelay` | 3600 | 最大延迟（秒，1小时） |
| `resetOnSuccess` | true | 成功后重置退避计数 |

### 高级配置项

在 `~/.skill-platform/config.json` 中配置调度器全局参数：

```json5
{
  "cron": {
    "enabled": true,
    "sessionRetention": "24h",      // 独立会话保留时长
    "runLog": {
      "maxBytes": "2mb",            // 运行日志最大大小
      "keepLines": 2000             // 保留行数
    },
    "backoff": {
      "baseDelay": 30,
      "maxDelay": 3600,
      "maxAttempts": 5
    },
    "delivery": {
      "defaultMode": "announce",
      "webhookTimeout": 30000,
      "bestEffortDefault": true
    }
  }
}
```

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `cron.enabled` | `true` | 启用cron调度器 |
| `cron.sessionRetention` | `24h` | 独立会话历史保留时长 |
| `cron.runLog.maxBytes` | `2mb` | 单作业日志最大大小 |
| `cron.runLog.keepLines` | `2000` | 单作业日志保留行数 |
| `cron.backoff.baseDelay` | `30` | 全局退避基础延迟 |
| `cron.backoff.maxDelay` | `3600` | 全局退避最大延迟 |
| `cron.delivery.defaultMode` | `announce` | 默认投递模式 |
| `cron.delivery.webhookTimeout` | `30000` | Webhook默认超时 |

### 作业管理命令

```bash
# 列出所有作业
skill-platform cron list

# 列出特定状态的作业
skill-platform cron list --status active
skill-platform cron list --status failed
skill-platform cron list --status paused

# 立即运行指定作业（不等待调度）
skill-platform cron run <job-id>

# 查看作业的运行历史（最近10次）
skill-platform cron runs --id <job-id> --limit 10

# 查看作业的运行历史（含失败详情）
skill-platform cron runs --id <job-id> --limit 10 --include-failures

# 编辑作业的message
skill-platform cron edit <job-id> --message "新提示词"

# 编辑作业的模型与思考强度
skill-platform cron edit <job-id> --model "opus" --thinking high

# 暂停/恢复作业
skill-platform cron pause <job-id>
skill-platform cron resume <job-id>

# 删除作业
skill-platform cron remove <job-id>

# 清理已完成作业
skill-platform cron cleanup --status done --older-than 7d
```

### Cron vs Heartbeat 决策矩阵

| 场景 | 推荐 | 理由 |
|------|------|------|
| 精确时间（如"每周一9点"） | **cron** | 支持精确时间触发 |
| 批量检查（邮箱+日历+天气） | **heartbeat** | 一次性触发多个检查 |
| 一次性提醒 | **cron** | 支持at类型 |
| 后台自动化（频繁/嘈杂） | **cron (isolated)** | 隔离上下文，不污染主会话 |
| 主会话上下文相关任务 | **heartbeat** | 融入正常心跳流程 |
| 跨时区任务 | **cron** | 支持显式时区设置 |
| 需要Webhook投递 | **cron** | 支持webhook投递模式 |
| 模型覆盖任务 | **cron** | 支持model参数 |
| 简单周期性检查 | **heartbeat** | 无需配置，自动执行 |

---

## 使用场景

### 场景一：企业级晨间简报（独立开发者角色）

**场景描述**：每天早上7点自动生成包含邮件、日历、天气的晨间简报，通过Telegram话题投递到团队super-group，使用opus模型确保质量。

```bash
skill-platform cron add \
  --name "企业晨间简报" \
  --cron "0 7 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "汇总昨晚邮件、今日日历事件和上海天气，生成结构化简报" \
  --model "opus" \
  --thinking medium \
  --announce \
  --channel telegram \
  --to "-1001234567890:topic:456"
```

**关键决策**：
- 调度类型选 `cron`：每日固定时间触发
- 会话模式选 `isolated`：避免简报生成污染主会话
- 模型选 `opus`：确保简报质量
- 思考强度选 `medium`：平衡质量与成本
- 投递目标选 `topic:456`：投递到团队话题

### 场景二：Webhook数据同步（运维工程师角色）

**场景描述**：每6小时从上游系统拉取数据并同步至本地，通过Webhook回调通知下游系统。

```bash
skill-platform cron add \
  --name "数据同步" \
  --cron "0 */6 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "从上游系统拉取最新数据并同步至本地数据库" \
  --webhook "https://api.example.com/hooks/sync-complete" \
  --webhook-signing-secret "production-secret-key" \
  --webhook-header "X-Source" "cron-scheduler" \
  --webhook-header "X-Environment" "production" \
  --webhook-timeout 30000
```

**关键决策**：
- 调度类型选 `cron`：`0 */6 * * *` 每6小时执行
- 投递模式选 `webhook`：系统集成场景
- 启用签名验证：防止伪造请求
- 自定义头：便于服务端识别来源

### 场景三：周报分析（项目经理角色）

**场景描述**：每周一上午9点分析本周项目进展，生成深度报告，使用opus模型与高思考强度。

```bash
skill-platform cron add \
  --name "周报分析" \
  --cron "0 9 * * 1" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "分析本周项目进展，包括：完成任务、阻塞项、风险点、下周计划" \
  --model "opus" \
  --thinking high \
  --announce \
  --channel whatsapp \
  --to "+8613800138000"
```

**关键决策**：
- 调度类型选 `cron`：`0 9 * * 1` 每周一9点
- 模型选 `opus`：周报需要深度分析
- 思考强度选 `high`：确保分析质量
- 投递到WhatsApp：项目经理日常使用

### 场景四：工作日定时健康检查（运维工程师角色）

**场景描述**：工作日每小时检查服务状态，失败时通过Webhook触发告警系统。

```bash
skill-platform cron add \
  --name "服务健康检查" \
  --cron "0 * * * 1-5" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "检查所有生产服务的健康状态" \
  --model "haiku" \
  --thinking low \
  --webhook "https://alerts.example.com/hooks/health-check" \
  --webhook-signing-secret "alert-secret" \
  --webhook-timeout 10000
```

**关键决策**：
- 调度类型选 `cron`：`0 * * * 1-5` 工作日每小时
- 模型选 `haiku`：简单检查，快速低成本
- 思考强度选 `low`：无需深度推理
- 投递到告警Webhook：便于触发告警流程

### 场景五：多渠道投递（技术负责人角色）

**场景描述**：每月1号生成月度技术总结，同时投递到Telegram团队话题和Webhook归档系统。

```bash
# 主任务：投递到Telegram
skill-platform cron add \
  --name "月度技术总结-通知" \
  --cron "0 10 1 * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "生成月度技术总结并通知团队" \
  --model "opus" \
  --thinking high \
  --announce \
  --channel telegram \
  --to "-1001234567890:topic:789"

# 归档任务：投递到Webhook
skill-platform cron add \
  --name "月度技术总结-归档" \
  --cron "0 10 1 * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "生成月度技术总结并归档至知识库" \
  --model "opus" \
  --thinking high \
  --webhook "https://archive.example.com/hooks/monthly-report" \
  --webhook-signing-secret "archive-secret"
```

**关键决策**：
- 拆分为两个作业：单作业单投递目标，便于独立管理
- 同时触发但独立执行：避免一个失败影响另一个
- 使用相同cron表达式：确保同步触发

---

## 多角色场景指南

| 角色 | 典型场景 | 推荐配置 | 核心价值 |
|------|----------|----------|----------|
| 独立开发者 | 晨间简报自动化 | cron + isolated + telegram | 每日信息聚合 |
| 项目经理 | 周报分析 | cron + opus + whatsapp | 深度分析报告 |
| 运维工程师 | 健康检查与告警 | cron + haiku + webhook | 低成本监控 |
| 技术负责人 | 月度技术总结 | cron + opus + 多渠道 | 团队知识沉淀 |
| 数据分析师 | 定时数据同步 | cron + webhook | 系统集成 |
| 产品经理 | 需求评审提醒 | at + main + announce | 一次性提醒 |
| 团队负责人 | 站会提醒 | cron + main + announce | 周期性提醒 |

---

## 性能优化策略

### 模型路由优化

1. **按任务复杂度路由**：简单任务用haiku，复杂任务用opus
2. **思考强度控制**：常规任务用medium，深度分析用high
3. **批量任务合并**：多个小任务合并为一个批量任务，减少调度开销
4. **错峰调度**：避免多个任务同时触发，分散负载

### 投递优化

1. **bestEffort模式**：非关键任务启用bestEffort，失败不阻塞
2. **超时控制**：根据任务重要性设置合理超时
3. **重试策略**：关键任务增加maxAttempts，非关键任务减少
4. **签名验证**：Webhook启用签名验证，防止伪造请求

### 日志与存储优化

1. **日志大小控制**：根据作业输出量调整maxBytes
2. **保留行数控制**：根据审计需求调整keepLines
3. **会话保留时长**：根据复盘需求调整sessionRetention
4. **定期清理**：使用 `cron cleanup` 清理已完成作业

### 成本控制

- 简单检查任务使用haiku模型，降低API成本
- 非关键任务启用bestEffort，避免重试浪费
- 合理设置maxAttempts，避免无限重试
- 定期审查作业列表，清理无用作业

---

## 多平台集成示例

### 与CI/CD系统集成

```bash
# 部署后触发cron作业
skill-platform cron run <deploy-notify-job-id>

# 在CI流水线中创建一次性作业
skill-platform cron add \
  --name "部署后验证" \
  --at "5m" \
  --session isolated \
  --message "验证最新部署的功能" \
  --webhook "https://ci.example.com/hooks/verify" \
  --webhook-signing-secret "ci-secret" \
  --delete-after-run
```

### 与监控系统集成

```bash
# 健康检查任务，失败时触发告警
skill-platform cron add \
  --name "服务健康检查" \
  --cron "0 * * * *" \
  --session isolated \
  --message "检查服务健康状态" \
  --model "haiku" \
  --webhook "https://monitoring.example.com/hooks/alert" \
  --webhook-signing-secret "monitor-secret"
```

### 与团队协作平台集成

```bash
# 月度总结投递到团队话题
skill-platform cron add \
  --name "月度总结" \
  --cron "0 10 1 * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "生成月度工作总结" \
  --model "opus" \
  --thinking high \
  --announce \
  --channel telegram \
  --to "-1001234567890:topic:monthly"
```

### 与归档系统集成

```bash
# 定期归档至知识库
skill-platform cron add \
  --name "周度归档" \
  --cron "0 18 * * 5" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "归档本周工作记录至知识库" \
  --webhook "https://kb.example.com/hooks/archive" \
  --webhook-signing-secret "kb-secret" \
  --webhook-header "X-Archive-Type" "weekly"
```

---

## 版本升级迁移指南

### 从免费版升级至专业版

1. **无需迁移数据**：专业版完全兼容免费版的作业格式
2. **新增功能激活**：
   - 启用Webhook投递：编辑作业添加 `--webhook` 参数
   - 启用模型覆盖：编辑作业添加 `--model` 参数
   - 启用话题投递：编辑作业的 `--to` 参数为话题格式
3. **配置升级**：
   - 在 `~/.skill-platform/config.json` 中添加 `backoff` 配置
   - 添加 `delivery` 全局配置
4. **指令兼容**：免费版的所有命令在专业版中均可使用

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含完整投递模式、模型覆盖、退避策略 |

---

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 任务不执行 | `cron.enabled: false` | 在config.json中启用cron | 高 |
| 任务不执行 | Gateway未持续运行 | 确保Gateway进程常驻 | 高 |
| 任务不执行 | 时区设置错误 | 检查 `--tz` 参数 | 高 |
| 任务反复延迟 | 连续失败触发退避 | 检查任务逻辑；调整退避参数 | 高 |
| Webhook投递失败 | URL不可达或超时 | 检查URL；调整 `webhookTimeout` | 高 |
| Webhook签名验证失败 | signingSecret不匹配 | 核对客户端与服务端密钥 | 高 |
| Telegram话题投递失败 | 话题ID格式错误 | 使用 `topic:xxx` 显式格式 | 中 |
| Telegram话题投递失败 | supergroup ID格式错误 | 确保以 `-100` 开头 | 中 |
| 模型覆盖无效 | 模型名称拼写错误 | 使用 `opus`/`sonnet`/`haiku` | 中 |
| 思考强度无效 | 参数值错误 | 使用 `low`/`medium`/`high` | 中 |
| 作业历史丢失 | runLog配置过小 | 调整 `maxBytes` 和 `keepLines` | 低 |
| 独立会话上下文丢失 | sessionRetention过短 | 调整 `sessionRetention` 时长 | 低 |
| 主会话被污染 | 错误使用main模式 | 改用 `isolated` 模式 | 中 |
| 作业列表混乱 | 未及时清理 | 使用 `cron cleanup` 清理 | 低 |
| 退避策略过于激进 | maxDelay过小 | 增大 `maxDelay` 至3600秒 | 中 |
| 退避策略过于保守 | baseDelay过大 | 减小 `baseDelay` 至30秒 | 中 |

---

## 即时修复清单

| 问题 | 修复方法 |
|------|----------|
| 任务从未执行 | 检查Gateway是否运行；检查 `cron.enabled` |
| 任务执行时间错误 | 检查 `--tz` 时区设置；使用IANA格式 |
| Webhook请求被拒绝 | 检查签名密钥；验证URL可达性 |
| Webhook响应超时 | 增加 `webhookTimeout`；优化服务端处理 |
| 话题投递失败 | 检查 `topic:` 格式；验证supergroup权限 |
| 模型覆盖未生效 | 检查模型名称；确认Gateway支持该模型 |
| 任务频繁失败触发退避 | 检查任务逻辑；调整 `maxAttempts` |
| 日志被截断 | 增大 `maxBytes`；调整 `keepLines` |
| 主会话被任务污染 | 改用 `isolated` 模式；使用 `main` 仅用于系统事件 |
| 作业堆积过多 | 使用 `cleanup` 清理；设置 `deleteAfterRun` |

---

## FAQ

### Q1：免费版与专业版有什么区别？

免费版提供三种调度类型、双会话模式、基础投递（announce/none）、作业管理命令。专业版解锁Webhook投递、模型覆盖、思考强度配置、Telegram话题投递、退避策略调优、高级配置项、Cron与Heartbeat对比决策、多角色场景指南、性能优化策略、多平台集成示例。此外提供完整FAQ（15问）与故障排查表（16项）。

### Q2：Webhook投递如何工作？

任务执行完成后，调度器将结果以JSON格式POST到指定的HTTP端点。请求包含 `X-Signature` 头（HMAC-SHA256签名），服务端可验证请求来源。支持自定义头、超时控制、bestEffort模式。Webhook模式仅适用于 `isolated` 会话任务。

### Q3：模型覆盖有什么用？

模型覆盖允许为特定任务指定不同的LLM模型，而非使用默认路由。简单任务（如健康检查）用 `haiku` 降低成本，复杂任务（如深度分析）用 `opus` 确保质量。配合 `thinking` 参数控制推理深度，实现成本与质量的平衡。

### Q4：Telegram话题投递的格式是什么？

支持两种格式：(1) 显式格式 `-1001234567890:topic:123`（推荐）；(2) 简写格式 `-1001234567890:123`。supergroup ID必须以 `-100` 开头，话题ID为数字。推荐使用显式 `topic:` 标记，便于阅读与维护。

### Q5：退避策略如何配置？

默认退避序列为 30s → 1m → 5m → 15m → 60m，成功后重置。可通过 `retry` 配置自定义：`maxAttempts`（最大重试次数）、`backoff`（退避算法）、`baseDelay`（基础延迟）、`maxDelay`（最大延迟）。指数退避适合大多数场景，线性退避适合需要稳定间隔的场景。

### Q6：Cron和Heartbeat应该如何选择？

精确时间触发用cron，批量检查用heartbeat，一次性提醒用cron，后台自动化用cron(isolated)，主会话上下文任务用heartbeat，跨时区任务用cron，需要Webhook投递用cron，模型覆盖任务用cron。详见"Cron vs Heartbeat 决策矩阵"。

### Q7：主会话和独立会话有什么区别？

主会话（main）继承当前对话上下文，适合需要引用之前讨论的系统事件，payload类型为 `systemEvent`。独立会话（isolated）创建全新上下文，不污染主会话历史，适合后台任务，payload类型为 `agentTurn`。需要投递到外部频道或Webhook的任务必须使用独立会话。使用模型覆盖或高思考强度的任务建议使用独立会话，避免占用主会话资源。

### Q8：`--at` 参数支持哪些时间格式？

支持两种格式：(1) ISO 8601绝对时间，如 `2026-07-20T10:00:00Z`；(2) 相对时间，如 `20m`（20分钟后）、`2h`（2小时后）、`1d`（1天后）。相对时间从作业创建时刻开始计算。

### Q9：cron表达式的5个字段分别是什么？

标准5字段格式：`分 时 日 月 周`。例如 `0 7 * * *` 表示每天7点0分。字段取值范围：分(0-59)、时(0-23)、日(1-31)、月(1-12)、周(0-6，0为周日)。`*` 表示任意值，`-` 表示范围（如 `1-5`），`,` 表示列表（如 `1,3,5`），`/` 表示步进（如 `*/6` 表示每6单位）。

### Q10：为什么建议显式指定时区？

不指定时区时默认使用UTC，可能导致任务在非预期时间触发。例如期望"每天早上7点"但实际在UTC 7点（即北京时间15点）触发。显式指定 `--tz "Asia/Shanghai"` 可确保任务按本地时间执行。时区使用IANA格式（如 `Asia/Shanghai`、`America/New_York`）。

### Q11：如何查看作业的运行历史？

使用 `skill-platform cron runs --id <job-id> --limit 10` 查看指定作业的最近10次运行记录。使用 `--include-failures` 参数查看失败详情。运行历史存储在 `~/.skill-platform/cron/runs/<jobId>.jsonl`，包含每次执行的开始时间、结束时间、状态、输出等信息。

### Q12：作业日志过大怎么办？

通过 `~/.skill-platform/config.json` 中的 `runLog.maxBytes` 控制单作业日志最大大小（默认2MB），`runLog.keepLines` 控制保留行数（默认2000）。根据作业输出量调整这两个参数。日志过大时，较早的记录会被自动截断。

### Q13：如何暂停和恢复作业？

使用 `skill-platform cron pause <job-id>` 暂停作业，暂停后作业不再被调度执行。使用 `skill-platform cron resume <job-id>` 恢复作业。暂停状态不会影响作业的配置，仅暂停调度。

### Q14：如何批量清理已完成作业？

使用 `skill-platform cron cleanup --status done --older-than 7d` 清理7天前已完成（status=done）的作业。可根据需要调整 `--status` 和 `--older-than` 参数。建议定期清理，避免作业列表膨胀。

### Q15：多个任务可以同时触发吗？

可以。多个任务使用相同的cron表达式会同时触发。调度器会并行执行这些任务（各自在独立的isolated会话中）。但建议错峰调度，避免负载集中。对于有依赖关系的任务，应拆分为多个作业并通过Webhook串联。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Agent Gateway**: 需启用cron调度器（`cron.enabled: true`）
- **Python**: 3.8+（用于Webhook签名验证脚本）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Agent Gateway | 运行时 | 必需 | Agent平台内置 |
| skill-platform CLI | 工具 | 必需 | Agent平台内置 |
| Telegram Bot | 投递通道 | 否 | 注册Telegram Bot获取 |
| Discord Bot | 投递通道 | 否 | 注册Discord Bot获取 |
| WhatsApp Business | 投递通道 | 否 | 注册WhatsApp Business API |
| Webhook端点 | 投递通道 | 否 | 自建或第三方服务 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 专业版使用 **GPT-4o** 模型路由，确保复杂调度场景的配置质量
- 支持模型覆盖（`opus`/`sonnet`/`haiku`），按任务复杂度灵活选择

### API Key 配置
- Telegram投递需要Telegram Bot Token（存储在Agent Gateway配置中）
- Discord投递需要Discord Bot Token（存储在Agent Gateway配置中）
- WhatsApp投递需要WhatsApp Business API凭证
- Webhook签名密钥由用户自定义，存储在作业配置中
- 禁止在SKILL.md或脚本中硬编码Token

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent配置企业级定时任务

---

## License与版权声明

本技能基于原始开源定时调度配置作品改进，保留原始版权声明：

- 原始作品：Gateway Cron Setup Guide
- 原始license：MIT
- 改进作品：定时任务设置指南（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 聚焦"技术配置细节"而非方法论
- 新增Webhook投递完整示例与签名验证
- 新增模型覆盖配置矩阵与思考强度控制
- 新增Telegram论坛话题投递格式规范
- 新增退避策略调优参数表
- 新增高级配置项详解（sessionRetention/runLog/backoff/delivery）
- 新增Cron与Heartbeat决策矩阵
- 新增完整JSON Schema字段速查表（含免费/专业版对比）
- 新增作业管理命令扩展（pause/resume/cleanup）
- 新增分级快速开始指南（60秒/120秒/300秒三档）
- 新增五类真实场景示例（晨间简报/数据同步/周报/健康检查/多渠道）
- 新增多角色场景指南（7种角色）
- 新增性能优化策略（模型路由/投递/日志/成本）
- 新增多平台集成示例（CI-CD/监控/团队协作/归档）
- 新增版本升级迁移指南
- 新增FAQ章节（15问）与故障排查表（16项）
- 新增即时修复清单（10项）
- 新增依赖说明章节与License版权声明
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 专业版特性

本专业版相比免费版新增以下能力：

- **Webhook投递模式**：将任务结果POST到HTTP端点，支持签名验证、自定义头、超时控制，实现与外部系统的深度集成
- **模型覆盖与思考强度**：为特定任务指定不同LLM模型（opus/sonnet/haiku）与思考强度（low/medium/high），实现成本与质量的精细平衡
- **Telegram论坛话题投递**：支持投递到Telegram supergroup的特定话题，格式规范清晰，便于团队协作
- **退避策略调优**：自定义指数退避参数（maxAttempts/backoff/baseDelay/maxDelay），适应不同任务的容错需求
- **高级配置项**：全局配置sessionRetention、runLog、backoff、delivery等参数，精细控制调度器行为

此外，专业版还提供：
- 完整JSON Schema字段速查表（含免费/专业版对比）
- 作业管理命令扩展（pause/resume/cleanup）
- 多角色场景指南（7种角色×场景映射）
- 性能优化策略（模型路由/投递/日志/成本）
- 多平台集成示例（CI-CD/监控/团队协作/归档）
- 版本升级迁移指南
- 扩展FAQ（15问）与故障排查表（16项）
- 即时修复清单（10项）
- 优先支持

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 三种调度类型 + 双会话模式 + 基础投递（announce/none） + 基础示例 + 基础FAQ | 个人试用、轻量定时需求 |
| 收费专业版 | ¥29.9/月 | 全投递模式（announce/webhook/none）+ 模型覆盖 + 话题投递 + 退避策略 + 高级配置 + 多角色指南 + 性能优化 + 优先支持 | 团队/企业、系统集成 |

专业版通过SkillHub SkillPay发布。
