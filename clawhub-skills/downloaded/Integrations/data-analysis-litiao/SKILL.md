---
slug: data-analysis-litiao
name: data-analysis-litiao
version: "1.0.0"
displayName: Data Analysis Litiao
summary: "把原始数据变决策,统计严谨/方法得当/警惕分析陷阱"
  and awareness of analyti...
license: MIT-0
description: |-
  Turn raw data into decisions with statistical rigor, proper methodology,
  and awareness of analyti。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Data Analysis Litiao

## When to Load

User asks about: analyzing data, finding patterns, understanding metrics, testing hypotheses, cohort analysis, A/B testing, churn analysis, statistical significance.

## Core Principle

Analysis without a decision is just arithmetic. Always clarify: **What would change if this analysis shows X vs Y?**

## Methodology First

Before touching data:

1. **What decision** is this analysis supporting?
2. **What would change your mind?** (the real question)
3. **What data do you actually have** vs what you wish you had?
4. **What timeframe** is relevant?

## Statistical Rigor Checklist

* Sample size sufficient? (small N = wide confidence intervals)
* Comparison groups fair? (same time period, similar conditions)
* Multiple comparisons? (20 tests = 1 "significant" by chance)
* Effect size meaningful? (statistically significant ≠ practically important)
* Uncertainty quantified? ("12-18% lift" not just "15% lift")

## Analytical Pitfalls to Catch

| Pitfall | What it looks like | How to avoid |
| --- | --- | --- |
| Simpson's Paradox | Trend reverses when you segment | Always check by key dimensions |
| Survivorship bias | Only analyzing current users | Include churned/failed in dataset |
| Comparing unequal periods | Feb (28d) vs March (31d) | Normalize to per-day or same-length windows |
| p-hacking | Testing until something is "significant" | Pre-register hypotheses or adjust for multiple comparisons |
| Correlation in time series | Both went up = "related" | Check if controlling for time removes relationship |
| Aggregating percentages | Averaging percentages directly | Re-calculate from underlying totals |

For detailed examples of each pitfall, see `pitfalls.md`.

## Approach Selection

| Question type | Approach | Key output |
| --- | --- | --- |
| "Is X different from Y?" | Hypothesis test | p-value + effect size + CI |
| "What predicts Z?" | Regression/correlation | Coefficients + R² + residual check |
| "How do users behave over time?" | Cohort analysis | Retention curves by cohort |
| "Are these groups different?" | Segmentation | Profiles + statistical comparison |
| "What's unusual?" | Anomaly detection | Flagged points + context |

For technique details and when to use each, see `techniques.md`.

## Output Standards

1. **Lead with the insight**, not the methodology
2. **Quantify uncertainty** — ranges, not point estimates
3. **State limitations** — what this analysis can't tell you
4. **Recommend next steps** — what would strengthen the conclusion

## Red Flags to Escalate

* User wants to "prove" a predetermined conclusion
* Sample size too small for reliable inference
* Data quality issues that invalidate analysis
* Confounders that can't be controlled for

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

- Turn raw data into decisions with statistical rigor, proper methodology,
  and awareness of analyti
- 触发关键词: turn, analysis, data, litiao, decisions

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

### Q1: 如何开始使用Data Analysis Litiao？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Data Analysis Litiao有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
