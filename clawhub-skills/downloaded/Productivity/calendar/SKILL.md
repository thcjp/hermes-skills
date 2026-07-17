---
slug: calendar
name: calendar
version: "1.0.0"
displayName: Calendar
summary: Calendar management and scheduling. Create events, manage meetings, and sync
  across calendar prov...
license: MIT
description: |-
  Calendar management and scheduling. Create events, manage meetings,
  and sync across calendar prov...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: events, create, calendar, management, scheduling
tags:
- Productivity
tools:
- read
- exec
---

# Calendar

Calendar and scheduling management.

## Features

* Create events
* Schedule meetings
* Set reminders
* View availability
* Recurring events
* Calendar sync

## Supported Providers

* Google Calendar
* Apple Calendar
* Outlook Calendar

## Usage Examples

```text
"Schedule meeting tomorrow at 2pm"
"Show my calendar for this week"
"Find free time for a 1-hour meeting"
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
