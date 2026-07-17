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
  source evaluation, and i...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: investigation, source, conduct, multi, exhaustive, deep, research, depth
tags:
- Research
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
