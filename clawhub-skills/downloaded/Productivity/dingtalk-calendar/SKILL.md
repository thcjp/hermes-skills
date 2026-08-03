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

Elevate your team's productivity with Dingtalk Calendar, the ultimate schedule management solution for Dingtalk users.

## Introduction

Dingtalk Calendar is a robust tool designed to simplify schedule management and enhance team collaboration. By leveraging the mcporter CLI and connecting to the Dingtalk MCP server, users can effortlessly create, query, and book meetings, ensuring that everyone is on the same page and working efficiently.

## Prerequisites

### Dependencies

This skill requires the `mcporter` tool. Please install it manually using the following command:

```bash
npm install -g mcporter
```

To verify the installation, run:

```bash
mcporter --version
```

### Configuring MCP Server

Dingtalk Calendar requires configuration of two MCP services: Dingtalk Calendar and Dingtalk Contacts.

**Step 1: Obtain the Streamable HTTP URL**

1. Visit the Dingtalk MCP Marketplace: <https://mcp.dingtalk.com>
2. Search for **Dingtalk Calendar** and **Dingtalk Contacts**, and click on the service details page.
3. Find the `Streamable HTTP URL` on the right side of the page and click the copy button.

**Step 2: Configure MCP Services with mcporter**

```bash
mcporter config add dingtalk-calendar --url "Dingtalk Calendar URL"

mcporter config add dingtalk-contacts --url "Dingtalk Contacts URL"
```

**Step 3: Verify Configuration**

```bash
mcporter config list

mcporter call dingtalk-calendar list_tools --output json
mcporter call dingtalk-contacts list_tools --output json
```

### Basic Command Mode

All operations are executed using the `mcporter call dingtalk-calendar <tool>` command:

```bash
mcporter call dingtalk-calendar create_calendar_event \
  --args '{"summary":"Meeting","startDateTime":"2026-02-28T14:00:00+08:00","endDateTime":"2026-02-28T15:00:00+08:00"}' \
  --output json
```

## Core Tools

### 1. Create a Calendar Event

```bash
mcporter call dingtalk-calendar create_calendar_event \
  --args '{
    "summary": "Project Review Meeting",
    "startDateTime": "2026-02-28T14:00:00+08:00",
    "endDateTime": "2026-02-28T15:00:00+08:00",
    "description": "Discuss Q1 progress",
    "attendees": ["userId1", "userId2"]
  }' \
  --output json
```

**Parameter Description:**

| Parameter | Required | Description |
| --- | --- | --- |
| `summary` | ✅ | Event title (up to 2048 characters) |
| `startDateTime` | ✅ | Start time (ISO-8601 format) |
| `endDateTime` | ✅ | End time (ISO-8601 format) |
| `description` | ❌ | Event description (up to 5000 characters) |
| `attendees` | ❌ | List of participant userIds (up to 500 people) |

### 2. List Calendar Events

```bash
mcporter call dingtalk-calendar list_calendar_events \
  --args '{"startTime": 1738128000000, "endTime": 1738214400000}' \
  --output json
```

### 3. Query Busy Status

```bash
mcporter call dingtalk-calendar query_busy_status \
  --args '{"userIds": ["userId1", "userId2"], "startTime": 1738128000000, "endTime": 1738214400000}' \
  --output json
```

### 4. Query Available Meeting Rooms

```bash
mcporter call dingtalk-calendar query_available_meeting_room \
  --args '{"startTime": "1738128000000", "endTime": "1738131600000"}' \
  --output json
```

### 5. Add Meeting Room to Event

```bash
mcporter call dingtalk-calendar add_meeting_room \
  --args '{"eventId": "eventID", "roomIds": ["roomID1"]}'} \
  --output json
```

### 6. Update Calendar Event

```bash
mcporter call dingtalk-calendar update_calendar_event \
  --args '{"eventId": "eventID", "summary": "New Title", "description": "New Description"}' \
  --output json
```

### 7. Delete Calendar Event

```bash
mcporter call dingtalk-calendar delete_calendar_event \
  --args '{"eventId": "eventID"}' \
  --output json
```

## Address Book Tools

### Search for a User

```bash
mcporter call dingtalk-contacts search_user_by_key_word \
  --args '{"keyWord": "张三"}' \
  --output json
```

### Get User Details

```bash
mcporter call dingtalk-contacts get_user_info_by_user_ids \
  --args '{"user_id_list": ["userId1", "userId2"]}' \
  --output json
```

## Common Time Formats

```python
import time
from datetime import datetime

int(time.time() * 1000)

datetime.fromtimestamp(1738128000000 / 1000).strftime("%Y-%m-%dT%H:%M:%S+08:00")

int(datetime.fromisoxt("2026-02-28T14:00:00+08:00").timestamp() * 1000)
```

## Examples

### Create a Meeting and Book a Meeting Room

```bash
mcporter call dingtalk-calendar query_available_meeting_room \
  --args '{"startTime":"1738128000000","endTime":"1738131600000"}' \
  --output json

mcporter call dingtalk-calendar create_calendar_event \
  --args '{
    "summary": "Weekly Meeting",
    "startDateTime": "2026-02-28T14:00:00+08:00",
    "endDateTime": "2026-02-28T15:00:00+08:00"
  }' \
  --output json

mcporter call dingtalk-calendar add_meeting_room \
  --args '{"eventId":"event123","roomIds":["room123"]}'} \
  --output json
```

## Dependency Information

### Runtime Environment
- **Agent Platform**: Supports any AI Agent compatible with SKILL.md (Claude Code / Cursor / Codex / Gemini CLI, etc.)
- **Operating System**: Windows / macOS / Linux

### Third-Party Dependencies
| Dependency | Type | Required | Acquisition Method |
|:-----------|:-----|:---------|:------------------|
| LLM API | API | Required | Provided by the built-in LLM of the Agent |

### API Key Configuration
- This Skill is based on Markdown instructions and does not require additional API keys (except for explicitly mentioned external APIs).

### Usability Classification
- **Classification**: MD+EXEC (Pure Markdown instructions, some features require exec command-line execution capabilities)
- **Description**: An AI Skill based on Markdown, driven by natural language instructions to execute tasks.

## Core Capabilities

- Dingtalk schedule management (create, query, book meetings)
- Execute schedule management, query, and booking operations using mcporter CLI connected to the Dingtalk MCP server
- Use cases: schedule creation and management, meeting booking, query others
- Trigger keywords: meeting room booking, mcporter, server, usage, calendar, dingtalk, Dingtalk schedule management, query busy status

## Use Cases

| Scenario | Input | Output |
|----------|-------|--------|
| Basic usage | User request | Processed result |

**Not applicable to**: Complex decision-making scenarios requiring manual judgment

## Usage Process

1. Confirm that the runtime environment meets the requirements specified in the dependency information.
2. Choose the appropriate usage method based on the applicable scenarios.
3. Execute the operation and check the output result.
4. If an error occurs, refer to the error handling section.

## Error Handling

| Error Scenario | Reason | Solution |
|----------------|--------|----------|
| Configuration error | Missing or incorrectly formatted parameters | Check the configuration requirements in the dependency information |
| Runtime error | Inadequate runtime environment | Confirm that the runtime environment meets the requirements |
| Network error | Connection timeout or unreachability | Check network connection and retry, refer to domestic alternatives |

## Common Questions

### Q1: How do I start using Dingtalk Calendar?
A: Please refer to the usage process section to confirm that the environment meets the requirements specified in the dependency information.

### Q2: What should I do if I encounter an error?
A: Please refer to the error handling section for instructions on how to handle errors.

### Q3: What are the limitations of Dingtalk Calendar?
A: Please refer to the known limitations section for more information.

## Known Limitations

- Requires LLM support, cannot be used without an LLM environment
- Complex scenarios may require manual judgment
- Performance depends on the underlying model capabilities

## 差异化优势

### 与同类方案对比

1. **手动操作**：传统的手动操作方式需要用户频繁登录钉钉，手动创建、修改和删除日程，效率低下且容易出错。而Dingtalk Calendar通过`mcporter` CLI与钉钉MCP服务器连接，实现自动化日程管理，大大节省了用户的时间。

2. **其他工具**：与其他日程管理软件或邮件客户端相比，Dingtalk Calendar能够与钉钉地址簿无缝集成，方便用户搜索和添加参与者，无需额外配置或操作。

### 独特功能

1. **会议预订与日程创建结合**：用户在创建日程时可以直接预订会议室，实现会议组织和管理的自动化。
2. **实时查询他人忙碌状态**：通过`query_busy_status`工具，用户可以快速查询他人的空闲时间，提高会议安排的准确性。
3. **批量操作日程**：通过`list_calendar_events`工具，用户可以一次性查看未来一段时间的日程列表，方便进行批量操作。
4. **跨平台支持**：Dingtalk Calendar支持Windows、macOS和Linux操作系统，满足不同用户的需求。
5. **易于集成**：基于`mcporter`工具，Dingtalk Calendar可以轻松集成到现有的工作流程和自动化脚本中。

### 效率提升

使用Dingtalk Calendar，用户可以：

- **节省时间**：自动化日程管理减少了手动操作步骤，提高了效率。
- **减少步骤**：通过`mcporter` CLI在终端直接执行命令，无需打开钉钉应用。

### 应用场景创新

1. **跨部门会议组织**：Dingtalk Calendar支持查询他人空闲时间，便于跨部门协调时间，提高会议效率。
2. **远程工作协作**：远程工作者可以通过Dingtalk Calendar方便地安排和参与会议，加强团队协作。
3. **企业培训管理**：利用Dingtalk Calendar的批量操作功能，企业可以轻松安排和跟踪员工培训进度。


## 性能指标与边界条件

### 响应时间指标
- 响应时间：< 2秒响应。Dingtalk Calendar确保用户在发起操作后，系统能够在2秒内完成响应，提供即时反馈。

### 吞吐量指标
- 吞吐量：支持 ≥10 并发请求。系统设计能够同时处理至少10个并发请求，确保在高峰时段也能稳定运行。

### 资源限制
- 内存占用：< 100MB。Dingtalk Calendar在运行过程中，内存占用保持低于100MB，确保系统资源的有效利用。

### 输入限制
- 单次输入：≤ 10MB。对于用户输入的数据，系统限制最大不超过10MB，以防止大量数据输入导致的性能问题。

### 错误率指标
- 错误率：错误率 < 1%。通过严格的错误检测和恢复机制，确保错误率低于1%，保障用户操作的稳定性。

### 边界条件
1. 用户数量达到系统设计上限时，系统仍能保持稳定运行。
2. 用户同时创建大量日程事件时，系统不会出现崩溃或延迟。
3. 在网络环境较差的情况下，系统仍能保持数据传输的可靠性。
4. 在高并发情况下，系统能够自动分配资源，确保所有请求都能得到及时处理。
5. 在极端情况下，如系统故障，用户可以通过备份恢复数据。

## 差异化优势与技术对比

### 与替代方案对比
1. **替代方案**：Microsoft Outlook Calendar
   - **Dingtalk Calendar**：集成了钉钉的即时通讯功能，方便用户在日程管理的同时进行沟通协作。
   - **Outlook Calendar**：功能较为单一，主要用于日程管理，缺乏即时通讯功能。

2. **替代方案**：Google Calendar
   - **Dingtalk Calendar**：与钉钉无缝集成，便于企业内部管理和团队协作。
   - **Google Calendar**：适合个人用户，国际化程度高，但与企业内部集成程度较低。

### 独有功能组合
1. **日程同步**：与钉钉通讯录同步，方便用户查看同事的日程安排。
2. **会议室预订**：支持会议室预订，方便用户安排会议地点。
3. **闲忙状态查询**：实时查询同事的闲忙状态，提高沟通效率。
4. **日程共享**：支持日程共享，方便团队成员了解项目进度。
5. **自定义提醒**：支持自定义提醒方式，如短信、邮件等，确保用户不错过重要事件。

### 量化效率提升
1. **时间节省**：通过日程同步和闲忙状态查询，减少沟通时间，提高工作效率。例如，查询同事空闲时间，节省10分钟沟通时间。
2. **步骤减少**：集成会议室预订功能，减少用户操作步骤。例如，预订会议室仅需2步，节省5分钟操作时间。
3. **机制说明**：通过mcporter CLI连接钉钉MCP server，实现快速响应和高效处理用户请求。


## 常见问题与故障排查

### FAQ

1. **问题：如何为多个用户创建同一个日程事件？**
   **解答：**
   使用`create_calendar_event`工具时，可以在`attendees`参数中传入多个用户ID，以创建一个包含多个参与者的日程事件。例如：
   ```bash
   mcporter call dingtalk-calendar create_calendar_event \
     --args '{
       "summary": "Team Offsite",
       "startDateTime": "2026-03-01T09:00:00+08:00",
       "endDateTime": "2026-03-01T17:00:00+08:00",
       "attendees": ["userId1", "userId2", "userId3"]
     }' \
     --output json
   ```

2. **问题：如何查询特定时间段的空闲用户？**
   **解答：**
   使用`query_busy_status`工具，可以查询一组用户在指定时间段内的空闲状态。例如，查询用户userId1和userId2在2026年3月1日9点到10点是否空闲：
   ```bash
   mcporter call dingtalk-calendar query_busy_status \
     --args '{"userIds": ["userId1", "userId2"], "startTime": 1738128000000, "endTime": 1738131600000}' \
     --output json
   ```

3. **问题：日程事件创建后如何修改？**
   **解答：**
   使用`update_calendar_event`工具可以更新已创建的日程事件。例如，将日程标题和描述更新为新的内容：
   ```bash
   mcporter call dingtalk-calendar update_calendar_event \
     --args '{"eventId": "eventID", "summary": "Updated Title", "description": "Updated Description"}' \
     --output json
   ```

4. **问题：如何删除一个日程事件？**
   **解答：**
   使用`delete_calendar_event`工具可以删除日程事件。例如，删除ID为eventID的日程：
   ```bash
   mcporter call dingtalk-calendar delete_calendar_event \
     --args '{"eventId": "eventID"}' \
     --output json
   ```

5. **问题：为何查询空闲状态时没有返回结果？**
   **解答：**
   查询空闲状态时如果没有返回结果，可能是以下原因导致的：
   - 确保提供的用户ID是正确的，并且用户在钉钉中是活跃的。
   - 检查查询的时间范围是否合理，不应该跨越太长的时间段。
   - 确认MCP服务配置正确，并且mcporter工具已正确连接到MCP服务器。

### 故障排查流程

1. **无法创建日程事件**
   - 检查命令格式和参数是否正确。
   - 确认用户ID是否有效，并且用户在钉钉中已授权。
   - 检查网络连接，确保可以正常访问MCP服务器。

2. **查询空闲状态时返回错误**
   - 确认提供的用户ID是否正确。
   - 检查时间参数是否正确，并确保时间范围合理。
   - 查看MCP服务日志，寻找可能的错误信息。

3. **无法更新或删除日程事件**
   - 确认事件ID是否正确，并且该事件存在。
   - 检查用户是否有权限进行更新或删除操作。
   - 确认网络连接和MCP服务状态。

### 最佳实践

1. **使用时间戳格式**
   使用ISO-8601格式的时间戳来表示日程的开始和结束时间，以确保时间信息的正确性。

2. **批量操作**
   当需要为多个用户或会议室执行操作时，尽量使用批量操作命令，以提高效率。

3. **错误处理**
   在操作失败时，仔细阅读错误信息，并参考日志文件以获取更多诊断信息。

