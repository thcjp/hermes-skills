---
slug: ui-ux-design-tool-pro
name: ui-ux-design-tool-pro
version: "1.0.0"
displayName: UI/UX设计指南专业版
summary: 企业级UI/UX设计体系,含WCAG 2.2合规、设计令牌、Shadcn/ui集成、2026趋势与顶级产品深度分析
license: MIT
edition: pro
description: |-
  面向企业设计团队和专业前端的完整UI/UX设计体系,涵盖WCAG 2.2无障碍合规、
  设计令牌系统、Shadcn/ui组件库深度集成、2026设计趋势、微交互动画模式、
  以及对顶级产品的深度设计分析。

  核心能力:
  - WCAG 2.2完整无障碍合规指南(ARIA、键盘导航、屏幕阅读器)
  - 设计令牌系统(色彩、字体、间距、圆角、阴影的语义化体系)
  - Shadcn/ui + Tailwind CSS深度集成与主题定制
  - 2026设计趋势(玻璃态、新拟态、3D交互、可变字体)
  - 高级微交互动画模式与状态设计
  - 顶级产品深度分析(Linear/Stripe/Vercel/Notion)
  - 组件库设计规范与文档体系

  适用场景:
  - 企业级Web/Mobile应用设计体系搭建
  - 设计系统的令牌化与组件规范化
  - 无障碍合规审计与改进
  - 团队设计规范文档编写

  差异化:专业版在免费版基础上扩展至完整企业级设计体系,新增设计令牌系统、
  Shadcn/ui集成、WCAG 2.2合规、2026趋势和顶级产品分析。完全兼容免费版
  设计原则,可无缝升级。

  触发关键词: 设计令牌, WCAG合规, Shadcn组件库, 设计系统, 无障碍审计, 2026设计趋势, 玻璃态, 微交互动画, 组件规范, 主题定制, ARIA标签, 焦点状态
tags:
- 设计
- UI
- UX
- 配色
- 字体
- 响应式
- 前端
- 企业级
- 无障碍
- 设计系统
- 组件库
tools:
- read
- exec
---

# UI/UX设计指南 - 专业版

## 概述

UI/UX设计指南专业版是一款面向企业设计团队和专业前端的完整设计体系参考。在免费版核心设计原则之上,扩展至WCAG 2.2无障碍合规、设计令牌系统、Shadcn/ui组件库深度集成、2026设计趋势、高级微交互动画,以及对Linear、Stripe、Vercel、Notion等顶级产品的深度设计分析。

专业版帮助企业建立可扩展、可维护、合规的设计系统,完全兼容免费版设计原则,可无缝升级。

## 核心能力

### 1. 设计令牌系统

专业版提供完整的语义化设计令牌体系,支持主题切换和跨平台一致性:

```css
/* 设计令牌 - 语义化命名 */
:root {
  /* 色彩令牌 */
  --color-brand-primary:    #2563eb;
  --color-brand-secondary:  #64748b;
  --color-brand-accent:     #22d3ee;

  /* 语义色彩 */
  --color-action-primary:   var(--color-brand-primary);
  --color-action-hover:     #1d4ed8;
  --color-action-disabled:  #93c5fd;

  --color-feedback-success: #10b981;
  --color-feedback-error:   #ef4444;
  --color-feedback-warning: #f59e0b;
  --color-feedback-info:    #3b82f6;

  /* 表面色彩 */
  --color-surface-base:     #ffffff;
  --color-surface-raised:   #f8fafc;
  --color-surface-overlay:  rgba(255, 255, 255, 0.8);

  /* 文字色彩 */
  --color-text-primary:     #0f172a;
  --color-text-secondary:   #475569;
  --color-text-disabled:    #94a3b8;
  --color-text-inverse:     #ffffff;

  /* 间距令牌 */
  --space-xs:  4px;
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  24px;
  --space-xl:  32px;
  --space-2xl: 48px;
  --space-3xl: 64px;

  /* 圆角令牌 */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-full: 9999px;

  /* 阴影令牌 */
  --shadow-sm:  0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md:  0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg:  0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl:  0 20px 25px rgba(0, 0, 0, 0.15);
}

/* 暗色主题令牌覆盖 */
[data-theme="dark"] {
  --color-surface-base:     #0f172a;
  --color-surface-raised:   #1e293b;
  --color-text-primary:     #f8fafc;
  --color-text-secondary:   #cbd5e1;
}
```

### 2. WCAG 2.2完整无障碍合规

| 合规项 | 标准要求 | 实现方法 |
|--------|----------|----------|
| 文字对比度 | 正常文字4.5:1,大文字3:1 | 使用WebAIM Contrast Checker验证 |
| UI组件对比度 | 3:1最低 | 边框、图标需达到3:1对比 |
| 键盘导航 | Tab顺序逻辑化 | tabindex合理设置,焦点可见 |
| 焦点状态 | 3:1对比度可见焦点环 | `focus:ring-2 focus:ring-blue-500` |
| ARIA标签 | 图标按钮需aria-label | `<button aria-label="关闭">` |
| 表单标签 | label与input关联 | `<label for="email">` |
| 屏幕阅读器 | 语义化HTML | 使用header/main/nav/section/footer |
| 减少动画 | 尊重prefers-reduced-motion | `@media (prefers-reduced-motion: reduce)` |

```css
/* 无障碍焦点状态 */
.focusable:focus-visible {
  outline: 2px solid var(--color-brand-primary);
  outline-offset: 2px;
}

/* 尊重减少动画偏好 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 3. Shadcn/ui + Tailwind深度集成

```bash
# Next.js项目初始化
npx create-next-app@latest my-project --typescript --tailwind --app
cd my-project

# Shadcn/ui初始化
npx shadcn@latest init
# 选择:Style(Default), Base color(Blue), CSS variables(Yes)

# 添加核心组件
npx shadcn@latest add button card dialog dropdown-menu
npx shadcn@latest add form input label select
npx shadcn@latest add table tabs toast tooltip
```

组件所有权模型:
- 组件代码生成到 `components/ui/` 目录
- 你完全拥有代码,可自由定制
- 不依赖运行时组件库,减少包体积

### 4. 2026设计趋势

| 趋势 | 特征 | 适用场景 | Tailwind实现 |
|------|------|----------|-------------|
| 玻璃态 | 半透明+模糊背景 | 导航栏、卡片 | `bg-white/80 backdrop-blur-md` |
| 新拟态 | 柔和阴影凹凸 | 按钮、开关 | 自定义box-shadow |
| 3D交互 | 深度感与视差 | Hero区、展示 | transform + perspective |
| 可变字体 | 动态字重调整 | 全站排版 | font-variation-settings |
| 大圆角 | 16-24px圆角 | 卡片、按钮 | rounded-2xl rounded-3xl |
| 渐变边框 | 彩色边框效果 | 卡片、按钮 | gradient + mask |

### 5. 高级微交互动画

```css
/* 状态转换动画 */
.button {
  /* 基础态 */
  background-color: var(--color-action-primary);
  transform: scale(1);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.button:hover {
  background-color: var(--color-action-hover);
  transform: scale(1.02);
  box-shadow: var(--shadow-md);
}

.button:active {
  transform: scale(0.98);
  box-shadow: var(--shadow-sm);
}

.button:disabled {
  background-color: var(--color-action-disabled);
  cursor: not-allowed;
  transform: none;
}

/* 加载状态 */
.button.loading {
  color: transparent;
  position: relative;
}
.button.loading::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### 6. 顶级产品深度分析

| 产品 | 设计亮点 | 可借鉴模式 |
|------|----------|-----------|
| Linear | 键盘优先UI、微妙动画 | 命令面板、快捷键提示、平滑过渡 |
| Stripe Dashboard | 数据可视化、完美间距 | 图表配色、数据密度控制、留白节奏 |
| Vercel | 极简、快速、现代渐变 | 渐变背景、单色强调、排版层次 |
| Notion | 直觉拖拽、清晰层次 | 块编辑器、悬浮工具栏、上下文菜单 |

## 使用场景

### 场景一:企业SaaS设计系统搭建

一家B2B SaaS公司需要建立完整的设计系统,支持多主题和团队协作。

```bash
# 步骤1:初始化项目
npx create-next-app@latest enterprise-app --typescript --tailwind --app
cd enterprise-app

# 步骤2:集成Shadcn/ui
npx shadcn@latest init
npx shadcn@latest add button card dialog dropdown-menu form input select table tabs toast

# 步骤3:配置设计令牌
# 编辑 globals.css 添加设计令牌变量
```

设计令牌配置(globals.css):

```css
@layer base {
  :root {
    /* 完整设计令牌体系 */
    --background: 0 0% 100%;
    --foreground: 222 47% 11%;
    --primary: 221 83% 53%;
    --primary-foreground: 0 0% 100%;
    --secondary: 215 16% 47%;
    --muted: 210 40% 96%;
    --accent: 189 94% 43%;
    --destructive: 0 84% 60%;
    --border: 214 32% 91%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222 47% 11%;
    --foreground: 210 40% 98%;
    --primary: 221 83% 53%;
    --muted: 217 33% 17%;
    --border: 217 33% 20%;
  }
}
```

### 场景二:无障碍合规审计

对现有产品进行WCAG 2.2合规审计并修复问题:

```html
<!-- 修复前:无障碍问题 -->
<button>×</button>  <!-- 无aria-label,屏幕阅读器无法理解 -->
<img src="logo.png">  <!-- 无alt文本 -->
<div class="link" onclick="...">点击</div>  <!-- 非语义化,键盘不可达 -->

<!-- 修复后:合规实现 -->
<button aria-label="关闭对话框" class="focus:ring-2 focus:ring-blue-500">
  <svg aria-hidden="true">...</svg>
</button>
<img src="logo.png" alt="公司Logo" />
<a href="/page" class="focus:ring-2 focus:ring-blue-500 cursor-pointer">点击</a>
```

### 场景三:高级组件设计模式

设计一个状态丰富的数据表格组件:

```tsx
// 企业级数据表格组件
function DataTable({ data, loading, error }) {
  // 加载状态:骨架屏
  if (loading) {
    return <TableSkeleton rows={5} cols={4} />;
  }

  // 错误状态:可操作的错误提示
  if (error) {
    return (
      <ErrorState
        message="数据加载失败"
        action="重试"
        onAction={refetch}
      />
    );
  }

  // 空状态:引导首次操作
  if (data.length === 0) {
    return (
      <EmptyState
        title="还没有数据"
        description="点击下方按钮创建第一条记录"
        action="新建记录"
        onAction={handleCreate}
      />
    );
  }

  // 正常状态:数据表格
  return <Table data={data} />;
}
```

## 快速开始

### 企业级项目初始化

```bash
# 创建Next.js + Tailwind + Shadcn/ui项目
npx create-next-app@latest my-app --typescript --tailwind --app --eslint
cd my-app

# 初始化Shadcn/ui
npx shadcn@latest init -d

# 添加企业级核心组件
npx shadcn@latest add button card dialog dropdown-menu \
  form input label select textarea table tabs toast \
  tooltip badge avatar separator skeleton

# 验证安装
npm run dev
```

### 设计系统文档结构

```text
design-system/
├── tokens/
│   ├── colors.md        # 色彩令牌定义
│   ├── typography.md    # 字体令牌定义
│   ├── spacing.md       # 间距令牌定义
│   └── shadows.md       # 阴影令牌定义
├── components/
│   ├── button.md        # 按钮规范
│   ├── card.md          # 卡片规范
│   └── form.md          # 表单规范
├── patterns/
│   ├── layouts.md       # 布局模式
│   └── interactions.md  # 交互模式
└── guidelines/
    ├── accessibility.md # 无障碍指南
    └── responsive.md    # 响应式指南
```

## 配置示例

### Tailwind CSS企业级配置

```javascript
// tailwind.config.ts
import type { Config } from 'tailwindcss';

const config: Config = {
  darkMode: ['class'],
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
};
export default config;
```

### 专业版与免费版完整对比

| 功能维度 | 免费版 | 专业版 |
|----------|--------|--------|
| 设计原则 | 核心原则 | 完整体系+2026趋势 |
| 配色系统 | 基础色阶(50-900) | 设计令牌+语义系统+主题切换 |
| 组件库 | Tailwind基础类 | Shadcn/ui完整集成+定制 |
| 无障碍 | 基础对比度检查 | WCAG 2.2完整合规审计 |
| 微交互 | 基础悬停/点击 | 高级动画+状态机设计 |
| 响应式 | 移动优先基础 | 全断点深度适配+容器查询 |
| 设计参考 | 基础建议 | 顶级产品深度分析 |
| 文档体系 | 基础 | 完整设计系统文档结构 |
| 暗色模式 | 基础dark:前缀 | 完整双主题令牌系统 |
| 适用对象 | 个人/小团队 | 企业/设计团队 |
| 兼容性 | - | 完全兼容免费版原则 |

## 最佳实践

### 1. 使用设计令牌而非硬编码值

```css
/* 错误:硬编码值 */
.card {
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* 正确:使用设计令牌 */
.card {
  background-color: var(--color-surface-base);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-lg);
  box-shadow: var(--shadow-md);
}
```

### 2. 组件状态完整性

每个交互组件应覆盖以下状态:

| 状态 | Tailwind类 | 说明 |
|------|-----------|------|
| 默认 | `base styles` | 基础外观 |
| 悬停 | `hover:` | 鼠标悬停反馈 |
| 聚焦 | `focus-visible:ring-2` | 键盘聚焦可见 |
| 激活 | `active:scale-95` | 点击按下反馈 |
| 禁用 | `disabled:opacity-50` | 不可用状态 |
| 加载 | `loading` 类 | 异步操作中 |

### 3. 无障碍设计检查清单

- [ ] 所有图片有alt文本
- [ ] 表单input有关联label
- [ ] 图标按钮有aria-label
- [ ] 颜色不是唯一信息指示器
- [ ] 键盘可完成所有操作
- [ ] 焦点状态可见(3:1对比度)
- [ ] 文字对比度达标(4.5:1)
- [ ] 尊重prefers-reduced-motion
- [ ] 语义化HTML结构(header/main/nav/footer)
- [ ] ARIA roles正确使用

### 4. 响应式设计深度适配

```css
/* 容器查询 - 组件级响应式 */
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card-layout {
    flex-direction: row;
  }
}

@container (max-width: 399px) {
  .card-layout {
    flex-direction: column;
  }
}
```

## 常见问题

### Q1: 专业版是否兼容免费版的设计原则?

完全兼容。专业版在免费版核心原则之上扩展,所有免费版的设计规则在专业版中同样适用。专业版新增了设计令牌、Shadcn/ui集成、WCAG合规等高级功能。

### Q2: Shadcn/ui与普通Tailwind组件有何区别?

Shadcn/ui将组件代码直接生成到你的项目中,你完全拥有代码所有权,可自由定制。不依赖运行时组件库,减少包体积,同时保持一致性。普通Tailwind组件需要手动编写所有样式。

### Q3: 设计令牌如何支持多主题?

通过CSS变量定义令牌,在 `[data-theme="dark"]` 或 `.dark` 选择器中覆盖变量值。Tailwind CSS通过 `hsl(var(--token))` 引用令牌,实现主题切换时自动更新所有组件样式。

### Q4: WCAG 2.2合规需要哪些工具?

推荐使用:
- WebAIM Contrast Checker - 对比度验证
- axe DevTools - 浏览器无障碍审计
- Lighthouse - Chrome内置无障碍评分
- WAVE - Web无障碍评估工具

### Q5: 如何在团队中推广设计系统?

1. 建立设计令牌文件,纳入版本控制
2. 使用Storybook展示组件库
3. 编写设计系统文档(使用上述文档结构)
4. 定期进行设计评审和合规审计
5. 将设计令牌同步至设计工具(Figma Variables)

### Q6: 2026设计趋势中哪些最值得采用?

推荐优先采用:大圆角(提升亲和力)、玻璃态(现代感导航栏)、可变字体(性能优化)。新拟态和3D交互视产品调性选择性采用,避免过度使用导致性能问题。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 18及以上(推荐20 LTS)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官网下载或nvm安装 |
| Tailwind CSS | 前端框架 | 必需 | npm install -D tailwindcss |
| Shadcn/ui | 组件库 | 必需 | npx shadcn@latest init |
| tailwindcss-animate | 插件 | 推荐 | npm install -D tailwindcss-animate |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Figma | 设计工具 | 推荐 | 用于设计令牌同步 |

安装命令:

```bash
# 创建企业级项目
npx create-next-app@latest my-app --typescript --tailwind --app --eslint
cd my-app

# 安装Shadcn/ui和动画插件
npx shadcn@latest init -d
npm install -D tailwindcss-animate
```

### API Key 配置

本Skill基于Markdown设计指南,无需额外API Key。设计建议的生成由Agent内置LLM驱动。Shadcn/ui组件安装通过npx本地执行,不依赖外部API。Figma设计令牌同步如需使用,需配置Figma API Token。

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。项目初始化、Shadcn/ui组件安装和Tailwind配置需要exec工具执行npm/npx命令。无障碍审计需配合浏览器开发工具使用。
