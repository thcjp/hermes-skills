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

Unleash the potential of AI in crafting sophisticated music pieces.

**Usage Guidelines:**

* Inquire about user requirements: full songs with vocals, instrumentals, background music, or sound effects
* Validate provider files: `suno.md`, `udio.md`, `stable-audio.md`, `musicgen.md`, `mubert.md`, `soundraw.md`, `riffusion.md`, `replicate.md`
* Refer to `prompting.md` for advanced music prompt techniques
* Start with short clips to assess style before proceeding to full generation

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

## Prompting Essentials

* **Genre selection** — Specify the desired genre such as "electronic", "jazz", "hip-hop", "orchestral"
* **Mood/energy** — Define the mood or energy, e.g., "upbeat", "melancholic", "aggressive", "calm"
* **Instruments** — Specify instruments, e.g., "piano", "guitar", "synth", "strings"
* **Tempo** — Define the tempo, e.g., "120 BPM", "slow", "fast-paced"
* **Reference artists** — Indicate style, e.g., "in the style of Hans Zimmer" (where supported)

---

## Output Formats

* **WAV** — Uncompressed, highest quality, suitable for high-resolution listening
* **MP3** — Compressed, widely compatible with various devices
* **FLAC** — Lossless compression, ideal for archiving
* **Stems** — Separate tracks (drums, bass, vocals) when available for custom mixing

---

## Common Workflows

### Background Music for Video

1. Determine the video's duration and mood
2. Generate an instrumental track of the matching duration
3. Adjust tempo if necessary to align with video cuts
4. Mix levels for optimal audio quality

### Full Song Production

1. Write or generate lyrics
2. Describe the musical style in detail
3. Generate multiple variations
4. Select the best variation and edit as needed
5. Export stems if available for advanced mixing

### Sound Design

1. Clearly describe the desired sound effect
2. Specify the required duration
3. Generate variations
4. Layer and process sounds as needed for the desired effect

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

**Always verify current licensing terms before using for commercial purposes.**

---

## Quality Enhancement Tips

* **Specificity** — Be detailed in your prompts, such as "acoustic guitar fingerpicking" instead of just "guitar"
* **Layering** — Combine outputs for a richer sound
* **Stems** — Use stems for greater control over individual elements
* **Contextual Relevance** — Consider the context in which the audio will be used
* **Iterative Process** — Expect iterations; the first generation is often a starting point

---

### Current Setup

### Projects

### Preferences

---

*Consult provider files for detailed setup and API usage.*

## Dependency Information

### Runtime Environment
- **Agent Platform**: Compatible with any AI Agent that supports SKILL.md (Claude Code, Cursor, Codex, Gemini CLI, etc.)
- **Operating System**: Windows, macOS, Linux

### Dependency Description
| Dependency | Type | Required | Acquisition Method |
|:-------|:-----|:---------|:---------|
| LLM API | API | Required | Provided by the built-in LLM of the Agent |

### API Key Configuration
- This Skill does not require an additional API Key, except for explicitly marked external APIs.

### Availability Classification
- **Classification**: MD+EXEC (Pure Markdown instructions, some features require exec command-line execution capabilities)
- **Description**: An AI Skill based on Markdown, driven by natural language instructions to execute tasks on the Agent.

## Core Capabilities

- Generate AI music with optimized prompts, style control, and production-ready audio output
- Trigger Keywords: generate, optimized, music, style, AI

## Applicable Scenarios

| Scenario | Input | Output |
|------|------|------|
| Basic Usage | User request | Generated music |
| Advanced Customization | Detailed prompts | Custom music piece |

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
Output: Generated music
```

### Example 2: Advanced Customization

```
Input: Detailed prompts including genre, mood, instruments, tempo
Processing: Generate music based on the detailed prompts
Output: Custom music piece
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
- **Text Length**: Input text length should not exceed 500 characters to ensure accurate understanding and music generation
- **Complexity**: Avoid overly complex music style descriptions to prevent inaccurate results
- **Format Specification**: Input text should follow the correct format, such as using commas to separate different music element descriptions

### Performance Boundaries
- **Real-time**: Music generation involves complex algorithm processing, which may cause delays, so please be patient
- **Generation Quality**: AI-generated music quality is limited by training data and algorithms, and may not reach professional levels

### Compatibility Constraints
- **Operating System**: Compatible with AI Agents that support SKILL.md, such as Claude Code, Cursor, Codex, Gemini CLI, etc.
- **Network Environment**: Requires stable network connection for normal operation
- **External APIs**: Some services may require external API support, ensure correct configuration of API Keys and parameters

### Other Restrictions
- **Copyright Issues**: AI-generated music may have copyright concerns, understand relevant laws and regulations before use
- **Personalization Customization**: AI-generated music styles and elements may be limited
- **Language Support**: Currently supports English input, other languages may have limitations

---

## Differentiation Advantages

### Comparison with Similar Solutions

1. **Manual Music Creation**: Significantly improves efficiency compared to manual music creation, which requires music theory knowledge and extensive practice
2. **Other Music Generation Tools**: Offers better security and stability, optimized for performance and metadata management
3. **Traditional Music Production Methods**: Provides a more convenient and efficient music creation experience with simple instructions and diverse output formats

### Unique Features

1. **Style Control**: Supports a wide range of music styles, allowing users to select the appropriate style for their needs
2. **Mood/Energy Adjustment**: Enables users to adjust the mood and energy of the music to fit specific scenarios
3. **Instrument Selection**: Allows users to specify the required instruments for personalized music effects
4. **Rhythm Adjustment**: Supports rhythm adjustments to meet different occasion requirements
5. **Reference Artists**: Users can create music in the style of specific artists, enhancing the creative process

### Efficiency Improvement

Music Generation skill allows users to quickly generate music that meets specific styles and requirements, saving time and effort. For example, when creating background music for videos, users can quickly generate matching music without manual creation.

### Innovation in Application Scenarios

1. **Video Game Music**: Generates music that matches the game atmosphere, enhancing the gaming experience
2. **Short Video Background Music**: Generates music that matches the video theme, improving the viewing experience
3. **Ad Music Production**: Helps advertisers create music that matches the advertisement's theme and mood, improving advertisement effectiveness

---

## 差异化优势

### 与同类方案对比

1. **手动音乐创作**：相比传统手动音乐创作，Music Generation技能大幅提升创作效率。手动音乐创作需要深厚的音乐理论基础和长时间的实践，而Music Generation通过AI技术，能够在短时间内生成符合特定风格和要求的音乐，极大节省了创作者的时间和精力。

2. **其他音乐生成工具**：相比其他音乐生成工具，Music Generation在安全性和稳定性方面表现更优。一些工具可能存在安全漏洞或稳定性问题，而Music Generation经过深度优化，移除了原始风险代码，增强了元数据和触发控制，确保了使用过程中的安全稳定。

3. **传统音乐制作方法**：相比传统的音乐制作方法，Music Generation技能提供了更加便捷高效的创作体验。传统音乐制作通常需要多个步骤和复杂的流程，而Music Generation通过简单的指令和丰富的输出格式，简化了创作过程。

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