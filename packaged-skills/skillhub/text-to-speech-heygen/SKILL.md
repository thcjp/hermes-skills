---
slug: "text-to-speech-heygen"
name: "text-to-speech-heygen"
version: "2.23.0"
displayName: "Text to Speech"
summary: "HeyGen TTS语音合成工具's Starfish TTS model. Use"
license: "Proprietary"
description: |-
  Generate speech audio from text using HeyGen's Starfish TTS model。Use when: (1) Generating stand。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Creative
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Text to Speech

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Generate speech audio from text using HeyGen's Starfish TTS model | 支持 | 支持 |
| Use when: (1) Generating stand | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Generate speech audio from text using HeyGen's Starfish TTS model
- Use when: (1) Generating stand
#
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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### Basic TTS

```typescript
const result = await textToSpeech({
  text: "Welcome to our quarterly earnings call.",
  voice_id: "YOUR_VOICE_ID",
});

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

  if (!voice) {
    throw new Error(`No TTS voice found for language: ${language}`);
  }

  const result = await textToSpeech({
    text,
    voice_id: voice.voice_id,
  });

  return result.audio_url;
}

const audioUrl = await generateSpeech("Hello and welcome!", "english");
```

## 常见问题

### Q1: 如何开始使用Text to Speech？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Text to Speech有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

