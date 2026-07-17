---
slug: productivity-improving
name: productivity-improving
version: "1.1.0"
displayName: Productivity Tracker
summary: Productivity tracker and daily review assistant. Input activity logs, time
  notes, goals, or a dai...
license: MIT-0
description: |-
  Productivity tracker and daily review assistant. Input activity logs,
  time notes, goals, or a dai...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: tracker, productivity, assistant, improving, review, daily
tags:
- Productivity
tools:
- read
- exec
---

# Productivity Tracker

Track, categorize, and analyze your work and life activities to improve efficiency and maintain balance.

## Input Methods

### Voice/Text Input

* **Start Activity**: "start [activity name]"
* **Complete Activity**: "complete"
* **Quick Log**: "log [activity] took [duration]"

### Natural Language Examples

```text
"start coding"
"start meeting"
"complete"
"log workout 45 minutes"
"what did I do today"
"analyze my productivity this week"
```

## Core Features

### 1. Activity Recording

* Real-time activity tracking with start/end timestamps
* Automatic duration calculation
* Support for interruptions and resumption
* Voice and text input support

### 2. Smart Categorization

Auto-categorize activities into:

* **Work**: coding, meetings, emails, planning
* **Learning**: reading, courses, research
* **Health**: exercise, meditation, sleep
* **Life**: cooking, cleaning, family time
* **Rest**: entertainment, social media, breaks

### 3. Time Analysis

* Daily/weekly/monthly time distribution
* Focus time vs. fragmented time analysis
* Peak productivity hours identification
* Work-life balance metrics

### 4. Daily Report Generation

```markdown

## Overview
- Total activities: 12
- Focus time: 6.5 hours
- Rest time: 2 hours
- Work/Life ratio: 65%/35%

## Time Distribution
| Category | Duration | Percentage |
|----------|----------|------------|
| Deep Work | 4h | 40% |
| Meetings | 1.5h | 15% |
| Learning | 1h | 10% |
| Life Tasks | 2h | 20% |
| Rest | 1.5h | 15% |

## Key Activities
- Completed project docs (2h, Deep Work)
- Team weekly meeting (1h, Meetings)
- Read tech article (45min, Learning)

## Insights
Highlight: Peak focus 9-11 AM, core tasks completed
Improvement: Frequent interruptions 3-4 PM, reserve block time
Trend: Deep work time increased 15% vs last week

## Tomorrow's Suggestions
1. Maintain morning deep work routine
2. Batch email processing after 4 PM
3. Reserve 30 minutes for tomorrow's planning
```

## Data Storage

### Local Storage

* **Activities**: `data/activities.json`
* **Daily Logs**: `data/logs/YYYY-MM-DD.md`
* **Analytics**: `data/analytics/`

### Export Options

* Daily/weekly Markdown reports
* CSV for spreadsheet analysis
* JSON for API integration

## Workflow

### Phase 1: Capture

1. User says "start [activity]"
2. Record timestamp and activity name
3. Auto-categorize based on keywords
4. Confirm category with user if uncertain

### Phase 2: Track

1. Monitor active activity
2. Allow "pause" and "resume"
3. Handle interruptions gracefully
4. Record end timestamp on completion

### Phase 3: Analyze

1. Calculate duration and metrics
2. Update category totals
3. Compare with historical patterns
4. Generate insights

### Phase 4: Report

1. Generate daily summary at user-defined time
2. Weekly review with trends
3. Monthly analysis with recommendations
4. Export to Obsidian or other tools

## Commands

| Command | Description |
| --- | --- |
| `/track start [activity]` | Start tracking an activity |
| `/track stop` | Stop current activity |
| `/track status` | Show current activity and today's summary |
| `/track log [activity] [duration]` | Quick log a completed activity |
| `/track report daily` | Generate today's report |
| `/track report weekly` | Generate weekly analysis |
| `/track category [name]` | Show time spent in category |
| `/track insights` | Get productivity suggestions |

## Configuration

```json
{
  "dailyReportTime": "21:00",
  "categories": {
    "work": { "color": "#4CAF50", "keywords": ["code", "meeting", "email"] },
    "learning": { "color": "#2196F3", "keywords": ["read", "study", "course"] },
    "health": { "color": "#FF9800", "keywords": ["exercise", "meditation", "sleep"] },
    "life": { "color": "#9C27B0", "keywords": ["cook", "clean", "family"] },
    "rest": { "color": "#607D8B", "keywords": ["rest", "entertainment", "break"] }
  },
  "focusThresholdMinutes": 25,
  "breakReminderIntervalMinutes": 90
}
```

## Privacy & Security

* All data stored locally
* No cloud sync by default
* Optional encryption for sensitive logs
* User owns all data

## Integration

* Export to Obsidian daily notes
* Sync with calendar events
* Connect with health apps (optional)
* API for custom workflows

## Technical Info

| Property | Value |
| --- | --- |
| **Name** | Productivity Tracker |
| **Slug** | `productivity-improving` |
| **Version** | 1.0.5 |
| **Category** | Productivity / Lifestyle |
| **Tags** | time-tracking, productivity, analytics, daily-log |

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
