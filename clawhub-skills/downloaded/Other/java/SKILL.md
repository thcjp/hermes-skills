---
slug: java
name: java
version: "1.0.1"
displayName: Java
summary: Write robust Java avoiding null traps, equality bugs, and concurrency pitfalls.
license: MIT
description: |-
  Write robust Java avoiding null traps, equality bugs, and concurrency
  pitfalls.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: write, avoiding, java, null, robust
tags:
- Other
tools:
- read
- exec
---

# Java

## Quick Reference

| Topic | File |
| --- | --- |
| Nulls, Optional, autoboxing | `nulls.md` |
| Collections and iteration traps | `collections.md` |
| Generics and type erasure | `generics.md` |
| Concurrency and synchronization | `concurrency.md` |
| Classes, inheritance, memory | `classes.md` |
| Streams and CompletableFuture | `streams.md` |
| Testing (JUnit, Mockito) | `testing.md` |
| JVM, GC, modules | `jvm.md` |

## Critical Rules

* `==` compares references, not content — always use `.equals()` for strings
* Override `equals()` must also override `hashCode()` — HashMap/HashSet break otherwise
* `Optional.get()` throws if empty — use `orElse()`, `orElseGet()`, or `ifPresent()`
* Modifying while iterating throws `ConcurrentModificationException` — use Iterator.remove()
* Type erasure: generic type info gone at runtime — can't do `new T()` or `instanceof List<String>`
* `volatile` ensures visibility, not atomicity — `count++` still needs synchronization
* Unboxing null throws NPE — `Integer i = null; int x = i;` crashes
* `Integer == Integer` uses reference for values outside -128 to 127 — use `.equals()`
* Try-with-resources auto-closes — implement `AutoCloseable`, Java 7+
* Inner classes hold reference to outer — use static nested class if not needed
* Streams are single-use — can't reuse after terminal operation
* `thenApply` vs `thenCompose` — compose for chaining CompletableFutures
* Records are implicitly final — can't extend, components are final
* `serialVersionUID` mismatch breaks deserialization — always declare explicitly

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
