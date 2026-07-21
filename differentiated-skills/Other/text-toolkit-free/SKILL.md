---
slug: text-toolkit-free
name: text-toolkit-free
version: "1.0.0"
displayName: 文本处理工具免费版
summary: 提供编码校验、空白清理、格式检测与快速变换的文本处理工具，适合个人开发日常。
license: Proprietary
edition: free
description: |-
  文本处理工具免费版，面向个人开发者的轻量级文本变换与清理工具。核心能力:
  - 编码识别与 BOM/换行符规范化
  - 空白字符清理与智能引号归一化
  - 格式检测（CSV/TSV/分隔符识别）
  - 常用快速变换（大小写、去重、提取邮箱/URL）

  适用场景:
  - 数据清洗前的格式预处理
  - 跨平台文本文件的换行符统一
  - 日常开发中的快速文本变换

  差异化: 免费版聚焦核心文本清理与变换能力，去除所有外部平台与作者引用，强化中文本地化与触发关键词，适合个人用户零成本上手
tags:
- 文本处理
- 数据清洗
- 编码规范
- 免费版
tools:
  - - read
- exec
---

# 文本处理工具（免费版）

## 概述

文本处理工具免费版聚焦日常开发中最常见的文本变换与清理任务。提供编码校验、空白清理、格式检测与快速变换四大核心能力，帮助你把杂乱的文本快速整理为可解析、可入库的结构。

## 核心能力

| 能力 | 说明 |
|:-----|:-----|
| 编码校验 | 识别文件编码，规范化 BOM 与换行符 |
| 空白清理 | 折叠多余空格、修剪首尾空白、归一化智能引号 |
| 格式检测 | 识别 CSV/TSV/管道/分号等分隔符 |
| 快速变换 | 大小写、去重、提取邮箱/URL、统计词频 |

## 使用场景

### 场景一：跨平台换行符统一

从 Windows 同事处收到 CRLF 文件，需要统一为 LF。

```bash
# 识别当前编码与换行符
file -bi document.txt
cat -A document.txt | head -1

# 规范化换行符
tr -d '\r' < document.txt > document-clean.txt

# 移除 BOM（若存在）
sed -i '1s/^\xEF\xBB\xBF//' document-clean.txt
```

### 场景二：CSV 文件预处理

拿到一份来源不明的 CSV，需要先识别分隔符再处理。

```bash
# 检测分隔符（统计逗号、分号、制表符、管道符数量）
head -1 data.csv | tr -cd ',;\t|' | fold -1 | sort | uniq -c

# 折叠多余空格
sed 's/[[:space:]]\+/ /g' data.csv > data-trimmed.csv

# 修剪首尾空白
sed 's/^[[:space:]]*//;s/[[:space:]]*$//' data-trimmed.csv > data-clean.csv
```

### 场景三：从日志中提取邮箱与 URL

```bash
# 提取所有邮箱
grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' access.log > emails.txt

# 提取所有 URL
grep -oE 'https?://[^[:space:]<>"]+' access.log > urls.txt

# 去重并排序
sort -u emails.txt -o emails-unique.txt
sort -u urls.txt -o urls-unique.txt
```

## 快速开始

```bash
# 1. 编码校验
file -I document.txt

# 2. 快速变换参考
echo "Hello WORLD" | tr '[:upper:]' '[:lower:]'      # 转小写
echo "Hello,World" | tr -d '[:punct:]'                # 去标点
wc -w document.txt                                    # 统计词数
sort document.txt | uniq -d                           # 查找重复行
```

## 示例

免费版通过命令行参数配置，无需配置文件：

```bash
# 常用命令速查
| 任务           | 命令                                          |
|:---------------|:---------------------------------------------|
| 转小写         | tr '[:upper:]' '[:lower:]'                   |
| 去标点         | tr -d '[:punct:]'                            |
| 统计词数       | wc -w                                        |
| 统计唯一行     | sort -u \| wc -l                             |
| 查找重复行     | sort \| uniq -d                              |
| 提取邮箱       | grep -oE '[a-zA-Z0-9._%+-]+@...'             |
| 折叠多余空格   | sed 's/[[:space:]]\+/ /g'                    |
| 修剪首尾空白   | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'    |
```

## 最佳实践

* 处理前先用 `file -I` 确认编码，避免乱码。
* 智能引号（`"` `"`）会破坏解析器，先归一化为 `"`。
* 零宽字符不可见但会破坏比较，处理前先剥离。
* UTF-8 下字符串长度不等于字节长度（`"café"` = 4 字符，5 字节）。
* 处理结构化文本前，先识别分隔符再写解析逻辑。

## 常见问题

**Q：免费版支持正则替换吗？**
A：支持基础的正则替换（通过 `sed`），但不支持高级回溯引用。如需复杂正则与多文件批处理，请考虑 PRO 版本。

**Q：可以处理 GBK/GB2312 编码的文件吗？**
A：可以识别，但转换编码需要系统安装 `iconv`。免费版提供识别能力，编码转换建议在 PRO 版本中使用批量工具。

**Q：免费版支持多文件批处理吗？**
A：免费版面向单文件处理。如需多文件批量变换与流水线编排，请使用 PRO 版本。

**Q：处理大文件会卡顿吗？**
A：免费版基于流式命令行工具，可处理 GB 级文件。但复杂正则在超大文件上可能较慢。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **命令行工具**: grep, sed, tr, sort, uniq（系统自带）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| coreutils | 系统工具 | 必需 | 系统自带 |
| iconv | 工具 | 可选 | 系统包管理器安装 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令 + 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行文本处理任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
