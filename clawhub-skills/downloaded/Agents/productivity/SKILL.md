---
slug: productivity
name: productivity
version: "1.0.4"
displayName: Productivity
summary: Plan, focus, and complete work with energy management, time blocking, goals,
  projects, tasks, hab...
license: MIT-0
description: |-
  Plan, focus, and complete work with energy management, time blocking,
  goals, projects, tasks, hab。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Agents
tools:
  - - read
- exec
---

# Productivity

## When to Use

Use this skill when the user wants a real productivity system, not just one-off motivation. It should cover goals, projects, tasks, habits, planning, reviews, overload triage, and situation-specific constraints in one coherent operating model.

## Architecture

Productivity lives in `~/productivity/`. If `~/productivity/` does not exist yet, run `setup.md`.

```text
~/productivity/
├── memory.md                 # Work style, constraints, energy, preferences
├── inbox/
│   ├── capture.md            # Quick capture before sorting
│   └── triage.md             # Triage rules and current intake
├── dashboard.md              # High-level direction and current focus
├── goals/
│   ├── active.md             # Outcome goals and milestones
│   └── someday.md            # Goals not committed yet
├── projects/
│   ├── active.md             # In-flight projects
│   └── waiting.md            # Blocked or delegated projects
├── tasks/
│   ├── next-actions.md       # Concrete next steps
│   ├── this-week.md          # This week's commitments
│   ├── waiting.md            # Waiting-for items
│   └── done.md               # Completed items worth keeping
├── habits/
│   ├── active.md             # Current habits and streak intent
│   └── friction.md           # Things that break consistency
├── planning/
│   ├── daily.md              # Daily focus and must-win
│   ├── weekly.md             # Weekly plan and protected time
│   └── focus-blocks.md       # Deep work and recovery blocks
├── reviews/
│   ├── weekly.md             # Weekly reset
│   └── monthly.md            # Monthly reflection and adjustments
├── commitments/
│   ├── promises.md           # Commitments made to self or others
│   └── delegated.md          # Handed-off work to track
├── focus/
│   ├── sessions.md           # Deep work sessions and patterns
│   └── distractions.md       # Repeating focus breakers
├── routines/
│   ├── morning.md            # Startup routine and first-hour defaults
│   └── shutdown.md           # End-of-day reset and carry-over logic
└── someday/
    └── ideas.md              # Parked ideas and optional opportunities
```

The skill should treat this as the user's productivity operating system: one trusted place for direction, commitments, execution, habits, and periodic review.

## Quick Reference

| Topic | File |
| --- | --- |
| Setup and routing | `setup.md` |
| Memory structure | `memory-template.md` |
| Productivity system template | `system-template.md` |
| Cross-situation frameworks | `frameworks.md` |
| Common mistakes | `traps.md` |
| Student context | `situations/student.md` |
| Executive context | `situations/executive.md` |
| Freelancer context | `situations/freelancer.md` |
| Parent context | `situations/parent.md` |
| Creative context | `situations/creative.md` |
| Burnout context | `situations/burnout.md` |
| Entrepreneur context | `situations/entrepreneur.md` |
| ADHD context | `situations/adhd.md` |
| Remote work context | `situations/remote.md` |
| Manager context | `situations/manager.md` |
| Habit context | `situations/habits.md` |
| Guilt and recovery context | `situations/guilt.md` |

## What This Skill Sets Up

| Layer | Purpose | Default location |
| --- | --- | --- |
| Capture | Catch loose inputs fast | `~/productivity/inbox/` |
| Direction | Goals and active bets | `~/productivity/dashboard.md` + `goals/` |
| Execution | Next actions and commitments | `~/productivity/tasks/` |
| Projects | Active and waiting project state | `~/productivity/projects/` |
| Habits | Repeated behaviors and friction | `~/productivity/habits/` |
| Planning | Daily, weekly, and focus planning | `~/productivity/planning/` |
| Reflection | Weekly and monthly reset | `~/productivity/reviews/` |
| Commitments | Promises and delegated follow-through | `~/productivity/commitments/` |
| Focus | Deep work protection and distraction logs | `~/productivity/focus/` |
| Routines | Startup and shutdown defaults | `~/productivity/routines/` |
| Parking lot | Non-committed ideas | `~/productivity/someday/` |
| Personal fit | Constraints, energy, preferences | `~/productivity/memory.md` |

This skill should give the user a single framework that can absorb:

* goals
* projects
* tasks
* habits
* priorities
* focus sessions
* routines
* focus blocks
* reviews
* commitments
* inbox capture
* parked ideas
* bottlenecks
* context-specific adjustments

## Quick Queries

| User says | Action |
| --- | --- |
| "Set up my productivity system" | Create the `~/productivity/` baseline and explain the folders |
| "What should I focus on?" | Check dashboard + tasks + commitments + focus, then surface top priorities |
| "Help me plan my week" | Use goals, projects, commitments, routines, and energy patterns to build a weekly plan |
| "I'm overwhelmed" | Triage commitments, cut scope, and reset next actions |
| "Turn this goal into a plan" | Convert goal -> project -> milestones -> next actions |
| "Do a weekly review" | Update wins, blockers, carry-overs, and next-week focus |
| "Help me with habits" | Use `habits/` to track what to keep, drop, or redesign |
| "Help me reset my routine" | Use `routines/` and `planning/` to simplify startup and shutdown loops |
| "Remember this preference" | Save it to `~/productivity/memory.md` after explicit confirmation |

## Core Rules

### 1. Build One System, Not Five Competing Ones

* Prefer one trusted productivity structure over scattered notes, random task lists, and duplicated plans.
* Route goals, projects, tasks, habits, routines, focus, planning, and reviews into the right folder instead of inventing a fresh system each time.
* If the user already has a good system, adapt to it rather than replacing it for style reasons.

### 2. Start With the Real Bottleneck

* Diagnose whether the problem is priorities, overload, unclear next actions, bad estimates, weak boundaries, or low energy.
* Give the smallest useful intervention first.
* Do not prescribe a full life overhaul when the user really needs a clearer next step.

### 3. Separate Goals, Projects, and Tasks Deliberately

* Goals describe outcomes.
* Projects package the work needed to reach an outcome.
* Tasks are the next visible actions.
* Habits are repeated behaviors that support the system over time.
* Never leave a goal sitting as a vague wish without a concrete project or next action.

### 4. Adapt the System to Real Constraints

* Use the situation guides when the user's reality matters more than generic advice.
* Energy, childcare, deadlines, meetings, burnout, and ADHD constraints should shape the plan.
* A sustainable system beats an idealized one that collapses after two days.

### 5. Reviews Matter More Than Constant Replanning

* Weekly review is where the system regains trust.
* Clear stale tasks, rename vague items, and reconnect tasks to real priorities.
* If the user keeps replanning daily without progress, simplify and review instead.

### 6. Save Only Explicitly Approved Preferences

* Store work-style information only when the user explicitly asks you to save it or clearly approves.
* Before writing to `~/productivity/memory.md`, ask for confirmation.
* Never infer long-term preferences from silence, patterns, or one-off comments.

## Common Traps

* Giving motivational talk when the problem is actually structural.
* Treating every task like equal priority.
* Mixing goals, projects, and tasks in the same vague list.
* Building a perfect system the user will never maintain.
* Recommending routines that ignore the user's real context.
* Preserving stale commitments because deleting them feels uncomfortable.

## Scope

This skill ONLY:

* builds or improves a local productivity operating system
* gives productivity advice and planning frameworks
* reads included reference files for context-specific guidance
* writes to `~/productivity/` only after explicit user approval

This skill NEVER:

* accesses calendar, email, contacts, or external services by itself
* monitors or tracks behavior in the background
* infers long-term preferences from observation alone
* writes files without explicit user confirmation
* makes network requests
* modifies its own SKILL.md or auxiliary files

## External Endpoints

This skill makes NO external network requests.

| Endpoint | Data Sent | Purpose |
| --- | --- | --- |
| None | None | N/A |

No data is sent externally.

## Data Storage

Local files live in `~/productivity/`.

* `~/productivity/memory.md` stores approved preferences, constraints, and work-style notes
* `~/productivity/inbox/` stores fast captures and triage
* `~/productivity/dashboard.md` stores top-level direction and current focus
* `~/productivity/goals/` stores active and someday goals
* `~/productivity/projects/` stores active and waiting projects
* `~/productivity/tasks/` stores next actions, weekly commitments, waiting items, and completions
* `~/productivity/habits/` stores active habits and friction notes
* `~/productivity/planning/` stores daily plans, weekly plans, and focus blocks
* `~/productivity/reviews/` stores weekly and monthly reviews
* `~/productivity/commitments/` stores promises and delegated follow-through
* `~/productivity/focus/` stores deep-work sessions and distraction patterns
* `~/productivity/routines/` stores startup and shutdown defaults
* `~/productivity/someday/` stores parked ideas

Create or update these files only after the user confirms they want the system written locally.

## Migration

If upgrading from an older version, see `migration.md` before restructuring any existing `~/productivity/` files.
Keep legacy files until the user confirms the new system is working for them.

## Security & Privacy

**Data that leaves your machine:**

* Nothing. This skill performs no network calls.

**Data stored locally:**

* Only the productivity files the user explicitly approves in `~/productivity/`
* Work preferences, constraints, priorities, and planning artifacts the user chose to save

**This skill does NOT:**

* access internet or third-party services
* read calendar, email, contacts, or system data automatically
* run scripts or commands by itself
* monitor behavior in the background
* infer hidden preferences from passive observation

## Trust

This skill is instruction-only. It provides a local framework for productivity planning, prioritization, and review. Install it only if you are comfortable storing your own productivity notes in plain text under `~/productivity/`.

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `self-improving` — Compound execution quality and reusable lessons across tasks
* `goals` — Deeper goal-setting and milestone design
* `calendar-planner` — Calendar-driven planning and scheduling support
* `notes` — Structured note capture for ongoing work and thinking

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

- Plan, focus, and complete work with energy management, time blocking,
  goals, projects, tasks, hab
- 触发关键词: complete, plan, productivity, focus

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

### Q1: 如何开始使用Productivity？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Productivity有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
