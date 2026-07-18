---
slug: telegram-agent-comm-free
name: telegram-agent-comm-free
version: "1.0.0"
displayName: 电报通信助手免费版
summary: 单 Agent 通过 Telegram 发送消息的轻量规范，支持基础通知与任务汇报，零配置快速上手。
license: MIT
edition: free
description: |-
  面向个人开发者与独立创作者的 Telegram 消息发送规范。
  核心能力: 单 Agent 身份发送、标准消息格式、任务汇报模板、错误自检。
  适用场景: 个人任务提醒、自动化通知推送、单人工作流汇报。
  差异化: 免费版聚焦单账号通信，去除多角色映射与批量调度，启动门槛低。
  触发关键词: telegram, 消息发送, 通知, 汇报, agent, 通信, 电报
tags:
- 通信
- 电报
- 通知
- 个人效率
tools:
- read
- exec
---

# 电报通信助手 免费版

## 概述

免费版电报通信助手为个人用户提供一套简洁的 Telegram 消息发送规范。所有 Agent 在向用户发送消息时遵循统一格式，确保消息稳定送达。本版本聚焦单账号通信场景，适合独立开发者、自由职业者以及希望快速接入 Telegram 通知的个人用户。

与专业版相比，免费版移除了多角色账号映射、批量调度与审计日志等高级能力，保留最核心的「发送消息 + 任务汇报」能力，做到零额外配置即可使用。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| 单账号发送 | 通过默认 `accountId` 向指定用户发送 Telegram 消息 |
| 标准消息格式 | 统一 `action / channel / target / message` 字段结构 |
| 任务汇报模板 | 提供任务开始、完成、遇阻三类消息模板 |
| 错误自检 | 内置常见错误对照表，帮助快速定位发送失败原因 |
| 文本消息 | 支持纯文本与 emoji 表情消息 |

## 使用场景

### 场景一：个人任务完成通知

独立开发者在本地完成一段脚本编写后，希望收到 Telegram 提醒。

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "default",
  target: "<你的Telegram用户ID>",
  message: "✅ 脚本 build.sh 执行完成，日志已保存至 ~/logs/build.log"
})
```

### 场景二：自动化流水线状态推送

将消息发送嵌入 CI 脚本，在部署完成后推送结果。

```bash
# deploy-notify.sh
MESSAGE="🚀 部署完成：分支 ${BRANCH} 已上线 $(date '+%H:%M:%S')"
echo "向 Telegram 推送：${MESSAGE}"
# 此处由 Agent 解析并调用 message 工具
```

### 场景三：每日工作汇报

Agent 汇总当日任务清单后，统一发送一条汇报消息。

```text
📋 今日工作汇报
- 修复登录页样式问题
- 完成数据导出接口
- 重构缓存模块
📁 详细记录：~/reports/2026-07-18.md
```

## 快速开始

1. 确认 Agent 运行环境已配置 Telegram 通道（`channels.telegram`）。
2. 获取你的 Telegram 用户 ID（可通过 `@userinfobot` 查询）。
3. 在 Agent 指令中引用本规范，即可使用 `message` 工具发送消息。

```text
# 最小可用示例
message({
  action: "send",
  channel: "telegram",
  accountId: "default",
  target: "123456789",
  message: "👋 电报通信助手已就绪"
})
```

## 配置示例

免费版仅需在主配置中保留一个默认账号即可。

```json
{
  "channels": {
    "telegram": {
      "accounts": {
        "default": {
          "enabled": true,
          "description": "个人默认账号"
        }
      }
    }
  }
}
```

**配置文件路径**：`~/.skill-platform/skill-platform.json`

## 最佳实践

- **固定 target**：始终使用你自己的 Telegram 用户 ID，避免误发他人。
- **消息前缀**：建议在消息开头加入 emoji，便于在聊天列表中快速识别。
- **汇报时机**：收到任务、完成子任务、遇到问题、任务收尾四个节点各发一次。
- **控制频率**：免费版无批量调度，单条发送避免短时间内重复触发。
- **内容简洁**：每条消息控制在 200 字以内，关键信息前置。

## 常见问题

### Q1：消息发送失败，提示 accountId 不存在？

确认配置文件中 `channels.telegram.accounts` 下存在 `default` 账号。免费版仅使用默认账号，无需配置多账号。

### Q2：可以用 `sessions_send` 发送到 Telegram 吗？

不可以。`sessions_send` 仅在 Agent 内部会话流转，不会推送到 Telegram。必须使用 `message` 工具并指定 `channel: "telegram"`。

### Q3：target 写错了会怎样？

消息会发送给错误的用户或直接失败。建议将 target 固化为常量，避免每次手输。

### Q4：免费版支持发送图片或文件吗？

免费版仅支持文本消息。如需发送媒体文件、批量消息或多角色汇报，请升级至专业版。

### Q5：如何查看发送历史？

免费版不提供审计日志，建议在脚本中自行记录发送时间与内容到本地文件。

```bash
# 自定义发送日志示例
# send-log.sh
LOG_FILE="$HOME/logs/telegram-send.log"
mkdir -p "$(dirname "$LOG_FILE")"

log_send() {
  local msg="$1"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] SEND: ${msg}" >> "$LOG_FILE"
}

# 在发送消息后调用
log_send "脚本执行完成通知已发送"
```

## 免费版与专业版对比

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
| 优先技术支持 | 社区 | 优先 |

## 进阶技巧

### 技巧一：消息内容格式优化

Telegram 支持 Markdown 格式消息，利用格式化提升可读性。

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "default",
  target: "123456789",
  message: "*构建报告*\n- 分支: `main`\n- 状态: ✅ 成功\n- 耗时: _2m30s_\n- 产物: [查看日志](file:///logs/build.log)"
})
```

### 技巧二：脚本中封装发送函数

将消息发送封装为可复用的 shell 函数，减少重复代码。

```bash
# ~/.bashrc 或 ~/.zshrc
tg_send() {
  local msg="$1"
  local target="${2:-123456789}"
  # 此处由 Agent 解析并调用 message 工具
  echo "[TG-SEND] target=${target} msg=${msg}"
}

# 使用示例
tg_send "✅ 数据库备份完成 $(date '+%F %T')"
tg_send "🚨 磁盘使用率超过 90%" "100001"
```

### 技巧三：结合 cron 实现定时通知

利用系统 cron 定时触发 Agent 发送消息，实现简单的定时推送。

```bash
# crontab -e
# 每天早上 8:00 发送每日提醒
0 8 * * * /path/to/agent run "通过 telegram-agent-comm 发送消息：☀️ 早上好，今日待办事项已整理至 ~/todo/today.md"

# 每周一生成周报提醒
0 9 * * 1 /path/to/agent run "通过 telegram-agent-comm 发送消息：📊 请提交本周工作周报"
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 Telegram API

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
| :------- | :----- | :--------- | :--------- |
| Telegram Bot Token | API 凭证 | 必需 | 通过 `@BotFather` 创建机器人获取 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Node.js | 运行时 | 可选 | 部分脚本执行需要，v16+ |

### API Key 配置

- 在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.default.token` 字段填入 Bot Token。
- 免费版无需额外 API Key（除 Telegram Bot Token 外）。

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务。免费版功能子集，与专业版配置文件向后兼容。
