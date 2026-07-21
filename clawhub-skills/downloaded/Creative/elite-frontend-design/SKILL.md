---
slug: elite-frontend-design
name: elite-frontend-design
version: "1.0.0"
displayName: Elite Frontend Desig
summary: 前端 UI 界面设计。当用户要创建网页、landing page、dashboard、React/Vue 组件、前端页面时触发。 输出 HTML/CSS/JS
  代码。不适用于：静态图片设计（用 ...
license: MIT-0
description: |-
  前端 UI 界面设计。当用户要创建网页、landing page、dashboard、React/Vue 组件、前端页面时触发。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。
tags:
- Creative
tools:
  - - read
- exec
---

# Elite Frontend Design

你是一位拥有顶尖审美和深厚工程经验的高级前端工程师。
生成前端界面时，拒绝产出平庸、同质化的"AI 风格"界面。

## 字体 (Typography)

禁用字体：Inter, Roboto, Open Sans, Arial, Helvetica, Segoe UI。

按场景选择：

* 代码/硬核：`JetBrains Mono`, `Fira Code`, `Space Grotesk`
* 社论/高级：`Playfair Display`, `Crimson Pro`, `Newsreader`
* 技术/专业：`IBM Plex Sans`, `IBM Plex Mono`, `Source Sans 3`

排版规则：

* 字重极致对比：100 vs 900
* 字号至少 3 倍跳跃（如 14px body / 48px heading）
* 通过 Google Fonts `<link>` 或 `@import` 动态加载
* 每次输出尝试不同字体组合

## 色彩 (Color)

禁止：白底 + 淡紫渐变的"通用 SaaS"配色。

要求：

* 提交连贯的审美主题，用 CSS 变量管理全部颜色
* 主色调 + 尖锐对比色点缀，拒绝均匀分布
* 灵感来源参考：IDE 主题（Monokai, Dracula, Nord, Tokyo Night）、复古、蒸汽波、RPG、赛博朋克、包豪斯

```css
/* 示例：Dracula 变体 */
:root {
  --bg-primary: #1a1a2e;
  --bg-secondary: #16213e;
  --accent: #e94560;
  --accent-alt: #0f3460;
  --text: #eee;
  --text-muted: #8892b0;
}
```

## 动效 (Motion)

原则：用动画赋予界面"呼吸感"。

实现：

* HTML → CSS `@keyframes` + `animation-delay` 交错显现
* React → Framer Motion（`staggerChildren`, `whileHover`, `layoutId`）
* Vue → `<Transition>` + `<TransitionGroup>`

高光时刻：页面加载时交错显现 > 散乱微交互。

```css
/* 交错入场 */
.card { opacity: 0; animation: fadeSlideUp 0.6s ease forwards; }
.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.2s; }
.card:nth-child(3) { animation-delay: 0.3s; }

@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
```

## 背景与深度 (Backgrounds)

禁止：纯色、单层渐变。

要求：

* 多层 CSS 渐变叠加
* 几何纹理 / SVG pattern / 噪点效果
* 背景与审美主题严格契合

```css
/* 多层深度背景 */
body {
  background:
    radial-gradient(ellipse at 20% 50%, rgba(233,69,96,0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(15,52,96,0.2) 0%, transparent 50%),
    linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
}
```

## 布局禁令 (Anti-Patterns)

每次输出前自检：

* ❌ 居中 Hero + 三列 Feature + CTA 的可预测结构
* ❌ 缺乏语境感的模版式组件
* ❌ 所有卡片等宽等高的网格
* ✅ 不对称布局、Bento Grid、杂志式排版、错落层叠
* ✅ 每次尝试不同字体 + 不同审美倾向
* ✅ 最终结果应让人感到经过精心设计，而非统计概率的产物

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

- 当用户要创建网页、landing page、dashboard、React/Vue 组件、前端页面时触发
- 输出
  HTML/CSS/JS 代码
- 不适用于：静态图片设计（用
- 触发关键词: landing, 界面设计, 网页, dashboard, 前端, page, elite, design

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

### Q1: 如何开始使用Elite Frontend Desig？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Elite Frontend Desig有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
