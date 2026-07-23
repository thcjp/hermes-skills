---
slug: "telegram-messaging"
name: "telegram-messaging"
version: "1.0.0"
displayName: "Telegram 消息机器人"
summary: "通过 Telegram Bot API 发送消息、管理聊天、处理文件与自动化机器人工作流。"
license: "Proprietary"
description: |-
  Telegram Bot API 集成 Skill。支持发送文本、图片、文档、位置、投票等多类型消息，
  管理聊天信息与成员、检索聊天历史、转发与编辑消息、生成与撤销邀请链接、
  处理内联键盘回调、设置机器人命令列表。所有写操作需用户确认后执行，读操作可直接调用。
  覆盖部署通知推送、群组投票反馈、历史检索转发、社区邀请链接生命周期管理等场景。
tags:
  - 通用办公
  - Automation
  - Bot
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# Telegram 消息机器人

通过 Telegram Bot API 实现 Telegram 机器人消息发送、聊天管理、文件处理与自动化工作流。所有调用通过 Bot Token 认证，写操作需用户显式确认后执行。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| **多类型消息发送**：支持文本、图片、文档、位置、投票五种消息类型，图片与文档可附加 caption 说明 | 支持 | 支持 |
| **消息生命周期管理**：编辑已发送消息、删除消息（限机器人自身消息或管理员权限群组）、转发消息到其他聊天 | 不支持 | 支持 |
| **聊天信息检索**：获取聊天基本信息、聊天历史消息、成员状态与角色、管理员列表、成员计数 | 不支持 | 支持 |
| **邀请链接管理**：生成新的聊天邀请链接、撤销已有邀请链接，支持社区入群管控 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- **多类型消息发送**：支持文本、图片、文档、位置、投票五种消息类型，图片与文档可附加 caption 说明
- **消息生命周期管理**：编辑已发送消息、删除消息（限机器人自身消息或管理员权限群组）、转发消息到其他聊天
- **聊天信息检索**：获取聊天基本信息、聊天历史消息、成员状态与角色、管理员列表、成员计数
- **邀请链接管理**：生成新的聊天邀请链接、撤销已有邀请链接，支持社区入群管控
- **回调与命令**：应答内联键盘回调查询、设置与获取机器人命令列表
- **更新获取**：通过长轮询获取 incoming updates，与 webhook 互斥
- **写操作确认机制**：所有写操作（发消息、删消息、编辑消息、转发消息等）需用户确认后执行
- **速率限制处理**：遵循全局 30 条/秒、单聊天 1 条/秒的速率限制，HTTP 429 时按 retry_after 延迟重试
### 多类型消息发送

执行多类型消息发送操作,处理用户输入并返回结果。

**输入**: 用户提供多类型消息发送所需的参数和指令。

**输出**: 返回多类型消息发送的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`多类型消息发送`相关配置参数进行设置
### 消息生命周期管理

执行消息生命周期管理操作,处理用户输入并返回结果。

**输入**: 用户提供消息生命周期管理所需的参数和指令。

**输出**: 返回消息生命周期管理的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`消息生命周期管理`相关配置参数进行设置
### 聊天信息检索

执行聊天信息检索操作,处理用户输入并返回结果。

**输入**: 用户提供聊天信息检索所需的参数和指令。

**输出**: 返回聊天信息检索的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`聊天信息检索`相关配置参数进行设置
#
## 工具列表

### 机器人信息
- `telegram_get_me`：获取机器人基本信息（用户名、名称、能力）— 读操作
- `telegram_get_updates`：通过长轮询获取 incoming updates — 读操作

### 消息发送与管理
- `telegram_send_message`：发送文本消息 — 写操作
- `telegram_send_photo`：发送图片 — 写操作
- `telegram_send_document`：发送文档/文件 — 写操作
- `telegram_send_location`：发送地理位置 — 写操作
- `telegram_send_poll`：发送原生投票 — 写操作
- `telegram_edit_message`：编辑已发送的消息 — 写操作
- `telegram_delete_message`：删除消息 — 写操作
- `telegram_forward_message`：转发消息到其他聊天 — 写操作

### 聊天管理
- `telegram_get_chat`：按 ID 获取聊天信息 — 读操作
- `telegram_get_chat_history`：获取聊天历史消息 — 读操作
- `telegram_get_chat_member`：获取用户在聊天中的状态/角色 — 读操作
- `telegram_get_chat_administrators`：列出聊天管理员 — 读操作
- `telegram_get_chat_members_count`：获取聊天成员计数 — 读操作
- `telegram_create_chat_invite_link`：生成新的邀请链接 — 写操作
- `telegram_revoke_chat_invite_link`：撤销已有邀请链接 — 写操作

### 回调与命令
- `telegram_answer_callback_query`：应答内联键盘回调查询 — 写操作
- `telegram_set_my_commands`：设置机器人命令列表 — 写操作
- `telegram_get_my_commands`：获取当前命令列表 — 读操作

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 部署通知推送 | CI/CD 完成部署事件 | 向开发群发送文本通知 + 周报图表图片 |
| 群组投票与反馈收集 | 功能优先级决策需求 | 发送原生投票，成员点击选项即可投票 |
| 聊天历史检索与转发 | 关键词与目标广播频道 | 检索历史消息并转发到广播频道 |
| 邀请链接生命周期管理 | 社区入群管控需求 | 生成邀请链接，过期或泄露后撤销 |

**不适用于**：需要端到端加密的敏感通信、用户私信内容监听、大规模营销群发、非 Telegram 渠道消息推送。

## 使用流程

1. **确认 Bot Token 已配置**：Bot Token 通过 @BotFather 创建，配置在 Agent 环境中。调用 `telegram_get_me` 验证 Token 有效性
2. **获取目标聊天 ID**：群组/频道 ID 以 `-100` 开头（如 `-1001234567890`），用户私信用用户数字 ID
3. **读操作优先**：对于不熟悉的聊天，先调用 `telegram_get_chat` 确认聊天存在且机器人为成员
4. **写操作预览确认**：写操作前向用户预览消息内容与目标聊天，用户确认后执行
5. **执行与错误处理**：调用工具执行，若返回错误按错误处理章节排查

## 认证配置

Bot Token 通过 @BotFather 创建获取，配置在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.default.token` 字段。所有 API 调用自动注入 Bot Token，无需在调用参数中传递。

### 验证连接

```
telegram_get_me({})
```

返回机器人用户名、名称、能力信息，确认 Token 有效。

## 案例展示

### 案例 1：向开发群发送部署完成通知（含图片）

**触发**：CI/CD 流水线完成生产部署

**执行**：

```
telegram_send_message({
  chat_id: "-1001234567890",
  text: "部署完成！版本 2.1.0 已上线生产环境。"
})

telegram_send_photo({
  chat_id: "-1001234567890",
  photo: "https://example.com/chart.png",
  caption: "本周活动报告"
})
```

**结果**：开发群收到一条文本通知与一张周报图表，caption 标注为"本周活动报告"。

### 案例 2：发送功能优先级投票

**触发**：产品团队需要收集下一迭代功能优先级

**执行**：

```
telegram_send_poll({
  chat_id: "-1001234567890",
  question: "下一个迭代应优先开发哪个功能？",
  options: ["深色模式", "导出 PDF", "团队共享", "API 访问"]
})
```

**结果**：群内出现原生投票组件，成员直接点击选项投票，无需额外交互。

### 案例 3：检索历史消息并转发到广播频道

**触发**：需要将内部讨论的关键决策同步到广播频道

**执行**：

```
telegram_get_chat_history({
  chat_id: "-1001234567890",
  limit: 50
})
```

从返回的消息列表中定位目标消息 ID（如 42），再转发：

```
telegram_forward_message({
  chat_id: "-1009876543210",
  from_chat_id: "-1001234567890",
  message_id: 42
})
```

**结果**：消息 ID 42 的内容从内部群转发到广播频道 `-1009876543210`。

## 错误处理


| 错误 | 原因 | 处理方式 |
|------|------|---------|
| `chat_not_found` | 聊天 ID 不存在或机器人非成员 | 确认 ID 格式正确，群组以 `-100` 开头；将机器人加入目标聊天 |
| `bot_not_member` | 机器人不是目标聊天成员 | 通过群主邀请机器人加入群组并赋予发消息权限 |
| `message_not_found` | 消息 ID 在该聊天中不存在 | 确认消息 ID 来自同一聊天，重新检索历史获取正确 ID |
| `not_enough_rights` | 机器人在群组缺少管理员权限 | 群主需将机器人设为管理员并赋予所需权限（删消息、踢人等） |
| HTTP 429 `retry_after` | 触发速率限制 | 按 `retry_after` 字段指定的秒数等待后单聊天不超过 1 条/秒 |
| 409 Conflict | `get_updates` 与 webhook 同时启用 | 二选一：停用 webhook 后使用长轮询，或改用 webhook 接收更新 |
| `message_to_delete_not_found` | 消息超 48 小时或非机器人发送 | 群组中仅可删除 48 小时内的消息，且需管理员权限才能删他人消息 |
| `invalid_token` | Bot Token 无效或已过期 | 通过 @BotFather 重新获取 Token，更新配置后重启 Agent |

## 常见问题

### Q1：如何获取群组或频道的 chat_id？
A：将机器人加入目标群组后，调用 `telegram_get_updates` 获取 incoming updates，其中 `chat.id` 字段即为群组 ID。群组/频道 ID 以 `-100` 开头。也可通过 `telegram_get_chat_history` 获取消息后从返回结构中提取 chat_id。

### Q2：`get_updates` 和 webhook 有什么区别？
A：`get_updates` 是主动长轮询，Agent 定期向 Telegram 服务器拉取更新；webhook 是被动接收，Telegram 服务器在用户交互时推送更新到指定 URL。两者互斥，同时启用会返回 409 Conflict。长轮询适合开发调试，webhook 适合生产环境。

### Q3：为什么机器人无法删除群组中超过 48 小时的消息？
A：Telegram Bot API 限制机器人在群组中只能删除 48 小时内的消息。这是平台级限制，无法通过权限提升绕过。机器人始终可以删除自己发送的消息（不受 48 小时限制），但在群组中删除他人消息需要管理员权限且受时间窗口约束。

### Q4：发送图片后画质降低，如何保留原图质量？
A：Telegram 会对通过 `send_photo` 发送的图片进行压缩与重新编码。如需保留原始画质，改用 `telegram_send_document` 发送文件，文档类型不会触发压缩。代价是图片不会在聊天中直接预览，而是显示为可下载文件。

### Q5：速率限制的具体规则是什么？
A：全局限制约 30 条消息/秒，单聊天限制约 1 条/秒。当触发限制时返回 HTTP 429 状态码，响应体中 `retry_after` 字段指明需等待的秒数。应按该值延迟后重试，不要立即重发。批量发送时建议在单聊天消息间加入 1 秒间隔。

### Q6：如何设置机器人的命令菜单？
A：调用 `telegram_set_my_commands` 传入命令列表，用户在聊天框输入 `/` 时会看到这些命令。命令名以小写字母开头，可含数字与下划线，长度 1-32 字符。设置后可通过 `telegram_get_my_commands` 验证。

## 已知限制

- 机器人只能向其已加入且有发消息权限的聊天发送消息
- 群组中删除他人消息需管理员权限，且消息须在 48 小时内
- `get_updates` 长轮询与 webhook 互斥，不可同时使用
- 速率限制为全局 30 条/秒、单聊天 1 条/秒，超限返回 429
- 通过 `send_photo` 发送的图片会被压缩，需原图质量改用 `send_document`
- 服务消息（用户加入/退出）无法被删除
- 消息日期使用 Unix 时间戳（UTC），需自行转换为本地时区
- 不支持端到端加密，敏感信息不应通过 Bot 通道传输

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 Telegram Bot API（`https://api.telegram.org`）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Telegram Bot Token | 凭证 | 必需 | 通过 @BotFather 创建 Bot 获取 |
| Agent 工具运行时 | Agent 平台工具 | 必需 | Agent 平台内置或插件提供 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供决策能力 |

### API Key 配置
- Bot Token 配置在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.default.token` 字段
- 所有 Telegram API 调用自动注入该 Token，无需在调用参数中传递

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，工具调用需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
