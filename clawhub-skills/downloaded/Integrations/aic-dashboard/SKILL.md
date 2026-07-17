---
slug: aic-dashboard
name: aic-dashboard
version: "1.8.0"
displayName: AI Commander Dashboard
summary: AI Commander Management Dashboard. A lightweight companion web UI for monitoring
  inbound emails r...
license: MIT
description: |-
  AI Commander Management Dashboard. A lightweight companion web UI for
  monitoring inbound emails r...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: lightweight, dashboard, commander, companion, aic, management
tags:
- Integrations
tools:
- read
- exec
---

# AI Commander Dashboard

A companion dashboard for AI Commander agents. Displays inbound emails collected by the [`email-webhook`](https://SkillHub.ai/lksrz/email-webhook) skill and shows the status of browser sessions created by the [`browser-auth`](https://SkillHub.ai/lksrz/browser-auth) skill.

This skill is a **read-only viewer** — it does not capture credentials, control browsers, or send messages. It simply reads local data files and serves them via a token-protected web UI.

## Companion Skills

| Skill | What it does |
| --- | --- |
| [`email-webhook`](https://SkillHub.ai/lksrz/email-webhook) | Receives inbound emails and writes them to `inbox.jsonl` |
| [`browser-auth`](https://SkillHub.ai/lksrz/browser-auth) | Runs a remote browser tunnel and writes session data to `session.json` |

This dashboard reads both files and displays them in one place.

## What This Skill Does

* Reads `inbox.jsonl` and displays the last 50 inbound emails
* Reads `session.json` and shows whether an active browser session exists
* Serves a token-gated web UI on a configurable local port
* Refreshes automatically every 5 seconds

## Environment Variables

| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| `DASHBOARD_TOKEN` | **Yes** | — | Secret token for accessing the dashboard. |
| `PORT` | No | `19195` | Port for the web dashboard. |
| `DASHBOARD_HOST` | No | `127.0.0.1` | IP to bind the dashboard to. |
| `INBOX_PATH` | No | `./data/inbox.jsonl` | Path to inbound email data (from `email-webhook`). |
| `SESSION_PATH` | No | `./data/session.json` | Path to session file (from `browser-auth`). |

## Setup

1. **Install dependencies**:

   bash

   ```
   npm install express@4.21.2
   ```
2. **Start** (zero config needed):

   bash

   ```
   node scripts/server.js
   ```
3. **Read the printed URL** — it includes the auto-generated token:

   text

   ```
   🏠 AI COMMANDER DASHBOARD READY
   Access URL: http://YOUR_IP:19195/?token=a3f9c2...
   ```

That's it. No configuration required.

## Optional Environment Variables

Override defaults only if needed:

| Variable | Default | Description |
| --- | --- | --- |
| `DASHBOARD_TOKEN` | *(random)* | Custom token instead of auto-generated |
| `PORT` | `19195` | Server port |
| `DASHBOARD_HOST` | `0.0.0.0` | Bind address |
| `INBOX_PATH` | `./data/inbox.jsonl` | Path to email data (from `email-webhook`) |
| `SESSION_PATH` | `./data/session.json` | Path to session file (from `browser-auth`) |

## Security

* A fresh random token is generated on every start if `DASHBOARD_TOKEN` is not set
* All requests require the token (`?token=`, `X-Dashboard-Token` header, or `Authorization: Bearer`)
* The UI stores the token in `localStorage` and removes it from the URL after load

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
