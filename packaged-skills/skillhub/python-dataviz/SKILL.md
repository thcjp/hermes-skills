---
slug: "python-dataviz"
name: "python-dataviz"
version: "1.0.0"
displayName: "Python Dataviz"
summary: "用Python(matplotlib/seaborn/plotly)做专业数据可视化"
license: "Proprietary"
description: |-
  Professional data visualization using Python (matplotlib, seaborn, plotly)。Create publication-qu。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Other
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec", "glob"]
tags: "数据处理,数据分析,工具"
---
# Python Dataviz

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

- Professional data visualization using Python (matplotlib, seaborn, plotly)
- Create publication-qu
#
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

## 使用流程

### Setup Environment

```bash
cd skills/python-dataviz
python3 -m venv .venv
source .venv/（请参考skill目录中的脚本文件）
pip install .
```

### Create a Chart

```python
import matplotlib.pyplot as plt
import numpy as np
# ...
x = np.linspace(0, 10, 100)
y = np.sin(x)
# ...
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, color='#667eea')
plt.title('Sine Wave', fontsize=16, fontweight='bold')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(alpha=0.3)
plt.tight_layout()
# ...
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.savefig('output.svg', bbox_inches='tight')
```

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "dataviz 相关配置参数",
    result: "dataviz 相关配置参数"
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 其他异常 | 内部处理异常 | 检查输入后 |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

See scripts/ for ready-to-use examples:

* `（请参考skill目录中的脚本文件）` - Bar and grouped bar charts
* `（请参考skill目录中的脚本文件）` - Line plots with multiple series
* `（请参考skill目录中的脚本文件）` - Scatter plots with regression
* `（请参考skill目录中的脚本文件）` - Correlation heatmaps
* `（请参考skill目录中的脚本文件）` - Histograms, KDE, violin plots
* `（请参考skill目录中的脚本文件）` - Plotly interactive charts

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

