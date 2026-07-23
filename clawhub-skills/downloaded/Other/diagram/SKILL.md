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
  for architecture, flows, seq。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Generate diagrams from descriptions with Mermaid, PlantUML, or ASCII
  for architecture, flows, seq
- 触发关键词: descriptions, diagrams, generate, diagram

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

### Q1: 如何开始使用Diagram？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Diagram有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
