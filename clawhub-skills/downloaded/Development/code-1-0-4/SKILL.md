---
slug: code-1-0-4
name: code-1-0-4
version: "1.0.0"
displayName: Code 1.0.4
summary: Coding workflow with planning, implementation, verification, and testing
  for clean software devel...
license: MIT
description: |-
  Coding workflow with planning, implementation, verification, and testing
  for clean software devel...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: planning, code, implementation, workflow, 1.0.4, coding
tags:
- Development
tools:
- read
- exec
---

# Code 1.0.4

## When to Use

User explicitly requests code implementation. Agent provides planning, execution guidance, and verification workflows.

## Architecture

User preferences stored in `~/code/` when user explicitly requests.

```text
~/code/
  - memory.md    # User-provided preferences only
```

Create on first use: `mkdir -p ~/code`

## Quick Reference

| Topic | File |
| --- | --- |
| Memory setup | `memory-template.md` |
| Task breakdown | `planning.md` |
| Execution flow | `execution.md` |
| Verification | `verification.md` |
| Multi-task state | `state.md` |
| User criteria | `criteria.md` |

## Scope

This skill ONLY:

* Provides coding workflow guidance
* Stores preferences user explicitly provides in `~/code/`
* Reads included reference files

This skill NEVER:

* Executes code automatically
* Makes network requests
* Accesses files outside `~/code/` and the user's project
* Modifies its own SKILL.md or auxiliary files
* Takes autonomous action without user awareness

## Core Rules

### 1. Check Memory First

Read `~/code/memory.md` for user's stated preferences if it exists.

### 2. User Controls Execution

* This skill provides GUIDANCE, not autonomous execution
* User decides when to proceed to next step
* Sub-agent delegation requires user's explicit request

### 3. Plan Before Code

* Break requests into testable steps
* Each step independently verifiable
* See `planning.md` for patterns

### 4. Verify Everything

| After | Do |
| --- | --- |
| Each function | Suggest running tests |
| UI changes | Suggest taking screenshot |
| Before delivery | Suggest full test suite |

### 5. Store Preferences on Request

| User says | Action |
| --- | --- |
| "Remember I prefer X" | Add to memory.md |
| "Never do Y again" | Add to memory.md Never section |

Only store what user explicitly asks to save.

## Workflow

```text
Request -> Plan -> Execute -> Verify -> Deliver
```

## Common Traps

* **Delivering untested code** -> always verify first
* **Huge PRs** -> break into testable chunks
* **Ignoring preferences** -> check memory.md first

## Self-Modification

This skill NEVER modifies its own SKILL.md or auxiliary files.
User data stored only in `~/code/memory.md` after explicit request.

## External Endpoints

This skill makes NO network requests.

| Endpoint | Data Sent | Purpose |
| --- | --- | --- |
| None | None | N/A |

## Security & Privacy

**Data that stays local:**

* Only preferences user explicitly asks to save
* Stored in `~/code/memory.md`

**Data that leaves your machine:**

* None. This skill makes no network requests.

**This skill does NOT:**

* Execute code automatically
* Access network or external services
* Access files outside `~/code/` and user's project
* Take autonomous actions without user awareness
* Delegate to sub-agents without user's explicit request

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
