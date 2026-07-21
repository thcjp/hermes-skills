---
slug: json-toolkit-pro
name: json-toolkit-pro
version: "1.0.0"
displayName: JSON工具箱(专业版)
summary: 全功能 JSON 处理，含高级序列化、解析安全、Unicode 边界、自动化校验。
license: Proprietary
edition: pro
description: |-
  全功能 JSON 处理。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- 集成工具
- 数据规范
- 企业效率
- 安全
tools:
  - - read
- exec
---

# JSON 工具箱（专业版）

## 概述

专业版在免费版基础最佳实践之上，扩展了高级序列化、深度解析安全、Unicode 边界三大能力，覆盖企业级与安全敏感场景。支持 Map/Set/BigInt/循环引用的自定义序列化、reviver 类型重建、原型污染防护、BOM 与控制字符处理、自动化校验流水线，让 JSON 处理"边界全覆盖、安全无死角"。

## 核心能力

| 能力 | 说明 | 免费版 | 专业版 |
|------|------|--------|--------|
| Schema 校验 | 不可信输入校验 | 是 | 是 |
| 命名规范 | 一致性管理 | 是 | 是 |
| 空值处理 | null 与缺失区分 | 是 | 是 |
| 日期时间 | ISO 8601 规范 | 是 | 是 |
| 数字与 ID | 大数与金额 | 是 | 是 |
| 结构最佳实践 | 嵌套与信封 | 是 | 是 |
| API 响应模式 | 错误结构化 | 是 | 是 |
| 基础序列化 | toJSON 注意事项 | 是 | 是 |
| 基础解析安全 | try/catch | 是 | 是 |
| 高级序列化 | Map/Set/BigInt/循环引用 | 否 | 是 |
| 深度解析安全 | reviver 与 BOM | 否 | 是 |
| Unicode 边界 | 代理对与控制字符 | 否 | 是 |
| 原型污染防护 | __proto__ 与 Object.create | 否 | 是 |
| 自动化校验流水线 | 批量校验与报告 | 否 | 是 |
| 自定义 replacer/reviver | 模板化 | 否 | 是 |
| 敏感数据剥离 | 安全序列化 | 否 | 是 |

## 使用场景

### 场景 1：企业级 API 契约校验
API 网关团队用自动化校验流水线批量校验所有接口的请求与响应 Schema，生成校验报告标注违规字段与位置。专业版的批量校验覆盖 50+ 接口，避免人工逐个检查。

### 场景 2：复杂数据结构序列化
应用需要序列化含 Map、Set、BigInt、Date 的复杂对象到 JSON 并反序列化还原。专业版的自定义 replacer 与 reviver 模板处理这些非标准类型，避免 `toJSON()` 默认行为带来的意外。

### 场景 3：安全敏感数据脱敏
日志服务在序列化用户数据前剥离敏感字段（密码、token、身份证号），避免依赖消费方忽略额外字段。专业版的敏感数据剥离在序列化时完成，从源头杜绝泄露。

### 场景 4：跨语言数据交换边界处理
跨语言系统交换数据时遇到 BOM 头、控制字符、emoji 代理对导致解析失败。专业版的 Unicode 边界处理在解析前清洗这些隐患，确保跨语言兼容。

## 快速开始

> 上手时间：< 60 秒。专业版提供自定义模板，建议先复用模板再定制。

### 步骤 1：处理循环引用

```javascript
// 检测循环引用后再序列化
function safeStringify(obj) {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (typeof value === 'object' && value !== null) {
      if (seen.has(value)) return '[Circular]';
      seen.add(value);
    }
    return value;
  });
}
```

### 步骤 2：自定义 replacer 处理 Map/Set/BigInt

```javascript
const data = { map: new Map([['a', 1]]), big: 9007199254740993n };
JSON.stringify(data, (key, value) => {
  if (value instanceof Map) return Object.fromEntries(value);
  if (typeof value === 'bigint') return value.toString();
  return value;
});
```

### 步骤 3：reviver 类型重建

```javascript
JSON.parse(json, (key, value) => {
  if (key.endsWith('_at')) return new Date(value);
  if (/^\d+n$/.test(value)) return BigInt(value.slice(0, -1));
  return value;
});
```

### 步骤 4：剥离 BOM 与控制字符

```javascript
function sanitizeInput(str) {
  return str
    .replace(/^\uFEFF/, '')           // 剥离 BOM
    .replace(/[\u0000-\u001F]/g, ''); // 剥离控制字符
}
JSON.parse(sanitizeInput(rawInput));
```

## 示例

### 自动化校验流水线

```yaml
# json_validation_pipeline.yaml
schemas_dir: ./schemas
endpoints:
  - name: create_user
    request_schema: user_create.json
    response_schema: user_response.json
  - name: list_orders
    request_schema: order_list.json
    response_schema: order_list_response.json
options:
  additional_properties: false
  strict_required: true
  report_format: json   # json / markdown / html
  fail_fast: false      # false 时校验全部，汇总报告
```

### 敏感字段剥离配置

```json
{
  "strip_fields": ["password", "token", "secret", "ssn", "credit_card"],
  "mask_fields": {"email": "partial", "phone": "partial"},
  "depth": 5,
  "throw_on_unknown": false
}
```

### Unicode 边界处理对照表

| 字符 | 问题 | 处理方式 |
|------|------|----------|
| BOM `\uFEFF` | 文件头导致解析失败 | 解析前剥离 |
| 控制字符 U+0000–U+001F | 粘贴文本含不可见字符 | 剥离或转义 |
| emoji 单字符 `\u1F600` | 非法代理对 | 用代理对 `\uD83D\uDE00` |
| 嵌入式 NULL `\u0000` | 截断字符串 | 剥离或拒绝 |

## 最佳实践

1. **循环引用先检测**：序列化前用 WeakSet 检测循环引用，避免 `JSON.stringify` 抛出异常。
2. **自定义 replacer 处理非标准类型**：Map/Set/BigInt 需自定义 replacer 转换为可序列化形式。
3. **reviver 还原类型**：反序列化时用 reviver 重建 Date、BigInt、自定义类型，避免类型丢失。
4. **原型污染防护**：解析含 `__proto__` 的输入会污染原型，用 `Object.create(null)` 或过滤危险键。
5. **解析必 try/catch**：外部来源的 JSON 畸形很常见，解析必须包裹 try/catch。
6. **BOM 先剥离**：文件输入可能含 BOM 头，解析前剥离 `\uFEFF`。
7. **控制字符清洗**：粘贴文本可能含 U+0000–U+001F 控制字符，序列化前清洗或转义。
8. **emoji 用代理对**：😀 需要 `\uD83D\uDE00` 代理对，单个 `\u1F600` 非法。
9. **敏感数据源头剥离**：序列化前剥离敏感字段，不依赖消费方忽略，从源头杜绝泄露。
10. **自动化校验全覆盖**：用流水线批量校验所有接口 Schema，生成报告定位违规，避免人工遗漏。
11. **掩码优于完全剥离**：邮箱、手机号部分掩码（`a***@example.com`）保留可识别性，优于完全删除。
12. **toJSON 注意默认行为**：`toJSON()` 会静默覆盖输出（Date 变字符串、自定义类意外），序列化前确认是否有 toJSON。

## 常见问题

### Q1：循环引用如何安全序列化？

A：用 WeakSet 跟踪已访问对象，遇到重复时返回 `[Circular]` 标记而非抛出异常。或使用 `flatted` 等专用库处理循环结构。

### Q2：Map 和 Set 为什么不能直接序列化？

A：`JSON.stringify` 对 Map/Set 返回 `{}`（空对象），数据丢失。需自定义 replacer 将 Map 转为 `Object.fromEntries`，Set 转为数组。

### Q3：BigInt 序列化报错怎么办？

A：`JSON.stringify` 不支持 BigInt，直接报 TypeError。需在 replacer 中 `value.toString()` 转字符串，反序列化时用 reviver 还原。

### Q4：__proto__ 键如何污染原型？

A：`JSON.parse('{"__proto__":{"isAdmin":true}}')` 会污染 Object.prototype，导致所有对象继承 `isAdmin: true`。防护方式：(1) 用 `Object.create(null)` 创建对象；(2) 过滤 `__proto__`、`constructor`、`prototype` 键。

### Q5：BOM 头为何导致解析失败？

A：UTF-8 文件可能以 `\uFEFF`（BOM）开头，`JSON.parse` 会将其视为非法字符报错。解析前用 `str.replace(/^\uFEFF/, '')` 剥离。

### Q6：emoji 为何解析异常？

A：emoji（如 😀）在 JSON 中需用代理对 `\uD83D\uDE00` 表示。单个 `\u1F600` 是非法代理对，会导致解析错误或显示乱码。

### Q7：自动化校验流水线如何集成到 CI/CD？

A：将校验脚本作为 CI 步骤，读取配置文件批量校验所有 Schema，校验失败时流水线红灯。建议 `fail_fast: false` 汇总全部违规再修复。

### Q8：敏感字段剥离与字段过滤有何区别？

A：字段过滤在消费方忽略额外字段（被动）；敏感字段剥离在序列化时移除（主动）。后者更安全，因为剥离后数据中根本不存在敏感字段，即使被记录日志也安全。

### Q9：toJSON() 何时会带来意外？

A：Date 对象的 `toJSON()` 返回 ISO 字符串（而非 Date 对象），自定义类的 `toJSON()` 可能改变输出结构。序列化前确认对象是否有 toJSON 方法，避免静默覆盖。

### Q10：专业版是否支持自定义校验规则？

A：支持。除 JSON Schema 标准校验外，可自定义业务规则（如"金额必须为正""邮箱格式校验"），集成到自动化校验流水线。

## 错误处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 序列化报循环引用 | 对象存在循环结构 | 用 WeakSet 检测或 flatted 库 | P1 |
| Map/Set 序列化为空 | 未自定义 replacer | replacer 中转换 Map/Set | P2 |
| BigInt 报 TypeError | 未转换即序列化 | replacer 中 toString | P2 |
| 解析报 __proto__ 污染 | 输入含危险键 | Object.create(null) 或过滤键 | P1 |
| 解析报非法字符 | BOM 或控制字符 | 剥离 BOM 与控制字符 | P2 |
| emoji 显示乱码 | 单字符而非代理对 | 用代理对表示 | P3 |
| 敏感字段泄露 | 未在序列化时剥离 | 配置 strip_fields | P1 |
| 类型丢失 | 反序列化未用 reviver | reviver 重建 Date/BigInt | P2 |
| 校验报告缺失 | fail_fast 为 true | 设为 false 汇总全部 | P3 |
| 跨语言解析失败 | Unicode 边界未处理 | 清洗 BOM 与控制字符 | P2 |

## 专业版特性

本专业版相比免费版新增以下能力：
- 高级序列化：Map/Set/BigInt/循环引用的自定义处理
- 深度解析安全：reviver 类型重建、BOM 剥离、原型污染防护
- Unicode 边界：代理对、控制字符、BOM 的清洗与转义
- 自动化校验流水线：批量校验多接口 Schema，生成报告
- 自定义 replacer/reviver 模板：复用与定制类型转换
- 敏感数据剥离：序列化时主动移除敏感字段，源头杜绝泄露
- 原型污染防护：__proto__/constructor/prototype 键过滤
- 跨语言兼容：BOM 与控制字符清洗，确保跨语言交换

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 基础校验 + 命名 + 空值 + 日期 + 数字 + 结构 | 个人试用 |
| 收费专业版 | ¥19.9/月 | 全功能 + 高级序列化 + 解析安全 + Unicode + 自动化校验 + 优先支持 | 团队 / 企业 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **编程语言**：任意支持 JSON 的语言（JavaScript / Python / Go / Java 等）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| JSON Schema 校验库 | 库 | 推荐 | 各语言生态均有（如 JS 的 ajv、Python 的 jsonschema） |
| flatted（可选） | 库 | 可选 | `npm install flatted` 或 `pip install flatted`，用于循环引用 |
| 标准库 JSON 模块 | 运行时 | 必需 | 各语言标准库自带 |

### API Key 配置
- **本 Skill 基于指令驱动**：无需额外 API Key，纯 Markdown 最佳实践指南与模板
- **自动化校验流水线（可选）**：如需对接外部 Schema 注册中心，按对应服务配置凭证

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，自动化校验流水线需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 遵循 JSON 处理最佳实践，支持自动化校验与模板复用

## 已知限制

- 需要API Key，无Key环境无法使用
