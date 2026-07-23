---
slug: discord
name: discord
version: "1.0.1"
displayName: Discord
summary: "Use when you need to control Discord from Clawdbot via the discord tool:
  send messages, react, po"
license: MIT
description: |-
  Use when you need to control Discord from Clawdbot via the discord tool:
  send messages, react, po。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Discord

## Overview

Use `discord` to manage messages, reactions, threads, polls, and moderation. You can disable groups via `discord.actions.*` (defaults to enabled, except roles/moderation). The tool uses the bot token configured for Clawdbot.

## Inputs to collect

* For reactions: `channelId`, `messageId`, and an `emoji`.
* For stickers/polls/sendMessage: a `to` target (`channel:<id>` or `user:<id>`). Optional `content` text.
* Polls also need a `question` plus 2–10 `answers`.
* For media: `mediaUrl` with `file:///path` for local files or `https://...` for remote.
* For emoji uploads: `guildId`, `name`, `mediaUrl`, optional `roleIds` (limit 256KB, PNG/JPG/GIF).
* For sticker uploads: `guildId`, `name`, `description`, `tags`, `mediaUrl` (limit 512KB, PNG/APNG/Lottie JSON).

Message context lines include `discord message id` and `channel` fields you can reuse directly.

**Note:** `sendMessage` uses `to: "channel:<id>"` format, not `channelId`. Other actions like `react`, `readMessages`, `editMessage` use `channelId` directly.

## Actions

### React to a message

```json
{
  "action": "react",
  "channelId": "123",
  "messageId": "456",
  "emoji": "✅"
}
```

### List reactions + users

```json
{
  "action": "reactions",
  "channelId": "123",
  "messageId": "456",
  "limit": 100
}
```

### Send a sticker

```json
{
  "action": "sticker",
  "to": "channel:123",
  "stickerIds": ["9876543210"],
  "content": "Nice work!"
}
```

* Up to 3 sticker IDs per message.
* `to` can be `user:<id>` for DMs.

### Upload a custom emoji

```json
{
  "action": "emojiUpload",
  "guildId": "999",
  "name": "party_blob",
  "mediaUrl": "file:///tmp/party.png",
  "roleIds": ["222"]
}
```

* Emoji images must be PNG/JPG/GIF and <= 256KB.
* `roleIds` is optional; omit to make the emoji available to everyone.

### Upload a sticker

```json
{
  "action": "stickerUpload",
  "guildId": "999",
  "name": "clawdbot_wave",
  "description": "Clawdbot waving hello",
  "tags": "👋",
  "mediaUrl": "file:///tmp/wave.png"
}
```

* Stickers require `name`, `description`, and `tags`.
* Uploads must be PNG/APNG/Lottie JSON and <= 512KB.

### Create a poll

```json
{
  "action": "poll",
  "to": "channel:123",
  "question": "Lunch?",
  "answers": ["Pizza", "Sushi", "Salad"],
  "allowMultiselect": false,
  "durationHours": 24,
  "content": "Vote now"
}
```

* `durationHours` defaults to 24; max 32 days (768 hours).

### Check bot permissions for a channel

```json
{
  "action": "permissions",
  "channelId": "123"
}
```

## Ideas to try

* React with ✅/⚠️ to mark status updates.
* Post a quick poll for release decisions or meeting times.
* Send celebratory stickers after successful deploys.
* Upload new emojis/stickers for release moments.
* Run weekly “priority check” polls in team channels.
* DM stickers as acknowledgements when a user’s request is completed.

## Action gating

Use `discord.actions.*` to disable action groups:

* `reactions` (react + reactions list + emojiList)
* `stickers`, `polls`, `permissions`, `messages`, `threads`, `pins`, `search`
* `emojiUploads`, `stickerUploads`
* `memberInfo`, `roleInfo`, `channelInfo`, `voiceStatus`, `events`
* `roles` (role add/remove, default `false`)
* `moderation` (timeout/kick/ban, default `false`)

### Read recent messages

```json
{
  "action": "readMessages",
  "channelId": "123",
  "limit": 20
}
```

### Send/edit/delete a message

```json
{
  "action": "sendMessage",
  "to": "channel:123",
  "content": "Hello from Clawdbot"
}
```

**With media attachment:**

```json
{
  "action": "sendMessage",
  "to": "channel:123",
  "content": "Check out this audio!",
  "mediaUrl": "file:///tmp/audio.mp3"
}
```

* `to` uses format `channel:<id>` or `user:<id>` for DMs (not `channelId`!)
* `mediaUrl` supports local files (`file:///path/to/file`) and remote URLs (`https://...`)
* Optional `replyTo` with a message ID to reply to a specific message

```json
{
  "action": "editMessage",
  "channelId": "123",
  "messageId": "456",
  "content": "Fixed typo"
}
```

```json
{
  "action": "deleteMessage",
  "channelId": "123",
  "messageId": "456"
}
```

### Threads

```json
{
  "action": "threadCreate",
  "channelId": "123",
  "name": "Bug triage",
  "messageId": "456"
}
```

```json
{
  "action": "threadList",
  "guildId": "999"
}
```

```json
{
  "action": "threadReply",
  "channelId": "777",
  "content": "Replying in thread"
}
```

### Pins

```json
{
  "action": "pinMessage",
  "channelId": "123",
  "messageId": "456"
}
```

```json
{
  "action": "listPins",
  "channelId": "123"
}
```

### Search messages

```json
{
  "action": "searchMessages",
  "guildId": "999",
  "content": "release notes",
  "channelIds": ["123", "456"],
  "limit": 10
}
```

### Member + role info

```json
{
  "action": "memberInfo",
  "guildId": "999",
  "userId": "111"
}
```

```json
{
  "action": "roleInfo",
  "guildId": "999"
}
```

### List available custom emojis

```json
{
  "action": "emojiList",
  "guildId": "999"
}
```

### Role changes (disabled by default)

```json
{
  "action": "roleAdd",
  "guildId": "999",
  "userId": "111",
  "roleId": "222"
}
```

### Channel info

```json
{
  "action": "channelInfo",
  "channelId": "123"
}
```

```json
{
  "action": "channelList",
  "guildId": "999"
}
```

### Voice status

```json
{
  "action": "voiceStatus",
  "guildId": "999",
  "userId": "111"
}
```

### Scheduled events

```json
{
  "action": "eventList",
  "guildId": "999"
}
```

### Moderation (disabled by default)

```json
{
  "action": "timeout",
  "guildId": "999",
  "userId": "111",
  "durationMinutes": 10
}
```

## Discord Writing Style Guide

**Keep it conversational!** Discord is a chat platform, not documentation.

### Do

* Short, punchy messages (1-3 sentences ideal)
* Multiple quick replies > one wall of text
* Use emoji for tone/emphasis 🦞
* Lowercase casual style is fine
* Break up info into digestible chunks
* Match the energy of the conversation

### Don't

* No markdown tables (Discord renders them as ugly raw `| text |`)
* No `## Headers` for casual chat (use **bold** or CAPS for emphasis)
* Avoid multi-paragraph essays
* Don't over-explain simple things
* Skip the "I'd be happy to help!" fluff

### Formatting that works

* **bold** for emphasis
* `code` for technical terms
* Lists for multiple items
* > quotes for referencing
* Wrap multiple links in `<>` to suppress embeds

### 示例

❌ Bad:

```text
I'd be happy to help with that! Here's a comprehensive overview of the versioning strategies available:

## Semantic Versioning
Semver uses MAJOR.MINOR.PATCH format where...

## Calendar Versioning
CalVer uses date-based versions like...
```

✅ Good:

```text
versioning options: semver (1.2.3), calver (2026.01.04), or yolo (`latest` forever). what fits your release cadence?
```

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

Use `discord` to manage messages, reactions, threads, polls, and moderation. You can disable groups via `discord.actions.*` (defaults to enabled, except roles/moderation). The tool uses the bot token configured for Clawdbot.

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Discord？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Discord有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
