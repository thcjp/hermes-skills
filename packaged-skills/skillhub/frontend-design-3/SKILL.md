---
slug: "frontend-design-3"
name: "frontend-design-3"
version: "0.1.0"
displayName: "Frontend Design"
summary: "创建独特的生产级前端界面，避免通用 AI 风格，支持 11 种美学方向。"
license: "Proprietary"
description: |-
  frontend-design-3 是一个前端设计技能，创建独特的生产级界面，避免通用"AI slop"美学。
  支持 11 种美学方向（极简、最大化、复古未来、有机自然、奢华精致、俏皮玩具、编辑杂志、
  粗野主义、艺术装饰、柔和粉彩、工业实用），覆盖字体、色彩、动效、空间构图和背景细节。
  输出生产级 HTML/CSS/JS 或 React/Vue 代码。适用于前端工程师和 UI 设计师的界面创建场景。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 创意设计
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Frontend Design

frontend-design-3 创建独特的生产级前端界面，避免通用"AI slop"美学。实现真正可用的代码，
对美学细节和创意选择保持卓越的关注度。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 设计思维与美学方向选择
在编码前理解上下文并承诺一个 BOLD 美学方向。分析四个维度：Purpose（界面解决什么问题、谁在使用）、
Tone（从 11 种方向中选择一种并极致执行）、Constraints（技术约束：框架、性能、无障碍）、
Differentiation（什么让这个界面令人难忘）。11 种美学方向：brutally minimal、maximalist chaos、
retro-futuristic、organic/natural、luxury/refined、playful/toy-like、editorial/magazine、
brutalist/raw、art deco/geometric、soft/pastel、industrial/utilitarian。- 验证执行结果，确认输出符合预期格式
- 参考`设计思维与美学方向选择`相关配置参数进行设置
### 2. 字体策略（Display + Body 配对）
选择美观、独特、有趣的字体。避免通用字体（Arial、Inter、Roboto、system fonts）。
将独特的 display 字体与精致的 body 字体配对。禁止跨代收敛到常见 AI 选择（如 Space Grotesk）。
根据美学方向匹配字体气质：editorial 方向使用衬线 display + 无衬线 body；
brutalist 方向使用等宽字体；art deco 方向使用几何无衬线。

**输入**: 用户提供字体策略（Display + Body 配对）所需的指令和必要参数。
**输出**: 返回字体策略（Display + Body 配对）的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`字体策略（Display + Body 配对）`相关配置参数进行设置
### 3. 色彩与主题系统
承诺一个连贯的美学。使用 CSS variables 保持一致性。主色配以锐利强调色优于胆怯的均匀分布调色板。
根据美学方向建立色彩系统：maximalist 使用高饱和度撞色；minimalist 使用单色+一个强调色；
retro-futuristic 使用霓虹色+暗色背景；organic/natural 使用大地色系。
支持 light/dark 主题切换，每次设计应使用不同的主题和配色。

**输入**: 用户提供色彩与主题系统所需的指令和必要参数。
**处理**: 按照skill规范执行色彩与主题系统操作,遵循单一意图原则。
**输出**: 返回色彩与主题系统的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`色彩与主题系统`相关配置参数进行设置
### 4. 动效与微交互
使用动画创造效果和微交互。HTML 优先使用 CSS-only 方案（`@keyframes`、`transition`、
`transform`）。React 环境优先使用 Motion 库（`motion.div`、`useScroll`、`useTransform`）。
聚焦高影响力时刻：一次精心编排的页面加载配合 staggered reveals 比散落的微交互更有感染力。
maximalist 设计需要大量动画和效果；minimalist 设计需要克制、精准和细微细节。

**输入**: 用户提供动效与微交互所需的指令和必要参数。
**处理**: 按照skill规范执行动效与微交互操作,遵循单一意图原则。
**输出**: 返回动效与微交互的执行结果,包含操作状态和输出数据。

### 5. 空间构图与布局
使用意想不到的布局。非对称构图、重叠元素、对角线流向、grid-breaking 元素。
慷慨的负空间或受控的密度。根据美学方向选择构图策略：editorial 方向使用严格的网格+刻意打破；
brutalist 方向使用原始的未对齐布局；art deco 方向使用对称几何构图。
使用 CSS Grid 和 Flexbox 实现复杂布局，`grid-template-areas` 定义区域关系。

**输入**: 用户提供空间构图与布局所需的指令和必要参数。
**处理**: 按照skill规范执行空间构图与布局操作,遵循单一意图原则。
**输出**: 返回空间构图与布局的执行结果,包含操作状态和输出数据。

### 6. 背景与视觉细节
创造氛围和深度而非默认纯色背景。应用创意形式：gradient meshes（`radial-gradient` 叠加）、
noise textures（SVG `feTurbulence` 滤镜）、geometric patterns（`repeating-linear-gradient`）、
layered transparencies（`rgba` + `backdrop-filter`）、dramatic shadows（多层 `box-shadow`）、
decorative borders（`border-image` 或伪元素）、custom cursors（`cursor: url()`）、
grain overlays（SVG noise pattern 叠加 `mix-blend-mode`）。

**输入**: 用户提供背景与视觉细节所需的指令和必要参数。
**处理**: 按照skill规范执行背景与视觉细节操作,遵循单一意图原则。
**输出**: 返回背景与视觉细节的执行结果,包含操作状态和输出数据。

### 7. 反模式规避
禁止使用：过度使用的字体族（Inter、Roboto、Arial、system fonts）；老套配色方案
（白色背景上的紫色渐变）；可预测的布局和组件模式；缺乏上下文特征的千篇一律设计。
禁止跨代收敛到常见 AI 选择。每次设计应使用不同的字体、配色和美学方向。

**输入**: 用户提供反模式规避所需的指令和必要参数。
**处理**: 按照skill规范执行反模式规避操作,遵循单一意图原则。
**输出**: 返回反模式规避的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`反模式规避`相关配置参数进行设置
### 8. 实现复杂度匹配
根据美学愿景匹配实现复杂度。maximalist 设计需要精心编写大量代码，包含丰富的动画和效果。
minimalist 设计需要克制、精准，仔细关注间距、字体和细微细节。优雅来自于对愿景的精准执行。
输出生产级功能代码（HTML/CSS/JS、React、Vue 等），视觉上引人注目且令人难忘。- 验证执行结果，确认输出符合预期格式
- 参考`实现复杂度匹配`相关配置参数进行设置
#
## 使用流程

1. 分析界面目的、目标用户和技术约束
2. 从 11 种美学方向中选择一种并极致执行
3. 确定 Differentiation：这个界面令人难忘的一个特征
4. 选择字体配对（display + body），避免通用字体
5. 建立色彩系统，使用 CSS variables，主色+锐利强调色
6. 设计空间构图，使用非对称、重叠或 grid-breaking 布局
7. 添加背景细节（gradient meshes、noise textures、grain overlays）
8. 实现动效，聚焦高影响力时刻（staggered reveals 页面加载）
9. 检查反模式：确认无 Inter/Roboto/Arial、无紫色渐变白底、无可预测布局
10. 输出生产级代码，在 light/dark 主题和不同美学间变化

#
## 示例

### 示例1：Editorial 杂志风格落地页

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <style>
    :root {
      --display-font: 'Playfair Display', serif;
      --body-font: 'Inter', sans-serif; /* 注意：实际应避免 Inter，此处仅演示结构 */
      --ink: #1a1a1a;
      --paper: #f5f0e8;
      --accent: #c8102e;
    }
    body {
      font-family: var(--body-font);
      background: var(--paper);
      color: var(--ink);
      margin: 0;
    }
    .hero {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 48px;
      padding: 80px 64px;
    }
    .hero h1 {
      font-family: var(--display-font);
      font-size: 96px;
      font-weight: 900;
      line-height: 0.9;
      letter-spacing: -2px;
    }
    .hero h1 span {
      color: var(--accent);
      font-style: italic;
    }
    /* Grain overlay */
    body::after {
      content: '';
      position: fixed;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.08'/%3E%3C/svg%3E");
      pointer-events: none;
      mix-blend-mode: multiply;
    }
    @keyframes reveal {
      from { opacity: 0; transform: translateY(24px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .hero h1 { animation: reveal 0.8s ease-out; }
    .hero p { animation: reveal 0.8s ease-out 0.2s both; }
  </style>
</head>
<body>
  <section class="hero">
    <h1>The Art of <span>Slow</span> Design</h1>
    <p>A quarterly journal on craft, intention, and the spaces between.</p>
  </section>
</body>
</html>
```

### 示例2：React + Motion 库的 Maximalist 仪表盘

```jsx
import { motion } from 'motion/react';

const stats = [
  { label: 'Active Users', value: '12,847', color: '#ff006e' },
  { label: 'Revenue', value: '$48.2K', color: '#8338ec' },
  { label: 'Growth', value: '+23%', color: '#3a86ff' },
];

export default function Dashboard() {
  return (
    <div style={{
      background: 'linear-gradient(135deg, #0d0221 0%, #1a0b3d 50%, #0d0221 100%)',
      minHeight: '100vh',
      padding: '32px',
    }}>
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: '24px',
        }}
      >
        {stats.map((stat, i) => (
          <motion.div
            key={stat.label}
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: i * 0.15, duration: 0.6, ease: 'easeOut' }}
            style={{
              background: `${stat.color}22`,
              border: `2px solid ${stat.color}`,
              borderRadius: '0px', /* Brutalist: sharp corners */
              padding: '32px',
              boxShadow: `8px 8px 0px ${stat.color}`,
            }}
          >
            <div style={{ color: stat.color, fontSize: '48px', fontWeight: 900 }}>
              {stat.value}
            </div>
            <div style={{ color: '#fff', fontSize: '14px', textTransform: 'uppercase' }}>
              {stat.label}
            </div>
          </motion.div>
        ))}
      </motion.div>
    </div>
  );
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 字体跨代收敛到 Space Grotesk | AI 倾向于重复选择"安全"的独特字体 | 明确禁止 Space Grotesk，每次从不同字体族选择（如 Fraunces、DM Mono、Cormorant） |
| 使用 Inter/Roboto/Arial 通用字体 | 默认使用系统字体或流行字体 | 选择 Distinctive 字体配对，display 字体使用 Google Fonts 或自托管字体 |
| 白底紫色渐变老套配色 | AI 默认倾向常见的科技感配色 | 根据美学方向选择独特配色：editorial 用 ink+paper+accent；brutalist 用黑白+一个霓虹色 |
| 可预测的居中三列卡片布局 | 默认使用 Bootstrap 风格的对称网格 | 使用非对称 grid-template-columns（如 2fr 1fr）、重叠定位、对角线流向 |
| 散落的微交互缺乏编排 | 每个元素独立动画，缺乏整体节奏 | 聚焦一次 staggered reveals 页面加载，使用 transition delay 编排时序 |
| 背景使用纯色缺乏深度 | 忽略背景层次和氛围 | 添加 gradient meshes（多层 radial-gradient）、noise textures（SVG feTurbulence）、grain overlays |
| Minimalist 设计过度装饰 | 在需要克制的方向上添加过多元素 | minimalist 方向使用严格限制：单一字体、2-3 种颜色、大量负空间、仅必要的动画 |

## 常见问题

### Q1: 11 种美学方向如何选择？
A: 根据 Purpose 和 Tone 选择。界面面向创意人群 → editorial/magazine 或 brutalist/raw；
面向企业用户 → luxury/refined 或 industrial/utilitarian；面向消费者 → playful/toy-like
或 soft/pastel；面向技术人群 → retro-futuristic 或 art deco/geometric。关键是选择一种
并极致执行，不要混合多种方向。

### Q2: 字体配对有什么具体建议？
A: Display 字体负责标题和视觉冲击，Body 字体负责正文可读性。Editorial 方向：Playfair Display
（display）+ DM Sans（body）；Brutalist 方向：Space Mono（display）+ JetBrains Mono（body）；
Organic 方向：Cormorant（display）+ Nunito（body）。禁止使用 Inter、Roboto、Arial 作为
display 字体。

### Q3: Motion 库和 CSS 动画如何选择？
A: HTML 项目优先使用 CSS-only 方案（`@keyframes`、`transition`、`transform`），减少依赖。
React 项目使用 Motion 库获得更强大的编排能力（`useScroll`、`useTransform`、`stagger`）。
无论哪种方式，聚焦高影响力时刻：一次精心编排的页面加载比散落的微交互更有效。

### Q4: gradient meshes 和 noise textures 如何实现？
A: Gradient meshes 使用多层 `radial-gradient` 叠加创建有机色彩过渡。Noise textures 使用
SVG `feTurbulence` 滤镜生成纹理，通过 `mix-blend-mode` 叠加到背景上。Grain overlays 使用
SVG noise pattern 作为 `body::after` 伪元素背景，设置 `pointer-events: none` 和
`mix-blend-mode: multiply` 实现胶片颗粒效果。

### Q5: 如何避免"AI slop"美学？
A: AI slop 的特征是：居中布局、紫色渐变白底、Inter 字体、圆角卡片、通用阴影。避免方法是
每次设计选择不同的美学方向、字体、配色和布局。使用反模式清单自查：确认无 Inter/Roboto/Arial、
无紫色渐变白底、无可预测的三列卡片、无圆角 8px 通用样式。每次设计应在 light/dark 主题间变化。

### Q6: minimalist 和 maximalist 的实现复杂度有何不同？
A: Maximalist 需要精心编写大量代码：多层背景、丰富动画、复杂布局、装饰元素。
Minimalist 需要克制和精准：严格限制字体（1-2 种）、颜色（2-3 种）、动画（仅必要）。
两者都需要对细节的极致关注，但方向相反——maximalist 在做加法中求和谐，minimalist 在做减法中求精度。

## 已知限制

- 字体选择依赖 Google Fonts 或自托管字体文件的可用性
- 复杂动画在低端设备上可能影响性能，需测试 `will-change` 和 `transform` 优化
- SVG noise textures 在某些浏览器中渲染表现不一致
- 自定义光标（`cursor: url()`）在触屏设备上无效
- 每次设计的美学方向选择具有主观性，建议与团队对齐方向后再执行
