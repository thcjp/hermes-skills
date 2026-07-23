---
slug: excel-xlsx
name: excel-xlsx
version: "1.0.2"
displayName: Excel / XLSX
summary: Create, inspect, and edit Microsoft Excel workbooks and XLSX files with reliable
  formulas, dates,...
license: MIT-0
description: |-
  Create, inspect, and edit Microsoft Excel workbooks and XLSX files with
  reliable formulas, dates,。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Excel / XLSX

## When to Use

Use when the main artifact is a Microsoft Excel workbook or spreadsheet file, especially when formulas, dates, formatting, merged cells, workbook structure, or cross-platform behavior matter.

## Core Rules

### 1. Choose the workflow by job, not by habit

* Use `pandas` for analysis, reshaping, and CSV-like tasks.
* Use `openpyxl` when formulas, styles, sheets, comments, merged cells, or workbook preservation matter.
* Treat CSV as plain data exchange, not as an Excel feature-complete format.
* Reading values, preserving a live workbook, and building a model from scratch are different spreadsheet jobs.

### 2. Dates are serial numbers with legacy quirks

* Excel stores dates as serial numbers, not real date objects.
* The 1900 date system includes the false leap-day bug, and some workbooks use the 1904 system.
* Time is fractional day data, so formatting and conversion both matter.
* Date correctness is not enough if the number format still displays the wrong thing to the user.

### 3. Keep calculations in Excel when the workbook should stay live

* Write formulas into cells instead of hardcoding derived results from Python.
* Use references to assumption cells instead of magic numbers inside formulas.
* Cached formula values can be stale, so do not trust them blindly after edits.
* Check copied formulas for wrong ranges, wrong sheets, and silent off-by-one drift before delivery.
* Absolute and relative references are part of the logic, so copied formulas can be wrong even when they still "work".
* Test new formulas on a few representative cells before filling them across a whole block.
* Verify denominators, named ranges, and precedent cells before shipping formulas that depend on them.
* A workbook should ship with zero formula errors, not with known `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or circular-reference fallout left for the user to fix.
* For model-style work, document non-obvious hardcodes, assumptions, or source inputs in comments or nearby notes.

### 4. Protect data types before Excel mangles them

* Long identifiers, phone numbers, ZIP codes, and leading-zero values should usually be stored as text.
* Excel silently truncates numeric precision past 15 digits.
* Mixed text-number columns need explicit handling on read and on write.
* Scientific notation, auto-parsed dates, and stripped leading zeros are common corruption, not cosmetic issues.

### 5. Preserve workbook structure before changing content

* Existing templates override generic styling advice.
* Only the top-left cell of a merged range stores the value.
* Hidden rows, hidden columns, named ranges, and external references can still affect formulas and outputs.
* Shared strings, defined names, and sheet-level conventions can matter even when the visible cells look simple.
* Match styles for newly filled cells instead of quietly introducing a new visual system.
* If the workbook is a template, preserve sheet order, widths, freezes, filters, print settings, validations, and visual conventions unless the task explicitly changes them.
* Conditional formatting, filters, print areas, and data validation often carry business meaning even when users only mention the numbers.
* If there is no existing style guide and the file is a model, keep editable inputs visually distinguishable from formulas, but never override an established template to force a generic house style.

### 6. Recalculate and review before delivery

* Formula strings alone are not enough if the recipient needs current values.
* `openpyxl` preserves formulas but does not calculate them.
* Verify no `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or circular-reference fallout remains.
* If layout matters, render or visually review the workbook before calling it finished.
* Be careful with read modes: opening a workbook for values only and then saving can flatten formulas into static values.
* If assumptions or hardcoded overrides must stay, make them obvious enough that the next editor can audit the workbook.

### 7. Scale the workflow to the file size

* Large workbooks can fail for boring reasons: memory spikes, padded empty rows, and slow full-sheet reads.
* Use streaming or chunked reads when the file is big enough that loading everything at once becomes fragile.
* Large-file workflows also need narrower reads, explicit dtypes, and sheet targeting to avoid accidental damage.

## Common Traps

* Type inference on read can leave numbers as text or convert IDs into damaged numeric values.
* Column indexing varies across tools, so off-by-one mistakes are common in generated formulas.
* Newlines in cells need wrapping to display correctly.
* External references break easily when source files move.
* Password protection in old Excel workflows is not serious security.
* `.xlsm` can contain macros, and `.xls` remains a tighter legacy format.
* Large files may need streaming reads or more careful memory handling.
* Google Sheets and LibreOffice can reinterpret dates, formulas, or styling differently from Excel.
* Dynamic array or newer Excel functions like `FILTER`, `XLOOKUP`, `SORT`, or `SEQUENCE` may fail or degrade in older viewers.
* A workbook can look fine while still carrying stale cached values from a prior recalculation.
* Saving the wrong workbook view can replace formulas with cached values and quietly destroy a live model.
* Copying formulas without checking relative references can push one bad range across an entire block.
* Hidden sheets, named ranges, validations, and merged areas often keep business logic that is invisible in a quick skim.
* A workbook can appear numerically correct while still failing because filters, conditional formats, print settings, or data validation were stripped.
* A workbook can be numerically correct and still fail visually because wrapped text, clipped labels, or narrow columns were never reviewed.

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `csv` — Plain-text tabular import and export workflows.
* `data` — General data handling patterns before spreadsheet output.
* `data-analysis` — Higher-level analysis that can feed workbook deliverables.

## Feedback

* If useful: `
* Stay updated: `

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

- Create, inspect, and edit Microsoft Excel workbooks and XLSX files with
  reliable formulas, dates,
- 触发关键词: edit, create, microsoft, excel, inspect, xlsx

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

### Q1: 如何开始使用Excel / XLSX？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Excel / XLSX有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
