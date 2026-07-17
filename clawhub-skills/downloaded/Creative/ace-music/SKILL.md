---
slug: ace-music
name: ace-music
version: "1.0.0"
displayName: ACE Music - Free Suno Alternative Generate unlimited AI music for free
  using ACE-Step 1.5. Full songs with vocals, lyrics, any genre, any language. No
  subscription, no credits, no limits. The open-source Suno alternative, powered by
  ACE Music's free API.
summary: Generate AI music using ACE-Step 1.5 via ACE Music's free API. Use when the
  user asks to create, ...
license: MIT
description: |-
  Generate AI music using ACE-Step 1.5 via ACE Music's free API. Use
  when the user asks to create, ...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: full, alternative,, open-source, step, limits., ace-step, songs, music''s'
tags:
- Creative
tools:
- read
- exec
---

# ACE Music - Free Suno Alternative Generate unlimited AI music for free using ACE-Step 1.5. Full songs with vocals, lyrics, any genre, any language. No subscription, no credits, no limits. The open-source Suno alternative, powered by ACE Music's free API.

Generate music via ACE Music's free hosted API (ACE-Step 1.5 model).

## Setup

**API Key** is stored in env `ACE_MUSIC_API_KEY`. If not set:

1. Open <https://acemusic.ai/playground/api-key> in the browser for the user
2. Ask them to sign up (free) and paste the API key
3. Store it: `export ACE_MUSIC_API_KEY=<key>` or add to TOOLS.md

## Quick Generation

Use `scripts/generate.sh` for one-shot generation:

```bash
scripts/generate.sh "upbeat pop song about summer" --duration 30 --output summer.mp3

scripts/generate.sh "gentle acoustic ballad, female vocal" \
  --lyrics "[Verse 1]\nSunlight through the window\n\n[Chorus]\nWe are the dreamers" \
  --duration 60 --output ballad.mp3

scripts/generate.sh "lo-fi hip hop beats, chill, rainy day" --instrumental --duration 120 --output lofi.mp3

scripts/generate.sh "write me a jazz song about coffee" --sample-mode --output jazz.mp3

scripts/generate.sh "rock anthem" --bpm 140 --key "E minor" --language en --seed 42 --output rock.mp3

scripts/generate.sh "electronic dance track" --batch 3 --output edm.mp3
```

Script outputs file path(s) to stdout. Send the file to the user.

## Advanced Usage (curl/direct API)

For covers, repainting, or audio input — see `references/api-docs.md` for full API spec.

Key task types:

* `text2music` (default) — generate from text/lyrics
* `cover` — cover an existing song (requires audio input)
* `repaint` — modify a section of existing audio

## Parameters Guide

| Want | Use |
| --- | --- |
| Specific style | Describe in prompt: "jazz, saxophone solo, smoky bar" |
| Custom lyrics | `--lyrics "[Verse]...[Chorus]..."` |
| AI writes everything | `--sample-mode` |
| No vocals | `--instrumental` |
| Longer songs | `--duration 120` (seconds) |
| Specific tempo | `--bpm 120` |
| Specific key | `--key "C major"` |
| Multiple outputs | `--batch 3` |
| Reproducible | `--seed 42` |
| Non-English vocals | `--language ja` (zh, en, ja, ko, etc.) |

## Notes

* API is **free forever** (confirmed by ACE Music team)
* Base URL: `https://api.acemusic.ai`
* Audio returned as base64 MP3, decoded automatically by the script
* Duration: if omitted, AI decides based on content
* For best results, use tagged mode (prompt + lyrics separated)

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
