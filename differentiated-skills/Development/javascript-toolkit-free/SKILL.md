---
slug: javascript-toolkit-free
name: javascript-toolkit-free
version: "1.0.0"
displayName: JavaScript工具包免费版
summary: JavaScript 陷阱防范与优选实践指南，覆盖异步、类型转换、闭包等核心场景。
license: Proprietary
edition: free
description: |-
  面向 JavaScript 开发者的代码陷阱防范工具，帮助编写健壮的 JS 代码。核心能力:
  - 相等性比较陷阱（== vs ===）识别与规避
  - this 绑定问题分析与修复
  - 闭包陷阱与变量捕获防范
  - 数组变异陷阱与不可变操作
  - 异步编程陷阱与正确模式
  - 隐式类型转换陷阱识别

  适用场景:
  - JavaScript 代码编写与审查时的陷阱规避
  - 异步编程的错误排查
  - 类型转换与比较的边界情况处理

  差异化: 免费版聚焦 JavaScript 核心陷阱的识别与防范...
tags:
- 开发工具
- JavaScript
- 代码质量
- 异步编程
tools:
  - - read
- exec
# JavaScript 工具包（免费版）
## 概述
---
本工具为 JavaScript 开发者提供代码陷阱防范与优选实践指引，覆盖相等性比较、this 绑定、闭包、数组变异、异步编程、类型转换、严格模式等核心场景。通过自然语言指令驱动，帮助开发者识别和规避 JavaScript 中常见的陷阱，编写更加健壮、可靠的代码。免费版聚焦个人开发者高频遇到的语言陷阱，提供简明速查表与代码示例。

## 核心能力
| 能力模块 | 描述 | 典型陷阱 |
| --- | --- | --- |
| 相等性比较 | == 与 === 的区别 | `"0" == false` 为 true |
| this 绑定 | 函数中 this 的指向 | 回调中 this 丢失 |
| 闭包陷阱 | 变量捕获问题 | 循环中共享变量 |
| 数组变异 | 原地修改方法 | sort/reverse 修改原数组 |
| 异步编程 | Promise/async 陷阱 | 忘记 await、forEach 不等待 |
| 类型转换 | 隐式转换规则 | `[] + {}` 的结果 |
| 数字精度 | 浮点数计算 | `0.1 + 0.2 !== 0.3` |
| 迭代 | for...in vs for...of | 遍历键还是值 |

## 使用场景
### 场景一：异步编程陷阱排查
开发者遇到异步代码不按预期执行的问题。

> 详细代码示例已移至 `references/detail.md`

### 场景二：this 绑定问题修复
开发者的事件回调中 this 指向错误。

> 详细代码示例已移至 `references/detail.md`

### 场景三：数组不可变操作
开发者修改数组后发现原始数据被意外修改。

> 详细代码示例已移至 `references/detail.md`

## 不适用场景

以下场景JavaScript工具包免费版不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理


## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求。


## 快速开始
### 相等性比较速查
```javascript
// 始终使用 === 而非 ==
0 == false       // true（不安全）
0 === false      // false（安全）
"" == false      // true（不安全）
"" === false     // false（安全）
"0" == false     // true（不安全）
"0" === false    // false（安全）
null == undefined  // true
null === undefined // false

// NaN 判断
NaN === NaN        // false
Number.isNaN(NaN)  // true（正确方式）
isNaN("hello")     // true（会先转换类型）
Number.isNaN("hello")  // false（不转换类型）

// null 检查
typeof null        // "object"（历史遗留）
typeof undefined   // "undefined"
null === null      // true
null === undefined // false
```

### 闭包陷阱速查

> 详细代码示例已移至 `references/detail.md`

### 数字精度速查
```javascript
// 浮点数精度问题
0.1 + 0.2          // 0.30000000000000004
0.1 + 0.2 === 0.3  // false

// 解决方案一：整数计算（推荐用于金额）
const cents = 10 + 20;  // 以分为单位
const yuan = cents / 100;

// 解决方案二：toFixed（用于显示）
(0.1 + 0.2).toFixed(2)  // "0.30"（字符串）

// 解决方案三：精度库
// npm install decimal.js
import Decimal from 'decimal.js';
new Decimal(0.1).plus(0.2).toNumber()  // 0.3

// 大整数精度
Number.MAX_SAFE_INTEGER  // 9007199254740991
9007199254740992 === 9007199254740993  // true（精度丢失）

// 使用 BigInt
9007199254740992n === 9007199254740993n  // false
```

## 示例
### 隐式类型转换速查
```javascript
// 加法：字符串优先
"5" + 1      // "51"（数字转字符串）
"5" + true   // "5true"
[] + []      // ""（数组转字符串）
[] + {}      // "[object Object]"
{} + []      // 0（特殊：{} 被解析为块）

// 减法：数字优先
"5" - 1      // 4（字符串转数字）
"5" - "2"    // 3
true - 1     // 0

// 比较运算
"10" < "9"   // true（字符串比较）
"10" < 9     // false（转为数字比较）

// 布尔转换（falsy 值）
// false, 0, -0, 0n, "", null, undefined, NaN
// 所有其他值都是 truthy

// 显式转换（推荐）
String(123)      // "123"
Number("123")    // 123
Boolean("")      // false
parseInt("12px") // 12
parseFloat("1.5em")  // 1.5
```

### 迭代速查
```javascript
// for...in：遍历键（包括继承的）
const obj = { a: 1, b: 2 };
for (const key in obj) {
    console.log(key);  // "a", "b"
}

// for...of：遍历值（需要可迭代）
const arr = [1, 2, 3];
for (const val of arr) {
    console.log(val);  // 1, 2, 3
}

// 对象不可直接用 for...of
for (const val of obj) { }  // TypeError

// 对象遍历的正确方式
Object.keys(obj)      // ["a", "b"]  键
Object.values(obj)    // [1, 2]      值
Object.entries(obj)   // [["a", 1], ["b", 2]]  键值对

for (const [key, val] of Object.entries(obj)) {
    console.log(key, val);
}

// 获取所有属性（含 Symbol）
Reflect.ownKeys(obj)  // 包括 Symbol 和不可枚举属性
```

### 严格模式速查
```javascript
// 文件顶部启用严格模式
"use strict";

// 严格模式下的变化：
// 1. 隐式全局变量报错
x = 5;  // ReferenceError

// 2. this 默认为 undefined
function test() {
    return this;  // undefined（非严格模式为 globalThis）
}

// 3. 禁止重复参数
function bad(a, a) { }  // SyntaxError

// 4. 禁止 with 语句
with (obj) { }  // SyntaxError

// 5. 禁止删除不可删除属性
delete Object.prototype;  // TypeError

// 模块默认启用严格模式
// ES Module 中无需手动声明
export function test() {
    // 自动严格模式
}
```

## 优选实践
1. **始终使用 ===**：避免隐式类型转换的坑

2. **回调用箭头函数**：自动继承外层 this

3. **循环用 let**：避免 var 的变量提升和共享

4. **数组用不可变操作**：toSorted/toReversed 或展开运算符

5. **异步用 async/await**：比 Promise 链更易读

6. **金额用整数计算**：避免浮点精度问题

7. **启用严格模式**：捕获潜在错误

8. **显式类型转换**：不要依赖隐式转换

## 常见问题
### Q1：为什么 forEach 不能 await？
```javascript
// forEach 的回调返回值被忽略，不会等待 Promise
async function bad() {
    [1, 2, 3].forEach(async (n) => {
        await delay(n);
    });
    // 不会等待！
}

// 正确：for...of
async function good() {
    for (const n of [1, 2, 3]) {
        await delay(n);
    }
}
```

### Q2：Promise.all 和 Promise.allSettled 的区别？
```javascript
// all：一个失败就全部失败
const results = await Promise.all([
    fetch('/api/1'),
    fetch('/api/2'),  // 如果失败，整个 Promise.all 失败
]);

// allSettled：等待所有完成，无论成功失败
const results = await Promise.allSettled([
    fetch('/api/1'),
    fetch('/api/2'),
]);
// results: [{status: "fulfilled", value: ...}, {status: "rejected", reason: ...}]
```

### Q3：深拷贝怎么做？
```javascript
// 浅拷贝
const shallow = { ...obj };
const shallowArr = [...arr];

// 深拷贝方式一：structuredClone（推荐）
const deep = structuredClone(obj);

// 深拷贝方式二：JSON（不支持函数、Symbol、循环引用）
const deep = JSON.parse(JSON.stringify(obj));

// 深拷贝方式三：递归
function deepClone(obj) {
    if (obj === null || typeof obj !== 'object') return obj;
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof Array) return obj.map(deepClone);
    const cloned = {};
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            cloned[key] = deepClone(obj[key]);
        }
    }
    return cloned;
}
```

### Q4：如何正确判断数组？
```javascript
// 错误：typeof
typeof []  // "object"

// 正确方式
Array.isArray([1, 2])  // true
Array.isArray('abc')   // false

// 跨框架安全
Array.isArray(document.querySelectorAll('div'))  // false（NodeList）
```

### Q5：如何处理可选链和空值合并？
```javascript
// 可选链 ?.
const name = user?.profile?.name;  // 不会报错，返回 undefined

// 空值合并 ??
const displayName = user?.name ?? '匿名';  // 仅 null/undefined 时用默认值

// 与 || 的区别
0 ?? 'default'   // 0（?? 不处理 0）
0 || 'default'   // "default"（|| 处理所有 falsy）

// 函数调用可选链
const result = obj?.method?.();  // 安全调用
```

### Q6：如何避免内存泄漏？
```javascript
// 1. 清除定时器
const timer = setInterval(() => {}, 1000);
// 组件销毁时
clearInterval(timer);

// 2. 移除事件监听
const handler = () => {};
element.addEventListener('click', handler);
// 组件销毁时
element.removeEventListener('click', handler);

// 3. 清除引用
let heavyData = largeArray;
// 使用完后
heavyData = null;  // 释放引用

// 4. 使用 WeakMap/WeakSet
const cache = new WeakMap();
cache.set(element, data);  // element 被回收时自动清理
```

## 依赖说明
### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js 版本**: 建议 18 及以上（需支持 ES2023+）
- **浏览器**: 现代浏览器（Chrome 90+ / Firefox 88+ / Safari 14+）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 推荐 | nodejs.org 下载 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- 部分示例需要 npm 包（如 decimal.js），按需安装

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 提供 JavaScript 代码建议，代码验证需要 Node.js 执行能力

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
