---
slug: ai-podcast
name: ai-podcast
version: "1.0.11"
displayName: Ai Podcast
summary: "用MagicPodcast从PDF/文本/笔记/链接生成AI播客剧集"
  in OpenClaw. Cr...
license: MIT
description: |-
  Generate AI podcast episodes from PDFs, text, notes, and links using
  MagicPodcast in OpenClaw。Cr。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Podcast Generation from PDF, Text, and Links

## What this skill does

Magic Podcast turns PDFs, documents, and notes into a natural two-host conversation you can listen to in minutes.

Use MagicPodcast to:

1. Ask what the podcast should be about.
2. Ask for source: PDF URL or pasted text.
3. Ask for podcast language (do not assume).
4. Confirm: `Ok, want me to make a podcast of this "topic/pdf" in "language". Should I do it?`
5. Create a two-person dialogue podcast from that exact source.
6. Immediately return `https://www.magicpodcast.app/app` so user can open their podcast dashboard.
7. Check status only when user asks.
8. Return title plus the shareable podcast URL when complete.

## Keywords

ai podcast, podcast, podcast generator, ai podcast generator, pdf to podcast, text to podcast, podcast from pdf, audio podcast, magicpodcast

## Setup

Set required env:

```bash
export MAGICPODCAST_API_URL="https://api.magicpodcast.app"
export MAGICPODCAST_API_KEY="[REDACTED]"
```

Get API key:
<https://www.magicpodcast.app/skill-platform>

## Guided onboarding (one step at a time)

1. Ask one question at a time, then wait for the user's reply before asking the next.
2. If API key is missing or invalid, stop and say:
   `It's free to get started, and it takes under a minute. Open https://www.magicpodcast.app/skill-platform, sign in with Google, copy your API key, and paste it here.`
3. If user has a local PDF file, ask them to upload it to a reachable URL first.
4. After key is available, continue:
   1. topic
   2. source (PDF URL or pasted text)
   3. language
   4. final confirmation before create

## Secure command templates

Never interpolate raw user text directly into shell commands.
Always validate first, then JSON-encode with `jq`.

```bash
safe_job_id() {
  printf '%s' "$1" | grep -Eq '^[A-Za-z0-9_-]{8,128}$'
}

safe_http_url() {
  printf '%s' "$1" | grep -Eq '^https?://[^[:space:]]+$'
}
```

Create from PDF:

```bash
if ! safe_http_url "$PDF_URL"; then
  echo "Invalid PDF URL" >&2
  exit 1
fi

payload="$(jq -n --arg pdfUrl "$PDF_URL" --arg language "$LANGUAGE" '{pdfUrl:$pdfUrl,language:$language}')"

curl -sS -X POST "$MAGICPODCAST_API_URL/agent/v1/podcasts/pdf" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MAGICPODCAST_API_KEY" \
  --data-binary "$payload"
```

Create from text:

```bash
payload="$(jq -n --arg text "$SOURCE_TEXT" --arg language "$LANGUAGE" '{text:$text,language:$language}')"

curl -sS -X POST "$MAGICPODCAST_API_URL/agent/v1/podcasts/text" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MAGICPODCAST_API_KEY" \
  --data-binary "$payload"
```

Check job once:

```bash
if ! safe_job_id "$JOB_ID"; then
  echo "Invalid job id" >&2
  exit 1
fi

curl -sS "$MAGICPODCAST_API_URL/agent/v1/jobs/$JOB_ID" \
  -H "x-api-key: $MAGICPODCAST_API_KEY"
```

* Signed-in users can generate free podcast.
* Expected generation time is usually 2-5 minutes.
* Right after starting, direct users to `https://www.magicpodcast.app/app`.
* Tell the user this page is their dashboard: they can see created podcasts, live progress/status, and finished episodes.
* Return `outputs.shareUrl` as the default completion link.
* If `outputs.shareUrl` is missing, fall back to `outputs.appUrl`.
* On completion, answer: `Here is your podcast link: <url>`.
* If API returns an error, surface the exact error message and details.
* Warn users not to send sensitive documents unless they approve external processing.

Status checks:

* `statusLabel = "complete"`: return `outputs.shareUrl` (or `outputs.appUrl` as fallback).
* `statusLabel = "failed"`: return error message/details to user.

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

- Generate AI podcast episodes from PDFs, text, notes, and links using
  MagicPodcast in OpenClaw
- 触发关键词: links, pdfs, text,, generate, pdf,, episodes, generation, podcast

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

### Q1: 如何开始使用Ai Podcast？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Ai Podcast有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
