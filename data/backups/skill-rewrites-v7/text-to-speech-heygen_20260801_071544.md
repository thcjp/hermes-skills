---

slug: text-to-speech-heygen
name: "text-to-speech-heygen"
version: 2.23.1
displayName: "语音合成工具"
summary: "HeyGen TTS语音合成工具's Starfish TTS model. Use。Generate speech audio from text using HeyGen's Starf"
summary_zh: "HeyGen TTS语音合成工具's Starfish TTS model. Use。Generate speech audio from text using HeyGen's Starf"
license: "MIT"
description: |-
  Generate speech audio from text using HeyGen's Starfish TTS model。Use when: (1) Generating stand。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Creative
  - 工具
  - 效率
  - text
  - result
  - const
  - await
  - language
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"

---

# Text to Speech

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- Generate speech audio from text using HeyGen's Starfish TTS model
- Use when: (1) Generating stand

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| HeyGen TTS | 目标数据与配置参数 | 处理结果与执行状态 |
| text操作执行 | text相关参数与配置 | 执行结果与返回数据 |
| text状态查询 | 查询条件与过滤选项 | 当前状态与详细信息 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | 处理的内容输入 |
| mode | string | 否 | 处理模式, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "处理结果",
    "status": "success",
    "metadata": {
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### Basic TTS

```typescript
const result = await textToSpeech({
  text: "Welcome to our quarterly earnings call.",
  voice_id: "YOUR_VOICE_ID",
});
// ...
console.log(`Audio URL: ${result.audio_url}`);
console.log(`Duration: ${result.duration}s`);
```

### With Speed Adjustment

```typescript
const result = await textToSpeech({
  text: "We're thrilled to announce our newest feature!",
  voice_id: "YOUR_VOICE_ID",
  speed: 1.1,
});
```

### With Language and Locale for Multilingual Voices

```typescript
const result = await textToSpeech({
  text: "Bem-vindo ao nosso produto.",
  voice_id: "MULTILINGUAL_VOICE_ID",
  language: "pt",
  locale: "pt-BR",
});
```

### With SSML Input

```typescript
const result = await textToSpeech({
  text: '<speak>Hello <break time="1s"/> and welcome!</speak>',
  voice_id: "YOUR_VOICE_ID",
  input_type: "ssml",
});
```

### Find a Voice and Generate Audio

```typescript
async function generateSpeech(text: string, language: string): Promise<string> {
  const voices = await listTTSVoices();
  const voice = voices.find(
    (v) => v.language.toLowerCase().includes(language.toLowerCase())
  );
// ...
  if (!voice) {
    throw new Error(`No TTS voice found for language: ${language}`);
  }
// ...
  const result = await textToSpeech({
    text,
    voice_id: voice.voice_id,
  });
// ...
  return result.audio_url;
}
// ...
const audioUrl = await generateSpeech("Hello and welcome!", "english");
```

## 常见问题

### Q1: 如何开始使用Text to Speech？
A: 请参考使用流程和依赖说明章节，确保运行环境满足要求后调用本技能。
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 功能详解与边界条件

### 核心功能详解

1. **语音合成**：
   - **输入参数**：`content`（文本内容），`voice_id`（语音模型ID），`speed`（语速调整，1.0为正常速度），`language`（语言），`locale`（地区），`style`（输出风格）。
   - **处理逻辑**：将文本内容通过HeyGen的Starfish TTS模型转换为语音音频。
   - **输出结果**：返回包含音频URL、音频时长、使用的模板、单词计数和风格等信息的JSON对象。

2. **SSML输入**：
   - **输入参数**：`text`（SSML格式的文本），`voice_id`（语音模型ID）。
   - **处理逻辑**：将SSML格式的文本内容通过HeyGen的Starfish TTS模型转换为语音音频。

3. **语音模型选择**：
   - **输入参数**：`voice_id`（语音模型ID）。
   - **处理逻辑**：根据提供的语音模型ID选择相应的语音模型进行语音合成。

### 边界条件

1. **输入文本长度限制**：单次请求的文本长度不超过5000个字符。
2. **并发请求限制**：同一时间内的并发请求不超过100个。
3. **字符编码要求**：输入文本必须使用UTF-8编码。
4. **语音模型ID限制**：只能使用HeyGen提供的有效语音模型ID。
5. **输出音频格式限制**：输出音频格式为MP3。
6. **API Key限制**：每个API Key每月有免费的请求次数限制。
7. **网络连接限制**：请求必须通过HTTPS协议发送。
8. **地区限制**：部分语音模型可能仅支持特定地区。

### 错误处理

1. **配置错误**：参数缺失或格式错误，检查依赖说明中的配置要求。
2. **运行时错误**：运行环境不满足，确认运行环境符合依赖说明。
3. **网络错误**：连接超时或不可达，检查网络连接。
4. **输入内容格式不正确**：用户输入不符合skill预期格式，检查输入是否符合skill使用说明中的格式要求。
5. **执行结果与预期不符**：指令描述不够明确或上下文不足，提供更详细的指令描述，补充必要的上下文信息。
6. **LLM响应超时或无响应**：网络延迟或模型负载过高，请求；确认Agent平台LLM服务正常。
7. **API Key限制**：超出每月免费请求次数限制，联系HeyGen客服获取更多资源。
8. **语音模型ID无效**：提供的语音模型ID不存在或已停用，选择有效的语音模型ID。

## 差异化优势

### 与同类方案对比

1. **手动操作**：手动操作语音合成通常需要使用音频编辑软件，如Audacity或Adobe Audition，这些工具虽然功能强大，但操作复杂，需要一定的音频处理知识。相比之下，HeyGen TTS语音合成工具通过简单的API调用即可实现文本到语音的转换，无需音频编辑技能，大大降低了使用门槛。

2. **其他语音合成工具**：市场上存在一些其他的语音合成工具，如Google Text-to-Speech、Amazon Polly等。虽然这些工具也提供文本到语音的转换功能，但HeyGen TTS语音合成工具在以下方面具有明显优势：
   - **更丰富的语音模型**：HeyGen提供了多种语音模型，包括多种语言和口音，满足不同场景的需求。
   - **更自然的语音效果**：HeyGen的Starfish TTS模型能够生成更自然、流畅的语音，优于一些通用语音合成工具。

### 独特功能

1. **风格定制**：HeyGen TTS语音合成工具支持自定义输出风格，如专业、友好、正式等，满足不同场合的语音需求。
2. **多语言支持**：除了英语，HeyGen还支持多种语言和地区，方便全球用户使用。
3. **SSML输入**：支持SSML（Speech Synthesis Markup Language）输入，允许用户更精确地控制语音合成过程。
4. **语音模型选择**：用户可以根据需要选择不同的语音模型，以获得不同的语音效果。
5. **API集成**：HeyGen TTS语音合成工具提供API接口，方便与其他应用程序集成。

### 效率提升

使用HeyGen TTS语音合成工具，用户可以节省大量时间，例如：
- **节省音频编辑时间**：无需使用音频编辑软件进行语音合成，节省了音频编辑的时间。
- **提高工作效率**：通过自动化语音合成，可以快速生成语音内容，提高工作效率。

### 应用场景创新

1. **智能客服**：将HeyGen TTS语音合成工具集成到智能客服系统中，实现自动语音回复，提高客户服务效率。
2. **在线教育**：利用HeyGen TTS语音合成工具生成教学语音，方便学生随时随地学习。
3. **有声读物**：将文本内容转换为语音，制作有声读物，拓展阅读方式。

