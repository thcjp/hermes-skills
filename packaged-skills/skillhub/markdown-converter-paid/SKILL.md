---
slug: "markdown-converter-paid"
name: "markdown-converter-paid"
version: 1.0.1
displayName: "Markdown转换器专业版"
summary: "企业级文档批量转换系统,支持目录扫描、批量处理、自定义模板、元数据提取与CI/CD集成,适合团队与商业项目。"
license: "Proprietary"
edition: "pro"
description: |-
  Markdown转换器专业版为企业与内容团队提供系统化的文档转换解决方案。在免费版基础转换能力之上,增加批量处理、目录扫描、自定义输出模板、
  元数据提取、文档质量审计与CI/CD集成能力。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解.
tags:
  - Markdown
  - 文档转换
  - 企业级
  - 批量处理
  - 自动化
  - CI/CD
  - 文档
  - 工具
  - true
  - markdown
  - 转换器专
  - 不支持
  - 元数据提
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# Markdown转换器专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Markdown转换器专业版企业级文档批量转换 | 不支持 | 支持 |
| Markdown转换器专业版支持目录扫描 | 不支持 | 支持 |
| Markdown转换器专业版批量处理 | 不支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |

## 核心能力

### 批量目录扫描
```bash
# 递归扫描目录,批量转换所有文档
python3 batch_convert.py \
  --input ./documents/ \
  --output ./markdown/ \
  --recursive \
  --formats "pdf,docx,pptx,xlsx,html" \
  --parallel 8 \
  --preserve-structure
```

```python
# 批量转换配置
batch_config = {
    "input_dir": "./documents/",
    "output_dir": "./markdown/",
    "recursive": True,
    "formats": ["pdf", "docx", "pptx", "xlsx", "html", "csv", "json"],
    "parallel_workers": 8,
    "preserve_structure": True,      # 保留目录结构
    "skip_existing": True,           # 跳过已转换的文件
    "quality_check": True,           # 转换后质量检查
    "extract_metadata": True,        # 提取元数据
    "generate_index": True           # 生成索引文件
}
```- 验证返回数据的完整性和格式正确性
- 参考`元数据提取`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`自定义输出模板`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`批量目录扫描`的配置文档进行参数调优
### 自定义输出模板
```yaml
# output-template.yml
template:
  header: |
    ---
    title: "{title}"
    author: "{author}"
    date: "{date}"
    source: "{source_file}"
    converted: "{conversion_date}"
    format: "{source_format}"
    ---
# ...
  body: |
    # {title}
    > 来源: {source_file}
    > 转换时间: {conversion_date}
# ...
    {content}
# ...
  footer: |
    ---
    *本文档由Markdown转换器专业版自动生成*
# ...
  metadata:
    extract:
      - title
      - author
      - date
      - keywords
      - description
    frontmatter: true
```

**输入**: 用户提供自定义输出模板所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `自定义输出模板` 选项
- 处理流程: 接收输入 -> 执行自定义输出模板 -> 返回结果
- 输入: 用户提供自定义输出模板所需的参数和指令
- 输出: 返回自定义输出模板的处理结果,包含执行状态码、结果数据和执行日志

### 元数据提取
```python
# 元数据提取与管理
metadata_config = {
    "extract_fields": [
        "title",           # 文档标题
        "author",          # 作者
        "created_date",    # 创建日期
        "modified_date",   # 修改日期
        "keywords",        # 关键词
        "description",     # 描述
        "page_count",      # 页数(PDF)
        "word_count",      # 字数
        "language"         # 语言
    ],
    "frontmatter_format": "yaml",    # YAML前置元数据
    "index_file": "index.md",        # 生成索引文件
    "searchable": True               # 可搜索
}
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `元数据提取` 选项
- 处理流程: 接收输入 -> 执行元数据提取 -> 返回结果
- 输入: 用户提供元数据提取所需的参数和指令
- 输出: 返回元数据提取的处理结果,包含执行状态码、结果数据和执行日志

### 文档质量审计
```python
# 转换质量自动审计
quality_audit = {
    "checks": [
        {
            "name": "结构完整性",
            "test": "structure_intact",
            "items": ["headings", "tables", "lists", "links", "images"]
        },
        {
            "name": "内容完整性",
            "test": "content_completeness",
            "min_ratio": 0.95          # 内容保留率>=95%
        },
        {
            "name": "格式正确性",
            "test": "markdown_valid",
            "validator": "markdownlint"
        },
        {
            "name": "编码正确性",
            "test": "encoding_correct",
            "expected": "UTF-8"
        },
        {
            "name": "链接有效性",
            "test": "links_valid",
            "check_external": False     # 仅检查内部链接
        }
    ],
    "report_format": "html",
    "auto_fix": True
}
```

**输入**: 用户提供文档质量审计所需的指令和必要参数.
**输出**: 返回文档质量审计的处理结果,包含执行状态码、结果数据和执行日志。### 转换历史与版本管理
```python
# 转换历史管理
history_config = {
    "track_changes": True,
    "version_control": "git",
    "diff_output": True,              # 生成差异对比
    "change_log": "CHANGELOG.md",     # 变更日志
    "rollback": True,                 # 支持回滚
    "metadata_db": "conversions.db"   # 转换记录数据库
}
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `文档质量审计` 选项

#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:企业文档库数字化
需求:企业需要将历史文档库(数千文件)批量转为Markdown.
```bash
# 批量转换企业文档库
python3 batch_convert.py \
  --input /company/documents/ \
  --output /company/markdown/ \
  --recursive \
  --formats "pdf,docx,pptx,xlsx" \
  --parallel 16 \
  --template enterprise-template.yml \
  --extract-metadata \
  --quality-check \
  --generate-index \
  --preserve-structure
```

输出结构:

```
company/markdown/
├── index.md                    # 文档索引
├── reports/
│   ├── 2024-q1-report.md
│   └── 2024-q2-report.md
├── presentations/
│   ├── product-launch.md
│   └── annual-review.md
├── spreadsheets/
│   ├── budget-2024.md
│   └── sales-data.md
├── audit/
│   ├── quality-report.html
│   └── conversion-log.json
└── metadata/
    └── documents.db
```

### 场景二:团队知识库建设
需求:技术团队需要将各类文档统一转为Markdown建立知识库.
```python
# 知识库建设配置
knowledge_base = {
    "sources": [
        {"type": "directory", "path": "./docs/", "category": "技术文档"},
        {"type": "directory", "path": "./wiki/", "category": "团队Wiki"},
        {"type": "directory", "path": "./meetings/", "category": "会议记录"},
        {"type": "directory", "path": "./designs/", "category": "设计文档"}
    ],
    "output": "./knowledge-base/",
    "template": "knowledge-base-template.yml",
    "features": {
        "auto_categorize": True,       # 自动分类
        "extract_metadata": True,      # 元数据提取
        "generate_index": True,        # 生成索引
        "full_text_search": True,     # 全文搜索
        "cross_references": True       # 交叉引用
    }
}
```

### 场景三:技术文档自动化处理
需求:将API文档、设计文档等自动转为Markdown并集成到文档站.
```bash
# CI/CD集成的文档处理
python3 process_docs.py \
  --input ./source-docs/ \
  --output ./docs/content/ \
  --template docs-template.yml \
  --validate \
  --generate-search-index \
  --deploy-preview
```

## 使用流程

### 步骤一:初始化转换项目
```bash
python3 init_project.py \
  --name "DocumentConversion" \
  --input ./source/ \
  --output ./output/ \
  --template output-template.yml
```

### 步骤二:配置批量转换
```bash
python3 batch_convert.py \
  --config conversion-config.yml \
  --parallel 8 \
  --quality-check
```

### 步骤三:生成索引与审计
```bash
# 生成文档索引
python3 generate_index.py \
  --input ./output/ \
  --format "html,markdown" \
  --searchable
# ...
# 质量审计
python3 audit_conversion.py \
  --input ./output/ \
  --report ./audit/
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | markdown-converter处理的内容输入 |,  |
| content | string | 否 | markdown-converter处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "converter 相关配置参数",
    result: "converter 相关配置参数",
    result: "converter 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md规范的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.10+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| uv/uvx | 工具 | 必需 | astral.sh安装 |
| markitdown | Python包 | 必需 | uvx自动安装 |
| markdownlint | 工具 | 推荐 | npm install markdownlint-cli |
| Git | 版本控制 | 推荐 | git-scm.com |

### API Key 配置
- 本Skill基于指令驱动驱动,基础LLM由Agent平台提供
- 基础转换使用本地工具,无需云端服务
- 如使用Azure文档智能,需配置Azure端点与API Key
- 企业版支持密钥管理与轮换

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行批量文档转换任务,通过Python脚本实现目录扫描、质量审计与CI/CD集成
- **PRO版增强**: 批量转换、自定义模板、元数据提取、质量审计、索引生成、版本管理、CI/CD集成

## 案例展示

### 企业级转换配置
```yaml
# enterprise-conversion.yml
project:
  name: "企业文档数字化"
  version: "1.0.0"
# ...
input:
  directories:
    - path: "./documents/"
      recursive: true
      formats: ["pdf", "docx", "pptx", "xlsx"]
  exclude:
    - "*.tmp"
    - "*.bak"
    - "temp/"
# ...
output:
  directory: "./markdown/"
  preserve_structure: true
  encoding: "UTF-8"
# ...
template:
  file: "enterprise-template.yml"
  frontmatter: true
  metadata: true
# ...
processing:
  parallel_workers: 16
  skip_existing: true
  quality_check: true
  extract_metadata: true
# ...
index:
  generate: true
  format: "html"
  searchable: true
  categories: true
# ...
audit:
  enabled: true
  checks: ["structure", "completeness", "format", "encoding"]
  report: "html"
  auto_fix: true
```

### CI/CD集成
```yaml
# .github/workflows/doc-conversion.yml
name: Document Conversion
on:
  push:
    paths: ["source-docs/**"]
  schedule:
    - cron: "0 2 * * *"  # 每日凌晨2点
jobs:
  convert:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Install uv
        run: pip install uv
      - name: Batch Convert Documents
        run: |
          python3 batch_convert.py \
            --input ./source-docs/ \
            --output ./docs/ \
            --parallel 8 \
            --quality-check \
            --generate-index
      - name: Quality Audit
        run: |
          python3 audit_conversion.py \
            --input ./docs/ \
            --report ./audit/
      - name: Upload Documents
        uses: actions/upload-artifact@v3
        with:
          name: markdown-docs
          path: ./docs/
```

## 常见问题

### Q1: 如何从免费版迁移至PRO版?
A: PRO版完全兼容免费版。现有的转换命令与选项可直接使用。安装PRO版增强包即可启用批量处理、模板与审计功能.
### Q2: 批量转换时如何处理大文件?
A: PRO版支持大文件分块处理,自动跳过内存不足的文件并记录到错误日志。可通过`--max-file-size`参数限制单文件大小.
### Q3: 如何自定义输出格式?
A: 使用自定义模板文件(`--template`),可定义header、body、footer结构与元数据字段。模板支持变量插值.
### Q4: 转换历史如何管理?
A: PRO版自动记录每次转换的元数据(源文件、时间、格式、质量分等),存储在数据库中。支持差异对比与版本回滚.
### Q5: 支持哪些CI/CD平台?
A: 支持GitHub Actions、GitLab CI、Jenkins等主流CI/CD平台。提供标准命令行接口与配置文件,易于集成到任意流水线.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

