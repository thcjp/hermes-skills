---
slug: csv-analyzer
name: csv-analyzer
version: "1.0.0"
displayName: Csv Analyzer
summary: Analyze CSV/Excel files with natural language. Get statistics, filter rows,
  find anomalies, gener...
license: MIT
description: |-
  Analyze CSV/Excel files with natural language。Get statistics, filter
  rows, find anomalies, gener。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Csv Analyzer

Analyze CSV files with simple commands. Get instant statistics, filter data, detect anomalies, and export results — all without pandas or heavy dependencies.

## Usage

### Quick stats

```bash
python3 {baseDir}/scripts/csv_analyze.py stats data.csv
```

Shows row count, column types, min/max/mean for numeric columns, unique counts for text columns.

### Filter rows

```bash
python3 {baseDir}/scripts/csv_analyze.py filter data.csv --where "amount>1000" --output big_orders.csv
```

### Top/Bottom N

```bash
python3 {baseDir}/scripts/csv_analyze.py top data.csv --column revenue --n 10
python3 {baseDir}/scripts/csv_analyze.py bottom data.csv --column revenue --n 5
```

### Detect anomalies (values outside 2σ)

```bash
python3 {baseDir}/scripts/csv_analyze.py anomalies data.csv --column price
```

### Group and aggregate

```bash
python3 {baseDir}/scripts/csv_analyze.py group data.csv --by category --agg "sum:amount" "count:id"
```

## Features

* 📊 Automatic column type detection (numeric, date, text)
* 🔍 Flexible filtering with comparison operators
* 📈 Statistical summary (mean, median, std, min, max, percentiles)
* 🚨 Anomaly detection (z-score based)
* 📋 Grouping and aggregation
* 💾 Export filtered/processed results
* 🪶 **Zero external dependencies** — Python stdlib only (csv module)

## Dependencies

None! Uses only Python standard library.

## Why Not Pandas?

Pandas is great but:

* Takes 100MB+ RAM just to import
* Overkill for quick analysis tasks
* This skill runs on 2GB RAM servers without issues
* For truly large datasets, the agent can recommend installing pandas

## Limitations

* Designed for files up to ~100MB (loads into memory)
* For larger files, use streaming mode or install pandas
* Date parsing is basic (ISO format preferred)

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

### Q1: 如何开始使用Csv Analyzer？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Csv Analyzer有什么限制？
A: 请参考已知限制章节了解具体限制。
