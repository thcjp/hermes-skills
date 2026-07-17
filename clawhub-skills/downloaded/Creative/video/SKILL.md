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
  format conversion, captioni...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: edit, video, optimize, platform, process, videos
tags:
- Creative
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
