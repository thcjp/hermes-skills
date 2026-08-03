---
slug: chart
name: chart
version: "1.0.0"
displayName: Chart
summary: "本地优先图表生成引擎,趋势/对比/分布可视化"
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

## 差异化优势分析

Chart作为本地优先图表生成引擎，其差异化优势主要体现在以下几个方面：
- **本地优先**：Chart不依赖于网络，所有数据存储和图表生成都在本地完成，确保了数据的安全性和隐私性。
- **简单易用**：Chart提供了简单直观的命令行接口，用户无需学习复杂的图表生成工具即可快速生成图表。
- **高度定制**：Chart支持自定义图表样式，用户可以根据自己的需求调整图表的外观。

## 同类方案对比

与市场上其他图表生成工具相比，Chart具有以下优势：
- **开源免费**：Chart遵循MIT-0协议，用户可以免费使用和修改。
- **轻量级**：Chart的安装包体积小，运行速度快，适合在资源受限的环境中运行。
- **易于集成**：Chart可以通过命令行接口与其他工具和脚本集成，方便用户构建自动化工作流。

## 解决的痛点

Chart解决了以下痛点：
- **数据可视化困难**：对于数据分析师和业务人员来说，将数据转化为直观的图表是一个挑战。Chart提供了简单易用的图表生成工具，帮助他们快速将数据可视化。
- **数据安全担忧**：许多用户担心数据在网络上传输和存储时的安全性。Chart的本地优先特性确保了数据的安全性和隐私性。

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

## 错误处理补充

### 错误场景 | 原因 | 处理方式
|---------|------|---------
| 依赖库版本不匹配 | 运行时依赖库版本与要求版本不匹配 | 确认依赖库版本，使用`pip install -r requirements.txt`来安装正确的版本。
| 图表生成失败 | 数据格式错误或数据不完整 | 检查输入数据，确保数据格式正确且完整。
| 网络连接问题 | 网络连接不稳定或中断 | 检查网络连接，确保网络连接稳定。
| 权限不足 | 没有足够的权限访问文件或目录 | 确保脚本有足够的权限，或者以管理员身份运行脚本。

## 常见问题

### Q1: 如何开始使用Chart？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Chart有什么限制？
A: 请参考已知限制章节了解具体限制。

## FAQ补充

### Q4: 如何自定义图表样式？
A: Chart支持自定义图表样式，您可以通过`make_chart.py`脚本中的`--style`参数来指定样式配置文件路径。样式配置文件是一个JSON文件，您可以在其中定义图表的颜色、字体、边框等样式属性。

### Q5: 如何导出图表？
A: 生成的图表默认保存在本地目录中。您可以使用操作系统提供的文件管理工具来导出图表，或者使用`make_chart.py`脚本中的`--output`参数来指定输出文件路径。

### Q6: 如何更新依赖库？
A: 您可以使用Python的`pip`工具来更新依赖库。首先，确保您的环境中安装了`pip`，然后运行`pip install --upgrade matplotlib`来更新matplotlib库。

### Q7: 如何在报告中嵌入图表？
A: 您可以将生成的图表文件嵌入到Markdown文档中，使用`![alt text](image_path)`语法来引用图表。确保将`image_path`替换为图表文件的路径。

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步

## 边界条件补充

Chart在处理边界条件时，应考虑以下情况：
- 输入数据为空或包含非法字符时，应返回错误信息并提示用户。
- 输入数据中的值超出图表类型支持的取值范围时，应返回错误信息并提示用户。
- 图表生成过程中，如果发生异常，应记录异常信息并返回错误信息。
