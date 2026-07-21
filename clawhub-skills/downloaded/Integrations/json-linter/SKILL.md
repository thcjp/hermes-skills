---
slug: json-linter
name: json-linter
version: "1.0.0"
displayName: Json Linter
summary: Validates JSON syntax across the workspace. Use this skill to check for syntax
  errors in configur...
license: MIT
description: |-
  Validates JSON syntax across the workspace。Use this skill to check
  for syntax errors in configur。Use when 用户需要Json Linter相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
- Integrations
tools:
  - - read
- exec
---

# Json Linter

A simple utility to recursively scan the workspace for `.json` files and validate their syntax using `JSON.parse()`.

## Usage

```bash
node skills/json-linter/index.js

node skills/json-linter/index.js --dir path/to/dir
```

## Output

JSON report containing:

* `scanned_at`: Timestamp
* `total_files`: Number of `.json` files scanned
* `valid_files`: Number of valid files
* `invalid_files`: Number of invalid files
* `errors`: Array of error objects:
  + `path`: Relative path to file
  + `error`: Error message (e.g., "Unexpected token } in JSON at position 42")

## 示例

```json
{
  "scanned_at": "2026-02-14T21:45:00.000Z",
  "total_files": 150,
  "valid_files": 149,
  "invalid_files": 1,
  "errors": [
    {
      "path": "config/broken.json",
      "error": "Unexpected token } in JSON at position 42"
    }
  ]
}
```

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

- Validates JSON syntax across the workspace
- Use this skill to check
  for syntax errors in configur
- 触发关键词: linter, syntax, json, across, workspace, validates

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

### Q1: 如何开始使用Json Linter？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Json Linter有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
