---
slug: archive
name: archive
version: "1.0.0"
displayName: Archive
summary: Capture and preserve content as intelligent snapshots with semantic search,
  automatic extraction,...
license: MIT
description: |-
  Capture and preserve content as intelligent snapshots with semantic
  search, automatic extraction,...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: content, archive, intelligent, snapshots, preserve, capture
tags:
- Research
tools:
- read
- exec
---

# Archive

## Architecture

Archive storage lives in `~/archive/` with tiered structure. See `memory-template.md` for setup.

```text
~/archive/
├── memory.md          # HOT: recent items, ≤100 lines
├── index.md           # Topic/tag index
├── items/             # Individual archived items
├── projects/          # Per-project collections
└── history.md         # Search/access history
```

## Quick Reference

| Topic | File |
| --- | --- |
| What to capture | `capture.md` |
| Search patterns | `search.md` |
| Resurfacing rules | `resurface.md` |

## Core Rules

### 1. Capture Complete, Not Just Links

When user sends something to archive:

* Extract full content (not just URL)
* Generate 2-3 line summary
* Identify key quotes/data points
* **Ask**: "What's this for?" — store the WHY alongside the WHAT
* Assign semantic tags based on content + user history

### 2. Content Types

| Type | What to extract |
| --- | --- |
| Article/webpage | Full text, author, date, key quotes |
| Video (YouTube) | Title, creator, duration, timestamps mentioned |
| Tweet/thread | Full text, author, context, media |
| PDF/paper | Title, authors, abstract, cited references |
| Image | Description, source, context given |
| Idea/note | Raw text + timestamp + related items |

### 3. Storage Structure

Each archived item stored as:

```text
items/{date}_{slug}.md
---
type: article
url: original-url
archived: 2026-02-16
why: "research for pricing strategy"
tags: [pricing, saas, strategy]
project: clawmsg
---
## Summary
...
## Key Points
...
## Full Content
...
```

### 4. Semantic Search

User can ask naturally:

* "What did I save about X?" → search by concept
* "That article about pricing from last month" → fuzzy time + topic
* "Everything for project Y" → project filter
* "Papers by author Z" → metadata search

NEVER require exact keywords. Match by meaning.

### 5. Proactive Resurfacing

When user works on a topic:

* Check if archived items relate
* Surface ONLY if genuinely relevant (max 1-2 per session)
* Include context: "You saved this 3 months ago when researching X"

### 6. Never Delete Without Asking

* Old items → mark as "possibly outdated", don't delete
* Duplicates → merge, keep both URLs
* Project closed → archive to cold storage, don't remove

### 7. Differentiation from Other Skills

| This skill | What it does | NOT this |
| --- | --- | --- |
| archive | Preserves external content as snapshots | memory (agent context) |
| archive | Captures full content for permanence | bookmark (just URLs) |
| archive | Stores raw material | second-brain (processed knowledge) |
| archive | Immutable snapshots | pkm (evolving notes) |

## Scope

This skill ONLY:

* Stores content user explicitly sends to archive
* Searches within archived content
* Surfaces related items when contextually relevant

This skill NEVER:

* Monitors or observes without explicit request
* Deletes content without confirmation
* Modifies original archived content
* Accesses external services without user action

## Data Storage

All data in `~/archive/`. Create on first use:

```bash
mkdir -p ~/archive/items ~/archive/projects
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
