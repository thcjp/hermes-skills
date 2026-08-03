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

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配Skil...
tags:
- Integrations
- Communication
- Automation
tools:
  - - read
- exec
pricing_tier: "L2-标准级"
pricing_model: "per_use"
suggested_price: 19.9
---

## 触发条件

需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于非本工具能力范围的需求。


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

* 🤖 Bot Setup (BotFather)
* ⌨️ Reply/Inline Keyboards
* 👥 Group Management
* 🔗 Webhook Integration
* 📩 Auto-reply / Filters
* 💰 Payment (Stars)

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

### Q1: 如何开始使用Telegram Bot Builder？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Telegram Bot Builder有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制

Telegram Bot Builder技能的边界条件与限制如下：

- **输入限制**：技能接受基于Markdown格式的指令，不支持非Markdown格式的输入。
- **性能边界**：由于依赖LLM API，处理大量并发请求时可能会出现性能瓶颈，建议在高峰时段合理分配请求。
- **兼容性约束**：目前仅支持Windows、macOS和Linux操作系统，不支持其他操作系统。
- **API Key限制**：虽然技能本身无需额外API Key，但某些外部API可能需要API Key才能正常工作。
- **功能限制**：某些高级功能可能需要通过exec命令行执行，这要求Agent具备相应的执行能力。
- **语言限制**：技能目前仅支持英语指令，不支持其他语言。
- **消息限制**：由于Telegram的限制，单个用户每30秒内只能发送30条消息，超过此限制可能导致消息发送失败。
- **权限限制**：技能在执行某些操作时可能需要用户授权，如访问用户聊天记录等。

---

