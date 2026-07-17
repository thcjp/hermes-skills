---
slug: google-fonts
name: google-fonts
version: "1.0.0"
displayName: Google Fonts
summary: Load Google Fonts with proper performance, subsetting, and proven font pairings.
license: MIT
description: |-
  Load Google Fonts with proper performance, subsetting, and proven font
  pairings.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: proper, google, load, fonts
tags:
- Other
tools:
- read
- exec
---

# Google Fonts

## Loading Mistakes

* Missing `display=swap` causes invisible text until font loads—always add it to URL
* Load only weights you use: `wght@400;600;700` not the entire family—each unused weight wastes ~20KB
* Missing preconnect slows load—add both: `<link rel="preconnect" href="https://fonts.googleapis.com">` and `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`

## Variable Fonts

* Inter, Roboto Flex, Montserrat, Open Sans have variable versions—one file for all weights
* Use `wght@100..900` syntax for variable—downloads single file instead of multiple
* CSS for variable: `font-weight: 450` works with any value in range
* Check "Variable" badge on font page—not all Google Fonts are variable

## Subsetting

* Default includes latin—only add `&subset=latin-ext` if you need Polish, Vietnamese, etc.
* CJK fonts (Noto Sans JP, etc.) are huge—Google serves them sliced, but still heavy
* Unused subsets = wasted bytes—check what characters you actually need

## Proven Pairings

**Serif + Sans-Serif (classic contrast):**

* Playfair Display (heading) + Source Sans Pro (body)
* Lora (heading) + Roboto (body)
* Libre Baskerville (heading) + Montserrat (body)
* Merriweather (heading) + Open Sans (body)

**Sans-Serif only (modern/clean):**

* Inter (both)—vary weight for hierarchy
* Montserrat (heading) + Hind (body)
* Poppins (heading) + Nunito (body)
* Work Sans (heading) + Open Sans (body)

**Tech/Startup:**

* Space Grotesk (heading) + Space Mono (code)
* DM Sans (heading) + DM Mono (code)
* IBM Plex Sans + IBM Plex Mono

**Display fonts (headings only):**

* Abril Fatface, Bebas Neue, Oswald—never use these for body text

## Font Selection by Purpose

* **Long-form reading:** Merriweather, Lora, Source Serif Pro, Crimson Text
* **UI/Interfaces:** Inter, Roboto, Open Sans, Nunito Sans (tall x-height, clear at small sizes)
* **Impact headings:** Playfair Display, Oswald, Bebas Neue (not for body)
* **Monospace:** JetBrains Mono, Fira Code, Source Code Pro

## Common Mistakes

* Loading 6+ weights "to be safe"—pick exactly the weights you use (usually 2-3)
* Using display fonts for paragraphs—Lobster, Pacifico, Abril Fatface are heading-only
* Two fonts too similar—Roboto + Open Sans look almost identical; just use one
* Missing font-weight in CSS—`font-weight: 600` won't work if you only loaded 400 and 700
* No fallback stack—always: `font-family: 'Inter', system-ui, sans-serif`

## Self-Hosting

* Self-host for GDPR compliance—Google Fonts loads from Google servers, logs IP addresses
* Use google-webfonts-helper to download files
* Same `font-display: swap` needed in your @font-face
* Self-hosted can be faster if your CDN is closer than Google's

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
