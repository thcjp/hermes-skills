---
slug: dingtalk-calendar
name: dingtalk-calendar
version: "1.0.2"
displayName: Dingtalk Calendar
summary: 钉钉日程管理（创建日程、查询闲忙、会议室预订）。使用 mcporter CLI 连接钉钉 MCP server 执行日程管理、日程查询、会议室预订等操作。使用场景：日程创建管理、会议预订、查询他...
license: MIT
description: |-
  钉钉日程管理（创建日程、查询闲忙、会议室预订）。使用 mcporter CLI 连接钉钉 MCP server 执行日程管理、日程查询、会议室预订等操作。使用场景：日程创建管理、会议预订、查询他...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 会议室预订, mcporter, server, 使用, calendar, dingtalk, 钉钉日程管理, 查询闲忙
tags:
- Productivity
tools:
- read
- exec
---

# Dingtalk Calendar

使用 `mcporter` CLI 调用钉钉日历 MCP 创建和管理日程。

## 前置要求

### 安装 mcporter CLI

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

## 使用示例

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
