---
slug: javascript
name: javascript
version: "1.0.3"
displayName: JavaScript
summary: Write robust JavaScript with async patterns, type coercion handling, and
  modern ES2023+ features.
license: MIT
description: |-
  Write robust JavaScript with async patterns, type coercion handling,
  and modern ES2023+ features.

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: write, robust, javascript, async
tags:
- Development
tools:
- read
- exec
---

# JavaScript

## When to Use

User needs JavaScript expertise — from core language features to modern patterns. Agent handles async/await, closures, module systems, and ES2023+ features.

## Quick Reference

| Topic | File |
| --- | --- |
| Async patterns | `async.md` |
| Type coercion rules | `coercion.md` |
| Array and object methods | `collections.md` |
| Modern ES features | `modern.md` |

## Equality Traps

* `==` coerces: `"0" == false` is true — use `===` always
* `NaN !== NaN` — use `Number.isNaN()`, not `=== NaN`
* `typeof null === "object"` — check `=== null` explicitly
* Objects compare by reference — `{} === {}` is false

## this Binding

* Regular functions: `this` depends on call site — lost in callbacks
* Arrow functions: `this` from lexical scope — use for callbacks
* `setTimeout(obj.method)` loses `this` — use arrow or `.bind()`
* Event handlers: `this` is element in regular function, undefined in arrow (if no outer this)

## Closure Traps

* Loop variable captured by reference — `let` in loop or IIFE to capture value
* `var` hoisted to function scope — creates single binding shared across iterations
* Returning function from loop: all share same variable — use `let` per iteration

## Array Mutation

* `sort()`, `reverse()`, `splice()` mutate original — use `toSorted()`, `toReversed()`, `toSpliced()` (ES2023)
* `push()`, `pop()`, `shift()`, `unshift()` mutate — spread `[...arr, item]` for immutable
* `delete arr[i]` leaves hole — use `splice(i, 1)` to remove and reindex
* Spread and `Object.assign` are shallow — nested objects still reference original

## Async Pitfalls

* Forgetting `await` returns Promise, not value — easy to miss without TypeScript
* `forEach` doesn't await — use `for...of` for sequential async
* `Promise.all` fails fast — one rejection rejects all, use `Promise.allSettled` if need all results
* Unhandled rejection crashes in Node — always `.catch()` or try/catch with await

## Numbers

* `0.1 + 0.2 !== 0.3` — floating point, use integer cents or `toFixed()` for display
* `parseInt("08")` works now — but `parseInt("0x10")` is 16, watch prefixes
* `Number("")` is 0, `Number(null)` is 0 — but `Number(undefined)` is NaN
* Large integers lose precision over 2^53 — use `BigInt` for big numbers

## Iteration

* `for...in` iterates keys (including inherited) — use `for...of` for values
* `for...of` on objects fails — objects aren't iterable, use `Object.entries()`
* `Object.keys()` skips non-enumerable — `Reflect.ownKeys()` gets all including symbols

## Implicit Coercion

* `[] + []` is `""` — arrays coerce to strings
* `[] + {}` is `"[object Object]"` — object toString
* `{} + []` is `0` in console — `{}` parsed as block, not object
* `"5" - 1` is 4, `"5" + 1` is "51" — minus coerces, plus concatenates

## Strict Mode

* `"use strict"` at top of file or function — catches silent errors
* Implicit globals throw in strict — `x = 5` without declaration fails
* `this` is undefined in strict functions — not global object
* Duplicate parameters and `with` forbidden

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
