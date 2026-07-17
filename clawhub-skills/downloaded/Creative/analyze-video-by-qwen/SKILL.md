---
slug: analyze-video-by-qwen
name: analyze-video-by-qwen
version: "1.0.1"
displayName: analyze video by qwen
summary: 使用 Qwen 3.5 Plus 模型分析视频内容，支持本地文件和远程 URL，可自定义分析提示词和抽帧频率
license: MIT-0
description: |-
  使用 Qwen 3.5 Plus 模型分析视频内容，支持本地文件和远程 URL，可自定义分析提示词和抽帧频率

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 模型分析视频, 支持本地文件, 和远程, 使用, qwen, video, 内容, analyze
tags:
- Creative
tools:
- read
- exec
---

# analyze video by qwen

## Overview

使用阿里云 Qwen 3.5 Plus 多模态模型对视频进行智能分析。支持本地视频文件和远程 URL，可自定义分析问题和视频抽帧频率（FPS）。

## 何时使用

* 需要理解视频内容、场景描述
* 需要视频中的动作识别、物体检测
* 需要生成视频摘要或分析报告
* 需要分析远程在线视频

## 快速用法

### 分析本地视频

默认设置分析视频：

```bash
python scripts/analyze.py /path/to/video.mp4
```

自定义提示词：

```bash
python scripts/analyze.py /path/to/video.mp4 --prompt "请详细描述视频中的每个场景"
```

自定义抽帧频率（FPS越高，分析越精细）：

```bash
python scripts/analyze.py /path/to/video.mp4 --fps 5
```

### 分析远程视频 URL

直接分析远程视频：

```bash
python scripts/analyze.py https://example.com/video.mp4
```

组合使用：

```bash
python scripts/analyze.py /path/to/video.mp4 --fps 3 --prompt "视频中出现了哪些人物和物体？"
python scripts/analyze.py https://example.com/video.mp4 --fps 4 --prompt "请详细描述视频场景"
```

## 参数说明

| 参数 | 说明 | 默认值 | 必填 |
| --- | --- | --- | --- |
| `video_source` | 视频文件路径或远程 URL（支持 http/https） | - | 是 |
| `--fps` | 抽帧频率，每秒抽取的帧数 | 2 | 否 |
| `--prompt` | 分析提示词 | "这段视频描绘的是什么景象？" | 否 |

## 配置

API Key 从 `~/.skill-platform/skill-platform.json` 的 `skills.dashscope.apiKey` 字段读取。

如未配置，请添加以下内容：

```json
{
  "skills": {
    "dashscope": {
      "apiKey": "your-dashscope-api-key"
    }
  }
}
```

## 备注

* 本地视频路径可以是绝对路径或相对路径
* 远程视频 URL 必须是可公开访问的直链
* FPS 越高，API 调用成本越高，建议根据视频长度和需求调整

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
