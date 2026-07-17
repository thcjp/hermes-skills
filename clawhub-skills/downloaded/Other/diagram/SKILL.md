---
slug: diagram
name: diagram
version: "1.0.0"
displayName: Diagram
summary: Generate diagrams from descriptions with Mermaid, PlantUML, or ASCII for
  architecture, flows, seq...
license: MIT
description: |-
  Generate diagrams from descriptions with Mermaid, PlantUML, or ASCII
  for architecture, flows, seq...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: descriptions, diagrams, generate, diagram
tags:
- Other
tools:
- read
- exec
---

# Diagram

## Principle

Diagrams should **clarify, not complicate**. Start simple, add detail only when needed. A 5-box flowchart beats a 50-node sprawl.

## When User Describes a System or Flow

1. **Identify diagram type** — Is this a flow, architecture, sequence, or data model?
2. **Choose format** — Mermaid (default), PlantUML (complex), ASCII (inline), SVG (custom)
3. **Draft minimal version** — Core elements only, no decoration
4. **Iterate** — Add detail based on feedback

## Diagram Types

| Type | Use For | Format |
| --- | --- | --- |
| Flowchart | Processes, decisions, workflows | Mermaid `flowchart` |
| Sequence | API calls, interactions, protocols | Mermaid `sequenceDiagram` |
| Architecture | System components, infrastructure | Mermaid `flowchart` or `C4` |
| ER/Data model | Database schemas, relationships | Mermaid `erDiagram` |
| Class | Object structure, inheritance | Mermaid `classDiagram` |
| State | Lifecycles, status transitions | Mermaid `stateDiagram-v2` |
| Timeline | Project phases, history | Mermaid `timeline` |
| Mindmap | Brainstorming, concept mapping | Mermaid `mindmap` |

## Output Methods

| Method | When |
| --- | --- |
| Mermaid code block | User can render (docs, GitHub, Notion) |
| Render to PNG/SVG | User needs image file |
| ASCII inline | Quick sketch in chat |
| HTML + Mermaid.js | Interactive viewing |

### Rendering Mermaid to Image

```bash
npx -y @mermaid-js/mermaid-cli mmdc -i diagram.mmd -o diagram.png -b transparent

```

## Mermaid Quick Reference

**Flowchart:**

Rendering diagram...

**Sequence:**

Rendering diagram...

**ER Diagram:**

Rendering diagram...

## Style Guidelines

* **Left-to-right (LR)** for processes, **top-to-bottom (TB)** for hierarchies
* **Max 10-15 nodes** per diagram, split if larger
* **Consistent naming** — all caps for systems, lowercase for actions
* **Subgraphs** to group related components
* **Color sparingly** — highlight critical paths only

## Common Requests

| Request | Interpret As |
| --- | --- |
| "Draw my API flow" | Sequence diagram: client → API → services |
| "Show the architecture" | Flowchart with subgraphs for components |
| "Database schema" | ER diagram with relationships |
| "How the auth works" | Sequence or flowchart depending on complexity |
| "User journey" | Flowchart with decision points |

## Anti-Patterns

* ❌ Too many nodes (split into multiple diagrams)
* ❌ Decorative icons without meaning
* ❌ Mixing abstraction levels (database tables next to business concepts)
* ❌ Arrows in all directions (confuses flow)
* ❌ Labels too long (use short names, add legend if needed)

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
