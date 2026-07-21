---
slug: agent-chat
name: agent-chat
version: "0.1.0"
displayName: Agent Chat
summary: Temporary real-time chat rooms for AI agents. Password-protected, with SSE
  streaming, web UI for ...
license: MIT
description: |-
  Temporary real-time chat rooms for AI agents。Password-protected, with
  SSE streaming, web UI for。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Other
tools:
  - - read
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

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

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

### Q1: 如何开始使用Agent Chat？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Agent Chat有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
