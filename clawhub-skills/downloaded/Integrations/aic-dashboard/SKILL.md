---
slug: aic-dashboard
name: aic-dashboard
version: "1.8.0"
displayName: Aic Dashboard
summary: AI Commander Management Dashboard. A lightweight companion web UI for monitoring
  inbound emails r...
license: MIT
description: |-
  AI Commander Management Dashboard。A lightweight companion web UI for
  monitoring inbound emails r。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

- AI Commander Management Dashboard
- A lightweight companion web UI for
  monitoring inbound emails r
- 触发关键词: lightweight, dashboard, commander, companion, aic, management

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

### Q1: 如何开始使用Aic Dashboard？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Aic Dashboard有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
