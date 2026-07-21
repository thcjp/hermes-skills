---
slug: vue
name: vue
version: "1.0.1"
displayName: Vue
summary: Avoid common Vue mistakes — reactivity traps, ref vs reactive, computed timing,
  and Composition A...
license: MIT
description: |-
  Avoid common Vue mistakes — reactivity traps, ref vs reactive, computed
  timing, and Composition A。Use when 用户需要Vue相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---

# Vue

## When to Use

User needs Vue expertise — from Composition API patterns to production optimization. Agent handles reactivity, component design, state management, and performance.

## Quick Reference

| Topic | File |
| --- | --- |
| Reactivity patterns | `reactivity.md` |
| Component patterns | `components.md` |
| Composables design | `composables.md` |
| Performance optimization | `performance.md` |

## Composition API Philosophy

* Composition API is not about replacing Options API—it's about better code organization
* Group code by feature, not by option type—related logic stays together
* Extract reusable logic into composables—the main win of Composition API
* `<script setup>` is the recommended syntax—cleaner and better performance

## Reactivity Traps

* `ref` for primitives—access with `.value` in script, auto-unwrapped in template
* `reactive` can't reassign whole object—`state = {...}` breaks reactivity
* Destructuring `reactive` loses reactivity—use `toRefs(state)` to preserve
* Array index assignment reactive in Vue 3—`arr[0] = x` works, unlike Vue 2
* Nested refs unwrap inside reactive—`reactive({count: ref(0)}).count` is number, not ref

## Watch vs Computed

* `computed` for derived state—cached, recalculates only when dependencies change
* `watch` for side effects—when you need to DO something in response to changes
* `computed` should be pure—no side effects, no async
* `watchEffect` for immediate reaction with auto-tracked dependencies

## Watch Traps

* Watching reactive object needs `deep: true`—or watch a getter function
* `watch` is lazy by default—use `immediate: true` for initial run
* Watch callback receives old/new—`watch(source, (newVal, oldVal) => {})`
* `watchEffect` can't access old value—use `watch` if you need old/new comparison
* Stop watchers with returned function—`const stop = watch(...); stop()`

## Props and Emits Traps

* `defineProps` for type-safe props—`defineProps<{ msg: string }>()`
* Props are readonly—don't mutate, emit event to parent
* `defineEmits` for type-safe events—`defineEmits<{ (e: 'update', val: string): void }>()`
* `v-model` is `:modelValue` + `@update:modelValue`—custom v-model with `defineModel()`
* Default value for objects must be factory function—`default: () => ({})`

## Template Ref Traps

* `ref="name"` + `const name = ref(null)`—names must match exactly
* Template refs available after mount—access in `onMounted`, not during setup
* `ref` on component gives component instance—`ref` on element gives DOM element
* Template ref with `v-for` becomes array of refs

## Lifecycle Traps

* `onMounted` for DOM access—component mounted to DOM
* `onUnmounted` for cleanup—subscriptions, timers, event listeners
* `onBeforeMount` runs before DOM insert—rarely needed but exists
* Hooks must be called synchronously in setup—not inside callbacks or conditionals
* Async setup needs `<Suspense>` wrapper

## Provide/Inject Traps

* `provide('key', value)` in parent—`inject('key')` in any descendant
* Reactive if value is ref/reactive—otherwise static snapshot
* Default value: `inject('key', defaultVal)`—third param for factory function
* Symbol keys for type safety—avoid string key collisions

## Vue Router Traps

* `useRoute` for current route—reactive, use in setup
* `useRouter` for navigation—`router.push('/path')`
* Navigation guards: `beforeEach`, `beforeResolve`, `afterEach`—return `false` to cancel
* `<RouterView>` with named views—multiple views per route

## Common Mistakes

* `v-if` vs `v-show`—v-if removes from DOM, v-show toggles display
* Key on `v-for` required—`v-for="item in items" :key="item.id"`
* Event modifiers order matters—`.prevent.stop` vs `.stop.prevent`
* Teleport for modals—`<Teleport to="body">` renders outside component tree

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Avoid common Vue mistakes — reactivity traps, ref vs reactive, computed
  timing, and Composition A
- 触发关键词: avoid, mistakes, common, traps, vue, reactivity

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Vue？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Vue有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
