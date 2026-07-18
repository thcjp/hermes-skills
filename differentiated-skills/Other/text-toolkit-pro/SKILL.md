---
slug: text-toolkit-pro
name: text-toolkit-pro
version: "1.0.0"
displayName: 文本处理工具专业版
summary: 多文件批处理、流水线编排、编码批量转换与自定义变换模板，适合数据团队与内容工程场景。
license: MIT
edition: pro
description: |-
  文本处理工具专业版，面向数据团队与内容工程师的高阶文本处理平台。

  核心能力:
  - 多文件批量变换与流水线编排
  - 编码批量转换（UTF-8/GBK/GB2312/Shift-JIS 等）
  - 自定义变换模板与正则回溯引用
  - 结构化文本解析（CSV/TSV/JSON/XML 互转）
  - 处理报告生成与差异对比

  适用场景:
  - 数据团队的 ETL 前置清洗
  - 多语言内容工程的编码统一
  - 文档批量规范化与质量审计

  差异化: 专业版在免费版核心能力之上扩展批量处理与流水线编排，新增自定义模板、编码批量转换、结构化互转等企业级能力，并与免费版命令兼容。

  触发关键词: 文本处理, 批量变换, 流水线编排, 编码转换, 自定义模板, CSV转JSON, 文本审计, 差异对比
tags:
- 文本处理
- 批量变换
- 数据工程
- 专业版
tools:
- read
- exec
---

# 文本处理工具（专业版）

## 概述

专业版在免费版的编码校验、空白清理、格式检测与快速变换之上，扩展为面向数据团队与内容工程师的完整文本处理平台。支持多文件批量变换、流水线编排、编码批量转换、自定义变换模板与结构化文本互转，同时与免费版的命令行语法保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 文件处理 | 单文件 | 多文件批量 + 递归目录 |
| 编码转换 | 识别为主 | 批量转换（10+ 编码） |
| 正则能力 | 基础 | 回溯引用 + 多模式匹配 |
| 流水线 | 单命令 | 多步骤编排 + 条件分支 |
| 结构化互转 | 不支持 | CSV/TSV/JSON/XML/YAML 互转 |
| 变换模板 | 不支持 | 自定义模板保存与复用 |
| 处理报告 | 不支持 | 自动生成处理报告与差异对比 |
| 并发控制 | 不支持 | 可配置并发数 |

## 使用场景

### 场景一：数据团队 ETL 前置清洗

将多个来源的 CSV 文件统一为 UTF-8 编码并规范化分隔符。

```bash
# 批量将目录下所有 CSV 转为 UTF-8 并统一为逗号分隔
text-pro batch transform \
  --input ./raw-csv/ \
  --output ./clean-csv/ \
  --encoding utf-8 \
  --delimiter "," \
  --recursive

# 处理报告
# ✅ 已处理 128 个文件
# ⚠️ 3 个文件编码异常，已跳过并记录至 report.log
# 📊 总耗时: 12.3s
```

### 场景二：多语言内容工程的编码统一

将日语 Shift-JIS、中文 GBK、韩语 EUC-KR 的文档统一为 UTF-8。

```bash
# 批量编码转换
text-pro batch convert-encoding \
  --input ./multilingual/ \
  --from auto \
  --to utf-8 \
  --backup ./backup/

# 自动检测源编码并转换，保留原始文件备份
```

### 场景三：CSV 与 JSON 互转

将业务系统导出的 CSV 转为 JSON 供 API 消费。

```bash
# CSV 转 JSON（自动推断类型）
text-pro convert csv-to-json \
  --input products.csv \
  --output products.json \
  --infer-types \
  --pretty

# JSON 转 CSV（自定义字段顺序）
text-pro convert json-to-csv \
  --input products.json \
  --output products-export.csv \
  --fields "id,name,price,stock"
```

## 快速开始

```bash
# 1. 初始化专业版工作区
text-pro init --workspace ~/text-pro

# 2. 批量变换
text-pro batch transform --input ./data/ --encoding utf-8 --recursive

# 3. 保存自定义模板
text-pro template save --name "etl-clean" --steps "normalize-newline,strip-bom,fold-spaces,trim"

# 4. 应用模板
text-pro template apply --name "etl-clean" --input ./raw/ --output ./clean/

# 5. 生成处理报告
text-pro report --input ./clean/ --format markdown --output report.md
```

## 配置示例

```yaml
# ~/text-pro/config.yaml
edition: pro
default_encoding: utf-8
batch:
  max_concurrent: 8
  recursive: true
  backup: true
  backup_dir: ./backup
encoding:
  auto_detect: true
  fallback: utf-8
  supported: [utf-8, gbk, gb2312, shift-jis, euc-kr, big5, latin1]
convert:
  csv:
    delimiter: auto
    quote: '"'
    infer_types: true
  json:
    pretty: true
    ensure_ascii: false
pipeline:
  default_steps: [normalize-newline, strip-bom, fold-spaces, trim]
  on_error: skip-and-log
report:
  format: markdown
  include_diff: true
  output: ./reports
```

## 变换模板库

| 模板名 | 步骤 | 适用场景 |
|:-------|:-----|:---------|
| etl-clean | 规范换行 + 去 BOM + 折叠空格 + 修剪 | ETL 前置清洗 |
| csv-normalize | 检测分隔符 + 统一逗号 + 去空行 | CSV 规范化 |
| log-extract | 提取时间戳 + 提取邮箱 + 提取 URL | 日志分析 |
| markdown-tidy | 统一标题层级 + 修剪空格 + 去多余空行 | 文档规范化 |
| custom | 用户自定义 | 专业场景 |

## 最佳实践

* 批量处理前先用 `--dry-run` 预览变换结果，避免误操作。
* 启用 `--backup` 保留原始文件，便于回滚。
* 编码转换优先使用 `auto` 检测，遇到异常时回退到指定编码。
* 自定义模板保存到工作区后可在团队内共享。
* 处理报告包含差异对比，便于审计与质量追溯。

## 常见问题

**Q：专业版与免费版的命令兼容吗？**
A：兼容。免费版的所有命令在专业版中可直接使用，专业版额外提供 `batch`、`convert`、`template` 等子命令。

**Q：批量处理有文件数量上限吗？**
A：无硬性上限，但建议单次不超过 10,000 个文件以保证报告可读性。可通过 `--max-concurrent` 控制并发数。

**Q：支持哪些编码的自动检测？**
A：支持 UTF-8、GBK、GB2312、Shift-JIS、EUC-KR、Big5、Latin1 等常见编码的自动检测与转换。

**Q：自定义模板如何共享给团队？**
A：将模板配置文件放入共享目录，团队成员通过 `template import --path <shared-path>` 导入即可。

**Q：处理报告包含哪些信息？**
A：报告包含处理文件数、成功/失败统计、异常详情、变换前后的差异对比（可选）。

**Q：可以与数据库集成吗？**
A：专业版支持将处理结果导出为 SQL 插入语句，便于导入各类数据库。直接数据库连接建议通过中间文件中转。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（批量与转换功能需要）
- **Python**: 3.9+（结构化互转功能需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方站点下载 |
| Python | 运行时 | 可选 | 官方站点下载 |
| iconv | 工具 | 可选 | 系统包管理器安装 |
| pandas | 库 | 可选 | pip 安装 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）
- 批量处理若调用外部 LLM API，需配置对应的 API Key 环境变量

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令 + 脚本执行能力）
- **说明**: 专业版在 Markdown 指令基础上，提供命令行工具支持批量、转换与模板管理
