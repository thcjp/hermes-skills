---
slug: csv-analyzer
name: csv-analyzer
version: "1.0.0"
displayName: Csv Analyzer
summary: Analyze CSV/Excel files with natural language. Get statistics, filter rows,
  find anomalies, gener...
license: MIT
description: |-
  Analyze CSV/Excel files with natural language. Get statistics, filter
  rows, find anomalies, gener...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: files, excel, natural, csv, analyze, analyzer
tags:
- Integrations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
