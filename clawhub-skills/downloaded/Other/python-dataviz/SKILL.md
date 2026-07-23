---
slug: python-dataviz
name: python-dataviz
version: "1.0.0"
displayName: Python Dataviz
summary: Professional data visualization using Python (matplotlib, seaborn, plotly).
  Create publication-qu...
license: MIT
description: |-
  Professional data visualization using Python (matplotlib, seaborn, plotly)。Create publication-qu。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Python Dataviz

Create professional charts, graphs, and statistical visualizations using Python's leading libraries.

## 适用场景

**matplotlib** - Static plots, publication-quality, full control

* Bar, line, scatter, pie, histogram, heatmap
* Multi-panel figures, subplots
* Custom styling, annotations
* Export: PNG, SVG, PDF

**seaborn** - Statistical visualizations, beautiful defaults

* Distribution plots (violin, box, kde, histogram)
* Categorical plots (bar, count, swarm, box)
* Relationship plots (scatter, line, regression)
* Matrix plots (heatmap, clustermap)
* Built on matplotlib, integrates seamlessly

**plotly** - Interactive charts, web-friendly

* Hover tooltips, zoom, pan
* 3D plots, animations
* Dashboards via Dash framework
* Export: HTML, PNG (requires kaleido)

## Quick Start

### Setup Environment

```bash
cd skills/python-dataviz
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

### Create a Chart

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, color='#667eea')
plt.title('Sine Wave', fontsize=16, fontweight='bold')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.savefig('output.svg', bbox_inches='tight')
```

## Chart Selection Guide

**Distribution/Statistical:**

* Histogram → `plt.hist()` or `sns.histplot()`
* Box plot → `sns.boxplot()`
* Violin plot → `sns.violinplot()`
* KDE → `sns.kdeplot()`

**Comparison:**

* Bar chart → `plt.bar()` or `sns.barplot()`
* Grouped bar → `sns.barplot(hue=...)`
* Horizontal bar → `plt.barh()` or `sns.barplot(orient='h')`

**Relationship:**

* Scatter → `plt.scatter()` or `sns.scatterplot()`
* Line → `plt.plot()` or `sns.lineplot()`
* Regression → `sns.regplot()` or `sns.lmplot()`

**Heatmaps:**

* Correlation matrix → `sns.heatmap(df.corr())`
* 2D data → `plt.imshow()` or `sns.heatmap()`

**Interactive:**

* Any plotly chart → `plotly.express` or `plotly.graph_objects`
* See references/plotly-examples.md

## Best Practices

### 1. Figure Size & DPI

```python
plt.figure(figsize=(10, 6))  # Width x Height in inches
plt.savefig('output.png', dpi=300)  # Publication: 300 dpi, Web: 72-150 dpi
```

### 2. Color Palettes

```python
import seaborn as sns
sns.set_palette("husl")  # Colorful
sns.set_palette("muted")  # Soft
sns.set_palette("deep")  # Bold

colors = ['#667eea', '#764ba2', '#f6ad55', '#4299e1']
```

### 3. Styling

```python
import seaborn as sns
sns.set_theme()  # Better defaults
sns.set_style("whitegrid")  # Options: whitegrid, darkgrid, white, dark, ticks

plt.style.use('ggplot')  # Options: ggplot, seaborn, bmh, fivethirtyeight
```

### 4. Multiple Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y1)
axes[0, 1].plot(x, y2)
plt.tight_layout()  # Prevent label overlap
```

### 5. Export Formats

```python
plt.savefig('chart.png', dpi=300, bbox_inches='tight', transparent=False)

plt.savefig('chart.svg', bbox_inches='tight')

import plotly.express as px
fig = px.scatter(df, x='col1', y='col2')
fig.write_html('chart.html')
```

## Advanced Topics

See references/ for detailed guides:

* **Color theory & palettes**: references/colors.md
* **Statistical plots**: references/statistical.md
* **Plotly interactive charts**: references/plotly-examples.md
* **Multi-panel layouts**: references/layouts.md

## 示例

See scripts/ for ready-to-use examples:

* `scripts/bar_chart.py` - Bar and grouped bar charts
* `scripts/line_chart.py` - Line plots with multiple series
* `scripts/scatter_plot.py` - Scatter plots with regression
* `scripts/heatmap.py` - Correlation heatmaps
* `scripts/distribution.py` - Histograms, KDE, violin plots
* `scripts/interactive.py` - Plotly interactive charts

## Common Patterns

### Data from CSV

```python
import pandas as pd
df = pd.read_csv('data.csv')

df.plot(x='date', y='value', kind='line', figsize=(10, 6))
plt.savefig('output.png', dpi=300)

sns.lineplot(data=df, x='date', y='value')
plt.savefig('output.png', dpi=300)
```

### Dictionary Data

```python
data = {'Category A': 25, 'Category B': 40, 'Category C': 15}

plt.bar(data.keys(), data.values())
plt.savefig('output.png', dpi=300)

import pandas as pd
df = pd.DataFrame(list(data.items()), columns=['Category', 'Value'])
sns.barplot(data=df, x='Category', y='Value')
plt.savefig('output.png', dpi=300)
```

### NumPy Arrays

```python
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.savefig('output.png', dpi=300)
```

## Troubleshooting

**"No module named matplotlib"**

```bash
cd skills/python-dataviz
source .venv/bin/activate
pip install -r requirements.txt
```

**Blank output / "Figure is empty"**

* Check that `plt.savefig()` comes AFTER plotting commands
* Use `plt.show()` for interactive viewing during development

**Labels cut off**

```python
plt.tight_layout()  # Add before plt.savefig()
plt.savefig('output.png', bbox_inches='tight')
```

**Low resolution output**

```python
plt.savefig('output.png', dpi=300)  # Not 72 or 100
```

## Environment

The skill includes a venv with all dependencies. Always activate before use:

```bash
cd /home/matt/.skill-platform/workspace/skills/python-dataviz
source .venv/bin/activate
```

Dependencies: matplotlib, seaborn, plotly, pandas, numpy, kaleido (for plotly static export)

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

- Professional data visualization using Python (matplotlib, seaborn, plotly)
- Create publication-qu
- 触发关键词: using, python, visualization, dataviz, professional, data

## 常见问题

### Q1: 如何开始使用Python Dataviz？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Python Dataviz有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
