---
slug: vue-component-generator
name: vue-component-generator
version: "1.0.0"
displayName: Vue Component Generator
summary: 生成 Vue 3 组件模板，支持 Composition API、Options API、TypeScript、SFC 单文件组件，一键生成完整
  Vue 组件代码。
license: MIT
description: |-
  生成 Vue 3 组件模板，支持 Composition API、Options API、TypeScript、SFC 单文件组件，一键生成完整
  Vue 组件代码。

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: composition, generator, typescript, component, 支持, 一键生成完整, 单文件组件, vue
tags:
- Development
tools:
- read
- exec
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

## 输出示例

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
