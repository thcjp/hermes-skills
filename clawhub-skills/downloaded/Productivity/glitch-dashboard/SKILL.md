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
  viewing ZeroTier statu...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: dashboard, unified, queues, glitch, task, managing
tags:
- Productivity
- Operations
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
