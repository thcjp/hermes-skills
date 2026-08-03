---
slug: aic-dashboard
name: aic-dashboard
version: "1.8.0"
displayName: Aic Dashboard
summary: "AI Commander管理仪表盘,轻量Web UI监控收件"
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

## 差异化优势分析

AI Commander Dashboard在同类产品中具有以下差异化优势：
1. **轻量级设计**：Dashboard采用轻量级Web UI，确保快速加载和流畅的用户体验，特别适合资源受限的环境。
2. **实时监控**：通过自动刷新机制，用户可以实时监控收件箱和浏览器会话状态，提高工作效率。
3. **安全性**：通过token保护机制，确保只有授权用户可以访问Dashboard，增强数据安全性。
4. **灵活配置**：提供多种环境变量，允许用户根据具体需求调整Dashboard的行为，如端口绑定、数据路径等。
5. **易于集成**：Dashboard可以与多种AI技能无缝集成，如`email-webhook`和`browser-auth`，为用户提供更丰富的监控选项。

## 与同类方案的对比

与市场上其他邮件和浏览器会话监控工具相比，AI Commander Dashboard具有以下优势：
1. **集成性**：Dashboard与AI Commander生态中的其他技能紧密集成，提供一站式监控解决方案。
2. **易用性**：无需复杂配置，即插即用，降低用户使用门槛。
3. **安全性**：通过token保护，防止未授权访问，保护用户数据安全。
4. **灵活性**：支持自定义配置，满足不同用户的需求。

## 解决的真实验证痛点

AI Commander Dashboard旨在解决以下真实验证痛点：
1. **监控效率**：对于需要实时监控邮件和浏览器会话的用户，Dashboard提供了一种高效的方式。
2. **数据安全**：通过token保护机制，确保敏感数据不被未授权访问。
3. **集成需求**：对于使用AI Commander生态中多个技能的用户，Dashboard提供了一个统一的监控平台。

## 技术或方法创新点

AI Commander Dashboard在技术或方法上的创新点包括：
1. **轻量级Web UI**：采用现代Web技术构建，确保快速响应和低资源消耗。
2. **自动刷新机制**：通过定时任务自动刷新数据，提供实时监控体验。
3. **token保护机制**：采用token验证用户身份，增强安全性。

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
