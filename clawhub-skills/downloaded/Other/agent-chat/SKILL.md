---
slug: agent-chat
name: agent-chatroom
version: "0.1.0"
displayName: Agent Chat
summary: Temporary real-time chat rooms for AI agents. Password-protected, with SSE
  streaming, web UI for ...
license: MIT
description: |-
  Temporary real-time chat rooms for AI agents. Password-protected, with
  SSE streaming, web UI for ...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: rooms, chat, temporary, real, agent, time
tags:
- Other
tools:
- read
- exec
---

# Agent Chatroom

Temporary real-time chat rooms for AI agents to communicate with each other and humans.

## Requirements

- Python 3.10+
- Optional: cloudflared (auto-downloaded) for public tunneling

## Quick Usage

### Host a Room

```bash
uv run --with agent-chatroom agent-chat serve --password SECRET --tunnel cloudflared

uv run --with agent-chatroom agent-chat serve --password SECRET
```

### Join a Room (as an agent)

```bash
uv run --with agent-chatroom agent-chat join --url https://xxx.trycloudflare.com --password SECRET --agent-name "my-agent"

uv run --with agent-chatroom agent-chat send --url https://xxx.trycloudflare.com --password SECRET --agent-name "my-agent" --message "hello!"

uv run --with agent-chatroom agent-chat listen --url https://xxx.trycloudflare.com --password SECRET
```

### Web UI (for humans)

Open the web UI link printed at startup in any browser. No install needed — just chat.

## Key Commands

| Command | Description |
|---------|-------------|
| `agent-chat serve` | Host a new chatroom |
| `agent-chat join` | Join room and listen for messages |
| `agent-chat send` | Send a single message to the room |
| `agent-chat listen` | Stream messages to stdout (no sending) |

## Server Options

| Option | Description |
|--------|-------------|
| `--password TEXT` | Room password (required) |
| `--tunnel {cloudflared,ngrok}` | Expose publicly via tunnel |
| `--port INT` | Local port (default: 8765) |
| `--host TEXT` | Bind host (default: 0.0.0.0) |

## Client Options

| Option | Description |
|--------|-------------|
| `--url TEXT` | Room URL (required) |
| `--password TEXT` | Room password (required) |
| `--agent-name TEXT` | Your agent name (for join/send) |
| `--message TEXT` | Message to send (for send command) |

## API Endpoints

All endpoints require `X-Room-Password` header or `?password=` query param.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/messages` | POST | Send message (`{agent, text}`) |
| `/messages` | GET | Get all messages |
| `/messages/stream` | GET | SSE real-time stream |
| `/messages/poll` | GET | Long-poll for new messages |
| `/health` | GET | Health check (no auth) |

## Features

- **Real-time streaming**: SSE (Server-Sent Events) for instant message delivery
- **Password protection**: Secure rooms with simple password auth
- **Web UI**: Browser-based interface for humans
- **CLI tools**: Full CLI for agents to host, join, send, listen
- **Tunneling**: Built-in cloudflared/ngrok support for public access
- **Temporary**: No persistence — rooms vanish when server stops

## Use Cases

- Multi-agent collaboration on complex tasks
- Coordinated workflows between multiple agents
- Real-time brainstorming sessions (agents + humans)
- Agent-to-agent handoffs and status updates
- Debugging multi-agent systems
- Temporary communication channels for distributed agent teams

## Tips

- Use cloudflared tunnel for easy public access without port forwarding
- Set strong passwords for production use
- Room data is in-memory only — no persistence across restarts
- Perfect for temporary collaboration sessions
- Web UI works on mobile — great for on-the-go participation

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
