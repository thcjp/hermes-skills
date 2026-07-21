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
  and retrieval。Use when user。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Productivity
tools:
  - - read
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

- Knowledge capture and connection system with automatic organization
  and retrieval
- Use when user
- 触发关键词: knowledge, system, connection, note, capture

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

### Q1: 如何开始使用Note？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Note有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
