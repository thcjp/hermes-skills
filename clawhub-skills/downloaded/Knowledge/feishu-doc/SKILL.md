---
slug: feishu-doc
name: feishu-doc
version: "1.2.7"
displayName: Feishu Doc
summary: Fetch content from Feishu (Lark) Wiki, Docs, Sheets, and Bitable. Automatically
  resolves Wiki URL...
license: MIT
description: |-
  Fetch content from Feishu (Lark) Wiki, Docs, Sheets, and Bitable. Automatically
  resolves Wiki URL...

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: content, feishu, doc, lark, fetch
tags:
- Knowledge
tools:
- read
- exec
---

# Feishu Doc

Fetch content from Feishu (Lark) Wiki, Docs, Sheets, and Bitable. Write and update documents.

## Prerequisites

* Install `feishu-common` first.
* This skill depends on `../feishu-common/index.js` for token and API auth.

## Capabilities

* **Read**: Fetch content from Docs, Sheets, Bitable, and Wiki.
* **Create**: Create new blank documents.
* **Write**: Overwrite document content with Markdown.
* **Append**: Append Markdown content to the end of a document.
* **Blocks**: List, get, update, and delete specific blocks.

## Long Document Handling (Unlimited Length)

To generate long documents (exceeding LLM output limits of ~2000-4000 tokens):

1. **Create** the document first to get a `doc_token`.
2. **Chunk** the content into logical sections (e.g., Introduction, Chapter 1, Chapter 2).
3. **Append** each chunk sequentially using `feishu_doc_append`.
4. Do NOT try to write the entire document in one `feishu_doc_write` call if it is very long; use the append loop pattern.

## Usage

```bash
node index.js --action read --token <doc_token>

node index.js --action create --title "My Doc"

node index.js --action write --token <doc_token> --content "# Title\nHello world"

node index.js --action append --token <doc_token> --content "## Section 2\nMore text"
```

## Configuration

Create a `config.json` file in the root of the skill or set environment variables:

```json
{
  "app_id": "YOUR_APP_ID",
  "app_secret": "YOUR_APP_SECRET"
}
```

Environment variables:

* `FEISHU_APP_ID`
* `FEISHU_APP_SECRET`

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
