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
  generating clips, and bu...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: grow, create, planning, episodes, podcasts, podcast
tags:
- Creative
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
