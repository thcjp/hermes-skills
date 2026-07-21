---
slug: podcast-chaptering-highlights
name: podcast-chaptering-highlights
version: "1.0.0"
displayName: Podcast Chaptering H
summary: Create chapters, highlights, and show notes from podcast audio or transcripts.
  Use when a user wa...
license: MIT
description: |-
  Create chapters, highlights, and show notes from podcast audio or transcripts。Use when a user wa。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
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

- Create chapters, highlights, and show notes from podcast audio or transcripts
- Use when a user wa
- 触发关键词: chaptering, highlights, create, chapters, show, podcast, notes

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

### Q1: 如何开始使用Podcast Chaptering H？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Podcast Chaptering H有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
