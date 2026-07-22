---
slug: "upstage-document-parse-free"
name: "upstage-document-parse-free"
version: "1.0.5"
displayName: "Document Parse Free"
summary: "基础版文档解析技能，将 PDF 和图片转换为 Markdown，支持同步模式。"
license: "MIT-0"
description: |-
  upstage-document-parse-free 是文档解析技能的基础版本，将 PDF 和图片转换为 Markdown 格式。
  支持同步模式解析（最多 100 页/50MB）和基础版面元素识别。不包含异步模式、enhanced 模式、
  force OCR 和跨页表格合并。适合快速解析标准文档，升级完整版获取全量解析能力。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 文档处理
---
# Document Parse Free

document-parse-free 将文档转换为 Markdown 格式。基础版支持 PDF 和图片的同步模式解析，
识别基础版面元素（段落、标题、表格）。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 基础文档解析
支持 JPEG、PNG、BMP、PDF、TIFF 格式。通过 `model: "document-parse"` 调用解析模型，
将文档内容转换为 `content.markdown` 格式输出。基础版仅支持 Markdown 输出，
不支持 HTML 和 text 格式。标准文档处理时间约 3 秒。

### 2. 同步模式解析（Sync）
通过 `POST /v1/document-digitization` 端点进行同步解析。限制：最多 100 页、50 MB 文件大小、
5 分钟服务器超时。参数包括 `model`（必填，值为 `document-parse`）、
`output_formats`（固定为 `['markdown']`）、`mode`（固定为 `standard`）、
`ocr`（默认 `auto`）、`coordinates`（默认 `true`）。
基础版不支持 enhanced 模式和 force OCR。

### 3. 基础版面元素识别
解析结果包含 `elements` 数组，每个元素包含 `id`、`category`、`content`、`page` 和 `coordinates`。
基础版支持基础元素类别：`paragraph`、`heading1`、`heading2`、`heading3`、`list`、`table`、
`figure`、`caption`。不支持 `chart`、`equation`、`header`、`footer`、`index`、`footnote`
等高级元素类别。

#
## 使用流程

1. 确认文档格式在支持列表中（JPEG/PNG/BMP/PDF/TIFF）
2. 确认文档页数不超过 100 页，文件大小不超过 50 MB
3. 设置 API Key 到环境变量 `DOCUMENT_PARSE_API_KEY`
4. 发送同步请求到 `/v1/document-digitization`，参数 `model=document-parse`
5. 解析响应 JSON，提取 `content.markdown`
6. 将结果写入输出文件，打印绝对路径

#
## 示例

### 示例1：同步模式解析 PDF

```python
import os
import requests

with open("report.pdf", "rb") as f:
    response = requests.post(
        "https://api.example.com/v1/document-digitization",
        headers={"Authorization": f"Bearer {os.environ['DOCUMENT_PARSE_API_KEY']}"},
        files={"document": f},
        data={
            "model": "document-parse",
            "output_formats": "['markdown']",
            "mode": "standard",
            "ocr": "auto",
            "coordinates": "true"
        }
    )

result = response.json()
print(result["content"]["markdown"])
# 输出：
# # Quarterly Report Q2 2026
#
# ## Revenue Summary
# Total revenue reached $48.2M, representing a 23% year-over-year growth.

print(f"Pages processed: {result['usage']['pages']}")
# 输出：Pages processed: 12
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| API Key 缺失或无效 | 环境变量 `DOCUMENT_PARSE_API_KEY` 未设置 | 在控制台获取 API Key，设置到环境变量中 |
| 文件超过 50 MB 限制 | 文档体积超出上限 | 拆分文档后分批处理 |
| 同步模式页数超过 100 页 | 文档页数超出同步模式限制 | 升级到完整版使用异步模式，支持最多 1000 页 |
| 同步模式 5 分钟超时 | 文档复杂度高导致处理时间过长 | 升级到完整版使用异步模式 |
| 不支持的文件格式 | 使用了不在支持列表中的格式 | 转换为支持的格式：JPEG/PNG/BMP/PDF/TIFF |

## 常见问题

### Q1: 免费版支持异步模式吗？
A: 免费版仅支持同步模式（`/v1/document-digitization`），最多 100 页/50MB/5 分钟超时。
完整版支持异步模式（`/v1/document-digitization/async`），最多 1000 页，按 10 页批次处理。

### Q2: 免费版可以使用 enhanced 模式吗？
A: 免费版仅支持 `mode=standard`。完整版支持 `mode=enhanced`（复杂表格精确解析）和
`mode=auto`（逐页自动选择），以及 `merge_multipage_tables=true` 跨页表格合并。

### Q3: 免费版支持哪些文件格式？
A: 免费版支持 JPEG、PNG、BMP、PDF、TIFF。完整版额外支持 HEIC、DOCX、PPTX、XLSX、HWP、HWPX。

### Q4: 免费版可以使用 force OCR 吗？
A: 免费版仅支持 `ocr=auto`（自动检测）。完整版支持 `ocr=force` 强制对扫描 PDF 或图片
执行 OCR，适用于非原生数字文档。

### Q5: 免费版支持哪些元素类别？
A: 免费版支持基础元素：paragraph、heading1-3、list、table、figure、caption。完整版支持
全部 14 种类别，额外包括 chart、equation、header、footer、index、footnote。

### Q6: 如何升级到完整版？
A: 将技能替换为完整版 upstage-document-parse 即可。完整版包含 6 项核心能力：多格式解析、
同步/异步模式、增强模式与 OCR 控制、14 种版面元素识别、跨页表格合并和输出文件管理。

## 已知限制

- 仅支持同步模式，最多 100 页/50MB/5 分钟超时
- 仅支持 `mode=standard`，不支持 enhanced 和 auto 模式
- 仅支持 `ocr=auto`，不支持 force OCR
- 仅支持 JPEG/PNG/BMP/PDF/TIFF 格式，不支持 HEIC/DOCX/PPTX/XLSX/HWP
- 仅支持基础元素类别，不支持 chart/equation/header/footer/index/footnote
- 仅支持 Markdown 输出，不支持 HTML 和 text 格式
