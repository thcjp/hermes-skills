---
slug: json-formatter
name: json-formatter
version: "1.0.0"
displayName: JSON Formatter
summary: "格式化/校验/压缩JSON并提取路径,提升可读性(社区下载版)"
  readability and structu...
license: MIT
description: |-
  Format, validate, compress JSON data, and extract JSON paths for improved
  readability and structu。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# JSON Formatter

格式化、验证和压缩 JSON 数据。

## 功能

* JSON 格式化（缩进）
* JSON 验证
* JSON 压缩
* 路径提取

## 触发词

* "格式化JSON"
* "json格式化"
* "prettify json"
* "验证json"

## 示例

```text
输入: {"a":1,"b":2}
输出: {
  "a": 1,
  "b": 2
}
```

## 输出

```json
{
  "formatted": "...",
  "valid": true,
  "size": 1024,
  "paths": ["$.a", "$.b"]
}
```

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

* JSON 格式化（缩进）
* JSON 验证
* JSON 压缩
* 路径提取

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用JSON Formatter？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: JSON Formatter有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制

### 输入限制
- **JSON格式**：输入必须为有效的JSON格式，否则技能将无法正确处理。
- **数据大小**：对于非常大的JSON数据，技能可能无法处理，因为内存和处理能力有限。
- **路径复杂性**：对于复杂的JSON路径，技能可能无法正确提取，特别是当路径包含非法字符或超过技能处理能力时。

### 性能边界
- **处理速度**：对于大型JSON文件，格式化和压缩操作可能需要较长时间。
- **并发处理**：技能不支持同时处理多个大型JSON文件，可能会因为资源限制而影响性能。

### 兼容性约束
- **操作系统**：虽然技能在Windows、macOS和Linux上运行，但某些特定功能可能在不同操作系统之间存在差异。
- **LLM API版本**：技能依赖于LLM API，因此需要确保API版本与技能兼容。
- **浏览器兼容性**：如果技能通过Web界面使用，可能存在浏览器兼容性问题。

### 其他限制
- **实时数据处理**：技能不适用于实时流数据处理，因为它需要处理整个JSON数据。
- **外部API依赖**：技能可能依赖于外部API，如果这些API不可用或受限，可能会影响技能的功能。

---

