---
slug: pandoc-convert-openclaw
name: pandoc-convert-openclaw
version: "0.1.0"
displayName: Pandoc Convert
summary: Convert documents between 40+ formats using pandoc CLI. Handles Markdown
  ↔ Word ↔ PDF ↔ HTML ↔ La...
license: MIT
description: |-
  Convert documents between 40+ formats using pandoc CLI。Handles Markdown
  ↔ Word ↔ PDF ↔ HTML ↔ La。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
---
# Pandoc Convert

## 核心能力

* **40+ Format Support**: Markdown, Word, PDF, HTML, LaTeX, EPUB, RST, AsciiDoc, Org-mode, and more
* **Dual Toolset**: Python for smart conversions + bash for validation/batch processing
* **Professional Templates**: 12 templates covering academic, business, and web use cases
* **Comprehensive Documentation**: Format guides, troubleshooting, templates, and quick reference
* **Smart Defaults**: Optimized settings for each conversion path
* **Metadata Preservation**: Keep titles, authors, dates across formats
* **Error Recovery**: Validation and helpful error messages

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Using Python Helper (Recommended)

```bash
python scripts/convert.py input.md output.pdf

python scripts/convert.py report.md report.pdf --template business --toc

python scripts/convert.py --batch *.md --format pdf --output-dir ./pdfs
```

### Using Bash Utilities

```bash
./scripts/batch_convert.sh input/*.md pdf output/

./scripts/validate.sh output/document.pdf
./scripts/validate.sh output/book.epub
```

### Direct Pandoc

```bash
pandoc input.md -o output.pdf

pandoc input.md -o output.docx

pandoc input.docx -o output.md --extract-media=./media
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理

### Common Issues

* **"pandoc: command not found"** → Install pandoc (see INSTALL.md)
* **"pdflatex not found"** → Install LaTeX distribution
* **Unicode broken in PDF** → Use `--pdf-engine=xelatex`
* **Images missing** → Check paths and use `--resource-path`
* **EPUB validation fails** → Run epubcheck for details

See `references/troubleshooting.md` for comprehensive solutions.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1：基础用法

```
### Using Python Helper (Recommended)

```bash
python scripts/convert.py input.md output.pdf

python scripts/convert.py report.md report.pdf --template business --toc

python scripts/convert.py --batch *.md --format pdf --output-dir ./pdfs
```

### Using Bash Utilities

```bash
./scripts/batch_convert.sh input/*.md pdf output/

./scripts/validate.sh output/document.pdf
./scripts/validate.sh output/book.epub
```

### Direct Pandoc

```bash
pandoc input.md -o output.pdf

pandoc input.md -o output.
```

## 常见问题

### Q1: 如何开始使用Pandoc Convert？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Pandoc Convert有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
