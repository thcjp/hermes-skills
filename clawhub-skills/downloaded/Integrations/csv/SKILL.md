---
slug: csv
name: csv
version: "1.0.0"
displayName: CSV
summary: Parse and generate RFC 4180 compliant CSV that works across tools.
license: MIT
description: |-
  Parse and generate RFC 4180 compliant CSV that works across tools。核心能力:

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

# CSV

## Quoting Rules

* Fields containing comma, quote, or newline MUST be wrapped in double quotes
* Double quotes inside quoted fields escape as `""` (two quotes), not backslash
* Unquoted fields with leading/trailing spaces—some parsers trim, some don't; quote to preserve
* Empty field `,,` vs empty string `,"",`—semantically different; be explicit

## Delimiters

* CSV isn't always comma—detect `;` (European Excel), `\t` (TSV), `|` in legacy systems
* Excel exports use system locale delimiter; semicolon common in non-US regions
* Sniff delimiter from first line but verify—header might not contain special chars

## Encoding

* UTF-8 BOM (`0xEF 0xBB 0xBF`) breaks naive parsers but Excel needs it for UTF-8 detection
* When generating for Excel on Windows: add BOM; for programmatic use: omit BOM
* Latin-1 vs UTF-8 ambiguity—explicitly declare or detect encoding before parsing

## Common Parsing Failures

* Newlines inside quoted fields are valid—don't split on `\n` before parsing
* Unescaped quote in middle of field corrupts rest of file—validate early
* Trailing newline at EOF—some parsers create empty last row; strip or handle
* Inconsistent column count per row—validate all rows match header count

## Numbers & Dates

* `1,234.56` vs `1.234,56`—locale-dependent; standardize or document format
* Dates: ISO 8601 (`2024-01-15`) only unambiguous format; `01/02/24` is chaos
* Leading zeros in numeric fields (`007`)—quote to preserve or document as string

## Excel Quirks

* Formula injection: fields starting with `=`, `+`, `-`, `@` execute as formulas—prefix with `'` or tab
* Long numbers (>15 digits) lose precision—quote and format as text
* Scientific notation triggered by `E` in numbers—quote if literal text needed

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

- Parse and generate RFC 4180 compliant CSV that works across tools
- 触发关键词: generate, compliant, parse, csv, works

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

### Q1: 如何开始使用CSV？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: CSV有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
