---
slug: "telegram-toolkit"
name: "telegram-toolkit"
version: 1.0.1
displayName: "TG机器人工具(专业版)"
summary: "面向企业的Telegram Bot专业版，含对话状态机、富媒体模板、多机器人管理、消息队列与优先支持。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队、企业与专业开发者的Telegram Bot工作流设计工具专业版。在免费版基础上新增对话状态机与会话管理、富媒体消息模板库、多机器人统一管理面板、消息队列削峰与批量发送、Webhook健康监控与自动告警等高级能力，配套面向运维、产品、开发者角色的多角色场景指南。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修.
tags:
  - 集成工具
  - 即时通讯
  - 机器人
  - 高级特性
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# TG机器人工具(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| TG机器人工具(专业版)多机器人管理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 对话管理 | 单轮命令 | 多轮状态机+上下文持久化 |
| 富媒体 | 纯文本 | 图片/视频/文件/按钮模板库 |
| 多Bot管理 | 单Bot | 统一面板管理多Bot |
| 消息发送 | 同步发送 | 队列削峰+批量+限流控制 |
| Webhook监控 | 无 | 健康检查+告警+故障切换 |
| 国际化 | 无 | 多语言模板+语言自适应 |
| 优先支持 | 社区 | 工单优先响应 |
### 能力分类

针对能力分类,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力分类相关的配置参数、输入数据和处理选项.
**输出**: 返回能力分类的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力分类`的配置文档进行参数调优
### 对话管理

针对对话,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供对话管理相关的配置参数、输入数据和处理选项.
**输出**: 返回对话管理的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`对话管理`的配置文档进行参数调优
### 富媒体

针对富媒体,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供富媒体相关的配置参数、输入数据和处理选项.
**输出**: 返回富媒体的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`富媒体`的配置文档进行参数调优
#
## 适用场景

### 场景一：多轮客服对话（产品视角）

通过状态机编排"收集问题→分类→转人工→满意度回访"的多轮对话流程，上下文跨轮次持久化.
```python
from telegram_toolkit import ProFeatures, StateMachine
# ...
pro = ProFeatures(token_env="TG_BOT_TOKEN")
# ...
sm = StateMachine()
sm.add_state("await_issue", prompt="请描述您遇到的问题")
sm.add_state("await_category", prompt="请选择问题分类：1.账单 2.功能 3.故障")
sm.add_transition("await_issue", "await_category", on="text_received")
sm.add_transition("await_category", "resolved", on="category_selected")
# ...
pro.register_conversation("/support", sm)
```

### 场景二：多Bot矩阵运营（运营视角）

通过统一面板管理客服Bot、通知Bot、营销Bot的配置、监控与消息统计，无需逐个切换.
```python
pro.manage_bots([
    {"name": "客服Bot", "token_env": "SUPPORT_BOT_TOKEN"},
    {"name": "通知Bot", "token_env": "NOTIFY_BOT_TOKEN"},
    {"name": "营销Bot", "token_env": "MARKETING_BOT_TOKEN"}
])
pro.dashboard.start()  # 启动统一监控面板
```

### 场景三：高并发营销推送（营销视角）

将10万条营销消息入队，按Telegram限流规则自动节流发送，支持优先级与失败重试.
```python
pro.broadcast(
    audience="subscribers.csv",
    template="templates/promo.html",
    rate_limit=25,            # 每秒25条（低于Telegram限制）
    priority="normal",
    retry_failed=True
)
```

### 场景四：富媒体通知（开发者视角）

通过模板库发送带Inline Keyboard按钮、图片、格式化文本的富媒体通知，提升信息可读性.
```python
pro.send_template(
    chat_id=user_id,
    template="alert_with_buttons",
    context={
        "title": "部署完成",
        "detail": "服务v1.2.3已上线",
        "buttons": [
            {"text": "查看日志", "callback_data": "view_log"},
            {"text": "回滚", "callback_data": "rollback"}
        ]
    }
)
```

### 场景五：Webhook健康监控（运维视角）

持续监控Webhook健康状态，延迟超阈值自动告警，故障时自动切换到长轮询兜底.
```python
pro.webhook_monitor(
    health_check_interval=60,        # 60秒检查一次
    latency_alert_ms=5000,          # 延迟超5秒告警
    auto_fallback_to_polling=True,  # Webhook故障自动切长轮询
    webhook_env="OPS_WEBHOOK"       # 告警地址
)
```

## 使用流程

### 优秀步：启用专业版功能

```python
from telegram_toolkit import ProFeatures
# ...
pro = ProFeatures(token_env="TG_BOT_TOKEN")
pro.enable_message_queue(max_size=10000, rate_limit=25)
pro.webhook_monitor(auto_fallback_to_polling=True)
```

### 第二步：注册对话状态机

```python
sm = pro.create_conversation("/onboarding")
sm.add_state("ask_name", prompt="请输入您的姓名")
sm.add_state("ask_email", prompt="请输入您的邮箱")
sm.add_state("done", prompt="注册完成！")
sm.add_transition("ask_name", "ask_email", on="text_received")
sm.add_transition("ask_email", "done", on="text_received")
```

### 第三步：发送富媒体模板

```python
pro.send_template(chat_id, "welcome_card", context={"user": "张三"})
```

完整上手时间约120秒.
#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | telegram-toolkit处理的内容输入 |,  |
| content | string | 否 | telegram-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
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

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需能访问 api.telegram.org
- **Python**: 3.8+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| requests | Python包 | 必需 | `pip install requests` |
| Python | 运行时 | 必需 | python.org 官方下载 |
| redis | Python包 | 可选 | `pip install redis`（会话持久化） |
| sqlite3 | Python模块 | 可选 | Python标准库（会话持久化） |
| jinja2 | Python包 | 可选 | `pip install jinja2`（模板渲染） |

### API Key 配置
- **TG_BOT_TOKEN**: 通过 @BotFather 获取，存入环境变量，禁止硬编码
- **多Bot Token**: 每个Bot独立环境变量（如 SUPPORT_BOT_TOKEN、NOTIFY_BOT_TOKEN）
- **Webhook secret_token**: 设置Webhook时生成，服务端校验请求头
- **OPS_WEBHOOK**: 监控告警Webhook地址，通过环境变量配置

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 消息队列削峰

```python
pro.queue_config(
    max_size=50000,           # 队列上限
    rate_limit=25,            # 每秒发送上限（Telegram限制约30/s）
    batch_size=25,            # 批量发送数
    retry_policy="exponential",  # 失败指数退避
    priority_levels=3         # 3级优先级
)
```

### 多Bot统一监控

```python
pro.dashboard_config(
    metrics=["uptime", "msg_sent", "msg_failed", "active_users"],
    refresh_interval=30,
    alert_on_failure=True,
    webhook_env="OPS_WEBHOOK"
)
```

### 国际化配置

```python
pro.i18n_config(
    default_lang="zh-CN",
    detect_user_lang=True,     # 从用户语言设置自动检测
    templates_dir="locales/"
)
# locales/zh-CN/welcome.json
# locales/en/welcome.json
```

## 常见问题

### Q1：状态机对话中途用户输入无关内容怎么办？

A：为每个状态设计`fallback`处理，当输入不匹配预期时提示用户正确输入或重置对话。可用`sm.add_fallback(state, handler)`配置.
### Q2：批量推送时部分消息429失败如何重试？

A：专业版消息队列自带失败重试。429会按`retry_after`等待后重试，重试3次仍失败则记录到失败队列，可用`pro.retry_failed()`单独重发.
### Q3：Webhook故障切换到长轮询会丢消息吗？

A：不会。切换前会先`deleteWebhook`，Telegram将未投递的更新保留在服务端，长轮询通过`getUpdates`的`offset`参数从断点继续拉取.
### Q4：多Bot管理的Token如何安全存储？

A：每个Bot的Token存入独立环境变量（如`SUPPORT_BOT_TOKEN`、`NOTIFY_BOT_TOKEN`），专业版通过`token_env`参数引用，绝不落盘明文.
### Q5：富媒体模板如何复用？

A：模板存为JSON文件放`templates/`目录，通过`pro.send_template(chat_id, "template_name", context)`渲染发送。不同Bot可共享模板目录.
### Q6：国际化模板如何组织？

A：按语言代码建子目录：`locales/zh-CN/`、`locales/en/`。每语言下保持相同文件名结构，专业版根据用户语言设置自动选择对应模板.
### Q7：消息队列积压怎么办？

A：(1) 检查`rate_limit`是否过低；(2) 评估是否为营销推送峰值，考虑分批错峰发送；(3) 提高队列`max_size`或增加并发worker；(4) 监控队列长度告警，超阈值触发降级.
### Q8：对话上下文如何持久化？

A：专业版支持将会话状态持久化到本地SQLite或Redis。配置`sm.persist(backend="sqlite", path="sessions.db")`，Bot重启后可恢复未完成的对话.
### Q9：Inline Keyboard按钮回调超时怎么办？

A：Telegram对callback_query无硬性超时，但用户体验上建议30秒内应答。专业版消息队列会优先处理callback应答，避免用户长时间等待.
### Q10：专业版支持Telegram Mini App吗？

A：支持。专业版提供Mini App的Web App URL配置与`web_app_data`更新处理，可用于构建内嵌在Telegram中的Web应用交互.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 依赖Agent平台的LLM能力与运行环境配置
- 免费版功能受限，高级能力需升级专业版
- 处理能力受限于本地硬件资源
