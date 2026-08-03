---
slug: glitch-dashboard
name: glitch-dashboard
version: "2026.2.18"
displayName: Dashboard
summary: "统一Web仪表盘,管理任务队列、监控系统指标、查看ZeroTier状态,运维可视化"
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
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

---
## 边界条件与限制

### 输入限制
- **任务队列长度**：Dashboard能够处理的任务队列长度有一定的限制，超过此限制可能导致队列处理延迟或失败。
- **系统监控指标**：Dashboard支持的系统监控指标类型有限，不支持所有可能的系统性能指标。
- **ZeroTier状态查询**：Dashboard仅支持ZeroTier网络连接状态的查询，不支持其他ZeroTier相关配置或操作。

### 性能边界
- **响应时间**：Dashboard的响应时间受限于服务器性能和网络延迟，可能无法保证在所有情况下都能达到实时监控的效果。
- **数据刷新频率**：Dashboard的数据刷新频率为每3秒自动刷新一次，对于需要更高频率监控的场景，可能需要手动刷新或使用其他工具。

### 兼容性约束
- **浏览器兼容性**：Dashboard需要在支持HTML5、CSS3和JavaScript的现代浏览器中运行，不支持旧版浏览器。
- **操作系统兼容性**：Dashboard在Windows、macOS和Linux操作系统上均能运行，但某些特定功能可能因操作系统差异而受限。

### 其他限制
- **外部API调用**：Dashboard依赖于外部API进行部分功能实现，如LLM API，因此可能受到外部API的限制或中断影响。
- **技能版本限制**：Dashboard可能需要特定版本的依赖技能才能正常运行，使用旧版本技能可能导致功能缺失或错误。
---

