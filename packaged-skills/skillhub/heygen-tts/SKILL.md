---
slug: "heygen-tts"
name: "heygen-tts"
version: "1.0.0"
displayName: "HeyGen TTS专业版"
summary: "企业级HeyGen TTS工具,支持SSML标记、批量生成、词级时间戳与API服务化,适配生产环境。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与企业用户的 HeyGen 文字转语音工具(专业版)。核心能力:
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
  - 视频批...
tags:
  - 创意设计
  - 语音合成
  - TTS
  - HeyGen
  - 企业级
  - 批量处理
  - SSML
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# HeyGen TTS专业版

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

**输入**: 用户提供免费版 vs 专业版对比所需的指令和必要参数。
### TTS 合成

执行TTS 合成操作,处理用户输入并返回结果。

**输入**: 用户提供TTS 合成所需的参数和指令。

**输出**: 返回TTS 合成的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`TTS 合成`相关配置参数进行设置
### 多语言

执行多语言操作,处理用户输入并返回结果。

**输入**: 用户提供多语言所需的参数和指令。

**输出**: 返回多语言的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`多语言`相关配置参数进行设置
#
## 适用场景

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

> 详细代码示例已移至 `references/detail.md`

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

> 详细代码示例已移至 `references/detail.md`

## 使用流程

### 依赖说明

### 运行环境
1. **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
2. **操作系统**: Windows / macOS / Linux
3. **Python**: 3.9 及以上
4. **网络**: 需访问 `api.heygen.com`

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| requests | Python 库 | 必需 | `pip install requests` |
| fastapi | Python 库 | 可选(API 服务) | `pip install fastapi uvicorn` |
| ffmpeg | 音频处理 | 推荐(后处理) | `brew install ffmpeg` |
| Python 3.9+ | 运行时 | 必需 | `python.org` 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
5. 必须配置 `HEYGEN_API_KEY` 环境变量
6. 在 HeyGen 控制台创建,通过 `X-Api-Key` 请求头传递
7. API 服务化建议配置鉴权 Token 保护接口
8. 企业部署建议通过密钥管理服务统一托管
9. 建议监控 API 配额用量,设置预算告警

### 可用性分类
10. **分类**: MD+EXEC()
11. **说明**: 基于Markdown的AI Skill,。专业版支持 SSML、批量生成、词级时间戳与 API 服务化,适合企业级语音内容生产流水线。

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 批量任务配置
```yaml
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
