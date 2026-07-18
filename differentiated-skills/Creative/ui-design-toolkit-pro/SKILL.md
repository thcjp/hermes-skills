---
slug: ui-design-toolkit-pro
name: ui-design-toolkit-pro
version: "1.0.0"
displayName: UI设计工具包专业版
summary: 企业级UI设计工具包,支持设计系统、设计令牌、可访问性与组件库,适配团队协作与大型项目。
license: MIT
edition: pro
description: |-
  面向团队与企业用户的 UI 设计工具包(专业版)。

  核心能力:
  - 涵盖免费版全部能力(视觉层次、排版、色彩、间距、状态)
  - 设计系统(Design System)构建与维护
  - 设计令牌(Design Tokens)管理
  - 可访问性(a11y)深度规范与自动化检测
  - 组件库抽象与复用
  - 多主题与品牌切换
  - 动效系统(Motion Design)
  - 国际化(i18n)设计考虑
  - Figma 协作规范
  - 设计文档与 Storybook 集成
  - 设计评审 Checklist

  适用场景:
  - 企业级产品设计系统建设
  - 多产品/多品牌设计统一
  - 团队协作与设计规范
  - 可访问性合规(WCAG/ADA)
  - 组件库开发与维护

  差异化:
  - 专业版支持完整设计系统建设
  - 设计令牌实现设计与代码统一
  - 可访问性覆盖规范与自动化检测
  - 组件库抽象提升团队复用效率
  - 与免费版原则兼容,可平滑升级

  触发关键词: ui, design, system, tokens, a11y, accessibility, component library, theme, motion, i18n, figma, storybook, 设计系统, 设计令牌, 可访问性, 组件库, pro
tags:
- 创意设计
- UI设计
- 企业级
- 设计系统
- 可访问性
- 组件库
tools:
- read
- exec
---

# UI 设计工具包 - 专业版

## 概述

UI 设计工具包(专业版)在免费版(`ui-design-toolkit-free`)核心设计原则之上,新增设计系统构建、设计令牌管理、可访问性深度规范、组件库抽象与多主题支持等企业级能力。适合大型项目与团队协作场景。

专业版与免费版设计原则完全兼容,已使用免费版的项目无需调整,升级后可直接启用高级特性。

## 核心能力

### 免费版 vs 专业版对比

| 能力 | 免费版 | 专业版 | 增量价值 |
|:-----|:-------|:-------|:---------|
| 视觉层次 | 支持 | 支持 | - |
| 排版规范 | 支持 | 支持 | - |
| 色彩使用 | 支持 | 支持 | - |
| 间距系统 | 支持 | 支持 | - |
| 组件状态 | 支持 | 支持 | - |
| 响应式 | 基础 | 完整体系 | 全端适配 |
| 暗黑模式 | 基础 | 多主题 | 多品牌 |
| 动效设计 | 基础 | 动效系统 | 体验提升 |
| 设计系统 | 不支持 | 完整建设 | 一致性 |
| 设计令牌 | 不支持 | Token 管理 | 设计代码统一 |
| 可访问性 | 基础 | 深度规范 + 检测 | 合规 |
| 组件库 | 不支持 | 抽象与复用 | 团队效率 |
| 国际化 | 不支持 | i18n 设计 | 全球化 |
| Figma 协作 | 不支持 | 规范与同步 | 设计开发协同 |
| Storybook | 不支持 | 集成与文档 | 组件文档 |
| 设计评审 | 不支持 | Checklist | 质量保证 |

## 使用场景

### 场景一:设计系统构建

构建完整的企业设计系统。

```javascript
// design-tokens.js - 设计令牌定义
export const tokens = {
  // 颜色令牌
  color: {
    // 品牌色
    brand: {
      50: '#eff6ff',
      100: '#dbeafe',
      200: '#bfdbfe',
      300: '#93c5fd',
      400: '#60a5fa',
      500: '#3b82f6',  // 主色
      600: '#2563eb',
      700: '#1d4ed8',
      800: '#1e40af',
      900: '#1e3a8a',
    },
    // 语义色
    semantic: {
      success: { DEFAULT: '#10b981', light: '#d1fae5', dark: '#065f46' },
      warning: { DEFAULT: '#f59e0b', light: '#fef3c7', dark: '#92400e' },
      error:   { DEFAULT: '#ef4444', light: '#fee2e2', dark: '#991b1b' },
      info:    { DEFAULT: '#3b82f6', light: '#dbeafe', dark: '#1e40af' },
    },
    // 中性色
    gray: {
      50: '#f9fafb', 100: '#f3f4f6', 200: '#e5e7eb',
      300: '#d1d5db', 400: '#9ca3af', 500: '#6b7280',
      600: '#4b5563', 700: '#374151', 800: '#1f2937', 900: '#111827',
    },
  },

  // 排版令牌
  typography: {
    fontFamily: {
      sans: ['Inter', 'PingFang SC', 'Microsoft YaHei', 'sans-serif'],
      mono: ['JetBrains Mono', 'Consolas', 'monospace'],
    },
    fontSize: {
      xs:   '0.75rem',  // 12px
      sm:   '0.875rem', // 14px
      base: '1rem',     // 16px
      lg:   '1.125rem', // 18px
      xl:   '1.25rem',  // 20px
      '2xl': '1.5rem',  // 24px
      '3xl': '1.875rem',// 30px
      '4xl': '2.25rem', // 36px
    },
    fontWeight: {
      regular: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
    lineHeight: {
      tight: 1.25,
      normal: 1.5,
      relaxed: 1.75,
    },
  },

  // 间距令牌(4px 网格)
  spacing: {
    0: '0',
    1: '0.25rem',  // 4px
    2: '0.5rem',   // 8px
    3: '0.75rem',  // 12px
    4: '1rem',     // 16px
    5: '1.25rem',  // 20px
    6: '1.5rem',   // 24px
    8: '2rem',     // 32px
    10: '2.5rem',  // 40px
    12: '3rem',    // 48px
    16: '4rem',    // 64px
  },

  // 圆角令牌
  borderRadius: {
    none: '0',
    sm: '0.125rem',   // 2px
    DEFAULT: '0.25rem', // 4px
    md: '0.375rem',   // 6px
    lg: '0.5rem',     // 8px
    xl: '0.75rem',    // 12px
    full: '9999px',
  },

  // 阴影令牌
  boxShadow: {
    sm: '0 1px 2px rgba(0,0,0,0.05)',
    DEFAULT: '0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)',
    md: '0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06)',
    lg: '0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)',
    xl: '0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04)',
  },

  // 动效令牌
  animation: {
    duration: { fast: '150ms', normal: '300ms', slow: '500ms' },
    easing: {
      easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
      easeOut: 'cubic-bezier(0.0, 0, 0.2, 1)',
      easeIn: 'cubic-bezier(0.4, 0, 1, 1)',
      spring: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
    },
  },
}
```

### 场景二:可访问性深度规范

实现 WCAG 2.1 AA 级合规。

```javascript
// a11y-checklist.js - 可访问性检查清单
export const a11yChecklist = {
  // 感知(Perceivable)
  perceptible: {
    '1.1.1 非文本内容': '所有图片有 alt 文本(装饰性用 alt="")',
    '1.3.1 信息与关系': '使用语义化 HTML(header/nav/main/article)',
    '1.4.3 对比度(最低)': '正文文字对比度 >= 4.5:1',
    '1.4.3 对比度(大文字)': '18px+ 文字对比度 >= 3:1',
    '1.4.4 文字缩放': '支持 200% 缩放不丢失功能',
    '1.4.11 非文字对比度': 'UI 组件对比度 >= 3:1',
  },

  // 可操作(Operable)
  operable: {
    '2.1.1 键盘可访问': '所有功能可通过键盘操作',
    '2.1.2 无键盘陷阱': '焦点不会被组件困住',
    '2.4.3 焦点顺序': 'DOM 顺序与视觉顺序一致',
    '2.4.7 焦点可见': '聚焦状态清晰可见',
    '2.5.5 目标尺寸': '触摸目标 >= 44x44px',
  },

  // 可理解(Understandable)
  understandable: {
    '3.2.1 可预测': '组件行为一致',
    '3.2.2 输入标识': '表单字段有清晰标签',
    '3.3.1 错误识别': '错误信息清晰描述',
    '3.3.2 标签或指令': '提供输入指导',
  },

  // 健壮(Robust)
  robust: {
    '4.1.2 名称、角色、值': 'ARIA 属性正确使用',
    '4.1.3 状态消息': '使用 role="status" 或 aria-live',
  },
}

// 自动化检测工具集成
// 推荐工具:
// - axe-core: 自动化可访问性检测
// - Lighthouse: Chrome 内置审计
// - jest-axe: Jest 集成测试
```

```python
# 使用 axe-core 进行可访问性检测的示例配置
"""
# 安装
npm install --save-dev axe-core jest-axe

# jest.config.js
module.exports = {
  setupFilesAfterEnv: ['jest-axe/extend-expect'],
}

# 测试示例
import { render } from '@testing-library/react'
import { axe } from 'jest-axe'
import { Button } from './Button'

test('Button 满足可访问性标准', async () => {
  const { container } = render(<Button>点击</Button>)
  const results = await axe(container)
  expect(results).toHaveNoViolations()
})
"""
```

### 场景三:组件库抽象

构建可复用的组件库。

```typescript
// components/ui/Button.tsx
import { clsx } from 'clsx'
import { forwardRef } from 'react'

type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger'
type ButtonSize = 'sm' | 'md' | 'lg'

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant
  size?: ButtonSize
  isLoading?: boolean
  leftIcon?: React.ReactNode
  rightIcon?: React.ReactNode
}

const variantStyles: Record<ButtonVariant, string> = {
  primary: 'bg-brand-500 text-white hover:bg-brand-600 active:bg-brand-700',
  secondary: 'bg-transparent border border-gray-300 text-gray-700 hover:bg-gray-50',
  ghost: 'bg-transparent text-gray-700 hover:bg-gray-100',
  danger: 'bg-red-500 text-white hover:bg-red-600',
}

const sizeStyles: Record<ButtonSize, string> = {
  sm: 'px-3 py-1.5 text-sm',
  md: 'px-4 py-2 text-base',
  lg: 'px-6 py-3 text-lg',
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', isLoading, leftIcon, rightIcon,
     children, className, disabled, ...props }, ref) => {
    return (
      <button
        ref={ref}
        disabled={disabled || isLoading}
        className={clsx(
          'inline-flex items-center justify-center gap-2',
          'rounded-md font-medium transition-colors',
          'focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2',
          'disabled:opacity-50 disabled:cursor-not-allowed',
          variantStyles[variant],
          sizeStyles[size],
          className
        )}
        {...props}
      >
        {isLoading && <Spinner className="w-4 h-4" />}
        {!isLoading && leftIcon}
        {children}
        {!isLoading && rightIcon}
      </button>
    )
  }
)

Button.displayName = 'Button'
```

### 场景四:多主题切换

支持多品牌动态切换。

```css
/* themes/brand-a.css */
:root[data-theme="brand-a"] {
  --color-brand-50: #eff6ff;
  --color-brand-500: #3b82f6;
  --color-brand-600: #2563eb;
  --color-brand-700: #1d4ed8;
}

/* themes/brand-b.css */
:root[data-theme="brand-b"] {
  --color-brand-50: #f0fdf4;
  --color-brand-500: #22c55e;
  --color-brand-600: #16a34a;
  --color-brand-700: #15803d;
}

/* themes/brand-c.css */
:root[data-theme="brand-c"] {
  --color-brand-50: #faf5ff;
  --color-brand-500: #a855f7;
  --color-brand-600: #9333ea;
  --color-brand-700: #7e22ce;
}
```

```javascript
// 主题切换
function setBrand(brand) {
  document.documentElement.setAttribute('data-theme', `brand-${brand}`)
  localStorage.setItem('brand', brand)
}

// 初始化
const savedBrand = localStorage.getItem('brand') || 'a'
setBrand(savedBrand)
```

## 快速开始

### 1. 初始化设计系统

```bash
# 创建设计系统项目
mkdir my-design-system && cd my-design-system
npm init -y

# 安装依赖
npm install clsx
npm install -D tailwindcss storybook @storybook/react
```

### 2. 定义设计令牌

```bash
# 复制令牌模板
cp templates/design-tokens.js ./src/
cp templates/tailwind.config.js ./
```

### 3. 搭建组件库

```bash
# 初始化 Storybook
npx storybook init

# 创建组件目录
mkdir -p src/components/ui
```

## 配置示例

### Storybook 集成

```yaml
# .storybook/main.yaml
version: 2
stories:
  - glob: '**/*.stories.@(ts|tsx|js|jsx)'
    dir: ../src/components
addons:
  - '@storybook/addon-essentials'
  - '@storybook/addon-a11y'        # 可访问性检测
  - '@storybook/addon-designs'     # Figma 集成
```

### 设计评审 Checklist

```markdown
# 设计评审 Checklist

## 一致性
- [ ] 使用设计令牌,无硬编码值
- [ ] 间距遵循 4px 网格
- [ ] 色彩使用语义化命名
- [ ] 字体使用预定义字号

## 可访问性
- [ ] 文字对比度 >= 4.5:1
- [ ] 触摸目标 >= 44x44px
- [ ] 所有图片有 alt 文本
- [ ] 焦点状态清晰可见
- [ ] 支持键盘导航

## 响应式
- [ ] 移动端优先设计
- [ ] 断点选择合理
- [ ] 触摸与鼠标交互区分

## 状态完整性
- [ ] 默认/悬停/聚焦/激活/禁用
- [ ] 加载状态设计
- [ ] 错误状态设计
- [ ] 空状态设计

## 国际化
- [ ] 文本不硬编码
- [ ] 支持 RTL 布局
- [ ] 长文本不破坏布局
- [ ] 日期/时间本地化
```

## 最佳实践

### 1. 设计系统原则

- **单一数据源**:所有令牌定义在统一文件
- **语义命名**:用 `color-error` 而非 `color-red`
- **层级清晰**:令牌 > 样式 > 组件 > 模式
- **版本管理**:设计系统纳入 Git,版本化发布

### 2. 设计令牌管理

```javascript
// 令牌转换工具:统一导出为各平台格式
// Style Dictionary 配置
module.exports = {
  source: ['tokens/**/*.json'],
  platforms: {
    web: { transformGroup: 'css', buildPath: 'build/web/', files: [{
      destination: 'tokens.css', format: 'css/variables'
    }]},
    ios: { transformGroup: 'ios-swift', buildPath: 'build/ios/', files: [{
      destination: 'Tokens.swift', format: 'ios-swift/class.swift'
    }]},
    android: { transformGroup: 'android', buildPath: 'build/android/', files: [{
      destination: 'colors.xml', format: 'android/colors'
    }]},
  },
}
```

### 3. 可访问性自动化

```yaml
# .github/workflows/a11y.yml
name: Accessibility Check
on: [pull_request]
jobs:
  a11y:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - name: Run axe-core
        run: npm run test:a11y
      - name: Lighthouse audit
        run: npx lighthouse-ci --accessibility=90
```

### 4. Figma 协作规范

- 设计师在 Figma 中使用与代码一致的令牌命名
- 使用 Figma Variables 同步设计令牌
- 组件命名与代码组件一一对应
- 变更通过 PR 流程评审

### 5. 国际化设计考虑

- 文本长度预留 30% 扩展空间(德文较长)
- 支持 RTL(从右到左)布局
- 日期/时间/数字本地化
- 货币与单位适配
- 颜色文化差异考量

## 常见问题

### Q1: 设计系统如何保证一致性?

通过将所有设计令牌集中在统一文件,团队成员只能使用预定义的令牌。配合设计 lint 工具(如 Stylelint)检测硬编码值。

### Q2: 设计令牌如何同步到代码?

使用 Style Dictionary 等工具,从单一数据源自动生成各平台格式(CSS 变量、iOS Swift、Android XML)。

### Q3: 可访问性合规需要达到什么级别?

建议至少达到 WCAG 2.1 AA 级。部分场景(政府、医疗)可能要求 AAA 级。使用 axe-core 自动化检测 + 人工评审。

### Q4: 组件库如何版本管理?

- 遵循语义化版本(SemVer)
- 破坏性变更需迁移指南
- 使用 Changesets 管理版本
- 通过 npm/内部 registry 分发

### Q5: 专业版与免费版的迁移?

零迁移成本。专业版是免费版的超集,设计原则完全兼容。升级后原有组件继续可用,新特性按需启用。

### Q6: 如何与 Figma 协作?

使用 Figma Variables 同步设计令牌,组件命名与代码一一对应,变更通过 PR 评审。专业版提供详细的协作规范。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18 及以上

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| tailwindcss | npm 库 | 推荐 | `npm install -D tailwindcss` |
| clsx | npm 库 | 推荐(组件) | `npm install clsx` |
| storybook | npm 库 | 可选(文档) | `npx storybook init` |
| axe-core | npm 库 | 可选(a11y) | `npm install -D axe-core` |
| style-dictionary | npm 库 | 可选(令牌) | `npm install -D style-dictionary` |
| Node.js 18+ | 运行时 | 必需 | `nodejs.org` 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本 Skill **无需任何 API Key**
- 设计系统为本地构建,不依赖云服务
- Figma 集成可能需要 Figma API Token(可选)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。专业版支持设计系统建设、设计令牌管理与可访问性规范,适合企业级产品设计与团队协作。
