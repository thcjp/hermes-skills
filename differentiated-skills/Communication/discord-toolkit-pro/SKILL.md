---
slug: discord-toolkit-pro
name: discord-toolkit-pro
version: "1.0.0"
displayName: Discord工具箱专业版
summary: 企业级 Discord 管理工具,支持批量操作、审核管理、角色权限与自定义表情贴纸。
license: Proprietary
edition: pro
description: |-
  面向企业运营与社区管理团队的 Discord 全功能管理工具。核心能力:
  - 批量消息发送、清理与定时发布
  - 完整审核管理(禁言/踢出/封禁)与角色权限管理
  - 自定义表情与贴纸上传管理
  - 成员/角色/频道批量信息查询与导出
  - 语音状态查询与日程事件管理

  适用场景:
  - 中大型 Discord 社区的日常审核与运营
  - 企业品牌社区的角色权限自动化管理
  - 跨频道批量通知与内容分发

  差异化: Pro 版在免费版基础上解锁审核管理、角色操作、批量处理与自定义资源上传;与免费版操作格式完全兼容
tags:
- Discord
- 企业管理
- Communication
- 社区审核
- 批量操作
tools:
  - - read
- exec
---
# Discord 工具箱(专业版)

## 概述

Discord 工具箱专业版是一款面向企业运营与社区管理团队的 Discord 全功能管理工具。它在免费版基础消息操作之上,解锁审核管理(禁言/踢出/封禁)、角色权限管理、自定义表情与贴纸上传、成员/角色/频道批量查询、语音状态与日程事件管理等高级能力,并提供批量消息发送与定时发布功能,帮助社区管理团队高效完成日常运营与审核工作。

专业版与免费版操作格式完全兼容:免费版使用的所有 `action` 调用在专业版中可直接使用,升级后无需调整原有指令即可获得高级能力。专业版适合中大型 Discord 社区、企业品牌社区和需要批量管理能力的运营团队。

## 核心能力

| 能力模块 | 说明 | 免费版 | Pro 版 |
|:-------|:-----|:------:|:------:|
| 消息操作 | 发送/编辑/删除 | 单条 | 批量+定时 |
| 表情反应 | 添加/查看 | 支持 | 支持(批量) |
| 投票 | 创建投票 | 单题 | 多题+批量 |
| 审核管理 | 禁言/踢出/封禁 | 不支持 | 支持 |
| 角色管理 | 角色增删与权限 | 不支持 | 支持 |
| 表情上传 | 自定义表情 | 不支持 | 支持 |
| 贴纸上传 | 自定义贴纸 | 不支持 | 支持 |
| 成员/角色查询 | 批量信息 | 不支持 | 支持 |
| 频道/语音/事件 | 状态查询 | 部分 | 全量 |
| 操作门控 | 细粒度权限控制 | 部分 | 完整 |

## 使用场景

### 场景一:批量发布多频道通知

运营团队需要将一条重要公告同步发布到多个频道,并加上统一的 ✅ 反应。

```json
{
  "action": "batchSend",
  "targets": [
    "channel:1111111",
    "channel:2222222",
    "channel:3333333"
  ],
  "content": "**【重要】** 服务器规则更新,请查看置顶公告。",
  "autoReact": "✅",
  "pinFirst": true
}
```

批量发送支持自动反应、首条置顶和发送结果汇总,避免逐条手动操作。

### 场景二:违规成员审核处理

社区管理员发现违规成员,需要进行禁言处理。

```json
{
  "action": "timeout",
  "guildId": "9999999999",
  "userId": "1111111111",
  "durationMinutes": 60,
  "reason": "发布广告内容,违反社区规则第3条"
}
```

更严重的违规可执行踢出或封禁:

```json
{
  "action": "ban",
  "guildId": "9999999999",
  "userId": "1111111111",
  "deleteMessageDays": 1,
  "reason": "多次违规,封禁处理"
}
```

审核操作默认需二次确认,可在配置中开启自动审核策略。

### 场景三:角色权限自动化管理

新成员加入服务器后,自动分配对应身份角色。

```json
{
  "action": "roleAdd",
  "guildId": "9999999999",
  "userId": "1111111111",
  "roleId": "2222222222"
}
```

批量角色分配:

```json
{
  "action": "batchRoleAdd",
  "guildId": "9999999999",
  "userIds": ["111", "222", "333"],
  "roleId": "2222222222",
  "reason": "新成员入门角色批量分配"
}
```

### 场景四:自定义表情与贴纸上传

为品牌社区上传专属表情和贴纸。

```json
{
  "action": "emojiUpload",
  "guildId": "9999999999",
  "name": "brand_celebrate",
  "mediaUrl": "file:///tmp/celebrate.png",
  "roleIds": ["222", "333"]
}
```

```json
{
  "action": "stickerUpload",
  "guildId": "9999999999",
  "name": "brand_welcome",
  "description": "品牌欢迎贴纸",
  "tags": "👋",
  "mediaUrl": "file:///tmp/welcome.png"
}
```

表情限制 256KB(PNG/JPG/GIF),贴纸限制 512KB(PNG/APNG/Lottie JSON)。

## 不适用场景

以下场景Discord工具箱专业版不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调


## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求。


## 快速开始

### 第一步:启用高级操作组

在配置中启用审核与角色操作组(默认禁用):

```json5
{
  "discord": {
    "actions": {
      "moderation": true,
      "roles": true,
      "emojiUploads": true,
      "stickerUploads": true,
      "events": true,
      "voiceStatus": true
    }
  }
}
```

### 第二步:验证权限

检查机器人是否具备目标频道的审核与角色权限:

```json
{
  "action": "permissions",
  "channelId": "1234567890"
}
```

机器人需要「禁言成员」「踢出成员」「封禁成员」「管理角色」等高级权限。

### 第三步:执行批量操作

```json
{
  "action": "batchSend",
  "targets": ["channel:111", "channel:222"],
  "content": "测试批量发送",
  "dryRun": true
}
```

建议先用 `dryRun: true` 预演,确认无误后正式执行。

## 示例

### 操作门控完整配置

```json5
{
  "discord": {
    "actions": {
      // 默认启用
      "reactions": true,
      "stickers": true,
      "polls": true,
      "permissions": true,
      "messages": true,
      "threads": true,
      "pins": true,
      "search": true,
      "memberInfo": true,
      "roleInfo": true,
      "channelInfo": true,
      "voiceStatus": true,
      "events": true,
      // Pro 版解锁(默认仍关闭,按需开启)
      "emojiUploads": true,
      "stickerUploads": true,
      "roles": true,
      "moderation": true
    },
    "batch": {
      "enabled": true,
      "maxConcurrency": 5,
      "rateLimitMs": 500,
      "dryRunByDefault": false
    },
    "audit": {
      "enabled": true,
      "logPath": "logs/discord-audit.jsonl",
      "sensitiveActions": ["ban", "batchDelete", "roleRemove"]
    }
  }
}
```

### 批量消息清理

```json
{
  "action": "batchDelete",
  "channelId": "1234567890",
  "filters": {
    "authorId": "1111111111",
    "before": "9876543210",
    "limit": 50
  },
  "reason": "清理违规用户的历史消息"
}
```

### 定时消息发布

```json
{
  "action": "scheduleSend",
  "to": "channel:1234567890",
  "content": "每周一例会提醒:今晚 20:00 技术分享",
  "schedule": {
    "cron": "0 10 * * 1",
    "timezone": "Asia/Shanghai"
  }
}
```

### 成员与角色批量查询

```json
{
  "action": "memberInfo",
  "guildId": "9999999999",
  "userId": "1111111111"
}
```

```json
{
  "action": "roleInfo",
  "guildId": "9999999999"
}
```

```json
{
  "action": "channelList",
  "guildId": "9999999999"
}
```

### 语音状态与日程事件

```json
{
  "action": "voiceStatus",
  "guildId": "9999999999",
  "userId": "1111111111"
}
```

```json
{
  "action": "eventList",
  "guildId": "9999999999"
}
```

## 最佳实践

1. **批量操作先预演**: 所有批量操作(批量发送、批量删除、批量角色分配)建议先用 `dryRun: true` 预演,确认目标列表和操作内容无误后再正式执行,避免误操作。

2. **审核操作二次确认**: 禁言、踢出、封禁等高影响操作建议开启 `audit.sensitiveActions`,执行前强制二次确认,并记录完整审计日志(操作人、目标、原因、时间)。

3. **频率控制**: 批量操作配置合理的 `rateLimitMs`(建议 500ms 以上)和 `maxConcurrency`(建议 5 以内),避免触发 Discord API 频率限制导致机器人被临时封禁。

4. **角色权限最小化**: 分配角色时遵循最小权限原则,新成员只分配基础身份角色,管理角色需人工审核后单独分配,避免自动批量分配高权限角色。

5. **审核原因必填**: 所有审核操作建议强制填写 `reason` 字段,既满足 Discord 平台审计要求,也便于后续复盘和申诉处理。

6. **自定义资源命名规范**: 表情和贴纸命名建议带品牌前缀(如 `brand_`、`team_`),避免与默认表情冲突,也便于批量管理时检索。

7. **频道信息缓存**: 频道列表和成员信息查询结果建议在 Agent 侧缓存(如 5 分钟),避免高频重复查询 Discord API,降低调用次数。

8. **与免费版兼容**: Pro 版完全兼容免费版指令格式。建议在过渡期保留免费版配置,逐步启用 Pro 版高级操作组,降低切换风险。

## 常见问题

### Q1: Pro 版如何启用审核操作?

审核操作(禁言/踢出/封禁)默认关闭。需在配置中设置 `discord.actions.moderation = true` 启用,并确保机器人具备「禁言成员」「踢出成员」「封禁成员」等服务器权限。建议同时开启审计日志记录敏感操作。

### 已知限制

会。Discord API 有全局和按频道维度的频率限制。Pro 版内置 `rateLimitMs`(默认 500ms)和 `maxConcurrency`(默认 5)控制,接近限制时自动排队。若仍触发 429 限制,Agent 会按响应头 `Retry-After` 自动退避重试。

### Q3: 角色管理操作有风险吗?

角色增删属于高影响操作。建议:仅对非关键角色启用自动化;管理角色和敏感权限角色需人工审核后单独操作;所有角色变更记录审计日志。Pro 版支持 `sensitiveActions` 配置,对指定操作强制二次确认。

### Q4: 自定义表情上传失败怎么办?

检查:表情图片是否为 PNG/JPG/GIF 格式;大小是否超过 256KB;服务器表情槽位是否已满(普通服务器 50 个,提升等级后更多);机器人是否有「管理表情」权限。

### Q5: 如何查询服务器所有成员?

Discord API 不支持一次拉取全部成员。Pro 版通过分页查询 + 缓存的方式,可分批获取成员列表。大规模社区建议配合成员加入事件实时维护本地成员缓存,而非全量拉取。

### Q6: 定时消息可靠吗?

Pro 版定时消息依赖 Agent 平台的 cron 调度。若 Agent 进程在调度时刻未运行,消息会延迟到下次启动时补发(可配置)。对时效性要求高的通知,建议结合外部监控确保 Agent 可用性。

### Q7: Pro 版和免费版能同时使用吗?

可以。两者指令格式兼容。建议生产环境统一使用 Pro 版(包含全部能力),免费版仅用于轻量测试场景。两者共用同一机器人令牌,无需重复配置。

### Q8: 审计日志包含哪些内容?

审计日志记录:操作时间、操作人、操作类型、目标(用户/频道/角色)、原因、结果(成功/失败)。敏感操作(ban、batchDelete、roleRemove 等)会额外记录操作前后的状态快照,便于追溯。日志写入 `audit.logPath` 指定的文件,保留期建议 90 天以上。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux(推荐 Linux 用于生产环境)
- **网络**: 需稳定访问 Discord API
- **机器人**: Discord Developer Portal 创建的机器人,具备高级权限(审核/角色/表情管理)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| Discord Bot Token | 凭证 | 必需 | Discord Developer Portal 创建机器人获取 |
| Discord API | 服务 | 必需 | Discord 平台提供 |
| 调度器 | 服务 | 可选 | Agent 平台 cron 调度或系统 crontab |
| 媒体文件 | 本地资源 | 可选 | 本地路径或远程 URL(表情/贴纸上传) |

### API Key 配置

- **Discord Bot Token**: 在 Agent 环境配置机器人令牌(建议使用环境变量 `DISCORD_TOKEN` 注入)。
- **高级权限范围**: 机器人需在目标服务器被授予「禁言成员」「踢出成员」「封禁成员」「管理角色」「管理表情和贴纸」「管理服务器」等高级权限。
- **操作门控配置**: 审核与角色操作需在配置中显式启用 `discord.actions.moderation` 和 `discord.actions.roles`。
- **审计日志存储**: 审计日志写入本地文件,建议配置独立的日志目录并设置保留策略。

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 执行能力)
- **说明**: 以自然语言指令驱动 Agent 调用 Discord 工具完成消息、审核、角色与资源管理操作
- **适用规模**: 中大型社区、企业品牌社区,日操作量 1000 次以上,支持批量与定时
- **兼容性**: 与 `discord-toolkit-free` 指令格式完全兼容,可平滑升级
- **支持级别**: 优先支持(Pro 版享有问题优先响应与功能迭代建议通道)

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
