---
slug: json-repair-kit
name: json-repair-kit
version: "1.0.0"
displayName: Json Repair Kit
summary: "经Node.js求值规范化修复畸形JSON文件"
  Use this to fix trail...
license: MIT
description: |-
  Repair malformed JSON files by normalizing them through Node。js evaluation。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Json Repair Kit

A utility to repair broken or "loose" JSON files (like those with trailing commas, single quotes, or unquoted keys) by parsing them as JavaScript objects and re-serializing as valid JSON.

## Usage

```bash
node skills/json-repair-kit/index.js --file path/to/broken.json

node skills/json-repair-kit/index.js --file broken.json --out fixed.json

node skills/json-repair-kit/index.js --dir config/ --recursive
```

## Supported Repairs

* **Trailing Commas**: `{"a": 1,}` -> `{"a": 1}`
* **Single Quotes**: `{'a': 'b'}` -> `{"a": "b"}`
* **Unquoted Keys**: `{key: "value"}` -> `{"key": "value"}`
* **Comments**: Removes JS-style comments `//` (if parser supports it, standard Node `eval` may strip them if they are line comments outside of strings).
* **Hex/Octal Numbers**: `0xFF` -> `255`

## Safety

* **Backup**: Always creates a `.bak` file before overwriting (unless `--no-backup` is used, but default is safe).
* **Validation**: Verifies the repaired content is valid JSON before writing.
* **Eval Sandbox**: Uses `vm.runInNewContext` to parse, ensuring no access to global scope or process. It is safer than `/* REMOVED: eval */ ()`.

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

- Repair malformed JSON files by normalizing them through Node
- js evaluation
- Use this to fix trail
- 触发关键词: files, malformed, kit, normalizing, json, repair

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

### Q1: 如何开始使用Json Repair Kit？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Json Repair Kit有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制

Json Repair Kit技能在处理畸形JSON文件时存在一些边界条件和限制，以下是一些需要注意的方面：

- **文件大小限制**：由于Node.js的`eval`函数和`vm.runInNewContext`的使用，处理非常大的JSON文件可能会导致性能问题或内存溢出。建议文件大小不超过100MB。
- **复杂度限制**：对于包含大量嵌套或复杂结构的JSON文件，技能可能无法完全修复所有问题，尤其是当这些问题超出了JavaScript对象字面量的语法限制时。
- **兼容性限制**：Json Repair Kit依赖于Node.js的`eval`函数，因此可能不支持所有JavaScript语法和特性。此外，某些特定的JSON格式（如使用JavaScript特定的日期格式）可能无法正确修复。
- **输入文件类型限制**：技能仅支持JSON文件，不支持其他文件类型，如XML、CSV等。
- **输出文件格式限制**：技能输出文件格式固定为JSON，不支持其他格式如YAML、XML等。
- **网络依赖限制**：技能在处理过程中不涉及网络请求，因此不受网络连接稳定性影响。
- **安全性限制**：虽然技能使用`vm.runInNewContext`来限制代码执行环境，但仍然存在一定安全风险，特别是在处理不受信任的输入文件时。

---

