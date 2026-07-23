---
slug: tailwindcss
name: tailwindcss
version: "1.0.0"
displayName: Tailwind CSS
summary: Write Tailwind utility classes with proper responsive design, dark mode,
  and configuration.
license: MIT
description: |-
  Write Tailwind utility classes with proper responsive design, dark mode,
  and configuration。核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关...
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Tailwind CSS

## Content Configuration

* `content` array in tailwind.config.js must include ALL files with classes—missing paths = missing styles in production
* Glob patterns: `"./src/**/*.{js,jsx,ts,tsx,html}"` covers nested directories
* Dynamic class names like `bg-${color}-500` won't be detected—use complete class names or safelist
* Check production build size—if unexpectedly small, content paths are wrong

## Responsive Prefixes

* Mobile-first: unprefixed styles apply to all sizes, `md:` applies at medium AND above
* `sm:hidden md:block` means hidden on small, visible on medium+—not "only on medium"
* Breakpoints: sm(640px), md(768px), lg(1024px), xl(1280px), 2xl(1536px)
* Custom breakpoints in config override defaults—use `extend.screens` to add without replacing

## Dark Mode

* `dark:` prefix requires `darkMode: 'class'` in config—won't work with default media strategy if you need manual toggle
* Dark class on `<html>` or `<body>`, not on individual components
* `dark:bg-gray-900` only applies when ancestor has `class="dark"`
* System preference: `darkMode: 'media'` uses `prefers-color-scheme`

## State Variants

* `hover:`, `focus:`, `active:` work as expected
* `group-hover:` requires `group` class on parent—child reacts to parent hover
* `peer-focus:` requires `peer` class on sibling AND sibling must come first in DOM
* Stack variants: `dark:hover:bg-gray-700` applies on hover in dark mode

## Arbitrary Values

* `bg-[#1da1f2]` for one-off colors—brackets for any arbitrary value
* `w-[calc(100%-2rem)]` for calc expressions
* `grid-cols-[1fr_2fr_1fr]` underscores for spaces in values
* Arbitrary properties: `[mask-type:alpha]` for unsupported CSS properties

## @apply Traps

* `@apply` in component CSS loses responsive/state variants—`@apply hover:bg-blue-500` doesn't work as expected
* Order in `@apply` matters unlike HTML classes—later utilities override earlier
* Prefer HTML classes over `@apply`—easier to maintain, better tree-shaking
* If you must use `@apply`, keep it simple: base styles only

## Configuration

* `extend` adds to defaults: `extend: { colors: { brand: '#xxx' } }` keeps all existing colors
* Top-level replaces defaults: `colors: { brand: '#xxx' }` removes all default colors
* `theme()` function in CSS: `border-color: theme('colors.gray.200')`
* Plugin order matters—later plugins can override earlier ones

## Important Modifier

* `!` prefix forces important: `!mt-4` generates `margin-top: 1rem !important`
* Use sparingly—usually indicates specificity battle that should be fixed
* `important: true` in config makes ALL utilities important—avoid, breaks third-party CSS
* `important: '#app'` scopes specificity to selector—better than global important

## Common Mistakes

* `class="px-4 px-6"` last one wins in stylesheet, not in HTML—both get applied, cascade decides
* Forgetting `overflow-hidden` with `rounded-*` on parent with absolute children
* `h-screen` doesn't account for mobile browser chrome—use `h-dvh` (dynamic viewport height)
* `truncate` needs width constraint or `max-w-*` to actually truncate

## Performance

* JIT is default since v3—generates only used classes, no purge needed
* Avoid `safelist` with patterns like `bg-*`—defeats tree-shaking
* `@layer components` for reusable component styles—proper cascade order
* Large arbitrary values generate unique classes—extract to config if repeated

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

- Write Tailwind utility classes with proper responsive design, dark mode,
  and configuration
- 触发关键词: utility, css, write, tailwindcss, tailwind, classes

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

### Q1: 如何开始使用Tailwind CSS？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Tailwind CSS有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
