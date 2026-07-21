---
slug: test-wa-free
name: test-wa-free
version: "1.0.0"
displayName: WhatsApp 消息 LITE
summary: 通过 wacli CLI 向他人发送 WhatsApp 文本消息与查询聊天列表。
license: MIT
description: |-
  WhatsApp 消息集成 Skill 免费版。基于 wacli CLI 实现向他人发送文本消息、
  查询聊天列表。支持二维码登录认证与基础消息发送。
  适用于向第三方发送文本提醒、查找聊天等基础场景。
tags:
  - Communication
tools:
  - read
  - exec
---

# WhatsApp 消息 LITE

WhatsApp 消息集成免费版。基于 wacli CLI 实现向他人发送文本消息与查询聊天列表。仅当用户明确要求向他人发送 WhatsApp 消息时使用。用户与 Agent 的常规聊天不应使用此工具。

## 核心能力

- **文本消息发送**：向个人发送文本消息，需明确指定收件人号码与消息内容
- **聊天列表查询**：按名称或号码查询聊天列表，支持 limit 限制返回数量
- **认证**：二维码登录认证，扫描手机 WhatsApp"已关联设备"完成关联
- **环境诊断**：运行 `wacli doctor` 检查认证状态与连接质量
- **JID 格式识别**：直聊 JID 为 `<number>@s.whatsapp.net`，群组 JID 为 `<id>@g.us`

## 工具命令

- `wacli auth`：二维码登录与初始同步
- `wacli doctor`：诊断环境与连接状态
- `wacli chats list --limit 20 --query "名称或号码"`：查询聊天列表
- `wacli send text --to "+14155551212" --message "文本内容"`：发送文本消息

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 发送文本提醒 | 收件人号码与提醒文本 | 向收件人发送 WhatsApp 文本消息 |
| 查找聊天 | 名称或号码 | 返回匹配的聊天列表含 JID |

**不适用于**：文件发送、群组消息、历史消息检索、历史回填、持续同步等高级场景。

## 使用流程

1. **确认认证状态**：首次使用运行 `wacli auth` 扫码登录，完成后运行 `wacli doctor` 确认连接正常
2. **识别收件人**：通过 `wacli chats list --query "名称"` 查找目标聊天，获取 JID 或号码
3. **确认发送内容**：向用户预览收件人与消息内容，确认后执行发送
4. **执行与错误处理**：调用命令执行，若返回错误按错误处理章节排查

## 认证配置

运行 `wacli auth` 后终端显示二维码，打开手机 WhatsApp 的"设置 - 已关联设备"扫描二维码完成登录。登录后自动执行初始同步。认证凭证存储在 `~/.wacli` 目录，无需额外 API Key。完成后运行 `wacli doctor` 确认连接状态正常。

## 安全机制

- 发送消息必须明确指定收件人与消息文本，两者缺一不可
- 发送前向用户确认收件人号码/JID 与消息内容
- 信息有歧义时先提问澄清，不猜测收件人或内容
- 不用于用户与 Agent 的常规聊天，仅用于向第三方发送消息

## 案例展示

### 案例 1：向联系人发送文本提醒

**触发**：需要提醒联系人明天的会议时间变更

**执行**：

```bash
wacli send text --to "+14155551212" --message "明天的会议改到下午 2 点。"
```

**结果**：联系人 `+14155551212` 收到一条 WhatsApp 文本消息。发送前已向用户确认收件人与消息内容。

### 案例 2：查询聊天列表查找联系人

**触发**：需要查找某个联系人的聊天记录以获取 JID

**执行**：

```bash
wacli chats list --limit 20 --query "张"
```

**结果**：返回最多 20 条匹配的聊天记录，含聊天名称与 JID。从结果中获取目标联系人的 JID 后可用于发送消息。

## 错误处理

| 错误 | 原因 | 处理方式 |
|------|------|---------|
| 认证失败 / 未登录 | 未完成 `wacli auth` 或登录已过期 | 重新运行 `wacli auth` 扫码登录，完成后 `wacli doctor` 验证 |
| JID 格式错误 | 直聊与群组 JID 混用或格式不完整 | 直聊用 `<number>@s.whatsapp.net`，群组用 `<id>@g.us`，通过 `chats list` 获取正确 JID |
| 收件人不在联系人 | 号码未注册 WhatsApp 或格式错误 | 确认号码含国际区号（如 `+1`），收件人需有有效 WhatsApp 账号 |
| 免费版不支持文件发送 | 误用 `wacli send file` 命令 | 免费版仅支持文本消息，如需发送文件请升级付费版 |
| doctor 报告异常 | 存储目录损坏或连接状态异常 | 运行 `wacli doctor` 查看诊断详情，按提示修复存储目录 `~/.wacli` |

## 常见问题

### Q1：如何完成 wacli 首次登录？
A：运行 `wacli auth`，终端显示二维码。打开手机 WhatsApp"已关联设备"扫描二维码完成登录。登录后自动执行初始同步，完成后运行 `wacli doctor` 确认连接正常。

### Q2：免费版支持发送哪些消息类型？
A：免费版仅支持发送文本消息（`wacli send text`）。如需发送文件、群组消息等，请升级付费版。

### Q3：直聊和群组的 JID 有什么区别？
A：直聊 JID 为 `<number>@s.whatsapp.net`（如 `14155551212@s.whatsapp.net`），群组 JID 为 `<id>@g.us`。不确定 JID 时运行 `wacli chats list --query "名称"` 查询，返回结果中包含正确的 JID。

### Q4：什么时候应该用 wacli？
A：仅当用户明确要求向他人发送 WhatsApp 消息时使用。用户与 Agent 的常规聊天由平台自动路由，不应使用此工具。

## 已知限制

- 仅支持发送文本消息，不支持文件与群组消息
- 不支持历史消息检索与回填
- 不支持持续同步（`sync --follow`）
- 不支持 `--json` 结构化输出
- 发送消息必须明确收件人与内容，不支持模糊发送
- 存储目录 `~/.wacli` 不可手动修改，损坏后需重新认证
- 不用于用户与 Agent 的常规聊天，仅用于向第三方发送消息

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **wacli CLI**：需已安装并可在命令行执行
- **手机端 WhatsApp**：需保持在线以支持认证与发送

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| wacli CLI | 命令行工具 | 必需 | 安装 wacli 命令行工具 |
| WhatsApp 账号 | 凭证 | 必需 | 手机端 WhatsApp 扫码关联 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供决策能力 |

### API Key 配置
- 无需额外 API Key，通过 `wacli auth` 扫码登录完成认证
- 认证凭证存储在 `~/.wacli` 目录

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，功能需要 exec 命令行执行 wacli）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务

---

## 升级提示

当前为免费版，仅支持文本消息发送与聊天列表查询。如需以下完整功能，请升级付费版：

- **多类型消息发送**：支持文件发送（含 caption）、群组消息
- **消息检索**：按关键词与日期范围检索历史消息
- **历史回填**：对指定聊天回填历史消息，支持控制请求数与消息数
- **持续同步**：通过 `sync --follow` 持续同步新消息
- **JSON 输出**：支持 `--json` 参数输出结构化数据供程序化处理
- **环境诊断**：完整的 doctor 诊断与修复指引

升级至付费版：`https://SkillHub.ai/skill/test-wa`
