---
slug: music-generation
name: music-generation
version: "1.0.0"
displayName: Music Generation
summary: Generate AI music with optimized prompts, style control, and production-ready
  audio output.
license: MIT
description: |-
  Generate AI music with optimized prompts, style control, and production-ready
  audio output。核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关...
tags:
- Creative
tools:
  - - read
- exec
---

# Music Generation

Help users create AI-generated music and audio.

**Rules:**

* Ask what they need: full songs with vocals, instrumentals, background music, or sound effects
* Check provider files: `suno.md`, `udio.md`, `stable-audio.md`, `musicgen.md`, `mubert.md`, `soundraw.md`, `riffusion.md`, `replicate.md`
* Check `prompting.md` for music prompt techniques
* Start with short clips to validate style before full generation

---

## Provider Selection

| Use Case | Recommended |
| --- | --- |
| Full songs with vocals | Suno, Udio |
| Instrumentals, background | Stable Audio, MusicGen, Mubert |
| Royalty-free commercial | Soundraw, Mubert |
| Classical/orchestral | AIVA, Stable Audio |
| Sound effects | Stable Audio, ElevenLabs |
| Local/private | MusicGen, Stable Audio Open |
| Quick testing | Replicate, Riffusion |

---

## Prompting Fundamentals

* **Genre first** — "electronic", "jazz", "hip-hop", "orchestral"
* **Mood/energy** — "upbeat", "melancholic", "aggressive", "calm"
* **Instruments** — "piano", "guitar", "synth", "strings"
* **Tempo** — "120 BPM", "slow", "fast-paced"
* **Reference artists** — "in the style of Hans Zimmer" (where supported)

---

## Output Formats

* **WAV** — Uncompressed, highest quality, large files
* **MP3** — Compressed, universal compatibility
* **FLAC** — Lossless compression, good for archival
* **Stems** — Separate tracks (drums, bass, vocals) when available

---

## Common Workflows

### Background Music for Video

1. Determine video length and mood
2. Generate instrumental at matching duration
3. Adjust tempo to match cuts if needed
4. Mix levels appropriately

### Full Song Production

1. Write or generate lyrics
2. Describe musical style in detail
3. Generate multiple variations
4. Select best, extend or edit
5. Export stems if available for mixing

### Sound Design

1. Describe sound effect clearly
2. Specify duration needed
3. Generate variations
4. Layer and process as needed

---

## Licensing Considerations

| Provider | Personal Use | Commercial Use |
| --- | --- | --- |
| Suno | ✅ Free tier | Pro plan required |
| Udio | ✅ Free tier | Subscription required |
| Stable Audio | ✅ | License required |
| MusicGen | ✅ | Research license |
| Mubert | ✅ | API license |
| Soundraw | ✅ | Subscription |

**Always check current licensing terms before commercial use.**

---

## Quality Tips

* **Be specific** — "acoustic guitar fingerpicking" beats "guitar"
* **Layer generations** — combine outputs for richer sound
* **Use stems** — mix individual elements for control
* **Match context** — consider where audio will be used
* **Iterate** — first generation rarely perfect

---

### Current Setup

### Projects

### Preferences

---

*Check provider files for detailed setup and API usage.*

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

## 核心能力

- Generate AI music with optimized prompts, style control, and production-ready
  audio output
- 触发关键词: generate, optimized, generation, prompts, music

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Music Generation？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Music Generation有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
