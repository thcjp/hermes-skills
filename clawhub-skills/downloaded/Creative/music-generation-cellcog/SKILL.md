---
slug: music-generation-cellcog
name: music-generation-cellcog
version: "1.0.11"
displayName: Music Generation Cel
summary: "CellCog驱动AI音乐生成,原创器乐与人声5秒到10分钟(社区下载版)"
  5 seconds to 10 m...
license: MIT-0
description: |-
  AI music generation powered by CellCog。Original instrumental and vocal
  tracks, 5 seconds to 10 m。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Music Generation Cellcog

Music generation — 5 seconds to 10 minutes. Instrumental and vocal tracks with high-quality AI vocals.

Generated tracks are royalty-free for commercial use per CellCog's terms of service — YouTube, podcasts, apps, games, ads, films, streaming.

## How to Use

For your first CellCog task in a session, read the **cellcog** skill for the full SDK reference — file handling, chat modes, timeouts, and more.

**Skill平台 (fire-and-forget):**

```python
result = client.create_chat(
    prompt="[your task prompt]",
    notify_session_key="agent:main:main",
    task_label="my-task",
    chat_mode="agent",
)
```

**All agents except Skill平台 (blocks until done):**

```python
from cellcog import CellCogClient
client = CellCogClient(agent_provider="skill-platform|cursor|claude-code|codex|...")
result = client.create_chat(
    prompt="[your task prompt]",
    task_label="my-task",
    chat_mode="agent",
)
print(result["message"])
```

---

## Two Ways to Create Music

### Simple Prompt (Use This 99% of the Time)

Just describe what you want. The model handles the rest — genre, arrangement, instrumentation, dynamics, and even lyrics:

> "Compose a 90-second cinematic score. Start with solo piano, layer in strings at 30 seconds, build to a full orchestral swell, then resolve softly. Mood: bittersweet turning hopeful."

> "Create a 3-minute lo-fi hip-hop track with soft piano, vinyl crackle, and mellow drums. 75 BPM. Study vibes."

> "Write a 2-minute upbeat pop song with female vocals about starting fresh on a Monday morning. Catchy chorus, feel-good energy."

The model is exceptionally sophisticated — it handles any genre, genre fusion, songs with lyrics, complex arrangements, and mood transitions from a simple description.

### Composition Plan (For Precise Timing Control)

Only use this when you need **exact section durations** — for example, syncing music to specific video segments or presentation slides:

> "I need music that syncs with my video:
>
> * Intro: exactly 10 seconds, soft ambient
> * Build: exactly 20 seconds, energy rising
> * Climax: exactly 15 seconds, full orchestra
> * Outro: exactly 10 seconds, gentle fade"

This mode gives precise timing control per section but should only be used when timing accuracy matters for syncing with other media.

---

## What Music You Can Create

### Instrumental

| Type | Example |
| --- | --- |
| **Cinematic scores** | Epic orchestral, tense thriller, emotional piano, sci-fi ambient |
| **Background tracks** | Lo-fi beats, corporate background, cafe jazz, ambient soundscapes |
| **Podcast intros/outros** | 5-10 second branded stings, transitions, bumpers |
| **Game soundtracks** | Battle themes, exploration music, boss fights, menu themes |
| **Jingles** | Ad jingles, notification sounds, reveal stingers |
| **Ambient** | Meditation, nature soundscapes, focus music |

### Vocal Tracks

CellCog generates songs with **perfect AI vocals** — just describe the lyrical theme:

| Type | Example |
| --- | --- |
| **Pop songs** | Catchy hooks, verse-chorus structure, radio-ready |
| **Ballads** | Emotional, piano-driven, storytelling |
| **Hip-hop/Rap** | Rhythmic vocals, beats, flow |
| **Rock** | Guitar-driven, powerful vocals |
| **R&B/Soul** | Smooth, melodic, groove |

---

## Specs

| Parameter | Range |
| --- | --- |
| **Duration** | 5 seconds to 10 minutes |
| **Output** | MP3 (44.1kHz, 128kbps) |
| **Vocals** | Instrumental or with AI vocals |
| **Licensing** | Royalty-free per CellCog terms of service |

---

## Chat Mode

**Use `chat_mode="agent"`** for music generation. Music executes well in agent mode.

---

## 示例

**Cinematic score:**

> "Compose a 2-minute cinematic score for a nature documentary finale. Begin with solo cello (melancholic), layer in strings and piano at 40 seconds, build to a hopeful orchestral swell, resolve with gentle piano. Think Planet Earth meets Interstellar."

**Lo-fi background:**

> "Create 5 minutes of lo-fi study beats. Soft piano, mellow drums, vinyl crackle, gentle bass. 75 BPM. Warm and unobtrusive — good for focus."

**Podcast intro + outro:**

> "Create a podcast intro (8 seconds) and outro (6 seconds). Show is a tech startup podcast. Intro: energetic, modern electronic with a hook. Outro: same vibe but mellower wind-down. Should feel like the same show."

**Song with vocals:**

> "Write a 3-minute upbeat indie pop song with female vocals. Theme: the excitement of moving to a new city. Catchy chorus, acoustic guitar foundation, builds with drums and synth. Feel-good, sing-along energy."

**Game soundtrack:**

> "Compose a 2-minute boss battle theme for a fantasy RPG. Intense orchestral with choir, driving percussion, escalating tension. Think Dark Souls meets Final Fantasy."

---

## Tips

1. **Describe the feeling, not just the genre**: "Music that makes a startup pitch feel like the future" works better than "electronic music."
2. **Specify duration**: "45 seconds" vs "3 minutes" changes composition structure significantly.
3. **Reference moods, not copyrighted songs**: "Hans Zimmer-style epic" and "ChilledCow lo-fi vibes" work well. Do not reference specific copyrighted songs.
4. **For vocals**: Set the lyrical theme and mood. The model writes lyrics that fit. Or provide specific lyrics you want sung.
5. **Energy arc matters**: "Starts quiet, builds at midpoint, resolves softly" gives clear compositional structure.
6. **For video background music**: If the music is for a CellCog video, mention it in your video prompt instead — CellCog handles music as part of video production automatically.

---

## If CellCog is not installed

Run `/cellcog-setup` (or `/cellcog:cellcog-setup` depending on your tool) to install and authenticate.
**Skill平台 users:** Run `* 安装此Skill请参考SkillHub平台指南
**Manual setup:** `pip install -U cellcog` and set `CELLCOG_API_KEY`. See the **cellcog** skill for SDK reference.

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

- AI music generation powered by CellCog
- Original instrumental and vocal
  tracks, 5 seconds to 10 m
- 触发关键词: powered, original, cellcog, generation, music

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Music Generation Cel？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Music Generation Cel有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
