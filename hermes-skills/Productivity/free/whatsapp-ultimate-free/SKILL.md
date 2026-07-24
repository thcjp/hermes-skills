---
name: "whatsapp-ultimate-free"
description: "通讯应用消息发送、交互反应、群组管理和多Agent讨论工具(免费版)"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "通讯应用工具(免费版)"
  version: "1.0.0"
  summary: "通讯应用消息发送、交互反应、群组管理和多Agent讨论工具(免费版)"
  tags:
    - "通用办公"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# 通讯应用工具(免费版)

通讯应用消息发送、交互反应、群组管理和多Agent讨论。

## 核心能力

### 1. 消息发送
支持多种消息类型：
- 文本消息：`message action=send --type text`
- 图片消息：`message action=send --type image`
- 语音消息：`message action=send --type voice`（采样率64k，格式opus）
- 视频消息：`message action=send --type video`
- 贴纸消息：`message action=send --type sticker`（尺寸512x512）
- 文件消息：`message action=send --type document`

```bash
python3 scripts/message action=send --to "contact-id@s.whatsapp.net" --type text --content "你好，这是一条测试消息"
```

**输入**: 用户提供消息发送所需的指令和必要参数。
**处理**: 按照skill规范执行消息发送操作,遵循单一意图原则。
**输出**: 返回消息发送的执行结果,包含操作状态和输出数据。

### 2. 交互反应
对消息添加表情反应、回复消息和转发消息。

```bash
python3 scripts/message action=react --message-id "msg-abc123" --emoji "👍"
python3 scripts/message action=reply --message-id "msg-abc123" --content "收到"
```

**输入**: 用户提供交互反应所需的指令和必要参数。
**处理**: 按照skill规范执行交互反应操作,遵循单一意图原则。
**输出**: 返回交互反应的执行结果,包含操作状态和输出数据。

### 3. 群组管理
创建群组、添加/移除成员、修改群组信息。

```bash
python3 scripts/message action=group-create --name "项目讨论组" --participants "user1@s.whatsapp.net" "user2@s.whatsapp.net"
```

**处理**: 按照skill规范执行群组管理操作,遵循单一意图原则。
### 4. 历史搜索
搜索聊天历史记录，支持关键词和日期范围。

```bash
python3 scripts/message action=search --chat "contact-id@s.whatsapp.net" --query "会议纪要" --limit 20
```

**输入**: 用户提供历史搜索所需的指令和必要参数。
**输出**: 返回历史搜索的执行结果,包含操作状态和输出数据。

### 输出格式

执行结果以Markdown格式返回,包含操作状态(成功/失败)、处理摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证执行结果，确认输出符合预期格式
- 参考`输出格式`相关配置参数进行设置
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 发送消息 | 收件人JID+消息内容 | 消息发送状态 |
| 群组管理 | 群组名+成员列表 | 群组创建结果 |
| 历史搜索 | 聊天JID+关键词 | 匹配消息列表 |

## 使用流程

1. 确认收件人JID格式:个人 `数字@s.whatsapp.net`,群组 `ID@g.us`
2. 选择消息类型(text/image/voice/video/sticker/document)
3. 如需媒体消息,先用ffmpeg转换格式
4. 执行发送命令
5. 如需搜索历史,使用 `action=search`

#
## 示例

### 示例:发送文本消息

```bash
python3 scripts/message action=send \
  --to "8613800138000@s.whatsapp.net" \
  --type text \
  --content "会议已开始，请准时参加"
```

输出：
```json
{
  "success": true,
  "message_id": "msg-abc123def456",
  "timestamp": "2026-07-21T10:00:00Z",
  "status": "sent"
}
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 消息发送速率限制 | 短时间内发送过多消息 | 等待30秒后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，控制发送频率 |
| JID格式无效 | 收件人ID格式错误 | 确保格式为 `数字@s.whatsapp.net`（个人）或 `ID@g.us`（群组） |
| 语音消息格式错误 | 非opus格式或采样率不是64k | 用 `ffmpeg -ar 48000 -b:a 64k -c:a libopus` 转换 |
| 贴纸尺寸不符合要求 | 不是512x512或非webp格式 | 用 `ffmpeg -vf scale=512:512` 调整尺寸，转为webp |

## 常见问题

### Q1: 贴纸的尺寸和格式要求是什么？
A: 贴纸必须是512x512像素的webp格式文件，大小不超过100KB。使用 `ffmpeg -i input.png -vf "scale=512:512:force_original_aspect_ratio=decrease" -lossless 1 output.webp` 生成。

### Q2: 语音消息的采样率是多少？
A: 语音消息采样率为48000Hz，比特率64k，格式为opus。使用 `ffmpeg -i input.wav -ar 48000 -ac 1 -b:a 64k -c:a libopus output.opus` 转换。

### Q3: JID格式有哪些？
A: 个人聊天JID格式为 `国际区号+号码@s.whatsapp.net`（如 `8613800138000@s.whatsapp.net`）。群组JID格式为 `群组ID@g.us`（如 `project-group@g.us`）。

## 已知限制

- 贴纸必须为512x512像素的webp格式，大小不超过100KB
- 语音消息采样率48000Hz，比特率64k，格式opus
- 消息发送有速率限制，触发后需等待30秒

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 升级提示

本免费版提供基础功能。升级到完整版 whatsapp-ultimate 获取全部能力和高级特性。
