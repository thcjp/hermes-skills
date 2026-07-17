---
slug: logo-design-guide
name: logo-design-guide
version: "0.1.5"
displayName: Logo Design Guide
summary: Logo design principles and AI image generation best practices for creating
  logos. Covers logo typ...
license: MIT
description: |-
  Logo design principles and AI image generation best practices for creating
  logos. Covers logo typ...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: logo, guide, principles, design, generation, image
tags:
- Creative
tools:
- read
- exec
---

# Logo Design Guide

Design effective logos with AI image generation via [inference.sh](https://inference.sh) CLI.

## Quick Start

```bash
curl -fsSL https://cli.inference.sh | sh && infsh login

infsh app run falai/flux-dev-lora --input '{
  "prompt": "flat vector logo of a mountain peak with a sunrise, minimal geometric style, single color, clean lines, white background",
  "width": 1024,
  "height": 1024
}'
```

> **Install note:** The [install script](https://cli.inference.sh) only detects your OS/architecture, downloads the matching binary from `dist.inference.sh`, and verifies its SHA-256 checksum. No elevated permissions or background processes. [Manual install & verification](https://dist.inference.sh/cli/checksums.txt) available.

## Logo Types

| Type | Description | When to Use | Example |
| --- | --- | --- | --- |
| **Wordmark** | Company name styled as logo | Strong brand name, short (< 10 chars) | Google, Coca-Cola |
| **Lettermark** | Initials only | Long company name, formal | IBM, HBO, CNN |
| **Pictorial** | Recognizable icon/symbol | Universal brand, works without text | Apple, Twitter bird |
| **Abstract** | Geometric/non-literal shape | Tech companies, conceptual brands | Nike swoosh, Pepsi |
| **Mascot** | Character illustration | Friendly brands, food/sports | KFC Colonel, Pringles |
| **Combination** | Icon + wordmark together | New brands needing both recognition and name | Burger King, Adidas |

## Critical AI Limitation

**AI image generators cannot reliably render text.** Letters will be distorted, misspelled, or garbled.

Strategy:

1. Generate the **icon/symbol only** with AI
2. Add text/wordmark in a design tool (Figma, Canva, Illustrator)
3. Or use a combination approach: AI icon + manually set typography

## Prompting for Logos

### Keywords That Work

```text
flat vector logo, simple minimal icon, single color silhouette,
geometric logo mark, clean lines, negative space design,
line art logo, flat design icon, minimalist symbol
```

### Keywords That Fail

```text
❌ photorealistic logo (contradiction — logos aren't photos)
❌ 3D rendered logo (too complex, won't scale down)
❌ gradient logo (inconsistent results, hard to reproduce)
❌ logo with text "Company Name" (text rendering fails)
```

### Prompt Structure

```text
flat vector logo of [subject], [style], [color constraint], [background], [additional detail]
```

### Examples by Logo Type

```bash
infsh app run falai/flux-dev-lora --input '{
  "prompt": "flat vector abstract logo, interlocking hexagonal shapes forming a letter S, minimal geometric style, single navy blue color, white background, clean sharp edges"
}'

infsh app run falai/flux-dev-lora --input '{
  "prompt": "flat vector logo of a fox head in profile, geometric faceted style, orange and white, minimal clean lines, white background, negative space design"
}'

infsh app run bytedance/seedream-4-5 --input '{
  "prompt": "friendly cartoon owl mascot logo, simple flat illustration, wearing graduation cap, purple and gold colors, white background, clean vector style"
}'

infsh app run xai/grok-imagine-image-pro --input '{
  "prompt": "minimal abstract logo mark, interconnected nodes forming a brain shape, line art style, single teal color, white background, tech startup aesthetic"
}'
```

## Scalability Rules

A logo must work at every size:

| Context | Size | What Must Work |
| --- | --- | --- |
| Favicon | 16x16 px | Silhouette recognizable |
| App icon | 1024x1024 px | Full detail visible |
| Social avatar | 400x400 px | Clear at a glance |
| Business card | ~1 inch | Clean print reproduction |
| Billboard | 10+ feet | No pixelation, simple enough |

### Scalability Checklist

* Recognizable as a 16px favicon (squint test)
* Works in single color (black on white)
* Works inverted (white on black)
* No tiny details that disappear at small sizes
* No thin lines that vanish when shrunk
* Clear silhouette without color

## Color Guidelines

* **Maximum 2-3 colors** for the primary logo
* Must work in **single color** (black, white, or brand primary)
* Consider **color psychology**:
  + Blue: trust, professional (finance, tech, healthcare)
  + Red: energy, urgency (food, entertainment, retail)
  + Green: growth, nature (health, sustainability, finance)
  + Orange: friendly, creative (startups, youth brands)
  + Purple: luxury, wisdom (beauty, education)
  + Black: premium, elegant (fashion, luxury, tech)
* Test on both light and dark backgrounds

## Iteration Workflow

```bash
for i in {1..5}; do
  infsh app run falai/flux-dev-lora --input '{
    "prompt": "flat vector logo of a lighthouse, minimal geometric, single color, white background"
  }' --no-wait
done

infsh app run falai/flux-dev-lora --input '{
  "prompt": "flat vector logo of a geometric lighthouse with light beam rays, minimal line art, navy blue, white background, negative space design"
}'

infsh app run bytedance/seedream-4-5 --input '{
  "prompt": "flat vector logo of a geometric lighthouse with radiating light beams, minimal clean design, navy blue single color, pure white background",
  "size": "2K"
}'

infsh app run falai/topaz-image-upscaler --input '{
  "image": "path/to/best-logo.png",
  "scale": 4
}'
```

## Common Mistakes

| Mistake | Problem | Fix |
| --- | --- | --- |
| Too much detail | Loses clarity at small sizes | Simplify to essential shapes |
| Relies on color | Fails in B&W contexts | Design in black first |
| Text in AI generation | Garbled/misspelled letters | Generate icon only, add text manually |
| Trendy effects (glows, shadows) | Dates quickly, reproduction issues | Stick to flat, timeless design |
| Too many colors | Hard to reproduce, expensive printing | Max 2-3 colors |
| Asymmetric without purpose | Looks unfinished | Use intentional asymmetry or stay balanced |

## File Format Delivery

| Format | Use Case |
| --- | --- |
| SVG | Scalable vector, web, editing |
| PNG (transparent) | Digital use, presentations |
| PNG (white bg) | Documents, email signatures |
| ICO / Favicon | Website favicon (16, 32, 48px) |
| High-res PNG (4096px+) | Print, billboards |

Note: AI generates raster images (PNG). For true vector SVG, use the AI output as a reference and trace in a vector tool, or use AI-to-SVG conversion tools.

## Related Skills

```bash
* 安装此Skill请参考SkillHub平台指南
* 安装此Skill请参考SkillHub平台指南
```

Browse all apps: `infsh app list`

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
