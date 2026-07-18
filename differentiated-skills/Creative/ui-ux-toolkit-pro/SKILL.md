---
slug: ui-ux-toolkit-pro
name: ui-ux-toolkit-pro
version: "1.0.0"
displayName: UI/UX设计工具箱专业版
summary: 全域设计数据库+持久化设计系统+多技术栈+批量搜索,面向团队企业的专业UI/UX设计决策引擎
license: MIT
edition: pro
description: |-
  面向设计团队和企业项目的专业级UI/UX设计决策引擎,涵盖全部10个设计域、
  10种技术栈、设计系统持久化、页面级覆盖、批量搜索等高级能力。

  核心能力:
  - 全部10个设计域搜索(product/style/typography/color/landing/chart/ux/react/web/prompt)
  - 10种技术栈实现指引(html-tailwind/react/nextjs/vue/svelte/swiftui/react-native/flutter/shadcn/jetpack-compose)
  - 设计系统持久化:MASTER全局规则 + 页面级覆盖
  - 批量搜索与多格式输出(Markdown/JSON)
  - 层级检索与跨会话设计一致性保障
  - 推理规则引擎(ui-reasoning.csv)驱动的智能推荐

  适用场景:
  - 企业级多页面应用的设计系统管理
  - 跨技术栈团队的统一设计规范
  - 设计系统版本化与页面级定制
  - 团队协作的设计决策记录

  差异化:专业版在免费版基础上扩展全部设计域和技术栈,新增设计系统持久化、
  层级检索、批量操作和推理引擎,支持MASTER+页面覆盖模式,保障大型项目中
  设计决策的一致性与可追溯性。完全兼容免费版查询语法。

  触发关键词: 设计系统持久化, 页面级覆盖, 批量设计搜索, 多技术栈适配, MASTER设计规范, 设计令牌, 企业设计系统, 跨会话一致性, 层级检索
tags:
- 设计
- UI
- UX
- 配色
- 字体
- 前端
- 企业级
- 设计系统
- 技术栈
- 批量处理
tools:
- read
- exec
---

# UI/UX设计工具箱 - 专业版

## 概述

UI/UX设计工具箱专业版是一款面向设计团队和企业项目的专业级设计决策引擎。在免费版核心查询能力之上,扩展至全部10个设计域、10种技术栈,并引入设计系统持久化、页面级覆盖、批量搜索、推理规则引擎等高级能力。

通过MASTER全局规则与页面级覆盖的层级检索机制,专业版可保障大型多页面项目中设计决策的一致性与可追溯性,是团队协作和跨技术栈项目的理想选择。完全兼容免费版查询语法,可无缝升级。

## 核心能力

### 1. 全域设计数据库

专业版支持全部10个设计域的深度搜索:

| 域 | 用途 | 示例关键词 |
|----|------|-----------|
| `product` | 产品类型推荐 | SaaS, 电商, 作品集, 医疗, 美容, 服务 |
| `style` | UI风格与效果 | 玻璃态, 极简, 暗色模式, 粗野主义 |
| `typography` | 字体配对 | 优雅, 活泼, 专业, 现代 |
| `color` | 配色方案 | saas, ecommerce, healthcare, fintech |
| `landing` | 页面结构与CTA策略 | hero, 推荐证言, 定价, 社交证明 |
| `chart` | 图表类型与库推荐 | 趋势, 对比, 时间线, 漏斗 |
| `ux` | 最佳实践与反模式 | 动画, 无障碍, z-index, 加载 |
| `react` | React/Next.js性能 | 瀑布流, 打包, Suspense, 缓存 |
| `web` | Web界面规范 | aria, focus, 键盘, 语义化 |
| `prompt` | AI提示词与CSS关键词 | (风格名称) |

### 2. 全技术栈支持

| 技术栈 | 聚焦领域 |
|--------|----------|
| `html-tailwind` | Tailwind工具类, 响应式, 无障碍(默认) |
| `react` | 状态管理, Hooks, 性能, 模式 |
| `nextjs` | SSR, 路由, 图片, API路由 |
| `vue` | Composition API, Pinia, Vue Router |
| `svelte` | Runes, Stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | 组件, 导航, 列表 |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui组件, 主题, 表单 |
| `jetpack-compose` | Composables, Modifiers, State Hoisting |

### 3. 设计系统持久化(核心高级功能)

通过 `--persist` 标志将设计系统保存为文件,实现跨会话一致性:

```bash
# 持久化设计系统到项目目录
python3 scripts/search.py "fintech crypto dashboard" --design-system --persist -p "FinApp"

# 创建页面级覆盖
python3 scripts/search.py "fintech crypto" --design-system --persist -p "FinApp" --page "dashboard"
```

持久化创建的文件结构:

```text
design-system/
├── MASTER.md          # 全局设计规则(唯一真相源)
└── pages/
    ├── dashboard.md   # 仪表盘页面覆盖规则
    ├── checkout.md    # 结算页面覆盖规则
    └── profile.md     # 个人中心页面覆盖规则
```

**层级检索机制**:构建特定页面时,优先检查 `pages/<page>.md`。若存在,其规则覆盖MASTER文件;若不存在,则使用MASTER规则。

### 4. 推理规则引擎

专业版集成 `ui-reasoning.csv` 推理规则,在设计系统生成时自动应用:

```bash
# 推理引擎自动选择最佳匹配并解释原因
python3 scripts/search.py "healthcare SaaS" --design-system --persist -p "MedApp"
```

输出包含:
- 匹配的风格及选择理由
- 配色方案及适用原因
- 反模式警示(应避免的设计决策)

### 5. 批量搜索与多格式输出

```bash
# Markdown格式输出
python3 scripts/search.py "fintech crypto" --design-system -f markdown

# 批量搜索多个域并合并结果
python3 scripts/search.py "glassmorphism" --domain style -n 5
python3 scripts/search.py "modern elegant" --domain typography -n 5
python3 scripts/search.py "fintech" --domain color -n 5
```

## 使用场景

### 场景一:企业级多页面应用设计系统管理

一家金融科技公司需要为包含仪表盘、结算、个人中心等10+页面的Web应用建立统一设计系统。

```bash
# 步骤1:生成并持久化MASTER设计系统
python3 scripts/search.py "fintech SaaS dashboard professional" \
  --design-system --persist -p "FinApp"

# 步骤2:为仪表盘页面创建覆盖规则
python3 scripts/search.py "real-time data visualization dark" \
  --design-system --persist -p "FinApp" --page "dashboard"

# 步骤3:为结算页面创建覆盖规则
python3 scripts/search.py "checkout payment trust security" \
  --design-system --persist -p "FinApp" --page "checkout"

# 步骤4:获取React技术栈实现指引
python3 scripts/search.py "state hooks performance" --stack react
```

层级检索使用提示(提供给Agent的上下文):

```text
我正在构建 dashboard 页面。请读取 design-system/MASTER.md。
同时检查 design-system/pages/dashboard.md 是否存在。
如果页面文件存在,优先使用其规则。
如果不存在,则使用 MASTER 规则。
现在开始生成代码...
```

### 场景二:跨技术栈团队统一设计规范

团队同时维护Web(React)、iOS(SwiftUI)、Android(Jetpack Compose)三端,需要统一设计语言。

```bash
# 统一的设计系统
python3 scripts/search.py "enterprise SaaS professional" --design-system --persist -p "UnifiedApp"

# Web端实现指引
python3 scripts/search.py "component state hooks" --stack react

# iOS端实现指引
python3 scripts/search.py "views state navigation" --stack swiftui

# Android端实现指引
python3 scripts/search.py "composables modifiers state" --stack jetpack-compose
```

### 场景三:设计系统审计与反模式检测

对现有项目进行设计审计,检测常见UX问题和反模式:

```bash
# 审计无障碍和交互规则
python3 scripts/search.py "accessibility focus keyboard touch" --domain ux -n 10

# 审计性能和布局规则
python3 scripts/search.py "performance layout responsive" --domain ux -n 10

# 审计React性能反模式
python3 scripts/search.py "rerender waterfall bundle memo" --domain react -n 10
```

## 快速开始

### 环境验证

```bash
# 验证Python环境
python3 --version
# 预期: Python 3.10+

# 验证专业版功能
python3 scripts/search.py "test" --design-system --persist -p "TestProject"
ls design-system/MASTER.md
```

### 企业级设计系统五步流程

```bash
# 第1步:分析需求
# 提取:产品类型、行业、风格关键词、技术栈

# 第2步:生成并持久化MASTER设计系统
python3 scripts/search.py "beauty spa wellness elegant" \
  --design-system --persist -p "Serenity Spa"

# 第3步:创建页面级覆盖(按需)
python3 scripts/search.py "booking calendar soft" \
  --design-system --persist -p "Serenity Spa" --page "booking"

# 第4步:补充详细搜索
python3 scripts/search.py "animation accessibility" --domain ux
python3 scripts/search.py "hero testimonial pricing" --domain landing

# 第5步:获取技术栈指引
python3 scripts/search.py "layout responsive form" --stack html-tailwind
```

## 配置示例

### 企业设计系统配置

```json
{
  "project": "FinApp",
  "version": "2.0.0",
  "master_design_system": "design-system/MASTER.md",
  "page_overrides": [
    "design-system/pages/dashboard.md",
    "design-system/pages/checkout.md",
    "design-system/pages/profile.md"
  ],
  "stacks": ["react", "nextjs", "swiftui", "jetpack-compose"],
  "domains_enabled": [
    "product", "style", "typography", "color", "landing",
    "chart", "ux", "react", "web", "prompt"
  ],
  "reasoning_engine": true,
  "persistence": true,
  "batch_search": true,
  "output_formats": ["markdown", "json"]
}
```

### 页面覆盖规则示例(design-system/pages/dashboard.md)

```markdown
# Dashboard 页面设计覆盖

## 覆盖MASTER的规则

### 配色
- 背景: 深色模式(bg-slate-900)
- 主色: Cyan-400(数据高亮)
- 次要色: Slate-600(面板背景)

### 布局
- 侧边栏宽度: 240px
- 内容区域: max-w-7xl
- 卡片间距: gap-6

### 图表
- 使用 chart 域推荐的实时趋势图
- 数据密度: 中等
```

### 专业版与免费版完整对比

| 功能维度 | 免费版 | 专业版 |
|----------|--------|--------|
| 设计域数量 | 5个基础域 | 全部10个域 |
| 技术栈支持 | html-tailwind | 全部10种技术栈 |
| 设计系统持久化 | 不支持 | MASTER + 页面覆盖 |
| 推理规则引擎 | 不支持 | ui-reasoning.csv驱动 |
| 批量搜索 | 不支持 | 支持多域批量 |
| 输出格式 | 纯文本 | Markdown + JSON |
| 层级检索 | 不支持 | 页面级覆盖优先 |
| 反模式检测 | 基础UX检查 | 全域深度审计 |
| 跨会话一致性 | 不支持 | 持久化保障 |
| 适用对象 | 个人开发者 | 团队/企业 |
| 兼容性 | - | 完全兼容免费版语法 |

## 最佳实践

### 1. 始终从MASTER开始

```bash
# 正确:先生成MASTER,再创建页面覆盖
python3 scripts/search.py "enterprise SaaS" --design-system --persist -p "MyApp"
python3 scripts/search.py "data table" --design-system --persist -p "MyApp" --page "reports"

# 错误:跳过MASTER直接创建页面
python3 scripts/search.py "data table" --design-system --persist -p "MyApp" --page "reports"
```

### 2. 页面覆盖只定义差异

页面覆盖文件应只包含与MASTER不同的规则,而非完整复制:

```markdown
# Reports 页面覆盖

## 仅覆盖以下规则
### 配色
- 主色改为: Indigo-600(数据强调)

### 布局
- 移除侧边栏,使用全宽布局

## 其余规则遵循MASTER
```

### 3. 多技术栈并行查询

```bash
# 一次设计决策,多端实现指引
python3 scripts/search.py "form validation" --stack react
python3 scripts/search.py "form validation" --stack swiftui
python3 scripts/search.py "form validation" --stack flutter
```

### 4. 交付前质量检查矩阵

| 检查维度 | 命令 | 通过标准 |
|----------|------|----------|
| 无障碍 | `--domain ux "accessibility"` | WCAG 2.2 AA合规 |
| 交互 | `--domain ux "touch interaction"` | 44x44px最小触摸区 |
| 性能 | `--domain ux "performance"` | WebP/懒加载/动画优化 |
| 布局 | `--domain ux "layout responsive"` | 375/768/1024/1440px适配 |
| 对比度 | `--domain color` | 4.5:1文字/3:1UI组件 |
| React性能 | `--domain react` | 无重渲染/瀑布流问题 |

## 常见问题

### Q1: 专业版是否兼容免费版的查询语法?

完全兼容。专业版支持免费版的所有命令和参数,免费版用户可无缝升级。专业版新增 `--persist`、`--page`、`-f markdown`、`--domain react/web/chart/prompt` 等高级参数。

### Q2: MASTER和页面覆盖的优先级如何工作?

构建特定页面时:首先检查 `design-system/pages/<page>.md`。若存在,其规则**覆盖**MASTER文件中的对应规则;若不存在,则使用MASTER规则。页面覆盖文件只需定义与MASTER不同的规则。

### Q3: 如何在团队中共享设计系统?

将 `design-system/` 目录纳入版本控制(Git),团队成员克隆仓库后即可使用相同的MASTER和页面覆盖规则。每次修改设计系统后提交变更,确保全员设计决策一致。

### Q4: 推理规则引擎如何工作?

推理引擎读取 `ui-reasoning.csv` 中定义的规则,在生成设计系统时自动匹配产品类型、行业和风格关键词,选择最佳设计方案并解释选择理由,同时标注应避免的反模式。

### Q5: 支持哪些输出格式?

专业版支持纯文本(默认)和Markdown格式输出。使用 `-f markdown` 获取格式化输出,便于直接粘贴到文档或Wiki中。

### Q6: 批量搜索如何提升效率?

通过组合多个域的搜索结果,一次性获取完整的设计系统建议。例如,同时搜索style + typography + color + landing + chart五个域,获取从风格到图表的完整推荐。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.10 及以上(推荐3.12)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3 | 运行时 | 必需 | 系统包管理器安装 |
| CSV数据文件 | 数据 | 必需 | 随Skill包内置 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Git | 版本控制 | 推荐 | 用于设计系统版本管理 |

Python安装命令:

```bash
# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip

# Windows
winget install Python.Python.3.12
```

### API Key 配置

本Skill的CLI搜索工具基于本地数据文件运行,无需额外API Key。设计建议的生成由Agent内置LLM驱动。推理规则引擎读取本地CSV文件,不依赖外部API。

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。核心查询、持久化和批量搜索功能依赖Python CLI脚本执行,需确保exec工具和Python环境可用。设计系统持久化创建的文件建议纳入版本控制以保障团队协作。
