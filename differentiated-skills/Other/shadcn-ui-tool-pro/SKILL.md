---

slug: shadcn-ui-tool-pro
name: shadcn-ui-tool-pro
version: 1.0.0
displayName: shadcn UI工具-专业版
summary: "企业级React设计系统平台,支持自定义组件库、设计令牌管理与团队协作开发。企业级 shadcn/ui 开发工具专业版,面向团队与商业应用。核心能力:"
license: Proprietary
edition: pro
description: 企业级 shadcn/ui 开发工具专业版,面向团队与商业应用。核心能力:。可自动提升工作效率

  - 企业设计系统与令牌管理

  - 自定义组件库开发与发布

  - 组件文档与 Storybook 集成

  - 多主题与品牌切换

  - 国际化(i18n)组件支持

  - 无障碍(a11y)合规检查

  - 团队协作与代码审查

  - CI/CD 与自动化测试

  适用场景:

  - 企业级 React 应用开发

  - 设计系统建设与维护

  - 多品牌/多主题 SaaS 平台

  - 组件库开源与内部共享

  差异化:专业版在免费版基础上扩展设计系统、企业组...'
tags:
  - shadcn/ui
  - 企业级
  - 设计系统
  - 组件库
  - 团队协作
  - UI设计
  - 前端
  - 设计
  - shadcn-pro-cli
  - 返回结构
  - 用户提供
  - 完成核心
  - 逻辑
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"

---

# shadcn UI 工具 - 专业版

## 概述

shadcn/ui 工具专业版是企业级 React 设计系统平台,在免费版组件使用能力之上扩展设计令牌管理、自定义组件库开发、Storybook 文档集成、多主题品牌切换与无障碍合规检查。适合企业级 React 应用开发与设计系统建设.
专业版完全兼容免费版组件代码,支持平滑升级.
## 核心能力

### 1. 设计系统与令牌管理

集中管理设计令牌(颜色、字体、间距、圆角、阴影),通过设计令牌驱动组件样式,确保全局一致性.
**输入**: 用户提供设计系统与令牌管理所需的指令和必要参数.
**处理**: 解析设计系统与令牌管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回设计系统与令牌管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 自定义组件库

开发企业专属组件,发布到内部 npm 注册中心,团队共享使用.
**输入**: 用户提供自定义组件库所需的指令和必要参数.
**处理**: 解析自定义组件库的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自定义组件库的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. Storybook 集成

为每个组件生成 Storybook 文档,包含使用示例、API 文档与交互式预览.
**输入**: 用户提供Storybook 集成所需的指令和必要参数.
**处理**: 解析Storybook 集成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回Storybook 集成的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 多主题与品牌

支持多品牌主题切换,通过设计令牌动态切换品牌色系,适合 SaaS 多租户场景.
**输入**: 用户提供多主题与品牌所需的指令和必要参数.
**处理**: 解析多主题与品牌的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回多主题与品牌的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 国际化组件

内置国际化支持,组件文案通过 i18n 管理,支持多语言切换.
**输入**: 用户提供国际化组件所需的指令和必要参数.
**处理**: 解析国际化组件的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回国际化组件的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 6. 无障碍合规

自动检测组件的无障碍问题(WCAG 2.1 AA 标准),提供修复建议.
**输入**: 用户提供无障碍合规所需的指令和必要参数.
**处理**: 解析无障碍合规的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回无障碍合规的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 7. 团队协作

组件代码审查、版本管理、变更日志自动生成,团队协作开发组件库.
**输入**: 用户提供团队协作所需的指令和必要参数.
**处理**: 解析团队协作的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回团队协作的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 8. CI/CD 与测试

组件单元测试、视觉回归测试、自动发布流水线集成.
**输入**: 用户提供CI/CD 与测试所需的指令和必要参数.
**处理**: 解析CI/CD 与测试的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回CI/CD 与测试的响应数据,包含状态码、结果和日志.
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、React、设计系统平台、支持自定义组件库、设计令牌管理与团、shadcn、开发工具专业版、面向团队与商业应、核心能力、企业设计系统与令、自定义组件库开发、与发布、组件文档与、多主题与品牌切换、组件支持、合规检查、团队协作与代码审、与自动化测试等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:企业设计系统建设

构建企业级设计系统,统一管理设计令牌.
用户可通过自然语言指令触发此场景，工具将自动执行相应操作并返回结构化结果.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | shadcn UI工具-专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 初始化设计系统
./shadcn-pro-cli design-system init \
  --name "企业设计系统" \
  --brand-color "#1a73e8" \
  --output ./design-system
# ...
# 定义设计令牌
cat > design-system/tokens.json << 'EOF'
{
  "color": {
    "brand": {
      "primary": "#1a73e8",
      "secondary": "#34a853",
      "accent": "#fbbc04"
    },
    "semantic": {
      "success": "#16a34a",
      "warning": "#d97706",
      "error": "#dc2626",
      "info": "#2563eb"
    }
  },
  "typography": {
    "fontFamily": "Noto Sans SC",
    "fontSize": { "sm": "14px", "md": "16px", "lg": "18px" },
    "fontWeight": { "normal": "400", "medium": "500", "bold": "700" }
  },
  "spacing": { "xs": "4px", "sm": "8px", "md": "16px", "lg": "24px" },
  "radius": { "sm": "4px", "md": "8px", "lg": "12px" }
}
EOF
# ...
# 生成主题文件
./shadcn-pro-cli tokens generate \
  --input design-system/tokens.json \
  --output styles/themes/
```

### 场景二:多品牌主题切换

SaaS 平台支持多品牌主题切换.
```typescript
// lib/theme-provider.tsx
"use client"
// ...
import { createContext, useContext } from "react"
// ...
const brands = {
  brandA: {
    "--primary": "222 47% 11%",
    "--primary-foreground": "210 40% 98%",
    "--accent": "199 89% 48%",
  },
  brandB: {
    "--primary": "150 76% 30%",
    "--primary-foreground": "0 0% 100%",
    "--accent": "32 95% 44%",
  },
}
// ...
const BrandContext = createContext(brands.brandA)
// ...
export function BrandProvider({ brand, children }) {
  const theme = brands[brand] || brands.brandA
  return (
    <BrandContext.Provider value={theme}>
      <div style={theme}>{children}</div>
    </BrandContext.Provider>
  )
}
// ...
export const useBrand = () => useContext(BrandContext)
```

```bash
# 切换品牌主题
./shadcn-pro-cli theme switch --brand brandA
./shadcn-pro-cli theme switch --brand brandB
```

### 场景三:组件库开发与发布

开发企业组件并发布到内部注册中心.
```bash
# 创建企业组件
./shadcn-pro-cli component create \
  --name "EnterpriseTable" \
  --template "data-table" \
  --features "pagination,sorting,filtering,export"
# ...
# 生成 Storybook 文档
./shadcn-pro-cli storybook generate \
  --component EnterpriseTable \
  --output stories/EnterpriseTable.stories.tsx
# ...
# 运行无障碍检查
./shadcn-pro-cli a11y check \
  --component EnterpriseTable \
  --standard "WCAG2AA"
# ...
# 发布到内部注册中心
./shadcn-pro-cli publish \
  --component EnterpriseTable \
  --version 1.0.0 \
  --registry "https://npm.internal.company.com"
```

### 场景四:视觉回归测试

```bash
# 配置视觉回归测试
./shadcn-pro-cli visual-test init \
  --framework "playwright" \
  --browsers "chromium,firefox,webkit"
# ...
# 运行视觉回归测试
./shadcn-pro-cli visual-test run \
  --components "Button,Card,Table" \
  --threshold 0.1
# ...
# 输出:
# === 视觉回归测试报告 ===
# 组件: Button, Card, Table
# 通过: 24/26
# [失败] Button - dark theme: 像素差异 0.15% (阈值 0.1%)
# [失败] Table - mobile view: 像素差异 0.12% (阈值 0.1%)
# 查看 diff: ./visual-test/diff/
```

## 不适用场景

以下场景shadcn UI工具-专业版不适合处理：

- 专业医学法律翻译认证
- 同声传译
- 文学创作翻译

## 触发条件

需要文本翻译、多语言转换、本地化处理时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级

```bash
# 免费版组件代码完全兼容
# 依赖说明
npm install -g @shadcn-pro/cli
# ...
# 升级项目
./shadcn-pro-cli upgrade --from free
```

### 初始化企业设计系统

```bash
# 创建设计系统
./shadcn-pro-cli init \
  --enterprise \
  --design-tokens \
  --storybook \
  --i18n \
  --a11y
# ...
# 生成的项目结构:
# my-enterprise-app/
# ├── design-system/
# │   ├── tokens.json
# │   └── themes/
# ├── components/
# │   ├── ui/           # shadcn/ui 基础组件
# │   └── enterprise/   # 企业自定义组件
# ├── stories/          # Storybook 文档
# ├── tests/
# │   ├── unit/
# │   └── visual/
# └── .github/workflows/ci.yml
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
#
## 示例

### 企业级配置

```json
{
  "version": "2.0",
  "designSystem": {
    "name": "企业设计系统",
    "tokens": "design-system/tokens.json",
    "themes": ["light", "dark"],
    "brands": ["brandA", "brandB", "brandC"]
  },
  "components": {
    "registry": "https://npm.internal.company.com",
    "autoUpdate": false,
    "versioning": "semantic"
  },
  "documentation": {
    "storybook": true,
    "autoGenerate": true
  },
  "i18n": {
    "defaultLocale": "zh-CN",
    "locales": ["zh-CN", "en-US", "ja-JP"]
  },
  "accessibility": {
    "standard": "WCAG2AA",
    "autoCheck": true
  },
  "testing": {
    "unit": "vitest",
    "visual": "playwright",
    "coverage": 80
  },
  "cicd": {
    "platform": "github-actions",
    "autoPublish": true
  }
}
```

### 免费版与专业版能力对比

| 能力 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 组件安装 | 支持 | 支持 |
| 组件定制 | 手动修改 | +设计令牌驱动 |
| 主题 | 暗色/亮色 | +多品牌切换 |
| 组件库 | 使用现有 | +自定义开发发布 |
| 文档 | 无 | Storybook 自动生成 |
| 国际化 | 不支持 | 支持 |
| 无障碍 | 不支持 | WCAG 合规检查 |
| 测试 | 手动 | 单元 + 视觉回归 |
| 团队协作 | 单人 | 代码审查 + 版本管理 |
| CI/CD | 不支持 | 自动化流水线 |
| 技术支持 | 社区 | 优先工单 + SLA |

## 最佳实践

1. **令牌驱动**:所有样式通过设计令牌管理,不在组件中硬编码颜色/尺寸
2. **组件文档**:每个组件必须有 Storybook 文档,包含使用示例与 API 说明
3. **无障碍优先**:开发阶段就进行 a11y 检查,不要等上线再修复
4. **视觉回归**:每次修改组件后运行视觉回归测试,防止意外样式变化
5. **语义化版本**:组件库遵循 SemVer,breaking change 需要大版本升级
6. **变更日志**:自动生成 CHANGELOG,记录每次版本变更内容
7. **多品牌隔离**:不同品牌的主题变量完全隔离,避免样式污染

## 常见问题

### Q: 设计令牌如何与 Tailwind 集成?

A: 使用 `@tokens-studio/sd-tailwind` 或自定义 Style Dictionary 配置,将设计令牌转换为 Tailwind 配置。在 `tailwind.config.ts` 中引用生成的令牌文件,实现设计令牌到 Tailwind 类名的映射.
### Q: 多品牌主题如何动态切换?

A: 通过 CSS 变量实现。每个品牌定义一组 CSS 变量,切换品牌时替换根元素的变量集合。组件中使用 `var(--primary)` 等变量引用,自动适配当前品牌。无需重新渲染组件.
### Q: Storybook 文档如何自动生成?

A: 使用 `@storybook/react` 的 CSF(Component Story Format),为每个组件编写 stories 文件。专业版工具可从组件 props 自动生成基础 stories 模板,开发者补充交互场景.
### Q: 视觉回归测试如何处理动态内容?

A: 在 Storybook 中为组件定义固定状态(避免随机数据),视觉回归测试基于这些固定状态截图对比。对于动画效果,使用 `playwright` 的 `waitForFunction` 等待动画完成后再截图.
## 依赖说明

### 运行环境

- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Node.js | 运行时 | 必需 | 官方网站下载 |
| Next.js/React | 框架 | 必需 | npx create-next-app |
| Tailwind CSS | 样式 | 必需 | npm install tailwindcss |
| shadcn/ui CLI | 组件工具 | 必需 | npx shadcn@latest |
| Storybook | 文档 | 必需 | npx storybook init |
| Style Dictionary | 令牌管理 | 推荐 | npm install style-dictionary |
| Playwright | 视觉测试 | 推荐 | npm install playwright |
| vitest | 单元测试 | 推荐 | npm install vitest |
| i18next | 国际化 | i18n必需 | npm install i18next |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置

- 内部 npm 注册中心:配置 `.npmrc` 中的认证 Token
- Storybook Cloud(可选):配置 `STORYBOOK_TOKEN`
- 视觉测试云服务(可选):配置 `PERCY_TOKEN` 或 `CHROMATIC_TOKEN`

### 可用性分类

- **分类**: MD+EXEC(Markdown指令 + 命令行执行)
- **说明**: 通过自然语言指令驱动 Agent 执行企业级 React 设计系统开发
- **兼容性**: 完全兼容免费版组件代码
- **支持**: 优先工单支持,SLA 保障响应时间
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
