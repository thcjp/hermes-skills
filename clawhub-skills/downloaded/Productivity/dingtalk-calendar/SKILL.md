---
slug: dingtalk-calendar
name: dingtalk-calendar
version: "1.0.2"
displayName: Dingtalk Calendar
summary: 钉钉日程管理（创建日程、查询闲忙、会议室预订）。使用 mcporter CLI 连接钉钉 MCP server 执行日程管理、日程查询、会议室预订等操作。使用场景：日程创建管理、会议预订、查询他...
license: MIT
description: |-
  钉钉日程管理（创建日程、查询闲忙、会议室预订）。使用 mcporter CLI 连接钉钉 MCP server 执行日程管理、日程查询、会议室预订等操作。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Dingtalk Calendar

使用 `mcporter` CLI 调用钉钉日历 MCP 创建和管理日程。

## 前置要求

### 依赖说明

本技能依赖 `mcporter` 工具。请在终端中手动执行以下命令安装：

```bash
npm install -g mcporter

bun install -g mcporter
```

验证安装：

```bash
mcporter --version
```

### 配置 MCP Server

本技能需要配置两个 MCP 服务：**钉钉日历** 和 **钉钉通讯录**。

**步骤一：获取 Streamable HTTP URL**

1. 访问钉钉 MCP 广场：<https://mcp.dingtalk.com>
2. 搜索 **钉钉日历**，点击进入服务详情页
3. 在页面右侧找到 `Streamable HTTP URL`，点击复制按钮
4. 同样的方法，获取 **钉钉通讯录** 的 URL

**步骤二：使用 mcporter 配置 MCP 服务**

```bash
mcporter config add dingtalk-calendar --url "这里粘贴钉钉日历的URL"

mcporter config add dingtalk-contacts --url "这里粘贴钉钉通讯录的URL"
```

**步骤三：验证配置**

```bash
mcporter config list

mcporter call dingtalk-calendar list_tools --output json
mcporter call dingtalk-contacts list_tools --output json
```

### 基本命令模式

所有操作通过 `mcporter call dingtalk-calendar <tool>` 执行：

```bash
mcporter call dingtalk-calendar create_calendar_event \
  --args '{"summary":"会议","startDateTime":"2026-02-28T14:00:00+08:00","endDateTime":"2026-02-28T15:00:00+08:00"}' \
  --output json

mcporter call dingtalk-calendar list_calendar_events \
  --args '{"startTime":1738128000000,"endTime":1738214400000}' \
  --output json

mcporter call dingtalk-calendar query_busy_status \
  --args '{"userIds":["userId1"],"startTime":1738128000000,"endTime":1738214400000}' \
  --output json
```

## 核心工具

### 1. 创建日程

```bash
mcporter call dingtalk-calendar create_calendar_event \
  --args '{
    "summary": "项目评审会议",
    "startDateTime": "2026-02-28T14:00:00+08:00",
    "endDateTime": "2026-02-28T15:00:00+08:00",
    "description": "讨论 Q1 进度",
    "attendees": ["userId1", "userId2"]
  }' \
  --output json
```

**参数说明：**

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `summary` | ✅ | 日程标题（最长 2048 字符） |
| `startDateTime` | ✅ | 开始时间（ISO-8601 格式，如 `2026-02-28T14:00:00+08:00`） |
| `endDateTime` | ✅ | 结束时间（ISO-8601 格式） |
| `description` | ❌ | 日程描述（最长 5000 字符） |
| `attendees` | ❌ | 参与人 userId 列表（最多 500 人） |

### 2. 查询日程列表

```bash
mcporter call dingtalk-calendar list_calendar_events \
  --args '{
    "startTime": 1738128000000,
    "endTime": 1738214400000
  }' \
  --output json
```

### 3. 查询他人闲忙

```bash
mcporter call dingtalk-calendar query_busy_status \
  --args '{
    "userIds": ["userId1", "userId2"],
    "startTime": 1738128000000,
    "endTime": 1738214400000
  }' \
  --output json
```

### 4. 查询空闲会议室

```bash
mcporter call dingtalk-calendar query_available_meeting_room \
  --args '{
    "startTime": "1738128000000",
    "endTime": "1738131600000"
  }' \
  --output json
```

### 5. 为日程添加会议室

```bash
mcporter call dingtalk-calendar add_meeting_room \
  --args '{
    "eventId": "日程ID",
    "roomIds": ["会议室ID1"]
  }' \
  --output json
```

### 6. 更新日程

```bash
mcporter call dingtalk-calendar update_calendar_event \
  --args '{
    "eventId": "日程ID",
    "summary": "新标题",
    "description": "新描述"
  }' \
  --output json
```

### 7. 删除日程

```bash
mcporter call dingtalk-calendar delete_calendar_event \
  --args '{"eventId": "日程ID"}' \
  --output json
```

## 通讯录工具

### 搜索用户

```bash
mcporter call dingtalk-contacts search_user_by_key_word \
  --args '{"keyWord": "张三"}' \
  --output json
```

### 获取用户详情

```bash
mcporter call dingtalk-contacts get_user_info_by_user_ids \
  --args '{"user_id_list": ["userId1", "userId2"]}' \
  --output json
```

## 常用时间格式

```python
import time
from datetime import datetime

int(time.time() * 1000)

datetime.fromtimestamp(1738128000000 / 1000).strftime("%Y-%m-%dT%H:%M:%S+08:00")

int(datetime.fromisoxt("2026-02-28T14:00:00+08:00").timestamp() * 1000)
```

## 示例

### 创建会议并预订会议室

```bash
mcporter call dingtalk-calendar query_available_meeting_room \
  --args '{"startTime":"1738128000000","endTime":"1738131600000"}' \
  --output json

mcporter call dingtalk-calendar create_calendar_event \
  --args '{
    "summary": "周会",
    "startDateTime": "2026-02-28T14:00:00+08:00",
    "endDateTime": "2026-02-28T15:00:00+08:00"
  }' \
  --output json

mcporter call dingtalk-calendar add_meeting_room \
  --args '{"eventId":"event123","roomIds":["room123"]}' \
  --output json
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 钉钉日程管理（创建日程、查询闲忙、会议室预订）
- 使用 mcporter CLI 连接钉钉 MCP server 执行日程管理、日程查询、会议室预订等操作
- 使用场景：日程创建管理、会议预订、查询他
- 触发关键词: 会议室预订, mcporter, server, 使用, calendar, dingtalk, 钉钉日程管理, 查询闲忙

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Dingtalk Calendar？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Dingtalk Calendar有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
