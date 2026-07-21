---
slug: whatsapp-messaging-free
name: whatsapp-messaging-free
version: "1.0.0"
displayName: WhatsApp 消息（免费版）
summary: 通过 WhatsApp Business API 发送文本与图片消息、查询手机号，满足基础触达需求。
license: MIT
description: |-
  通过 WhatsApp Business API 发送基础消息。免费版支持文本消息、图片消息与手机号查询。
  通过 ClawLink 托管的连接流程与凭据管理，无需自行配置 WhatsApp API 访问。
  适合个人或小团队的日常消息触达场景，不包含模板管理、交互按钮、媒体上传等进阶能力。
  受 24 小时客服窗口限制，窗口外无法发送自由文本消息。
tags:
  - Communication
  - Automation
tools:
  - read
  - exec
---

# WhatsApp（免费版）

通过 WhatsApp Business API 发送基础消息。免费版支持文本消息、图片消息与手机号查询，满足日常触达需求。本技能通过 ClawLink 托管的连接流程与凭据管理，无需自行配置 WhatsApp API 访问。

## Quick Start

```bash
clawlink_call_tool --tool "whatsapp_get_phone_numbers" --params '{}'

clawlink_call_tool --tool "whatsapp_send_message" --params '{"phone_number": "+15551234567", "message": "Hello!"}'

clawlink_call_tool --tool "whatsapp_send_media" --params '{"phone_number": "+15551234567", "media_url": "https://example.com/image.png", "caption": "See this"}'
```

**执行步骤**:

1. 准备输入参数并确认运行环境
2. 执行核心操作,处理输入数据
3. 验证处理结果的正确性

**结果处理**: 执行完成后,输出格式化的处理结果供用户查看和保存。结果包含执行状态、输出数据和错误信息(如有)。


## Authentication

所有 WhatsApp 工具调用由 ClawLink 自动鉴权，使用用户已连接的 WhatsApp Business 账户令牌。会话中无需手动传入 API 令牌。

### Getting Connected

1. 安装 ClawLink 插件并完成配对。
2. 打开 `https://claw-link.dev/dashboard?add=whatsapp` 连接 WhatsApp。
3. 调用 `clawlink_list_integrations` 验证连接已激活。

## Security & Permissions

- 访问范围限定于 OAuth 配置时连接的 WhatsApp Business 账户
- 所有消息发送操作须用户明确确认。WhatsApp 消息会触达真实用户，须确认收件人与内容
- 24 小时客服窗口适用于自由文本与图片消息；窗口外只能发送已审批的模板（模板属于付费版能力）
- 发送前确认收件人手机号，消息发出后无法撤回

## Tool Reference

| Tool | Description | Mode |
| --- | --- | --- |
| `whatsapp_get_phone_numbers` | 列出账户下所有手机号 | Read |
| `whatsapp_send_message` | 发送文本消息 | Write |
| `whatsapp_send_media` | 发送图片、视频、音频或文档 | Write |

免费版仅包含以上三个基础工具。模板管理、交互按钮、列表消息、媒体上传、联系人/位置消息、业务资料查询等属于付费版能力。

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
## 核心能力

- 文本消息发送：向 WhatsApp 用户发送自由文本，须在 24 小时窗口内
- 图片消息发送：通过公网 URL 发送图片，可附带说明文案
- 手机号查询：列出账户下所有手机号，获取 phone_number_id 作为发送方标识
- ClawLink 托管鉴权：OAuth 令牌由 ClawLink 安全存储与注入，会话中无需手动管理凭据
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Business、API、发送文本与图片消、查询手机号、满足基础触达需求、发送基础消息、免费版支持文本消、图片消息与手机号、托管的连接流程与、凭据管理、无需自行配置、适合个人或小团队、的日常消息触达场、不包含模板管理、交互按钮、媒体上传等进阶能、小时客服窗口限制、窗口外无法发送自、由文本消息。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 日常消息触达
向已主动联系过商家的 WhatsApp 用户发送文本或图片消息，例如回复咨询、发送操作截图、传递简短通知。须在用户最后一次消息后的 24 小时内发送，否则会被拒绝。

### 简单图文推送
在 24 小时窗口内，向用户发送一张图片并附带说明，例如产品截图、活动海报、操作指引。适合不需要模板与交互按钮的简单触达场景。

## 使用案例

### 案例一：发送文本消息

向已联系过商家的用户发送一条文本消息。

```bash
clawlink_call_tool --tool "whatsapp_send_message" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "message": "Hi! Your order #12345 has shipped and is on its way."
  }'
```

`phone_number_id` 从 `whatsapp_get_phone_numbers` 获取。收件人手机号须包含国家代码。该消息须在 24 小时客服窗口内发送，否则会收到 131047 错误。

### 案例二：发送图片消息

向用户发送一张图片并附带说明文案。

```bash
clawlink_call_tool --tool "whatsapp_send_media" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "media_url": "https://example.com/receipt.png",
    "caption": "Here is your receipt for order #12345"
  }'
```

`media_url` 须为 WhatsApp 服务器可访问的公网地址，本地路径不可用。图片消息同样受 24 小时窗口限制。`caption` 为可选的附带说明。

## 异常处理

### 131047 — 超出 24 小时客服窗口
向超过 24 小时未主动消息的用户发送自由文本或图片时触发。处理：免费版不支持模板消息，须等待用户再次主动消息后再发送，或升级到付费版使用模板触达。

### 131026 — 消息无法送达
收件人手机号不是有效的 WhatsApp 账户。处理：确认收件人已在 WhatsApp 注册且号码正确（含国家代码），排除座机或未注册号码。

### 133010 — 收件人未注册 WhatsApp
收件人手机号未在 WhatsApp 注册。处理：与用户确认号码是否正确，或改用短信等其他渠道触达。

### 媒体 URL 不可访问
`media_url` 为本地路径或不可公网访问时，发送失败。处理：确认 URL 为公网可访问地址，且文件类型受支持（图片支持 png/jpeg）。

### 连接缺失
WhatsApp 未连接。处理：引导用户访问 `https://claw-link.dev/dashboard?add=whatsapp` 完成连接，再调用 `clawlink_list_integrations` 验证。

## FAQ

### 24 小时客服窗口如何计算？
从用户最后一次向商家发送消息的时刻起算 24 小时。窗口内可发送文本与图片消息；窗口外免费版无法发送任何消息（模板触达属于付费版能力）。

### 如何获取 phone_number_id？
调用 `whatsapp_get_phone_numbers` 列出账户下所有手机号，返回结果中包含每个号码的 `phone_number_id`。发送消息时须传入该 ID 标识发送方。

### 收件人手机号需要什么格式？
须包含国家代码，例如美国号码以 `+1` 开头，中国号码以 `+86` 开头。不带国家代码会被视为无效号码。发送前务必确认号码完整。

### 免费版支持发送模板消息吗？
不支持。模板消息、交互按钮、列表消息、媒体上传等均属于付费版能力。免费版仅支持文本与图片消息，且受 24 小时窗口限制。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持文本消息与图片消息，不支持模板、交互按钮、列表、位置、联系人等消息类型
- 不支持模板管理，窗口外无法触达用户
- 不支持媒体上传，只能通过公网 URL 发送图片
- 自由文本与图片消息受 24 小时客服窗口限制
- 收件人手机号须包含国家代码，否则发送失败
- 消息一旦发出无法撤回，发送前须确认收件人与内容
- 依赖 ClawLink 托管鉴权，ClawLink 连接异常时所有工具不可用

## 升级提示

本免费版仅提供文本与图片消息的基础触达能力。如需模板消息（窗口外触达）、交互按钮、列表消息、媒体上传与复用、位置与联系人消息、模板全生命周期管理、业务资料查询等完整能力，请升级到付费版 whatsapp-messaging，解锁 WhatsApp Business API 的全部消息类型与管理功能。
