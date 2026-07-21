---
slug: file-auto-organizer
name: file-auto-organizer
version: "1.0.0"
displayName: File Auto Organizer
summary: 文件自动整理工具。按文件类型、日期自动归类下载文件夹，适合整理控和洁癖用户。
license: MIT-0
description: |-
  文件自动整理工具。按文件类型、日期自动归类下载文件夹，适合整理控和洁癖用户。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。
tags:
- Other
tools:
  - - read
- exec
---

# File Auto Organizer

自动整理文件夹，按类型/日期归类文件，告别凌乱桌面！

## 功能

* 📂 按文件类型自动归类（图片、文档、视频、压缩包等）
* 📅 按日期整理（今天、昨天、本周等）
* 🔍 支持自定义规则
* 🗑️ 可选：删除重复文件
* 📊 整理报告

## 使用方法

### 整理下载文件夹

```bash
python3 scripts/organizer.py organize ~/Downloads
```

### 按类型整理

```bash
python3 scripts/organizer.py by-type ~/Downloads
```

### 按日期整理

```bash
python3 scripts/organizer.py by-date ~/Downloads
```

### 查看统计

```bash
python3 scripts/organizer.py stats ~/Downloads
```

## 规则说明

默认类型分类：

* 🖼️ 图片: jpg, png, gif, webp, svg, psd, ai
* 📄 文档: pdf, doc, docx, txt, md, xls, xlsx, ppt, pptx
* 📦 压缩包: zip, rar, 7z, tar, gz
* 🎬 视频: mp4, mkv, avi, mov, flv
* 🎵 音频: mp3, wav, flac, aac
* 💻 代码: js, py, java, cpp, html, css

## 示例

```bash
python3 scripts/organizer.py organize ~/Desktop

python3 scripts/organizer.py organize ~/Downloads --report
```

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

* 📂 按文件类型自动归类（图片、文档、视频、压缩包等）
* 📅 按日期整理（今天、昨天、本周等）
* 🔍 支持自定义规则
* 🗑️ 可选：删除重复文件
* 📊 整理报告

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用File Auto Organizer？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: File Auto Organizer有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
