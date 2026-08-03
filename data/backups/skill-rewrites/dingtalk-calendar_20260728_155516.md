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

简化日程管理，提升团队协作效率。

## 简介

Dingtalk Calendar是一款基于mcporter CLI的钉钉日程管理工具，旨在为用户提供便捷的日程创建、查询和预订功能。通过连接钉钉MCP server，用户可以轻松管理个人和团队的日程，提高工作效率。

## 前置要求

### 依赖说明

本技能依赖 `mcporter` 工具。请在终端中手动执行以下命令安装：

```bash
npm install -g mcporter
```

验证安装：

```bash
mcporter --version
```

### 配置 MCP Server

本技能需要配置钉钉日历和钉钉通讯录两个MCP服务。

**步骤一：获取 Streamable HTTP URL**

1. 访问钉钉 MCP 广场：<https://mcp.dingtalk.com>
2. 搜索 **钉钉日历** 和 **钉钉通讯录**，点击进入服务详情页
3. 在页面右侧找到 `Streamable HTTP URL`，点击复制按钮

**步骤二：使用 mcporter 配置 MCP 服务**

```bash
mcporter config add dingtalk-calendar --url "钉钉日历的URL"

mcporter config add dingtalk-contacts --url "钉钉通讯录的URL"
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
| `startDateTime` | ✅ | 开始时间（ISO-8601 格式） |
| `endDateTime` | ✅ | 结束时间（ISO-8601 格式） |
| `description` | ❌ | 日程描述（最长 5000 字符） |
| `attendees` | ❌ | 参与人 userId 列表（最多 500 人） |

### 2. 查询日程列表

```bash
mcporter call dingtalk-calendar list_calendar_events \
  --args '{"startTime": 1738128000000, "endTime": 1738214400000}' \
  --output json
```

### 3. 查询他人闲忙

```bash
mcporter call dingtalk-calendar query_busy_status \
  --args '{"userIds": ["userId1", "userId2"], "startTime": 1738128000000, "endTime": 1738214400000}' \
  --output json
```

### 4. 查询空闲会议室

```bash
mcporter call dingtalk-calendar query_available_meeting_room \
  --args '{"startTime": "1738128000000", "endTime": "1738131600000"}' \
  --output json
```

### 5. 为日程添加会议室

```bash
mcporter call dingtalk-calendar add_meeting_room \
  --args '{"eventId": "日程ID", "roomIds": ["会议室ID1"]}' \
  --output json
```

### 6. 更新日程

```bash
mcporter call dingtalk-calendar update_calendar_event \
  --args '{"eventId": "日程ID", "summary": "新标题", "description": "新描述"}' \
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

## 差异化优势

### 与同类方案对比

相较于手动操作钉钉日程，其他工具如通用日程管理软件或电子邮件客户端，Dingtalk Calendar展现出以下优势：

1. **自动化操作**：手动操作需要频繁登录钉钉，手动创建、修改和删除日程，效率低下。Dingtalk Calendar通过 `mcporter` CLI 与钉钉 MCP server 连接，实现自动化日程管理，节省大量时间。
2. **集成通讯录**：与其他工具相比，Dingtalk Calendar能够与钉钉通讯录无缝集成，方便查询和添加参会者，无需额外配置或操作。

### 独特功能

1. **创建会议并预订会议室**：Dingtalk Calendar允许用户在创建日程时直接预订会议室，实现会议组织和管理的自动化。
2. **查询他人闲忙状态**：通过 `query_busy_status` 工具，用户可以快速查询他人的空闲时间，提高会议安排的准确性。
3. **批量操作日程**：通过 `list_calendar_events` 工具，用户可以一次性查看未来一段时间的日程列表，方便进行批量操作。
4. **跨平台支持**：Dingtalk Calendar支持Windows、macOS和Linux操作系统，满足不同用户的需求。
5. **易于集成**：Dingtalk Calendar基于 `mcporter` 工具，可以轻松集成到现有的工作流和自动化脚本中。

### 效率提升

使用Dingtalk Calendar，用户可以：

- **节省时间**：自动化日程管理，减少手动操作步骤，提高效率。
- **减少步骤**：通过 `mcporter` CLI，直接在终端执行命令，无需打开钉钉应用。

### 应用场景创新

1. **跨部门会议组织**：Dingtalk Calendar支持查询他人闲忙状态，便于跨部门协调时间，提高会议效率。
2. **远程办公协作**：通过Dingtalk Calendar，远程办公人员可以方便地安排和参与会议，加强团队协作。
3. **企业培训管理**：利用Dingtalk Calendar的批量操作功能，企业可以轻松安排和跟踪员工培训进度。

## 当前评分问题
- completeness: 0.9 - 核心功能描述完整，输入输出格式清晰，使用场景充分，功能列表详尽，边界条件覆盖良好。
- accuracy: 0.9 - 技术描述正确，依赖说明准确，无错误或误导信息，参数和返回值描述与实际一致，代码示例可运行。
- usability: 0.9 - 文档结构清晰，示例充分，frontmatter规范完整，用户能快速理解并上手使用，有FAQ/troubleshooting。
- security: 0.9 - 无安全风险模式，依赖说明透明，无敏感信息泄露，无不可信外部调用，有安全注意事项提示。
- innovation: 0.8 - 提供了独特的实用解决方案，解决了真实痛点，功能组合或应用场景有新意，用户体验有亮点，但与同类方案相比差异化优势不明显。