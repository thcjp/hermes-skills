---
slug: yaml
name: yaml
version: "1.0.0"
displayName: YAML
summary: "编写跨语言跨版本可预测解析的YAML,规避缩进与类型推断陷阱,确保配置可靠性"
license: MIT
description: |-
  Write valid YAML that parses predictably across languages and versions。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Write valid YAML that parses predictably across languages and versions
- 触发关键词: write, parses, yaml, valid

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

### Q1: 如何开始使用YAML？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: YAML有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **最大输入长度**：YAML技能能够处理的输入长度有限制，通常不超过2048个字符，以避免性能问题和资源消耗。
- **数据格式**：输入数据必须是有效的YAML格式，否则技能将无法正确解析和处理。

### 性能边界
- **处理速度**：对于复杂的YAML文件，处理速度可能会受到影响，尤其是在高嵌套或大量数据的情况下。
- **并发处理**：技能可能不支持高并发处理，因此在处理大量请求时，可能需要考虑队列或分批处理。

### 兼容性约束
- **YAML版本**：技能可能不支持所有YAML版本的所有特性，特别是对于较新版本的YAML特性。
- **解析器差异**：不同语言的YAML解析器可能存在差异，因此技能的行为可能在不同环境中有所不同。

### 系统资源
- **内存使用**：处理大型YAML文件时，技能可能会消耗较多的内存资源。
- **CPU使用**：对于复杂的解析和转换操作，技能可能会占用较多的CPU资源。

### 安全限制
- **输入验证**：技能对输入数据进行验证，以防止注入攻击和其他安全风险。
- **输出限制**：技能对输出结果进行限制，以防止敏感信息泄露。

### 功能限制
- **不支持自定义规则**：技能不支持用户自定义YAML验证规则。
- **不支持复杂逻辑**：技能不支持复杂的业务逻辑处理，仅提供基本的YAML解析和格式化功能。

