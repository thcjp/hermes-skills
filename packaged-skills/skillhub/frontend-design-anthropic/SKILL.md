---
slug: "frontend-design-anthropic"
name: "frontend-design-anthropic"
version: 1.0.1
displayName: "前端设计-专业版"
summary: "企业级前端设计工具,支持设计系统生成、组件库批量产出、多端适配,适配商业产品开发。"
license: "Proprietary"
edition: "pro"
description: |-
  前端设计专业版,面向企业团队与专业设计师的高级前端界面设计工具。核心能力:
  - 完整设计系统生成(Design Tokens、主题、规范文档)
  - 组件库批量设计与产出,支持 Storybook 集成
  - 响应式多端适配(桌面/平板/移动/暗色模式)
  - 设计Token管理与团队协作
  - 可访问性(a11y)合规检查与修复
  - 性能优化建议与代码审查

  适用场景:
  - 企业产品设计系统建设
  - 组件库标准化与批量产出
  - 多端产品界面统一设计
  - 设计团队协作与规范沉淀

  差异化:专业版在免费版基础上...
tags:
  - Creative
  - 前端设计
  - 企业版
  - 设计系统
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 前端设计-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 前端设计-专业版支持设计系统生成 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-----|:-----|:-----|:-----|
| 设计思维引导 | 是 | 是 | 目的/调性/约束/差异化 |
| 字体选择指导 | 是 | 是 | 避免通用字体 |
| 配色方案指导 | 是 | 是 | CSS变量一致性 |
| 动效设计指导 | 是 | 是 | CSS优先方案 |
| 空间构图指导 | 是 | 是 | 布局与负空间 |
| HTML/CSS/JS 实现 | 是 | 是 | 生产级代码 |
| React/Vue 实现 | 是 | 是 | 主流框架 |
| 设计系统生成 | 否 | 是 | Tokens/主题/规范 |
| 组件库批量生成 | 否 | 是 | Storybook 集成 |
| 响应式多端适配 | 否 | 是 | 桌面/平板/移动 |
| 设计Token管理 | 否 | 是 | 团队共享 |
| 可访问性检查 | 否 | 是 | a11y 合规 |
| 性能优化建议 | 否 | 是 | 代码审查 |
| 技术支持 | 社区 | 专属 | 工单响应 |
### 能力项

针对能力项,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力项相关的配置参数、输入数据和处理选项.
**输出**: 返回能力项的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力项`的配置文档进行参数调优
### 设计思维引导

针对设计思维引导,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供设计思维引导相关的配置参数、输入数据和处理选项.
**输出**: 返回设计思维引导的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`设计思维引导`的配置文档进行参数调优
### 字体选择指导

针对字体选择指导,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供字体选择指导相关的配置参数、输入数据和处理选项.
**输出**: 返回字体选择指导的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`字体选择指导`的配置文档进行参数调优
#
## 适用场景

### 场景一:企业设计系统建设

企业需建立完整的设计系统,包含 Design Tokens、主题与规范文档.
```css
/* 专业版生成的 Design Tokens */
:root {
  /* 颜色系统 */
  --color-primary-50: #f0f9ff;
  --color-primary-500: #0ea5e9;
  --color-primary-900: #0c4a6e;
// ...
  /* 字体系统 */
  --font-display: 'Playfair Display', serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
// ...
  /* 间距系统(8px 基准) */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-8: 2rem;
// ...
  /* 圆角系统 */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
// ...
  /* 阴影系统 */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
// ...
  /* 动效系统 */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 150ms;
  --duration-normal: 300ms;
}
```

### 场景二:组件库批量产出

设计团队需批量生成标准化组件,并集成到 Storybook.
```bash
# 批量生成组件
python3 （请参考skill目录中的脚本文件） \
  --config components.yaml \
  --output ./src/components/ \
  --framework react \
  --storybook \
  --types
# ...
# 示例
# components:
#   - name: Button
#     variants: [primary, secondary, ghost, danger]
#     sizes: [sm, md, lg]
#   - name: Card
#     variants: [default, outlined, elevated]
#   - name: Input
#     variants: [text, password, search]
```

### 场景三:多端响应式适配

产品需同时支持桌面、平板、移动端及暗色模式.
```css
/* 专业版生成的响应式系统 */
/* 断点系统 */
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}
// ...
/* 响应式组件 */
.card {
  padding: var(--space-4);
  /* 移动端优先 */
}
// ...
@media (min-width: 768px) {
  .card {
    padding: var(--space-8);
  }
}
// ...
/* 暗色模式 */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0a0a0a;
    --color-text: #f5f5f5;
    --color-surface: #141414;
  }
}
```

### 场景四:可访问性合规检查

产品需符合 WCAG 2.1 AA 标准,使用 a11y 检查工具.
```bash
# 可访问性检查
python3 （请参考skill目录中的脚本文件） \
  --input ./src/ \
  --standard wcag2.1-aa \
  --output ./reports/a11y_report.md \
  --fix-suggestions
# ...
# 检查项目:颜色对比度、键盘导航、屏幕阅读器、焦点管理
```

## 使用流程

### 优秀步:启用专业版功能

```bash
export FRONTEND_DESIGN_EDITION="pro"
export FRONTEND_DESIGN_LICENSE="your_license_key"
```

### 第二步:生成设计系统

```bash
# 生成完整设计系统
python3 （请参考skill目录中的脚本文件） \
  --brand "企业品牌" \
  --tone "精致奢华" \
  --output ./design-system/ \
  --format all
```

### 第三步:批量生成组件

```bash
python3 （请参考skill目录中的脚本文件） \
  --config components.yaml \
  --output ./src/components/ \
  --storybook
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | frontend-design-anthropic处理的内容输入 |,  |
| content | string | 否 | frontend-design-anthropic处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "anthropic 相关配置参数",
    result: "anthropic 相关配置参数",
    result: "anthropic 相关配置参数",
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
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 18+ + Python 3.9+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Node.js 18+ | 运行时 | 必需 | 官方安装 |
| Python 3.9+ | 脚本运行 | 必需 | 官方安装 |
| Storybook | 组件文档 | 推荐 | npx storybook init |
| Style Dictionary | Token 管理 | 推荐 | npm install style-dictionary |

### API Key 配置
- **环境变量名**: `FRONTEND_DESIGN_LICENSE`(企业版授权)
- **附加变量**: `FRONTEND_DESIGN_EDITION=pro`
- **获取方式**: 通过企业服务渠道申请,支持团队席位授权
- **安全建议**: License 通过环境变量配置,避免写入代码仓库

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持设计系统生成、组件库批量产出、多端适配等企业级前端设计场景

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有设计思维与美学维度,迁移时仅需设置 `FRONTEND_DESIGN_EDITION=pro` 并配置 License.
### Q2:设计系统包含哪些内容?
A:包含 Design Tokens(CSS 变量)、主题配置(亮/暗)、规范文档(字体/颜色/间距/组件用法)、组件库(带 TypeScript 类型与 Storybook).
### Q3:支持哪些前端框架?
A:支持 React、Vue、Angular、Svelte 等主流框架,以及原生 HTML/CSS/JS。可生成 TypeScript 类型定义.
### Q4:响应式适配如何实现?
A:采用移动优先策略,默认移动端样式,通过媒体查询逐级放大。支持 sm/md/lg/xl/2xl 标准断点,可自定义.
### Q5:可访问性检查覆盖哪些标准?
A:支持 WCAG 2.1 A/AA/AAA 标准检查,覆盖颜色对比度、键盘导航、屏幕阅读器、焦点管理、ARIA 属性等,并提供修复建议.
### Q6:能否集成到现有设计系统?
A:可以。支持导入现有 Figma Tokens 或 Style Dictionary 配置,生成兼容代码。支持增量更新而非全量替换.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

