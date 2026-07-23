---
slug: telegram-messaging
name: telegram-messaging
version: "0.2.2"
displayName: Telegram
summary: Send messages, manage chats, handle files, and automate Telegram bot workflows
  via the Telegram B...
license: MIT-0
description: |-
  Send messages, manage chats, handle files, and automate Telegram bot
  workflows via the Telegram B。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Communication
- Automation
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Telegram

Send messages, manage chats, handle files, and automate Telegram bot workflows via the Telegram Bot API.

This skill uses [ClawLink](https://claw-link.dev/?utm_source=SkillHub&utm_medium=referral&utm_content=telegram-messaging) for hosted connection flows and credentials so you do not need to configure Telegram API access yourself.

### Setup in 3 Steps

| Step 1: Install | Step 2: Pair Account | Step 3: Connect Telegram |
| --- | --- | --- |
|  |  | *App-specific connection GIF coming soon* |
| Run the install command in Skill平台 | Sign in and approve the device | Open the dashboard and connect Telegram |

## How It Works

```text
┌─────────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Skill平台      │────▶│   ClawLink   │────▶│  Telegram Bot    │
│   (User Chat)   │     │   (OAuth)    │     │      API         │
└─────────────────┘     └──────────────┘     └──────────────────┘
         │                       │                       │
         │  1. Install Plugin    │                       │
         │  2. Pair Device       │                       │
         │  3. Connect Telegram  │                       │
         │                       │  4. Secure Token      │
         │                       │  5. Proxy Requests   │
         │                       │                       │
         ▼                       ▼                       ▼
   ┌──────────┐           ┌──────────┐           ┌──────────┐
   │  SKILL   │           │ Dashboard│           │ Telegram │
   │  File    │           │ Auth     │           │   Bot    │
   └──────────┘           └──────────┘           └──────────┘
```

## Install

Install the verified ClawLink plugin from SkillHub. After the user confirms, complete the full setup so ClawLink tools are visible in the next Skill平台 chat.

```bash
skill-platform plugins install SkillHub:clawlink-plugin
skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
skill-platform gateway restart
```

Then tell the user: "Skill平台 has been restarted. Send `/new` as a standalone message to start a fresh chat, then ask for Telegram again."

## Quick Start

```bash
clawlink_call_tool --tool "telegram_get_me" --params '{}'

clawlink_call_tool --tool "telegram_get_chat" --params '{"chat_id": "CHAT_ID"}'

clawlink_call_tool --tool "telegram_send_message" --params '{"chat_id": "CHAT_ID", "text": "Hello from Skill平台!"}'
```

## Authentication

All Telegram tool calls are authenticated automatically by ClawLink using the bot token from the user's connected Telegram bot.

**No bot token is required in chat.** ClawLink stores the bot token securely and injects it into every Telegram Bot API request on the user's behalf.

### Getting Connected

1. Install the ClawLink plugin (see Install above).
2. Pair the plugin with `clawlink_begin_pairing` if it is not configured yet.
3. Open <https://claw-link.dev/dashboard?add=telegram> and connect Telegram.
4. Call `clawlink_list_integrations` to verify the connection is active.

## Connection Management

### List Connections

```bash
clawlink_list_integrations
```

**Response:** Returns all connected integrations. Look for `telegram` in the list.

### Verify Connection

```bash
clawlink_list_tools --integration telegram
```

**Response:** Returns the live tool catalog for Telegram.

### Reconnect

If Telegram tools are missing or the connection shows an error:

1. Direct the user to <https://claw-link.dev/dashboard?add=telegram>
2. After they confirm, call `clawlink_list_integrations` to verify
3. Then call `clawlink_list_tools --integration telegram`

## Security & Permissions

* Access is scoped to the Telegram bot token connected during setup.
* **All write operations (send message, delete message, kick user) require explicit user confirmation.**
* Messages can only be sent to chats where the bot is a member with posting rights.
* The bot must have admin rights in groups/channels to perform moderation actions.
* Rate limits apply (~30 messages/second globally, ~1 message/second per chat).

## Tool Reference

### Bot Info

| Tool | Description | Mode |
| --- | --- | --- |
| `telegram_get_me` | Get basic bot information (username, name, capabilities) | Read |
| `telegram_get_updates` | Receive incoming updates via long polling | Read |

### Messages

| Tool | Description | Mode |
| --- | --- | --- |
| `telegram_send_message` | Send a text message to a chat | Write |
| `telegram_send_photo` | Send a photo to a chat | Write |
| `telegram_send_document` | Send a document/file to a chat | Write |
| `telegram_send_location` | Send a location point on a map | Write |
| `telegram_send_poll` | Send a native poll to a chat | Write |
| `telegram_edit_message` | Edit an existing bot-sent message | Write |
| `telegram_delete_message` | Delete a bot-sent or service message | Write |
| `telegram_forward_message` | Forward a message to another chat | Write |

### Chats

| Tool | Description | Mode |
| --- | --- | --- |
| `telegram_get_chat` | Get chat information by ID | Read |
| `telegram_get_chat_history` | Get messages from a chat | Read |
| `telegram_get_chat_member` | Get a user's status/role in a chat | Read |
| `telegram_get_chat_administrators` | List admins in a chat | Read |
| `telegram_get_chat_members_count` | Get member count for a chat | Read |
| `telegram_create_chat_invite_link` | Generate a new primary invite link | Write |
| `telegram_revoke_chat_invite_link` | Revoke an existing invite link | Write |

### Callbacks

| Tool | Description | Mode |
| --- | --- | --- |
| `telegram_answer_callback_query` | Send an answer to a callback query from inline keyboard | Write |

### Bot Commands

| Tool | Description | Mode |
| --- | --- | --- |
| `telegram_set_my_commands` | Set the bot's command list | Write |
| `telegram_get_my_commands` | Get the bot's current command list | Read |

## 示例

### Send a text message

```bash
clawlink_call_tool --tool "telegram_send_message" \
  --params '{
    "chat_id": "-1001234567890",
    "text": "Deployment complete! Version 2.1.0 is live on production."
  }'
```

### Send a photo

```bash
clawlink_call_tool --tool "telegram_send_photo" \
  --params '{
    "chat_id": "-1001234567890",
    "photo": "https://example.com/chart.png",
    "caption": "Weekly activity report"
  }'
```

### Send a poll

```bash
clawlink_call_tool --tool "telegram_send_poll" \
  --params '{
    "chat_id": "-1001234567890",
    "question": "Which feature should we prioritize next?",
    "options": ["Dark mode", "Export to PDF", "Team sharing", "API access"]
  }'
```

### Get chat information

```bash
clawlink_call_tool --tool "telegram_get_chat" \
  --params '{
    "chat_id": "-1001234567890"
  }'
```

### Get chat member info

```bash
clawlink_call_tool --tool "telegram_get_chat_member" \
  --params '{
    "chat_id": "-1001234567890",
    "user_id": "123456789"
  }'
```

### Forward a message

```bash
clawlink_call_tool --tool "telegram_forward_message" \
  --params '{
    "chat_id": "-1009876543210",
    "from_chat_id": "-1001234567890",
    "message_id": 42
  }'
```

## Discovery Workflow

1. Call `clawlink_list_integrations` to confirm Telegram is connected.
2. Call `clawlink_list_tools --integration telegram` to see the live catalog.
3. Treat the returned list as the source of truth. Do not guess or assume what tools exist.
4. If the user describes a capability but the exact tool is unclear, call `clawlink_search_tools` with a short query and integration `telegram`.
5. If no Telegram tools appear, direct the user to <https://claw-link.dev/dashboard?add=telegram>.

## Execution Workflow

```text
┌─────────────────────────────────────────────────────────────┐
│  READ OPERATIONS (Safe)                                     │
│  get → list → fetch → describe                              │
│                                                             │
│  Example: Get chat info → Get chat history → Report        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  WRITE OPERATIONS (Require Confirmation)                    │
│  describe → preview → confirm → call                        │
│                                                             │
│  Example: Preview message → User approves → Send message    │
└─────────────────────────────────────────────────────────────┘
```

1. For unfamiliar tools, ambiguous requests, or any write action, call `clawlink_describe_tool` first.
2. Use the returned guidance, schema, `whenToUse`, `askBefore`, `safeDefaults`, `examples`, and `followups` to shape the call.
3. Prefer read and get operations before writes when that reduces ambiguity.
4. For writes or anything marked as requiring confirmation, call `clawlink_preview_tool` first.
5. Execute with `clawlink_call_tool`. Pass confirmation only after the preview matches the user's intent.
6. If the tool call fails, report the real error. Do not invent results or restate the failure as a missing capability unless the live catalog supports that conclusion.

## Notes

* Chat IDs for groups/channels start with `-100` (e.g., `-1001234567890`). User DMs use the user's numeric ID.
* Telegram Bot API uses Unix timestamps in UTC for message dates.
* `telegram_get_updates` and webhooks are mutually exclusive — if a webhook is active, polling returns a 409 Conflict.
* Rate limits: ~30 messages/second globally, ~1 message/second per chat. On HTTP 429, honor the `retry_after` value.
* The bot can only delete messages it sent itself or messages in groups where it has admin rights.
* Photos are re-encoded by Telegram; use `send_document` to preserve original quality.
* Messages older than 48 hours cannot be deleted in groups.

## Error Handling

| Status / Error | Meaning |
| --- | --- |
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration telegram`. |
| Missing connection | Telegram is not connected. Direct the user to <https://claw-link.dev/dashboard?add=telegram>. |
| `chat_not_found` | The chat ID does not exist or the bot is not a member. |
| `bot_not_member` | The bot is not a member of the target chat. |
| `message_not_found` | The message ID does not exist in the chat. |
| `user_not_found` | The user ID does not match any chat member. |
| `message_to_delete_not_found` | Cannot delete — message may be too old (48h+ in groups) or not bot-authored. |
| `not_enough_rights` | Bot lacks admin rights needed for this action in the group. |
| `retry_after` | Rate limited — honor the retry delay (seconds). |
| `invalid_token` | The bot token is invalid. Reconnect Telegram. |
| Write rejected | User did not confirm a write action. Always confirm before executing writes. |

### 错误处理

1. Check that the ClawLink plugin is installed:

   bash

   ```
   skill-platform plugins list
   ```
2. If the plugin is installed but tools are missing, tell the user to send `/new` as a standalone message to reload the catalog.
3. If a fresh chat does not help, run:

   bash

   ```
   skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
   skill-platform gateway restart
   ```
4. After restart, tell the user to send `/new` again and retry.

### Troubleshooting: Message Send Fails

1. Confirm the bot is a member of the target chat with post rights.
2. Check the chat ID format — groups use `-100` prefix, users use numeric ID.
3. Verify the bot has permission to send media if attaching photos/documents.
4. If `chat_not_found` appears, the bot may have been removed from the group.

### Troubleshooting: Delete Message Fails

1. The bot can only delete its own messages or messages in groups where it is an admin.
2. Messages older than 48 hours in groups cannot be deleted via the Bot API.
3. Service messages (user join/leave) cannot be deleted.

## Resources

* [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
* [Telegram Bot Features](https://core.telegram.org/bots/features)
* [BotFather](https://t.me/botfather) — manage bot settings and commands
* ClawLink: <https://claw-link.dev/?utm_source=SkillHub&utm_medium=referral&utm_content=telegram-messaging>
* ClawLink Docs: <https://docs.claw-link.dev/skill-platform>
* ClawLink Verification: <https://claw-link.dev/verify>

---

**Powered by [ClawLink](https://claw-link.dev/?utm_source=SkillHub&utm_medium=referral&utm_content=telegram-messaging)** — an integration hub for Skill平台

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

- Send messages, manage chats, handle files, and automate Telegram bot
  workflows via the Telegram B
- 触发关键词: messaging, chats, telegram, handle, manage, send, messages

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题

### Q1: 如何开始使用Telegram？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Telegram有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
