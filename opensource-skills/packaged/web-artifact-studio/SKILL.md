---
slug: web-artifact-studio
name: web-artifact-studio
version: "1.0.0"
displayName: "Web工件工作室"
summary: "React+Tailwind+shadcn构建复杂交互Web工件,状态路由组件全搞定"
license: Apache-2.0
description: |-
  Web工件工作室——用现代前端技术栈(React/Tailwind CSS/shadcn/ui)构建复杂的多组件HTML工件。状态管理、路由、shadcn/ui组件组合,让交互式演示、数据仪表盘、表单工作流一站搞定。

  核心能力:
  - React组件架构:多组件组合与状态管理
  - shadcn/ui集成:专业级UI组件库快速搭建
  - Tailwind CSS样式:原子化CSS快速实现设计
  - 路由与导航:单页应用路由与条件渲染
  - 交互与事件:点击/拖拽/表单/实时数据交互
  - 状态持久化:本地存储与状态恢复

  适用场景:
  - 独立创业者交互演示:可点击/拖拽的产品演示原型
  - 副业达人数据仪表盘:多图表/过滤器/实时数据展示
  - 一人公司表单工作流:多步表单/条件分支/数据收集
  - 内容创作者组件展示:设计系统/组件库预览页面

  差异化:不是简单单文件HTML生成器,而是构建复杂多组件Web工件的专业工作室,React+Tailwind+shadcn全栈能力,让需要状态管理与路由的复杂工件轻松实现。

  触发关键词:Web工件、HTML工件、React组件、Tailwind、shadcn、ui组件、前端工件、交互组件、单页应用、SPA、组件库
tags: [Web工件, React组件, 前端开发, 交互应用, shadcn]
tools: [read, exec]
---

# Web工件工作室

用现代前端技术栈构建复杂的多组件 HTML 工件。当工件需要状态管理、路由或复杂交互时使用,简单单文件 HTML 不在此范畴。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 交互式演示 | 需要可点击/拖拽的演示 | React + 事件处理 |
| 数据仪表盘 | 多图表/过滤器/实时数据 | 状态管理 + 图表库 |
| 表单工作流 | 多步表单/条件分支 | 路由 + 表单状态 |
| 组件展示 | 设计系统/组件库预览 | shadcn/ui 组合 |
| 小型应用 | 单页应用原型 | 路由 + 状态 + 持久化 |

## 工作流

### 1. 需求分析

1. **明确工件目标**:展示什么?交互什么?数据从哪来?
2. **复杂度评估**:
   - 简单展示 → 单文件 HTML 即可
   - 需要状态/路由/多组件 → 使用本工作室
3. **技术选型确认**:React + Tailwind + shadcn/ui

### 2. 项目搭建

1. **目录结构**:
   ```
   artifact/
   ├── index.html          # 入口
   ├── src/
   │   ├── main.tsx        # 挂载点
   │   ├── App.tsx         # 根组件
   │   ├── components/      # 业务组件
   │   ├── ui/              # shadcn/ui 组件
   │   ├── hooks/           # 自定义 Hook
   │   ├── lib/             # 工具函数
   │   └── styles/          # 全局样式
   └── package.json
   ```
2. **依赖引入**:React、Tailwind、shadcn/ui、按需引入图表/路由库
3. **构建配置**:Vite 或内联打包

### 3. 组件设计

1. **组件拆分**:按职责拆分,单一职责
2. **shadcn/ui 组合**:优先使用 shadcn/ui 组件(Button/Card/Dialog/Table 等)
3. **状态管理**:
   - 局部状态:useState
   - 跨组件:Context 或 Zustand
   - 持久化:localStorage
4. **路由**:React Router(如需多页面)

### 4. 样式与交互

1. **Tailwind 优先**:用工具类,少写自定义 CSS
2. **响应式**:移动优先,sm/md/lg/xl 断点
3. **无障碍**:语义化 HTML、ARIA 标签、键盘导航
4. **动效**:CSS transition / Framer Motion(按需)

### 5. 打包与交付

1. **构建产物**:单 HTML 文件(内联 JS/CSS)或多文件
2. **资源处理**:图片转 base64 或 CDN
3. **可移植性**:确保工件可独立运行,无外部依赖

## 设计原则

1. **组件化**:一切皆组件,可复用可组合
2. **类型安全**:TypeScript,props 有类型定义
3. **无障碍优先**:WCAG 2.1 AA 合规
4. **性能考虑**:懒加载、虚拟列表(长数据)
5. **避免过度工程**:工件不是产品,够用即可

## 输出规范

- 工件源码:`output/{artifact-name}/src/`
- 构建产物:`output/{artifact-name}/dist/index.html`
- 组件文档:`output/{artifact-name}/components.md`
- 使用说明:`output/{artifact-name}/README.md`

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js 18+ | 运行时 | 可选 | React/Vite/Tailwind环境 |
| LLM API | API | 可选 | 由Agent内置LLM提供代码生成 |

### API Key 配置
- 本Skill无需额外API Key配置

### 纯Markdown使用说明
本Skill为Web组件构建方法论指导。实际开发需要Node.js和前端工具链。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用
