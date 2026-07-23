---
slug: "stock-filter"
name: "stock-filter"
version: "1.0.0"
displayName: "股票筛选专业版"
summary: "多市场股票筛选系统，支持多策略组合、自定义公式、历史回测与批量导出。"
license: "Proprietary"
edition: "pro"
description: |-
  面向专业投资者与机构的股票筛选系统。支持A股/美股/港股多市场筛选、
  多策略组合（AND/OR逻辑）、自定义选股公式、历史回测验证与批量导出。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
  - Finance
  - 股票筛选
  - 量化选股
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
---
# 股票筛选专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### PRO版功能增强对比
| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 市场覆盖 | 仅A股 | A股/美股/港股/ETF |
| 策略组合 | 单策略AND | 多策略AND/OR嵌套 |
| 自定义公式 | 不支持 | Python表达式 |
| 历史回测 | 不支持 | 支持+收益曲线 |
| 批量导出 | 不支持 | CSV/Excel/JSON |
| 行业基准 | 不支持 | 百分位排名 |
| 智能推荐 | 不支持 | 基于历史表现 |
| 实时监控 | 不支持 | 策略自动触发 |

**处理**: 按照skill规范执行PRO版功能增强对比操作,遵循单一意图原则。
### 示例
```yaml
# PRO版支持复杂逻辑组合
strategy:
  name: "价值成长复合策略"
  logic: AND
  groups:
    - name: "价值条件"
      logic: OR
      conditions:
        - pe < 20
        - pb < 1.5
    - name: "成长条件"
      logic: AND
      conditions:
        - revenue_growth > 0.2
        - net_income_growth > 0.25
    - name: "技术确认"
      logic: OR
      conditions:
        - macd_cross = golden
        - price_above_ma20 = true
```

**输入**: 用户提供示例所需的指令和必要参数。
**处理**: 按照skill规范执行示例操作,遵循单一意图原则。
**输出**: 返回示例的执行结果,包含操作状态和输出数据。
### 市场覆盖

执行市场覆盖操作,处理用户输入并返回结果。

**输入**: 用户提供市场覆盖所需的参数和指令。

**输出**: 返回市场覆盖的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`市场覆盖`相关配置参数进行设置
#
## 适用场景

### 场景一：多市场筛选

用户输入："在A股和美股中筛选PE<20、ROE>15%的股票"

```bash
# 多市场筛选
python3 scripts/filter_pro.py \
  --markets "a-share,us-stock" \
  --conditions "pe<20,roe>15" \
  --export \
  --output multi_market_stocks.xlsx

# 输出包含：
# - A股符合条件的股票列表
# - 美股符合条件的股票列表
# - 多市场对比分析
```

### 场景二：策略回测

用户输入："回测这个选股策略过去3年的表现"

```bash
# 历史回测
python3 scripts/backtest.py \
  --strategy "value_growth" \
  --period "3y" \
  --rebalance "monthly" \
  --benchmark "CSI300" \
  --output backtest_report.pdf

# 输出包含：
# - 年化收益率
# - 最大回撤
# - 夏普比率
# - 收益曲线图
# - 月度收益分布
```

### 场景三：自定义公式

用户输入："用自定义公式筛选PEG<1且现金流为正的股票"

```bash
# 自定义公式筛选
python3 scripts/filter_pro.py \
  --formula "peg < 1 and operating_cashflow > 0 and debt_ratio < 0.5" \
  --markets "a-share" \
  --export \
  --output custom_screen.xlsx
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 配置数据源
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# 多市场筛选
python3 scripts/filter_pro.py --markets "a-share,us-stock" --conditions "pe<20,roe>15" --export

# 自定义公式
python3 scripts/filter_pro.py --formula "peg < 1 and roe > 15" --export

# 历史回测
python3 scripts/backtest.py --strategy "value_growth" --period "3y" --benchmark "CSI300"

# 行业基准
python3 scripts/benchmark.py --industry "白酒" --metric "roe,pe,pb"

# 智能推荐
python3 scripts/recommend.py --risk-tolerance moderate --count 20
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明"
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| akshare | Python库 | 必需 | `pip install akshare` |
| yfinance | Python库 | 必需 | `pip install yfinance`（美股） |
| pandas | Python库 | 必需 | `pip install pandas` |
| numpy | Python库 | 必需 | `pip install numpy` |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |
| matplotlib | Python库 | 可选 | `pip install matplotlib`（图表） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| Tushare | `TUSHARE_TOKEN` | 推荐 | A股专业数据 |
| Alpha Vantage | `ALPHA_VANTAGE_API_KEY` | 可选 | 美股数据备选 |

- 未配置API Key时使用AkShare免费数据
- API Key存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 多市场股票筛选系统，支持策略回测与批量导出
- **PRO版特性**: 多市场、多策略组合、自定义公式、历史回测、批量导出、智能推荐
- **兼容性**: 完全兼容免费版筛选条件与命令

## 案例展示

### 示例1: 基础用法
**输入**: 示例数据
**输出**: 示例数据

### 示例2: 进阶用法
**输入**: 示例数据
**输出**: 示例数据

### 示例3: 边界情况 - 边界情况
**输入**: 示例数据
**输出**: 示例数据

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

