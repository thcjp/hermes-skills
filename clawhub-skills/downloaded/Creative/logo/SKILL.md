---
slug: logo
name: logo
version: "1.0.0"
displayName: Logo
summary: "用AI图像工具生成logo,提示结构/校验/导出"
  loops, and expor...
license: MIT
description: |-
  Generate logos with AI image tools using effective prompt structures,
  validation loops, and expor。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Logo

## 使用流程

**Best model for most logos: Nano Banana Pro** (Gemini 3 Pro Image)

### Basic Prompt Formula

```text
Create a [STYLE] logo featuring [ELEMENT] on [BACKGROUND].
[DESCRIPTION]. The logo should look good at 32px with recognizable shapes.
```

### Example

```text
Create a minimalist logo featuring a geometric mountain peak on white background.
Clean lines, navy blue (#1E3A5A), modern and professional style.
The logo should look good at 32px with recognizable shapes.
```

For the full 7-step prompt framework and model comparison, load `ai-generation.md`.

---

## Decision Tree

| Situation | Load |
| --- | --- |
| AI generation (Nano Banana, GPT Image, prompts, iOS icons) | `ai-generation.md` |
| Logo types (wordmark, symbol, combo, emblem) | `types.md` |
| Design process with a human designer | `process.md` |
| File formats and export requirements | `formats.md` |
| DIY without AI (templates, Canva) | `diy.md` |
| Hiring designers or agencies | `hiring.md` |

---

## Model Quick Reference

| Model | Best For |
| --- | --- |
| **Nano Banana Pro** | Overall best, text + icons, App Store icons |
| **GPT Image 1.5** | Conversational iteration, natural language |
| **Ideogram** | Perfect text rendering |
| **Midjourney v7** | Artistic icons only (no text) |

---

## iOS App Icons (Liquid Glass)

iOS 26 uses Liquid Glass design. Use this prompt structure:

```text
Create a polished iOS app icon featuring [ELEMENT].
Rounded square with [COLOR] gradient, minimalist white symbol centered.
Soft shadows, glassy depth effect, works at 60px.
The icon represents [APP PURPOSE].
```

See `ai-generation.md` for the complete iOS 26 prompt template.

---

## Validation Loop (MANDATORY)

**NEVER deliver without visual review.** Every AI output must be inspected before sharing.

1. Generate → 2. Look at the actual image → 3. Check for issues → 4. Fix or regenerate → 5. Repeat (max 5-7 attempts)

**Common fixes:**

* Unwanted padding → Crop
* Elements cut off → Regenerate with "centered composition"
* Text garbled → Use Nano Banana/Ideogram or add manually
* Too complex → Simplify prompt

If 5-7 attempts fail, change model or strategy entirely.

---

## Universal Truths

**AI output is a starting point.** Every AI logo needs vectorization, cleanup, and manual text refinement. Never use raw output as final.

**Test at small sizes early.** If it doesn't work at 32px, simplify. Most real-world usage is small.

**Text handling varies.** Only Nano Banana and Ideogram reliably render text. For Midjourney, generate icon-only.

**Simple logos last.** Nike, Apple, McDonald's. Complexity dates quickly and fails at small sizes.

---

## Before Finalizing

* Works in black and white
* Readable at 32px (favicon test)
* Vectorized (SVG), not just PNG
* All variants created (horizontal, stacked, icon-only)
* Text manually refined, not AI-generated
* Tested on dark and light backgrounds

---

## When to Load More

| Situation | Reference |
| --- | --- |
| Full prompt frameworks, model comparison, iOS icons | `ai-generation.md` |
| Wordmark vs symbol vs emblem decisions | `types.md` |
| Working with designers, brief templates | `process.md` |
| SVG, PNG, favicon, size requirements | `formats.md` |
| Track what works, learn from iterations | `feedback.md` |

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

- Generate logos with AI image tools using effective prompt structures,
  validation loops, and expor
- 触发关键词: logo, generate, logos, tools, image

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Logo？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Logo有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
