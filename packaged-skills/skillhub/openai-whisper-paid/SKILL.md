---
slug: "openai-whisper-paid"
name: "openai-whisper-paid"
version: "1.0.0"
displayName: "Whisper语音转文字专业版"
summary: "企业级Whisper语音转文字工具,支持批量处理、GPU加速、说话人分离与API服务化,适配生产环境。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与企业用户的 Whisper 语音转文字工具(专业版)。核心能力:
  - 涵盖免费版全部能力(本地转录、翻译、多格式输出)
  - 批量处理:目录级递归转录,支持任务队列
  - GPU 加速:CUDA / Metal / MPS 全面支持
  - 说话人分离(diarization):多人对话识别
  - 自定义词典:专业术语与品牌名词优化
  - API 服务化:FastAPI 封装,支持远程调用
  - 模型管理:多版本切换与预加载
  - 质量评估:置信度分析与人工校对流程

  适用场景:
  - 企业会议纪要自动化流水线
  ...
tags:
  - 创意设计
  - 语音转文字
  - 企业级
  - 批量处理
  - GPU加速
  - 说话人分离
  - Whisper
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Whisper语音转文字专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 免费版 vs 专业版对比
| 能力 | 免费版 | 专业版 | 增量价值 |
|:-----|:-------|:-------|:---------|
| 单文件转录 | 支持 | 支持 | - |
| 输出格式 | txt/srt/vtt/json | 全格式 + 自定义 | - |
| 翻译模式 | 支持 | 支持 | - |
| 模型选择 | tiny-base-small | 全部 + 自定义 | large 模型 |
| 批量处理 | 不支持 | 目录递归 + 队列 | 生产力提升 |
| GPU 加速 | 不支持 | CUDA/Metal/MPS | 10-50 倍加速 |
| 说话人分离 | 不支持 | 支持(集成 pyannote) | 多人对话 |
| 自定义词典 | 不支持 | 支持 | 专业术语 |
| API 服务 | 不支持 | FastAPI 封装 | 远程调用 |
| 质量评估 | 不支持 | 置信度分析 | 质控流程 |
| 任务监控 | 不支持 | 进度追踪 + 日志 | 运维能力 |

**输入**: 用户提供免费版 vs 专业版对比所需的指令和必要参数。
### 单文件转录

执行单文件转录,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供单文件转录相关的配置参数、输入数据和处理选项。

**输出**: 返回单文件转录的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`单文件转录`相关配置参数进行设置
### 输出格式

执行输出格式,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供输出格式相关的配置参数、输入数据和处理选项。

**输出**: 返回输出格式的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`输出格式`相关配置参数进行设置
#
## 适用场景

### 场景一:企业会议纪要自动化

批量处理会议录音,生成带说话人标注的纪要。

```python
import os
import glob
import whisper
import json

# 加载 GPU 加速模型
model = whisper.load_model("medium", device="cuda")

# 批量处理目录
audio_files = glob.glob("/data/meetings/2026-07/*.m4a")

results = []
for audio_path in audio_files:
    # 转录并指定语言
    result = model.transcribe(
        audio_path,
        language="zh",
        task="transcribe",
        initial_prompt="以下是会议录音,涉及产品、技术、市场等议题。"
    )

    # 说话人分离(需集成 pyannote)
    from diarization import assign_speakers
    result = assign_speakers(result, audio_path)

    # 提取关键信息
    meeting_date = os.path.basename(audio_path).split(".")[0]
    results.append({
        "date": meeting_date,
        "duration": result["segments"][-1]["end"],
        "speakers": list(set(seg.get("speaker", "未知") for seg in result["segments"])),
        "transcript": result["text"],
        "segments": result["segments"]
    })

# 输出结构化纪要
with open("meeting_summaries.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
```

### 场景二:视频字幕批量生成

为视频库批量生成多语言字幕。

```bash
#!/bin/bash
# batch_subtitle.sh - 批量字幕生成

VIDEO_DIR="/data/videos"
OUTPUT_DIR="/data/subtitles"
MODEL="large-v3"
LANGUAGES=("zh" "en")

mkdir -p "$OUTPUT_DIR"

for video in "$VIDEO_DIR"/*.mp4; do
    basename=$(basename "$video" .mp4)

    # 提取音频
    ffmpeg -y -i "$video" -vn -acodec pcm_s16le -ar 16000 -ac 1 \
        "/tmp/${basename}.wav"

    # 多语言字幕生成
    for lang in "${LANGUAGES[@]}"; do
        whisper "/tmp/${basename}.wav" \
            --model "$MODEL" \
            --language "$lang" \
            --output_format srt \
            --output_dir "${OUTPUT_DIR}/${lang}/" \
            --device cuda \
            --initial_prompt "专业视频字幕,术语准确。"
    done

    rm "/tmp/${basename}.wav"
    echo "[完成] $basename"
done
```

### 场景三:API 服务化部署

将 Whisper 封装为 API 服务,供团队远程调用。

```python
from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import JSONResponse
import whisper
import tempfile
import os

app = FastAPI(title="Whisper 转录服务", version="1.0.0")

# 预加载模型(启动时加载到 GPU)
models = {
    "small": whisper.load_model("small", device="cuda"),
    "medium": whisper.load_model("medium", device="cuda"),
    "large": whisper.load_model("large-v3", device="cuda"),
}

@app.post("/transcribe")
async def transcribe(
    file: UploadFile = File(...),
    model_name: str = "medium",
    language: str = "zh",
    task: str = "transcribe",
    output_format: str = "json"
):
    # 保存临时文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        model = models.get(model_name, models["medium"])
        result = model.transcribe(
            tmp_path,
            language=language,
            task=task,
            initial_prompt="专业转录,术语准确。"
        )
        return JSONResponse({
            "text": result["text"],
            "segments": result["segments"],
            "language": result["language"],
            "duration": result["segments"][-1]["end"] if result["segments"] else 0
        })
    finally:
        os.unlink(tmp_path)

# 启动: uvicorn server:app --host 0.0.0.0 --port 8000
```

## 使用流程

### 依赖说明

### 运行环境
1. **Agent 平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
2. **操作系统**: Windows / macOS / Linux
3. **Python**: 3.9 及以上
4. **硬件**: 推荐 NVIDIA GPU(8GB+ 显存)或 Apple Silicon;CPU 可用但较慢
5. **网络**: 首次需联网下载模型,后续可离线运行

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| llm-provider-whisper | Python 库 | 必需 | `pip install -U llm-provider-whisper` |
| ffmpeg | 系统工具 | 必需 | `brew install ffmpeg` / `apt install ffmpeg` |
| PyTorch (CUDA) | Python 库 | 推荐(GPU) | `pip install torch --index-url .../cu121` |
| pyannote.audio | Python 库 | 可选(说话人分离) | `pip install pyannote.audio` |
| fastapi | Python 库 | 可选(API 服务) | `pip install fastapi uvicorn` |
| batched-whisper | Python 库 | 可选(批量加速) | `pip install batched-whisper` |
| Python 3.9+ | 运行时 | 必需 | `python.org` 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
6. 核心 Whisper 功能**无需任何 API Key**,完全本地运行
7. 说话人分离需在 Hugging Face 申请 `pyannote/speaker-diarization-3.1` 模型访问权限
8. API 服务化建议配置鉴权 Token(如 JWT)保护接口
9. 企业部署建议通过密钥管理服务统一托管

### 可用性分类
10. **分类**: MD+EXEC()
11. **说明**: 基于Markdown的AI Skill,。专业版支持批量处理、GPU 加速与 API 服务化,适合企业级语音转文字生产环境。

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | openai-whisper处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 自定义词典

通过 `initial_prompt` 注入领域术语,显著提升专业内容准确度。

```python
# 法律领域术语
legal_prompt = "以下是法律庭审录音,涉及原告、被告、审判长、诉讼请求、证据质证、法庭辩论等术语。"

result = model.transcribe(
    "court_hearing.wav",
    language="zh",
    initial_prompt=legal_prompt
)
```

### 模型预加载管理

```python
class WhisperModelManager:
    """多模型管理器,支持预加载与热切换"""

    def __init__(self, device="cuda"):
        self.device = device
        self._cache = {}

    def get_model(self, name):
        if name not in self._cache:
            print(f"加载模型 {name}...")
            self._cache[name] = whisper.load_model(name, device=self.device)
        return self._cache[name]

    def preload(self, names):
        for name in names:
            self.get_model(name)

    def clear(self):
        self._cache.clear()

manager = WhisperModelManager(device="cuda")
manager.preload(["small", "medium", "large-v3"])
```

### 批量任务配置

```python
# batch_config.yaml
batch:
  input_dir: "/data/audios"
  output_dir: "/data/transcripts"
  model: "medium"
  device: "cuda"
  language: "zh"
  output_format: "srt"
  initial_prompt: "专业会议转录,术语准确。"
  max_workers: 4          # 并发数
  retry: 3                # 失败重试
  skip_existing: true     # 跳过已处理文件
```

## 常见问题

### Q1: GPU 加速如何启用?

安装 CUDA 版 PyTorch 后,Whisper 会自动检测并使用 GPU。可通过 `--device cuda` 显式指定,或代码中 `whisper.load_model("medium", device="cuda")`。

### Q2: 说话人分离准确度如何?

`pyannote/speaker-diarization-3.1` 在常见场景下准确度可达 85%-95%。影响准确度的因素包括:说话人数量、背景噪声、说话人音色相似度。建议录音时使用多麦克风阵列。

### Q3: 自定义词典如何优化?

通过 `initial_prompt` 注入领域术语与上下文。建议:
- 包含 5-10 句典型领域文本
- 涵盖核心专业术语与缩写
- 使用与目标音频一致的语言风格
- 避免过长(超过 200 tokens 会占用上下文窗口)

### Q4: 批量处理如何避免中断丢失?

- 启用 `skip_existing` 跳过已处理文件
- 记录处理日志与状态文件
- 使用任务队列(Celery)管理失败重试
- 定期备份输出目录

### Q5: API 服务的并发能力?

单 GPU 下建议并发 2-4(取决于模型大小与显存)。多 GPU 可线性扩展。CPU 模式建议串行处理。生产环境建议配合任务队列处理大文件。

### Q6: 专业版与免费版的迁移?

零迁移成本。专业版是免费版的超集,命令行参数完全兼容。升级后原有脚本自动受益于 GPU 加速(若已安装),新特性按需启用。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
