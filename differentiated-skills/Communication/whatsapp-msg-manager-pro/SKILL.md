---
slug: whatsapp-msg-manager-pro
name: whatsapp-msg-manager-pro
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
WhatsApp消息管理专业版是一款面向企业和专业团队的全功能WhatsApp Business消息平台。在免费版文本消息能力的基础上,PRO版全面覆盖WhatsApp Cloud API的全部消息类型,包括媒体消息、交互式按钮、列表消息、位置消息、联系人卡片等,同时提供消息模板全生命周期管理、批量发送、定时调度、多账号统一管理等企业级能力。

PRO版与免费版完全兼容,升级后原有连接和配置无需任何更改,即可获得全部高级功能。适合企业客户服务、电商营销触达、多租户消息管理等复杂业务场景。

### PRO版增强能力总览
| 能力分类 | 具体功能 | 免费版 | PRO版 |
|:---------|:---------|:-------|:------|
| 文本消息 | 纯文本发送 | 支持 | 支持 |
| 媒体消息 | 图片/视频/音频/文档 | - | 支持 |
| 媒体消息 | 通过media_id复用已上传媒体 | - | 支持 |
| 交互消息 | 回复按钮(最多3个) | - | 支持 |
| 交互消息 | 列表消息(最多10项) | - | 支持 |
| 特殊消息 | 位置消息 | - | 支持 |
| 特殊消息 | 联系人卡片 | - | 支持 |
| 模板管理 | 浏览模板 | 支持 | 支持 |
| 模板管理 | 创建新模板 | - | 支持 |
| 模板管理 | 删除模板 | - | 支持 |
| 模板管理 | 查询审批状态 | 支持 | 支持 |
| 批量操作 | 批量消息发送 | - | 支持 |
| 批量操作 | 定时消息调度 | - | 支持 |
| 账号管理 | 多账号切换 | - | 支持 |
| 账号管理 | 业务资料查询 | - | 支持 |
| 媒体管理 | 媒体上传 | - | 支持 |
| 媒体管理 | 媒体信息查询 | - | 支持 |
| 技术支持 | 支持级别 | 社区 | 专属SLA |

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

### 2. 交互式按钮消息
发送带回复按钮的消息,引导用户快速交互,提升转化率。

> 详细代码示例已移至 `references/detail.md`

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

### 4. 消息模板全生命周期管理

> 详细代码示例已移至 `references/detail.md`

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

### 6. 业务资料与多账号管理
```bash
connector_call_tool --tool "whatsapp_get_business_profile" --params '{}'

connector_call_tool --tool "whatsapp_get_phone_numbers" --params '{}'
```

### 7. 批量消息发送
PRO版支持批量消息发送,适合营销触达和批量通知场景。

> 详细代码示例已移至 `references/detail.md`

## 使用场景
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

## 不适用场景

以下场景WhatsApp消息管理-专业版不适合处理：

- 逆向工程闭源API
- API安全渗透测试
- 非标准协议集成


## 触发条件

需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于非本工具能力范围的需求。


## 快速开始
### 前置条件
如果您已在使用免费版,PRO版可直接继承现有连接和配置,无需重新设置。

### 依赖说明
```bash
skill-platform plugins install SkillHub:connector-plugin
skill-platform config set tools.alsoAllow '["connector-plugin"]' --strict-json
skill-platform gateway restart

connector_begin_pairing
connector_list_integrations
connector_list_tools --integration whatsapp

connector_call_tool --tool "whatsapp_get_phone_numbers" --params '{}'
connector_call_tool --tool "whatsapp_get_business_profile" --params '{}'
```

### 从免费版升级
```bash
skill-platform skills install whatsapp-msg-manager-pro

skill-platform gateway restart

```

## 配置示例
### PRO版企业级配置

> 详细代码示例已移至 `references/detail.md`

### 消息发送队列配置
```python
QUEUE_CONFIG = {
    "worker_count": 3,              # 并发工作线程数
    "batch_size": 50,              # 每批处理数量
    "rate_limit_per_second": 10,   # 每秒最大发送数
    "retry_config": {
        "max_attempts": 3,
        "backoff_seconds": [5, 30, 120],
        "retry_on_errors": ["131026", "timeout"]
    },
    "priority_levels": {
        "high": 0,     # 验证码、紧急通知
        "normal": 1,   # 订单通知
        "low": 2       # 营销消息
    }
}
```

## 最佳实践
### 1. 模板管理策略

> 详细代码示例已移至 `references/detail.md`

### 2. 媒体缓存优化
```python
import hashlib
import requests
from datetime import datetime, timedelta

class MediaCache:
    """媒体ID缓存,避免重复上传"""

    def __init__(self):
        self.cache = {}  # {url_hash: {"media_id": "...", "expires": ...}}
    def get_cached(self, media_url: str) -> str:
        """获取缓存的media_id"""
        url_hash = hashlib.md5(media_url.encode()).hexdigest()
        entry = self.cache.get(url_hash)
        if entry and datetime.now() < entry["expires"]:
            return entry["media_id"]
        return None

    def set_cache(self, media_url: str, media_id: str, ttl_hours: int = 24):
        """缓存media_id"""
        url_hash = hashlib.md5(media_url.encode()).hexdigest()
        self.cache[url_hash] = {
            "media_id": media_id,
            "expires": datetime.now() + timedelta(hours=ttl_hours)
        }
```

### 3. 批量发送速率控制
WhatsApp API有速率限制,批量发送时需合理控制发送频率,避免触发限流。

| 账号类型 | 建议速率 | 每日上限 | 说明 |
|:---------|:---------|:---------|:-----|
| 新账号 | 1条/秒 | 1000条 | 前7天建议保守发送 |
| 普通账号 | 5条/秒 | 10000条 | 已验证的Business账号 |
| 验证账号 | 10条/秒 | 100000条 | Meta验证的品牌账号 |

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

### 已知限制
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

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络环境**: 需可访问WhatsApp Cloud API服务端点
- **浏览器**: 用于OAuth授权流程的现代浏览器
- **Python**: 3.8+(批量发送和模板管理脚本需要)

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
- 本Skill通过连接器服务自动管理OAuth令牌,无需手动配置API Key
- WhatsApp Business API凭证由连接器服务安全存储并自动注入
- 批量发送脚本的连接器调用使用本地已认证的会话,无需额外Key
- 如需直接调用WhatsApp Cloud API,需在Meta开发者平台获取Access Token和Phone Number ID

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
- **连接模式**: 通过连接器服务代理WhatsApp Cloud API请求,支持多账号并发
- **安全等级**: 所有写操作需用户显式确认;批量发送支持操作日志审计;OAuth令牌由连接器安全管理
- **兼容性**: 与免费版(whatsapp-msg-manager-free)完全兼容,支持无缝升级

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
