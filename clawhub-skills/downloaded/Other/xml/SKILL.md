---
slug: xml
name: xml
version: "1.0.0"
displayName: XML
summary: Parse, generate, and transform XML with correct namespace handling and encoding.
license: MIT
description: |-
  Parse, generate, and transform XML with correct namespace handling and
  encoding.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generate, correct, parse, transform, xml
tags:
- Other
tools:
- read
- exec
---

# XML

## Namespaces

* XPath `/root/child` fails if document has default namespace—use `//*[local-name()='child']` or register prefix
* Default namespace (`xmlns="..."`) applies to elements, not attributes—attributes need explicit prefix
* Namespace prefix is arbitrary—`<foo:element>` and `<bar:element>` are identical if both prefixes map to same URI
* Child elements don't inherit parent's prefixed namespace—each must declare or use prefix explicitly

## Encoding

* `<?xml version="1.0" encoding="UTF-8"?>` must match actual file encoding—mismatch corrupts non-ASCII
* Encoding declaration must be first thing in file—no whitespace or BOM before it (except UTF-8 BOM allowed)
* Default encoding is UTF-8 if declaration omitted—but explicit is safer across parsers

## Escaping & CDATA

* Five entities always escape in text: `&amp;` `&lt;` `&gt;` `&quot;` `&apos;`
* CDATA sections `<![CDATA[...]]>` for blocks with many special chars—but `]]>` inside CDATA breaks it
* Attribute values: use `&quot;` if delimited by `"`, or `&apos;` if delimited by `'`
* Numeric entities `&#60;` and `&#x3C;` work everywhere—useful for edge cases

## Whitespace

* Whitespace between elements is preserved by default—pretty-printing adds nodes that may break processing
* `xml:space="preserve"` attribute signals whitespace significance—but not all parsers respect it
* Normalize-space in XPath: `normalize-space(text())` trims and collapses internal whitespace

## XPath Pitfalls

* `//element` is expensive—traverses entire document; use specific paths when structure is known
* Position is 1-indexed: `[1]` is first, not `[0]`
* `text()` returns direct text children only—use `string()` or `.` for concatenated descendant text
* Boolean in predicates: `[@attr]` tests existence, `[@attr='']` tests empty value—different results

## Structure

* Self-closing `<tag/>` and empty `<tag></tag>` are semantically identical—but some legacy systems choke on self-closing
* Comments cannot contain `--`—will break parser even inside string content
* Processing instructions `<?target data?>` cannot have `?>` in data
* Root element required—document with only comments/PIs and no element is invalid

## Validation

* Well-formed ≠ valid—parser may accept structure but fail against schema
* DTD validates but can't express complex constraints—prefer XSD or RelaxNG for new projects
* XSD namespace `xmlns:xs="http://www.w3.org/2001/XMLSchema"` commonly confused with instance namespace

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
