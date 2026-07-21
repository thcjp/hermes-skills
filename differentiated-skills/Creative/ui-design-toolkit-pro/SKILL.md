---
slug: ui-design-toolkit-pro
name: ui-design-toolkit-pro
version: "1.0.0"
displayName: UI设计工具包专业版
summary: 企业级UI设计工具包,支持设计系统、设计令牌、可访问性与组件库,适配团队协作与大型项目。
license: Proprietary
edition: pro
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
---
# UI 设计工具包 - 专业版
## 概述
UI 设计工具包(专业版)在免费版(`ui-design-toolkit-free`)核心设计原则之上,新增设计系统构建、设计令牌管理、可访问性深度规范、组件库抽象与多主题支持等企业级能力。适合大型项目与团队协作场景。

专业版与免费版设计原则完全兼容,已使用免费版的项目无需调整,升级后可直接启用高级特性。

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

## 使用场景
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

## 不适用场景

以下场景UI设计工具包专业版不适合处理：

- 3D建模和动画制作
- 照片级写实渲染
- 手绘原创插画


## 触发条件

需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于非本工具能力范围的需求。


## 快速开始
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

## 配置示例
### Storybook 集成
```yaml
version: 2
stories:
  - glob: '**/*.stories.@(ts|tsx|js|jsx)'
    dir: ../src/components
addons:
  - '@storybook/addon-essentials'
  - '@storybook/addon-a11y'        # 可访问性检测
  - '@storybook/addon-designs'     # Figma 集成
```

### 设计评审 Checklist
```markdown
- [ ] 使用设计令牌,无硬编码值
- [ ] 间距遵循 4px 网格
- [ ] 色彩使用语义化命名
- [ ] 字体使用预定义字号

- [ ] 文字对比度 >= 4.5:1
- [ ] 触摸目标 >= 44x44px
- [ ] 所有图片有 alt 文本
- [ ] 焦点状态清晰可见
- [ ] 支持键盘导航

- [ ] 移动端优先设计
- [ ] 断点选择合理
- [ ] 触摸与鼠标交互区分

- [ ] 默认/悬停/聚焦/激活/禁用
- [ ] 加载状态设计
- [ ] 错误状态设计
- [ ] 空状态设计

- [ ] 文本不硬编码
- [ ] 支持 RTL 布局
- [ ] 长文本不破坏布局
- [ ] 日期/时间本地化
```

## 最佳实践
### 1. 设计系统原则
- **单一数据源**:所有令牌定义在统一文件
- **语义命名**:用 `color-error` 而非 `color-red`
- **层级清晰**:令牌 > 样式 > 组件 > 模式
- **版本管理**:设计系统纳入 Git,版本化发布

### 2. 设计令牌管理
```javascript
// 令牌转换工具:统一导出为各平台格式
// Style Dictionary 配置
module.exports = {
  source: ['tokens/**/*.json'],
  platforms: {
    web: { transformGroup: 'css', buildPath: 'build/web/', files: [{
      destination: 'tokens.css', format: 'css/variables'
    }]},
    ios: { transformGroup: 'ios-swift', buildPath: 'build/ios/', files: [{
      destination: 'Tokens.swift', format: 'ios-swift/class.swift'
    }]},
    android: { transformGroup: 'android', buildPath: 'build/android/', files: [{
      destination: 'colors.xml', format: 'android/colors'
    }]},
  },
}
```

### 3. 可访问性自动化
```yaml
name: Accessibility Check
on: [pull_request]
jobs:
  a11y:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - name: Run axe-core
        run: npm run test:a11y
      - name: Lighthouse audit
        run: npx lighthouse-ci --accessibility=90
```

### 4. Figma 协作规范
- 设计师在 Figma 中使用与代码一致的令牌命名
- 使用 Figma Variables 同步设计令牌
- 组件命名与代码组件一一对应
- 变更通过 PR 流程评审

### 5. 国际化设计考虑
- 文本长度预留 30% 扩展空间(德文较长)
- 支持 RTL(从右到左)布局
- 日期/时间/数字本地化
- 货币与单位适配
- 颜色文化差异考量

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
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。专业版支持设计系统建设、设计令牌管理与可访问性规范,适合企业级产品设计与团队协作。

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
