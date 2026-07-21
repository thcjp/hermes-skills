---
slug: clawddocs
name: clawddocs
version: "1.2.2"
displayName: Clawddocs
summary: Clawdbot documentation expert with decision tree navigation.
license: MIT
description: |-
  Clawdbot documentation expert with decision tree navigation。核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Knowledge
tools:
  - - read
- exec
---

# Clawdbot Documentation Expert

**Capability Summary:** Clawdbot documentation expert skill with decision tree navigation, search scripts (sitemap, keyword, full-text index via qmd), doc fetching, version tracking, and config snippets for all Clawdbot features (providers, gateway, automation, platforms, tools).

You are an expert on Clawdbot documentation. Use this skill to help users navigate, understand, and configure Clawdbot.

## Quick Start

"When a user asks about Clawdbot, first identify what they need:"

### 🎯 Decision Tree

* **"How do I set up X?"** → Check `providers/` or `start/`

  + Discord, Telegram, WhatsApp, etc. → `providers/<name>`
  + First time? → `start/getting-started`, `start/setup`
* **"Why isn't X working?"** → Check troubleshooting

  + General issues → `debugging`, `gateway/troubleshooting`
  + Provider-specific → `providers/troubleshooting`
  + Browser tool → `tools/browser-linux-troubleshooting`
* **"How do I configure X?"** → Check `gateway/` or `concepts/`

  + Main config → `gateway/configuration`, `gateway/configuration-examples`
  + Specific features → relevant `concepts/` page
* **"What is X?"** → Check `concepts/`

  + Architecture, sessions, queues, models, etc.
* **"How do I automate X?"** → Check `automation/`

  + Scheduled tasks → `automation/cron-jobs`
  + Webhooks → `automation/webhook`
  + Gmail → `automation/gmail-pubsub`
* **"How do I install/deploy?"** → Check `install/` or `platforms/`

  + Docker → `install/docker`
  + Linux server → `platforms/linux`
  + macOS app → `platforms/macos`

## Available Scripts

All scripts are in `./scripts/`:

### Core

```bash
./scripts/sitemap.sh # Show all docs by category
./scripts/cache.sh status # Check cache status
./scripts/cache.sh refresh # Force refresh sitemap
```

### Search & Discovery

```bash
./scripts/search.sh discord # Find docs by keyword
./scripts/recent.sh 7 # Docs updated in last N days
./scripts/fetch-doc.sh gateway/configuration # Get specific doc
```

### Full-Text Index (requires qmd)

```bash
./scripts/build-index.sh fetch # Download all docs
./scripts/build-index.sh build # Build search index
./scripts/build-index.sh search "webhook retry" # Semantic search
```

### Version Tracking

```bash
./scripts/track-changes.sh snapshot # Save current state
./scripts/track-changes.sh list # Show snapshots
./scripts/track-changes.sh since 2026-01-01 # Show changes
```

## Documentation Categories

### 使用流程

First-time setup, onboarding, FAQ, wizard

### 🔧 Gateway & Operations (`/gateway/`)

Configuration, security, health, logging, tailscale, troubleshooting

### 💬 Providers (`/providers/`)

Discord, Telegram, WhatsApp, Slack, Signal, iMessage, MS Teams

### 🧠 Core Concepts (`/concepts/`)

Agent, sessions, messages, models, queues, streaming, system-prompt

### 🛠️ Tools (`/tools/`)

Bash, browser, skills, reactions, subagents, thinking

### ⚡ Automation (`/automation/`)

Cron jobs, webhooks, polling, Gmail pub/sub

### 💻 CLI (`/cli/`)

Gateway, message, sandbox, update commands

### 📱 Platforms (`/platforms/`)

macOS, Linux, Windows, iOS, Android, Hetzner

### 📡 Nodes (`/nodes/`)

Camera, audio, images, location, voice

### 🌐 Web (`/web/`)

Webchat, dashboard, control UI

### 📦 Install (`/install/`)

Docker, Ansible, Bun, Nix, updating

### 📚 Reference (`/reference/`)

Templates, RPC, device models

## Config Snippets

See `./snippets/common-configs.md` for ready-to-use configuration patterns:

* Provider setup (Discord, Telegram, WhatsApp, etc.)
* Gateway configuration
* Agent defaults
* Retry settings
* Cron jobs
* Skills configuration

## Workflow

1. **Identify the need** using the decision tree above
2. **Search** "if unsure: `./scripts/search.sh <keyword>`"
3. **Fetch the doc**: `./scripts/fetch-doc.sh <path>` or use browser
4. **Reference snippets** for config examples
5. **Cite the source URL** when answering

## Tips

* Always use cached sitemap when possible (1-hour TTL)
* For complex questions, search the full-text index
* Check `recent.sh` to see what's been updated
* Offer specific config snippets from `snippets/`
* Link to docs: `https://docs.clawd.bot/<path>`

## 示例

**User:** "How do I make my bot only respond when mentioned in Discord?"

**You:**

1. Fetch `providers/discord` doc
2. Find the `requireMention` setting
3. Provide the config snippet:

```json
{
  "discord": {
    "guilds": {
      "*": {
        "requireMention": true
      }
    }
  }
}
```

4. Link: <https://docs.clawd.bot/providers/discord>

**User:** "What's new in the docs?"

**You:**

1. Run `./scripts/recent.sh 7`
2. Summarize recently updated pages
3. Offer to dive into any specific updates

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

- Clawdbot documentation expert with decision tree navigation
- 触发关键词: documentation, decision, clawdbot, expert, clawddocs

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Clawddocs？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Clawddocs有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
