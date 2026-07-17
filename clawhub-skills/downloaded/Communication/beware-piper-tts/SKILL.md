---
slug: beware-piper-tts
name: beware-piper-tts
version: "1.0.1"
displayName: Piper TTS
summary: Local text-to-speech using Piper for voice message delivery. Use when the
  user asks for voice res...
license: MIT
description: |-
  Local text-to-speech using Piper for voice message delivery. Use when
  the user asks for voice res...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: using, local, speech, text, piper, tts, beware
tags:
- Communication
- Creative
tools:
- read
- exec
---

# Piper TTS

Generate voice messages using [Piper](https://github.com/rhasspy/piper), a fast local TTS engine. Zero cloud calls, zero cost, zero API keys.

## Setup

If Piper is not installed, run the setup script:

```bash
scripts/setup-piper.sh
```

This installs `piper-tts` via pip and downloads a default voice (`en_US-kusal-medium`).

## Generating Voice Messages

Use `scripts/piper-speak.sh` to generate and deliver voice:

```bash
scripts/piper-speak.sh "<text>" [voice]
```

* `text`: The text to speak (required)
* `voice`: Piper voice name (default: `en_US-kusal-medium`)

The script outputs an MP3 path. Include it in your reply as:

```text
[[audio_as_voice]]
MEDIA:<path-to-mp3>
```

This delivers the audio as a native voice message on supported channels (Telegram, Discord, etc.).

## Example Workflow

1. User asks: "Tell me a joke as audio"
2. Run: `scripts/piper-speak.sh "Why do programmers prefer dark mode? Because light attracts bugs!"`
3. Get MP3 path from output
4. Reply with `[[audio_as_voice]]` + `MEDIA:<path>`

## Available Voices

After setup, download additional voices:

```bash
scripts/setup-piper.sh --voice en_US-ryan-high
scripts/setup-piper.sh --voice en_GB-northern_english_male-medium
```

Popular voices:

* `en_US-kusal-medium` — Clear male voice (default, recommended)
* `en_US-ryan-high` — High quality US male
* `en_US-hfc_male-medium` — US male
* `en_GB-northern_english_male-medium` — British male
* Browse all: <https://huggingface.co/rhasspy/piper-voices>

## Important Notes

* **Speed**: Local generation is ~0.5-1s. Much faster than cloud TTS.
* **No API keys**: Works completely offline after setup.
* **Platform**: macOS (Apple Silicon + Intel), Linux. Requires Python 3.9+.
* **Do NOT** set `messages.tts.auto: "always"` in Skill平台 config — it makes every response slow. Keep TTS on-demand.

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
