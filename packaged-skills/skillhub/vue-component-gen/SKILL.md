---
slug: "vue-component-gen"
name: "vue-component-gen"
version: 1.0.1
displayName: "Vue组件生成(专业版)"
summary: "面向团队的企业级Vue 3组件工程平台,含组件库结构、批量生成、可访问性、测试模板与CI集成。"
license: "Proprietary"
edition: "pro"
description: |-
  Vue组件生成工具专业版为团队与企业提供端到端Vue 3组件工程能力,涵盖企业级组件库结构、批量组件生成、WCAG AA可访问性、单元测试模板与CI/CD集成。核心能力:
  - 企业级组件库目录结构与文档
  - 批量组件生成脚手架
  - WCAG AA可访问性内建
  - 单元测试模板(Vitest + Vue Test Utils)
  - 多API类型同步输出(Composition/Options)
  - 设计令牌驱动的样式
  - CI/CD组件质量门禁

  适用场景:
  - 中大型团队Vue组件库从0到1搭建
  - 企业级产...
tags:
  - Vue
  - 组件库
  - 企业开发
  - 可访问性
  - 自动化测试
  - 团队协作
  - CI/CD
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# Vue组件生成(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Vue组件生成(专业版)批量生成 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
|:-----|:-----|:-----|
| 单组件生成 | 免费版全部 Composition/Options/TS/SCSS 能力 | 完全兼容 |
| 企业组件库结构 | 目录、文档、版本管理、barrel 导出 | Pro 新增 |
| 批量组件生成 | 脚手架脚本一次性生成整套组件 | Pro 新增 |
| WCAG AA 可访问性 | 默认合规,键盘/屏幕阅读器/对比度 | Pro 新增 |
| 单元测试模板 | Vitest + Vue Test Utils 标准模板 | Pro 新增 |
| 设计令牌驱动 | 令牌化样式,支持暗色模式 | Pro 新增 |
| 多 API 类型输出 | Composition 与 Options 同步输出 | Pro 新增 |
| CI 质量门禁 | 类型检查、测试、可访问性、视觉回归 | Pro 新增 |
### 单组件生成

针对单组件,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供单组件生成相关的配置参数、输入数据和处理选项.
**输出**: 返回单组件生成的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`单组件生成`的配置文档进行参数调优
### 企业组件库结构

针对企业组件库结构,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供企业组件库结构相关的配置参数、输入数据和处理选项.
**输出**: 返回企业组件库结构的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`企业组件库结构`的配置文档进行参数调优
### 批量组件生成

针对批量组件,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供批量组件生成相关的配置参数、输入数据和处理选项.
**输出**: 返回批量组件生成的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量组件生成`的配置文档进行参数调优
#
## 适用场景

### 场景 1:企业组件库结构搭建

为团队生成完整的 Vue 组件库目录结构.
```
src/
├── components/                  # 组件实现
│   ├── Button/
│   │   ├── Button.vue           # 组件实现
│   │   ├── Button.test.ts       # 单元测试
│   │   ├── Button.stories.ts    # Storybook 故事
│   │   ├── types.ts             # 类型定义
│   │   └── README.md            # 组件文档
│   ├── Input/
│   │   └── ...
│   └── ...
├── composables/                 # 组合式函数
│   ├── useTheme.ts
│   └── useA11y.ts
├── tokens/                      # 设计令牌
│   ├── colors.scss
│   ├── typography.scss
│   └── index.scss
├── utils/                       # 工具函数
│   ├── a11y.ts
│   └── cn.ts
└── index.ts                     # barrel 导出
```

### 场景 2:批量组件生成脚本

生成一个脚手架脚本,一次性创建整套组件骨架.
```bash
#!/usr/bin/env bash
# （请参考skill目录中的脚本文件） — 批量生成 Vue 组件
set -euo pipefail
# ...
COMPONENTS=(
  "Button" "Input" "Select" "Checkbox" "Radio"
  "Table" "Pagination" "Tag" "Badge"
  "Card" "Modal" "Drawer" "Tooltip"
  "Navbar" "Sidebar" "Breadcrumb"
)
# ...
BASE_DIR="src/components"
# ...
for comp in "${COMPONENTS[@]}"; do
  dir="$BASE_DIR/$comp"
  mkdir -p "$dir"
  comp_kebab=$(echo "$comp" | sed 's/\([A-Z]\)/-\1/g' | tr '[:upper:]' '[:lower:]' | sed 's/^-//')
# ...
  # 组件实现(<script setup lang="ts"> + 可访问性)
  cat > "$dir/$comp.vue" <<EOF
<template>
  <component
    :is="tag"
    class="${comp_kebab}"
    :aria-disabled="disabled"
    :tabindex="disabled ? -1 : 0"
  >
    <slot />
  </component>
</template>
# ...
<script setup lang="ts">
interface Props {
  tag?: string
  disabled?: boolean
}
# ...
withDefaults(defineProps<Props>(), {
  tag: 'div',
  disabled: false
})
</script>
# ...
<style scoped lang="scss">
.${comp_kebab} {
  padding: var(--spacing-4);
  border-radius: var(--radius-md);
  transition: var(--motion-duration-base) var(--motion-ease-in-out);
# ...
  &[aria-disabled="true"] {
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
  }
# ...
  &:focus-visible {
    outline: 3px solid var(--color-primary-500);
    outline-offset: 2px;
  }
}
</style>
EOF
# ...
  # 类型定义
  cat > "$dir/types.ts" <<EOF
export interface ${comp}Props {
  tag?: string
  disabled?: boolean
}
# ...
export interface ${comp}Emits {
  // 详情见说明: 定义事件
}
EOF
# ...
  # 单元测试模板
  cat > "$dir/$comp.test.ts" <<EOF
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ${comp} from './${comp}.vue'
# ...
describe('${comp}', () => {
  it('应正确渲染默认 slot', () => {
    const wrapper = mount(${comp}, {
      slots: { default: '内容' }
    })
    expect(wrapper.text()).toContain('内容')
  })
# ...
  it('disabled 时应设置 aria-disabled', () => {
    const wrapper = mount(${comp}, {
      props: { disabled: true }
    })
    expect(wrapper.attributes('aria-disabled')).toBe('true')
    expect(wrapper.attributes('tabindex')).toBe('-1')
  })
# ...
  it('键盘应可聚焦', async () => {
    const wrapper = mount(${comp})
    expect(wrapper.attributes('tabindex')).toBe('0')
  })
})
EOF
# ...
  # 文档
  cat > "$dir/README.md" <<EOF
# ${comp}
# ...
## 使用流程
# ...
### 优秀步:声明团队上下文
# ...
在对话中说明团队规模、技术栈与组件库目标,例如:
# ...
```
我们是 12 人的前端团队,技术栈是 Vue 3 + TypeScript + Vite,
需要从 0 搭建企业组件库,要求 WCAG AA 合规,含单元测试,
支持暗色模式,并集成到 CI.
```
# ...
### 第二步:获取工程方案
# ...
工具会输出组件库目录结构、批量生成脚本、可访问性模板、测试模板与 CI 配置.
# ...
### 第三步:落地与维护
# ...
```bash
# 应用设计令牌
cp tokens.scss src/styles/

# 批量生成组件骨架
bash （请参考skill目录中的脚本文件）

# 运行单元测试
npx vitest run

# 启动 Storybook 文档
npm run storybook
```
# ...
#
## 输入格式
# ...
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | vue-component-gen处理的内容输入 |,  |
| content | string | 否 | vue-component-gen处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```
# ...
输出模板参考: `assets/output.json`
# ...
## 异常处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 
# ...
## 依赖说明
# ...
### 运行环境
# ...
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 20 LTS+
- **Vue**:建议 3.3+
- **CI 平台**:GitHub Actions / GitLab CI / Jenkins
# ...
### 依赖说明(补充)
# ...
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Vue 3 | npm 包 | 必需 | `npm i vue` |
| TypeScript | npm 包 | 必需 | `npm i -D typescript` |
| vue-tsc | npm 包 | 必需 | `npm i -D vue-tsc` |
| vitest | 测试框架 | 必需 | `npm i -D vitest` |
| @vue/test-utils | 测试工具 | 必需 | `npm i -D @vue/test-utils` |
| sass | npm 包 | 推荐 | `npm i -D sass` |
| @storybook/vue3 | 文档工具 | 推荐 | `npx storybook init` |
| eslint-plugin-vue | npm 包 | 推荐 | `npm i -D eslint-plugin-vue` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
# ...
### API Key 配置
# ...
- 基础LLM由Agent平台内置提供，Skill基于Markdown指令驱动
- 私有 npm 发布需配置 `NODE_AUTH_TOKEN` 环境变量
- 视觉回归工具(Chromatic)需配置 `CHROMATIC_TOKEN`
- 代码覆盖率上传(Codecov)需配置 `CODECOV_TOKEN`
# ...
### 可用性分类
# ...
- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出企业级 Vue 组件工程方案;脚手架与测试脚本需在仓库中落地并由本地或 CI 执行
# ...
## 案例展示
# ...
### CI/CD 组件质量门禁
# ...
```yaml
# .github/workflows/component-quality.yml
name: Vue Component Quality Gate
on:
  pull_request:
    branches: [main]
    paths: ['src/components/**']

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci

      - name: 类型检查
        run: npx vue-tsc --noEmit

      - name: 单元测试
        run: npx vitest run --coverage

      - name: 可访问性检查
        run: npx vitest run --testNamePattern="可访问性"

      - name: ESLint 检查
        run: npx eslint src/components --max-warnings=0

      - name: 构建
        run: npm run build

      - name: 上传覆盖率
        uses: codecov/codecov-action@v4
```
# ...
## 常见问题
# ...
### Q1: 企业组件库如何发布与版本化?
# ...
将组件库配置为独立 npm 包,采用语义化版本(1.0.0),通过 CHANGELOG 记录变更。CI 中自动发布到私有 npm 注册表.
# ...
### Q2: 多项目如何复用组件库?
# ...
发布为私有 npm 包,各项目通过 `npm i @your-org/vue-components` 安装。配合语义化版本,实现可控升级.
# ...
### Q3: 可访问性测试如何自动化?
# ...
Vitest 中编写可访问性测试(键盘聚焦、aria 属性、对比度),CI 中运行。更深入测试推荐 `@axe/playwright`.
# ...
### Q4: 设计令牌如何与 Tailwind / UnoCSS 协同?
# ...
Tailwind:在 `tailwind.config.js` 中将令牌映射为 theme 字段;UnoCSS:在 `unocss.config.ts` 中将令牌映射为 theme 字段.
# ...
### Q5: Pro 版与免费版如何协同?
# ...
Pro 版完全兼容免费版的所有单组件输出。个人开发者可继续使用免费版,团队场景启用 Pro 版获得企业级结构、批量生成与可访问性能力。两个版本可在同一仓库并存.
# ...
### Q6: 如何度量组件库健康度?
# ...
跟踪四个指标:组件复用率、WCAG AA 合规率、单元测试覆盖率、文档覆盖率。四者共同反映组件库健康度.
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
## 已知限制
# ...
# ...