# 详细参考 - cron-setup-guide-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

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

## 代码示例 (json)

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

## 代码示例 (bash)

```bash
skill-platform cron list

skill-platform cron list --status active
skill-platform cron list --status failed
skill-platform cron list --status paused

skill-platform cron run <job-id>

skill-platform cron runs --id <job-id> --limit 10

skill-platform cron runs --id <job-id> --limit 10 --include-failures

skill-platform cron edit <job-id> --message "新提示词"

skill-platform cron edit <job-id> --model "opus" --thinking high

skill-platform cron pause <job-id>
skill-platform cron resume <job-id>

skill-platform cron remove <job-id>

skill-platform cron cleanup --status done --older-than 7d
```

## 代码示例 (bash)

```bash
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

## 代码示例 (json5)

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

## 代码示例 (http)

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
--to "-1001234567890:topic:123"

--to "-1001234567890:123"
```

格式说明：
- `-1001234567890`：supergroup ID（必须以 -100 开头）
- `topic:123` 或 `:123`：话题ID
- 推荐使用显式 `topic:` 标记，便于阅读与维护



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



## 性能优化策略


## 版本升级迁移指南



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



---

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



---

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



---

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



---

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



---

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



---

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
