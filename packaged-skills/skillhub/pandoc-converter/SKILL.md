---

slug: "pandoc-converter"
name: "pandoc-convert-openclaw"
version: "0.1.0"
displayName: "Pandoc Convert"
summary: "用pandoc CLI在40+格式间转文档,Markdown/Word/PDF/HTML。Convert documents between 40+ formats using pandoc"
license: "MIT"
description: |-
  Convert documents between 40+ formats using pandoc CLI。Handles Markdown
  ↔ Word ↔ PDF ↔ HTML ↔ La。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解.
tags: 文档,工作流,pdf,format,请参考,目录中的
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"

---

# Pandoc Convert

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

* **40+ Format Support**: Markdown, Word, PDF, HTML, LaTeX, EPUB, RST, AsciiDoc, Org-mode, and more
* **Dual Toolset**: Python for smart conversions + bash for validation/batch processing
* **Professional Templates**: 12 templates covering academic, business, and web use cases
* **Comprehensive Documentation**: Format guides, troubleshooting, templates, and quick reference
* **Smart Defaults**: Optimized settings for each conversion path
* **Metadata Preservation**: Keep titles, authors, dates across formats
* **Error Recovery**: Validation and helpful error messages
### 40+ Format Support

针对40+ Format Support,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供40+ Format Support相关的配置参数、输入数据和处理选项.
**输出**: 返回40+ Format Support的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`+ Format Support`的配置文档进行参数调优
### Dual Toolset

针对Dual Toolset,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Dual Toolset相关的配置参数、输入数据和处理选项.
**输出**: 返回Dual Toolset的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Dual Toolset`的配置文档进行参数调优
### Professional Templates

针对Professional Templates,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Professional Templates相关的配置参数、输入数据和处理选项.
**输出**: 返回Professional Templates的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Professional Templates`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 格式转换 | 源文件与目标格式(MD/Word/PDF/HTML) | 转换后的目标格式文档 |
| 批量处理 | 多个源文件与统一输出格式 | 批量转换结果目录 |
| 模板应用 | 文档与模板类型(学术/商务/网页) | 带目录与元数据的专业文档 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Using Python Helper (Recommended)

```bash
python （请参考skill目录中的脚本文件） input.md output.pdf
# ...
python （请参考skill目录中的脚本文件） report.md report.pdf --template business --toc
# ...
python （请参考skill目录中的脚本文件） --batch *.md --format pdf --output-dir ./pdfs
```

### Using Bash Utilities

```bash
（请参考skill目录中的脚本文件） input/*.md pdf output/
# ...
（请参考skill目录中的脚本文件） output/document.pdf
（请参考skill目录中的脚本文件） output/book.epub
```

### Direct Pandoc

```bash
pandoc input.md -o output.pdf
# ...
pandoc input.md -o output.docx
# ...
pandoc input.docx -o output.md --extract-media=./media
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | pandoc-convert-openclaw处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "openclaw_result": "openclaw_result_value",
      "openclaw_metadata": "openclaw_metadata_value",
      "openclaw_status": "openclaw_status_value"
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

中间产物模板参考: `assets/pandoc-convert-openclaw_template`

## 异常处理

### Common Issues

* **"pandoc: command not found"** → Install pandoc (see INSTALL.md)
* **"pdflatex not found"** → Install LaTeX distribution
* **Unicode broken in PDF** → Use `--pdf-engine=xelatex`
* **Images missing** → Check paths and use `--resource-path`
* **EPUB validation fails** → Run epubcheck for details

See `references/troubleshooting.md` for comprehensive solutions.

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置;检查命令权限设置 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1：基础用法

```
### Using Python Helper (Recommended)(补充)
# ...
```bash
python （请参考skill目录中的脚本文件） input.md output.pdf

python （请参考skill目录中的脚本文件） report.md report.pdf --template business --toc

python （请参考skill目录中的脚本文件） --batch *.md --format pdf --output-dir ./pdfs
```
# ...
### Using Bash Utilities(补充)
# ...
```bash
（请参考skill目录中的脚本文件） input/*.md pdf output/

（请参考skill目录中的脚本文件） output/document.pdf
（请参考skill目录中的脚本文件） output/book.epub
```
# ...
### Direct Pandoc(补充)
# ...
```bash
pandoc input.md -o output.pdf

pandoc input.md -o output.
```
# ...
## 常见问题
# ...
### Q1: 如何开始使用Pandoc Convert？
A: 
# ...
### Q2: 遇到错误怎么办？
A: 
# ...
### Q3: Pandoc Convert有什么限制？
A: 
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...