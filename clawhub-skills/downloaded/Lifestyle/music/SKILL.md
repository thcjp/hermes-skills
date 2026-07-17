---
slug: music
name: music
version: "1.0.0"
displayName: Music
summary: Build a personal music system for tracking discoveries, favorites, concerts,
  and listening memories.
license: MIT
description: |-
  Build a personal music system for tracking discoveries, favorites, concerts,
  and listening memories.

  核心能力:

  - 生活工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 个人健康、生活管理、习惯养成

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: personal, system, build, tracking, music
tags:
- Lifestyle
tools:
- read
- exec
---

# Music

## Core Behavior

* User shares song/album → offer to save with context
* User asks for music → check their saved collection first
* User mentions concert → track in events
* Create `~/music/` as workspace

## File Structure

```text
~/music/
├── discover/
│   └── to-listen.md
├── favorites/
│   ├── songs.md
│   ├── albums.md
│   └── artists.md
├── playlists/
│   ├── workout.md
│   ├── focus.md
│   └── road-trip.md
├── concerts/
│   ├── upcoming.md
│   └── attended/
├── collection/
│   └── vinyl.md
└── memories/
    └── 2024.md
```

## Discovery Queue

```markdown
## Albums
- Blonde — Frank Ocean (recommended by Jake)
- Kid A — Radiohead (classic I never explored)

## Artists to Explore
- Japanese Breakfast — heard one song, dig deeper
- Khruangbin — background music recs
```

## Favorites Tracking

```markdown
## All-Time
- Purple Rain — Prince
- Pyramids — Frank Ocean
- Paranoid Android — Radiohead

## Current Rotation
- [updates frequently]

## Perfect Front to Back
- Abbey Road — The Beatles
- Channel Orange — Frank Ocean
- In Rainbows — Radiohead
```

## Playlists by Context

```markdown
## For Deep Work
- Brian Eno — Ambient 1
- Tycho — Dive
- Bonobo — Black Sands

## Why These Work
Instrumental, steady tempo, no lyrics distraction
```

## Concert Tracking

```markdown
- Khruangbin — May 15, Red Rocks — tickets bought
- Tame Impala — TBD, watching for dates

## Date
July 2018, Madison Square Garden

## Highlights
- Everything in Its Right Place opener
- Idioteque crowd energy

## Notes
Best live show ever, would see again anywhere
```

## Physical Collection

```markdown
## Own
- Dark Side of the Moon — Pink Floyd
- Rumours — Fleetwood Mac

## Want
- Kind of Blue — Miles Davis
- Vespertine — Björk
```

## Music Memories

```markdown
## Summer Soundtrack
- Brat — Charli XCX
- GNX — Kendrick

## Discovery of the Year
Japanese Breakfast — finally clicked
```

## By Mood/Activity

* Workout: high energy, tempo 120+
* Focus: instrumental, ambient, lo-fi
* Cooking: upbeat, familiar favorites
* Sad hours: cathartic, emotional
* Party: crowd-pleasers, danceable
* Road trip: singalongs, classics

## What To Surface

* "You saved that album 3 months ago, still unlistened"
* "Artist you like is touring near you"
* "Last time you needed focus music you liked Tycho"
* "This sounds like artists in your favorites"

## Artist Deep Dives

When user discovers artist they love:

* Map discography chronologically
* Note fan-favorite albums
* Flag essential tracks for sampling
* Track which albums explored vs pending

## What To Track Per Entry

* Song/album/artist name
* How discovered (who, where, when)
* Context (mood it fits, activity)
* Rating after listening
* Standout tracks on albums

## Progressive Enhancement

* Week 1: list current favorite songs/albums
* Ongoing: save discoveries with source
* Build mood-based playlists over time
* Log concerts attended

## What NOT To Do

* Assume streaming platform integration
* Push genres they don't enjoy
* Over-organize — simple lists work
* Forget to ask what they're in the mood for

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
