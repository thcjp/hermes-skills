---
slug: typescript-skills
name: typescript-skills
version: "1.0.6"
displayName: TypeScript
summary: Provide best-practice coding conventions and generate standards-compliant
  TypeScript code.
license: MIT-0
description: |-
  Provide best-practice coding conventions and generate standards-compliant
  TypeScript code。核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词...
tags:
- Development
tools:
  - - read
- exec
# TypeScript
---
> **Activation**: This skill activates whenever the user says or implies **TypeScript**. It responds
> with standards-compliant TypeScript code and can explain any rule on demand.

## Table of Contents
> 详细内容已移至 `references/detail.md`

## 1. General Principles
* **Strict mode always**: Enable `"strict": true` in `tsconfig.json`. This turns on `noImplicitAny`,
  `strictNullChecks`, `strictFunctionTypes`, and more.
* **Prefer readability over cleverness**: Code is read far more often than written. Favour explicit,
  self-documenting code.
* **Minimise `any`**: Treat every use of `any` as tech debt. Prefer `unknown` when the type is
  truly not known, or use generics.
* **Immutability by default**: Use `const` over `let`; prefer `readonly` properties and
  `ReadonlyArray<T>` / `Readonly<T>` utility types.
* **Single responsibility**: Each file, class, and function should have one clear purpose.
* **Keep files small**: A file should ideally stay under 400 lines. If it grows larger, consider
  splitting it.

## 2. Naming Conventions
| Construct | Convention | Example |
| --- | --- | --- |
| **Variable / Function** | `camelCase` | `getUserName`, `isActive` |
| **Boolean variable** | `camelCase` with prefix | `isLoading`, `hasAccess`, `canEdit` |
| **Constant (module)** | `UPPER_SNAKE_CASE` | `MAX_RETRY_COUNT`, `API_BASE_URL` |
| **Constant (local)** | `camelCase` | `const defaultTimeout = 3000` |
| **Class** | `PascalCase` | `UserService`, `HttpClient` |
| **Interface** | `PascalCase` | `UserProfile`, `ApiResponse` |
| **Type alias** | `PascalCase` | `UserId`, `Theme` |
| **Enum** | `PascalCase` | `Direction`, `HttpStatus` |
| **Enum member** | `PascalCase` | `Direction.Up`, `HttpStatus.Ok` |
| **Generic parameter** | Single uppercase letter or descriptive `PascalCase` | `T`, `TKey`, `TValue` |
| **File name** | `kebab-case.ts` | `user-service.ts`, `api-client.ts` |
| **Test file name** | `kebab-case.test.ts` or `kebab-case.spec.ts` | `user-service.test.ts` |
| **React component file** | `PascalCase.tsx` | `UserProfile.tsx` |
| **Private field** | `camelCase` (no `_` prefix) | `private count: number` |

### Additional Naming Rules
* **Do NOT** prefix interfaces with `I` (e.g., ~~`IUser`~~ → `User`).
* **Do NOT** suffix types/interfaces with `Type` or `Interface`.
* Use descriptive names. Avoid single-letter variables except for conventional usages like loop
  indices (`i`, `j`) or generic type parameters (`T`, `K`, `V`).
* Acronyms of 2 characters stay uppercase (`IO`, `ID`); 3+ characters use PascalCase
  (`Http`, `Xml`, `Api`).

## 3. Types & Interfaces
### Prefer `interface` for Object Shapes
```typescript
// ✅ Good — use interface for object shapes
interface User {
  readonly id: string;
  name: string;
  email: string;
}

// ✅ Good — use type for unions, intersections, mapped types
type Status = 'active' | 'inactive' | 'suspended';
type Result<T> = Success<T> | Failure;
```

### When to Use `type` vs `interface`
| Use `interface` when … | Use `type` when … |
| --- | --- |
| Defining the shape of an object or class | Creating union or intersection types |
| You want declaration merging | Using mapped / conditional types |
| Extending other interfaces | Aliasing primitive or tuple types |

### Rules
* Always annotate function return types explicitly for public APIs.
* Let TypeScript infer types for local variables when the type is obvious.
* Prefer `type` over `interface` for function signatures:

  typescript

  ```
  type Comparator<T> = (a: T, b: T) => number;
  ```
* Avoid empty interfaces. If extending, include at least a comment explaining intent.
* Use `Record<K, V>` instead of `{ [key: string]: V }`.
* Use utility types (`Partial<T>`, `Pick<T, K>`, `Omit<T, K>`, `Required<T>`) to derive types
  rather than duplicating.

## 4. Enums
### Prefer String Enums
```typescript
// ✅ Good — string enum for readability and debuggability
enum Direction {
  Up = 'UP',
  Down = 'DOWN',
  Left = 'LEFT',
  Right = 'RIGHT',
}
```

### When to Use `const` Enum or Union Types
```typescript
// ✅ Good — const enum for zero-runtime-cost enums (no reverse mapping needed)
const enum HttpMethod {
  Get = 'GET',
  Post = 'POST',
  Put = 'PUT',
  Delete = 'DELETE',
}

// ✅ Also good — string literal union (simpler, tree-shakeable)
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
```

### Rules
* **Do NOT** use numeric enums without explicit values (auto-increment is fragile).
* Prefer **string literal union types** over enums when the set is small and no namespace features
  are needed.
* Never mix string and numeric members in the same enum.

## 5. Variables & Constants
```typescript
// ✅ Good
const maxRetries = 3;
const baseUrl = 'https://api.example.com';
let currentAttempt = 0;

// ❌ Bad — using var
var legacyValue = 'old';

// ❌ Bad — using let when value never changes
let neverReassigned = 42;
```

### Rules
> 详细内容已移至 `references/detail.md`

## 6. Functions
### Function Declarations
```typescript
// ✅ Good — explicit return type for public functions
function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// ✅ Good — arrow function for callbacks / short lambdas
const double = (n: number): number => n * 2;

// ✅ Good — use default parameters instead of optional + fallback
function createUser(name: string, role: Role = Role.Viewer): User {
  // ...
}
```

### Rules
> 详细内容已移至 `references/detail.md`

## 7. Classes
```typescript
// ✅ Good
class UserService {
  private readonly repository: UserRepository;

  constructor(repository: UserRepository) {
    this.repository = repository;
  }

  async findById(id: string): Promise<User | undefined> {
    return this.repository.get(id);
  }
}
```

### Rules
> 详细内容已移至 `references/detail.md`

## 8. Modules & Imports
```typescript
// ✅ Good — named exports
export function parseConfig(raw: string): Config { ... }
export interface Config { ... }

// ✅ Good — re-export barrel file (index.ts)
export { parseConfig } from './parse-config';
export type { Config } from './parse-config';
```

### Rules
> 详细内容已移至 `references/detail.md`

## 9. Generics

### Rules
* Use a **single uppercase letter** (`T`, `U`, `K`, `V`) for simple generics.
* Use **descriptive PascalCase prefixed with `T`** (`TKey`, `TValue`, `TResult`) when there are
  multiple type parameters or the purpose is not obvious.
* Always add constraints when possible (`<T extends SomeType>`).
* Avoid unnecessary generics — if a type parameter is used only once, it's likely not needed.
* Prefer generic utility types (`Array<T>`, `Promise<T>`, `Map<K, V>`) over their shorthand where
  readability benefits.

## 10. Error Handling

### Rules
* **Never** swallow errors silently (empty `catch` blocks).
* Use **custom error classes** that extend `Error` for domain-specific errors.
* Type the `catch` variable as `unknown` (default in TS 4.4+) and narrow before use.
* Prefer **Result / Either patterns** for expected failures in libraries:

  typescript

  ```
  type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E };
  ```
* Always clean up resources in `finally` blocks or use disposable patterns.
* Log errors with sufficient context (operation name, input summary, stack trace).

## 11. Async / Await & Promises

### Rules
* **Prefer `async/await`** over `.then()` chains for readability.
* Always annotate return types as `Promise<T>`.
* Use `Promise.all()` for independent concurrent operations.
* Use `Promise.allSettled()` when failures should not abort sibling operations.
* **Never** use `new Promise()` when an async function suffices (avoid the explicit-construction
  antipattern).
* Avoid `async void` functions — they cannot be `await`-ed and swallow errors.
  Exception: event handlers where the framework requires `void`.
* Prefer `for...of` with `await` for sequential async iteration, not `forEach`.

## 12. Comments & Documentation
> 详细内容已移至 `references/detail.md`

### Rules
* Use **TSDoc** (`/** */`) for all public APIs, exported functions, classes, interfaces, and types.
* Include `@param`, `@returns`, `@throws`, and `@example` tags where applicable.
* **Do NOT** comment obvious code. The code should be self-documenting.
* Use `// TODO:` with a ticket number for planned improvements.
* Use `// FIXME:` for known issues that need resolution.
* Use `// HACK:` for workarounds that should be revisited.
* Never leave commented-out code in the main branch.
* Place file-level comments at the top if the module's purpose is not obvious from its name.
* Keep comments up-to-date with code changes.

## 13. Formatting & Style
### General
* **Indentation**: 2 spaces (no tabs).
* **Semicolons**: Required at the end of every statement.
* **Quotes**: Single quotes (`'`) for strings; backticks (`` ` ``) for template literals.
* **Trailing commas**: Always use in multi-line constructs (arrays, objects, parameters, generics).
* **Max line length**: 100 characters (soft limit), 120 characters (hard limit).
* **Braces**: Required for all control structures, even single-line bodies.
* **Blank lines**: One blank line between top-level declarations; no multiple consecutive blank lines.

### Specific Patterns

### Tooling
* Use **Prettier** for auto-formatting with the following baseline config:

  json

  ```
  {
    "semi": true,
    "singleQuote": true,
    "trailingComma": "all",
    "printWidth": 100,
    "tabWidth": 2,
    "arrowParens": "always"
  }
  ```
* Use **ESLint** with `@typescript-eslint/eslint-plugin` and
  `@typescript-eslint/parser` for linting.

## 14. Null & Undefined Handling

### Rules
* **Enable `strictNullChecks`** (included in `strict` mode).
* Prefer `undefined` over `null` as the "absence of value" indicator, unless interacting with
  external APIs that use `null`.
* Use **optional chaining** (`?.`) and **nullish coalescing** (`??`) instead of manual checks.
* **Do NOT** use non-null assertion (`!`) unless you can prove the value is always defined (add a
  comment explaining why).
* Prefer the `satisfies` operator (TS 5.0+) to validate types without widening.

## 15. Type Assertions & Guards

### Rules
* **Prefer type guards** (`is` keyword) over type assertions (`as`).
* Use `as const` for literal narrowing, not `as SpecificType`.
* Use **discriminated unions** with a `kind` / `type` field for state machines and result types.
* Avoid `as unknown as T` double assertions — they are almost always a design smell.
* When assertions are necessary, add a comment justifying them.
* Use `satisfies` for type validation without assertion:

  typescript

  ```
  const palette = {
    red: [255, 0, 0],
    green: '#00ff00',
  } satisfies Record<string, string | number[]>;
  ```

## 16. React & JSX (when applicable)

### Rules
* Use **function declarations** or **named function expressions** for components (not anonymous).
* Define props as an `interface` (e.g., `UserCardProps`), not inline.
* Mark all props as `readonly`.
* **Do NOT** use `React.FC` — it is discouraged since React 18.
* Use `React.ReactElement` or `React.ReactNode` as return type annotation.
* Colocate styles, tests, and types with the component when practical.
* Prefer **controlled components** over uncontrolled.
* Memoize expensive computations with `useMemo`, stable callbacks with `useCallback`.
* Extract custom hooks when logic is reused across components.
* Component file structure:
  1. Imports
  2. Types / Interfaces
  3. Constants
  4. Component function
  5. Helper functions (private to the module)

## 17. Testing Conventions

### Rules
* Test files are colocated or in a `__tests__` directory.
* Name test files `*.test.ts` or `*.spec.ts`.
* Follow the **Arrange → Act → Assert** pattern.
* One assertion concept per test (multiple `expect` calls are okay if they test one logical
  assertion).
* Use **descriptive test names** that read like a sentence.
* Mock external dependencies; do NOT mock the module under test.
* Prefer **dependency injection** to make code testable.
* Aim for high test coverage on business logic; don't chase 100% on boilerplate.
* Use `jest.fn()` or equivalent for spies/mocks; type them properly:

  typescript

  ```
  const mockFetch = jest.fn<Promise<User>, [string]>();
  ```

## 18. Tooling & Configuration
### Recommended `tsconfig.json` (Baseline)
jsonc

### Recommended ESLint Rules
| Rule | Setting |
| --- | --- |
| `@typescript-eslint/no-explicit-any` | `error` |
| `@typescript-eslint/explicit-function-return-type` | `warn` (for exported functions) |
| `@typescript-eslint/no-unused-vars` | `error` |
| `@typescript-eslint/consistent-type-imports` | `error` |
| `@typescript-eslint/no-non-null-assertion` | `warn` |
| `@typescript-eslint/prefer-nullish-coalescing` | `error` |
| `@typescript-eslint/prefer-optional-chain` | `error` |
| `@typescript-eslint/strict-boolean-expressions` | `warn` |
| `@typescript-eslint/naming-convention` | `error` (configured per construct) |

## Usage
### Natural Language Activation
Simply mention **TypeScript** in your conversation — the skill activates automatically.

**Example prompts:**

| Prompt | Skill Response |
| --- | --- |
| "Write a TypeScript function to merge two objects deeply" | Generates a fully typed, standards-compliant `deepMerge<T, U>()` function following all rules above. |
| "Review my TypeScript code for style issues" | Analyses the provided code against this guide and suggests improvements. |
| "Convert this JavaScript to TypeScript" | Converts code, adds strict types, interfaces, and follows all naming / formatting conventions. |
| "What's the TypeScript best practice for error handling?" | Explains the Result pattern, custom error classes, and typed catch blocks per §10. |
| "Create a TypeScript React component for a data table" | Generates a well-typed functional component following §16 React rules with proper props interface. |
| "Set up a new TypeScript project" | Provides `tsconfig.json`, ESLint config, Prettier config, and project structure following §18. |

### Inline Rule References
You can ask about any specific section:

* *"Explain TypeScript naming conventions"* → References §2
* *"How should I handle null in TypeScript?"* → References §14
* *"Show me TypeScript generic best practices"* → References §9

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
- Provide best-practice coding conventions and generate standards-compliant
  TypeScript code
- 触发关键词: conventions, typescript, provide, skills, practice, coding, best

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例
### 示例1：基础用法
```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用TypeScript？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: TypeScript有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
