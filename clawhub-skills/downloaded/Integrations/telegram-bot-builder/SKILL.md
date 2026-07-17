---
slug: telegram-bot-builder
name: telegram-bot-builder
version: "1.0.0"
displayName: Telegram Bot Builder
summary: Telegram Bot 快速build工具 - Keyboard、Inline Buttons、Webhook、Auto-reply、Group管理
license: MIT
description: |-
  Telegram Bot 快速build工具 - Keyboard、Inline Buttons、Webhook、Auto-reply、Group管理

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: buttons, inline, builder, 快速, build, keyboard, telegram, 工具
tags:
- Integrations
- Communication
- Automation
tools:
- read
- exec
---

# Telegram Bot Builder

快速整Telegram Bot既技能。

## 功能

* 🤖 Bot Setup (BotFather)
* ⌨️ Reply/Inline Keyboards
* 👥 Group Management
* 🔗 Webhook Integration
* 📩 Auto-reply / Filters
* 💰 Payment (Stars)

## 常用Code

```python
{
    "inline_keyboard": [
        [{"text": "✅ Yes", "callback_data": "yes"}],
        [{"text": "❌ No", "callback_data": "no"}]
    ]
}
```

## Use Cases

* Customer Support Bot
* Order/Booking System
* Crypto Trading Bot
* Content Subscription
* Quiz/Poll Bot

## Error Handling

* Handle "Bot was blocked"
* Rate limiting (30 msg/sec)
* Chat permission checks

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
