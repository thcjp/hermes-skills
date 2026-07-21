---
slug: javascript-skills
name: javascript-skills
version: "1.0.2"
displayName: JavaScript
summary: A comprehensive JavaScript style guide skill. When activated, it provides
  best-practice JavaScrip...
license: MIT-0
description: |-
  A comprehensive JavaScript style guide skill。When activated, it provides
  best-practice JavaScrip。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
- exec
# JavaScript
## Activation
---
This skill activates when the user mentions or implies **JavaScript** in their request. Once activated, it:

* Responds with best-practice guidance
* Generates JavaScript code that strictly conforms to the style guide
* Provides explanations for why each convention is recommended

## Complete Style Rules
### 1. References
* Use `const` for all references; avoid `var`.
* If you must reassign references, use `let` instead of `var`.
* Both `const` and `let` are block-scoped, whereas `var` is function-scoped.

```javascript
// bad
var count = 1;

// good
const count = 1;
let mutableValue = 1;
mutableValue += 1;
```

### 2. Objects
* Use literal syntax for object creation.
* Use computed property names when creating objects with dynamic property names.
* Use object method shorthand and property value shorthand.
* Group shorthand properties at the beginning of the object declaration.
* Only quote properties that are invalid identifiers.
* Prefer the object spread syntax (`...`) over `Object.assign` to shallow-copy objects.

> 详细代码示例已移至 `references/detail.md`

### 3. Arrays
* Use literal syntax for array creation.
* Use `Array.from` or the spread operator to convert array-like objects.
* Use `return` statements in array method callbacks.
* Use line breaks after the opening bracket and before the closing bracket if the array has multiple lines.

> 详细代码示例已移至 `references/detail.md`

### 4. Destructuring
* Use object destructuring when accessing multiple properties of an object.
* Use array destructuring.
* Use object destructuring for multiple return values, not array destructuring.

> 详细代码示例已移至 `references/detail.md`

### 5. Strings
* Use single quotes `''` for strings.
* Use template literals for string interpolation and multi-line strings.
* Never use `/* REMOVED: eval */ ()` on a string.
* Do not unnecessarily escape characters in strings.

```javascript
// bad
const name = "Alice";
const greeting = 'Hello, ' + name + '!';

// good
const name = 'Alice';
const greeting = `Hello, ${name}!`;
```

### 6. Functions
* Use named function expressions instead of function declarations.
* Wrap immediately invoked function expressions (IIFE) in parentheses.
* Never declare a function in a non-function block (`if`, `while`, etc.).
* Never name a parameter `arguments`.
* Use default parameter syntax rather than mutating function arguments.
* Always put default parameters last.
* Never use the `Function` constructor to create a new function.
* Use the spread operator `...` to call variadic functions.
* Use rest parameters (`...args`) instead of `arguments`.

> 详细代码示例已移至 `references/detail.md`

### 7. Arrow Functions
* Use arrow function notation for anonymous functions (callbacks).
* If the function body consists of a single expression, omit the braces and use the implicit return.
* If the expression spans multiple lines, wrap it in parentheses for readability.
* Always include parentheses around arguments for clarity and consistency.

> 详细代码示例已移至 `references/detail.md`

### 8. Classes & Constructors
* Always use `class`; avoid manipulating `prototype` directly.
* Use `extends` for inheritance.
* Methods can return `this` to enable method chaining.
* Classes have a default constructor if no constructor is specified; an empty constructor or one that just delegates to a parent is unnecessary.
* Avoid duplicate class members.

> 详细代码示例已移至 `references/detail.md`

### 9. Modules
* Always use ES modules (`import`/`export`) over a non-standard module system.
* Do not use wildcard imports.
* Do not export directly from an import.
* Only import from a path in one place.
* Do not export mutable bindings.
* Prefer default export for modules that only export a single thing.
* Put all `import`s above non-import statements.
* Multi-line imports should be indented like multi-line array and object literals.

> 详细代码示例已移至 `references/detail.md`

### 10. Iterators and Generators
* Prefer JavaScript's higher-order functions over `for-in` or `for-of` loops.
* Use `map`, `filter`, `reduce`, `find`, `findIndex`, `every`, `some`, etc.
* Don't use generators for now (if targeting ES5 environments).

```javascript
const numbers = [1, 2, 3, 4, 5];

// bad
let sum = 0;
for (const num of numbers) {
  sum += num;
}

// good
const sum = numbers.reduce((total, num) => total + num, 0);

// filtering
const evens = numbers.filter((num) => num % 2 === 0);
```

### 11. Properties
* Use dot notation when accessing properties.
* Use bracket notation `[]` when accessing properties with a variable.
* Use the exponentiation operator `**` instead of `Math.pow`.

```javascript
const luke = { jedi: true, age: 28 };

// dot notation
const isJedi = luke.jedi;

// bracket notation
const prop = 'jedi';
const isJedi = luke[prop];

// exponentiation
const result = 2 ** 10;
```

### 12. Variables
* Always use `const` or `let`; never use `var`.
* Use one `const` or `let` declaration per variable or assignment.
* Group all `const`s and then group all `let`s.
* Assign variables where you need them, but place them in a reasonable place.
* Don't chain variable assignments.
* Avoid using unary increments (`++`, `--`); use `+= 1` / `-= 1` instead.
* Avoid linebreaks before or after `=` in an assignment.

> 详细代码示例已移至 `references/detail.md`

### 13. Hoisting
* `var` declarations get hoisted; `const` and `let` are in Temporal Dead Zone.
* Named function expressions hoist the variable name but not the function body.
* Function declarations hoist the name and the function body.

### 14. Comparison Operators & Equality
* Use `===` and `!==` over `==` and `!=`.
* Use shortcuts for booleans, but explicit comparisons for strings and numbers.
* Use braces to create blocks in `case` and `default` clauses that contain lexical declarations.
* Ternaries should not be nested and generally be single-line expressions.
* Avoid unneeded ternary statements.
* When mixing operators, enclose them in parentheses (except `**`, `+`, `-`).

```javascript
// bad
if (isValid == true) { /* ... */ }
if (name != '') { /* ... */ }

// good
if (isValid) { /* ... */ }
if (name !== '') { /* ... */ }
if (collection.length > 0) { /* ... */ }

// no nested ternaries
const thing = foo === 123 ? bar : foobar;
```

### 15. Blocks
* Use braces with all multiline blocks.
* Put `else` on the same line as the `if` block's closing brace.
* If an `if` block always executes a `return`, the subsequent `else` block is unnecessary.

> 详细代码示例已移至 `references/detail.md`

### 16. Control Statements
* If a control statement (`if`, `while`, etc.) gets too long, each grouped condition should be on a new line, with the logical operator at the beginning of the line.
* Don't use selection operators in place of control statements.

```javascript
if (
  foo === 123
  && bar === 'abc'
) {
  thing1();
}
```

### 17. Comments
* Use `/** ... */` for multiline comments.
* Use `//` for single-line comments. Place them on a new line above the subject.
* Start all comments with a space for readability.
* Prefix comments with `FIXME:` or `TODO:` to annotate problems or suggest actions.

> 详细代码示例已移至 `references/detail.md`

### 18. Whitespace
* Use soft tabs (spaces) set to 2 spaces.
* Place 1 space before the leading brace.
* Place 1 space before the opening parenthesis in control statements.
* Set off operators with spaces.
* End files with a single newline character.
* Use indentation when making long method chains (more than 2 method chains).
* Leave a blank line after blocks and before the next statement.
* Do not pad blocks with blank lines.
* Do not use multiple blank lines to pad your code.
* Do not add spaces inside parentheses, brackets.
* Add spaces inside curly braces.

> 详细代码示例已移至 `references/detail.md`

### 19. Commas
* Do **not** use leading commas.
* Use trailing commas (dangling commas) for multiline structures.

> 详细代码示例已移至 `references/detail.md`

### 20. Semicolons
* **Always** use semicolons.

```javascript
// bad
const name = 'Alice'

// good
const name = 'Alice';
```

### 21. Type Casting & Coercion
* Perform type coercion at the beginning of the statement.
* Use `String()` for strings, `Number()` for numbers, `Boolean()` or `!!` for booleans.
* Use `parseInt` always with a radix.

```javascript
const val = '4';

// bad
const totalScore = val + 0;

// good
const totalScore = Number(val);
const inputValue = String(someNum);
const hasAge = Boolean(age);
const hasName = !!name;
const count = parseInt(inputValue, 10);
```

### 22. Naming Conventions
* Avoid single-letter names; be descriptive.
* Use **camelCase** for objects, functions, and instances.
* Use **PascalCase** for classes and constructors.
* Use **UPPERCASE_SNAKE_CASE** for constants that are exported and truly immutable.
* Do not use trailing or leading underscores.
* A base filename should exactly match the name of its default export.
* Use **camelCase** when exporting a function; use **PascalCase** when exporting a class / constructor / singleton / function library / bare object.
* Acronyms and initialisms should always be all uppercased or all lowercased.

> 详细代码示例已移至 `references/detail.md`

### 23. Accessors
* Accessor functions for properties are not required.
* Do not use JavaScript getters/setters as they cause unexpected side effects.
* If you do make accessor functions, use `getVal()` and `setVal('value')`.
* If the property/method is a boolean, use `isVal()` or `hasVal()`.

```javascript
// bad
dragon.age();

// good
dragon.getAge();
dragon.setAge(25);
dragon.isAlive();
dragon.hasWings();
```

### 24. Events
* When attaching data payloads to events, pass an object (hash) instead of a raw value.

```javascript
// bad
emitter.emit('itemUpdate', item.id);

// good
emitter.emit('itemUpdate', { itemId: item.id });
```

### 25. Promises & Async/Await
* Prefer `async`/`await` over chaining `.then()` and `.catch()`.
* Always handle errors with `try...catch` in `async` functions.
* Avoid mixing callbacks and promises.
* Use `Promise.all` for concurrent independent async operations.
* Use `Promise.allSettled` when you need results of all promises regardless of rejection.

> 详细代码示例已移至 `references/detail.md`

### 26. Error Handling
* Only throw `Error` objects (or subclasses of `Error`).
* Always catch errors where they can be meaningfully handled.
* Use custom error classes for domain-specific errors.

> 详细代码示例已移至 `references/detail.md`

### 27. Optional Chaining & Nullish Coalescing
* Use optional chaining (`?.`) to access nested properties that may not exist.
* Use nullish coalescing (`??`) instead of `||` when you want to allow falsy values like `0` or `''`.

```javascript
// bad
const city = user && user.address && user.address.city;
const port = config.port || 3000; // breaks if port is 0

// good
const city = user?.address?.city;
const port = config.port ?? 3000;
```

### 28. Standard Library
* Use `Number.isNaN` instead of global `isNaN`.
* Use `Number.isFinite` instead of global `isFinite`.

```javascript
// bad
isNaN('1.2');
isFinite('2e3');

// good
Number.isNaN('1.2');
Number.isFinite('2e3');
```

## Usage
This is a **Prompt-based Skill** (natural language activation).

### How to Use
1. **Automatic Activation**: Simply mention "JavaScript" in your request. The skill will be activated automatically.
2. **Ask for Style Guidance**:

   text

   ```
   "How should I write a JavaScript function that fetches user data?"
   ```
3. **Request Code Review**:

   text

   ```
   "Review this JavaScript code for style issues: [paste code]"
   ```
4. **Generate Compliant Code**:

   text

   ```
   "Write a JavaScript module to handle form validation"
   ```
5. **Ask About Specific Rules**:

   text

   ```
   "What's the correct way to declare variables in JavaScript?"
   "How should I handle async errors in JavaScript?"
   ```

### 示例
**User**: Write a JavaScript utility function to deep clone an object.

**Skill Response**: Generates clean, style-guide-compliant code:

> 详细代码示例已移至 `references/detail.md`

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
- A comprehensive JavaScript style guide skill
- When activated, it provides
  best-practice JavaScrip
- 触发关键词: style, comprehensive, guide, skills, javascript, skill

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

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用JavaScript？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: JavaScript有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
