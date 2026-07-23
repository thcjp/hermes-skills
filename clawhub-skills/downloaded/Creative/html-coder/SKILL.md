---
slug: html-coder
name: html-coder
version: "2.0.1"
displayName: HTML Coder
summary: "专家级HTML开发,构建网页/表单/交互内容(社区下载版)"
  content. Use when cr...
license: MIT-0
description: |-
  Expert HTML development skill for building web pages, forms, and interactive
  content。Use when cr。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# HTML Coder

Expert skill for professional HTML development with focus on semantic markup, accessibility, HTML5 features, and standards-compliant web content.

## When to Use This Skill

* Creating HTML documents with semantic structure
* Building accessible forms with HTML5 validation
* Implementing responsive markup and multimedia
* Using HTML5 APIs (Canvas, SVG, Storage, Geolocation)
* Troubleshooting validation or accessibility issues

## Core Capabilities

* **Semantic HTML**: Document structure, content sections, accessibility-first markup
* **Forms**: All input types, validation attributes, fieldsets, labels
* **Media**: Responsive images, audio/video, Canvas, SVG
* **HTML5 APIs**: Web Storage, Geolocation, Drag & Drop, Web Workers
* **Accessibility**: ARIA, screen reader support, WCAG compliance

## Essential References

Core documentation for HTML experts:

* [`references/add-css-style.md`](/api/v1/skills/html-coder/file?path=references%2Fadd-css-style.md&ownerHandle=jhauga) - Add CSS via `link` tag, inline, or embedded in html
* [`references/add-javascript.md`](/api/v1/skills/html-coder/file?path=references%2Fadd-javascript.md&ownerHandle=jhauga) - Add JavaScript via `script src="link.js"` tag, inline `script`, or embedded in html
* [`references/attributes.md`](/api/v1/skills/html-coder/file?path=references%2Fattributes.md&ownerHandle=jhauga) - HTML attribute essentials
* [`references/essentials.md`](/api/v1/skills/html-coder/file?path=references%2Fessentials.md&ownerHandle=jhauga) - Semantic markup, validation, responsive techniques
* [`references/global-attributes.md`](/api/v1/skills/html-coder/file?path=references%2Fglobal-attributes.md&ownerHandle=jhauga) - Complete global attribute information
* [`references/glossary.md`](/api/v1/skills/html-coder/file?path=references%2Fglossary.md&ownerHandle=jhauga) - Complete HTML element and attribute reference
* [`references/standards.md`](/api/v1/skills/html-coder/file?path=references%2Fstandards.md&ownerHandle=jhauga) - HTML5 specifications and standards

## Best Practices

**Semantic HTML** - Use elements that convey meaning: `<article>`, `<nav>`, `<header>`, `<section>`, `<footer>`, not div soup.

**Accessibility First** - Proper heading hierarchy, alt text, labels with inputs, keyboard navigation, ARIA when needed.

**HTML5 Validation** - Leverage built-in validation (`required`, `pattern`, `type="email"`) before JavaScript.

**Responsive Images** - Use `<picture>`, srcset, and `loading="lazy"` for performance.

**Performance** - Minimize DOM depth, optimize images, defer non-critical scripts, use semantic elements.

## Quick Patterns

### Semantic Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
</head>
<body>
  <header><nav><!-- Navigation --></nav></header>
  <main><article><!-- Content --></article></main>
  <aside><!-- Sidebar --></aside>
  <footer><!-- Footer --></footer>
</body>
</html>
```

### Accessible Form

```html
<form method="post" action="/submit">
  <fieldset>
    <legend>Contact</legend>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required
           pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$">
    <button type="submit">Send</button>
  </fieldset>
</form>
```

### Responsive Image

```html
<picture>
  <source media="(min-width: 1200px)" srcset="large.webp">
  <source media="(min-width: 768px)" srcset="medium.webp">
  <img src="small.jpg" alt="Description" loading="lazy">
</picture>
```

## Troubleshooting

* **Validation**: W3C Validator (validator.w3.org), check unclosed tags, verify nesting
* **Accessibility**: Lighthouse audit, screen reader testing, keyboard nav, color contrast
* **Compatibility**: Can I Use (caniuse.com), feature detection, provide fallbacks

## Key Standards

* **WHATWG HTML Living Standard**: <https://html.spec.whatwg.org/>
* **WCAG Accessibility**: <https://www.w3.org/WAI/WCAG21/quickref/>
* **MDN Web Docs**: <https://developer.mozilla.org/en-US/docs/Web/HTML>

---

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

- Expert HTML development skill for building web pages, forms, and interactive
  content
- Use when cr
- 触发关键词: development, skill, building, html, expert, coder

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

## 常见问题

### Q1: 如何开始使用HTML Coder？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: HTML Coder有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
