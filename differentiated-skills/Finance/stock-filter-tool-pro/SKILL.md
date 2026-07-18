---
slug: stock-filter-tool-pro
name: stock-filter-tool-pro
version: "1.0.0"
displayName: 股票筛选专业版
summary: 多市场股票筛选系统，支持多策略组合、自定义公式、历史回测与批量导出。
license: MIT
edition: pro
description: |-
  面向专业投资者与机构的股票筛选系统。支持A股/美股/港股多市场筛选、
  多策略组合（AND/OR逻辑）、自定义选股公式、历史回测验证与批量导出。
  内置行业基准对比与智能选股推荐，全面满足专业选股需求。

  核心能力:
  - 多市场支持（A股/美股/港股/ETF）
  - 多策略组合（AND/OR嵌套逻辑）
  - 自定义选股公式（支持Python表达式）
  - 历史回测验证策略有效性
  - 批量导出（CSV/Excel/JSON）
  - 行业基准对比与百分位排名
  - 智能选股推荐（基于历史表现）

  适用场景:
  - 量化选股策略开发
  - 投研团队批量筛选
  - 策略回测与验证
  - 多市场跨市场筛选
  - 智能投顾选股

  差异化:
  - 兼容免费版全部功能，无缝升级
  - 新增多市场与多策略支持
  - 自定义公式与历史回测
  - 批量导出与行业基准
  - 智能选股推荐

  触发关键词: 股票筛选, 多策略, 自定义公式, 历史回测, 批量导出, 行业基准, 智能选股, stock filter, backtest
tags:
- Finance
- 股票筛选
- 量化选股
- 企业级
tools:
- read
- exec
---

# 股票筛选专业版（PRO版）

## 概述

本系统为专业投资者和机构提供全功能的股票筛选能力。相比免费版，PRO版新增多市场支持、多策略组合、自定义公式、历史回测和批量导出等高级功能，全面满足专业选股与策略开发的复杂需求。

PRO版完全兼容免费版全部筛选条件与命令，升级后原有筛选策略可直接使用。

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

### 多策略组合示例

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

## 使用场景

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

## 快速开始

### PRO版初始化

```bash
# 安装PRO版依赖
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

## 配置示例

### PRO系统配置

```yaml
pro_config:
  markets:
    a_share:
      source: "tushare"
      api_key: "${TUSHARE_TOKEN}"
    us_stock:
      source: "yfinance"
    hk_stock:
      source: "akshare"

  strategy:
    max_conditions: 20             # 单策略最大条件数
    nested_logic: true             # 支持嵌套逻辑
    custom_formula: true           # 自定义公式
    formula_engine: "python_eval"

  backtest:
    enabled: true
    max_period: "10y"
    rebalance: ["daily", "weekly", "monthly", "quarterly"]
    benchmarks: ["CSI300", "SPY", "HSI"]
    metrics:
      - annual_return
      - max_drawdown
      - sharpe_ratio
      - sortino_ratio
      - win_rate

  export:
    formats: ["csv", "excel", "json"]
    include_charts: true
    template_dir: "./templates"

  intelligence:
    recommendation: true
    based_on: "historical_performance"
    risk_models: ["var", "beta", "volatility"]

  monitoring:
    auto_trigger: true             # 策略自动触发
    notification: true
    channels: ["telegram", "email"]
```

## 最佳实践

### PRO版高级实践

| 实践领域 | 建议做法 |
| --- | --- |
| 策略开发 | 先回测验证，再实盘应用 |
| 多市场筛选 | 注意汇率与会计准则差异 |
| 自定义公式 | 充分测试公式逻辑，避免边界错误 |
| 回测验证 | 至少覆盖3年数据，包含牛熊周期 |
| 智能推荐 | 结合个人风险偏好调整参数 |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
filter.py --conditions "pe<20"  → filter_pro.py --markets "a-share,us-stock" --export
单策略AND                      → 多策略AND/OR嵌套
终端展示                       → 批量导出CSV/Excel
```

## 常见问题

### Q1：回测结果能代表未来表现吗？

不能。历史回测仅用于验证策略逻辑的有效性，过去表现不代表未来收益。实盘交易还需考虑滑点、手续费和市场冲击成本。

### Q2：自定义公式支持哪些函数？

支持Python标准数学函数（abs、max、min、sum等）和金融函数（PEG、ROIC、Z-Score等）。可通过eval引擎执行任意合法的Python表达式。

### Q3：多市场筛选如何处理汇率？

PRO版使用实时汇率将不同市场的市值、营收等指标统一换算为人民币进行比较。汇率数据每日更新。

### Q4：智能推荐基于什么算法？

基于历史回测数据，分析不同策略在不同市场环境下的表现，结合用户风险偏好推荐最适合的选股策略和标的组合。

### Q5：支持实时策略触发吗？

支持。PRO版可设置策略自动监控，当市场出现符合条件的标的时自动触发通知。通知通过Telegram/邮件等渠道推送。

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
