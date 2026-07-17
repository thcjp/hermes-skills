---
slug: finance
name: finance
version: "1.1.2"
displayName: finance
summary: Track stocks, ETFs, indices, crypto (where available), and FX pairs with
  caching + provider fallb...
license: MIT
description: |-
  Track stocks, ETFs, indices, crypto (where available), and FX pairs
  with caching + provider fallb...

  核心能力:

  - 金融工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 交易分析、投资决策、财务计算

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: track, stocks, indices, finance, crypto, etfs
tags:
- Finance
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
