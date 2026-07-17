---
slug: dlazy-audio-generate
name: dlazy-audio-generate
version: "1.3.3"
displayName: "é\x9F³é¢\x91ç\x94\x9Fæ\x88\x90 Audio Generate"
summary: Audio generation skill. Automatically selects the best dlazy CLI audio/TTS
  model based on the pro...
license: MIT-0
description: |-
  Audio generation skill. Automatically selects the best dlazy CLI audio/TTS\
  \ model based on the pro...\n\n核心能力:\n- 创意设计领域的专业化AI辅助工具\n- 基于高人气开源Skill深度优化升级\n\
  - 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 内容创作、设计生成、多媒体制作\n- 独立开发者与一人公司效率提升\n- 自动化工作流与智能决策辅助\n\
  \n差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。\n\n触发关键词: selects,\
  \ generate, dlazy, automatically, é\x9F³é¢\x91ç\x94\x9Fæ\x88\x90, audio, generation,\
  \ skill
tags: '[''Creative'']'
tools: '[read, exec]'
---

# é³é¢çæ Audio Generate

[English](/api/v1/skills/dlazy-audio-generate/file?path=SKILL.md&ownerHandle=dlazyai) · [中文](/api/v1/skills/dlazy-audio-generate/file?path=SKILL-cn.md&ownerHandle=dlazyai)

Audio generation skill. Automatically selects the best dlazy CLI audio/TTS model based on the prompt. 音频生成技能。根据提示词自动选择最佳的 dlazy CLI 音频/TTS 模型。

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

* **CLI source code**: [github.com/dlazyai/cli](https://github.com/dlazyai/cli)
* **Maintainer**: dlazyai
* **npm package**: `@dlazy/cli` (pinned to `1.0.9` in this skill's install spec)
* **Homepage**: [dlazy.com](https://dlazy.com)

You can install on demand without persisting a global binary by running:

```bash
npx @dlazy/cli@latest <command>
```

Or, if you prefer a global install, the skill's `metadata.clawdbot.install` field declares the exact pinned version (`npm install -g @dlazy/cli@latest`). Review the GitHub source before installing.

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

### Examples

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
* `dlazy elevenlabs-tts`: ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and stability/similarity/style controls. Great for dubbing, audiobooks, and character dialog. Before picking a voice, you can search for the right one via elevenlabs-search.
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

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
