---
slug: ui-component-paid
name: ui-component-paid
version: "1.0.0"
displayName: UI组件生成(专业版)
summary: 面向团队的企业级UI组件工程平台,含设计系统、批量生成、可访问性增强与组件库管理。
license: Proprietary
edition: pro
description: |-
  UI组件生成工具专业版为团队与企业提供端到端UI组件工程能力,涵盖设计系统令牌、批量组件生成、WCAG AA可访问性增强与企业级组件库管理。核心能力:
  - 设计系统令牌(颜色/排版/间距/圆角/阴影)生成与管理
  - 批量组件生成与脚手架
  - WCAG AA可访问性审查与增强
  - 多框架输出(HTML/React/Vue/Angular)
  - 企业级组件库结构与文档生成
  - 主题切换与暗色模式工程化

  适用场景:
  - 中大型团队设计系统落地与维护
  - 企业级组件库从0到1搭建
  - 多项目组件复用与版本管理
  ...
tags:
- UI组件
- 设计系统
- 企业开发
- 可访问性
- 组件库
- 团队协作
tools:
  - - read
- exec
---
# UI组件生成(专业版)

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
| --- | --- | --- |
| 基础组件生成 | 免费版全部表单、表格、卡片、模态框、导航栏 | 完全兼容 |
| 设计系统令牌 | 颜色、排版、间距、圆角、阴影令牌生成 | Pro 新增 |
| 批量组件生成 | 脚手架脚本一次性生成整套组件 | Pro 新增 |
| WCAG AA 可访问性 | 自动审查与增强,达到 WCAG AA 合规 | Pro 新增 |
| 多框架输出 | HTML / React / Vue / Angular 同步输出 | Pro 新增 |
| 企业组件库结构 | 目录结构、文档站点、版本管理 | Pro 新增 |
| 主题与暗色模式 | 令牌驱动的多主题工程化 | Pro 新增 |
### 基础组件生成

执行基础组件生成操作,处理用户输入并返回结果。

**输入**: 用户提供基础组件生成所需的参数和指令。

**输出**: 返回基础组件生成的处理结果。
### 设计系统令牌

执行设计系统令牌操作,处理用户输入并返回结果。

**输入**: 用户提供设计系统令牌所需的参数和指令。

**输出**: 返回设计系统令牌的处理结果。
### 批量组件生成

执行批量组件生成操作,处理用户输入并返回结果。

**输入**: 用户提供批量组件生成所需的参数和指令。

**输出**: 返回批量组件生成的处理结果。


## 适用场景

### 场景 1:设计系统令牌生成

为团队生成完整的设计系统令牌,作为所有组件的样式基础。

```css
/* tokens.css — 设计系统令牌 */
:root {
  /* 颜色令牌 */
  --color-primary-50: #e6f0ff;
  --color-primary-100: #b3d1ff;
  --color-primary-500: #0066ff;
  --color-primary-700: #0052cc;
  --color-neutral-0: #ffffff;
  --color-neutral-100: #f5f5f5;
  --color-neutral-500: #888888;
  --color-neutral-900: #1a1a1a;
  --color-danger-500: #cc0000;
  --color-success-500: #00875a;

  /* 排版令牌 */
  --font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  --line-height-tight: 1.25;
  --line-height-base: 1.5;

  /* 间距令牌(8px 基准) */
  --spacing-0: 0;
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-3: 0.75rem;
  --spacing-4: 1rem;
  --spacing-6: 1.5rem;
  --spacing-8: 2rem;
  --spacing-12: 3rem;

  /* 圆角令牌 */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* 阴影令牌 */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 2px 8px rgba(0,0,0,0.1);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.15);

  /* 过渡令牌 */
  --transition-fast: 150ms ease-in-out;
  --transition-base: 250ms ease-in-out;
}

/* 暗色模式令牌覆盖 */
@media (prefers-color-scheme: dark) {
  :root {
    --color-neutral-0: #1a1a1a;
    --color-neutral-100: #2a2a2a;
    --color-neutral-900: #f5f5f5;
  }
}
```

### 场景 2:批量组件生成脚本

生成一个脚手架脚本,一次性创建整套组件目录结构。

```bash
#!/usr/bin/env bash
# scripts/scaffold-components.sh — 批量生成企业组件库
set -euo pipefail

COMPONENTS=(
  "Button" "Input" "Select" "Checkbox" "Radio"
  "Table" "Pagination" "Tag" "Badge"
  "Card" "Modal" "Drawer" "Tooltip"
  "Navbar" "Sidebar" "Breadcrumb"
)

BASE_DIR="src/components"

for comp in "${COMPONENTS[@]}"; do
  dir="$BASE_DIR/$comp"
  mkdir -p "$dir"

  # React 组件
  cat > "$dir/$comp.tsx" <<EOF
import React from 'react';
import { ${comp}Props } from './types';
import './${comp}.css';

export const ${comp}: React.FC<${comp}Props> = (props) => {
  return (
    <div className="${comp,,}">
      {/* 详情见说明: 实现 ${comp} */}
    </div>
  );
};
EOF

  # 类型定义
  cat > "$dir/types.ts" <<EOF
export interface ${comp}Props {
  /** 详情见说明: 添加 ${comp} 属性 */
}
EOF

  # 样式(使用设计令牌)
  cat > "$dir/${comp}.css" <<EOF
.${comp,,} {
  /* 使用设计系统令牌 */
  padding: var(--spacing-4);
  border-radius: var(--radius-md);
}
EOF

  # 单元测试
  cat > "$dir}/${comp}.test.tsx" <<EOF
import { render } from '@testing-library/react';
import { ${comp} } from './${comp}';

describe('${comp}', () => {
  it('应正确渲染', () => {
    const { container } = render(<${comp} />);
    expect(container.firstChild).toBeInTheDocument();
  });
});
EOF

  # 文档
  cat > "$dir}/README.md" <<EOF
# ${comp}

## 使用流程

### 优秀步:声明团队上下文

在对话中说明团队规模、技术栈与设计系统现状,例如:

```
我们是 15 人的前端团队,技术栈是 React + TypeScript,
需要从 0 搭建一套企业组件库,要求 WCAG AA 合规,支持暗色模式。
```

### 第二步:获取工程方案

工具会输出设计系统令牌、组件库目录结构、脚手架脚本、可访问性审查脚本与文档站点配置。

### 第三步:落地与维护

```bash
# 应用设计系统令牌
cp tokens.css src/styles/

# 批量生成组件骨架
bash scripts/scaffold-components.sh

# 运行可访问性审查
bash scripts/a11y-audit.sh

# 启动文档站点(Storybook 等)
npm run storybook
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 20 LTS+
- **浏览器**:任意现代浏览器(Chrome / Firefox / Safari / Edge)
- **CI 平台**:GitHub Actions / GitLab CI / Jenkins

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官方安装包 |
| React / Vue / Angular | 框架 | 推荐 | `npm i react` 等 |
| Storybook | 文档工具 | 推荐 | `npx storybook init` |
| pa11y / axe-core | 可访问性 | 推荐 | `npm i -D pa11y axe-core` |
| Chromatic / Percy | 视觉回归 | 可选 | 官方注册 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 完全基于 Markdown 指令,无需额外 API Key
- 视觉回归工具(Chromatic / Percy)需配置对应平台的 `TOKEN` 环境变量
- 私有 npm 发布需配置 `NODE_AUTH_TOKEN`

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出企业级组件工程方案;脚手架与审查脚本需在仓库中落地并由本地或 CI 执行

## 案例展示

### 企业组件库目录结构

```
src/
├── components/           # 组件实现
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.test.tsx
│   │   ├── Button.css
│   │   ├── types.ts
│   │   └── README.md
│   └── ...
├── tokens/               # 设计系统令牌
│   ├── colors.css
│   ├── typography.css
│   ├── spacing.css
│   └── index.css
├── themes/               # 主题
│   ├── light.css
│   └── dark.css
├── utils/                # 工具函数
│   ├── a11y.ts
│   └── cn.ts
└── index.ts              # 统一导出
```

### 多框架输出对照表

| 组件 | HTML 输出 | React 输出 | Vue 输出 |
| --- | --- | --- | --- |
| Button | `<button class="btn">` | `<Button onClick>` | `<Button @click>` |
| Input | `<input class="input">` | `<Input value onChange>` | `<Input v-model>` |
| Modal | `<div class="modal">` | `<Modal open onClose>` | `<Modal v-model:open>` |
| Table | `<table class="table">` | `<Table data columns>` | `<Table :data :columns>` |

## 常见问题

### Q1: 如何在多项目中复用企业组件库?

将组件库发布为私有 npm 包,各项目通过 `npm i @your-org/ui-components` 安装。配合语义化版本与 CHANGELOG,实现可控升级。

### Q2: 设计令牌如何与 Tailwind / CSS-in-JS 协同?

Tailwind:在 `tailwind.config.js` 中将令牌映射为 theme 字段;CSS-in-JS:将令牌导出为 JS 对象,在 styled-components / emotion 中引用。

### Q3: 多框架输出如何维护?

推荐以 Web Components 为基础层(Stencil / Lit),各框架输出为薄包装。或采用 mitosis 等工具从单一源码编译多框架输出。

### Q4: WCAG AA 审查如何自动化?

集成 `pa11y`、`axe-core`、`@axe/playwright` 到 CI 中,对每个组件故事(Story)运行审查,违规阻断 PR。

### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有单文件 HTML 输出。个人开发者可继续使用免费版,团队场景启用 Pro 版获得设计系统与企业级能力。两个版本可在同一仓库并存。

### Q6: 如何度量组件库的健康度?

跟踪四个指标:组件复用率(被多少项目引用)、WCAG AA 合规率、视觉回归测试通过率、文档覆盖率。四者共同反映组件库健康度。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
