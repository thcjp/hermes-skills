---
slug: rust
name: rust
version: "1.0.1"
displayName: Rust
summary: Write idiomatic Rust avoiding ownership pitfalls, lifetime confusion, and
  common borrow checker b...
license: MIT
description: |-
  Write idiomatic Rust avoiding ownership pitfalls, lifetime confusion,
  and common borrow checker b...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: write, ownership, avoiding, idiomatic, rust
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
