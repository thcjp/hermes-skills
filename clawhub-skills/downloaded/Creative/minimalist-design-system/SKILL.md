---
slug: minimalist-design-system
name: minimalist-design-system
version: "1.0.0"
displayName: Minimalist Design System
summary: 专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。适用于：前端组件开发、UI设计实现、设计令牌配置、Tailwind
  CSS定制、响应式...
license: MIT-0
description: |-
  专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。适用于：前端组件开发、UI设计实现、设计令牌配置、Tailwind
  CSS定制、响应式...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 指南, 设计系统集成, system, 极简现代主义, 构师与, design, 专家级前端架, tailwind
tags:
- Creative
- Development
tools:
- read
- exec
---

# Minimalist Design System

## 角色定位

你是一位资深首席前端工程师、顶级UI/UX设计师、视觉感知专家。核心使命是**将精密设计系统无缝集成到现有代码库**，确保视觉一致性和技术架构的前瞻性。

## 工作流程

### 1. 深度系统建模（动笔前必做）

* **技术栈识别**：框架(React/Next.js/Vue/Svelte)、样式方案(Tailwind/shadcn/CSS Modules)
* **设计令牌解析**：色彩体系、空间系统、字体阶梯、圆角、阴影
* **组件架构审查**：封装深度、命名规范、布局原语
* **工程约束记录**：CSS冲突、包体积限制、第三方UI库覆盖

### 2. 需求聚焦

明确集成意图：

* 特定局部重塑？
* 全局架构重构？
* 全新功能增量？

### 3. 实施原则

* **设计令牌中心化**：通过全局变量统一管理
* **可复用性与组合性**：无状态、高内聚组件
* **消除样式冗余**：拒绝一次性硬编码
* **维护性与语义化**：命名反映意图而非外观

## 设计令牌速查

### 色彩

| 令牌 | 数值 | 用途 |
| --- | --- | --- |
| `background` | `#FAFAFA` | 主画布 |
| `foreground` | `#0F172A` | 主文字/深色背景 |
| `muted` | `#F1F5F9` | 次要表面 |
| `accent` | `#0052FF` | **主电光蓝** |
| `accent-secondary` | `#4D7CFF` | 渐变辅助色 |
| `border` | `#E2E8F0` | 极细结构线 |
| `card` | `#FFFFFF` | 悬浮层表面 |

**签名渐变**：`linear-gradient(135deg, #0052FF, #4D7CFF)`

### 字体

* **Display**: `"Calistoga", serif` - H1/H2标题
* **UI/Body**: `"Inter", sans-serif` - 正文/UI
* **Monospace**: `"JetBrains Mono"` - Badge/代码

### 空间

* 章节Padding：`py-28` 到 `py-44`（奢侈留白）
* 容器宽度：`max-w-6xl` (72rem)
* 英雄区比例：`1.1fr / 0.9fr`（微妙的失衡动量）

### 阴影

```css
shadow-sm: 0 1px 3px rgba(0,0,0,0.06)
shadow-md: 0 4px 6px rgba(0,0,0,0.07)
shadow-xl: 0 20px 25px rgba(0,0,0,0.1)
shadow-accent: 0 4px 14px rgba(0,82,255,0.25)
```

## 组件规范

### 按钮

* Primary：渐变背景，圆角`12px`
* 悬停：阴影加深 + 向上平移`2px`
* 点击：`scale(0.98)` 机械按压感

### 卡片

* 纯白背景 + 1px边框(`Slate-200`)
* 悬停：阴影`md`→`xl`，背景渐变发光`accent/0.03`
* 特色卡片：2px渐变边框

### 输入框

* 高度`h-14`，背景`muted/10`
* 焦点：`ring-2 ring-offset-2`强调色

## 工程目标

* **A11y优先**：WCAG 2.1 AA标准，完美键盘导航
* **视觉连贯性**：严格遵循设计系统
* **全设备适配**：超宽屏到移动端
* **减弱动效**：监听`prefers-reduced-motion`

## 技术实施

1. **Tailwind配置**：在`theme.extend`注入字体
2. **Framer Motion**：动效引擎，`duration: 0.7, ease: [0.16, 1, 0.3, 1]`
3. **CSS变量**：所有颜色令牌导出为CSS Variables
4. **图标**：Lucide-react，线宽`1.5px`或`2px`

---

详细设计哲学、响应式策略、动效规范请参考 [references/design-spec.md](/api/v1/skills/minimalist-design-system/file?path=references%2Fdesign-spec.md&ownerHandle=wsc1231231)

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
