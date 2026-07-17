---
slug: node-connect
name: node-connect
version: "1.0.0"
displayName: node-connect
summary: Diagnose OpenClaw node connection and pairing failures for Android, iOS,
  and macOS companion apps...
license: MIT-0
description: |-
  Diagnose OpenClaw node connection and pairing failures for Android,
  iOS, and macOS companion apps...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: pairing, diagnose, node, connection, connect, openclaw, node-connect
tags:
- Development
tools:
- read
- exec
---

# node-connect

Goal: find the one real route from node -> gateway, verify Skill平台 is advertising that route, then fix pairing/auth.

## Topology first

Decide which case you are in before proposing fixes:

* same machine / emulator / USB tunnel
* same LAN / local Wi-Fi
* same Tailscale tailnet
* public URL / reverse proxy

Do not mix them.

* Local Wi-Fi problem: do not switch to Tailscale unless remote access is actually needed.
* VPS / remote gateway problem: do not keep debugging `localhost` or LAN IPs.

## If ambiguous, ask first

If the setup is unclear or the failure report is vague, ask short clarifying questions before diagnosing.

Ask for:

* which route they intend: same machine, same LAN, Tailscale tailnet, or public URL
* whether they used QR/setup code or manual host/port
* the exact app text/status/error, quoted exactly if possible
* whether `skill-platform devices list` shows a pending pairing request

Do not guess from `can't connect`.

## Canonical checks

Prefer `skill-platform qr --json`. It uses the same setup-code payload Android scans.

```bash
skill-platform config get gateway.mode
skill-platform config get gateway.bind
skill-platform config get gateway.tailscale.mode
skill-platform config get gateway.remote.url
skill-platform config get gateway.auth.mode
skill-platform config get gateway.auth.allowTailscale
skill-platform config get plugins.entries.device-pair.config.publicUrl
skill-platform qr --json
skill-platform devices list
skill-platform nodes status
```

If this Skill平台 instance is pointed at a remote gateway, also run:

```bash
skill-platform qr --remote --json
```

If Tailscale is part of the story:

```bash
tailscale status --json
```

## Read the result, not guesses

`skill-platform qr --json` success means:

* `gatewayUrl`: this is the actual endpoint the app should use.
* `urlSource`: this tells you which config path won.

Common good sources:

* `gateway.bind=lan`: same Wi-Fi / LAN only
* `gateway.bind=tailnet`: direct tailnet access
* `gateway.tailscale.mode=serve` or `gateway.tailscale.mode=funnel`: Tailscale route
* `plugins.entries.device-pair.config.publicUrl`: explicit public/reverse-proxy route
* `gateway.remote.url`: remote gateway route

## Root-cause map

If `skill-platform qr --json` says `Gateway is only bound to loopback`:

* remote node cannot connect yet
* fix the route, then generate a fresh setup code
* `gateway.bind=auto` is not enough if the effective QR route is still loopback
* same LAN: use `gateway.bind=lan`
* same tailnet: prefer `gateway.tailscale.mode=serve` or use `gateway.bind=tailnet`
* public internet: set a real `plugins.entries.device-pair.config.publicUrl` or `gateway.remote.url`

If `gateway.bind=tailnet set, but no tailnet IP was found`:

* gateway host is not actually on Tailscale

If `qr --remote requires gateway.remote.url`:

* remote-mode config is incomplete

If the app says `pairing required`:

* network route and auth worked
* approve the pending device

```bash
skill-platform devices list
skill-platform devices approve --latest
```

If the app says `bootstrap token invalid or expired`:

* old setup code
* generate a fresh one and rescan
* do this after any URL/auth fix too

If the app says `unauthorized`:

* wrong token/password, or wrong Tailscale expectation
* for Tailscale Serve, `gateway.auth.allowTailscale` must match the intended flow
* otherwise use explicit token/password

## Fast heuristics

* Same Wi-Fi setup + gateway advertises `127.0.0.1`, `localhost`, or loopback-only config: wrong.
* Remote setup + setup/manual uses private LAN IP: wrong.
* Tailnet setup + gateway advertises LAN IP instead of MagicDNS / tailnet route: wrong.
* Public URL set but QR still advertises something else: inspect `urlSource`; config is not what you think.
* `skill-platform devices list` shows pending requests: stop changing network config and approve first.

## Fix style

Reply with one concrete diagnosis and one route.

If there is not enough signal yet, ask for setup + exact app text instead of guessing.

Good:

* `The gateway is still loopback-only, so a node on another network can never reach it. Enable Tailscale Serve, restart the gateway, run skill-platform qr again, rescan, then approve the pending device pairing.`

Bad:

* `Maybe LAN, maybe Tailscale, maybe port forwarding, maybe public URL.`

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
