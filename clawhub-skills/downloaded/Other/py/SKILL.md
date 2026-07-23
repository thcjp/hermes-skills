---
slug: py
name: py
version: "1.0.1"
displayName: Python
summary: Write reliable Python avoiding mutable defaults, import traps, and common
  runtime surprises.
license: MIT
description: |-
  Write reliable Python avoiding mutable defaults, import traps, and common
  runtime surprises。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关...
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Python

## Quick Reference

| Topic | File |
| --- | --- |
| Dynamic typing, type hints, duck typing | `types.md` |
| List/dict/set gotchas, comprehensions | `collections.md` |
| Args/kwargs, closures, decorators, generators | `functions.md` |
| Inheritance, descriptors, metaclasses | `classes.md` |
| GIL, threading, asyncio, multiprocessing | `concurrency.md` |
| Circular imports, packages, **init**.py | `imports.md` |
| Pytest, mocking, fixtures | `testing.md` |

## Critical Rules

* `def f(items=[])` shares list across all calls — use `items=None` then `items = items or []`
* `is` checks identity, `==` checks equality — `"a" * 100 is "a" * 100` may be False
* Modifying list while iterating skips elements — iterate over copy: `for x in list(items):`
* GIL prevents true parallel Python threads — use multiprocessing for CPU-bound
* Bare `except:` catches `SystemExit` and `KeyboardInterrupt` — use `except Exception:`
* `UnboundLocalError` when assigning to outer scope variable — use `nonlocal` or `global`
* `open()` without context manager leaks handles — always use `with open():`
* Circular imports fail silently or partially — import inside function to break cycle
* `0.1 + 0.2 != 0.3` — floating point, use `decimal.Decimal` for money
* Generator exhausted after one iteration — can't reuse, recreate or use `itertools.tee`
* Class attributes with mutables shared across instances — define in `__init__` instead
* `__init__` is not constructor — `__new__` creates instance, `__init__` initializes
* Default encoding is platform-dependent — always specify `encoding='utf-8'`

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

- Write reliable Python avoiding mutable defaults, import traps, and common
  runtime surprises
- 触发关键词: python, mutable, write, reliable, avoiding

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

### Q1: 如何开始使用Python？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Python有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
