---
slug: typescript
name: typescript
version: "1.0.2"
displayName: TypeScript
summary: Write type-safe TypeScript with proper narrowing, inference patterns, and
  strict mode best practi...
license: MIT
description: |-
  Write type-safe TypeScript with proper narrowing, inference patterns,
  and strict mode best practi...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: write, safe, type, typescript
tags:
- Development
tools:
- read
- exec
---

# TypeScript

## When to Use

User needs TypeScript expertise — from basic typing to advanced generics. Agent handles type narrowing, inference, discriminated unions, and strict mode patterns.

## Quick Reference

| Topic | File |
| --- | --- |
| Generic patterns | `generics.md` |
| Utility types | `utility-types.md` |
| Declaration files | `declarations.md` |
| Migration from JS | `migration.md` |

## Stop Using `any`

* `unknown` forces you to narrow before use — `any` silently breaks type safety
* API responses: type them or use `unknown`, never `any`
* When you don't know the type, that's `unknown`, not `any`

## Narrowing Failures

* `filter(Boolean)` doesn't narrow — use `.filter((x): x is T => Boolean(x))`
* `Object.keys(obj)` returns `string[]`, not `keyof typeof obj` — intentional, objects can have extra keys
* `Array.isArray()` narrows to `any[]` — may need assertion for element type
* `in` operator narrows but only if property is in exactly one branch of union

## Literal Type Traps

* `let x = "hello"` is `string` — use `const` or `as const` for literal type
* Object properties widen: `{ status: "ok" }` has `status: string` — use `as const` or type annotation
* Function return types widen — annotate explicitly for literal returns

## Inference Limits

* Callbacks lose inference in some array methods — annotate parameter when TS guesses wrong
* Generic functions need usage to infer — `fn<T>()` can't infer, pass a value or annotate
* Nested generics often fail — break into steps with explicit types

## Discriminated Unions

* Add a literal `type` or `kind` field to each variant — enables exhaustive switch
* Exhaustive check: `default: const _never: never = x` — compile error if case missed
* Don't mix discriminated with optional properties — breaks narrowing

## `satisfies` vs Type Annotation

* `const x: Type = val` widens to Type — loses literal info
* `const x = val satisfies Type` keeps literal, checks compatibility — prefer for config objects

## Strict Null Handling

* Optional chaining `?.` returns `undefined`, not `null` — matters for APIs expecting `null`
* `??` only catches `null`/`undefined` — `||` catches all falsy including `0` and `""`
* Non-null `!` should be last resort — prefer narrowing or early return

## Module Boundaries

* `import type` for type-only imports — stripped at runtime, avoids bundler issues
* Re-exporting types: `export type { X }` — prevents accidental runtime dependency
* `.d.ts` augmentation: use `declare module` with exact module path

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
