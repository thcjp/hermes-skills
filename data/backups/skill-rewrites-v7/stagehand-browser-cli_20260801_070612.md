---
slug: stagehand-browser-cli
name: "stagehand-browser-cli"
version: 1.0.1
displayName: "浏览器命令行"
summary: "经CLI用自然语言自动化浏览器交互。Automate web browser interactions using natural language via CLI commands。Use"
summary_zh: "经CLI用自然语言自动化浏览器交互。Automate web browser interactions using natural language via CLI commands。Use"
license: "MIT"
description: |-
  Automate web browser interactions using natural language via CLI commands。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。
tags:
  - Research
  - Automation
  - 工具
  - 效率
  - browser
  - step
  - cli
  - stagehand
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Stagehand Browser Cl

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多标签页并行抓取 | 不支持 | 支持 |
| 反爬虫策略自动绕过 | 不支持 | 支持 |
| 页面结构变化自适应 | 不支持 | 支持 |
| 批量导出结构化数据 | 不支持 | 支持 |
| Cookie池管理与IP轮换 | 不支持 | 支持 |

## 核心能力

- Automate web browser interactions using natural language via CLI commands
- Use when the user asks

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 交互响应 | 事件与回调数据 | 响应状态与交互结果 |
| 自动化流程 | 流程定义与触发参数 | 执行状态与步骤日志 |
| 经CLI用自然语言自 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | stagehand-browser-cli处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "cli_result": "cli_result_value",
      "cli_metadata": "cli_metadata_value",
      "cli_status": "cli_status_value"
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

中间产物模板参考: `assets/stagehand-browser-cli_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| Step Stagehand Browser Cli 核心处理处理失败 | 按流程执行 | 自动(最多max_retries次), 仍失败则记录断点, 暂停流程 |
| Gate条件不满足 | Step Stagehand Browser Cli 智能分析输出质量不达标 | 返回Step Stagehand Browser Cli 智能分析重新处理, 或提示用户调整输入 |
| 输入数据格式错误 | content格式不符合要求 | 列出期望格式, 提供示例, 中止流程 |
| 断点续传失败 | 缓存的中间产物已过期或损坏 | 从Step 1重新开始, 清除旧缓存 |
| 超时 | 总处理时间超过Stagehand Browser Cli 批量处理分钟 | 返回已完成步骤的结果, 标记为partial |
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

```bash
browser navigate https://example.com
browser act "click the Sign In button"
browser extract "get the page title"
browser close
```

## 常见问题

### Q1: 如何开始使用Stagehand Browser Cl？
A: 请参考使用流程和依赖说明章节，确保运行环境满足要求后调用本技能。
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

---
## 边界条件与限制 (Boundary Conditions)

Stagehand Browser CLI 2在执行任务时存在一些边界条件和限制，以下是该技能可能遇到的具体情况：

- **输入内容长度限制**：由于性能和资源限制，输入内容（如网页URL、文本数据）长度可能存在上限，超过此长度可能导致处理失败。
- **并发处理限制**：在付费版中，虽然支持多标签页并行抓取，但系统对同时处理的标签页数量有限制，过多并发可能导致性能下降或服务不可用。
- **网络稳定性要求**：Stagehand Browser CLI 2依赖于稳定的网络连接，频繁的网络中断或延迟可能导致任务失败或执行超时。
- **浏览器兼容性**：虽然技能旨在自动化浏览器交互，但某些浏览器扩展或特定浏览器版本的兼容性问题可能导致技能无法正常工作。
- **数据结构复杂性**：对于复杂的页面结构，技能可能无法完全解析和提取所需数据，特别是当页面使用高度非标准的HTML或JavaScript时。
- **API调用限制**：如果依赖LLM API，可能会遇到API调用频率限制，超过限制可能导致服务暂时不可用。
- **输出格式限制**：技能支持的输出格式有限，对于非JSON、非文本、非Markdown格式的输出请求，技能可能无法正确处理。
- **错误处理限制**：对于某些不可预见的异常情况，技能可能无法提供详细的错误信息，需要用户自行排查问题。

以上限制和条件需要在使用Stagehand Browser CLI 2时予以考虑，以确保技能能够高效、稳定地执行任务。

