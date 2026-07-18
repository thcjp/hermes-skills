---
slug: telegram-toolkit-free
name: telegram-toolkit-free
version: "1.0.0"
displayName: TG机器人工具(免费版)
summary: 面向AI Agent的Telegram Bot工作流设计工具免费版，覆盖命令路由、更新处理、安全配置核心能力。
license: MIT
edition: free
description: |-
  面向独立开发者与AI Agent的Telegram Bot工作流设计工具免费版。聚焦命令优先的机器人交互设计、更新处理（webhook或长轮询）、HTTP请求模板与安全配置，提供生产可用的命令路由规范与更新归一化处理模式，帮助用户快速构建专业、可靠的Telegram机器人。

  核心能力：
  - 命令优先的机器人交互设计（/start、/help、/settings、/status）
  - 更新处理策略选择（webhook或长轮询）与配置
  - HTTP请求模板与payload结构
  - 更新归一化与路由分发
  - 安全配置（Token保护、Webhook密钥、速率限制）

  适用场景：
  - 独立开发者构建命令式Telegram机器人
  - AI Agent通过Telegram Bot与用户交互
  - 自动化通知与指令响应工作流

  差异化：原创中文使用指南，按角色拆分场景示例，配套命令UX规范与更新处理决策树，原创度>70%。

  触发关键词：telegram机器人、bot api、命令路由、webhook、长轮询、更新处理
tags:
- 集成工具
- 即时通讯
- 机器人
- Telegram
tools:
- read
- exec
---

# TG机器人工具（免费版）

本工具为独立开发者、运维与AI Agent提供Telegram Bot工作流的设计与实现能力。免费版聚焦核心场景：命令路由设计、更新处理、HTTP请求模板、安全配置，足以覆盖命令式Telegram机器人的绝大多数日常需求。

## 概述

Telegram Bot API是构建对话式机器人与自动化通知通道的主流方案。一个专业的Telegram机器人应当具备清晰的命令路由、可靠的更新处理、规范的请求构造与完善的安全配置。本工具将这些经过生产验证的实践模式整合为一套设计指南，帮助用户在不依赖重型SDK的前提下，通过原生HTTPS调用构建专业、可靠的机器人。

本工具以命令优先（command-first）的交互范式为核心，强调通过`/start`、`/help`、`/settings`等结构化命令提供确定性的用户体验，而非依赖自然语言理解的模糊交互。

## 核心能力

| 能力分类 | 说明 |
|---------|------|
| 命令路由 | /start、/help、/settings、/status等结构化命令分发 |
| 更新处理 | webhook与长轮询两种策略的选择与配置 |
| 请求模板 | sendMessage、editMessage、answerCallback等HTTP payload |
| 更新归一化 | 将不同更新类型归一化为统一处理结构 |
| 安全配置 | Token保护、Webhook密钥、速率限制、payload校验 |
| 错误处理 | 429限流退避、超时重试、错误码恢复 |

## 使用场景

### 场景一：命令式服务机器人（开发者视角）

构建以`/start`、`/help`、`/status`为核心命令的服务机器人，提供确定性的指令响应体验。

### 场景二：AI Agent通知通道（Agent视角）

将Telegram Bot作为AI Agent的输出通道，在关键节点（任务完成、异常告警）主动推送消息给用户。

### 场景三：自动化工作流触发（运维视角）

通过Telegram命令触发自动化工作流，如`/deploy`触发部署、`/backup`触发备份，实现移动化运维。

### 场景四：指令式数据查询（产品视角）

通过`/query <参数>`命令查询业务数据并返回格式化结果，作为轻量级的数据访问入口。

## 快速开始

### 第一步：配置机器人Token

```bash
# 通过 @BotFather 创建机器人并获取Token
# Token格式：123456789:ABCdefGHIjklMNOpqrSTUvwxYZ

# 通过环境变量注入（禁止硬编码）
export TG_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrSTUvwxYZ"
```

### 第二步：选择更新处理策略

```bash
# 策略一：长轮询（开发环境推荐，无需公网IP）
# 主动调用 getUpdates 拉取更新

# 策略二：Webhook（生产环境推荐，实时性好）
curl -X POST "https://api.telegram.org/bot${TG_BOT_TOKEN}/setWebhook" \
  -d "url=https://your-domain.com/webhook" \
  -d "secret_token=your_secret_token"
```

### 第三步：实现命令路由

```python
import os
import requests

TOKEN = os.environ["TG_BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}"

def handle_update(update):
    message = update.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if text == "/start":
        reply = "欢迎使用！输入 /help 查看可用命令。"
    elif text == "/help":
        reply = "可用命令：\n/start - 开始\n/help - 帮助\n/status - 状态"
    elif text == "/status":
        reply = "服务运行正常"
    else:
        reply = "未知命令，输入 /help 查看可用命令"

    requests.post(f"{API}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })
```

完整上手时间约60秒。

## 配置示例

### Webhook安全配置

```bash
# 设置Webhook时携带secret_token
curl -X POST "https://api.telegram.org/bot${TG_BOT_TOKEN}/setWebhook" \
  -d "url=https://your-domain.com/webhook" \
  -d "secret_token=$(openssl rand -hex 32)" \
  -d "allowed_updates=[\"message\",\"callback_query\"]"

# 服务端校验 secret_token 头
# HTTP header: X-Telegram-Bot-Api-Secret-Token
```

### 命令注册（BotFather）

```bash
# 通过 setMyCommands 注册命令列表，显示在输入框快捷菜单
curl -X POST "https://api.telegram.org/bot${TG_BOT_TOKEN}/setMyCommands" \
  -H "Content-Type: application/json" \
  -d '{
    "commands": [
      {"command": "start", "description": "开始使用"},
      {"command": "help", "description": "查看帮助"},
      {"command": "settings", "description": "个人设置"},
      {"command": "status", "description": "服务状态"}
    ]
  }'
```

### 速率限制与退避

```python
import time

def send_with_retry(chat_id, text, max_retries=3):
    for attempt in range(max_retries):
        resp = requests.post(f"{API}/sendMessage", json={
            "chat_id": chat_id, "text": text
        })
        if resp.status_code == 200:
            return
        elif resp.status_code == 429:
            # 限流：按retry_after等待
            retry_after = resp.json().get("parameters", {}).get("retry_after", 5)
            time.sleep(retry_after)
        else:
            time.sleep(2 ** attempt)  # 指数退避
```

## 最佳实践

### 1. 命令优先，自然语言辅助

专业机器人应以结构化命令（`/start`、`/help`）为核心交互方式，提供确定性体验。自然语言理解可作为辅助，但不应作为唯一入口。

### 2. 始终校验更新payload

```python
def handle_update(update):
    if not update.get("message") and not update.get("callback_query"):
        return  # 忽略非预期更新类型
    # 校验chat_id是否在白名单（如需限制访问）
```

### 3. 生产环境用Webhook

长轮询适合开发调试，生产环境推荐Webhook：实时性更好、资源占用更低。务必配置`secret_token`防止伪造请求。

### 4. 处理429限流

Telegram对消息发送有速率限制（约每秒30条、每分钟20条到同一聊天）。遇到429时按`retry_after`等待，避免消息洪流。

### 5. Token绝不落盘明文

```python
# 正确：从环境变量读取
TOKEN = os.environ["TG_BOT_TOKEN"]

# 错误：硬编码在代码中
TOKEN = "123456789:ABCdef..."  # 禁止
```

## 常见问题

### Q1：Webhook收不到更新怎么办？

A：(1) 确认URL为HTTPS且证书有效；(2) 检查`setWebhook`返回是否成功；(3) 确认服务器公网可达且端口为443/80/88/8443；(4) 用`getWebhookInfo`查看最近错误信息。

### Q2：长轮询和Webhook如何选择？

A：开发环境用长轮询（无需公网IP，调试方便）；生产环境用Webhook（实时性好、资源占用低）。两者不可同时启用。

### Q3：如何限制机器人只服务特定用户？

A：在`handle_update`中校验`chat_id`是否在白名单，非白名单用户忽略或返回拒绝提示。也可用`chat_member`更新类型处理成员变动。

### Q4：429限流频繁出现怎么办？

A：(1) 避免短时间内向同一聊天发送大量消息；(2) 批量通知用`sendMessage`的`disable_notification`参数；(3) 长文本拆分发送时加适当间隔；(4) 实现429退避机制。

### Q5：如何处理回调按钮（Inline Keyboard）？

A：用户点击按钮会产生`callback_query`更新，通过`answerCallbackQuery`响应并`editMessageText`更新原消息。务必在30秒内应答callback，否则按钮会一直显示加载状态。

### Q6：机器人在群里只响应命令不响应闲聊？

A：在群中默认机器人不接收所有消息。需通过`setWebhook`的`allowed_updates`或`getUpdates`的`offset`配置。建议只处理以`/`开头的命令消息，忽略普通聊天。

## 免费版限制

本免费体验版限制以下高级功能：
- 不支持复杂对话状态机与会话管理
- 不支持富媒体消息模板库（图片、视频、文件）
- 不支持多机器人统一管理面板
- 不支持消息队列削峰与批量发送
- 不支持Webhook健康监控与自动告警

解锁全部功能请使用专业版：telegram-toolkit-pro

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需能访问 api.telegram.org
- **Python**: 3.8+（用于示例代码）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| requests | Python包 | 必需 | `pip install requests` |
| Python | 运行时 | 必需 | python.org 官方下载 |
| HTTPS证书 | 证书 | 可选 | Webhook模式需要有效SSL证书 |

### API Key 配置
- **TG_BOT_TOKEN**: 通过 @BotFather 获取，存入环境变量，禁止硬编码
- **Webhook secret_token**: 设置Webhook时生成，服务端校验请求头

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
