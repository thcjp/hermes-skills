---
slug: chromecast-control
name: chromecast-control
version: "1.0.0"
displayName: Control Chromecast
summary: "控局域网Chromecast,发现/投屏/播放/音量管理"
  control playback, manage...
license: MIT
description: |-
  Control Chromecast devices on your local network - discover, cast media,
  control playback, manage。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

## 依赖说明

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

## 核心能力

- Control Chromecast devices on your local network - discover, cast media,
  control playback, manage
- 触发关键词: local, control, chromecast, devices

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

### Q1: 如何开始使用Control Chromecast？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Control Chromecast有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步

---
## 边界条件与限制

### 输入限制
- **URL格式**：输入的媒体URL必须遵循正确的格式，例如YouTube视频URL需要包含`v=VIDEO_ID`参数。
- **文件格式**：对于本地文件，支持的格式有限，如MP4, MKV, WebM等，不支持的格式无法投屏。
- **字符限制**：输入的命令和参数长度有限制，超过限制可能导致命令无法执行。

### 性能边界
- **并发投屏**：同一时间只能对一个Chromecast设备进行投屏操作，多设备投屏需要逐一操作。
- **网络延迟**：网络延迟可能影响投屏的流畅性和响应速度，建议在稳定的网络环境下使用。

### 兼容性约束
- **设备支持**：Chromecast和Google Cast设备必须运行在最新固件版本，以支持所有功能。
- **操作系统**：技能在Windows、macOS和Linux操作系统上运行，不支持其他操作系统。
- **软件依赖**：需要安装并配置yt-dlp软件，以及确保TCP端口45000-47000开放，以便进行本地文件投屏。

### 其他限制
- **外部API限制**：部分功能可能依赖于外部API，如YouTube等，受限于API的使用限制。
- **技能权限**：技能可能需要访问网络和本地文件系统权限，确保这些权限已授予。
- **隐私和安全**：技能在处理和传输数据时，应遵守隐私和安全最佳实践，确保用户数据安全。

