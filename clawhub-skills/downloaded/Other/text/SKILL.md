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
  cleaning, localization, citat...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: format, text, process, transform
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
