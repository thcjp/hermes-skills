---
slug: llm-provider-whisper-1-0-0
name: openai-whisper-1-0-0
version: "1.0.0"
displayName: llm-provider Whisper
summary: "用Whisper CLI本地语音转文字,免API Key,v1.0.0稳定版(社区下载版)"
license: MIT
description: |-
  Local speech-to-text with the Whisper CLI (no API key)。核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# llm-provider Whisper 1.0.0

The `whisper` tool is designed to transcribe audio files locally, without the need for an API key. This section provides a comprehensive guide to using Whisper 1.0.0.

## Quick Start

To get started with Whisper, follow these steps:

1. Download and install Whisper from the [official repository](https://github.com/openai/whisper).
2. Open your terminal or command prompt.
3. Run the following command to transcribe an audio file:

```bash
whisper /path/to/audio.mp3 --model medium --output_format txt --output_dir .
```

For video files, you can use:

```bash
whisper /path/to/audio.m4a --task translate --output_format srt
```

## Notes

- On the first run, Whisper will download the necessary models to `~/.cache/whisper`.
- The default model is `turbo`. You can use smaller models for faster processing or larger models for higher accuracy.

## Dependency Requirements

### Operating System

- **Windows**
- **macOS**
- **Linux**

### Software Dependencies

- Python 3.7 or later
- `ffmpeg` for video file support

### API Key Configuration

- No API key is required for Whisper. All operations are performed locally.

## Core Capabilities

- **Local Speech-to-Text**: Convert audio to text without the need for an internet connection or API key.
- **Customizable Output**: Supports various output formats, including plain text and subtitle files.
- **Efficient Processing**: Optimized for performance and accuracy.

## Use Cases

- **Content Creation**: Transcribe spoken words for articles, blogs, and scripts.
- **Multimedia Production**: Create transcripts for videos and podcasts.
- **Business Applications**: Enhance accessibility and productivity in corporate environments.

## Input and Output Formats

| Input Format | Output Format | Description |
|--------------|---------------|-------------|
| Audio Files (MP3, M4A) | Plain Text (TXT), Subtitle (SRT) | Whisper can transcribe audio files into text and subtitle files. |

## Usage Workflow

1. **Environment Setup**: Ensure your operating system and software dependencies meet the requirements.
2. **Command Execution**: Run the appropriate Whisper command based on your use case.
3. **Result Review**: Verify the accuracy of the transcribed text or subtitle file.

## Examples

### Example 1: Transcribing an Audio File

```bash
whisper /path/to/audio.mp3 --model medium --output_format txt --output_dir .
```

### Example 2: Transcribing a Video File

```bash
whisper /path/to/video.m4a --task translate --output_format srt
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Model Download Error | Network issue or model not found | Check your internet connection and try again. |
| Transcription Error | Poor audio quality | Improve the audio quality or use a different model. |

## Common Questions

### Q1: Do I need an API key to use Whisper?

A1: No, Whisper does not require an API key. All operations are performed locally.

### Q2: How do I choose the right model for my audio?

A2: If you need speed, use a smaller model. For higher accuracy, use a larger model.

## Known Limitations

- **No Cloud Support**: Whisper operates locally and does not support cloud-based processing.
- **Limited Language Support**: Whisper supports a limited number of languages.

## Security Considerations

- Whisper operates locally and does not transmit data over the internet, reducing the risk of data breaches.
- Ensure that you trust the source of the Whisper installation to prevent potential security risks.