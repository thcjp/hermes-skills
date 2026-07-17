---
slug: learn
name: learn
version: "1.0.2"
displayName: Learn
summary: Structure and track learning with spaced repetition and active recall across
  any domain.
license: MIT
description: |-
  Structure and track learning with spaced repetition and active recall
  across any domain.

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: track, spaced, learn, structure, learning
tags:
- Knowledge
tools:
- read
- exec
---

# Learn

## Data Storage

```text
~/learn/
├── topics/              # One folder per topic
│   └── {topic}/
│       ├── concepts.json   # Concepts with SR schedule
│       ├── notes.md        # Study notes
│       └── progress.md     # Mastery tracking
├── reviews/             # Due review queue
│   └── due.json
└── config.json          # Preferences
```

Create on first use: `mkdir -p ~/learn/{topics,reviews}`

## Scope

This skill:

* ✅ Creates learning plans in ~/learn/
* ✅ Tracks concepts with spaced repetition
* ✅ Generates quizzes for active recall
* ✅ Reminds user when reviews are due (stores schedule in ~/learn/reviews/)
* ❌ NEVER accesses external learning platforms without permission
* ❌ NEVER stores data outside ~/learn/

## Quick Reference

| Topic | File |
| --- | --- |
| Cognitive principles | `cognition.md` |
| Spaced repetition math | `retention.md` |
| Verification methods | `verification.md` |

## Core Rules

### 1. Workflow

```text
Goal → Plan → Study → Practice → Verify → Review
```

### 2. Active Recall Only

NEVER passive review. Always:

* Ask question first, user answers
* Then show correct answer
* User rates: easy / good / hard / wrong

### 3. Starting a Topic

1. User states what they want to learn
2. Create ~/learn/topics/{topic}/
3. Break down into concepts
4. Add to spaced repetition queue

### 4. Spaced Repetition

In concepts.json:

```json
{
  "concept_name": {
    "added": "2024-03-15",
    "interval_days": 1,
    "next_review": "2024-03-16",
    "ease_factor": 2.5,
    "reviews": 0
  }
}
```

After each review:

* Correct → increase interval (×ease_factor)
* Incorrect → reset to 1 day

### 5. Verification

Before marking "mastered":

* Generate 5 questions covering concept
* User must answer 4/5 correctly
* Track in progress.md (topic folder)

### 6. Configuration

In ~/learn/config.json:

```json
{
  "depth": "standard",
  "learner_type": "practical",
  "daily_review_limit": 20
}
```

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
