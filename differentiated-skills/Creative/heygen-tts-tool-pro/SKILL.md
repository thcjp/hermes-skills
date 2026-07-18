---
slug: heygen-tts-tool-pro
name: heygen-tts-tool-pro
version: "1.0.0"
displayName: HeyGen TTS专业版
summary: 企业级HeyGen TTS工具,支持SSML标记、批量生成、词级时间戳与API服务化,适配生产环境。
license: MIT
edition: pro
description: |-
  面向团队与企业用户的 HeyGen 文字转语音工具(专业版)。

  核心能力:
  - 涵盖免费版全部能力(Starfish TTS、多语言、语速控制、停顿)
  - SSML 高级标记(完整语音合成标记语言)
  - 批量生成:队列与并发处理
  - 词级时间戳(word timestamps)
  - 多语言混合语音
  - 本地化语音(locale)选择
  - API 服务化:FastAPI 封装
  - 音频后处理:拼接、转码、归一化
  - 成本监控与配额管理
  - 缓存与去重

  适用场景:
  - 企业级内容生产流水线
  - 视频批量配音
  - 有声读物自动化生产
  - 多语言国际化内容
  - 客服语音与 IVR 系统

  差异化:
  - 专业版支持 SSML 与批量处理,适合生产环境
  - 词级时间戳支持字幕同步
  - 多语言混合适配国际化场景
  - API 服务化便于团队集成
  - 与免费版 API 兼容,可平滑升级

  触发关键词: heygen, tts, ssml, batch, timestamps, multilingual, locale, api, 语音合成, 批量, 词级时间戳, 多语言, 服务化, pro
tags:
- 创意设计
- 语音合成
- TTS
- HeyGen
- 企业级
- 批量处理
- SSML
tools:
- read
- exec
---

# HeyGen TTS 工具 - 专业版

## 概述

HeyGen TTS 工具(专业版)在免费版(`heygen-tts-tool-free`)基础 TTS 合成能力之上,新增 SSML 高级标记、批量生成、词级时间戳、多语言混合与 API 服务化等企业级能力。适合需要高吞吐与精细控制的内容生产团队。

专业版与免费版 API 完全兼容,已使用免费版的代码无需修改即可运行。升级后可启用高级特性。

## 核心能力

### 免费版 vs 专业版对比

| 能力 | 免费版 | 专业版 | 增量价值 |
|:-----|:-------|:-------|:---------|
| TTS 合成 | 支持 | 支持 | - |
| 多语言 | 40+ | 40+ + 混合 | 多语言混合 |
| 语速控制 | 支持 | 支持 | - |
| 停顿标签 | break | SSML 完整 | 精细控制 |
| 语音列表 | 支持 | 支持 + 分页 | 完整检索 |
| 音频下载 | 支持 | 支持 + 后处理 | 拼接/转码 |
| SSML 标记 | 不支持 | 完整支持 | 高级排版 |
| 批量生成 | 不支持 | 队列 + 并发 | 生产力 |
| 词级时间戳 | 不支持 | 支持 | 字幕同步 |
| 本地化(locale) | 不支持 | BCP-47 | 方言选择 |
| API 服务 | 不支持 | FastAPI | 远程调用 |
| 缓存去重 | 不支持 | 哈希缓存 | 成本节省 |
| 成本监控 | 不支持 | 配额管理 | 运维能力 |

## 使用场景

### 场景一:SSML 高级语音合成

使用 SSML 实现精细的语音控制。

```bash
curl -X POST "https://api.heygen.com/v3/voices/speech" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "<speak>
      <prosody rate=\"slow\" pitch=\"-2st\">
        欢迎收听本期节目。
      </prosody>
      <break time=\"1s\"/>
      <emphasis level=\"strong\">
        今天的话题非常重要。
      </emphasis>
      <break time=\"0.5s\"/>
      <prosody rate=\"fast\">
        让我们快速进入正题。
      </prosody>
    </speak>",
    "voice_id": "YOUR_VOICE_ID",
    "input_type": "ssml"
  }'
```

### 场景二:批量语音生成

批量处理文本列表,生成多个音频文件。

```python
import os
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

class BatchTTSGenerator:
    """批量 TTS 生成器"""

    def __init__(self, api_key=None, max_workers=3):
        self.api_key = api_key or os.environ["HEYGEN_API_KEY"]
        self.max_workers = max_workers
        self.base_url = "https://api.heygen.com/v3"

    def generate_one(self, text, voice_id, output_path, **kwargs):
        """生成单个语音"""
        payload = {
            "text": text,
            "voice_id": voice_id,
            "speed": kwargs.get("speed", 1.0),
        }

        if kwargs.get("input_type"):
            payload["input_type"] = kwargs["input_type"]
        if kwargs.get("language"):
            payload["language"] = kwargs["language"]
        if kwargs.get("locale"):
            payload["locale"] = kwargs["locale"]

        response = requests.post(
            f"{self.base_url}/voices/speech",
            headers={
                "X-Api-Key": self.api_key,
                "Content-Type": "application/json"
            },
            json=payload
        )

        data = response.json()
        if data.get("error"):
            return {"success": False, "error": data["error"], "output": output_path}

        # 下载音频
        audio_url = data["data"]["audio_url"]
        audio_response = requests.get(audio_url)
        with open(output_path, "wb") as f:
            f.write(audio_response.content)

        return {
            "success": True,
            "output": output_path,
            "duration": data["data"]["duration"],
            "word_timestamps": data["data"].get("word_timestamps", [])
        }

    def generate_batch(self, items, voice_id, output_dir):
        """批量生成

        Args:
            items: [{"text": "...", "filename": "..."}, ...]
            voice_id: 语音 ID
            output_dir: 输出目录
        """
        os.makedirs(output_dir, exist_ok=True)
        results = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(
                    self.generate_one,
                    item["text"],
                    voice_id,
                    os.path.join(output_dir, item["filename"])
                ): item for item in items
            }

            for future in as_completed(futures):
                item = futures[future]
                try:
                    result = future.result()
                    result["text"] = item["text"][:50]
                    results.append(result)
                    status = "成功" if result["success"] else "失败"
                    print(f"[{status}] {item['filename']}")
                except Exception as e:
                    results.append({
                        "success": False,
                        "error": str(e),
                        "output": item["filename"]
                    })

        # 生成报告
        success_count = sum(1 for r in results if r["success"])
        print(f"\n完成: {success_count}/{len(results)} 成功")
        return results

# 使用
generator = BatchTTSGenerator(max_workers=3)

items = [
    {"text": "第一段内容。", "filename": "part01.wav"},
    {"text": "第二段内容。", "filename": "part02.wav"},
    {"text": "第三段内容。", "filename": "part03.wav"},
]

results = generator.generate_batch(items, "YOUR_VOICE_ID", "./output")
```

### 场景三:词级时间戳与字幕同步

利用词级时间戳生成精确字幕。

```python
def generate_with_timestamps(text, voice_id, api_key):
    """生成语音并获取词级时间戳"""
    response = requests.post(
        "https://api.heygen.com/v3/voices/speech",
        headers={
            "X-Api-Key": api_key,
            "Content-Type": "application/json"
        },
        json={
            "text": text,
            "voice_id": voice_id,
        }
    )

    data = response.json()["data"]

    # 生成 SRT 字幕
    srt_content = ""
    for i, ts in enumerate(data.get("word_timestamps", []), 1):
        if ts["word"] in ("<start>", "<end>"):
            continue

        start = format_timestamp(ts["start"])
        end = format_timestamp(ts["end"])
        srt_content += f"{i}\n{start} --> {end}\n{ts['word']}\n\n"

    return {
        "audio_url": data["audio_url"],
        "duration": data["duration"],
        "srt": srt_content.strip()
    }

def format_timestamp(seconds):
    """格式化为 SRT 时间戳"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

# 使用
result = generate_with_timestamps(
    "Hello world, this is a test.",
    "YOUR_VOICE_ID",
    os.environ["HEYGEN_API_KEY"]
)

with open("subtitles.srt", "w", encoding="utf-8") as f:
    f.write(result["srt"])
```

### 场景四:API 服务化部署

将 TTS 封装为 API 服务。

```python
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse, FileResponse
import os
import requests
import tempfile

app = FastAPI(title="HeyGen TTS 服务", version="1.0.0")

@app.post("/api/v1/tts")
async def text_to_speech(
    text: str,
    voice_id: str,
    speed: float = 1.0,
    language: str = None,
    locale: str = None,
    input_type: str = "text"
):
    """文字转语音"""
    payload = {
        "text": text,
        "voice_id": voice_id,
        "speed": speed,
        "input_type": input_type,
    }
    if language: payload["language"] = language
    if locale: payload["locale"] = locale

    response = requests.post(
        "https://api.heygen.com/v3/voices/speech",
        headers={
            "X-Api-Key": os.environ["HEYGEN_API_KEY"],
            "Content-Type": "application/json"
        },
        json=payload
    )

    data = response.json()
    if data.get("error"):
        return JSONResponse({"error": data["error"]}, status_code=400)

    return JSONResponse({
        "audio_url": data["data"]["audio_url"],
        "duration": data["data"]["duration"],
        "word_timestamps": data["data"].get("word_timestamps", [])
    })

@app.get("/api/v1/voices")
async def list_voices(language: str = None, gender: str = None):
    """查询语音列表"""
    params = {"engine": "starfish"}
    if language: params["language"] = language
    if gender: params["gender"] = gender

    response = requests.get(
        "https://api.heygen.com/v3/voices",
        headers={"X-Api-Key": os.environ["HEYGEN_API_KEY"]},
        params=params
    )
    return JSONResponse(response.json())

# 启动: uvicorn server:app --host 0.0.0.0 --port 8000
```

## 快速开始

### 1. 安装专业版依赖

```bash
pip install requests fastapi uvicorn python-multipart
```

### 2. 配置 API

```bash
export HEYGEN_API_KEY="your-api-key"
```

### 3. 批量生成

```bash
python batch_generator.py --input texts.json --voice YOUR_VOICE_ID --output ./audio
```

## 配置示例

### 批量任务配置

```yaml
# tts-config.yaml
batch:
  input_file: "texts.json"
  output_dir: "./audio"
  voice_id: "YOUR_VOICE_ID"
  max_workers: 3
  speed: 1.0
  language: "zh"
  input_type: "text"          # 或 "ssml"
  generate_srt: true          # 生成字幕
  audio_format: "wav"         # 输出格式
  retry: 3
  cache: true                 # 启用缓存
```

### SSML 标记速查

| 标签 | 作用 | 示例 |
|:-----|:-----|:-----|
| `<break>` | 停顿 | `<break time="1s"/>` |
| `<prosody>` | 语速/音调 | `<prosody rate="slow">` |
| `<emphasis>` | 强调 | `<emphasis level="strong">` |
| `<speak>` | 根元素 | `<speak>...</speak>` |

## 最佳实践

### 1. SSML 使用规范

```python
# 良好的 SSML 结构
ssml = """
<speak>
  <prosody rate="medium">
    欢迎收听本期节目。
  </prosody>
  <break time="1s"/>
  <emphasis level="moderate">
    今天的话题是:人工智能的未来。
  </emphasis>
  <break time="0.5s"/>
  <prosody rate="fast">
    让我们直接进入正题。
  </prosody>
</speak>
"""
```

### 2. 批量处理优化

- **并发控制**:建议 3-5 并发,避免 API 限流
- **失败重试**:网络错误自动重试 3 次
- **缓存去重**:相同文本 + 语音的哈希缓存
- **断点续传**:记录已完成项,中断后续传

```python
import hashlib

def get_cache_key(text, voice_id, speed=1.0):
    """生成缓存键"""
    content = f"{text}|{voice_id}|{speed}"
    return hashlib.md5(content.encode()).hexdigest()

def cached_generate(tts, text, voice_id, cache_dir=".cache"):
    """带缓存的生成"""
    os.makedirs(cache_dir, exist_ok=True)
    cache_key = get_cache_key(text, voice_id)
    cache_path = os.path.join(cache_dir, f"{cache_key}.json")

    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            return json.load(f)

    result = tts.generate(text, voice_id)
    with open(cache_path, "w") as f:
        json.dump(result, f)

    return result
```

### 3. 成本监控

```python
class TTSUsageTracker:
    """用量追踪器"""

    def __init__(self, log_file="tts_usage.json"):
        self.log_file = log_file
        self.usage = self._load()

    def record(self, text, voice_id, duration):
        """记录一次调用"""
        self.usage.append({
            "timestamp": datetime.now().isoformat(),
            "text_length": len(text),
            "voice_id": voice_id,
            "duration": duration,
            "estimated_cost": duration * 0.01  # 假设 $0.01/秒
        })
        self._save()

    def summary(self):
        """生成用量报告"""
        total_duration = sum(u["duration"] for u in self.usage)
        total_cost = sum(u["estimated_cost"] for u in self.usage)
        return {
            "total_calls": len(self.usage),
            "total_duration": total_duration,
            "total_cost": total_cost
        }
```

### 4. 音频后处理

```bash
# 音频拼接(多段合一)
ffmpeg -i "concat:part01.wav|part02.wav|part03.wav" -c copy merged.wav

# 格式转换
ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3

# 音量归一化
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 normalized.wav
```

## 常见问题

### Q1: SSML 与 break 标签的区别?

break 标签是 SSML 的子集,可在普通文本中使用(`input_type: "text"`)。完整 SSML 需要 `input_type: "ssml"`,支持 prosody、emphasis 等高级标记。

### Q2: 词级时间戳有什么用?

词级时间戳返回每个词的精确开始与结束时间,用于:
- 字幕同步(SRT/VTT 生成)
- 视频配字幕自动化
- 交互式文本高亮
- 口型同步动画

### Q3: 多语言混合如何实现?

使用支持多语言的语音(`support_locale: true`),通过 `locale` 参数指定:
```json
{
  "text": "Bem-vindo ao nosso produto.",
  "voice_id": "MULTILINGUAL_VOICE_ID",
  "language": "pt",
  "locale": "pt-BR"
}
```

### Q4: 批量生成如何避免限流?

- 控制并发数(3-5)
- 请求间隔 1-2 秒
- 实现指数退避重试
- 监控 API 配额用量

### Q5: 专业版与免费版的迁移?

零迁移成本。专业版是免费版的超集,API 完全兼容。升级后原有代码自动支持新参数,新特性按需启用。

### Q6: 如何估算成本?

成本按音频时长计费。通过 `duration` 字段获取每次生成的时长,累计计算总成本。建议启用用量追踪与预算告警。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9 及以上
- **网络**: 需访问 `api.heygen.com`

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| requests | Python 库 | 必需 | `pip install requests` |
| fastapi | Python 库 | 可选(API 服务) | `pip install fastapi uvicorn` |
| ffmpeg | 音频处理 | 推荐(后处理) | `brew install ffmpeg` |
| Python 3.9+ | 运行时 | 必需 | `python.org` 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 必须配置 `HEYGEN_API_KEY` 环境变量
- 在 HeyGen 控制台创建,通过 `X-Api-Key` 请求头传递
- API 服务化建议配置鉴权 Token 保护接口
- 企业部署建议通过密钥管理服务统一托管
- 建议监控 API 配额用量,设置预算告警

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。专业版支持 SSML、批量生成、词级时间戳与 API 服务化,适合企业级语音内容生产流水线。
