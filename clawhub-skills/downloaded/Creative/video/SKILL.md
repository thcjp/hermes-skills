---
slug: video
name: video
version: "1.0.1"
displayName: Video
summary: Process, edit, and optimize videos for any platform with compression, format
  conversion, captioni...
license: MIT
description: |-
  Process, edit, and optimize videos for any platform with compression,
  format conversion, captioni。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
---

# Video

## Requirements

**Required:**

* `ffmpeg` / `ffprobe` — core video processing

**Optional:**

* `whisper` — local transcription for captions
* `realesrgan` — AI upscaling

## Quick Reference

| Situation | Load |
| --- | --- |
| Platform specs (YouTube, TikTok, Instagram) | `platforms.md` |
| FFmpeg commands by task | `commands.md` |
| Quality/compression settings | `quality.md` |
| Workflow by use case | `workflows.md` |

## Core Capabilities

| Task | Method |
| --- | --- |
| Convert/compress | FFmpeg (see `commands.md`) |
| Generate captions | Whisper → SRT/VTT |
| Change aspect ratio | Crop, pad, or smart reframe |
| Clean audio | Normalize, denoise, enhance |
| Batch operations | Process entire folders in one run |

## Execution Pattern

1. **Clarify target** — What platform? What format? File size limit?
2. **Check source** — `ffprobe` for codec, resolution, duration, audio
3. **Process** — FFmpeg for transformation
4. **Verify** — Confirm output meets specs before delivering
5. **Deliver** — Provide file to user

## Common Requests → Actions

| User says | Agent does |
| --- | --- |
| "Make this work for TikTok" | Reframe to 9:16, check duration ≤3min, compress |
| "Add subtitles" | Whisper → SRT → burn-in or deliver separately |
| "Compress for WhatsApp" | Target <64MB, H.264, AAC |
| "Extract audio" | `-vn -acodec mp3` or `-acodec copy` |
| "Make a GIF" | Extract frames, optimize palette, loop |
| "Split into clips" | Cut at timestamps with `-ss` and `-t` |

## Quality Rules

* **Always re-encode audio to AAC** for maximum compatibility
* **Use `-movflags +faststart`** for web playback
* **CRF 23** is good default for H.264 (lower = better, bigger)
* **Check before delivering** — verify duration, file size, playability

## Platform Quick Reference

| Platform | Aspect | Max Duration | Max Size |
| --- | --- | --- | --- |
| TikTok | 9:16 | 3 min | 287MB |
| Instagram Reels | 9:16 | 90s | 250MB |
| YouTube Shorts | 9:16 | 60s | No limit |
| YouTube | 16:9 | 12h | 256GB |
| WhatsApp | Any | 3 min | 64MB |

## Scope

This skill:

* Processes video files user explicitly provides
* Runs FFmpeg commands on user request
* Does NOT access files without user instruction
* Does NOT upload to external services automatically

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

- Process, edit, and optimize videos for any platform with compression,
  format conversion, captioni
- 触发关键词: edit, video, optimize, platform, process, videos

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Video？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Video有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
