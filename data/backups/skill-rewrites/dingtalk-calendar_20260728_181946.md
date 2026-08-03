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

## Differentiated Advantages

### Comparison with Similar Solutions

Compared to manual operation of Dingtalk schedule, other tools such as general schedule management software or email clients, Dingtalk Calendar demonstrates the following advantages:

1. **Automated Operations**: Manual operation requires frequent login to Dingtalk and manual creation, modification, and deletion of schedules, which is inefficient. Dingtalk Calendar connects to the Dingtalk MCP server through `mcporter` CLI to realize automated schedule management, saving a lot of time.
2. **Integration with Address Book**: Compared to other tools, Dingtalk Calendar can be seamlessly integrated with the Dingtalk address book, facilitating the search and addition of participants without additional configuration or operation.

### Unique Features

1. **Create a Meeting and Book a Meeting Room**: Dingtalk Calendar allows users to book a meeting room directly when creating a schedule, realizing the automation of meeting organization and management.
2. **Query Others' Busy Status**: Through the `query_busy_status` tool, users can quickly query others' available time, improving the accuracy of meeting scheduling.
3. **Batch Operation of Schedules**: Through the `list_calendar_events` tool, users can view the schedule list for a future period at one time, facilitating batch operations.
4. **Cross-Platform Support**: Dingtalk Calendar supports Windows, macOS, and Linux operating systems, meeting the needs of different users.
5. **Easy to Integrate**: Based on the `mcporter` tool, Dingtalk Calendar can be easily integrated into existing workflows and automated scripts.

### Efficiency Improvement

Using Dingtalk Calendar, users can:

- **Save Time**: Automated schedule management reduces manual operation steps and improves efficiency.
- **Reduce Steps**: Directly execute commands in the terminal through `mcporter` CLI, without the need to open the Dingtalk application.

### Innovation in Application Scenarios

1. **Cross-departmental Meeting Organization**: Dingtalk Calendar supports querying others' available time, facilitating cross-departmental coordination of time and improving meeting efficiency.
2. **Remote Work Collaboration**: Through Dingtalk Calendar, remote workers can conveniently arrange and participate in meetings, strengthening team collaboration.
3. **Enterprise Training Management**: Utilizing the batch operation function of Dingtalk Calendar, enterprises can easily arrange and track employee training progress.

## Current Rating Issues
- completeness: 0.9 - Core function descriptions are comprehensive, input/output formats are clear, applicable scenarios are sufficient, function lists are detailed, and boundary conditions are well-covered.
- accuracy: 0.9 - Technical descriptions are correct, dependency information is accurate, there are no errors or misleading information, parameter and return value descriptions are consistent with the actual, and code examples can be run.
- usability: 0.9 - Document structure is clear, examples are sufficient, frontmatter is standardized, users can quickly understand and use it, and there are FAQs/troubleshooting.
- security: 0.9 - No security risk mode, dependency information is transparent, no sensitive information is leaked, no untrusted external calls, and there are security precautions.
- innovation: 0.8 - Provides unique practical solutions, solves real pain points, functional combinations or application scenarios have new ideas, and user experience has highlights, but the differentiated advantages compared to similar solutions are not obvious.
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

