---
slug: powerpoint
name: powerpoint
version: "1.0.0"
displayName: PowerPoint
summary: Control PowerPoint app sessions, slides, notes, export, and presentation
  state with osascript wor...
license: MIT-0
description: |-
  Control PowerPoint app sessions, slides, notes, export, and presentation
  state with osascript wor...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: sessions, slides, powerpoint, control, notes
tags:
- Other
tools:
- read
- exec
---

# PowerPoint

## When to Use

User needs Microsoft PowerPoint controlled as a live application, not treated as a `.pptx` file format.
Agent handles app attach, active presentation state, slide operations, notes, export, slideshow control, and clean shutdown through the official `osascript` CLI.
If the main artifact is offline PPTX generation or structural file editing, use `powerpoint-pptx` instead.

## Architecture

Memory lives in `~/powerpoint/`. If `~/powerpoint/` does not exist, run `setup.md`. See `memory-template.md` for structure.

```text
~/powerpoint/
├── memory.md             # Environment facts, safe defaults, and last working control path
├── incidents.md          # Reusable failures and proven recovery steps
└── deck-notes.md         # Non-sensitive notes about trusted decks, layouts, and export targets
```

## Quick Reference

Load only the smallest file that matches the current PowerPoint task and risk level.

| Topic | File |
| --- | --- |
| Setup guide | `setup.md` |
| Memory template | `memory-template.md` |
| Interface selection | `execution-matrix.md` |
| Live control patterns | `live-control-patterns.md` |
| Destructive action guardrails | `safety-checklist.md` |
| Debug and recovery | `troubleshooting.md` |

## Requirements

* Microsoft PowerPoint installed locally.
* macOS with `osascript` available.
* Explicit confirmation before destructive presentation actions.

## Core Rules

### 1. Choose the app-control path by presentation state

* Use `osascript` for live PowerPoint control through the app's scripting dictionary.
* Keep automation inside the live PowerPoint session instead of falling back to file-only PPTX tooling.
* Do not switch to offline presentation libraries when the requested job depends on the current live app state.

### 2. Identify the exact presentation, slide, and window before acting

* Confirm whether the target is the active presentation, a named open deck, or a path to open now.
* Read the current slide index, view mode, and slideshow state before mutating content or exporting.
* Never assume the frontmost deck is the intended one.

### 3. Read before write, then verify the final state

* Pre-read presentation name, active slide, notes state, or export target before mutation.
* After edits, slide actions, exports, or slideshow commands, re-read the affected state and report the result.
* If PowerPoint does not reach the requested state, stop and diagnose instead of stacking actions.

### 4. Treat slide-order and layout actions as high-risk

* Moving, duplicating, deleting, or reordering slides can break references, animations, and presenter flow.
* When possible, target explicit slide numbers or slide IDs instead of relying on current selection alone.
* If slide identity is ambiguous, clarify first.

### 5. Separate reversible view actions from destructive deck cleanup

* Changing view mode, starting a slideshow, and exporting are usually reversible.
* Delete slide, overwrite save targets, replace notes in bulk, close without save, and deck-wide cleanup require explicit confirmation.
* Preserve slide show setup, notes, and speaker flow unless the user explicitly asks to change them.

### 6. Keep provenance explicit

* State whether the target deck was already open or opened just for this task.
* Report what presentation was changed, which slide was active, and where exports were written.
* Preserve user-owned open decks that were outside the task scope.

### 7. Recover cleanly and avoid orphaned app sessions

* If you opened PowerPoint just for this task, keep ownership clear and close only what you created.
* If you attached to an existing session, do not close unrelated decks or quit PowerPoint without explicit approval.
* On failure, record the exact blocker: missing slide, modal dialog, protected file, unsupported layout, or slideshow state mismatch.

## PowerPoint Traps

* Treating a live deck like a static `.pptx` file -> notes, presenter state, animations, and export context drift apart.
* Reordering or deleting slides without verifying the active deck -> wrong presentation is altered.
* Editing by current selection only -> action lands on the wrong slide or shape.
* Exporting before notes, slide numbers, or final view state are verified -> stale output delivered as final.
* Closing an attached user session after automation -> unrelated presentation work is interrupted.
* Ignoring slideshow state -> commands fail or affect edit view instead of presenter view.

## Security & Privacy

**Data that stays local:**

* Presentation paths, environment notes, and reusable fixes in `~/powerpoint/`.
* Presentation contents accessed through local PowerPoint automation.

**Data that may leave your machine:**

* Nothing by default from this skill itself.
* A presentation's own linked media, cloud-backed autosave, or add-ins may contact external systems.

**This skill does NOT:**

* Use cloud slide APIs or OAuth flows.
* Disable presentation warnings silently.
* Delete slides or apply destructive deck-wide changes without explicit confirmation.
* Bypass PowerPoint protection prompts.

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `office` — Broader Office task routing across documents, spreadsheets, and presentations.
* `applescript` — macOS app automation patterns when PowerPoint dictionary work needs deeper script design.
* `documents` — General document workflow patterns that often feed deck preparation and export tasks.

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
