---
slug: slack-api
name: slack-api
version: "1.0.11"
displayName: Slack
summary: Slack API integration with managed OAuth. Send messages, manage channels,
  search conversations, a...
license: MIT-0
description: |-
  Slack API integration with managed OAuth。Send messages, manage channels,
  search conversations, a。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
- Automation
tools:
  - - read
- exec
# Slack
---
Access the Slack API with managed OAuth authentication. Send messages, manage channels, list users, and automate Slack workflows.

## Quick Start
> 详细内容已移至 `references/detail.md`

## Base URL
```text
https://api.maton.ai/slack/{method}
```

Maton proxies requests to `slack.com` and automatically injects your OAuth token.

## Installation
**NPM:**

```bash
npm install -g @maton/cli
```

**Homebrew:**

```bash
brew install maton-ai/cli/maton
```

## Authentication
> 详细内容已移至 `references/detail.md`

## Connection Management
Manage your Slack OAuth connections at `https://api.maton.ai`.

### List Connections
> 详细内容已移至 `references/detail.md`

### Create Connection
> 详细内容已移至 `references/detail.md`

### Get Connection
> 详细内容已移至 `references/detail.md`

### Delete Connection
> 详细内容已移至 `references/detail.md`

### Specifying Connection
> 详细内容已移至 `references/detail.md`

## Security & Permissions
* Access is scoped to messages, channels, users, files, and reactions within the connected Slack account.
* **All write operations require explicit user approval.** Before executing any create, update, or delete call, confirm the target resource and intended effect with the user.

## API Reference
### Authentication
#### Auth Test
```bash
GET /slack/api/auth.test
```

Returns current user and team info.

Example:

```bash
maton slack whoami
```

> 详细内容已移至 `references/detail.md` - ### Messages
> 详细内容已移至 `references/detail.md` - ### Conversations (Channels)
> 详细内容已移至 `references/detail.md` - ### Direct Messages

### Users
> 详细内容已移至 `references/detail.md`

### Stars
> 详细内容已移至 `references/detail.md`

### Pins
> 详细内容已移至 `references/detail.md`

### Bots
#### Get Bot Info
```bash
GET /slack/api/bots.info?bot=B0123456789
```

Example:

```bash
maton slack bot view B0123456789
```

Note: this expects the `B`-prefixed bot ID (from `bot_id` on a message), not the bot's `U`-prefixed user ID. Passing a `U…` ID returns `bot_not_found`.

### Search
#### Search Messages
```bash
GET /slack/api/search.messages?query=keyword
```

Example:

```bash
maton slack search messages 'keyword'
```

#### Search Files
```bash
GET /slack/api/search.files?query=keyword
```

Note: `search.files` matches against filename and title, not file body content. Newly uploaded files may take a moment to appear in results due to indexing lag.

## 示例
### CLI
```bash
maton slack message send --channel C0123456789 --text 'Hello team'

maton slack channel list --types public_channel,private_channel

maton slack user lookup --email alice@example.com

maton slack reaction add --channel C012 --ts 1700000000.000100 --emoji thumbsup
```

### JavaScript
```javascript
const response = await fetch('https://api.maton.ai/slack/api/chat.postMessage', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.MATON_API_KEY}`
  },
  body: JSON.stringify({ channel: 'C0123456', text: 'Hello!' })
});
const result = await response.json();
console.log(result);
```

### Python
```python
import os
import requests

response = requests.post(
    'https://api.maton.ai/slack/api/chat.postMessage',
    headers={'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}'},
    json={'channel': 'C0123456', 'text': 'Hello!'}
)
print(response.json())
```

## Notes
* Channel IDs: `C` (public), `G` (private/group), `D` (DM)
* User IDs start with `U`, Bot IDs start with `B`, Team IDs start with `T`
* Message timestamps (`ts`) are unique identifiers
* Use `mrkdwn` type for Slack-flavored markdown formatting
* Thread replies use `thread_ts` to reference the parent message
* Cursor-based pagination: use `cursor` from `response_metadata.next_cursor`

### Shell Notes
* IMPORTANT: When using curl commands, use `curl -g` when URLs contain brackets (`fields[]`, `sort[]`, `records[]`) to disable glob parsing
* IMPORTANT: When piping curl output to `jq` or other commands, environment variables like `$MATON_API_KEY` may not expand correctly in some shell environments. You may get "Invalid API key" errors when piping.

## Error Handling
| Status | Meaning |
| --- | --- |
| 400 | Missing Slack connection |
| 401 | Invalid or missing Maton API key |
| 429 | Rate limited (10 req/sec per account) |
| 4xx/5xx | Passthrough error from Slack API |

**Missing Scope Errors:** If you encounter `missing_scope` errors, contact [Maton Support](mailto:support@maton.ai) to request additional scopes for your connection.

### 错误处理
**CLI:**

1. Check your auth state:

```bash
maton whoami
```

2. Verify the API key is valid by listing connections:

```bash
maton connection list
```

**Manual:**

1. Check that the `MATON_API_KEY` environment variable is set:

```bash
echo $MATON_API_KEY
```

2. Verify the API key is valid by listing connections:

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

### Troubleshooting: Invalid App Name
1. Ensure your URL path starts with `slack`. For example:

* Correct: `https://api.maton.ai/slack/api/chat.postMessage`
* Incorrect: `https://api.maton.ai/api/chat.postMessage`

## Resources
* [Slack API Methods](https://api.slack.com/methods)
* [Web API Reference](https://api.slack.com/web)
* [Block Kit Reference](https://api.slack.com/reference/block-kit)
* [Message Formatting](https://api.slack.com/reference/surfaces/formatting)
* [Rate Limits](https://api.slack.com/docs/rate-limits)
* [Maton CLI Manual](https://cli.maton.ai/manual)
* [Maton Community](https://discord.com/invite/dBfFAcefs2)
* [Maton Support](mailto:support@maton.ai)

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
- Slack API integration with managed OAuth
- Send messages, manage channels,
  search conversations, a
- 触发关键词: oauth, api, managed, integration, slack

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用Slack？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Slack有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
