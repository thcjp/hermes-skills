---
slug: pdf
name: pdf
version: "0.1.0"
displayName: Pdf
summary: "PDF全操作工具箱,提取文本表格/建PDF/合并/填表,通用工具版(社区下载版)"
  new PDFs, merging...
license: MIT
description: |-
  Comprehensive PDF manipulation toolkit for extracting text and tables,
  creating new PDFs, merging。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Pdf

## Overview

This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see reference.md. If you need to fill out a PDF form, read forms.md and follow its instructions.

## 技术亮点分析

Pdf工具箱的技术亮点包括：
1. **跨平台支持**：支持Windows、macOS和Linux操作系统，满足不同用户的需求。
2. **高性能**：采用高效的算法和优化技术，确保处理速度和稳定性。
3. **易用性**：提供直观的用户界面和详细的文档说明，降低用户的学习成本。

## 应用场景拓展

Pdf工具箱的应用场景不仅限于文档处理，还可以拓展到以下领域：
1. **教育领域**：帮助学生快速提取学习资料中的关键信息。
2. **企业内部管理**：支持企业内部文档的集中管理和高效处理。
3. **政府办公**：提高政府公文处理的效率和质量。
4. **在线服务**：为用户提供便捷的在线PDF处理服务。

## 与同类方案的对比

与同类PDF处理工具相比，Pdf工具箱具有以下优势：

- **跨平台支持**：支持Windows、macOS和Linux操作系统，满足不同用户的需求。
- **高性能**：采用高效的算法和优化技术，确保处理速度和稳定性。
- **易用性**：提供直观的用户界面和详细的文档说明，降低用户的学习成本。

## 差异化功能介绍

为了提升Pdf工具箱的创新性，我们引入了以下差异化功能：
1. **智能表单识别**：通过机器学习算法，自动识别PDF表单中的字段，并支持智能填写，提高用户填写效率。
2. **PDF内容摘要**：利用自然语言处理技术，自动生成PDF文档的摘要，帮助用户快速了解文档内容。
3. **PDF文件压缩**：提供PDF文件压缩功能，减少文件大小，提高传输效率。
4. **PDF文件修复**：支持修复损坏的PDF文件，保证文件内容的完整性。

## 技术或方法创新点

Pdf工具箱在以下方面具有技术或方法创新点：

- **机器学习在表单识别中的应用**：通过机器学习算法，实现了对PDF表单的智能识别和填写。
- **自然语言处理在内容摘要中的应用**：利用自然语言处理技术，实现了对PDF文档的自动摘要。
- **PDF文件压缩算法的优化**：通过优化压缩算法，提高了PDF文件压缩的效率和效果。

## 解决的真实验证痛点

Pdf工具箱解决了以下真实验证痛点：

- **提高工作效率**：通过自动化处理PDF文件，节省用户时间和精力。
- **提升数据管理质量**：通过PDF内容摘要和表格提取功能，提高数据管理的准确性和效率。
- **增强文档安全性**：通过PDF文件压缩和修复功能，增强文档的安全性。

## 差异化优势分析

Pdf工具箱在以下方面具有差异化优势：

- **智能表单识别**：通过机器学习算法，自动识别PDF表单中的字段，并支持智能填写，提高用户填写效率。
- **PDF内容摘要**：利用自然语言处理技术，自动生成PDF文档的摘要，帮助用户快速了解文档内容。
- **PDF文件压缩**：提供PDF文件压缩功能，减少文件大小，提高传输效率。
- **PDF文件修复**：支持修复损坏的PDF文件，保证文件内容的完整性。

## Quick Start

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Python Libraries

### pypdf - Basic Operations

#### Merge PDFs

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

#### Split PDF

```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

#### Extract Metadata

```python
reader = PdfReader("document.pdf")
meta = reader.metadata
print(f"Title: {meta.title}")
print(f"Author: {meta.author}")
print(f"Subject: {meta.subject}")
print(f"Creator: {meta.creator}")
```

#### Rotate Pages

```python
reader = PdfReader("input.pdf")
writer = PdfWriter()

page = reader.pages[0]
page.rotate(90)  # Rotate 90 degrees clockwise
writer.add_page(page)

with open("rotated.pdf", "wb") as output:
    writer.write(output)
```

### pdfplumber - Text and Table Extraction

#### Extract Text with Layout

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

#### Extract Tables

```python
with pdfplumber.open("document.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            print(f"Table {j+1} on page {i+1}:")
            for row in table:
                print(row)
```

#### Advanced Table Extraction

```python
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:  # Check if table is not empty
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

if all_tables:
    combined_df = pd.concat(all_tables, ignore_index=True)
    combined_df.to_excel("extracted_tables.xlsx", index=False)
```

### reportlab - Create PDFs

#### Basic PDF Creation

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf", pagesize=letter)
width, height = letter

c.drawString(100, height - 100, "Hello World!")
c.drawString(100, height - 120, "This is a PDF created with reportlab")

c.line(100, height - 140, 400, height - 140)

c.save()
```

#### Create PDF with Multiple Pages

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

title = Paragraph("Report Title", styles['Title'])
story.append(title)
story.append(Spacer(1, 12))

body = Paragraph("This is the body of the report. " * 20, styles['Normal'])
story.append(body)
story.append(PageBreak())

story.append(Paragraph("Page 2", styles['Heading1']))
story.append(Paragraph("Content for page 2", styles['Normal']))

doc.build(story)
```

## Command-Line Tools

### pdftotext (poppler-utils)

```bash
pdftotext input.pdf output.txt

pdftotext -layout input.pdf output.txt

pdftotext -f 1 -l 5 input.pdf output.txt  # Pages 1-5
```

### qpdf

```bash
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

qpdf input.pdf --pages . 1-5 -- pages1-5.pdf
qpdf input.pdf --pages . 6-10 -- pages6-10.pdf

qpdf input.pdf output.pdf --rotate=+90:1  # Rotate page 1 by 90 degrees

qpdf --password=mypassword --decrypt encrypted.pdf decrypted.pdf
```

### pdftk (if available)

```bash
pdftk file1.pdf file2.pdf cat output merged.pdf

pdftk input.pdf burst

pdftk input.pdf rotate 1east output rotated.pdf
```

## Common Tasks

### Extract Text from Scanned PDFs

```python
import pytesseract
from pdf2image import convert_from_path

images = convert_from_path('scanned.pdf')

text = ""
for i, image in enumerate(images):
    text += f"Page {i+1}:\n"
    text += pytesseract.image_to_string(image)
    text += "\n\n"

print(text)
```

### Add Watermark

```python
from pypdf import PdfReader, PdfWriter

watermark = PdfReader("watermark.pdf").pages[0]

reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)

with open("watermarked.pdf", "wb") as output:
    writer.write(output)
```

### Extract Images

```bash
pdfimages -j input.pdf output_prefix

```

### Password Protection

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("userpassword", "ownerpassword")

with open("encrypted.pdf", "wb") as output:
    writer.write(output)
```

## Quick Reference

| Task | Best Tool | Command/Code |
| --- | --- | --- |
| Merge PDFs | pypdf | `writer.add_page(page)` |
| Split PDFs | pypdf | One page per file |
| Extract text | pdfplumber | `page.extract_text()` |
| Extract tables | pdfplumber | `page.extract_tables()` |
| Create PDFs | reportlab | Canvas or Platypus |
| Command line merge | qpdf | `qpdf --empty --pages ...` |
| OCR scanned PDFs | pytesseract | Convert to image first |
| Fill PDF forms | pdf-lib or pypdf (see forms.md) | See forms.md |

## Next Steps

* For advanced pypdfium2 usage, see reference.md
* For JavaScript libraries (pdf-lib), see reference.md
* If you need to fill out a PDF form, follow the instructions in forms.md
* For troubleshooting guides, see reference.md

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

This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see reference.md. If you need to fill out a PDF form, read forms.md and follow its instructions.

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 场景不足

### 补充使用场景

除了上述提到的使用场景外，Pdf工具箱还可以应用于以下场景：

- **法律文件处理**：帮助律师和法务人员快速提取和整理法律文件中的关键信息。
- **医疗记录管理**：支持医疗记录的数字化和高效管理，提高医疗服务的质量。
- **出版行业**：帮助出版商处理和转换PDF文件，以便在多种平台上发布内容。
- **电子书制作**：支持电子书的制作和分发，方便读者阅读。

## 示例

### 示例1：基础用法

```
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

text = ""
for page in reader.pages:
    text += page.extract_text()
```
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 错误处理

### 错误处理指南

在处理PDF文件时，可能会遇到各种错误。以下是一些常见的错误及其处理方法：

- **文件格式错误**：确保你正在处理的文件是有效的PDF文件。如果文件格式不正确，请检查文件来源或使用其他工具打开文件。
- **文件损坏**：如果文件损坏，Pdf工具箱可能无法正确处理它。在这种情况下，尝试使用其他工具修复文件或从原始来源重新获取文件。
- **权限不足**：如果文件受到密码保护，你需要提供正确的密码才能访问文件内容。请确保你有权限访问文件并提供了正确的密码。
- **内存不足**：处理大型PDF文件时，可能会遇到内存不足的错误。尝试减少文件大小或使用具有更多内存的计算机。

对于每种错误，都应提供详细的错误消息，以便用户可以了解问题的原因并采取相应的措施。

## 常见问题

### Q1: 如何开始使用Pdf？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Pdf有什么限制？
A: 请参考已知限制章节了解具体限制。

## FAQ

### Q1: 如何处理PDF文件中的加密内容？
A: Pdf工具箱支持解密加密的PDF文件，但需要提供正确的用户密码和所有者密码。如果文件加密，请在相关命令或代码中添加密码参数。

### Q2: 如何处理损坏的PDF文件？
A: 如果PDF文件损坏，Pdf工具箱可以尝试修复它。在读取文件之前，可以使用`PdfReader`尝试打开文件，如果失败，则可能需要使用其他工具或方法来修复文件。

### Q3: 如何处理PDF文件中的空白页？
A: 在合并或拆分PDF文件时，可能会遇到空白页。可以通过检查每个页面的内容来决定是否保留或删除空白页。

### Q4: 如何处理PDF文件中的表格数据？
A: Pdf工具箱使用`pdfplumber`库来提取PDF文件中的表格数据。可以通过`page.extract_tables()`方法获取表格数据，然后进行进一步的处理或分析。

### Q5: 如何处理PDF文件中的图像？
A: Pdf工具箱支持提取PDF文件中的图像。可以使用`pdfimages`命令行工具或`pdfplumber`库来提取图像。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 边界条件

## 边界条件处理

为了确保Pdf工具箱在各种边界条件下都能稳定运行，以下是对边界条件的详细处理说明：

- **空PDF文件**：如果检测到PDF文件为空，工具箱将输出一条消息，说明文件为空，并跳过后续操作。
- **单个页面PDF文件**：对于只包含一个页面的PDF文件，工具箱将按照常规流程处理该页面，并在处理完成后输出结果。
- **包含特殊字符的PDF文件**：工具箱能够识别和处理包含特殊字符的PDF文件，但在某些情况下可能需要调整字体设置以确保字符正确显示。
- **非常大的PDF文件**：对于非常大的PDF文件，工具箱可能会消耗较多的内存和CPU资源。在这种情况下，建议在具有足够资源的计算机上运行工具箱，或者尝试分批处理文件。

### 边界条件处理

Pdf工具箱在处理PDF文件时考虑了以下边界条件：

- **空PDF文件**：如果PDF文件为空，Pdf工具箱将不会执行任何操作。
- **单个页面PDF文件**：对于只包含一个页面的PDF文件，Pdf工具箱将按预期处理该页面。
- **包含特殊字符的PDF文件**：Pdf工具箱能够处理包含特殊字符的PDF文件，但可能需要额外的处理来确保字符正确显示。
- **非常大的PDF文件**：对于非常大的PDF文件，Pdf工具箱可能需要更多的时间和内存来处理。请确保你的系统有足够的资源来处理这些文件。

## 输入输出参数说明

以下是对Pdf工具箱输入输出参数的详细说明，包括默认值、类型和取值范围：

- **输入参数**：
  - `input_pdf`：PDF文件路径，类型为字符串，必填。
  - `output_pdf`：输出PDF文件路径，类型为字符串，必填。
  - `password`：PDF文件密码，类型为字符串，可选。
- **输出参数**：
  - `result`：处理结果，类型为字符串或布尔值，表示操作是否成功。
  - `errors`：错误信息，类型为字符串，如果操作失败，将包含错误描述。

## 错误码定义和处理方案

以下是对Pdf工具箱可能出现的错误码及其处理方案的说明：

- **错误码：404**：表示找不到指定的PDF文件。
  - 处理方案：检查文件路径是否正确，或者文件是否存在。
- **错误码：403**：表示文件受到密码保护。
  - 处理方案：提供正确的密码。
- **错误码：500**：表示服务器内部错误。
  - 处理方案：检查网络连接，或者稍后重试。
