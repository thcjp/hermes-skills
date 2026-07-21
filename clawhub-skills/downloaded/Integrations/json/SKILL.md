---
slug: json
name: json
version: "1.0.0"
displayName: JSON
summary: Work with JSON data structures, APIs, and serialization effectively.
license: MIT
description: |-
  Work with JSON data structures, APIs, and serialization effectively。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Integrations
tools:
  - - read
- exec
---

# JSON

## Schema & Validation

* Always validate against JSON Schema before processing untrusted input—don't assume structure
* Define schemas for API responses—catches contract violations early
* Use `additionalProperties: false` to reject unknown fields in strict contexts

## Naming & Consistency

* Pick one convention and stick to it—`camelCase` for JS ecosystems, `snake_case` for Python/Ruby
* Avoid mixed conventions in same payload—`userId` alongside `user_name` confuses consumers
* Use plural for collections: `"users": []` not `"user": []`

## Null Handling

* Distinguish "field is null" from "field is absent"—they mean different things
* Omit optional fields entirely rather than sending `null`—reduces payload, clearer intent
* Document which fields are nullable in schema—don't surprise consumers

## Dates & Times

* Always use ISO 8601: `"2024-01-15T14:30:00Z"`—no ambiguous formats like `"01/15/24"`
* Include timezone or use UTC with `Z` suffix—local times without zone are useless
* Timestamps as strings, not epoch integers—human-readable, no precision loss

## Numbers & IDs

* Large IDs as strings: `"id": "9007199254740993"`—JavaScript loses precision above 2^53
* Money as string or integer cents—never float: `"price": "19.99"` or `"price_cents": 1999`
* Avoid floats for anything requiring exactness—currency, coordinates with precision

## Structure Best Practices

* Keep nesting shallow—3 levels max; flatten or split into related endpoints
* Consistent envelope for APIs: `{"data": ..., "meta": ..., "errors": ...}`
* Paginate large arrays—never return unbounded lists; include `next`/`prev` links or cursor

## API Response Patterns

* Errors as structured objects: `{"code": "INVALID_EMAIL", "message": "...", "field": "email"}`
* Include request ID in responses for debugging: `"request_id": "abc-123"`
* Return created/updated resource in response—saves client a follow-up GET

## Serialization

* `toJSON()` method silently overrides output—Date becomes string, custom classes may surprise
* Map, Set, BigInt don't serialize—need custom replacer function
* Circular references throw—detect cycles before stringify or use libraries like `flatted`
* Strip sensitive data before serializing—don't rely on client to ignore extra fields

## Parsing Safety

* `__proto__` key can pollute prototypes—sanitize input or use `Object.create(null)`
* Parse in try/catch—malformed JSON from external sources is common
* Reviver function for type reconstruction: dates, BigInt, custom types

## Unicode

* Emoji need surrogate pairs in escapes: 😀 = `\uD83D\uDE00`—single `\u1F600` invalid
* Control chars U+0000–U+001F must be escaped—pasted text may contain invisible ones
* BOM at file start breaks parsing—strip `\uFEFF` from file input

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

- Work with JSON data structures, APIs, and serialization effectively
- 触发关键词: data, structures, json

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

### Q1: 如何开始使用JSON？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: JSON有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
