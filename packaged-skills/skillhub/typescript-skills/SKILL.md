---
slug: "typescript-skills"
name: "typescript-skills"
version: "1.0.6"
displayName: "TypeScript规范"
summary: "提供TypeScript最佳实践编码规范并生成符合标准的TypeScript代码。"
license: "Proprietary"
description: |-
  TypeScript编码规范技能提供最佳实践编码约定并生成符合标准的TypeScript代码。
  覆盖Naming Conventions命名约定、Types & Interfaces类型与接口、Enums枚举、
  Error Handling错误处理、async/await、工具配置（Recommended tsconfig.json、
  Recommended ESLint Rules、Prettier）。
tags:
  - Development
  - TypeScript
  - 编码规范
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# TypeScript — 编码规范


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | TypeScript规范处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 命名约定（Naming Conventions）
| 构造 | 约定 | 示例 |
|------|------|------|
| 变量/函数 | `camelCase` | `getUserName`, `isActive` |
| 布尔变量 | `camelCase`带前缀 | `isLoading`, `hasAccess`, `canEdit` |
| 模块常量 | `UPPER_SNAKE_CASE` | `MAX_RETRY_COUNT`, `API_BASE_URL` |
| 类/接口/类型别名/枚举 | `PascalCase` | `UserService`, `UserProfile`, `UserId` |
| 文件名 | `kebab-case.ts` | `user-service.ts` |
| React组件文件 | `PascalCase.tsx` | `UserProfile.tsx` |

规则：不使用 `I` 前缀接口名（~~`IUser`~~ → `User`）；不使用 `Type` 或 `Interface` 后缀；2字符缩写保持大写（`IO`、`ID`），3+字符用PascalCase（`Http`、`Xml`）。

**处理**: 解析命名约定（Naming Conventions）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回命名约定（Naming Conventions）的处理结果,包含执行状态码、结果数据和执行日志。### 类型与接口（Types & Interfaces）
- 对象形状优先使用 `interface`，联合/交叉/映射类型使用 `type`
- 公共API始终显式标注函数返回类型；局部变量让TypeScript推断
- 函数签名优先使用 `type`：`type Comparator<T> = (a: T, b: T) => number`
- 使用 `Record<K, V>` 而非 `{ [key: string]: V }`
- 使用工具类型（`Partial<T>`、`Pick<T, K>`、`Omit<T, K>`、`Required<T>`）派生类型

**输入**: 用户提供类型与接口（Types & Interfaces）所需的指令和必要参数。
**处理**: 解析类型与接口（Types & Interfaces）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 枚举（Enums）
- 优先使用字符串枚举（String Enums）以提高可读性和可调试性
- 不需要反向映射时使用 `const enum`（零运行时成本）
- 小集合优先使用字符串字面量联合类型（String Literal Union）：`type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE'`
- 不使用无显式值的数字枚举；不混合字符串和数字成员

**输入**: 用户提供枚举（Enums）所需的指令和必要参数。
**输出**: 返回枚举（Enums）的处理结果,包含执行状态码、结果数据和执行日志。### 错误处理（Error Handling）

- 永不静默吞错（空 `catch` 块）；`catch` 变量类型为 `unknown`（TS 4.4+默认）
- 使用扩展 `Error` 的自定义错误类处理领域特定错误
- 库中预期失败优先使用 Result/Either 模式：`type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E }`
- 在 `finally` 块中清理资源；记录含足够上下文的错误（操作名、输入摘要、堆栈）

### Async/Await 与 Promise
- 优先使用 `async/await` 而非 `.then()` 链；返回类型始终标注为 `Promise<T>`
- 独立并发操作使用 `Promise.all()`；失败不应中止兄弟操作时使用 `Promise.allSettled()`
- 永不在async函数足够时使用 `new Promise()`；避免 `async void` 函数
- 顺序异步迭代用 `for...of` + `await`，而非 `forEach`

**输入**: 用户提供Async/Await 与 Promise所需的指令和必要参数。
**处理**: 解析Async/Await 与 Promise的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### Null 与 Undefined 处理
- 启用 `strictNullChecks`（包含在 `strict` 模式中）
- 优先使用 `undefined` 而非 `null`（除非外部API使用 `null`）
- 使用可选链（`?.`）和空值合并（`??`）替代手动检查
- 不使用非空断言（`!`），除非能证明值始终已定义并添加注释
- 优先使用 `satisfies` 运算符（TS 5.0+）验证类型而不扩展

**输入**: 用户提供Null 与 Undefined 处理所需的指令和必要参数。
**输出**: 返回Null 与 Undefined 处理的处理结果,包含执行状态码、结果数据和执行日志。### 类型断言与守卫（Type Assertions & Guards）
- 优先使用类型守卫（`is` 关键字）而非类型断言（`as`）
- 使用 `as const` 进行字面量收窄；使用判别联合（discriminated unions）+ `kind`/`type` 字段
- 避免 `as unknown as T` 双重断言；断言必要时添加注释说明

**输入**: 用户提供类型断言与守卫（Type Assertions & Guards）所需的指令和必要参数。
**处理**: 解析类型断言与守卫（Type Assertions & Guards）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回类型断言与守卫（Type Assertions & Guards）的处理结果,包含执行状态码、结果数据和执行日志。### 工具配置（Tooling & Configuration）
### Recommended `tsconfig.json` (Baseline)

启用 `"strict": true`（含 `noImplicitAny`、`strictNullChecks`、`strictFunctionTypes`）。2空格缩进、单引号、分号、尾逗号、100字符行宽。

#### Recommended ESLint Rules

| Rule | Setting |
|------|---------|
| `@typescript-eslint/no-explicit-any` | `error` |
| `@typescript-eslint/explicit-function-return-type` | `warn`（导出函数） |
| `@typescript-eslint/no-unused-vars` | `error` |
| `@typescript-eslint/consistent-type-imports` | `error` |
| `@typescript-eslint/no-non-null-assertion` | `warn` |
| `@typescript-eslint/prefer-nullish-coalescing` | `error` |
| `@typescript-eslint/prefer-optional-chain` | `error` |
| `@typescript-eslint/strict-boolean-expressions` | `warn` |
| `@typescript-eslint/naming-convention` | `error`（按构造配置） |

使用 Prettier 自动格式化（`semi: true`、`singleQuote: true`、`trailingComma: "all"`、`printWidth: 100`、`tabWidth: 2`、`arrowParens: "always"`）。

**输入**: 用户提供工具配置（Tooling & Configuration）所需的指令和必要参数。
**处理**: 解析工具配置（Tooling & Configuration）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。


### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。

## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`typescript-skills`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 示例

### 基本用法

向Agent发送指令:

```
使用 TypeScript规范 处理以下任务:
[具体任务描述]
```

### 输出说明

Agent将根据指令调用对应能力,返回响应数据。响应格式取决于具体能力点的输出定义。

## 使用方式

在对话中提及 **TypeScript** 即可自动激活。支持自然语言激活与内联规则引用。

| 提示 | 技能响应 |
|------|---------|
| "写一个深度合并两个对象的TypeScript函数" | 生成完整类型化的 `deepMerge<T, U>()` 函数 |
| "审查我的TypeScript代码风格" | 按规范分析代码并建议改进 |
| "将这段JavaScript转为TypeScript" | 添加严格类型、接口，遵循命名/格式约定 |
| "TypeScript错误处理最佳实践" | 解释Result模式、自定义错误类、类型化catch块 |

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 使用 `any` 类型 | 违反规范 | 替换为 `unknown` 或使用泛型；触发 `@typescript-eslint/no-explicit-any` |
| 使用 `var` 声明 | 违反规范 | 替换为 `const`（默认）或 `let`（需重新赋值时） |
| 空catch块吞错 | 违反规范 | `catch` 变量类型为 `unknown`，记录含上下文的错误 |
| 使用非空断言 `!` | 不安全 | 证明值始终已定义并添加注释，或使用类型守卫 |
| 数字枚举无显式值 | 自动递增脆弱 | 使用显式值或字符串字面量联合类型 |
| `async void` 函数 | 无法await、吞错 | 改为 `async` 函数返回 `Promise<void>` |
| 使用 `React.FC` | React 18后不推荐 | 使用函数声明或命名函数表达式 |
| 接口名含 `I` 前缀 | 违反命名约定 | 移除 `I` 前缀（`IUser` → `User`） |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪。

### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界。

## 已知限制

- 仅覆盖TypeScript编码规范，不提供编译或构建能力
- 详细规则参考 `references/detail.md`
- 依赖LLM理解与执行规范，复杂场景可能需要人工判断
- React/JSX规则仅在适用时生效
