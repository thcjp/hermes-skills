---
slug: rho-telegram-alerts
name: rho-telegram-alerts
version: "1.0.1"
displayName: Telegram Alerts
summary: Send formatted trading alerts, portfolio updates, and market signals via
  Telegram. Supports price...
license: MIT
description: |-
  Send formatted trading alerts, portfolio updates, and market signals
  via Telegram. Supports price...

  核心能力:

  - 金融工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 交易分析、投资决策、财务计算

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: trading, alerts, portfolio, telegram, rho, send, formatted
tags:
- Finance
- Automation
tools:
- read
- exec
---

# Telegram Alerts

Send rich trading alerts to Telegram for any crypto event or portfolio update.

## Alert Types

* **Trade alerts**: entry/exit with P&L, entry price, stop, target
* **Price alerts**: trigger when asset crosses threshold
* **Portfolio summaries**: NAV, daily P&L, positions
* **Stop-loss warnings**: drawdown approaching limit
* **Win/loss streaks**: celebration + tilt prevention
* **Scheduled reports**: daily 18:00, weekly Monday

## Usage

```text
Use telegram-alerts to send a trade entry notification for BTC LONG at $68,000

Use telegram-alerts to send my daily portfolio summary

Use telegram-alerts to alert me when SOL breaks $90
```

## Format Example

```text
🟢 TRADE OPENED
Asset: BTC/USDT | LONG
Entry: $68,247 | Stop: $67,200 | Target: $70,000
Risk: $0.38 (0.05% NAV) | R:R = 1:2.6
```

## Setup

Requires TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in your .env file.

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
