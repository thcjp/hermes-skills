---
slug: excel-formula
name: excel-formula
version: "2.0.1"
displayName: Excel Formula
summary: "从描述生成Excel公式并诊断表格错误,VLOOKUP不再难(社区下载版)"
  Use when writing VLOOK...
license: MIT-0
description: |-
  Generate Excel formulas from descriptions and diagnose spreadsheet errors。Use when writing VLOOK。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
- Integrations
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Excel Formula

## 使用流程

Just ask your AI assistant: / 直接告诉 AI 助手：

* "Help me VLOOKUP price from Sheet2 based on ID" (根据ID从Sheet2匹配价格)
* "Calculate days between two dates" (计算两个日期之间的天数)
* "Sum sales where category is Electronics" (计算电子类产品总销售额)

## Description / 描述

Generate Excel formulas from descriptions and diagnose spreadsheet errors. Use when writing VLOOKUP formulas, debugging errors, or converting formulas.

## 依赖说明

* bash 4+
* python3

## Feedback

<https://bytesagain.com/feedback/>
Powered by BytesAgain | bytesagain.com

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

- Generate Excel formulas from descriptions and diagnose spreadsheet errors
- Use when writing VLOOK
- 触发关键词: formulas, generate, excel, descriptions, formula

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
Just ask your AI assistant: / 直接告诉 AI 助手：

* "Help me VLOOKUP price from Sheet2 based on ID" (根据ID从Sheet2匹配价格)
* "Calculate days between two dates" (计算两个日期之间的天数)
* "Sum sales where category is Electronics" (计算电子类产品总销售额)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Excel Formula？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Excel Formula有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **描述清晰度**：输入描述必须足够清晰，避免歧义。模糊或过于宽泛的描述可能导致生成公式不准确。
- **数据格式**：输入的数据格式必须符合Excel公式的要求，如日期格式、数字格式等。
- **数据量**：对于非常大的数据集，生成公式可能需要较长时间，且性能可能会受到影响。

### 性能边界
- **响应时间**：对于复杂的查询或大型的数据集，技能的响应时间可能会增加。
- **并发处理**：技能可能不支持高并发请求，对于大量同时请求的情况，性能可能会下降。

### 兼容性约束
- **Excel版本**：技能可能不完全兼容所有Excel版本，特别是在使用较旧版本时。
- **操作系统**：技能可能对操作系统有特定的要求，如Windows 10或更高版本。
- **浏览器兼容性**：如果技能通过Web界面访问，可能需要特定的浏览器或浏览器插件。

### 其他限制
- **外部API限制**：如果技能依赖于外部API，可能会受到API提供商的限制，如请求频率限制。
- **模型能力**：技能的性能受限于其底层模型的能力，对于非常复杂的公式或错误诊断，技能可能无法提供准确的结果。
---

