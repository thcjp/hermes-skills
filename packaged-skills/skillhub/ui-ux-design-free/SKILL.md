---
slug: "ui-ux-design-free"
name: "ui-ux-design-free"
version: 1.0.1
displayName: "UI/UX设计指南免费版"
summary: "免费版UI/UX设计指南，涵盖基础设计原则、配色与排版系统。"
license: "MIT"
description: |-
  UI/UX设计指南免费版，提供基础设计原则与快速参考.
  涵盖Mobile-First设计、配色系统、排版尺度与基础无障碍要求.
  适用于个人项目的界面设计指导.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 创意设计
pricing_tier: "L2-标准级"
suggested_price: "19.9 CNY/per_use"
tools: ["read", "write", "exec"]
tags: "设计,UI/UX,创意"
category: "Creative"
---
# UI/UX设计指南（免费版）

涵盖基础设计原则、配色与排版系统的UI/UX指南.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | UI/UX设计指南免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 核心设计原则（Core Design Principles）
基础设计原则指导UI决策：

- **Mobile-First**：从320px宽度开始，断点576px/768px/992px/1200px
- **Visual Hierarchy**：通过大小、颜色、留白、对比引导注意力
- **Whitespace**：间距使用8px倍数（8, 16, 24, 32, 48, 64）

**输入**: 用户提供核心设计原则（Core Design Principles）所需的指令和必要参数.
**处理**: 解析核心设计原则（Core Design Principles）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回核心设计原则（Core Design Principles）的处理结果,包含执行状态码、结果数据和执行日志。### 配色系统（Color System）
基础配色方案构建：

- **Primary**：品牌色（CTA、链接、激活状态）
- **Neutrals**：灰色50-900（文本、背景、边框）
- **Semantic**：Success（绿）、Error（红）、Warning（黄）

**输入**: 用户提供配色系统（Color System）所需的指令和必要参数.
**处理**: 解析配色系统（Color System）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回配色系统（Color System）的处理结果,包含执行状态码、结果数据和执行日志。### 排版系统（Typography Scale）
基于8px基线的排版尺度：

```text
text-base: 16px / 24px (body default)
text-lg:   18px / 28px
text-xl:   20px / 28px
text-2xl:  24px / 32px
text-3xl:  30px / 36px (section headers)
```

字体配对：最多2种字体（UI用无衬线，标题可选衬线）

**输入**: 用户提供排版系统（Typography Scale）所需的指令和必要参数.
**处理**: 解析排版系统（Typography Scale）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回排版系统（Typography Scale）的处理结果,包含执行状态码、结果数据和执行日志。### 基础无障碍（Accessibility）
WCAG基础要求：

- 文本对比度：最低4.5:1（正常文本），3:1（大文本）
- UI组件：最低3:1对比度
- 键盘导航：Tab顺序合理，焦点状态可见

**输入**: 用户提供基础无障碍（Accessibility）所需的指令和必要参数.
**处理**: 解析基础无障碍（Accessibility）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回基础无障碍（Accessibility）的处理结果,包含执行状态码、结果数据和执行日志.
### Mobile-First

针对Mobile-First,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Mobile-First相关的配置参数、输入数据和处理选项.
**输出**: 返回Mobile-First的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Mobile-First`的配置文档进行参数调优
### Visual Hierarchy

针对Visual Hierarchy,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Visual Hierarchy相关的配置参数、输入数据和处理选项.
**输出**: 返回Visual Hierarchy的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Visual Hierarchy`的配置文档进行参数调优
#
## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 确定设计需求：配色、排版、布局等
3. 参考核心设计原则指导设计决策
4. 使用快速参考中的尺度生成代码
5. 验证无障碍对比度

#
## 示例

### 示例1：选择基础配色方案

```
用户: 帮我设计一个SaaS产品的配色方案
# ...
Agent: 推荐配色方案：
- Primary: #3B82F6 (blue-500) - 品牌色，用于CTA按钮
- Neutrals: gray-50 到 gray-900 - 文本与背景
- Success: #22C55E (green-500)
- Error: #EF4444 (red-500)
- Warning: #F59E0B (amber-500)
- 文本对比度: gray-900 on white = 16.1:1 ✅
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 对比度不达标 | 配色选择不当 | 调整颜色深度至4.5:1以上 |
| 排版不一致 | 尺度未统一 | 使用8px基线排版尺度 |
| 布局错乱 | 断点使用不当 | 确认Mobile-First顺序 |

## 常见问题

### Q1: 免费版与付费版有什么区别？
A: 免费版提供基础设计原则、配色与排版指导。付费版额外提供Shadcn/ui+Tailwind技术栈集成、微交互设计、UI设计五法则、构建前检查清单等完整功能.
### Q2: 如何确保无障碍合规？
A: 确保文本对比度至少4.5:1，UI组件对比度至少3:1，提供键盘导航与焦点状态，为交互元素添加ARIA标签.
### Q3: Mobile-First设计怎么做？
A: 从最小屏幕（320px）开始设计单列布局，使用断点逐步扩展到大屏幕。在CSS中使用min-width媒体查询.
## 已知限制

- 不包含Shadcn/ui + Tailwind技术栈集成
- 不包含微交互设计指导
- 不包含UI设计五法则详解
- 不包含构建前检查清单

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "UI/UX设计指南免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "ui-ux-design"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
