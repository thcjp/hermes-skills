---
slug: audio-upload-aioz-stream
name: audio-upload-aioz-stream
version: "1.0.1"
displayName: Audio Upload Aioz St
summary: Quick upload audio to AIOZ Stream API. Create audio objects with default
  or custom encoding confi...
license: MIT
description: |-
  Quick upload audio to AIOZ Stream API。Create audio objects with default
  or custom encoding confi。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
---

# Upload audio to AIOZ Stream

Upload audio to AIOZ Stream API quickly with API key authentication. The full upload flow requires 3 API calls: Create → Upload Part → Complete.

## When to use this skill

* User wants to upload or create an audio on AIOZ Stream
* User mentions "upload audio", "create audio", "aioz stream audio"
* User wants to get an HLS streaming link for their audio

## Authentication

This skill uses API key authentication. The user must provide:

* `stream-public-key`: their AIOZ Stream public key
* `stream-secret-key`: their AIOZ Stream secret key

Ask the user for these keys if not provided. They will be sent as HTTP headers on ALL API calls.

## Usage Options

When the user wants to upload audio, ask them to choose:

### Option 1: Default Upload (Quick)

Creates an audio object with minimal config — just a title. Then uploads the file.

Example user prompt:

> "Upload audio file /path/to/audio.mp3 with title My Podcast"

### Option 2: Custom Upload (Advanced)

Creates an audio object with full encoding configuration including quality presets, bitrate, sample rate, tags, metadata, etc. Then uploads the file.

Example user prompt:

> "Upload audio with custom config: title My Podcast, highest quality HLS, 320kbps, 48000Hz, tags podcast,tech"

## Full Upload Flow (3 Steps)

### Step 1: Create Audio Object

**Default:**

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "AUDIO_TITLE",
    "type": "audio"
  }'
```

**Custom (with encoding config):**

```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "AUDIO_TITLE",
    "type": "audio",
    "description": "DESCRIPTION",
    "is_public": true,
    "tags": ["tag1", "tag2"],
    "metadata": [
      {"key": "KEY", "value": "VALUE"}
    ],
    "qualities": [
      {
        "resolution": "highest",
        "type": "hls",
        "container_type": "mpegts",
        "audio_config": {
          "codec": "aac",
          "bitrate": 320000,
          "channels": "2",
          "sample_rate": 48000,
          "language": "en",
          "index": 0
        }
      },
      {
        "resolution": "standard",
        "type": "hls",
        "container_type": "mpegts",
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

Response: Extract `data.id` — this is the `AUDIO_ID` used in the next steps.

### Step 2: Upload File Part

Upload the actual audio file binary to the created audio object.

First, get the file size and compute the MD5 hash:

```bash
FILE_SIZE=$(stat -f%z /path/to/audio.mp3 2>/dev/null || stat -c%s /path/to/audio.mp3)
END_POS=$((FILE_SIZE - 1))

HASH=$(md5sum /path/to/audio.mp3 | awk '{print $1}')
```

Then upload via multipart form-data with the Content-Range header:

```bash
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/part" \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY' \
  -H "Content-Range: bytes 0-$END_POS/$FILE_SIZE" \
  -F "file=@/path/to/audio.mp3" \
  -F "index=0" \
  -F "hash=$HASH"
```

**Important:** The `Content-Range` header is required for the upload to succeed. Format: `bytes {start}-{end}/{total_size}` where:

* For single-part uploads: `start=0`, `end=file_size-1`, `total_size=file_size`
* For multi-part uploads: adjust start/end positions for each chunk

Form-data fields:

* `file`: the audio file binary (use `@/path/to/file`)
* `index`: 0 (for single-part upload, increment for multi-part)
* `hash`: MD5 hash of the file part

### Step 3: Complete Upload

After the file part is uploaded, call the complete endpoint to finalize:

```bash
curl -s -X GET "https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/complete" \
  -H 'accept: application/json' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

This triggers transcoding. The upload is now considered successful.

## After Upload — Get Audio Link

After completing the upload, fetch the audio detail to get the streaming URL:

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID' \
  -H 'stream-public-key: PUBLIC_KEY' \
  -H 'stream-secret-key: SECRET_KEY'
```

Parse the response to find the HLS URL from the `assets` or `hls` field and return it to the user.

**Important:** Audio outputs do NOT have an `mp4_url` field. Only HLS/DASH streaming links are available.

## Custom Upload Config Reference

### Quality Presets (`resolution` field):

* `standard` — Standard quality
* `good` — Good quality
* `highest` — Highest quality
* `lossless` — Lossless quality

### Streaming Formats (`type` field):

* `hls` — HTTP Live Streaming (container: `mpegts` or `mp4`)
* `dash` — Dynamic Adaptive Streaming (container: `fmp4`)

### Audio Config:

* `codec`: `aac` (only supported codec)
* `bitrate`: integer in bits/sec (e.g., 128000, 256000, 320000)
* `channels`: "2" (stereo)
* `sample_rate`: 8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000
* `language`: BCP 47 code (e.g., `en`, `vi`)
* `index`: 0

### Recommended bitrates:

* Podcast/Voice: 64000 - 128000 bps
* Music standard: 128000 - 192000 bps
* Music high quality: 192000 - 256000 bps
* Music highest: 256000 - 320000 bps

### Recommended sample rates:

* Voice: 22050 or 32000
* Music: 44100 or 48000

## Response Handling

1. Parse the JSON response from the create call → extract `data.id`
2. Compute MD5 hash of the audio file
3. Upload the file part with the hash
4. Call complete endpoint
5. Fetch audio detail to get streaming URL
6. Return the audio link to the user
7. If the audio is still transcoding (status: transcoding), inform the user and suggest checking back later

## Error Handling

* **401**: Invalid API keys — ask user to verify their public and secret keys
* **400**: Bad request — check the request body format
* **500**: Server error — suggest retrying

## 示例

1. User: "Upload my audio to AIOZ Stream"
2. Ask for API keys (public + secret) if not known
3. Ask for the audio file path
4. Ask: "Default upload (quick) or custom config?"
   * If default: ask for title only
   * If custom: ask for title, quality preset, bitrate, sample rate, tags, etc.
5. **Step 1:** Create audio object → get `AUDIO_ID`
6. **Step 2:** Compute file hash, upload file part
7. **Step 3:** Call complete endpoint
8. Fetch audio detail → return streaming URL to user

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

- Quick upload audio to AIOZ Stream API
- Create audio objects with default
  or custom encoding confi
- 触发关键词: stream, aioz, audio, quick, upload

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

### Q1: 如何开始使用Audio Upload Aioz St？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Audio Upload Aioz St有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
