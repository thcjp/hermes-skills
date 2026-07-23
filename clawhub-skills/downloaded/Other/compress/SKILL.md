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
  and verified information 。Use when 用户需要Compress相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Compress

## 已知限制

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

- Compress text semantically with iterative validation, anchor checksums,
  and verified information
- 触发关键词: compress, text, semantically, iterative

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

### Q1: 如何开始使用Compress？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Compress有什么限制？
A: 请参考已知限制章节了解具体限制。
