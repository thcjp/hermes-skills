---
slug: "trading-strategy-guide"
name: "trading-strategy-guide"
version: "1.1.1"
displayName: "Trade With Taro"
summary: "提供交易策略分析与决策支持的AI技能。Provide AI-powered trading strategy analysis and decision support. Analyze m"
license: "Proprietary"
description: |-
  Provide AI-powered trading strategy analysis and decision support. Analyze
  market trends, evaluate trading signals, and generate strategy recommendations.
  自动分析市场趋势与交易信号,生成策略建议,提供专业的风险管理能力
tags:
  - Other
  - agent
  - llm
  - 交易
  - 策略
  - 分析
  - 风险
tools:
  - read
  - write
  - exec
homepage: ""
category: "Creative"
---
# Trade With Taro

## 核心能力

### 一、交易策略分析
- **趋势跟踪策略**: 基于移动平均线(MA/EMA)交叉、MACD金叉死叉、ADX趋势强度指标判断趋势方向,生成买入/卖出信号
- **均值回归策略**: 基于布林带(Bollinger Bands)、RSI超买超卖、Z-Score偏离度识别价格回归机会,适合震荡市场
- **动量策略**: 基于价格动量指标(ROC/MOM)、相对强度排名(RS)筛选强势标的,追涨杀跌
- **突破策略**: 基于支撑阻力位、价格通道(Donchian)、成交量突破识别关键价位突破信号

### 二、市场趋势研判
- **技术指标分析**: 综合MA/EMA/MACD/RSI/KDJ/布林带等多维度技术指标,输出趋势判断与信号强度
- **K线形态识别**: 识别常见K线形态(锤子线/十字星/吞没/启明星),结合成交量验证信号可靠性
- **多周期分析**: 结合日线/周线/月线多周期趋势一致性,过滤虚假信号,提高判断准确率
- **市场情绪指标**: 基于VIX恐慌指数、成交量比率、资金流向等指标评估市场情绪状态

### 三、策略回测与评估
- **历史回测**: 基于历史行情数据回测策略表现,计算年化收益率、最大回撤、夏普比率等核心指标
- **参数优化**: 对策略参数(如均线周期、止损比例)进行网格搜索,输出最优参数组合与过拟合风险提示
- **绩效评估**: 输出完整绩效报告,含胜率、盈亏比、收益曲线、月度收益分布等

### 四、风险管理
- **仓位管理**: 基于凯利公式(Kelly Criterion)或固定比例法计算最优仓位,控制单笔风险敞口
- **止损止盈设置**: 根据ATR(平均真实波幅)或支撑阻力位设置动态止损,锁定利润控制亏损
- **风险敞口评估**: 计算组合Beta、VaR(风险价值)、最大回撤等风险指标,评估整体风险水平
- **资金曲线分析**: 分析策略资金曲线的平稳度与回撤特征,识别策略失效信号
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 策略分析 | 市场数据与交易参数 | 策略评估结果与建议 |
| 趋势研判 | 历史行情与技术指标 | 趋势判断与信号提示 |
| 风险评估 | 持仓与风险参数 | 风险等级与止损建议 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 处理的输入数据或指令,支持文本/JSON格式,包含市场数据与交易参数 |
| strategy_type | string | 否 | 策略类型: `trend`(趋势跟踪)/`mean_reversion`(均值回归)/`momentum`(动量)/`breakout`(突破) |
| options | object | 否 | 附加配置选项,如回测周期、止损比例、仓位比例等 |
| callback_url | string | 否 | 异步回调通知URL |

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "策略分析与决策支持结果",
    "execution_time": "1.5s",
    "metadata": {
      "version": "1.0",
      "processor": "trading-strategy-guide"
    }
  },
  "execution_log": ["解析输入参数", "加载市场数据", "执行策略分析", "生成风险评估", "格式化输出结果"],
  "error": null
}
```

输出模板参考: `assets/output.json`

## 示例代码

### 1. 双均线趋势跟踪策略回测（Python）

基于短/长期移动平均线交叉信号进行历史回测,计算核心绩效指标:

```python
import pandas as pd
import numpy as np

def ma_crossover_backtest(df, short_window=20, long_window=50, initial_capital=100000):
    """双均线交叉策略回测"""
    # 计算移动平均线
    df['MA_short'] = df['close'].rolling(window=short_window).mean()
    df['MA_long'] = df['close'].rolling(window=long_window).mean()

    # 生成交易信号: 短均线上穿长均线买入(1),下穿卖出(-1)
    df['signal'] = 0
    df.loc[df['MA_short'] > df['MA_long'], 'signal'] = 1
    df.loc[df['MA_short'] < df['MA_long'], 'signal'] = -1
    df['position'] = df['signal'].shift(1).fillna(0)  # 次日开盘执行

    # 计算策略收益
    df['daily_return'] = df['close'].pct_change()
    df['strategy_return'] = df['position'] * df['daily_return']
    df['equity_curve'] = (1 + df['strategy_return']).cumprod() * initial_capital

    # 绩效指标
    total_days = len(df)
    annual_return = (df['equity_curve'].iloc[-1] / initial_capital) ** (252 / total_days) - 1
    max_drawdown = ((df['equity_curve'] / df['equity_curve'].cummax()) - 1).min()
    sharpe_ratio = df['strategy_return'].mean() / df['strategy_return'].std() * np.sqrt(252)
    win_rate = (df[df['strategy_return'] != 0]['strategy_return'] > 0).mean()

    return {
        "annual_return": f"{annual_return:.2%}",
        "max_drawdown": f"{max_drawdown:.2%}",
        "sharpe_ratio": round(sharpe_ratio, 2),
        "win_rate": f"{win_rate:.2%}",
        "final_equity": round(df['equity_curve'].iloc[-1], 2),
    }

# 示例：对某股票日线数据进行回测
# df = pd.read_csv('stock_daily.csv', parse_dates=['date'])
# result = ma_crossover_backtest(df, short_window=20, long_window=50)
# print(result)
# {'annual_return': '15.30%', 'max_drawdown': '-12.50%', 'sharpe_ratio': 1.05, ...}
```

### 2. 基于ATR的动态止损设置（Python）

```python
def atr_stop_loss(df, period=14, multiplier=2.0):
    """基于ATR设置动态止损价位"""
    high_low = df['high'] - df['low']
    high_close = (df['high'] - df['close'].shift(1)).abs()
    low_close = (df['low'] - df['close'].shift(1)).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.rolling(window=period).mean()

    # 多头止损 = 最高价 - ATR × 倍数
    df['stop_loss'] = df['high'].rolling(window=period).max() - atr * multiplier
    return df[['close', 'stop_loss', 'atr']]
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 常见问题

### Q1: 如何开始使用Trade With Taro？
A: 在AI Agent对话中直接调用本技能,提供市场数据(如股票代码、历史行情)和分析目标(如趋势判断、策略回测、风险评估),技能将自动生成分析报告与策略建议。建议首次使用时先提供少量数据验证分析效果,再逐步扩展到完整回测。

### Q2: 回测结果可靠吗?如何避免过拟合?
A: 回测结果仅供参考,不构成投资建议。避免过拟合的方法:(1)使用样本外数据进行验证;(2)限制参数优化空间,避免过度调参;(3)关注策略逻辑的经济学含义而非纯数据拟合;(4)检查策略在不同市场环境下的稳定性。

### Q3: 支持哪些市场的数据分析?
A: 支持A股、港股、美股等主要市场的历史行情数据分析。需用户提供OHLCV(开盘/最高/最低/收盘/成交量)格式的行情数据,技能据此进行技术指标计算、信号生成与回测评估。

## 已知限制

- **非投资建议**: 本技能提供的所有分析结果仅供参考与学习,不构成任何投资建议,实际交易决策需投资者自行判断并承担风险
- **历史不代表未来**: 基于历史数据回测的策略表现无法保证未来收益,市场环境变化可能导致策略失效
- **数据质量依赖**: 分析结果的准确性高度依赖输入数据的质量与完整性,缺失或错误数据将导致误导性结论
- **技术分析局限**: 技术指标与K线形态基于历史价格数据,无法预测突发事件(黑天鹅)对市场的冲击
- **不支持实时交易**: 本技能仅提供分析与建议,不连接实盘交易系统,无法执行实际买卖操作

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
