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
  and bundled resources. Use...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: create, write, proper, skills, agent, skill
tags:
- Other
tools:
- read
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

## Advanced features

[Link to separate files: See [REFERENCE.md](REFERENCE.md)]
```

## Description Requirements

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
