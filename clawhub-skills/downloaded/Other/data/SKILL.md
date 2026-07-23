---
slug: data
name: data
version: "1.0.1"
displayName: Data
summary: Work with data across the full lifecycle from extraction and cleaning to
  analysis, visualization,...
license: MIT
description: |-
  Work with data across the full lifecycle from extraction and cleaning
  to analysis, visualization,。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Data

## When to Use

User needs to: extract data from sources (databases, APIs, files), clean and transform messy datasets, analyze and find patterns, visualize results, or automate recurring data tasks. Agent handles the full data workflow.

## Quick Reference

| Area | File | Focus |
| --- | --- | --- |
| Querying & Extraction | `querying.md` | SQL generation, API fetching, multi-source |
| Cleaning & Transformation | `cleaning.md` | Nulls, duplicates, normalization, joins |
| Analysis & Statistics | `analysis.md` | EDA, statistical tests, insights |
| Visualization & Reporting | `visualization.md` | Charts, dashboards, exports |
| Quality & Validation | `quality.md` | Data checks, anomaly detection, drift |
| Workflow Patterns | `patterns.md` | Common data workflows, automation |

## Core Operations

**Query generation:** User describes what data they need → Agent writes SQL/query, handles joins, filters, aggregations → Returns results or explains execution plan.

**Data cleaning:** Load messy dataset → Detect issues (nulls, duplicates, outliers, inconsistent formats) → Apply appropriate fixes → Document transformations.

**Exploratory analysis:** New dataset arrives → Generate descriptive stats, distributions, correlations → Surface interesting patterns and anomalies → Produce summary with key findings.

**Visualization:** Analysis complete → Generate appropriate chart type → Export in requested format (PNG, SVG, interactive HTML) → Ready for stakeholders.

**Recurring reports:** Define report once → Agent runs on schedule → Updates charts and metrics → Delivers summary with highlights.

## Critical Rules

* Always preview transformations before applying — show sample of what will change
* Document every data transformation with source, operation, and rationale
* Validate data types and ranges before analysis — garbage in, garbage out
* Use appropriate statistical tests — check assumptions first
* Generate reproducible outputs — include seeds, versions, timestamps
* Handle missing data explicitly — document chosen strategy (drop, impute, flag)
* Match chart type to data type — categorical, continuous, time series

## User Modes

| Mode | Focus | Trigger |
| --- | --- | --- |
| Analyst | SQL, exploration, insights | "What does this data tell us?" |
| Engineer | Pipelines, transformations, quality | "Clean this and load it there" |
| Business | KPIs, dashboards, plain language | "How are we doing vs last quarter?" |
| Researcher | Statistical rigor, reproducibility | "Is this difference significant?" |
| Developer | Schema design, API data, types | "Generate types from this JSON" |

See `patterns.md` for workflows per mode.

## On First Use

1. Identify data source (database, file, API)
2. Establish connection or load file
3. Initial EDA — shape, types, quality issues
4. Clean and transform as needed
5. Analyze or visualize per user goal

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

- Work with data across the full lifecycle from extraction and cleaning
  to analysis, visualization,
- 触发关键词: across, data, full

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

### Q1: 如何开始使用Data？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Data有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
