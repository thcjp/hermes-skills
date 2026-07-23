---
slug: shadcn-ui
name: shadcn-ui
version: "1.0.0"
displayName: Shadcn Ui
summary: "使用shadcn/ui组件、Tailwind CSS布局、react-hook-form构建UI,加速前端开发"
  patterns with react-ho...
license: MIT
description: |-
  Use when building UI with shadcn/ui components, Tailwind CSS layouts,
  form patterns with react-ho。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
# Shadcn Ui
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

Comprehensive guide for building production UIs with shadcn/ui, Tailwind CSS, react-hook-form, and zod.

## Core Concepts
shadcn/ui is **not** a component library — it's a collection of copy-paste components built on Radix UI primitives. You own the code. Components are added to your project, not installed as dependencies.

## Installation
```bash
npx shadcn@latest init

npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
npx shadcn@latest add form
npx shadcn@latest add input
npx shadcn@latest add select
npx shadcn@latest add table
npx shadcn@latest add toast
npx shadcn@latest add dropdown-menu
npx shadcn@latest add sheet
npx shadcn@latest add tabs
npx shadcn@latest add sidebar

npx shadcn@latest add button card input label textarea select checkbox
```

## Component Categories & When to Use
### Layout & Navigation
| Component | Use When |
| --- | --- |
| `sidebar` | App-level navigation with collapsible sections |
| `navigation-menu` | Top-level site navigation with dropdowns |
| `breadcrumb` | Showing page hierarchy/location |
| `tabs` | Switching between related views in same context |
| `separator` | Visual divider between content sections |
| `sheet` | Slide-out panel (mobile nav, filters, detail views) |
| `resizable` | Adjustable panel layouts |

### Forms & Input
| Component | Use When |
| --- | --- |
| `form` | Any form with validation (wraps react-hook-form) |
| `input` | Text, email, password, number inputs |
| `textarea` | Multi-line text input |
| `select` | Choosing from a list (native-like) |
| `combobox` | Searchable select (uses `command` + `popover`) |
| `checkbox` | Boolean or multi-select toggles |
| `radio-group` | Single selection from small set |
| `switch` | On/off toggle (settings, preferences) |
| `slider` | Numeric range selection |
| `date-picker` | Date selection (uses `calendar` + `popover`) |
| `toggle` | Pressed/unpressed state (toolbar buttons) |

### Feedback & Overlay
| Component | Use When |
| --- | --- |
| `dialog` | Modal confirmation, forms, or detail views |
| `alert-dialog` | Destructive action confirmation ("Are you sure?") |
| `sheet` | Side panel for forms, filters, mobile nav |
| `toast` | Brief non-blocking notifications (via `sonner`) |
| `alert` | Inline status messages (info, warning, error) |
| `tooltip` | Hover hints for icons/buttons |
| `popover` | Rich content on click (color pickers, date pickers) |
| `hover-card` | Preview content on hover (user profiles, links) |
| `skeleton` | Loading placeholders |
| `progress` | Task completion indicators |

### Data Display
| Component | Use When |
| --- | --- |
| `table` | Tabular data display |
| `data-table` | Tables with sorting, filtering, pagination (uses `@tanstack/react-table`) |
| `card` | Content containers with header, body, footer |
| `badge` | Status labels, tags, counts |
| `avatar` | User profile images |
| `accordion` | Collapsible FAQ or settings sections |
| `carousel` | Image/content slideshows |
| `scroll-area` | Custom scrollable containers |

### Actions
| Component | Use When |
| --- | --- |
| `button` | Primary actions, form submissions |
| `dropdown-menu` | Context menus, action menus |
| `context-menu` | Right-click menus |
| `menubar` | Application menu bars |
| `command` | Command palette / search (⌘K) |

## Form Patterns (react-hook-form + zod)
### 示例
```bash
npx shadcn@latest add form input select textarea checkbox button
```

> 详细代码示例已移至 `references/detail.md`

### Form with Server Action
```tsx
'use client'

import { useFormState } from 'react-dom'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'

export function ContactForm() {
  const form = useForm<FormValues>({
    resolver: zodResolver(schema),
  })

  async function onSubmit(values: FormValues) {
    const formData = new FormData()
    Object.entries(values).forEach(([key, value]) => formData.append(key, String(value)))
    await submitContact(formData)
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
        {/* fields */}
      </form>
    </Form>
  )
}
```

## Theming & Dark Mode
### Setup with next-themes
```bash
npm install next-themes
npx shadcn@latest add dropdown-menu
```

```tsx
// app/providers.tsx
'use client'
import { ThemeProvider } from 'next-themes'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem disableTransitionOnChange>
      {children}
    </ThemeProvider>
  )
}
```

> 详细代码示例已移至 `references/detail.md`

### Custom Colors in `globals.css`
```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 11.2%;
    /* ... etc */
  }
}
```

## Common Layouts
### App Shell with Sidebar
```tsx
import { SidebarProvider, SidebarTrigger } from '@/components/ui/sidebar'
import { AppSidebar } from '@/components/app-sidebar'

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main className="flex-1">
        <header className="flex h-14 items-center gap-4 border-b px-6">
          <SidebarTrigger />
          <h1 className="text-lg font-semibold">Dashboard</h1>
        </header>
        <div className="p-6">{children}</div>
      </main>
    </SidebarProvider>
  )
}
```

### Responsive Header with Mobile Nav

> 详细代码示例已移至 `references/detail.md`

### Card Grid
```tsx
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

export function StatsGrid({ stats }: { stats: Stat[] }) {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      {stats.map((stat) => (
        <Card key={stat.label}>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">{stat.label}</CardTitle>
            <stat.icon className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stat.value}</div>
            <p className="text-xs text-muted-foreground">{stat.description}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
```

## Tailwind CSS Patterns
### Common Utility Patterns
```tsx
// Centering
<div className="flex items-center justify-center min-h-screen">

// Container with max-width
<div className="container mx-auto px-4">

// Responsive grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

// Sticky header
<header className="sticky top-0 z-50 border-b bg-background/95 backdrop-blur">

// Truncated text
<p className="truncate">Very long text...</p>

// Line clamp
<p className="line-clamp-3">Multi-line truncation...</p>

// Aspect ratio
<div className="aspect-video rounded-lg overflow-hidden">

// Animations
<div className="animate-pulse">    {/* Loading skeleton */}
<div className="animate-spin">     {/* Spinner */}
<div className="transition-all duration-200 hover:scale-105">
```

### Button Variants
```tsx
<Button>Default</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="outline">Outline</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="link">Link</Button>
<Button variant="destructive">Delete</Button>
<Button size="sm">Small</Button>
<Button size="lg">Large</Button>
<Button size="icon"><Plus className="h-4 w-4" /></Button>
<Button disabled>Disabled</Button>
<Button asChild><Link href="/page">As Link</Link></Button>
```

## Toast Notifications
```bash
npx shadcn@latest add sonner
```

```tsx
// app/layout.tsx
import { Toaster } from '@/components/ui/sonner'

export default function RootLayout({ children }) {
  return (
    <html><body>{children}<Toaster /></body></html>
  )
}

// Usage anywhere
import { toast } from 'sonner'

toast.success('User created')
toast.error('Something went wrong')
toast.info('New update available')
toast.warning('This action cannot be undone')
toast.promise(asyncAction(), {
  loading: 'Creating...',
  success: 'Created!',
  error: 'Failed to create',
})
```

## Command Palette (⌘K)

> 详细代码示例已移至 `references/detail.md`

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
- Use when building UI with shadcn/ui components, Tailwind CSS layouts,
  form patterns with react-ho
- 触发关键词: building, shadcn, components

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

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Shadcn Ui？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Shadcn Ui有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
