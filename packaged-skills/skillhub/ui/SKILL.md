---
slug: "ui"
name: "ui"
version: 1.0.1
displayName: "UI"
summary: "设计清晰一致视觉精致的用户界面。Design clear, consistent, and visually polished user interfaces。核心能力: - 创意设计领域的"
license: "Proprietary"
description: |-
  Design clear, consistent, and visually polished user interfaces。核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Creative
  - UI设计
  - 前端
  - 设计
  - button
  - rem
  - class
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# UI

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

- Design clear, consistent, and visually polished user interfaces
- 设计系统构建：颜色体系、字体规范、间距栅格
- 组件库设计：按钮、表单、卡片、导航、模态框等
- 响应式布局与无障碍设计（WCAG 2.1 AA）

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 设计原则

| 原则 | 核心理念 | 实践要点 |
|:-----|:------|:------|
| 清晰性 | 用户一眼理解界面用途 | 视觉层级分明，标签语义化，操作可预测 |
| 一致性 | 相同功能用相同方式呈现 | 组件复用，交互模式统一，命名规范 |
| 反馈性 | 每个操作都有即时反馈 | Loading状态、Hover/Active态、Toast提示 |
| 容错性 | 防止用户犯错，犯错后易恢复 | 确认对话框、撤销操作、输入验证 |

## 颜色设计系统

### 语义化颜色令牌

```css
:root {
  /* 主色 */
  --color-primary-50:  #eef2ff;
  --color-primary-100: #e0e7ff;
  --color-primary-500: #6366f1;  /* 主按钮、链接 */
  --color-primary-600: #4f46e5;  /* Hover态 */
  --color-primary-700: #4338ca;  /* Active态 */

  /* 语义色 */
  --color-success: #10b981;  /* 成功操作 */
  --color-warning: #f59e0b;  /* 警告提示 */
  --color-danger:  #ef4444;  /* 错误/删除 */
  --color-info:    #3b82f6;  /* 信息提示 */

  /* 中性色 */
  --color-bg:        #ffffff;
  --color-surface:   #f8fafc;
  --color-border:    #e2e8f0;
  --color-text:      #1e293b;
  --color-text-muted: #64748b;
}
```

### 对比度要求（WCAG 2.1 AA）

| 元素类型 | 最低对比度 | 示例 |
|:------|:------|:------|
| 正文文本 | 4.5:1 | `#1e293b` on `#ffffff` = 14.7:1 |
| 大文本（18px+） | 3.0:1 | `#64748b` on `#ffffff` = 4.7:1 |
| 交互组件边框 | 3.0:1 | 输入框边框需可见 |
| 禁用状态 | 不要求 | 但需视觉上明显区分 |

## 字体规范

### 字体层级

| 层级 | 用途 | 字号 | 字重 | 行高 |
|:-----|:------|:------|:------|:------|
| Display | 首页大标题 | 48px / 3rem | 700 | 1.2 |
| H1 | 页面标题 | 36px / 2.25rem | 700 | 1.3 |
| H2 | 区块标题 | 28px / 1.75rem | 600 | 1.4 |
| H3 | 子标题 | 22px / 1.375rem | 600 | 1.4 |
| Body | 正文 | 16px / 1rem | 400 | 1.6 |
| Body Small | 辅助文本 | 14px / 0.875rem | 400 | 1.5 |
| Caption | 标签/说明 | 12px / 0.75rem | 400 | 1.4 |

### 间距系统（8px栅格）

```
--space-1:  4px   /* 组件内紧凑间距 */
--space-2:  8px   /* 基础间距 */
--space-3:  12px  /* 组件内元素间距 */
--space-4:  16px  /* 组件间间距 */
--space-6:  24px  /* 区块内间距 */
--space-8:  32px  /* 区块间间距 */
--space-12: 48px  /* 大区块间距 */
--space-16: 64px  /* 页面级间距 */
```

## 响应式断点

| 断点名称 | 宽度范围 | 栅格列数 | 典型设备 |
|:------|:------|:------|:------|
| xs | < 640px | 4列 | 手机竖屏 |
| sm | 640-767px | 4列 | 手机横屏 |
| md | 768-1023px | 8列 | 平板 |
| lg | 1024-1279px | 12列 | 笔记本 |
| xl | >= 1280px | 12列 | 桌面显示器 |

## 组件设计规范

### 按钮组件

```html
<!-- 主按钮 -->
<button class="btn btn-primary">提交</button>

<!-- 次要按钮 -->
<button class="btn btn-secondary">取消</button>

<!-- 危险按钮 -->
<button class="btn btn-danger">删除</button>

<!-- 禁用状态 -->
<button class="btn btn-primary" disabled>提交中...</button>
```

**按钮设计要点**：
- 最小高度 40px，最小点击区域 44x44px（移动端）
- 内边距：水平 16px，垂直 8px
- 圆角：4-8px（与整体风格一致）
- Hover态：加深10%背景色
- Focus态：2px outline，颜色为主色

### 表单输入

```html
<label for="email">邮箱地址</label>
<input type="email" id="email" placeholder="user@example.com" required />
<span class="field-error">请输入有效的邮箱地址</span>
```

**表单设计要点**：
- 标签始终在输入框上方
- 错误提示紧邻输入框下方，红色文字
- 必填字段标注星号
- 输入框最小高度 40px

## 无障碍设计清单

- [ ] 所有交互元素可通过键盘操作（Tab导航，Enter/Space激活）
- [ ] 焦点态可见（focus outline 不被移除）
- [ ] 图片有 alt 文本，装饰图片用 alt=""
- [ ] 颜色对比度满足 WCAG 2.1 AA 标准
- [ ] 表单字段有关联的 label 标签
- [ ] 错误信息通过 aria-describedby 关联到输入框
- [ ] 动态内容变化通过 aria-live 通知屏幕阅读器
- [ ] 页面有清晰的 h1-h6 标题层级结构
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 设计清晰一致视觉精致 | 目标数据与配置参数 | 处理结果与执行状态 |
| ui操作执行 | ui相关参数与配置 | 执行结果与返回数据 |
| ui状态查询 | 查询条件与过滤选项 | 当前状态与详细信息 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | ui处理的内容输入 |,  |
| content | string | 否 | ui处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "ui 相关配置参数",
    result: "ui 相关配置参数",
    result: "ui 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用UI？
A: 描述你的界面设计需求即可，例如"设计一个SaaS产品的Dashboard侧边栏"或"创建一个电商商品卡片组件"。系统会基于设计原则输出完整的HTML/CSS代码，包含颜色令牌、间距规范和响应式布局。也可指定设计风格，如"Material Design风格"或"极简风格"。

### Q2: 如何确保设计的一致性？
A: 系统会自动使用语义化的设计令牌（Design Tokens）确保一致性。所有颜色使用CSS变量（如 `--color-primary-500`），间距遵循8px栅格系统，字体使用预定义的层级规范。多次生成同一产品时，系统会记住之前的设计决策并保持一致。

### Q3: 生成的代码是否支持深色模式？
A: 支持。在请求中说明"需要深色模式"即可。系统会生成 `prefers-color-scheme: dark` 媒体查询，并为深色模式定义对应的颜色令牌覆盖。语义色（成功/警告/危险）在深色模式下会使用更高亮度的变体以保证可读性。

### Q4: 如何处理移动端适配？
A: 系统默认采用移动优先（Mobile First）的响应式设计策略。所有组件默认针对小屏设计，通过媒体查询逐步增强大屏体验。生成的代码包含响应式断点（xs/sm/md/lg/xl），栅格布局自动适配不同屏幕宽度。可额外指定"需要触摸优化"以增大移动端点击区域。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

