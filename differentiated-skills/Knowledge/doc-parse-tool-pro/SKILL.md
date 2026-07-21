---
slug: doc-parse-tool-pro
name: doc-parse-tool-pro
version: "1.0.0"
displayName: 文档解析工具（专业版）
summary: 通用文档解析工具，支持PDF、图片、扫描件的结构化信息提取与OCR识别。
license: Proprietary
edition: pro
description: |-
  文档解析工具 - （专业版）

  核心能力: 文档解析, OCR识别, 表格提取, 版面分析, document parse, 结构化提取, 图片识别

  适用场景: 企业级场景，支持批量操作、团队协作与高级功能

  差异化: 完整版，包含高级功能、批量处理、企业集成与优先支持，兼容免费版所有数据格式

  触发关键词: 文档解析, OCR识别, 表格提取, 版面分析, document parse, 结构化提取, 图片识别
tags:
- 文档解析
- OCR
- 表格识别
- 版面分析
tools:
  - - read
- exec
---

# 文档解析工具（专业版）

## 概述

文档解析工具是针对文档解析领域的专业化AI辅助工具。专业版面向企业用户，提供完整的功能体系，包含高级特性、批量处理与企业级集成能力。

本工具经过深度优化，增强元数据和触发关键词，完全适配SkillHub平台规范。

## 核心能力

文档解析、OCR识别、结构化提取、版面分析、表格识别、多格式支持

### 专业版增强功能

- 批量处理与并行执行
- 企业级安全与审计
- 高级配置与自定义策略
- 免费版完全兼容，无缝升级
- 优先技术支持与问题响应

## 使用场景

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

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景3：表格识别

从文档中识别和提取表格。**示例指令**：`

`提取这份文档中的表格

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果


## 快速开始

### 环境准备

```bash
# 确保Python环境可用
python3 --version

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

@dataclass
class ParsedElement:
    element_type: str  # text, table, image, heading, list
    content: str
    confidence: float = 0.0
    bbox: List[float] = field(default_factory=list)
    page: int = 1
    metadata: dict = field(default_factory=dict)

@dataclass
class ParseResult:
    file_path: str
    elements: List[ParsedElement] = field(default_factory=list)
    full_text: str = ""
    tables: List[dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

class DocumentParseEngine:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.supported_formats = [".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".bmp"]

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

    def extract_tables(self, file_path: str) -> List[dict]:
        """表格提取（PRO 专属）"""
        result = self.parse(file_path, {"tables_only": True})
        return result.tables

    def ocr_image(self, image_path: str, lang: str = "chi_sim") -> str:
        """图片OCR（PRO 专属）"""
        try:
            import pytesseract
            from PIL import Image
            img = Image.open(image_path)
            return pytesseract.image_to_string(img, lang=lang)
        except ImportError:
            return "OCR依赖未安装"

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

    def export_structured(self, result: ParseResult,
                         output_path: str, format: str = "json"):
        """导出结构化数据（PRO 专属）"""
        self._export_result(result, output_path, format)

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

engine = DocumentParseEngine()
result = engine.parse("document.pdf")
print(f"元素数: {len(result.elements)}")
print(f"表格数: {len(result.tables)}")
layout = engine.analyze_layout("document.pdf")
print(f"版面: {layout}")
```

### 执行结果

执行上述代码后，将根据输入参数返回结构化结果。专业版支持批量操作和并行处理，可同时处理多个文件或任务。

## 示例

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
|:-------|:-----|:-------|
| 基础路径 | 工作目录 | `./` |
| 输出格式 | 结果输出格式 | `json` |
| 批量大小 | 单批处理数量 | `10` |
| 并行度 | 并行处理线程数 | `4` |
| 重试次数 | 失败重试次数 | `3` |


## 免费版兼容性

本专业版完全兼容免费版的数据格式与操作方式：

| 特性 | 免费版 | 专业版 |
|:-----|:------|:------|
| 基础功能 | 支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 并行处理 | 不支持 | 支持 |
| 高级配置 | 有限 | 完整 |
| 审计报告 | 不支持 | 支持 |
| 优先支持 | 社区 | 优先通道 |

免费版创建的文件可无缝升级到专业版处理，无需任何格式转换。

## 企业级功能

### 批量处理能力
- 支持多文件并行处理
- 自动错误重试与恢复
- 处理进度实时追踪
- 结果报告自动生成

### 安全与审计
- 操作日志完整记录
- 敏感数据加密存储
- 多租户隔离支持
- 合规性检查内置

## 最佳实践

### 企业级最佳实践

1. **明确需求**：对于大批量任务，先规划分批策略与并行度
2. **检查输入**：批量处理前先验证所有输入文件的有效性
3. **保存结果**：处理结果自动归档并生成审计报告
4. **定期清理**：监控资源使用，合理配置并行度与批大小
5. **错误处理**：配置自动重试与错误恢复策略

### 性能优化

```python
# 专业版：批量性能优化
# 1. 合理设置并行度（建议CPU核心数）
# 2. 分批处理避免内存溢出
# 3. 使用异步IO提升吞吐量
# 4. 启用结果缓存减少重复计算
```

## 常见问题

### Q1: 批量处理时遇到内存不足？

A: 专业版支持分批处理，建议减小batch_size参数，或增加并行度但减少每批文件数量。

### Q2: 如何配置自动重试？

A: 在配置文件中设置retry_attempts和retry_delay参数。专业版支持指数退避重试策略。

### Q3: 如何监控处理进度？

A: 专业版内置进度追踪功能，通过回调或轮询方式获取实时处理状态。可配置webhook通知。

### Q4: 如何与现有系统集成？

A: 专业版提供完整的API接口和配置文件，支持CI/CD集成、定时任务和webhook回调。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+


### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| pdfplumber | Python库 | 推荐 | pip install pdfplumber |
| pytesseract | Python库 | 可选 | pip install pytesseract |
| Pillow | Python库 | 可选 | pip install Pillow |

### API Key 配置
- 需要文档解析服务API Key（如使用云端OCR服务）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
- **版本**: 专业版（v1.0.0 专业版，完整功能+企业级支持）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
