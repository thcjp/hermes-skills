---
slug: rust
name: rust
version: "1.0.1"
displayName: Rust
summary: "编写地道Rust代码,规避所有权、生命周期、借用检查常见陷阱,降低编译错误率"
  common borrow checker b...
license: MIT
description: |-
  Write idiomatic Rust avoiding ownership pitfalls, lifetime confusion,
  and common borrow checker b。Use when 用户需要Rust相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Rust

## Quick Reference

| Topic | File | Key Trap |
| --- | --- | --- |
| Ownership & Borrowing | `ownership-borrowing.md` | Move semantics catch everyone |
| Strings & Types | `types-strings.md` | `String` vs `&str`, UTF-8 indexing |
| Errors & Iteration | `errors-iteration.md` | `unwrap()` in production, lazy iterators |
| Concurrency & Memory | `concurrency-memory.md` | `Rc` not `Send`, `RefCell` panics |
| Advanced Traps | `advanced-traps.md` | unsafe, macros, FFI, performance |

---

## Critical Traps (High-Frequency Failures)

### Ownership — #1 Source of Compiler Errors

* **Variable moved after use** — clone explicitly or borrow with `&`
* **`for item in vec` moves vec** — use `&vec` or `.iter()` to borrow
* **`String` moved into function** — pass `&str` for read-only access

### Borrowing — The Borrow Checker Always Wins

* **Can't have `&mut` and `&` simultaneously** — restructure or interior mutability
* **Returning reference to local fails** — return owned value instead
* **Mutable borrow through `&mut self` blocks all access** — split struct or `RefCell`

### Lifetimes — When Compiler Can't Infer

* **`'static` means CAN live forever, not DOES** — `String` is 'static capable
* **Struct with reference needs `<'a>`** — `struct Foo<'a> { bar: &'a str }`
* **Function returning ref must tie to input** — `fn get<'a>(s: &'a str) -> &'a str`

### Strings — UTF-8 Surprises

* **`s[0]` doesn't compile** — use `.chars().nth(0)` or `.bytes()`
* **`.len()` returns bytes, not chars** — use `.chars().count()`
* **`s1 + &s2` moves s1** — use `format!("{}{}", s1, s2)` to keep both

### Error Handling — Production Code

* **`unwrap()` panics** — use `?` or `match` in production
* **`?` needs `Result`/`Option` return type** — main needs `-> Result<()>`
* **`expect("context")` > `unwrap()`** — shows why it panicked

### Iterators — Lazy Evaluation

* **`.iter()` borrows, `.into_iter()` moves** — choose carefully
* **`.collect()` needs type** — `collect::<Vec<_>>()` or typed binding
* **Iterators are lazy** — nothing runs until consumed

### Concurrency — Thread Safety

* **`Rc` is NOT `Send`** — use `Arc` for threads
* **`Mutex` lock returns guard** — auto-unlocks on drop, don't hold across await
* **`RwLock` deadlock** — reader upgrading to writer blocks forever

### Memory — Smart Pointers

* **`RefCell` panics at runtime** — if borrow rules violated
* **`Box` for recursive types** — compiler needs known size
* **Avoid `Rc<RefCell<T>>` spaghetti** — rethink ownership

---

## Common Compiler Errors (NEW)

| Error | Cause | Fix |
| --- | --- | --- |
| `value moved here` | Used after move | Clone or borrow |
| `cannot borrow as mutable` | Already borrowed | Restructure or RefCell |
| `missing lifetime specifier` | Ambiguous reference | Add `<'a>` |
| `the trait bound X is not satisfied` | Missing impl | Check trait bounds |
| `type annotations needed` | Can't infer | Turbofish or explicit type |
| `cannot move out of borrowed content` | Deref moves | Clone or pattern match |

---

## Cargo Traps (NEW)

* **`cargo update` updates Cargo.lock, not Cargo.toml** — manual version bump needed
* **Features are additive** — can't disable a feature a dependency enables
* **`[dev-dependencies]` not in release binary** — but in tests/examples
* **`cargo build --release` much faster** — debug builds are slow intentionally

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

- Write idiomatic Rust avoiding ownership pitfalls, lifetime confusion,
  and common borrow checker b
- 触发关键词: write, ownership, avoiding, idiomatic, rust

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

### Q1: 如何开始使用Rust？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Rust有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
