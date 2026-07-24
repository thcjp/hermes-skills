---
slug: "task-planner"
name: "task-planner"
version: 3.0.6
displayName: "Task Planner"
summary: "本地管任务/设优先级/追截止,支持中英双语。Manage tasks, set priorities, and track deadlines locally。Supports biling"
license: "MIT"
description: |-
  Manage tasks, set priorities, and track deadlines locally。Supports
  bilingual (EN/CN) documentati。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估.
tags:
  - Productivity
  - 任务管理
  - 效率
  - 工具
  - task
  - add
  - bash
  - priority
  - list
tools:
  - read
  - exec
  - write
homepage: ""
category: "Productivity"
---
# Task Planner

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

### add
Add a new task with optional priority and due date.

```bash
bash （请参考skill目录中的脚本文件） add "Task description" --priority high --due 2026-12-31
```

**输入**: 用户提供add所需的指令和必要参数.
**处理**: 解析add的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回add的处理结果,包含执行状态码、结果数据和执行日志。### list
Display pending or all tasks.

```bash
bash （请参考skill目录中的脚本文件） list --status pending
```

**输入**: 用户提供list所需的指令和必要参数.
**处理**: 解析list的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回list的处理结果,包含执行状态码、结果数据和执行日志。### done
Complete a task by ID.

```bash
bash （请参考skill目录中的脚本文件） done 1
```

**输入**: 用户提供done所需的指令和必要参数.
**处理**: 解析done的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回done的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

* **Daily Workflow**: Organizing your immediate to-do list and staying productive.
* **Deadline Tracking**: Keeping an eye on upcoming project milestones and due dates.
* **Privacy First**: When you need a task manager that doesn't upload your data to the cloud.

## 使用流程

Just ask your AI assistant: / 直接告诉 AI 助手：

1. "Add a high priority task: Finish report by Friday" (添加高优先级任务：周五前完成报告)
2. "Show all tasks due today" (显示今日待办任务)
3. "Mark task #1 as completed" (标记任务1为已完成)

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | task-planner处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1：基础用法

```
Just ask your AI assistant: / 直接告诉 AI 助手：
# ...
* "Add a high priority task: Finish report by Friday" (添加高优先级任务：周五前完成报告)
* "Show all tasks due today" (显示今日待办任务)
* "Mark task #1 as completed" (标记任务1为已完成)
```

## 常见问题

### Q1: 如何开始使用Task Planner？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 本地运行，不支持多设备同步
- 本地存储任务数据，不支持团队协作分配
- 免费版不支持甘特图与依赖关系管理等高级功能
- 任务提醒依赖Agent心跳触发，存在可能的延迟
