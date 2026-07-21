---
slug: in-depth-research
name: in-depth-research
version: "1.0.0"
displayName: Deep Research
summary: Conduct exhaustive multi-source investigation with methodology tracking,
  source evaluation, and i...
license: MIT
description: |-
  Conduct exhaustive multi-source investigation with methodology tracking,
  source evaluation, and i。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Research
tools:
  - - read
- exec
---

# Deep Research

## Core Role

Deep Research = investigate thoroughly until the question is answered. Not surface search — systematic exploration with documented methodology.

**Not:** quick lookups (→ just search), combining existing docs (→ Synthesize), ongoing monitoring (→ Digest)

## Protocol

```text
Scope → Search → Evaluate → Deepen → Synthesize → Document → Deliver
```

### 1. Scope

Before searching, clarify:

* What exactly needs answering?
* What depth is required? (Overview / Thorough / Exhaustive)
* What's the decision this enables?
* Time/effort budget?

Reframe vague questions into specific, answerable queries.

### 2. Search

Multi-vector approach (see `methodology.md`):

* Start broad, then narrow
* Multiple search engines/sources
* Follow citation trails
* Check primary sources when secondary cite them
* Look for contradicting viewpoints

Track every source. Nothing unattributed.

### 3. Evaluate

For each source (see `sources.md`):

* Authority: Who wrote this? What credentials?
* Recency: When? Still valid?
* Evidence: Claims backed by data?
* Bias: Any agenda or conflict?
* Corroboration: Do others confirm this?

Flag low-credibility sources. Weight findings accordingly.

### 4. Deepen

Research is iterative:

* Initial findings reveal new questions
* Follow promising threads
* Fill gaps identified
* Stop when: answer is clear, returns diminish, or budget exhausted

Document decision to stop and why.

### 5. Synthesize

Merge findings (use Synthesize skill patterns):

* Reconcile contradictions explicitly
* Weight by source quality
* Note confidence levels
* Identify remaining unknowns

### 6. Document

Research trail matters:

* Sources consulted (with links)
* Search queries used
* Why certain sources were weighted higher
* What was NOT found (gaps)

### 7. Deliver

Format per user needs (see `output-formats.md`):

* Executive: BLUF + key findings + confidence
* Academic: Full methodology + citations
* Working doc: All findings for further work

## Output Format (Default)

```text
🔬 DEEP RESEARCH: [Topic]

⚡ ANSWER
[Direct answer to the question — 2-3 sentences]

📊 CONFIDENCE: [High/Medium/Low] — [why]

🔍 KEY FINDINGS
• [Finding 1] — [source]
• [Finding 2] — [source]
• [Finding 3] — [source]

⚠️ CAVEATS
• [Important limitation or uncertainty]

🕳️ GAPS
• [What couldn't be determined]

📚 SOURCES ([count])
[Numbered list with credibility notes]

🔎 METHODOLOGY
[Brief: what was searched, how sources were evaluated]
```

## Depth Levels

| Level | Effort | Sources | When |
| --- | --- | --- | --- |
| Quick | 5-10 min | 3-5 | Simple factual questions |
| Standard | 30-60 min | 8-15 | Most research requests |
| Thorough | 2-4 hours | 20-30 | Important decisions |
| Exhaustive | Days | 50+ | Critical, high-stakes |

Confirm depth before starting. Adjust if findings warrant.

---

*References: `methodology.md`, `sources.md`, `output-formats.md`*

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

- Conduct exhaustive multi-source investigation with methodology tracking,
  source evaluation, and i
- 触发关键词: investigation, source, conduct, multi, exhaustive, deep, research, depth

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

### Q1: 如何开始使用Deep Research？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Deep Research有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
