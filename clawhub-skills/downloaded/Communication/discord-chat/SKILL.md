---
slug: discord-chat
name: discord-chat
version: "1.0.0"
displayName: Discord Chat
summary: Send messages, reply to messages, and search message history in Discord channels
  using the messag...
license: MIT
description: |-
  Send messages, reply to messages, and search message history in Discord
  channels using the messag...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: discord, chat, reply, send, search, messages
tags:
- Communication
tools:
- read
- exec
---

# Discord Chat

Interact with Discord channels using Clawdbot's `message` tool.

## Core Actions

### Send Messages

Send a message to a Discord channel:

```bash
message action=send channel=discord target="#channel-name" message="Your message here"
```

Or by channel ID:

```bash
message action=send channel=discord target="1234567890" message="Your message here"
```

**Tips:**

* Use channel names with `#` prefix or channel IDs
* For multiple links, wrap in `<>` to suppress embeds: `<https://example.com>`
* No markdown tables! Use bullet lists instead
* Support effects with `effect=balloons` or `effectId=invisible-ink`

### Reply to Messages

Reply to a specific message:

```bash
message action=send channel=discord target="#channel-name" message="Reply text" replyTo="message-id"
```

The `replyTo` parameter creates a threaded reply to the specified message ID.

### Search Messages

Search for messages in a channel:

```bash
message action=search channel=discord channelId="1234567890" query="search terms" limit=50
```

**Search options:**

* `query`: Search terms
* `authorId`: Filter by author
* `before`/`after`/`around`: Message ID for pagination
* `limit`: Max results (default 25)

See [SEARCH.md](/api/v1/skills/discord-chat/file?path=references%2FSEARCH.md&ownerHandle=bowenqt) for advanced search patterns.

### Other Actions

**Read messages:**

```bash
message action=read channel=discord target="#channel-name" limit=20
```

**React to messages:**

```bash
message action=react channel=discord messageId="1234567890" emoji="👍"
```

**Edit messages:**

```bash
message action=edit channel=discord messageId="1234567890" message="Updated text"
```

**Delete messages:**

```bash
message action=delete channel=discord messageId="1234567890"
```

## Quick Reference

Common patterns:

* **Announce to channel**: `action=send target="#announcements"`
* **Reply in thread**: `action=send replyTo="msg-id"`
* **Recent activity**: `action=read limit=10`
* **Find mentions**: `action=search query="@username"`
* **Acknowledge**: `action=react emoji="✅"`

## Channel Management

**List channels:**

```bash
message action=channel-list channel=discord guildId="server-id"
```

**Get channel info:**

```bash
message action=channel-info channel=discord channelId="1234567890"
```

For creating/editing channels, see [CHANNELS.md](/api/v1/skills/discord-chat/file?path=references%2FCHANNELS.md&ownerHandle=bowenqt).

## Best Practices

1. **Use target names when possible** - `target="#general"` is clearer than IDs
2. **Batch reactions** - One emoji per message, pick the best fit
3. **Format for Discord** - Bullets not tables, `<link>` to suppress embeds
4. **Search before asking** - Check history before requesting info
5. **React > Reply** - Use reactions for simple acknowledgments

## Configuration

Your Discord bot configuration should be in the gateway config. The `message` tool routes to the configured Discord plugin automatically when `channel=discord` is specified.

For setup help, see [CONFIG.md](/api/v1/skills/discord-chat/file?path=references%2FCONFIG.md&ownerHandle=bowenqt).

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
