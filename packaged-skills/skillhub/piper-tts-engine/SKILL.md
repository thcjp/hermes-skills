---

slug: "piper-tts-engine"
name: "piper-tts-engine"
version: 1.0.1
displayName: "本地语音合成专业版"
summary: "企业级本地 TTS 引擎，支持批量合成、自定义音色训练、多语言、SSML 标记与 API 服务化。。面向团队与企业的本地离线文字转语音引擎. 核心能力: 批量合成、自定义音色训练、多语言支持"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  面向团队与企业的本地离线文字转语音引擎.
  核心能力: 批量合成、自定义音色训练、多语言支持、SSML 标记、API 服务化、语音后处理、跨平台部署.
  适用场景: 内容批量配音、多语言客服、有声书制作、无障碍服务、企业通知语音化.
  差异化: 专业版在免费版基础上新增批量处理与音色定制，兼容免费版合成命令与音色模型.
tags:
  - 语音合成
  - 批量TTS
  - 自定义音色
  - 多语言
  - 企业级
  - 有声书
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 知识
  - 文档
  - 写作
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# 本地语音合成专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |
| 数据质量检测与清洗规则 | 不支持 | 支持 |

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 单条文本合成 | 支持 | 支持 |
| 预置音色 | 4 个 | 全部音色库 |
| 批量合成 | - | 支持 |
| 自定义音色训练 | - | 支持 |
| 多语言合成 | 英语为主 | 20+ 语言 |
| SSML 标记 | - | 支持 |
| API 服务化 | - | 支持 |
| 语音后处理（降噪/拼接） | - | 支持 |
| 跨平台（含 Windows 原生） | - | 支持 |
| 语速/音高/音量控制 | 基础 | 精细控制 |
| 优先技术支持 | - | 支持 |
### 单条文本合成

针对单条文本合成,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供单条文本合成相关的配置参数、输入数据和处理选项.
**输出**: 返回单条文本合成的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`单条文本合成`的配置文档进行参数调优
### 预置音色

针对预置音色,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供预置音色相关的配置参数、输入数据和处理选项.
**输出**: 返回预置音色的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`预置音色`的配置文档进行参数调优
### 批量合成

针对批量合成,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供批量合成相关的配置参数、输入数据和处理选项.
**输出**: 返回批量合成的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`批量合成`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：有声书批量章节配音

将一本电子书的全部章节批量转为语音文件，自动拼接为完整有声书.
```python
# batch_tts_audiobook.py
import os
import subprocess
import json
# ...
# 章节配置
chapters = [
    {"id": "ch01", "title": "优秀章 序章",  "file": "book/ch01.txt"},
    {"id": "ch02", "title": "第二章 启程",  "file": "book/ch02.txt"},
    {"id": "ch03", "title": "第三章 相遇",  "file": "book/ch03.txt"},
    {"id": "ch04", "title": "第四章 挑战",  "file": "book/ch04.txt"},
    {"id": "ch05", "title": "第五章 转折",  "file": "book/ch05.txt"},
]
# ...
voice = "zh_CN-huayan-medium"  # 中文音色
output_dir = "audiobook/output"
os.makedirs(output_dir, exist_ok=True)
# ...
# 第1步: 批量合成各章节
results = []
for ch in chapters:
    with open(ch["file"], "r", encoding="utf-8") as f:
        text = f.read().strip()
# ...
    output_path = os.path.join(output_dir, f"{ch['id']}.mp3")
    cmd = [
        "piper-speak-pro",
        "--text", text,
        "--voice", voice,
        "--output", output_path,
        "--speed", "0.95",      # 略慢，适合听书
        "--post-process", "denoise"  # 降噪后处理
    ]
    subprocess.run(cmd, check=True)
    results.append({"chapter": ch["id"], "title": ch["title"], "file": output_path})
    print(f"✅ {ch['title']} 合成完成 -> {output_path}")
# ...
# 第2步: 拼接为完整有声书
concat_file = os.path.join(output_dir, "concat_list.txt")
with open(concat_file, "w", encoding="utf-8") as f:
    for r in results:
        f.write(f"file '{r['file']}'\n")
# ...
full_output = os.path.join(output_dir, "full_audiobook.mp3")
subprocess.run([
    "ffmpeg", "-f", "concat", "-safe", "0",
    "-i", concat_file, "-c", "copy", full_output
], check=True)
# ...
print(f"\n📚 有声书合成完成: {full_output}")
print(f"   共 {len(results)} 章，总时长约 {len(results) * 15} 分钟")
```

### 场景二：SSML 精细控制语音表现

使用 SSML 标记控制停顿、重音与语速，实现专业级语音表现.
```xml
<!-- ssml_input.xml -->
<speak>
  <prosody rate="slow" pitch="-2st">
    欢迎收听今日新闻速递.
  </prosody>
  <break time="500ms"/>
  <prosody rate="normal">
    头条新闻：<emphasis level="strong">人工智能领域迎来重大突破</emphasis>.
  </prosody>
  <break time="300ms"/>
  <prosody rate="fast">
    详细内容请关注后续报道.
  </prosody>
</speak>
```

```bash
# 使用 SSML 合成
piper-speak-pro --ssml ssml_input.xml --voice zh_CN-huayan-medium --output news_broadcast.mp3
```

### 场景三：自定义音色训练

使用自有录音数据训练专属音色，打造品牌统一的声音形象.
```bash
# 第1步: 准备训练数据（至少30分钟清晰录音 + 对应文本）
# audio_samples/  目录存放 WAV 录音
# transcripts/    目录存放对应文本
# ...
# 第2步: 启动音色训练
piper-train-pro \
  --name "BrandVoice-Aria" \
  --language "zh_CN" \
  --audio-dir audio_samples/ \
  --transcript-dir transcripts/ \
  --quality "high" \
  --output-dir models/custom/
# ...
# 训练完成后输出
# 模型路径: models/custom/zh_CN-BrandVoice-Aria-high.onnx
# 配置文件: models/custom/zh_CN-BrandVoice-Aria-high.json
# ...
# 第3步: 使用自定义音色合成
piper-speak-pro \
  --text "欢迎致电客户服务中心，我是您的专属助手。" \
  --voice models/custom/zh_CN-BrandVoice-Aria-high.onnx \
  --output welcome.mp3
```

### 场景四：API 服务化部署

将 TTS 引擎部署为 HTTP API 服务，供团队内部系统调用.
```python
# tts_api_server.py
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import subprocess
import uuid
import os
# ...
app = FastAPI(title="Piper TTS Pro API")
# ...
class TTSRequest(BaseModel):
    text: str
    voice: str = "zh_CN-huayan-medium"
    speed: float = 1.0
    pitch: int = 0
    ssml: str = None
# ...
@app.post("/api/tts")
async def synthesize(req: TTSRequest, bg: BackgroundTasks):
    task_id = str(uuid.uuid4())
    output_path = f"output/{task_id}.mp3"
# ...
    cmd = ["piper-speak-pro", "--output", output_path, "--voice", req.voice]
    if req.ssml:
        cmd += ["--ssml", req.ssml]
    else:
        cmd += ["--text", req.text, "--speed", str(req.speed), "--pitch", str(req.pitch)]
# ...
    bg.add_task(run_synthesis, cmd)
    return {"task_id": task_id, "status": "processing", "output": output_path}
# ...
@app.get("/api/tts/{task_id}")
async def get_status(task_id: str):
    path = f"output/{task_id}.mp3"
    if os.path.exists(path):
        return {"task_id": task_id, "status": "completed", "output": path}
    return {"task_id": task_id, "status": "processing"}
# ...
def run_synthesis(cmd):
    subprocess.run(cmd, check=True)
```

```bash
# 启动 API 服务
uvicorn tts_api_server:app --host 0.0.0.0 --port 8100
# ...
# 示例
curl -X POST http://localhost:8100/api/tts \
  -H "Content-Type: application/json" \
  -d '{"text":"您好，这是一条测试语音","voice":"zh_CN-huayan-medium"}'
```

## 使用流程

1. 安装专业版引擎与音色库.
```bash
（请参考skill目录中的脚本文件） --install-all
```

2. 生成优秀条语音（与免费版命令兼容）.
```bash
（请参考skill目录中的脚本文件） "专业版语音合成已就绪" zh_CN-huayan-medium
```

3. 尝试批量合成.
```bash
piper-speak-pro --batch input_texts.json --voice zh_CN-huayan-medium --output-dir batch_output/
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | piper-tts-engine处理的内容输入 |,  |
| content | string | 否 | piper-tts-engine处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "engine 相关配置参数",
    result: "engine 相关配置参数",
    result: "engine 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS（Apple Silicon + Intel）/ Linux
- **运行时**：Python 3.9+
- **GPU（可选）**：NVIDIA GPU + CUDA（音色训练推荐）

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Python 3.9+ | 运行时 | 必需 | python.org 官方下载 |
| piper-tts-pro | Python 包 | 必需 | `pip install piper-tts-pro`（安装脚本自动处理） |
| onnxruntime | Python 包 | 必需 | `pip install onnxruntime`（自动安装） |
| FFmpeg | 工具 | 推荐 | 系统包管理器安装，音频拼接与后处理 |
| FastAPI | Python 包 | 可选 | `pip install fastapi uvicorn`，API 服务化 |
| CUDA Toolkit | GPU 驱动 | 可选 | NVIDIA 官网下载，音色训练加速 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 专业版本地合成无需 API Key.
- 若部署 API 服务，在 `api_server.auth_token` 中设置鉴权令牌.
- 若使用云端 GPU 训练音色，需配置对应云服务商的 API 凭证.
```bash
# 环境变量示例
export PIPER_PRO_LICENSE="your_pro_license"
export PIPER_API_TOKEN="your_api_auth_token"
export CUDA_HOME="/usr/local/cuda"  # GPU训练需要
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务。专业版在免费版基础上新增批量合成、音色训练与 API 服务化，合成命令与音色模型向后兼容免费版.
## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：专业版如何兼容免费版？

专业版与免费版使用相同的底层 Piper 引擎。免费版的合成命令、音色模型与配置可直接在专业版中使用，升级后已有音色自动识别.
### Q2：自定义音色训练需要多少数据？

最低要求 30 分钟清晰录音与对应文本转录。数据越多、质量越高，训练出的音色越自然。推荐 1-2 小时高质量数据.
### Q3：SSML 支持哪些标记？

专业版支持以下 SSML 标记：
- `<speak>`：根元素
- `<break time="...">`：停顿
- `<prosody rate/pitch/volume>`：语速/音高/音量
- `<emphasis level="...">`：重音
- `<say-as>`：特殊读法（数字、日期等）

### Q4：批量合成时如何处理超长文本？

专业版自动将超长文本按句子分段合成，再拼接为完整文件。通过 `batch.chunk_size` 控制分段大小（默认 500 字符）.
### Q5：API 服务支持并发请求吗？

支持。通过 `engine.max_workers` 控制并发合成任务数（默认 4）。建议根据服务器 CPU 配置调整.
### Q6：专业版支持 Windows 原生运行吗？

支持。专业版提供 Windows 原生支持，无需 WSL。安装脚本会自动检测操作系统并选择对应的二进制文件.
### Q7：音色训练需要什么硬件？

- 最低：8GB 内存，CPU 训练（耗时较长，约 4-8 小时）
- 推荐：16GB+ 内存，NVIDIA GPU（CUDA 支持），训练时间约 1-2 小时
- 高质量模型训练建议使用 GPU

### Q8：如何实现多语言混合合成？

在 SSML 中使用 `<voice>` 标记切换音色，实现多语言混合合成.
```xml
<speak>
  <voice name="zh_CN-huayan-medium">欢迎来到</voice>
  <voice name="en_US-ryan-high">New York</voice>
  <voice name="zh_CN-huayan-medium">，祝您旅途愉快。</voice>
</speak>
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 本地运行，不支持多设备同步
