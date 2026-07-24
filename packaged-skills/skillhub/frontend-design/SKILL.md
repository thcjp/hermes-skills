---
slug: "frontend-design"
name: "frontend-design"
version: 1.1.1
displayName: "Frontend Design"
summary: "打造独特生产级前端界面,高设计质量,告别AI通用感。Create distinctive, production-grade frontend interfaces with high de"
license: "Proprietary"
description: |-
  Create distinctive, production-grade frontend interfaces with high design
  quality。Use this skill。
tags:
  - Other
  - 设计
  - UI/UX
  - 创意
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# Frontend Design

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

- 生成生产级前端界面代码，涵盖 React/Vue/Svelte 组件、HTML+CSS+JS 单文件应用
- 摆脱 AI 通用美学，打造具有品牌辨识度的独特视觉设计
- 响应式布局设计，覆盖移动端/平板/桌面端/超宽屏全断点适配
- 微交互动画与过渡效果设计，运用 CSS Animation、Framer Motion、GSAP
- 设计系统（Design System）搭建：Token 体系、组件库、设计规范文档
- 无障碍设计（a11y）集成：WCAG 2.1 AA 合规、ARIA 语义、键盘导航
- 性能优化：CSS 架构选择、Bundle 分析、关键渲染路径、图片优化策略

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 界面构建 | 设计需求与组件描述 | 生产级前端界面代码 |
| 设计差异化 | 风格定位与视觉参考 | 摆脱AI通用感的前端实现 |
| 落地页制作 | 产品信息与转化目标 | 高转化率着陆页代码 |
| 组件库开发 | 设计规范与组件需求 | 可复用组件库代码与文档 |
| 设计系统 | 品牌色/字体/间距规范 | Design Token 与主题配置 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

### 流程详解：从概念到生产级界面

**步骤 1：明确设计目标**

在生成界面前，需明确以下维度：

| 维度 | 选项 | 影响 |
|:-----|:-----|:-----|
| 技术栈 | React / Vue / Svelte / 原生 HTML | 组件写法与状态管理方式 |
| 风格定位 | 极简 / 拟物 / 玻璃态 / 新拟态 / Brutalism | 视觉语言与色彩方案 |
| 目标用户 | 消费者 / 企业 / 开发者 / 儿童 | 信息密度与交互复杂度 |
| 品牌调性 | 专业 / 活泼 / 优雅 / 科技 | 字体选择与色彩搭配 |
| 响应式策略 | 移动优先 / 桌面优先 | 断点设置与布局方向 |

**步骤 2：设计 Token 体系**

```css
:root {
  /* 色彩 Token */
  --color-primary: #6366f1;
  --color-primary-hover: #4f46e5;
  --color-bg: #0f0f23;
  --color-surface: #1a1a2e;
  --color-text: #e2e8f0;
  --color-text-muted: #94a3b8;
  --color-border: rgba(255, 255, 255, 0.08);
  --color-accent: #f59e0b;

  /* 间距 Token（4px 基准） */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-12: 3rem;    /* 48px */

  /* 圆角 Token */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  /* 阴影 Token */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.4);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.3);
  --shadow-glow: 0 0 24px rgba(99, 102, 241, 0.15);
}
```

**步骤 3：组件实现**

## 设计差异化策略

### 避免通用 AI 美学的关键手法

AI 生成的前端界面常有以下通病，需刻意避免：

| 通用 AI 特征 | 差异化手法 |
|:-------------|:-----------|
| 大量圆角卡片堆叠 | 混合使用直角与圆角，引入不规则形状 |
| 紫蓝渐变泛滥 | 使用独特的品牌色，尝试互补色或类比色方案 |
| 居中布局千篇一律 | 使用非对称网格、黄金分割、Z 型阅读路径 |
| 通用的 hover 缩放 | 使用视差、变形、色彩位移等独特交互 |
| 灰白背景 + 蓝色按钮 | 尝试深色模式、暖色调、高对比度方案 |

### 视觉层次构建

```css
/* 通过对比创造层次感，而非仅靠间距 */
.hero-title {
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.05;
  background: linear-gradient(135deg, #fff 0%, #94a3b8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* 装饰性元素增加品牌感 */
.hero-bg::before {
  content: '';
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, var(--color-primary) 0%, transparent 70%);
  opacity: 0.08;
  filter: blur(60px);
  top: -200px;
  right: -100px;
}
```

## 微交互动画示例

### 按钮交互

```css
.btn-primary {
  position: relative;
  padding: var(--space-3) var(--space-6);
  background: var(--color-primary);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

/* 光泽扫过效果 */
.btn-primary::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(110deg, transparent 30%, rgba(255,255,255,0.2) 50%, transparent 70%);
  transform: translateX(-100%);
  transition: transform 0.5s;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-glow);
}

.btn-primary:hover::after {
  transform: translateX(100%);
}
```

### 列表项入场动画

```css
@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.list-item {
  opacity: 0;
  animation: slideUp 0.5s ease forwards;
}

/* 使用 animation-delay 实现交错入场 */
.list-item:nth-child(1) { animation-delay: 0.05s; }
.list-item:nth-child(2) { animation-delay: 0.1s; }
.list-item:nth-child(3) { animation-delay: 0.15s; }
.list-item:nth-child(4) { animation-delay: 0.2s; }
```

## 响应式布局策略

### 断点设计

```css
/* 移动优先的断点体系 */
/* 默认: 移动端 (< 640px) */
.container { padding: var(--space-4); }

/* 平板 (>= 640px) */
@media (min-width: 640px) {
  .container { padding: var(--space-6); }
}

/* 桌面 (>= 1024px) */
@media (min-width: 1024px) {
  .container {
    padding: var(--space-8);
    max-width: 1200px;
    margin: 0 auto;
  }
}

/* 超宽屏 (>= 1536px) */
@media (min-width: 1536px) {
  .container { max-width: 1400px; }
}
```

### 容器查询（现代方案）

```css
.card-container {
  container-type: inline-size;
  container-name: card;
}

@container card (min-width: 400px) {
  .card {
    flex-direction: row;  /* 宽度足够时切换为水平布局 */
  }
  .card-image {
    width: 200px;
  }
}
```

## 无障碍设计要点

| 检查项 | 标准 | 实现方式 |
|:-------|:-----|:---------|
| 颜色对比度 | WCAG AA 4.5:1（正文）/ 3:1（大文本） | 使用对比度检查工具验证 |
| 焦点可见 | 键盘导航可见焦点环 | `:focus-visible { outline: 2px solid var(--color-primary); }` |
| 语义化标签 | 使用 HTML5 语义标签 | `<nav>`/`<main>`/`<article>`/`<aside>` |
| ARIA 标签 | 交互元素有 `aria-label` | 图标按钮: `aria-label="关闭"` |
| 动画偏好 | 尊重 `prefers-reduced-motion` | `@media (prefers-reduced-motion: reduce)` |
| 键盘导航 | Tab 顺序符合阅读顺序 | 合理使用 `tabindex`，避免 `tabindex > 0` |

## 性能优化建议

### CSS 架构选择

| 方案 | 适用场景 | 优点 | 缺点 |
|:-----|:---------|:-----|:-----|
| Tailwind CSS | 快速开发、组件库 | 原子化、无命名冲突 | 类名较长、学习成本 |
| CSS Modules | React 项目 | 局部作用域、零运行时 | 需构建工具支持 |
| Styled Components | 动态主题 | JS 中写 CSS、动态样式 | 运行时开销 |
| Vanilla CSS | 简单页面 | 无依赖、性能最优 | 全局作用域管理 |

### 关键渲染路径优化

1. **内联关键 CSS**：首屏样式内联到 `<style>` 标签中，避免渲染阻塞
2. **异步加载非关键 CSS**：`<link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'">`
3. **字体优化**：使用 `font-display: swap`，预加载关键字体
4. **图片优化**：使用 `loading="lazy"` 延迟加载非首屏图片，使用 WebP/AVIF 格式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | frontend-design处理的内容输入，可选值: json/text/markdown |
| design_brief | string | 否 | 设计需求描述，包含风格、目标用户、品牌调性 |
| tech_stack | string | 否 | 技术栈: `react`/`vue`/`svelte`/`html` |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "components": [
      {
        "name": "HeroSection",
        "code": "export function HeroSection() { ... }",
        "type": "react"
      },
      {
        "name": "FeatureGrid",
        "code": "export function FeatureGrid() { ... }",
        "type": "react"
      }
    ],
    "styles": ":root { --color-primary: #6366f1; ... }",
    "design_tokens": {
      "colors": {"primary": "#6366f1", "bg": "#0f0f23"},
      "spacing": {"base": "4px", "scale": "1.5"}
    },
    "metadata": {
      "template_used": "frontend-design-pro",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。

## 常见问题

### Q1: 如何开始使用Frontend Design？
A: 描述你的设计需求即可。例如"帮我设计一个 SaaS 产品落地页，深色主题，科技风格，需要 Hero 区、功能展示区、定价区"。系统会根据需求生成完整的前端代码（React 组件或 HTML+CSS），包含设计 Token、响应式布局、微交互动画和无障碍适配。你也可以指定技术栈和品牌色调。

### Q2: 如何避免生成的界面看起来像通用 AI 风格？
A: 提供具体的品牌调性描述和视觉参考。避免使用默认的紫蓝渐变方案，指定独特的品牌色彩。在描述中明确风格方向（如 Brutalism、玻璃态、新拟态），并要求使用非对称布局、混合圆角、独特交互效果。系统会根据这些差异化要求生成具有辨识度的设计。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

