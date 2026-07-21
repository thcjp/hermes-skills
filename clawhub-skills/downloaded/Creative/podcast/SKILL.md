---
slug: podcast
name: podcast
version: "1.0.1"
displayName: Podcast
summary: Create and grow podcasts by planning episodes, producing audio or video,
  generating clips, and bu...
license: MIT
description: |-
  Create and grow podcasts by planning episodes, producing audio or video,
  generating clips, and bu。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。
tags:
- Creative
tools:
  - - read
- exec
---

# Podcast

## Core Workflow

Every podcast follows: Concept → Plan → Record/Generate → Edit → Publish → Promote.

Before starting ANY podcast:

1. **Format** — Solo, interview, panel, narrative, or AI-generated
2. **Niche** — Specific topic + audience (not "business" but "bootstrapped SaaS founders")
3. **Cadence** — Weekly, biweekly, or seasonal (consistency > frequency)

## Project Structure

```text
~/podcasts/<show>/
├── brand/              # Cover art, intro/outro, music
├── episodes/           # One folder per episode
│   └── 001/
│       ├── outline.md
│       ├── recording.mp3
│       ├── transcript.md
│       ├── show-notes.md
│       └── clips/
├── guests.md           # Guest tracker + relationship notes
└── analytics.md        # Performance patterns
```

## Episode Checklist

Pre-production:

* Topic researched, angle clear
* Outline/script with hooks and transitions
* Guest prep (if interview): questions + research

Post-production:

* Audio cleaned, levels normalized
* Show notes with timestamps
* 3-5 clips extracted for social
* Thumbnail (if video)

## Quick Reference

| Need | Load |
| --- | --- |
| Format-specific guidance (solo, interview, panel) | `formats.md` |
| Audio and video production techniques | `production.md` |
| AI-generated podcast creation | `ai-generation.md` |
| Growth, SEO, social, monetization | `growth.md` |
| Episode planning, scripts, show notes | `episodes.md` |
| Tools, platforms, APIs | `tools.md` |

## Critical Rules

1. **Hook in first 30 seconds** — State the value, tease the best moment
2. **Consistency beats perfection** — Ship on schedule, improve incrementally
3. **Clips are growth engine** — Every episode = 3-5 social clips minimum
4. **Engage the niche** — Better to own a small audience than chase a big one
5. **Video is optional but powerful** — YouTube podcast search is growing fast

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

- Create and grow podcasts by planning episodes, producing audio or video,
  generating clips, and bu
- 触发关键词: grow, create, planning, episodes, podcasts, podcast

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

### Q1: 如何开始使用Podcast？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Podcast有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
