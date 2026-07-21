---
slug: minimalist-design-system
name: minimalist-design-system
version: "1.0.0"
displayName: Minimalist Design Sy
summary: 专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。适用于：前端组件开发、UI设计实现、设计令牌配置、Tailwind
  CSS定制、响应式...
license: MIT-0
description: |-
  专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。
tags:
- Creative
- Development
tools:
  - - read
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

- 专家级前端架构师与UI/UX设计系统集成指南
- 极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库
- 适用于：前端组件开发、UI设计实现、设计令牌配置、Tailwind
  CSS定制、响应式
- 触发关键词: 指南, 设计系统集成, system, 极简现代主义, 构师与, design, 专家级前端架, tailwind

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
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
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Minimalist Design Sy？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Minimalist Design Sy有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
