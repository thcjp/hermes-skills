---
slug: go
name: go
version: "1.0.2"
displayName: Go
summary: Write reliable Go code avoiding goroutine leaks, interface traps, and common
  concurrency bugs.
license: MIT
description: |-
  Write reliable Go code avoiding goroutine leaks, interface traps, and
  common concurrency bugs。核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触...
tags:
- Development
tools:
  - - read
- exec
---

# Go

## Quick Reference

| Topic | File |
| --- | --- |
| Concurrency patterns | `concurrency.md` |
| Interface and type system | `interfaces.md` |
| Slices, maps, strings | `collections.md` |
| Error handling patterns | `errors.md` |

## Goroutine Leaks

* Goroutine blocked on channel with no sender = leak forever—always ensure channel closes or use context
* Unbuffered channel send blocks until receive—deadlock if receiver never comes
* `for range` on channel loops forever until channel closed—sender must `close(ch)`
* Context cancellation doesn't stop goroutine automatically—must check `ctx.Done()` in loop
* Leaked goroutines accumulate memory and never garbage collect

## Channel Traps

* Sending to nil channel blocks forever—receiving from nil also blocks forever
* Sending to closed channel panics—closing already closed channel panics
* Only sender should close channel—receiver closing causes sender panic
* Buffered channel full = send blocks—size buffer for expected load
* `select` with multiple ready cases picks randomly—not first listed

## Defer Traps

* Defer arguments evaluated immediately, not when deferred function runs—`defer log(time.Now())` captures now
* Defer in loop accumulates—defers stack, run at function end not iteration end
* Defer runs even on panic—good for cleanup, but recover only in deferred function
* Named return values modifiable in defer—`defer func() { err = wrap(err) }()` works
* Defer order is LIFO—last defer runs first

## Interface Traps

* Nil concrete value in interface is not nil interface—`var p *MyType; var i interface{} = p; i != nil` is true
* Type assertion on wrong type panics—use comma-ok: `v, ok := i.(Type)`
* Empty interface `any` accepts anything but loses type safety—avoid when possible
* Interface satisfaction is implicit—no compile error if method signature drifts
* Pointer receiver doesn't satisfy interface for value type—only `*T` has the method

## Error Handling

* Errors are values, not exceptions—always check returned error
* `err != nil` after every call—unchecked errors are silent bugs
* `errors.Is` for wrapped errors—`==` doesn't work with `fmt.Errorf("%w", err)`
* Sentinel errors should be `var ErrFoo = errors.New()` not recreated
* Panic for programmer errors only—return error for runtime failures

## Slice Traps

* Slice is reference to array—modifying slice modifies original
* Append may or may not reallocate—never assume capacity
* Slicing doesn't copy—`a[1:3]` shares memory with `a`
* Nil slice and empty slice differ—`var s []int` vs `s := []int{}`
* `copy()` copies min of lengths—doesn't extend destination

## Map Traps

* Reading from nil map returns zero value—writing to nil map panics
* Map iteration order is random—don't rely on order
* Maps not safe for concurrent access—use `sync.Map` or mutex
* Taking address of map element forbidden—`&m[key]` doesn't compile
* Delete from map during iteration is safe—but add may cause issues

## String Traps

* Strings are immutable byte slices—each modification creates new allocation
* `range` over string iterates runes, not bytes—index jumps for multi-byte chars
* `len(s)` is bytes, not characters—use `utf8.RuneCountInString()`
* String comparison is byte-wise—not Unicode normalized
* Substring shares memory with original—large string keeps memory alive

## Struct and Memory

* Struct fields padded for alignment—field order affects memory size
* Zero value is valid—`var wg sync.WaitGroup` works, no constructor needed
* Copying struct with mutex copies unlocked mutex—always pass pointer
* Embedding is not inheritance—promoted methods can be shadowed
* Exported fields start uppercase—lowercase fields invisible outside package

## Build Traps

* `go build` caches aggressively—use `-a` flag to force rebuild
* Unused imports fail compilation—use `_` import for side effects only
* `init()` runs before main, order by dependency—not file order
* `go:embed` paths relative to source file—not working directory
* Cross-compile: `GOOS=linux GOARCH=amd64 go build`—easy but test on target

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

- Write reliable Go code avoiding goroutine leaks, interface traps, and
  common concurrency bugs
- 触发关键词: write, reliable, code, goroutine, avoiding

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

### Q1: 如何开始使用Go？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Go有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
