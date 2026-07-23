---
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
summary: "把冗长混乱高风险文档转为更清晰推理与决策"
---
# ai-assistant

> **Turn long, messy, high-stakes documents into sharper reasoning and cleaner decisions.**

ai-assistant is a long-context reasoning optimizer for commercial and legal document workflows.

Use this skill when you need to:

* analyze long contracts, memos, proposals, or negotiations
* improve reasoning quality across dense written material
* surface contradictions, weak logic, or missing assumptions
* compress large documents into decision-ready summaries
* strengthen document structure before review or approval
* compare multiple versions of a long-form document

This skill does NOT:

* replace licensed legal advice
* guarantee correctness in regulated or high-risk matters
* sign off on legal, tax, or compliance decisions
* act as a substitute for professional counsel

---

## What This Skill Does

ai-assistant helps:

* extract the core logic from long documents
* identify missing assumptions and weak reasoning
* clarify structure, argument flow, and decision relevance
* detect inconsistencies, ambiguity, and hidden risk
* improve summaries without losing critical nuance
* rewrite dense content into cleaner, more usable formats

---

## 适用场景

* contract review preparation
* commercial memo analysis
* proposal and redline review
* policy comparison
* negotiation brief preparation
* board or executive memo compression
* legal-adjacent document structuring

---

## What to Provide

Useful input includes:

* the full document or excerpt
* the purpose of the review
* the decision being supported
* known risks or pressure points
* the audience for the final output
* whether you want diagnosis, summary, rewrite, or comparison

---

## Standard Output Format

DOCUMENT ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━
Purpose: [What this document is trying to do]
Audience: [Who the output is for]
Decision relevance: [Why this matters]

CORE LOGIC
━━━━━━━━━━━━━━━━━━━━━━━━━━

* [Main claim / obligation / commercial point]
* [Supporting logic]
* [Critical assumption]

RISKS / WEAK POINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ [Ambiguity]
⚠️ [Contradiction]
⚠️ [Missing assumption]
⚠️ [Commercial or legal risk signal]

STRUCTURE IMPROVEMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━

1. [How to make reasoning clearer]
2. [How to reduce ambiguity]
3. [How to improve decision usefulness]

RECOMMENDED NEXT STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━

* [Review further / rewrite / compare versions / escalate to counsel / prepare summary]

---

## Reasoning Principles

* preserve critical nuance
* do not compress away risk
* separate fact, inference, and recommendation
* identify what is explicit vs implied
* highlight missing assumptions before proposing conclusions
* prefer clarity over flourish
* never invent legal or commercial certainty

---

## Execution Protocol (for AI agents)

When user provides a long document, follow this sequence:

### Step 1: Parse context

Extract:

* document type
* intended audience
* decision being supported
* major obligations, claims, or asks
* commercial or legal sensitivity

### Step 2: Identify logic structure

Map:

* what the document is saying
* why it matters
* what assumptions it depends on
* what could fail under scrutiny

### Step 3: Detect weaknesses

Check for:

* ambiguity
* contradiction
* undefined terms
* missing scope boundaries
* missing decision logic
* hidden risk transfer
* structural confusion

### Step 4: Improve usefulness

Depending on request:

* summarize
* rewrite
* compare
* diagnose
* convert into brief / memo / checklist

### Step 5: Guardrails

If legal or commercial certainty cannot be established from the text:

* say so clearly
* mark uncertainty
* do not fabricate confidence

---

## Activation Rules (for AI agents)

### Use this skill when the user asks about:

* long documents
* contract-like text
* legal-adjacent review
* memo analysis
* commercial document reasoning
* dense text summarization with nuance
* comparing two long versions of a document

### Do NOT use this skill when:

* user only needs a casual short rewrite
* user needs creative writing instead of reasoning
* user needs formal legal advice or sign-off
* user asks for certainty where the text does not support it

### If context is ambiguous

Ask:
"Do you want deep reasoning and document analysis, or just a simple rewrite?"

---

## Works Well With

* `@ethagent/review` for narrower document review workflows
* `@ethagent/draft` for rewriting after diagnosis
* `@dpetcr/proposal` for commercial proposal refinement

---

## Boundaries

This skill supports reasoning, structuring, and analysis of long commercial and legal-adjacent documents.

It does not replace:

* licensed legal advice
* contract execution authority
* procurement approval
* tax or compliance judgment

Use outputs as analytical support, not formal sign-off.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
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

- Optimize long-context reasoning for commercial, legal, and high-stakes
  documents
- Built for users
- 触发关键词: context, optimize, commercial, long, ai-assistant, reasoning

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

### Q1: 如何开始使用Claude？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Claude有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
