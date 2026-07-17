---
slug: chart-generator-2-0-0
name: chart-generator-2-0-0
version: "1.0.0"
displayName: Chart Generator 2.0.0
summary: Data visualization tool producing SVG charts. Use when you need bar charts,
  line charts, pie char...
license: MIT-0
description: |-
  Data visualization tool producing SVG charts. Use when you need bar
  charts, line charts, pie char...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generator, visualization, chart, data, 2.0.0, charts, producing
tags:
- Other
tools:
- read
- exec
---

# Chart Generator 2.0.0

数据可视化图表生成器，通过 `scripts/chart.sh` 生成ASCII图表或HTML文件。

## 为什么用这个 Skill？ / Why This Skill?

* **即开即用**：一条命令直接出图，不需要安装matplotlib、echarts等复杂依赖
* **双输出**：终端ASCII图表（方便命令行查看）+ HTML文件（方便分享和嵌入）
* **迷你趋势图**：Unicode sparkline一行搞定趋势展示
* Compared to asking AI directly: produces actual runnable chart output (ASCII art + HTML files), not just code snippets you'd need to run yourself

## 使用方式

脚本路径：`scripts/chart.sh`（相对于本skill目录）

### 命令一览

```bash
chart.sh bar "标签1:值1,标签2:值2,标签3:值3" [--title "标题"]

chart.sh line "1,5,3,8,2,7" [--title "趋势"]

chart.sh pie "A:30,B:50,C:20" [--title "分布"]

chart.sh table "H1,H2,H3|R1C1,R1C2,R1C3|R2C1,R2C2,R2C3"

chart.sh html-bar "A:30,B:50,C:20" --output chart.html

chart.sh sparkline "1,5,3,8,2,7,4,9"

chart.sh dashboard "标题"

chart.sh progress "已完成,总数" [--title "项目进度"]

chart.sh trend "10,15,12,20,18,25" [--title "月度增长"]

chart.sh heatmap "1,2,3|4,5,6|7,8,9" [--title "活跃度"]

chart.sh svg-bar "销售报告" "Q1:120,Q2:180,Q3:95,Q4:210" [--color blue|green|red|rainbow]

chart.sh svg-pie "市场份额" "苹果:35,三星:25,华为:20"

chart.sh svg-line "月度趋势" "1月:100,2月:150,3月:120"

chart.sh help
```

See also: `tips.md` for data visualization best practices.

### 数据格式

* **键值对**: `"标签:数值,标签:数值"` — 用于 bar, pie, html-bar
* **纯数值**: `"1,5,3,8,2,7"` — 用于 line, sparkline
* **表格**: `"列头1,列头2|行1值1,行1值2|行2值1,行2值2"` — 管道符分隔行，逗号分隔列

### 选项

* `--title "标题"` — 图表标题（bar, line, pie）
* `--output file.html` — HTML输出文件路径（html-bar）

## 输出示例 / Example Output

### 柱状图 (bar)

```text
$ chart.sh bar "销售:85,市场:62,研发:93,运维:41" --title "部门预算(万)"

  部门预算(万)
  销售  ████████████████████░  85
  市场  ███████████████░░░░░░  62
  研发  ██████████████████████ 93
  运维  ██████████░░░░░░░░░░░  41
```

### 迷你趋势图 (sparkline)

```text
$ chart.sh sparkline "3,7,2,8,5,9,1,6"
▃▆▁█▄█▁▅
```

---

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

## Commands

Use `chart-generator help` to see all available commands.

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
