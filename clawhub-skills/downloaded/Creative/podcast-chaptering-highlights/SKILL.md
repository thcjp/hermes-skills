---
slug: podcast-chaptering-highlights
name: podcast-chaptering-highlights
version: "1.0.0"
displayName: Podcast Chaptering Highlights
summary: Create chapters, highlights, and show notes from podcast audio or transcripts.
  Use when a user wa...
license: MIT
description: |-
  Create chapters, highlights, and show notes from podcast audio or transcripts.
  Use when a user wa...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: chaptering, highlights, create, chapters, show, podcast, notes
tags:
- Creative
tools:
- read
- exec
---

# Podcast Chaptering Highlights

## Goal

Produce podcast chapter markers and highlight suggestions with concise show notes.

## Best fit

* Use when the user provides audio files or transcripts.
* Use when the user wants chapter timestamps and titles.
* Use when the user needs highlight clip ideas and show notes.

## Not fit

* Avoid when the user asks to publish or upload to hosting platforms.
* Avoid when rights or consent are unclear.
* Avoid when audio quality is too poor to segment.

## Quick orientation

* `references/overview.md` for workflow and quality bar.
* `references/auth.md` for access and token handling.
* `references/endpoints.md` for optional integrations and templates.
* `references/webhooks.md` for async event handling.
* `references/ux.md` for intake questions and output formats.
* `references/troubleshooting.md` for common issues.
* `references/safety.md` for safety and privacy guardrails.

## Required inputs

* Audio file path or transcript.
* Target chapter format (MM:SS or HH:MM:SS).
* Preferred chapter length range.
* Show description and guest details if available.

## Expected output

* Chapter markers with timestamps and titles.
* Highlight clip suggestions with timestamps.
* Show notes draft with key links or topics.
* Optional social post drafts.

## Operational notes

* Keep chapters aligned to topic shifts.
* Ensure titles are concise and descriptive.
* Provide drafts only; do not publish or upload.

## Security notes

* Treat audio content as private unless told otherwise.
* Avoid sharing raw audio beyond the workspace.

## Safe mode

* Analyze and draft chapters, highlights, and notes only.
* No publishing or distribution actions.

## Sensitive ops

* Uploading or publishing audio is out of scope.

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
