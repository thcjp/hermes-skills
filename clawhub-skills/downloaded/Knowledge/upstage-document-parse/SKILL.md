---
slug: upstage-document-parse
name: upstage-document-parse
version: "1.0.5"
displayName: Upstage Document Parse
summary: Parse documents (PDF, images, DOCX, PPTX, XLSX, HWP) into layout-aware markdown/HTML
  with tables,...
license: MIT-0
description: |-
  Parse documents (PDF, images, DOCX, PPTX, XLSX, HWP) into layout-aware
  markdown/HTML with tables,...

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: upstage, images, document, parse, docx, documents, pptx
tags:
- Knowledge
tools:
- read
- exec
---

# Upstage Document Parse

Convert documents into structured HTML/Markdown. Recognizes layout elements such as tables, images, equations, and charts with bounding box coordinates.

## Quick Start

```python
import os
import requests

with open("report.pdf", "rb") as f:
    response = requests.post(
        "https://api.upstage.ai/v1/document-digitization",
        headers={"Authorization": f"Bearer {os.environ['UPSTAGE_API_KEY']}"},
        files={"document": f},
        data={"model": "document-parse", "output_formats": "['markdown']"}
    )
print(response.json()["content"]["markdown"])
```

**API Key**: Always use `os.environ["UPSTAGE_API_KEY"]`. Get your key at [console.upstage.ai](https://console.upstage.ai).

## Supported Formats

JPEG, PNG, BMP, PDF (up to 1000 pages with async), TIFF, HEIC, DOCX, PPTX, XLSX, HWP, HWPX

## Sync vs Async

| Mode | Endpoint | Max pages | Max file size | Notes |
| --- | --- | --- | --- | --- |
| **Sync** | `/v1/document-digitization` | 100 | 50 MB | Result returned in response (5 min server timeout). Best for ≤ 100 pages and quick turnaround. |
| **Async** | `/v1/document-digitization/async` | 1000 | 50 MB | Returns `request_id`; processed in 10-page batches. Use when document exceeds sync limits or sync would time out. |

Decision rule:

* ≤ 100 pages **and** expected to finish within 5 min → sync.
* 100 pages, scanned/complex content, or batch jobs → async.

For async submit/poll workflow, see `references/async-workflow.md`.

## Key Parameters (Sync)

| Parameter | Default | Common Values |
| --- | --- | --- |
| `model` | required | `document-parse` |
| `output_formats` | `['html']` | `['markdown']`, `['html', 'markdown']` |
| `mode` | `standard` | `enhanced` (complex tables), `auto` |
| `ocr` | `auto` | `force` (always OCR scanned PDFs) |
| `coordinates` | `true` | `false` to omit bounding boxes |

For full parameter reference and curl variations (enhanced mode, force OCR, base64 table images, LangChain integration), see `references/sync-options.md`.

## Response Structure

```json
{
  "api": "2.0",
  "model": "document-parse-251217",
  "content": {
    "html": "<h1>...</h1>",
    "markdown": "# ...",
    "text": "..."
  },
  "elements": [
    {
      "id": 0,
      "category": "heading1",
      "content": { "html": "...", "markdown": "...", "text": "..." },
      "page": 1,
      "coordinates": [{"x": 0.06, "y": 0.05}, ...]
    }
  ],
  "usage": { "pages": 1 }
}
```

### Element Categories

`paragraph`, `heading1`, `heading2`, `heading3`, `list`, `table`, `figure`, `chart`, `equation`, `caption`, `header`, `footer`, `index`, `footnote`

## Output Files

* **Default**: write to `<system-temp>/<input-stem>.parsed.<ext>` where `<ext>` matches `output_formats` (`md` or `html`). Example: `/tmp/report.parsed.md`. Use `tempfile.gettempdir()` for cross-platform code.
* **Override**: if the user specifies an output path, use it.
* **Always print the resolved absolute path** in your response so the user can locate the file.

## Tips

* Use `mode=enhanced` for complex tables, charts, images
* Use `mode=auto` to let API decide per page
* Use async API for documents > 100 pages, > 50 MB, or when sync would exceed the 5-min timeout (async caps at 1000 pages)
* Use `ocr=force` for scanned PDFs or images
* `merge_multipage_tables=true` combines split tables (max 20 pages with enhanced mode)
* Standard documents process in ~3 seconds; sync API timeout is 5 minutes

## Detailed References

| File | Content |
| --- | --- |
| `references/sync-options.md` | Full sync parameter reference, mode selection, curl variations, LangChain |
| `references/async-workflow.md` | Async submit/poll/status, Python polling pattern, retention rules |

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
