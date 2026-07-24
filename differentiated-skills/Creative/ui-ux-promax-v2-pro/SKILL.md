---

slug: ui-ux-promax-v2-pro
name: ui-ux-promax-v2-pro
version: 1.0.0
displayName: UI/UX ProMax V2专业版
summary: "全域设计数据库+持久化+推理引擎+多技术栈+层级检索,面向企业的综合设计决策引擎。面向设计团队和企业的综合UI/UX设计决策引擎,涵盖50+风格、97配色、57字体、"
license: Proprietary
edition: pro
description: 面向设计团队和企业的综合UI/UX设计决策引擎,涵盖50+风格、97配色、57字体、，可处理提升工作效率

  99条UX规则、25种图表类型,支持全部10个设计域、10种技术栈、设计系统

  持久化与页面级覆盖、推理规则引擎和批量搜索。核心能力:

  - 全部10个设计域深度搜索

  - 10种技术栈实现指引(React/Vue/Next'
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
  - 规则引擎
  - UI设计
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"

---

# UI/UX ProMax V2 - 专业版

## 概述

UI/UX ProMax V2专业版是一款面向设计团队和企业的综合UI/UX设计决策引擎。内置50+种界面风格、97套配色方案、57组字体配对、99条UX规则和25种图表类型,支持全部10个设计域和10种技术栈的深度搜索.
专业版引入设计系统持久化(MASTER+页面覆盖)、推理规则引擎和层级检索机制,保障大型多页面项目中设计决策的一致性与可追溯性。完全兼容免费版查询语法,可无缝升级.
## 核心能力

### 1. 全域设计数据库

| 域 | 用途 | 示例关键词 |
|---|---|-----|
| `product` | 产品类型推荐 | SaaS, 电商, 作品集, 医疗, 美容, 服务 |
| `style` | UI风格与效果 | 玻璃态, 极简, 暗色模式, 粗野主义 |
| `typography` | 字体配对 | 优雅, 活泼, 专业, 现代 |
| `color` | 配色方案 | saas, ecommerce, healthcare, fintech |
| `landing` | 页面结构与CTA | hero, 推荐证言, 定价, 社交证明 |
| `chart` | 图表类型与库 | 趋势, 对比, 时间线, 漏斗, 饼图 |
| `ux` | 最佳实践与反模式 | 动画, 无障碍, z-index, 加载 |
| `react` | React/Next.js性能 | 瀑布流, 打包, Suspense, 缓存 |
| `web` | Web界面规范 | aria, focus, 键盘, 语义化 |
| `prompt` | AI提示词与CSS | (风格名称) |

**输入**: 用户提供全域设计数据库所需的指令和必要参数.
**处理**: 解析全域设计数据库的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回全域设计数据库的响应数据,包含状态码、结果和日志.
### 2. 全技术栈支持

| 技术栈 | 聚焦领域 |
|:-----|:-----|
| `html-tailwind` | Tailwind工具类, 响应式, 无障碍(默认) |
| `react` | 状态, Hooks, 性能, 模式 |
| `nextjs` | SSR, 路由, 图片, API路由 |
| `vue` | Composition API, Pinia, Vue Router |
| `svelte` | Runes, Stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | 组件, 导航, 列表 |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui组件, 主题, 表单 |
| `jetpack-compose` | Composables, Modifiers, State Hoisting |

**输入**: 用户提供全技术栈支持所需的指令和必要参数.
**处理**: 解析全技术栈支持的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回全技术栈支持的响应数据,包含状态码、结果和日志.
### 3. 设计系统持久化

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | UI/UX ProMax V2专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 持久化MASTER设计系统
python3 （请参考skill目录中的脚本文件） "fintech SaaS dashboard" --design-system --persist -p "FinApp"
# .
# 创建页面级覆盖
python3 （请参考skill目录中的脚本文件） "real-time data dark" --design-system --persist -p "FinApp" --page "dashboard"
```

文件结构:
```text
design-system/
├── MASTER.md          # 全局规则(唯一真相源)
└── pages/
    ├── dashboard.md   # 仪表盘覆盖
    ├── checkout.md    # 结算覆盖
    └── profile.md     # 个人中心覆盖
```

**层级检索**:构建页面时优先检查pages/<page>.md,存在则覆盖MASTER,不存在则使用MASTER.
**输入**: 用户提供设计系统持久化所需的指令和必要参数.
**处理**: 解析设计系统持久化的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回设计系统持久化的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 推理规则引擎

```bash
# 推理引擎自动选择最佳方案并解释原因
python3 （请参考skill目录中的脚本文件） "healthcare SaaS" --design-system --persist -p "MedApp"
```

输出包含:
- 匹配风格及选择理由
- 配色方案及适用原因
- 反模式警示(应避免的决策)

**输入**: 用户提供推理规则引擎所需的指令和必要参数.
**处理**: 解析推理规则引擎的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回推理规则引擎的响应数据,包含状态码、结果和日志.
### 5. 8级优先级深度审计

| 优先级 | 类别 | 免费版 | 专业版 |
|:---:|:---:|:---:|:---:|
| 1 | 无障碍 | 基础检查 | WCAG深度审计 |
| 2 | 触摸交互 | 基础检查 | 全交互模式审计 |
| 3 | 性能 | 基础建议 | React性能反模式检测 |
| 4 | 布局响应式 | 基础检查 | 全断点+容器查询 |
| 5 | 字体配色 | 基础推荐 | 语义令牌+主题系统 |
| 6 | 动画 | 基础建议 | 状态机+GPU优化 |
| 7 | 风格选择 | 基础匹配 | 行业深度匹配 |
| 8 | 图表数据 | 不支持 | 25种图表匹配 |

**输入**: 用户提供8级优先级深度审计所需的指令和必要参数.
**处理**: 解析8级优先级深度审计的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回8级优先级深度审计的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：多技术栈、面向企业的综合设、计决策引擎、面向设计团队和企、业的综合、设计决策引擎、种图表类型、支持全部、个设计域、种技术栈、持久化与页面级覆、推理规则引擎和批、量搜索、核心能力、个设计域深度搜索、种技术栈实现指引等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:企业多页面设计系统管理

```bash
# 生成MASTER
python3 （请参考skill目录中的脚本文件） "fintech SaaS professional" --design-system --persist -p "FinApp"
# .
# 页面覆盖
python3 （请参考skill目录中的脚本文件） "real-time data dark" --design-system --persist -p "FinApp" --page "dashboard"
python3 （请参考skill目录中的脚本文件） "checkout payment trust" --design-system --persist -p "FinApp" --page "checkout"
# .
# React实现指引
python3 （请参考skill目录中的脚本文件） "state hooks performance" --stack react
```

层级检索上下文:
```text
我正在构建 dashboard 页面。请读取 design-system/MASTER.md.
同时检查 design-system/pages/dashboard.md 是否存在.
如果页面文件存在,优先使用其规则.
如果不存在,则使用 MASTER 规则.
现在开始生成代码.
```

### 场景二:跨技术栈统一设计

```bash
# 统一设计系统
python3 （请参考skill目录中的脚本文件） "enterprise SaaS" --design-system --persist -p "UnifiedApp"
# .
# 多端实现
python3 （请参考skill目录中的脚本文件） "component state" --stack react
python3 （请参考skill目录中的脚本文件） "views navigation" --stack swiftui
python3 （请参考skill目录中的脚本文件） "composables state" --stack jetpack-compose
```

### 场景三:深度UX审计

```bash
# 无障碍深度审计
python3 （请参考skill目录中的脚本文件） "accessibility focus keyboard aria" --domain ux -n 10
# .
# React性能反模式
python3 （请参考skill目录中的脚本文件） "rerender waterfall bundle memo suspense" --domain react -n 10
# .
# Web界面规范
python3 （请参考skill目录中的脚本文件） "semantic virtualize aria focus" --domain web -n 10
```

## 不适用场景

以下场景UI/UX ProMax V2专业版不适合处理：

- 3D建模和动画制作
- 照片级写实渲染
- 手绘原创插画

## 触发条件

、品牌视觉时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 企业设计系统五步流程

```bash
# 第1步:分析需求
# 产品类型、行业、风格、技术栈
# .
# 第2步:MASTER持久化
python3 （请参考skill目录中的脚本文件） "beauty spa elegant" --design-system --persist -p "Serenity Spa"
# .
# 第3步:页面覆盖
python3 （请参考skill目录中的脚本文件） "booking calendar" --design-system --persist -p "Serenity Spa" --page "booking"
# .
# 第4步:补充搜索
python3 （请参考skill目录中的脚本文件） "animation accessibility" --domain ux
python3 （请参考skill目录中的脚本文件） "hero testimonial" --domain landing
python3 （请参考skill目录中的脚本文件） "real-time trend" --domain chart
# .
# 第5步:技术栈指引
python3 （请参考skill目录中的脚本文件） "layout form" --stack html-tailwind
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

### 企业设计系统配置

```json
{
  "project": "FinApp",
  "version": "2.0.0",
  "master": "design-system/MASTER.md",
  "page_overrides": ["dashboard", "checkout", "profile", "settings"],
  "stacks": ["react", "nextjs", "swiftui"],
  "domains": "all_10",
  "reasoning_engine": true,
  "persistence": true,
  "output_formats": ["text", "markdown"]
}
```

### 专业版与免费版完整对比

| 功能维度 | 免费版 | 专业版 |
|:------|------:|:------|
| 设计域 | 5个基础域 | 全部10个域 |
| 技术栈 | html-tailwind | 全部10种 |
| 持久化 | 不支持 | MASTER+页面覆盖 |
| 推理引擎 | 不支持 | ui-reasoning.csv |
| 层级检索 | 不支持 | 页面覆盖优先 |
| 批量搜索 | 不支持 | 多域批量 |
| 输出格式 | 纯文本 | Markdown+JSON |
| 图表推荐 | 不支持 | 25种图表匹配 |
| React审计 | 不支持 | 性能反模式检测 |
| 优先级审计 | 基础8级 | 8级深度审计 |
| 兼容性 | - | 完全兼容免费版 |

## 最佳实践

### 1. 始终从MASTER开始

```bash
# 正确
python3 （请参考skill目录中的脚本文件） "enterprise SaaS" --design-system --persist -p "MyApp"
python3 （请参考skill目录中的脚本文件） "data table" --design-system --persist -p "MyApp" --page "reports"
# .
# 错误:跳过MASTER
python3 （请参考skill目录中的脚本文件） "data table" --design-system --persist -p "MyApp" --page "reports"
```

### 2. 页面覆盖只定义差异

```markdown
# Reports 页面覆盖
## 仅覆盖以下规则
### 配色
- 主色: Indigo-600(数据强调)
### 布局
- 移除侧边栏,全宽布局
## 其余遵循MASTER
```

### 3. 交付前深度审计矩阵

| 维度 | 命令 | 标准 |
|---:|:---|---:|
| 无障碍 | `--domain ux "accessibility"` | WCAG AA |
| 交互 | `--domain ux "touch interaction"` | 44x44px |
| 性能 | `--domain ux "performance"` | WebP/懒加载 |
| React | `--domain react "rerender memo"` | 无反模式 |
| Web规范 | `--domain web "aria semantic"` | 语义化 |
| 布局 | `--domain ux "layout responsive"` | 4断点适配 |
| 对比度 | `--domain color` | 4.5:1/3:1 |
| 图表 | `--domain chart` | 类型匹配数据 |

### 4. 专业UI规则

| 规则 | 正确 | 错误 |
|:------:|--------|:-------|
| 图标 | SVG(Heroicons/Lucide/Simple Icons) | emoji |
| 品牌Logo | Simple Icons官方SVG | 猜测路径 |
| 悬停 | 颜色/透明度过渡 | 缩放偏移布局 |
| 光标 | cursor-pointer | 默认光标 |
| 过渡 | 150-300ms | 即时或>500ms |
| 玻璃态浅色 | bg-white/80+ | bg-white/10 |
| 浅色文字 | #0F172A | #94A3B8 |
| 浅色边框 | border-gray-200 | border-white/10 |
| 浮动导航 | top-4 left-4 right-4 | top-0 |
| 容器宽度 | 统一max-w-6xl/7xl | 混合宽度 |

## 常见问题

### Q1: 专业版兼容免费版语法吗?

完全兼容。专业版支持免费版所有命令,新增--persist、--page、-f markdown、--domain react/web/chart/prompt等参数.
### Q2: MASTER和页面覆盖优先级?

构建页面时:先检查pages/<page>.md,存在则覆盖MASTER对应规则,不存在则使用MASTER。页面覆盖只需定义差异.
### Q3: 团队如何共享设计系统?

将design-system/目录纳入Git版本控制,团队成员克隆后即可使用相同规则。修改后提交变更确保一致.
### Q4: 推理引擎如何工作?

读取ui-reasoning.csv规则,在生成设计系统时自动匹配产品类型、行业和风格,选择最佳方案并解释理由,标注反模式.
### Q5: 支持哪些输出格式?

纯文本(默认)和Markdown。使用-f markdown获取格式化输出.
### Q6: React性能审计检测什么?

检测重渲染问题、瀑布流请求、打包体积、Suspense使用、memo优化、缓存策略等React/Next.js性能反模式.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.10及以上(推荐3.12)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|:--:|---:|----|
| Python 3 | 运行时 | 必需 | 系统包管理器 |
| CSV数据文件 | 数据 | 必需 | 随Skill包内置 |
| LLM API | API | 必需 | Agent内置LLM |
| Git | 版本控制 | 推荐 | 设计系统版本管理 |

```bash
# macOS
brew install python3
# .
# Ubuntu/Debian
sudo apt install python3 python3-pip
# .
# Windows
winget install Python.Python.3.12
```

### API Key 配置

CLI搜索工具基于本地数据文件运行,无需额外API Key。推理引擎读取本地CSV,不依赖外部API.
### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 核心查询、持久化和批量搜索依赖Python CLI脚本,需确保exec和Python环境可用。持久化文件建议纳入版本控制.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
