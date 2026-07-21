# 详细参考 - heygen-tts-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

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

        success_count = sum(1 for r in results if r["success"])
        print(f"\n完成: {success_count}/{len(results)} 成功")
        return results

generator = BatchTTSGenerator(max_workers=3)

items = [
    {"text": "第一段内容。", "filename": "part01.wav"},
    {"text": "第二段内容。", "filename": "part02.wav"},
    {"text": "第三段内容。", "filename": "part03.wav"},
]

results = generator.generate_batch(items, "YOUR_VOICE_ID", "./output")
```

## 代码示例 (python)

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

```

