---
slug: finance-toolkit-free
name: finance-toolkit-free
version: "1.0.0"
displayName: 行情追踪基础工具
summary: 股票、ETF、指数、外汇行情查询工具，支持本地自选股与历史数据获取。
license: MIT
edition: free
description: |-
  面向个人投资者的轻量级行情追踪工具，支持股票、ETF、指数、外汇的实时
  报价与历史序列获取。内置缓存机制避免频率限制，适合日常行情查询与
  个人自选股管理。

  核心能力:
  - 股票/ETF/指数最新报价查询
  - 外汇汇率查询
  - 30天历史数据序列获取
  - 本地自选股管理（添加/删除/汇总）

  适用场景:
  - 个人日常行情查询
  - 自选股组合追踪
  - 外汇汇率换算
  - 轻量级投资记录

  差异化:
  - 免费版使用Yahoo Finance免费数据源
  - 适合个人用户低频查询场景
  - 本地缓存降低API调用
  - 不支持加密货币高频数据

  触发关键词: 行情, 股价, 报价, ETF, 指数, 外汇, 汇率, 自选股, 历史数据, stock, quote, forex
tags:
- Finance
- 行情追踪
- 自选股
tools:
- read
- exec
---

# 行情追踪基础工具（免费版）

## 概述

本工具为个人投资者提供轻量级的金融市场行情查询能力。支持股票、ETF、指数和外汇的最新报价与历史数据获取，内置本地自选股管理功能。通过缓存机制优化请求频率，适合日常投资追踪使用。

## 核心能力

### 行情查询

| 功能 | 支持标的 | 数据频率 |
| --- | --- | --- |
| 最新报价 | 股票/ETF/指数 | 延迟约15分钟 |
| 外汇汇率 | 主要货币对 | 每日更新 |
| 历史序列 | 全部标的 | 日线数据 |
| 自选股 | 自定义标的列表 | 手动触发 |

### 数据源策略

| 标的类型 | 默认数据源 | 是否需Key | 说明 |
| --- | --- | --- | --- |
| 股票/ETF/指数 | Yahoo Finance | 否 | 覆盖广，非官方接口 |
| 外汇 | ExchangeRate-API | 否 | 每日更新一次 |

## 使用场景

### 场景一：查询最新股价

用户输入："AAPL现在多少钱？"

```bash
# 获取苹果公司最新报价
python scripts/market_quote.py AAPL

# 输出示例：
# AAPL: $178.45 (+1.23%)
# 时间: 2026-07-18 10:30:00
# 数据源: Yahoo Finance
```

### 场景二：获取历史数据

用户输入："给我看看VOO最近30天的走势"

```bash
# 获取30天历史数据
python scripts/market_series.py VOO --days 30

# 输出CSV格式历史数据
# date,open,high,low,close,volume
# 2026-06-19,420.1,422.5,419.8,421.3,1234567
# ...
```

### 场景三：自选股管理

用户输入："帮我追踪AAPL、MSFT和USD/ZAR"

```bash
# 添加自选股
python scripts/market_watchlist.py add AAPL MSFT USD/ZAR

# 查看自选股汇总
python scripts/market_watchlist.py summary

# 移除某只股票
python scripts/market_watchlist.py remove MSFT
```

## 快速开始

### 环境准备

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 常用命令

```bash
# 查询股票报价
python scripts/market_quote.py AAPL

# 查询指数
python scripts/market_quote.py ^GSPC    # 标普500

# 查询外汇
python scripts/market_quote.py USD/ZAR
python scripts/market_quote.py EURUSD
python scripts/market_quote.py GBP-JPY

# 历史数据
python scripts/market_series.py AAPL --days 30
python scripts/market_series.py USD/ZAR --days 30

# 自选股管理
python scripts/market_watchlist.py add AAPL MSFT USD/ZAR
python scripts/market_watchlist.py summary
```

## 配置示例

### 自选股配置

```yaml
watchlist:
  stocks:
    - ticker: AAPL
      name: 苹果公司
      note: 长期持有
    - ticker: MSFT
      name: 微软
      note: 云业务关注
  etfs:
    - ticker: VOO
      name: 标普500ETF
  forex:
    - pair: USD/ZAR
      note: 南非兰特
  indices:
    - ticker: ^GSPC
      name: 标普500指数

cache:
  ttl: 300              # 缓存有效期（秒）
  max_size: 100         # 最大缓存条目
```

## 最佳实践

1. **利用缓存**：相同标的的重复查询会命中缓存，避免触发频率限制
2. **外汇注意频率**：免费外汇数据每日仅更新一次，不适合实时交易
3. **历史数据预取**：如需多次分析同一标的，先下载历史数据到本地
4. **自选股定期维护**：定期清理不再关注的标的，保持汇总报告简洁

| 实践要点 | 说明 |
| --- | --- |
| 查询频率 | 建议间隔≥30秒，避免被数据源限流 |
| 数据验证 | Yahoo Finance为非官方接口，重要决策前验证数据 |
| 外汇限制 | 免费外汇数据每日更新，不适合高频场景 |
| 缓存管理 | 定期清理缓存目录，避免占用过多磁盘 |

## 常见问题

### Q1：查询返回频率限制错误怎么办？

Yahoo Finance为非官方接口，高频请求会被限流。建议：增加查询间隔至60秒以上、启用缓存机制、或升级至PRO版使用多数据源回退策略。

### Q2：外汇数据为什么不是实时的？

免费版使用ExchangeRate-API开放接口，每日更新一次。如需实时外汇数据，建议升级至PRO版接入付费数据源。

### Q3：支持加密货币查询吗？

免费版对加密货币仅提供有限支持（取决于Yahoo Finance覆盖）。如需专业的加密货币行情，建议使用专用的加密货币工具。

### Q4：自选股数据保存在哪里？

自选股列表保存在本地文件中，不会上传至任何服务器。文件位置由配置中的watchlist_path指定。

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
| requests | Python库 | 必需 | `pip install requests` |
| pandas | Python库 | 可选 | `pip install pandas`（数据处理） |

### API Key 配置

- 免费版无需任何API Key
- 股票/ETF/指数数据通过yfinance免费获取
- 外汇数据通过ExchangeRate-API开放接口免费获取

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 通过Python脚本调用免费数据源API获取行情数据
- **免费版限制**: 单数据源、无自动回退、外汇每日更新、不支持加密货币高频数据
