---
slug: whatsapp-image-tool-pro
name: whatsapp-image-tool-pro
version: "1.0.0"
displayName: WhatsApp图片发送-专业版
summary: 企业级WhatsApp多媒体消息平台，支持批量发送、视频音频文档、定时发送、群组消息与模板管理。
license: MIT
edition: pro
description: |-
  WhatsApp 多媒体消息发送专业版，面向企业团队与营销机构的高级消息分发方案。

  核心能力:
  - 批量多媒体发送（图片/视频/音频/文档）
  - 定时发送与延时队列
  - 群组消息与广播列表
  - 消息模板管理（预设模板复用）
  - 发送报告与状态追踪
  - 联系人列表管理
  - 个性化变量替换（按收件人定制内容）
  - 发送频率控制（防封号）
  - 失败重试与断点续传
  - 多账号轮询发送

  适用场景:
  - 企业营销活动批量推送
  - 客户服务多媒体消息
  - 电商订单通知与商品图
  - 团队协作文件分发
  - 定时提醒与公告

  差异化:
  - 专业版支持完整多媒体类型（图片/视频/音频/文档）
  - 内置批量发送与定时发送工作流
  - 支持消息模板与个性化变量替换
  - 与免费版完全兼容，已有配置可无缝迁移
  - 提供发送频率控制，降低封号风险

  触发关键词: 批量发送, WhatsApp 营销, 定时发送, 群组消息, 消息模板, 多媒体发送, broadcast, scheduled message
tags:
- Creative
- 消息发送
- WhatsApp
- 专业版
- 批量处理
- 企业级
- 营销
tools:
- read
- exec
---

# WhatsApp 图片发送工具 - 专业版

## 概述

WhatsApp 多媒体消息发送专业版是一款面向企业团队与营销机构的高级消息分发平台。在免费版单图发送能力之上，专业版扩展了批量发送、多媒体支持、定时发送、群组消息、模板管理等企业级能力。

专业版采用发送队列架构，支持频率控制、失败重试、断点续传，可稳定处理大批量消息分发任务。同时完全兼容免费版工作流，已有配置可无缝迁移。

### 免费版与专业版能力对比

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 单图发送 | 支持 | 支持 |
| 说明文字 | 支持 | 支持 |
| 图片格式 | JPG/PNG/GIF | 全格式 |
| 视频发送 | 不支持 | 支持 |
| 音频发送 | 不支持 | 支持 |
| 文档发送 | 不支持 | 支持 |
| 批量发送 | 不支持 | 100+ 并行 |
| 定时发送 | 不支持 | 支持 |
| 群组消息 | 不支持 | 支持 |
| 消息模板 | 不支持 | 支持 |
| 个性化变量 | 不支持 | 支持 |
| 发送报告 | 基础确认 | 详细报告 |
| 频率控制 | 不支持 | 支持 |
| 失败重试 | 不支持 | 支持 |
| 多账号轮询 | 不支持 | 支持 |
| 优先支持 | 社区 | 优先响应 |

## 核心能力

### 1. 多媒体类型支持

专业版支持完整多媒体类型：

| 类型 | 格式 | 适用场景 |
|:-----|:-----|:---------|
| 图片 | JPG/PNG/GIF/WebP | 照片、截图、设计稿 |
| 视频 | MP4/MOV/AVI | 宣传片、教程、演示 |
| 音频 | MP3/WAV/AAC | 语音消息、音乐 |
| 文档 | PDF/DOCX/XLSX/PPTX | 合同、报告、资料 |

### 2. 批量发送

支持单任务发送 100+ 消息：

```text
输入收件人列表（CSV/JSON）
      ↓
任务调度器分配并行发送
      ↓
频率控制（防封号）
      ↓
失败重试 + 结果聚合
      ↓
生成发送报告
```

### 3. 定时发送

支持指定时间发送消息：

- 单次定时（指定日期时间）
- 重复定时（每日/每周/每月）
- 时区感知（跨时区发送）

### 4. 群组消息与广播

- 单条消息发送至群组
- 广播列表（多收件人单独发送）
- 群组管理（创建/删除/查询）

### 5. 消息模板管理

预设消息模板，支持变量替换：

```text
模板：亲爱的 {name}，您的订单 {order_id} 已发货
变量：{name}=张三, {order_id}=A12345
结果：亲爱的 张三，您的订单 A12345 已发货
```

### 6. 发送频率控制

防止因发送过快导致封号：

- 每分钟发送上限
- 随机延时（模拟人工）
- 每日发送总量限制
- 多账号轮询分流

## 使用场景

### 场景 1：电商订单批量通知

某电商商家需要向 100 个客户发送订单发货通知（含商品图片）。

**批量配置 `batch-send.json`：**

```json
{
  "project": "订单发货通知",
  "template": "亲爱的 {name}，您的订单 {order_id} 已发货，预计 {delivery_date} 送达",
  "messages": [
    {
      "target": "+8613800138000",
      "variables": {"name": "张三", "order_id": "A12345", "delivery_date": "明天"},
      "image": "/images/product-a.jpg",
      "message": "亲爱的 张三，您的订单 A12345 已发货，预计 明天 送达"
    },
    {
      "target": "+8613900139000",
      "variables": {"name": "李四", "order_id": "A12346", "delivery_date": "后天"},
      "image": "/images/product-b.jpg",
      "message": "亲爱的 李四，您的订单 A12346 已发货，预计 后天 送达"
    }
  ],
  "options": {
    "rate_limit": 30,
    "delay_min": 2,
    "delay_max": 5
  }
}
```

**执行命令：**

```bash
python3 batch_send.py --config /path/to/batch-send.json --parallel 5
```

**输出报告：**

```text
/reports/
├── batch-send-report.json   # 批量发送总报告
├── success.log              # 成功记录
└── failed.log               # 失败记录（可重试）
```

### 场景 2：营销活动定时推送

某营销团队需要在促销活动当天 10:00 向所有订阅用户发送活动海报。

**定时发送配置：**

```json
{
  "project": "促销活动推送",
  "schedule": {
    "type": "once",
    "datetime": "2026-07-20T10:00:00+08:00",
    "timezone": "Asia/Shanghai"
  },
  "messages": [
    {
      "target": "+8613800138000",
      "image": "/images/promo-poster.jpg",
      "message": "限时促销 全场 8 折 立即抢购"
    },
    {
      "target": "+8613900139000",
      "image": "/images/promo-poster.jpg",
      "message": "限时促销 全场 8 折 立即抢购"
    }
  ],
  "options": {
    "rate_limit": 20,
    "delay_min": 3,
    "delay_max": 8
  }
}
```

**执行命令：**

```bash
python3 scheduled_send.py --config /path/to/schedule.json
```

### 场景 3：群组文件分发

某项目团队需要向项目群组发送会议录制视频与会议纪要文档。

**操作步骤：**

1. 告诉 Agent：「把会议视频 /videos/meeting.mp4 和会议纪要 /docs/minutes.pdf 发到项目群组」
2. Agent 复制文件到工作区
3. 依次发送视频与文档
4. 清理临时文件

**示例流程：**

```bash
# 复制文件到工作区
cp /videos/meeting.mp4 ~/.skill-platform/workspace/
cp /docs/minutes.pdf ~/.skill-platform/workspace/

# 发送视频到群组
message --channel whatsapp \
  --target "项目群组 ID" \
  --filePath ~/.skill-platform/workspace/meeting.mp4 \
  --message "本次会议录制"

# 发送文档到群组
message --channel whatsapp \
  --target "项目群组 ID" \
  --filePath ~/.skill-platform/workspace/minutes.pdf \
  --message "会议纪要文档"

# 清理
rm ~/.skill-platform/workspace/meeting.mp4
rm ~/.skill-platform/workspace/minutes.pdf
```

## 快速开始

### 第一步：环境检查

```bash
# 检查 Python 版本（需 3.8+）
python3 --version

# 检查 message 工具
which message

# 检查工作区目录
ls ~/.skill-platform/workspace/
```

### 第二步：批量发送示例

创建收件人列表：

```json
[
  {"target": "+8613800138000", "image": "/images/a.jpg", "message": "消息 A"},
  {"target": "+8613900139000", "image": "/images/b.jpg", "message": "消息 B"}
]
```

执行批量发送：

```bash
python3 batch_send.py \
  --config /tmp/recipients.json \
  --parallel 5 \
  --rate-limit 30 \
  --report /tmp/send-report.json
```

### 第三步：定时发送

```bash
python3 scheduled_send.py \
  --config /tmp/schedule.json \
  --datetime "2026-07-20T10:00:00+08:00"
```

### 第四步：使用消息模板

```bash
python3 batch_send.py \
  --config /tmp/recipients.json \
  --template "亲爱的 {name}，{content}" \
  --variables-file /tmp/variables.csv
```

## 配置示例

### 完整配置文件模板

```yaml
# pro-config.yaml - 专业版完整配置
batch:
  parallel_workers: 5              # 并行发送数
  max_retries: 3                    # 失败重试次数
  retry_delay: 10                   # 重试间隔（秒）
  queue_file: /tmp/send-queue.json

rate_limit:
  messages_per_minute: 30           # 每分钟发送上限
  delay_min: 2                      # 最小延时（秒）
  delay_max: 5                      # 最大延时（秒）
  daily_limit: 1000                 # 每日发送上限

schedule:
  timezone: "Asia/Shanghai"        # 默认时区
  retry_on_failure: true           # 失败后重试

template:
  enabled: true                     # 启用模板
  directory: /templates/           # 模板目录
  default_template: "default.json"  # 默认模板

media:
  supported_types:
    - image: [jpg, png, gif, webp]
    - video: [mp4, mov, avi]
    - audio: [mp3, wav, aac]
    - document: [pdf, docx, xlsx, pptx]
  max_file_size: 16777216          # 单文件最大（16MB）

accounts:
  rotation: true                    # 多账号轮询
  accounts:
    - id: account-1
      token: "token-1"
    - id: account-2
      token: "token-2"

report:
  enabled: true
  output: /tmp/reports/send-report.json
  include_status: true               # 包含发送状态
  include_timestamp: true           # 包含时间戳
```

### 消息模板示例

```json
{
  "name": "order-notification",
  "content": "亲爱的 {name}，您的订单 {order_id} 已{status}，预计 {delivery_date} 送达",
  "variables": ["name", "order_id", "status", "delivery_date"]
}
```

### 频率控制建议

| 场景 | 每分钟上限 | 延时范围 |
|:-----|:-----------|:---------|
| 营销推送 | 20-30 | 2-5 秒 |
| 订单通知 | 30-50 | 1-3 秒 |
| 客户服务 | 50-60 | 0.5-2 秒 |
| 团队协作 | 60+ | 无需延时 |

## 最佳实践

### 1. 防封号策略

```yaml
# 推荐防封号配置
rate_limit:
  messages_per_minute: 20           # 保守的发送频率
  delay_min: 3                      # 随机延时下限
  delay_max: 8                      # 随机延时上限
  daily_limit: 500                  # 每日上限
  
accounts:
  rotation: true                    # 多账号轮询
```

### 2. 模板复用

```bash
# 创建模板库
mkdir -p /templates/

# 创建订单通知模板
cat > /templates/order-notification.json << 'EOF'
{
  "name": "order-notification",
  "content": "亲爱的 {name}，您的订单 {order_id} 已{status}"
}
EOF

# 批量发送时引用模板
python3 batch_send.py \
  --config /tmp/recipients.json \
  --template /templates/order-notification.json
```

### 3. 发送报告分析

```bash
# 查看发送报告
python3 report_analyzer.py --report /tmp/reports/send-report.json

# 输出示例：
# 总发送数：100
# 成功：95
# 失败：5
# 成功率：95%
# 平均耗时：3.2 秒
```

### 4. 失败重试

```bash
# 仅重试失败的消息
python3 batch_send.py --retry-failed /tmp/send-queue.json

# 从断点续传
python3 batch_send.py --resume /tmp/send-queue.json
```

## 常见问题

### Q1：专业版与免费版工作流是否兼容？

**A：** 完全兼容。专业版包含免费版所有工作流，单图发送命令可直接运行。专业版扩展的是批量、定时、模板等能力。

### Q2：批量发送被限制或封号怎么办？

**A：** 使用频率控制：

```bash
python3 batch_send.py \
  --config batch.json \
  --rate-limit 20 \
  --delay-min 3 --delay-max 8 \
  --daily-limit 500
```

### Q3：定时发送如何处理时区？

**A：** 专业版支持时区感知：

```json
{
  "schedule": {
    "datetime": "2026-07-20T10:00:00+08:00",
    "timezone": "Asia/Shanghai"
  }
}
```

### Q4：消息模板如何使用变量？

**A：** 使用 `{variable}` 语法：

```json
{
  "template": "亲爱的 {name}，您的订单 {order_id} 已发货",
  "variables": {"name": "张三", "order_id": "A12345"}
}
```

### Q5：能否同时发送图片和文档？

**A：** 可以，但需分两条消息发送（WhatsApp 限制单条消息仅一种媒体类型）：

```bash
# 第一条：发送图片
message --channel whatsapp --target +8613800138000 \
  --filePath ~/.skill-platform/workspace/image.jpg --message "商品图片"

# 第二条：发送文档
message --channel whatsapp --target +8613800138000 \
  --filePath ~/.skill-platform/workspace/doc.pdf --message "合同文档"
```

### Q6：多账号轮询如何配置？

**A：** 在配置文件中添加多个账号：

```yaml
accounts:
  rotation: true
  accounts:
    - id: account-1
      token: "token-1"
    - id: account-2
      token: "token-2"
```

### Q7：发送报告包含哪些信息？

**A：** 专业版报告包含：

- 总发送数与成功率
- 每条消息的发送状态
- 发送时间戳
- 失败原因分析
- 耗时统计

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要网络连接（发送消息）
- **Skill 平台**：需安装并提供 `message` 命令

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:-------|:-----|:---------|:---------|:---------|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| curl | 命令行工具 | 必需 | 系统自带 | 任意版本 |
| message | 平台工具 | 必需 | Skill 平台安装 | - |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| WhatsApp 账号 | 服务 | 必需 | WhatsApp 注册 | - |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令

```bash
# 安装 Python 依赖
pip3 install requests pyyaml

# 验证安装
python3 --version
curl --version
which message
```

### API Key 配置

专业版需要以下配置：

| 配置项 | 环境变量 | 用途 | 获取方式 |
|:-------|:---------|:-----|:---------|
| WhatsApp 凭证 | 平台配置 | WhatsApp 账号认证 | Skill 平台配置 |
| Skill 平台 Token | 平台配置 | 平台认证 | Skill 平台控制台 |
| 多账号 Token | 配置文件 | 多账号轮询 | Skill 平台控制台 |

```bash
# Skill 平台通常会自动配置 WhatsApp 凭证
# 多账号轮询在配置文件中设置
```

### 可用性分类

- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 调用 `message` 命令与 Python 脚本完成批量消息发送
- **离线可用**：否（需要网络连接发送消息）
- **隐私等级**：中（消息内容经过平台中转）
- **企业部署**：支持私有化部署客户端

## 版本说明

- **当前版本**：1.0.0
- **版本类型**：PRO（专业版）
- **兼容性**：与 `whatsapp-image-tool-free` 完全兼容，免费版工作流可直接使用
- **支持策略**：优先响应企业用户问题，提供工单支持
