---
slug: translate-toolkit-free
name: translate-toolkit-free
version: "1.0.0"
displayName: 翻译工具免费版
summary: 提供格式保留、术语一致与文化适配的文本翻译，支持占位符保护与多语言处理，适合个人日常。
license: MIT
edition: free
description: |-
  翻译工具免费版，面向个人用户的轻量级文本翻译工具。

  核心能力:
  - 格式保留翻译（代码块、HTML、Markdown 结构不变）
  - 占位符保护（{name}、%s、$1 等原样保留）
  - 术语一致性与文化适配
  - 上下文感知与歧义消解

  适用场景:
  - 个人文档与邮件的日常翻译
  - Markdown/HTML 内容的格式保留翻译
  - 多语言学习与对比

  差异化: 免费版聚焦核心翻译与格式保留能力，去除所有外部平台与作者引用，强化中文本地化与触发关键词，适合个人用户零成本上手。

  触发关键词: 翻译, 格式保留, 占位符保护, 术语一致, 文化适配, 多语言, 上下文翻译
tags:
- 翻译
- 本地化
- 格式保留
- 免费版
tools:
- read
- exec
---

# 翻译工具（免费版）

## 概述

翻译工具免费版提供准确的文本翻译，在保留格式、占位符与文化上下文的同时传递原意。支持 Markdown、HTML、JSON 等结构化内容的格式保留翻译，适合个人日常使用。

## 核心能力

| 能力 | 说明 |
|:-----|:-----|
| 格式保留 | 代码块、HTML 标签、Markdown 语法原样保留 |
| 占位符保护 | `{name}`、`{{variable}}`、`%s`、`$1` 等原样保留 |
| 术语一致 | 重复术语保持一致，自动建立术语表 |
| 文化适配 | 习语意译、单位换算、日期/货币格式本地化 |
| 上下文感知 | 根据上下文消解歧义（bank: 银行 vs 河岸） |
| 语言特性 | 正确处理复数、性别、敬语、RTL 文本方向 |

## 使用场景

### 场景一：Markdown 文档翻译

翻译一份技术文档，保留 Markdown 结构。

```text
用户：帮我把这段 Markdown 翻译成英文，保留格式。

输入：
# 项目说明
本项目使用 {framework} 框架，支持 %s 种语言。
请参考 [文档](./docs.md) 了解更多。

输出：
# Project Description
This project uses the {framework} framework and supports %s languages.
Please refer to the [documentation](./docs.md) for more information.
```

### 场景二：JSON 文件本地化

翻译 JSON 文件的值，保留键名。

```text
用户：翻译这个 JSON 文件，只翻译值，保留键。

输入：
{
  "welcome": "欢迎回来，{name}",
  "settings": "设置",
  "save": "保存更改"
}

输出：
{
  "welcome": "Welcome back, {name}",
  "settings": "Settings",
  "save": "Save Changes"
}
```

### 场景三：文化适配翻译

将包含习语与单位的文本翻译为目标语言文化。

```text
用户：把这段话翻译成中文，注意文化适配。

输入：
The meeting is scheduled for July 4th, 2 miles from downtown.
Temperature will be around 85°F. Bring a "piece of cake" for the potluck.

输出：
会议定于 7 月 4 日举行，距离市中心约 3.2 公里。
气温约 29°C。请为聚餐带一份「小菜一碟」级别的甜点（意为简单易做）。
```

## 快速开始

```text
# 纯自然语言驱动，无需命令行操作
# 示例对话：
# 用户: 把这段 Markdown 翻译成英文，保留格式
# 用户: 翻译这个 JSON 文件，只翻译值
# 用户: 把这篇文章翻译成日语，注意文化适配
```

翻译流程：
1. 读取完整上下文理解原意
2. 识别格式标记与占位符
3. 翻译正文内容
4. 校验格式完整性
5. 检查术语一致性

## 配置示例

```text
翻译偏好示例：
- 目标语言: en
- 格式保留: Markdown + HTML + JSON
- 占位符保护: {name}, {{variable}}, %s, $1
- 术语表: 自动建立并保持一致
- 文化适配: 开启（单位换算、日期格式、货币）
- 敬语级别: 根据上下文自动判断
```

## 最佳实践

* 翻译前阅读完整上下文，理解原意再动手。
* 不翻译专有名词、品牌名、技术术语、URL、邮箱地址。
* 不翻译代码片段、CSS 类名、API 端点、文件扩展名。
* 保留数字、日期、ID 的原始格式，除非需要本地化。
* 重复术语保持一致，建立术语表辅助。
* 习语意译而非直译，避免产生歧义。
* 翻译后检查格式元素是否仍然可用。

## 常见问题

**Q：免费版支持术语表导入吗？**
A：免费版自动建立术语表，但不支持导入外部术语表。如需管理大型术语库，请考虑 PRO 版本。

**Q：免费版支持批量文件翻译吗？**
A：免费版面向单文档翻译。如需批量文件翻译与流水线，请使用 PRO 版本。

**Q：可以翻译代码注释吗？**
A：可以，免费版会保留代码结构，仅翻译注释内容。

**Q：翻译质量如何保证？**
A：免费版遵循上下文理解、格式保留、术语一致、文化适配四步质量控制流程。

**Q：支持哪些语言对？**
A：支持所有主流语言对，包括中日英韩、欧洲主要语言、阿拉伯语等 RTL 语言。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行翻译任务
