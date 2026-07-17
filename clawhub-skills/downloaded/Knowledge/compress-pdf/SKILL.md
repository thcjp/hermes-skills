---
slug: compress-pdf
name: compress-pdf
version: "1.0.0"
displayName: Compress PDF
summary: Compress a user-provided PDF by uploading it to Cross-Service-Solutions,
  polling until completion...
license: MIT
description: |-
  Compress a user-provided PDF by uploading it to Cross-Service-Solutions,
  polling until completion...

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: compress, cross, pdf, provided, uploading
tags:
- Knowledge
tools:
- read
- exec
---

# Compress PDF

## Purpose

This skill compresses a PDF by:

1. accepting a PDF file from the user,
2. uploading it to the Cross-Service-Solutions compression API,
3. polling the job status until it is finished,
4. returning the compressed file download URL.

## Credentials

The API requires an API key used as a Bearer token:

* `Authorization: Bearer <API_KEY>`

How the user gets an API key:

* They can sign up and get their key at:
  <https://login.cross-service-solutions.com/register>
* Or they can provide an API key directly to the bot.

**Rule:** never echo or log the API key.

## API endpoints

Base URL:

* `https://api.xss-cross-service-solutions.com/solutions/solutions`

Create compression job:

* `POST /api/29`
* `multipart/form-data` parameters:
  + `file` (PDF Dokument) — required — PDF file
  + `imageQuality` — required — number 0..100 (default 75)
  + `dpi` — required — number 72..300 (default 144)

Get result by ID:

* `GET /api/<ID>`

When done, the response contains:

* `output.files[]` with `{ name, path }` where `path` is a downloadable URL.

## Inputs

### Required

* A PDF file (binary)
* An API key (string)

### Optional

* `imageQuality` (0..100), default 75
* `dpi` (72..300), default 144

## Output

Return a structured result:

* `job_id` (number)
* `status` (string)
* `download_url` (string, when done)
* `file_name` (string, when available)
* `settings` (object)

Example output:

```json
{
  "job_id": 123,
  "status": "done",
  "download_url": "https://.../compressed.pdf",
  "file_name": "compressed.pdf",
  "settings": { "imageQuality": 75, "dpi": 144 }
}
```

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
