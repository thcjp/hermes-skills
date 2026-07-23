---
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
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

- Coding workflow with planning, implementation, verification, and testing
  for clean software devel
- 触发关键词: planning, code, implementation, workflow, 1

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

### Q1: 如何开始使用Code 1.0.4？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Code 1.0.4有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
