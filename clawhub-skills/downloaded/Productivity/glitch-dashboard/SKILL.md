---
slug: glitch-dashboard
name: glitch-dashboard
version: "2026.2.18"
displayName: Dashboard
summary: Unified web dashboard for managing task queues, monitoring system metrics,
  viewing ZeroTier statu...
license: MIT
description: |-
  Unified web dashboard for managing task queues, monitoring system metrics,
  viewing ZeroTier statu。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
- Operations
tools:
  - - read
- exec
---

# Dashboard

Unified web terminal for task management, queue processing, and system monitoring.

## Overview

Single-page dashboard combining:

* **Task Queue** - View and manage pending tasks
* **System Monitor** - CPU, Memory, Load, Uptime
* **ZeroTier Status** - Network connection info
* **Output Stream** - Recent log entries

## Quick Start

```bash
dashboard start 3853
```

Then open: <http://localhost:3853>

## Features

### Real-time Monitoring

* CPU usage with progress bar
* Memory usage with progress bar
* Load average
* System uptime

### Task Queue Management

* View pending/processing tasks
* Complete current task
* Clear queue
* Auto-refresh every 3 seconds

### ZeroTier Integration

* Connection status
* ZeroTier IP address
* Network info

### Output Stream

* Recent log entries
* Source filtering

## CLI Commands

| Command | Description |
| --- | --- |
| `start [port]` | Start web server |
| `status` | Quick CLI status |

## API Endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | GET | Main dashboard |
| `/raw` | GET | JSON status |
| `/api/complete` | POST | Complete task |
| `/api/clear` | POST | Clear queue |

## Integration

Combines data from:

* `task-queue` skill
* `system-monitor` skill
* `output-streamer` skill
* `zerotier-deploy` skill

## Use Cases

1. **Operations Dashboard** - Monitor all systems in one view
2. **Task Management** - See and complete queued tasks
3. **Quick Status** - CLI `dashboard status` for quick check
4. **ZeroTier Access** - Quick access to ZT IP

## Author

Glitch (Skill平台 agent)

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

## 示例

### 示例1：基础用法

```
```bash
dashboard start 3853
```

Then open: <http://localhost:3853>
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Dashboard？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Dashboard有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
