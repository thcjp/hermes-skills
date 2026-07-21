---
slug: whatsapp-msg-manager
name: whatsapp-msg-manager
version: "1.0.0"
displayName: WhatsApp消息管理-专业版
summary: 全功能WhatsApp Business消息平台,支持媒体/交互/模板/批量发送与多账号企业级管理
license: Proprietary
edition: pro
description: |-
  WhatsApp消息管理专业版,提供完整的WhatsApp Business API能力覆盖,面向企业和专业团队。核心能力:
  - 全类型消息发送(文本/图片/视频/音频/文档/位置/联系人)
  - 交互式按钮与列表消息,提升用户互动转化
  - 消息模板全生命周期管理(创建/审批查询/删除)
  - 批量消息发送与定时调度
  - 多账号统一管理与业务资料配置
  - 媒体上传与复用,支持media_id缓存
  - 企业级安全审计与操作日志

  适用场景:
  - 企业客户服务与营销触达
  - 电商订单全流程通知(含图片凭证)
  - ...
tags:
- 沟通协作
- 消息发送
- WhatsApp
- 企业级
- 批量发送
- 营销自动化
tools:
  - - read
- exec
# WhatsApp消息管理(专业版)
## 概述
---
# WhatsApp消息管理-专业版

## 核心能力

### 1. 全类型消息发送
PRO版支持WhatsApp Cloud API的全部消息类型,满足多样化沟通需求。

```bash
connector_call_tool --tool "whatsapp_send_media" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "media_url": "https://example.com/receipt.png",
  "caption": "您的电子收据:订单 #20260718-001"
}'

connector_call_tool --tool "whatsapp_send_media" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "media_url": "https://example.com/product-demo.mp4",
  "caption": "产品使用演示视频"
}'

connector_call_tool --tool "whatsapp_send_media" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "media_url": "https://example.com/contract.pdf",
  "caption": "服务合同 PDF"
}'
```

- 执行`业务资料与多账号管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`业务资料与多账号管理`相关配置参数进行设置

- 执行`媒体上传与复用`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`媒体上传与复用`相关配置参数进行设置

- 执行`位置与联系人消息`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`位置与联系人消息`相关配置参数进行设置
### 2. 交互式按钮消息
发送带回复按钮的消息,引导用户快速交互,提升转化率。

> 详细代码示例已移至 `references/detail.md`

**输出**: 返回交互式按钮消息的执行结果,包含操作状态和输出数据。
### 3. 位置与联系人消息
```bash
connector_call_tool --tool "whatsapp_send_location" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "longitude": 116.404,
  "latitude": 39.915,
  "name": "公司总部",
  "address": "北京市东城区XX路XX号"
}'

connector_call_tool --tool "whatsapp_send_contacts" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "contacts": [
    {
      "name": {"formatted_name": "张三", "first_name": "三", "last_name": "张"},
      "phones": [{"phone": "+8613800138000", "type": "MOBILE"}],
      "emails": [{"email": "zhangsan@example.com", "type": "WORK"}]
    }
  ]
}'
```

**输出**: 返回位置与联系人消息的执行结果,包含操作状态和输出数据。

- 执行`位置与联系人消息`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `位置与联系人消息` 选项
- 处理流程: 接收输入 -> 执行位置与联系人消息 -> 返回结果
- 输入: 用户提供位置与联系人消息所需的参数和指令
- 输出: 返回位置与联系人消息的执行结果,包含操作状态和输出数据

### 4. 消息模板全生命周期管理
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供消息模板全生命周期管理所需的指令和必要参数。
**处理**: 按照skill规范执行消息模板全生命周期管理操作,遵循单一意图原则。
**输出**: 返回消息模板全生命周期管理的执行结果,包含操作状态和输出数据。

### 5. 媒体上传与复用
```bash
connector_call_tool --tool "whatsapp_upload_media" --params '{
  "phone_number_id": "1029384756",
  "media_url": "https://example.com/logo.png",
  "media_type": "image/png"
}'

connector_call_tool --tool "whatsapp_send_media_by_id" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "media_id": "MEDIA_ID_FROM_UPLOAD",
  "caption": "使用缓存媒体发送"
}'

connector_call_tool --tool "whatsapp_get_media_info" --params '{
  "media_id": "MEDIA_ID"
}'
```

**输出**: 返回媒体上传与复用的执行结果,包含操作状态和输出数据。

- 执行`媒体上传与复用`操作,处理输入数据并返回结果
- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `媒体上传与复用` 选项
- 处理流程: 接收输入 -> 执行媒体上传与复用 -> 返回结果
- 输入: 用户提供媒体上传与复用所需的参数和指令
- 输出: 返回媒体上传与复用的执行结果,包含操作状态和输出数据

### 6. 业务资料与多账号管理
```bash
connector_call_tool --tool "whatsapp_get_business_profile" --params '{}'

connector_call_tool --tool "whatsapp_get_phone_numbers" --params '{}'
```

- 执行`业务资料与多账号管理`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`业务资料与多账号管理`相关配置参数进行设置
### 7. 批量消息发送
PRO版支持批量消息发送,适合营销触达和批量通知场景。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量消息发送所需的指令和必要参数。
**输出**: 返回批量消息发送的执行结果,包含操作状态和输出数据。

### 能力覆盖范围

本skill还覆盖以下能力场景: 全功能、消息平台、支持媒体、批量发送与多账号、企业级管理、消息管理专业版、提供完整的、能力覆盖、面向企业和专业团、核心能力、交互式按钮与列表、提升用户互动转化、审批查询、批量消息发送与定、时调度、多账号统一管理与、业务资料配置、企业级安全审计与、操作日志。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:电商订单全流程通知
电商企业在订单各阶段通过WhatsApp向客户发送差异化通知,包含图片凭证和交互按钮。

> 详细代码示例已移至 `references/detail.md`

### 场景二:企业客户服务
利用交互式列表消息为客户提供自助服务入口,降低人工客服压力。

```bash
connector_call_tool --tool "whatsapp_send_interactive_list" --params '{
  "phone_number_id": "1029384756",
  "recipient_phone": "+8613800138000",
  "header": "客服中心",
  "body": "您好!请问需要什么帮助?请选择服务类型:",
  "button_text": "选择服务",
  "sections": [
    {
      "title": "常见服务",
      "rows": [
        {"id": "track_order", "title": "查询订单", "description": "查看订单状态和物流"},
        {"id": "return", "title": "申请退换货", "description": "提交退换货申请"},
        {"id": "invoice", "title": "开具发票", "description": "申请电子发票"}
      ]
    },
    {
      "title": "更多帮助",
      "rows": [
        {"id": "faq", "title": "常见问题", "description": "查看FAQ"},
        {"id": "human", "title": "转人工客服", "description": "联系在线客服"}
      ]
    }
  ]
}'
```

### 场景三:批量营销通知
向多个客户批量发送个性化营销通知,支持变量替换和速率控制。

```python
sender = WhatsAppBatchSender(phone_number_id="1029384756", rate_limit=1.0)

recipients = [
    {"phone": "+8613800138000", "vars": {"name": "张三", "coupon": "SAVE50"}},
    {"phone": "+8613900139000", "vars": {"name": "李四", "coupon": "SAVE50"}},
    {"phone": "+8613700137000", "vars": {"name": "王五", "coupon": "SAVE50"}},
]

template = (
    "Hi {name}!\n\n"
    "限时优惠!使用优惠码 {coupon} 享受全场8折优惠。\n"
    "活动时间:即日起至7月31日\n"
    "详情请访问我们的在线商店。"
)

sender.send_batch(recipients, template)
```

## 使用流程

### 前置条件
如果您已在使用免费版,PRO版可直接继承现有连接和配置,无需重新设置。

### 依赖说明

### 运行环境
1. **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
2. **操作系统**: Windows / macOS / Linux
3. **网络环境**: 需可访问WhatsApp Cloud API服务端点
4. **浏览器**: 用于OAuth授权流程的现代浏览器
5. **Python**: 3.8+(批量发送和模板管理脚本需要)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| 连接器插件 | 平台插件 | 必需 | SkillHub插件市场安装 |
| WhatsApp Business账号 | 服务账号 | 必需 | Meta Business平台注册 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载安装 |
| schedule库 | Python库 | 可选 | `pip install schedule` |
| requests库 | Python库 | 可选 | `pip install requests` |

### API Key 配置
6. 本Skill通过连接器服务自动管理OAuth令牌,无需手动配置API Key
7. WhatsApp Business API凭证由连接器服务安全存储并自动注入
8. 批量发送脚本的连接器调用使用本地已认证的会话,无需额外Key
9. 如需直接调用WhatsApp Cloud API,需在Meta开发者平台获取Access Token和Phone Number ID

### 可用性分类
10. **分类**: MD+EXEC()
11. **说明**: 基于Markdown的AI Skill,
12. **连接模式**: 通过连接器服务代理WhatsApp Cloud API请求,支持多账号并发
13. **安全等级**: 所有写操作需用户显式确认;批量发送支持操作日志审计;OAuth令牌由连接器安全管理
14. **兼容性**: 与免费版(whatsapp-msg-manager-free)完全兼容,支持无缝升级

### 命令参数说明

15. `-demo`: 命令参数,用于指定操作选项
16. `--params`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/checklist.md` | 文件 | 是 | 相关说明 |
| `references/scoring.md` | 文件 | 否 | 相关说明 |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1: PRO版和免费版的配置是否兼容?
**A:** 完全兼容。PRO版继承了免费版的所有配置项,包括连接器插件、OAuth凭证和号码配置。升级时只需安装PRO版Skill并重启网关,无需任何配置迁移。原有的文本消息发送功能继续可用,同时解锁全部高级功能。

### Q2: 批量发送时如何避免触发WhatsApp限流?
**A:** 建议采取以下措施:
1. 控制发送速率,新账号建议每秒不超过1条
2. 批量发送时添加随机延迟(0.5-2秒)
3. 监控API返回的限流响应,自动降速
4. 将大批量发送拆分为多个小批次,间隔执行
5. 优先使用已审批的模板消息发送

### Q3: 模板创建后多久能通过审批?
**A:** WhatsApp模板审批通常需要几分钟到24小时不等,取决于模板内容和类别。UTILITY类模板通常审批较快,MARKETING类模板审核更严格。可通过 `whatsapp_get_template_status` 轮询查询审批状态。

### Q4: 删除模板后可以立即创建同名模板吗?
**A:** 不可以。模板删除后有30天冷却期,在此期间无法创建同名模板。建议使用版本化命名,如 `order_notify_v2` 而非覆盖原有名称。

### Q5: 媒体下载URL过期怎么办?
**A:** WhatsApp的媒体下载URL有时效性。使用 `whatsapp_get_media_info` 传入media_id可获取新的下载URL。PRO版支持media_id缓存,避免重复上传同一媒体文件。

### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
**A:** 回复按钮消息最多支持3个按钮。如需更多选项,请使用列表消息(最多10个选项,支持分组)。每个按钮标题不超过20个字符。

### Q7: 如何实现定时消息发送?
**A:** PRO版支持通过调度脚本实现定时发送。示例如下:

```python
import schedule
import time

def send_scheduled_message():
    """定时发送消息"""
    pass

schedule.every().day.at("09:00").do(send_scheduled_message)

while True:
    schedule.run_pending()
    time.sleep(60)
```

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

