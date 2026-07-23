---
slug: "telegram-bot-builder"
name: "telegram-bot-builder"
version: "1.0.0"
displayName: "Telegram Bot Builder"
summary: "Telegram Bot 快速build工具 - Keyboard、Inline Buttons、Webhook、Auto-reply、Group管理"
license: "Proprietary"
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
tags:
  - Integrations
  - Communication
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Telegram Bot Builder

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Telegram Bot BuilderGroup管理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 核心能力

* Bot Setup (BotFather) - 通过BotFather创建和配置Bot
* Reply/Inline Keyboards - 回复键盘与内联按钮
* Group Management - 群组管理与权限控制
* Webhook Integration - Webhook回调集成
* Auto-reply / Filters - 自动回复与消息过滤
* Payment (Stars) - Telegram Stars支付集成

## BotFather 创建流程

### 步骤1：创建Bot

1. 在Telegram中搜索 `@BotFather` 并启动对话
2. 发送 `/newbot` 命令
3. 输入Bot显示名称（如 "My Customer Support Bot"）
4. 输入Bot用户名（必须以 `bot` 结尾，如 `my_support_bot`）
5. BotFather返回Bot Token，格式为 `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

### 步骤2：配置Bot

```
/setdescription  - 设置Bot描述（用户在Bot页面看到）
/setabouttext    - 设置关于文本
/setuserpic      - 设置Bot头像
/setcommands     - 设置命令菜单
```

常用命令菜单配置示例：
```
start - 开始使用
help - 获取帮助
status - 查询订单状态
settings - 个人设置
```

## 键盘按钮示例

### Reply Keyboard（回复键盘）

```json
{
  "chat_id": 123456789,
  "text": "请选择您需要的服务：",
  "reply_markup": {
    "keyboard": [
      [{"text": "查询订单"}, {"text": "联系客服"}],
      [{"text": "个人设置"}, {"text": "使用帮助"}]
    ],
    "resize_keyboard": true,
    "one_time_keyboard": false
  }
}
```

### Inline Keyboard（内联按钮）

```json
{
  "chat_id": 123456789,
  "text": "请选择操作：",
  "reply_markup": {
    "inline_keyboard": [
      [
        {"text": "确认下单", "callback_data": "order_confirm_001"},
        {"text": "取消", "callback_data": "order_cancel_001"}
      ],
      [
        {"text": "查看详情", "url": "https://example.com/order/001"}
      ]
    ]
  }
}
```

### 回调数据处理

当用户点击内联按钮时，Bot收到 `callback_query` 更新，需回复：

```json
{
  "callback_query_id": "query_123",
  "text": "订单已确认！",
  "show_alert": false
}
```

## Webhook 配置

### 设置Webhook

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://yourdomain.com/webhook/telegram",
    "max_connections": 40,
    "allowed_updates": ["message", "callback_query", "edited_message"]
  }'
```

### 验证Webhook（推荐）

设置Webhook时添加 secret_token 参数，Bot发送的每个请求会在HTTP头中携带 `X-Telegram-Bot-Api-Secret-Token`，服务端验证该值是否匹配：

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook" \
  -d '{"url": "https://yourdomain.com/webhook/telegram", "secret_token": "MY_SECRET_123"}'
```

### Webhook vs Long Polling 对比

| 特性 | Webhook | Long Polling |
|:-----|:------|:------|
| 实时性 | 实时推送 | 轮询延迟 |
| 服务器要求 | 需要公网HTTPS | 无需公网 |
| 适用场景 | 生产环境 | 开发调试 |
| 资源消耗 | 低（事件驱动） | 较高（持续轮询） |

## 自动回复与消息过滤

### 关键词自动回复

设置关键词匹配规则，当用户消息包含特定关键词时自动回复：

```json
{
  "rules": [
    {
      "trigger": "你好|hello|hi",
      "reply": "您好！欢迎使用本Bot，输入 /help 查看可用命令。",
      "match_type": "regex"
    },
    {
      "trigger": "价格|多少钱|price",
      "reply": "我们的套餐：\n基础版 29元/月\n专业版 99元/月\n企业版 联系客服",
      "match_type": "keyword"
    }
  ]
}
```

## 群组管理功能

| 功能 | 命令/方法 | 说明 |
|:-----|:------|:------|
| 踢出成员 | `kickChatMember` | 踢出指定用户，可设置禁言时长 |
| 禁言成员 | `restrictChatMember` | 限制发送消息/媒体/贴纸 |
| 提升管理员 | `promoteChatMember` | 授予管理员权限 |
| 设置群标题 | `setChatTitle` | 修改群组名称 |
| 设置群描述 | `setChatDescription` | 修改群组描述 |
| 封禁频道 | `banChatSenderChat` | 禁止频道在群内发消息 |

## Telegram Stars 支付集成

### 发送支付发票

```json
{
  "chat_id": 123456789,
  "title": "高级会员 - 月度订阅",
  "description": "解锁全部高级功能，包括无限消息、优先客服",
  "payload": "subscription_premium_monthly",
  "currency": "XTR",
  "prices": [{"label": "月度订阅", "amount": 150}]
}
```

### 处理支付回调

用户完成支付后，Bot收到 `pre_checkout_query`，需在10秒内回复确认：

```json
{
  "ok": true,
  "pre_checkout_query_id": "query_xxx"
}
```
## 适用场景
- 不适用: 需要人工判断的复杂决策场景

* Customer Support Bot
* Order/Booking System
* Crypto Trading Bot
* Content Subscription
* Quiz/Poll Bot

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| bot_token | string | 是 | BotFather提供的Bot Token |
| action | string | 是 | 操作类型: create/send_message/set_webhook/set_keyboard/manage_group/send_invoice |
| chat_id | integer | 否 | 目标聊天ID，发消息时必填 |
| text | string | 否 | 消息文本内容，支持Markdown和HTML格式 |
| reply_markup | object | 否 | 键盘按钮配置JSON |
| webhook_url | string | 否 | Webhook回调URL，需HTTPS |
| parse_mode | string | 否 | 解析模式: MarkdownV2/HTML, 默认纯文本 |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "builder 相关配置参数",
    result: "builder 相关配置参数"
  },
  "error": null
}
```

## 异常处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key（Bot Token），无Token环境无法使用
- 单条消息文本上限4096字符，超长需分段发送
- Webhook要求HTTPS证书，本地开发需使用ngrok等隧道工具
- Bot无法主动给未启动对话的用户发消息（需用户先 `/start`）
- 群组中Bot只能看到以 `/` 开头的命令或被@提及的消息，除非关闭隐私模式

## 常见问题

**Q: 如何处理异常输入?**
A: 系统会自动检测并返回错误提示, 同时提供修复建议.

**Q: 支持哪些输入格式?**
A: 支持标准文本、JSON、CSV等常见格式. 消息内容支持MarkdownV2和HTML两种格式化模式，通过 `parse_mode` 参数指定。MarkdownV2需转义以下字符：`_ * [ ] ( ) ~ \` > # + - = | { } . !`。

**Q: Bot在群组中收不到普通消息怎么办？**
A: 默认情况下Bot开启了隐私模式（Privacy Mode），只能收到以 `/` 开头的命令或被@提及的消息。解决方法：在BotFather中发送 `/setprivacy`，选择对应Bot，设置为 `Disable`。注意修改后需要将Bot移出群组再重新加入才能生效。

**Q: Webhook设置失败返回422错误？**
A: 常见原因：（1）URL不是HTTPS（Telegram要求必须HTTPS）；（2）SSL证书无效或自签名（需使用受信任CA签发的证书或上传自签名证书公钥）；（3）URL端口不在支持范围内（仅支持443、80、88、8443端口）。排查时可先调用 `getWebhookInfo` 查看详细的错误描述。

**Q: 如何实现按钮点击后的状态更新（如编辑消息文本）？**
A: 在收到 `callback_query` 后，调用 `editMessageText` 方法，传入原始 `chat_id` 和 `message_id`，以及新的文本和 `reply_markup`。这是实现"确认/取消"按钮交互、多级菜单导航的标准模式。