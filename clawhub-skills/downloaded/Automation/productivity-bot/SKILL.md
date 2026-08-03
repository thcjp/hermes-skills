---
slug: productivity-bot
name: productivity-bot
version: "1.0.0"
displayName: Productivity Bot
summary: "生产力任务自动化bot,数据处理/定时通知/工作流(社区下载版)"
  notifications, and wor...
license: MIT-0
description: |-
  Automation bot for productivity tasks including data processing, scheduled
  notifications, and wor。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Automation
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Productivity Bot

Automation bot for everyday productivity tasks.

## Features

### 1. Data Automation

* Auto-process CSV/Excel files
* Data transformation pipelines
* Report generation

### 2. Scheduled Tasks

* Daily reminders
* Periodic data syncs
  -定时报告

### 3. Notifications

* Email alerts
* Slack/Discord messages
* Custom webhooks

## Usage

```python
from productivity_bot import Scheduler, DataProcessor

scheduler = Scheduler()
scheduler.every day.at("9:00").do(send_report)

processor = DataProcessor()
processor.clean("dirty_data.csv").export("clean_data.csv")
```

## Requirements

* Python 3.8+
* Various API keys

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

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Productivity Bot？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Productivity Bot有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **数据格式限制**：Productivity Bot主要支持CSV和Excel文件的处理，对于其他格式的数据文件，如JSON或XML，可能需要额外的转换步骤。
- **数据量限制**：由于性能和资源限制，处理的数据量不宜过大。对于大规模数据集，建议分批处理或使用更适合大数据处理的工具。
- **输入内容限制**：输入内容应避免包含特殊字符或脚本，以防止潜在的安全风险。

### 性能边界
- **处理速度**：处理大量数据或复杂的数据转换时，可能需要较长时间。
- **并发处理**：同时处理多个任务时，性能可能会受到影响，建议根据实际情况调整任务队列。

### 兼容性约束
- **操作系统兼容性**：虽然支持Windows、macOS和Linux，但某些特定功能可能在不同的操作系统上有所不同。
- **Python版本兼容性**：要求Python 3.8及以上版本，不支持旧版本Python。
- **API兼容性**：依赖的LLM API版本可能影响Skill的功能和性能，请确保使用兼容的API版本。

