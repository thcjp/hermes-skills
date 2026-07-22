---
slug: "chart-free"
name: "chart-free"
version: "1.0.0"
displayName: "本地图表生成-免费版"
summary: "本地优先的图表生成免费版，支持bar与line两种基础类型，无需联网，适合快速可视化。"
license: "MIT"
description: |-
  本地优先的图表生成引擎免费版，提供柱状图与折线图两种基础类型。
  基于Python与matplotlib，所有数据与产物仅落地本地。
  核心能力：
  - 两种基础图表类型：bar/line
  - 内联数据生成：make_chart.py 直接从--labels/--values生成图片
  - 存储初始化：init_storage.py 一键初始化本地存储
  升级付费版专享：pie/scatter类型、智能选型、历史管理、多类型组合工作流。
tags:
  - 需求设计
  - 数据可视化
  - matplotlib
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# Chart — 本地图表生成引擎（免费版）

## 核心理念

1. 优先清晰，而非图表种类繁多。
2. 选择让对比一目了然的最简图表。
3. 仅使用本地生成，不调用任何云端图表API。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。

## 核心能力

### 核心理念

1. 优先清晰，而非图表种类繁多。
2. 选择让对比一目了然的最简图表。
3. 仅使用本地生成，不调用任何云端图表API。

**输入**: 用户提供核心理念所需的参数和指令。

### 存储路径

所有数据仅落地本地：

- `~/.skill-platform/workspace/memory/chart/charts.json` — 图表历史索引
- `~/.skill-platform/workspace/memory/chart/output/` — 图表图片输出目录

无云同步，无第三方图表API。

**输入**: 用户提供存储路径所需的参数和指令。
**处理**: 按照skill规范执行存储路径操作。

### 支持的图表类型（免费版）

| 类型 | 字段名 | 适用场景 |
|------|--------|---------|
| 柱状图 | `bar` | 类别间数量对比 |
| 折线图 | `line` | 时间序列趋势 |

> 饼图 `pie` 与散点图 `scatter` 为付费版专享。

**输入**: 用户提供支持的图表类型（免费版）所需的参数和指令。
**处理**: 按照skill规范执行支持的图表类型（免费版）操作。
**输出**: 返回支持的图表类型（免费版）的执行结果,包含操作状态和输出数据。

### 脚本一览（免费版）

| 脚本 | 用途 |
|------|------|
| `init_storage.py` | 初始化本地图表存储目录与索引文件 |
| `make_chart.py` | 从内联数据生成图表图片 |

> `suggest_chart.py`（智能选型）与 `list_charts.py`（历史管理）为付费版专享。

**输入**: 用户提供脚本一览（免费版）所需的参数和指令。
**处理**: 按照skill规范执行脚本一览（免费版）操作。

### 核心能力（免费版）


**输入**: 用户提供核心能力（免费版）所需的指令和必要参数。
**处理**: 按照skill规范执行核心能力（免费版）操作,遵循单一意图原则。
**输出**: 返回核心能力（免费版）的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`核心能力（免费版）`相关配置参数进行设置
### 1. 内联数据生成图表

使用 `make_chart.py` 直接从命令行参数生成图表图片：

```bash
python3 {baseDir}/scripts/make_chart.py \
  --type bar \
  --title "季度销售额" \
  --labels "Q1,Q2,Q3,Q4" \
  --values "10,20,15,25"
```

- `--

**处理**: 按照skill规范执行核心能力（免费版）操作。

### 付费版专享能力

> 升级付费版解锁以下高级能力：

- **饼图 `pie`**：简单部分占整体比例可视化。
- **散点图 `scatter`**：两个变量间关系分析。
- **智能选型 `suggest_chart.py`**：根据数据特征自动推荐最佳图表类型与理由。
- **历史管理 `list_charts.py`**：查看历史生成记录，按时间/类型/标题回溯。
- **多类型组合工作流**：选型→生成→

**输入**: 用户提供付费版专享能力所需的参数和指令。
**处理**: 按照skill规范执行付费版专享能力操作。

#
## 存储路径

所有数据仅落地本地：

- `~/.skill-platform/workspace/memory/chart/charts.json` — 图表历史索引
- `~/.skill-platform/workspace/memory/chart/output/` — 图表图片输出目录

无云同步，无第三方图表API。

## 支持的图表类型（免费版）

| 类型 | 字段名 | 适用场景 |
|------|--------|---------|
| 柱状图 | `bar` | 类别间数量对比 |
| 折线图 | `line` | 时间序列趋势 |

> 饼图 `pie` 与散点图 `scatter` 为付费版专享。

## 脚本一览（免费版）

| 脚本 | 用途 |
|------|------|
| `init_storage.py` | 初始化本地图表存储目录与索引文件 |
| `make_chart.py` | 从内联数据生成图表图片 |

> `suggest_chart.py`（智能选型）与 `list_charts.py`（历史管理）为付费版专享。

## 核心能力（免费版）

### 1. 内联数据生成图表

使用 `make_chart.py` 直接从命令行参数生成图表图片：

```bash
python3 {baseDir}/scripts/make_chart.py \
  --type bar \
  --title "季度销售额" \
  --labels "Q1,Q2,Q3,Q4" \
  --values "10,20,15,25"
```

- `--type`：必填，免费版仅支持 `bar`/`line`
- `--title`：图表标题
- `--labels`：以英文逗号分隔的标签序列
- `--values`：以英文逗号分隔的数值序列，须与labels等长

输出PNG文件落地到 `~/.skill-platform/workspace/memory/chart/output/`。

### 2. 存储初始化

首次使用前运行 `init_storage.py` 创建目录结构与索引文件：

```bash
python3 {baseDir}/scripts/init_storage.py
```

## 使用流程

1. **确认环境**：检查 `python3` 与 `matplotlib` 是否可用（`python3 -c "import matplotlib"`）。
2. **初始化存储**：首次使用运行 `init_storage.py` 建立目录与索引。
3. **生成图表**：用 `make_chart.py --type bar|line --title "..." --labels "..." --values "..."` 生成PNG。
4. **校验输出**：检查 `output/` 目录下的图片文件，确认渲染正确。
5. **复用产物**：将PNG嵌入报告、幻灯片或决策文档。

## 示例

### 示例1：柱状图对比季度销售

```bash
python3 {baseDir}/scripts/make_chart.py \
  --type bar \
  --title "2024年季度销售额(万元)" \
  --labels "Q1,Q2,Q3,Q4" \
  --values "120,180,150,210"
```

输出文件：`~/.skill-platform/workspace/memory/chart/output/chart_20250320_001.png`

### 示例2：折线图展示月度趋势

```bash
python3 {baseDir}/scripts/make_chart.py \
  --type line \
  --title "月度活跃用户" \
  --labels "1月,2月,3月,4月,5月,6月" \
  --values "3200,3500,4100,4500,4300,4900"
```

## 付费版专享能力

> 升级付费版解锁以下高级能力：

- **饼图 `pie`**：简单部分占整体比例可视化。
- **散点图 `scatter`**：两个变量间关系分析。
- **智能选型 `suggest_chart.py`**：根据数据特征自动推荐最佳图表类型与理由。
- **历史管理 `list_charts.py`**：查看历史生成记录，按时间/类型/标题回溯。
- **多类型组合工作流**：选型→生成→回溯的完整链路。
- **高级渲染选项**：自定义颜色、字体、坐标系等。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `python3: command not found` | 系统未安装Python 3 | 安装Python 3.x并确保 `python3` 在PATH中 |
| `ModuleNotFoundError: matplotlib` | matplotlib未安装 | 运行 `pip3 install matplotlib` 后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |
| `--labels`与`--values`长度不匹配 | 序列项数不一致 | 检查逗号分隔项数，确保两序列等长 |
| `--type`取值非法或为pie/scatter | 免费版仅支持bar/line | 升级付费版解锁pie与scatter类型 |
| `--values`含非数值 | 数值序列中混入字符串 | 确保所有值为数字，移除单位与中文符号 |
| 输出目录不可写 | `output/` 权限不足 | 检查目录权限或重新运行 `init_storage.py` |
| 标签含中文乱码 | matplotlib默认字体缺中文字形 | 配置 `matplotlib.rcParams['font.sans-serif']` 添加中文字体 |

## 常见问题

### Q1：免费版支持哪些图表类型？
免费版支持 `bar`（柱状图）与 `line`（折线图）两种基础类型。`pie` 与 `scatter` 为付费版专享。

### Q2：是否需要联网？
不需要。所有生成过程本地完成，不调用任何第三方图表API，无云同步。

### Q3：如何选择图表类型？
免费版需手动判断：类别对比用 `bar`，时间趋势用 `line`。付费版提供 `suggest_chart.py` 自动推荐。

### Q4：生成的图片存在哪里？
统一落地到 `~/.skill-platform/workspace/memory/chart/output/` 目录，文件名带时间戳。

### Q5：matplotlib默认字体不支持中文怎么办？
通过 `matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']` 配置中文字体。

### Q6：如何升级到付费版？
参考 `chart` 付费版SKILL.md，解锁pie/scatter类型、智能选型、历史管理与多类型组合工作流。

## 已知限制

- 仅支持 `bar` 与 `line` 两种基础类型，pie/scatter为付费版专享。
- 数据需通过 `--labels`/`--values` 内联传入，暂不支持直接读取CSV。
- 输出固定为PNG格式，暂不支持SVG或PDF矢量输出。
- 中文字体需手动配置 `matplotlib.rcParams`，否则会出现乱码。
- 无历史管理能力，无法回溯历史生成记录。
- 无智能选型能力，需手动判断图表类型。
