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
  to analysis, visualization,...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: across, data, full
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
