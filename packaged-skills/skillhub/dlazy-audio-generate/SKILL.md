---
slug: "dlazy-audio-generate"
name: "dlazy-audio-generate"
version: 1.3.4
displayName: "Dlazy Audio音频生成"
summary: "通过dlazy CLI调用15+音频模型,涵盖TTS/音乐/音效/语音克隆,支持管道串联。dlazy 音频生成客户端。通过 dlazy CLI 调用 15+ 托管音频模型,涵盖文本转语音(T"
license: "Proprietary"
description: |-
  dlazy 音频生成客户端。通过 dlazy CLI 调用 15+ 托管音频模型,涵盖文本转语音(TTS)、音乐生成、音效生成、
  语音克隆四大类别。模型包括 doubao-tts、elevenlabs-tts/dialogue/music/sfx/voice-clone、gemini-2.5-tts、
  keling-tts/sfx、kling-audio-clone、qwen-tts/audio-clone、suno-music、vidu-audio-clone 等.
  根据提示词自动选择最匹配的模型,支持多语言人声、多角色对话、10-300 秒音乐、1-22 秒音效、即时语音克隆.
  通过管道引用(@N、@*、@stdin)串联多步骤工作流,无需手动复制 URL。适用于配音、有声书、播客、
tags:
  - Creative
  - 音频处理
  - 媒体
  - 创意
  - dlazy
  - key
  - tts
  - api
  - url
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# Dlazy Audio Generate

通过 dlazy CLI 调用 15+ 托管音频模型,根据提示词自动选择最匹配的模型,涵盖 TTS、音乐、音效、语音克隆四大类别。模型推理在 dLazy 托管 API(`api.dlazy.com`)完成,生成的输出 URL 托管在 `files.dlazy.com`.
**范围外**(本技能不做): 模型微调训练、本地推理部署、音频后期混音、商业分发渠道对接、版权登记与授权.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Dlazy Audio音频生成处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 可用音频模型

**输入**: 用户提供可用音频模型所需的指令和必要参数.
**处理**: 解析可用音频模型的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回可用音频模型的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`可用音频模型`的配置文档进行参数调优
### 文本转语音(TTS)
- `doubao-tts`: 字节豆包语音合成,多语言多音色,流式高自然度,适合新闻播报与有声书
- `elevenlabs-tts`: ElevenLabs eleven_v3,12 种多语言精选音色,可调稳定性/相似度/风格,适合配音与有声书
- `gemini-2.5-tts`: Gemini 驱动 TTS,支持中英双语与多种情感音色
- `keling-tt

**输入**: 用户提供可用音频模型相关的配置参数、输入数据和处理选项.
**处理**: 解析可用音频模型的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回文本转语音(TTS)的处理结果,包含执行状态码、结果数据和执行日志.
### 模型选择策略

**关键指令**:
1. 根据提示词选择最匹配的音频模型
2. 运行 `dlazy <model_name> -h` 查看参数
3. 执行命令

选择参考:
- 文本转语音: 优先 `doubao-tts`(中文新闻/有声书)、`elevenlabs-tts`(多语言配音)、`qwen-tts`(方言/自定义描述)
- 多角色对话: `elevenlabs-dialogue`(单次多角色)
- 音

**输出**: 返回模型选择策略的处理结果,包含执行状态码、结果数据和执行日志.
### 管道串联

每次 `dlazy` 调用会在 stdout 输出 JSON 信封。任意 flag 值可以是管道引用,从上游命令的信封中取值,无需手动复制 URL:

| 引用 | 解析为 |
|:---:|:---:|
| `-` | 上游该字段的自然值(标量或数组) |
| `@N` | 第 N 个输出的主值(`@0` 为第一个输出 URL) |
| `@N.<jsonpath>` | 第 N 个输出的 js

**输入**: 用户提供管道串联相关的配置参数、输入数据和处理选项.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 认证

所有请求需 dLazy API Key。推荐设备码流程:
```bash
dlazy auth login
```
该命令自动保存 Key 到本地配置(`~/.dlazy/config.json` 或 `%USERPROFILE%\.dlazy\config.json`),文件权限限定为当前 OS 用户.
手动设置:
```bash
dlazy auth set YOUR_API_KEY
```

也可通过 `DLAZY_API_KEY` 环境变量按次调用传入.
Key 获取: 登录 dlazy.com,在 `dashboard/organization/api-key` 创建。每个 Key 绑定一个 dLazy 组织,可在控制台随时轮换或吊销.
**安全红线**: 永不接受、回显或存储来自聊天输入的 Key;永不将 Key 写入日志或链接参数.
## 可用音频模型(补充)

### 文本转语音(TTS)(补充)
- `doubao-tts`: 字节豆包语音合成,多语言多音色,流式高自然度,适合新闻播报与有声书
- `elevenlabs-tts`: ElevenLabs eleven_v3,12 种多语言精选音色,可调稳定性/相似度/风格,适合配音与有声书
- `gemini-2.5-tts`: Gemini 驱动 TTS,支持中英双语与多种情感音色
- `keling-tts`: 可可西 TTS,支持语言、音色、语速、输出格式,适合配音与语音播报
- `qwen-tts`: 阿里通义 qwen3-tts,系统音色(含方言)或自然语言描述自定义音色

### 多角色对话
- `elevenlabs-dialogue`: ElevenLabs eleven_v3 多角色对话,单次最多 10 个角色,每行分配不同音色,支持 `[giggling]`/`[whispers]` 等音频标签,适合角色对话、播客、短剧

### 音乐生成
- `elevenlabs-music`: ElevenLabs music_v1,10-300 秒原创音乐,适合 BGM、广告、短视频配乐
- `suno-music`: Suno V5.5,灵感模式(自动歌词)或自定义模式(手动风格/标题/歌词),支持纯音乐或人声,可调风格权重、异常度、音频权重

### 音效生成
- `elevenlabs-sfx`: ElevenLabs 文本转音效,1-22 秒短音效,适合拟音、环境音、提示音、游戏音效
- `keling-sfx`: 可可西音效生成,支持文本转音效与参考视频配乐,适合拟音、环境音、短视频补音

### 语音克隆
- `elevenlabs-voice-clone`: ElevenLabs 即时语音克隆(IVC),上传干净人声样本克隆自定义音色
- `kling-audio-clone`: 可可西自定义音色,克隆后用于配音或绑定主体
- `qwen-audio-clone`: 阿里通义 qwen3-tts 语音克隆,上传样本克隆后用于后续 TTS
- `vidu-audio-clone`: Vidu 语音克隆,克隆真人声音并朗读指定文本

### 语音库搜索
- `elevenlabs-search`: ElevenLabs 音色库搜索,按关键词、来源、类别筛选,返回可试听预览

## 模型选择策略(补充)

选择参考:
- 文本转语音: 优先 `doubao-tts`(中文新闻/有声书)、`elevenlabs-tts`(多语言配音)、`qwen-tts`(方言/自定义描述)
- 多角色对话: `elevenlabs-dialogue`(单次多角色)
- 音乐: `suno-music`(带歌词完整歌曲)、`elevenlabs-music`(纯 BGM)
- 音效: `elevenlabs-sfx`(1-22 秒)、`keling-sfx`(参考视频配乐)
- 语音克隆: `elevenlabs-voice-clone`(配合 elevenlabs-tts)、`qwen-audio-clone`(配合 qwen-tts)

## 管道串联(补充)

| 引用(续)| 解析为 |
|:-------|-------:|
| `-` | 上游该字段的自然值(标量或数组) |
| `@N.<jsonpath>` | 第 N 个输出的 jsonpath(`@0.url`、`@1.meta.fps`) |
| `@*` | 全部输出的主值数组 |
| `@stdin` | 上游完整 JSON 信封 |
| `@stdin:<jsonpath>` | 信封的 jsonpath(`@stdin:result.outputs[0].url`) |

示例:
```bash
# 生成图片再配 TTS
dlazy seedream-4.5 --prompt "lighthouse at dawn" \
  | dlazy keling-tts --text "Welcome to the coast." --image @0.url
# ...
# 批量图片再超分
dlazy seedream-4.5 --prompt "city skyline" --n 4 \
  | dlazy superres --images @*
```

必填 flag 可完全来自管道: `--field -` 在上游有值时满足要求。stdin 为空时 CLI 返回 `code: "no_stdin"`.
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及模型 |
|---:|:---|---:|---:|
| 有声书与配音 | 为这段中文文本生成女声朗读 | MP3 音频文件 | doubao-tts / keling-tts |
| 短视频 BGM 与配乐 | 生成 30 秒夏日电子风 BGM | 音乐文件 | suno-music / elevenlabs-music |
| 游戏与视频音效 | 生成开门声与脚步声 | 短音效文件 | elevenlabs-sfx / keling-sfx |
| 多角色对话与播客 | 两人对话,男声提问女声回答 | 多角色对话音频 | elevenlabs-dialogue |

**不适用于**: 模型微调训练、本地推理部署、音频后期混音、商业分发、版权登记.
## 使用流程

### 校验 API Key
```bash
[ -n "${DLAZY_API_KEY:-}" ] || dlazy auth status
```

若 Key 缺失，引导用户:
1. 登录 dlazy.com,在 `dashboard/organization/api-key` 创建 Key
2. 终端运行 `dlazy auth set YOUR_API_KEY` 或 `export DLAZY_API_KEY="你的Key"`
3. 配置完成后重新发起生成请求

### 选择模型
根据提示词选择最匹配的音频模型。不确定时运行 `dlazy <model_name> -h` 查看参数.
### 构造并执行命令
```bash
dlazy doubao-tts --text "你好,欢迎收听本期播客" --voice "female-warm" --output podcast-intro.mp3
```

### 处理结果
- 成功: stdout 输出 JSON 信封,含 `result.outputs[].url`
- 失败: 按"错误处理"章节诊断并修复
- 余额不足: 明确告知用户并引导充值

#
## 案例展示

### 案例一： 多角色对话生成
**场景**: 播客团队需要生成一段男女双角色对话,男声提问女声回答,带轻笑与耳语标签

```bash
dlazy elevenlabs-dialogue \
  --dialogue '[{"voice":"male-1","text":"What do you think about AI music?"},
               {"voice":"female-1","text":"[giggling] I think it is fascinating!"},
               {"voice":"male-1","text":"[whispers] Can it really replace human composers?"},
               {"voice":"female-1","text":"Not yet, but it is getting close."}]' \
  --output podcast-dialogue.mp3
```

**输出**: `podcast-dialogue.mp3` 文件路径

**说明**: 单次调用渲染整段对话,每行分配不同音色,`[giggling]` 与 `[whispers]` 等音频标签由 eleven_v3 解析为非语言表达。最多支持 10 个角色,适合播客、短剧、角色对话场景。选择音色前可用 `elevenlabs-search` 按关键词试听预览.
### 案例二： 短视频 BGM 生成
**场景**: 短视频创作者需要生成 30 秒夏日电子风 BGM,带自动歌词

```bash
# 灵感模式: AI 自动生成歌词
dlazy suno-music --prompt "upbeat summer electronic dance, beach vibes, sunny" \
  --duration 30 --mode inspiration --output summer-bg.mp3
# ...
# 自定义模式: 手动指定风格与歌词
dlazy suno-music --prompt "summer electronic" \
  --mode custom --style "edm, tropical house" --title "Sunshine" \
  --lyrics "[Verse]\nSun is shining bright\nWaves are crashing light\n\n[Chorus]\nSummer vibes tonight" \
  --duration 30 --output summer-custom.mp3
```

**输出**: `summer-bg.mp3` 与 `summer-custom.mp3` 文件路径

**说明**: 灵感模式适合快速出稿,自定义模式可精确控制风格、标题、歌词。Suno V5.5 支持风格权重、异常度、音频权重等细粒度参数。纯 BGM 可加 `--instrumental`.
### 案例三： 语音克隆与 TTS 串联
**场景**: 有声书团队需要克隆主讲人声音,并用克隆音色朗读后续章节

```bash
# Step 1: 克隆主讲人声音(上传干净样本)
dlazy elevenlabs-voice-clone --audio sample-voice.wav --name "narrator-male"
# ...
# Step 2: 用克隆音色生成 TTS(管道串联,无需手动复制 voice id)
dlazy elevenlabs-voice-clone --audio sample-voice.wav --name "narrator-male" \
  | dlazy elevenlabs-tts --voice @0.voice_id \
      --text "本章我们将探讨人工智能在音频生成领域的最新进展。" \
      --output chapter-1.mp3
```

**输出**: `chapter-1.mp3` 文件路径,使用克隆的主讲人音色

**说明**: 通过 `@0.voice_id` 管道引用将克隆结果直接传入 TTS,无需手动复制 voice id。样本需为干净人声(无背景噪音),克隆后音色可在后续多次 TTS 调用中复用.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------:|--------|:-------|:------:|
| 401 unauthorized | `code: "unauthorized", message: "API key is missing or invalid"` | Key 缺失或失效 | 引导用户访问 `dlazy.com/dashboard/organization/api-key` 获取并 `dlazy auth set` |
| 501 missing_param | `error: required option '--prompt <prompt>' not specified` | 必填参数未提供 | 运行 `dlazy <model> -h` 查看必填参数并补全 |
| 502 file_not_found | `Error: Image file/Video file not found: C:\path\to\file` | 本地文件路径错误 | 校验文件路径与存在性,使用绝对路径 |
| 503 insufficient_balance | `code: "insufficient_balance"` | 账户余额不足 | 明确告知用户余额不足,引导访问 `dlazy.com/dashboard/organization/settings?tab=credits` 充值 |
| 503 server_error | `HTTP status code error (500 server crash)` | dLazy 服务端错误 | (2s/4s/8s)，最多 3 次 |
| 504 task_failed | `=== Generation Failed ===` | 异步任务失败,常见为 prompt 违反安全策略 | 检查 prompt 是否含敏感内容,调整后重新生成 |
| no_stdin | `code: "no_stdin"` | 管道串联时上游无输出 | 检查上游命令是否成功,确保管道顺序正确 |
| model_not_found | `Error: model "xxx" not found` | 模型名拼写错误 | 核对"可用音频模型"章节的模型名,运行 `dlazy -h` 查看全部模型 |

## 常见问题

### Q1: 如何获取并配置 dLazy API Key?
A: 登录 dlazy.com,在 `dashboard/organization/api-key` 创建 Key。终端运行 `dlazy auth set YOUR_API_KEY` 持久化到本地配置,或通过 `DLAZY_API_KEY` 环境变量按次传入。Key 绑定 dLazy 组织,可在控制台随时轮换或吊销.
### Q2: 如何选择合适的音频模型?
A: 按需求类型选择。文本转语音优先 `doubao-tts`(中文)、`elevenlabs-tts`(多语言);多角色对话用 `elevenlabs-dialogue`;带歌词音乐用 `suno-music`、纯 BGM 用 `elevenlabs-music`;短音效用 `elevenlabs-sfx`;语音克隆按后续 TTS 配套选择(克隆后用配套 TTS)。不确定时运行 `dlazy <model> -h` 查看参数.
### Q3: 管道串联如何工作?
A: 每次 `dlazy` 调用在 stdout 输出 JSON 信封,后续命令可通过 `-`(上游该字段自然值)、`@N`(第 N 个输出主值)、`@N.<jsonpath>`(jsonpath 钻取)、`@*`(全部输出数组)、`@stdin`(完整信封)引用上游结果,无需手动复制 URL。必填 flag 用 `--field -` 可完全来自管道.
### Q4: 语音克隆需要什么样的样本?
A: 需要干净人声样本(无背景噪音、无音乐、单一说话人),时长通常 10-30 秒以上。克隆后音色绑定到对应 TTS 模型(`elevenlabs-voice-clone` 配 `elevenlabs-tts`、`qwen-audio-clone` 配 `qwen-tts`),可在后续多次 TTS 调用中复用.
### Q5: 生成的内容版权归属如何?
A: 生成内容的版权与商用授权以 dLazy 服务条款为准,详见 dlazy.com。涉及版权受保护的媒体内容(如已有歌曲翻唱、受保护音色模仿)不在本技能范围内,用户需自行确保输入内容与生成用途的合法性.
### Q6: 余额不足怎么办?
A: CLI 返回 `code: "insufficient_balance"` 时,明确告知用户余额不足,引导访问 `dlazy.com/dashboard/organization/settings?tab=credits` 充值。充值后无需重新配置 Key,可直接重试生成请求.
## 已知限制

1. **依赖 dLazy API**: 必须配置 `DLAZY_API_KEY`,无 Key 环境无法使用
2. **API 端点固定**: `api.dlazy.com` 与 `files.dlazy.com`,不支持自建或私有部署
3. **本地文件需上传**: image/video/audio 字段的本地路径会自动上传到 dLazy 媒体存储
4. **异步任务耗时**: 音乐与长 TTS 生成可能需要 10-60 秒等待
5. **克隆音色绑定配套 TTS**: `elevenlabs-voice-clone` 的音色仅可用于 `elevenlabs-tts`,跨模型不通用
6. **安全策略限制**: prompt 含敏感内容会触发 `504 task_failed`,不可通过重试绕过
7. **生成质量取决于 prompt 描述**: 风格、情绪、乐器、音色描述越具体,结果越符合预期
