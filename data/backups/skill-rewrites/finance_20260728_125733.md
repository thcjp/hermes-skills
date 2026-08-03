---
slug: finance
name: finance
version: "1.1.2"
displayName: finance
summary: "跟踪股票/ETF/指数/加密/外汇,带缓存与提供商回退(社区下载版)"
  caching + provider fallb...
license: MIT
description: |-
  Track stocks, ETFs, indices, crypto (where available), and FX pairs
  with caching + provider fallb。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Finance
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# finance

This skill helps you fetch **latest quotes** and **historical series** for:

* Stocks / ETFs / Indices (e.g., AAPL, MSFT, ^GSPC, VOO)
* FX pairs (e.g., USD/ZAR, EURUSD, GBP-JPY)
* Crypto tickers supported by the chosen provider (best-effort)

It is optimized for:

* fast “what’s the price now?” queries
* lightweight tracking with a local watchlist
* caching to avoid rate-limits

## When to use

Use this skill when the user asks:

* “What’s the latest price of ___?”
* “Track ___ and ___ and show me daily changes.”
* “Give me a 30-day series for ___.”
* “Convert USD to ZAR (or track USD/ZAR).”
* “Maintain a watchlist and summarize performance.”

## Provider strategy (important)

* **Stocks/ETFs/indices** default: Yahoo Finance via `yfinance` (no key, broad coverage), but it is unofficial and can rate-limit.
* **FX** default: ExchangeRate-API Open Access endpoint (no key, daily update).
* If the user needs high-frequency or many symbols, recommend adding a paid provider later.

See `providers.md` for details and symbol formats.

---

These scripts are intended to be run from a terminal. The agent should:

1. ensure dependencies installed
2. run the scripts
3. summarize results cleanly

Install:

* `python -m venv .venv && source .venv/bin/activate` (or Windows equivalent)
* `pip install -r requirements.txt`

## Commands

### 1) Latest quote (stock/ETF/index)

Examples:

* `python scripts/market_quote.py AAPL`
* `python scripts/market_quote.py ^GSPC`
* `python scripts/market_quote.py VOO`

### 2) Latest FX rate

Examples:

* `python scripts/market_quote.py USD/ZAR`
* `python scripts/market_quote.py EURUSD`
* `python scripts/market_quote.py GBP-JPY`

### 3) Historical series (CSV to stdout)

Examples:

* `python scripts/market_series.py AAPL --days 30`
* `python scripts/market_series.py USD/ZAR --days 30`

### 4) Watchlist summary (local file)

* Add tickers: `python scripts/market_watchlist.py add AAPL MSFT USD/ZAR`
* Remove: `python scripts/market_watchlist.py remove MSFT`
* Show summary: `python scripts/market_watchlist.py summary`

---

* For quotes: price, change %, timestamp/source, and any caveats (like “FX updates daily”).
* For series: confirm date range, number of points, and show a small preview (first/last few rows).
* If rate-limited: explain what happened and retry with backoff OR advise to reduce frequency.

---

* Never claim “real-time” unless the provider is truly real-time. FX open access updates daily.
* Always cache responses and throttle repeated calls.
* If Yahoo blocks requests, propose a paid provider or increase cache TTL.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Track stocks, ETFs, indices, crypto (where available), and FX pairs
  with caching + provider fallb
- 触发关键词: track, stocks, indices, finance, crypto, etfs

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用finance？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: finance有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
