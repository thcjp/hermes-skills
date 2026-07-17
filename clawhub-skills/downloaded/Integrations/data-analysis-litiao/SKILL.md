---
slug: data-analysis-litiao
name: data-analysis-litiao
version: "1.0.0"
displayName: Data Analysis Litiao
summary: Turn raw data into decisions with statistical rigor, proper methodology,
  and awareness of analyti...
license: MIT-0
description: |-
  Turn raw data into decisions with statistical rigor, proper methodology,
  and awareness of analyti...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: turn, analysis, data, litiao, decisions
tags:
- Integrations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
