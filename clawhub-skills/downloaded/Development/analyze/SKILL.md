---
slug: analyze
name: analyze
version: "1.0.0"
displayName: Analyze
summary: Structured analysis for any input. Data, code, text, decisions, visuals.
  Prioritize, question, co...
license: MIT
description: |-
  Structured analysis for any input. Data, code, text, decisions, visuals.
  Prioritize, question, co...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: analysis, code, data, input, structured, analyze
tags:
- Development
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
