---
slug: text
name: text
version: "1.0.0"
displayName: Text
summary: Transform, format, and process text with patterns for writing, data cleaning,
  localization, citat...
license: MIT
description: |-
  Transform, format, and process text with patterns for writing, data
  cleaning, localization, citat。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Text

## Quick Reference

| Task | Load |
| --- | --- |
| Creative writing (voice, dialogue, POV) | `writing.md` |
| Data processing (CSV, regex, encoding) | `data.md` |
| Academic/citations (APA, MLA, Chicago) | `academic.md` |
| Marketing copy (headlines, CTA, email) | `copy.md` |
| Translation/localization | `localization.md` |

---

## Universal Text Rules

### Encoding

* **Always verify encoding first:** `file -bi document.txt`
* **Normalize line endings:** `tr -d '\r'`
* **Remove BOM if present:** `sed -i '1s/^\xEF\xBB\xBF//'`

### Whitespace

* **Collapse multiple spaces:** `sed 's/[[:space:]]\+/ /g'`
* **Trim leading/trailing:** `sed 's/^[[:space:]]*//;s/[[:space:]]*$//'`

### Common Traps

* **Smart quotes** (`"` `"`) break parsers → normalize to `"`
* **Em/en dashes** (`–` `—`) break ASCII → normalize to `-`
* **Zero-width chars** invisible but break comparisons → strip them
* **String length ≠ byte length** in UTF-8 (`"café"` = 4 chars, 5 bytes)

---

## Format Detection

```bash
file -I document.txt

cat -A document.txt | head -1

head -1 file | tr -cd ',;\t|' | wc -c
```

---

## Quick Transformations

| Task | Command |
| --- | --- |
| Lowercase | `tr '[:upper:]' '[:lower:]'` |
| Remove punctuation | `tr -d '[:punct:]'` |
| Count words | `wc -w` |
| Count unique lines | `sort -u | wc -l` |
| Find duplicates | `sort | uniq -d` |
| Extract emails | `grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'` |
| Extract URLs | `grep -oE 'https?://[^[:space:]<>"{} |

---

## Before Processing Checklist

* Encoding verified (UTF-8?)
* Line endings normalized
* Delimiter identified (for structured text)
* Target format/style defined
* Edge cases considered (empty, Unicode, special chars)

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

- Transform, format, and process text with patterns for writing, data
  cleaning, localization, citat
- 触发关键词: format, text, process, transform

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

### Q1: 如何开始使用Text？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Text有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步
