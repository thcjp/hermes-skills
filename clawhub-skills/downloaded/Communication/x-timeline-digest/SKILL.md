---
slug: x-timeline-digest
name: x-timeline-digest
version: "1.0.2"
displayName: X Timeline Digest
summary: Build a deduplicated digest from X (Twitter) For You and Following timelines
  using bird. Outputs ...
license: MIT
description: |-
  Build a deduplicated digest from X (Twitter) For You and Following timelines
  using bird. Outputs ...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: twitter, timeline, deduplicated, build, digest
tags:
- Communication
tools:
- read
- exec
---

# X Timeline Digest

## Overview

This skill uses bird to read X/Twitter timelines and build a high-signal digest.
Sources:

* For You timeline
* Following timeline
  What it does:

1. Fetch recent tweets
2. Filter incrementally (avoid reprocessing)
3. Deduplicate (ID + near-duplicate text)
4. Rank and trim
5. Generate a Chinese digest
6. Output a structured payload

> Delivery (Telegram, email, etc.) is NOT handled here.
> Upstream Skill平台 workflows decide how to notify users.

---

## Configuration

All config is read from: skills.entries["x-timeline-digest"].config

### Config fields

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| intervalHours | number | 6 | Interval window in hours |
| fetchLimitForYou | number | 100 | Tweets fetched from For You |
| fetchLimitFollowing | number | 60 | Tweets fetched from Following |
| maxItemsPerDigest | number | 25 | Max tweets in one digest |
| similarityThreshold | number | 0.9 | Near-duplicate similarity threshold |
| statePath | string | ~/.skill-platform/state/x-timeline-digest.json | State file path |

---

## Dependencies

* bird must be installed and available in PATH
* bird must already be authenticated (cookie login)
* Read-only usage

## Usage

### 1. Basic (Raw JSON)

Run the digest generator to get a clean, deduplicated JSON payload:

```bash
node skills/x-timeline-digest/digest.js
```

### 2. Intelligent Digest (Recommended)

To generate the "Smart Brief" (Categorized, Summarized, Denoised):

1. Run the script: `node skills/x-timeline-digest/digest.js > digest.json`
2. Read the prompt template: `read skills/x-timeline-digest/PROMPT.md`
3. Send the prompt to your LLM, injecting the content of `digest.json` where `{{JSON_DATA}}` is.

*Note: The script automatically applies heuristic filtering (removes "gm", ads, short spam) before outputting JSON.*

## Bird Commands Used

## For You timeline: bird home -n --json Following timeline: bird home --following -n --json

## State Management

State is persisted to statePath.

### State structure

{
"lastRunAt": "2026-02-01T00:00:00+08:00",
"sentTweetIds": {
"123456789": "2026-02-01T00:00:00+08:00"
}
}

### Rules

* Tweets already in sentTweetIds must not be included again
* After a successful run:
* Update lastRunAt
* Add pushed tweet IDs to sentTweetIds
* Keep IDs for at least 30 days

---

## Processing Pipeline

1. Fetch from For You and Following
2. Incremental filter using lastRunAt
3. Hard deduplication by tweet id
4. Near-duplicate merge using text similarity
5. Rank and trim to maxItemsPerDigest
6. **Generate a Categorized Chinese Digest** (via PROMPT.md + LLM)
   * Categories: 🤖 AI & Tech, 💰 Crypto & Markets, 💡 Insights, 🗞️ Other
   * Language: Simplified Chinese
   * Format: [Author](/api/v1/skills/x-timeline-digest/file?path=URL&ownerHandle=seandong): Summary
   * Denoising: Remove ads and low-value content

---

## Output

The skill returns one JSON object:
{
"window": {
"start": "2026-02-01T00:00:00+08:00",
"end": "2026-02-01T06:00:00+08:00",
"intervalHours": 6
},
"counts": {
"forYouFetched": 100,
"followingFetched": 60,
"afterIncremental": 34,
"afterDedup": 26,
"final": 20
},
"digestText": "中文摘要内容",
"items": [
{
"id": "123456",
"author": "@handle",
"createdAt": "2026-02-01T02:15:00+08:00",
"text": "tweet text",
"url": "<https://x.com/handle/status/123456>",
"sources": ["following"]
}
]
}

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
