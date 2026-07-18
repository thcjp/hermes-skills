---
slug: ace-music-tool-free
name: ace-music-tool-free
version: "1.0.0"
displayName: ACE音乐生成-免费版
summary: 通过ACE-Step模型免费生成带人声的AI歌曲,支持多语种、多风格,适合个人创作者快速出曲。
license: MIT
edition: free
description: |-
  ACE音乐生成免费版,面向个人内容创作者的AI音乐生成工具。

  核心能力:
  - 文本描述生成完整歌曲(含人声与歌词)
  - 支持流行、民谣、电子、爵士等多种风格
  - 提供中文、英文、日文等多语种演唱
  - 可调节时长、节奏(BPM)、调式等基础参数

  适用场景:
  - 短视频创作者快速生成背景音乐
  - 独立开发者制作游戏或应用配乐
  - 音乐爱好者进行创意灵感探索

  差异化:免费版聚焦核心生成能力,操作简单,适合个人用户体验AI音乐创作。提供基础参数调节与标准时长输出。

  触发关键词: AI音乐, 生成歌曲, 文生音乐, ACE-Step, 免费音乐, 人声合成, 歌词生成, 背景音乐
tags:
- Creative
- 音乐生成
- AI创作
tools:
- read
- exec
---

# ACE音乐生成工具 - 免费版

## 概述

ACE音乐生成免费版是一款面向个人用户的AI音乐创作工具。通过自然语言描述即可生成包含人声、歌词的完整歌曲,无需乐理知识,几分钟即可获得原创音乐作品。

本版本依托 ACE-Step 1.5 模型能力,提供基础的文生音乐(text2music)功能,支持多种音乐风格与语言,适合短视频创作者、独立开发者及音乐爱好者快速产出音乐内容。

## 核心能力

| 能力项 | 免费版支持 | 说明 |
|:-------|:-----------|:-----|
| 文本生成音乐 | 是 | 输入描述即可生成歌曲 |
| 自定义歌词 | 是 | 支持 Verse/Chorus 结构标记 |
| 纯音乐模式 | 是 | 仅生成伴奏无人声 |
| 多语种演唱 | 是 | 支持中英日韩等 |
| 时长控制 | 限制 | 最长 60 秒 |
| 批量生成 | 否 | 单次一首 |
| 风格翻唱 | 否 | PRO 版支持 |
| 片段重绘 | 否 | PRO 版支持 |

## 使用场景

### 场景一:短视频背景音乐

用户制作 30 秒短视频,需要一段轻快的流行风格背景音乐。

```bash
scripts/generate.sh "upbeat pop song about summer vacation" \
  --duration 30 \
  --instrumental \
  --output summer_bgm.mp3
```

### 场景二:歌词 demo 创作

音乐创作者希望快速将一段歌词转化为可听的人声 demo。

```bash
scripts/generate.sh "gentle acoustic ballad, female vocal" \
  --lyrics "[Verse 1]\n阳光洒进窗台\n\n[Chorus]\n我们都是追梦人" \
  --duration 60 \
  --language zh \
  --output demo.mp3
```

### 场景三:学习/工作背景音

用户希望生成一段 lo-fi 助眠或专注背景音乐。

```bash
scripts/generate.sh "lo-fi hip hop beats, chill, rainy night" \
  --instrumental \
  --duration 60 \
  --output lofi_focus.mp3
```

## 快速开始

### 第一步:配置 API Key

```bash
# 注册免费账号获取 Key
export ACE_MUSIC_API_KEY="your_api_key_here"
```

获取地址:`https://acemusic.ai/playground/api-key`

### 第二步:执行生成命令

```bash
scripts/generate.sh "rock anthem, energetic" \
  --bpm 140 \
  --key "E minor" \
  --output rock.mp3
```

### 第三步:获取结果

脚本将生成文件路径输出到 stdout,直接展示给用户即可。

## 配置示例

基础配置项说明:

```bash
# 环境变量
ACE_MUSIC_API_KEY=your_key         # 必填
ACE_MUSIC_BASE_URL=https://api.acemusic.ai  # 默认值

# 常用参数组合
# 纯音乐 + 长时长
--instrumental --duration 60

# 自定义歌词 + 指定语言
--lyrics "[Verse]...\n[Chorus]..." --language zh

# 固定随机种子(可复现)
--seed 42
```

## 最佳实践

1. **提示词要具体**:描述风格、乐器、情绪,例如"jazz, saxophone solo, smoky bar, melancholic"
2. **歌词用结构标记**:使用 `[Verse]`、`[Chorus]`、`[Bridge]` 分段,生成效果更佳
3. **时长选择**:免费版建议 30-60 秒,过短可能不完整,过长受限于配额
4. **语言匹配**:歌词为中文时务必加 `--language zh`,否则可能出现发音异常
5. **先试短后做长**:先用 30 秒测试风格是否符合预期,再生成完整版本

## 常见问题

### Q1:生成的音乐有杂音或人声不清晰?
A:尝试调整提示词,避免过多风格堆叠;确认网络稳定;如使用 `--sample-mode`,改为手动指定歌词模式。

### Q2:免费版有调用次数限制吗?
A:API 本身免费,但免费版单次时长限制为 60 秒,且不支持批量生成。如需更长时长或批量,请使用 PRO 版。

### Q3:可以生成纯中文歌词的歌曲吗?
A:可以,使用 `--language zh` 参数,并在 `--lyrics` 中提供中文歌词即可。

### Q4:生成的 MP3 文件保存在哪?
A:默认保存至当前工作目录,文件名由 `--output` 参数指定。如不指定,脚本自动生成随机文件名。

### Q5:如何复现同一首歌曲?
A:使用相同的提示词、歌词和 `--seed` 参数值即可生成相似结果。

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Bash shell + curl(脚本依赖)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| ACE Music API | 外部 API | 必需 | 官网注册免费获取 |
| curl | 命令行工具 | 必需 | 系统自带 |
| jq | JSON 处理 | 推荐 | 包管理器安装 |
| base64 | 解码工具 | 必需 | 系统自带 |

### API Key 配置
- **环境变量名**: `ACE_MUSIC_API_KEY`
- **获取方式**: 访问 `https://acemusic.ai/playground/api-key` 注册免费账号
- **存储建议**: 写入 `.env` 文件或系统环境变量,避免硬编码到脚本

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务,核心生成流程依赖外部API
