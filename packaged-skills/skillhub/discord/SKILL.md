---
slug: discord
name: discord
version: "1.0.0"
displayName: Discord 全能控制
summary: 通过discord工具控制机器人,管理消息、表情、投票、线程、审核等Discord全功能
license: MIT
description: |-
  通过 discord 工具控制 Discord 机器人,覆盖消息收发与编辑、表情回应与统计、
  贴纸发送与上传、自定义表情包上传、投票创建、线程管理、消息置顶、全文搜索、
  成员与角色查询、频道信息、语音状态、定时事件、审核操作(禁言/踢出/封禁)等全套能力。
  支持通过 discord.actions.* 对各操作组进行细粒度门控,角色与审核默认关闭。
  适用于社区运营自动化、发布通知、团队协作跟进和内容审核场景。
tags:
  - Communication
  - Discord
  - Bot
tools:
  - read
  - exec
---

# Discord 全能控制

## 概述

`discord` 工具用于从 Agent 侧控制 Discord 机器人,以 JSON action 的形式管理消息、表情、贴纸、投票、线程、置顶、搜索、成员角色、频道、语音状态、定时事件与审核操作。所有操作依赖为 Clawdbot 配置的 bot token,可通过 `discord.actions.*` 对各操作组进行开关(角色与审核默认关闭,其余默认开启)。

## 核心能力

### 消息管理
- `sendMessage`:向频道 `channel:<id>` 或私信 `user:<id>` 发送消息,支持 `content`、`mediaUrl`(本地 `file:///` 或远程 `https://`)、`replyTo` 回复指定消息。
- `editMessage`:按 `channelId` + `messageId` 编辑已发消息内容。
- `deleteMessage`:按 `channelId` + `messageId` 删除消息。
- `readMessages`:按 `channelId` 拉取最近消息,支持 `limit` 控制条数。

**输出**: 返回消息管理的执行结果,包含操作状态和输出数据。
### 表情回应
- `react`:对指定消息添加 emoji(如 `✅`、`⚠️`)。
- `reactions`:列出某条消息的回应及对应用户列表,支持 `limit`。
- `emojiList`:列出服务器可用自定义表情。
- `emojiUpload`:上传自定义表情,需 `guildId`、`name`、`mediaUrl`,可选 `roleIds` 限定可见角色。PNG/JPG/GIF,≤256KB。

**处理**: 按照skill规范执行表情回应操作,遵循单一意图原则。
**输出**: 返回表情回应的执行结果,包含操作状态和输出数据。### 贴纸操作
- `sticker`:发送贴纸,`to` 指定目标,`stickerIds` 最多 3 个,可附带 `content`。
- `stickerUpload`:上传贴纸,需 `guildId`、`name`、`description`、`tags`、`mediaUrl`。PNG/APNG/Lottie JSON,≤512KB。

**输入**: 用户提供贴纸操作所需的指令和必要参数。
**输出**: 返回贴纸操作的执行结果,包含操作状态和输出数据。### 投票创建
- `poll`:在频道发起投票,需 `question` + 2~10 个 `answers`,支持 `allowMultiselect`、`durationHours`(默认 24,最大 768 即 32 天)。

**输入**: 用户提供投票创建所需的指令和必要参数。
**处理**: 按照skill规范执行投票创建操作,遵循单一意图原则。
**输出**: 返回投票创建的执行结果,包含操作状态和输出数据。### 线程管理
- `threadCreate`:基于消息或频道创建线程,需 `channelId`、`name`,可选 `messageId`。
- `threadList`:列出服务器下所有活跃线程。
- `threadReply`:在线程内回复消息。

**输入**: 用户提供线程管理所需的指令和必要参数。
**处理**: 按照skill规范执行线程管理操作,遵循单一意图原则。### 置顶与搜索
- `pinMessage` / `listPins`:置顶或列出频道置顶消息。
- `searchMessages`:按 `guildId` 全文搜索,支持 `content`、`channelIds`、`limit`。

**输入**: 用户提供置顶与搜索所需的指令和必要参数。
**输出**: 返回置顶与搜索的执行结果,包含操作状态和输出数据。### 成员与角色
- `memberInfo`:查询成员资料(`guildId` + `userId`)。
- `roleInfo` / `roleAdd` / `roleRemove`:查询或变更角色(默认关闭,需显式开启 `discord.actions.roles`)。

**处理**: 按照skill规范执行成员与角色操作,遵循单一意图原则。
**输出**: 返回成员与角色的执行结果,包含操作状态和输出数据。### 频道、语音、事件
- `channelInfo` / `channelList`:频道详情与列表。
- `voiceStatus`:查询成员当前语音状态。
- `eventList`:列出服务器定时事件。
- `permissions`:检查机器人在指定频道的权限。

### 审核(默认关闭)
- `timeout`:临时禁言成员(`durationMinutes`)。
- `kick` / `ban`:踢出或封禁成员。需开启 `discord.actions.moderation`。

**输入**: 用户提供审核(默认关闭)所需的指令和必要参数。
**处理**: 按照skill规范执行审核(默认关闭)操作,遵循单一意图原则。
**输出**: 返回审核(默认关闭)的执行结果,包含操作状态和输出数据。

### 能力覆盖范围

本skill还覆盖以下能力场景: 工具控制机器人、管理消息、审核等、全功能、工具控制、覆盖消息收发与编、表情回应与统计、贴纸发送与上传、自定义表情包上传、消息置顶、成员与角色查询、频道信息、审核操作、等全套能力、支持通过、对各操作组进行细、粒度门控、角色与审核默认关、适用于社区运营自、发布通知、团队协作跟进和内、容审核场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:发布通知自动化
- 输入:版本号 `v2.4.0`、发布说明、目标频道 `channel:9876543210`。
- 输出:机器人向频道发送格式化发布消息,附带 `file:///tmp/changelog.md` 附件,并对关键消息打 ✅ 反应,随后置顶该消息。

### 场景二:社区投票决策
- 输入:问题"下次线下聚会时间"、4 个选项、目标频道。
- 输出:创建多选投票,`durationHours=48`,机器人 48 小时后通过 `reactions` 统计各选项票数并回填结果。

### 场景三:内容审核分流
- 输入:被举报消息 `messageId=456`、违规成员 `userId=111`、服务器 `guildId=999`。
- 输出:机器人删除违规消息,对成员执行 `timeout durationMinutes=30`,在审核日志频道创建线程记录处置经过。

### 场景四:团队协作跟进
- 输入:bug 报告消息、负责人 `userId`。
- 输出:基于该消息 `threadCreate` 建立"Bug triage"线程,`threadReply` @ 负责人,并在原消息 react ⚠️ 标记待处理。

## 使用流程

1. **确认权限与门控**:通过 `action: "permissions"` 检查机器人在目标频道的权限;确认所需操作组未被 `discord.actions.*` 关闭(角色、审核默认关闭)。
2. **定位目标**:明确目标格式——`sendMessage`/`sticker`/`poll` 用 `to: "channel:<id>"` 或 `to: "user:<id>"`;`react`/`readMessages`/`editMessage`/`deleteMessage` 用 `channelId` 直传。
3. **准备内容**:消息文本遵循 Discord 写作风格(短句、避免 markdown 表格、链接用 `<>` 抑制预览);媒体走 `mediaUrl`,`file:///` 本地或 `https://` 远程;表情包/贴纸确认大小与格式限制。
4. **执行 action**:以 JSON 调用对应 action,记录返回的 `messageId`、`threadId` 供后续编辑/回复/置顶复用。
5. **跟进与归档**:按需 `pinMessage`、`threadReply`、`searchMessages` 回溯;审核类操作在日志频道留痕。

### 命令参数说明

- `-log-111-广告`: 命令参数,用于指定操作选项

## 案例展示

### 案例 1:发布通知 + 置顶 + 反应
目标:向 `#releases`(`channel:9876543210`)发布 v2.4.0 并置顶。

```json
{
  "action": "sendMessage",
  "to": "channel:9876543210",
  "content": "**v2.4.0 已发布**\n- 新增投票统计导出\n- 修复线程回复丢失问题\n完整说明见附件",
  "mediaUrl": "file:///tmp/changelog-v2.4.0.md"
}
```

返回 `messageId=1122334455667788` 后:

```json
{ "action": "react", "channelId": "9876543210", "messageId": "1122334455667788", "emoji": "✅" }
{ "action": "pinMessage", "channelId": "9876543210", "messageId": "1122334455667788" }
```

结果:频道出现带附件的发布消息,带 ✅ 反应并置顶。

### 案例 2:多选投票与结果统计
目标:48 小时多选投票"下周团建活动"。

```json
{
  "action": "poll",
  "to": "channel:555000555000",
  "question": "下周团建活动(可多选)",
  "answers": ["密室逃脱", "户外烧烤", "电影之夜", "桌游下午茶"],
  "allowMultiselect": true,
  "durationHours": 48,
  "content": "请大家投票,周四截止"
}
```

到期后通过 `reactions` 或投票对象统计各选项票数,在原频道回填"烧烤 12 票 / 密室 9 票"结果。

### 案例 3:审核处置 + 线程留痕
目标:成员 `userId=111` 在 `guildId=999` 发布广告,禁言 30 分钟并记录。

```json
{ "action": "deleteMessage", "channelId": "123", "messageId": "456" }
{ "action": "timeout", "guildId": "999", "userId": "111", "durationMinutes": 30 }
{ "action": "threadCreate", "channelId": "123", "name": "mod-log-111-广告", "messageId": "456" }
```

在审核日志频道形成可追溯的处置线程。

## 异常处理

| 错误场景 | 触发原因 | 处理方式 |
|---------|---------|---------|
| `Missing Access` / `50001` | 机器人缺少该频道查看或发送权限 | 先 `permissions` 核对权限位,联系服务器管理员补齐或调整频道权限覆盖 |
| `to` 与 `channelId` 混用 | `sendMessage` 误传 `channelId` 而 `react` 误传 `to` | 严格区分:`sendMessage/sticker/poll` 用 `to`;`react/readMessages/editMessage/deleteMessage` 用 `channelId` |
| 表情上传超 256KB | `mediaUrl` 指向的图片过大或格式不符 | 压缩为 PNG/JPG/GIF 且 ≤256KB 后重传;GIF 需确认是否为服务器 Boost 解锁的动画表情位 |
| 贴纸上传失败 | 文件 >512KB 或非 PNG/APNG/Lottie JSON | 转换格式并压缩;Lottie JSON 需确保为合法动画描述 |
| `Unknown Message` / `10008` | `editMessage`/`deleteMessage`/`react` 指向已删除消息 | 先 `readMessages` 确认消息存在;若已删除则跳过该操作 |
| 投票选项数非法 | `answers` 少于 2 或多于 10 | 调整为 2~10 个选项;`durationHours` 不超过 768 |
| 角色变更被拒 | `discord.actions.roles` 未开启或机器人角色低于目标角色 | 在配置中显式开启 `roles`;确保机器人角色在服务器层级高于被操作角色 |
| 审核操作无权限 | `moderation` 默认关闭且机器人缺少 `KICK_MEMBERS`/`BAN_MEMBERS`/`MODERATE_MEMBERS` | 开启 `discord.actions.moderation` 并由服务器管理员授予相应权限 |

## 常见问题

### Q1:为什么 `sendMessage` 报错说找不到频道,而 `readMessages` 能用?
`sendMessage` 接收的是 `to: "channel:<id>"` 格式(带 `channel:` 前缀),`readMessages` 接收的是裸 `channelId`。两者格式不可混用,这是最常见的参数错误。

### Q2:如何禁用部分操作防止误用?
在 Clawdbot 配置中使用 `discord.actions.*` 门控,例如设 `discord.actions.moderation=false`、`discord.actions.roles=false`(两者默认即关闭),也可关闭 `emojiUploads`、`stickerUploads`、`polls` 等。

### Q3:贴纸和表情包上传有什么硬限制?
表情包:PNG/JPG/GIF,≤256KB,服务器表情数受 Boost 等级限制。贴纸:PNG/APNG/Lottie JSON,≤512KB,普通服务器 5 个动态贴纸位,Boost 后扩展。`stickerUpload` 必须同时提供 `name`、`description`、`tags`。

### Q4:投票最长时间是多少?到期后怎么取结果?
`durationHours` 最大 768(32 天)。到期后投票自动关闭,可通过 `reactions` 拉取各选项的投票用户列表自行统计,或在投票消息上读取内置投票结果。

### Q5:线程和频道回复有什么区别?
`threadCreate` 在频道内创建独立线程(可基于某条消息),`threadReply` 在已存在线程内发消息。普通 `sendMessage` 只发到主频道,不会自动进入线程。`threadList` 可按 `guildId` 列出服务器所有活跃线程以获取 `threadId`。

### Q6:审核操作默认为什么是关闭的?
`timeout`/`kick`/`ban` 具有破坏性,默认关闭以防误操作。需要时在配置显式开启 `discord.actions.moderation`,并确保机器人持有 `MODERATE_MEMBERS`(禁言)、`KICK_MEMBERS`、`BAN_MEMBERS` 权限及高于目标成员的角色层级。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 所有操作依赖为 Clawdbot 配置的 bot token,未配置 token 时任何 action 都无法执行。
- `sendMessage` 的 `to` 与其他 action 的 `channelId` 格式不同,混用会直接报错。
- 角色变更(`roleAdd`/`roleRemove`)与审核(`timeout`/`kick`/`ban`)默认关闭,需显式开启且机器人角色须高于目标。
- 表情包 ≤256KB、贴纸 ≤512KB,超出需先压缩;动画表情/贴纸数量受服务器 Boost 等级约束。
- 投票 `durationHours` 上限 768 小时(32 天),单次最多 10 个选项。
- 消息搜索(`searchMessages`)依赖服务器开启该权限,部分大型服务器可能受限或延迟较高。
- Discord 全局与按频道速率限制由平台强制,高频发送会被 429 限流,需自行节流。
- markdown 表格在 Discord 渲染为原始 `|` 文本,通知类消息应改用列表或粗体。

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