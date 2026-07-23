---
slug: memory
name: memory
version: "1.0.2"
displayName: Memory
summary: Infinite organized memory that complements your agent's built-in memory with
  unlimited categorize...
license: MIT
description: |-
  Infinite organized memory that complements your agent's built-in memory
  with unlimited categorize。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Agents
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Memory

**Superpowered memory that never forgets.**

Your agent has basic built-in memory. This skill adds infinite, perfectly organized memory for everything else — parallel and complementary, never conflicting.

## How It Works

```text
Built-in Agent Memory          This Skill (~/memory/)
┌─────────────────────┐        ┌─────────────────────────────┐
│ MEMORY.md           │        │ Infinite categorized storage │
│ memory/ (daily logs)│   +    │ Any structure you want       │
│ Basic recall        │        │ Perfect organization         │
└─────────────────────┘        └─────────────────────────────┘
         ↓                                  ↓
   Agent basics                    Everything else
   (works automatically)           (scales infinitely)
```

**Not a replacement.** Your agent's built-in memory keeps working. This adds a parallel system for unlimited, organized storage.

## Setup

On first use, read `setup.md` to configure the memory system with the user. Key decisions:

1. What categories do they need?
2. Should we sync anything from built-in memory?
3. How do they want to find things?

## When to Use

User needs organized long-term storage beyond basic agent memory: detailed project histories, extensive contact networks, decision logs, domain knowledge, collections, or any structured data that grows over time.

## Architecture

Memory lives in `~/memory/` — a dedicated folder separate from built-in agent memory.

```text
~/memory/
├── config.md              # System configuration
├── INDEX.md               # What's stored, where to find it
│
├── [user-defined]/        # Categories the user needs
│   ├── INDEX.md           # Category overview
│   └── {items}.md         # Individual entries
│
└── sync/                  # Optional: synced from built-in memory
    └── ...
```

**The user defines the categories.** Common examples:

* `projects/` — detailed project context
* `people/` — contact network with full context
* `decisions/` — reasoning behind choices
* `knowledge/` — domain expertise, reference material
* `collections/` — books, recipes, anything they collect

See `memory-template.md` for all templates.

## Quick Reference

| Topic | File |
| --- | --- |
| First-time setup | `setup.md` |
| All templates | `memory-template.md` |
| Organization patterns | `patterns.md` |
| Problems & fixes | `troubleshooting.md` |

---

## Core Rules

### 1. Separate from Built-In Memory

This system lives in `~/memory/`. Never modify:

* Agent's MEMORY.md (workspace root)
* Agent's `memory/` folder (if it exists in workspace)

**Parallel, not replacement.** Both systems work together.

### 2. User Defines Structure

During setup, ask what they want to store. Create categories based on their needs:

| They say... | Create |
| --- | --- |
| "I have many projects" | `~/memory/projects/` |
| "I meet lots of people" | `~/memory/people/` |
| "I want to track decisions" | `~/memory/decisions/` |
| "I'm learning [topic]" | `~/memory/knowledge/[topic]/` |
| "I collect [things]" | `~/memory/collections/[things]/` |

**No preset structure.** Build what they need.

### 3. Every Category Has an Index

Each folder gets an INDEX.md that lists contents:

```markdown

| Name | Status | Updated | File |
|------|--------|---------|------|
| Alpha | Active | 2026-02 | alpha.md |
| Beta | Paused | 2026-01 | beta.md |

Total: 2 active, 5 archived
```

Indices stay small (<100 entries). When full, split into subcategories.

### 4. Write Immediately

When user shares important information:

1. Write to appropriate file in ~/memory/
2. Update the category INDEX.md
3. Then respond

Don't wait. Don't batch. Write immediately.

### 5. Search Then Navigate

To find information:

1. **Ask first:** "Is this in ~/memory/ or built-in memory?"
2. **Search:** grep or semantic search in ~/memory/
3. **Navigate:** INDEX.md → category → specific file

```bash
grep -r "keyword" ~/memory/

cat ~/memory/INDEX.md           # What categories exist?
cat ~/memory/projects/INDEX.md  # What projects?
cat ~/memory/projects/alpha.md  # Specific project
```

### 6. Sync from Built-In (Optional)

If user wants certain info copied from built-in memory:

```text
~/memory/sync/
├── preferences.md    # Synced from built-in
└── decisions.md      # Synced from built-in
```

**Sync is one-way:** Built-in → this system. Never modify built-in.

### 7. Scale by Splitting

When a category grows large:

* INDEX.md > 100 entries → split into subcategories
* Create sub-INDEX.md for each subcategory
* Root INDEX.md points to subcategories

```text
~/memory/projects/
├── INDEX.md           # "See active/, archived/"
├── active/
│   ├── INDEX.md       # 30 active projects
│   └── ...
└── archived/
    ├── INDEX.md       # 200 archived projects
    └── ...
```

---

## What to Store Here (vs Built-In)

| Store HERE (~/memory/) | Keep in BUILT-IN |
| --- | --- |
| Detailed project histories | Current project status |
| Full contact profiles | Key contacts quick-ref |
| All decision reasoning | Recent decisions |
| Domain knowledge bases | Quick facts |
| Collections, inventories | — |
| Anything that grows large | Summaries |

**Rule:** Built-in for quick context. Here for depth and scale.

---

## Finding Things

### For Small Memory (<50 files)

```bash
grep -r "keyword" ~/memory/
```

### For Large Memory (50+ files)

Navigate via indices:

```text
1. ~/memory/INDEX.md → find category
2. ~/memory/{category}/INDEX.md → find item
3. ~/memory/{category}/{item}.md → read details
```

### For Huge Memory (500+ files)

Use semantic search if available, or hierarchical indices:

```text
~/memory/projects/INDEX.md → "web projects in web/"
~/memory/projects/web/INDEX.md → "alpha project"
~/memory/projects/web/alpha.md → details
```

---

## Maintenance

### Weekly (5 min)

* Update INDEX.md files if entries added
* Archive completed/inactive items

### Monthly (15 min)

* Review category sizes
* Split large categories
* Remove outdated entries

### When Memory is Slow

* Check INDEX.md sizes (keep <100 lines)
* Split big categories into subcategories
* Archive old content

---

## Common Traps

* **Modifying built-in memory** → Never touch agent's MEMORY.md or workspace memory/. This system is parallel.
* **No indices** → Without INDEX.md, finding things requires searching all files. Always maintain indices.
* **One giant category** → 500 items in one folder is slow. Split into subcategories.
* **Syncing everything** → Don't copy all built-in memory. Only sync what needs organization here.
* **Waiting to write** → Write immediately when user shares info. Don't batch.

---

## Security & Privacy

**Data location:**

* All data in `~/memory/` on user's machine
* No external services required
* No network requests

**This skill does NOT:**

* Access built-in agent memory (only reads if syncing)
* Send data anywhere
* Store credentials (never store secrets in memory)

---

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `decide` - Decision tracking patterns
* `escalate` - When to involve humans
* `learn` - Adaptive learning

## Feedback

* If useful: `
* Stay updated: `

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

- Infinite organized memory that complements your agent's built-in memory
  with unlimited categorize
- 触发关键词: organized, memory, infinite, complements'

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

### Q1: 如何开始使用Memory？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Memory有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
