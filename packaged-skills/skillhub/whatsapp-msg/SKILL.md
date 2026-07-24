---
slug: "whatsapp-msg"
name: "whatsapp-msg"
version: 1.0.1
displayName: "WhatsApp消息工具(专业版)"
summary: "WhatsApp消息全能力版：批量发送、历史回填、群组管理、持续同步与高级搜索。"
license: "Proprietary"
edition: "pro"
description: |-
  WhatsApp 消息工具（专业版）面向团队与企业用户，在免费版基础消息能力之上新增批量操作引擎、历史回填、群组管理、持续同步与高级搜索。支持从消息发送到数据归档的完整工作流。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - 沟通协作
  - 即时通讯
  - WhatsApp
  - 批量操作
  - 群组管理
  - 消息自动化
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "WhatsApp,社交,通信"
category: "Communication"
---
# WhatsApp消息工具(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| WhatsApp消息工具(专业版)批量发送 | 不支持 | 支持 |
| WhatsApp消息工具(专业版)群组管理 | 不支持 | 支持 |
| WhatsApp消息工具(专业版)持续同步 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |

## 核心能力

| 类别 | 能力 | 数量 | 免费版 |
|:-----|:-----|:-----|:-----|
| 基础消息 | 文本/文件发送/聊天列表 | 3 | 是 |
| 基础搜索 | 关键词/日期搜索 | 2 | 是 |
| 认证 | QR登录/健康检查 | 2 | 是 |
| 批量操作 | 批量文本/批量文件/批量群组/批量搜索 | 4 | 否 |
| 历史回填 | 全量回填/增量同步/媒体下载 | 3 | 否 |
| 群组管理 | 创建/邀请/退出/信息/参与者 | 5 | 否 |
| 持续同步 | 实时同步/事件推送/断线重连 | 3 | 否 |
| 高级搜索 | 正则/多维过滤/全文索引/跨格式 | 4 | 否 |
| 联系人提取 | vCard解析/电话归档/交叉引用 | 3 | 否 |
| 数据统计 | 发送量/活跃度/响应率/时段分析 | 4 | 否 |
| 多账号 | 切换/并行/隔离/凭证管理 | 4 | 否 |
### 基础消息

针对基础消息,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供基础消息相关的配置参数、输入数据和处理选项.
**输出**: 返回基础消息的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础消息`的配置文档进行参数调优
### 基础搜索

针对基础搜索,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供基础搜索相关的配置参数、输入数据和处理选项.
**输出**: 返回基础搜索的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础搜索`的配置文档进行参数调优
### 批量操作

针对批量,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供批量操作相关的配置参数、输入数据和处理选项.
**输出**: 返回批量操作的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量操作`的配置文档进行参数调优
#
## 适用场景

### 场景一：批量通知推送（运营视角）

需要向 50 个客户发送版本更新通知。批量发送引擎自动控制速率、支持个性化模板与失败重试，避免触发反垃圾机制.
```bash
# 批量文本发送
python wa_batch_sender.py \
  --store ~/.wacli \
  --recipients "contacts.json" \
  --message "您好 "msg_result"，我们的产品已更新至 v2.1.0，新增实时协作功能。" \
  --rate_limit 3 \
  --retry 3 \
  --dry_run false
```

```python
# 批量发送配置
batch_config = {
    "recipients": [
        {"phone": "+8613800138000", "name": "张三", "company": "A公司"},
        {"phone": "+8613900139000", "name": "李四", "company": "B公司"},
        {"phone": "+8613700137000", "name": "王五", "company": "C公司"}
    ],
    "message_template": "您好 "msg_metadata"（"msg_metadata"），\n\n产品已更新至 v2.1.0。\n新增功能：实时协作、自动保存。\n\n如有疑问请随时联系。",
    "rate_limit_sec": 3,          # 每条间隔 3 秒
    "max_per_hour": 100,           # 每小时最多 100 条
    "retry_on_failure": 3,
    "retry_delay_sec": 30,
    "respect_quiet_hours": True,   # 尊重静默时段
    "quiet_hours": {"start": "22:00", "end": "08:00"}
}
```

### 场景二：历史回填归档（合规视角）

需要拉取与某客户过去 6 个月的全部聊天记录归档，用于合规审计。回填引擎分批拉取，支持断点续传.
```bash
# 历史回填
wacli history backfill \
  --chat "8613800138000@s.whatsapp.net" \
  --requests 5 \
  --count 100 \
  --output "archive/customer_zhangsan/"
# ...
# 回填所有聊天
wacli history backfill \
  --all-chats \
  --requests 3 \
  --count 50 \
  --output "archive/all/"
```

```python
# 回填配置
backfill_config = {
    "target_chat": "8613800138000@s.whatsapp.net",
    "requests": 5,              # 拉取轮数
    "count_per_request": 100,   # 每轮拉取 100 条
    "output_dir": "archive/customer_zhangsan/",
    "format": "json",           # json | csv | sqlite
    "include_media": True,      # 下载媒体文件
    "media_dir": "archive/customer_zhangsan/media/",
    "resume": True,             # 断点续传
    "progress_file": "archive/progress.json"
}
```

### 场景三：群组运营管理（运营视角）

创建项目群组、邀请参与者、管理群组信息。所有操作通过命令行完成，支持批量邀请.
```bash
# 创建群组
wacli group create --name "项目协作组" --participants "+8613800138000,+8613900139000"
# ...
# 添加参与者
wacli group add-participants --group "1234567890-123456789@g.us" --participants "+8613700137000"
# ...
# 退出群组
wacli group leave --group "1234567890-123456789@g.us"
# ...
# 获取群组信息
wacli group info --group "1234567890-123456789@g.us"
```

### 场景四：持续同步与事件推送（开发者视角）

开启持续同步，实时接收新消息事件，用于自动化响应与消息流处理.
```bash
# 持续同步（前台运行）
wacli sync --follow
# ...
# 后台持续同步 + 事件输出
wacli sync --follow --json --output "events.jsonl" &
```

```python
# 同步配置
sync_config = {
    "mode": "follow",            # follow | backfill | hybrid
    "output": "events.jsonl",    # 事件流输出文件
    "format": "json",
    "filters": {
        "chats": ["8613800138000@s.whatsapp.net"],  # 限定同步聊天
        "exclude_groups": False,
        "media_auto_download": True
    },
    "reconnect": {
        "enabled": True,
        "max_retries": 10,
        "backoff": "exponential",
        "initial_delay_sec": 5
    },
    "webhook": {                 # 可选：事件推送到 Webhook
        "url": "https://your-app.com/webhook/whatsapp",
        "events": ["message", "receipt", "presence"]
    }
}
```

## 使用流程

### 120 秒上手

1. 确认已通过免费版完成 QR 码认证
2. 准备批量发送的联系人列表
3. 配置批量发送或回填参数
4. 执行批量操作或开启持续同步
5. 监控统计报表

### 批量文件发送

```bash
python wa_batch_sender.py \
  --store ~/.wacli \
  --recipients "contacts.json" \
  --file "/path/to/report.pdf" \
  --caption ""msg_status"您好，这是您本月的使用报告。" \
  --rate_limit 5 \
  --dry_run true
```

### 高级搜索

```bash
# 正则搜索
wacli messages search --regex "合同.*[0-9]{4}年" --limit 50 --json
# ...
# 多维度过滤
wacli messages search \
  --chat "8613800138000@s.whatsapp.net" \
  --after 2026-01-01 \
  --before 2026-07-31 \
  --from-me false \
  --has-media true \
  --limit 100 \
  --json
# ...
# 全文索引搜索
wacli messages search --fulltext "项目交付时间" --index "whatsapp.idx" --limit 30
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | whatsapp-msg处理的内容输入 |,  |
| content | string | 否 | whatsapp-msg处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "msg 相关配置参数",
    result: "msg 相关配置参数",
    result: "msg 相关配置参数",
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：可访问 WhatsApp 服务器的网络连接
- **手机**：已安装 WhatsApp 的手机（保持在线用于同步）
- **Node.js**：18+（运行 CLI 工具与同步引擎）
- **Python**：3.10+（运行批量发送与回填脚本）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| wacli | CLI 工具 | 必需 | 包管理器安装或源码编译 |
| Node.js 18+ | 运行时 | 必需 | 运行 CLI 工具与同步引擎 |
| Python 3.10+ | 运行时 | 批量操作必需 | 官方网站下载 |
| SQLite | 数据库 | 内置 | CLI 工具自带，消息存储 |
| jq | CLI 工具 | 推荐 | 用于 JSON 输出解析 |
| Webhook 接收端 | 服务 | 同步推送可选 | 自行部署 HTTP 接收服务 |
| 数据库 | 服务 | 统计推荐 | 用于历史数据归档与报表 |

### API Key 配置
- **WhatsApp 凭证**：通过 QR 码登录获取，由 CLI 持久化存储
- **多账号凭证**：每个账号独立 `--store` 目录，隔离存储
- **Webhook Secret**：配置在 `WEBHOOK_SECRET` 中，用于同步回调验签
- **禁止**：在 SKILL.md 或脚本中硬编码任何凭证或密钥
- **安全建议**：凭证泄露后需在 WhatsApp 中解除关联设备并重新认证

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 Claude Sonnet 进行消息分析与决策，Haiku 进行批量消息生成
- **数据存储**：历史消息与统计数据可归档到 `关系型数据库` 数据库做长期分析与合规审计

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 批量发送策略表

| 策略 | 间隔 | 每小时上限 | 适用场景 | 风险 |
|---:|:---|---:|---:|:---|
| 保守 | 10 秒 | 30 | 新客户首次接触 | 极低 |
| 标准 | 5 秒 | 100 | 日常通知推送 | 低 |
| 快速 | 3 秒 | 200 | 紧急通知 | 中 |
| 批量 | 1 秒 | 500 | 内部团队通知 | 高（需授权） |

### 历史回填配置

```yaml
backfill:
  strategy: "incremental"       # full | incremental | hybrid
  requests: 5
  count_per_request: 100
  output:
    format: "sqlite"             # json | csv | sqlite
    dir: "archive/"
    compress: true
  media:
    download: true
    dir: "archive/media/"
    max_size_mb: 50
  resume:
    enabled: true
    progress_file: "archive/progress.json"
  filters:
    date_range:
      after: "2026-01-01"
      before: "2026-07-31"
    exclude_types: ["sticker", "voice_note"]   # 跳过贴纸与语音
```

### 群组管理命令

```bash
# 创建群组
wacli group create --name "群组名" --participants "+8613800138000,+8613900139000"
# ...
# 邀请参与者
wacli group add-participants --group "<group_jid>" --participants "+8613700137000"
# ...
# 移除参与者
wacli group remove-participants --group "<group_jid>" --participants "+8613700137000"
# ...
# 修改群组名称
wacli group set-name --group "<group_jid>" --name "新名称"
# ...
# 修改群组描述
wacli group set-description --group "<group_jid>" --description "群组描述"
# ...
# 获取邀请链接
wacli group invite-link --group "<group_jid>"
# ...
# 退出群组
wacli group leave --group "<group_jid>"
```

### 持续同步配置

```yaml
sync:
  mode: "follow"                 # follow | backfill | hybrid
  output: "events.jsonl"
  format: "json"
  filters:
    chats: []                    # 空=同步所有聊天
    exclude_groups: false
    media_auto_download: true
  reconnect:
    enabled: true
    max_retries: 10
    backoff: "exponential"
    initial_delay_sec: 5
  webhook:
    enabled: false
    url: ""
    secret: "${WEBHOOK_SECRET}"
    events: ["message", "receipt", "presence"]
```

### 联系人提取

```bash
# 提取所有联系人（vCard 格式）
wacli contacts export --format vcard --output "contacts.vcf"
# ...
# 提取为 JSON
wacli contacts export --format json --output "contacts.json"
# ...
# 交叉引用 LID 与 JID
wacli contacts resolve --input "contacts.json" --output "resolved.json"
```

### 数据统计维度

| 报表 | 指标 | 频率 | 输出 |
|:------:|--------|:-------|:------:|
| 发送量 | 每日/每周/每月消息数 | 每日 | JSON+CSV |
| 活跃度 | 活跃聊天/沉默聊天/增长率 | 每周 | 图表数据 |
| 响应率 | 发送→回复/平均响应时间 | 每月 | 排序表 |
| 时段分析 | 消息量按小时分布 | 每周 | 热力图 |
| 媒体统计 | 图片/文件/语音占比 | 每月 | 饼图数据 |

## 常见问题

### Q1：批量发送被 WhatsApp 限流？
A：降低发送频率——间隔提升至 5-10 秒，每小时上限降至 30-50 条。避免向未互动联系人发送。严重时账号会被临时封禁 24-48 小时.
### Q2：历史回填不完整？
A：回填需要手机在线且 WhatsApp 处于活跃状态。`requests` 与 `count_per_request` 决定拉取量，增加轮数可拉取更多历史。部分旧消息可能已被服务器清理无法恢复.
### Q3：持续同步断线频繁？
A：检查手机网络稳定性与 WhatsApp 后台保活。iOS 设备需关闭后台应用刷新限制。`reconnect` 配置指数退避重连，避免频繁重试被封.
### Q4：全文索引构建很慢？
A：索引构建时间取决于历史消息量。1 万条约需 5 分钟，10 万条约需 30 分钟。建议在非高峰时段构建，后续增量更新很快.
### Q5：群组创建失败？
A：WhatsApp 限制群组参与者数量（最多 1024 人）。首次创建建议不超过 50 人，后续逐步添加。确保所有手机号已激活 WhatsApp.
### Q6：多账号同时运行冲突？
A：每个账号使用独立 `--store` 目录完全隔离。同一手机号只能在一个 CLI 实例中登录——第二个实例会挤掉优秀个.
### Q7：专业版与免费版命令是否兼容？
A：完全兼容。专业版包含免费版所有 `send text`、`send file`、`messages search` 等命令，额外扩展批量、回填、群组与同步命令。免费版脚本无需修改即可在专业版运行.
### Q8：vCard 联系人怎么提取电话号码？
A：`contacts export --format json` 返回结构化数据，每个联系人包含姓名与电话号码。vCard 格式（`.vcf`）可直接导入通讯录.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

