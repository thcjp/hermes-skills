---
slug: note
name: note
version: "2.1.0"
displayName: Note
summary: Knowledge capture and connection system with automatic organization and retrieval.
  Use when user ...
license: MIT-0
description: |-
  Knowledge capture and connection system with automatic organization
  and retrieval. Use when user ...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: knowledge, system, connection, note, capture
tags:
- Productivity
tools:
- read
- exec
---

# Note

Knowledge capture system. Remember everything, find anything.

## Critical Privacy & Safety

### Data Storage (CRITICAL)

* **All notes stored locally only**: `memory/notes/`
* **No cloud note services** connected
* **No external sync** - pure local storage
* **No sharing** of notes or ideas
* User controls all data retention and deletion

### Data Structure

Notes stored in your local workspace:

* `memory/notes/notes.json` - All captured notes
* `memory/notes/topics.json` - Automatic topic categorization
* `memory/notes/projects.json` - Project-based organization
* `memory/notes/connections.json` - Connections between notes
* `memory/notes/search_index.json` - Search optimization

## Core Workflows

### Capture Note

```text
User: "Note: The insight from the book about feedback loops applies to our onboarding problem"
→ Use scripts/capture_note.py --content "Feedback loops from book apply to onboarding" --context "reading"
→ Extract note, identify topics, store automatically
```

### Find Relevant Notes

```text
User: "What have I written about onboarding?"
→ Use scripts/find_notes.py --query "onboarding" --context current
→ Surface all notes related to onboarding, including unexpected connections
```

### Prepare for Meeting

```text
User: "I'm meeting with Sarah tomorrow"
→ Use scripts/prep_meeting.py --person "Sarah"
→ Pull all previous notes about Sarah, her projects, commitments made
```

### Connect Ideas

```text
User: "This reminds me of something I read last month"
→ Use scripts/connect_notes.py --current-note "NOTE-123" --search "last month"
→ Find and surface related notes, create explicit connection
```

### Transform to Knowledge

```text
User: "Synthesize my notes on product strategy"
→ Use scripts/synthesize.py --topic "product-strategy"
→ Transform scattered notes into coherent framework
```

## Module Reference

* **Capture System**: See [references/capture.md](/api/v1/skills/note/file?path=references%2Fcapture.md&ownerHandle=agenticio)
* **Automatic Organization**: See [references/organization.md](/api/v1/skills/note/file?path=references%2Forganization.md&ownerHandle=agenticio)
* **Retrieval & Search**: See [references/retrieval.md](/api/v1/skills/note/file?path=references%2Fretrieval.md&ownerHandle=agenticio)
* **Connection Building**: See [references/connections.md](/api/v1/skills/note/file?path=references%2Fconnections.md&ownerHandle=agenticio)
* **Knowledge Synthesis**: See [references/synthesis.md](/api/v1/skills/note/file?path=references%2Fsynthesis.md&ownerHandle=agenticio)
* **Meeting Preparation**: See [references/meeting-prep.md](/api/v1/skills/note/file?path=references%2Fmeeting-prep.md&ownerHandle=agenticio)

## Scripts Reference

| Script | Purpose |
| --- | --- |
| `capture_note.py` | Capture note from any context |
| `find_notes.py` | Search and retrieve relevant notes |
| `prep_meeting.py` | Prepare notes for meeting |
| `connect_notes.py` | Explicitly connect related notes |
| `synthesize.py` | Transform notes into knowledge |
| `review_recent.py` | Review recent captures |
| `organize_project.py` | Organize notes by project |
| `build_map.py` | Build knowledge map across domains |

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
