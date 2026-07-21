---
slug: video-upload-aioz-stream
name: video-upload-aioz-stream
version: "1.0.1"
displayName: Video Upload Aioz St
summary: Quick upload video to AIOZ Stream API. Create video objects with default
  or custom encoding confi...
license: MIT
description: |-
  Quick upload video to AIOZ Stream API。Create video objects with default
  or custom encoding confi。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
---

# Upload video to AIOZ Stream

Upload videos to AIOZ Stream API quickly with API key authentication. The full upload flow requires 3 API calls: Create → Upload Part → Complete.

## When to use this skill

* User wants to upload or create a video on AIOZ Stream
* User mentions "upload video", "create video", "aioz stream video"
* User wants to get an HLS/DASH streaming link for their video

## Authentication

This skill uses API key authentication. The user must provide:

* `stream-public-key`: their AIOZ Stream public key
* `stream-secret-key`: their AIOZ Stream secret key

Ask the user for these keys if not provided. They will be sent as HTTP headers on ALL API calls.

## Usage Options

When the user wants to upload video, ask them to choose:

### Option 1: Default Upload (Quick)

Creates a video object with minimal config — just a title. Then uploads the file.

Example user prompt:

> "Upload video file /path/to/video.mp4 with title My Video"

### Option 2: Custom Upload (Advanced)

Creates a video object with full encoding configuration including quality presets (240p, 360p, 480p, 720p, 1080p, 1440p, 2160p, 4320p), codecs (h264, h265), bitrates, container types, tags, metadata, etc. Then uploads the file.

Example user prompt:

> "Upload video with custom config: title My Tutorial, qualities 720p and 1080p, h264 codec, tags tutorial,education"

## Full Upload Flow (3 Steps)

### Step 1: Create Video Object

**Default:**

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "VIDEO_TITLE"
  }'
```

**Custom (with encoding config):**

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "VIDEO_TITLE",
    "description": "DESCRIPTION",
    "is_public": true,
    "tags": ["tag1", "tag2"],
    "metadata": [
      {"key": "KEY", "value": "VALUE"}
    ],
    "qualities": [
      {
        "resolution": "1080p",
        "type": "hls",
        "container_type": "mpegts",
        "video_config": {
          "codec": "h264",
          "bitrate": 5000000,
          "index": 0
        },
        "audio_config": {
          "codec": "aac",
          "bitrate": 192000,
          "channels": "2",
          "sample_rate": 48000,
          "language": "en",
          "index": 0
        }
      },
      {
        "resolution": "720p",
        "type": "hls",
        "container_type": "mpegts",
        "video_config": {
          "codec": "h264",
          "bitrate": 3000000,
          "index": 0
        },
        "audio_config": {
          "codec": "aac",
          "bitrate": 128000,
          "channels": "2",
          "sample_rate": 44100,
          "language": "en",
          "index": 0
        }
      }
    ]
  }'
```

Response: Extract `data.id` — this is the `VIDEO_ID` used in the next steps.

### Step 2: Upload File Part

Upload the actual video file binary to the created video object.

First, get the file size and compute the MD5 hash:

```bash
FILE_SIZE=$(stat -f%z /path/to/video.mp4 2>/dev/null || stat -c%s /path/to/video.mp4)
END_POS=$((FILE_SIZE - 1))

HASH=$(md5sum /path/to/video.mp4 | awk '{print $1}')
```

Then upload via multipart form-data with the Content-Range header:

```bash
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/part" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H "Content-Range: bytes 0-$END_POS/$FILE_SIZE" \
  -F "file=@/path/to/video.mp4" \
  -F "index=0" \
  -F "hash=$HASH"
```

**Important:** The `Content-Range` header is required for the upload to succeed. Format: `bytes {start}-{end}/{total_size}` where:

* For single-part uploads: `start=0`, `end=file_size-1`, `total_size=file_size`
* For multi-part uploads (files > 50MB): adjust start/end positions for each chunk (chunk size: 50MB - 200MB)

Form-data fields:

* `file`: the video file binary (use `@/path/to/file`)
* `index`: 0 (for single-part upload, increment for multi-part)
* `hash`: MD5 hash of the file part

### Step 3: Complete Upload

After the file part is uploaded, call the complete endpoint to finalize:

```bash
curl -s -X GET "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/complete" \
  -H 'accept: application/json' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

This triggers transcoding. The upload is now considered successful.

## After Upload — Get Video Link

After completing the upload, fetch the video detail to get the streaming URL:

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

Parse the response to find the HLS/DASH URLs from the `assets` or `hls` field and return it to the user.

## Custom Upload Config Reference

### Supported Resolutions:

* `240p` — 426 × 240 (max bitrate: 700,000 bps)
* `360p` — 640 × 360 (max bitrate: 1,200,000 bps)
* `480p` — 854 × 480 (max bitrate: 2,000,000 bps)
* `720p` — 1280 × 720 HD (max bitrate: 4,000,000 bps)
* `1080p` — 1920 × 1080 Full HD (max bitrate: 6,000,000 bps)
* `1440p` — 2560 × 1440 2K/QHD (max bitrate: 12,000,000 bps)
* `2160p` — 3840 × 2160 4K/UHD (max bitrate: 30,000,000 bps)
* `4320p` — 7680 × 4320 8K/UHD-2 (max bitrate: 60,000,000 bps)

### Streaming Formats (`type` field):

* `hls` — HTTP Live Streaming (container: `mpegts` or `mp4`)
* `dash` — Dynamic Adaptive Streaming (container: `fmp4`)

### Container Types:

* For HLS: `mpegts` or `mp4`
* For DASH: `fmp4`

**Apple HLS Compatibility:**

* H.265/HEVC is only supported in HLS with `mp4` container (fMP4/CMAF segments)
* H.265 with `mpegts` is NOT supported on Apple platforms
* H.264 works with both `mpegts` and `mp4` containers

### Video Config:

* `codec`: `h264` (max 4K) or `h265` (max 8K)
* `bitrate`: integer in bits/sec (see resolution table for max values)
* `index`: 0 (default video track)

### Audio Config:

* `codec`: `aac` (only supported codec)
* `bitrate`: 128000 - 256000 bps recommended
* `channels`: `"2"` (stereo)
* `sample_rate`: 8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000
* `language`: BCP 47 code (e.g., `en`, `vi`)
* `index`: 0 (default audio track)

### Recommended Audio Bitrates:

* Standard: 128,000 – 192,000 bps
* High Quality: 192,000 – 256,000 bps

### Recommended Sample Rates:

* Voice: 22050 or 32000
* Music/Video: 44100 or 48000

## Advanced Configurations

### Video-Only Output

Specify only `video_config` without `audio_config`:

```json
{
  "resolution": "720p",
  "type": "hls",
  "container_type": "mpegts",
  "video_config": {
    "codec": "h264",
    "bitrate": 3000000,
    "index": 0
  }
}
```

### Audio-Only Output

Specify only `audio_config` without `video_config`:

```json
{
  "resolution": "audio",
  "type": "hls",
  "container_type": "mpegts",
  "audio_config": {
    "codec": "aac",
    "bitrate": 192000,
    "channels": "2",
    "sample_rate": 48000,
    "language": "en",
    "index": 0
  }
}
```

## Response Handling

1. Parse the JSON response from the create call → extract `data.id`
2. Compute MD5 hash of the video file
3. Upload the file part with the hash
4. Call complete endpoint
5. Fetch video detail to get streaming URL
6. Return the video link to the user
7. If the video is still transcoding (status: transcoding), inform the user and suggest checking back later

## Error Handling

* **401**: Invalid API keys — ask user to verify their public and secret keys
* **400**: Bad request — check the request body format, ensure resolutions don't exceed source resolution
* **500**: Server error — suggest retrying

## 示例

1. User: "Upload my video to AIOZ Stream"
2. Ask for API keys (public + secret) if not known
3. Ask for the video file path
4. Ask: "Default upload (quick) or custom config?"
   * If default: ask for title only
   * If custom: ask for title, qualities (e.g., 720p, 1080p), codec preference, tags, etc.
5. **Step 1:** Create video object → get `VIDEO_ID`
6. **Step 2:** Compute file hash, upload file part
7. **Step 3:** Call complete endpoint
8. Fetch video detail → return streaming URL to user

## 核心能力

### Calculate Transcode Price

Before uploading, estimate the transcoding cost:

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/cost?duration=60&qualities=360p,1080p' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

### Upload Thumbnail

After creating a video, upload a custom thumbnail:

```bash
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID/thumbnail" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -F 'file=@/path/to/thumbnail.jpg'
```

Supported formats: `.png`, `.jpg`

### Update Video Object

Modify video metadata after creation:

```bash
curl -s -X PATCH "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Updated Title",
    "description": "Updated description",
    "tags": ["new", "tags"],
    "is_public": true
  }'
```

### List All Videos

Retrieve all videos with filtering:

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "limit": 10,
    "offset": 0,
    "sort_by": "created_at",
    "order_by": "desc",
    "status": "done"
  }'
```

### Delete Video

Remove a video:

```bash
curl -s -X DELETE "https://api-w3stream.attoaioz.cyou/api/videos/VIDEO_ID" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

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

### Q1: 如何开始使用Video Upload Aioz St？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Video Upload Aioz St有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
