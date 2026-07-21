---
slug: discord-chat-manager
name: discord-chat-manager
version: "1.0.0"
displayName: Discord聊天管理专业版
summary: 企业级 Discord 聊天管理,支持高级搜索、批量消息分发与频道全生命周期管理。
license: Proprietary
edition: pro
description: |-
  面向运营团队与企业场景的 Discord 聊天全功能管理工具。核心能力:
  - 多条件组合高级搜索(作者/时间范围/频道/关键词)
  - 批量消息发送、定时发布与分发策略
  - 频道创建、编辑、删除与分类管理
  - 消息分析统计与讨论主题聚合

  适用场景:
  - 运营团队多频道批量通知与内容分发
  - 社区知识库的消息检索与归档
  - 频道结构化搭建与生命周期管理

  差异化: Pro 版在免费版基础上扩展高级搜索、批量分发与频道管理;与免费版命令格式完全兼容
tags:
- Discord
- 聊天管理
- Communication
- 高级搜索
- 批量分发
tools:
  - - read
- exec
---
# Discord聊天管理专业版

## 核心能力

| 能力模块 | 说明 | 免费版 | Pro 版 |
|:-------|:-----|:------:|:------:|
| 发送消息 | 发送文本到频道 | 单条 | 批量+定时 |
| 回复消息 | 回复指定消息 | 支持 | 支持 |
| 读取消息 | 读取最近消息 | 支持 | 支持+游标分页 |
| 消息搜索 | 搜索历史 | 关键词 | 多条件组合 |
| 表情/编辑/删除 | 消息操作 | 支持 | 支持(批量删除) |
| 频道列表/信息 | 频道查询 | 支持 | 支持+分类视图 |
| 频道管理 | 创建/编辑/删除 | 不支持 | 支持 |
| 批量分发 | 多频道发送 | 不支持 | 支持 |
| 定时发布 | 定时消息 | 不支持 | 支持(cron) |
| 消息分析 | 统计与聚合 | 不支持 | 支持 |
### 能力模块

执行能力模块操作,处理用户输入并返回结果。

**输入**: 用户提供能力模块所需的参数和指令。

**输出**: 返回能力模块的处理结果。

- 执行`能力模块`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### 发送消息

执行发送消息操作,处理用户输入并返回结果。

**输入**: 用户提供发送消息所需的参数和指令。

**输出**: 返回发送消息的处理结果。

- 执行`发送消息`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`发送消息`相关配置参数进行设置
### 回复消息

执行回复消息操作,处理用户输入并返回结果。

**输入**: 用户提供回复消息所需的参数和指令。

**输出**: 返回回复消息的处理结果。

- 执行`回复消息`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`回复消息`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、Discord、聊天管理、支持高级搜索、批量消息分发与频、道全生命周期管理、面向运营团队与企、业场景的、聊天全功能管理工、核心能力、多条件组合高级搜、时间范围、批量消息发送、定时发布与分发策、频道创建、删除与分类管理、消息分析统计与讨、论主题聚合。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:多频道批量通知分发

运营团队需要将一条重要公告同步到多个分类频道,并附带统一表态。

```bash
message action=batch-send channel=discord \
  targets="#announcements,#general,#dev-team" \
  message="**【版本更新】** v3.0 已发布,详见更新日志。" \
  auto-react="✅" \
  pin-first=true
```

批量发送支持自动反应、首条置顶和发送结果汇总报告。

### 场景二:高级搜索定位历史讨论

需要查找某位成员在上周发布过的关于部署问题的所有讨论。

```bash
message action=advanced-search channel=discord \
  channelId="1234567890" \
  query="部署" \
  authorId="1111111111" \
  after="2026-07-10T00:00:00Z" \
  before="2026-07-17T00:00:00Z" \
  limit=100 \
  format=threaded
```

高级搜索支持按作者、时间范围、频道、关键词多条件组合,结果可按线索(threaded)或时间序列(chronological)输出。

### 场景三:频道结构化搭建

新社区搭建时,需要批量创建分类与频道。

```bash
message action=channel-create channel=discord \
  guildId="9999999999" \
  name="技术讨论" \
  type=text \
  category="tech" \
  topic="日常技术交流与答疑"

message action=category-create channel=discord \
  guildId="9999999999" \
  name="技术分类" \
  position=1
```

批量创建:

```bash
message action=batch-channel-create channel=discord \
  guildId="9999999999" \
  channels='[
    {"name":"announcements","type":"text","category":"info"},
    {"name":"general","type":"text","category":"info"},
    {"name":"voice-main","type":"voice","category":"voice"}
  ]'
```

## 使用流程

### 优秀步:确认高级功能启用

专业版高级功能(频道管理、批量操作)需在配置中启用:

```json5
{
  "discord-chat": {
    "advanced": {
      "channelManagement": true,
      "batchOperations": true,
      "advancedSearch": true,
      "analytics": true
    },
    "batch": {
      "maxConcurrency": 5,
      "rateLimitMs": 500,
      "dryRunByDefault": false
    }
  }
}
```

### 第二步:验证权限

```bash
message action=channel-info channel=discord channelId="1234567890"
```

机器人需具备「管理频道」权限才能执行创建/编辑/删除操作。

### 第三步:执行批量操作(建议预演)

```bash
message action=batch-send channel=discord \
  targets="#test-1,#test-2" \
  message="批量发送测试" \
  dry-run=true
```

`dry-run=true` 预演模式会返回将要发送的目标列表和内容,不实际发送。

### 命令参数说明

- `-team`: 命令参数,用于指定操作选项
- `-react`: 命令参数,用于指定操作选项
- `-by-hour`: 命令参数,用于指定操作选项
- `-first`: 命令参数,用于指定操作选项
- `-authors`: 命令参数,用于指定操作选项

### 命令参数说明

- `-main`: 命令参数,用于指定操作选项
- `-info`: 命令参数,用于指定操作选项
- `-reports`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux(推荐 Linux 用于生产环境)
- **网络**: 需稳定访问 Discord API
- **机器人**: Discord Developer Portal 创建的机器人,具备频道管理权限

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| Discord Bot Token | 凭证 | 必需 | Discord Developer Portal 创建机器人获取 |
| Discord 插件 | 集成 | 必需 | Agent 网关配置的 Discord 插件 |
| Discord API | 服务 | 必需 | Discord 平台提供 |
| 调度器 | 服务 | 可选 | Agent 平台 cron 调度或系统 crontab |

### API Key 配置

- **Discord Bot Token**: 在 Agent 网关配置中设置机器人令牌(建议通过环境变量 `DISCORD_TOKEN` 注入)。
- **高级权限范围**: 机器人需在目标服务器被授予「管理频道」权限才能执行创建/编辑/删除操作;批量操作需「管理消息」权限。
- **功能开关**: 高级搜索、批量操作、频道管理、分析统计需在配置中显式启用对应功能开关。
- **审计配置**: 建议为批量删除等高影响操作开启审计日志,记录操作人、目标范围和原因。

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 执行能力)
- **说明**: 以自然语言指令驱动 Agent 调用 `message` 工具完成聊天、搜索、批量与频道管理操作
- **适用规模**: 中大型社区、运营团队,日操作量 1000 次以上,支持批量与定时
- **兼容性**: 与 `discord-chat-manager-free` 命令格式完全兼容,可平滑升级
- **支持级别**: 优先支持(Pro 版享有问题优先响应与功能迭代建议通道)

## 案例展示

### 高级搜索完整配置

```bash
message action=advanced-search channel=discord \
  guildId="9999999999" \
  query="功能请求" \
  channelIds='["111","222","333"]' \
  authorId="1111111111" \
  has="attachment" \
  after="2026-07-01T00:00:00Z" \
  before="2026-07-18T00:00:00Z" \
  sort=desc \
  limit=200 \
  format=threaded \
  export=markdown
```

| 参数 | 说明 |
|:-----|:-----|
| `query` | 关键词(支持模糊匹配) |
| `channelIds` | 限定频道列表(JSON 数组) |
| `authorId` | 按作者过滤 |
| `has` | 包含特定元素(attachment/embed/link) |
| `after`/`before` | 时间范围(ISO 8601) |
| `sort` | 排序方向(asc/desc) |
| `format` | 输出格式(threaded/chronological/raw) |
| `export` | 导出格式(markdown/json/csv) |

### 批量消息发送

```bash
message action=batch-send channel=discord \
  targets='["channel:111","channel:222","channel:333"]' \
  message="统一公告内容" \
  auto-react="📢" \
  pin-first=true \
  stagger-ms=500
```

`stagger-ms` 控制每条发送间隔,避免触发频率限制。

### 定时消息发布

```bash
message action=schedule-send channel=discord \
  target="#announcements" \
  message="每周一例会提醒:今晚 20:00 线上见" \
  schedule='{"cron":"0 10 * * 1","timezone":"Asia/Shanghai"}'
```

### 频道管理操作

创建频道:

```bash
message action=channel-create channel=discord \
  guildId="9999999999" \
  name="bug-reports" \
  type=text \
  topic="Bug 上报与跟踪" \
  slowmode=10
```

编辑频道:

```bash
message action=channel-edit channel=discord \
  channelId="1234567890" \
  topic="更新后的频道主题" \
  slowmode=30
```

删除频道:

```bash
message action=channel-delete channel=discord \
  channelId="1234567890" \
  reason="频道合并,内容已迁移"
```

### 消息分析统计

```bash
message action=analytics channel=discord \
  channelId="1234567890" \
  range='{"after":"2026-07-01","before":"2026-07-18"}' \
  metrics="top-authors,activity-by-hour,keywords" \
  format=report
```

输出示例:

```markdown

## 常见问题

### Q1: 高级搜索支持哪些过滤条件?

Pro 版高级搜索支持:关键词(`query`)、作者(`authorId`)、频道列表(`channelIds`)、时间范围(`after`/`before`)、内容类型(`has`: attachment/embed/link)、排序(`sort`)、输出格式(`format`)和导出格式(`export`)。各条件可任意组合。

### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

Discord API 有全局和按频道频率限制。Pro 版内置 `stagger-ms`(默认 500ms)错峰控制和 `maxConcurrency`(默认 5)并发限制。接近限制时自动排队,触发 429 时按 `Retry-After` 自动退避重试。

### Q3: 频道创建支持哪些类型?

支持文本频道(text)、语音频道(voice)、公告频道(announcement)、舞台频道(stage)。创建时可指定分类(category)、主题(topic)、慢速模式(slowmode,单位秒)和位置(position)。

### Q4: 消息分析统计的数据范围多大?

单次分析建议覆盖 1-4 周(约 1000-5000 条消息)。范围过大会导致响应缓慢。需要长期趋势分析时,建议按周分批运行后合并报告。分析指标包括活跃度、TOP 发言者、活跃时段和热门关键词。

### Q5: 定时消息和批量消息能组合吗?

可以。可以创建一个定时任务,在指定时间执行批量发送到多频道。例如每周一 10:00 向三个频道发送周报提醒。配置时将 `schedule` 和 `targets` 同时指定即可。

### Q6: 搜索结果导出有哪些格式?

支持 markdown(可读性优秀,适合归档)、json(结构化,适合二次处理)和 csv(表格,适合数据分析)。建议日常归档用 markdown,数据统计用 csv,程序处理用 json。

### Q7: Pro 版如何与免费版共存?

两者 `message` 命令格式完全兼容,可共存。Pro 版额外支持 `advanced-search`、`batch-send`、`channel-create/edit/delete`、`analytics` 等高级 action。建议生产环境统一使用 Pro 版,免费版仅用于轻量测试。

### Q8: 批量删除消息有风险吗?

批量删除属于高影响操作。建议:先用 `dry-run` 确认删除范围;开启审计日志记录;按作者或时间范围精确过滤,避免误删。删除操作不可撤销,务必谨慎。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持
- 需要LLM支持

