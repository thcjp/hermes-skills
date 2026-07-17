---
slug: logo
name: logo
version: "1.0.0"
displayName: Logo
summary: Generate logos with AI image tools using effective prompt structures, validation
  loops, and expor...
license: MIT
description: |-
  Generate logos with AI image tools using effective prompt structures,
  validation loops, and expor...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: logo, generate, logos, tools, image
tags:
- Creative
tools:
- read
- exec
---

# Logo

## Quick Start: AI Logo Generation

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
