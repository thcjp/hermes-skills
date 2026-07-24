---

slug: "discord-chat"
name: "discord-chat"
version: 1.0.1
displayName: "Discord Chat"
summary: "通过message工具在Discord频道发消息、回复、搜索、读取、回应、编辑与删除。discord-chat 通过 message 工具与 Discord 频道交互,覆盖消息发送、线程回复"
license: "Proprietary"
description: |-，可自动提升工作效率
  discord-chat 通过 message 工具与 Discord 频道交互,覆盖消息发送、线程回复、
  全文搜索、历史读取、表情回应、消息编辑与删除、频道列表与详情查询.
  支持频道名(#name)或频道 ID 作为目标,支持回复指定消息、按作者/时间分页搜索、
  消息特效(balloons/invisible-ink)等。适用于社区答疑、内容检索、
  通知广播与频道管理自动化场景.
tags:
  - Communication
  - Discord
  - Chat
  - 社交
  - 通信
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Communication"

---

# Discord Chat

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Discord Chat处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 概述

`discord-chat` 通过 Clawdbot 的 `message` 工具与 Discord 频道交互。指定 `channel=discord` 后,工具自动路由到已配置的 Discord 插件。支持以频道名(`#name`)或频道 ID 作为 `target`,覆盖发送、回复、搜索、读取、回应、编辑、删除及频道管理操作.
## 核心能力

### 消息发送
```bash
message action=send channel=discord target="#channel-name" message="你的消息"
message action=send channel=discord target="1234567890" message="按 ID 发送"
```
- `target` 支持带 `#` 前缀的频道名或裸频道 ID.
- 多链接用 `<>` 包裹抑制预览:`<https://example.com>`.
- 支持消息特效:`effect=balloons`、`effectId=invisible-ink`.
- 不支持 markdown 表格,改用项目符号列表.
**输入**: 用户提供消息发送所需的指令和必要参数.
**输出**: 返回消息发送的处理结果,包含执行状态码、结果数据和执行日志。### 线程回复
```bash
message action=send channel=discord target="#channel-name" message="回复内容" replyTo="message-id"
```
- `replyTo` 以指定消息 ID 创建线程式回复.
**输入**: 用户提供线程回复所需的指令和必要参数.
**处理**: 解析线程回复的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 全文搜索
```bash
message action=search channel=discord channelId="1234567890" query="搜索词" limit=50
```
- `query`:搜索关键词.
- `authorId`:按作者过滤.
- `before`/`after`/`around`:以消息 ID 分页.
- `limit`:最大返回数,默认 25.
### 历史读取
```bash
message action=read channel=discord target="#channel-name" limit=20
```

**输入**: 用户提供历史读取所需的指令和必要参数.
**处理**: 解析历史读取的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回历史读取的处理结果,包含执行状态码、结果数据和执行日志。### 表情回应
```bash
message action=react channel=discord messageId="1234567890" emoji="👍"
```

**输入**: 用户提供表情回应所需的指令和必要参数.
**处理**: 解析表情回应的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回表情回应的处理结果,包含执行状态码、结果数据和执行日志。### 消息编辑与删除
```bash
message action=edit channel=discord messageId="1234567890" message="更新后的文本"
message action=delete channel=discord messageId="1234567890"
```

**输入**: 用户提供消息编辑与删除所需的指令和必要参数.
**处理**: 解析消息编辑与删除的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回消息编辑与删除的处理结果,包含执行状态码、结果数据和执行日志。### 频道管理
```bash
message action=channel-list channel=discord guildId="server-id"
message action=channel-info channel=discord channelId="1234567890"
```

**输入**: 用户提供频道管理所需的指令和必要参数.
**处理**: 解析频道管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回频道管理的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:社区答疑机器人
- 输入:用户提问"如何配置 webhook",频道 `#support`.
- 输出:机器人 `action=search` 检索历史中已有答案,`action=send replyTo` 回复提问消息并附上历史解答链接.
### 场景二:通知广播
- 输入:公告文本"今晚 20:00 维护",频道 `#announcements`.
- 输出:`action=send target="#announcements"` 发送公告,`action=react emoji="📌"` 标记,并通过 `channel-list` 同步到子公告频道.
### 场景三:历史内容检索归档
- 输入:服务器 `guildId`、关键词"release notes"、时间范围.
- 输出:跨频道 `action=search` 分页拉取匹配消息,提取作者、时间、内容写入本地归档文件.
## 使用流程

1. **确认配置**:Discord bot 已在 gateway config 中配置,`channel=discord` 能正确路由到 Discord 插件.
2. **定位目标频道**:优先用 `target="#频道名"`(更可读);频道名含特殊字符或需精确控制时用频道 ID。可用 `channel-list` 查询服务器频道清单.
3. **检索先行**:答疑或归档场景先 `action=search` 查历史,避免重复提问;读取近况用 `action=read limit=N`.
4. **发送与回复**:`action=send` 发新消息;需关联某条消息用 `replyTo`;纯确认用 `action=react` 优于回复.
5. **维护消息**:对已发消息用 `action=edit` 修正内容,过期信息用 `action=delete` 清理.
6. **格式适配**:Discord 用项目符号而非表格,链接用 `<>` 抑制预览,短句优于长段落.
#
## 案例展示

### 案例 1:搜索历史并回复
目标:用户在 `#support` 问"webhook 怎么配",检索历史答案并回复.
```bash
message action=search channel=discord channelId="1234567890" query="webhook 配置" limit=10
```

找到历史解答消息 ID `9988776655`,向提问用户回复:

```bash
message action=send channel=discord target="#support" message="webhook 配置见 <https://docs.example.com/webhook>,之前也有讨论" replyTo="1122334455"
```

结果:提问消息下出现线程式回复,附带文档链接与历史讨论引用.
### 案例 2:多频道通知广播
目标:向 `#announcements` 和 `#general` 同步维护通知.
```bash
message action=send channel=discord target="#announcements" message="**今晚 20:00-22:00 维护**,期间服务暂停"
```

返回消息 ID `4455667788` 后标记:

```bash
message action=react channel=discord messageId="4455667788" emoji="📌"
message action=send channel=discord target="#general" message="维护通知已发 #announcements,请提前知悉"
```

结果:主公告频道发布并置顶标记,通用频道同步提醒.
### 案例 3:按作者分页检索归档
目标:检索 `#dev-log` 中作者 `userId=444` 在某消息之后的所有发布,每页 50 条.
```bash
message action=search channel=discord channelId="555000555000" authorId="444" after="777888999000" limit=50
```

翻页时将上一页最后一条消息 ID 作为新的 `after` 值继续检索,直至返回为空,提取内容写入 `file:///tmp/dev-log-archive.md`.
## 异常处理

| 错误场景 | 触发原因 | 处理方式 |
|---:|---:|---:|
| 频道名找不到 | `target="#name"` 拼写错误或机器人不在该服务器 | 用 `channel-list guildId` 核对频道名;确认机器人已加入目标服务器 |
| `replyTo` 无效 | 指定的 message-id 不存在或已删除 | 先 `action=read` 确认消息存在;私信消息无法跨频道回复 |
| 搜索无结果 | `query` 过于具体或该频道未开启搜索权限 | 放宽关键词;改用 `authorId` 或 `before/after` 分页缩小范围;确认服务器搜索权限 |
| `editMessage` 失败 | 目标消息非机器人发送,或超过编辑时限 | Discord 仅允许编辑自己发送的消息;超时后改用 `action=send` 补发更正 |
| 删除被拒 | 机器人缺少 `MANAGE_MESSAGES` 权限或目标非自己发送 | 由服务器管理员授予 `MANAGE_MESSAGES`;非自身消息需相应权限 |
| 特效无效 | `effect=balloons` 在非支持频道或未开通 | 消息特效仅部分频道/服务器可用,改用纯文本发送 |
| 搜索分页丢失 | 未用上一页最后消息 ID 作为 `after` | 严格链式分页:每次取末条 ID 作为下次 `after`,不可跳跃 |
| 频道 ID 与名称混用导致歧义 | `target` 同时含 `#` 与纯数字 | 统一规范:用名称带 `#`,用 ID 则纯数字不带 `#` |

## 常见问题

### Q1:`target` 用频道名和频道 ID 有什么区别?
频道名带 `#` 前缀(如 `#general`)更可读,适合常用频道;频道 ID(纯数字)更精确,适合频道名含特殊字符或存在重名的场景。两者效果一致,推荐日常用名称、自动化脚本用 ID.
### Q2:`replyTo` 和普通 `send` 有什么区别?
普通 `action=send` 在频道发一条独立消息;带 `replyTo="消息ID"` 会以线程回复的形式挂在指定消息下方,适合答疑和上下文关联。注意 `replyTo` 的消息必须与 `target` 在同一频道.
### Q3:搜索支持哪些过滤条件?
`query`(关键词)、`authorId`(按作者)、`before`/`after`/`around`(以消息 ID 分页)、`limit`(最大返回数,默认 25)。可组合使用,例如按作者 + 时间范围精确检索.
### Q4:为什么我的消息里表格显示成一堆竖线?
Discord 不渲染 markdown 表格,会把 `| 列 | 列 |` 原样显示。应改用项目符号列表(`- 项目`)或粗体分组来呈现结构化信息.
### Q5:消息特效 `effect=balloons` 在所有频道都能用吗?
不能。消息特效受服务器 Boost 等级和频道设置约束,部分服务器未开通。特效失效时不会报错但无视觉效果,建议关键通知仍以文本为主.
### Q6:如何批量清理某频道的旧消息?
`message` 工具不提供批量删除接口。可循环 `action=search` 取目标消息 ID 列表,逐条 `action=delete` 执行,注意 Discord 速率限制(约每频道每秒限若干次).
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 所有操作依赖 gateway config 中配置的 Discord bot token,未配置时 `channel=discord` 无法路由.
- `action=edit` 仅能编辑机器人自己发送的消息,他人消息无法编辑.
- `action=delete` 删除他人消息需 `MANAGE_MESSAGES` 权限,否则只能删自己的.
- 消息特效(`effect`/`effectId`)受服务器 Boost 等级约束,并非所有频道可用.
- 搜索(`action=search`)依赖服务器开启搜索权限,大型服务器可能延迟较高.
- `limit` 默认 25,搜索与读取均有上限,大量历史需通过 `before`/`after` 链式分页.
- markdown 表格不被渲染,结构化内容应改用列表.
- 受 Discord 全局与按频道速率限制,高频操作会被 429 限流,需自行节流.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.