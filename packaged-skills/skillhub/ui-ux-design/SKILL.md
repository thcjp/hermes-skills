---
slug: "ui-ux-design"
name: "ui-ux-design"
version: 1.0.1
displayName: "UI/UX设计指南"
summary: "涵盖设计原则、配色系统、Shadcn/ui+Tailwind栈、响应式设计与WCAG 2.2无障碍的完整指南。"
license: "Proprietary"
description: |-
  现代UI/UX设计原则、模式与最佳实践指南.
  涵盖Mobile-First响应式设计、配色系统、排版、WCAG 2.2无障碍.
  包含Shadcn/ui + Tailwind CSS技术栈集成与微交互设计.
  适用于Web与移动应用的界面设计、布局选择与设计审查.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 创意设计
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# UI/UX设计指南

涵盖设计原则、配色系统、Shadcn/ui+Tailwind栈、响应式设计与WCAG 2.2无障碍的完整指南.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | UI/UX设计指南处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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
三大基础设计原则指导所有UI决策：

**1. Mobile-First Always（移动优先）**
- 从320px宽度（最小手机）开始设计
- 断点：576px（手机）、768px（平板）、992px（笔记本）、1200px（桌面）
- 默认单列布局，空间允许时再扩展

**2. Visual Hierarchy（视觉层次）**
- **Size（大小）**：越大越重要
- **Color（颜色）**：明亮/对比色吸引注意
- **Whitespace（留白）**：更多空间=更强调
- **Proximity（ proximity）**：相关项分组
- **Contrast（对比）**：深底浅字或浅底深字（文本最低4.5:1）

**3. Whitespace is Your Weapon（留白即武器）**
- 元素间距使用8px倍数（8, 16, 24, 32, 48, 64）
- 区块间最小留白：48-64px
- 卡片内边距：24-32px

**输入**: 用户提供核心设计原则（Core Design Principles）所需的指令和必要参数.
**处理**: 解析核心设计原则（Core Design Principles）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回核心设计原则（Core Design Principles）的处理结果,包含执行状态码、结果数据和执行日志。### 配色系统（Color System）
构建完整的主色阶（50-900）：

- **Primary（主色）**：品牌色（CTA、链接、激活状态）
- **Neutrals（中性色）**：灰色50-900（文本、背景、边框）
- **Semantic（语义色）**：Success（绿色）、Error（红色）、Warning（黄色/橙色）

工具推荐：Huevy.app、Coolors.co、Adobe Color

**输入**: 用户提供配色系统（Color System）所需的指令和必要参数.
**处理**: 解析配色系统（Color System）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回配色系统（Color System）的处理结果,包含执行状态码、结果数据和执行日志。### 排版系统（Typography Scale）
基于8px基线的排版尺度：

```text
text-xs:   12px / 16px line-height
text-sm:   14px / 20px
text-base: 16px / 24px (body default)
text-lg:   18px / 28px
text-xl:   20px / 28px
text-2xl:  24px / 32px
text-3xl:  30px / 36px (section headers)
text-4xl:  36px / 40px
text-5xl:  48px / 1 (hero titles)
```

字体配对：最多2种字体（UI用无衬线，标题可选衬线）

**输入**: 用户提供排版系统（Typography Scale）所需的指令和必要参数.
**处理**: 解析排版系统（Typography Scale）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回排版系统（Typography Scale）的处理结果,包含执行状态码、结果数据和执行日志。### Shadcn/ui + Tailwind CSS技术栈
完整的Shadcn/ui + Tailwind项目搭建与组件管理：

**项目初始化（Next.js）：**

```bash
npx create-next-app@latest project-name --typescript --tailwind --app
cd project-name
npx shadcn@latest init
```

选择：Style（Default）、Base color（Blue或自定义）、CSS variables（Yes）

**添加组件：**

```bash
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
npx shadcn@latest add calendar
```

组件出现在 `components/ui/`，你拥有代码所有权，可自由定制.
**Tailwind最佳实践：**
- 使用设计令牌（非任意值）：`p-4` 而非 `p-[17px]`
- 响应式工具类：`w-full md:w-1/2 lg:w-1/3`
- 暗色模式：`dark:bg-gray-900 dark:text-white`

**输入**: 用户提供Shadcn/ui + Tailwind CSS技术栈所需的指令和必要参数.
**处理**: 解析Shadcn/ui + Tailwind CSS技术栈的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 响应式设计（Responsive Design）
Mobile-First响应式布局模式：

- **CSS Grid**：2D布局（页面结构）
- **Flexbox**：1D布局（组件内部）
- **Auto-fit grid**：`repeat(auto-fit, minmax(280px, 1fr))`（无需媒体查询）

布局模式：
```css
/* 响应式网格 - 自动适应 */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }
```

**输入**: 用户提供响应式设计（Responsive Design）所需的指令和必要参数.
**处理**: 解析响应式设计（Responsive Design）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回响应式设计（Responsive Design）的处理结果,包含执行状态码、结果数据和执行日志。### 微交互设计（Micro-Interactions）
提升用户体验的微交互模式：

- **Hover（悬停）**：放大1.05x（按钮可点击感）
- **Click（点击）**：缩小0.95x（触觉反馈）
- **Duration（时长）**：0.2-0.3s（保持微妙）
- **Animate only（仅动画）**：`transform` 和 `opacity`（GPU加速）

**处理**: 解析微交互设计（Micro-Interactions）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回微交互设计（Micro-Interactions）的处理结果,包含执行状态码、结果数据和执行日志。### 无障碍设计（Accessibility - WCAG 2.2）
WCAG 2.2无障碍标准合规：

- **文本对比度**：最低4.5:1（正常文本），3:1（大文本）
- **UI组件**：最低3:1对比度
- **键盘导航**：Tab顺序合理，焦点状态可见（3:1对比度）
- **ARIA标签**：为按钮、图片、交互元素始终提供

**处理**: 解析无障碍设计（Accessibility - WCAG 2.2）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回无障碍设计（Accessibility - WCAG 2.2）的处理结果,包含执行状态码、结果数据和执行日志。### UI设计五法则（The 5 Laws of Beautiful UI）
1. **Contrast creates hierarchy**（对比创造层次）- 大vs小，深vs浅
2. **Whitespace creates calm**（留白创造宁静）- 不要害怕空白
3. **Consistency builds trust**（一致性建立信任）- 重复相同模式
4. **Feedback confirms action**（反馈确认操作）- 动画、成功消息
5. **Accessibility includes everyone**（无障碍包容所有人）- 对比度、键盘、屏幕阅读器

**输入**: 用户提供UI设计五法则（The 5 Laws of Beautiful UI）所需的指令和必要参数.
**处理**: 解析UI设计五法则（The 5 Laws of Beautiful UI）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 快速参考与构建前检查清单（Quick Reference & Pre-Build Checklist）
编码前需确认的检查清单：

- 配色方案已定义（主色+中性色+语义色）
- 排版尺度已选择（6-8种尺寸）
- 组件库已选定（Shadcn + Tailwind）
- 移动端断点已规划（576px, 768px, 992px）
- 无障碍对比度已检查（4.5:1文本，3:1 UI）
- 微交互列表已列出（悬停、点击、成功状态）
- 网格布局已草图（移动→桌面渐进）

**灵感来源：**
- Linear (linear.app) — 最佳键盘优先UI，微妙动画
- Stripe Dashboard — 干净数据可视化，完美间距
- Vercel — 极简，快速，现代渐变
- Notion — 直观拖放，清晰层次

**输入**: 用户提供快速参考与构建前检查清单（Quick Reference & Pre-Build Checklist）所需的指令和必要参数.
**输出**: 返回快速参考与构建前检查清单（Quick Reference & Pre-Build Checklist）的处理结果,包含执行状态码、结果数据和执行日志.
### Size（大小）

针对Size（大小）,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Size（大小）相关的配置参数、输入数据和处理选项.
**输出**: 返回Size（大小）的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Size（大小）`的配置文档进行参数调优
### Color（颜色）

针对Color（颜色）,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Color（颜色）相关的配置参数、输入数据和处理选项.
**输出**: 返回Color（颜色）的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Color（颜色）`的配置文档进行参数调优
#
## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 确定设计需求：界面设计、配色选择、排版、响应式、无障碍等
3. 参考核心设计原则与五法则指导设计决策
4. 如需项目搭建，使用Shadcn/ui + Tailwind初始化命令
5. 使用快速参考中的尺度与模式生成代码
6. 使用构建前检查清单验证设计完整性

#
## 示例

### 示例1：搭建Shadcn/ui + Tailwind项目

```
用户: 帮我搭建一个Shadcn/ui + Tailwind的Next.js项目
# ...
Agent: 执行以下命令：
1. npx create-next-app@latest my-app --typescript --tailwind --app
2. cd my-app
3. npx shadcn@latest init
4. npx shadcn@latest add button card dialog
# ...
- 组件位于 components/ui/
- 使用CSS变量主题
- 支持暗色模式
```

### 示例2：设计响应式卡片网格

```
用户: 设计一个响应式卡片网格，移动端单列，桌面三列
# ...
Agent: 使用auto-fit grid模式：
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
- 无需媒体查询
- 280px以下自动单列
- 自动适应可用空间
```

### 示例3：无障碍配色检查

```
用户: 我的按钮用#999灰底白字，符合WCAG吗？
# ...
Agent: 对比度检查：
- 背景 #999999 (L: 0.358)
- 文字 #FFFFFF (L: 1.000)
- 对比度: 2.79:1
- 结果: ❌ 不符合WCAG 2.2
- 正常文本要求 4.5:1，大文本要求 3:1
- 建议：使用 #6B7280 (gray-500) 作为背景，对比度 4.83:1 ✅
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| Shadcn初始化失败 | Node.js版本过低 | 升级Node.js至18+；检查package.json兼容性 |
| Tailwind类不生效 | CSS配置错误 | 检查tailwind.config.js的content路径；确认CSS导入了tailwind指令 |
| 对比度不达标 | 配色选择不当 | 使用WebAIM Contrast Checker验证；调整颜色深度至4.5:1以上 |
| 响应式布局错乱 | 断点使用不当 | 确认使用Mobile-First顺序；检查Tailwind响应式前缀顺序 |
| 组件样式不一致 | 设计令牌未使用 | 避免任意值如 `p-[17px]`；使用标准令牌如 `p-4` |
| 暗色模式不生效 | dark类未配置 | 在tailwind.config.js中配置 `darkMode: 'class'`；添加dark:前缀类 |

## 常见问题

### Q1: Mobile-First设计的原则是什么？
A: 从最小屏幕（320px）开始设计，默认单列布局。使用断点（576px、768px、992px、1200px）逐步扩展。Tailwind中响应式前缀按从小到大顺序应用：`w-full md:w-1/2 lg:w-1/3`.
### Q2: 如何选择配色方案？
A: 构建主色阶（50-900）：Primary为品牌色（CTA、链接），Neutrals为灰色系（文本、背景），Semantic为语义色（成功绿、错误红、警告黄）。使用Coolors.co或Huevy.app生成调色板.
### Q3: WCAG 2.2无障碍有哪些关键要求？
A: 文本对比度最低4.5:1（正常文本）或3:1（大文本）；UI组件最低3:1对比度；键盘导航Tab顺序合理且焦点可见；为交互元素提供ARIA标签.
### Q4: Shadcn/ui与其他组件库有什么区别？
A: Shadcn/ui将组件代码直接复制到你的项目中（components/ui/），你拥有完全所有权与定制权。不像MUI/Antd通过npm包引用，Shadcn让你自由修改任何组件代码.
### Q5: 微交互应该使用哪些CSS属性？
A: 仅动画 `transform`（translate、scale、rotate）和 `opacity`，这两个属性GPU加速，性能最优。避免动画width、height、margin等触发重排的属性。时长保持0.2-0.3s.
### Q6: 如何确保设计的一致性？
A: 使用设计令牌（design tokens）而非任意值；定义统一的排版尺度（6-8种尺寸）；保持间距使用8px倍数；重复使用相同的组件模式；参考Linear、Stripe等优秀产品的设计规范.
## 已知限制

- Shadcn/ui + Tailwind项目搭建需要Node.js环境
- 配色对比度检查需要手动使用WebAIM等工具验证
- 设计指导为文本描述，无法直接生成视觉设计稿
- 微交互的动画效果需在实际代码中验证
- WCAG合规检查覆盖常见项，完整审计需专业工具
- 灵感参考的产品设计可能随时间变化

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "UI/UX设计指南处理结果",
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
