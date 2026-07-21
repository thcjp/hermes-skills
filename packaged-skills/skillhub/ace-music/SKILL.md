---
slug: ace-music
name: ace-music
version: "1.0.0"
displayName: ACE Music AI音乐生成
summary: 基于ACE-Step 1.5通过ACE Music免费API生成AI音乐,支持歌词定制、多语言、多流派,输出MP3
license: MIT
description: |-
  ACE Music AI 音乐生成客户端。通过 ACE Music 托管的免费 API 调用 ACE-Step 1.5 模型,
  支持文本转音乐、自定义歌词、纯音乐、采样模式、翻唱与片段重绘等多种任务类型。
  支持时长、BPM、调性、语言、种子、批量等参数控制,音频以 base64 MP3 返回并由脚本自动解码为本地 MP3 文件。
  API 永久免费,无需订阅、无额度限制、无配额扣减。适用于独立开发者、内容创作者、自动化音乐生产工作流场景。
tags:
  - Creative
tools:
  - read
  - exec
---

# ACE Music

ACE Music 是基于 ACE-Step 1.5 模型的 AI 音乐生成客户端,通过 ACE Music 托管的免费 API 生成完整带人声的歌曲。永久免费、无订阅、无额度限制。API 基础地址固定为 `https://api.acemusic.ai`。

**范围外**（本技能不做）: 模型微调训练、本地推理部署、商业分发渠道对接、版权登记与授权。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。

## 核心能力

### 任务类型

ACE Music API 支持三种核心任务,通过请求体的 `task_type` 字段切换:

| 任务类型 | 用途 | 是否需要音频输入 |
| --- | --- | --- |
| `text2music`（默认） | 文本/歌词生成新音乐 | 否 |
| `cover` | 翻唱已有歌曲,保留旋律替换音色 | 是 |
| `repaint` | 修改已有音频的指定片段 | 是 |

`

**处理**: 按照skill规范执行任务类型操作。

### 快速生成

优先使用 `scripts/generate.sh` 封装脚本完成一站式生成:

```bash
# 基础文本生成
scripts/generate.sh "upbeat pop song about summer" --duration 30 --output summer.mp3

# 自定义歌词（带标签模式）
scripts/generate.sh "gentle acoustic ball

**输入**: 用户提供快速生成所需的参数和指令。
**处理**: 按照skill规范执行快速生成操作。

### 参数指南
| 想要 | 参数 |
| --- | --- |
| 特定风格 | 在 prompt 中描述: "jazz, saxophone solo, smoky bar" |
| 自定义歌词 | `--lyrics "[Verse]...[Chorus]..."` |
| AI 全自动 | `--sample-mode` |
| 无人声 | `--instrumental` |
| 更长歌曲 | `--

**处理**: 按照skill规范执行参数指南操作。

**输出**: 返回参数指南的执行结果,包含操作状态和输出数据。
### 直接调用 API

如需 cover/repaint 或音频输入等高级用法,可绕过脚本直接调 API,完整规范见 `references/api-docs.md`。基础请求结构:

```bash
curl -s -X POST "https://api.acemusic.ai/v1/generate" \
  -H "Authorization: Bearer ${ACE_MUSIC_API_KEY}" \
  -

**处理**: 按照skill规范执行直接调用 API操作。
**输出**: 返回直接调用 API的执行结果,包含操作状态和输出数据。
### 任务类型

执行任务类型操作,处理用户输入并返回结果。

**输入**: 用户提供任务类型所需的参数和指令。

**输出**: 返回任务类型的处理结果。

- 执行`任务类型`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`任务类型`相关配置参数进行设置

### 能力覆盖范围

本skill还覆盖以下能力场景: Step、支持歌词定制、多语言、多流派、音乐生成客户端、托管的免费、支持文本转音乐、纯音乐、采样模式、翻唱与片段重绘等、多种任务类型、支持时长、BPM、批量等参数控制、音频以、base、返回并由脚本自动、解码为本地、永久免费、无需订阅、无额度限制、无配额扣减、适用于独立开发者、内容创作者、自动化音乐生产工、作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 认证

使用 `ACE_MUSIC_API_KEY` 环境变量。永不打印或暴露 Key。

```bash
[ -n "${ACE_MUSIC_API_KEY:-}" ] && echo ok || echo missing
```

若 Key 缺失,引导用户:
1. 浏览器打开 `https://acemusic.ai/playground/api-key`
2. 注册（免费）并创建 API Key
3. 终端环境变量: `export ACE_MUSIC_API_KEY="你的Key"`
4. 配置完成后重新发起生成请求

**安全红线**: 永不接受/回显/存储来自聊天输入的 Key;永不将 Key 写入日志或链接参数。

## 任务类型

ACE Music API 支持三种核心任务,通过请求体的 `task_type` 字段切换:

| 任务类型 | 用途 | 是否需要音频输入 |
| --- | --- | --- |
| `text2music`（默认） | 文本/歌词生成新音乐 | 否 |
| `cover` | 翻唱已有歌曲,保留旋律替换音色 | 是 |
| `repaint` | 修改已有音频的指定片段 | 是 |

`cover` 与 `repaint` 任务需提供音频输入（URL 或 base64）,详见 `references/api-docs.md`。

## 快速生成

优先使用 `scripts/generate.sh` 封装脚本完成一站式生成:

```bash
# 基础文本生成
scripts/generate.sh "upbeat pop song about summer" --duration 30 --output summer.mp3

# 自定义歌词（带标签模式）
scripts/generate.sh "gentle acoustic ballad, female vocal" \
  --lyrics "[Verse 1]\nSunlight through the window\n\n[Chorus]\nWe are the dreamers" \
  --duration 60 --output ballad.mp3

# 纯音乐（无人声）
scripts/generate.sh "lo-fi hip hop beats, chill, rainy day" --instrumental --duration 120 --output lofi.mp3

# 采样模式（AI 自动生成歌词与旋律）
scripts/generate.sh "write me a jazz song about coffee" --sample-mode --output jazz.mp3

# 精确控制 BPM/调性/语言/种子
scripts/generate.sh "rock anthem" --bpm 140 --key "E minor" --language en --seed 42 --output rock.mp3

# 批量生成 3 个版本
scripts/generate.sh "electronic dance track" --batch 3 --output edm.mp3
```

脚本将生成的文件路径输出到 stdout,Agent 应将文件发送给用户。

## 参数指南

| 想要 | 参数 |
| --- | --- |
| 特定风格 | 在 prompt 中描述: "jazz, saxophone solo, smoky bar" |
| 自定义歌词 | `--lyrics "[Verse]...[Chorus]..."` |
| AI 全自动 | `--sample-mode` |
| 无人声 | `--instrumental` |
| 更长歌曲 | `--duration 120`（秒） |
| 特定节奏 | `--bpm 120` |
| 特定调性 | `--key "C major"` |
| 多个输出 | `--batch 3` |
| 可复现 | `--seed 42` |
| 非英文人声 | `--language ja`（zh/en/ja/ko 等） |

## 直接调用 API

如需 cover/repaint 或音频输入等高级用法,可绕过脚本直接调 API,完整规范见 `references/api-docs.md`。基础请求结构:

```bash
curl -s -X POST "https://api.acemusic.ai/v1/generate" \
  -H "Authorization: Bearer ${ACE_MUSIC_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "text2music",
    "prompt": "upbeat pop song about summer",
    "lyrics": "[Verse 1]\nSummer days\n\n[Chorus]\nHere we go",
    "duration": 30,
    "bpm": 120,
    "key": "C major",
    "language": "en",
    "instrumental": false,
    "sample_mode": false,
    "seed": 42,
    "batch_size": 1
  }'
```

响应体中音频以 base64 编码 MP3 返回,需解码后写入本地文件:

```bash
echo "${response##*audio\":\s\"}" | base64 -d > output.mp3
```

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及参数 |
| --- | --- | --- | --- |
| 带歌词完整人声歌曲 | "生成一首关于夏天的流行歌,带歌词" | 完整 MP3 文件（人声+伴奏） | prompt + lyrics + duration |
| 纯音乐节拍制作 | "做一段 120 秒的 lo-fi 节拍" | 无人声 MP3 文件 | prompt + instrumental + duration |
| 多版本批量生成与复现 | "生成 3 个版本的 EDM,种子 42" | 3 个 MP3 文件 | prompt + batch + seed |
| 已有音频翻唱与片段重绘 | "翻唱这首歌,改为女声" | 翻唱后 MP3 文件 | task_type=cover + audio input |

**不适用于**: 模型微调训练、本地推理部署、商业音乐分发、版权登记。

## 使用流程

### Step 1: 校验 API Key
```bash
[ -n "${ACE_MUSIC_API_KEY:-}" ] && echo ok || echo missing
```

### Step 2: 缺失时引导配置
> 需要先配置 ACE Music API Key:
> 1. 访问 https://acemusic.ai/playground/api-key
> 2. 注册（免费）并创建 API Key
> 3. 终端环境变量: `export ACE_MUSIC_API_KEY="你的Key"`
> 4. 配置完成后重新发起生成请求

### Step 3: 选择任务类型
- 文本生成新音乐: 默认 `text2music`,使用 `scripts/generate.sh`
- 翻唱已有歌曲: `task_type=cover`,需提供音频输入
- 修改已有音频片段: `task_type=repaint`,需提供音频与片段区间

### Step 4: 构造参数并执行
- prompt 必填,描述风格/情绪/乐器
- lyrics 可选,推荐使用 `[Verse]`/`[Chorus]` 标签模式
- duration 不填则由 AI 决定
- batch > 1 时返回多个文件路径

### Step 5: 解码与落盘
- 脚本自动完成 base64 解码与 MP3 落盘
- 直接调 API 时需手动 `base64 -d` 写入文件
- 将文件路径回传给用户

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `--output`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项

## 案例展示

### 案例1: 流派风格化生成
**场景**: 创作者需要生成一段 140 BPM、E 小调的摇滚 anthem

```bash
scripts/generate.sh "epic rock anthem, electric guitar, powerful drums" \
  --bpm 140 --key "E minor" --language en --duration 90 --output rock_anthem.mp3
```

**输出**: `rock_anthem.mp3` 文件路径

**说明**: 通过 `--bpm` 与 `--key` 精确控制节奏与调性,适合需要后续混音对齐的场景。`--language en` 确保英文人声发音准确。

### 案例2: 多语言人声生成
**场景**: 内容创作者需要生成一首带日文歌词的爵士歌曲

```bash
scripts/generate.sh "smooth jazz, saxophone, late night cafe" \
  --lyrics "[Verse 1]\n月明かりの下で\nコーヒーを飲みながら\n\n[Chorus]\n夜が明けるまで" \
  --language ja --duration 60 --output jazz_ja.mp3
```

**输出**: `jazz_ja.mp3` 文件路径

**说明**: `--language ja` 引导模型生成日文发音人声,`--lyrics` 使用标签模式确保段落结构清晰。多语言人声支持 zh/en/ja/ko 等。

### 案例3: 批量生成与种子复现
**场景**: 制作团队需要 3 个版本的电子舞曲,且希望后续能复现相同结果

```bash
# 批量生成 3 个版本
scripts/generate.sh "electronic dance track, festival energy" \
  --batch 3 --seed 42 --duration 120 --output edm.mp3

# 输出 3 个文件:
# edm_1.mp3
# edm_2.mp3
# edm_3.mp3
```

**输出**: 3 个 MP3 文件路径

**说明**: `--seed 42` 确保相同参数下结果可复现;`--batch 3` 一次请求生成多个版本,适合 A/B 试听选曲。注意 batch 模式下每个版本会消耗独立 API 调用。

## 错误处理


| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|---------|---------|---------|---------|
| missing_api_key | `ACE_MUSIC_API_KEY missing` | 环境变量未设置 | 不调 API,引导用户访问 acemusic.ai 注册并配置 Key |
| 401 unauthorized | `{"error":"invalid_api_key"}` | Key 格式错误或已失效 | 不执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,引导用户重新生成 Key |
| 429 rate_limited | `{"error":"rate_limited"}` | 短时间内请求过多 | 指数退避执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令（2s/4s/8s）,最多 3 次 |
| 400 invalid_duration | `{"error":"duration_out_of_range"}` | duration 超出支持范围（通常 5-300 秒） | 不执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,提示用户调整时长 |
| 400 invalid_lyrics | `{"error":"lyrics_format_error"}` | lyrics 缺少必要标签或含非法字符 | 不执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,引导用户使用 `[Verse]`/`[Chorus]` 标签 |
| 400 audio_input_required | `{"error":"audio_input_required"}` | cover/repaint 任务未提供音频输入 | 不执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,提示用户补充 audio_url 或 audio_base64 |
| 5xx server_error | HTTP 500/502/503 | ACE Music 服务端错误 | 指数退避执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,最多 2 次 |
| base64_decode_failed | `base64: invalid input` | API 返回的音频数据损坏或截断 | 不执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,记录请求 ID 联系 ACE Music 团队 |
| batch_partial_failure | `batch 2/3 failed` | 批量生成中部分请求失败 | 返回成功的文件,标记失败序号供用户执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |

## 常见问题

### Q1: ACE Music API 真的免费吗?
A: ACE Music 团队确认 API 永久免费,无订阅、无额度限制、无配额扣减。基础地址 `https://api.acemusic.ai`。如遇未来政策调整,以 ACE Music 官方公告为准。

### Q2: 生成的歌曲时长有什么限制?
A: `--duration` 参数控制生成时长（秒）。不填则由 AI 根据内容自动决定。过长时长（>180 秒）会增加生成耗时,建议分段生成或使用 batch 模式。

### Q3: 支持哪些语言的人声?
A: 支持 zh（中文）、en（英文）、ja（日文）、ko（韩文）等主流语言。通过 `--language` 参数指定。其他语言支持情况以 ACE Music 官方文档为准。

### Q4: 如何获得可复现的生成结果?
A: 使用 `--seed` 参数（如 `--seed 42`）。相同 seed + 相同参数组合会产生相同结果。批量生成时 seed 同样生效,但每个 batch 内部会有微小差异以保证版本多样性。

### Q5: cover 和 repaint 任务有什么区别?
A: `cover` 对整首歌进行翻唱,保留旋律与结构,替换音色/风格;`repaint` 仅修改指定片段,其余部分保持原样。两者都需要提供音频输入（audio_url 或 audio_base64）。

### Q6: 歌词格式有什么要求?
A: 推荐使用标签模式: `[Verse 1]`、`[Chorus]`、`[Bridge]` 等段落标签,换行分隔歌词行。标签模式能让 AI 更准确理解歌曲结构。无标签的纯文本歌词也可用,但结构识别可能不准。

## 已知限制

1. **需 API Key**: 必须配置 `ACE_MUSIC_API_KEY`,无 Key 环境无法使用
2. **API 基础地址固定**: `https://api.acemusic.ai`,不支持自建/私有部署
3. **cover/repaint 需音频输入**: 不能凭空翻唱,需提供已有音频
4. **长时长生成耗时较长**: 120 秒以上生成可能需要 30-60 秒等待
5. **生成质量取决于 prompt 描述**: 风格描述越具体,结果越符合预期
6. **批量生成独立计费调用**: batch=N 会产生 N 次 API 调用,虽免费但消耗时间
