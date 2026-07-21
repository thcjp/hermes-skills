# 详细参考 - typescript-skills

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (typescript)

```typescript
// ✅ Good — type guard function
function isUser(value: unknown): value is User {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'name' in value
  );
}

// ✅ Good — discriminated union
interface Success<T> {
  kind: 'success';
  data: T;
}
interface Failure {
  kind: 'failure';
  error: Error;
}
type Result<T> = Success<T> | Failure;

function handleResult<T>(result: Result<T>): T {
  switch (result.kind) {
    case 'success':
      return result.data;
    case 'failure':
      throw result.error;
  }
}
```

## 代码示例 (typescript)

```typescript
// ✅ Good — custom error class
class AppError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly statusCode: number = 500,
  ) {
    super(message);
    this.name = 'AppError';
  }
}

// ✅ Good — typed error handling
function parseJson<T>(raw: string): T {
  try {
    return JSON.parse(raw) as T;
  } catch (error) {
    throw new AppError(
      `Failed to parse JSON: ${error instanceof Error ? error.message : String(error)}`,
      'PARSE_ERROR',
      400,
    );
  }
}
```

## 代码示例 ()

```
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true
  }
}
```

## 代码示例 (typescript)

```typescript
// ✅ Good — braces always, even for single-line if
if (isValid) {
  process();
}

// ❌ Bad
if (isValid) process();

// ✅ Good — trailing comma
const config = {
  host: 'localhost',
  port: 3000,
  debug: true,
};

// ✅ Good — consistent object shorthand
const name = 'Alice';
const user = { name, age: 30 };
```

## 代码示例 (tsx)

```tsx
// ✅ Good — functional component with explicit props type
interface UserCardProps {
  readonly user: User;
  readonly onSelect?: (userId: string) => void;
}

export function UserCard({ user, onSelect }: UserCardProps): React.ReactElement {
  const handleClick = useCallback(() => {
    onSelect?.(user.id);
  }, [onSelect, user.id]);

  return (
    <div className="user-card" onClick={handleClick} role="button" tabIndex={0}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
}
```

## 代码示例 (typescript)

```typescript
// ✅ Good — async/await
async function fetchUser(id: string): Promise<User> {
  const response = await httpClient.get<User>(`/users/${id}`);
  return response.data;
}

// ✅ Good — parallel execution
async function fetchDashboard(userId: string): Promise<Dashboard> {
  const [user, posts, notifications] = await Promise.all([
    fetchUser(userId),
    fetchPosts(userId),
    fetchNotifications(userId),
  ]);
  return { user, posts, notifications };
}
```

## 代码示例 (typescript)

```typescript
// ✅ Good — descriptive when intent is ambiguous
function merge<TTarget, TSource>(target: TTarget, source: TSource): TTarget & TSource {
  return { ...target, ...source };
}

// ✅ Good — single-letter when intent is obvious
function identity<T>(value: T): T {
  return value;
}

// ✅ Good — constrained generics
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

## 代码示例 (typescript)

```typescript
// ✅ Good — optional chaining
const city = user?.address?.city;

// ✅ Good — nullish coalescing
const displayName = user.nickname ?? user.name ?? 'Anonymous';

// ✅ Good — explicit null checks for critical paths
function getUser(id: string): User {
  const user = repository.findById(id);
  if (user === undefined) {
    throw new AppError(`User not found: ${id}`, 'USER_NOT_FOUND', 404);
  }
  return user;
}
```

## 代码示例 (typescript)

```typescript
// ✅ Good — descriptive test structure
describe('UserService', () => {
  describe('findById', () => {
    it('should return the user when the id exists', async () => {
      const user = await service.findById('user-1');
      expect(user).toEqual(expect.objectContaining({ id: 'user-1' }));
    });

    it('should return undefined when the id does not exist', async () => {
      const user = await service.findById('non-existent');
      expect(user).toBeUndefined();
    });
  });
});
```


## Table of Contents
1. [General Principles](#1-general-principles)
2. [Naming Conventions](#2-naming-conventions)
3. [Types & Interfaces](#3-types--interfaces)
4. [Enums](#4-enums)
5. [Variables & Constants](#5-variables--constants)
6. [Functions](#6-functions)
7. [Classes](#7-classes)
8. [Modules & Imports](#8-modules--imports)
9. [Generics](#9-generics)
10. [Error Handling](#10-error-handling)
11. [Async / Await & Promises](#11-async--await--promises)
12. [Comments & Documentation](#12-comments--documentation)
13. [Formatting & Style](#13-formatting--style)
14. [Null & Undefined Handling](#14-null--undefined-handling)
15. [Type Assertions & Guards](#15-type-assertions--guards)
16. [React & JSX (when applicable)](#16-react--jsx-when-applicable)
17. [Testing Conventions](#17-testing-conventions)
18. [Tooling & Configuration](#18-tooling--configuration)



---

### Rules
* **Always use `const`** unless the variable needs reassignment; then use `let`.
* **Never use `var`**.
* Declare variables as close to their first usage as possible.
* One variable declaration per statement.
* Prefer destructuring for extracting properties:

  typescript

  ```
  // ✅ Good
  const { name, age } = user;

  // ❌ Bad
  const name = user.name;
  const age = user.age;
  ```
* Use `as const` for immutable literal objects / arrays:

  typescript

  ```
  const ROUTES = {
    home: '/',
    about: '/about',
    contact: '/contact',
  } as const;
  ```



---

### Rules
* **Annotate return types** for all exported / public functions.
* Prefer **arrow functions** for callbacks and inline functions.
* Prefer **function declarations** for top-level named functions (they are hoisted and more
  readable in stack traces).
* **Maximum parameters**: 3. If more are needed, group them into an options object:

  typescript

  ```
  // ✅ Good
  interface CreateUserOptions {
    name: string;
    email: string;
    role?: Role;
    department?: string;
  }
  function createUser(options: CreateUserOptions): User { ... }

  // ❌ Bad — too many positional parameters
  function createUser(name: string, email: string, role: Role, dept: string): User { ... }
  ```
* Do **not** use `arguments`; use rest parameters (`...args`) instead.
* Avoid `Function` type. Use specific function signatures.
* Keep functions small — ideally under 30 lines of logic.
* Functions should **do one thing**.
* Prefer **early returns** to reduce nesting:

  typescript

  ```
  // ✅ Good
  function getDiscount(user: User): number {
    if (!user.isPremium) return 0;
    if (user.yearsActive < 2) return 5;
    return 10;
  }
  ```



---

### Rules
* Prefer **composition over inheritance**.
* Use `readonly` for properties that should not change after construction.
* Member ordering:
  1. Static fields
  2. Instance fields
  3. Constructor
  4. Static methods
  5. Public methods
  6. Protected methods
  7. Private methods
* Use **explicit access modifiers** (`public`, `protected`, `private`) on every member.
* **Do NOT** prefix private members with `_`. TypeScript's `private` keyword is sufficient.
* Use `#` (ES private fields) when true runtime privacy is required.
* Prefer **parameter properties** for simple constructor-only assignments:

  typescript

  ```
  class Logger {
    constructor(private readonly prefix: string) {}
  }
  ```
* Avoid classes with only static methods — use plain functions in a module instead.
* Implement interfaces explicitly:

  typescript

  ```
  class UserRepositoryImpl implements UserRepository { ... }
  ```



---

### Rules
* **Prefer named exports** over default exports (better refactoring, auto-import support).
* Use default exports only for React components if the project convention requires it.
* Use `import type` / `export type` for type-only imports to help bundlers tree-shake:

  typescript

  ```
  import type { User } from './user';
  ```
* Group and order imports:
  1. Node built-ins (`node:fs`, `node:path`)
  2. External packages (`react`, `lodash`)
  3. Internal aliases (`@/utils`, `@/components`)
  4. Relative parent (`../`)
  5. Relative sibling (`./`)
* Separate each group with a blank line.
* **Do NOT** use wildcard imports (`import * as`) unless re-exporting a module namespace.
* Keep barrel files (`index.ts`) thin — do not add logic.



---

## 12. Comments & Documentation
```typescript
/**
 * Calculate the compound interest for a principal amount.
 *
 * @param principal - The initial amount of money.
 * @param rate - The annual interest rate (decimal, e.g. 0.05 for 5%).
 * @param times - Number of times interest is compounded per year.
 * @param years - Number of years the money is invested.
 * @returns The total amount after compound interest.
 *
 * @example
 * ```typescript
 * const total = compoundInterest(1000, 0.05, 12, 10);
 * // total ≈ 1647.01
 * ```
 */
function compoundInterest(
  principal: number,
  rate: number,
  times: number,
  years: number,
): number {
  return principal * Math.pow(1 + rate / times, times * years);
}
```



---
