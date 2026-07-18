---
slug: ui-ux-toolkit-free
name: ui-ux-toolkit-free
version: "1.0.0"
displayName: UI/UX设计工具箱免费版
summary: 可搜索的UI/UX设计数据库,提供风格、配色、字体、UX规则的基础查询,适合个人开发者快速生成设计系统
license: MIT
edition: free
description: |-
  面向个人开发者的轻量级UI/UX设计查询工具,内置丰富的设计资源数据库,
  通过自然语言关键词即可获取专业设计建议。

  核心能力:
  - 可搜索的设计资源数据库(风格、配色、字体、UX规则)
  - 自然语言驱动的CLI查询工具
  - 基础设计系统一键生成
  - 多技术栈适配指引

  适用场景:
  - 个人项目快速搭建界面设计系统
  - 独立开发者选择配色方案和字体组合
  - 小型SaaS或落地页的UI风格决策

  差异化:免费版聚焦核心查询能力,提供基础设计域搜索和默认技术栈指引,
  去除企业级持久化和批量操作功能,降低使用门槛,适合个人快速上手。

  触发关键词: 设计系统, 配色方案, 字体配对, UX规则, UI风格, 落地页设计, 响应式布局
tags:
- 设计
- UI
- UX
- 配色
- 字体
- 前端
tools:
- read
- exec
---

# UI/UX设计工具箱 - 免费版

## 概述

UI/UX设计工具箱免费版是一款面向个人开发者的轻量级设计资源查询工具。内置涵盖50+种界面风格、97套配色方案、57组字体配对、99条UX规则的设计数据库,通过Python CLI工具以自然语言关键词驱动查询,帮助开发者在数秒内获取专业设计建议。

免费版聚焦核心查询能力,支持基础设计域搜索(style、color、typography、ux)和默认技术栈(html-tailwind)指引,适合个人项目快速搭建设计系统。

## 核心能力

### 1. 设计资源数据库查询

通过关键词搜索多维度设计资源,获取匹配的风格、配色、字体推荐:

```bash
# 按产品类型和行业搜索设计系统
python3 scripts/search.py "SaaS dashboard fintech" --design-system

# 按特定域搜索
python3 scripts/search.py "glassmorphism dark" --domain style
python3 scripts/search.py "elegant luxury" --domain typography
```

### 2. 规则优先级体系

设计规则按优先级分层,确保关键问题优先处理:

| 优先级 | 类别 | 影响等级 | 所属域 |
|--------|------|----------|--------|
| 1 | 无障碍设计 | 关键 | ux |
| 2 | 触摸与交互 | 关键 | ux |
| 3 | 性能优化 | 高 | ux |
| 4 | 布局与响应式 | 高 | ux |
| 5 | 字体与配色 | 中 | typography, color |
| 6 | 动画效果 | 中 | ux |
| 7 | 风格选择 | 中 | style |
| 8 | 图表与数据 | 低 | chart |

### 3. 基础设计域支持

| 域 | 用途 | 示例关键词 |
|----|------|-----------|
| `product` | 产品类型推荐 | SaaS, 电商, 作品集, 医疗 |
| `style` | UI风格与效果 | 玻璃态, 极简, 暗色模式 |
| `typography` | 字体配对 | 优雅, 活泼, 专业, 现代 |
| `color` | 配色方案 | saas, ecommerce, healthcare |
| `ux` | 最佳实践与反模式 | 动画, 无障碍, z-index |

### 4. 默认技术栈指引

免费版默认提供 `html-tailwind` 技术栈的实现指南:

```bash
# 获取Tailwind CSS实现建议
python3 scripts/search.py "layout responsive form" --stack html-tailwind
```

## 使用场景

### 场景一:个人SaaS项目配色选择

独立开发者正在构建一款任务管理SaaS,需要快速确定配色和字体方案。

```bash
# 步骤1:生成基础设计系统
python3 scripts/search.py "SaaS productivity tool minimal" --design-system -p "TaskFlow"

# 步骤2:补充字体搜索
python3 scripts/search.py "modern clean sans-serif" --domain typography

# 步骤3:获取Tailwind实现指引
python3 scripts/search.py "dashboard card layout" --stack html-tailwind
```

输出示例(配色方案):
```text
主色: Blue-600 (#2563EB)
辅助色: Slate-500 (#64748B)
强调色: Cyan-400 (#22D3EE)
背景色: White / Slate-50
文字色: Slate-900 / Slate-600
```

### 场景二:落地页设计风格决策

为一个新的播客平台设计落地页,需要确定视觉风格。

```bash
# 搜索适合播客/媒体类产品的风格
python3 scripts/search.py "podcast media creative bold" --domain style

# 搜索落地页结构建议
python3 scripts/search.py "hero testimonial pricing" --domain landing
```

### 场景三:UX规则自查

开发完成后,对照UX规则清单检查常见问题:

```bash
# 检查动画和无障碍相关规则
python3 scripts/search.py "animation accessibility" --domain ux

# 检查布局和响应式规则
python3 scripts/search.py "responsive viewport" --domain ux
```

## 快速开始

### 安装与验证

```bash
# 验证Python环境
python3 --version
# 预期输出: Python 3.10+

# 验证搜索工具可用
python3 scripts/search.py "minimal" --domain style -n 3
```

### 三步生成设计系统

```bash
# 第1步:分析需求并搜索
python3 scripts/search.py "beauty spa wellness elegant" --design-system -p "Serenity Spa"

# 第2步:补充详细搜索
python3 scripts/search.py "elegant luxury serif" --domain typography
python3 scripts/search.py "soft pastel" --domain color

# 第3步:获取技术栈指引
python3 scripts/search.py "layout responsive" --stack html-tailwind
```

## 配置示例

### 项目设计配置文件

在项目根目录创建 `design-config.json` 管理设计决策:

```json
{
  "project_name": "TaskFlow",
  "product_type": "SaaS",
  "industry": "productivity",
  "style": "minimal",
  "color_palette": {
    "primary": "#2563EB",
    "secondary": "#64748B",
    "accent": "#22D3EE",
    "background": "#FFFFFF",
    "text": "#0F172A"
  },
  "typography": {
    "heading": "Inter",
    "body": "Inter",
    "mono": "JetBrains Mono"
  },
  "stack": "html-tailwind"
}
```

### 免费版与专业版功能对比

| 功能项 | 免费版 | 专业版 |
|--------|--------|--------|
| 基础设计域搜索 | 5个(product/style/typography/color/ux) | 全部10个域 |
| 技术栈支持 | html-tailwind(默认) | 全部10种技术栈 |
| 设计系统生成 | 基础推荐 | 完整系统+推理规则 |
| 设计系统持久化 | 不支持 | MASTER+页面覆盖 |
| 批量搜索 | 不支持 | 支持 |
| 输出格式 | 纯文本 | Markdown+JSON |
| 适用对象 | 个人开发者 | 团队/企业 |

## 最佳实践

### 1. 关键词越具体,结果越精准

```bash
# 不推荐:过于宽泛
python3 scripts/search.py "app" --design-system

# 推荐:具体到产品类型和行业
python3 scripts/search.py "healthcare SaaS dashboard minimal" --design-system
```

### 2. 多域组合搜索构建完整系统

```bash
# 风格 + 字体 + 配色 = 完整设计系统
python3 scripts/search.py "glassmorphism" --domain style
python3 scripts/search.py "modern sans-serif" --domain typography
python3 scripts/search.py "fintech" --domain color
```

### 3. 始终检查UX规则

```bash
# 开发完成后必查
python3 scripts/search.py "accessibility focus keyboard" --domain ux
python3 scripts/search.py "animation performance" --domain ux
```

### 4. 专业UI质量检查清单

| 检查项 | 正确做法 | 错误做法 |
|--------|----------|----------|
| 图标使用 | SVG图标(Heroicons/Lucide) | 使用emoji作为UI图标 |
| 悬停状态 | 颜色/透明度过渡 | 缩放变换导致布局偏移 |
| 光标样式 | 可点击元素添加cursor-pointer | 保留默认光标 |
| 过渡时长 | 150-300ms | 即时变化或超过500ms |
| 文字对比度 | 4.5:1最低对比比 | 使用低对比度灰色 |

## 常见问题

### Q1: 免费版支持哪些技术栈?

免费版默认提供 `html-tailwind`(Tailwind CSS)技术栈的实现指引。如需React、Vue、Next.js、Svelte、SwiftUI、Flutter等更多技术栈支持,请升级至专业版。

### Q2: 搜索结果不相关怎么办?

尝试更换关键词组合。例如,将"app"替换为"healthcare SaaS dashboard",具体的产品类型、行业和风格关键词能显著提升匹配精度。

### Q3: 设计系统可以保存供后续使用吗?

免费版不支持设计系统持久化。每次搜索结果为即时输出。如需跨会话保存设计系统并支持页面级覆盖,请使用专业版的 `--persist` 功能。

### Q4: Python版本有要求吗?

需要 Python 3.8 及以上版本。可通过 `python3 --version` 检查。如未安装,请参考依赖说明部分。

### Q5: 可以搜索图表类型的推荐吗?

免费版不包含 `chart` 域搜索。图表类型推荐是专业版功能,支持趋势图、对比图、时间线、漏斗图等25种图表类型匹配。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8 及以上

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3 | 运行时 | 必需 | 系统包管理器安装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

Python安装命令:

```bash
# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3

# Windows
winget install Python.Python.3.12
```

### API Key 配置

本Skill的CLI搜索工具基于本地数据文件运行,无需额外API Key。设计建议的生成由Agent内置LLM驱动,无需独立配置。

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。核心查询功能依赖Python CLI脚本执行,需确保exec工具可用。
