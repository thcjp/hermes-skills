---
slug: "vue-component-generator"
name: "vue-component-generator"
version: 1.0.1
displayName: "Vue Component Genera"
summary: "生成 Vue 3 组件模板，支持 Composition API、Options API、TypeScript、SFC 单文件组件，一键生成完整"
license: "MIT"
description: |-
  生成 Vue 3 组件模板，支持 Composition API、Options API、TypeScript、SFC 单文件组件。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - Development
  - 工具
  - 效率
  - api
  - vue
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Vue Component Genera

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Vue Component Genera一键生成 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

* ⚡ 一键生成组件
* 📝 支持 TypeScript
* 🎯 Composition API / Options API
* 🎨 SCSS 样式支持
* 📖 Props/Emits 定义
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文件操作 | 文件路径与操作参数 | 操作结果与文件元信息 |
| 内容生成 | 提示词与风格参数 | 生成内容与质量评分 |
| 生成 Vue 3 组 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 基本用法

```bash
vue-component-generator MyButton --api composition
# ...
vue-component-generator MyModal --api options
# ...
vue-component-generator MyForm --typescript
```

### 选项

| 选项 | 说明 |
|---:|---:|
| `--api, -a` | API 类型 (composition/options) |
| `--typescript, -t` | 启用 TypeScript |
| `--scss, -s` | 启用 SCSS |
| `--output, -o` | 输出目录 |

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | vue-component-generator处理的内容输入 |,  |
| content | string | 否 | vue-component-generator处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "generator 相关配置参数",
    result: "generator 相关配置参数",
    result: "generator 相关配置参数",
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
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

```vue
<template>
  <div class="my-button">
    <button @click="handleClick">
      相关信息
    </button>
  </div>
</template>
# ...
<script setup>
import { ref } from 'vue'
# ...
const props = defineProps({
  label: {
    type: String,
    default: 'Click me'
  }
})
# ...
const emit = defineEmits(['click'])
# ...
const handleClick = () => {
  emit('click')
}
</script>
# ...
<style scoped>
.my-button {
  padding: 10px 20px;
}
</style>
```

## 常见问题

### Q1: 如何开始使用Vue Component Genera？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
