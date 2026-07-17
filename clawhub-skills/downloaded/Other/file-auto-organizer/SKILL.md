---
slug: file-auto-organizer
name: file-auto-organizer
version: "1.0.0"
displayName: File Auto Organizer
summary: 文件自动整理工具。按文件类型、日期自动归类下载文件夹，适合整理控和洁癖用户。
license: MIT-0
description: |-
  文件自动整理工具。按文件类型、日期自动归类下载文件夹，适合整理控和洁癖用户。

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: file, 下载文件夹, auto, organizer, 文件自动整理, 工具, 按文件类型, 日期自动归类
tags:
- Other
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
