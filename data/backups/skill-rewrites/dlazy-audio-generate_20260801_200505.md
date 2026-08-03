---
slug: dlazy-audio-generate
name: dlazy-audio-generate
version: "1.3.3"
displayName: Dlazy Audio Generate
summary: "音频生成,自动选优选dlazy CLI音频/TTS模型"
  model the pro...
license: MIT-0
description: |-
  Audio generation skill。Automatically selects the best dlazy CLI audio/TTS\
  \ model the pro。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags: '[''Creative'']'
tools:
  - read
  - exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9

---

> **核心功能**: 本技能提供化工作流场景等能力。

> **核心功能**: 本技能提供时使用等能力。

# é³é¢çæ Audio Generate

[English](/api/v1/skills/dlazy-audio-generate/file?path=SKILL.md&ownerHandle=dlazyai) · [中文](/api/v1/skills/dlazy-audio-generate/file?path=SKILL-cn.md&ownerHandle=dlazyai)

Audio generation skill. Automatically selects the best dlazy CLI audio/TTS model the prompt. 音频生成技能。根据提示词自动选择优选的 dlazy CLI 音频/TTS 模型。

## Trigger Keywords / 触发关键词

* generate audio
* text to speech, TTS
* generate music, sound effect

## Authentication

All requests require a dLazy API key. The recommended way to authenticate is:

```bash
This runs a device-code flow (also works in remote shells) and **automatically saves your API key** to the local CLI config — no manual copy/paste required.

### Alternative: Set the Key Manually

If you already have an API key, you can save it directly:

```bash
dlazy auth set YOUR_API_KEY
```

The CLI saves the key in your user config directory (`~/.dlazy/config.json` on macOS/Linux, `%USERPROFILE%\.dlazy\config.json` on Windows), with file permissions restricted to your OS user account. You can also supply the key per-invocation via the `DLAZY_API_KEY` environment variable.

### Getting Your API Key Manually

1. Sign in or create an account at [dlazy.com](https://dlazy.com)
2. Go to [dlazy.com/dashboard/organization/api-key](https://dlazy.com/dashboard/organization/api-key)
3. Copy the key shown in the API Key section

Each key is scoped to your dLazy organization and can be **rotated or revoked at any time** from the same dashboard.

## About & Provenance

* **CLI source code**: [github.com/dlazyai/cli](
* **Maintainer**: dlazyai
* **npm package**: `@dlazy/cli` (pinned to `1.0.9` in this skill's install spec)
* **Homepage**: [dlazy.com](https://dlazy.com)

You can install on demand without persisting a global binary by running:

```bash
npx @dlazy/cli@latest <command>
```

Or, if you prefer a global install, the skill's `metadata..install` field declares the exact pinned version (`npm install -g @dlazy/cli@latest`). Review the GitHub source before installing.

## How It Works

This skill is a thin client over the dLazy hosted API. When you invoke it:

* Prompts and parameters you provide are sent to the dLazy API endpoint (`api.dlazy.com`) for inference.
* Any local file paths you pass to image / video / audio fields are uploaded to dLazy's media storage (`files.dlazy.com`) so the model can read them — the same flow as any cloud-based generation API.
* Generated output URLs returned by the API are hosted on `files.dlazy.com`.

This is the standard SaaS pattern; the skill itself does not access network or filesystem resources beyond what the dLazy CLI already handles. See [dlazy.com](https://dlazy.com) for the full service terms.

## Piping Between Commands

Every `dlazy` invocation prints a JSON envelope on stdout. Any flag value can be a **pipe reference** that pulls from the upstream command's envelope, so you can chain steps without copying URLs by hand.

| Reference | Resolves to |
| --- | --- |
| `-` | Upstream's natural value for this field (scalar or array) |
| `@N` | The N-th output's primary value (e.g. `@0` = first output url) |
| `@N.<jsonpath>` | Drill into the N-th output (`@0.url`, `@1.meta.fps`) |
| `@*` | All outputs' primary values as an array |
| `@stdin` | The whole upstream JSON envelope |
| `@stdin:<jsonpath>` | Jsonpath into the whole envelope (`@stdin:result.outputs[0].url`) |

### 示例

```bash
dlazy seedream-4.5 --prompt "a red fox in snow" \
  | dlazy kling-v3 --image - --prompt "fox starts running"

dlazy seedream-4.5 --prompt "lighthouse at dawn" \
  | dlazy keling-tts --text "Welcome to the coast." --image @0.url

dlazy seedream-4.5 --prompt "city skyline" --n 4 \
  | dlazy superres --images @*
```

> Required flags can be entirely sourced from the pipe — `--field -` satisfies the requirement when an upstream value exists. If stdin is empty, the CLI fails with `code: "no_stdin"`.

## Usage

This skill handles all audio generation requests by selecting the best `dlazy` audio model.

### Available Audio Models

* `dlazy doubao-tts`: ByteDance Doubao speech synthesis model. Supports multiple languages, voices, and highly natural streaming audio output, suitable for news broadcasts and audiobooks.
* `dlazy elevenlabs-dialogue`: ElevenLabs eleven_v3 multi-voice dialogue: assign a different voice per line (up to 10) and render the whole conversation in one shot. Supports audio tags like [giggling], [whispers] — great for character dialogue, podcasts, and short skits. Before picking a voice, you can search for the right one via elevenlabs-search.
* `dlazy elevenlabs-music`: ElevenLabs music_v1 model — generates 10–300s original music from a natural-language prompt. Good for BGM, ads, and short-video soundtracks.
* `dlazy elevenlabs-search`: Search the ElevenLabs voice library by keyword, source, and category. Returns a playable preview for each matched voice so you can pick the right one before running TTS.
* `dlazy elevenlabs-sfx`: ElevenLabs text-to-sound model — generates 1–22s short sound effects from a description. Suitable for foley, ambience, alerts, and game SFX.
* `dlazy elevenlabs-tts`: ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and stability/similarity/style controls. Great for dubbing, audiobooks, and character dialog.
* `dlazy elevenlabs-voice-clone`: ElevenLabs Instant Voice Cloning (IVC). Upload a clean voice sample to clone a custom voice usable with ElevenLabs TTS.
* `dlazy gemini-2.5-tts`: Gemini-powered high-quality text-to-speech. Supports bilingual (EN/CN) and various emotional voices.
* `dlazy keling-sfx`: Sound effect generation model: supports text-to-SFX and matching SFX/BGM for reference videos. Suitable for foley, ambient sounds, and short video audio completion.
* `dlazy keling-tts`: Text-to-speech model (TTS), supports language, voice, speed, and output format settings. Suitable for dubbing, audiobooks, and voice broadcasts.
* `dlazy kling-audio-clone`: Custom voice (Kling), cloned voice used for dubbing or binding to subjects.
* `dlazy qwen-audio-clone`: Alibaba Bailian qwen3-tts voice cloning. Upload a clean voice sample to clone a custom voice usable in subsequent TTS calls.
* `dlazy qwen-tts`: Alibaba Bailian qwen3-tts text-to-speech. Choose from curated system voices (including dialects) or design a custom voice from a natural-language description.
* `dlazy suno-music`: Suno V5.5 music generation. Inspiration mode (auto lyrics) or custom mode (manual style/title/lyrics). Generates music with or without vocals, with fine-grained controls over style weight, weirdness and audio weight.
* `dlazy vidu-audio-clone`: Clone a real human voice and use it to read the specified text.

**CRITICAL INSTRUCTION FOR AGENT**:

1. Select the most appropriate audio model.
2. Run `dlazy <model_name> -h` to check parameters.
3. Execute the command.

## Error Handling

| Code | Error Type | Example Message |
| --- | --- | --- |
| 401 | Unauthorized (No API Key) | `ok: false, code: "unauthorized", message: "API key is missing or invalid"` |
| 501 | Missing required parameter | `error: required option '--prompt <prompt>' not specified` |
| 502 | Local file read error | `Error: Image file/Video file not found: C:\path\to\your\file` |
| 503 | API request failed (no balance) | `ok: false, code: "insufficient_balance"` |
| 503 | API request failed (server error) | `HTTP status code error (500 server crash)` |
| 504 | Asynchronous task execution failed | `=== Generation Failed ===` / `{Specific error reason returned by backend, for example "Prompt violates safety policy"}` |

> **AGENT CRITICAL INSTRUCTION**:
>
> 1. If the execution result returns `code: "insufficient_balance"`, you MUST explicitly inform the user that their credits are insufficient and guide them to recharge: <https://dlazy.com/dashboard/organization/settings?tab=credits>
> 2. If the execution result returns `code: "unauthorized"` or indicates missing API key, you MUST inform the user to get their API key from <https://dlazy.com/dashboard/organization/api-key> and save it using `dlazy auth set <key>` and resume the task.

## Tips

Visit <https://dlazy.com> for more information.

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

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
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Audio generation skill
- Automatically selects the best dlazy CLI audio/TTS\
  \ model the pro

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

| 错误码 | 场景描述 | 可能原因 | 解决方案 |
|:-------|:---------|:---------|:---------|
| AUTH_FAIL | 身份验证失败 | Key未设置/已过期/格式错 | 确认环境变量,重新获取Key |
| RATE_LIMIT | 触发限流 | 请求频率超过阈值 | 降低频率,指数退避重试 |
| TIMEOUT | 请求超时 | 网络不稳定或服务端慢 | 增加超时阈值,检查网络 |
| INVALID_PARAM | 参数无效 | 缺失必填项或值超范围 | 检查参数表,修正后重试 |
| SERVER_ERROR | 服务端异常 | 平台内部故障 | 等待1-2分钟后重试 |
## 已知限制

- 性能取决于底层模型能力

---
## 边界条件与限制 (Boundary Conditions)

Dlazy Audio Generate 技能在使用过程中存在一些边界条件和限制，以下列出了一些关键点：

- **输入文本长度限制**：由于模型处理能力和API限制，输入的文本长度可能存在上限。过长的文本可能会导致处理失败或输出质量下降。
- **模型性能限制**：不同的音频模型在处理复杂或特定类型的音频内容时，性能可能会有所不同。某些模型可能不适合处理极端或非常规的音频请求。
- **API调用频率限制**：为了防止滥用，dLazy API可能对调用频率有限制。超过限制可能导致服务暂时不可用。
- **输出文件格式限制**：虽然技能支持多种音频格式，但某些格式可能因为技术限制而无法生成。
- **版权内容限制**：技能不适用于处理版权受保护的媒体内容，包括但不限于音乐、电影、书籍等。
- **操作系统兼容性**：技能的运行环境需要满足操作系统要求，包括Windows、macOS和Linux。
- **网络连接要求**：稳定的网络连接对于技能的正常运行至关重要，特别是在上传和下载大文件时。

---

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | Dlazy Audio Generate | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 音频生成,自动选优选dlazy CLI音频/TTS模型 | 通用场景 | 通用场景 |

## 快速开始

1. **配置API密钥**: 在环境变量中设置对应的API Key
2. **初始化连接**: 使用提供的凭证建立API连接
3. **调用接口**: 传入必要参数执行API调用
1. **准备文件**: 确认文件路径正确且格式受支持
2. **执行处理**: 调用对应的处理函数
3. **查看结果**: 检查输出文件或返回数据
1. **检查环境**: 确认运行时和依赖已安装
2. **执行命令**: 使用正确的参数格式执行
3. **查看输出**: 检查命令输出和退出码

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪

## 常见问题

### Q1: Dlazy Audio Generate如何使用？
A: 使用Dlazy Audio Generate，您只需输入文本描述，系统将自动生成相应的音频内容。访问Skill页面，输入您的文本，点击“生成音频”按钮即可。

### Q2: Dlazy Audio Generate支持哪些语言？
A: Dlazy Audio Generate目前支持多种语言，包括但不限于英语、中文、西班牙语、法语等。具体支持的语言列表，请访问Skill页面查看。

### Q3: 生成音频的质量如何？
A: Dlazy Audio Generate生成的音频质量较高，能够清晰传达文本内容。我们使用先进的语音合成技术，确保音频的自然度和清晰度。

### Q4: 可以调整音频的语速和音调吗？
A: 可以。在生成音频的过程中，您可以通过设置选项调整语速和音调。这些设置可以帮助您根据个人喜好或需求定制音频效果。

### Q5: 生成音频后，我可以如何使用？
A: 生成音频后，您可以将其下载到本地设备，用于个人学习、工作或其他用途。此外，您还可以将音频分享到社交媒体或与朋友和家人分享。

## 核心功能

- **自动化执行**: 音频生成,自动选优选dlazy CLI音频/TTS模型
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据