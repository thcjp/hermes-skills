---
slug: yaml
name: yaml
version: "1.0.0"
displayName: YAML
summary: Write valid YAML that parses predictably across languages and versions.
license: MIT
description: |-
  Write valid YAML that parses predictably across languages and versions.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: write, parses, yaml, valid
tags:
- Other
tools:
- read
- exec
---

# YAML

## Type Coercion Traps

* `yes`, `no`, `on`, `off`, `true`, `false` → boolean; quote if literal string: `"yes"`
* `NO` (Norway country code) → false in YAML 1.1; always quote country codes
* `1.0` → float, `1` → int; quote version numbers: `"1.0"`
* `010` → octal (8) in YAML 1.1; quote or use `0o10` explicitly
* `null`, `~`, empty value → null; quote if literal: `"null"`, `"~"`
* `.inf`, `-.inf`, `.nan` → special floats; quote if literal strings

## Indentation

* Spaces only—tabs are forbidden and cause parse errors
* Consistent indent width required within document—2 spaces conventional
* Sequence items `-` count as indentation—nested content aligns after the space

## Strings

* Colon followed by space `:`  triggers key-value—quote strings containing `:`
* `#` starts comment unless quoted—quote strings with `#`
* Leading/trailing spaces stripped from unquoted strings—quote to preserve
* Quote strings starting with `@`, `` ` ``, `*`, `&`, `!`, `|`, `>`, `{`, `[`, `%`

## Multiline Strings

* `|` literal block preserves newlines; `>` folded block joins lines with spaces
* Trailing newline: `|-` and `>-` strip final newline; `|+` and `>+` keep trailing blank lines
* Indentation of first content line sets the block indent—be consistent

## Structure

* Duplicate keys: YAML spec says last wins, but some parsers error—avoid duplicates
* Anchors `&name` and aliases `*name` reduce repetition—but aliases can't override anchor values
* Document separator `---` starts new document; `...` ends document—useful in streams
* Empty documents between `---` markers are valid but often unintended

## Comments

* `#` only valid at line start or after whitespace—`key:value#comment` has no comment
* No inline comments after multiline block scalars—comment applies to next line
* No multi-line comment syntax—each line needs `#`

## Compatibility

* YAML 1.1 vs 1.2: boolean words (`yes`/`no`), octal syntax differ—know which version parser uses
* JSON is valid YAML 1.2—but YAML features (anchors, multiline) don't round-trip to JSON
* Some parsers limit nesting depth or file size—test with expected data scale

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
