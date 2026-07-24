---
slug: "vue-toolkit"
name: "vue-toolkit"
version: 1.0.1
displayName: "Vue工具箱(专业版)"
summary: "Vue 3 全栈实战：响应式、性能优化、SSR、Pinia、Composable 架构与团队规范。"
license: "Proprietary"
edition: "pro"
description: |-
  Vue 工具箱（专业版）面向中高级 Vue 3 开发者与团队，在免费版陷阱清单的基础上新增性能优化、SSR/SSG、Pinia 状态管理、Composable 架构、可访问性、测试与团队规范六大模块。目标是让 Agent 能够输出"架构级"建议而不仅是单点修复。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - 前端架构
  - Vue
  - 性能优化
  - SSR
  - 状态管理
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# Vue工具箱(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

| 模块 | 能力点 | 价值 |
|:-----|:-----|:-----|
| 响应式进阶 | shallowRef、triggerRef、customRef、markRaw | 大对象性能优化 |
| 性能优化 | v-memo、defineAsyncComponent、Suspense、keep-alive | 首屏 < 1.5s |
| SSR/SSG | hydration、async setup、streaming、Nuxt 集成 | SEO 与首屏 |
| Pinia | setup store、storeToRefs、持久化、模块化 | 全局状态治理 |
| Composable | useXxx 设计模式、副作用回收、类型推导 | 逻辑复用 |
| 可访问性 | ARIA、键盘导航、焦点管理、对比度 | 合规与体验 |
| 测试 | Vitest、@vue/test-utils、组件快照、E2E | 回归保障 |
| TypeScript | 泛型组件、defineSlots、类型工具 | 类型安全 |
| 团队规范 | ESLint、目录约定、命名约定、PR 模板 | 协作效率 |
### 响应式进阶

针对响应式进阶,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供响应式进阶相关的配置参数、输入数据和处理选项.
**输出**: 返回响应式进阶的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`响应式进阶`的配置文档进行参数调优
### 性能优化

针对性能,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供性能优化相关的配置参数、输入数据和处理选项.
**输出**: 返回性能优化的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`性能优化`的配置文档进行参数调优
### SSR/SSG

针对SSR/SSG,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供SSR/SSG相关的配置参数、输入数据和处理选项.
**输出**: 返回SSR/SSG的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`SSR/SSG`的配置文档进行参数调优
#
## 适用场景

### 场景一：首屏性能优化（架构师视角）
项目首屏 LCP > 3s，需要系统性优化。Agent 应建议：① 路由级懒加载 `defineAsyncComponent`；② 大列表用 `v-memo` 或虚拟滚动；③ 静态内容用 `shallowRef` 避免深度响应式开销；④ 关键 CSS 内联，非关键 CSS 延迟加载.
### 场景二：SSR 落地评估（架构师视角）
团队考虑将 CSR 项目迁移到 SSR。Agent 应给出评估清单：① 是否有窗口对象依赖（需 polyfill 或客户端 only）；② 数据获取方式（async setup + Suspense）；③ 状态 hydration（Pinia + initialState）；④ 部署目标（Node 服务 vs Edge）.
### 场景三：Pinia 模块化（开发者视角）
单一 store 膨胀到 800 行。Agent 应建议按领域拆分为多个 setup store，用 `storeToRefs` 解构保持响应式，跨 store 调用通过 `useOtherStore()` 注入而非全局单例.
### 场景四：Composable 设计（开发者视角）
需要封装一个 `useFetch`。Agent 应提供完整模板：① 接收 url 与 options；② 返回 `{ data, error, loading, refresh }`；③ 内部用 `AbortController` 支持取消；④ 在 `onUnmounted` 中清理副作用.
### 场景五：可访问性合规（QA 视角）
组件库需要通过 WCAG AA。Agent 应检查：① 所有交互元素有 `aria-label`；② 模态框有焦点陷阱；③ 颜色对比度 ≥ 4.5:1；④ 键盘可完整操作（Tab/Enter/Esc）.
### 场景六：测试覆盖（QA 视角）
关键组件需要 100% 覆盖。Agent 应建议：① 纯逻辑用单元测试；② 组件渲染用 `@vue/test-utils` 的 `mount`；③ 异步用 `flushPromises`；④ 用户交互用 `userEvent`；⑤ 路由用 mock router.
## 使用流程

### 120 秒上手
1. 描述你的项目阶段（CRUD/SSR/性能瓶颈/团队规范）
2. Agent 会按"诊断 → 方案 → 代码 → 指标"四步输出
3. 复制代码到工程并运行基准测试验证指标

### 性能优化模板

```vue
<script setup lang="ts">
import { shallowRef, triggerRef, defineAsyncComponent } from 'vue'
# ...
// 大数据用 shallowRef 避免深度代理开销
const bigList = shallowRef<Array<{ id: number; name: string }>>([])
# ...
function updateList(newList: typeof bigList.value) {
  bigList.value = newList
  triggerRef(bigList) // 显式触发更新
}
# ...
// 路由级懒加载
const HeavyChart = defineAsyncComponent(() => import('./HeavyChart.vue'))
</script>
# ...
<template>
  <!-- v-memo 跳过未变化的项 -->
  <div v-for="item in bigList" :key="item.id" v-memo="[item.id, item.name]">
    vue-toolkit
  </div>
</template>
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | vue-toolkit处理的内容输入 |,  |
| content | string | 否 | vue-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
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
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Node.js**：18+（SSR 项目推荐 20+）
- **Vue 版本**：Vue 3.4+（专业版大量使用 `defineModel`、`shallowRef` 等新特性）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
- SSR 项目如对接 `关系型数据库` 数据库，连接串通过环境变量 `DATABASE_URL` 注入

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 GPT-4o / Claude Sonnet 以获得更高质量的架构建议

## 案例展示

### Pinia Setup Store 模板

```ts
// stores/user.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useAuthStore } from './auth'
// ...
export const useUserStore = defineStore('user', () => {
  const auth = useAuthStore() // 跨 store 注入
  const profile = ref<{ name: string; role: string } | null>(null)
// ...
  const isAdmin = computed(() => profile.value?.role === 'admin')
// ...
  async function fetchProfile() {
    if (!auth.token) throw new Error('未登录')
    profile.value = await fetch('/api/me', {
      headers: { Authorization: `Bearer ${auth.token}` }
    }).then((r) => r.json())
  }
// ...
  return { profile, isAdmin, fetchProfile }
})
```

### SSR 数据 Hydration

```ts
// entry-server.ts
import { createSSRApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
// ...
export async function createApp() {
  const app = createSSRApp(App)
  const pinia = createPinia()
  app.use(pinia)
// ...
  // 预取数据
  const userStore = useUserStore(pinia)
  await userStore.fetchProfile()
// ...
  // 序列化状态到 HTML
  const state = JSON.stringify(pinia.state.value)
  return { app, state }
}
```

### Composable 标准模板

```ts
// composables/useFetch.ts
import { ref, shallowRef, onUnmounted, type Ref } from 'vue'
// ...
export function useFetch<T>(url: string) {
  const data = shallowRef<T | null>(null) as Ref<T | null>
  const error = ref<Error | null>(null)
  const loading = ref(false)
  let controller: AbortController | null = null
// ...
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
// ...
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
// ...
describe('Button', () => {
  it('emits click event', async () => {
    const wrapper = mount(Button, { props: { label: 'Submit' } })
    await wrapper.trigger('click')
    expect(wrapper.emitted('click')).toHaveLength(1)
  })
})
```

## 常见问题

### Q1：shallowRef 与 ref 该怎么选？
A：当数据量大且结构深、但你只关心整体替换时用 `shallowRef`（如表格数据、图表数据集）。需要深度响应式时用 `ref` 或 `reactive`。改了 `shallowRef` 内部属性后需手动 `triggerRef` 触发更新.
### Q2：SSR 项目里 window 未定义怎么办？
A：使用 `import.meta.env.SSR`（Vite）或 `process.server`（Nuxt）做环境判断，把客户端 only 的逻辑放到 `onMounted` 中执行，或用 `<ClientOnly>` 组件包裹.
### 依赖说明(补充)
A：不会。Pinia 在 `defineStore` 工厂函数内调用 `useOtherStore()` 是惰性求值，只要不在模块顶层直接调用即可避免循环.
### Q4：Composable 里发请求怎么取消？
A：用 `AbortController`，在 `onUnmounted` 中调用 `controller.abort()`。同时支持外部传入 signal 以便父级统一取消.
### Q5：v-memo 什么场景下用？
A：仅在列表项渲染成本高且大部分项不变时使用。简单列表用 v-memo 反而增加开销。基线：单次渲染 > 5ms 的列表项才考虑.
### Q6：keep-alive 内存泄漏怎么排查？
A：① 检查 `include`/`max` 配置；② 在 `onDeactivated` 中清理定时器与监听；③ 用 Chrome DevTools Memory 面板对比快照.
### Q7：defineAsyncComponent 加载失败如何降级？
A：使用 `errorComponent` 与 `timeout` 选项，配合 `onErrorCaptured` 在父级兜底.
### Q8：Suspense 与 async setup 的坑？
A：① async setup 必须配合 Suspense，否则报错；② Suspense 没有内置错误处理，需用 `onErrorCaptured`；③ 多个异步子组件会等到全部完成才切换.
### Q9：Pinia 持久化怎么按字段白名单？
A：使用 `pinia-plugin-persistedstate`，在 store 中配置 `persist: { paths: ['token', 'profile'] }`.
### Q10：Vitest 测异步组件怎么等待？
A：用 `flushPromises` from `@vue/test-utils`，或 `await nextTick()`。涉及路由用 `vi.mock('vue-router')`.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

