---
slug: vue-component-generator
name: vue-component-generator
version: "1.0.0"
displayName: Vue Component Genera
summary: 生成 Vue 3 组件模板，支持 Composition API、Options API、TypeScript、SFC 单文件组件，快速生成完整
  Vue 组件代码。
license: MIT
description: |-
  生成 Vue 3 组件模板，支持 Composition API、Options API、TypeScript、SFC 单文件组件。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

# Vue Component Generator

快速生成专业的 Vue 3 组件代码。

## 功能

* ⚡ 快速生成组件
* 📝 支持 TypeScript
* 🎯 Composition API / Options API
* 🎨 SCSS 样式支持
* 📖 Props/Emits 定义

## 支持的 API

| API | 说明 |
| --- | --- |
| composition | Composition API (推荐) |
| options | Options API |
| script-setup | `<script setup>` 语法 |

## 组件类型

* 普通组件
* 路由组件
* 布局组件
* 表单组件

## 使用方法

### 基本用法

```bash
vue-component-generator MyButton --api composition

vue-component-generator MyModal --api options

vue-component-generator MyForm --typescript
```

### 选项

| 选项 | 说明 |
| --- | --- |
| `--api, -a` | API 类型 (composition/options) |
| `--typescript, -t` | 启用 TypeScript |
| `--scss, -s` | 启用 SCSS |
| `--output, -o` | 输出目录 |

## 示例

```vue
<template>
  <div class="my-button">
    <button @click="handleClick">
      {{ label }}
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  label: {
    type: String,
    default: 'Click me'
  }
})

const emit = defineEmits(['click'])

const handleClick = () => {
  emit('click')
}
</script>

<style scoped>
.my-button {
  padding: 10px 20px;
}
</style>
```

## 安装

```bash
```

## 变现思路

1. **组件库模板** - 销售专业组件库模板
2. **企业服务** - 定制 Vue 组件
3. **培训** - Vue 开发培训

## 更多示例

### 表单组件

```bash
vue-component-generator InputField --api composition --typescript
```

### 模态框

```bash
vue-component-generator Modal --api composition --scss
```

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

* ⚡ 快速生成组件
* 📝 支持 TypeScript
* 🎯 Composition API / Options API
* 🎨 SCSS 样式支持
* 📖 Props/Emits 定义

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Vue Component Genera？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Vue Component Genera有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制

Vue Component Generator 作为一款自动化生成 Vue 3 组件模板的工具，存在一些边界条件和限制，以下是该技能在实际使用中可能会遇到的限制：

### 输入限制

- **组件名称**: 组件名称应遵循 Vue 的命名规范，即使用 kebab-case 或 PascalCase，且不能包含特殊字符。
- **API 类型**: 支持的 API 类型有限，目前只支持 Composition API、Options API 和 `<script setup>` 语法。
- **文件路径**: 输出目录路径需存在，且 Agent 有权限在该路径下创建文件。

### 性能边界

- **组件复杂度**: 对于过于复杂的组件，生成器可能无法完全满足需求，需要手动调整或优化。
- **生成速度**: 生成大量组件时，生成速度可能会受到影响，具体取决于运行环境的性能。

### 兼容性约束

- **Vue 版本**: 目前只支持 Vue 3，不支持 Vue 2 及以下版本。
- **操作系统**: 在不同操作系统中，生成器的表现可能会有所差异，建议在 Windows、macOS 或 Linux 系统中使用。
- **Agent 平台**: 支持SKILL.md的任意AI Agent，但具体表现可能因 Agent 而异。

### TypeScript 限制

- **类型声明**: 支持基本的类型声明，但对于复杂的类型定义和接口，可能需要手动调整。
- **模块导入**: 生成器默认使用 ES6 模块语法，不支持 CommonJS 模块。

### SCSS 限制

- **样式嵌套**: 支持简单的嵌套样式，但对于复杂的嵌套结构，可能需要手动调整。
- **变量和函数**: 支持基本的变量和函数，但对于复杂的变量和函数定义，可能需要手动调整。

## 边界条件与限制

Vue Component Generator 作为一款自动化生成 Vue 3 组件模板的工具，存在一些边界条件和限制，以下是该技能在实际使用中可能会遇到的限制：

### 输入限制

- **组件名称**: 组件名称应遵循 Vue 的命名规范，即使用 kebab-case 或 PascalCase，且不能包含特殊字符。
- **API 类型**: 支持的 API 类型有限，目前只支持 Composition API、Options API 和 `<script setup>` 语法。
- **文件路径**: 输出目录路径需存在，且 Agent 有权限在该路径下创建文件。

### 性能边界

- **组件复杂度**: 对于过于复杂的组件，生成器可能无法完全满足需求，需要手动调整或优化。
- **生成速度**: 生成大量组件时，生成速度可能会受到影响，具体取决于运行环境的性能。

### 兼容性约束

- **Vue 版本**: 目前只支持 Vue 3，不支持 Vue 2 及以下版本。
- **操作系统**: 在不同操作系统中，生成器的表现可能会有所差异，建议在 Windows、macOS 或 Linux 系统中使用。
- **Agent 平台**: 支持SKILL.md的任意AI Agent，但具体表现可能因 Agent 而异。

### TypeScript 限制

- **类型声明**: 支持基本的类型声明，但对于复杂的类型定义和接口，可能需要手动调整。
- **模块导入**: 生成器默认使用 ES6 模块语法，不支持 CommonJS 模块。

### SCSS 限制

- **样式嵌套**: 支持简单的嵌套样式，但对于复杂的嵌套结构，可能需要手动调整。
- **变量和函数**: 支持基本的变量和函数，但对于复杂的变量和函数定义，可能需要手动调整。

---

## 差异化优势

### 与同类方案对比

在 Vue 组件生成领域，Vue Component Generator 与以下几种方案相比，展现出独特的优势：

1. **手动操作**：手动编写 Vue 组件代码虽然灵活，但效率低下，且容易出错。Vue Component Generator 通过自动化生成代码，大幅提升开发效率，减少因手动编写代码而可能出现的错误。

2. **其他工具**：虽然市面上存在一些其他 Vue 组件生成工具，但它们往往功能单一，无法满足多样化的需求。Vue Component Generator 支持多种 API 类型、组件类型和样式支持，满足不同场景下的开发需求。

3. **通用方法**：一些开发者可能会使用通用方法（如模板字符串）来生成组件代码，但这些方法缺乏灵活性，难以适应复杂场景。Vue Component Generator 提供了丰富的配置选项，能够满足各种复杂场景下的需求。

### 独特功能

1. **支持多种 API 类型**：Vue Component Generator 支持 Composition API、Options API 和 `<script setup>` 语法，满足不同开发者习惯和项目需求。

2. **支持 TypeScript**：Vue Component Generator 支持 TypeScript，为开发者提供更强大的类型检查和代码提示功能。

3. **SCSS 样式支持**：Vue Component Generator 支持 SCSS 样式，方便开发者编写复杂的样式。

4. **Props/Emits 定义**：Vue Component Generator 自动生成 Props 和 Emits 定义，减少手动编写代码的工作量。

5. **路由组件和布局组件支持**：Vue Component Generator 支持生成路由组件和布局组件，方便开发者快速搭建项目架构。

### 效率提升

使用 Vue Component Generator 可以带来以下效率提升：

1. **节省时间**：自动化生成代码，减少手动编写代码的工作量，节省大量时间。

2. **减少步骤**：通过配置选项，一键生成所需组件，减少开发步骤。

### 应用场景创新

1. **组件库模板**：Vue Component Generator 可用于快速搭建组件库模板，方便团队成员共享和复用组件。

2. **企业内部培训**：Vue Component Generator 可用于企业内部培训，帮助开发者快速掌握 Vue 组件开发技能。

3. **自动化工作流**：Vue Component Generator 可集成到自动化工作流中，实现组件的自动化生成和部署。

