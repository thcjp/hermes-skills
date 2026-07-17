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
  20 countries for breaki...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: archival, real, agents, time, news, gives
tags:
- Research
tools:
- read
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

## Examples

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
