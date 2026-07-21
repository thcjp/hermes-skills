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
  syncing events, and mar。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Productivity
tools:
  - - read
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

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Manage Feishu (Lark) calendars by listing, searching, checking schedules,
  syncing events, and mar
- 触发关键词: feishu, calendar, manage, calendars, feishu-calendar, listing, lark

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用feishu-calendar？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: feishu-calendar有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
