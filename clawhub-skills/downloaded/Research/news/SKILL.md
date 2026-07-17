---
slug: news
name: news
version: "1.0.1"
displayName: News
summary: Personalized news briefings that learn your interests, formats, and timing
  preferences.
license: MIT
description: |-
  Personalized news briefings that learn your interests, formats, and
  timing preferences.

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: personalized, briefings, learn, news
tags:
- Research
tools:
- read
- exec
---

# News

## When to Use

User wants personalized news briefings. Agent builds a news profile, delivers formatted briefings, learns interests over time, and handles multi-source coverage.

## Architecture

Memory lives in `~/news/`. See `memory-template.md` for setup.

```text
~/news/
├── memory.md       # Profile: interests, format, timing
├── history.md      # Past briefings and engagement
└── sources.md      # Trusted sources and biases
```

## Quick Reference

| Topic | File |
| --- | --- |
| Memory setup | `memory-template.md` |

## Core Rules

### 1. Build Profile Before Delivering

On first interaction, ask about:

* Specific interests (not generic categories)
* Proportions if multiple interests ("70% AI, 30% markets")
* Format preference (bullets, narrative, headlines-only)
* Timing (morning, evening, weekly, on-demand)

### 2. Check Memory First

Before every briefing, read `~/news/memory.md` for user preferences. Tailor content to their stated interests and format.

### 3. Facts First, Analysis Second

Lead with what happened before why it matters. Always include when news broke. Cite sources by name.

### 4. Multi-Source on Contested Topics

Present at least 2 sources when covering controversy. Note when sources disagree. State editorial leanings when relevant.

### 5. Never Fabricate

If uncertain whether something happened, say so. Never assume or invent news events.

### 6. Update Memory from Engagement

Track which stories user engages with vs skips. Periodically suggest profile adjustments based on patterns.

## Common Traps

* Presenting stale news as fresh → destroys trust
* Single-source on controversy → reckless reporting
* Generic categories ("tech") → ask for specifics ("AI startups")
* Overwhelming with items → morning briefings max 5-7 items

## Security & Privacy

**Data that stays local:**

* User preferences in `~/news/`
* Engagement history in `~/news/history.md`

**This skill does NOT:**

* Send data to external services
* Access files outside `~/news/`
* Store news content permanently

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `summarizer` — condense long articles
* `scrape` — extract web content
* `reading` — reading lists and tracking

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
