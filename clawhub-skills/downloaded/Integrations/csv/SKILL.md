---
slug: csv
name: csv
version: "1.0.0"
displayName: CSV
summary: Parse and generate RFC 4180 compliant CSV that works across tools.
license: MIT
description: |-
  Parse and generate RFC 4180 compliant CSV that works across tools.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generate, compliant, parse, csv, works
tags:
- Integrations
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
