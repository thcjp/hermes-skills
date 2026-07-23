---
slug: "whatsapp-messaging"
name: "whatsapp-messaging"
version: "1.0.0"
displayName: "WhatsApp 商业消息"
summary: "通过 WhatsApp Business API 发送消息、管理模板、处理媒体，支持文本、图片、交互按钮、模板等消息类型。"
license: "Proprietary"
description: |-
  通过 WhatsApp Business API 发送消息、管理模板、处理媒体，自动化 WhatsApp Business 消息工作流。
  支持文本、图片、视频、音频、文档、位置、联系人、交互按钮、列表、模板等多种消息类型。
  通过 ClawLink 托管的连接流程与凭据管理，无需自行配置 WhatsApp API 访问。
  涵盖电话号码查询、消息发送、媒体上传下载、模板创建与审批状态、业务资料读取等完整能力。
  适用于订单通知、客户支持、预约提醒、营销活动等需要触达 WhatsApp 用户的业务场景。
tags:
  - 研发工具
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "WhatsApp,社交,通信"
---
# WhatsApp

通过 WhatsApp Business API 发送消息、管理模板、处理媒体，自动化 WhatsApp Business 消息工作流。本技能通过 ClawLink 托管的连接流程与凭据管理，无需自行配置 WhatsApp API 访问。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | WhatsApp 商业消息处理的输入数据或指令 |
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

## How It Works

```text
┌─────────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Agent 会话     │────▶│   ClawLink   │────▶│  WhatsApp Cloud  │
│   (用户对话)     │     │   (OAuth)    │     │      API         │
└─────────────────┘     └──────────────┘     └──────────────────┘
         │                       │                       │
         │  1. 安装插件           │                       │
         │  2. 配对设备           │                       │
         │  3. 连接 WhatsApp      │                       │
         │                       │  4. 安全存储令牌       │
         │                       │  5. 代理转发请求       │
         │                       │                       │
         ▼                       ▼                       ▼
   ┌──────────┐           ┌──────────┐           ┌──────────┐
   │  SKILL   │           │ Dashboard│           │ WhatsApp│
   │  文件    │           │ 鉴权     │           │ Business │
   └──────────┘           └──────────┘           └──────────┘
```

Agent 会话通过 ClawLink 代理访问 WhatsApp Cloud API。ClawLink 负责OAuth 鉴权、令牌存储与请求转发，Agent 只需调用 `clawlink_call_tool` 系列工具即可完成消息发送与管理。

## Install

安装 ClawLink 插件。用户确认后完成完整配置，使 ClawLink 工具在后续会话中可用。

```bash
skill-platform plugins install SkillHub:clawlink-plugin
skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
skill-platform gateway restart
```

重启后提示用户：发送 `/new` 开启新会话，再重新请求 WhatsApp 功能。

## Quick Start

```bash
clawlink_call_tool --tool "whatsapp_get_phone_numbers" --params '{}'
# ...
clawlink_call_tool --tool "whatsapp_send_message" --params '{"phone_number": "+15551234567", "message": "Hello!"}'
# ...
clawlink_call_tool --tool "whatsapp_get_message_templates" --params '{}'
```

**执行步骤**:

1. 准备输入参数并确认运行环境
2. 执行核心操作,处理输入数据
3. 验证处理结果的正确性

**结果处理**: 执行完成后,输出格式化的处理结果供用户查看和保存。结果包含执行状态、输出数据和错误信息(如有)。

## Authentication

所有 WhatsApp 工具调用由 ClawLink 自动鉴权，使用用户已连接的 WhatsApp Business 账户令牌。会话中无需手动传入 API 令牌。ClawLink 安全存储令牌并注入到每个 WhatsApp Business API 请求中。

### Getting Connected

1. 安装 ClawLink 插件（见 Install）。
2. 若未配置，调用 `clawlink_begin_pairing` 配对插件。
3. 打开 `https://claw-link.dev/dashboard?add=whatsapp` 连接 WhatsApp。
4. 调用 `clawlink_list_integrations` 验证连接已激活。

## Connection Management

### 列出连接

```bash
clawlink_list_integrations
```

返回所有已连接的集成。确认返回列表中包含 `whatsapp`。

### 验证连接

```bash
clawlink_list_tools --integration whatsapp
```

返回 WhatsApp 的实时工具目录。这是工具是否可用的权威来源。

### 重新连接

若 WhatsApp 工具缺失或连接报错：

1. 引导用户访问 `https://claw-link.dev/dashboard?add=whatsapp`
2. 用户确认后，调用 `clawlink_list_integrations` 验证
3. 再调用 `clawlink_list_tools --integration whatsapp` 确认工具可用

## Security & Permissions

- 访问范围限定于 OAuth 配置时连接的 WhatsApp Business 账户
- 所有消息发送操作须用户明确确认。WhatsApp 消息会触达真实用户，须确认收件人与内容
- 消息模板须经 WhatsApp 预审通过后方可使用
- 24 小时客服窗口适用于自由文本消息；窗口外只能发送已审批的模板
- 发送前确认收件人手机号，消息发出后无法撤回

## Tool Reference

### Phone Numbers

| Tool | Description | Mode |
|---:|---:|---:|
| `whatsapp_get_phone_numbers` | 列出账户下所有手机号 | Read |
| `whatsapp_get_phone_number` | 获取指定手机号详情 | Read |

### Messages

| Tool(续)| Description | Mode |
|:------:|:------:|:------:|
| `whatsapp_send_message` | 发送文本消息 | Write |
| `whatsapp_send_media` | 发送图片、视频、音频或文档 | Write |
| `whatsapp_send_media_by_id` | 通过已上传的 media ID 发送媒体 | Write |
| `whatsapp_send_location` | 发送带坐标的位置消息 | Write |
| `whatsapp_send_contacts` | 发送联系人卡片 | Write |
| `whatsapp_send_interactive_buttons` | 发送最多 3 个回复按钮的消息 | Write |
| `whatsapp_send_interactive_list` | 发送最多 10 个选项的列表消息 | Write |
| `whatsapp_send_template_message` | 发送已审批的消息模板 | Write |

### Media

| Tool(续)(续)| Description | Mode |
|:------------|------------:|:------------|
| `whatsapp_upload_media` | 上传媒体到 WhatsApp 服务器 | Write |
| `whatsapp_get_media_info` | 获取已上传媒体的元数据与下载 URL | Read |

### Message Templates

| Tool(续)(续)| Description | Mode |
|-------:|:-------|-------:|
| `whatsapp_get_message_templates` | 列出所有消息模板 | Read |
| `whatsapp_get_template_status` | 查询指定模板的审批状态 | Read |
| `whatsapp_create_message_template` | 创建新消息模板 | Write |
| `whatsapp_delete_message_template` | 删除消息模板 | Write |

### Business Profile

| Tool(续)(续)| Description | Mode |
|:------------:|--------------|:-------------|
| `whatsapp_get_business_profile` | 获取业务资料信息 | Read |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|:--:|---:|----|
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

- 多类型消息发送：文本、图片、视频、音频、文档、位置、联系人、交互按钮、列表、模板
- 模板全生命周期管理：创建、查询审批状态、列出、删除，支持窗口外触达
- 媒体上传与复用：上传媒体获取 media ID，后续可通过 ID 复用发送，避免重复上传
- 电话号码与业务资料查询：列出账户下所有手机号及业务资料信息
- 交互式消息：通过按钮（最多 3 个）或列表（最多 10 个选项）收集用户反馈
- ClawLink 托管鉴权：OAuth 令牌由 ClawLink 安全存储与注入，会话中无需手动管理凭据
- 读写分级执行：读操作（list/get/describe）可直接执行，写操作须经 preview 后用户确认再调用
#
## 适用场景

### 订单与物流通知
电商订单发货后，通过模板消息向买家推送发货确认，包含订单号、物流单号与预计送达时间。买家收到消息后可通过交互按钮确认收货或反馈问题。窗口外使用模板触达，窗口内可发送自由文本跟进。

### 客户支持与会话跟进
用户通过 WhatsApp 咨询售后问题，客服在 24 小时窗口内用自由文本回复，并可发送图片（如操作截图）或文档（如说明书）。需要收集结构化反馈时发送交互按钮，让用户快速选择问题类型。

### 预约与提醒触达
医疗、美容、教育等服务行业在预约前通过模板消息提醒客户，包含预约时间、地点与注意事项。模板保证窗口外也能触达，客户可通过按钮确认或改期。适合需要准时提醒且触达率高的场景。

### 营销活动与产品推广
向已订阅用户发送营销活动，使用已审批的模板保证合规触达。可附带产品图片与说明，通过交互列表展示多个促销选项，用户点击后进入对应详情。须确保用户已同意接收营销消息。

## 使用案例

### 案例一：发送发货确认模板消息

订单发货后，向买家发送已审批的 `shipping_confirmation` 模板，填充客户姓名与订单号。

```bash
clawlink_call_tool --tool "whatsapp_send_template_message" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "template_name": "shipping_confirmation",
    "language_code": "en",
    "components": [
      {
        "type": "body",
        "parameters": [
          {"type": "text", "text": "John"},
          {"type": "text", "text": "#12345"}
        ]
      }
    ]
  }'
```

`phone_number_id` 从 `whatsapp_get_phone_numbers` 获取。模板须已通过 WhatsApp 审批，语言代码与模板定义一致。窗口外触达必须使用模板，自由文本会被拒绝。

### 案例二：发送交互按钮收集收货反馈

包裹送达后，向买家发送带"是/否"两个按钮的消息，确认是否收到。

```bash
clawlink_call_tool --tool "whatsapp_send_interactive_buttons" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "header": "Order Update",
    "body": "Has your package arrived?",
    "buttons": [
      {"id": "yes", "title": "Yes"},
      {"id": "no", "title": "No"}
    ]
  }'
```

按钮最多 3 个，每个按钮需有唯一 id 与标题。交互按钮属于自由文本消息，须在 24 小时窗口内发送。买家的回复会触发 webhook，便于后续自动化处理。

### 案例三：上传并发送图片回执

先上传一张回执图片，再用 media ID 发送，避免重复上传同一图片。

```bash
# 上传媒体获取 media ID
clawlink_call_tool --tool "whatsapp_upload_media" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "media_url": "https://example.com/receipt.png",
    "media_type": "image/png"
  }'
# ...
# 通过 URL 直接发送图片（附带说明）
clawlink_call_tool --tool "whatsapp_send_media" \
  --params '{
    "phone_number_id": "PHONE_NUMBER_ID",
    "recipient_phone": "+15551234567",
    "media_url": "https://example.com/receipt.png",
    "caption": "Here is your receipt for order #12345"
  }'
```

`media_url` 须为 WhatsApp 服务器可访问的公网地址。媒体下载 URL 会过期，需要时通过 `whatsapp_get_media_info` 获取新的下载地址。

## Discovery & Execution

### 发现工具

1. 调用 `clawlink_list_integrations` 确认 WhatsApp 已连接
2. 调用 `clawlink_list_tools --integration whatsapp` 查看实时工具目录
3. 将返回列表视为权威来源，不臆测工具是否存在
4. 若用户描述的能力但工具名不明确，调用 `clawlink_search_tools` 传入简短查询与集成名 `whatsapp`
5. 若无 WhatsApp 工具出现，引导用户访问 `https://claw-link.dev/dashboard?add=whatsapp`

### 执行分级

```text
┌─────────────────────────────────────────────────────────────┐
│  读操作（安全）                                             │
│  list → get → describe                                     │
│  例：列出模板 → 查询状态 → 汇报                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  写操作（须确认）                                           │
│  describe → preview → confirm → call                       │
│  例：预览消息 → 用户确认 → 发送                             │
└─────────────────────────────────────────────────────────────┘
```

1. 不熟悉的工具、模糊的请求或任何写操作，先调用 `clawlink_describe_tool`
2. 根据返回的 schema、`whenToUse`、`askBefore`、`safeDefaults`、`examples`、`followups` 组织调用
3. 读操作优先于写操作，以减少歧义
4. 写操作或标记须确认的操作，先调用 `clawlink_preview_tool`
5. 用 `clawlink_call_tool` 执行。仅在 preview 符合用户意图后传入确认
6. 工具调用失败时，报告真实错误，不编造结果

## 异常处理

### 131026 — 消息无法送达
收件人手机号不是有效的 WhatsApp 账户，消息被 WhatsApp 拒绝。处理：确认收件人已在 WhatsApp 注册且号码正确（含国家代码），排除座机或未注册号码。

### 133010 — 收件人未注册 WhatsApp
收件人手机号未在 WhatsApp 注册。处理：与用户确认号码是否正确，或改用短信等其他渠道触达。

### 131047 — 超出 24 小时客服窗口
向超过 24 小时未主动消息的用户发送自由文本时触发。处理：改用已审批的模板消息发送，模板不受窗口限制。

### 模板未找到或未审批
模板名不存在或尚未通过 WhatsApp 审批。处理：调用 `whatsapp_get_message_templates` 确认模板名与状态，仅使用状态为 approved 的模板；新建模板须等待审批通过后再发送。

### 媒体上传失败
`media_url` 不可访问或格式不受支持。处理：确认 URL 为公网可访问地址（非本地路径），且 media_type 与实际文件类型一致；图片支持 png/jpeg，视频支持 mp4，文档支持 pdf/doc 等。

### 工具未找到
工具名在当前目录中不存在。处理：调用 `clawlink_list_tools --integration whatsapp` 核实工具名，以实时目录为准；若工具缺失，按"重新连接"步骤恢复。

### 连接缺失
WhatsApp 未连接。处理：引导用户访问 `https://claw-link.dev/dashboard?add=whatsapp` 完成连接，再调用 `clawlink_list_integrations` 验证。

### 写操作被拒绝
用户未确认写操作。处理：所有写操作（发送消息、上传媒体、创建/删除模板）须用户明确确认后再执行，不要跳过确认步骤。

## FAQ

### 24 小时客服窗口如何计算？
从用户最后一次向商家发送消息的时刻起算 24 小时。窗口内可发送自由文本、图片、交互按钮等任意消息；窗口外只能发送已审批的模板消息。超出窗口发送自由文本会收到 131047 错误。

### 如何获取 phone_number_id？
调用 `whatsapp_get_phone_numbers` 列出账户下所有手机号，返回结果中包含每个号码的 `phone_number_id`。发送消息时须传入该 ID 标识发送方。一个账户可有多个号码，按业务需要选择。

### 消息模板审批需要多久？
审批时长由 WhatsApp 决定，通常为数分钟到数小时不等。可通过 `whatsapp_get_template_status` 查询状态，状态为 `approved` 后方可用于发送。被拒绝的模板需修改后重新提交。

### 模板删除后能否立即重建同名模板？
不能。模板删除后有 30 天冷却期，期间同名模板无法创建。处理：删除前确认不再需要，或使用新名称创建。

### 收件人手机号需要什么格式？
须包含国家代码，例如美国号码以 `+1` 开头，中国号码以 `+86` 开头。不带国家代码会被视为无效号码。发送前务必确认号码完整，消息发出后无法撤回。

### 媒体下载 URL 会过期吗？
会。上传媒体后返回的下载 URL 有时效，过期后无法访问。需要下载时调用 `whatsapp_get_media_info` 获取新的下载地址。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 自由文本消息受 24 小时客服窗口限制，窗口外只能使用已审批模板
- 模板须经 WhatsApp 审批，审批时长与结果由 WhatsApp 决定
- 模板删除后有 30 天冷却期，期间无法重建同名模板
- 媒体下载 URL 会过期，需调用 `whatsapp_get_media_info` 刷新
- 交互按钮最多 3 个，列表消息最多 10 个选项，超出需拆分多条
- 收件人手机号须包含国家代码，否则发送失败
- 消息一旦发出无法撤回，发送前须确认收件人与内容
- 依赖 ClawLink 托管鉴权，ClawLink 连接异常时所有工具不可用

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "WhatsApp 商业消息处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "whatsapp-messaging"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
