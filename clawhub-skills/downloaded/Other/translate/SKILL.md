---
slug: translate
name: translate
version: "1.0.0"
displayName: Translate
summary: Translate text accurately — preserve formatting, handle plurals, and adapt
  tone per locale.
license: MIT
description: |-
  Translate text accurately — preserve formatting, handle plurals, and
  adapt tone per locale.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: text, accurately, formatting, translate, preserve
tags:
- Other
tools:
- read
- exec
---

# Translate

Master accurate translation that preserves meaning, formatting, and cultural context.

## Formatting Preservation

* Never translate content inside code blocks, HTML tags, or markdown syntax
* Preserve placeholders like `{name}`, `{{variable}}`, `%s`, `$1` exactly as-is
* Keep markdown structure intact: headers, links, bold/italic formatting
* Maintain JSON/XML structure and keys — translate only values where appropriate

## Content Rules

* Don't translate: proper nouns, brand names, technical terms, URLs, email addresses
* Don't translate: code snippets, CSS classes, API endpoints, file extensions
* Preserve numbers, dates, and IDs in their original format unless locale conversion needed
* Keep consistent terminology throughout — create a glossary for repeated terms

## Language-Specific Handling

* **Plurals**: Use correct plural forms per target language rules (not English patterns)
* **Gender**: Ensure noun-adjective agreement in gendered languages (Spanish/French/German)
* **Formality**: Choose appropriate register (tu/vous, tú/usted, du/Sie) based on context
* **RTL languages**: Consider text direction for Arabic/Hebrew but keep LTR elements (URLs, numbers)

## Cultural Adaptation

* Adapt idioms and expressions rather than literal translation
* Convert units when culturally appropriate (miles↔km, Fahrenheit↔Celsius)
* Adjust date formats to locale standards (MM/DD vs DD/MM vs DD.MM)
* Use local currency symbols and number formatting (, vs . for decimals)

## Context Awareness

* Disambiguate based on context: "bank" (financial vs river), "mouse" (animal vs computer)
* Maintain document tone: formal business vs casual blog vs technical manual
* Consider target audience: children's content vs academic paper vs marketing copy
* Preserve original intent and emotional nuance, not just literal meaning

## Quality Control

* Read full context before translating to understand meaning
* Check that translated text flows naturally in target language
* Verify all formatting elements remain functional after translation
* Ensure consistent voice and terminology across the entire document

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
