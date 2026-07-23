---
slug: productivity-improving
name: productivity-improving
version: "1.1.0"
displayName: Productivity Tracker
summary: "生产力追踪与每日复盘助手,输入活动日志与目标,量化效率趋势,辅助自我提升"
  notes, goals, or a dai...
license: MIT-0
description: |-
  Productivity tracker and daily review assistant。Input activity logs,
  time notes, goals, or a dai。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Productivity Tracker

Track, categorize, and analyze your work and life activities to improve efficiency and maintain balance.

## Input Methods

### Voice/Text Input

* **Start Activity**: "start [activity name]"
* **Complete Activity**: "complete"
* **Quick Log**: "log [activity] took [duration]"

### 示例

```text
"start coding"
"start meeting"
"complete"
"log workout 45 minutes"
"what did I do today"
"analyze my productivity this week"
```

## 核心能力

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

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

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

### Q1: 如何开始使用Productivity Tracker？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Productivity Tracker有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
