---
slug: "trading-strategy-guide"
name: "trading-strategy-guide"
version: "1.1.1"
displayName: "Trade With Taro"
summary: "提供交易策略分析与决策支持的AI技能。Provide AI-powered trading strategy analysis and decision support. Analyze m"
license: "Proprietary"
description: |-
  Provide AI-powered trading strategy analysis and decision support. Analyze
  market trends, evaluate trading signals, and generate strategy recommendations.
tags:
  - Other
  - UI设计
  - 前端
  - 设计
  - 依赖说明
  - agent
  - 确认运行
  - llm
  - 中的要求
tools:
  - read
  - write
  - exec
homepage: ""
category: "Creative"
---
# Trade With Taro

## 核心能力

- 提供交易策略分析与决策支持
- 分析市场趋势与交易信号
- 生成策略建议与风险评估
- 支持多种交易策略模式
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 策略分析 | 市场数据与交易参数 | 策略评估结果与建议 |
| 趋势研判 | 历史行情与技术指标 | 趋势判断与信号提示 |
| 风险评估 | 持仓与风险参数 | 风险等级与止损建议 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | trading-strategy-guide处理的内容输入 |,  |
| content | string | 否 | trading-strategy-guide处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "guide 相关配置参数",
    result: "guide 相关配置参数",
    result: "guide 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

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

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 常见问题

### Q1: 如何开始使用Trade With Taro？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
