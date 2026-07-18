---
slug: telegram-agent-comm-pro
name: telegram-agent-comm-pro
version: "1.0.0"
displayName: 电报通信助手专业版
summary: 多角色 Agent 团队 Telegram 通信中枢，支持账号映射、批量调度、审计日志与优先级路由。
license: MIT
edition: pro
description: |-
  面向团队与企业的多 Agent Telegram 通信管理规范。
  核心能力: 多角色账号映射、批量消息调度、优先级路由、审计日志、模板库、媒体发送。
  适用场景: 多 Agent 协作汇报、企业通知分发、定时批量推送、跨角色工作流编排。
  差异化: 专业版在免费版基础上扩展多账号体系与调度能力，兼容免费版配置，支持团队级通信治理。
  触发关键词: telegram, 多agent, 团队通信, 批量通知, 账号映射, 审计, 调度, 电报
tags:
- 通信
- 电报
- 团队协作
- 企业通知
- 自动化
tools:
- read
- exec
---

# 电报通信助手 专业版

## 概述

专业版电报通信助手为多 Agent 团队提供完整的 Telegram 通信治理方案。通过账号映射表，团队中每个角色（架构、后端、前端、产品、测试等）拥有独立身份与 emoji 标识，消息来源一目了然。专业版在免费版基础上新增批量调度、优先级路由、审计日志、模板库与媒体发送能力，满足企业级通信需求。

专业版完全兼容免费版配置：免费版的 `default` 账号可直接作为专业版账号映射表的一个条目，升级过程零迁移成本。

## 核心能力

| 能力 | 免费版 | 专业版 |
| --- | :---: | :---: |
| 单账号文本发送 | 支持 | 支持 |
| 多角色账号映射 | - | 支持 |
| 批量消息调度 | - | 支持 |
| 优先级路由 | - | 支持 |
| 审计日志 | - | 支持 |
| 消息模板库 | 3 个 | 8+ 个 |
| 媒体文件发送 | - | 支持 |
| 定时推送 | - | 支持 |
| 多目标分发 | - | 支持 |

## 使用场景

### 场景一：多角色团队任务汇报

团队中不同角色的 Agent 各司其职，按统一规范向负责人汇报。

**账号映射表**

| 角色 | accountId | Emoji | 职责 |
| --- | --- | --- | --- |
| 主控 | `default` | 🤖 | 任务分发与汇总 |
| 架构师 | `architect` | 🏗️ | 系统设计 |
| 后端 | `backend` | 🔧 | 接口开发 |
| 前端 | `frontend` | 🎨 | 界面开发 |
| 产品 | `product` | 🟡 | 需求管理 |
| 测试 | `qa` | 🧪 | 质量保障 |

**后端工程师汇报示例**

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "backend",
  target: "<负责人Telegram用户ID>",
  message: "🔧 API 接口开发完成\n✅ 已完成: 用户鉴权模块\n📁 文档: ~/docs/backend/api.md\n⏱️ 耗时: 2h15m"
})
```

**产品经理汇报示例**

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "product",
  target: "<负责人Telegram用户ID>",
  message: "🟡 需求文档已完成\n📄 文件: ~/docs/product/prd-v2.md\n📌 包含 12 个用户故事\n💡 建议周四评审"
})
```

### 场景二：批量定时通知分发

向多个团队成员定时推送每日站会提醒，专业版支持一次调度多条消息。

```python
# batch_notify.py
import json
from datetime import datetime

members = [
    {"accountId": "architect", "target": "100001", "name": "张工"},
    {"accountId": "backend",   "target": "100002", "name": "李工"},
    {"accountId": "frontend",  "target": "100003", "name": "王工"},
]

for m in members:
    payload = {
        "action": "send",
        "channel": "telegram",
        "accountId": m["accountId"],
        "target": m["target"],
        "message": f"📅 {m['name']}，今日站会 10:00 开始，请准备进度同步"
    }
    print(json.dumps(payload, ensure_ascii=False))
```

### 场景三：优先级路由与告警

生产环境故障时，按优先级路由至不同通道与负责人。

```text
# 优先级路由规则
P0 严重 → 立即发送 + 重复 3 次（间隔 30s）
P1 重要 → 立即发送
P2 一般 → 归并至每小时摘要
```

```javascript
// P0 故障告警示例
message({
  action: "send",
  channel: "telegram",
  accountId: "qa",
  target: "<运维负责人ID>",
  message: "🚨 [P0] 生产环境告警\n❌ 问题: 数据库连接池耗尽\n💡 建议: 立即扩容连接池上限\n⏰ 时间: " + new Date().toISOString()
})
```

## 快速开始

1. 在配置文件中定义账号映射表（见下方配置示例）。
2. 为每个角色分配独立的 `accountId` 与 Bot Token。
3. 在 Agent 指令中引用本规范，各角色 Agent 使用自身 `accountId` 发送消息。

```text
# 专业版最小示例（架构师角色）
message({
  action: "send",
  channel: "telegram",
  accountId: "architect",
  target: "5440561025",
  message: "🏗️ 架构设计稿已完成，请审阅"
})
```

## 配置示例

专业版配置包含多账号映射与调度策略。

```json
{
  "channels": {
    "telegram": {
      "accounts": {
        "default":    { "enabled": true, "emoji": "🤖", "description": "主控" },
        "architect":  { "enabled": true, "emoji": "🏗️", "description": "架构师" },
        "backend":    { "enabled": true, "emoji": "🔧", "description": "后端" },
        "frontend":   { "enabled": true, "emoji": "🎨", "description": "前端" },
        "product":    { "enabled": true, "emoji": "🟡", "description": "产品" },
        "qa":         { "enabled": true, "emoji": "🧪", "description": "测试" }
      },
      "routing": {
        "defaultPriority": "P2",
        "retryPolicy": { "P0": { "count": 3, "intervalSec": 30 } }
      },
      "audit": {
        "enabled": true,
        "logPath": "~/.skill-platform/logs/telegram-audit.jsonl"
      }
    }
  }
}
```

**配置文件路径**：`~/.skill-platform/skill-platform.json` → `channels.telegram`

## 消息模板库

专业版内置 8+ 模板，覆盖完整任务生命周期。

### 任务开始

```text
<emoji> 收到任务：<任务名>
📝 执行人：<accountId>
⏱️ 预计耗时：<时长>
🚀 开始执行...
```

### 任务完成

```text
<emoji> <任务名> 完成
✅ 已完成: <子任务清单>
📁 输出: <文件路径>
⏱️ 实际耗时: <时长>
```

### 遇到问题

```text
<emoji> <任务名> 遇到问题
❌ 问题: <描述>
💡 建议: <解决方案或请求决策>
⚠️ 阻塞中，等待指示
```

### 优先级告警

```text
<emoji> [<优先级>] <告警标题>
❌ 问题: <描述>
💥 影响: <影响范围>
💡 建议: <处理方案>
⏰ 时间: <ISO时间戳>
```

### 每日站会摘要

```text
<emoji> 每日站会摘要 <日期>
✅ 昨日完成: <清单>
🔄 今日计划: <清单>
🚧 风险阻塞: <清单>
```

## 最佳实践

- **账号隔离**：每个角色使用独立 Bot Token，避免单 Token 限流影响全团队。
- **emoji 前缀**：固定每个角色的 emoji，便于在聊天中快速过滤与检索。
- **优先级约定**：团队统一 P0/P1/P2 三级，P0 必须电话或即时通讯二次确认。
- **审计留痕**：开启 `audit.enabled`，所有发送记录写入 JSONL 日志，便于事后追溯。
- **批量限流**：批量发送时控制并发（建议每秒不超过 5 条），避免触发 Telegram API 限流。
- **模板复用**：将常用消息结构沉淀为模板，减少手写出错概率。
- **兼容免费版**：专业版配置中保留 `default` 账号，免费版脚本可直接复用。

## 常见问题

### Q1：专业版如何兼容免费版配置？

专业版账号映射表中保留 `default` 账号即可。免费版脚本中 `accountId: "default"` 的消息在专业版中照常工作，无需修改。

### Q2：批量发送时触发 Telegram 限流怎么办？

降低并发频率，建议每秒不超过 5 条。专业版路由策略支持自动退避重试，可在 `routing.retryPolicy` 中配置。

### Q3：不同角色可以使用同一个 Bot Token 吗？

技术上可以但不推荐。共享 Token 时单账号限流会影响所有角色。建议为关键角色分配独立 Token。

### Q4：审计日志格式是什么？

审计日志为 JSONL 格式，每行一条记录，包含 `timestamp / accountId / target / message / priority / status` 字段。

```json
{"timestamp":"2026-07-18T10:00:00Z","accountId":"backend","target":"5440561025","priority":"P2","status":"sent","message":"🔧 API 开发完成"}
```

### Q5：专业版支持发送图片或文件吗？

支持。通过 `media` 字段附加文件路径或 URL，可发送图片、文档等媒体消息。免费版不支持此能力。

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "qa",
  target: "5440561025",
  message: "🧪 测试报告截图",
  media: "~/reports/screenshot-20260718.png"
})
```

### Q6：如何实现定时推送？

结合 cron 调度工具，在指定时间触发 Agent 执行批量发送脚本。专业版路由策略支持按优先级排队。

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 Telegram API
- **调度工具**：cron / 任务计划程序（定时推送功能需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
| :------- | :----- | :--------- | :--------- |
| Telegram Bot Token（多账号） | API 凭证 | 必需 | 通过 `@BotFather` 为每个角色创建机器人 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Node.js | 运行时 | 可选 | 批量脚本执行需要，v16+ |
| Python | 运行时 | 可选 | 批量调度脚本需要，v3.9+ |
| cron / PM2 | 调度工具 | 可选 | 定时推送功能需要 |

### API Key 配置

- 在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.<accountId>.token` 字段为每个角色填入 Bot Token。
- 建议使用环境变量管理 Token，避免明文写入配置文件。

```bash
# 环境变量示例
export TG_TOKEN_DEFAULT="123456:ABC-DEF"
export TG_TOKEN_BACKEND="123456:GHI-JKL"
export TG_TOKEN_QA="123456:MNO-PQR"
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务。专业版在免费版基础上扩展多账号、批量调度与审计能力，配置文件向后兼容免费版。
