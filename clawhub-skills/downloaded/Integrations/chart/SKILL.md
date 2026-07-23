---
slug: chart
name: chart
version: "1.0.0"
displayName: Chart
summary: Local-first chart generation engine for trends, comparisons, distributions,
  and quick visual expl...
license: MIT-0
description: |-
  Local-first chart generation engine for trends, comparisons, distributions,
  and quick visual expl。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Chart

Turn numbers into clear visuals.

## Core Philosophy

1. Prefer clarity over chart variety.
2. Choose the simplest chart that makes the comparison obvious.
3. Use local generation only.
4. Make outputs reusable for reports, slides, and quick decision-making.

## 依赖说明

* Python 3 must be available as `python3`
* `matplotlib` must be installed
* No network access required

## Storage

All data is stored locally only under:

* `~/.skill-platform/workspace/memory/chart/charts.json`
* `~/.skill-platform/workspace/memory/chart/output/`

No cloud sync. No third-party chart APIs.

## Supported Chart Types

* `bar`: category comparison
* `line`: trend over time
* `pie`: simple part-to-whole
* `scatter`: relationship between two variables

## Key Workflows

* **Suggest**: `suggest_chart.py --labels ... --values ...`
* **Generate**: `make_chart.py --type bar --title "..." --labels "A,B,C" --values "10,20,15"`
* **History**: `list_charts.py`
* **Initialize**: `init_storage.py`

## Scripts

| Script | Purpose |
| --- | --- |
| `init_storage.py` | Initialize local chart storage |
| `make_chart.py` | Generate a chart image from inline data |
| `suggest_chart.py` | Recommend the best chart type |
| `list_charts.py` | Show previously generated charts |

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

## 核心能力

- Local-first chart generation engine for trends, comparisons, distributions,
  and quick visual expl
- 触发关键词: chart, engine, generation, local

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

### Q1: 如何开始使用Chart？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Chart有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
