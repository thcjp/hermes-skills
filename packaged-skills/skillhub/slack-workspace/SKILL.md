---
slug: slack-workspace
name: slack-workspace
version: "1.0.0"
displayName: Slack工作区管家
summary: Slack全量工作区管理：消息/频道/文件/提醒/画布/用户组，ClawLink OAuth托管
license: MIT
description: |-
  面向团队协作与工作区治理的Slack全量管理技能。通过ClawLink OAuth托管连接，
  提供消息管理、频道治理、对话历史、用户查询、文件操作、表情反应、提醒、
  置顶与星标、Canvas画布、团队管理、自定义emoji、通话管理十二大能力域。
  覆盖60+ Slack Web API工具，支持定时消息、线程回复、频道创建/归档/重命名、
  文件上传/下载/删除、用户组管理、企业Grid审计日志等高级操作。
  内置读写分级安全策略：读操作直接执行，写操作需用户确认后调用。
  适用于项目频道搭建、事件响应协作、文件分发、团队协调等场景。
tags:
  - Communication
  - 团队协作
  - 自动化
tools:
  - read
  - exec
---

# Slack工作区管家（Slack Workspace）

通过ClawLink OAuth托管连接管理Slack工作区，覆盖消息、频道、文件、用户、提醒、画布等60+ API工具。内置读写分级安全策略，写操作需用户确认后执行。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 `https://slack.com/api/*` 及 ClawLink 服务

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| ClawLink 插件 | 集成插件 | 必需 | Agent 平台插件市场安装 `clawlink-plugin` |
| Slack OAuth 连接 | OAuth 授权 | 必需 | 通过 ClawLink Dashboard 连接 Slack 工作区 |
| curl 或等价 HTTP 客户端 | 命令行工具 | 必需 | 系统自带或包管理器安装 |
| jq | JSON 处理工具 | 可选 | 提升响应可读性 |

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令驱动，需 exec 执行 clawlink 命令）
- **说明**: 通过 ClawLink 托管OAuth Token，Agent 调用 `clawlink_call_tool` 驱动 Slack Web API

### 连接架构
```text
Agent 聊话 ───▶ ClawLink (OAuth托管) ───▶ Slack Web API
                    │
                    ├─ 1. 安装插件并配对设备
                    ├─ 2. Dashboard连接Slack工作区
                    ├─ 3. OAuth Token安全存储
                    └─ 4. 代理API请求并注入Token
```

**无需在聊天中提供API Token**。ClawLink 安全存储 OAuth Token 并自动注入每个 Slack API 请求。

## 核心能力

### 1. 消息管理
发送文本消息到频道/DM/MPDM，回复指定消息线程，定时发送未来消息，更新已有消息文本，删除已发送消息，查询/取消待发送的定时消息。

**输入**: 用户提供消息管理所需的指令和必要参数。
**输出**: 返回消息管理的执行结果,包含操作状态和输出数据。

### 2. 频道治理
列出全部频道，按名称/话题/用途搜索频道，创建公开或私有频道，归档频道（设为只读），重命名频道，设置频道话题与用途，邀请用户加入频道，加入/离开频道，关闭DM会话。

### 3. 对话历史
获取频道主时间线消息（不含线程回复），获取指定线程的全部回复，列出用户可访问的会话。主时间线与线程回复需分别调用不同工具。

### 4. 用户查询
列出工作区全部用户，按姓名/邮箱/条件搜索用户，按邮箱精确查找用户，查询用户在线状态（active/away），查询用户勿扰状态。

### 5. 文件操作
列出工作区内共享文件（支持过滤），向频道上传文件，永久删除文件，下载文件内容并获取公开URL。大文件受Slack限制可能需先上传到文件托管服务。

**输入**: 用户提供文件操作所需的指令和必要参数。
**输出**: 返回文件操作的执行结果,包含操作状态和输出数据。

### 6. 表情反应
向消息添加emoji反应，移除消息上的emoji反应，获取消息上的全部反应列表。

**输入**: 用户提供表情反应所需的指令和必要参数。
**处理**: 按照skill规范执行表情反应操作,遵循单一意图原则。
**输出**: 返回表情反应的执行结果,包含操作状态和输出数据。

### 7. 提醒管理
创建定时提醒，列出全部提醒，查询提醒详情，标记提醒完成，删除提醒。支持自然语言时间（如"明天上午10点"、"每周四下午2点"）。

**输入**: 用户提供提醒管理所需的指令和必要参数。
**处理**: 按照skill规范执行提醒管理操作,遵循单一意图原则。

### 8. 置顶与星标
置顶消息到频道，列出频道置顶项，取消置顶，星标频道/文件/消息，列出星标项，取消星标。

**输入**: 用户提供置顶与星标所需的指令和必要参数。
**处理**: 按照skill规范执行置顶与星标操作,遵循单一意图原则。
**输出**: 返回置顶与星标的执行结果,包含操作状态和输出数据。

### 9. Canvas画布
创建Slack Canvas文档，编辑Canvas内容，永久删除Canvas，查询Canvas章节ID用于定向编辑。

**输入**: 用户提供Canvas画布所需的指令和必要参数。
**处理**: 按照skill规范执行Canvas画布操作,遵循单一意图原则。

### 10. 团队与管理
查询工作区元数据与设置，邀请新用户加入工作区，创建/禁用/启用用户组（子团队），列出用户组，列出企业Grid全部团队，读取企业Grid审计日志。

### 11. 自定义emoji
添加自定义emoji到工作区，列出全部自定义emoji，移除自定义emoji（仅企业Grid）。

**输入**: 用户提供自定义emoji所需的指令和必要参数。
**处理**: 按照skill规范执行自定义emoji操作,遵循单一意图原则。
**输出**: 返回自定义emoji的执行结果,包含操作状态和输出数据。

### 12. 通话管理
查询Slack通话详情，结束进行中的通话，添加/移除通话参与者。

**输入**: 用户提供通话管理所需的指令和必要参数。
**处理**: 按照skill规范执行通话管理操作,遵循单一意图原则。
**输出**: 返回通话管理的执行结果,包含操作状态和输出数据。
## 工具调用规范

### 调用格式
```bash
clawlink_call_tool --tool "工具名" --params '{JSON参数}'
```

### 工具发现
```bash
# 确认Slack已连接
clawlink_list_integrations

# 查看Slack可用工具目录（以返回列表为准）
clawlink_list_tools --integration slack

# 搜索工具
clawlink_search_tools --query "send message" --integration slack

# 查看工具参数说明
clawlink_describe_tool --tool "slack_send_message"
```

### 读写分级安全策略
| 操作类型 | 执行方式 | 示例工具 |
|:---------|:---------|:---------|
| 读操作（list/get/search/find） | 直接执行 | `slack_list_all_channels`、`slack_fetch_conversation_history` |
| 写操作（send/create/update/delete） | 需用户确认后执行 | `slack_send_message`、`slack_create_channel`、`slack_delete_file` |
| 破坏性操作（delete/archive） | 高风险确认 | `slack_delete_file`、`slack_archive_conversation`、`slack_deletes_a_message_from_a_chat` |

**写操作执行前必须**：1) 调 `clawlink_describe_tool` 查看参数；2) 调 `clawlink_preview_tool` 预览效果；3) 用户确认后调 `clawlink_call_tool` 执行。

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|------|---------|---------|---------|
| 项目频道搭建 | 创建#project-alpha频道，邀请5名成员，设置话题 | 频道创建确认+成员邀请结果 | 频道治理+用户查询 |
| 事件响应协作 | 向#incidents发送告警，线程跟进状态，置顶解决结论 | 告警消息+线程回复+置顶确认 | 消息管理+置顶 |
| 文件分发 | 将Q1报告上传到#reports频道 | 文件上传确认+分享链接 | 文件操作 |
| 团队协调 | 创建周三站会提醒，定时发送周报模板 | 提醒创建确认+定时消息确认 | 提醒+定时消息 |

**不适用于**：需要跨工作区操作的场景、Slack Connect外部频道管理、工作区套餐升级与计费管理

## 使用流程

### 确认连接状态
```bash
clawlink_list_integrations
```
返回列表中包含 `slack` 即已连接。若未连接，引导用户访问 ClawLink Dashboard 连接 Slack。

### 工具发现与参数确认
```bash
# 查看工具参数说明（写操作必做）
clawlink_describe_tool --tool "slack_send_message"
```
返回包含 `schema`、`whenToUse`、`askBefore`、`safeDefaults`、`examples` 等指导信息。

### 频道名解析为ID
大部分Slack工具需要频道ID（`C`/`G`/`D` 开头）。频道名需先解析：
```bash
clawlink_call_tool --tool "slack_find_channels" --params '{"name":"general"}'
```

### 写操作预览与确认
```bash
# 预览写操作效果
clawlink_preview_tool --tool "slack_send_message" --params '{"channel":"C0123456789","text":"Hello"}'

# 用户确认后执行
clawlink_call_tool --tool "slack_send_message" --params '{"channel":"C0123456789","text":"Hello"}'
```

### 透传结果
- 原始结构化 JSON 透传，不重命名、不丢弃
- 工具调用失败时报告真实错误，不编造结果

## 案例展示

### 案例1：项目频道搭建
**场景**：新项目启动，需要创建 `#project-alpha` 频道，邀请5名成员，设置话题

**执行**：
```bash
# 创建公开频道
clawlink_call_tool --tool "slack_create_channel" --params '{"name":"project-alpha","is_private":false}'

# 设置频道话题
clawlink_call_tool --tool "slack_set_channel_topic" --params '{"channel":"C0NEW12345","topic":"Project Alpha - 新支付系统"}'

# 按邮箱查找用户并邀请
clawlink_call_tool --tool "slack_find_user_by_email_address" --params '{"email":"alice@company.com"}'
clawlink_call_tool --tool "slack_invite_users_to_a_slack_channel" --params '{"channel":"C0NEW12345","users":"U0ALICE01,U0BOB002,U0CAROL03"}'
```

**输出**：
```json
// create_channel
{"ok": true, "channel": {"id": "C0NEW12345", "name": "project-alpha", "is_channel": true}}

// set_channel_topic
{"ok": true, "channel": {"id": "C0NEW12345", "topic": {"value": "Project Alpha - 新支付系统"}}}

// invite_users
{"ok": true, "channel": {"id": "C0NEW12345", "members": ["U0ALICE01","U0BOB002","U0CAROL03"]}}
```

**分析**：频道 `#project-alpha` 创建成功（ID: `C0NEW12345`），话题已设置，3名成员已邀请加入。写操作（创建/设置话题/邀请）均需用户确认后执行。

### 案例2：事件响应协作
**场景**：生产环境告警，需在 `#incidents` 频道发送告警，线程跟进处理状态，最后置顶解决结论

**执行**：
```bash
# 发送告警消息
clawlink_call_tool --tool "slack_send_message" --params '{
  "channel": "C0INCIDENT1",
  "text": ":rotating_light: *P1告警* 支付服务5xx错误率上升至12%\n影响范围: us-east-1\n开始时间: 14:32 UTC"
}'

# 线程回复处理进展
clawlink_call_tool --tool "slack_send_thread_reply" --params '{
  "channel": "C0INCIDENT1",
  "thread_ts": "1721452800.123456",
  "text": "已定位根因：数据库连接池耗尽。正在扩容连接池，预计5分钟恢复。"
}'

# 置顶解决结论
clawlink_call_tool --tool "slack_pin_item" --params '{
  "channel": "C0INCIDENT1",
  "timestamp": "1721453200.789012"
}'
```

**输出**：
```json
// send_message
{"ok": true, "channel": "C0INCIDENT1", "ts": "1721452800.123456"}

// send_thread_reply
{"ok": true, "channel": "C0INCIDENT1", "ts": "1721453000.456789", "message": {"thread_ts": "1721452800.123456"}}

// pin_item
{"ok": true, "channel": "C0INCIDENT1", "pinned": true}
```

**分析**：告警消息发送后获得时间戳 `1721452800.123456`，用作后续线程回复的 `thread_ts`。线程内跟进不打扰主时间线。解决结论消息被置顶，便于团队快速查看。

### 案例3：文件分发
**场景**：需要将Q1销售报告上传到 `#reports` 频道供团队查阅

**执行**：
```bash
# 上传文件到频道
clawlink_call_tool --tool "slack_upload_file_to_channel" --params '{
  "channel": "C0REPORTS1",
  "content": "Q1,Sales,Revenue\nJan,1200,36000\nFeb,1500,45000\nMar,1800,54000",
  "filename": "q1_sales_report.csv",
  "title": "Q1销售报告"
}'
```

**输出**：
```json
{
  "ok": true,
  "file": {
    "id": "F0FILE1234",
    "name": "q1_sales_report.csv",
    "title": "Q1销售报告",
    "mimetype": "text/csv",
    "size": 78,
    "url_private": "https://files.slack.com/...",
    "shares": {"public": {"C0REPORTS1": [{"ts": "1721453400.000000"}]}}
  }
}
```

**分析**：CSV文件已上传到 `#reports` 频道，文件ID `F0FILE1234` 可用于后续下载或删除。`url_private` 为带认证的下载链接，需授权才能访问。大文件建议先上传到外部托管服务再分享链接。

## 错误处理

| 错误码 | 错误信息 | 原因分析 | 处理方式 |
|:-------|:---------|:---------|:---------|
| `channel_not_found` | 频道ID不存在或Bot不是成员 | 频道ID拼写错误或频道已删除 | 用 `slack_find_channels` 重新解析频道名到ID |
| `user_not_found` | 用户邮箱或ID不匹配任何成员 | 邮箱拼写错误或用户已离开工作区 | 用 `slack_find_users` 模糊搜索确认用户是否存在 |
| `not_authed` | OAuth Token无效或已撤销 | 用户在Dashboard断开了Slack连接 | 引导用户重新连接 Slack |
| `missing_scope` | Token缺少所需权限范围 | 连接时未授权对应Scope | 引导用户在Dashboard重新授权，勾选所需权限 |
| `message_not_found` | 消息时间戳不匹配频道内任何消息 | `thread_ts` 或消息时间戳错误 | 用 `slack_fetch_conversation_history` 获取正确时间戳 |
| `cant_update_message` | 仅消息作者或管理员可编辑 | 尝试编辑他人发送的消息 | 仅编辑Bot自己发送的消息，或请作者手动编辑 |
| `is_archived` | 目标频道已归档（只读） | 向已归档频道发送消息或操作 | 引导用户解除归档或选择活跃频道 |
| `send_as_app` | 消息需要Bot Token发送 | 当前连接方式不支持Bot身份发送 | 引导用户使用Bot Token方式连接Slack |

## 常见问题

### Q1：如何将频道名解析为频道ID？
A：大部分Slack工具需要频道ID（`C`/`G`/`D` 开头）。使用 `slack_find_channels` 按名称搜索，或使用 `slack_list_all_channels` 列出全部频道后按 `name` 字段匹配。DM频道ID以 `D` 开头，MPDM以 `G` 开头，普通频道以 `C` 开头。

### Q2：线程回复与主时间线消息有什么区别？
A：`slack_fetch_conversation_history` 仅返回频道主时间线消息，不包含线程回复。获取线程回复需用 `slack_fetch_message_thread_from_a_conversation` 并传入父消息的 `thread_ts`。发送线程回复需在 `slack_send_thread_reply` 中指定 `thread_ts` 参数。

### Q3：文件上传有什么限制？
A：Slack对文件上传有大小限制（取决于套餐，免费版通常1GB/文件）。大文件建议先上传到外部文件托管服务（如S3、Google Drive），再将分享链接发到频道。上传后文件ID（`F` 开头）可用于下载、删除操作。`url_private` 为带认证链接，需授权才能访问。

### Q4：Token失效后如何重新连接？
A：若Slack工具返回 `not_authed` 错误，说明OAuth Token已失效。引导用户访问 ClawLink Dashboard 重新连接Slack工作区，重新授权后调用 `clawlink_list_integrations` 验证连接已恢复，再调用 `clawlink_list_tools --integration slack` 确认工具目录可用。

### Q5：DM和MPDM的频道ID有什么区别？
A：DM（私信）频道ID以 `D` 开头，仅限两人对话；MPDM（群组私信）频道ID以 `G` 开头，支持多人。两者均通过 `slack_list_conversations` 或 `slack_list_all_channels` 获取。向DM/MPDM发送消息使用与普通频道相同的 `slack_send_message` 工具，`channel` 参数传DM/MPDM的频道ID。

### Q6：如何查看频道历史消息？
A：使用 `slack_fetch_conversation_history` 获取频道主时间线消息，支持分页（`limit`、`cursor` 参数）。如需查看某条消息的线程讨论，先用历史接口找到父消息的 `ts`，再用 `slack_fetch_message_thread_from_a_conversation` 传入 `thread_ts` 获取全部线程回复。

## 已知限制

1. **频道ID必需**：大部分工具需要频道ID而非频道名，需先通过 `slack_find_channels` 解析
2. **速率限制**：列表类操作约1-2次/秒，需遵守 `Retry-After` 头，批量操作建议间隔1秒
3. **线程与主时间线分离**：`slack_fetch_conversation_history` 不含线程回复，需单独调用线程接口
4. **文件大小受限**：大文件上传受Slack套餐限制，建议大文件使用外部托管
5. **企业Grid功能**：审计日志（`slack_read_audit_logs`）、企业团队列表（`slack_list_enterprise_teams`）、emoji删除（`slack_remove_emoji`）仅企业Grid可用
6. **写操作需确认**：所有写操作（发送/创建/删除/更新）必须经用户确认后执行，破坏性操作需高风险确认
7. **工具目录动态变化**：以 `clawlink_list_tools --integration slack` 返回的实时目录为准，不假设工具存在
