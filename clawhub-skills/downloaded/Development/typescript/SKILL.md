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
  and strict mode best practi。Use when 用户需要TypeScript相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
- Development
tools:
  - - read
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

- Write type-safe TypeScript with proper narrowing, inference patterns,
  and strict mode best practi
- 触发关键词: write, safe, type, typescript

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

### Q1: 如何开始使用TypeScript？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: TypeScript有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
