---
slug: "telegram-messaging-free"
name: "telegram-messaging-free"
version: "1.0.0"
displayName: "Telegram 消息 LITE"
summary: "Telegram Bot API 基础消息发送与聊天信息查询。。Telegram Bot API 集成 Skill 免费版。支持发送文本消息与图片、获取机器人信息、 查询聊天基本信息与成员计"
license: "MIT"
description: |-
  Telegram Bot API 集成 Skill 免费版。支持发送文本消息与图片、获取机器人信息、
  查询聊天基本信息与成员计数。所有写操作需用户确认后执行.
  适用于基础消息通知、聊天信息查询等场景.
tags:
  - 通用办公
  - Automation
  - Telegram
  - 社交
  - 通信
  - token
  - telegram
  - agent
  - bot
  - api
tools:
  - read
  - exec
  - write
homepage: ""
category: "Communication"
---
# Telegram 消息 LITE

Telegram Bot API 集成免费版。支持发送文本消息与图片、获取机器人信息、查询聊天基本信息。所有写操作需用户确认后执行.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Telegram 消息 LITE处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心能力

- **基础消息发送**：支持发送文本消息与图片，图片可附加 caption 说明文本
- **机器人信息获取**：获取机器人用户名、名称、能力信息，验证 Token 有效性
- **聊天信息查询**：获取聊天基本信息与成员计数，确认目标聊天存在且机器人为成员
- **写操作确认机制**：发送消息与图片需用户确认后执行，避免误发
### 基础消息发送

针对基础消息发送,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供基础消息发送相关的配置参数、输入数据和处理选项.
**输出**: 返回基础消息发送的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础消息发送`的配置文档进行参数调优
### 机器人信息获取

针对机器人信息获取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供机器人信息获取相关的配置参数、输入数据和处理选项.
**输出**: 返回机器人信息获取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`机器人信息获取`的配置文档进行参数调优
### 聊天信息查询

针对聊天信息,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供聊天信息查询相关的配置参数、输入数据和处理选项.
**输出**: 返回聊天信息查询的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`聊天信息查询`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 工具列表

- `telegram_get_me`：获取机器人基本信息（用户名、名称、能力）— 读操作
- `telegram_send_message`：发送文本消息 — 写操作
- `telegram_send_photo`：发送图片 — 写操作
- `telegram_get_chat`：按 ID 获取聊天信息 — 读操作
- `telegram_get_chat_members_count`：获取聊天成员计数 — 读操作

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 基础消息通知 | 通知文本内容 | 向目标聊天发送文本消息 |
| 聊天信息查询 | 聊天 ID | 返回聊天基本信息与成员数 |

**不适用于**：文档/位置/投票等多类型消息、消息编辑删除转发、邀请链接管理、回调处理、命令列表设置等高级场景.
## 使用流程

1. **确认 Bot Token 已配置**：Bot Token 通过 @BotFather 创建，配置在 Agent 环境中。调用 `telegram_get_me` 验证 Token 有效性
2. **获取目标聊天 ID**：群组/频道 ID 以 `-100` 开头（如 `-1001234567890`），用户私信用用户数字 ID
3. **读操作优先**：对于不熟悉的聊天，先调用 `telegram_get_chat` 确认聊天存在且机器人为成员
4. **写操作预览确认**：发送消息前向用户预览内容与目标聊天，确认后执行

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 认证配置

Bot Token 通过 @BotFather 创建获取，配置在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.default.token` 字段。所有 API 调用自动注入 Bot Token，无需在调用参数中传递.
### 验证连接

```
telegram_get_me({})
```

返回机器人用户名与名称，确认 Token 有效.
## 案例展示

### 案例 1：向开发群发送文本通知

**触发**：需要通知开发群某项任务完成

**执行**：

```
telegram_send_message({
  chat_id: "-1001234567890",
  text: "构建完成，版本 2.1.0 已就绪。"
})
```

**结果**：开发群收到一条文本通知消息.
### 案例 2：发送带说明的图片

**触发**：需要向群组发送一张截图并附说明

**执行**：

```
telegram_send_photo({
  chat_id: "-1001234567890",
  photo: "https://example.com/screenshot.png",
  caption: "新版本界面预览"
})
```

**结果**：群组收到一张图片，下方显示 caption 文本"新版本界面预览".
## 错误处理

| 错误 | 原因 | 处理方式 |
|---:|---:|---:|
| `chat_not_found` | 聊天 ID 不存在或机器人非成员 | 确认 ID 格式正确，群组以 `-100` 开头；将机器人加入目标聊天 |
| `bot_not_member` | 机器人不是目标聊天成员 | 通过群主邀请机器人加入群组并赋予发消息权限 |
| HTTP 429 `retry_after` | 触发速率限制 | 按 `retry_after` 字段指定的秒数等待后检查网络连接和配置后重试，单聊天不超过 1 条/秒 |
| `invalid_token` | Bot Token 无效或已过期 | 通过 @BotFather 重新获取 Token，更新配置后重启 Agent |
| 写操作被拒绝 | 用户未确认写操作 | 所有发送操作须先预览并由用户确认后才执行 |

## 常见问题

### Q1：如何获取群组的 chat_id？
A：将机器人加入群组后，在群内发送一条消息。群组/频道 ID 以 `-100` 开头，可通过 Telegram 客户端转发消息到查询机器人获取。用户私信使用用户数字 ID.
### Q2：免费版支持发送哪些消息类型？
A：免费版支持发送文本消息与图片。如需发送文档、位置、投票等多类型消息，请升级付费版.
### Q3：发送图片后画质降低怎么办？
A：Telegram 会对通过 `send_photo` 发送的图片进行压缩与重新编码。免费版不支持文档发送功能，如需保留原图质量请升级付费版使用 `send_document`.
### Q4：速率限制是多少？
A：全局约 30 条/秒，单聊天约 1 条/秒。触发限制时返回 HTTP 429，按响应体中 `retry_after` 字段指定的秒数等待后重试.
## 已知限制

- 仅支持发送文本消息与图片，不支持文档/位置/投票
- 不支持消息编辑、删除、转发
- 不支持邀请链接管理与回调处理
- 不支持聊天历史检索与成员角色查询
- 不支持命令列表设置与更新获取
- 速率限制为全局 30 条/秒、单聊天 1 条/秒
- 通过 `send_photo` 发送的图片会被压缩

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 Telegram Bot API（`https://api.telegram.org`）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Telegram Bot Token | 凭证 | 必需 | 通过 @BotFather 创建 Bot 获取 |
| Agent 工具运行时 | Agent 平台工具 | 必需 | Agent 平台内置或插件提供 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供决策能力 |

### API Key 配置
- Bot Token 配置在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.default.token` 字段
- 所有 Telegram API 调用自动注入该 Token，无需在调用参数中传递

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，工具调用需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务

---
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 升级提示

当前为免费版，仅支持文本与图片发送及基础聊天查询。如需以下完整功能，请升级付费版：

- **多类型消息**：支持文档、位置、投票等消息类型
- **消息生命周期管理**：编辑、删除、转发消息
- **聊天深度检索**：获取聊天历史、成员角色、管理员列表
- **邀请链接管理**：生成与撤销聊天邀请链接
- **回调与命令**：处理内联键盘回调、设置机器人命令列表
- **更新获取**：通过长轮询获取 incoming updates

升级至付费版：`https://SkillHub.ai/skill/telegram-messaging`

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Telegram 消息 LITE处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "telegram-messaging"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
