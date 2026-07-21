---
slug: ace-music
name: ace-music
version: "1.0.0"
displayName: Ace Music
  using ACE-Step 1.5. Full songs with vocals, lyrics, any genre, any language. No
  subscription, no credits, no limits. The open-source Suno alternative, powered by
  ACE Music's free API.
summary: Generate AI music using ACE-Step 1.5 via ACE Music's free API. Use when the
  user asks to create, ...
license: MIT
description: |-
  Generate AI music using ACE-Step 1。5 via ACE Music's free API。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Creative
tools:
  - - read
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

- Generate AI music using ACE-Step 1
- 5 via ACE Music's free API
- Use
  when the user asks to create,
- 触发关键词: full, alternative,, open-source, step, limits
- , ace-step, songs, music''s'

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

### Q1: 如何开始使用Ace Music？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Ace Music有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
