---
slug: feishu-doc-write
name: feishu-doc-write
version: "1.0.0"
displayName: feishu-doc-write
summary: Feishu (Lark) Document API writing spec. Converts Markdown content to Feishu
  Block structures and...
license: MIT
description: |-
  Feishu (Lark) Document API writing spec。Converts Markdown content to
  Feishu Block structures and。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# feishu-doc-write

Reference spec for writing content to Feishu (Lark) cloud documents via the Docx API. Feishu docs use a **Block tree model** — raw Markdown is not accepted.

```text
Document (block_type=1, Page)
  +-- Heading1 Block (block_type=3)
  +-- Text Block (block_type=2)
  +-- Callout Block (block_type=19)
  |     +-- Text Block
  |     +-- Bullet Block
  +-- Image Block (block_type=27)
  +-- Divider Block (block_type=22)
```

## Preferred Approach: Convert API

Feishu provides an official **Markdown -> Blocks** conversion endpoint:

```text
POST /open-apis/docx/v1/documents/{document_id}/convert
```

```json
{
  "content": "# Title\n\nBody text\n\n- Item 1\n- Item 2\n\n> Quote",
  "content_type": "markdown"
}
```

**Pros**: No manual Block JSON construction. Handles most standard Markdown.
**Limitation**: Does not support Feishu-specific blocks (Callout, etc.) — use manual Block creation for those.

## Block Type Reference

| block_type | Name | JSON Key | Notes |
| --- | --- | --- | --- |
| 1 | Page | `page` | Document root |
| 2 | Text | `text` | Paragraph |
| 3-11 | Heading1-9 | `heading1`-`heading9` | Headings |
| 12 | Bullet | `bullet` | Unordered list (each item = separate block) |
| 13 | Ordered | `ordered` | Ordered list |
| 14 | Code | `code` | Code block (with `style.language` enum) |
| 15 | Quote | `quote` | Blockquote |
| 17 | Todo | `todo` | Checkbox item (with `style.done`) |
| 19 | Callout | `callout` | Highlight box (Feishu-specific, container block) |
| 22 | Divider | `divider` | Horizontal rule |
| 27 | Image | `image` | Two-step: create placeholder, then upload |
| 31 | Table | `table` | Table |
| 34 | QuoteContainer | `quote_container` | Quote container |

## Create Blocks API

```text
POST /open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children?document_revision_id=-1

Headers:
  Content-Type: application/json
  Authorization: Bearer <tenant_access_token>

Body:
{
  "children": [ ...Block array... ],
  "index": 0
}
```

* `block_id`: Parent block ID (usually `document_id` itself for root)
* `index`: Insert position (0 = beginning, -1 or omit = end)

## 示例

### Text

```json
{
  "block_type": 2,
  "text": {
    "elements": [{
      "text_run": {
        "content": "Paragraph text here",
        "text_element_style": { "bold": false, "italic": false }
      }
    }]
  }
}
```

### Heading

```json
{ "block_type": 3, "heading1": { "elements": [{ "text_run": { "content": "H1 Title" } }] } }
{ "block_type": 4, "heading2": { "elements": [{ "text_run": { "content": "H2 Title" } }] } }
```

### Bullet / Ordered List

```json
{ "block_type": 12, "bullet": { "elements": [{ "text_run": { "content": "List item" } }] } }
{ "block_type": 13, "ordered": { "elements": [{ "text_run": { "content": "Numbered item" } }] } }
```

Each list item is a **separate Block**.

### Code Block

```json
{
  "block_type": 14,
  "code": {
    "elements": [{ "text_run": { "content": "console.log('hello');" } }],
    "style": { "language": 23, "wrap": false }
  }
}
```

Common language enums: PlainText=1, JavaScript=23, Python=40, TypeScript=49, Go=20, Shell=46, SQL=47, Java=22, Rust=44, C=12, CSS=17, HTML=21, Docker=19.

### Callout (Feishu-specific highlight box)

Callout is a **container block** — create it first, then add child blocks inside.

```json
// Step 1: Create callout as document child
{ "block_type": 19, "callout": { "background_color": 3, "border_color": 3, "emoji_id": "star" } }

// Step 2: POST .../blocks/{callout_block_id}/children
{ "children": [{ "block_type": 2, "text": { "elements": [{ "text_run": { "content": "Highlight text" } }] } }] }
```

Color enums: Red=1, Orange=2, Yellow=3, Green=4, Blue=5, Purple=6, Grey=7.

### Divider

```json
{ "block_type": 22, "divider": {} }
```

### Image (two-step)

```text
Step 1: Create placeholder block { "block_type": 27, "image": {} }
Step 2: Upload via POST /open-apis/drive/v1/medias/upload_all
  - multipart/form-data: file, file_name, parent_type="docx_image", parent_node=<image_block_id>
```

## Text Styling

Apply styles via `text_element_style` in `text_run`:

| Property | Type | Effect |
| --- | --- | --- |
| `bold` | bool | Bold |
| `italic` | bool | Italic |
| `strikethrough` | bool | Strikethrough |
| `underline` | bool | Underline |
| `inline_code` | bool | Inline code |
| `text_color` | int | Text color (same enum as callout colors) |
| `background_color` | int | Background color |
| `link.url` | string | Hyperlink |

Multiple `text_run` elements in one block = mixed styles in one paragraph.

## Markdown to Block Mapping

| Markdown | block_type | JSON Key |
| --- | --- | --- |
| `# H1` | 3 | `heading1` |
| `## H2` | 4 | `heading2` |
| `### H3` | 5 | `heading3` |
| Paragraph | 2 | `text` |
| `- item` | 12 | `bullet` |
| `1. item` | 13 | `ordered` |
| Code fence | 14 | `code` |
| `> quote` | 15 | `quote` |
| `- [ ] todo` | 17 | `todo` |
| `---` | 22 | `divider` |
| `![](url)` | 27 | `image` (two-step) |
| `**bold**` | -- | `text_element_style.bold: true` |
| `*italic*` | -- | `text_element_style.italic: true` |
| `` `code` `` | -- | `text_element_style.inline_code: true` |
| `~~strike~~` | -- | `text_element_style.strikethrough: true` |
| `[text](url)` | -- | `text_element_style.link.url` |
| (no MD equivalent) | 19 | `callout` (Feishu-specific) |

## Concurrency & Ordering (Critical)

**Problem**: Concurrent Block creation API calls produce random ordering.

### Solution A: Single Batch Request (Recommended)

Put all blocks in one `children` array, single API call:

```json
{
  "children": [
    { "block_type": 3, "heading1": { "elements": [{"text_run": {"content": "Title"}}] } },
    { "block_type": 2, "text": { "elements": [{"text_run": {"content": "Paragraph 1"}}] } },
    { "block_type": 22, "divider": {} },
    { "block_type": 4, "heading2": { "elements": [{"text_run": {"content": "Section 2"}}] } }
  ],
  "index": 0
}
```

### Solution B: Serial Writes with Index

For long content requiring multiple requests, execute **serially** with explicit `index`:

```text
Request 1: index=0, write block A
Request 2: index=1, write block B (wait for A to succeed)
Request 3: index=2, write block C (wait for B to succeed)
```

### Solution C: Collect-Then-Write (Recommended)

```text
LLM outputs complete Markdown -> Conversion layer -> Single API batch write
```

**Never** let the LLM write one paragraph at a time with concurrent API calls.

## Complete Write Flow

1. **Create document**: `POST /open-apis/docx/v1/documents` with `{ "folder_token": "<token>", "title": "Title" }` -> returns `document_id`
2. **Build Block array**: Convert full content to Block JSON
3. **Batch write**: `POST .../documents/{doc_id}/blocks/{doc_id}/children?document_revision_id=-1` with all blocks
4. **Container blocks** (optional): For Callout etc., get `block_id` from step 3 response, then add children

## Custom Callout Syntax

Since Markdown has no Callout equivalent, use this custom markup:

```markdown
:::callout{color=yellow emoji=bulb}
Highlight content here.
Supports **bold**, *italic*, and lists.
:::
```

| Param | Values | Default | Purpose |
| --- | --- | --- | --- |
| `color` | red, orange, yellow, green, blue, purple, grey | yellow | Background & border |
| `emoji` | Any Feishu emoji_id (bulb, star, warning, fire) | bulb | Left icon |
| `border` | Same as color values | Same as color | Border color (override) |

Common templates:

```markdown
:::callout{color=yellow emoji=bulb}
**Key Insight**: The most important takeaway
:::

:::callout{color=red emoji=warning}
**Warning**: Common misconception
:::

:::callout{color=green emoji=check}
**Action Item**: What to do next
:::
```

## Rate Limits & Constraints

* Max blocks per batch: ~50 recommended
* Long articles: Split by H2/H3 sections, 200-500ms between batches
* Always use `document_revision_id=-1` (latest version)
* Token validity: ~2 hours, cache and refresh before expiry

## Authentication

```bash
curl -X POST 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal' \
  -H 'Content-Type: application/json' \
  -d '{ "app_id": "<app_id>", "app_secret": "<app_secret>" }'
```

## Schema Pitfalls (Battle-tested)

* **No Markdown tables in write ops** — use bullet lists instead (prevents schema errors)
* **No nested code blocks inside lists** — Feishu schema validation is strict on nesting depth
* **Callout is a container** — always requires a two-step create (container first, then children)
* **Each list item = separate Block** — don't try to put multiple items in one block

## References

* Create Blocks API: <https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document-block-children/create>
* Block Data Structure: <https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/data-structure/block>
* Convert API: <https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/convert>
* Extended API reference: See `FEISHU_API_HANDBOOK.md` in workspace root

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

- Feishu (Lark) Document API writing spec
- Converts Markdown content to
  Feishu Block structures and
- 触发关键词: writing, feishu-doc-write, feishu, write, document, doc, spec, lark

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用feishu-doc-write？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: feishu-doc-write有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
