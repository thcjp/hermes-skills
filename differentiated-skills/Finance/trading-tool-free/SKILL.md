---
slug: trading-tool-free
name: trading-tool-free
version: "1.0.0"
displayName: 交易分析入门工具
summary: 基于维加斯通道的交易分析工具，提供趋势识别与基础买卖信号判断。
license: MIT
edition: free
description: |-
  面向个人交易者的技术分析工具，基于维加斯通道（Vegas Channel）策略
  提供趋势识别与买卖信号判断。适合个人投资者进行单只标的的技术分析
  与交易决策辅助。

  核心能力:
  - 维加斯通道绘制与趋势识别
  - 基础买卖信号生成
  - 支撑阻力位识别
  - 单只标的技术分析

  适用场景:
  - 个人交易决策辅助
  - 趋势跟踪策略
  - 技术分析学习
  - 单只标的分析

  差异化:
  - 免费版聚焦维加斯通道单策略
  - 适合个人用户单标的分析
  - 不支持多策略组合
  - 不支持批量分析与回测

  触发关键词: 交易分析, 维加斯通道, 趋势识别, 买卖信号, 支撑阻力, 技术分析, trading, vegas channel
tags:
- Finance
- 交易分析
- 技术分析
tools:
- read
- exec
---

# 交易分析入门工具（免费版）

## 概述

本工具为个人交易者提供基于维加斯通道（Vegas Channel）的技术分析能力。维加斯通道是一种基于指数移动平均线（EMA）的趋势跟踪策略，通过上下通道线识别趋势方向与支撑阻力位。适合个人投资者进行单只标的的技术分析。

## 核心能力

### 维加斯通道策略

| 组成部分 | 参数 | 说明 |
| --- | --- | --- |
| 上轨 | EMA(144) + ATR | 阻力位/超买区 |
| 中轨 | EMA(144) | 趋势基准线 |
| 下轨 | EMA(144) - ATR | 支撑位/超卖区 |
| 信号线 | EMA(12) | 短期趋势信号 |

### 分析功能

| 功能 | 说明 | 免费版支持 |
| --- | --- | --- |
| 通道绘制 | 维加斯通道可视化 | 支持 |
| 趋势识别 | 上升/下降/震荡 | 支持 |
| 买卖信号 | 基础信号生成 | 支持 |
| 支撑阻力 | 关键价位识别 | 支持 |
| 多标的分析 | 批量分析 | 不支持 |
| 策略回测 | 历史验证 | 不支持 |
| 多策略组合 | 策略叠加 | 不支持 |
| 自动交易 | 信号执行 | 不支持 |

## 使用场景

### 场景一：趋势识别

用户输入："分析一下AAPL的当前趋势"

```bash
# 维加斯通道分析
python3 scripts/vegas_analysis.py --ticker AAPL

# 输出：
# === AAPL 维加斯通道分析 ===
# 当前价格: $178.45
# 上轨: $182.30 (阻力)
# 中轨: $175.20 (趋势线)
# 下轨: $168.10 (支撑)
# 趋势: 上升趋势
# 信号: 持有/观望
```

### 场景二：买卖信号

用户输入："BTC现在有买卖信号吗？"

```bash
# 信号检测
python3 scripts/signal.py --ticker BTC-USD

# 输出信号类型与建议
```

### 场景三：支撑阻力位

用户输入："TSLA的关键支撑阻力位在哪里？"

```bash
# 支撑阻力分析
python3 scripts/levels.py --ticker TSLA

# 输出各关键价位
```

## 快速开始

### 环境准备

```bash
# 安装依赖
pip install yfinance pandas numpy ta

# 运行分析
python3 scripts/vegas_analysis.py --ticker AAPL
```

### 常用命令

```bash
# 维加斯通道分析
python3 scripts/vegas_analysis.py --ticker AAPL
python3 scripts/vegas_analysis.py --ticker BTC-USD

# 买卖信号
python3 scripts/signal.py --ticker AAPL

# 支撑阻力
python3 scripts/levels.py --ticker TSLA

# 趋势判断
python3 scripts/trend.py --ticker MSFT
```

## 配置示例

### 策略配置

```yaml
trading_config:
  data_source: "yahoo_finance"
  cache_ttl: 300

  vegas_channel:
    ema_period: 144              # 中轨EMA周期
    atr_period: 14               # ATR周期
    atr_multiplier: 2.0          # ATR乘数
    signal_ema: 12               # 信号线EMA

  signals:
    buy_conditions:
      - price_above_middle
      - signal_ema_cross_up
    sell_conditions:
      - price_below_middle
      - signal_ema_cross_down

  timeframes:
    - "1d"                       # 日线
    - "1w"                       # 周线
```

## 最佳实践

1. **多周期确认**：日线与周线信号一致时更可靠
2. **趋势优先**：顺势交易，避免逆势操作
3. **止损纪律**：跌破下轨严格止损
4. **信号验证**：单一信号仅供参考，建议结合其他指标

| 实践要点 | 说明 |
| --- | --- |
| 通道含义 | 价格在中轨上方为多头，下方为空头 |
| 信号滞后 | EMA策略有滞后性，适合趋势而非震荡 |
| 假突破 | 价格短暂突破通道后回落需警惕 |
| 免责声明 | 分析结果仅供参考，不构成投资建议 |

## 常见问题

### Q1：维加斯通道适合什么市场？

维加斯通道适合趋势明显的市场，在震荡市中可能产生较多假信号。建议用于股票、指数等趋势性较强的标的。

### Q2：免费版支持多只标的同时分析吗？

免费版仅支持单只标的分析。如需批量分析多只标的，建议升级PRO版。

### Q3：信号准确率如何？

任何技术分析指标都无法保证100%准确率。维加斯通道在趋势市中表现较好，震荡市中可能频繁出错。建议结合基本面和其他技术指标综合判断。

### Q4：支持自动交易吗？

免费版仅提供信号分析，不支持自动交易执行。如需自动交易功能，建议升级PRO版。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| yfinance | Python库 | 必需 | `pip install yfinance` |
| pandas | Python库 | 必需 | `pip install pandas` |
| numpy | Python库 | 必需 | `pip install numpy` |
| ta | Python库 | 可选 | `pip install ta`（技术指标） |

### API Key 配置

- 免费版无需任何API Key
- 数据通过Yahoo Finance免费获取

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 基于维加斯通道策略的技术分析工具
- **免费版限制**: 单标的、单策略、不支持回测与自动交易
