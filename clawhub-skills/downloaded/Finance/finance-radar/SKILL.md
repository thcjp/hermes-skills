---
slug: finance-radar
name: finance-radar
version: "1.1.0"
displayName: Finance Radar
summary: "Stock and cryptocurrency analysis powered by Yahoo Finance data. Use when
  a user wants to: (1) An"
license: MIT
description: |-
  Stock and cryptocurrency analysis powered by Yahoo Finance data。Use
  when a user wants to: (1) An。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Finance
tools:
  - - read
- exec
---

# Finance Radar

Stock & crypto intelligence via Yahoo Finance. Charges 0.001 USDT/call via SkillPay.

## Commands

| Command | Script | Description |
| --- | --- | --- |
| **analyze** | `scripts/analyze.py` | Stock/crypto analysis (price, fundamentals, technicals) |
| **score** | `scripts/score.py` | 8-dimension stock scoring |
| **batch** | `scripts/batch.py` | Batch analyze multiple tickers + CSV export |
| **portfolio** | `scripts/portfolio.py` | Portfolio tracking & P/L |
| **watchlist** | `scripts/watchlist.py` | Watchlist with price alerts |
| **dividend** | `scripts/dividend.py` | Dividend yield & history |
| **hot-scan** | `scripts/hot_scan.py` | Viral trend detection |
| **rumor** | `scripts/rumor.py` | Rumor & early signal detection |
| **billing** | `scripts/billing.py` | SkillPay charge/balance/payment |

## Workflow

```text
1. Billing:  python3 scripts/billing.py --charge --user-id <id>
2. Execute:  python3 scripts/<command>.py --ticker AAPL
```

## 示例

```bash
python3 scripts/analyze.py --ticker AAPL

python3 scripts/analyze.py --ticker BTC-USD

python3 scripts/batch.py --tickers AAPL,GOOG,MSFT
python3 scripts/batch.py --tickers AAPL,GOOG,MSFT --export  # Export CSV

python3 scripts/score.py --ticker TSLA
```

## Config

| Env Var | Required | Description |
| --- | --- | --- |
| `SKILLPAY_API_KEY` | Yes | SkillPay.me API key |

## References

See `references/scoring-model.md` for 8-dimension scoring methodology.

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

- Stock and cryptocurrency analysis powered by Yahoo Finance data
- Use
  when a user wants to: (1) An
- 触发关键词: radar, powered, analysis, finance, cryptocurrency, yahoo, stock

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Finance Radar？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Finance Radar有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
