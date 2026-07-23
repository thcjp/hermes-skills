---
slug: analyze
name: analyze
version: "1.0.0"
displayName: Analyze
summary: "对任意输入做结构化分析,数据/代码/文本/决策/可视化"
  Prioritize, question, co...
license: MIT
description: |-
  Structured analysis for any input。Data, code, text, decisions, visuals。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Analyze

## Pattern

```text
Purpose → Structure → Analyze → Prioritize → Conclude
```

Before analyzing: State what decision this serves. Pick a framework. Note first impression to challenge later.

## Before

* **Purpose in one line**: "This analysis helps decide ___"
* **What's missing**: 3+ unknowns that would change conclusions
* **First impression**: Write it — then seek counter-evidence

## During

* **Prioritize always**: 🔴 Critical (1-2 max) · 🟡 Important (2-3) · ⚪ Minor
* **Mark sources**: Every claim gets `[from input]` or `[inferred]`
* **Seek disconfirmation**: Dedicate space to "why I might be wrong"
* **Distinguish**: Facts vs opinions. Correlation vs causation.

## After

* **One-line summary**: Force analysis into one sentence
* **So what?**: End with action, not summary
* **Obviousness test**: Would someone say this without reading? → Deeper

## Traps

* **Superficial**: Paraphrasing ≠ analysis
* **Equal weight**: Everything yellow = nothing prioritized
* **Confirmation bias**: First impression became conclusion
* **Missing denominator**: "500 cancellations" of 600 or 50,000?
* **Invented data**: Stats without source = hallucination

## By Domain

| Domain | Focus | Watch |
| --- | --- | --- |
| Data | Grain, missing, outliers | Centinels, mixed types |
| Code | Production breaks, dead code | Style ≠ bugs |
| Text | Thesis, evidence strength | Unsourced claims |
| Decisions | Unlisted options, reversibility | Status quo bias |
| Visual | Dominance, consistency | Platform conventions |

## Frameworks

Pick one before starting:

* **MECE**: Mutually exclusive, collectively exhaustive
* **Pros/Cons+**: Add reversibility + cost of inaction
* **Pre-mortem**: Assume failure — why?
* **Steel man**: Best opposing argument

## Output

```text
🎯 PURPOSE: Decide [X]
🔴 CRITICAL: [Finding + source]
🟡 IMPORTANT: [Findings]
⚠️ COUNTER: [Contradictions]
➡️ ACTION: [Recommendation]
```

---

*Channels, not teaches. Ensures prioritization, questioning, and conclusions.*

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Structured analysis for any input
- Data, code, text, decisions, visuals
- Prioritize, question, co
- 触发关键词: analysis, code, data, input, structured, analyze

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
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Analyze？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Analyze有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
