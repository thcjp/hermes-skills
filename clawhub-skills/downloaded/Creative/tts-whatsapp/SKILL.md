---
slug: tts-whatsapp
name: tts-whatsapp
version: "1.0.0"
displayName: TTS WhatsApp
summary: Send high-quality text-to-speech voice messages on WhatsApp in 40+ languages
  with automatic delivery
license: MIT
description: |-
  Send high-quality text-to-speech voice messages on WhatsApp in 40+ languages
  with automatic delivery

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依...
tags:
- Creative
- Communication
tools:
  - - read
- exec
---

# TTS WhatsApp

Send high-quality text-to-speech voice messages on WhatsApp with automatic delivery. Supports 40+ languages, personal messages, and group broadcasts.

## 核心能力

* 🎙️ **High-quality TTS** powered by Piper (40+ languages)
* 🎵 **Automatic conversion** to OGG/Opus (WhatsApp format)
* 📤 **Automatic sending** via Clawdbot
* 👥 **Group support** - Send to individuals or WhatsApp groups
* 🌍 **Multi-language** - French, English, Spanish, German, and 40+ more
* 🧹 **Smart cleanup** - Auto-delete files after successful send
* ⚡ **Fast** - ~2-3s from command to delivery

## 📦 Prerequisites

1. **Piper TTS**: `pip3 install --user piper-tts`
2. **FFmpeg**: `brew install ffmpeg` (macOS) or `apt install ffmpeg` (Linux)
3. **Voice models**: Download from [Hugging Face](https://huggingface.co/rhasspy/piper-voices)
   * Place in `~/.clawdbot/skills/piper-tts/models/`
   * Example: `fr_FR-siwis-medium.onnx`

## 使用流程

### Basic usage

```bash
tts-whatsapp "Hello, this is a test" --target "+15555550123"
```

### Send to WhatsApp group

```bash
tts-whatsapp "Hello everyone" --target "120363257357161211@g.us"
```

### Change language

```bash
tts-whatsapp "Hola mundo" --lang es_ES --voice carlfm --target "+34..."
```

### Different quality levels

```bash
tts-whatsapp "High quality" --quality high --target "+1..."
```

## 🌍 Supported Languages

* 🇫🇷 French (`fr_FR`): siwis, upmc, tom
* 🇬🇧 English GB (`en_GB`): alan, alba
* 🇺🇸 English US (`en_US`): lessac, amy, joe
* 🇪🇸 Spanish (`es_ES`, `es_MX`): carlfm, davefx
* 🇩🇪 German (`de_DE`): thorsten, eva_k
* 🇮🇹 Italian (`it_IT`): riccardo
* 🇵🇹 Portuguese (`pt_BR`, `pt_PT`): faber
* 🇳🇱 Dutch (`nl_NL`): mls, rdh
* 🇷🇺 Russian (`ru_RU`): dmitri, irina
* And 30+ more!

[Full voice list →](https://rhasspy.github.io/piper-samples/)

## 🔧 Configuration

Configure in `~/.clawdbot/clawdbot.json`:

```json
{
  "skills": {
    "entries": {
      "tts_whatsapp": {
        "enabled": true,
        "env": {
          "WHATSAPP_DEFAULT_TARGET": "+15555550123",
          "PIPER_DEFAULT_LANG": "en_US",
          "PIPER_DEFAULT_VOICE": "lessac",
          "PIPER_DEFAULT_QUALITY": "medium"
        }
      }
    }
  }
}
```

## 🎛️ All Options

```text
--target NUMBER       WhatsApp number or group ID
--message TEXT        Text message with audio
--lang LANGUAGE       Language (default: fr_FR)
--voice VOICE         Voice name (default: auto)
--quality QUALITY     x_low, low, medium, high
--speed SPEED         Playback speed (default: 1.0)
--no-send            Don't send automatically
```

## 📊 Performance

~2.3s total for a 10-second message:

* TTS generation: ~1s
* Format conversion: ~0.2s
* WhatsApp delivery: ~1s

## 📚 Full Documentation

See [README.md](/api/v1/skills/tts-whatsapp/file?path=README.md&ownerHandle=hopyky) for complete documentation, examples, and troubleshooting.

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
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### Basic usage

```bash
tts-whatsapp "Hello, this is a test" --target "+15555550123"
```

### Send to WhatsApp group

```bash
tts-whatsapp "Hello everyone" --target "120363257357161211@g.us"
```

### Change language

```bash
tts-whatsapp "Hola mundo" --lang es_ES --voice carlfm --target "+34..."
```

### Different quality levels

```bash
tts-whatsapp "High quality" --quality high --target "+1..."
```
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用TTS WhatsApp？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: TTS WhatsApp有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
