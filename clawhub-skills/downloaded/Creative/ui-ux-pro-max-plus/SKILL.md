---
slug: ui-ux-pro-max-plus
name: ui-ux-pro-max-plus
version: "1.0.0"
displayName: UI UX Pro Max
summary: Professional UI/UX design resource library with searchable design patterns,
  color palettes, font ...
license: MIT
description: |-
  Professional UI/UX design resource library with searchable design patterns,
  color palettes, font ...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: professional, design, library, resource
tags:
- Creative
tools:
- read
- exec
---

# UI UX Pro Max

完整的 UI/UX 设计资源库，让 AI 生成的界面像专业设计师作品一样精美。

## 何时使用此 Skill

* 设计任何用户界面时需要专业参考
* 选择配色方案（品牌色、功能色、中性色）
* 挑选字体组合（标题+正文）
* 设计数据可视化图表
* 需要 UX 最佳实践指导
* 寻找特定行业/风格的设计灵感

## 资源导航

| 资源类型 | 文件 | 内容 |
| --- | --- | --- |
| 🎨 **UI 风格库** | [references/ui-styles.md](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fui-styles.md&ownerHandle=ireact2code) | 50+ 种界面设计风格 |
| 🌈 **配色方案** | [references/color-palettes.md](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fcolor-palettes.md&ownerHandle=ireact2code) | 100+ 专业调色板 |
| 🔤 **字体配对** | [references/typography.md](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Ftypography.md&ownerHandle=ireact2code) | 精选字体组合 |
| 📊 **图表类型** | [references/charts.md](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fcharts.md&ownerHandle=ireact2code) | 数据可视化指南 |
| 📘 **UX 模式** | [references/ux-patterns.md](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fux-patterns.md&ownerHandle=ireact2code) | 用户体验最佳实践 |
| 🎯 **组件库** | [references/components.md](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fcomponents.md&ownerHandle=ireact2code) | 常用组件设计规范 |

## 快速开始

### 1. 确定设计风格

先读取 `references/ui-styles.md`，选择适合项目的设计风格：

* SaaS/企业应用 → Minimalist / Corporate
* 电商 → Modern E-commerce / Luxury
* 创意作品 → Brutalist / Glassmorphism
* 社交应用 → Neumorphism / Soft UI

### 2. 选择配色

读取 `references/color-palettes.md`，根据品牌调性选择：

* 科技/专业 → Blue/Cyan 系列
* 自然/健康 → Green/Earth 系列
* 时尚/美妆 → Purple/Pink 系列
* 金融/法律 → Navy/Gray 系列

### 3. 搭配字体

读取 `references/typography.md`：

* 现代科技感 → Inter + JetBrains Mono
* 优雅精致 → Playfair Display + Inter
* 友好亲和 → Nunito + Open Sans

### 4. 应用 UX 模式

读取 `references/ux-patterns.md` 获取具体场景的交互模式。

## 设计决策框架

### 选择 UI 风格的 3 个问题

1. **目标用户是谁？**

   * 企业用户 → 简洁、专业、高效
   * 年轻消费者 → 活泼、大胆、有趣
   * 高端客户 → 精致、留白、质感
2. **产品类型是什么？**

   * 工具类 → 功能优先，清晰直观
   * 内容类 → 阅读体验，排版优雅
   * 社交类 → 情感连接，互动感强
3. **品牌调性如何？**

   * 创新先锋 → 尝试新风格（Glassmorphism）
   * 稳定可靠 → 经典风格（Material Design）
   * 独特个性 → 大胆风格（Brutalist）

### 配色选择矩阵

| 场景 | 主色 | 辅助色 | 强调色 |
| --- | --- | --- | --- |
| 科技产品 | Blue-600 | Slate-500 | Cyan-400 |
| 健康医疗 | Teal-600 | Gray-500 | Emerald-400 |
| 金融科技 | Indigo-700 | Gray-600 | Amber-500 |
| 电商零售 | Rose-600 | Gray-500 | Violet-500 |
| 教育培训 | Violet-600 | Slate-500 | Yellow-400 |
| 娱乐社交 | Fuchsia-600 | Gray-500 | Pink-500 |

## 实用技巧

### Tailwind CSS 快速应用

```css
/* 配色示例 */
.bg-brand { @apply bg-blue-600; }
.text-muted { @apply text-gray-500; }
.border-accent { @apply border-cyan-400; }

/* 字体示例 */
.font-heading { @apply font-display text-3xl font-bold; }
.font-body { @apply font-sans text-base leading-relaxed; }
```

### 响应式断点建议

```text
Mobile First:
- 默认: 320px+
- sm: 640px+
- md: 768px+
- lg: 1024px+
- xl: 1280px+
```

### 间距系统

```css
/* 8px 基础倍数 */
space-1: 4px
space-2: 8px
space-3: 12px
space-4: 16px
space-6: 24px
space-8: 32px
space-12: 48px
space-16: 64px
```

## 专业提示

1. **不要混合太多风格** - 选择1种主风格，2-3个设计元素点缀
2. **颜色不超过5种** - 主色、辅助色、中性色、成功色、错误色
3. **字体最多2种** - 1种标题字体 + 1种正文字体
4. **留白是设计** - 不要害怕空白，它是呼吸空间
5. **一致性 > 创新** - 保持设计系统的一致性比追求独特更重要

## 参考资源

* [UI Styles →](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fui-styles.md&ownerHandle=ireact2code) 选择界面风格
* [Color Palettes →](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fcolor-palettes.md&ownerHandle=ireact2code) 选择配色方案
* [Typography →](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Ftypography.md&ownerHandle=ireact2code) 选择字体配对
* [Charts →](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fcharts.md&ownerHandle=ireact2code) 选择图表类型
* [UX Patterns →](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fux-patterns.md&ownerHandle=ireact2code) 学习交互模式
* [Components →](/api/v1/skills/ui-ux-pro-max-plus/file?path=references%2Fcomponents.md&ownerHandle=ireact2code) 查看组件规范

---

**记住：** 好的设计不是堆砌特效，而是解决问题。先确保可用性，再追求美观。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
