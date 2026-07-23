---
slug: "finance-toolkit"
name: "finance-toolkit"
version: "1.0.0"
displayName: "行情追踪专业工具"
summary: "多数据源行情追踪，支持股票、ETF、指数、外汇、加密货币，含告警与批量导出。"
license: "Proprietary"
edition: "pro"
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
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# 行情追踪专业工具

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

### 多数据源策略
| 标的类型 | 主数据源 | 备选数据源 | 更新频率 |
| --- | --- | --- | --- |
| 美股/ETF | Alpha Vantage | Yahoo Finance | 实时 |
| 指数 | Yahoo Finance | IEX Cloud | 延迟15分钟 |
| 外汇 | Fixer.io | ExchangeRate-API | 实时 |
| 加密货币 | CoinGecko Pro | CoinMarketCap | 实时 |
| A股 | Tushare | AkShare | 实时 |

**输入**: 用户提供多数据源策略所需的指令和必要参数。
**处理**: 解析多数据源策略的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回多数据源策略的处理结果,包含执行状态码、结果数据和执行日志。### PRO版增强功能

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
### 标的类型

针对标的类型,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供标的类型相关的配置参数、输入数据和处理选项。

**输出**: 返回标的类型的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`标的类型`的配置文档进行参数调优
### 美股/ETF

针对美股/ETF,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供美股/ETF相关的配置参数、输入数据和处理选项。

**输出**: 返回美股/ETF的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`美股/ETF`的配置文档进行参数调优
#
## 适用场景

### 场景一：投资组合批量估值

用户输入："帮我看看今天投资组合的表现"

```bash
# 批量获取组合中所有标的的最新报价
python （请参考skill目录中的脚本文件） \
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
python （请参考skill目录中的脚本文件） add \
  --ticker AAPL \
  --condition "below" \
  --threshold 170 \
  --channel "console"

# 查看所有告警
python （请参考skill目录中的脚本文件） list

# 启动告警监控
python （请参考skill目录中的脚本文件） monitor --interval 60
```

### 场景三：跨市场数据导出

用户输入："导出我关注的20只股票最近一年的历史数据"

```bash
# 批量导出历史数据
python （请参考skill目录中的脚本文件） \
  --tickers "AAPL,MSFT,GOOG,AMZN,TSLA,..." \
  --period "1y" \
  --interval "1d" \
  --output "./historical_data/" \
  --format csv

# 输出：每只标的一个CSV文件 + 汇总Excel
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 配置多数据源凭证
cp config_pro_template.yaml config_pro.yaml
# 编辑config_pro.yaml填入各数据源API Key

# 验证数据源连通性
python （请参考skill目录中的脚本文件）
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

# 自动选择优秀数据源并回退
quote = client.get_quote("AAPL")
print(f"AAPL: ${quote.price} ({quote.change_percent}%) | 来源: {quote.source}")

# 批量查询
quotes = client.get_quotes(["AAPL", "MSFT", "GOOG", "TSLA"])
```

### 加密货币行情

```bash
# 查询BTC价格
python （请参考skill目录中的脚本文件） BTC

# 查询多币种
python （请参考skill目录中的脚本文件） BTC ETH SOL BNB

# 获取历史K线
python （请参考skill目录中的脚本文件） BTC --days 90 --interval 1h
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | finance-toolkit处理的内容输入 |,  |
| content | string | 否 | finance-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
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

## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

