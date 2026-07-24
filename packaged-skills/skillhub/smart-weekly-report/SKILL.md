---
slug: "smart-weekly-report"
name: "smart-weekly-report"
version: 1.1.4
displayName: "Report Generator"
summary: "周报自动生成器,按pipeline流程配置质量gate检查,支持多模式批量处理,付费版独享高级功能。"
license: "Proprietary"
description: |-
  自动提炼关键信息，生成结构化、专业且具有洞察力的周报。核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Productivity
  - 工具
  - 效率
  - 自动化
  - 工作流
  - 开发
  - 代码
  - 创意
  - report
  - step
  - 按流程执
  - 依赖说明
  - agent
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Report Generator

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Report Generator周报自动生成 | 不支持 | 支持 |
| Report Generatorpeline流程配置 | 不支持 | 支持 |
| Report Generator支持多模式批量处理 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |

## 核心能力

- Smart Weekly Report 结果导出 - 按流程执行步端到端pipeline配置流程
- Smart Weekly Report 实时监控 - 步骤间自动质量gate检查
- Smart Weekly Report 错误重试 - 支持多种变体等多种处理模式
- Smart Weekly Report 多格式支持 - 失败自动重试+断点续传
- Smart Weekly Report 扩展能力9 - 全流程可追溯, 输出执行日志
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 质量检查 | 代码库与标准配置 | 问题列表与修复建议 |
| 内容生成 | 提示词与风格参数 | 生成内容与质量评分 |
| 配置管理 | 配置项与目标值 | 配置生效状态与差异 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Step 1：角色识别与信息收集
当用户发起对话时，首先判断用户的职业角色。如果用户未说明，主动询问：

> "请问您的职业角色是什么？（例如：前端工程师、运营、销售、HR 等）这样我可以为您生成最匹配的周报格式。"

收集以下核心信息（可通过追问补全）：

* 本周完成了哪些工作/任务？
* 遇到了哪些问题或阻碍？
* 下周计划做什么？
* 有哪些关键数据或指标？（如有）
* 需要向谁汇报？（决定报告风格：向上汇报 / 团队内部 / 跨部门）

### Step 2：模板匹配
根据职业角色自动选择对应模板（见下方模板库），并生成报告.
### Step 3：输出与优化
生成报告后，询问用户：

> "以上是根据您提供的信息生成的周报，您可以告诉我需要调整的地方，例如：修改某个措辞、补充某项数据、调整报告风格（更正式/更简洁）等。"

---
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | smart-weekly-report处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "report_result": "report_result_value",
      "report_metadata": "report_metadata_value",
      "report_status": "report_status_value"
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

中间产物模板参考: `assets/smart-weekly-report_template`

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

### 示例1：基础用法
```
### Step 1：角色识别与信息收集(补充)
当用户发起对话时，首先判断用户的职业角色。如果用户未说明，主动询问：
# ...

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。
> "请问您的职业角色是什么？（例如：前端工程师、运营、销售、HR 等）这样我可以为您生成最匹配的周报格式。"
# ...
收集以下核心信息（可通过追问补全）：
# ...
* 本周完成了哪些工作/任务？
* 遇到了哪些问题或阻碍？
* 下周计划做什么？
* 有哪些关键数据或指标？（如有）
* 需要向谁汇报？（决定报告风格：向上汇报 / 团队内部 / 跨部门）
# ...
### Step 2：模板匹配(补充)
根据职业角色自动选择对应模板（见下方模板库），并生成报告.
# ...
### Step 3：输出与优化(补充)
生成报告后，询问用户：
# ...
> "以上是根据您提供的信息生成的周报，您可以告诉我需要调整的地方，例如：修改某个措辞、补充某项数据、调整报告风格（更正式/更简洁）等。"
# ...
---
```

## 常见问题

### Q1: 如何开始使用Report Generator？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

