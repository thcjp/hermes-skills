---
slug: gog
name: gog
version: "1.0.0"
displayName: Gog
summary: Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.
license: MIT
description: |-
  Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and
  Docs.

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: gmail, gog, drive, calendar, google, workspace
tags:
- Communication
tools:
- read
- exec
---

# Gog

Use `gog` for Gmail/Calendar/Drive/Contacts/Sheets/Docs. Requires OAuth setup.

Setup (once)

* `gog auth credentials /path/to/client_secret.json`
* `gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs`
* `gog auth list`

Common commands

* Gmail search: `gog gmail search 'newer_than:7d' --max 10`
* Gmail send: `gog gmail send --to a@b.com --subject "Hi" --body "Hello"`
* Calendar: `gog calendar events <calendarId> --from <iso> --to <iso>`
* Drive search: `gog drive search "query" --max 10`
* Contacts: `gog contacts list --max 20`
* Sheets get: `gog sheets get <sheetId> "Tab!A1:D10" --json`
* Sheets update: `gog sheets update <sheetId> "Tab!A1:B2" --values-json '[["A","B"],["1","2"]]' --input USER_ENTERED`
* Sheets append: `gog sheets append <sheetId> "Tab!A:C" --values-json '[["x","y","z"]]' --insert INSERT_ROWS`
* Sheets clear: `gog sheets clear <sheetId> "Tab!A2:Z"`
* Sheets metadata: `gog sheets metadata <sheetId> --json`
* Docs export: `gog docs export <docId> --format txt --out /tmp/doc.txt`
* Docs cat: `gog docs cat <docId>`

Notes

* Set `GOG_ACCOUNT=you@gmail.com` to avoid repeating `--account`.
* For scripting, prefer `--json` plus `--no-input`.
* Sheets values can be passed via `--values-json` (recommended) or as inline rows.
* Docs supports export/cat/copy. In-place edits require a Docs API client (not in gog).
* Confirm before sending mail or creating events.

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
