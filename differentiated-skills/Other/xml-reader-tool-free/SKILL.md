---
slug: xml-reader-tool-free
name: xml-reader-tool-free
version: "1.0.0"
displayName: XML读取器免费版
summary: 快速读取与浏览XML文件结构，支持节点遍历与简单查询，适合个人开发者日常查阅。
license: Proprietary
edition: free
description: |-
  XML读取器工具免费版，面向个人开发者的轻量级XML文件读取与浏览工具。核心能力:
  - XML文件结构与节点遍历
  - 简单 XPath 查询
  - 格式化输出与高亮
  - 节点统计与基本信息

  适用场景:
  - 个人开发者查阅XML配置
  - 快速定位XML中的特定节点
  - 了解XML文件整体结构

  差异化: 免费版聚焦核心读取与浏览能力，去除所有外部平台与作者引用，强化中文本地化与触发关键词，适合个人用户零成本上手
tags:
- XML读取
- 节点遍历
- 配置查阅
- 免费版
tools:
  - - read
- exec
---

# XML读取器工具（免费版）

## 概述

XML读取器工具免费版帮助你快速读取与浏览 XML 文件结构。提供节点遍历、简单 XPath 查询、格式化输出与节点统计能力，适合个人开发者日常查阅 XML 配置与数据。

## 核心能力

| 能力 | 说明 |
|:-----|:-----|
| 节点遍历 | 深度优先/广度优先遍历所有节点 |
| XPath 查询 | 简单 XPath 1.0 查询 |
| 格式化输出 | 缩进、高亮、树形展示 |
| 节点统计 | 元素数量、属性数量、文本长度 |
| 编码识别 | 自动识别文件编码 |

## 使用场景

### 场景一：查看XML文件结构

快速了解 XML 文件的整体结构。

```bash
# 查看结构概览
xml-reader tree config.xml

# 输出
# 📄 config.xml 结构
# <configuration>
#   ├── <appSettings> (3 属性)
#   │   ├── <add key="server" value="localhost"/>
#   │   ├── <add key="port" value="8080"/>
#   │   └── <add key="timeout" value="30"/>
#   ├── <database>
#   │   ├── <connection>...</connection>
#   │   └── <pooling max="10"/>
#   └── <logging level="info"/>
#
# 📊 统计: 8 元素, 5 属性, 4 文本节点
```

### 场景二：XPath查询定位节点

使用 XPath 查询特定节点。

```bash
# 查询所有 add 元素
xml-reader query config.xml --xpath "//add"

# 查询特定属性
xml-reader query config.xml --xpath "//add[@key='server']"

# 输出
# 🔍 XPath 查询结果
# 查询: //add[@key='server']
# 匹配: 1 个节点
#   <add key="server" value="localhost"/>
```

### 场景三：格式化输出

将压缩的 XML 格式化为可读形式。

```bash
# 格式化输出
xml-reader format minified.xml --indent 2 --output formatted.xml

# 输入: <root><child>text</child></root>
# 输出:
# <root>
#   <child>text</child>
# </root>
```

## 快速开始

```bash
# 1. 查看结构
xml-reader tree config.xml

# 2. 查询节点
xml-reader query config.xml --xpath "//target"

# 3. 格式化
xml-reader format config.xml --indent 2

# 4. 统计信息
xml-reader stats config.xml

# 5. 提取文本
xml-reader text config.xml --xpath "//description"
```

## 示例

```bash
# 命令参数说明
| 命令   | 参数              | 说明                |
|:-------|:------------------|:--------------------|
| tree   | <file>            | 显示树形结构        |
| query  | <file> --xpath X  | XPath 查询          |
| format | <file> --indent N | 格式化输出          |
| stats  | <file>            | 显示统计信息        |
| text   | <file> --xpath X  | 提取文本内容        |

# 输出格式选项
--output json     # JSON 格式输出
--output text     # 纯文本输出
--output tree     # 树形展示（默认）
```

## 最佳实践

* 查看结构时先用 `tree` 了解整体布局，再用 `query` 精确定位。
* XPath 查询优先使用具体路径，避免 `//` 全文遍历。
* 格式化时缩进建议 2 空格，兼顾可读性与紧凑性。
* 大文件先看 `stats` 了解规模，再决定查询策略。
* 带命名空间的 XML 查询时注意前缀映射。
* 提取文本时使用 `text` 命令而非 `query`，避免标签干扰。

## 常见问题

**Q：免费版支持修改XML吗？**
A：免费版仅支持读取与查询。如需修改与编辑，请考虑 PRO 版本。

**Q：免费版支持大文件吗？**
A：免费版将整个文件加载至内存，建议文件不超过 50MB。如需流式处理大文件，请使用 PRO 版本。

**Q：XPath 支持哪些语法？**
A：免费版支持 XPath 1.0 基础语法。如需 XPath 2.0+ 高级功能，请使用 PRO 版本。

**Q：支持哪些编码？**
A：自动识别 UTF-8、UTF-16、GBK、Latin1 等常见编码。

**Q：可以导出查询结果吗？**
A：免费版支持输出至终端。如需导出至文件或 JSON，请使用 PRO 版本。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 官方站点下载 |
| xml.etree.ElementTree | 库 | 必需 | Python 标准库 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过命令行工具读取与查询 XML

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
