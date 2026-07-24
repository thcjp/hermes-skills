---
slug: "markdown-exporter"
name: "markdown-exporter"
version: 3.6.11
displayName: "Markdown导出工具"
summary: "Markdown转DOCX/PPTX/XLSX/PDF/HTML/IPYNB/CSV/JSON/XML多格式导出引擎。"
license: "Proprietary"
description: |-
  Markdown文本多格式导出引擎，支持将Markdown转换为DOCX、PPTX、XLSX、PDF、PNG、
  HTML、IPYNB、CSV、JSON、JSONL、XML、LaTeX等12种专业格式。核心能力：
  - 文档格式转换（md_to_docx/md_to_pdf/md_to_html）
  - 表格数据导出（md_to_xlsx/md_to_csv/md_to_json/md_to_xml）
  - 演示文稿生成（md_to_pptx，支持模板和分栏布局）
  - 代码块提取（md_to_codeblock，支持ZIP压缩）
  - Jupyter Notebook转换（md_to_ipynb）
  - LaTeX学术格式导出（md_to_latex）
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 文档处理
  - Markdown
  - 文档
  - 工具
  - markdown
  - path
  - markdown-exporter
  - input
  - output
category: "Development"
---
# Markdown导出工具

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Markdown导出工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Markdown导出工具XML多格式导出 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 核心能力

### 1. 文档格式转换
```bash
markdown-exporter md_to_docx /path/input.md /path/output.docx
markdown-exporter md_to_pdf /path/input.md /path/output.pdf
markdown-exporter md_to_html /path/input.md /path/output.html
markdown-exporter md_to_html_text /path/input.md
markdown-exporter md_to_md /path/input.md /path/output.md
```- 验证返回数据的完整性和格式正确性
- 参考`文档格式转换`的配置文档进行参数调优
### 2. 表格数据导出
将Markdown表格转换为结构化数据格式：
```bash
markdown-exporter md_to_xlsx /path/input.md /path/output.xlsx
markdown-exporter md_to_csv /path/input.md /path/output.csv
markdown-exporter md_to_json /path/input.md /path/output.json
markdown-exporter md_to_xml /path/input.md /path/output.xml
markdown-exporter md_to_latex /path/input.md /path/output.tex
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `表格数据导出` 选项
- 处理流程: 接收输入 -> 执行表格数据导出 -> 返回结果
- 输入: 用户提供表格数据导出所需的参数和指令
- 输出: 返回表格数据导出的处理结果,包含执行状态码、结果数据和执行日志

### 3. 演示文稿生成
```bash
markdown-exporter md_to_pptx /path/input.md /path/output.pptx
markdown-exporter md_to_pptx /path/input.md /path/output.pptx --template /path/template.pptx
```
支持Pandoc风格的幻灯片语法：分栏布局（`::::: columns`）、演讲者备注（`::: notes`）、增量列表（`::: incremental`）、背景图片.
**处理**: 解析演示文稿生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `演示文稿生成` 选项

### 4. 代码块提取
```bash
markdown-exporter md_to_codeblock /path/input.md /path/output_dir
markdown-exporter md_to_codeblock /path/input.md /path/output.zip --compress
```
从Markdown中提取所有代码块，按语言保存为独立文件（`.py`/`.js`/`.sh`等）.
**处理**: 解析代码块提取的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `代码块提取` 选项

### 5. Jupyter Notebook转换
```bash
markdown-exporter md_to_ipynb /path/input.md /path/output.ipynb
markdown-exporter md_to_ipynb /path/input.md /path/output.ipynb --strip-wrapper
```
`--strip-wrapper` 选项移除代码块外层```包裹后再处理.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 支持格式总览

| 工具 | 输入 | 输出格式 |
|:---:|:---:|:---:|
| `md_to_docx` | Markdown文本 | Word文档(.docx) |
| `md_to_html` | Markdown文本 | HTML文件(.html) |
| `md_to_html_text` | Markdown文本 | HTML文本字符串(stdout) |
| `md_to_pdf` | Markdown文本 | PDF文件(.pdf) |
| `md_to_md` | Markdown文本 | Markdown文件(.md) |
| `md_to_ipynb` | Markdown文本 | Jupyter Notebook(.ipynb) |
| `md_to_pptx` | Markdown幻灯片 | PowerPoint(.pptx) |
| `md_to_xlsx` | Markdown表格 | Excel表格(.xlsx) |
| `md_to_csv` | Markdown表格 | CSV文件(.csv) |
| `md_to_json` | Markdown表格 | JSON/JSONL文件(.json) |
| `md_to_xml` | Markdown表格 | XML文件(.xml) |
| `md_to_latex` | Markdown表格 | LaTeX文件(.tex) |
| `md_to_codeblock` | Markdown代码块 | 代码文件(.py/.js/.sh等) |

## 适用场景

| 场景 | 输入 | 输出 |
|:------|------:|:------|
| 技术文档导出 | Markdown文档 | `.docx` Word文档 |
| 数据表导出 | Markdown表格 | `.xlsx`/`.csv`/`.json` |
| 演示文稿制作 | Pandoc风格Markdown | `.pptx` PowerPoint |
| 代码提取 | 含代码块的Markdown | 独立代码文件或ZIP |
| 学术论文 | Markdown内容 | `.tex` LaTeX文件 |
| 网页发布 | Markdown内容 | `.html` 自包含HTML |

**不适用于**：加密文件破解、二进制文件转换、非Markdown格式间互转.
## 使用流程

1. 安装：`pip install md-exporter`
2. 准备Markdown输入文件（所有命令仅支持文件路径输入）
3. 选择目标格式对应的子命令
4. 执行转换：`markdown-exporter <subcommand> <input> <output> [options]`
5. 验证输出文件

## 示例

### 示例1：Markdown转Word
```bash
markdown-exporter md_to_docx /home/user/report.md /home/user/report.docx
```
输入 `report.md` 包含标题、段落、列表和表格，输出 `report.docx` 保留格式结构.
### 示例2：表格数据导出
```bash
markdown-exporter md_to_xlsx /home/user/data.md /home/user/data.xlsx
```
输入 `data.md`：
```markdown
| Name | Price | Stock |
|---:|:---|---:|
| Item A | $10 | 50 |
| Item B | $20 | 30 |
```
输出 `data.xlsx` Excel表格，表头为Name/Price/Stock，两行数据.
### 示例3：代码块提取为ZIP
```bash
markdown-exporter md_to_codeblock /home/user/tutorial.md /home/user/code.zip --compress
```
输入包含Python和JavaScript代码块的Markdown文件，输出ZIP包含 `block_1.py` 和 `block_2.js`.
### 示例4：PPTX带模板
```bash
markdown-exporter md_to_pptx /home/user/slides.md /home/user/output.pptx --template /home/user/corporate.pptx
```
使用企业模板 `corporate.pptx` 的样式生成演示文稿.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| `md_to_pptx` 输出幻灯片格式错乱 | Markdown未使用Pandoc幻灯片语法 | 确保每个 `##` 标题作为新幻灯片起始，分栏用 `::::: columns`，备注用 `::: notes` |
| `md_to_xlsx` 报 "no tables found" | 输入Markdown中无标准表格 | 确保表格使用 `| col |` 管道符格式，表头分隔行 `|---|---|` 必须存在 |
| `md_to_codeblock` 文件名冲突 | 多个代码块语言相同 | 输出文件自动编号：`block_1.py`、`block_2.py`，避免覆盖 |
| `md_to_ipynb` 代码单元格未正确分隔 | Markdown代码块缺少语言标注 | 确保代码块使用 ` ```python ` 格式标注语言，`--strip-wrapper` 可移除外层包裹 |
| `md_to_pdf` 中文字体缺失 | PDF生成引擎未安装中文字体 | 安装中文字体包（如Noto Sans CJK），或使用 `md_to_html` 后通过浏览器打印为PDF |
| `md_to_json` 表格含合并单元格 | Markdown标准不支持合并单元格 | JSON导出仅支持标准Markdown表格，合并单元格需先拆分为多行普通表格 |

## 常见问题

### Q1: 所有命令为什么只支持文件路径输入而不支持管道？
设计上要求所有输入为文件路径，确保大文件处理的稳定性和可重现性。如果需要处理管道输入的Markdown文本，先写入临时文件再调用命令：`echo "$markdown" > /tmp/input.md && markdown-exporter md_to_docx /tmp/input.md /tmp/output.docx`.
### Q2: `md_to_pptx` 支持哪些幻灯片布局？
支持Pandoc风格的幻灯片语法：标题+内容布局（`##` 标题后跟内容）、两栏布局（`::::: columns` + `::: column`）、比较布局（含图片的栏触发）、内容带说明（图片+caption）、增量列表（`::: incremental`）、空白布局（仅背景图+备注）。通过 `--template` 可使用自定义PPTX模板控制视觉风格.
### Q3: `md_to_codeblock` 如何处理代码块语言识别？
代码块的语言标注（如 ` ```python `）决定输出文件扩展名：`python`→`.py`，`javascript`→`.js`，`bash`→`.sh`，`sql`→`.sql`等。未标注语言的代码块默认输出为 `.txt`。使用 `--compress` 将所有代码块打包为ZIP，适合教程场景一次性分发所有示例代码.
### Q4: `md_to_html` 和 `md_to_html_text` 有什么区别？
`md_to_html` 输出完整的HTML文件（含`<html>`/`<head>`/`<body>`标签），适合直接部署或保存。`md_to_html_text` 仅输出HTML片段到stdout，适合嵌入到其他HTML页面或程序中处理。如果需要完整网页用 `md_to_html`，如果需要HTML片段用于集成用 `md_to_html_text`.
### Q5: 表格导出为JSON的格式是什么样的？
Markdown表格导出为JSON时，每行变为一个JSON对象，表头为键名。例如表格 `| Name | Price |` 导出为 `[{"Name": "Item A", "Price": "$10"}, {"Name": "Item B", "Price": "$20"}]`。JSONL格式则每行一个独立JSON对象，适合流式处理大数据量表格.
### Q6: 如何生成带样式的Word文档？
`md_to_docx` 基本转换保留Markdown的标题层级、列表、加粗/斜体、表格等结构。如需自定义样式（字体、颜色、页眉页脚），建议先转为HTML（`md_to_html`），在HTML中嵌入CSS样式，再通过Pandoc等工具转为DOCX。或使用 `--template` 参数指定已有的样式模板（部分子命令支持）.
## 已知限制

- 所有命令仅支持文件路径输入，不支持stdin管道
- 多表格/多代码块场景下输出文件自动编号
- PDF生成依赖系统字体配置，中文需额外安装字体
- PPTX布局基于Pandoc语法，不兼容所有PowerPoint功能
- LaTeX导出仅支持表格内容，全文LaTeX需额外处理

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Markdown导出工具处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "markdown-exporter"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
