---
slug: chromecast-control
name: chromecast-control
version: "1.0.0"
displayName: Control Chromecast
summary: Control Chromecast devices on your local network - discover, cast media,
  control playback, manage...
license: MIT
description: |-
  Control Chromecast devices on your local network - discover, cast media,
  control playback, manage...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: local, control, chromecast, devices
tags:
- Creative
tools:
- read
- exec
---

# Control Chromecast

Control Chromecast and Google Cast-enabled devices on your local network using `catt` (Cast All The Things).

## Quick Reference

| Command | Description |
| --- | --- |
| `catt scan` | Find all Chromecasts on network |
| `catt cast <url>` | Cast video/audio |
| `catt pause` / `play` | Pause/resume |
| `catt stop` | Stop playback |
| `catt status` | Current playback info |
| `catt volume <0-100>` | Set volume |

Use `-d <device>` to target a specific device by name or IP.

## Discovery & Device Management

```bash
catt scan

catt -d "Living Room TV" set_default

catt -d 192.168.1.163 set_alias tv

catt -d tv del_alias
catt del_default
```

## Casting Media

### Basic Casting

```bash
catt cast "https://www.youtube.com/watch?v=VIDEO_ID"

catt cast ./video.mp4

catt cast_site "https://example.com"
```

### Advanced Cast Options

```bash
catt cast -s ./subtitles.srt ./video.mp4

catt cast -t 01:30:00 "https://youtube.com/watch?v=VIDEO_ID"

catt cast -r "https://youtube.com/playlist?list=PLAYLIST_ID"

catt cast -n "https://youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID"

catt cast --no-subs ./video.mp4

catt cast -y format=best "https://youtube.com/watch?v=VIDEO_ID"

catt cast -b "https://example.com/video.mp4"
```

## Playback Control

```bash
catt play              # Resume playback
catt pause             # Pause playback
catt play_toggle       # Toggle play/pause
catt stop              # Stop playback completely
catt skip              # Skip to end of content

catt seek 300          # Jump to 5 minutes (seconds)
catt seek 01:30:00     # Jump to 1h 30m (HH:MM:SS)
catt ffwd 30           # Fast forward 30 seconds
catt rewind 30         # Rewind 30 seconds
```

## Volume Control

```bash
catt volume 50         # Set volume to 50%
catt volumeup 10       # Increase by 10
catt volumedown 10     # Decrease by 10
catt volumemute on     # Mute
catt volumemute off    # Unmute
```

## Queue Management (YouTube)

```bash
catt add "https://youtube.com/watch?v=VIDEO_ID"

catt add -n "https://youtube.com/watch?v=VIDEO_ID"

catt remove "https://youtube.com/watch?v=VIDEO_ID"

catt clear
```

## State Management

```bash
catt save

catt restore
```

## Device Information

```bash
catt status    # Brief: time, volume, mute status
catt info      # Full: title, URL, player state, media type, etc.
```

## Configuration

Config file: `~/.config/catt/catt.cfg`

```ini
[options]
device = Living Room TV

[aliases]
tv = Living Room TV
bedroom = Bedroom Speaker
```

## Network Requirements

* Chromecast and computer must be on same network
* For local file casting: TCP ports 45000-47000 must be open
* Some networks block mDNS - use IP address directly if `catt scan` fails

## Supported Sources

Catt uses yt-dlp internally, supporting:

* YouTube (videos, playlists, live streams)
* Vimeo, Dailymotion, Twitch
* Direct video URLs (MP4, MKV, WebM, etc.)
* Local files (video, audio, images)
* Hundreds more sites (see yt-dlp supported sites)

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
