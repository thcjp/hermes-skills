---
slug: data-format-converter
name: data-format-converter
version: "1.0.0"
displayName: Data Format Converte
summary: Convert data efficiently between CSV, JSON, XML, YAML, and TOML formats including
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
