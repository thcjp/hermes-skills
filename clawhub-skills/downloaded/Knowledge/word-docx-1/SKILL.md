---
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
summary: "处理Word/docx,修订/批注/页眉/编号/表格/模板"
---
# Word Docx 1

## When to Use

Use when the main artifact is a Microsoft Word document or `.docx` file, especially when tracked changes, comments, headers, numbering, fields, tables, templates, or compatibility matter.

## Core Rules

### 1. Treat DOCX as OOXML, not plain text

* A `.docx` file is a ZIP of XML parts, so structure matters as much as visible text.
* The critical parts are usually `word/document.xml`, `styles.xml`, `numbering.xml`, headers, footers, and relationship files.
* Text may be split across multiple runs; never assume one word or sentence lives in one XML node.
* Use different workflows on purpose: structured extraction for quick reading, style-driven generation for new files, and OOXML-aware editing for fragile existing documents.
* If the job is mainly reading, extracting, or reviewing, prefer a structure-preserving read path before touching OOXML.
* For deep edits, inspect the package layout instead of relying only on rendered output.
* Reading, generating, and preserving an existing reviewed document are different jobs even when the format is the same.
* Legacy `.doc` inputs usually need conversion before you can trust modern `.docx` assumptions.

### 2. Preserve styles and direct formatting deliberately

* Prefer named styles over direct formatting so the document stays editable.
* Styles layer: paragraph styles, character styles, and direct formatting do not behave the same.
* Removing direct formatting is often safer than stacking more inline formatting on top.
* When editing an existing file, extend the current style system instead of inventing a parallel one.
* Copying content between documents can silently import foreign styles, theme settings, and numbering definitions.

### 3. Lists and numbering are their own system

* Bullets and numbering belong to Word's numbering definitions, not pasted Unicode characters.
* `abstractNum`, `num`, and paragraph numbering properties all matter, so restart behavior is rarely "visual only".
* Indentation and numbering are related but not identical; a list can have broken numbering even if the indent looks right.
* A list that looks correct in one editor can restart, flatten, or renumber itself later if the underlying numbering state is wrong.

### 4. Page layout lives in sections

* Margins, orientation, headers, footers, and page numbering are section-level behavior.
* First-page and odd/even headers can differ inside the same document, so one header fix may not fix the document.
* Set page size explicitly because A4 and US Letter defaults change pagination and table widths.
* Use section breaks for layout changes; manual spacing and stray page breaks usually create drift.
* Header and footer media use part-specific relationships, so copied IDs often break images or links.
* Tables, page breaks, and headers often drift together, so treat layout fixes as document-wide, not local cosmetic edits.
* Table geometry depends on page width, margins, and fixed widths, so "close enough" table edits often break later in Google Docs or LibreOffice.

### 5. Track changes, comments, and fields need precise edits

* Visible text is not the full document when tracked changes are enabled.
* Insertions, deletions, and comments carry metadata that can survive careless edits.
* Deleted text may still exist in the XML even when it no longer appears on screen.
* Comment anchors and review ranges can break if edits move text without preserving the surrounding structure.
* Comment markers and review wrappers do not behave like inline formatting, so moving text carelessly can orphan or misplace them.
* Comments, footnotes, bookmarks, and linked media may live in separate parts, not only in the main document body.
* Tables of contents, page numbers, dates, cross-references, and mail merge placeholders are fields.
* Edit the field source carefully and expect cached display values to lag until refresh.
* Hyperlinks, bookmarks, and references can break if IDs or relationships stop matching.
* Bookmarks, footnotes, comment ranges, and cross-references depend on stable anchors even when the visible text seems untouched.
* A document can look correct while still containing stale field output that refreshes later into something different.
* For review workflows, make minimal replacements instead of rewriting whole paragraphs.
* In tracked-change workflows, only the changed span should look changed; broad rewrites create noisy reviews and can destroy the original formatting context.
* For legal, academic, or business review documents, default to review-style edits over wholesale paragraph rewrites unless the user explicitly wants a rewrite.

### 6. Verify round-trip compatibility before delivery

* Complex documents can shift between Word, LibreOffice, Google Docs, and conversion tools.
* Tables, headers, embedded fonts, and copied styles are common sources of layout drift.
* Treat `.docm` as macro-bearing and higher risk; treat `.doc` as legacy input that may need conversion first.
* When layout matters, explicit table widths are safer than auto-fit or percentage-style behavior that different editors reinterpret.
* A document that passes a text check can still fail on pagination, table widths, or reference refresh after the recipient opens it.

## Common Traps

* Copy-paste can import unwanted styles and numbering definitions.
* Header or footer images use part-specific relationships, so reusing IDs blindly breaks them.
* Empty paragraphs used as spacing make templates fragile; spacing belongs in paragraph settings.
* A clean-looking export can still hide unresolved revisions, comments, or stale field values.
* Restarting lists "by eye" usually fails because numbering state lives outside the paragraph text.
* One visible phrase can be split across several runs, bookmarks, revision tags, or field boundaries.
* Replacing a whole paragraph to change one clause often breaks review quality, bookmarks, comments, or nearby inline formatting.
* Deleting all visible text from a paragraph or list item can still leave behind an empty paragraph mark, empty bullet, or unstable numbering.
* Table auto-fit and percentage-like width behavior can look acceptable in Word and still drift in Google Docs or LibreOffice.
* LibreOffice and Google Docs can shift complex tables, section behavior, and embedded fonts even when Word looks perfect.
* Compatibility mode can silently cap newer features or change pagination behavior.
* A single change in page size or margin defaults can ripple through tables, headers, TOC, and cross-references.
* A revision workflow can look accepted on screen while leftover metadata, comments, or field caches still make the file unstable later.
* TOC entries, footnotes, and cross-references can look correct until the recipient updates fields and exposes broken anchors.

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `documents` — General document handling and format conversion.
* `brief` — Concise business writing and structured summaries.
* `article` — Long-form drafting and editorial structure.

## Feedback

* If useful: `
* Stay updated: `

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

- Create, inspect, and edit Microsoft Word documents and DOCX files with
  reliable styles, numbering
- 触发关键词: edit, create, microsoft, inspect, docx, word

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

### Q1: 如何开始使用Word Docx 1？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Word Docx 1有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
