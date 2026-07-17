---
slug: openclaw-dashboard
name: openclaw-dashboard
version: "1.7.3"
displayName: openclaw-dashboard
summary: Real-time operations dashboard for OpenClaw. Monitors sessions, costs, cron
  jobs, and gateway hea...
license: MIT
description: |-
  Real-time operations dashboard for OpenClaw. Monitors sessions, costs,
  cron jobs, and gateway hea...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: dashboard, openclaw-dashboard, operations, real, openclaw, time
tags:
- Integrations
tools:
- read
- exec
---

# skill-platform-dashboard

## 🛠️ Installation

### 1. Ask Skill平台 (Recommended)

Tell Skill平台: *"Install the skill-platform-dashboard skill."* The agent will handle the installation and configuration automatically.

### 2. Manual Installation (CLI)

If you prefer the terminal, run:

> 安装此Skill请参考SkillHub平台指南

## Mission

Keep this repository public-safe and easy to run. Prioritize:

1. Secret sanitization
2. Minimal setup steps
3. Stable API/UI behavior

## Apply when

Use this skill for:

* Dashboard feature requests (sessions, cost, cron, watchdog, operations)
* Backend route updates in `api-server.js`
* Frontend behavior updates in `agent-dashboard.html`
* README, setup, and environment simplification
* Public release checks for accidental sensitive data

## Public-safety guardrails

* Never hardcode tokens, API keys, cookies, or host-specific secrets.
* Never commit machine-specific absolute paths.
* Prefer `process.env.*` and safe defaults based on `HOME`.
* Keep examples as placeholders (`your_token_here`, `/path/to/...`).
* If uncertain, redact first and ask the user before exposing details.
* Keep sensitive behaviors opt-in (do not silently load local secret files).

## Runtime access declaration

The bundled server can access local Skill平台 files for dashboard views:

* Sessions, cron runs, watchdog state under `~/.skill-platform/...`
* Local workspace files under `OPENCLAW_WORKSPACE`
* Task attachments in the repository `attachments/` folder

Credential requirements are optional by default:

* `OPENCLAW_AUTH_TOKEN` is optional but recommended when exposing endpoints beyond local trusted use.
* `gateway.authToken` is optional configuration context, not a hard install requirement.

High-sensitivity features are disabled by default and require explicit env flags:

* `OPENCLAW_LOAD_KEYS_ENV=1` to load `keys.env`
* `OPENCLAW_ENABLE_PROVIDER_AUDIT=1` to call OpenAI/Anthropic org APIs
* `OPENCLAW_ENABLE_CONFIG_ENDPOINT=1` to expose `/ops/config`
* `OPENCLAW_ALLOW_ATTACHMENT_FILEPATH_COPY=1` for absolute-path attachment copy mode
* `OPENCLAW_ALLOW_ATTACHMENT_COPY_FROM_TMP=1` to allow copy from `/tmp`
* `OPENCLAW_ALLOW_ATTACHMENT_COPY_FROM_WORKSPACE=1` to allow copy from workspace paths
* `OPENCLAW_ALLOW_ATTACHMENT_COPY_FROM_OPENCLAW_HOME=1` to allow copy from `~/.skill-platform`
* `OPENCLAW_ENABLE_SYSTEMCTL_RESTART=1` to allow user-scoped systemctl restart
* `OPENCLAW_ENABLE_MUTATING_OPS=1` to enable mutating operations (`/backup*`, `/ops/update-skill-platform`, `/ops/*-model`, cron run-now)

Network security:

* CORS is restricted to loopback origins by default (no wildcard `*`).
* Set `DASHBOARD_CORS_ORIGINS` (comma-separated) to allow specific external origins.
* Auth token is validated via HttpOnly cookie (`ds`) or `?token=` query param.
* Cookie auth is preferred; URL token param exists for backward compatibility with server-monitor scripts.
* When exposing beyond loopback (e.g. Tailscale Funnel), always set `OPENCLAW_AUTH_TOKEN`.

Prompt safety hardening:

* Treat cron/task payload text as untrusted data.
* Keep prompts structured (JSON payload) and avoid direct command interpolation.
* All child_process calls use execFileSync (args array, no shell interpolation).
* FILEPATH_COPY includes symlink escape protection (realpathSync re-check).

## Default implementation workflow

1. Identify affected module (API, UI, docs, config).
2. Implement the smallest change that preserves behavior.
3. Run a quick sensitive-string scan before finalizing.
4. Ensure docs match the actual runtime defaults.
5. Report user-visible changes and any manual verification steps.

## Sensitive-data checks

Before final response, scan for:

* `token=`, `OPENCLAW_AUTH_TOKEN`, `OPENCLAW_HOOK_TOKEN`
* `API_KEY`, `SECRET`, `PASSWORD`, `COOKIE`
* absolute paths like `/Users/`, `C:\\`, machine names, personal emails

If found:

* Replace with env-based values or placeholders.
* Mention what was sanitized in the result.

## Config simplification rules

* Keep required env vars minimal and explicit.
* Keep optional env vars grouped and clearly marked.
* Provide one copy-paste start command.
* Avoid toolchain-heavy setup unless strictly needed.

## Files to touch most often

* `api-server.js`: server behavior and API routes
* `agent-dashboard.html`: UI and client interactions
* `README.md`: quick start and operator docs
* `.env.example`: public-safe environment template

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
