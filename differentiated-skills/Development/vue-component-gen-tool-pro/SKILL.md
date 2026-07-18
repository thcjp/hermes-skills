---
slug: vue-component-gen-tool-pro
name: vue-component-gen-tool-pro
version: "1.0.0"
displayName: Vue组件生成(专业版)
summary: 面向团队的企业级Vue 3组件工程平台,含组件库结构、批量生成、可访问性、测试模板与CI集成。
license: MIT
edition: pro
description: |-
  Vue组件生成工具专业版为团队与企业提供端到端Vue 3组件工程能力,涵盖企业级组件库结构、批量组件生成、WCAG AA可访问性、单元测试模板与CI/CD集成。

  核心能力:
  - 企业级组件库目录结构与文档
  - 批量组件生成脚手架
  - WCAG AA可访问性内建
  - 单元测试模板(Vitest + Vue Test Utils)
  - 多API类型同步输出(Composition/Options)
  - 设计令牌驱动的样式
  - CI/CD组件质量门禁

  适用场景:
  - 中大型团队Vue组件库从0到1搭建
  - 企业级产品组件复用与版本管理
  - 可访问性合规改造(WCAG AA)
  - 组件库自动化测试与发布

  差异化:专业版兼容免费版的所有组件输出,扩展企业级结构、批量生成、可访问性与测试能力,适合规模化团队与生产级Vue项目。

  触发关键词: vue, 组件库, 批量生成, 可访问性, vitest, 组件测试, 设计令牌, ci集成, 企业组件
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
---

# Vue 组件生成工具(专业版)

## 概述

`vue-component-gen-tool-pro` 是面向团队与企业的 Vue 3 组件工程平台。它在免费版单组件生成之上,扩展了企业级组件库结构、批量组件脚手架、WCAG AA 可访问性内建、单元测试模板与 CI/CD 质量门禁能力,帮助团队构建可复用、可测试、可访问的 Vue 组件体系。

本版本完全兼容免费版输出的所有单文件组件代码,可平滑升级。所有指令通过 Markdown 驱动 Agent,配套脚本用于批量生成与 CI 集成。

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
| --- | --- | --- |
| 单组件生成 | 免费版全部 Composition/Options/TS/SCSS 能力 | 完全兼容 |
| 企业组件库结构 | 目录、文档、版本管理、barrel 导出 | Pro 新增 |
| 批量组件生成 | 脚手架脚本一次性生成整套组件 | Pro 新增 |
| WCAG AA 可访问性 | 默认合规,键盘/屏幕阅读器/对比度 | Pro 新增 |
| 单元测试模板 | Vitest + Vue Test Utils 标准模板 | Pro 新增 |
| 设计令牌驱动 | 令牌化样式,支持暗色模式 | Pro 新增 |
| 多 API 类型输出 | Composition 与 Options 同步输出 | Pro 新增 |
| CI 质量门禁 | 类型检查、测试、可访问性、视觉回归 | Pro 新增 |

## 使用场景

### 场景 1:企业组件库结构搭建

为团队生成完整的 Vue 组件库目录结构。

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

生成一个脚手架脚本,一次性创建整套组件骨架。

```bash
#!/usr/bin/env bash
# scripts/scaffold-vue-components.sh — 批量生成 Vue 组件
set -euo pipefail

COMPONENTS=(
  "Button" "Input" "Select" "Checkbox" "Radio"
  "Table" "Pagination" "Tag" "Badge"
  "Card" "Modal" "Drawer" "Tooltip"
  "Navbar" "Sidebar" "Breadcrumb"
)

BASE_DIR="src/components"

for comp in "${COMPONENTS[@]}"; do
  dir="$BASE_DIR/$comp"
  mkdir -p "$dir"
  comp_kebab=$(echo "$comp" | sed 's/\([A-Z]\)/-\1/g' | tr '[:upper:]' '[:lower:]' | sed 's/^-//')

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

<script setup lang="ts">
interface Props {
  tag?: string
  disabled?: boolean
}

withDefaults(defineProps<Props>(), {
  tag: 'div',
  disabled: false
})
</script>

<style scoped lang="scss">
.${comp_kebab} {
  padding: var(--spacing-4);
  border-radius: var(--radius-md);
  transition: var(--motion-duration-base) var(--motion-ease-in-out);

  &[aria-disabled="true"] {
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
  }

  &:focus-visible {
    outline: 3px solid var(--color-primary-500);
    outline-offset: 2px;
  }
}
</style>
EOF

  # 类型定义
  cat > "$dir/types.ts" <<EOF
export interface ${comp}Props {
  tag?: string
  disabled?: boolean
}

export interface ${comp}Emits {
  // TODO: 定义事件
}
EOF

  # 单元测试模板
  cat > "$dir/$comp.test.ts" <<EOF
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ${comp} from './${comp}.vue'

describe('${comp}', () => {
  it('应正确渲染默认 slot', () => {
    const wrapper = mount(${comp}, {
      slots: { default: '内容' }
    })
    expect(wrapper.text()).toContain('内容')
  })

  it('disabled 时应设置 aria-disabled', () => {
    const wrapper = mount(${comp}, {
      props: { disabled: true }
    })
    expect(wrapper.attributes('aria-disabled')).toBe('true')
    expect(wrapper.attributes('tabindex')).toBe('-1')
  })

  it('键盘应可聚焦', async () => {
    const wrapper = mount(${comp})
    expect(wrapper.attributes('tabindex')).toBe('0')
  })
})
EOF

  # 文档
  cat > "$dir/README.md" <<EOF
# ${comp}

## 用法

\`\`\`vue
<template>
  <${comp}>内容</${comp}>
</template>

<script setup lang="ts">
import { ${comp} } from '@/components/${comp}'
</script>
\`\`\`

## Props

| 属性 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| tag | string | 'div' | 渲染的 HTML 标签 |
| disabled | boolean | false | 是否禁用 |

## 可访问性

- 默认支持键盘聚焦(tabindex)
- disabled 状态使用 aria-disabled
- focus-visible 提供可见焦点样式
- 对比度符合 WCAG AA

## 测试

\`\`\`bash
npx vitest run src/components/${comp}
\`\`\`
EOF

done

# barrel 导出
{
  echo "// 自动生成的 barrel 导出"
  for comp in "${COMPONENTS[@]}"; do
    echo "export { default as ${comp} } from './${comp}/${comp}.vue'"
    echo "export type { ${comp}Props } from './${comp}/types'"
  done
} > "$BASE_DIR/index.ts"

echo "已生成 ${#COMPONENTS[@]} 个组件于 $BASE_DIR/"
```

### 场景 3:可访问性增强组件模板

生成默认符合 WCAG AA 的组件,内置键盘与屏幕阅读器支持。

```vue
<template>
  <button
    class="btn"
    :class="[\`btn--\${variant}\`, { 'btn--loading': loading }]"
    :disabled="disabled"
    :aria-busy="loading"
    :aria-pressed="pressed"
    @click="handleClick"
  >
    <span v-if="loading" class="btn__spinner" aria-hidden="true" />
    <slot />
  </button>
</template>

<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary' | 'danger'
  disabled?: boolean
  loading?: boolean
  pressed?: boolean
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  disabled: false,
  loading: false,
  pressed: undefined
})

const emit = defineEmits<{
  (e: 'click', event: MouseEvent): void
}>()

const handleClick = (event: MouseEvent) => {
  // disabled 与 loading 状态阻止点击
  // (disabled 由原生 button 处理,loading 需手动阻止)
}
</script>

<style scoped lang="scss">
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
  padding: var(--spacing-2) var(--spacing-4);
  border: none;
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  cursor: pointer;
  transition: var(--motion-duration-fast) var(--motion-ease-in-out);

  // WCAG AA: 焦点可见
  &:focus-visible {
    outline: 3px solid var(--color-primary-500);
    outline-offset: 2px;
  }

  &--primary {
    background: var(--color-primary-500);
    color: var(--color-neutral-0);
    &:hover { background: var(--color-primary-700); }
  }

  &--secondary {
    background: var(--color-neutral-100);
    color: var(--color-neutral-900);
    &:hover { background: var(--color-neutral-500); }
  }

  &--danger {
    background: var(--color-danger-500);
    color: var(--color-neutral-0);
    &:hover { filter: brightness(0.9); }
  }

  &[disabled],
  &--loading {
    opacity: 0.5;
    cursor: not-allowed;
  }
}
</style>
```

## 快速开始

### 第一步:声明团队上下文

在对话中说明团队规模、技术栈与组件库目标,例如:

```
我们是 12 人的前端团队,技术栈是 Vue 3 + TypeScript + Vite,
需要从 0 搭建企业组件库,要求 WCAG AA 合规,含单元测试,
支持暗色模式,并集成到 CI。
```

### 第二步:获取工程方案

工具会输出组件库目录结构、批量生成脚本、可访问性模板、测试模板与 CI 配置。

### 第三步:落地与维护

```bash
# 应用设计令牌
cp tokens.scss src/styles/

# 批量生成组件骨架
bash scripts/scaffold-vue-components.sh

# 运行单元测试
npx vitest run

# 启动 Storybook 文档
npm run storybook
```

## 配置示例

### CI/CD 组件质量门禁

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

## 最佳实践

1. **`<script setup lang="ts">` 优先**:Vue 3 最佳实践,类型安全且编译期优化最好。
2. **WCAG AA 内建**:组件默认支持键盘、屏幕阅读器与对比度,而非可选附加。
3. **设计令牌驱动**:样式引用令牌变量,支持暗色模式与主题切换。
4. **`aria-*` 属性显式声明**:disabled 用 `aria-disabled`,loading 用 `aria-busy`,pressed 用 `aria-pressed`。
5. **`focus-visible` 提供焦点样式**:键盘用户可见焦点,鼠标用户不干扰。
6. **每个组件配单元测试**:Vitest + Vue Test Utils,覆盖渲染、交互、可访问性。
7. **barrel 导出统一接口**:`index.ts` 导出所有组件,消费方按需引入。
8. **Storybook 文档同步**:每个组件配 stories,文档与实现通过 PR 审查保持一致。

## 常见问题

### Q1: 企业组件库如何发布与版本化?

将组件库配置为独立 npm 包,采用语义化版本(1.0.0),通过 CHANGELOG 记录变更。CI 中自动发布到私有 npm 注册表。

### Q2: 多项目如何复用组件库?

发布为私有 npm 包,各项目通过 `npm i @your-org/vue-components` 安装。配合语义化版本,实现可控升级。

### Q3: 可访问性测试如何自动化?

Vitest 中编写可访问性测试(键盘聚焦、aria 属性、对比度),CI 中运行。更深入测试推荐 `@axe/playwright`。

### Q4: 设计令牌如何与 Tailwind / UnoCSS 协同?

Tailwind:在 `tailwind.config.js` 中将令牌映射为 theme 字段;UnoCSS:在 `unocss.config.ts` 中将令牌映射为 theme 字段。

### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有单组件输出。个人开发者可继续使用免费版,团队场景启用 Pro 版获得企业级结构、批量生成与可访问性能力。两个版本可在同一仓库并存。

### Q6: 如何度量组件库健康度?

跟踪四个指标:组件复用率、WCAG AA 合规率、单元测试覆盖率、文档覆盖率。四者共同反映组件库健康度。

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 20 LTS+
- **Vue**:建议 3.3+
- **CI 平台**:GitHub Actions / GitLab CI / Jenkins

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Vue 3 | npm 包 | 必需 | `npm i vue` |
| TypeScript | npm 包 | 必需 | `npm i -D typescript` |
| vue-tsc | npm 包 | 必需 | `npm i -D vue-tsc` |
| vitest | 测试框架 | 必需 | `npm i -D vitest` |
| @vue/test-utils | 测试工具 | 必需 | `npm i -D @vue/test-utils` |
| sass | npm 包 | 推荐 | `npm i -D sass` |
| @storybook/vue3 | 文档工具 | 推荐 | `npx storybook init` |
| eslint-plugin-vue | npm 包 | 推荐 | `npm i -D eslint-plugin-vue` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 完全基于 Markdown 指令,无需额外 API Key
- 私有 npm 发布需配置 `NODE_AUTH_TOKEN` 环境变量
- 视觉回归工具(Chromatic)需配置 `CHROMATIC_TOKEN`
- 代码覆盖率上传(Codecov)需配置 `CODECOV_TOKEN`

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出企业级 Vue 组件工程方案;脚手架与测试脚本需在仓库中落地并由本地或 CI 执行
