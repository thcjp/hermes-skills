---
slug: music-generation
name: music-generation
version: "1.0.0"
displayName: Music Generation
summary: "优化提示生成AI音乐,风格控制/产出级音频(社区下载版)"
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
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# Music Generation

Unlock the power of AI to create professional-grade music.

**Rules:**

* Inquire about user needs: full songs with vocals, instrumentals, background music, or sound effects
* Verify provider files: `suno.md`, `udio.md`, `stable-audio.md`, `musicgen.md`, `mubert.md`, `soundraw.md`, `riffusion.md`, `replicate.md`
* Refer to `prompting.md` for advanced music prompt techniques
* Start with short clips to validate style before full generation

---

## Provider Selection

| Use Case | Recommended Providers |
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

* **Genre selection** — "electronic", "jazz", "hip-hop", "orchestral"
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

**Always verify current licensing terms before commercial use.**

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

## Dependency Information

### Runtime Environment
- **Agent Platform**: Supports any AI Agent compatible with SKILL.md (Claude Code / Cursor / Codex / Gemini CLI, etc.)
- **Operating System**: Windows / macOS / Linux

### Dependency Description
| Dependency | Type | Required | Acquisition Method |
|:-------|:-----|:---------|:---------|
| LLM API | API | Required | Provided by the built-in LLM of the Agent |

### API Key Configuration
- This Skill is based on Markdown instructions and does not require an additional API Key, except for explicitly marked external APIs.

### Availability Classification
- **Classification**: MD+EXEC (Pure Markdown instructions, some features require exec command-line execution capabilities)
- **Description**: An AI Skill based on Markdown, driven by natural language instructions to execute tasks on the Agent.

## Core Capabilities

- Generate AI music with optimized prompts, style control, and production-ready audio output
- Trigger Keywords: generate, optimized, generation, prompts, music

## Applicable Scenarios

| Scenario | Input | Output |
|------|------|------|
| Basic Usage | User request | Processing result |

**Not Applicable**: Complex decision-making scenarios requiring human judgment

## Usage Process

1. Confirm that the runtime environment meets the requirements specified in the Dependency Information section
2. Select the appropriate usage method based on the applicable scenarios
3. Execute the operation and check the output result
4. If an error occurs, refer to the Error Handling section

## Examples

### Example 1: Basic Usage

```
Input: User request
Processing: Execute according to the usage process
Output: Processing result
```

## Error Handling

| Error Scenario | Reason | Handling Method |
|---------|------|---------|
| Configuration Error | Missing or incorrectly formatted parameters | Check the configuration requirements in the Dependency Information section |
| Runtime Error | Inadequate runtime environment | Confirm that the runtime environment meets the requirements specified in the Dependency Information section |
| Network Error | Connection timeout or unreachability | Check network connection and retry, refer to domestic alternatives |

## Common Questions

### Q1: How do I start using Music Generation?
A: Please read the Usage Process section first and confirm that the environment meets the requirements specified in the Dependency Information section.

### Q2: What should I do if I encounter an error?
A: Please refer to the Error Handling section and operate according to the procedures in the table.

### Q3: What are the limitations of Music Generation?
A: Please refer to the Known Limitations section for specific limitations.

## Known Limitations

- Requires LLM support, cannot be used without an LLM environment
- Complex scenarios may require human judgment assistance
- Performance depends on the underlying model capabilities

---
## Boundary Conditions and Limitations

### Input Restrictions
- **Text Length**: Input text length should not be too long, recommended not to exceed 500 characters to ensure that the AI can accurately understand and generate music.
- **Complexity**: Avoid overly complex music style descriptions to prevent the AI from understanding and generating results that meet the requirements.
- **Format Specification**: Input text should follow the correct format, such as using commas to separate different music element descriptions.

### Performance Boundaries
- **Real-time**: Due to the complex algorithm processing involved in music generation, real-time generation may be delayed, and users are advised to be patient.
- **Generation Quality**: The quality of AI-generated music is limited by the training data and algorithms, and may not reach the level of professional music production.

### Compatibility Constraints
- **Operating System**: Skill.md skills run on AI Agents that support SKILL.md, such as Claude Code, Cursor, Codex, Gemini CLI, etc.
- **Network Environment**: Stable network connection is a key factor for the normal operation of the skill, and it is recommended to use it in a high-speed network environment.
- **External APIs**: Some music generation services may require external API support, and it is necessary to ensure that API Keys and related parameters have been correctly configured.

### Other Restrictions
- **Copyright Issues**: AI-generated music may have copyright issues, and it is necessary to understand relevant laws and regulations before use.
- **Personalization Customization**: AI-generated music styles and elements may be limited, and may not meet all personalized needs.
- **Language Support**: Currently, the music generation skill mainly supports English input, and other languages may have limitations.

---
## Differentiation Advantages

### Comparison with Similar Solutions

1. **Manual Music Creation**: Compared with manual music creation, Music Generation skill significantly improves efficiency. Manual music creation requires music theory knowledge and a long period of practice, while this skill generates music that meets specific styles and requirements in a short time through AI technology, saving creators' time and effort.

2. **Other Music Generation Tools**: Compared with other music generation tools, Music Generation performs better in terms of security and stability. Some tools may have security vulnerabilities or stability issues, while Music Generation has been deeply optimized, removed the original risk code, and enhanced metadata and trigger control to ensure safety and stability during use.

3. **General Method**: Compared with traditional music production methods, Music Generation skill provides a more convenient and efficient music creation experience. Traditional music production methods usually require multiple steps and complex processes, while Music Generation skill simplifies the creation process through simple instructions and rich output formats.

### Unique Features

1. **Style Control**: Music Generation skill supports the generation of various music styles, and users can choose the appropriate style according to their needs, such as electronic, jazz, hip-hop, orchestral, etc.

2. **Mood/Energy Adjustment**: In addition to style control, users can adjust the mood and energy of music to meet the needs of specific scenarios, such as upbeat, melancholic, aggressive, calm, etc.

3. **Instrument Selection**: Users can specify the required instruments, such as piano, guitar, synth, strings, etc., to achieve personalized music effects.

4. **Rhythm Adjustment**: Music Generation skill supports the adjustment of music rhythm, such as 120 BPM, slow, fast-paced, etc., to meet the needs of different occasions.

5. **Reference Artists**: For supported styles, users can create according to the style of specific artists, such as "in the style of Hans Zimmer".

### Efficiency Improvement

Using Music Generation skill, users can generate music that meets specific styles and requirements in a short time, saving a lot of time and effort. For example, when creating background music, users only need to input video length and mood, and can quickly generate matching music without manual creation.

### Innovation in Application Scenarios

1. **Video Game Music**: Music Generation skill can quickly generate music that matches the atmosphere of the game, adding immersion to the game.

2. **Short Video Background Music**: Users can quickly generate music that matches the theme of the short video to improve the viewing experience of the video.

3. **Ad Music Production**: Music Generation skill can help advertisers quickly generate music that matches the theme and mood of the advertisement to improve the effectiveness of the advertisement.

---
## 差异化优势

### 与同类方案对比

1. **手动音乐创作**：与传统的手动音乐创作相比，Music Generation技能能够显著提升创作效率。手动创作音乐需要深厚的音乐理论基础和长时间的实践，而Music Generation通过AI技术，可以在短时间内生成符合特定风格和要求的音乐，极大节省了创作者的时间和精力。

2. **其他音乐生成工具**：与其他音乐生成工具相比，Music Generation在安全性和稳定性方面表现更佳。一些工具可能存在安全漏洞或稳定性问题，而Music Generation经过深度优化，移除了原始风险代码，增强了元数据和触发控制，确保了使用过程中的安全稳定。

3. **传统音乐制作方法**：与传统的音乐制作方法相比，Music Generation技能提供了更加便捷高效的创作体验。传统音乐制作通常需要多个步骤和复杂的流程，而Music Generation通过简单的指令和丰富的输出格式，简化了创作过程。

### 独特功能

1. **风格控制**：Music Generation技能支持生成各种音乐风格，用户可以根据需求选择合适的风格，如电子、爵士、嘻哈、管弦乐等。

2. **情绪/能量调整**：除了风格控制，用户还可以调整音乐的情绪和能量，以满足特定场景的需求，如欢快、忧郁、激昂、平静等。

3. **乐器选择**：用户可以指定所需的乐器，如钢琴、吉他、合成器、弦乐等，以实现个性化的音乐效果。

4. **节奏调整**：Music Generation技能支持调整音乐节奏，如120 BPM、慢速、快速等，以满足不同场合的需求。

5. **参考艺术家**：对于支持的风格，用户可以模仿特定艺术家的风格进行创作，如“以汉斯·齐默的风格”。

### 效率提升

使用Music Generation技能，用户可以在短时间内生成符合特定风格和要求的音乐，节省大量时间。例如，在制作视频背景音乐时，用户只需输入视频长度和情绪，即可快速生成匹配的音乐，无需手动创作。

### 应用场景创新

1. **游戏音乐**：Music Generation技能可以快速生成与游戏氛围相匹配的音乐，提升游戏沉浸感。

2. **短视频背景音乐**：用户可以快速生成与短视频主题相匹配的音乐，提升视频观看体验。

3. **广告音乐制作**：Music Generation技能可以帮助广告商快速生成与广告主题和情绪相匹配的音乐，提高广告效果。

