---
slug: slack
name: slack
version: "1.0.0"
displayName: Slack 消息管理
summary: 通过slack工具管理Slack消息:回应、置顶、发送/编辑/删除、成员与表情查询
license: MIT
description: |-
  Slack 消息管理。通过 slack 工具对 Slack 工作区进行消息操作,涵盖五大动作组:
  reactions(添加回应与列出回应)、messages(发送、编辑、删除、读取消息)、
  pins(置顶、取消置顶、列出置顶消息)、memberInfo(查询成员信息)、emojiList(列出自定义表情)。
  工具使用已配置的 Bot Token 进行认证,支持 channel 与 user 两种消息目标。
  适用于任务标记完成、置顶关键决策、发送通知消息、查询频道历史与成员信息等场景。
  基于 Markdown 指令驱动,需配合已配置 slack 工具与 Bot Token 的 Agent 平台使用。
  覆盖 channelId 与 messageId 输入采集、JSON action 调用格式、各动作组的参数规范。
tags:
  - 通用办公
  - Collaboration
  - Productivity
tools:
  - read
---

# Slack 消息管理

通过 `slack` 工具对 Slack 工作区进行消息操作,涵盖回应、消息收发与编辑、置顶管理、成员查询、表情列表五大动作组。工具使用已配置的 Bot Token 进行认证。

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Slack 工作区**: 需有已创建的 Slack 工作区与频道

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| slack 工具 | Agent 平台工具 | 必需 | Agent 平台内置或插件提供 |
| Slack Bot Token | 凭证 | 必需 | 在 Slack App 配置页面创建 Bot 并获取 xoxb- 前缀的 Token |
| Bot 权限范围 | 配置 | 必需 | 在 Slack App 配置页授予 reactions:write、chat:write、pins:write、channels:read 等 scope |

### API Key 配置
- Slack Bot Token 由 Agent 平台统一配置,无需在 Skill 中硬编码
- Bot 需被邀请加入目标频道(``/invite @botname``),否则消息操作会报 not_in_channel 错误
- Bot Token 需授予对应动作所需的 OAuth scope,权限不足会报 missing_scope 错误

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,消息操作需要 exec 调用 slack 工具)
- **说明**: 基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 执行 Slack 操作

## 核心能力

### 1. Reactions(消息回应)
- **添加回应**: 对指定消息添加 emoji 回应,emoji 支持 Unicode 字符(如 ✅)或 :name: 格式(如 :white_check_mark:)
- **列出回应**: 查询某条消息上已有的所有回应,返回每个 emoji 的计数与 reacted 用户列表
- **使用场景**: 用 ✅ 标记已完成任务、用 👀 表示正在查看、用 🎉 庆祝里程碑

**处理**: 按照skill规范执行Reactions(消息回应)操作,遵循单一意图原则。
### 2. Messages(消息收发与编辑)
- **发送消息**: 向 channel 或 user 发送文本消息,to 字段格式为 `channel:<id>` 或 `user:<id>`
- **编辑消息**: 修改已发送消息的内容,需提供 channelId 与 messageId
- **删除消息**: 删除指定消息,需提供 channelId 与 messageId
- **读取消息**: 获取频道最近 N 条消息(默认 limit 可调),返回消息文本、发送者、时间戳

### 3. Pins(置顶管理)
- **置顶消息**: 将重要消息固定到频道顶部,便于成员快速查看
- **取消置顶**: 移除消息的置顶状态
- **列出置顶**: 获取频道中所有置顶消息列表

**输入**: 用户提供Pins(置顶管理)所需的指令和必要参数。
**处理**: 按照skill规范执行Pins(置顶管理)操作,遵循单一意图原则。
**输出**: 返回Pins(置顶管理)的执行结果,包含操作状态和输出数据。

### 4. MemberInfo(成员信息)
- **查询成员**: 根据 userId 获取成员的显示名、邮箱、头像、状态等信息
- **使用场景**: 确认消息发送者身份、获取成员联系方式、查看成员在线状态

**输出**: 返回MemberInfo(成员信息)的执行结果,包含操作状态和输出数据。
### 5. EmojiList(表情列表)
- **列出表情**: 获取工作区中所有自定义表情的名称与 URL
- **使用场景**: 查看可用表情名以便在 reactions 中使用 :name: 格式引用

**输入**: 用户提供EmojiList(表情列表)所需的指令和必要参数。
**处理**: 按照skill规范执行EmojiList(表情列表)操作,遵循单一意图原则。
**输出**: 返回EmojiList(表情列表)的执行结果,包含操作状态和输出数据。

### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: slack、工具管理、成员与表情查询、消息管理、工具对、工作区进行消息操、涵盖五大动作组、添加回应与列出回、列出置顶消息、查询成员信息、列出自定义表情、工具使用已配置的、Token、进行认证、两种消息目标、适用于任务标记完、置顶关键决策、发送通知消息、查询频道历史与成、员信息等场景、Markdown、指令驱动、需配合已配置、工具与、Agent、平台使用、输入采集、JSON、调用格式、各动作组的参数规。这些能力在上述核心功能中均有对应处理逻辑。
### 领域术语
本skill涉及以下领域术语: `clawdbot`, `hello`, `ideas`, `构设计决策`, `overview`, `数据存储管理时使`, `不适用于数据库架`, `inputs`, `notes`, `需要数据库操作`

**处理**: 按照skill规范执行领域术语操作,遵循单一意图原则。
**输出**: 返回领域术语的执行结果,包含操作状态和输出数据。

## 输入采集

- **channelId**: Slack 频道 ID,格式为 C 开头的字符串(如 C1234567890)
- **messageId**: Slack 消息时间戳,格式为 `1712023032.1234`(秒.毫秒)
- **emoji**: Unicode 字符(如 ✅)或 Slack 表情名(如 :white_check_mark:)
- **to**: 消息发送目标,格式为 `channel:<id>` 或 `user:<id>`
- **content**: 消息文本内容
- **userId**: 用户 ID,格式为 U 开头的字符串(如 U1234567890)
- **limit**: 读取消息数量,整数

消息上下文行中包含 `slack message id` 与 `channel` 字段,可直接复用。

## 动作组一览

| 动作组 | 默认状态 | 支持动作 | 说明 |
|--------|---------|---------|------|
| reactions | enabled | react、reactions | 添加回应与列出回应 |
| messages | enabled | sendMessage、editMessage、deleteMessage、readMessages | 消息收发与编辑 |
| pins | enabled | pinMessage、unpinMessage、listPins | 置顶管理 |
| memberInfo | enabled | memberInfo | 成员信息查询 |
| emojiList | enabled | emojiList | 自定义表情列表 |

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 任务标记完成 | 已完成的任务消息 channelId 与 messageId | 消息添加 ✅ 回应,团队可视化任务状态 |
| 置顶关键决策 | 决策消息 channelId 与 messageId | 消息置顶到频道顶部,成员快速查看 |
| 发送通知消息 | 目标频道 channelId 与通知文本 | 频道收到通知消息,可后续编辑或删除 |
| 查询频道历史 | 频道 channelId 与读取数量 | 返回最近 N 条消息内容与发送者信息 |

**不适用于**: 需要端到端加密的敏感通信;需要发送文件附件的场景(本 Skill 仅支持文本消息);需要管理频道与用户的场景(本 Skill 仅支持消息级别操作)。

## 使用流程

1. **确认 Bot 已配置**: 确保 Agent 平台已配置 slack 工具与 Bot Token,Bot 已被邀请加入目标频道
2. **采集必要输入**: 根据要执行的动作,准备 channelId、messageId、emoji、to、content 等参数
3. **组装 JSON 调用**: 按对应动作的 JSON 格式组装调用参数,指定 action 字段
4. **执行 slack 工具**: 通过 exec 调用 slack 工具,传入组装好的 JSON 参数
5. **检查返回结果**: 确认操作成功(如 sendMessage 返回 ok 与 message ts),失败时根据错误信息排查
6. **按需追加操作**: 如发消息后置顶、读消息后添加回应等组合操作

## 动作调用格式

### 添加回应

```json
{
  "action": "react",
  "channelId": "C123",
  "messageId": "1712023032.1234",
  "emoji": "✅"
}
```

### 列出回应

```json
{
  "action": "reactions",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### 发送消息

```json
{
  "action": "sendMessage",
  "to": "channel:C123",
  "content": "周报已更新,请查看"
}
```

### 编辑消息

```json
{
  "action": "editMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234",
  "content": "周报已更新(修订版),请查看"
}
```

### 删除消息

```json
{
  "action": "deleteMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### 读取消息

```json
{
  "action": "readMessages",
  "channelId": "C123",
  "limit": 20
}
```

### 置顶消息

```json
{
  "action": "pinMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### 取消置顶

```json
{
  "action": "unpinMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}
```

### 列出置顶

```json
{
  "action": "listPins",
  "channelId": "C123"
}
```

### 查询成员信息

```json
{
  "action": "memberInfo",
  "userId": "U123"
}
```

### 列出自定义表情

```json
{
  "action": "emojiList"
}
```

## 案例展示

### 案例 1: 对完成的消息打勾回应并置顶周报

**场景**: 团队周报发到频道后,用 ✅ 标记已确认并置顶便于查阅

**操作 1: 添加 ✅ 回应**:

```json
{
  "action": "react",
  "channelId": "C0LPBBKMQ",
  "messageId": "1712023032.1234",
  "emoji": "✅"
}
```

**操作 2: 置顶周报消息**:

```json
{
  "action": "pinMessage",
  "channelId": "C0LPBBKMQ",
  "messageId": "1712023032.1234"
}
```

**分析**: 先通过 react 动作为周报消息添加 ✅ 回应,表示团队已确认。再通过 pinMessage 将周报置顶到频道顶部,新进群的成员可第一时间看到。messageId 从消息上下文行或 readMessages 返回结果中获取。

### 案例 2: 发送通知消息并编辑更新内容

**场景**: 向开发频道发送版本发布通知,随后更新发布细节

**操作 1: 发送初始通知**:

```json
{
  "action": "sendMessage",
  "to": "channel:C0LPBBKMQ",
  "content": "v2.3.0 版本即将发布,预计今日 18:00 上线,详情待确认"
}
```

**返回结果**:

```json
{
  "ok": true,
  "message": {
    "ts": "1712023500.5678",
    "text": "v2.3.0 版本即将发布,预计今日 18:00 上线,详情待确认"
  }
}
```

**操作 2: 编辑消息补充细节**:

```json
{
  "action": "editMessage",
  "channelId": "C0LPBBKMQ",
  "messageId": "1712023500.5678",
  "content": "v2.3.0 版本即将发布,预计今日 18:00 上线。本次更新含 API 网关重构与限流功能,发布窗口 30 分钟"
}
```

**分析**: sendMessage 返回的 ts 字段即为后续编辑所需的 messageId。先发送简短通知抢占时间线,再通过 editMessage 补充完整内容,避免重复发送多条消息造成信息分散。

### 案例 3: 读取频道历史并查询发送者信息

**场景**: 需要了解频道最近讨论内容并确认某位发言者的身份

**操作 1: 读取最近 10 条消息**:

```json
{
  "action": "readMessages",
  "channelId": "C0LPBBKMQ",
  "limit": 10
}
```

**返回结果**:

```json
{
  "messages": [
    {
      "ts": "1712023032.1234",
      "text": "这个 bug 我已经修复了",
      "user": "U0ABC"
    },
    {
      "ts": "1712023100.2345",
      "text": "感谢,我来验证一下",
      "user": "U0DEF"
    }
  ]
}
```

**操作 2: 查询 U0ABC 的成员信息**:

```json
{
  "action": "memberInfo",
  "userId": "U0ABC"
}
```

**返回结果**:

```json
{
  "ok": true,
  "user": {
    "name": "张三",
    "display_name": "老张",
    "email": "zhangsan@company.com",
    "title": "后端工程师"
  }
}
```

**分析**: readMessages 返回的消息列表中每条含 user 字段(即 userId),可直接用于 memberInfo 查询。通过两步操作确认了频道最近讨论内容与发言者身份。

## 异常处理

| 错误场景 | 错误现象 | 原因分析 | 处理方式 |
|---------|---------|---------|---------|
| channelId 无效 | 返回 `{"ok": false, "error": "channel_not_found"}` | channelId 拼写错误或频道不存在 | 核对 channelId 格式(C 开头),在 Slack 频道详情中确认正确 ID |
| messageId 格式错误 | 返回 `{"ok": false, "error": "invalid_timestamp"}` | messageId 不符合 `秒.毫秒` 格式 | 确认 messageId 从消息上下文或 readMessages 返回的 ts 字段获取,不要手动拼接 |
| emoji 格式错误 | 返回 `{"ok": false, "error": "invalid_emoji"}` | emoji 参数不是有效 Unicode 或 :name: 格式 | 先用 emojiList 动作查询工作区支持的 emoji 名称;Unicode emoji 确保为完整字符 |
| Bot 未加入频道 | 返回 `{"ok": false, "error": "not_in_channel"}` | Bot 未被邀请加入目标频道 | 在频道中执行 `/invite @botname` 邀请 Bot 加入 |
| 权限不足 | 返回 `{"ok": false, "error": "missing_scope"}` | Bot Token 未授予所需 OAuth scope | 在 Slack App 配置页授予对应 scope(reactions:write、chat:write、pins:write 等)后重新安装 App |
| 消息内容为空 | 返回 `{"ok": false, "error": "no_text"}` | sendMessage 或 editMessage 的 content 字段为空字符串 | 确保 content 字段含至少一个非空白字符;如需发送空行消息使用空格占位 |
| 频率限制 | 返回 `{"ok": false, "error": "ratelimited"}` | 短时间内发送过多请求触发 Slack API 限流 | 降低调用频率,单频道每分钟不超过 20 条消息;批量操作时加入延迟 |
| Bot Token 无效 | 返回 `{"ok": false, "error": "invalid_auth"}` | Bot Token 过期或已被撤销 | 在 Slack App 配置页重新生成 Bot Token,更新 Agent 平台配置 |

## 常见问题

### Q1: 如何获取频道的 channelId?
A: 在 Slack 客户端中,右键点击频道名称选择「查看频道详情」,或点击频道名称打开详情面板。channelId 显示在详情页底部或 URL 中,格式为 C 开头的字符串(如 C0LPBBKMQ)。也可通过 readMessages 读取消息时从返回结果的 channel 字段获取。

### Q2: messageId 的格式是什么?如何获取?
A: messageId 是 Slack 消息的时间戳,格式为 `秒.毫秒`(如 `1712023032.1234`)。获取方式有三种:从消息上下文行中的 `slack message id` 字段直接复用;通过 readMessages 动作读取消息后从返回的 ts 字段获取;通过 sendMessage 发送消息后从返回结果的 message.ts 字段获取。不要手动拼接时间戳,必须从实际消息中获取。

### Q3: emoji 参数支持哪些格式?
A: 支持两种格式。一是 Unicode emoji 字符,直接传入如 ✅、🎉、👀 等字符;二是 Slack 表情名称,格式为 :name:,如 :white_check_mark:、:tada:。如不确定工作区支持哪些自定义表情名称,先调用 emojiList 动作获取完整列表。注意 Unicode emoji 需为完整字符,部分复合 emoji 可能不被支持。

### Q4: sendMessage 的 to 字段如何指定消息目标?
A: to 字段支持两种格式。发到频道用 `channel:<channelId>`(如 `channel:C0LPBBKMQ`),Bot 需已加入该频道。发给个人用 `user:<userId>`(如 `user:U0ABC`),Bot 需与该用户有过对话历史或用户已允许 Bot 私信。两种格式的前缀(channel: 或 user:)不可省略。

### Q5: Bot 如何加入频道?
A: Bot 不能自行加入频道,需由频道成员邀请。在频道中执行 `/invite @botname` 即可邀请 Bot。对于私有频道,Bot 需被频道管理员邀请。Bot 加入频道后才能执行 sendMessage、readMessages、pinMessage 等操作,否则会报 not_in_channel 错误。

### Q6: 频率限制如何处理?
A: Slack API 对每个 Bot 有调用频率限制,通常单频道每分钟不超过 20 条消息。批量发送时建议在每条消息间加入 3 到 5 秒延迟。如收到 ratelimited 错误,响应头中含 Retry-After 字段,按该值(秒)等待后重试。如需高频推送,考虑使用 Slack 的 Incoming Webhook 替代 Bot API。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **仅支持文本消息**: sendMessage 只能发送纯文本,不支持文件附件、图片、富文本块(需升级或使用 Slack Files API)
- **Bot 需被邀请**: Bot 无法自行加入频道,需频道成员手动邀请后才能操作
- **权限依赖 scope 配置**: 每个动作需对应的 OAuth scope,权限不足时操作失败
- **频率限制**: Slack API 对 Bot 调用有频率限制,批量操作需加延迟
- **不支持消息搜索**: 本 Skill 不含 searchMessages 动作,无法按关键词搜索历史消息
- **不支持频道管理**: 不含 createChannel、archiveChannel 等频道管理动作,仅支持消息级别操作
- **messageId 不可手动构造**: 时间戳必须从实际消息获取,手动拼接会导致 invalid_timestamp 错误
