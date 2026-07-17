---
slug: web
name: web
version: "1.0.0"
displayName: Web Development
summary: Build, debug, and deploy websites using HTML, CSS, JavaScript, and modern
  frameworks following pr...
license: MIT
description: |-
  Build, debug, and deploy websites using HTML, CSS, JavaScript, and modern
  frameworks following pr...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: web, development, using, websites, build, debug, deploy
tags:
- Development
tools:
- read
- exec
---

# Web Development

## Quick Reference

| Need | See |
| --- | --- |
| HTML/CSS issues | `html-css.md` |
| JavaScript patterns | `javascript.md` |
| React/Next.js/frameworks | `frameworks.md` |
| Deploy to production | `deploy.md` |
| Performance/SEO/a11y | `performance.md` |

## Critical Rules

1. **DOCTYPE matters** — Missing `<!DOCTYPE html>` triggers quirks mode; layouts break unpredictably
2. **CSS specificity beats cascade** — `.class` overrides element selectors regardless of order
3. **`===` not `==`** — Type coercion causes `"0" == false` to be true
4. **Async/await in loops** — `forEach` doesn't await; use `for...of` or `Promise.all`
5. **CORS is server-side** — No client-side fix; configure `Access-Control-Allow-Origin` on the server
6. **Responsive = viewport meta** — Without `<meta name="viewport">`, mobile renders desktop-width
7. **Form without `preventDefault`** — Page reloads; call `e.preventDefault()` in submit handler
8. **Images need dimensions** — Missing `width`/`height` causes layout shift (CLS penalty)
9. **HTTPS or blocked** — Mixed content (HTTP resources on HTTPS pages) gets blocked by browsers
10. **Environment variables leak** — `NEXT_PUBLIC_*` exposes to client; never prefix secrets

## Common Requests

**"Make it responsive"** → Mobile-first CSS with media queries; test at 320px, 768px, 1024px
**"Deploy to production"** → See `deploy.md` for Vercel/Netlify/VPS patterns
**"Fix CORS error"** → Server must send headers; proxy through same-origin if you can't control server
**"Improve performance"** → Lighthouse audit; focus on LCP, CLS, FID; lazy-load below-fold images
**"Add SEO"** → Title/description per page, semantic HTML, OG tags, sitemap.xml

## Framework Decision Tree

* **Static content, fast builds** → Astro or plain HTML
* **Blog/docs with MDX** → Astro or Next.js App Router
* **Interactive app with auth** → Next.js or Remix
* **Full SSR/ISR control** → Next.js
* **Simple SPA, no SEO needed** → Vite + React/Vue

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
