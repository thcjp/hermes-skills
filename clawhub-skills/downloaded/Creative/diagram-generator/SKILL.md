---
slug: diagram-generator
name: diagram-generator
version: "1.1.6"
displayName: diagram-generator
summary: "经mcp-diagram-generator MCP生成编辑图"
  this skill for new diag...
license: MIT-0
description: |-
  Generate and edit diagrams with the mcp-diagram-generator MCP server。Use this skill for new diag。Use when 用户需要diagram-generator相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# diagram-generator

## Purpose

Create and edit diagrams by converting user intent into a structured JSON specification, then delegating file generation to the `mcp-diagram-generator` MCP server.

Supported formats:

* Draw.io: `.drawio`
* Mermaid: `.mmd` or markdown Mermaid content
* Excalidraw: `.excalidraw`

Supported work:

* Natural-language diagram creation
* Existing `.drawio`, `.mmd`, and `.excalidraw` edits
* Default output paths under `diagrams/{format}/`
* Custom filenames and output paths

Contact: AlkaidY, `tccio2023@gmail.com`.

## Required MCP Tools

Before generating a diagram, verify that the MCP server tools are available:

* `mcp__mcp-diagram-generator__get_config`
* `mcp__mcp-diagram-generator__generate_diagram`
* `mcp__mcp-diagram-generator__init_config`

If the tools are missing, configure the MCP server.

Recommended remote configuration:

```json
{
  "mcpServers": {
    "mcp-diagram-generator": {
      "command": "npx",
      "args": ["-y", "mcp-diagram-generator"]
    }
  }
}
```

Local development configuration:

```json
{
  "mcpServers": {
    "mcp-diagram-generator": {
      "command": "node",
      "args": ["/absolute/path/to/mcp-diagram-generator/dist/index.js"]
    }
  }
}
```

After changing configuration, restart the agent environment. On first use, the server creates `.diagram-config.json` and default output directories.

## Main Workflow

### 1. Intake

For new diagrams, collect the basic options before accepting or processing the full diagram prompt:

* Diagram type
* Output format
* Layout direction
* Usage context
* Optional filename or output directory

Read `references/interaction-intake-guide.md` before asking intake questions.

Skip intake when the user already provided all required options and the full prompt. For existing-file edits, ask only for the target file and requested changes if missing.

### 2. Dispatch To A Playbook

Select exactly one primary playbook based on the diagram type:

| User Intent | Primary Playbook |
| --- | --- |
| Network topology, datacenter, zone, router, switch, firewall | `references/playbook-network-topology.md` |
| System architecture, application architecture, layered component diagram | `references/playbook-architecture.md` |
| Flowchart, process, decision tree | `references/playbook-flowchart.md` |
| Swimlane, cross-team handoff, approval workflow by department | `references/playbook-swimlane.md` |
| Sequence, class, ER, UML-style diagrams | `references/playbook-uml.md` |
| Whiteboard sketch, hand-drawn style, informal Excalidraw diagram | `references/playbook-excalidraw.md` |
| Unsure about format | `references/format-selection-guide.md` first, then the matching playbook |

Only read the playbook needed for the current diagram. If a playbook points to `json-schema-guide.md` or `network-topology-examples.md`, read only the relevant section.
For explicit geometry, also read `references/layout-quality-guide.md`.

### 3. Choose Format

Use these defaults unless the user explicitly chooses otherwise:

| Diagram Type | Default Format | Default Direction |
| --- | --- | --- |
| Network topology | Draw.io | Vertical |
| Architecture | Draw.io | Vertical or automatic |
| Flowchart | Mermaid | Vertical |
| Swimlane | Draw.io | Horizontal |
| Sequence | Mermaid | Automatic |
| Class | Mermaid | Automatic |
| ER | Mermaid | Automatic |
| Mind map | Mermaid | Automatic |
| Whiteboard sketch | Excalidraw | Automatic |

Usage context can override defaults:

* Word: prefer portrait-friendly vertical layouts.
* PPT: horizontal layouts are acceptable when readability improves.
* Code repositories and documentation: prefer Mermaid for simple flow, sequence, class, and ER diagrams.
* Whiteboard collaboration: prefer Excalidraw.
* Complex network or architecture diagrams: prefer Draw.io unless the user explicitly asks for Excalidraw.

### 4. Build The JSON Specification

Follow `references/json-schema-guide.md` for the schema. Core structure:

```json
{
  "format": "drawio",
  "diagramType": "architecture",
  "title": "Diagram title",
  "elements": [
    {
      "id": "unique-id",
      "type": "container",
      "name": "Display name",
      "level": "environment",
      "geometry": { "x": 0, "y": 0, "width": 800, "height": 600 },
      "children": []
    },
    {
      "type": "edge",
      "source": "source-id",
      "target": "target-id"
    }
  ]
}
```

Universal rules:

* `elements` must be an array.
* IDs must be unique.
* Edges must be top-level elements, never inside `children`.
* Edge `source` and `target` must resolve to an existing node or container.
* `style` must be an object.
* Colors should use `#RRGGBB`.
* Use `fillColor: "none"` for Draw.io no-fill nodes when needed.

### 5. Quality Gate

Before calling the MCP server, verify:

* The chosen format matches the intake answer and playbook.
* `diagramType` is explicit when supported.
* Layout direction is reflected in coordinates or generator-specific fields.
* Complex Draw.io and Excalidraw diagrams have explicit `geometry`.
* Container hierarchy is valid.
* Edges are top-level elements.
* Text and connector rules for the selected format are followed.

After generation, inspect the saved file enough to confirm the expected format-specific properties exist. For code changes to the MCP server, also run `npm run test:diagrams` from `mcp-diagram-generator/`.

### 6. Generate

Preferred call:

```json
{
  "diagram_spec": "<spec object>"
}
```

Optional filename:

```json
{
  "diagram_spec": "<spec object>",
  "filename": "my-diagram.drawio"
}
```

Optional explicit output path:

```json
{
  "diagram_spec": "<spec object>",
  "output_path": "custom/path/to/diagram.drawio"
}
```

The MCP server validates the schema, creates missing directories, and writes to the configured default directory when no output path is supplied.

## Configuration Helpers

Initialize defaults:

```text
init_config()
```

Set custom paths:

```json
{
  "paths": {
    "drawio": "output/diagrams/drawio",
    "mermaid": "output/diagrams/mermaid",
    "excalidraw": "output/diagrams/excalidraw"
  }
}
```

Inspect configuration:

```text
get_config()
```

Update one format path:

```json
{
  "format": "drawio",
  "path": "custom/drawio-path"
}
```

## Troubleshooting

Tool missing:

* Configure the MCP server and restart the agent environment.

Schema validation failed:

* Read `references/json-schema-guide.md`.
* Check required fields, unique IDs, edge source/target, and parent-child structure.

Directory error:

* Check write permissions.
* Run `get_config()`.
* Reinitialize with `init_config()` if needed.

Wrong extension:

* Draw.io uses `.drawio`.
* Mermaid uses `.mmd` or markdown output.
* Excalidraw uses `.excalidraw`.

Nested container issue:

* Child coordinates are relative to the direct parent.
* Container sizes must fit child bounds plus padding.
* Network topology must follow environment -> datacenter -> zone -> device.

## Reference Index

Read only what is needed:

* `references/interaction-intake-guide.md`: interactive intake defaults and question template.
* `references/format-selection-guide.md`: format selection matrix.
* `references/playbook-network-topology.md`: Draw.io and Excalidraw network topology rules.
* `references/playbook-architecture.md`: layered architecture rules.
* `references/playbook-flowchart.md`: process and decision flow rules.
* `references/playbook-swimlane.md`: swimlane and handoff rules.
* `references/playbook-uml.md`: sequence, class, and ER rules.
* `references/playbook-excalidraw.md`: Excalidraw whiteboard and binding rules.
* `references/layout-quality-guide.md`: explicit geometry, spacing, and connector readability rules.
* `references/json-schema-guide.md`: schema details and examples.
* `references/network-topology-examples.md`: network topology JSON patterns.

## Output Discipline

When responding to the user:

* Confirm the selected diagram type, format, direction, and output file.
* Do not paste the full JSON unless the user asks.
* Provide the saved file path.
* Mention any validation or regression command that was run.

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

- Generate and edit diagrams with the mcp-diagram-generator MCP server
- Use this skill for new diag
- 触发关键词: edit, diagram-generator, generator, generate, diagram, diagrams

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

## 常见问题

### Q1: 如何开始使用diagram-generator？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: diagram-generator有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制

- **自然语言描述的复杂性**：技能能够处理简单的自然语言描述，但对于非常复杂或模糊的描述，可能需要用户进一步澄清或提供更详细的输入。
- **文件格式支持**：技能仅支持Draw.io、Mermaid和Excalidraw三种格式的文件生成和编辑，不支持其他格式。
- **文件大小**：生成的文件大小受限于MCP服务器和存储环境，过大文件可能导致生成失败。

### 性能边界

- **并发处理**：技能不支持同时处理多个生成请求，如果需要同时生成多个图表，需要依次提交请求。
- **响应时间**：响应时间取决于MCP服务器的处理速度和当前负载，对于复杂的图表生成，可能需要较长时间。

### 兼容性约束

- **MCP服务器版本**：技能依赖于特定的MCP服务器版本，需要确保MCP服务器版本与技能版本兼容。
- **操作系统**：技能的运行环境需要支持Node.js，因此对操作系统的兼容性有限。

### 其他限制

- **自定义路径**：技能默认输出路径为`diagrams/{format}/`，不支持用户自定义路径的写入权限。
- **外部API**：技能不直接使用外部API，但可能需要通过MCP服务器间接调用外部服务。
- **人工干预**：对于超出技能能力范围的复杂需求，可能需要人工干预或使用其他工具。

