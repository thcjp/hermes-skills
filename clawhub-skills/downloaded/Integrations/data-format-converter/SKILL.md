---
slug: data-format-converter
name: data-format-converter
version: "1.0.0"
displayName: Data Format Converte
summary: "CSV/JSON/XML/YAML/TOML间高效转换,支持批量"
  batch processin...
license: MIT
description: |-
  Convert data efficiently between CSV, JSON, XML, YAML, and TOML formats
  including batch processin。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Data Format Converter

在不同数据格式间转换：CSV、JSON、XML、YAML、TOML 等。

## 功能

* CSV ↔ JSON 转换
* JSON ↔ YAML 转换
* XML ↔ JSON 转换
* TOML ↔ JSON 转换
* 批量转换

## 触发词

* "格式转换"
* "格式互转"
* "convert format"
* "csv to json"

## 支持格式

| 输入 | 输出 |
| --- | --- |
| CSV | JSON |
| JSON | YAML |
| YAML | JSON |
| XML | JSON |
| TOML | JSON |

## 示例

```text
输入 (CSV):
name,age
John,30
Jane,25

输出 (JSON):
[
  {"name": "John", "age": "30"},
  {"name": "Jane", "age": "25"}
]
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

* CSV ↔ JSON 转换
* JSON ↔ YAML 转换
* XML ↔ JSON 转换
* TOML ↔ JSON 转换
* 批量转换

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

### Q1: 如何开始使用Data Format Converte？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Data Format Converte有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制

### 输入限制
- **文件大小限制**：单个文件的大小不能超过服务器的处理能力限制，通常为100MB。
- **数据行数限制**：由于内存和处理能力限制，转换的数据行数不宜过多，建议单次转换的数据行数不超过100万行。
- **数据格式限制**：输入文件必须符合CSV、JSON、XML、YAML或TOML的标准格式，否则可能无法正确解析和转换。

### 性能边界
- **转换速度**：转换速度取决于文件大小、复杂度和服务器性能。对于中等大小的文件，转换速度通常在几秒到几分钟之间。
- **并发处理**：服务可能支持有限的并发转换任务，超过限制可能导致任务排队或失败。

### 兼容性约束
- **操作系统兼容性**：尽管技能在多个操作系统上运行，但某些特定功能可能需要特定的操作系统版本或配置。
- **软件版本兼容性**：技能可能依赖于特定版本的软件库或框架，需要确保相关软件版本兼容。

### 批量处理限制
- **批量任务限制**：批量转换任务的数量和大小可能受到服务器的处理能力和配置限制。
- **文件路径限制**：批量处理时，文件路径长度可能有限制，特别是Windows系统下的路径长度限制。

### 安全与隐私
- **输入数据安全**：确保输入数据不包含敏感信息，如个人身份信息，以防止数据泄露。
- **输出数据安全**：输出文件应当妥善存储，防止未授权访问。

---

