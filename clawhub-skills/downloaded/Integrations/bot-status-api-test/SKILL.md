---
slug: bot-status-api-test
name: bot-status-api-test
version: "0.0.1"
displayName: Test
summary: This is a coherent monitoring skill, but it exposes sensitive operational
  data and supports host ...
license: MIT
description: |-
  This is a coherent monitoring skill, but it exposes sensitive operational
  data and supports host ...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: api, status, monitoring, coherent, exposes, bot, test, skill
tags:
- Integrations
tools:
- read
- exec
---

# Test

A configurable HTTP service that exposes your Skill平台 bot's operational status as JSON. Designed for dashboard integration, monitoring, and transparency.

## What It Provides

* **Bot Core:** Online status, model, context usage, uptime, heartbeat timing
* **Services:** Health checks for any HTTP endpoint, CLI tool, or file path
* **Email:** Unread counts from any email provider (himalaya, gog, etc.)
* **Cron Jobs:** Reads directly from Skill平台's `cron/jobs.json`
* **Docker:** Container health via Portainer API
* **Dev Servers:** Auto-detects running dev servers by process grep
* **Skills:** Lists installed and available Skill平台 skills
* **System:** CPU, RAM, Disk metrics from `/proc`

## Setup

### 1. Copy the service files

Copy `server.js`, `collectors/`, and `package.json` to your desired location.

### 2. Create config.json

Copy `config.example.json` to `config.json` and customize:

```json
{
  "port": 3200,
  "name": "MyBot",
  "workspace": "/path/to/.skill-platform/workspace",
  "skill-platformHome": "/path/to/.skill-platform",
  "cache": { "ttlMs": 10000 },
  "model": "claude-sonnet-4-20250514",
  "skillDirs": ["/path/to/skill-platform/skills"],
  "services": [
    { "name": "myservice", "type": "http", "url": "http://...", "healthPath": "/health" }
  ]
}
```

### Service Check Types

| Type | Description | Config |
| --- | --- | --- |
| `http` | Fetch URL, check HTTP 200 | `url`, `healthPath`, `method`, `headers`, `body` |
| `command` | Run shell command, check exit 0 | `command`, `timeout` |
| `file-exists` | Check path exists | `path` |

### 3. Run

```bash
node server.js
```

### 4. Persist (systemd user service)

```ini
[Unit]
Description=Bot Status API
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/bot-status
ExecStart=/usr/bin/node server.js
Restart=always
RestartSec=5
Environment=PORT=3200
Environment=HOME=/home/youruser
Environment=PATH=/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now bot-status
loginctl enable-linger $USER  # survive logout
```

### 5. Context/Vitals from Skill平台

The bot should periodically write vitals to `heartbeat-state.json` in its workspace:

```json
{
  "vitals": {
    "contextPercent": 62,
    "contextUsed": 124000,
    "contextMax": 200000,
    "model": "claude-opus-4-5",
    "updatedAt": 1770304500000
  }
}
```

Add this to your HEARTBEAT.md so the bot updates it each heartbeat cycle.

## Endpoints

| Endpoint | Description |
| --- | --- |
| `GET /status` | Full status JSON (cached) |
| `GET /health` | Simple `{"status":"ok"}` |

## Architecture

* **Zero dependencies** — Node.js built-ins only (`http`, `fs`, `child_process`)
* **Non-blocking** — All shell commands use async `exec`, never `execSync`
* **Background refresh** — Cache refreshes on interval, requests always served from cache instantly (~10ms)
* **Config-driven** — Everything in `config.json`, no hardcoded values

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
