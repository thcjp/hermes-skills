---
slug: discord-chat
name: discord-chat
version: "1.0.0"
displayName: Discord Chat
summary: "在Discord频道发消息/回复/搜历史"
  using the messag...
license: MIT
description: |-
  Send messages, reply to messages, and search message history in Discord
  channels using the messag。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

- Send messages, reply to messages, and search message history in Discord
  channels using the messag
- 触发关键词: discord, chat, reply, send, search, messages

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Discord Chat？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Discord Chat有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制

- **消息长度**：发送的消息长度不能超过Discord平台规定的最大长度，通常为2000个字符。
- **频率限制**：为了避免滥用，Discord Chat技能可能对发送消息的频率有限制，例如每分钟只能发送一定数量的消息。
- **特殊字符**：输入中不应包含可能导致Discord客户端崩溃或行为异常的特殊字符。

### 性能边界

- **并发处理**：Discord Chat技能可能对同时处理的消息数量有限制，例如同时只能处理一定数量的消息发送或搜索请求。
- **延迟**：由于网络延迟和Discord服务器的响应时间，消息发送和搜索可能存在一定的延迟。

### 兼容性约束

- **Discord版本**：技能可能仅支持特定版本的Discord客户端或服务器。
- **插件兼容性**：如果Discord Chat技能依赖于特定的插件，则可能存在插件版本兼容性问题。
- **操作系统**：技能可能对操作系统版本有限制，例如仅支持Windows 10或更高版本。

### 其他限制

- **黑名单用户**：如果技能用于自动发送消息，则可能无法向被Discord服务器管理员加入黑名单的用户发送消息。
- **敏感内容**：技能可能无法处理包含敏感内容的消息，例如色情、暴力等。
- **API限制**：技能的使用可能受到Discord API调用频率和限制的影响。

