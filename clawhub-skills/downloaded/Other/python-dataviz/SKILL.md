---
slug: python-dataviz
name: python-dataviz
version: "1.0.0"
displayName: Python Dataviz
summary: Professional data visualization using Python (matplotlib, seaborn, plotly).
  Create publication-qu...
license: MIT
description: |-
  Professional data visualization using Python (matplotlib, seaborn, plotly).
  Create publication-qu...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: using, python, visualization, dataviz, professional, data
tags:
- Other
tools:
- read
- exec
---

# Python Dataviz

Create professional charts, graphs, and statistical visualizations using Python's leading libraries.

## Libraries & Use Cases

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

## Example Scripts

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
