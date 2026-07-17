---
slug: file-organizer-zh
name: file-organizer-zh
version: "1.0.0"
displayName: File Organizer
summary: 文件整理器，按类型自动分类（中文版）
license: MIT
description: |-
  文件整理器，按类型自动分类（中文版）

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 中文版, 按类型自动分, 文件整理器, file, organizer
tags:
- Other
tools:
- read
- exec
---

# File Organizer

自动按类型分类整理文件。

## 功能

1. **按类型分类** - 图片/文档/代码/视频/音频/压缩包
2. **智能归类** - 根据文件内容智能分类
3. **清理重复** - 识别并清理重复文件

## 触发关键词

* 整理
* 分类
* 整理文件
* 分类文件

## 文件类型映射

* images: .jpg, .jpeg, .png, .gif, .bmp, .webp, .svg
* documents: .doc, .docx, .pdf, .txt, .md, .xls, .xlsx, .ppt, .pptx
* code: .js, .ts, .py, .java, .cpp, .c, .html, .css, .json
* videos: .mp4, .avi, .mov, .wmv, .flv
* audio: .mp3, .wav, .flac, .aac, .ogg
* archives: .zip, .rar, .7z, .tar, .gz

## 使用示例

* "整理 D:\Downloads"
* "分类 C:\Users\Documents"
* "整理桌面"

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
