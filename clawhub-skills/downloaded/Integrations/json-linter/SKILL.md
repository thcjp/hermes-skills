---
slug: json-linter
name: json-linter
version: "1.0.0"
displayName: Json Linter
summary: Validates JSON syntax across the workspace. Use this skill to check for syntax
  errors in configur...
license: MIT
description: |-
  Validates JSON syntax across the workspace. Use this skill to check
  for syntax errors in configur...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: linter, syntax, json, across, workspace, validates
tags:
- Integrations
tools:
- read
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

## Example Output

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
