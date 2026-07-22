---
slug: "cron-scheduler-setup"
name: "cron-scheduler-setup"
version: "1.0.0"
displayName: "SkillHub Cron Setup"
summary: "SkillHub Gateway 内置定时任务调度器。用于创建一次性提醒、周期性任务、后台自动化。支持主会话系统事件和独立会话执行，可配置投递到聊天频道或"
license: "MIT"
description: |-
  SkillHub Gateway 内置定时任务调度器。用于创建一次性提醒、周期性任务、后台自动化。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
  - Automation
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# SkillHub Cron Setup

## 核心能力

- SkillHub Gateway 内置定时任务调度器
- 用于创建一次性提醒、周期性任务、后台自动化
- 支持主会话系统事件和独立会话执行，可配置投递到聊天频道或
  Webhook
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
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Use、需要提升效率、自动化流程、批量处理、工作流优化时使用、不适用于需要人工、创意判断的任务、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. 创建一次性提醒（主会话）

```bash
skill-platform cron add \
  --name "提醒事项" \
  --at "20m" \
  --session main \
  --system-event "20 分钟后检查日历" \
  --wake now \
  --delete-after-run
```

### 2. 创建周期性任务（独立会话）

```bash
skill-platform cron add \
  --name "晨间简报" \
  --cron "0 7 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "总结昨晚的邮件和日历事件" \
  --announce \
  --channel telegram \
  --to "+8613800138000"
```

### 3. 创建带模型覆盖的深度任务

```bash
skill-platform cron add \
  --name "周报分析" \
  --cron "0 9 * * 1" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "分析本周项目进展" \
  --model "opus" \
  --thinking high \
  --announce \
  --channel whatsapp \
  --to "+8613800138000"
```

### 命令参数说明

1. `--thinking`: 命令参数,用于指定操作选项
2. `--channel`: 命令参数,用于指定操作选项
3. `--wake`: 命令参数,用于指定操作选项
4. `--session`: 命令参数,用于指定操作选项
5. `--announce`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `-health-summary`: 命令参数,用于指定操作选项
- `--delete-after-run`: 命令参数,用于指定操作选项
- `--message`: 命令参数,用于指定操作选项
- `--model`: 命令参数,用于指定操作选项
- `--system-event`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理

### 任务不执行

1. 检查 cron 是否启用：`cron.enabled: true`（配置中）
2. 检查 Gateway 是否持续运行（cron 在 Gateway 进程内执行）
3. 确认时区设置正确（`--tz` 参数）

### 任务反复延迟

* 连续失败会触发指数退避：30s → 1m → 5m → 15m → 60m
* 成功执行后退避重置

### 查看存储位置

* 任务存储：`~/.skill-platform/cron/jobs.json`
* 运行历史：`~/.skill-platform/cron/runs/<jobId>.jsonl`

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
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

当前工作配置示例（`~/.skill-platform/cron/jobs.json`）：

```json
{
  "name": "daily-health-summary",
  "schedule": {
    "kind": "cron",
    "expr": "0 10 * * *",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "从 Bitable 查询健康数据并生成总结"
  },
  "delivery": {
    "mode": "none",
    "channel": "last"
  }
}
```

## 常见问题

### Q1: 如何开始使用OpenClaw Cron Setup？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: SkillHub Cron Setup有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
