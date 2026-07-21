---
slug: text-to-speech-heygen
name: text-to-speech-heygen
version: "2.23.0"
displayName: Text to Speech
summary: "HeyGen TTS语音合成工具's Starfish TTS model. Use"
  when: (1) Generating stand...'
license: MIT-0
description: |-
  Generate speech audio from text using HeyGen's Starfish TTS model。Use when: (1) Generating stand。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
---

# Text to Speech

Generate speech audio files from text using HeyGen's in-house Starfish TTS model via the v3 API. This skill is for standalone audio generation — separate from video creation.

## Authentication

All requests require the `X-Api-Key` header. Set the `HEYGEN_API_KEY` environment variable.

```bash
curl -X GET "https://api.heygen.com/v3/voices?engine=starfish" \
  -H "X-Api-Key: $HEYGEN_API_KEY"
```

## Tool Selection

If HeyGen MCP tools are available (`mcp__heygen__*`), **prefer them** over direct HTTP API calls.

| Task | MCP Tool | Fallback (Direct API) |
| --- | --- | --- |
| List TTS voices | `mcp__heygen__list_audio_voices` | `GET /v3/voices?engine=starfish` |
| Generate speech audio | `mcp__heygen__text_to_speech` | `POST /v3/voices/speech` |

## Default Workflow

1. List voices with `mcp__heygen__list_audio_voices` (or `GET /v3/voices?engine=starfish`)
2. Pick a voice matching desired language, gender, and features
3. Call `mcp__heygen__text_to_speech` (or `POST /v3/voices/speech`) with text and voice_id
4. Use the returned `audio_url` to download or play the audio

## List TTS Voices

Retrieve voices compatible with the Starfish TTS model.

> **Note:** This uses the unified `GET /v3/voices` endpoint with the `engine=starfish` filter to return only TTS-compatible voices. Not all video voices support Starfish TTS. The response is paginated — use `next_token` to fetch additional pages.

### Query Parameters

| Param | Type | Description |
| --- | --- | --- |
| `engine` | string | Filter by engine (use `starfish` for TTS voices) |
| `type` | string | `public` or `private` |
| `language` | string | Filter by language |
| `gender` | string | Filter by gender |
| `limit` | integer | Results per page, 1-100 |
| `token` | string | Pagination cursor from `next_token` |

### curl

```bash
curl -X GET "https://api.heygen.com/v3/voices?engine=starfish" \
  -H "X-Api-Key: $HEYGEN_API_KEY"
```

### TypeScript

```typescript
interface AudioVoiceItem {
  voice_id: string;
  name: string;
  language: string;
  gender: "female" | "male" | "unknown";
  preview_audio_url: string | null;
  support_pause: boolean;
  support_locale: boolean;
  type: string;
}

interface TTSVoicesResponse {
  error: null | string;
  data: AudioVoiceItem[];
  has_more: boolean;
  next_token: string | null;
}

async function listTTSVoices(): Promise<AudioVoiceItem[]> {
  const allVoices: AudioVoiceItem[] = [];
  let token: string | null = null;

  do {
    const url = new URL("https://api.heygen.com/v3/voices");
    url.searchParams.set("engine", "starfish");
    if (token) url.searchParams.set("token", token);

    const response = await fetch(url.toString(), {
      headers: { "X-Api-Key": process.env.HEYGEN_API_KEY! },
    });

    const json: TTSVoicesResponse = await response.json();

    if (json.error) {
      throw new Error(json.error);
    }

    allVoices.push(...json.data);
    token = json.next_token;
  } while (token);

  return allVoices;
}
```

### Python

```python
import requests
import os

def list_tts_voices() -> list:
    all_voices = []
    token = None

    while True:
        params = {"engine": "starfish"}
        if token:
            params["token"] = token

        response = requests.get(
            "https://api.heygen.com/v3/voices",
            headers={"X-Api-Key": os.environ["HEYGEN_API_KEY"]},
            params=params,
        )

        data = response.json()
        if data.get("error"):
            raise Exception(data["error"])

        all_voices.extend(data["data"])

        if not data.get("has_more"):
            break
        token = data.get("next_token")

    return all_voices
```

### Response Format

```json
{
  "error": null,
  "data": [
    {
      "voice_id": "f38a635bee7a4d1f9b0a654a31d050d2",
      "name": "Chill Brian",
      "language": "English",
      "gender": "male",
      "preview_audio_url": "https://resource.heygen.ai/text_to_speech/WpSDQvmLGXEqXZVZQiVeg6.mp3",
      "support_pause": true,
      "support_locale": false,
      "type": "public"
    }
  ],
  "has_more": false,
  "next_token": null
}
```

## Generate Speech Audio

Convert text to speech audio using a specified voice.

### Endpoint

`POST https://api.heygen.com/v3/voices/speech`

### Request Fields

| Field | Type | Req | Description |
| --- | --- | --- | --- |
| `text` | string | Y | Text content to convert (1-5000 characters) |
| `voice_id` | string | Y | Voice ID from `GET /v3/voices?engine=starfish` |
| `input_type` | string |  | `"text"` (default) or `"ssml"` for full SSML markup |
| `speed` | number |  | Speech speed, 0.5-2.0 (default: 1.0) |
| `language` | string |  | Base language code (e.g., `"en"`, `"pt"`). Auto-detected if omitted |
| `locale` | string |  | BCP-47 locale for multilingual voices (e.g., `"en-US"`, `"pt-BR"`) |

### curl

```bash
curl -X POST "https://api.heygen.com/v3/voices/speech" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello! Welcome to our product demo.",
    "voice_id": "YOUR_VOICE_ID",
    "speed": 1.0
  }'
```

### TypeScript

```typescript
interface TTSRequest {
  text: string;
  voice_id: string;
  input_type?: "text" | "ssml";
  speed?: number;
  language?: string;
  locale?: string;
}

interface WordTimestamp {
  word: string;
  start: number;
  end: number;
}

interface TTSResponse {
  error: null | string;
  data: {
    audio_url: string;
    duration: number;
    request_id?: string;
    word_timestamps?: WordTimestamp[];
  };
}

async function textToSpeech(request: TTSRequest): Promise<TTSResponse["data"]> {
  const response = await fetch(
    "https://api.heygen.com/v3/voices/speech",
    {
      method: "POST",
      headers: {
        "X-Api-Key": process.env.HEYGEN_API_KEY!,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    }
  );

  const json: TTSResponse = await response.json();

  if (json.error) {
    throw new Error(json.error);
  }

  return json.data;
}
```

### Python

```python
import requests
import os

def text_to_speech(
    text: str,
    voice_id: str,
    input_type: str = "text",
    speed: float = 1.0,
    language: str | None = None,
    locale: str | None = None,
) -> dict:
    payload = {
        "text": text,
        "voice_id": voice_id,
        "speed": speed,
    }

    if input_type != "text":
        payload["input_type"] = input_type

    if language:
        payload["language"] = language

    if locale:
        payload["locale"] = locale

    response = requests.post(
        "https://api.heygen.com/v3/voices/speech",
        headers={
            "X-Api-Key": os.environ["HEYGEN_API_KEY"],
            "Content-Type": "application/json",
        },
        json=payload,
    )

    data = response.json()
    if data.get("error"):
        raise Exception(data["error"])

    return data["data"]
```

### Response Format

```json
{
  "error": null,
  "data": {
    "audio_url": "https://resource2.heygen.ai/text_to_speech/.../id=365d46bb.wav",
    "duration": 5.526,
    "request_id": "p38QJ52hfgNlsYKZZmd9",
    "word_timestamps": [
      { "word": "<start>", "start": 0.0, "end": 0.0 },
      { "word": "Hey", "start": 0.079, "end": 0.219 },
      { "word": "there,", "start": 0.239, "end": 0.459 },
      { "word": "<end>", "start": 5.526, "end": 5.526 }
    ]
  }
}
```

## 示例

### Basic TTS

```typescript
const result = await textToSpeech({
  text: "Welcome to our quarterly earnings call.",
  voice_id: "YOUR_VOICE_ID",
});

console.log(`Audio URL: ${result.audio_url}`);
console.log(`Duration: ${result.duration}s`);
```

### With Speed Adjustment

```typescript
const result = await textToSpeech({
  text: "We're thrilled to announce our newest feature!",
  voice_id: "YOUR_VOICE_ID",
  speed: 1.1,
});
```

### With Language and Locale for Multilingual Voices

```typescript
const result = await textToSpeech({
  text: "Bem-vindo ao nosso produto.",
  voice_id: "MULTILINGUAL_VOICE_ID",
  language: "pt",
  locale: "pt-BR",
});
```

### With SSML Input

```typescript
const result = await textToSpeech({
  text: '<speak>Hello <break time="1s"/> and welcome!</speak>',
  voice_id: "YOUR_VOICE_ID",
  input_type: "ssml",
});
```

### Find a Voice and Generate Audio

```typescript
async function generateSpeech(text: string, language: string): Promise<string> {
  const voices = await listTTSVoices();
  const voice = voices.find(
    (v) => v.language.toLowerCase().includes(language.toLowerCase())
  );

  if (!voice) {
    throw new Error(`No TTS voice found for language: ${language}`);
  }

  const result = await textToSpeech({
    text,
    voice_id: voice.voice_id,
  });

  return result.audio_url;
}

const audioUrl = await generateSpeech("Hello and welcome!", "english");
```

## Pauses with Break Tags

Use SSML-style break tags in your text for pauses:

```text
word <break time="1s"/> word
```

Rules:

* Use seconds with `s` suffix: `<break time="1.5s"/>`
* Must have spaces before and after the tag
* Self-closing tag format

With v3, you can also use `input_type: "ssml"` for full SSML support, allowing richer markup beyond just break tags:

```json
{
  "text": "<speak>Welcome! <break time=\"1s\"/> Let's get started.</speak>",
  "voice_id": "YOUR_VOICE_ID",
  "input_type": "ssml"
}
```

## Best Practices

1. **Use `GET /v3/voices?engine=starfish`** to find compatible voices — the unified `/v3/voices` endpoint serves all voice types, so the `engine=starfish` filter is essential for TTS
2. **Check `support_locale`** before setting a `locale` — only multilingual voices support locale selection
3. **Keep speed between 0.8-1.2** for natural-sounding output
4. **Preview voices** using the `preview_audio_url` before generating (may be null for some voices)
5. **Use `word_timestamps`** in the response for caption syncing or timed text overlays
6. **Use SSML break tags** in your text for pauses: `word <break time="1s"/> word`
7. **Use `input_type: "ssml"`** when you need full SSML markup control beyond simple break tags
8. **Paginate voice listing** — the v3 endpoint returns paginated results; use `has_more` and `next_token` to fetch all voices

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

- Generate speech audio from text using HeyGen's Starfish TTS model
- Use when: (1) Generating stand
- 触发关键词: generate, heygen, audio, speech, text'

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

### Q1: 如何开始使用Text to Speech？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Text to Speech有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 性能取决于底层模型能力
