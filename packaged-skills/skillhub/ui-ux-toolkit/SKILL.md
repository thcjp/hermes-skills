---
slug: "ui-ux-toolkit"
name: "ui-ux-toolkit"
version: "1.0.0"
displayName: "UI/UX设计工具箱专业版"
summary: "全域设计数据库+持久化设计系统+多技术栈+批量搜索,面向团队企业的专业UI/UX设计决策引擎"
license: "Proprietary"
edition: "pro"
description: |-
  面向设计团队和企业项目的专业级UI/UX设计决策引擎,涵盖全部10个设计域、
  10种技术栈、设计系统持久化、页面级覆盖、批量搜索等高级能力。核心能力:
  - 全部10个设计域搜索(product/style/typography/color/landing/chart/ux/react/web/prompt)
  - 10种技术栈实现指引(html-tailwind/react/nextjs/vue/svelte/swiftui/react-native/flutter/shadcn/jetpack-compose)
  - 设计系统持久化:...
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
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# UI/UX设计工具箱专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

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
| `ux` | 优秀实践与反模式 | 动画, 无障碍, z-index, 加载 |
| `react` | React/Next.js性能 | 瀑布流, 打包, Suspense, 缓存 |
| `web` | Web界面规范 | aria, focus, 键盘, 语义化 |
| `prompt` | AI提示词与CSS关键词 | (风格名称) |

**输入**: 用户提供全域设计数据库所需的指令和必要参数。
**输出**: 返回全域设计数据库的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`批量搜索与多格式输出`相关配置参数进行设置
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

**输出**: 返回全技术栈支持的执行结果,包含操作状态和输出数据。
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

**输入**: 用户提供设计系统持久化(核心高级功能)所需的指令和必要参数。
### 4. 推理规则引擎
专业版集成 `ui-reasoning.csv` 推理规则,在设计系统生成时自动应用:

```bash
# 推理引擎自动选择优秀匹配并解释原因
python3 scripts/search.py "healthcare SaaS" --design-system --persist -p "MedApp"
```

输出包含:
- 匹配的风格及选择理由
- 配色方案及适用原因
- 反模式警示(应避免的设计决策)

**输入**: 用户提供推理规则引擎所需的指令和必要参数。
### 5. 批量搜索与多格式输出

```bash
# Markdown格式输出
python3 scripts/search.py "fintech crypto" --design-system -f markdown

# 批量搜索多个域并合并结果
python3 scripts/search.py "glassmorphism" --domain style -n 5
python3 scripts/search.py "modern elegant" --domain typography -n 5
python3 scripts/search.py "fintech" --domain color -n 5
```- 验证执行结果，确认输出符合预期格式
- 参考`批量搜索与多格式输出`相关配置参数进行设置
#
## 适用场景

### 场景一:企业级多页面应用设计系统管理

一家金融科技公司需要为包含仪表盘、结算、个人中心等10+页面的Web应用建立统一设计系统。

```bash
# 第1步:生成并持久化MASTER设计系统
python3 scripts/search.py "fintech SaaS dashboard professional" \
  --design-system --persist -p "FinApp"

# 第2步:为仪表盘页面创建覆盖规则
python3 scripts/search.py "real-time data visualization dark" \
  --design-system --persist -p "FinApp" --page "dashboard"

# 第3步:为结算页面创建覆盖规则
python3 scripts/search.py "checkout payment trust security" \
  --design-system --persist -p "FinApp" --page "checkout"

# 第4步:获取React技术栈实现指引
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

## 使用流程

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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.10 及以上(推荐3.12)

### 依赖说明

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

- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。核心查询、持久化和批量搜索功能依赖Python CLI脚本执行,需确保exec工具和Python环境可用。设计系统持久化创建的文件建议纳入版本控制以保障团队协作。

## 案例展示

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

## 常见问题

### Q1: 专业版是否兼容免费版的查询语法?

完全兼容。专业版支持免费版的所有命令和参数,免费版用户可无缝升级。专业版新增 `--persist`、`--page`、`-f markdown`、`--domain react/web/chart/prompt` 等高级参数。

### Q2: MASTER和页面覆盖的优先级如何工作?

构建特定页面时:首先检查 `design-system/pages/<page>.md`。若存在,其规则**覆盖**MASTER文件中的对应规则;若不存在,则使用MASTER规则。页面覆盖文件只需定义与MASTER不同的规则。

### Q3: 如何在团队中共享设计系统?

将 `design-system/` 目录纳入版本控制(Git),团队成员克隆仓库后即可使用相同的MASTER和页面覆盖规则。每次修改设计系统后提交变更,确保全员设计决策一致。

### Q4: 推理规则引擎如何工作?

推理引擎读取 `ui-reasoning.csv` 中定义的规则,在生成设计系统时自动匹配产品类型、行业和风格关键词,选择优秀设计方案并解释选择理由,同时标注应避免的反模式。

### Q5: 支持哪些输出格式?

专业版支持纯文本(默认)和Markdown格式输出。使用 `-f markdown` 获取格式化输出,便于直接粘贴到文档或Wiki中。

### Q6: 批量搜索如何提升效率?

通过组合多个域的搜索结果,一次性获取完整的设计系统建议。例如,同时搜索style + typography + color + landing + chart五个域,获取从风格到图表的完整推荐。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

