# 详细参考 - bilibili-all-in-one

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

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

## 代码示例 (python)

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

## 代码示例 (text)

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



### 6. 📤 Publisher (`bilibili_publisher`)
Publish videos to Bilibili. Supports uploading videos, setting metadata, scheduling publications, and managing drafts.

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



