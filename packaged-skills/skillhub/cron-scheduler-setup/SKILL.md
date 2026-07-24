---
slug: "cron-scheduler-setup"
name: "cron-scheduler-setup"
version: 1.0.1
displayName: "SkillHub Cron Setup"
summary: "SkillHub Gateway 内置定时任务调度器。用于创建一次性提醒、周期性任务、后台自动化。支持主会话系统事件和独立会话执行，可配置投递到聊天频道或"
license: "Proprietary"
description: |-
  SkillHub Gateway 内置定时任务调度器。用于创建一次性提醒、周期性任务、后台自动化。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "定时任务,调度,自动化"
category: "Automation"
---
# SkillHub Cron Setup

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| SkillHub Cron Setup内置定时任务调度 | 不支持 | 支持 |
| SkillHub Cron Setup用于创建 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |

## 核心能力

- SkillHub Gateway 内置定时任务调度器
- 用于创建一次性提醒、周期性任务、后台自动化
- 支持主会话系统事件和独立会话执行，可配置投递到聊天频道或
  Webhook
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 会话管理 | 用户ID与消息内容 | 消息记录与会话状态 |
| 定时任务 | Cron表达式与任务定义 | 调度状态与执行记录 |
| 任务调度 | 任务ID与触发条件 | 执行结果与调度日志 |

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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | cron-scheduler-setup处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "setup_result": "setup_result_value",
      "setup_metadata": "setup_metadata_value",
      "setup_status": "setup_status_value"
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

中间产物模板参考: `assets/cron-scheduler-setup_template`

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

### 依赖说明(补充)
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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

