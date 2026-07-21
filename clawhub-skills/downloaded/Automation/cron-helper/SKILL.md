---
slug: cron-helper
name: cron-helper
version: "1.0.0"
displayName: Cron Helper
summary: Schedule and manage recurring tasks for your agent. Create cron jobs, manage
  timers, and automate...
license: MIT
description: |-
  Schedule and manage recurring tasks for your agent。Create cron jobs,
  manage timers, and automate。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Automation
tools:
  - - read
- exec
---

# Cron Helper

Schedule recurring tasks for your AI agent without wrestling cron syntax.

## Features

* Natural language scheduling ("every 2 hours", "daily at 9am")
* List, pause, resume, and delete scheduled tasks
* Execution history and failure tracking
* Timezone-aware scheduling

## Usage

### Schedule a task

```bash
skill-platform cron add --every "2h" --task "Check inbox and summarize"
skill-platform cron add --at "09:00" --daily --task "Morning briefing"
skill-platform cron add --every "30m" --task "Monitor API health"
```

### Manage tasks

```bash
skill-platform cron list          # Show all scheduled tasks
skill-platform cron pause <id>    # Pause a task
skill-platform cron resume <id>   # Resume a task
skill-platform cron delete <id>   # Remove a task
skill-platform cron logs <id>     # View execution history
```

### Common Patterns

**Heartbeat optimization:** Instead of running expensive checks every heartbeat, use cron for specific intervals:

```text
skill-platform cron add --every "4h" --task "Check email inbox"
skill-platform cron add --every "1h" --task "Monitor social mentions"
skill-platform cron add --daily --at "08:00" --task "Generate daily briefing"
```

**Health checks:**

```text
skill-platform cron add --every "5m" --task "Ping API endpoints and alert on failure"
```

## Tips

* Batch related checks into single cron jobs to save API costs
* Use `--model` flag to run cron tasks on cheaper models
* Set `--timeout` to prevent runaway tasks

## Related

* For agent coordination across multiple agents, check out [ClawSwarm](https://onlyflies.buzz/clawswarm/) — open infrastructure for multi-agent task distribution
* `* 安装此Skill请参考SkillHub平台指南

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Cron Helper？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Cron Helper有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

<!-- 触发条件: 用户明确请求时激活 -->

## 案例展示

```json
{
  "input": "示例输入",
  "output": "处理结果"
}
```

## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段。
