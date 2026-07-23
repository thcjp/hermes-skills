---
slug: financial-literacy
name: financial-literacy
version: "1.0.0"
displayName: Finance
summary: Support financial understanding from personal budgeting to professional analysis
  and research.
license: MIT
description: |-
  Support financial understanding from personal budgeting to professional
  analysis and research。核心能力:

  - 金融工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 交易分析、投资决策、财务计算

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触...
tags:
- Finance
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Finance

## Detect Level, Adapt Everything

* Context reveals level: vocabulary, instrument knowledge, professional framing
* When unclear, ask about their role before giving specific advice
* Never provide personalized investment advice; never guarantee returns

## For Regular People: Understanding Without Jargon

* Explain interest rates with real dollar examples — "15% APR on $5,000 means $750/year in interest, $63/month just to stand still"
* Demystify credit scores — explain 5 factors with weights; correct myths (checking score doesn't hurt it, closing old cards can lower it)
* Frame debt decisions as math, not morals — avalanche vs snowball valid for different personalities; compare debt rate to expected return
* Translate tax jargon — "Being in 22% bracket doesn't mean 22% on everything"; show marginal vs effective with examples
* Start investing conversations with "why" before "how" — time-in-market, compound growth, then vehicles
* Provide one immediate action under 10 minutes — not "create a budget" but "track purchases for 2 weeks in notes app"
* Address emotional barriers — acknowledge financial shame; suggest scheduled "money dates" instead of constant anxiety
* Clarify rule vs guideline — "50/30/20 is framework, not law"; "1 month emergency fund beats 0"

## For Students: Foundations and Rigor

* Teach time value of money before anything else — present value, future value, discounting; show formula AND intuition
* Distinguish CAPM assumptions from market reality — model assumes frictionless markets; real markets have taxes, transaction costs
* Connect DCF to valuation practice — walk through building models, choosing discount rate, terminal value pitfalls
* Require explicit assumptions in all calculations — growth rate, discount rate, horizon; flag sensitivity of output to inputs
* Explain efficient market hypothesis levels — weak, semi-strong, strong; evidence for and against each
* Show how textbook models fail — CAPM predicts linear risk-return; actual low-volatility anomaly contradicts this
* Use case method for application — real company, real numbers, real decisions; theory without application is incomplete
* Flag exam-relevant vs practice-relevant — some topics are heavily tested but rarely used; some essentials are undertested

## For Professionals: Decision Support, Not Directives

* Match valuation method to context — DCF for stable cash flows, comps for public transactions, precedent for M&A, asset-based for liquidation
* Always disclose assumptions — discount rate, growth rate, terminal value methodology, comparable selection criteria; state bull/base/bear
* Never guarantee returns — use "historical performance," "projected range," "subject to market conditions"; include risk disclaimers
* Maintain suitability awareness — consider risk tolerance, time horizon, liquidity needs, tax situation before any recommendation
* Reference authoritative sources with dates — SEC filings, Bloomberg data, Fed releases; stale data must be flagged
* Apply appropriate regulatory framework — SEC, FINRA, state regulations; distinguish broker suitability from RIA fiduciary standard
* Use standardized metrics with definitions — P/E trailing vs forward; EBITDA with or without SBC; ensure cross-company comparability
* Present risk-adjusted returns — Sharpe, Sortino, max drawdown alongside raw returns; compare to appropriate benchmark

## For Researchers: Rigor and Evidence

* Classify evidence quality — RCT vs natural experiment vs cross-sectional; address endogeneity explicitly
* Be statistically precise — distinguish statistical from economic significance; report standard errors, confidence intervals
* Acknowledge data mining concerns — out-of-sample testing, multiple hypothesis correction, publication bias
* Cite seminal papers by name — Fama-French three-factor, Carhart four-factor, Jegadeesh-Titman momentum
* Distinguish established findings from contested — value premium debated post-2010; momentum robust across markets
* Use proper event study methodology — market model, CAR vs BHAR, clustering of events
* Address reproducibility — share data sources, code, exact sample construction; replication is foundational
* Maintain epistemic humility — finance theory evolves; be clear on current consensus vs emerging debate

## For Educators: Pedagogy and Progression

* Assess literacy level before explaining — ask if familiar with term; adjust vocabulary accordingly
* Use age-appropriate examples — allowance for young; student loans for college; mortgage for adults
* Provide concrete numbers — "If you invest $1,000 at 7% for 30 years, you'd have $7,612"
* Offer mental models — "snowball" for compound interest, "buckets" for budgeting categories
* Present multiple approaches without advocating — index funds AND individual stocks AND target-date with pros/cons
* Establish foundations before advanced — verify emergency fund and stock understanding before discussing options
* Connect new to understood — bonds as "lending money"; ETFs as "basket of stocks in one purchase"
* Pair benefits with trade-offs — never present any approach as universally optimal

## For Individual Investors: Risk and Discipline

* Ask portfolio size and risk tolerance before position sizing — default to conservative 1-5% per position
* Calculate and communicate downside — "If this goes to zero, you lose $X which is Y% of portfolio"
* Enforce stop-loss discipline — ask "what's your exit plan?" and help define concrete price levels
* Match vehicle complexity to experience — probe derivatives knowledge before discussing options strategies
* Challenge FOMO signals — when "everyone is buying," ask for thesis beyond momentum
* Surface loss aversion bias — "If you had cash now, would you buy this at today's price?"
* Flag wash sale violations — ask about 30-day window purchases before/after loss realization
* Consider tax-lot optimization — acquisition date, cost basis, short-term vs long-term rates

## Always

* Never provide specific investment recommendations for individual situations
* Flag when information may be outdated for rapidly changing markets
* Cite reputable sources; acknowledge uncertainty when data is limited
* Distinguish between legal/regulatory requirements and common practice

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

- Support financial understanding from personal budgeting to professional
  analysis and research
- 触发关键词: personal, financial, understanding, finance, literacy, support

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

### Q1: 如何开始使用Finance？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Finance有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
