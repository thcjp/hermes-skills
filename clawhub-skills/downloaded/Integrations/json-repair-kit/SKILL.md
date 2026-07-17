---
slug: json-repair-kit
name: json-repair-kit
version: "1.0.0"
displayName: Json Repair Kit
summary: Repair malformed JSON files by normalizing them through Node.js evaluation.
  Use this to fix trail...
license: MIT
description: |-
  Repair malformed JSON files by normalizing them through Node.js evaluation.
  Use this to fix trail...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: files, malformed, kit, normalizing, json, repair
tags:
- Integrations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
