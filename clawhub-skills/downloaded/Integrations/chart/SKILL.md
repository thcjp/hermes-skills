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
  and quick visual expl...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: chart, engine, generation, local
tags:
- Integrations
tools:
- read
- exec
---

# Chart

Turn numbers into clear visuals.

## Core Philosophy

1. Prefer clarity over chart variety.
2. Choose the simplest chart that makes the comparison obvious.
3. Use local generation only.
4. Make outputs reusable for reports, slides, and quick decision-making.

## Runtime Requirements

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
