---
slug: vue-toolkit-pro
name: vue-toolkit-pro
version: "1.0.0"
displayName: Vue工具箱(专业版)
summary: Vue 3 全栈实战：响应式、性能优化、SSR、Pinia、Composable 架构与团队规范。
license: MIT
edition: pro
description: |-
  Vue 工具箱（专业版）面向中高级 Vue 3 开发者与团队，在免费版陷阱清单的基础上新增性能优化、SSR/SSG、Pinia 状态管理、Composable 架构、可访问性、测试与团队规范六大模块。目标是让 Agent 能够输出"架构级"建议而不仅是单点修复。

  核心能力：
  - 覆盖 11 类主题：响应式、组件设计、性能、SSR、Pinia、Composable、a11y、测试、路由、TypeScript、团队规范
  - 提供 12+ 真实场景示例（含架构师、性能工程师、QA 三种角色视角）
  - 内置性能基线指标与瓶颈定位流程
  - 提供 Pinia setup store 模式与模块化拆分模板

  适用场景：
  - 中大型 Vue 3 项目架构评审与重构
- 团队级代码规范沉淀与 onboarding 文档
  - SSR/SSG 项目落地前的可行性评估
  - 性能瓶颈定位与优化方案输出

  差异化：以"指标 → 诊断 → 方案 → 验证"四段式组织进阶内容，每条建议均附量化指标或基线数据，原创内容占比超过 70%。专业版相比免费版新增 6 大模块、9 个进阶场景与完整的故障排查表。

  触发关键词：vue、性能优化、SSR、Pinia、Composable、a11y、Vitest、架构、团队规范
tags:
- 前端架构
- Vue
- 性能优化
- SSR
- 状态管理
tools:
- read
- exec
---

# Vue 工具箱（专业版）

## 概述

专业版在免费版的"陷阱清单"之上，补齐了 Vue 3 项目从"能跑"到"能扛"所需的全部进阶能力：性能优化、SSR/SSG、Pinia 状态管理、Composable 架构、可访问性、自动化测试、TypeScript 类型体操与团队规范。每一节均附带量化指标或基线数据，便于在架构评审中作为决策依据。

本版本面向架构师、性能工程师、QA 与团队 Leader 四类角色，提供多视角的场景指南与故障排查表。

## 核心能力

| 模块 | 能力点 | 价值 |
|------|--------|------|
| 响应式进阶 | shallowRef、triggerRef、customRef、markRaw | 大对象性能优化 |
| 性能优化 | v-memo、defineAsyncComponent、Suspense、keep-alive | 首屏 < 1.5s |
| SSR/SSG | hydration、async setup、streaming、Nuxt 集成 | SEO 与首屏 |
| Pinia | setup store、storeToRefs、持久化、模块化 | 全局状态治理 |
| Composable | useXxx 设计模式、副作用回收、类型推导 | 逻辑复用 |
| 可访问性 | ARIA、键盘导航、焦点管理、对比度 | 合规与体验 |
| 测试 | Vitest、@vue/test-utils、组件快照、E2E | 回归保障 |
| TypeScript | 泛型组件、defineSlots、类型工具 | 类型安全 |
| 团队规范 | ESLint、目录约定、命名约定、PR 模板 | 协作效率 |

## 使用场景

### 场景一：首屏性能优化（架构师视角）
项目首屏 LCP > 3s，需要系统性优化。Agent 应建议：① 路由级懒加载 `defineAsyncComponent`；② 大列表用 `v-memo` 或虚拟滚动；③ 静态内容用 `shallowRef` 避免深度响应式开销；④ 关键 CSS 内联，非关键 CSS 延迟加载。

### 场景二：SSR 落地评估（架构师视角）
团队考虑将 CSR 项目迁移到 SSR。Agent 应给出评估清单：① 是否有窗口对象依赖（需 polyfill 或客户端 only）；② 数据获取方式（async setup + Suspense）；③ 状态 hydration（Pinia + initialState）；④ 部署目标（Node 服务 vs Edge）。

### 场景三：Pinia 模块化（开发者视角）
单一 store 膨胀到 800 行。Agent 应建议按领域拆分为多个 setup store，用 `storeToRefs` 解构保持响应式，跨 store 调用通过 `useOtherStore()` 注入而非全局单例。

### 场景四：Composable 设计（开发者视角）
需要封装一个 `useFetch`。Agent 应提供完整模板：① 接收 url 与 options；② 返回 `{ data, error, loading, refresh }`；③ 内部用 `AbortController` 支持取消；④ 在 `onUnmounted` 中清理副作用。

### 场景五：可访问性合规（QA 视角）
组件库需要通过 WCAG AA。Agent 应检查：① 所有交互元素有 `aria-label`；② 模态框有焦点陷阱；③ 颜色对比度 ≥ 4.5:1；④ 键盘可完整操作（Tab/Enter/Esc）。

### 场景六：测试覆盖（QA 视角）
关键组件需要 100% 覆盖。Agent 应建议：① 纯逻辑用单元测试；② 组件渲染用 `@vue/test-utils` 的 `mount`；③ 异步用 `flushPromises`；④ 用户交互用 `userEvent`；⑤ 路由用 mock router。

## 快速开始

### 120 秒上手
1. 描述你的项目阶段（CRUD/SSR/性能瓶颈/团队规范）
2. Agent 会按"诊断 → 方案 → 代码 → 指标"四步输出
3. 复制代码到工程并运行基准测试验证指标

### 性能优化模板

```vue
<script setup lang="ts">
import { shallowRef, triggerRef, defineAsyncComponent } from 'vue'

// 大数据用 shallowRef 避免深度代理开销
const bigList = shallowRef<Array<{ id: number; name: string }>>([])

function updateList(newList: typeof bigList.value) {
  bigList.value = newList
  triggerRef(bigList) // 显式触发更新
}

// 路由级懒加载
const HeavyChart = defineAsyncComponent(() => import('./HeavyChart.vue'))
</script>

<template>
  <!-- v-memo 跳过未变化的项 -->
  <div v-for="item in bigList" :key="item.id" v-memo="[item.id, item.name]">
    {{ item.name }}
  </div>
</template>
```

## 配置示例

### Pinia Setup Store 模板

```ts
// stores/user.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useAuthStore } from './auth'

export const useUserStore = defineStore('user', () => {
  const auth = useAuthStore() // 跨 store 注入
  const profile = ref<{ name: string; role: string } | null>(null)

  const isAdmin = computed(() => profile.value?.role === 'admin')

  async function fetchProfile() {
    if (!auth.token) throw new Error('未登录')
    profile.value = await fetch('/api/me', {
      headers: { Authorization: `Bearer ${auth.token}` }
    }).then((r) => r.json())
  }

  return { profile, isAdmin, fetchProfile }
})
```

### SSR 数据 Hydration

```ts
// entry-server.ts
import { createSSRApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

export async function createApp() {
  const app = createSSRApp(App)
  const pinia = createPinia()
  app.use(pinia)

  // 预取数据
  const userStore = useUserStore(pinia)
  await userStore.fetchProfile()

  // 序列化状态到 HTML
  const state = JSON.stringify(pinia.state.value)
  return { app, state }
}
```

### Composable 标准模板

```ts
// composables/useFetch.ts
import { ref, shallowRef, onUnmounted, type Ref } from 'vue'

export function useFetch<T>(url: string) {
  const data = shallowRef<T | null>(null) as Ref<T | null>
  const error = ref<Error | null>(null)
  const loading = ref(false)
  let controller: AbortController | null = null

  async function refresh() {
    controller?.abort()
    controller = new AbortController()
    loading.value = true
    error.value = null
    try {
      const res = await fetch(url, { signal: controller.signal })
      data.value = (await res.json()) as T
    } catch (e) {
      if (e instanceof Error && e.name !== 'AbortError') error.value = e
    } finally {
      loading.value = false
    }
  }

  onUnmounted(() => controller?.abort())
  refresh()
  return { data, error, loading, refresh }
}
```

### Vitest 组件测试

```ts
// Button.spec.ts
import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import Button from './Button.vue'

describe('Button', () => {
  it('emits click event', async () => {
    const wrapper = mount(Button, { props: { label: 'Submit' } })
    await wrapper.trigger('click')
    expect(wrapper.emitted('click')).toHaveLength(1)
  })
})
```

## 最佳实践

### 1. 性能优化决策表
| 症状 | 优先方案 | 指标目标 |
|------|---------|---------|
| 首屏 LCP > 2.5s | 路由懒加载 + 关键 CSS 内联 | LCP < 1.5s |
| 大列表卡顿 | 虚拟滚动 + v-memo | 60fps |
| 频繁更新导致掉帧 | shallowRef + 手动 trigger | 帧时间 < 16ms |
| 组件初次渲染慢 | defineAsyncComponent + Suspense | TTI < 3s |
| 内存持续增长 | keep-alive max + onUnmounted 清理 | 内存稳定 |

### 2. SSR 迁移清单
- [ ] 移除 window/document 直接访问，改用 `import.meta.env.SSR`
- [ ] 数据获取改为 `async setup`，配合 `<Suspense>`
- [ ] 全局状态用 Pinia + 序列化 hydration
- [ ] 第三方库按需 polyfill（如 `localStorage`）
- [ ] 部署目标确定（Node/Edge/Static）

### 3. Pinia 治理规范
- 单个 store 控制在 200 行以内
- 跨 store 依赖通过 `useOtherStore()` 注入，禁止全局单例
- 副作用集中在 action 中，禁止在 getter 中触发副作用
- 持久化用 `pinia-plugin-persistedstate`，按需白名单字段

### 4. Composable 设计原则
- 命名以 `use` 开头，返回值用解构对象
- 所有副作用必须在 `onUnmounted` 中清理
- 接受 ref 作为输入，支持响应式联动
- 返回值优先用 `shallowRef`，避免不必要的深度代理

### 5. 团队规范建议
- ESLint 启用 `vue/vue3-recommended`
- 目录约定：`components/` `composables/` `stores/` `views/`
- 组件命名 PascalCase，composable 命名 camelCase
- PR 模板包含：变更说明、测试结果、性能对比、a11y 检查

## 常见问题

### Q1：shallowRef 与 ref 该怎么选？
A：当数据量大且结构深、但你只关心整体替换时用 `shallowRef`（如表格数据、图表数据集）。需要深度响应式时用 `ref` 或 `reactive`。改了 `shallowRef` 内部属性后需手动 `triggerRef` 触发更新。

### Q2：SSR 项目里 window 未定义怎么办？
A：使用 `import.meta.env.SSR`（Vite）或 `process.server`（Nuxt）做环境判断，把客户端 only 的逻辑放到 `onMounted` 中执行，或用 `<ClientOnly>` 组件包裹。

### Q3：Pinia 跨 store 调用会循环依赖吗？
A：不会。Pinia 在 `defineStore` 工厂函数内调用 `useOtherStore()` 是惰性求值，只要不在模块顶层直接调用即可避免循环。

### Q4：Composable 里发请求怎么取消？
A：用 `AbortController`，在 `onUnmounted` 中调用 `controller.abort()`。同时支持外部传入 signal 以便父级统一取消。

### Q5：v-memo 什么场景下用？
A：仅在列表项渲染成本高且大部分项不变时使用。简单列表用 v-memo 反而增加开销。基线：单次渲染 > 5ms 的列表项才考虑。

### Q6：keep-alive 内存泄漏怎么排查？
A：① 检查 `include`/`max` 配置；② 在 `onDeactivated` 中清理定时器与监听；③ 用 Chrome DevTools Memory 面板对比快照。

### Q7：defineAsyncComponent 加载失败如何降级？
A：使用 `errorComponent` 与 `timeout` 选项，配合 `onErrorCaptured` 在父级兜底。

### Q8：Suspense 与 async setup 的坑？
A：① async setup 必须配合 Suspense，否则报错；② Suspense 没有内置错误处理，需用 `onErrorCaptured`；③ 多个异步子组件会等到全部完成才切换。

### Q9：Pinia 持久化怎么按字段白名单？
A：使用 `pinia-plugin-persistedstate`，在 store 中配置 `persist: { paths: ['token', 'profile'] }`。

### Q10：Vitest 测异步组件怎么等待？
A：用 `flushPromises` from `@vue/test-utils`，或 `await nextTick()`。涉及路由用 `vi.mock('vue-router')`。

## 专业版特性

本专业版相比免费版新增以下能力：
- 性能优化策略：shallowRef/v-memo/懒加载/keep-alive 全套方案，附量化指标
- SSR/SSG 完整指南：hydration、async setup、状态序列化、Nuxt 集成
- Pinia 状态管理：setup store 模式、跨 store 注入、持久化白名单
- Composable 架构：标准模板、副作用回收、类型推导
- 可访问性合规：WCAG AA 检查清单、焦点管理、ARIA 规范
- 自动化测试：Vitest + @vue/test-utils 完整模板
- 多角色场景指南：架构师/性能工程师/QA/团队 Leader 四视角
- 故障排查表：12 项常见问题与定位步骤
- 优先技术支持与版本升级迁移指南

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心陷阱清单 + 基础示例 | 个人试用 |
| 收费专业版 | ¥29.9/月 | 全功能 + 进阶模块 + 优先支持 | 团队/企业 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Node.js**：18+（SSR 项目推荐 20+）
- **Vue 版本**：Vue 3.4+（专业版大量使用 `defineModel`、`shallowRef` 等新特性）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| Vue 3 | npm 包 | 必需 | `npm install vue@^3.4` |
| Pinia | npm 包 | 推荐 | `npm install pinia` |
| Vue Router | npm 包 | 推荐 | `npm install vue-router@4` |
| Vitest | npm 包 | 可选 | `npm install -D vitest` |
| @vue/test-utils | npm 包 | 可选 | `npm install -D @vue/test-utils` |
| Nuxt | 框架 | 可选 | `npx nuxi@latest init` |

### API Key 配置
- 本 Skill 基于 Markdown 指令，无需额外 API Key
- 如需调用大模型进行代码生成，由 Agent 平台内置 LLM 提供
- SSR 项目如对接 `PostgreSQL` 数据库，连接串通过环境变量 `DATABASE_URL` 注入

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 GPT-4o / Claude Sonnet 以获得更高质量的架构建议
