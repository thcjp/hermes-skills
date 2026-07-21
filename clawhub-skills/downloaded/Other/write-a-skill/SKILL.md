---
slug: write-a-skill
name: write-a-skill
version: "202.0.20"
displayName: Write A Skill
summary: Create new agent skills with proper structure, progressive disclosure, and
  bundled resources. Use...
license: MIT-0
description: |-
  Create new agent skills with proper structure, progressive disclosure,
  and bundled resources。Use。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Other
tools:
  - - read
- exec
---

# Write A Skill

## Process

1. **Gather requirements** - ask user about:

   * What task/domain does the skill cover?
   * What specific use cases should it handle?
   * Does it need executable scripts or just instructions?
   * Any reference materials to include?
2. **Draft the skill** - create:

   * SKILL.md with concise instructions
   * Additional reference files if content exceeds 500 lines
   * Utility scripts if deterministic operations needed
3. **Review with user** - present draft and ask:

   * Does this cover your use cases?
   * Anything missing or unclear?
   * Should any section be more/less detailed?

## Skill Structure

```text
skill-name/
├── SKILL.md           # Main instructions (required)
├── REFERENCE.md       # Detailed docs (if needed)
├── EXAMPLES.md        # Usage examples (if needed)
└── scripts/           # Utility scripts (if needed)
    └── helper.js
```

## SKILL.md Template

```md
---
name: skill-name
description: Brief description of capability. Use when [specific triggers].
---

## Quick start

[Minimal working example]

## Workflows

[Step-by-step processes with checklists for complex tasks]

## 核心能力

[Link to separate files: See [REFERENCE.md](REFERENCE.md)]
```

## 依赖说明

The description is **the only thing your agent sees** when deciding which skill to load. It's surfaced in the system prompt alongside all other installed skills. Your agent reads these descriptions and picks the relevant skill based on the user's request.

**Goal**: Give your agent just enough info to know:

1. What capability this skill provides
2. When/why to trigger it (specific keywords, contexts, file types)

**Format**:

* Max 1024 chars
* Write in third person
* First sentence: what it does
* Second sentence: "Use when [specific triggers]"

**Good example**:

```text
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
```

**Bad example**:

```text
Helps with documents.
```

The bad example gives your agent no way to distinguish this from other document skills.

## When to Add Scripts

Add utility scripts when:

* Operation is deterministic (validation, formatting)
* Same code would be generated repeatedly
* Errors need explicit handling

Scripts save tokens and improve reliability vs generated code.

## When to Split Files

Split into separate files when:

* SKILL.md exceeds 100 lines
* Content has distinct domains (finance vs sales schemas)
* Advanced features are rarely needed

## Review Checklist

After drafting, verify:

* Description includes triggers ("Use when...")
* SKILL.md under 100 lines
* No time-sensitive info
* Consistent terminology
* Concrete examples included
* References one level deep

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
[Minimal working example]
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Write A Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Write A Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
