---
slug: tg-bot-builder-free
name: tg-bot-builder-free
version: "1.0.0"
displayName: TG机器人构建免费版
summary: 零代码快速搭建Telegram机器人，支持键盘按钮、内联菜单、Webhook与自动回复
license: MIT
edition: free
description: |-
  面向独立开发者与小团队的Telegram机器人构建助手，覆盖Bot创建、交互菜单、消息流转、群组管理等核心场景。

  核心能力：通过自然语言指令生成Bot配置代码，支持Reply键盘、Inline内联按钮、Webhook接入、自动回复规则与基础群组权限管理。

  适用场景：客服自动化、订单查询、内容订阅、社群运营、投票问卷等高频业务场景，特别适合个人项目与小型社群的快速验证。

  差异化：重新设计中文交互流程，新增错误恢复策略与速率限制处理，去除外部依赖引用，完全适配国内开发者使用习惯。

  触发关键词：telegram、bot、机器人、键盘、内联按钮、webhook、自动回复、群组管理
tags:
- 集成工具
- 通信自动化
- 机器人开发
tools:
- read
- exec
---

# TG机器人构建助手（免费版）

## 概述

本Skill帮助开发者通过自然语言描述快速生成Telegram机器人的配置代码与交互逻辑。无需手翻文档，只需描述你想要的机器人行为，即可获得可直接运行的代码片段与部署指引。

免费版覆盖Bot创建、键盘交互、Webhook接入、自动回复等核心能力，满足个人项目与小型社群的日常需求。

## 核心能力

| 能力模块 | 说明 | 免费版支持 |
|:---------|:-----|:-----------|
| Bot创建与配置 | 通过BotFather创建Bot、获取Token、设置命令 | 是 |
| Reply键盘 | 底部固定菜单按钮 | 是 |
| Inline内联按钮 | 消息内嵌的可点击按钮 | 是 |
| Webhook接入 | 替代轮询模式，实时接收更新 | 是 |
| 自动回复规则 | 关键词匹配自动回复 | 是 |
| 基础群组管理 | 入群欢迎、简单权限控制 | 是 |
| 支付集成（Stars） | Telegram Stars内购支付 | 否（专业版） |
| 批量消息推送 | 一次向多用户发送通知 | 否（专业版） |
| 高级会话状态机 | 多轮对话状态管理 | 否（专业版） |

## 使用场景

### 场景一：客服自动应答机器人

某独立开发者运营一个产品社群，每天收到大量重复问题。通过本Skill生成一个关键词匹配的自动回复Bot，将常见问题（价格、文档链接、退款政策）设置为自动响应，人工只处理复杂问题。

### 场景二：订单查询机器人

小型电商希望用户通过Telegram查询订单状态。使用Inline按钮构建查询菜单，用户点击"查询订单"后输入订单号，Bot返回物流信息。

### 场景三：内容订阅通知

内容创作者搭建订阅通知系统，新文章发布时通过Webhook推送到订阅者群组，支持富文本格式与图片附件。

## 快速开始

### 第一步：创建Bot（约60秒）

1. 在Telegram中搜索 `@BotFather`
2. 发送 `/newbot` 命令
3. 按提示输入Bot名称和用户名
4. 保存返回的API Token（格式如 `123456789:ABCdefGHIjklMNOpqrSTUvwxYZ`）

### 第二步：生成你的第一个键盘菜单

向Agent描述需求：

```
帮我创建一个客服Bot的Reply键盘，包含"产品咨询"、"价格查询"、"联系人工"三个按钮
```

Agent将生成如下配置：

```python
from telegram import ReplyKeyboardMarkup

keyboard = [
    ["产品咨询", "价格查询"],
    ["联系人工"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
```

### 第三步：部署Webhook

```bash
# 设置Webhook（替换TOKEN和你的域名）
curl -s "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://yourdomain.com/webhook"
```

## 配置示例

### Inline按钮菜单配置

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# 构建内联菜单
keyboard = [
    [InlineKeyboardButton("查看订单", callback_data="order_view"),
     InlineKeyboardButton("物流追踪", callback_data="logistics")],
    [InlineKeyboardButton("联系客服", callback_data="contact_support")]
]
markup = InlineKeyboardMarkup(keyboard)
```

### 自动回复规则配置

```python
auto_reply_rules = {
    "价格": "我们的套餐分为：基础版¥29/月、专业版¥99/月。详情请访问官网。",
    "文档": "开发文档地址：https://docs.example.com",
    "退款": "退款政策：购买7天内无条件退款，请联系人工客服处理。"
}

def match_reply(text):
    for keyword, reply in auto_reply_rules.items():
        if keyword in text:
            return reply
    return None
```

### 基础群组欢迎配置

```python
WELCOME_TEMPLATE = """
欢迎 {user_name} 加入 {group_name}！
请阅读群规：{rules_link}
如有疑问请@管理员
"""
```

## 最佳实践

### 速率限制处理

Telegram Bot API限制每秒最多30条消息，单个聊天每分钟最多20条。建议实现请求队列：

```python
import asyncio
from collections import defaultdict

class RateLimiter:
    def __init__(self):
        self.user_last_msg = defaultdict(float)
        self.global_queue = asyncio.Queue()

    async def send(self, user_id, message):
        # 单用户限流：每60秒最多20条
        elapsed = time.time() - self.user_last_msg[user_id]
        if elapsed < 3:  # 至少间隔3秒
            await asyncio.sleep(3 - elapsed)
        self.user_last_msg[user_id] = time.time()
        await self.global_queue.put(message)
```

### 错误恢复策略

| 错误类型 | 原因 | 恢复策略 |
|:---------|:-----|:---------|
| 401 Unauthorized | Token无效或过期 | 检查Token是否正确，必要时通过BotFather重新生成 |
| 429 Too Many Requests | 触发速率限制 | 读取`retry_after`字段，等待指定秒数后重试 |
| 403 Forbidden: bot was blocked by user | 用户已屏蔽Bot | 标记用户为非活跃，停止向其发送消息 |
| 400 Bad Request: chat not found | chat_id错误 | 验证chat_id来源，提示用户先与Bot互动 |
| 网络超时 | 网络波动或Telegram服务异常 | 指数退避重试，最多3次 |

### 安全注意事项

- Token存储在环境变量中，禁止硬编码到代码或仓库
- Webhook端点必须使用HTTPS
- 验证Webhook请求来源，防止伪造请求
- 用户输入需做转义处理，防止注入攻击

## 常见问题

### Q1：Bot无法发送消息，提示403怎么办？

A：用户可能已屏蔽你的Bot。403错误表示"bot was blocked by user"，此时应停止向该用户发送消息，并在数据库中标记为非活跃。不要反复重试，否则会触发速率限制。

### Q2：Webhook一直收不到消息怎么排查？

A：按以下顺序检查：(1) 确认Webhook URL使用HTTPS且证书有效；(2) 使用 `getWebhookInfo` 接口查看Telegram返回的错误信息；(3) 确认服务器防火墙放行了443端口；(4) 检查Webhook处理脚本是否有语法错误导致500响应。

### Q3：如何处理按钮点击事件？

A：Inline按钮的点击通过 `callback_query` 更新类型传递。需要监听 `CallbackQuery` 并调用 `answerCallbackQuery` 确认，否则用户端会一直显示加载状态。

### Q4：群组中Bot无法读取用户消息？

A：默认情况下Bot只能读取以 `/` 开头的命令和@提及。需要在BotFather中通过 `/setprivacy` 设置为 `Disabled`，Bot才能读取群内所有消息（需Bot为群管理员）。

### Q5：免费版有哪些功能限制？

A：免费版不限制使用次数，但不支持Telegram Stars支付集成、批量消息推送、高级会话状态机、自定义模板库等高级功能。如需这些能力请使用专业版。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（如使用python-telegram-bot库）
- **Node.js**: 16+（如使用telegraf.js库）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| python-telegram-bot | Python库 | 推荐 | `pip install python-telegram-bot` |
| telegraf | Node.js库 | 可选 | `npm install telegraf` |
| requests | Python库 | 可选 | `pip install requests` |
| HTTPS证书 | 证书 | Webhook必需 | Let's Encrypt免费申请 |

### API Key 配置
- **Telegram Bot Token**: 通过 `@BotFather` 创建Bot后获取，存储于环境变量 `TELEGRAM_BOT_TOKEN`
- **禁止**: 在代码或配置文件中明文硬编码Token
- **推荐**: 使用 `.env` 文件管理，并在 `.gitignore` 中排除

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成代码与配置

## 免费版限制

本免费体验版限制以下高级功能：
- 不支持 Telegram Stars 支付集成
- 不支持批量消息推送（单次上限受Telegram API限制）
- 不支持高级会话状态机（多轮对话管理）
- 不支持自定义模板库与主题切换
- 不提供优先技术支持

解锁全部功能请使用专业版：tg-bot-builder-pro
