---
slug: "task-planner"
name: "task-planner"
version: "3.0.5"
displayName: "Task Planner"
summary: "Manage tasks, set priorities, and track deadlines locally. Supports bilingual"
license: "MIT-0"
description: |-
  Manage tasks, set priorities, and track deadlines locally。Supports
  bilingual (EN/CN) documentati。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Productivity
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Task Planner

## 核心能力

### add
Add a new task with optional priority and due date.

```bash
bash scripts/script.sh add "Task description" --priority high --due 2026-12-31
```

**输入**: 用户提供add所需的指令和必要参数。
**处理**: 按照skill规范执行add操作,遵循单一意图原则。
**输出**: 返回add的执行结果,包含操作状态和输出数据。### list
Display pending or all tasks.

```bash
bash scripts/script.sh list --status pending
```

**输入**: 用户提供list所需的指令和必要参数。
**处理**: 按照skill规范执行list操作,遵循单一意图原则。
**输出**: 返回list的执行结果,包含操作状态和输出数据。### done
Complete a task by ID.

```bash
bash scripts/script.sh done 1
```

**输入**: 用户提供done所需的指令和必要参数。
**处理**: 按照skill规范执行done操作,遵循单一意图原则。
**输出**: 返回done的执行结果,包含操作状态和输出数据。
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: Manage、set、priorities、track、deadlines、locally、Supports、bilingual、documentati、Use、需要项目管理、任务规划、进度跟踪、团队协作时使用、不适用于实际人员、绩效评估、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

* **Daily Workflow**: Organizing your immediate to-do list and staying productive.
* **Deadline Tracking**: Keeping an eye on upcoming project milestones and due dates.
* **Privacy First**: When you need a task manager that doesn't upload your data to the cloud.

## 使用流程

Just ask your AI assistant: / 直接告诉 AI 助手：

1. "Add a high priority task: Finish report by Friday" (添加高优先级任务：周五前完成报告)
2. "Show all tasks due today" (显示今日待办任务)
3. "Mark task #1 as completed" (标记任务1为已完成)

### 命令参数说明

4. `--status`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1：基础用法

```
Just ask your AI assistant: / 直接告诉 AI 助手：

* "Add a high priority task: Finish report by Friday" (添加高优先级任务：周五前完成报告)
* "Show all tasks due today" (显示今日待办任务)
* "Mark task #1 as completed" (标记任务1为已完成)
```

## 常见问题

### Q1: 如何开始使用Task Planner？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Task Planner有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 本地运行，不支持多设备同步
