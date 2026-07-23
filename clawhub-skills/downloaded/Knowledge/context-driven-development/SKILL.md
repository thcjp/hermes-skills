---
slug: context-driven-development
name: context-driven-development
version: "1.0.0"
displayName: Context Driven Devel
summary: Treat project context as a managed artifact alongside code. Use structured
  context documents (pro...
license: MIT
description: |-
  Treat project context as a managed artifact alongside code。Use structured
  context documents (pro。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Context Driven Development

Treat project context as a first-class artifact managed alongside code. Instead of relying on ad-hoc prompts or scattered documentation, establish a persistent, structured foundation that informs all AI interactions.

## Installation

### Skill平台 / Moltbot / Clawbot

```bash
npx SkillHub@latest install context-driven-development
```

## WHAT This Skill Does

Creates and maintains a set of context documents that:

* Define what you're building and why (product.md)
* Specify technology choices and constraints (tech-stack.md)
* Establish how the team works (workflow.md)
* Track what's happening (tracks.md)

## WHEN to Use

**Use for:**

* Setting up new projects with AI-assisted development
* Onboarding team members to existing codebases
* Ensuring consistent AI behavior across sessions
* Documenting decisions that affect code generation
* Managing projects with multiple contributors or AI assistants

**Skip for:**

* Solo experiments or throwaway prototypes
* Single-file scripts
* Projects without AI assistance

**Keywords:** context, project setup, documentation, AI alignment, team workflow, product vision, tech stack

## Core Philosophy

```text
Context precedes code.
Living documentation.
Single source of truth.
AI alignment.
```

1. **Context precedes code** — Define what you're building and how before implementation
2. **Living documentation** — Context artifacts evolve with the project
3. **Single source of truth** — One canonical location for each type of information
4. **AI alignment** — Consistent context produces consistent AI behavior

## The Workflow

```text
Context → Spec & Plan → Implement
```

1. **Context Phase:** Establish or verify project context artifacts exist and are current
2. **Specification Phase:** Define requirements and acceptance criteria for work units
3. **Planning Phase:** Break specifications into phased, actionable tasks
4. **Implementation Phase:** Execute tasks following established workflow patterns

## The Context Documents

### product.md — WHAT and WHY

Purpose: Captures product vision, goals, target users, and business context.

**Contents:**

* Product name and one-line description
* Problem statement and solution approach
* Target user personas
* Core features and capabilities
* Success metrics and KPIs
* Product roadmap (high-level)

**Update when:**

* Product vision or goals change
* New major features are planned
* Target audience shifts

### tech-stack.md — WITH WHAT

Purpose: Documents technology choices, dependencies, and architectural decisions.

**Contents:**

* Primary languages and frameworks
* Key dependencies with versions
* Infrastructure and deployment targets
* Development tools and environment
* Testing frameworks
* Code quality tools

**Update when:**

* Adding new dependencies
* Upgrading major versions
* Changing infrastructure
* Adopting new tools or patterns

### workflow.md — HOW to Work

Purpose: Establishes development practices, quality gates, and team workflows.

**Contents:**

* Development methodology (TDD, trunk-based, etc.)
* Git workflow and commit conventions
* Code review requirements
* Testing requirements and coverage targets
* Quality assurance gates
* Deployment procedures

**Update when:**

* Team practices evolve
* Quality standards change
* New workflow patterns are adopted

### tracks.md — WHAT'S HAPPENING

Purpose: Registry of all work units with status and metadata.

**Contents:**

* Active tracks with current status
* Completed tracks with completion dates
* Track metadata (type, priority, assignee)
* Links to individual track specs

**Update when:**

* New work starts
* Work status changes
* Work completes

## Directory Structure

```text
context/
├── product.md            # Product vision and goals
├── tech-stack.md         # Technology choices
├── workflow.md           # Development practices
├── tracks.md             # Work unit registry
└── styleguides/          # Language-specific conventions
    ├── python.md
    ├── typescript.md
    └── ...
```

## Setup: New Project (Greenfield)

For new projects, create all artifacts from scratch:

1. **Create `context/product.md`:**

   * Define the problem you're solving
   * Describe target users
   * List core features for v1
   * Define success metrics
2. **Create `context/tech-stack.md`:**

   * Choose languages and frameworks
   * Document key dependencies with versions
   * Specify infrastructure targets
   * List development tools
3. **Create `context/workflow.md`:**

   * Define branching strategy
   * Set commit conventions
   * Establish testing requirements
   * Document deployment process
4. **Create `context/tracks.md`:**

   * Start with empty registry
   * Add work units as they're created

## Setup: Existing Project (Brownfield)

For existing codebases, extract context from what exists:

1. **Analyze the codebase:**

   * Read package.json, requirements.txt, go.mod, etc.
   * Look at existing README and docs
   * Check git history for patterns
2. **Create `context/tech-stack.md`:**

   * Document discovered dependencies
   * Note infrastructure from configs (Docker, CI, etc.)
3. **Create `context/product.md`:**

   * Infer product purpose from code
   * Document current feature set
   * Note any README content
4. **Create `context/workflow.md`:**

   * Document existing practices
   * Note any established patterns

## Maintenance Principles

### Keep Artifacts Synchronized

Changes in one artifact should reflect in related documents:

* New feature in product.md → Update tech-stack.md if new dependencies needed
* Completed track → Update product.md to reflect new capabilities
* Workflow change → Update all affected track plans

### 依赖说明

Before adding any new dependency:

1. Check if existing dependencies solve the need
2. Document the rationale for new dependencies
3. Add version constraints
4. Note any configuration requirements

### Verify Context Before Implementation

Before starting any work:

1. Read all context artifacts
2. Flag any outdated information
3. Propose updates before proceeding
4. Confirm context accuracy

## Validation Checklist

Before starting implementation, validate:

**Product Context:**

* product.md reflects current vision
* Target users are accurately described
* Feature list is up to date

**Technical Context:**

* tech-stack.md lists all current dependencies
* Version numbers are accurate
* Infrastructure targets are correct

**Workflow Context:**

* workflow.md describes current practices
* Quality gates are defined
* Commit conventions are documented

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
| --- | --- | --- |
| Stale Context | Documents become outdated and misleading | Update context as part of each track's completion |
| Context Sprawl | Information scattered across multiple locations | Use defined artifact structure; resist new document types |
| Implicit Context | Relying on knowledge not captured in artifacts | If referenced repeatedly, add to appropriate artifact |
| Over-Specification | Context so detailed it's impossible to maintain | Keep focused on decisions affecting AI behavior and team alignment |

## Session Continuity

### Starting a New Session

1. Read context/product.md to orient yourself
2. Check context/tracks.md for active work
3. Read relevant track specs for current task
4. Verify context artifacts are current

### Ending a Session

1. Update track status with current progress
2. Note any blockers or decisions made
3. Commit in-progress work with clear status
4. Update tracks.md if status changed

## Benefits

**Team Alignment:**

* New team members onboard faster with explicit context
* Consistent terminology across the team
* Shared understanding of product goals

**AI Consistency:**

* AI assistants produce aligned outputs across sessions
* Reduced need to re-explain context
* Predictable behavior based on documented standards

**Institutional Memory:**

* Decisions and rationale are preserved
* Context survives team changes
* Historical context informs future decisions

## NEVER Do

1. **NEVER start implementation without reading context** — context precedes code
2. **NEVER add dependencies without updating tech-stack.md** — keep the source of truth current
3. **NEVER let context documents get stale** — update them as part of completing work
4. **NEVER scatter context across ad-hoc documents** — use the defined structure
5. **NEVER assume AI remembers previous sessions** — context must be in artifacts
6. **NEVER skip context for "quick" changes** — small changes compound into drift

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

## 核心能力

- Treat project context as a managed artifact alongside code
- Use structured
  context documents (pro
- 触发关键词: project, development, treat, driven, context, artifact, managed

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

### Q1: 如何开始使用Context Driven Devel？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Context Driven Devel有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
