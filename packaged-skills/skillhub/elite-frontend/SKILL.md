---

slug: "elite-frontend"
name: "elite-frontend"
version: 1.0.1
displayName: "精英前端设计-专业版"
summary: "企业级前端设计系统，支持多页面应用、React/Vue组件、品牌一致性与高级动效编排。。精英前端设计工具专业版，面向团队的企业级前端设计系统。核心能力： - 多页面应用设计，统一视觉语言贯穿"
license: "Proprietary"
edition: "pro"
description: |-
  精英前端设计工具专业版，面向团队的企业级前端设计系统。核心能力：
  - 多页面应用设计，统一视觉语言贯穿全站
  - React/Vue 组件库生成，含 TypeScript 类型定义
  - 高级动效编排，Framer Motion / Vue Transition 深度集成
  - 品牌设计系统，色彩/字体/间距/组件规范化
  - 设计令牌（Design Token）自动生成与管理
  - 响应式适配策略，多断点一致体验
  - 可访问性合规...
tags: Frontend,工具,代码,vue,typescript,json
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# 精英前端设计-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 精英前端设计-专业版一致性与高级动效编排 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

### 能力对比
| 能力维度 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 输出格式 | HTML/CSS | HTML/CSS + React + Vue + TypeScript |
| 页面范围 | 单页面 | 多页面应用全站 |
| 组件管理 | 无 | 组件库 + TypeScript 类型 |
| 动效方案 | CSS @keyframes | CSS + Framer Motion + Vue Transition |
| 设计系统 | 规范指导 | Design Token 自动生成与管理 |
| 品牌管理 | 不支持 | 品牌色彩/字体/间距规范化 |
| 响应式 | 基础 | 多断点策略 + 一致性保障 |
| 可访问性 | 基础 | WCAG 合规检查 |

**输入**: 用户提供能力对比所需的指令和必要参数.
### 核心能力(补充)
```text
多页面应用:
  - 统一视觉语言贯穿全站
  - 页面间导航动效一致性
  - 布局系统复用
  - 路由级动画过渡
# ...
组件库生成:
  - React 组件（含 TypeScript 类型定义）
  - Vue 组件（含 Composition API）
  - 组件 Props/Events/Slots 规范
  - 组件文档与示例
# ...
高级动效:
  - Framer Motion: staggerChildren, whileHover, layoutId
  - Vue: <Transition> + <TransitionGroup>
  - 页面级转场动画
  - 滚动驱动动效
# ...
设计系统:
  - Design Token 自动生成
  - 色彩系统（主色/强调/语义色/中性色）
  - 字体系统（标题/正文/代码 + 字重/字号阶梯）
  - 间距系统（4px 基准 + 语义间距）
  - 组件规范（圆角/阴影/边框）
# ...
品牌管理:
  - 品牌色彩体系
  - 品牌字体规范
  - 品牌组件风格
  - 一致性自动校验
# ...
响应式策略:
  - 多断点设计（mobile/tablet/desktop/wide）
  - 流式布局 + 自适应排版
  - 触摸/鼠标交互适配
# ...
可访问性:
  - WCAG 2.1 AA 合规
  - 语义化 HTML
  - ARIA 标签
  - 键盘导航支持
```

**输入**: 用户提供核心能力所需的指令和必要参数.
**处理**: 解析核心能力的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 能力维度

针对能力维度,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力维度相关的配置参数、输入数据和处理选项.
**输出**: 返回能力维度的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力维度`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：企业级 Web 应用全站设计
为 SaaS 产品设计完整的多页面应用界面.
> 详细代码示例已移至 `references/detail.md`

### 场景二：设计系统与 Design Token 生成
自动生成完整的设计系统配置.
### 场景三：Vue 组件库生成
```vue
<!-- Vue 3 + Composition API 组件示例 -->
<template>
  <TransitionGroup name="stagger" tag="div" class="card-grid">
    <div
      v-for="(card, index) in cards"
      :key="card.id"
      class="card"
      :style="{ '--delay': `${index * 0.1}s` }"
    >
      <h3>elite-frontend</h3>
      <p>frontend 相关配置参数</p>
    </div>
  </TransitionGroup>
</template>
# ...
<script setup lang="ts">
import { ref } from 'vue';
# ...
interface Card {
  id: string;
  title: string;
  content: string;
}
# ...
const cards = ref<Card[]>([
  { id: '1', title: '设计系统', content: '统一的视觉语言' },
  { id: '2', title: '组件库', content: '可复用的 UI 组件' },
  { id: '3', title: '品牌一致性', content: '全站统一规范' },
]);
</script>
# ...
<style scoped>
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}
# ...
.card {
  background: var(--color-bg-secondary, #16213e);
  border: 1px solid rgba(233, 69, 96, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
}
# ...
/* TransitionGroup 交错动效 */
.stagger-enter-active {
  transition: all 0.6s ease;
  transition-delay: var(--delay, 0s);
}
.stagger-enter-from {
  opacity: 0;
  transform: translateY(24px);
}
</style>
```

## 使用流程

### 优秀步：定义品牌配置
```json
{
  "brand": {
    "name": "Acme",
    "colors": {
      "primary": "#1a1a2e",
      "secondary": "#16213e",
      "accent": "#e94560"
    },
    "typography": {
      "heading": "Playfair Display",
      "body": "IBM Plex Sans",
      "mono": "JetBrains Mono"
    }
  }
}
```

### 第二步：生成设计系统
```bash
python3 generate-design-system.py --brand brand.json --output tokens.css
# ...
```

### 第三步：生成组件库
```bash
generate-components --framework react --typescript --tokens tokens.json
# ...
generate-components --framework vue --typescript --tokens tokens.json
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | elite-frontend处理的内容输入 |,  |
| content | string | 否 | elite-frontend处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "frontend 相关配置参数",
    result: "frontend 相关配置参数",
    result: "frontend 相关配置参数",
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
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（组件构建工具需要）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js 16+ | 运行时 | 必需 | nodejs.org 官方下载 |
| Framer Motion | 库 | 可选 | `npm install framer-motion`（React动效） |
| Vue 3 | 框架 | 可选 | `npm install vue`（Vue项目） |
| TypeScript | 语言 | 可选 | `npm install -D typescript` |
| Google Fonts | 字体 | 可选 | CDN免费加载 |

### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- Google Fonts 通过 CDN 免费加载

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 企业级AI Skill，支持多页面应用、组件库与设计系统管理
- **适用规模**: 团队与企业级，多页面应用全站设计
- **兼容性**: 与免费版设计规范完全兼容，支持无缝升级

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q: 如何从免费版升级到专业版？
A: 免费版的字体、色彩和动效规则在专业版中完整保留。专业版新增设计系统生成、组件库和品牌管理能力，无需迁移已有代码.
### Q: 支持 React 和 Vue 吗？
A: 专业版同时支持 React（含 TypeScript + Framer Motion）和 Vue 3（含 Composition API + Transition），可根据项目需求选择.
### Q: Design Token 支持哪些输出格式？
A: 支持 CSS 变量、JSON、TypeScript 类型定义三种格式，可同时导出供不同消费端使用.
### Q: 组件库生成后如何维护？
A: Design Token 变更后，组件样式自动同步更新。建议将 Token 文件纳入版本控制，变更时运行同步脚本.
### Q: 响应式策略如何保证一致性？
A: 采用移动优先策略，通过 Design Token 统一间距和字号，各断点按比例缩放，确保视觉一致性.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

