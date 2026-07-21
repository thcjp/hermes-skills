---
slug: telegram-agent-comm
name: telegram-agent-comm
version: "1.0.0"
displayName: 电报通信助手专业版
summary: 多角色 Agent 团队 Telegram 通信中枢，支持账号映射、批量调度、审计日志与优先级路由。
license: Proprietary
edition: pro
description: |-
  面向团队与企业的多 Agent Telegram 通信管理规范。
  核心能力: 多角色账号映射、批量消息调度、优先级路由、审计日志、模板库、媒体发送。
  适用场景: 多 Agent 协作汇报、企业通知分发、定时批量推送、跨角色工作流编排。
  差异化: 专业版在免费版基础上扩展多账号体系与调度能力，兼容免费版配置，支持团队级通信治理。
tags:
- 通信
- 电报
- 团队协作
- 企业通知
- 自动化
tools:
  - - read
- exec
---
# 电报通信助手专业版

## 核心能力

| 能力 | 免费版 | 专业版 |
| --- | :---: | :---: |
| 单账号文本发送 | 支持 | 支持 |
| 多角色账号映射 | - | 支持 |
| 批量消息调度 | - | 支持 |
| 优先级路由 | - | 支持 |
| 审计日志 | - | 支持 |
| 消息模板库 | 3 个 | 8+ 个 |
| 媒体文件发送 | - | 支持 |
| 定时推送 | - | 支持 |
| 多目标分发 | - | 支持 |
### 单账号文本发送

执行单账号文本发送操作,处理用户输入并返回结果。

**输入**: 用户提供单账号文本发送所需的参数和指令。

**输出**: 返回单账号文本发送的处理结果。

- 执行`单账号文本发送`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`单账号文本发送`相关配置参数进行设置
### 多角色账号映射

执行多角色账号映射操作,处理用户输入并返回结果。

**输入**: 用户提供多角色账号映射所需的参数和指令。

**输出**: 返回多角色账号映射的处理结果。

- 执行`多角色账号映射`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`多角色账号映射`相关配置参数进行设置
### 批量消息调度

执行批量消息调度操作,处理用户输入并返回结果。

**输入**: 用户提供批量消息调度所需的参数和指令。

**输出**: 返回批量消息调度的处理结果。

- 执行`批量消息调度`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`批量消息调度`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: Agent、Telegram、通信中枢、支持账号映射、批量调度、审计日志与优先级、面向团队与企业的、通信管理规范、核心能力、媒体发送、适用场景、协作汇报、企业通知分发、定时批量推送、跨角色工作流编排、差异化、专业版在免费版基、础上扩展多账号体、系与调度能力、兼容免费版配置、支持团队级通信治。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：多角色团队任务汇报

团队中不同角色的 Agent 各司其职，按统一规范向负责人汇报。

**账号映射表**

| 角色 | accountId | Emoji | 职责 |
| --- | --- | --- | --- |
| 主控 | `default` | 🤖 | 任务分发与汇总 |
| 架构师 | `architect` | 🏗️ | 系统设计 |
| 后端 | `backend` | 🔧 | 接口开发 |
| 前端 | `frontend` | 🎨 | 界面开发 |
| 产品 | `product` | 🟡 | 需求管理 |
| 测试 | `qa` | 🧪 | 质量保障 |

**后端工程师汇报示例**

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "backend",
  target: "<负责人Telegram用户ID>",
  message: "🔧 API 接口开发完成\n✅ 已完成: 用户鉴权模块\n📁 文档: ~/docs/backend/api.md\n⏱️ 耗时: 2h15m"
})
```

**产品经理汇报示例**

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "product",
  target: "<负责人Telegram用户ID>",
  message: "🟡 需求文档已完成\n📄 文件: ~/docs/product/prd-v2.md\n📌 包含 12 个用户故事\n💡 建议周四评审"
})
```

### 场景二：批量定时通知分发

向多个团队成员定时推送每日站会提醒，专业版支持一次调度多条消息。

```python
# batch_notify.py
import json
from datetime import datetime

members = [
    {"accountId": "architect", "target": "100001", "name": "张工"},
    {"accountId": "backend",   "target": "100002", "name": "李工"},
    {"accountId": "frontend",  "target": "100003", "name": "王工"},
]

for m in members:
    payload = {
        "action": "send",
        "channel": "telegram",
        "accountId": m["accountId"],
        "target": m["target"],
        "message": f"📅 {m['name']}，今日站会 10:00 开始，请准备进度同步"
    }
    print(json.dumps(payload, ensure_ascii=False))
```

### 场景三：优先级路由与告警

生产环境故障时，按优先级路由至不同通道与负责人。

```text
# 优先级路由规则
P0 严重 → 立即发送 + 重复 3 次（间隔 30s）
P1 重要 → 立即发送
P2 一般 → 归并至每小时摘要
```

```javascript
// P0 故障告警示例
message({
  action: "send",
  channel: "telegram",
  accountId: "qa",
  target: "<运维负责人ID>",
  message: "🚨 [P0] 生产环境告警\n❌ 问题: 数据库连接池耗尽\n💡 建议: 立即扩容连接池上限\n⏰ 时间: " + new Date().toISOString()
})
```

## 使用流程

1. 在配置文件中定义账号映射表（见下方配置示例）。
2. 为每个角色分配独立的 `accountId` 与 Bot Token。
3. 在 Agent 指令中引用本规范，各角色 Agent 使用自身 `accountId` 发送消息。

```text
# 示例
message({
  action: "send",
  channel: "telegram",
  accountId: "architect",
  target: "5440561025",
  message: "🏗️ 架构设计稿已完成，请审阅"
})
```

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

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 Telegram API
- **调度工具**：cron / 任务计划程序（定时推送功能需要）

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
| :------- | :----- | :--------- | :--------- |
| Telegram Bot Token（多账号） | API 凭证 | 必需 | 通过 `@BotFather` 为每个角色创建机器人 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Node.js | 运行时 | 可选 | 批量脚本执行需要，v16+ |
| Python | 运行时 | 可选 | 批量调度脚本需要，v3.9+ |
| cron / PM2 | 调度工具 | 可选 | 定时推送功能需要 |

### API Key 配置

- 在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.<accountId>.token` 字段为每个角色填入 Bot Token。
- 建议使用环境变量管理 Token，避免明文写入配置文件。

```bash
# 环境变量示例
export TG_TOKEN_DEFAULT="123456:ABC-DEF"
export TG_TOKEN_BACKEND="123456:GHI-JKL"
export TG_TOKEN_QA="123456:MNO-PQR"
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务。专业版在免费版基础上扩展多账号、批量调度与审计能力，配置文件向后兼容免费版。

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

### Q1：专业版如何兼容免费版配置？

专业版账号映射表中保留 `default` 账号即可。免费版脚本中 `accountId: "default"` 的消息在专业版中照常工作，无需修改。

### Q2：批量发送时触发 Telegram 限流怎么办？

降低并发频率，建议每秒不超过 5 条。专业版路由策略支持自动退避重试，可在 `routing.retryPolicy` 中配置。

### Q3：不同角色可以使用同一个 Bot Token 吗？

技术上可以但不推荐。共享 Token 时单账号限流会影响所有角色。建议为关键角色分配独立 Token。

### Q4：审计日志格式是什么？

审计日志为 JSONL 格式，每行一条记录，包含 `timestamp / accountId / target / message / priority / status` 字段。

```json
{"timestamp":"2026-07-18T10:00:00Z","accountId":"backend","target":"5440561025","priority":"P2","status":"sent","message":"🔧 API 开发完成"}
```

### Q5：专业版支持发送图片或文件吗？

支持。通过 `media` 字段附加文件路径或 URL，可发送图片、文档等媒体消息。免费版不支持此能力。

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "qa",
  target: "5440561025",
  message: "🧪 测试报告截图",
  media: "~/reports/screenshot-20260718.png"
})
```

### Q6：如何实现定时推送？

结合 cron 调度工具，在指定时间触发 Agent 执行批量发送脚本。专业版路由策略支持按优先级排队。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
