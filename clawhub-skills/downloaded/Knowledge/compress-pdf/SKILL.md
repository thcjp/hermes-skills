---
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
summary: "压缩PDF文件大小,保持质量的同时减少存储与传输成本"
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

- Compress a user-provided PDF by uploading it to Cross-Service-Solutions,
  polling until completion
- 触发关键词: compress, cross, pdf, provided, uploading

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

```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Compress PDF？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Compress PDF有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **文件大小限制**：由于API限制，上传的PDF文件大小不应超过某个特定阈值（例如100MB）。超过此大小的文件将无法处理。
- **文件格式限制**：仅支持PDF格式文件。其他格式如Word、Excel等将无法压缩。

### 性能边界
- **处理速度**：压缩PDF文件的时间取决于文件大小和复杂度，通常情况下，中等大小的PDF文件压缩处理时间在几秒到几分钟之间。
- **并发处理**：同时处理的任务数量可能受到API服务端的限制，超过限制可能导致任务排队等待。

### 兼容性约束
- **操作系统兼容性**：该技能在Windows、macOS和Linux操作系统上均应能正常运行，但具体表现可能因操作系统版本和配置而异。
- **浏览器兼容性**：如果技能通过Web界面使用，需要确保在主流浏览器中表现一致。

### API限制
- **API调用频率**：避免在短时间内频繁调用API，以免触发频率限制。
- **API错误处理**：在处理API响应时，需要妥善处理错误响应，包括但不限于网络错误、API限制错误等。

### 资源限制
- **存储空间**：压缩后的文件可能会比原始文件小，但存储空间仍需足够以存储临时文件和处理结果。
- **计算资源**：处理大量或大型PDF文件时，可能需要更多的计算资源。

---

