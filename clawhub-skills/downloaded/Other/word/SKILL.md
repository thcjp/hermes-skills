---
slug: word
name: word
version: "1.0.0"
displayName: Word
summary: Control Word app sessions, documents, selections, comments, export, and review
  state with osascri...
license: MIT-0
description: |-
  Control Word app sessions, documents, selections, comments, export,
  and review state with osascri...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: selections, sessions, word, documents, control
tags:
- Other
tools:
- read
- exec
---

# Word

## When to Use

User needs Microsoft Word controlled as a live application, not treated as a `.docx` file format.
Agent handles app attach, active document state, selection-aware edits, comments, track changes, export, and clean shutdown through the official `osascript` CLI.
If the main artifact is offline DOCX creation or structural file editing, use `word-docx` instead.

## Architecture

Memory lives in `~/word/`. If `~/word/` does not exist, run `setup.md`. See `memory-template.md` for structure.

```text
~/word/
├── memory.md             # Environment facts, safe defaults, and last working control path
├── incidents.md          # Reusable failures and proven recovery steps
└── document-notes.md     # Non-sensitive notes about trusted documents, views, and export targets
```

## Quick Reference

Load only the smallest file that matches the current Word task and risk level.

| Topic | File |
| --- | --- |
| Setup guide | `setup.md` |
| Memory template | `memory-template.md` |
| Interface selection | `execution-matrix.md` |
| Live control patterns | `live-control-patterns.md` |
| Destructive action guardrails | `safety-checklist.md` |
| Debug and recovery | `troubleshooting.md` |

## Requirements

* Microsoft Word installed locally.
* macOS with `osascript` available.
* Explicit confirmation before destructive document actions.

## Core Rules

### 1. Choose the app-control path by document state

* Use `osascript` for live Word document control through the app's scripting dictionary.
* Keep automation inside the live Word session instead of falling back to file-only DOCX tooling.
* Do not switch to offline document libraries when the requested job depends on the current live Word app state.

### 2. Identify the exact document and view before acting

* Confirm whether the target is the active document, a named open document, or a path to open now.
* Read the current view, selection, and review mode before making edits tied to cursor position or markup state.
* Never assume the frontmost Word window is the intended document.

### 3. Read before write, then verify the final state

* Pre-read document name, current selection, target paragraph, comment count, or export target before mutation.
* After edits, comments, accept/reject actions, or exports, re-read the affected state and report what changed.
* If Word does not reach the requested state, stop and diagnose instead of layering more edits.

### 4. Treat selection-driven actions as high-risk

* Selection-based commands can land in the wrong paragraph, story range, header, or comment balloon.
* When possible, anchor the action to a specific document object instead of only the current insertion point.
* If the selection context is ambiguous, clarify first.

### 5. Separate reversible review actions from destructive cleanup

* Adding comments, changing view, and exporting are usually reversible.
* Accept all changes, reject all changes, remove comments, close without save, and overwrite exports require explicit confirmation.
* If review state matters, preserve track changes and display settings unless the user explicitly asks to change them.

### 6. Keep provenance explicit

* State whether the target was already open or opened just for this task.
* Report what document was changed, which review mode was active, and where exports were written.
* Preserve user-owned open documents that were outside the task scope.

### 7. Recover cleanly and avoid orphaned app sessions

* If you opened Word just for this task, keep ownership clear and close only what you created.
* If you attached to an existing session, do not close unrelated documents or quit Word without explicit approval.
* On failure, record the exact blocker: protected document, modal dialog, compatibility mode, track changes mismatch, or missing permissions.

## Word Traps

* Treating a live document like a static `.docx` file -> review state, comments, fields, and view context drift apart.
* Writing relative to the current cursor without verifying selection -> text lands in the wrong story range.
* Accepting or rejecting changes globally when only one section was intended -> irreversible editorial loss.
* Exporting before fields, references, or TOC are updated -> stale output delivered as final.
* Closing an attached user session after automation -> unrelated writing work is interrupted.
* Ignoring protected view or tracked-change mode -> edits silently fail or create the wrong markup history.

## Security & Privacy

**Data that stays local:**

* Document paths, environment notes, and reusable fixes in `~/word/`.
* Document contents accessed through local Word automation.

**Data that may leave your machine:**

* Nothing by default from this skill itself.
* A document's own links, add-ins, macros, or cloud-backed autosave behavior may contact external systems.

**This skill does NOT:**

* Use Microsoft Graph, cloud document APIs, or OAuth flows.
* Disable review warnings silently.
* Accept destructive document-wide changes without explicit confirmation.
* Bypass Word protection prompts.

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `word-docx` — Offline DOCX generation and editing when Word does not need to stay open.
* `office` — Broader Office task routing across documents, spreadsheets, and presentations.
* `applescript` — macOS app automation patterns when Word dictionary work needs deeper script design.

## Feedback

* If useful: `
* Stay updated: `

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
