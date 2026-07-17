---
slug: feishu-calendar
name: feishu-calendar
version: "1.0.0"
displayName: feishu-calendar
summary: Manage Feishu (Lark) calendars by listing, searching, checking schedules,
  syncing events, and mar...
license: MIT
description: |-
  Manage Feishu (Lark) calendars by listing, searching, checking schedules,
  syncing events, and mar...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: feishu, calendar, manage, calendars, feishu-calendar, listing, lark
tags:
- Productivity
tools:
- read
- exec
---

# feishu-calendar

Manage Feishu (Lark) Calendars. Use this skill to list calendars, check schedules, and sync events.

## Usage

### List Calendars

Check available calendars and their IDs.

```bash
node skills/feishu-calendar/list_test.js
```

### Search Calendar

Find a calendar by name/summary.

```bash
node skills/feishu-calendar/search_cal.js
```

### Check Master's Calendar

Specific check for the Master's calendar status.

```bash
node skills/feishu-calendar/check_master.js
```

### Sync Routine

Run the calendar synchronization routine (syncs events to local state/memory).

```bash
node skills/feishu-calendar/sync_routine.js
```

## Setup

Requires `FEISHU_APP_ID` and `FEISHU_APP_SECRET` in `.env`.

## Standard Protocol: Task Marking

**Trigger**: User says "Mark this task" or "Remind me to...".
**Action**:

1. **Analyze**: Extract date/time (e.g., "Feb 4th" -> YYYY-MM-04).
2. **Execute**: Run `create.js` with `--attendees` set to the requester's ID.
3. **Format**:

   bash

   ```
   node skills/feishu-calendar/create.js --summary "Task: <Title>" --desc "<Context>" --start "<ISO>" --end "<ISO+1h>" --attendees "<User_ID>"
   ```

### Setup Shared Calendar

Create a shared calendar for a project and add members.

```bash
node skills/feishu-calendar/setup_shared.js --name "Project Name" --desc "Description" --members "ou_1,ou_2" --role "writer"
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
