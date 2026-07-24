---
slug: "whatsapp-ultimate"
name: "whatsapp-ultimate"
version: 4.0.4
displayName: "通讯应用工具"
summary: "通讯应用消息发送、交互反应、群组管理和多Agent讨论工具。通讯应用消息发送、交互反应、群组管理和多Agent讨论工具。支持文本、图片、 语音、视频、贴纸等多种消息类型，支持投票、群组创建、"
license: "MIT"
description: |-
  通讯应用消息发送、交互反应、群组管理和多Agent讨论工具。支持文本、图片、
  语音、视频、贴纸等多种消息类型，支持投票、群组创建、历史搜索和多Agent
  协作讨论。通过协议库桥接通讯应用，提供完整的消息交互能力。适用于独立
  开发者、企业团队和自动化工作流场景。不适用于无通讯应用账号的场景.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - WhatsApp
  - 社交
  - 通信
  - action
  - agent
category: "Communication"
---
# 通讯应用工具

通讯应用消息发送、交互反应、群组管理和多Agent讨论.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 通讯应用工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 通讯应用工具通讯应用消息发送 | 不支持 | 支持 |
| 通讯应用工具群组管理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

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
python3 （请参考skill目录中的脚本文件） action=send --to "contact-id@s.whatsapp.net" --type text --content "你好，这是一条测试消息"
```

**输入**: 用户提供消息发送所需的指令和必要参数.
**处理**: 解析消息发送的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回消息发送的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 交互反应
对消息添加表情反应、回复消息和转发消息.
```bash
python3 （请参考skill目录中的脚本文件） action=react --message-id "msg-abc123" --emoji "👍"
python3 （请参考skill目录中的脚本文件） action=reply --message-id "msg-abc123" --content "收到"
```

**输入**: 用户提供交互反应所需的指令和必要参数.
**处理**: 解析交互反应的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回交互反应的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 投票创建
在群组或个人聊天中创建投票.
```bash
python3 （请参考skill目录中的脚本文件） action=poll --to "group-id@g.us" --question "下周会议时间" --options "周一" "周二" "周三"
```

**输入**: 用户提供投票创建所需的指令和必要参数.
**处理**: 解析投票创建的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 4. 群组管理
创建群组、添加/移除成员、修改群组信息.
```bash
python3 （请参考skill目录中的脚本文件） action=group-create --name "项目讨论组" --participants "user1@s.whatsapp.net" "user2@s.whatsapp.net"
```

**处理**: 解析群组管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `群组管理` 选项

### 5. 历史搜索
搜索聊天历史记录，支持关键词和日期范围.
```bash
python3 （请参考skill目录中的脚本文件） action=search --chat "contact-id@s.whatsapp.net" --query "会议纪要" --limit 20
```

**输入**: 用户提供历史搜索所需的指令和必要参数.
**输出**: 返回历史搜索的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `历史搜索` 选项

### 6. 多Agent讨论
多个Agent在同一群组中进行协作讨论，通过 `staleness_threshold` 0.85控制消息新鲜度，避免回声循环.
```bash
python3 （请参考skill目录中的脚本文件） --group "project-group@g.us" --agents 3 --staleness-threshold 0.85
```

**输入**: 用户提供多Agent讨论所需的指令和必要参数.
**处理**: 解析多Agent讨论的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多Agent讨论的处理结果,包含执行状态码、结果数据和执行日志.
### 7. 媒体处理
通过 `ffmpeg` 处理媒体文件：
- 语音消息：采样率64k，格式opus
- 贴纸：尺寸512x512，格式webp
- 视频：压缩至适合发送的大小

```bash
# 生成贴纸
ffmpeg -i input.png -vf "scale=512:512:force_original_aspect_ratio=decrease" -lossless 1 output.webp
# ...
# 生成语音消息
ffmpeg -i input.wav -ar 48000 -ac 1 -b:a 64k -c:a libopus output.opus
```

### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`whatsapp-ultimate`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 消息格式要求

| 消息类型 | 格式要求 | 最大大小 |
|:---:|:---:|:---:|
| 文本 | UTF-8编码 | 无限制 |
| 图片 | jpg/png/webp | 16MB |
| 语音 | opus格式，64k采样率 | 16MB |
| 视频 | mp4格式 | 64MB |
| 贴纸 | webp格式，512x512 | 100KB |
| 文件 | 任意格式 | 100MB |

## 真实示例

### 示例1：发送文本消息

```bash
python3 （请参考skill目录中的脚本文件） action=send \
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

### 示例2：发送语音消息

```bash
# 先用ffmpeg转换音频
ffmpeg -i recording.wav -ar 48000 -ac 1 -b:a 64k -c:a libopus voice_msg.opus
# ...
# 发送语音消息
python3 （请参考skill目录中的脚本文件） action=send \
  --to "8613800138000@s.whatsapp.net" \
  --type voice \
  --file "/tmp/voice_msg.opus"
```

输出：
```json
{
  "success": true,
  "message_id": "msg-voice789",
  "media_type": "audio",
  "duration_seconds": 15,
  "timestamp": "2026-07-21T10:05:00Z"
}
```

### 示例3：创建投票

```bash
python3 （请参考skill目录中的脚本文件） action=poll \
  --to "project-group@g.us" \
  --question "本周冲刺目标选择" \
  --options "功能A" "功能B" "功能C" \
  --multi-select false
```

输出：
```json
{
  "success": true,
  "poll_id": "poll-xyz789",
  "question": "本周冲刺目标选择",
  "options": ["功能A", "功能B", "功能C"],
  "timestamp": "2026-07-21T10:10:00Z"
}
```

### 示例4：搜索历史消息

```bash
python3 （请参考skill目录中的脚本文件） action=search \
  --chat "project-group@g.us" \
  --query "部署" \
  --limit 10
```

输出：
```json
{
  "results": [
    {"message_id": "msg-001", "sender": "张三", "content": "生产环境部署完成", "timestamp": "2026-07-20T15:30:00Z"},
    {"message_id": "msg-002", "sender": "李四", "content": "部署文档已更新", "timestamp": "2026-07-20T16:00:00Z"}
  ],
  "total_found": 2
}
```

### 示例5：生成并发送贴纸

```bash
# 生成贴纸
ffmpeg -i sticker_input.png -vf "scale=512:512:force_original_aspect_ratio=decrease" -lossless 1 /tmp/sticker.webp
# ...
# 发送贴纸
python3 （请参考skill目录中的脚本文件） action=send \
  --to "8613800138000@s.whatsapp.net" \
  --type sticker \
  --file "/tmp/sticker.webp"
```

输出：
```json
{
  "success": true,
  "message_id": "msg-sticker456",
  "media_type": "sticker",
  "dimensions": "512x512",
  "timestamp": "2026-07-21T10:15:00Z"
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 消息发送速率限制 | 短时间内发送过多消息 | 等待30秒后控制发送频率 |
| JID格式无效 | 收件人ID格式错误 | 确保格式为 `数字@s.whatsapp.net`（个人）或 `ID@g.us`（群组） |
| 语音消息格式错误 | 非opus格式或采样率不是64k | 用 `ffmpeg -ar 48000 -b:a 64k -c:a libopus` 转换 |
| 贴纸尺寸不符合要求 | 不是512x512或非webp格式 | 用 `ffmpeg -vf scale=512:512` 调整尺寸，转为webp |
| 多Agent回声循环 | Agent互相回复导致无限循环 | 设置 `staleness-threshold` 为0.85，过滤过时消息 |
| 消息发送超时 | 网络延迟超过60000ms窗口 | ，发送 |
| 媒体文件超过大小限制 | 文件超过16MB（图片）或64MB（视频） | 用 `ffmpeg` 压缩或裁剪后再发送 |

## 常见问题

### Q1: 贴纸的尺寸和格式要求是什么？
A: 贴纸必须是512x512像素的webp格式文件，大小不超过100KB。使用 `ffmpeg -i input.png -vf "scale=512:512:force_original_aspect_ratio=decrease" -lossless 1 output.webp` 生成.
### Q2: 语音消息的采样率是多少？
A: 语音消息采样率为48000Hz，比特率64k，格式为opus。使用 `ffmpeg -i input.wav -ar 48000 -ac 1 -b:a 64k -c:a libopus output.opus` 转换.
### Q3: JID格式有哪些？
A: 个人聊天JID格式为 `国际区号+号码@s.whatsapp.net`（如 `8613800138000@s.whatsapp.net`）。群组JID格式为 `群组ID@g.us`（如 `project-group@g.us`）.
### Q4: 多Agent讨论如何避免回声循环？
A: 设置 `staleness-threshold` 为0.85。当消息的新鲜度低于0.85时，Agent不再回复该消息。新鲜度基于消息时间戳和当前时间的差值计算，超过60000ms窗口的消息新鲜度降为0.
### Q5: 消息发送有速率限制吗？
A: 有。短时间内发送过多消息会触发速率限制。建议每次发送间隔至少1秒。触发限制后等待30秒重试.
### Q6: 如何搜索特定聊天中的历史消息？
A: 使用 `message action=search` 命令，提供 `--chat`（聊天JID）、`--query`（搜索关键词）和 `--limit`（最大结果数）。返回匹配的消息列表，包含发送者、内容和时间戳.
### Q7: 投票支持多选吗？
A: 支持。通过 `--multi-select true` 参数启用多选模式。默认为单选（`--multi-select false`）。每个投票最多支持12个选项.
## 已知限制

- 贴纸必须为512x512像素的webp格式，大小不超过100KB
- 语音消息采样率48000Hz，比特率64k，格式opus
- 消息发送有速率限制，触发后需等待30秒
- 多Agent讨论的 `staleness-threshold` 默认0.85，60000ms窗口
- JID格式必须为 `数字@s.whatsapp.net` 或 `ID@g.us`
- 媒体文件大小限制：图片16MB、视频64MB、文件100MB
- 投票最多支持12个选项
