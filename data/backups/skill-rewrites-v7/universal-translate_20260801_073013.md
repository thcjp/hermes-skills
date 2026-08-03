---
slug: universal-translate
name: "universal-translate"
version: 1.0.1
displayName: "翻译"
summary: "在任意语言间翻译文本/文件/对话,自动检测源语言。Translate text, files, and conversations between any languages。Auto-de"
summary_zh: "在任意语言间翻译文本/文件/对话,自动检测源语言。Translate text, files, and conversations between any languages。Auto-de"
license: "MIT"
description: |-
  Translate text, files, and conversations between any languages。Auto-detects
  source language。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Development
  - 翻译
  - 语言
  - 工具
  - agent
  - api
tools:
  - read
  - exec
  - write
homepage: ""
category: "Knowledge"
---
# Universal Translate

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |
| 结果导出与多格式转换 | 不支持 | 支持 |
| 实时状态监控与异常告警 | 不支持 | 支持 |
| 历史记录回溯与差异对比 | 不支持 | 支持 |

## 核心能力

- Translate text, files, and conversations between any languages
- Auto-detects
  source language

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文件操作 | 文件路径与操作参数 | 操作结果与文件元信息 |
| AI对话 | 消息内容与会话ID | 回复文本与Token用量 |
| 在任意语言间翻译文本 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | universal-translate处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "translate_result": "translate_result_value",
      "translate_metadata": "translate_metadata_value",
      "translate_status": "translate_status_value"
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

中间产物模板参考: `assets/universal-translate_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

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
## 常见问题

### Q1: 如何开始使用Universal Translate？
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

### 输入限制
- **文本长度限制**：Universal Translate 2技能对单次翻译的文本长度有限制，超过限制的文本将被截断，可能导致翻译结果不完整。
- **文件大小限制**：对于文件翻译功能，上传的文件大小受到限制，过大文件可能导致上传失败或翻译错误。
- **并发请求限制**：技能的并发请求量有限制，超过限制可能导致请求被拒绝或延迟响应。

### 性能边界
- **翻译速度**：翻译速度受限于LLM API的响应速度和系统资源，对于大量或复杂的翻译任务，可能需要较长时间完成。
- **资源消耗**：翻译过程中，系统资源消耗较大，特别是在处理大量或大型文件时，可能导致系统性能下降。

### 兼容性约束
- **源语言支持**：虽然技能自动检测源语言，但并非所有语言都得到支持，部分罕见或小众语言可能无法正确识别或翻译。
- **目标语言支持**：技能支持多种目标语言，但某些语言组合可能因为LLM API的限制而无法翻译。
- **操作系统兼容性**：技能在Windows、macOS和Linux操作系统上运行，但某些特定功能可能在某些操作系统上不可用。

