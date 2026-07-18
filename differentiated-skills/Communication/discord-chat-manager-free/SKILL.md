---
slug: discord-chat-manager-free
name: discord-chat-manager-free
version: "1.0.0"
displayName: Discord聊天管理免费版
summary: 基础 Discord 聊天管理工具,支持消息发送、回复、搜索与读取,适合个人日常使用。
license: MIT
edition: free
description: |-
  面向个人用户的 Discord 频道聊天管理工具。

  核心能力:
  - 向频道发送消息并支持回复指定消息
  - 读取频道最近消息与按关键词搜索历史
  - 对消息添加表情反应与基础编辑删除
  - 查询频道列表与频道基础信息

  适用场景:
  - 个人 Discord 服务器的日常聊天互动
  - 小型团队的快速通知与状态更新
  - 个人机器人的消息检索与回复

  差异化: 免费版聚焦高频聊天操作,命令简洁即用;Pro 版提供高级搜索、批量消息与频道管理能力。

  触发关键词: discord, 聊天, 消息, 回复, 搜索, 读取, message, send, reply, search, read, react
tags:
- Discord
- 聊天管理
- Communication
- 消息搜索
tools:
- read
- exec
---

# Discord 聊天管理(免费版)

## 概述

Discord 聊天管理免费版是一款面向个人用户的 Discord 频道聊天管理工具。它通过统一的 `message` 工具调用,覆盖日常聊天最高频的操作:发送消息、回复消息、读取最近消息、按关键词搜索历史消息,以及对消息添加表情反应和基础编辑删除。免费版命令简洁,零额外配置即可上手。

免费版适合个人 Discord 服务器、小型团队和独立开发者的日常聊天互动。如果你需要高级搜索模式(按作者/时间范围/多条件组合)、批量消息分发和频道创建编辑能力,请升级至 Pro 版。

## 核心能力

| 能力模块 | 说明 | 免费版支持 |
|:-------|:-----|:----------|
| 发送消息 | 发送文本到频道 | 支持(单条) |
| 回复消息 | 回复指定消息 ID | 支持 |
| 读取消息 | 读取频道最近消息 | 支持 |
| 搜索消息 | 按关键词搜索 | 支持(基础) |
| 表情反应 | 添加表情 | 支持 |
| 编辑/删除 | 修改或删除消息 | 支持 |
| 频道列表 | 查询服务器频道 | 支持 |
| 频道信息 | 查询频道详情 | 支持 |
| 高级搜索 | 多条件组合搜索 | 不支持 |
| 批量消息 | 批量发送/分发 | 不支持 |
| 频道管理 | 创建/编辑/删除频道 | 不支持 |

## 使用场景

### 场景一:向频道发布公告

需要向公告频道发送一条重要通知。

```bash
message action=send channel=discord target="#announcements" message="**提醒**:今日 20:00 例会改为线上进行,会议室见。"
```

`target` 支持频道名称(带 `#` 前缀)或频道 ID 两种形式。多个链接用 `< >` 包裹以抑制预览嵌入。

### 场景二:回复特定消息形成话题

在讨论频道中,回复某条提问消息,形成话题式讨论。

```bash
message action=send channel=discord target="#help" message="这个问题我之前遇到过,需要检查配置文件的第三行。" replyTo="112233445566778899"
```

`replyTo` 传入要回复的消息 ID,会在 Discord 中形成话题式回复引用。

### 场景三:搜索历史消息

想查找频道中之前讨论过的某个主题。

```bash
message action=search channel=discord channelId="1234567890" query="部署问题" limit=50
```

搜索结果会返回匹配的消息列表,包含消息内容、作者和时间。`limit` 默认 25 条,最大可设 100。

## 快速开始

### 第一步:确认配置

机器人配置应在 Agent 网关配置中完成。`message` 工具在指定 `channel=discord` 时会自动路由到已配置的 Discord 插件。

### 第二步:发送测试消息

```bash
message action=send channel=discord target="#general" message="聊天管理工具已接入,连接正常 ✅"
```

### 第三步:开始使用

向 Agent 描述需求,例如「在 #general 频道读取最近 10 条消息并总结讨论主题」。

## 配置示例

### 读取最近消息

```bash
message action=read channel=discord target="#general" limit=20
```

### 添加表情反应

```bash
message action=react channel=discord messageId="112233445566778899" emoji="👍"
```

### 编辑消息

```bash
message action=edit channel=discord messageId="112233445566778899" message="更新后的内容"
```

### 删除消息

```bash
message action=delete channel=discord messageId="112233445566778899"
```

### 查询频道列表

```bash
message action=channel-list channel=discord guildId="9999999999"
```

### 查询频道信息

```bash
message action=channel-info channel=discord channelId="1234567890"
```

### 常用模式速查

| 需求 | 命令模式 |
|:-----|:--------|
| 频道公告 | `action=send target="#announcements"` |
| 话题回复 | `action=send replyTo="msg-id"` |
| 最近动态 | `action=read limit=10` |
| 查找提及 | `action=search query="@username"` |
| 确认表态 | `action=react emoji="✅"` |

## 最佳实践

1. **优先用频道名称**: `target="#general"` 比直接用 ID 更清晰可读,便于后续维护和复盘。仅在频道名称含特殊字符或重复时使用 ID。

2. **反应优于回复**: 简单确认场景用表情反应(`react`)比回复消息更高效,减少频道消息量。一个表情胜过一条「收到」。

3. **格式适配 Discord**: Discord 聊天用列表而非表格(表格会渲染成难看的 `| 文本 |`),链接用 `< >` 包裹抑制预览。保持消息简短(1-3 句)。

4. **先搜后问**: 需要信息时先用 `search` 查历史,避免重复提问。搜索时关键词越具体命中率越高。

5. **消息效果增强**: 发送消息时可附加效果,例如 `effect=balloons`(气球)或 `effectId=invisible-ink`(隐形墨水),适用于庆祝或趣味场景。

6. **回复引用规范**: `replyTo` 使用消息 ID(纯数字),不要混入频道名。回复会自动带上原消息引用,无需在内容中重复原话。

7. **读取后总结**: 读取消息后可让 Agent 自动总结讨论主题、提取待办事项或生成会议纪要,提升信息消费效率。

## 常见问题

### Q1: `target` 用频道名还是 ID?

两种都支持。推荐用频道名(`#general`),更清晰;频道名含特殊字符或存在重名时使用频道 ID(纯数字)。私信场景目前不支持通过用户名发送,需使用用户 ID。

### Q2: 搜索能按作者过滤吗?

免费版搜索仅支持 `query` 关键词搜索。如需按作者、时间范围、多条件组合搜索,请升级到 Pro 版使用高级搜索模式。

### Q3: 一次能读取多少条消息?

`read` 操作 `limit` 参数控制读取数量,默认 25 条,建议不超过 100 条以避免响应过大。需要更多历史消息可通过多次读取配合 `before`/`after` 游标分页。

### Q4: 编辑消息会通知 @提及吗?

编辑消息不会重新触发 @提及通知。如需重新通知被提及的用户,建议删除原消息后重新发送。

### Q5: 机器人需要什么权限?

基础聊天操作需要「查看频道」「发送消息」「读取消息历史」权限。编辑/删除他人消息需「管理消息」权限。添加反应需「添加反应」权限。请在服务器设置中为机器人角色配置对应权限。

### Q6: 如何抑制链接预览?

在链接外包裹 `< >`,例如 `<https://example.com>`,Discord 会抑制该链接的嵌入预览,保持消息整洁。多个链接建议都包裹。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 Discord API
- **机器人**: 已在 Discord Developer Portal 创建并配置的机器人

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| Discord Bot Token | 凭证 | 必需 | Discord Developer Portal 创建机器人获取 |
| Discord 插件 | 集成 | 必需 | Agent 网关配置的 Discord 插件 |
| Discord API | 服务 | 必需 | Discord 平台提供 |

### API Key 配置

- **Discord Bot Token**: 在 Agent 网关配置中设置机器人令牌(建议通过环境变量 `DISCORD_TOKEN` 注入)。
- **权限范围**: 机器人需在目标服务器被授予「查看频道」「发送消息」「读取消息历史」「添加反应」等基础权限。
- **其他 API Key**: 免费版不依赖额外 API Key,仅使用 Discord Bot Token。

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 执行能力)
- **说明**: 以自然语言指令驱动 Agent 调用 `message` 工具完成 Discord 聊天操作
- **适用规模**: 单服务器、个人/小团队,日操作量 100 次以内
- **升级建议**: 如需高级搜索、批量消息、频道管理,请升级至 `discord-chat-manager-pro`
