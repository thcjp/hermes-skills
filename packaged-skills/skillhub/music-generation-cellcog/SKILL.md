---
slug: "music-generation-cellcog"
name: "music-generation-cellcog"
version: 1.0.12
displayName: "Music Generation Cel"
summary: "CellCog驱动AI音乐生成,原创器乐与人声5秒到10分钟。AI music generation powered by CellCog。Original instrumental and"
license: "Proprietary"
description: |-
  AI music generation powered by CellCog。Original instrumental and vocal
  tracks, 5 seconds to 10 m。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理.
tags:
  - Creative
  - 音乐生成
  - 音频
  - 创意
  - agent
  - cellcog
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# Music Generation Cel

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Music Generation Celog驱动AI音乐生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

- AI music generation powered by CellCog
- Original instrumental and vocal
  tracks, 5 seconds to 10 m
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 内容生成 | 提示词与风格参数 | 生成内容与质量评分 |
| CellCog驱动A | 目标数据与配置参数 | 处理结果与执行状态 |
| 原创器乐与人声5秒到 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | music-generation-cellcog处理的内容输入 |,  |
| content | string | 否 | music-generation-cellcog处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "cellcog 相关配置参数",
    result: "cellcog 相关配置参数",
    result: "cellcog 相关配置参数",
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

**Cinematic score:**

> "Compose a 2-minute cinematic score for a nature documentary finale. Begin with solo cello (melancholic), layer in strings and piano at 40 seconds, build to a hopeful orchestral swell, resolve with gentle piano. Think Planet Earth meets Interstellar."

**Lo-fi background:**

> "Create 5 minutes of lo-fi study beats. Soft piano, mellow drums, vinyl crackle, gentle bass. 75 BPM. Warm and unobtrusive — good for focus."

**Podcast intro + outro:**

> "Create a podcast intro (8 seconds) and outro (6 seconds). Show is a tech startup podcast. Intro: energetic, modern electronic with a hook. Outro: same vibe but mellower wind-down. Should feel like the same show."

**Song with vocals:**

> "Write a 3-minute upbeat indie pop song with female vocals. Theme: the excitement of moving to a new city. Catchy chorus, acoustic guitar foundation, builds with drums and synth. Feel-good, sing-along energy."

**Game soundtrack:**

> "Compose a 2-minute boss battle theme for a fantasy RPG. Intense orchestral with choir, driving percussion, escalating tension. Think Dark Souls meets Final Fantasy."

---
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 常见问题

### Q1: 如何开始使用Music Generation Cel？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

