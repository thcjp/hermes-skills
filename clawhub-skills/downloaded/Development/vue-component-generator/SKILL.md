---
slug: vue-component-generator
name: vue-component-generator
version: "1.0.0"
displayName: Vue Component Genera
summary: 生成 Vue 3 组件模板，支持 Composition API、Options API、TypeScript、SFC 单文件组件，一键生成完整
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

* ⚡ 一键生成组件
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

* ⚡ 一键生成组件
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
