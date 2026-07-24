---
slug: "smart-auto-updater"
name: "smart-auto-updater"
version: 1.0.1
displayName: "Smart Auto Updater"
summary: "AI驱动影响评估的智能自动更新器,查更新/析变更。Smart auto-updater with AI-powered impact assessment。Checks updates, a"
license: "Proprietary"
description: |-
  Smart auto-updater with AI-powered impact assessment。Checks updates,
  analyzes changes, evaluates。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags:
  - Other
  - 工具
  - 效率
  - 自动化
  - 创意
  - 图像
  - 工作流
  - AI代理
  - 按流程执
  - smart
  - step
  - auto
  - updater
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Smart Auto Updater

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Smart Auto UpdaterAI驱动影响评估 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

1. **Dry Run First** - Always check before acting
2. **Risk Classification** - AI-powered impact assessment
3. **Configurable Thresholds** - Set your own risk tolerance
4. **Detailed Logging** - Every decision is logged
5. **Manual Override** - Always can review before updating
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 智能家居 | 设备ID与场景模式 | 设备状态与执行确认 |
| AI驱动影响评估的智 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Basic usage

```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Run smart update check"
```

### With custom parameters

```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Check updates with custom settings: auto-update LOW risk, report MEDIUM risk"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | smart-auto-updater处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "updater_result": "updater_result_value",
      "updater_metadata": "updater_metadata_value",
      "updater_status": "updater_status_value"
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

中间产物模板参考: `assets/smart-auto-updater_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| Step Smart Auto Updater 核心处理处理失败 | 按流程执行 | 自动(最多max_retries次), 仍失败则记录断点, 暂停流程 |
| Gate条件不满足 | Step Smart Auto Updater 智能分析输出质量不达标 | 返回Step Smart Auto Updater 智能分析重新处理, 或提示用户调整输入 |
| 输入数据格式错误 | content格式不符合要求 | 列出期望格式, 提供示例, 中止流程 |
| 断点续传失败 | 缓存的中间产物已过期或损坏 | 从Step 1重新开始, 清除旧缓存 |
| 超时 | 总处理时间超过Smart Auto Updater 批量处理分钟 | 返回已完成步骤的结果, 标记为partial |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
### Basic usage(补充)
# ...
```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Run smart update check"
```
# ...
### With custom parameters(补充)
# ...
```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Check updates with custom settings: auto-update LOW risk, report MEDIUM risk"
```
```

## 常见问题

### Q1: 如何开始使用Smart Auto Updater？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

