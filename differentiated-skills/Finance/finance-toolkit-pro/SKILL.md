---
slug: finance-toolkit-pro
name: finance-toolkit-pro
version: "1.0.0"
displayName: 行情追踪专业工具
summary: 多数据源行情追踪，支持股票、ETF、指数、外汇、加密货币，含告警与批量导出。
license: Proprietary
edition: pro
description: |-
  面向专业投资者与交易团队的多数据源行情追踪工具。支持股票、ETF、指数、
  外汇、加密货币的实时报价与深度历史数据，内置多数据源自动回退、价格
  告警、批量导出与组合分析功能。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Finance
- 行情追踪
- 多数据源
- 企业级
tools:
  - - read
- exec
---

# 行情追踪专业工具（PRO版）

## 概述

本工具为专业投资者和交易团队提供多数据源聚合的金融市场行情追踪能力。相比免费版，PRO版新增多数据源自动回退、加密货币实时行情、价格告警、批量导出与组合分析等高级功能，全面满足专业交易与投资管理需求。

PRO版完全兼容免费版全部命令与工作流，升级后无需修改现有配置。

## 核心能力

### 多数据源策略

| 标的类型 | 主数据源 | 备选数据源 | 更新频率 |
| --- | --- | --- | --- |
| 美股/ETF | Alpha Vantage | Yahoo Finance | 实时 |
| 指数 | Yahoo Finance | IEX Cloud | 延迟15分钟 |
| 外汇 | Fixer.io | ExchangeRate-API | 实时 |
| 加密货币 | CoinGecko Pro | CoinMarketCap | 实时 |
| A股 | Tushare | AkShare | 实时 |

### PRO版增强功能

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 数据源数量 | 1个 | 5+个自动回退 |
| 加密货币 | 有限支持 | 实时行情 |
| 外汇更新 | 每日 | 实时 |
| 价格告警 | 不支持 | 支持 |
| 批量导出 | 不支持 | CSV/Excel |
| 组合分析 | 不支持 | 支持 |
| 历史数据 | 30天 | 10年+ |
| 请求频率 | 低频 | 高频+限流管理 |

## 使用场景

### 场景一：投资组合批量估值

用户输入："帮我看看今天投资组合的表现"

```bash
# 批量获取组合中所有标的的最新报价
python scripts/portfolio_valuation.py \
  --portfolio portfolio.csv \
  --output valuation_report.xlsx \
  --include-charts

# 输出包含：
# - 各标的最新价格与日涨跌幅
# - 组合总市值与日P&L
# - 资产配置分布图
# - 各标的权重变化
```

### 场景二：价格告警设置

用户输入："AAPL跌破170的时候提醒我"

```bash
# 设置价格告警
python scripts/price_alert.py add \
  --ticker AAPL \
  --condition "below" \
  --threshold 170 \
  --channel "console"

# 查看所有告警
python scripts/price_alert.py list

# 启动告警监控
python scripts/price_alert.py monitor --interval 60
```

### 场景三：跨市场数据导出

用户输入："导出我关注的20只股票最近一年的历史数据"

```bash
# 批量导出历史数据
python scripts/batch_export.py \
  --tickers "AAPL,MSFT,GOOG,AMZN,TSLA,..." \
  --period "1y" \
  --interval "1d" \
  --output "./historical_data/" \
  --format csv

# 输出：每只标的一个CSV文件 + 汇总Excel
```

## 快速开始

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 配置多数据源凭证
cp config_pro_template.yaml config_pro.yaml
# 编辑config_pro.yaml填入各数据源API Key

# 验证数据源连通性
python scripts/verify_sources.py
```

### 多数据源查询

```python
from pro_quote import MultiSourceQuote

# 初始化多数据源客户端
client = MultiSourceQuote(
    sources=["alpha_vantage", "yahoo", "iex"],
    fallback=True,
    cache_ttl=60
)

# 自动选择最佳数据源并回退
quote = client.get_quote("AAPL")
print(f"AAPL: ${quote.price} ({quote.change_percent}%) | 来源: {quote.source}")

# 批量查询
quotes = client.get_quotes(["AAPL", "MSFT", "GOOG", "TSLA"])
```

### 加密货币行情

```bash
# 查询BTC价格
python scripts/crypto_quote.py BTC

# 查询多币种
python scripts/crypto_quote.py BTC ETH SOL BNB

# 获取历史K线
python scripts/crypto_series.py BTC --days 90 --interval 1h
```

## 示例

### PRO多数据源配置

```yaml
pro_config:
  sources:
    alpha_vantage:
      api_key: "${ALPHA_VANTAGE_API_KEY}"
      priority: 1
      rate_limit: 5              # 每分钟请求上限
      markets: ["us_stock", "etf"]

    yahoo_finance:
      priority: 2
      rate_limit: 60
      markets: ["us_stock", "etf", "index", "forex"]

    iex_cloud:
      api_key: "${IEX_API_KEY}"
      priority: 3
      rate_limit: 100
      markets: ["us_stock"]

    fixer:
      api_key: "${FIXER_API_KEY}"
      priority: 1
      rate_limit: 100
      markets: ["forex"]

    coingecko:
      api_key: "${COINGECKO_API_KEY}"
      priority: 1
      rate_limit: 50
      markets: ["crypto"]

  alerts:
    check_interval: 60           # 告警检查间隔（秒）
    channels:
      - console
      - webhook
    webhook_url: "${WEBHOOK_URL}"

  export:
    formats: ["csv", "excel", "json"]
    max_batch: 100               # 单次批量导出上限
    parallel: 5                  # 并行下载数

  cache:
    strategy: "ttl"              # ttl | lru
    ttl: 60                      # 缓存有效期（秒）
    max_size: 10000
    storage: "./cache/"
```

## 最佳实践

### PRO版高级实践

| 实践领域 | 建议做法 |
| --- | --- |
| 数据源选择 | 美股优先Alpha Vantage，外汇优先Fixer，加密优先CoinGecko |
| 限流管理 | 配置rate_limit参数，避免触发数据源限流 |
| 告警策略 | 设置合理的检查间隔，平衡及时性与API消耗 |
| 批量导出 | 使用并行下载，但不超过数据源并发限制 |
| 缓存优化 | 高频标的设短TTL，低频标的设长TTL |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
market_quote.py AAPL     → 多数据源自动回退
market_series.py VOO     → 支持10年+历史数据
market_watchlist.py      → 支持组合级分析与导出
```

## 常见问题

### Q1：多数据源回退是如何工作的？

当主数据源请求失败或被限流时，PRO版自动按优先级切换到备选数据源。整个过程对用户透明，返回结果中会标注实际使用的数据源。

### Q2：价格告警支持哪些通知方式？

PRO版支持控制台输出、Webhook推送和邮件通知三种方式。可在配置中同时启用多个通道。Webhook支持集成企业微信、钉钉、飞书等IM工具。

### Q3：批量导出支持多少只标的？

单次批量导出最多支持100只标的，并行下载数可配置（默认5个）。如需导出更多标的，建议分批执行，避免触发数据源限流。

### Q4：加密货币数据是否实时？

PRO版通过CoinGecko Pro接口获取加密货币实时行情，更新频率可达每分钟一次。历史K线支持分钟级、小时级和日线数据。

### Q5：PRO版支持A股行情吗？

支持。PRO版可接入Tushare或AkShare获取A股实时行情与历史数据。需在配置中填入Tushare API Token。

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
| yfinance | Python库 | 必需 | `pip install yfinance` |
| requests | Python库 | 必需 | `pip install requests` |
| pandas | Python库 | 必需 | `pip install pandas` |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |
| aiohttp | Python库 | 可选 | `pip install aiohttp`（异步请求） |

### API Key 配置

| 数据源 | 环境变量 | 用途 | 获取方式 |
|:-------|:---------|:-----|:---------|
| Alpha Vantage | `ALPHA_VANTAGE_API_KEY` | 美股实时行情 | 官网免费注册 |
| IEX Cloud | `IEX_API_KEY` | 美股行情备选 | 官网注册 |
| Fixer.io | `FIXER_API_KEY` | 实时外汇汇率 | 官网注册 |
| CoinGecko Pro | `COINGECKO_API_KEY` | 加密货币行情 | 官网注册 |
| Tushare | `TUSHARE_TOKEN` | A股行情 | 官网注册 |

- 未配置某数据源时，自动跳过该源并使用备选
- 所有API Key存储在本地配置文件，不会上传至任何服务器

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 多数据源聚合行情追踪，支持自动回退、告警与批量导出
- **PRO版特性**: 多数据源回退、加密货币实时行情、价格告警、批量导出、组合分析
- **兼容性**: 完全兼容免费版全部命令与工作流

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
