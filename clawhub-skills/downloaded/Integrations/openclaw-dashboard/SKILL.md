---
slug: openclaw-dashboard
name: openclaw-dashboard
version: "1.7.3"
displayName: openclaw-dashboard
summary: "OpenClaw实时运营仪表盘,监控会话/成本/cron/网关"
  jobs, and gateway hea...
license: MIT
description: |-
  Real-time operations dashboard for OpenClaw。Monitors sessions, costs,
  cron jobs, and gateway hea。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
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

- Real-time operations dashboard for OpenClaw
- Monitors sessions, costs,
  cron jobs, and gateway hea
- 触发关键词: dashboard, openclaw-dashboard, operations, real, openclaw, time

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

### Q1: 如何开始使用openclaw-dashboard？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: openclaw-dashboard有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
