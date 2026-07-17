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
  timing, and Composition A...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: avoid, mistakes, common, traps, vue, reactivity
tags:
- Integrations
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
