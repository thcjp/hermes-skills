---
slug: mermaid-diagram
name: mermaid-diagram
version: "1.0.0"
displayName: Mermaid Diagram
summary: Generate valid Mermaid diagrams like flowcharts, sequence diagrams, mind
  maps, ER diagrams, or us...
license: MIT-0
description: |-
  Generate valid Mermaid diagrams like flowcharts, sequence diagrams,
  mind maps, ER diagrams, or us...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generate, diagrams, valid, diagram, mermaid
tags:
- Development
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
