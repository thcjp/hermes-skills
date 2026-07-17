---
slug: dashboard
name: dashboard
version: "1.0.1"
displayName: Dashboard
summary: Build custom dashboards from any data source with local hosting and visual
  QA loops.
license: MIT
description: |-
  Build custom dashboards from any data source with local hosting and
  visual QA loops.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: custom, dashboard, build, data, dashboards
tags:
- Other
tools:
- read
- exec
---

# Dashboard

## Data Storage

```text
~/dashboard/
├── registry.json           # Dashboard index
├── {name}/
│   ├── config.json         # Layout, widgets
│   ├── data.json           # Current data
│   └── index.html          # Dashboard page
```

Create on first use: `mkdir -p ~/dashboard`

## Scope

This skill:

* ✅ Generates static HTML dashboards
* ✅ Creates fetch scripts user can run
* ✅ Stores dashboards in ~/dashboard/

**User-driven model:**

* User specifies data sources
* User provides API credentials via environment
* User runs fetch scripts (cron or manual)
* Skill generates HTML and fetch scripts

This skill does NOT:

* ❌ Access credentials without user providing them
* ❌ Run automated fetches (user's cron runs scripts)
* ❌ Scrape services without user consent

## Quick Reference

| Topic | File |
| --- | --- |
| Data source patterns | `sources.md` |
| Visual design rules | `design.md` |
| Widget templates | `widgets.md` |

## Core Rules

### 1. User Provides Data

When creating a dashboard:

```text
User: "Dashboard for my Stripe revenue"
Agent: "I'll create a fetch script. Set STRIPE_API_KEY
        in your environment, then run the script."
→ Generates: ~/dashboard/stripe/fetch.sh
→ User adds to cron: */15 * * * * ~/dashboard/stripe/fetch.sh
```

### 2. Architecture

```text
[User's Cron] → [fetch.sh] → [data.json] → [index.html]
                    ↓
              Uses $API_KEY from env
```

Agent generates scripts. User runs them.

### 3. Fetch Script Template

```bash
#!/bin/bash
curl -s -u "$STRIPE_API_KEY:" \
  https://api.stripe.com/v1/balance \
  | jq '.' > ~/dashboard/stripe/data.json
```

### 4. Visual QA (Before Delivery)

* Open in browser, take screenshot
* Check: no overlap, readable fonts (≥14px), good contrast
* If issues → fix → repeat
* Only deliver after visual validation

### 5. Design Defaults

| Element | Value |
| --- | --- |
| Background | `#0f172a` (dark) / `#f8fafc` (light) |
| Text | `#e2e8f0` (dark) / `#1e293b` (light) |
| Spacing | 16px, 24px, 32px |
| Corners | 8px |
| KPI | 48-72px number, 14px label |

### 6. Security

* Credentials via env vars, never in files
* Dashboards on `127.0.0.1` by default
* No PII in displayed data
* User adds auth if exposing to network

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
