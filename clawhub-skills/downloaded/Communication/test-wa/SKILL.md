---
slug: test-wa
name: test-wa
version: "1.0.0"
displayName: test
summary: Send WhatsApp messages to other people or search/sync WhatsApp history via
  the wacli CLI (not for...
license: MIT
description: |-
  Send WhatsApp messages to other people or search/sync WhatsApp history
  via the wacli CLI (not for...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: whatsapp, people, messages, send, other, test
tags:
- Communication
tools:
- read
- exec
---

# test

Use `wacli` only when the user explicitly asks you to message someone else on WhatsApp or when they ask to sync/search WhatsApp history.
Do NOT use `wacli` for normal user chats; Clawdbot routes WhatsApp conversations automatically.
If the user is chatting with you on WhatsApp, you should not reach for this tool unless they ask you to contact a third party.

Safety

* Require explicit recipient + message text.
* Confirm recipient + message before sending.
* If anything is ambiguous, ask a clarifying question.

Auth + sync

* `wacli auth` (QR login + initial sync)
* `wacli sync --follow` (continuous sync)
* `wacli doctor`

Find chats + messages

* `wacli chats list --limit 20 --query "name or number"`
* `wacli messages search "query" --limit 20 --chat <jid>`
* `wacli messages search "invoice" --after 2025-01-01 --before 2025-12-31`

History backfill

* `wacli history backfill --chat <jid> --requests 2 --count 50`

Send

* Text: `wacli send text --to "+14155551212" --message "Hello! Are you free at 3pm?"`
* Group: `wacli send text --to "1234567890-123456789@g.us" --message "Running 5 min late."`
* File: `wacli send file --to "+14155551212" --file /path/agenda.pdf --caption "Agenda"`

Notes

* Store dir: `~/.wacli` (override with `--store`).
* Use `--json` for machine-readable output when parsing.
* Backfill requires your phone online; results are best-effort.
* WhatsApp CLI is not needed for routine user chats; it’s for messaging other people.
* JIDs: direct chats look like `<number>@s.whatsapp.net`; groups look like `<id>@g.us` (use `wacli chats list` to find).

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
