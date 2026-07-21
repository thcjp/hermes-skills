---
slug: feishu-doc
name: feishu-doc
version: "1.2.7"
displayName: Feishu Doc
summary: Fetch content from Feishu (Lark) Wiki, Docs, Sheets, and Bitable. Automatically
  resolves Wiki URL...
license: MIT
description: |-
  Fetch content from Feishu (Lark) Wiki, Docs, Sheets, and Bitable。Automatically
  resolves Wiki URL。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
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

- Fetch content from Feishu (Lark) Wiki, Docs, Sheets, and Bitable
- Automatically
  resolves Wiki URL
- 触发关键词: content, feishu, doc, lark, fetch

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

### Q1: 如何开始使用Feishu Doc？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Feishu Doc有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
