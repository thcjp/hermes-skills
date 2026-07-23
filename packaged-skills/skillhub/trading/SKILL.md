---
slug: "trading"
name: "trading"
version: "1.0.0"
displayName: "交易分析专业版"
summary: "多策略交易分析系统，支持批量分析、策略回测、自动交易与风险控制。"
license: "Proprietary"
edition: "pro"
description: |-
  面向专业交易者的多策略交易分析系统。支持维加斯通道、MACD、布林带
  等多种技术策略组合，提供批量标的分析、历史回测验证、自动信号触发
  与风险控制功能。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Finance
  - 交易分析
  - 量化策略
  - 企业级
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 交易分析专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 交易分析专业版多策略交易分析 | 不支持 | 支持 |
| 交易分析专业版支持批量分析 | 不支持 | 支持 |
| DCF估值建模与敏感性分析 | 不支持 | 支持 |
| 财务舞弊识别(Beneish M-Score) | 不支持 | 支持 |
| 批量财报处理与自动化报告 | 不支持 | 支持 |

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
|:-----|:-----|:-----|
| 策略数量 | 仅维加斯通道 | 10+种策略组合 |
| 标的分析 | 单只 | 批量并行 |
| 历史回测 | 不支持 | 支持+绩效报告 |
| 自动触发 | 不支持 | 信号自动通知 |
| 风险控制 | 不支持 | 止损/仓位管理 |
| 多周期 | 日线/周线 | 分钟至月线 |
| 策略优化 | 不支持 | 参数自动优化 |
| 数据导出 | 不支持 | CSV/Excel |

### 支持的策略
| 策略 | 类型 | 说明 |
|---:|---:|---:|
| 维加斯通道 | 趋势跟踪 | EMA+ATR通道 |
| MACD | 动量指标 | 金叉死叉信号 |
| 布林带 | 波动率 | 突破回归策略 |
| RSI | 超买超卖 | 反转信号 |
| 均线系统 | 趋势 | 多空排列 |
| KDJ | 随机指标 | 短期反转 |
| 量价分析 | 量能 | 量价配合 |
| 斐波那契 | 回调位 | 支撑阻力 |
| 海龟交易 | 突破 | 唐奇安通道 |
| 自定义 | 组合 | Python公式 |

**输入**: 用户提供支持的策略所需的指令和必要参数.
**输出**: 返回支持的策略的处理结果,包含执行状态码、结果数据和执行日志.
### 策略数量

针对策略数量,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供策略数量相关的配置参数、输入数据和处理选项.
**输出**: 返回策略数量的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`策略数量`的配置文档进行参数调优
#
## 适用场景

### 场景一：批量信号扫描

用户输入："扫描科技板块所有股票的买卖信号"

```bash
# 批量信号扫描
python3 （请参考skill目录中的脚本文件） \
  --sector "科技" \
  --strategies "vegas,macd,bollinger" \
  --export \
  --output tech_signals.xlsx
# ...
# 输出包含：
# - 各标的信号汇总
# - 策略一致性评分
# - 信号强度排名
# - 建议关注列表
```

### 场景二：策略回测

用户输入："回测维加斯通道策略在AAPL上过去5年的表现"

```bash
# 历史回测
python3 （请参考skill目录中的脚本文件） \
  --ticker AAPL \
  --strategy "vegas" \
  --period "5y" \
  --initial-capital 100000 \
  --output backtest_report.pdf
# ...
# 输出包含：
# - 年化收益率
# - 最大回撤
# - 夏普比率
# - 交易记录
# - 收益曲线
```

### 场景三：自动信号触发

用户输入："监控我的自选股，出现买入信号时通知我"

```bash
# 设置自动监控
python3 （请参考skill目录中的脚本文件） \
  --watchlist "AAPL,MSFT,GOOG,TSLA" \
  --strategies "vegas,macd" \
  --signal-type "buy" \
  --notify "telegram,webhook" \
  --interval 60
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt
# ...
# 配置策略与通知
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# 批量扫描
python3 （请参考skill目录中的脚本文件） --sector "科技" --strategies "vegas,macd" --export
# ...
# 多策略分析
python3 （请参考skill目录中的脚本文件） --ticker AAPL --strategies "vegas,macd,bollinger"
# ...
# 历史回测
python3 （请参考skill目录中的脚本文件） --ticker AAPL --strategy "vegas" --period "5y"
# ...
# 自动监控
python3 （请参考skill目录中的脚本文件） --watchlist "AAPL,MSFT" --notify "telegram"
# ...
# 策略优化
python3 （请参考skill目录中的脚本文件） --strategy "vegas" --ticker AAPL --period "3y"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | trading处理的内容输入 |,  |
| content | string | 否 | trading处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "trading 相关配置参数",
    result: "trading 相关配置参数",
    result: "trading 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
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
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| yfinance | Python库 | 必需 | `pip install yfinance` |
| pandas | Python库 | 必需 | `pip install pandas` |
| numpy | Python库 | 必需 | `pip install numpy` |
| ta | Python库 | 必需 | `pip install ta`（技术指标） |
| matplotlib | Python库 | 可选 | `pip install matplotlib`（图表） |
| scipy | Python库 | 可选 | `pip install scipy`（优化） |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:------:|--------|:-------|:------:|
| Tushare | `TUSHARE_TOKEN` | 可选 | A股专业数据 |
| Telegram Bot | `TELEGRAM_BOT_TOKEN` | 可选 | 信号通知 |
| Webhook | `WEBHOOK_URL` | 可选 | 信号推送 |

- 未配置的服务自动跳过，不影响核心功能
- 所有凭证存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 多策略交易分析系统，支持批量分析与历史回测
- **PRO版特性**: 多策略组合、批量扫描、历史回测、自动触发、风险控制、参数优化
- **兼容性**: 完全兼容免费版维加斯通道策略与命令
- **风险提示**: 交易有风险，策略仅供参考，不构成投资建议

## 案例展示

### PRO交易系统配置

```yaml
pro_config:
  strategies:
    enabled:
      - vegas
      - macd
      - bollinger
      - rsi
      - ma_system
    combination_logic: "majority_vote"   # 多数表决
    min_consensus: 0.6                   # 最低一致性
# ...
  backtest:
    initial_capital: 100000
    commission: 0.0003                   # 手续费率
    slippage: 0.001                      # 滑点
    benchmarks: ["SPY", "CSI300"]
# ...
  risk_control:
    stop_loss: 0.05                      # 止损5%
    take_profit: 0.15                    # 止盈15%
    max_position: 0.25                   # 单标的最大仓位25%
    max_drawdown: 0.20                   # 最大回撤20%
    position_sizing: "kelly"             # 凯利公式
# ...
  monitoring:
    watchlist: ["AAPL", "MSFT", "GOOG"]
    scan_interval: 60
    notification:
      channels: ["telegram", "webhook"]
      webhook_url: "${WEBHOOK_URL}"
# ...
  optimization:
    method: "grid_search"                # grid_search | bayesian
    parameters:
      vegas:
        ema_period: [55, 144, 233]
        atr_multiplier: [1.5, 2.0, 2.5, 3.0]
# ...
  export:
    formats: ["csv", "excel", "json"]
    include_charts: true
```

## 常见问题

### Q1：多策略组合如何工作？

PRO版支持多种策略组合方式：多数表决（至少N个策略信号一致）、加权评分（各策略加权综合）、OR逻辑（任一策略触发）。默认使用多数表决，可配置.
### Q2：回测结果可靠吗？

回测使用历史数据模拟，存在过拟合风险。建议：留出样本外数据验证、考虑交易成本、使用稳健的参数（非最优参数）。过去表现不代表未来收益.
### Q3：自动交易功能安全吗？

PRO版的自动触发仅推送信号通知，不直接执行交易。如需自动执行交易，需额外对接券商API，并充分了解相关风险.
### Q4：参数优化会过拟合吗？

存在过拟合风险。PRO版提供网格搜索和贝叶斯优化两种方法，建议留出至少30%的数据作为样本外验证，避免在样本内过度优化.
### Q5：支持哪些市场？

PRO版支持A股、美股、港股和加密货币市场。A股数据来自AkShare/Tushare，美股来自Yahoo Finance，加密货币来自CoinGecko.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

