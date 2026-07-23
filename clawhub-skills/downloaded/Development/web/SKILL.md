---
slug: web
name: web
version: "1.0.0"
displayName: Web Development
summary: "用HTML/CSS/JS与现代框架建调部署网站(社区下载版)"
  frameworks following pr...
license: MIT
description: |-
  Build, debug, and deploy websites using HTML, CSS, JavaScript, and modern
  frameworks following pr。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Build, debug, and deploy websites using HTML, CSS, JavaScript, and modern
  frameworks following pr
- 触发关键词: web, development, using, websites, build, debug, deploy

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

### Q1: 如何开始使用Web Development？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Web Development有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
