---
slug: typescript-toolkit-free
name: typescript-toolkit-free
version: "1.0.0"
displayName: TypeScript工具集(免费版)
summary: 面向个人开发者的TypeScript类型安全辅助工具,覆盖基础类型收窄、推断与严格模式实践。
license: MIT
edition: free
description: |-
  TypeScript工具集免费版为个人开发者提供日常类型安全辅助,涵盖类型收窄、字面量陷阱、严格空值处理等核心主题。

  核心能力:
  - 基础类型安全指导与代码审查
  - any/unknown的替代方案与收窄技巧
  - 字面量类型陷阱识别与修复建议
  - 严格空值处理与可选链最佳实践

  适用场景:
  - 个人项目TypeScript代码编写与重构
  - 学习并掌握类型系统基础概念
  - 快速定位并修复常见类型错误

  差异化:免费版聚焦个人开发场景,提供核心类型安全指导,适合中小型项目日常使用。Pro版扩展企业级规范、批量迁移与CI集成能力。

  触发关键词: typescript, 类型安全, 类型收窄, strict, any, unknown, narrowing
tags:
- TypeScript
- 类型系统
- 前端开发
- 代码质量
- 个人开发
tools:
- read
- exec
---

# TypeScript 工具集(免费版)

## 概述

`typescript-toolkit-free` 是面向个人开发者的 TypeScript 类型安全辅助工具。它聚焦日常编码中最常见的类型陷阱与最佳实践,帮助你写出类型安全、易于维护的代码。免费版覆盖核心场景,适合独立项目、学习实践与小型应用开发。

本版本不依赖任何外部脚本或私有 API,完全通过 Markdown 指令驱动 AI Agent 输出建议与代码片段。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| 类型收窄指导 | `typeof`、`in`、`Array.isArray` 等收窄技巧与陷阱识别 |
| `any` 替代方案 | 用 `unknown`、泛型、类型守卫替换 `any` 的实战方法 |
| 字面量陷阱修复 | `let` vs `const`、对象属性拓宽、函数返回类型拓宽 |
| 严格空值处理 | 可选链 `?.`、空值合并 `??`、非空断言 `!` 的使用边界 |
| 模块边界规范 | `import type`、`export type` 与 `.d.ts` 增强基本用法 |

## 使用场景

### 场景 1:API 响应类型化

当你需要为 API 响应定义类型时,本工具会建议用 `unknown` 替代 `any`,并通过类型守卫收窄。

```typescript
// 不推荐:用 any 静默破坏类型安全
async function fetchUser(): Promise<any> {
  const res = await fetch('/api/user');
  return res.json();
}

// 推荐:用 unknown 强制收窄
async function fetchUser(): Promise<User> {
  const res = await fetch('/api/user');
  const data: unknown = await res.json();
  if (isValidUser(data)) {
    return data;
  }
  throw new Error('Invalid user payload');
}

function isValidUser(value: unknown): value is User {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'name' in value
  );
}
```

### 场景 2:过滤数组时保留类型

`filter(Boolean)` 不会收窄类型,本工具会提示你使用类型谓词函数。

```typescript
// 不推荐:filtered 仍是 (string | null)[]
const filtered = list.filter(Boolean);

// 推荐:显式类型谓词,filtered 收窄为 string[]
const filtered = list.filter((x): x is string => Boolean(x));
```

### 场景 3:配置对象的字面量保留

为配置对象定义类型时,使用 `satisfies` 保留字面量信息。

```typescript
const palette = {
  primary: '#0066ff',
  danger: '#cc0000',
} satisfies Record<string, string>;
// palette.primary 类型为字面量 '#0066ff',而非 string
```

## 快速开始

### 第一步:提出问题

直接在对话中描述你的 TypeScript 问题,例如:

```
我在用 filter(Boolean) 后类型没有收窄,该怎么修?
```

```
帮我看看这段 API 响应类型定义是否安全。
```

### 第二步:获取建议

工具会输出问题分析、修复代码与简要解释,并标注是否符合严格模式要求。

### 第三步:应用并验证

将建议代码复制到你的项目中,运行 `tsc --noEmit` 验证类型是否通过。

```bash
npx tsc --noEmit
```

## 配置示例

### 推荐 `tsconfig.json`(个人项目基线)

```jsonc
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "lib": ["ES2022", "DOM"],
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUncheckedIndexedAccess": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

### 推荐 ESLint 规则(个人项目)

```jsonc
{
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-unused-vars": "warn",
    "@typescript-eslint/consistent-type-imports": "error",
    "@typescript-eslint/prefer-optional-chain": "error"
  }
}
```

## 最佳实践

1. **永远不要在生产代码中使用 `any`**。改用 `unknown` 并显式收窄,或用泛型表达意图。
2. **优先使用 `satisfies` 而非类型注解** 来保留字面量信息,尤其适用于配置对象。
3. **为可辨识联合添加 `type` 字段**,启用穷举 switch 检查,避免漏掉分支。
4. **`Object.keys(obj)` 返回 `string[]`**,不要假设它是 `keyof typeof obj`,因为对象可能有额外键。
5. **`Array.isArray()` 收窄为 `any[]`**,如需更精确的元素类型,需要额外断言或类型守卫。
6. **`import type` 仅用于类型导入**,避免打包器产生运行时依赖。
7. **非空断言 `!` 应作为最后手段**,优先用收窄或提前返回。

## 常见问题

### Q1: `filter(Boolean)` 为什么不收窄类型?

JavaScript 的 `Boolean` 函数签名返回 `boolean`,TypeScript 无法据此推断元素类型已收窄。需要用类型谓词函数显式声明:`.filter((x): x is T => Boolean(x))`。

### Q2: `let x = "hello"` 为什么类型是 `string` 而不是 `"hello"`?

`let` 声明的变量会被拓宽为更宽的类型,因为它们可被重新赋值。用 `const` 或 `as const` 可保留字面量类型。

### Q3: 可选链 `?.` 返回 `undefined`,但 API 需要 `null`,怎么办?

显式处理:`const value = obj?.field ?? null;`,或在收窄阶段统一为 `null`。

### Q4: `import type` 和普通 `import` 有什么区别?

`import type` 仅在编译期存在,运行时会被完全移除,适合只引用类型的场景,有助于打包器 tree-shaking。

### Q5: 免费版与 Pro 版的主要区别是什么?

免费版聚焦个人日常类型安全指导;Pro 版在此基础上提供团队规范、批量 JS→TS 迁移、CI 集成与企业级代码审查能力。

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Node.js**:建议 18+ 用于本地 `tsc` 验证
- **TypeScript**:建议 5.0+(支持 `satisfies` 关键字)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| TypeScript | npm 包 | 推荐 | `npm i -D typescript` |
| ESLint + @typescript-eslint | npm 包 | 可选 | `npm i -D eslint @typescript-eslint/eslint-plugin` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 完全基于 Markdown 指令,无需额外 API Key
- 本地 `tsc` 验证使用本地 TypeScript 编译器,不涉及任何外部 API

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出类型安全建议与代码片段;用户可通过 `tsc --noEmit` 在本地验证类型
