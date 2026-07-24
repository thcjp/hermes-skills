---
slug: "agent-browser-automation"
name: "agent-browser-automation"
version: "0.1.0"
displayName: "Agent Browser"
summary: "无头浏览器自动化CLI,专为AI Agent优化,带可访问性树快照与引用,稳定抓取。Headless browser automation CLI optimized for AI agen"
license: "Proprietary"
description: |-
  Headless browser automation CLI optimized for AI agents with accessibility
  tree snapshots and ref。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags:
  - Research
  - Automation
  - 自动化
  - 工作流
  - 效率
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Agent Browser

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Agent Browser稳定抓取 | 不支持 | 支持 |
| 多标签页并行抓取 | 不支持 | 支持 |
| 反爬虫策略自动绕过 | 不支持 | 支持 |
| 页面结构变化自适应 | 不支持 | 支持 |
| 批量导出结构化数据 | 不支持 | 支持 |

## 核心能力

- Headless browser automation CLI optimized for AI agents with accessibility
  tree snapshots and ref
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 场景1: 无头浏览器自动化CLI | 用户请求数据 | 结构化处理结果 |
| 场景2: 专为AI Agent优化 | 用户请求数据 | 结构化处理结果 |
| 场景3: 带可访问性树快照与引用 | 用户请求数据 | 结构化处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. **初始化浏览器会话**: 启动无头浏览器实例,配置代理与用户代理参数
2. **执行页面交互**: 按照用户指令进行导航/点击/输入/提取等页面操作
3. **采集与返回数据**: 提取页面内容或操作结果,返回结构化数据与截图
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | agent-browser-automation处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "automation_result": "automation_result_value",
      "automation_metadata": "automation_metadata_value",
      "automation_status": "automation_status_value"
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

中间产物模板参考: `assets/agent-browser-automation_template`

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
## 案例展示

```bash
agent-browser open https://www.google.com
agent-browser snapshot -i --json
agent-browser fill @e1 "AI agents"
agent-browser press Enter
agent-browser wait --load networkidle
agent-browser snapshot -i --json
agent-browser get text @e3 --json
agent-browser get attr @e4 "href" --json
```

## 常见问题

### Q1: 如何开始使用Agent Browser？
A: 

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

