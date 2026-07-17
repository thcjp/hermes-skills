---
slug: gif-whatsapp
name: gif-whatsapp
version: "1.3.0"
displayName: Gif Whatsapp
summary: Search and send GIFs on WhatsApp. Handles the Tenor→MP4 conversion required
  for WhatsApp.
license: MIT-0
description: |-
  Search and send GIFs on WhatsApp. Handles the Tenor→MP4 conversion required
  for WhatsApp.

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: whatsapp, gifs, search, send, handles, gif
tags:
- Research
tools:
- read
- exec
---

# Gif Whatsapp

Send GIFs naturally in WhatsApp conversations.

## CRITICAL: WhatsApp GIF Workflow

WhatsApp doesn't support direct Tenor/Giphy URLs. You MUST:

1. Download the GIF
2. Convert to MP4
3. Send with `gifPlayback: true`

## Complete Workflow

### Step 1: Search for GIF

```bash
gifgrep "SEARCH QUERY" --max 5 --format url
```

Search in English for best results.

**Always get 5 results and pick the best one** based on the filename/description - don't just take the first result.

### Step 2: Download the GIF

```bash
curl -sL "GIF_URL" -o /tmp/gif.gif
```

### Step 3: Convert to MP4

```bash
ffmpeg -i /tmp/gif.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" /tmp/gif.mp4 -y
```

### Step 4: Copy to workspace (REQUIRED!)

```bash
cp /tmp/gif.mp4 /root/.skill-platform/workspace/gif.mp4
```

⚠️ The message tool can ONLY send files from the workspace directory. Files in `/tmp` will fail with `LocalMediaAccessError`.

### Step 5: Send via message tool

```text
message action=send to=NUMBER message=" " filePath=/root/.skill-platform/workspace/gif.mp4 gifPlayback=true
```

Use a single space as the message body — WhatsApp requires a non-empty message to send media, but the space won't be visible to the recipient.

## One-liner Example

```bash
gifgrep "thumbs up" --max 3 --format url

curl -sL "https://media.tenor.com/xxx.gif" -o /tmp/g.gif && \
ffmpeg -i /tmp/g.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" /tmp/g.mp4 -y 2>/dev/null && \
cp /tmp/g.mp4 /root/.skill-platform/workspace/g.mp4

```

## When to Send GIFs

✅ Good times:

* User asks for a GIF
* Celebrating good news
* Funny reactions
* Expressing emotions (excitement, facepalm, etc.)

❌ Don't overuse:

* One GIF per context is enough
* Not every message needs a GIF

## Popular Search Terms

| Emotion | Search Terms |
| --- | --- |
| Happy | celebration, party, dancing, excited |
| Approval | thumbs up, nice, good job, applause |
| Funny | laugh, lol, haha, funny |
| Shocked | mind blown, shocked, surprised, wow |
| Sad | crying, sad, disappointed |
| Frustrated | facepalm, ugh, annoyed |
| Love | heart, love, hug |
| Cool | sunglasses, cool, awesome |

## Security & Safety Notes

* **Source domains**: gifgrep only searches trusted GIF providers (Tenor, Giphy)
* **File handling**: Downloads go to `/tmp`, then MUST be copied to workspace before sending (message tool only allows workspace paths)
* **Empty caption**: A single space is used as the message body so WhatsApp sends the GIF without visible text
* **WhatsApp integration**: Uses the platform's built-in `message` tool — no separate WhatsApp credentials needed
* **ffmpeg safety**: Processes only GIF files from trusted providers; no arbitrary file execution

## Why This Works

* WhatsApp converts all GIFs to MP4 internally
* Direct Tenor/Giphy URLs often fail
* MP4 with `gifPlayback=true` displays as looping GIF
* Small file size = fast delivery

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
