---
slug: mermaid-diagram
name: mermaid-diagram
version: "1.0.0"
displayName: Mermaid Diagram
summary: "生成有效Mermaid图,流程/时序/思维导图/ER图(社区下载版)"
  maps, ER diagrams, or us...
license: MIT-0
description: |-
  Generate valid Mermaid diagrams like flowcharts, sequence diagrams,
  mind maps, ER diagrams, or us。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Mermaid Diagram

Generate valid Mermaid diagram code from text descriptions.

## Diagram Type Selection

| 需求 | 推荐类型 | Mermaid 关键字 |
| --- | --- | --- |
| 业务流程 / 逻辑流程 | Flowchart | `flowchart TD` |
| 系统交互 / API 时序 | Sequence | `sequenceDiagram` |
| 产品架构 / 系统结构 | Flowchart / C4 | `flowchart LR` |
| 状态机 / 用户状态 | State | `stateDiagram-v2` |
| 脑图 / 功能树 | Mindmap | `mindmap` |
| 数据库结构 | ER | `erDiagram` |
| 项目时间线 | Timeline | `timeline` |
| 用户旅程 | Journey | `journey` |

## Output Rules

1. Always wrap output in ```` ```mermaid ```` code blocks
2. Use Chinese labels when the user writes in Chinese
3. Add comments (`%%`) for complex diagrams to explain sections
4. Keep node names short (≤10 chars) to avoid layout issues
5. Validate syntax mentally before outputting — common mistakes:
   * Missing quotes around labels with spaces/Chinese
   * Wrong arrow syntax (`-->` vs `---` vs `->>`)
   * Unclosed brackets

## Quick Syntax Reference

```text
flowchart TD
    A[开始] --> B{判断条件}
    B -- 是 --> C[执行操作]
    B -- 否 --> D[结束]
    C --> D
```

```text
sequenceDiagram
    用户->>服务端: 发起请求
    服务端->>数据库: 查询数据
    数据库-->>服务端: 返回结果
    服务端-->>用户: 响应
```

```text
mindmap
  root((产品名))
    功能A
      子功能1
      子功能2
    功能B
```

## Reference Files

* **references/diagram-patterns.md** — 产品经理常用图模式（带完整示例代码）

Read when: user asks for a specific diagram type or needs a complex multi-node diagram.

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

- Generate valid Mermaid diagrams like flowcharts, sequence diagrams,
  mind maps, ER diagrams, or us
- 触发关键词: generate, diagrams, valid, diagram, mermaid

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

### Q1: 如何开始使用Mermaid Diagram？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Mermaid Diagram有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
