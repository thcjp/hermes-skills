---
slug: "telegram-msg-toolkit"
name: "telegram-msg-toolkit"
version: 1.0.1
displayName: "Telegram消息工具箱(专业版)"
summary: "Telegram Bot 全能力版：批量操作、群组管理、频道运营、审核与Webhook回调。。Telegram 消息工具箱（专业版）面向团队与企业用户，在免费版基础消息能力之上新增批量操作引"
license: "MIT"
edition: "pro"
description: |-
  Telegram 消息工具箱（专业版）面向团队与企业用户，在免费版基础消息能力之上新增批量操作引擎、群组管理、频道运营、消息审核与 Webhook 回调。支持从消息发送到群组运营的完整工作流。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - 沟通协作
  - 即时通讯
  - Telegram
  - 群组管理
  - 自动化运营
  - 消息自动化
  - 社交
  - 通信
  - telegram
  - webhook
  - bot
  - json
  - chat_id
tools:
  - read
  - exec
  - write
homepage: ""
category: "Communication"
---
# Telegram消息工具箱(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Telegram消息工具箱(专业版)群组管理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 核心能力

| 类别 | 能力 | 数量 | 免费版 |
|:-----|:-----|:-----|:-----|
| 基础消息 | 文本/图片/文件/位置/投票/转发 | 6 | 是 |
| 消息操作 | 编辑/删除/复制 | 3 | 是 |
| 聊天查询 | 信息/成员/管理员/数量 | 4 | 是 |
| 邀请链接 | 生成/撤销/编辑 | 3 | 是 |
| 批量操作 | 批量消息/投票/转发/编辑 | 4 | 否 |
| 群组管理 | 踢人/封禁/权限/管理员/限制 | 5 | 否 |
| 频道运营 | 发布/定时/信息/统计 | 4 | 否 |
| 消息审核 | 关键词/媒体/自动处置/日志 | 4 | 否 |
| Webhook | 设置/回调/重试/签名 | 4 | 否 |
| 高级媒体 | 音视频/贴纸包/动图/语音 | 4 | 否 |
| 多 Bot | 负载分担/联动/故障转移 | 3 | 否 |
| 数据统计 | 消息量/活跃度/成员分析 | 3 | 否 |
### 基础消息

针对基础消息,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供基础消息相关的配置参数、输入数据和处理选项.
**输出**: 返回基础消息的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础消息`的配置文档进行参数调优
### 消息操作

针对消息,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供消息操作相关的配置参数、输入数据和处理选项.
**输出**: 返回消息操作的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`消息操作`的配置文档进行参数调优
### 聊天查询

针对聊天,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供聊天查询相关的配置参数、输入数据和处理选项.
**输出**: 返回聊天查询的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`聊天查询`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：批量通知推送（运营视角）

需要向 10 个群组同时发送版本更新通知。批量消息引擎自动控制速率，支持个性化模板与失败重试.
```bash
# 批量消息发送
python tg_batch_sender.py \
  --bot_token "${TELEGRAM_BOT_TOKEN}" \
  --chats "groups.json" \
  --message "v2.1.0 已发布！新增：实时协作、自动保存、版本回溯。" \
  --parse_mode "MarkdownV2" \
  --rate_limit 1 \
  --retry 3 \
  --dry_run false
```

```python
# 批量发送配置
batch_config = {
    "chats": [
        {"chat_id": "-1001234567890", "name": "开发群"},
        {"chat_id": "-1001234567891", "name": "测试群"},
        {"chat_id": "-1001234567892", "name": "用户群"}
    ],
    "message_template": "v"toolkit_result" 已发布！\n\n新增功能：\n内容生成工具\n\n更新时间："toolkit_result"",
    "variables": {
        "version": "2.1.0",
        "features": "- 实时协作\n- 自动保存\n- 版本回溯",
        "time": "2026-07-18 10:00"
    },
    "rate_limit_per_sec": 1,       # 每秒最多 1 条（单聊限制）
    "global_limit_per_sec": 25,    # 全局每秒最多 25 条
    "retry_on_failure": 3,
    "retry_delay_sec": 5
}
```

### 场景二：群组审核管理（管理员视角）

新成员加入时自动验证，关键词过滤垃圾消息，违规用户自动禁言或封禁。所有审核动作记录日志.
```yaml
moderation:
  enabled: true
  rules:
    - type: "keyword_filter"
      keywords: ["spam", "广告", "推广链接"]
      action: "delete_message"
      notify: true
    - type: "new_member"
      action: "restrict_permissions"
      duration_minutes: 5
      allowed_permissions: ["send_messages"]
      restricted_permissions: ["send_media", "send_other"]
    - type: "flood_detection"
      threshold: 10            # 10 条消息/分钟
      window_minutes: 1
      action: "mute"
      duration_minutes: 30
    - type: "media_filter"
      blocked_types: ["sticker", "animation"]
      action: "delete_message"
  logging:
    enabled: true
    chat_id: "-1001234567999"    # 审核日志群
    log_actions: ["delete", "mute", "ban", "restrict"]
```

### 场景三：频道定时发布（内容视角）

提前编排一周的频道内容，设置定时发布。支持 Markdown 格式与禁用预览.
```bash
# 定时发布配置
python tg_channel_scheduler.py \
  --bot_token "${TELEGRAM_BOT_TOKEN}" \
  --channel "@mychannel" \
  --schedule "schedule.json" \
  --timezone "Asia/Shanghai"
```

```json
{
  "channel": "@mychannel",
  "schedule": [
    {
      "time": "2026-07-20T09:00:00+08:00",
      "text": "周一早安！本周技术分享：构建可扩展的微服务架构。",
      "parse_mode": "MarkdownV2",
      "disable_preview": true
    },
    {
      "time": "2026-07-21T12:00:00+08:00",
      "photo": "https://example.com/diagram.png",
      "caption": "架构图分享：服务发现与负载均衡流程。"
    },
    {
      "time": "2026-07-22T18:00:00+08:00",
      "text": "用户问答精选：本周收集了 15 个高频问题，详细解答如下...",
      "parse_mode": "HTML"
    }
  ]
}
```

### 场景四：Webhook 实时处理（开发者视角）

设置 Webhook 接收实时更新，处理内联键盘回调、新成员事件与命令，无需轮询.
```bash
# 设置 Webhook
curl -X POST "https://api.telegram.org/bot"toolkit_metadata"/setWebhook" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://your-app.com/webhook/telegram",
    "secret_token": ""toolkit_status"",
    "allowed_updates": ["message", "callback_query", "chat_member"],
    "max_connections": 40
  }'
# ...
# 获取 Webhook 信息
curl "https://api.telegram.org/bot"toolkit_summary"/getWebhookInfo"
```

## 使用流程

### 120 秒上手

1. 确认已拥有免费版 Bot Token 与基础消息能力
2. 配置批量发送或群组审核规则
3. 设置 Webhook 接收实时事件（可选）
4. 启动定时发布或审核引擎
5. 监控数据统计报表

### 群组管理命令

```bash
# 踢出成员（可恢复）
curl -X POST "https://api.telegram.org/bot"toolkit_details"/kickChatMember" \
  -H "Content-Type: application/json" \
  -d '{"chat_id": "-1001234567890", "user_id": 123456789, "until_date": 0}'
# ...
# 解除封禁
curl -X POST "https://api.telegram.org/bot"toolkit_count"/unbanChatMember" \
  -H "Content-Type: application/json" \
  -d '{"chat_id": "-1001234567890", "user_id": 123456789, "only_if_banned": true}'
# ...
# 已知限制
curl -X POST "https://api.telegram.org/bot"toolkit_timestamp"/restrictChatMember" \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": "-1001234567890",
    "user_id": 123456789,
    "permissions": {
      "can_send_messages": false,
      "can_send_media_messages": false,
      "can_send_other_messages": false,
      "can_add_web_page_previews": false
    },
    "until_date": 0
  }'
# ...
# 提升为管理员
curl -X POST "https://api.telegram.org/bot"toolkit_version"/promoteChatMember" \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": "-1001234567890",
    "user_id": 123456789,
    "can_delete_messages": true,
    "can_restrict_members": true,
    "can_invite_users": true
  }'
```

### 邀请链接管理

```bash
# 创建邀请链接
curl -X POST "https://api.telegram.org/bot"field_9"/createChatInviteLink" \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": "-1001234567890",
    "expire_date": 1752790800,
    "member_limit": 50,
    "name": "7月活动邀请"
  }'
# ...
# 编辑邀请链接
curl -X POST "https://api.telegram.org/bot"field_10"/editChatInviteLink" \
  -H "Content-Type: application/json" \
  -d '{"chat_id": "-1001234567890", "invite_link": "https://t.me/+ABC...", "member_limit": 100}'
# ...
# 撤销邀请链接
curl -X POST "https://api.telegram.org/bot"field_11"/revokeChatInviteLink" \
  -H "Content-Type: application/json" \
  -d '{"chat_id": "-1001234567890", "invite_link": "https://t.me/+ABC..."}'
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | telegram-msg-toolkit处理的内容输入 |,  |
| content | string | 否 | telegram-msg-toolkit处理的内容输入 |, 可选值: json/text/markdown |
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
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：可访问 `api.telegram.org` 的网络连接
- **Python**：3.10+（运行批量引擎与审核脚本）
- **Node.js**：18+（运行 Webhook 接收端）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| curl | CLI 工具 | 必需 | 系统自带或包管理器安装 |
| Telegram Bot Token | 凭证 | 必需 | 通过 BotFather 创建 Bot 获取 |
| Python 3.10+ | 运行时 | 批量操作必需 | 官方网站下载 |
| requests | Python 库 | 推荐 | pip install requests |
| Webhook 接收端 | 服务 | Webhook 必需 | 自行部署 HTTPS 接收服务 |
| 数据库 | 服务 | 统计推荐 | 用于审核日志与统计数据存储 |

### API Key 配置
- **Bot Token**：通过 BotFather 创建 Bot 获取，保存在环境变量 `TELEGRAM_BOT_TOKEN` 中
- **Webhook Secret**：自定义密钥，配置在 `WEBHOOK_SECRET` 中，用于回调验签
- **多 Bot Token**：配置在 `BOT_TOKEN_1`、`BOT_TOKEN_2` 等环境变量中
- **禁止**：在 SKILL.md 或脚本中硬编码任何 Token 或密钥
- **安全建议**：Token 泄露后通过 BotFather `/revokenewtoken` 重置

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 Claude Sonnet 进行审核决策，Haiku 进行批量消息生成
- **数据存储**：审核日志与统计数据可归档到 `关系型数据库` 数据库做长期分析

## 案例展示

### 群组权限配置

```yaml
group_management:
  default_permissions:
    can_send_messages: true
    can_send_media_messages: true
    can_send_polls: true
    can_send_other_messages: true
    can_add_web_page_previews: false
    can_change_info: false
    can_invite_users: true
    can_pin_messages: false
  restricted_permissions:
    can_send_messages: true
    can_send_media_messages: false
    can_send_other_messages: false
    can_add_web_page_previews: false
```

### 审核规则配置

| 规则类型 | 触发条件 | 处置动作 | 通知 |
|---:|:---|---:|---:|
| 关键词过滤 | 消息含敏感词 | 删除消息 | 是 |
| 新成员限制 | 加入后 5 分钟内 | 限制媒体发送 | 是 |
| 洪水检测 | 10 条/分钟 | 禁言 30 分钟 | 是 |
| 媒体过滤 | 表情包/动图 | 删除消息 | 否 |
| 链接过滤 | 外部链接 | 删除+警告 | 是 |
| 重复消息 | 3 条相同内容 | 删除+禁言 | 是 |

### Webhook 事件配置

```yaml
webhook:
  url: "https://your-app.com/webhook/telegram"
  secret_token: "${WEBHOOK_SECRET}"
  allowed_updates:
    - message               # 消息事件
    - callback_query        # 内联回调
    - chat_member           # 成员变动
    - channel_post          # 频道发布
    - edited_message        # 编辑消息
  max_connections: 40
  drop_pending_updates: false
  retry:
    max_attempts: 3
    backoff: "exponential"   # 指数退避
    initial_delay_sec: 1
```

### 多 Bot 负载分担

```yaml
multi_bot:
  enabled: true
  strategy: "round_robin"       # round_robin | weighted | failover
  bots:
    - token: "${BOT_TOKEN_1}"
      weight: 3
      role: "sender"
    - token: "${BOT_TOKEN_2}"
      weight: 2
      role: "sender"
    - token: "${BOT_TOKEN_3}"
      weight: 1
      role: "backup"
  failover:
    enabled: true
    health_check_interval: 60
    auto_switch: true
```

### 数据统计维度

| 报表 | 指标 | 频率 | 输出 |
|:------:|--------|:-------|:------:|
| 消息量 | 每日/每周/每月消息数 | 每日 | JSON+CSV |
| 活跃度 | 活跃成员/发言率/沉默率 | 每周 | 图表数据 |
| 成员分析 | 增长/流失/留存 | 每月 | 折线图 |
| 审核日志 | 删除/禁言/封禁次数 | 每日 | 日志表 |
| 频道统计 | 阅读/分享/订阅 | 每周 | 排序表 |

## 常见问题

### Q1：批量发送触发限流？
A：专业版支持全局每秒 25 条、单聊每秒 1 条。`rate_limit_per_sec` 控制节奏。收到 429 时按 `retry_after` 等待后重试，最多重试 3 次.
### Q2：审核误杀正常消息？
A：调整关键词列表精确度，使用正则匹配而非纯文本。新成员限制设 5 分钟而非永久。开启审核日志群人工复核，误杀可恢复.
### Q3：Webhook 设置失败？
A：检查 URL 是否为 HTTPS（Telegram 强制要求）、端口是否在支持列表（443/80/88/8443）、服务器是否可公网访问。`getWebhookInfo` 查看错误详情.
### Q4：promoteChatMember 返回 400？
A：Bot 需为群组管理员且拥有 `can_promote_members` 权限。通过 BotFather 的 `/setprivacy` 关闭隐私模式，或将 Bot 设为群组管理员.
### Q5：频道定时发布时区错误？
A：`schedule.json` 中的时间使用 ISO 8601 带时区格式（如 `2026-07-20T09:00:00+08:00`）。脚本配置 `timezone: "Asia/Shanghai"` 确保本地时间正确转换.
### Q6：多 Bot 切换后消息丢失？
A：切换前确保 `offset` 同步——所有 Bot 共享 `getUpdates` 的 offset。使用 Webhook 模式则无此问题。故障转移后通知管理员人工确认.
### Q7：专业版与免费版 API 是否兼容？
A：完全兼容。专业版包含免费版所有 `sendMessage`、`sendPhoto` 等接口，额外扩展批量端点、管理接口与 Webhook。免费版代码无需修改即可在专业版运行.
### Q8：restrictChatMember 的 until_date 怎么填？
A：Unix 时间戳（秒）。`0` 或不填表示永久限制。临时禁言填未来时间戳，如 `until_date: 1752790800`.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 依赖Agent平台的LLM能力与运行环境配置
- 免费版功能受限，高级能力需升级专业版
- 处理能力受限于本地硬件资源
