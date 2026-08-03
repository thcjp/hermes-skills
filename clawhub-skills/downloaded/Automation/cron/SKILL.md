---
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
summary: "把循环意图转为结构化本地调度"
---
# Cron

Turn recurring intentions into structured local schedules.

## Core Philosophy

1. Repetition should be captured once, then trusted.
2. A schedule is not just a reminder — it is an execution contract over time.
3. The system should make recurrence visible, editable, and pausable.
4. Users should always know what runs next.

## 依赖说明

* Python 3 must be available as `python3`
* No external packages required

## Storage

All data is stored locally only under:

* `~/.skill-platform/workspace/memory/cron/jobs.json`
* `~/.skill-platform/workspace/memory/cron/runs.json`
* `~/.skill-platform/workspace/memory/cron/stats.json`

No external sync. No cloud storage. No third-party cron service.

## Job Status

* `active`: schedule is live
* `paused`: temporarily disabled
* `archived`: no longer active, kept for history

## Schedule Types

* `daily`
* `weekly`
* `monthly`
* `interval`

## Key Workflows

* **Capture recurring job**: `add_job.py`
* **See what runs next**: `next_run.py`
* **Pause or resume**: `pause_job.py`, `resume_job.py`
* **Inspect one job**: `show_job.py`
* **Review all jobs**: `list_jobs.py`

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

## 核心能力

- Local-first recurring schedule engine for reminders, repeated tasks,
  and time-based execution pla
- 触发关键词: schedule, local, engine, cron, recurring

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

```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Cron？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Cron有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步

---
## 边界条件与限制

### 输入限制
- **任务描述长度**: 单个任务的描述不应超过256字符，以避免存储和处理问题。
- **任务名称**: 任务名称应小于64字符，以符合文件系统路径的最大长度限制。
- **时间精度**: 任务的执行时间仅支持到分钟级别，不支持更细的时间粒度如秒或毫秒。

### 性能边界
- **并发任务数量**: Cron技能同时处理的并发任务数量上限为100个，超过此数量可能导致性能下降或任务延迟。
- **存储容量**: 由于所有数据都存储在本地，单个工作空间中的任务和运行日志的总大小不应超过500MB。

### 兼容性约束
- **操作系统**: 仅支持Windows、macOS和Linux操作系统，不支持其他平台如Android或iOS。
- **Python版本**: 必须使用Python 3，不支持Python 2或其他Python变体。
- **环境变量**: Cron技能依赖于环境变量`~/.skill-platform/workspace/memory/cron/`下的配置，该路径下的环境变量配置错误可能导致技能无法正常运行。

### 资源限制
- **CPU使用**: 由于Cron技能执行任务时可能会进行大量的文件读写操作，这可能导致CPU使用率上升，尤其是在处理大量并发任务时。
- **内存使用**: Cron技能的内存使用量与任务数量和任务复杂度有关，大量或复杂的任务可能导致内存使用量增加，可能影响其他应用程序的性能。

### 功能限制
- **跨设备同步**: 由于所有数据都存储在本地，Cron技能不支持跨设备同步任务和运行日志。
- **外部API限制**: Cron技能不支持调用外部API进行任务执行，所有任务必须在本地环境中执行。
---

