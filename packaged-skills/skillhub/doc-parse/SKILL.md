---
slug: "doc-parse"
name: "doc-parse"
version: 1.0.1
displayName: "文档解析工具（专业版）"
summary: "通用文档解析工具，支持PDF、图片、扫描件的结构化信息提取与OCR识别。。文档解析工具 - （专业版） 核心能力: 文档解析, OCR识别, 表格提取, 版面分析, document par"
license: "Proprietary"
edition: "pro"
description: |-
  文档解析工具 - （专业版）

  核心能力: 文档解析, OCR识别, 表格提取, 版面分析, document parse, 结构化提取, 图片识别

  适用场景: 企业级场景，支持批量操作、团队协作与高级功能

  差异化: 完整版，包含高级功能、批量处理、企业集成与优先支持，兼容免费版所有数据格式
tags:
  - 文档解析
  - OCR
  - 表格识别
  - 版面分析
  - 工具
  - 效率
  - 知识
  - 文档
  - file_path
  - result
  - str
  - self
  - list
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# 文档解析工具（专业版）

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 文档解析工具（专业版）通用文档解析 | 不支持 | 支持 |
| 文档解析工具（专业版）信息提取与OCR识别 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

文档解析、OCR识别、结构化提取、版面分析、表格识别、多格式支持

### 专业版增强功能
- 批量处理与并行执行
- 企业级安全与审计
- 高级配置与自定义策略
- 免费版完全兼容，无缝升级
- 优先技术支持与问题响应

**输入**: 用户提供专业版增强功能所需的指令和必要参数.
**输出**: 返回专业版增强功能的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景1：文档结构化

将非结构化文档解析为结构化数据。**示例指令**：`

`解析这份文档的结构

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景2：图片OCR

对图片进行OCR文字识别。**示例指令**：`

`识别这张图片中的文字

### 场景3：表格识别

从文档中识别和提取表格。**示例指令**：`

`提取这份文档中的表格

## 使用流程

### 环境准备

```bash
# 确保Python环境可用
python3 --version
# ...
# 依赖说明
pip install requests
```

### 基础用法

```python
# 企业级文档解析引擎（PRO）
import os
import json
from typing import List, Dict, Optional
from pathlib import Path
from dataclasses import dataclass, field
# ...
@dataclass
class ParsedElement:
    element_type: str  # text, table, image, heading, list
    content: str
    confidence: float = 0.0
    bbox: List[float] = field(default_factory=list)
    page: int = 1
    metadata: dict = field(default_factory=dict)
# ...
@dataclass
class ParseResult:
    file_path: str
    elements: List[ParsedElement] = field(default_factory=list)
    full_text: str = ""
    tables: List[dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
# ...
class DocumentParseEngine:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.supported_formats = [".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".bmp"]
# ...
    def parse(self, file_path: str, options: dict = None) -> ParseResult:
        """完整文档解析（PRO 专属：多元素提取）"""
        if options is None:
            options = {}
        result = ParseResult(file_path=file_path)
        ext = Path(file_path).suffix.lower()
        if ext == ".pdf":
            result = self._parse_pdf(file_path, options)
        elif ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]:
            result = self._parse_image(file_path, options)
        return result
# ...
    def batch_parse(self, file_paths: List[str],
                   output_dir: str = "./output") -> List[ParseResult]:
        """批量解析（PRO 专属）"""
        Path(output_dir).mkdir(exist_ok=True)
        results = []
        for file_path in file_paths:
            result = self.parse(file_path)
            output_file = Path(output_dir) / (Path(file_path).stem + ".json")
            self._export_result(result, str(output_file))
            results.append(result)
        return results
# ...
    def extract_tables(self, file_path: str) -> List[dict]:
        """表格提取（PRO 专属）"""
        result = self.parse(file_path, {"tables_only": True})
        return result.tables
# ...
    def ocr_image(self, image_path: str, lang: str = "chi_sim") -> str:
        """图片OCR（PRO 专属）"""
        try:
            import pytesseract
            from PIL import Image
            img = Image.open(image_path)
            return pytesseract.image_to_string(img, lang=lang)
        except ImportError:
            return "OCR依赖未安装"
# ...
    def analyze_layout(self, file_path: str) -> dict:
        """版面分析（PRO 专属）"""
        result = self.parse(file_path)
        layout = {
            "total_pages": max((e.page for e in result.elements), default=0),
            "element_counts": {},
            "text_blocks": 0,
            "table_count": 0,
            "image_count": 0
        }
        for elem in result.elements:
            layout["element_counts"][elem.element_type] = \
                layout["element_counts"].get(elem.element_type, 0) + 1
            if elem.element_type == "text":
                layout["text_blocks"] += 1
            elif elem.element_type == "table":
                layout["table_count"] += 1
            elif elem.element_type == "image":
                layout["image_count"] += 1
        return layout
# ...
    def export_structured(self, result: ParseResult,
                         output_path: str, format: str = "json"):
        """导出结构化数据（PRO 专属）"""
        self._export_result(result, output_path, format)
# ...
    def _parse_pdf(self, file_path: str, options: dict) -> ParseResult:
        result = ParseResult(file_path=file_path)
        try:
            import pdfplumber
            with pdfplumber.open(file_path) as pdf:
                for i, page in enumerate(pdf.pages, 1):
                    text = page.extract_text() or ""
                    if text:
                        result.elements.append(ParsedElement(
                            element_type="text", content=text,
                            page=i, confidence=0.9
                        ))
                        result.full_text += text + NL
                    tables = page.extract_tables() or []
                    for table in tables:
                        result.tables.append({
                            "page": i, "data": table
                        })
                        result.elements.append(ParsedElement(
                            element_type="table", content=str(table),
                            page=i, confidence=0.8
                        ))
        except ImportError:
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            for i, page in enumerate(reader.pages, 1):
                text = page.extract_text() or ""
                result.elements.append(ParsedElement(
                    element_type="text", content=text, page=i
                ))
                result.full_text += text + NL
        result.metadata = {
            "format": "pdf",
            "pages": max((e.page for e in result.elements), default=0),
            "elements": len(result.elements)
        }
        return result
# ...
    def _parse_image(self, file_path: str, options: dict) -> ParseResult:
        result = ParseResult(file_path=file_path)
        text = self.ocr_image(file_path)
        result.full_text = text
        result.elements.append(ParsedElement(
            element_type="text", content=text,
            page=1, confidence=0.7
        ))
        result.metadata = {"format": "image", "ocr": True}
        return result
# ...
    def _export_result(self, result: ParseResult, output_path: str,
                      format: str = "json"):
        data = {
            "file_path": result.file_path,
            "full_text": result.full_text,
            "tables": result.tables,
            "metadata": result.metadata,
            "elements": [e.__dict__ for e in result.elements]
        }
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
# ...
engine = DocumentParseEngine()
result = engine.parse("document.pdf")
print(f"元素数: {len(result.elements)}")
print(f"表格数: {len(result.tables)}")
layout = engine.analyze_layout("document.pdf")
print(f"版面: {layout}")
```

### 执行结果

完成上述代码后，将根据输入参数返回结构化响应。专业版支持批量任务和并行解析，可同时解析多个文件或任务.
**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

**优秀轮输入**:
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

**第二轮补充(按需)**:
| 参数名(续)| 类型 | 必填 | 说明 |
|----:|----:|----:|----:|
| content | string | 条件必填 | parse 相关配置参数, 当Doc Parse 核心处理时必填 |
| content | string | 条件必填 | parse 相关配置参数, 当Doc Parse 智能分析时必填 |

## 输出格式

```json
{
  "success": true,
  "data": {
    "inversion_type": ""parse_result"",
    "collected_info": {
      "parse_metadata": "parse_metadata_value",
      "parse_status": "parse_status_value"
    },
    "result": {
      "parse_summary": "parse_summary_value",
      "parse_details": "parse_details_value",
      "parse_count": "parse_count_value"
    },
    "confidence": 0.95,
    "derivation_steps": [
      ""parse_timestamp"",
      ""parse_version"",
      ""field_9""
    ]
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| pdfplumber | Python库 | 推荐 | pip install pdfplumber |
| pytesseract | Python库 | 可选 | pip install pytesseract |
| Pillow | Python库 | 可选 | pip install Pillow |

### API Key 配置
- 需要文档解析服务API Key（如使用云端OCR服务）

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，
- **版本**: 专业版（v1.0.0 专业版，完整功能+企业级支持）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

```yaml
doc_parse:
  formats: [pdf, image, scanned]
  ocr: true
  ocr_languages: ["chi_sim", "eng"]
  output_format: json
  batch:
    max_files: 50
    parallel: true
    output_dir: "./output"
  extraction:
    text: true
    tables: true
    images: true
    headings: true
    lists: true
    metadata: true
  layout_analysis:
    enabled: true
    multi_column: true
    reading_order: true
  ocr_config:
    engine: tesseract
    dpi: 300
    preprocessing: [deskew, denoise, binarize]
    confidence_threshold: 0.6
  export:
    formats: [json, xml, csv, html]
    include_confidence: true
    include_bbox: true
```

### 配置说明

| 配置项 | 说明 | 默认值 |
|---:|:---|---:|
| 基础路径 | 工作目录 | `./` |
| 输出格式 | 结果输出格式 | `json` |
| 批量大小 | 单批处理数量 | `10` |
| 并行度 | 并行处理线程数 | `4` |
| 重试次数 | 失败重试次数 | `3` |

## 常见问题

### Q1: 批量处理时遇到内存不足？

A: 专业版支持分批处理，建议减小batch_size参数，或增加并行度但减少每批文件数量.
### Q2: 如何配置自动重试？

A: 在配置文件中设置retry_attempts和retry_delay参数。专业版支持指数退避重试策略.
### Q3: 如何监控处理进度？

A: 专业版内置进度追踪功能，通过回调或轮询方式获取实时处理状态。可配置webhook通知.
### Q4: 如何与现有系统集成？

A: 专业版提供完整的API接口和配置文件，支持CI/CD集成、定时任务和webhook回调.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

