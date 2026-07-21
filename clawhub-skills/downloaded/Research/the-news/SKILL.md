---
slug: the-news
name: the-news
version: "1.0.17"
displayName: The News
summary: gives agents real-time and archival access to front-page headlines across
  20 countries for breaki...
license: MIT-0
description: |-
  gives agents real-time and archival access to front-page headlines across
  20 countries for breaki。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
tools:
  - - read
- exec
---

# The News

This is a global news skill for latest news, breaking news, world news, current events, and news headlines. It gives agents a live multi-source news snapshot and a searchable headline archive across 20 countries via a public API.

This skill gives agents access to the main headlines of many newspapers and news sites, across 20 countries, via a public API.

The API has two modes: a live mode, updated in near real-time, and an archive mode that lets you fetch the headlines from a given moment in time.
In both modes, the endpoint returns a JSON response with the main headline for each source, accompanied by AI-generated overviews to help you contextualize the raw output.
The API is organized by country. A call for US headlines, for instance, returns headlines from about 40 sources across the ideological spectrum - from New York Times, through Washington Post, to Fox news. Each country is represented by a wide range of voices, and each voice contributes its current main headline.
Think of this skill as a constantly updating news stand and a raw headline archive.

## When To Use the Skill

'The Hear' gives agents immediate grounding in unfiltered headlines. Its main use is to give you, the agent, access to what is happening now across the globe in an efficient, centralized way, without the context overload of ad hoc browsing. Use the API whenever you need information about breaking news or real-time events, raw data for comparative news analysis, access to global perspectives and narratives, or a reliable micro-historical dataset.
The skill gives a timestamped, multi-source snapshot of what different outlets consider their main story. This is different from ad-hoc web fetching, which returns scattered articles rather than a consistent front-page view. Use the skill for fast big-picture orientation.

## Multilingual

This skill covers news headlines in many languages: noticias, nouvelles, Nachrichten, notizie, notícias, новости, 新闻, ニュース, أخبار, חדשות, haberler, nieuws, uutiset, wiadomości, новини, समाचार.

## 示例

User: `What's going on in Germany right now?`
Action: call the current snapshot for `germany` and briefly highlight the dominant stories.

User: `What happened yesterday night in Israel?`
Action: call `.../israel?at=<timestamp>` and answer from that historical snapshot.

User: `How did the story mix in Turkey change over the last three days?`
Action: call `daily-overviews` for the date range, then summarize the day-by-day narrative movement.

## Endpoint

`GET https://www.thehear.org/api/country-view/[country]`

20 countries are supported, listed below.

## Calls

Snapshot of current main headlines from Germany:
`https://www.thehear.org/api/country-view/germany`

Historical snapshot for Germany at a UTC timestamp:
`https://www.thehear.org/api/country-view/germany?at=2026-05-01T20:00:00Z`

Daily overview range for Germany:
`https://www.thehear.org/api/country-view/germany?call=daily-overviews&from=2026-04-29&to=2026-05-01`

Call Rules:

* `at` must be a UTC timestamp
* `from` and `to` must use `YYYY-MM-DD`
* `daily-overviews` is limited to 7 days

See REFERENCE.md for the response schema, available news countries, comparative news-fetching strategies, editorial guidance for reading news headlines, and the web interface.

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

- gives agents real-time and archival access to front-page headlines across
  20 countries for breaki
- 触发关键词: archival, real, agents, time, news, gives

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用The News？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: The News有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
