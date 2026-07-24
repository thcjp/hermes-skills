---
slug: "tg-bot-builder"
name: "tg-bot-builder"
version: 1.0.1
displayName: "TG机器人构建专业版"
summary: "全功能Telegram机器人构建平台，支持支付集成、批量推送、状态机与高级群管。面向企业团队与专业开发者的Telegram机器人全功能构建平台，覆盖Bot全生命周期管理与高级业务集成。核心能"
license: "MIT"
edition: "pro"
description: |-
  面向企业团队与专业开发者的Telegram机器人全功能构建平台，覆盖Bot全生命周期管理与高级业务集成。核心能力：在免费版基础上新增Telegram Stars支付集成、批量消息推送引擎、多轮对话状态机、高级群组权限矩阵、自定义模板库、A/B测试支持与性能监控仪表盘。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - 集成工具
  - 通信自动化
  - 企业级机器人
  - 支付集成
  - UI设计
  - 前端
  - 设计
  - self
  - bot
  - await
  - user_id
  - reply
tools:
  - read
  - exec
  - write
homepage: ""
category: "Creative"
---
# TG机器人构建专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 说明 | 专业版增强 |
|:-----|:-----|:-----|
| Bot创建与配置 | BotFather全流程配置 | 支持多Bot统一管理 |
| Reply/Inline键盘 | 交互菜单 | 支持动态菜单生成与A/B测试 |
| Webhook接入 | 实时更新接收 | 支持负载均衡与故障转移 |
| 自动回复规则 | 关键词匹配 | 支持正则匹配与上下文感知 |
| Telegram Stars支付 | 内购支付集成 | 全流程支付闭环 |
| 批量消息推送 | 大规模消息分发 | 队列引擎+速率控制+回执追踪 |
| 会话状态机 | 多轮对话管理 | 可视化状态流转图 |
| 高级群组管理 | 权限矩阵 | 分级权限+自动审计日志 |
| 自定义模板库 | 可复用模板 | 团队共享+版本管理 |
| 性能监控 | 运行指标仪表盘 | 实时告警+SLA追踪 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### Bot创建与配置

针对Bot创建与,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Bot创建与配置相关的配置参数、输入数据和处理选项.
**输出**: 返回Bot创建与配置的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Bot创建与配置`的配置文档进行参数调优
### Reply/Inline键盘

针对Reply/Inline键盘,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Reply/Inline键盘相关的配置参数、输入数据和处理选项.
**输出**: 返回Reply/Inline键盘的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Reply/Inline键盘`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：电商交易闭环（开发者视角）

某跨境电商团队需要完整的Telegram交易流程：用户浏览商品 -> 加入购物车 -> Stars支付 -> 订单确认 -> 物流追踪。专业版提供端到端的支付集成方案：

```python
# Stars支付流程
async def create_invoice(self, product_id, user_id):
    product = await self.get_product(product_id)
    invoice = {
        "title": product.name,
        "description": product.description,
        "payload": f"order_{product_id}_{user_id}",
        "provider_token": "",  # Stars支付留空
        "currency": "XTR",     # Telegram Stars货币
        "prices": [{"label": "商品价格", "amount": product.stars_price}]
    }
    return await self.bot.send_invoice(user_id, **invoice)
# ...
# 支付成功回调
async def on_pre_checkout(self, update, context):
    query = update.pre_checkout_query
    # 验证订单有效性
    order = await self.verify_order(query.invoice_payload)
    if order:
        await query.answer(ok=True)
    else:
        await query.answer(ok=False, error_message="订单验证失败")
# ...
async def on_successful_payment(self, update, context):
    payment = update.message.successful_payment
    await self.fulfill_order(payment.invoice_payload, payment.total_amount)
    await self.send_receipt(update.message.chat_id, payment)
```

### 场景二：大规模社群运营（运营视角）

某游戏公会管理50+Telegram群组，需要统一公告推送、违规用户批量管理、新人引导流程。专业版的批量推送引擎支持：

```python
class BatchPushEngine:
    def __init__(self, bot, rate_limit=25):
        self.bot = bot
        self.rate_limit = rate_limit  # 每秒消息数
        self.delivery_tracker = {}
# ...
    async def broadcast(self, group_ids, message, parse_mode="HTML"):
        """批量推送消息到多个群组"""
        results = {"success": 0, "failed": 0, "blocked": 0}
        for group_id in group_ids:
            try:
                await asyncio.sleep(1 / self.rate_limit)  # 速率控制
                await self.bot.send_message(group_id, message, parse_mode=parse_mode)
                results["success"] += 1
                self.delivery_tracker[group_id] = {"status": "delivered", "ts": time.time()}
            except Exception as e:
                if "blocked" in str(e):
                    results["blocked"] += 1
                else:
                    results["failed"] += 1
                self.delivery_tracker[group_id] = {"status": "failed", "error": str(e)}
        return results
```

### 场景三：付费内容订阅系统（产品视角）

知识付费创作者搭建订阅系统：用户通过Stars支付订阅费 -> 获得专属群组访问权 -> 每日接收付费内容 -> 到期自动续费提醒。专业版的会话状态机管理订阅全生命周期：

```python
class SubscriptionStateMachine:
    STATES = {
        "TRIAL": "试用中",
        "ACTIVE": "已订阅",
        "EXPIRING": "即将到期",
        "EXPIRED": "已过期",
        "CHURNED": "已流失"
    }
# ...
    async def transition(self, user_id, new_state):
        old_state = await self.get_state(user_id)
        valid = self.validate_transition(old_state, new_state)
        if not valid:
            raise InvalidTransitionError(f"{old_state} -> {new_state}")
        await self.set_state(user_id, new_state)
        await self.trigger_hook(user_id, old_state, new_state)
```

## 使用流程

### 企业级部署（约120秒）

1. **环境准备**：确保Python 3.8+和pip已安装
2. **安装依赖**：`pip install python-telegram-bot redis aiohttp`
3. **配置Token**：将Bot Token存入环境变量
4. **初始化项目**：运行Agent生成的脚手架代码

```bash
# 配置环境变量
export TELEGRAM_BOT_TOKEN="your_token_here"
export REDIS_URL="redis://localhost:6379/0"
# ...
# 启动Bot（带热重载）
python bot_main.py --env production --reload
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | tg-bot-builder处理的内容输入 |,  |
| content | string | 否 | tg-bot-builder处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "builder 相关配置参数",
    result: "builder 相关配置参数",
    result: "builder 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 问题现象 | 可能原因 | 排查步骤 | 优先级 |
|:---:|:---:|:---:|:---:|
| Webhook无响应 | 证书过期/防火墙阻断 | 检查证书有效期，调用getWebhookInfo查看错误 | P0 |
| 大量429错误 | 速率控制未生效 | 检查rate_limit配置，确认队列缓冲正常 | P0 |
| 支付回调丢失 | pre_checkout超时 | 确认handler响应时间<10秒，
| 状态机卡死 | 超时未触发 | 检查Redis连接，确认定时任务正常运行 | P1 |
| 群组消息遗漏 | Bot被踢出群组 | 调用getChat验证成员状态，重新邀请 | P2 |
| 模板渲染失败 | 变量缺失 | 检查模板变量注入逻辑，添加默认值 | P2 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **Node.js**: 16+（可选，用于前端仪表盘）
- **Redis**: 6.0+（用于会话缓存与消息队列）

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| python-telegram-bot | Python库 | 必需 | `pip install python-telegram-bot` |
| redis | Python库 | 必需 | `pip install redis` |
| aiohttp | Python库 | 必需 | `pip install aiohttp` |
| prometheus-client | Python库 | 推荐 | `pip install prometheus-client` |
| Stripe SDK | 支付SDK | 可选 | `pip install stripe` |

### API Key 配置
- **Telegram Bot Token**: 通过 `@BotFather` 获取，存储于环境变量 `TELEGRAM_BOT_TOKEN`
- **Redis连接**: 存储于环境变量 `REDIS_URL`，格式 `redis://user:pass@host:port/db`
- **Fragment账户**: 用于Stars提现，在Telegram内配置
- **禁止**: 在代码或配置文件中硬编码任何Token或密钥

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成企业级代码

## 案例展示

### 高级会话状态机配置

```python
CONVERSATION_FLOW = {
    "ENTRY": {
        "handler": "start_conversation",
        "transitions": {
            "menu_select": "MAIN_MENU",
            "direct_question": "QA_MODE"
        }
    },
    "MAIN_MENU": {
        "handler": "show_menu",
        "transitions": {
            "product_browse": "PRODUCT_LIST",
            "order_query": "ORDER_LOOKUP",
            "human_support": "ESCALATE_HUMAN"
        }
    },
    "PRODUCT_LIST": {
        "handler": "list_products",
        "transitions": {
            "add_to_cart": "CART_REVIEW",
            "product_detail": "PRODUCT_DETAIL",
            "back": "MAIN_MENU"
        }
    }
}
```

### 群组权限矩阵配置

```python
GROUP_PERMISSIONS = {
    "owner":    {"ban": True,  "pin": True,  "mute": True,  "invite": True,  "manage": True},
    "admin":    {"ban": True,  "pin": True,  "mute": True,  "invite": True,  "manage": False},
    "moderator": {"ban": True,  "pin": False, "mute": True,  "invite": True,  "manage": False},
    "member":   {"ban": False, "pin": False, "mute": False, "invite": False, "manage": False},
}
```

### 批量推送与回执追踪

```python
PUSH_CONFIG = {
    "rate_limit_per_sec": 25,       # 全局速率
    "per_user_interval": 3600,      # 单用户间隔（秒）
    "max_retries": 3,               # 失败重试次数
    "retry_backoff": "exponential", # 退避策略
    "track_delivery": True,         # 追踪送达状态
    "auto_clean_blocked": True      # 自动清理已屏蔽用户
}
```

## 常见问题

### Q1：Stars支付和传统支付有什么区别？

A：Telegram Stars是平台内虚拟货币，用户无需跳转第三方支付页面，转化率更高。Stars支付不需要provider_token，currency设为"XTR"。提现时通过Fragment平台将Stars兑换为法币.
### Q2：批量推送如何避免触发429限流？

A：专业版内置速率控制器，全局速率建议设为25条/秒（留出余量）。同时实现单用户间隔控制（默认1小时1条），并使用指数退避重试机制。批量推送前先调用 `getChat` 验证Bot是否仍在群组中.
### Q3：会话状态机如何处理用户中途退出？

A：状态机默认设置30分钟超时，超时后自动回到ENTRY状态。对于关键流程（如支付中途），状态会持久化到Redis，用户重新进入时恢复到上次状态.
### Q4：如何监控Bot的运行健康度？

A：专业版提供MetricsCollector模块，实时采集以下指标：(1) 消息处理延迟P50/P95/P99；(2) 错误率与错误分类分布；(3) 活跃用户数与会话数；(4) 支付转化漏斗。数据可推送到Prometheus/Grafana.
### Q5：高级群管如何实现自动化审计？

A：通过GroupManager模块记录所有管理操作（封禁/解禁/置顶/修改权限），生成审计日志并定期导出。支持设置敏感操作告警（如批量封禁超过阈值时通知优秀管理员）.
### Q6：自定义模板库如何团队共享？

A：模板库支持Git版本管理，团队成员通过模板仓库共享和同步。每个模板包含版本号、变更记录和使用说明，支持回滚到历史版本.
### Q7：专业版是否提供SLA保障？

A：专业版提供99.5%可用性SLA保障，包括7x24小时优先技术支持、4小时内关键问题响应、每月性能优化报告.
### Q8：如何处理跨时区的批量推送？

A：BatchPushEngine支持按用户时区分组推送，避免在用户深夜发送消息。时区信息从用户首次互动时获取并存储，支持夏令时自动调整.
### Q9：Bot被封禁后如何快速恢复？

A：(1) 检查是否违反Telegram Bot条款（如发送垃圾消息）；(2) 通过BotFather申诉；(3) 专业版提供备用Bot方案，主Bot被封时自动切换到备用Bot.
### Q10：如何评估是否需要专业版？

A：如果你有以下需求之一，建议升级：(1) 需要支付集成；(2) 群组数量超过10个；(3) 日活用户超过1000；(4) 需要多轮对话管理；(5) 需要团队协作管理Bot.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

