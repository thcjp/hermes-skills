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
  using bird。Outputs。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
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

### Q1: 如何开始使用X Timeline Digest？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: X Timeline Digest有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
