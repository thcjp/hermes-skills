---
slug: "ui-design-toolkit"
name: "ui-design-toolkit"
version: "1.0.0"
displayName: "UI设计工具包专业版"
summary: "企业级UI设计工具包,支持设计系统、设计令牌、可访问性与组件库,适配团队协作与大型项目。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与企业用户的 UI 设计工具包(专业版)。核心能力:
  - 涵盖免费版全部能力(视觉层次、排版、色彩、间距、状态)
  - 设计系统(Design System)构建与维护
  - 设计令牌(Design Tokens)管理
  - 可访问性(a11y)深度规范与自动化检测
  - 组件库抽象与复用
  - 多主题与品牌切换
  - 动效系统(Motion Design)
  - 国际化(i18n)设计考虑
  - Figma 协作规范
  - 设计文档与 Storybook 集成
  - 设计评审 Checklist

  适用场景:
tags:
  - 创意设计
  - UI设计
  - 企业级
  - 设计系统
  - 可访问性
  - 组件库
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# UI设计工具包专业版

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

### 免费版 vs 专业版对比
| 能力 | 免费版 | 专业版 | 增量价值 |
|:-----|:-------|:-------|:---------|
| 视觉层次 | 支持 | 支持 | - |
| 排版规范 | 支持 | 支持 | - |
| 色彩使用 | 支持 | 支持 | - |
| 间距系统 | 支持 | 支持 | - |
| 组件状态 | 支持 | 支持 | - |
| 响应式 | 基础 | 完整体系 | 全端适配 |
| 暗黑模式 | 基础 | 多主题 | 多品牌 |
| 动效设计 | 基础 | 动效系统 | 体验提升 |
| 设计系统 | 不支持 | 完整建设 | 一致性 |
| 设计令牌 | 不支持 | Token 管理 | 设计代码统一 |
| 可访问性 | 基础 | 深度规范 + 检测 | 合规 |
| 组件库 | 不支持 | 抽象与复用 | 团队效率 |
| 国际化 | 不支持 | i18n 设计 | 全球化 |
| Figma 协作 | 不支持 | 规范与同步 | 设计开发协同 |
| Storybook | 不支持 | 集成与文档 | 组件文档 |
| 设计评审 | 不支持 | Checklist | 质量保证 |

**输入**: 用户提供免费版 vs 专业版对比所需的指令和必要参数。
**处理**: 解析免费版 vs 专业版对比的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回免费版 vs 专业版对比的处理结果,包含执行状态码、结果数据和执行日志。
### 视觉层次

针对视觉层次,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供视觉层次相关的配置参数、输入数据和处理选项。

**输出**: 返回视觉层次的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`视觉层次`的配置文档进行参数调优
### 排版规范

针对排版规范,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应。

**输入**: 用户提供排版规范相关的配置参数、输入数据和处理选项。

**输出**: 返回排版规范的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`排版规范`的配置文档进行参数调优
#
## 适用场景

### 场景一:设计系统构建
构建完整的企业设计系统。

> 详细代码示例已移至 `references/detail.md`

### 场景二:可访问性深度规范
实现 WCAG 2.1 AA 级合规。

```javascript
// a11y-checklist.js - 可访问性检查清单
export const a11yChecklist = {
  // 感知(Perceivable)
  perceptible: {
    '1.1.1 非文本内容': '所有图片有 alt 文本(装饰性用 alt="")',
    '1.3.1 信息与关系': '使用语义化 HTML(header/nav/main/article)',
    '1.4.3 对比度(最低)': '正文文字对比度 >= 4.5:1',
    '1.4.3 对比度(大文字)': '18px+ 文字对比度 >= 3:1',
    '1.4.4 文字缩放': '支持 200% 缩放不丢失功能',
    '1.4.11 非文字对比度': 'UI 组件对比度 >= 3:1',
  },

  // 可操作(Operable)
  operable: {
    '2.1.1 键盘可访问': '所有功能可通过键盘操作',
    '2.1.2 无键盘陷阱': '焦点不会被组件困住',
    '2.4.3 焦点顺序': 'DOM 顺序与视觉顺序一致',
    '2.4.7 焦点可见': '聚焦状态清晰可见',
    '2.5.5 目标尺寸': '触摸目标 >= 44x44px',
  },

  // 可理解(Understandable)
  understandable: {
    '3.2.1 可预测': '组件行为一致',
    '3.2.2 输入标识': '表单字段有清晰标签',
    '3.3.1 错误识别': '错误信息清晰描述',
    '3.3.2 标签或指令': '提供输入指导',
  },

  // 健壮(Robust)
  robust: {
    '4.1.2 名称、角色、值': 'ARIA 属性正确使用',
    '4.1.3 状态消息': '使用 role="status" 或 aria-live',
  },
}

// 自动化检测工具集成
// 推荐工具:
// - axe-core: 自动化可访问性检测
// - Lighthouse: Chrome 内置审计
// - jest-axe: Jest 集成测试
```

```python
"""
npm install --save-dev axe-core jest-axe

module.exports = {
  setupFilesAfterEnv: ['jest-axe/extend-expect'],
}

import { render } from '@testing-library/react'
import { axe } from 'jest-axe'
import { Button } from './Button'

test('Button 满足可访问性标准', async () => {
  const { container } = render(<Button>点击</Button>)
  const results = await axe(container)
  expect(results).toHaveNoViolations()
})
"""
```

### 场景三:组件库抽象
构建可复用的组件库。

> 详细代码示例已移至 `references/detail.md`

### 场景四:多主题切换
支持多品牌动态切换。

```css
/* themes/brand-a.css */
:root[data-theme="brand-a"] {
  --color-brand-50: #eff6ff;
  --color-brand-500: #3b82f6;
  --color-brand-600: #2563eb;
  --color-brand-700: #1d4ed8;
}

/* themes/brand-b.css */
:root[data-theme="brand-b"] {
  --color-brand-50: #f0fdf4;
  --color-brand-500: #22c55e;
  --color-brand-600: #16a34a;
  --color-brand-700: #15803d;
}

/* themes/brand-c.css */
:root[data-theme="brand-c"] {
  --color-brand-50: #faf5ff;
  --color-brand-500: #a855f7;
  --color-brand-600: #9333ea;
  --color-brand-700: #7e22ce;
}
```

```javascript
// 主题切换
function setBrand(brand) {
  document.documentElement.setAttribute('data-theme', `brand-${brand}`)
  localStorage.setItem('brand', brand)
}

// 初始化
const savedBrand = localStorage.getItem('brand') || 'a'
setBrand(savedBrand)
```

## 使用流程

### 1. 初始化设计系统
```bash
mkdir my-design-system && cd my-design-system
npm init -y

npm install clsx
npm install -D tailwindcss storybook @storybook/react
```

### 2. 定义设计令牌
```bash
cp templates/design-tokens.js ./src/
cp templates/tailwind.config.js ./
```

### 3. 搭建组件库
```bash
npx storybook init

mkdir -p src/components/ui
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | ui-design-toolkit处理的内容输入 |, 默认: 全部维度 |
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
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18 及以上

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| tailwindcss | npm 库 | 推荐 | `npm install -D tailwindcss` |
| clsx | npm 库 | 推荐(组件) | `npm install clsx` |
| storybook | npm 库 | 可选(文档) | `npx storybook init` |
| axe-core | npm 库 | 可选(a11y) | `npm install -D axe-core` |
| style-dictionary | npm 库 | 可选(令牌) | `npm install -D style-dictionary` |
| Node.js 18+ | 运行时 | 必需 | `nodejs.org` 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本 Skill **无需任何 API Key**
- 设计系统为本地构建,不依赖云服务
- Figma 集成可能需要 Figma API Token(可选)

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。专业版支持设计系统建设、设计令牌管理与可访问性规范,适合企业级产品设计与团队协作。

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1: 设计系统如何保证一致性?
通过将所有设计令牌集中在统一文件,团队成员只能使用预定义的令牌。配合设计 lint 工具(如 Stylelint)检测硬编码值。

### Q2: 设计令牌如何同步到代码?
使用 Style Dictionary 等工具,从单一数据源自动生成各平台格式(CSS 变量、iOS Swift、Android XML)。

### Q3: 可访问性合规需要达到什么级别?
建议至少达到 WCAG 2.1 AA 级。部分场景(政府、医疗)可能要求 AAA 级。使用 axe-core 自动化检测 + 人工评审。

### Q4: 组件库如何版本管理?
- 遵循语义化版本(SemVer)
- 破坏性变更需迁移指南
- 使用 Changesets 管理版本
- 通过 npm/内部 registry 分发

### Q5: 专业版与免费版的迁移?
零迁移成本。专业版是免费版的超集,设计原则完全兼容。升级后原有组件继续可用,新特性按需启用。

### Q6: 如何与 Figma 协作?
使用 Figma Variables 同步设计令牌,组件命名与代码一一对应,变更通过 PR 评审。专业版提供详细的协作规范。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

