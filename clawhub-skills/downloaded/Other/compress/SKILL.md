---
slug: compress
name: compress
version: "1.0.0"
displayName: Compress
summary: Compress text semantically with iterative validation, anchor checksums, and
  verified information ...
license: MIT
description: |-
  Compress text semantically with iterative validation, anchor checksums,
  and verified information ...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: compress, text, semantically, iterative
tags:
- Other
tools:
- read
- exec
---

# Compress

## ⚠️ Important Limitations

**This is SEMANTIC compression, not bit-perfect lossless.**

* L1-L2: Verified reconstruction, production-ready
* L3-L4: Experimental, may lose subtle information
* **Never use for:** Medical dosages, legal text, financial figures, safety-critical data

---

## The Validation Loop

```text
1. Compress original O → compressed C
2. Extract anchors from O (entities, numbers, dates)
3. Reconstruct C → R (without seeing O)
4. Verify: anchors match + semantic diff
5. If mismatch → refine C with missing info
6. Repeat until validated (max 3 iterations)
```

**Convergence = verified. No convergence after 3 rounds = level too aggressive.**

---

## Quick Reference

| Task | Load |
| --- | --- |
| Compression levels (L1-L4) | `levels.md` |
| Validation algorithm details | `validation.md` |
| Format-specific strategies | `formats.md` |
| Token budgeting and metrics | `metrics.md` |

---

## Compression Levels

| Level | Ratio | Reliability | Use Case |
| --- | --- | --- | --- |
| L1 | ~0.8x | ✅ High | Production, human-readable |
| L2 | ~0.5x | ✅ Good | System prompts, repeated use |
| L3 | ~0.3x | ⚠️ Moderate | Experimental, review output |
| L4 | ~0.15x | ⚠️ Low | Research only, expect losses |

---

## Anchor Checksum System

Before compression, extract critical facts:

```text
[ANCHORS: 3 people, $42,000, 2024-03-15, "Project Alpha"]
```

Reconstruction MUST reproduce these exactly. If anchors mismatch → compression failed.

---

## Core Rules

1. **Always validate** — Never trust compression without reconstruction test
2. **Use anchors** — Extract numbers, names, dates before compressing
3. **Cap at L2 for production** — L3-L4 are experimental
4. **Report confidence** — Include iteration count and anchor match rate
5. **Independent verification** — Consider different model for reconstruction

---

## Cost-Benefit Reality

Each compression costs 3-4 LLM calls. Break-even calculation:

```text
break_even_retrievals = compression_tokens / saved_tokens_per_use
```

**Only cost-effective if:** You'll retrieve the compressed content 6-8+ times.

For one-time use → just use the original text.

---

## Before Compressing

* Content type is NOT safety-critical
* Target level chosen (L1-L2 recommended)
* Anchors identified (numbers, names, dates)
* ROI makes sense (multiple retrievals expected)

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
