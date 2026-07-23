---
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
summary: "把bot运营状态暴露为JSON,供仪表盘与监控"
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

- This is a coherent monitoring skill, but it exposes sensitive operational
  data and supports host
- 触发关键词: api, status, monitoring, coherent, exposes, bot, test, skill

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

### Q1: 如何开始使用Test？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Test有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
