---
slug: ui-ux-design-paid
name: ui-ux-design-paid
version: "1.0.0"
displayName: UI/UX设计指南专业版
summary: 企业级UI/UX设计体系,含WCAG 2.2合规、设计令牌、Shadcn/ui集成、2026趋势与高级产品深度分析
license: Proprietary
edition: pro
description: |-
  面向企业设计团队和专业前端的完整UI/UX设计体系,涵盖WCAG 2。2无障碍合规、
  设计令牌系统、Shadcn/ui组件库深度集成、2026设计趋势、微交互动画模式、
  以及对高级产品的深度设计分析。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。
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
  - - read
- exec
# UI/UX设计指南 - 专业版
## 概述
---
# UI/UX设计指南专业版

## 核心能力

### 1. 设计令牌系统
专业版提供完整的语义化设计令牌体系,支持主题切换和跨平台一致性:

> 详细代码示例已移至 `references/detail.md`

**处理**: 按照skill规范执行设计令牌系统操作,遵循单一意图原则。
**输出**: 返回设计令牌系统的执行结果,包含操作状态和输出数据。

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

**处理**: 按照skill规范执行WCAG 2.2完整无障碍合规操作,遵循单一意图原则。
**输出**: 返回WCAG 2.2完整无障碍合规的执行结果,包含操作状态和输出数据。

### 3. Shadcn/ui + Tailwind深度集成
```bash
npx create-next-app@latest my-project --typescript --tailwind --app
cd my-project

npx shadcn@latest init
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

**输入**: 用户提供2026设计趋势所需的指令和必要参数。
**处理**: 按照skill规范执行2026设计趋势操作,遵循单一意图原则。
**输出**: 返回2026设计趋势的执行结果,包含操作状态和输出数据。

### 5. 高级微交互动画
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供高级微交互动画所需的指令和必要参数。
**处理**: 按照skill规范执行高级微交互动画操作,遵循单一意图原则。
**输出**: 返回高级微交互动画的执行结果,包含操作状态和输出数据。

### 6. 高级产品深度分析
| 产品 | 设计亮点 | 可借鉴模式 |
|------|----------|-----------|
| Linear | 键盘优先UI、微妙动画 | 命令面板、快捷键提示、平滑过渡 |
| Stripe Dashboard | 数据可视化、完善间距 | 图表配色、数据密度控制、留白节奏 |
| Vercel | 极简、快速、现代渐变 | 渐变背景、单色强调、排版层次 |
| Notion | 直觉拖拽、清晰层次 | 块编辑器、悬浮工具栏、上下文菜单 |

**输入**: 用户提供高级产品深度分析所需的指令和必要参数。
**处理**: 按照skill规范执行高级产品深度分析操作,遵循单一意图原则。
**输出**: 返回高级产品深度分析的执行结果,包含操作状态和输出数据。
## 适用场景

### 场景一:企业SaaS设计系统搭建
一家B2B SaaS公司需要建立完整的设计系统,支持多主题和团队协作。

```bash
npx create-next-app@latest enterprise-app --typescript --tailwind --app
cd enterprise-app

npx shadcn@latest init
npx shadcn@latest add button card dialog dropdown-menu form input select table tabs toast

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
        description="点击下方按钮创建领先条记录"
        action="新建记录"
        onAction={handleCreate}
      />
    );
  }

  // 正常状态:数据表格
  return <Table data={data} />;
}
```

## 使用流程

### 企业级项目初始化
```bash
npx create-next-app@latest my-app --typescript --tailwind --app --eslint
cd my-app

npx shadcn@latest init -d

npx shadcn@latest add button card dialog dropdown-menu \
  form input label select textarea table tabs toast \
  tooltip badge avatar separator skeleton

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

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

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
npx create-next-app@latest my-app --typescript --tailwind --app --eslint
cd my-app

npx shadcn@latest init -d
npm install -D tailwindcss-animate
```

### API Key 配置
本Skill基于Markdown设计指南,无需额外API Key。设计建议的生成由Agent内置LLM驱动。Shadcn/ui组件安装通过npx本地执行,不依赖外部API。Figma设计令牌同步如需使用,需配置Figma API Token。

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。项目初始化、Shadcn/ui组件安装和Tailwind配置需要exec工具执行npm/npx命令。无障碍审计需配合浏览器开发工具使用。

## 案例展示

### Tailwind CSS企业级配置

> 详细代码示例已移至 `references/detail.md`

### 专业版与免费版完整对比
| 功能维度 | 免费版 | 专业版 |
|----------|--------|--------|
| 设计原则 | 核心原则 | 完整体系+2026趋势 |
| 配色系统 | 基础色阶(50-900) | 设计令牌+语义系统+主题切换 |
| 组件库 | Tailwind基础类 | Shadcn/ui完整集成+定制 |
| 无障碍 | 基础对比度检查 | WCAG 2.2完整合规审计 |
| 微交互 | 基础悬停/点击 | 高级动画+状态机设计 |
| 响应式 | 移动优先基础 | 全断点深度适配+容器查询 |
| 设计参考 | 基础建议 | 高级产品深度分析 |
| 文档体系 | 基础 | 完整设计系统文档结构 |
| 暗色模式 | 基础dark:前缀 | 完整双主题令牌系统 |
| 适用对象 | 个人/小团队 | 企业/设计团队 |
| 兼容性 | - | 完全兼容免费版原则 |

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
