---
slug: markdown
name: markdown
version: "1.0.1"
displayName: Markdown
summary: "生成干净可移植的Markdown,确保跨解析器正确渲染,解决文档格式兼容性问题"
license: MIT
description: |-
  Generate clean, portable Markdown that renders correctly across parsers。核心能力:

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
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# Markdown

## Whitespace Traps

* Blank line required before lists, code blocks, and blockquotes—without it, many parsers continue the previous paragraph
* Nested lists need 4 spaces (not 2) for GitHub/CommonMark; 2 spaces breaks nesting in strict parsers
* Two trailing spaces for `<br>` break—invisible and often stripped by editors; prefer blank line or `<br>` tag
* Lines with only spaces still break paragraphs—trim trailing whitespace

## Links & Images

* Parentheses in URLs break `[text](url)`—use `%28` `%29` or angle brackets: `[text](<url with (parens)>)`
* Spaces in URLs need `%20` or angle bracket syntax
* Reference-style links `[text][ref]` fail silently if `[ref]: url` is missing—verify all refs exist
* Images without alt text: always provide `![alt](url)` even if empty `![]()` for accessibility tools

## Code

* Triple backticks inside fenced blocks—use 4+ backticks for outer fence or indent method
* Inline backticks containing backtick—wrap with double backticks and pad: ``` `` `code` `` ```
* Language hint after fence affects syntax highlighting—omit only when truly plain text

## Tables

* Alignment colons go in separator row: `:---` left, `:---:` center, `---:` right
* Pipe `|` in cell content needs backslash escape: `\|`
* No blank line before table—some parsers fail
* Empty cells need at least one space or break rendering

## Escaping

* Characters needing escape in text: `*`, `_`, `[`, `]`, `\#`, `\>`, ``` \``, ``` \`
* Escape not needed inside code spans/blocks
* Ampersand only needs escape as `&amp;` when it could form an HTML entity

## Portability

* HTML tags work in GitHub but stripped in many renderers—prefer pure Markdown
* Extended syntax (footnotes, task lists, emoji shortcodes) not universal—check target parser
* YAML frontmatter needs `---` fences and only at file start; some parsers render it as text

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

- Generate clean, portable Markdown that renders correctly across parsers
- 触发关键词: portable, markdown, generate, clean

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

### Q1: 如何开始使用Markdown？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Markdown有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

Markdown技能的边界条件与限制主要包括以下几个方面：

- **输入长度限制**：由于性能和资源限制，输入内容长度可能存在上限，超过该长度的输入可能导致技能无法正确处理或响应。
- **复杂格式支持限制**：虽然Markdown技能旨在生成干净可移植的Markdown，但对于一些复杂的Markdown扩展语法（如脚注、任务列表、表情符号等），技能可能不完全支持或支持有限。
- **跨平台兼容性限制**：虽然技能设计时考虑了跨解析器的兼容性，但在某些特定平台上，解析器可能存在差异，导致Markdown渲染结果不一致。
- **性能限制**：技能的性能可能受到底层模型能力的影响，对于大量或复杂的内容生成，可能需要较长时间。
- **外部API依赖限制**：技能可能依赖于外部API，如LLM API，如果外部API不可用或响应超时，技能可能无法正常工作。
- **安全限制**：技能在处理用户输入时，可能对某些风险代码进行移除，但这可能导致一些合法的Markdown格式无法被正确生成。

---

