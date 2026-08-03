---
slug: "whatsapp-ultimate-free"
name: "whatsapp-ultimate-free"
version: "1.0.0"
displayName: "通讯应用工具(免费版)"
summary: "通讯应用消息发送、交互,提供核心能力"
summary_zh: "通讯应用消息发送、交互,提供核心能力"
license: "MIT"
description: "|- 通讯应用消息发送、交互反应、群组管控和多Agent讨论工具。兼容文本、图片、 语音、视频、贴纸等多种消息类型，兼容投票、群组创建、历史搜索和多Agent 协作讨论。通过协议库桥接通讯应用，包含完整的消息交互能力。适用于独立 开发者、企业团队和自发化工作流场景。不适用于无通讯应用账号的场景.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
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
  - net
  - send
  - type
category: "Communication"
pricing_tier: free
---
# 通讯应用工具(免费版)

通讯应用消息发送、交互反应、群组管理和多Agent讨论. 关键词: whatsapp ultimate
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 通讯应用工具(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心能力

### 1. 消息发送
支持多种消息类型：
- 文本消息：`message action=send --type text`
- 图片消息：`message action=send --type image`
- 语音消息：`message action=send --type voice`（采样率64k，格式opus）
- 视频消息：`message action=send --type video`
- 贴纸消息：`message action=send --type sticker`（尺寸512x512）
- 文件消息：`message action=send --type document`

```网络连接说明d@s.whatsapp.net" --type text --content "你好，这是一条测试消息"
```

### 2. 交互反应
对消息添加表情反应、回复消息和转发消息.
```网络连接说明d "msg-abc123" --emoji "👍"
python3 （请参考skill目录中的脚本文件） action=reply --message-id "msg-abc123" --content "收到"
```

### 3. 群组管理
创建群组、添加/移除成员、修改群组信息.
```bash
python3 （请参考skill目录中的脚本文件） action=group-create --name "项目讨论组" --participants "user1@s.whatsapp.net" "user2@s.whatsapp.net"
```

### 4. 历史搜索
搜索聊天历史记录，支持关键词和日期范围.
```网络连接说明d@s.whatsapp.net" --query "会议纪要" --limit 20
```

### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 发送消息 | 收件人JID+消息内容 | 消息发送状态 |
| 群组管理 | 群组名+成员列表 | 群组创建结果 |
| 历史搜索 | 聊天JID+关键词 | 匹配消息列表 |

## 使用流程

1. 确认收件人JID格式:个人 `数字@s.whatsapp.net`,群组 `ID@g.us`
2. 选择消息类型(text/image/voice/video/sticker/document)
3. 如需媒体消息,先用ffmpeg转换格式
4. 执行发送命令
5. 如需搜索历史,使用 `action=search`

## 示例

### 示例:发送文本消息

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 消息发送速率限制 | 短时间内发送过多消息 | 等待30秒后检查网络连接和配置后重试，控制发送频率 |
| JID格式无效 | 收件人ID格式错误 | 确保格式为 `数字@s.whatsapp.net`（个人）或 `ID@g.us`（群组） |
| 语音消息格式错误 | 非opus格式或采样率不是64k | 用 `ffmpeg -ar 48000 -b:a 64k -c:a libopus` 转换 |
| 贴纸尺寸不符合要求 | 不是512x512或非webp格式 | 用 `ffmpeg -vf scale=512:512` 调整尺寸，转为webp |

## 常见问题

### Q1: 贴纸的尺寸和格式要求是什么？
A: 贴纸必须是512x512像素的webp格式文件，大小不超过100KB。使用 `ffmpeg -i input.png -vf "scale=512:512:force_original_aspect_ratio=decrease" -lossless 1 output.webp` 生成.
### Q2: 语音消息的采样率是多少？
A: 语音消息采样率为48000Hz，比特率64k，格式为opus。使用 `ffmpeg -i input.wav -ar 48000 -ac 1 -b:a 64k -c:a libopus output.opus` 转换.
### Q3: JID格式有哪些？
A: 个人聊天JID格式为 `国际区号+号码@s.whatsapp.net`（如 `8613800138000@s.whatsapp.net`）。群组JID格式为 `群组ID@g.us`（如 `project-group@g.us`）.
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
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 升级提示

本免费版提供基础功能。升级到完整版 whatsapp-ultimate 获取全部能力和高级特性.
---
## 边界条件与限制 (Boundary Conditions)

### 输入限制
- **消息长度**：文本消息的长度限制为2,000个字符。
- **文件大小**：发送的图片、视频、语音和文件消息的大小限制为100MB。
- **贴纸尺寸**：贴纸必须为512x512像素的webp格式，大小不超过100KB。
- **语音消息格式**：语音消息必须为opus格式，采样率必须为64k。

### 性能边界
- **并发处理**：技能同时处理的消息数量限制为10条。
- **响应时间**：技能对单个请求的处理时间不超过5秒。

### 兼容性约束
- **操作系统**：技能在Windows、macOS和Linux操作系统上运行。
- **通讯应用版本**：技能兼容WhatsApp的Android和iOS版本。
- **网络要求**：需要稳定的网络连接，建议使用Wi-Fi或4G/5G网络。

### 其他限制
- **消息发送速率**：为了避免滥用，技能对消息发送速率有限制，短时间内发送过多消息可能导致速率限制。
- **API调用频率**：技能对API的调用频率有限制，超过限制可能导致API调用失败。
- **技能版本**：whatsapp ultimate free技能仅提供基础功能，部分高级功能需要升级到完整版whatsapp-ultimate。

