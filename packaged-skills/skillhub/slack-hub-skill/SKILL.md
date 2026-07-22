---
slug: "slack-hub-skill"
name: "slack-hub-skill"
version: "1.0.0"
displayName: "Slack消息中枢"
summary: "Slack消息发送/线程回复/工作区搜索/频道发现，Bot Token直连Web API"
license: "Proprietary"
description: |-
  面向团队协作场景的Slack消息与搜索集成技能。通过Slack Bot Token直连Slack Web API，
  提供频道与用户消息发送、线程回复、工作区内容搜索、公共频道列表四大能力。
  支持频道名与频道ID双向寻址、用户ID提及、Slack消息格式化（粗体/斜体/代码块/引用）、
  线程化讨论路由、工作区历史消息与文件检索。
  适用于发布部署通知、路由讨论到线程、检索过往决策与文档、发现团队频道等场景。
  内置速率限制感知与指数退避重试，支持高活跃工作区下的稳定消息投递。
tags:
  - Communication
  - 团队协作
  - 消息API
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# Slack消息中枢（Slack Hub Skill）

面向团队协作场景的Slack消息与搜索集成。通过Bot Token直连Slack Web API，提供消息投递、线程回复、工作区搜索、频道发现四大能力。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 消息发送与线程回复
向指定频道或用户发送文本消息，支持以 `thread_ts` 参数回复指定消息的线程。频道参数接受频道ID（`C0123456789`）或频道名（`#general`）；用户消息需使用用户ID或DM频道ID。支持Slack消息格式化语法：`*bold*`、`_italic_`、`~strike~`、`` `code` ``、` ```code block``` `、`>quote`。

**输出**: 返回消息发送与线程回复的执行结果,包含操作状态和输出数据。
### 2. 工作区内容搜索
按关键词检索工作区内的消息和文件。搜索范围包括所有可访问的公共频道及Bot已加入的私有频道。支持Slack搜索修饰符：`from:@user`、`in:#channel`、`has:link`、`has:file`、`before:YYYY-MM-DD`、`after:YYYY-MM-DD`。搜索结果包含匹配片段、来源频道、作者、时间戳与永久链接。- 验证执行结果，确认输出符合预期格式
- 参考`工作区内容搜索`相关配置参数进行设置
### 3. 公共频道发现
列出工作区内所有公共频道，返回频道ID、名称、成员数、话题、用途、创建时间。支持分页遍历大型工作区。可用于频道发现、ID解析、成员统计。- 验证执行结果，确认输出符合预期格式
- 参考`公共频道发现`相关配置参数进行设置
### 4. 速率限制感知
Slack Web API 对不同端点有独立速率限制：`chat.postMessage` 约1次/秒/频道，`search.messages` 约20次/分钟，`conversations.list` 约20次/分钟。本技能在收到 `429 rate_limited` 响应时读取 `Retry-After` 头并指数退避重试，最多3次。

**输入**: 用户提供速率限制感知所需的指令和必要参数。
**处理**: 按照skill规范执行速率限制感知操作,遵循单一意图原则。
**输出**: 返回速率限制感知的执行结果,包含操作状态和输出数据。

#
## 频道与用户寻址

### 频道寻址
| 输入格式 | 说明 | 示例 |
|:---------|:-----|:-----|
| 频道ID | 以 `C` 开头的9位字符串 | `C0123456789` |
| 频道名 | 以 `#` 开头或纯名称 | `#general` 或 `general` |

频道名解析：`#general` 会先调 `conversations.list` 匹配 `name` 字段获取 `id`，再发送消息。

### 用户寻址
| 输入格式 | 说明 | 示例 |
|:---------|:-----|:-----|
| 用户ID | 以 `U` 开头的9位字符串 | `U0123456789` |
| DM频道ID | 以 `D` 开头的9位字符串 | `D0123456789` |

消息中提及用户使用 `<@U0123456789>` 语法，提及频道使用 `<#C0123456789>` 语法。

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|------|---------|---------|---------|
| 部署通知发布 | 向#deployments频道发送v2.1.0上线通知 | 消息投递确认+时间戳 | 消息发送 |
| 讨论路由到线程 | 回复#general里关于API变更的消息，说周三评审 | 线程回复确认 | 线程回复 |
| 工作区知识检索 | 搜索工作区里关于数据库迁移方案的讨论 | 匹配消息列表+来源频道+作者 | 工作区搜索 |
| 频道发现与解析 | 列出所有公共频道并找到#dev-team的ID | 频道列表+目标频道ID | 频道发现 |

**不适用于**：频道创建/归档/重命名、文件上传、定时消息、用户管理、表情反应（需使用 slack-workspace 技能）

## 使用流程

### 检查 Bot Token（永不打印值）
```bash
[ -n "${SLACK_BOT_TOKEN:-}" ] && echo ok || echo missing
```

### 缺失时引导配置
> 需要先配置 Slack Bot Token：
> 1. 访问 https://api.slack.com/apps 创建新App
> 2. 配置 Bot Token Scopes：`chat:write`、`search:read`、`channels:read`
> 3. 安装App到工作区，获取 `xoxb-` 开头的Bot Token
> 4. 终端环境变量：`export SLACK_BOT_TOKEN="xoxb-你的Token"`
> 5. 将Bot邀请到目标频道（`/invite @botname`）

**安全红线**：永不接受/回显/存储来自聊天输入的Token；Token仅作为 `Authorization: Bearer` 请求头使用。

### 解析目标地址
频道名需先调 `conversations.list` 解析为频道ID。用户DM需先调 `conversations.list` 过滤 `is_im: true` 的频道。

### 执行操作
1. 发送消息：`POST chat.postMessage`，传 `channel`、`text`、可选 `thread_ts`
2. 搜索内容：`GET search.messages`，传 `query`、可选 `count`、`page`
3. 列出频道：`GET conversations.list`，传 `types=public_channel`

### 透传结果
4. 原始结构化 JSON 透传，不重命名、不丢弃
5. 发送成功返回 `{ok: true, channel, ts, message}`
6. 搜索返回 `{ok: true, messages: {matches, total, paging}}`

#
## 案例展示

### 案例1：部署通知发布
**场景**：工程团队需要在 `#deployments` 频道发布 v2.1.0 上线通知

**执行**：
```bash
# 解析频道名到ID（首次需要）
curl -s "https://slack.com/api/conversations.list?types=public_channel&limit=200" \
  -H "Authorization: Bearer ${SLACK_BOT_TOKEN}" | jq '.channels[] | select(.name=="deployments") | .id'

# 发送部署通知
curl -s -X POST "https://slack.com/api/chat.postMessage" \
  -H "Authorization: Bearer ${SLACK_BOT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "channel": "C0123456789",
    "text": ":rocket: *部署完成* v2.1.0 已上线\n• 服务: payment-api\n• 区域: us-east-1\n• 提交: a1b2c3d\n• 耗时: 2m30s"
  }'
```

**输出**：
```json
{
  "ok": true,
  "channel": "C0123456789",
  "ts": "1721452800.123456",
  "message": {
    "text": ":rocket: *部署完成* v2.1.0 已上线\n• 服务: payment-api\n• 区域: us-east-1\n• 提交: a1b2c3d\n• 耗时: 2m30s",
    "type": "message",
    "user": "U0BOT1234"
  }
}
```

**分析**：消息成功投递到 `#deployments` 频道，时间戳 `1721452800.123456` 可用于后续线程回复或消息更新。Slack格式化语法 `:rocket:` 会被渲染为emoji，`*部署完成*` 渲染为粗体。

### 案例2：工作区知识检索
**场景**：新成员需要检索工作区内关于数据库迁移方案的过往讨论

**执行**：
```bash
# 搜索工作区消息，限定在#eng-platform频道
curl -s "https://slack.com/api/search.messages?query=migration%20in%3A%23eng-platform&count=5&page=1" \
  -H "Authorization: Bearer ${SLACK_BOT_TOKEN}"
```

**输出**：
```json
{
  "ok": true,
  "messages": {
    "matches": [
      {
        "iid": "msg-001",
        "text": "我们决定用pg-verify做增量迁移，回滚方案见附件",
        "channel": {"id": "C0123456789", "name": "eng-platform"},
        "user": "U0123456789",
        "username": "alice",
        "ts": "1721200000.000000",
        "permalink": "https://workspace.slack.com/archives/C0123456789/p1721200000000000"
      }
    ],
    "total": 3,
    "paging": {"page": 1, "pages": 1, "count": 5, "total": 3}
  }
}
```

**分析**：共匹配 3 条消息，当前返回全部（不足5条）。alice 在 `#eng-platform` 频道提到使用 pg-verify 做增量迁移，可通过 `permalink` 跳转查看完整上下文。搜索修饰符 `in:#eng-platform` 将范围限定到指定频道。

### 案例3：讨论路由到线程
**场景**：在 `#general` 频道找到关于API变更的消息，将评审安排回复到该消息的线程中

**执行**：
```bash
# 第一步：搜索找到目标消息的ts
curl -s "https://slack.com/api/search.messages?query=API%20change%20in%3A%23general&count=1" \
  -H "Authorization: Bearer ${SLACK_BOT_TOKEN}"

# 第二步：用thread_ts回复该消息的线程
curl -s -X POST "https://slack.com/api/chat.postMessage" \
  -H "Authorization: Bearer ${SLACK_BOT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "channel": "C0GENERAL01",
    "thread_ts": "1721400000.000000",
    "text": "已安排周三下午2点评审API变更方案，议程：1) 变更范围 2) 兼容性影响 3) 迁移路径"
  }'
```

**输出**：
```json
{
  "ok": true,
  "channel": "C0GENERAL01",
  "ts": "1721453000.123456",
  "message": {
    "text": "已安排周三下午2点评审API变更方案...",
    "thread_ts": "1721400000.000000"
  }
}
```

**分析**：回复成功投递到原消息的线程中，`thread_ts` 指向父消息时间戳，`ts` 是本次回复的时间戳。线程内参与者将收到通知，主时间线不会被打扰。

## 错误处理


| 错误码 | 错误信息 | 原因分析 | 处理方式 |
|:-------|:---------|:---------|:---------|
| `invalid_auth` | `{ok:false, error:"invalid_auth"}` | Token无效/过期/格式错误 | 不执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，引导用户检查 `SLACK_BOT_TOKEN` 是否以 `xoxb-` 开头 |
| `channel_not_found` | `{ok:false, error:"channel_not_found"}` | 频道ID不存在或Bot不是成员 | 引导用户用 `/invite @botname` 将Bot加入频道 |
| `not_in_channel` | `{ok:false, error:"not_in_channel"}` | Bot未加入目标频道 | 同上，需先将Bot邀请到频道 |
| `rate_limited` | HTTP 429 + `Retry-After` 头 | 触发速率限制 | 读取 `Retry-After` 值，等待后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，最多3次指数退避 |
| `missing_scope` | `{ok:false, error:"missing_scope"}` | Token缺少所需权限 | 引导用户在App配置中添加对应Scope（`chat:write`/`search:read`/`channels:read`） |
| `no_text` | `{ok:false, error:"no_text"}` | 消息内容为空或仅含空格 | 检查 `text` 参数非空，至少包含一个可见字符 |
| `search_disabled` | `{ok:false, error:"search_disabled"}` | 工作区未启用搜索或套餐不支持 | 引导用户检查工作区套餐，搜索功能需Standard及以上 |
| `is_archived` | `{ok:false, error:"is_archived"}` | 目标频道已归档（只读） | 引导用户选择活跃频道或解除归档 |

## 常见问题

### Q1：如何获取Slack Bot Token？
A：访问 https://api.slack.com/apps 创建新App，在 **OAuth & Permissions** 页面配置 Bot Token Scopes（至少 `chat:write`、`channels:read`；搜索需加 `search:read`），然后安装App到工作区，复制 `xoxb-` 开头的 Bot User OAuth Token。注意将Bot邀请到目标频道后才能发送消息。

### Q2：如何在消息中提及用户或频道？
A：提及用户使用 `<@U0123456789>` 格式（需用户ID），提及频道使用 `<#C0123456789>` 格式（需频道ID）。纯文本 `@username` 不会产生实际提及通知。用户ID可通过 `users.list` API获取，频道ID可通过 `conversations.list` 获取。

### Q3：搜索为什么返回空结果？
A：可能原因：1) 搜索词拼写错误；2) Bot缺少 `search:read` 权限；3) 工作区套餐不支持搜索（需Standard及以上）；4) 搜索范围受限，Bot只能搜索公共频道和已加入的私有频道。建议先用简单关键词测试，确认返回 `ok: true` 且 `total: 0` 表示搜索成功但无匹配。

### Q4：如何处理速率限制？
A：Slack对 `chat.postMessage` 限制约1次/秒/频道，`search.messages` 约20次/分钟。收到 HTTP 429 时读取 `Retry-After` 头的秒数，等待后重试。批量发送时建议每条间隔1秒，或使用频道级队列。本技能内置3次指数退避重试（1s/2s/4s）。

### Q5：能否发送DM（私信）？
A：可以。需先通过 `conversations.list` 过滤 `is_im: true` 的频道获取DM频道ID（以 `D` 开头），然后向该DM频道ID发送消息。Bot需有 `im:write` 和 `im:read` 权限。注意DM仅限Bot与单个用户之间的对话。

### Q6：如何格式化消息内容？
A：Slack支持 `*bold*`（粗体）、`_italic_`（斜体）、`~strike~`（删除线）、`` `code` ``（行内代码）、` ```code block``` `（代码块）、`>quote`（引用）、`---`（分隔线）。emoji使用 `:name:` 语法，如 `:rocket:`、`:white_check_mark:`。链接使用 `<https://example.com|显示文本>` 格式。

## 已知限制

1. **仅支持公共频道列表**：`conversations.list` 默认仅返回公共频道，私有频道需Bot已被邀请并指定 `types=private_channel`
2. **搜索范围受限**：Bot只能搜索公共频道和已加入的私有频道，无法搜索未加入的私有频道
3. **无文件上传能力**：本技能仅支持消息发送与搜索，文件上传需使用 slack-workspace 技能
4. **速率限制严格**：高活跃工作区下 `search.messages` 的20次/分钟限制可能影响批量检索，需配合分页与缓存
5. **频道名解析额外消耗**：使用频道名（如 `#general`）需额外调 `conversations.list` 解析，大型工作区可能需多次分页
6. **无定时消息**：不支持消息定时发送，需Agent层自行调度或使用 slack-workspace 技能的 `slack_schedule_message`
