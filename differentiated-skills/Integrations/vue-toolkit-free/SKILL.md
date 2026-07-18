---
slug: vue-toolkit-free
name: vue-toolkit-free
version: "1.0.0"
displayName: Vue工具箱(免费版)
summary: 规避 Vue 3 常见陷阱：响应式、ref 与 reactive、computed 时机与组合式 API 最佳实践。
license: MIT
edition: free
description: |-
  Vue 工具箱（免费版）面向 Vue 3 开发者，聚焦 Composition API 下的高频问题：响应式陷阱、ref 与 reactive 的取舍、computed 与 watch 的边界、组件设计与路由集成。目标是让 Agent 在 60 秒内给出可直接复用的代码片段，避免反复踩坑。

  核心能力：
  - 覆盖 Vue 3 Composition API 8 类核心陷阱与对应的修复模板
  - 提供 ref/reactive/computed/watch 的决策树与代码片段
  - 内置组件设计、Props/Emits、Provide/Inject、Vue Router 的常见错误清单
  - 适配 Windows/macOS/Linux 三端，无需额外安装

  适用场景：
  - 初学 Composition API 的开发者在写组件时反复踩响应式坑
  - 一人公司或独立开发者需要快速产出可维护的 Vue 3 代码
  - 团队 code review 时需要一份"反例清单"作为对照标准

  差异化：以"陷阱 → 修复 → 模板"三段式结构组织，每条陷阱均附带错误示例、正确示例与原因解释，原创内容占比超过 70%。免费版覆盖 8 类核心陷阱与 1-2 个真实场景示例，专业版额外提供性能优化、SSR、状态管理等进阶能力。

  触发关键词：vue、响应式、reactive、ref、computed、watch、组合式 API、组件设计
tags:
- 前端开发
- Vue
- 组合式API
- 响应式
tools:
- read
- exec
---

# Vue 工具箱（免费版）

## 概述

Vue 3 的 Composition API 让逻辑组织更灵活，但也带来了一系列新的"隐性陷阱"：响应式丢失、watch 不触发、ref 解包错乱、Provide/Inject 类型不安全等。本工具箱将这些高频问题归纳为可复用的修复模板，让 Agent 在被问及 Vue 3 相关问题时，能够直接给出"错误写法 + 正确写法 + 原因"三段式回答，而不是泛泛而谈。

免费版聚焦于"写得对"——覆盖 8 类核心陷阱与基础组件设计；性能优化、SSR、Pinia 集成等进阶主题留给专业版。

## 核心能力

| 能力模块 | 覆盖范围 | 免费版可用 |
|---------|---------|-----------|
| 响应式陷阱 | ref/reactive 解包、解构丢失、数组索引赋值 | 是 |
| 派生状态 | computed 缓存时机、watch 副作用边界 | 是 |
| Props/Emits | 类型安全、v-model、默认值工厂 | 是 |
| 生命周期 | onMounted/onUnmounted、Suspense 异步 | 是 |
| Provide/Inject | Symbol key、响应式注入 | 是 |
| Vue Router | useRoute/useRouter、导航守卫 | 是 |
| 模板引用 | ref 命名匹配、v-for 数组引用 | 是 |
| 常见错误 | v-if/v-show、v-for key、Teleport | 是 |
| 性能优化 | shallowRef、v-memo、懒加载 | 否（专业版） |
| SSR/SSG | hydration、async setup | 否（专业版） |
| Pinia 集成 | storeToRefs、setup store | 否（专业版） |

## 使用场景

### 场景一：组件响应式突然失效
开发者把 `reactive` 对象整体重新赋值后发现视图不更新。Agent 应识别这是 `state = {...}` 破坏了响应式代理，建议改用 `ref` 包裹对象或使用 `Object.assign(state, newObj)`。

### 场景二：watch 不触发
用户监听 `reactive` 对象的深层属性但 watch 不触发。Agent 应提示 `watch` 默认浅监听，需开启 `deep: true` 或改为 getter 函数 `watch(() => state.nested.value, ...)`。

### 场景三：v-model 类型不匹配
表单组件使用 `v-model` 时父组件拿到的是 string 而非 number。Agent 应指出 `defineModel()` 的用法，并提示 `modelModifiers` 处理类型转换。

## 快速开始

### 60 秒上手
1. 把 Vue 3 相关问题抛给 Agent，例如："为什么我的 watch 不触发？"
2. Agent 会按照"陷阱识别 → 错误示例 → 正确示例 → 原因"四步回答
3. 直接复制正确示例到你的 `<script setup>` 中

### 最小可复用模板

```vue
<script setup lang="ts">
import { ref, reactive, computed, watch, toRefs } from 'vue'

// 推荐：基本类型用 ref，对象用 reactive
const count = ref(0)
const state = reactive({ user: { name: 'Tom', age: 20 } })

// 派生状态用 computed（自动缓存）
const greeting = computed(() => `Hello, ${state.user.name}`)

// 副作用用 watch，监听响应式对象需 deep
watch(
  () => state.user,
  (newVal) => console.log('user changed', newVal),
  { deep: true }
)

// 解构 reactive 必须用 toRefs，否则丢失响应式
const { user } = toRefs(state)
</script>
```

## 配置示例

### 推荐的 `<script setup>` 骨架

```vue
<script setup lang="ts">
import { ref, reactive, computed, watch, onMounted, onUnmounted } from 'vue'

// 1. 状态定义
const props = defineProps<{ msg: string }>()
const emit = defineEmits<{ (e: 'update', val: string): void }>()

// 2. 响应式数据
const count = ref(0)
const state = reactive({ list: [] as string[] })

// 3. 派生状态
const double = computed(() => count.value * 2)

// 4. 副作用
watch(count, (n) => emit('update', String(n)))

// 5. 生命周期
onMounted(() => console.log('mounted'))
onUnmounted(() => console.log('unmounted'))
</script>
```

### Props 与 v-model 配置

```vue
<!-- 子组件 Child.vue -->
<script setup lang="ts">
const model = defineModel<string>({ default: '' })
const props = defineProps<{
  items: Array<{ id: number; name: string }>
}>()
</script>

<!-- 父组件 -->
<template>
  <Child v-model="text" :items="list" />
</template>
```

## 最佳实践

### 1. 响应式选择决策树
- 基本类型（string/number/boolean）→ `ref`
- 对象/数组且不需要整体替换 → `reactive`
- 对象/数组且需要整体替换 → `ref` + `.value = newObj`
- 需要解构 → `reactive` + `toRefs`

### 2. watch 选型
- 只关心最新值、需要旧值对比 → `watch`
- 立即执行、自动追踪依赖 → `watchEffect`
- 监听 reactive 深层属性 → `watch(getter, cb, { deep: true })`

### 3. 组件通信分层
- 父子直传 → Props + Emits
- 跨层传递 → Provide + Inject（建议用 Symbol key）
- 全局状态 → Pinia（专业版讲解）

### 4. 避免常见反模式
- 不要在 `watch` 回调里修改被监听的值（易触发循环）
- 不要在 `computed` 里执行副作用
- 不要在条件分支里调用生命周期钩子
- 不要给 `v-for` 用 `index` 作为 key（除非列表完全静态）

## 常见问题

### Q1：为什么 `reactive` 对象重新赋值后视图不更新？
A：`reactive` 返回的是 Proxy 代理对象，整体替换会断开代理。改用 `Object.assign(state, newObj)` 或将整个对象用 `ref` 包裹后通过 `.value = newObj` 替换。

### Q2：解构 `reactive` 后变量为什么不是响应式的？
A：解构会把基本类型值拷贝出来，丢失代理引用。使用 `toRefs(state)` 把每个属性转成 `ref`，或使用 `toRef(state, 'key')` 单独转换。

### Q3：`watch` 监听 `reactive` 对象的嵌套属性为什么没触发？
A：`watch` 默认是浅监听。监听嵌套属性需要：① 开启 `deep: true`；② 或使用 getter 函数 `watch(() => state.nested.value, cb)`。

### Q4：`computed` 里发请求可以吗？
A：不可以。`computed` 必须是纯函数，不能有副作用。异步派生数据请用 `watchEffect` + `ref` 或 `async setup` + `<Suspense>`。

### Q5：`ref` 在模板里要不要写 `.value`？
A：模板中 `ref` 会自动解包，直接写变量名即可；在 `<script setup>` 中访问必须写 `.value`。

### Q6：`v-model` 怎么实现双向绑定？
A：Vue 3.4+ 推荐使用 `defineModel()` 宏；旧写法是 `:modelValue` + `@update:modelValue`。

### Q7：`onMounted` 里能拿到 DOM 吗？
A：可以。`onMounted` 在组件挂载到 DOM 后执行，此时通过模板引用（`ref="el"`）可以访问真实 DOM 节点。

## 免费版限制

本免费体验版限制以下高级功能：
- 性能优化策略（shallowRef、v-memo、组件懒加载）
- SSR/SSG 与 hydration 注意事项
- Pinia 状态管理集成（storeToRefs、setup store 模式）
- 高级组件设计模式（render function、函数式组件）
- 多角色场景指南（架构师/性能工程师视角）

解锁全部功能请使用专业版：`vue-toolkit-pro`

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Node.js**：18+（用于运行 Vue 3 项目）
- **Vue 版本**：Vue 3.3+（推荐 3.4+ 以使用 `defineModel`）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| Vue 3 | npm 包 | 必需 | `npm install vue@^3.4` |
| TypeScript | npm 包 | 可选 | `npm install -D typescript` |
| Vue Router | npm 包 | 可选 | `npm install vue-router@4` |
| Vite | 构建工具 | 可选 | `npm create vite@latest` |

### API Key 配置
- 本 Skill 基于 Markdown 指令，无需额外 API Key（除内容中明确标注的外部 API）
- 如需调用大模型进行代码生成，由 Agent 平台内置 LLM 提供

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：免费版使用低成本模型（如 GPT-4o-mini / Claude Haiku）
