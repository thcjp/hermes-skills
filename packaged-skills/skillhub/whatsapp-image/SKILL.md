---
slug: "whatsapp-image"
name: "whatsapp-image"
version: 1.0.1
displayName: "WhatsApp图片发送-专业版"
summary: "企业级WhatsApp多媒体消息平台，支持批量发送、视频音频文档、定时发送、群组消息与模板管理。。WhatsApp 多媒体消息发送专业版。Use when 需要视频处理、音频编辑、媒体转换、"
license: "Proprietary"
edition: "pro"
description: |-
  WhatsApp 多媒体消息发送专业版。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理.
tags:
  - Creative
  - 消息发送
  - WhatsApp
  - 专业版
  - 批量处理
  - 企业级
  - 营销
  - 图像处理
  - AI绘图
  - 创意
  - json
  - message
  - image
  - target
  - jpg
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# WhatsApp图片发送-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| WhatsApp图片发送-专业版支持批量发送 | 不支持 | 支持 |
| WhatsApp图片发送-专业版定时发送 | 不支持 | 支持 |
| WhatsApp图片发送-专业版群组消息与模板管理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |

## 核心能力

### 1. 多媒体类型支持
专业版支持完整多媒体类型：

| 类型 | 格式 | 适用场景 |
|:-----|:-----|:-----|
| 图片 | JPG/PNG/GIF/WebP | 照片、截图、设计稿 |
| 视频 | MP4/MOV/AVI | 宣传片、教程、演示 |
| 音频 | MP3/WAV/AAC | 语音消息、音乐 |
| 文档 | PDF/DOCX/XLSX/PPTX | 合同、报告、资料 |

**处理**: 解析多媒体类型支持的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多媒体类型支持的处理结果,包含执行状态码、结果数据和执行日志.
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
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量发送` 选项
- 处理流程: 接收输入 -> 执行批量发送 -> 返回结果
- 输入: 用户提供批量发送所需的参数和指令
- 输出: 返回批量发送的处理结果,包含执行状态码、结果数据和执行日志

### 3. 定时发送
支持指定时间发送消息：

- 单次定时（指定日期时间）
- 重复定时（每日/每周/每月）
- 时区感知（跨时区发送）

**输入**: 用户提供定时发送所需的指令和必要参数.
**输出**: 返回定时发送的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 群组消息与广播
- 单条消息发送至群组
- 广播列表（多收件人单独发送）
- 群组管理（创建/删除/查询）

**输入**: 用户提供群组消息与广播所需的指令和必要参数.
### 5. 消息模板管理
预设消息模板，支持变量替换：

```text
模板：亲爱的 {name}，您的订单 {order_id} 已发货
变量：{name}=张三, {order_id}=A12345
结果：亲爱的 张三，您的订单 A12345 已发货
```

**输入**: 用户提供消息模板管理所需的指令和必要参数.
**处理**: 解析消息模板管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `消息模板管理` 选项

### 6. 发送频率控制
防止因发送过快导致封号：

- 每分钟发送上限
- 随机延时（模拟人工）
- 每日发送总量限制
- 多账号轮询分流

**输入**: 用户提供发送频率控制所需的指令和必要参数.
**输出**: 返回发送频率控制的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景 1：电商订单批量通知
某电商商家需要向 100 个客户发送订单发货通知（含商品图片）.
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
某营销团队需要在促销活动当天 10:00 向所有订阅用户发送活动海报.
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
某项目团队需要向项目群组发送会议录制视频与会议纪要文档.
**操作步骤：**

1. 告诉 Agent：「把会议视频 /videos/meeting.mp4 和会议纪要 /docs/minutes.pdf 发到项目群组」
2. Agent 复制文件到工作区
3. 依次发送视频与文档
4. 清理临时文件

**示例流程：**

```bash
cp /videos/meeting.mp4 ~/.skill-platform/workspace/
cp /docs/minutes.pdf ~/.skill-platform/workspace/
# ...
message --channel whatsapp \
  --target "项目群组 ID" \
  --filePath ~/.skill-platform/workspace/meeting.mp4 \
  --message "本次会议录制"
# ...
message --channel whatsapp \
  --target "项目群组 ID" \
  --filePath ~/.skill-platform/workspace/minutes.pdf \
  --message "会议纪要文档"
# ...
rm ~/.skill-platform/workspace/meeting.mp4
rm ~/.skill-platform/workspace/minutes.pdf
```

## 使用流程

### 优秀步：环境检查
```bash
python3 --version
# ...
which message
# ...
ls ~/.skill-platform/workspace/
```

### 示例
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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | whatsapp-image处理的内容输入 |,  |
| content | string | 否 | whatsapp-image处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "image 相关配置参数",
    result: "image 相关配置参数",
    result: "image 相关配置参数",
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
- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要网络连接（发送消息）
- **Skill 平台**：需安装并提供 `message` 命令

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:------|------:|:------|:------|------:|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| curl | 命令行工具 | 必需 | 系统自带 | 任意版本 |
| message | 平台工具 | 必需 | Skill 平台安装 | - |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| WhatsApp 账号 | 服务 | 必需 | WhatsApp 注册 | - |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令
```bash
pip3 install requests pyyaml
# ...
python3 --version
curl --version
which message
```

### API Key 配置
专业版需要以下配置：

| 配置项 | 环境变量 | 用途 | 获取方式 |
|---:|:---|---:|---:|
| WhatsApp 凭证 | 平台配置 | WhatsApp 账号认证 | Skill 平台配置 |
| Skill 平台 Token | 平台配置 | 平台认证 | Skill 平台控制台 |
| 多账号 Token | 配置文件 | 多账号轮询 | Skill 平台控制台 |

```bash
```

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 调用 `message` 命令与 Python 脚本完成批量消息发送
- **离线可用**：否（需要网络连接发送消息）
- **隐私等级**：中（消息内容经过平台中转）
- **企业部署**：支持私有化部署客户端

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：专业版与免费版工作流是否兼容？
**A：** 完全兼容。专业版包含免费版所有工作流，单图发送命令可直接运行。专业版扩展的是批量、定时、模板等能力.
### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
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
message --channel whatsapp --target +8613800138000 \
  --filePath ~/.skill-platform/workspace/image.jpg --message "商品图片"
# ...
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

## 错误处理

| 错误场景(续)(续)| 原因 | 处理方式 |
|-------|:-----:|------:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 图像处理能力受限于本地硬件与内存
- 大尺寸图片处理可能较慢或失败
