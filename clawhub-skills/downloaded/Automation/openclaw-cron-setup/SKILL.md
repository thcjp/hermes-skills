---
slug: openclaw-cron-setup
name: openclaw-cron-setup
version: "1.0.0"
displayName: OpenClaw Cron Setup
summary: OpenClaw Gateway 内置定时任务调度器。用于创建一次性提醒、周期性任务、后台自动化。支持主会话系统事件和独立会话执行，可配置投递到聊天频道或
  Webhook。
license: MIT
description: |-
  OpenClaw Gateway 内置定时任务调度器。用于创建一次性提醒、周期性任务、后台自动化。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Automation
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Skill平台 Cron Setup

Cron 是 Gateway 内置的调度器，持久化存储任务，在指定时间唤醒 agent 执行，并可选择将结果投递到聊天频道。

## 核心概念

### 两种执行模式

| 模式 | 用途 | payload 类型 |
| --- | --- | --- |
| **main** (主会话) | 系统事件，融入正常心跳流程 | `systemEvent` |
| **isolated** (独立会话) | 后台任务，不污染主会话历史 | `agentTurn` |

### 三种调度类型

| 类型 | 字段 | 示例 |
| --- | --- | --- |
| **一次性** | `schedule.kind: "at"` | `2026-03-04T10:00:00Z` 或 `20m` (相对时间) |
| **固定间隔** | `schedule.kind: "every"` | `everyMs: 3600000` (1 小时) |
| **Cron 表达式** | `schedule.kind: "cron"` | `expr: "0 7 * * *"` (每天 7 点) |

## 快速开始

### 1. 创建一次性提醒（主会话）

```bash
skill-platform cron add \
  --name "提醒事项" \
  --at "20m" \
  --session main \
  --system-event "20 分钟后检查日历" \
  --wake now \
  --delete-after-run
```

### 2. 创建周期性任务（独立会话）

```bash
skill-platform cron add \
  --name "晨间简报" \
  --cron "0 7 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "总结昨晚的邮件和日历事件" \
  --announce \
  --channel telegram \
  --to "+8613800138000"
```

### 3. 创建带模型覆盖的深度任务

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

## 常用命令

```bash
skill-platform cron list

skill-platform cron run <job-id>

skill-platform cron runs --id <job-id> --limit 10

skill-platform cron edit <job-id> --message "新提示词"

skill-platform cron remove <job-id>
```

## JSON Schema（工具调用）

### 一次性主会话任务

```json
{
  "name": "提醒",
  "schedule": { "kind": "at", "at": "2026-03-04T10:00:00Z" },
  "sessionTarget": "main",
  "wakeMode": "now",
  "payload": { "kind": "systemEvent", "text": "提醒内容" },
  "deleteAfterRun": true
}
```

### 周期性独立会话任务

```json
{
  "name": "晨间简报",
  "schedule": { "kind": "cron", "expr": "0 7 * * *", "tz": "Asia/Shanghai" },
  "sessionTarget": "isolated",
  "wakeMode": "next-heartbeat",
  "payload": { "kind": "agentTurn", "message": "总结隔夜更新" },
  "delivery": {
    "mode": "announce",
    "channel": "telegram",
    "to": "+8613800138000",
    "bestEffort": true
  }
}
```

## 投递模式（Delivery）

仅适用于 `isolated` 任务：

| 模式 | 说明 |
| --- | --- |
| `announce` | 投递到指定频道，并在主会话发送简短摘要 |
| `webhook` | POST 到 HTTP 端点 |
| `none` | 仅内部执行，无投递 |

**省略 `delivery` 时默认行为：** `announce` 模式

## Telegram 话题投递

支持论坛话题（topic）：

```bash
--to "-1001234567890:topic:123"  # 推荐：显式话题标记
--to "-1001234567890:123"         # 简写：数字后缀
```

## 示例

当前工作配置示例（`~/.skill-platform/cron/jobs.json`）：

```json
{
  "name": "daily-health-summary",
  "schedule": {
    "kind": "cron",
    "expr": "0 10 * * *",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "从 Bitable 查询健康数据并生成总结"
  },
  "delivery": {
    "mode": "none",
    "channel": "last"
  }
}
```

## 故障排查

### 任务不执行

1. 检查 cron 是否启用：`cron.enabled: true`（配置中）
2. 检查 Gateway 是否持续运行（cron 在 Gateway 进程内执行）
3. 确认时区设置正确（`--tz` 参数）

### 任务反复延迟

* 连续失败会触发指数退避：30s → 1m → 5m → 15m → 60m
* 成功执行后退避重置

### 查看存储位置

* 任务存储：`~/.skill-platform/cron/jobs.json`
* 运行历史：`~/.skill-platform/cron/runs/<jobId>.jsonl`

## 高级配置

在 `~/.skill-platform/config.json` 中：

json5

```
{
  cron: {
    enabled: true,
    sessionRetention: "24h",      // 独立会话保留时长
    runLog: {
      maxBytes: "2mb",            // 运行日志最大大小
      keepLines: 2000,            // 保留行数
    },
  }
}
```

## Cron vs Heartbeat

| 场景 | 推荐 |
| --- | --- |
| 精确时间（如"每周一 9 点"） | **cron** |
| 批量检查（邮箱 + 日历 + 天气） | **heartbeat** |
| 一次性提醒 | **cron** |
| 后台自动化（频繁/嘈杂） | **cron (isolated)** |
| 主会话上下文相关任务 | **heartbeat** |

---

**文档来源：** <https://docs.skill-platform.ai/automation/cron-jobs>

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- OpenClaw Gateway 内置定时任务调度器
- 用于创建一次性提醒、周期性任务、后台自动化
- 支持主会话系统事件和独立会话执行，可配置投递到聊天频道或
  Webhook
- 触发关键词: 周期性任务, setup, 性提醒, 用于创建一次, webhook, cron, openclaw, 内置定时任务

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题

### Q1: 如何开始使用OpenClaw Cron Setup？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: OpenClaw Cron Setup有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
