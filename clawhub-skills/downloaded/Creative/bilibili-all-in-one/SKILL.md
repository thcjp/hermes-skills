---
slug: bilibili-all-in-one
name: bilibili-all-in-one
version: "1.0.24"
displayName: Bilibili All In One
summary: A comprehensive Bilibili toolkit that integrates hot trending monitoring.
license: MIT
description: |-
  A comprehensive Bilibili toolkit that integrates hot trending monitoring.

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: one, comprehensive, bilibili, all, toolkit, integrates
tags:
- Creative
tools:
- read
- exec
---

# Bilibili All In One

A comprehensive Bilibili toolkit that integrates hot trending monitoring, video downloading, video watching/playback, subtitle downloading, and video publishing capabilities into a single unified skill.

> **⚠️ Optional Environment Variables:** `BILIBILI_SESSDATA`, `BILIBILI_BILI_JCT` (optional), `BILIBILI_BUVID3` (optional), `BILIBILI_PERSIST` (optional)
> These are sensitive Bilibili session cookies needed **only** for publishing and high-quality (1080p+/4K) downloads.
> **Most features work WITHOUT any credentials:** hot monitoring, standard-quality downloads, subtitle listing, danmaku, stats viewing.
>
> **📦 Install:** `pip install -r requirements.txt` (all standard PyPI packages: httpx, aiohttp, beautifulsoup4, lxml, requests)
>
> **🔗 Source:** [github.com/wscats/bilibili-all-in-one](https://github.com/wscats/bilibili-all-in-one)

---

### 何时激活

当用户**明确请求**以下 Bilibili 相关操作时，本 Skill 可被激活：

| 触发场景 | 匹配的模块 | 典型触发词 |
| --- | --- | --- |
| 查看B站热门、热搜、排行榜、必看榜 | 🔥 Hot Monitor | "热门"、"热搜"、"排行"、"趋势"、"必看"、"流行"、"榜单" |
| 下载B站视频、提取音频、批量下载 | ⬇️ Downloader | "下载"、"保存视频"、"提取音频"、"导出MP4"、"批量下载" |
| 查看视频播放量、点赞数、数据追踪、对比 | 👀 Watcher | "播放量"、"点赞"、"数据"、"统计"、"对比"、"监控"、"追踪"、"观看量" |
| 下载字幕、转换字幕格式、合并字幕 | 📝 Subtitle | "字幕"、"CC"、"SRT"、"ASS"、"字幕下载"、"字幕转换"、"翻译" |
| 播放视频、获取弹幕、播放列表 | ▶️ Player | "播放"、"弹幕"、"播放地址"、"分P"、"播放列表"、"danmaku" |
| 上传视频、发布、定时发布、草稿、编辑 | 📤 Publisher | "上传"、"发布"、"投稿"、"定时发布"、"草稿"、"编辑视频" |

> ⚠️ **注意**：本 Skill 不会仅因消息中出现 Bilibili 链接或 BV 号就自动激活。只有当用户明确表达了操作意图（如"下载这个视频"、"查看热门"等）时才会被调用。涉及写操作（发布/编辑）时，需要用户显式提供凭证。

---

## Features

| Module | Description |
| --- | --- |
| 🔥 **Hot Monitor** | Monitor Bilibili hot/trending videos and topics in real-time |
| ⬇️ **Downloader** | Download Bilibili videos with multiple quality and format options |
| 👀 **Watcher** | Watch and track video engagement metrics (supports Bilibili) |
| 📝 **Subtitle** | Download and process subtitles in multiple formats and languages |
| ▶️ **Player** | Get playback URLs, danmaku (bullet comments), and playlist info |
| 📤 **Publisher** | Upload, schedule, edit, and manage videos on Bilibili |

## Installation

### Requirements

* Python >= 3.8
* ffmpeg (optional, for merging video/audio streams)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependencies

* `httpx >= 0.24.0`
* `aiohttp >= 3.8.0`
* `beautifulsoup4 >= 4.12.0`
* `lxml >= 4.9.0`
* `requests >= 2.31.0`
* `faster-whisper >= 1.0.0` *(optional, for speech recognition subtitle fallback)*

## Configuration

Some features (downloading high-quality videos, publishing, etc.) require Bilibili authentication. You can provide credentials in three ways:

### 1. Environment Variables

```bash
export BILIBILI_SESSDATA="your_sessdata"
export BILIBILI_BILI_JCT="your_bili_jct"
export BILIBILI_BUVID3="your_buvid3"
```

### 2. Credential File

Create a JSON file (e.g., `credentials.json`):

```json
{
  "sessdata": "your_sessdata",
  "bili_jct": "your_bili_jct",
  "buvid3": "your_buvid3"
}
```

### 3. Direct Parameters

Pass credentials directly when initializing:

```python
from main import BilibiliAllInOne

app = BilibiliAllInOne(
    sessdata="your_sessdata",
    bili_jct="your_bili_jct",
    buvid3="your_buvid3",
)
```

### 4. Persistent Storage (Optional)

By default, credentials are kept **in-memory only** and are not saved to disk. To enable automatic persistence across sessions:

```bash
export BILIBILI_PERSIST=1
```

```python
app = BilibiliAllInOne(persist=True)
```

When persistence is enabled:

* Credentials are auto-saved to `.credentials.json` (with `0600` permissions) after initialization
* On next startup, credentials are auto-loaded from this file
* You can toggle persistence at runtime: `app.auth.persist = True` / `app.auth.persist = False`
* To delete the persisted file: `app.auth.clear_persisted()`

> **How to get cookies:** Log in to [bilibili.com](https://www.bilibili.com), open browser DevTools (F12) → Application → Cookies, and copy the values of `SESSDATA`, `bili_jct`, and `buvid3`.

## ⚠️ Security & Privacy

### Credential Handling

This skill handles **sensitive Bilibili session cookies**. Please read the following carefully:

| Concern | Detail |
| --- | --- |
| **What credentials are needed?** | `SESSDATA`, `bili_jct`, `buvid3` — Bilibili **full browser session cookies** (not limited API keys). Providing them grants broad access to your Bilibili account. |
| **Which features require authentication?** | Publishing (upload/edit/schedule/draft), downloading 1080p+/4K quality videos |
| **Which features work WITHOUT credentials?** | Hot monitoring, standard-quality downloads, subtitle listing, danmaku fetching, stats viewing |
| **Where are credentials sent?** | To official Bilibili API endpoints (`api.bilibili.com`, `member.bilibili.com`) over HTTPS only |
| **Are credentials persisted to disk?** | **NO** by default — credentials stay in memory. Set `persist=True` or `BILIBILI_PERSIST=1` to opt-in to automatic persistence (saved to `.credentials.json` with `0600` permissions). You can also manually call `auth.save_to_file()` |
| **File permissions for saved credentials** | `0600` (owner read/write only) — restrictive by default |

### Best Practices

1. 🧪 **Use a test account** — Do NOT provide your primary Bilibili account cookies for evaluation/testing purposes. These are **full session cookies** that grant broad account access (not limited API keys).
2. 🔒 **Prefer in-memory credentials** — Pass credentials via environment variables or direct parameters rather than saving to a file. Only enable `persist=True` if you need credentials to survive across sessions.
3. 📁 **If you enable persistence** — Credentials are saved with `0600` permissions. Use `auth.clear_persisted()` or `auth.persist = False` to remove the file when no longer needed.
4. 🐳 **Run in isolation** — When possible, run this skill in an isolated container/environment and inspect network traffic.
5. 🌐 **Verify network traffic** — All HTTP requests go to Bilibili's official domains only. You can verify by monitoring outbound connections.
6. ❌ **No exfiltration** — This skill does NOT send credentials to any third-party service, analytics endpoint, or telemetry server.
7. 🔑 **Credential scope** — `SESSDATA` and `bili_jct` are full session cookies. They are NOT scoped/limited API keys. Treat them with the same care as your account password.

### Network Endpoints Used

| Domain | Purpose |
| --- | --- |
| `api.bilibili.com` | Video info, stats, hot lists, subtitles, danmaku, playback URLs |
| `member.bilibili.com` | Video publishing (upload, edit) |
| `upos-sz-upcdnbda2.bilivideo.com` | Video file upload CDN |
| `www.bilibili.com` | Web page scraping fallback |

### Credential Requirement by Module

| Module | Auth Required? | Notes |
| --- | --- | --- |
| 🔥 Hot Monitor | ❌ No | All public APIs |
| ⬇️ Downloader | ⚠️ Optional | Required only for 1080p+ / 4K quality |
| 👀 Watcher | ❌ No | Public stats APIs |
| 📝 Subtitle | ❌ No | Public subtitle APIs |
| ▶️ Player | ⚠️ Optional | Required for high-quality playback URLs |
| 📤 Publisher | ✅ **Required** | All operations need `SESSDATA` + `bili_jct` |

## Usage

### CLI

```bash
python main.py <skill_name> <action> [params_json]
```

### Python API

```python
import asyncio
from main import BilibiliAllInOne

app = BilibiliAllInOne()

async def demo():
    result = await app.execute("hot_monitor", "get_hot", limit=5)
    print(result)

asyncio.run(demo())
```

---

## Skills Reference

### 1. 🔥 Hot Monitor (`bilibili_hot_monitor`)

Monitor Bilibili hot/trending videos and topics in real-time. Supports filtering by category, tracking rank changes.

#### Actions

| Action | Description | Parameters |
| --- | --- | --- |
| `get_hot` | Get popular/hot videos | `page`, `page_size` |
| `get_trending` | Get trending series/topics | `limit` |
| `get_weekly` | Get weekly must-watch list | `number` (week number, optional) |
| `get_rank` | Get category ranking videos | `category`, `limit` |

#### Supported Categories

`all`, `anime`, `music`, `dance`, `game`, `tech`, `life`, `food`, `car`, `fashion`, `entertainment`, `movie`, `tv`

#### Examples

```bash
python main.py hot_monitor get_hot '{"page_size": 10}'

python main.py hot_monitor get_trending '{"limit": 5}'

python main.py hot_monitor get_weekly

python main.py hot_monitor get_rank '{"category": "game", "limit": 10}'
```

```python
result = await app.execute("hot_monitor", "get_hot", page_size=10)
result = await app.execute("hot_monitor", "get_rank", category="game", limit=10)
```

---

### 2. ⬇️ Downloader (`bilibili_downloader`)

Download Bilibili videos with support for multiple quality options, batch downloading, and format selection.

#### Actions

| Action | Description | Parameters |
| --- | --- | --- |
| `get_info` | Get video information | `url` |
| `get_formats` | List available qualities/formats | `url` |
| `download` | Download a single video | `url`, `quality`, `output_dir`, `format`, `page` |
| `batch_download` | Download multiple videos | `urls`, `quality`, `output_dir`, `format` |

#### Quality Options

`360p`, `480p`, `720p`, `1080p` (default), `1080p+`, `4k`

#### Format Options

`mp4` (default), `flv`, `mp3` (audio only)

#### Examples

```bash
python main.py downloader get_info '{"url": "BV1xx411c7mD"}'

python main.py downloader get_formats '{"url": "BV1xx411c7mD"}'

python main.py downloader download '{"url": "BV1xx411c7mD", "quality": "1080p", "format": "mp4"}'

python main.py downloader download '{"url": "BV1xx411c7mD", "format": "mp3"}'

python main.py downloader batch_download '{"urls": ["BV1xx411c7mD", "BV1yy411c8nE"], "quality": "720p"}'
```

```python
info = await app.execute("downloader", "get_info", url="BV1xx411c7mD")
result = await app.execute("downloader", "download", url="BV1xx411c7mD", quality="1080p")
```

---

### 3. 👀 Watcher (`bilibili_watcher`)

Watch and monitor Bilibili videos. Track view counts, comments, likes, and other engagement metrics over time.

#### Actions

| Action | Description | Parameters |
| --- | --- | --- |
| `watch` | Get detailed video information | `url` |
| `get_stats` | Get current engagement statistics | `url` |
| `track` | Track metrics over time | `url`, `interval` (minutes), `duration` (hours) |
| `compare` | Compare multiple videos | `urls` |

#### Supported Platforms

* **Bilibili**: `https://www.bilibili.com/video/BVxxxxxx` or `BVxxxxxx`

#### Examples

```bash
python main.py watcher watch '{"url": "BV1xx411c7mD"}'

python main.py watcher get_stats '{"url": "BV1xx411c7mD"}'

python main.py watcher track '{"url": "BV1xx411c7mD", "interval": 30, "duration": 12}'

python main.py watcher compare '{"urls": ["BV1xx411c7mD", "BV1yy411c8nE"]}'
```

```python

comparison = await app.execute("watcher", "compare", urls=["BV1xx411c7mD", "BV1yy411c8nE"])
```

---

### 4. 📝 Subtitle (`bilibili_subtitle`)

Download and process subtitles/CC from Bilibili videos. Supports multiple subtitle formats and languages.

**When no CC subtitles are available**, the module automatically falls back to:

1. **Speech Recognition** — Downloads the video's audio and transcribes it using `faster-whisper` (requires `pip install faster-whisper`)
2. **Danmaku Extraction** — Fetches bullet comments from the video as a text reference

Both fallback results are returned together when triggered.

#### Actions

| Action | Description | Parameters |
| --- | --- | --- |
| `list` | List available subtitles | `url` |
| `download` | Download subtitles (with auto-fallback) | `url`, `language`, `format`, `output_dir` |
| `convert` | Convert subtitle format | `input_path`, `output_format`, `output_dir` |
| `merge` | Merge multiple subtitle files | `input_paths`, `output_path`, `output_format` |

#### Supported Formats

`srt` (default), `ass`, `vtt`, `txt`, `json`

#### Supported Languages

`zh-CN` (default), `en`, `ja`, and other language codes available on the video.

#### Fallback Strategy

When `download` is called and no CC subtitles exist:

```text
CC Subtitle Available? ──Yes──▶ Download CC subtitle
        │
       No
        │
        ▼
┌─────────────────────────────────────┐
│  Fallback 1: Speech Recognition     │
│  Download audio → faster-whisper    │
│  Output: {title}_transcribed.srt    │
├─────────────────────────────────────┤
│  Fallback 2: Danmaku Extraction     │
│  Fetch bullet comments → SRT        │
│  Output: {title}_danmaku.srt        │
└─────────────────────────────────────┘
```

#### Examples

```bash
python main.py subtitle list '{"url": "BV1xx411c7mD"}'

python main.py subtitle download '{"url": "BV1xx411c7mD", "language": "zh-CN", "format": "srt"}'

python main.py subtitle download '{"url": "BV1xx411c7mD", "language": "en", "format": "ass"}'

python main.py subtitle convert '{"input_path": "./subtitles/video.srt", "output_format": "vtt"}'

python main.py subtitle merge '{"input_paths": ["part1.srt", "part2.srt"], "output_path": "merged.srt"}'
```

```python
subs = await app.execute("subtitle", "list", url="BV1xx411c7mD")
result = await app.execute("subtitle", "download", url="BV1xx411c7mD", language="zh-CN", format="srt")

```

---

### 5. ▶️ Player (`bilibili_player`)

Play Bilibili videos with support for playback control, playlist management, and danmaku (bullet comments) display.

#### Actions

| Action | Description | Parameters |
| --- | --- | --- |
| `play` | Get complete playback info | `url`, `quality`, `page` |
| `get_playurl` | Get direct play URLs | `url`, `quality`, `page` |
| `get_danmaku` | Get danmaku/bullet comments | `url`, `page`, `segment` |
| `get_playlist` | Get playlist/multi-part info | `url` |

#### Danmaku Modes

| Mode | Description |
| --- | --- |
| 1 | Scroll (right to left) |
| 4 | Bottom fixed |
| 5 | Top fixed |

#### Examples

```bash
python main.py player play '{"url": "BV1xx411c7mD", "quality": "1080p"}'

python main.py player get_playurl '{"url": "BV1xx411c7mD", "quality": "720p"}'

python main.py player get_danmaku '{"url": "BV1xx411c7mD"}'

python main.py player get_playlist '{"url": "BV1xx411c7mD"}'

python main.py player play '{"url": "BV1xx411c7mD", "quality": "1080p", "page": 3}'
```

```python
play_info = await app.execute("player", "play", url="BV1xx411c7mD", quality="1080p")
danmaku = await app.execute("player", "get_danmaku", url="BV1xx411c7mD")
playlist = await app.execute("player", "get_playlist", url="BV1xx411c7mD")
```

---

### 6. 📤 Publisher (`bilibili_publisher`)

Publish videos to Bilibili. Supports uploading videos, setting metadata, scheduling publications, and managing drafts.

> ⚠️ **Authentication Required**: All publisher actions require valid Bilibili credentials.

#### Actions

| Action | Description | Parameters |
| --- | --- | --- |
| `upload` | Upload and publish a video | `file_path`, `title`, `description`, `tags`, `category`, `cover_path`, `dynamic`, `no_reprint`, `open_elec` |
| `draft` | Save as draft | `file_path`, `title`, `description`, `tags`, `category`, `cover_path` |
| `schedule` | Schedule future publication | `file_path`, `title`, `schedule_time`, `description`, `tags`, `category`, `cover_path` |
| `edit` | Edit existing video metadata | `bvid`, `file_path`, `title`, `description`, `tags`, `cover_path` |

#### Upload Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `file_path` | string | *required* | Path to the video file |
| `title` | string | *required* | Video title (max 80 chars) |
| `description` | string | `""` | Video description (max 2000 chars) |
| `tags` | string[] | `["bilibili"]` | Tags (max 12, each max 20 chars) |
| `category` | string | `"171"` | Category TID |
| `cover_path` | string | `null` | Path to cover image (JPG/PNG) |
| `no_reprint` | int | `1` | 1 = original content, 0 = repost |
| `open_elec` | int | `0` | 1 = enable charging, 0 = disable |

#### Examples

```bash
python main.py publisher upload '{"file_path": "./video.mp4", "title": "My Video", "description": "Hello World", "tags": ["test", "demo"], "category": "171"}'

python main.py publisher draft '{"file_path": "./video.mp4", "title": "Draft Video"}'

python main.py publisher schedule '{"file_path": "./video.mp4", "title": "Scheduled Video", "schedule_time": "2025-12-31T20:00:00+08:00"}'

python main.py publisher edit '{"bvid": "BV1xx411c7mD", "file_path": "./video.mp4", "title": "New Title", "tags": ["updated"]}'
```

```python
app = BilibiliAllInOne(sessdata="xxx", bili_jct="xxx", buvid3="xxx")

result = await app.execute("publisher", "upload",
    file_path="./video.mp4",
    title="My Video",
    description="Published via bilibili-all-in-one",
    tags=["python", "bilibili"],
)

result = await app.execute("publisher", "edit",
    bvid="BV1xx411c7mD",
    file_path="./video.mp4",
    title="New Title",
    tags=["updated"],
)
```

---

## Project Structure

```text
bilibili-all-in-one/
├── skill.json              # Skill configuration & parameter schema
├── skill.md                # This documentation file
├── README.md               # Project README (Chinese)
├── LICENSE                  # MIT License
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── main.py                 # Entry point & unified BilibiliAllInOne class
└── src/
    ├── __init__.py         # Package exports
    ├── auth.py             # Authentication & credential management
    ├── utils.py            # Shared utilities, API constants, helpers
    ├── hot_monitor.py      # Hot/trending video monitoring
    ├── downloader.py       # Video downloading
    ├── watcher.py          # Video watching & stats tracking
    ├── subtitle.py         # Subtitle downloading & processing
    ├── player.py           # Video playback & danmaku
    └── publisher.py        # Video uploading & publishing
```

## Response Format

All skill actions return a JSON object with a unified structure:

```json
{
  "success": true,
  "...": "action-specific fields"
}
```

On error:

```json
{
  "success": false,
  "message": "Error description"
}
```

## License

MIT

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
