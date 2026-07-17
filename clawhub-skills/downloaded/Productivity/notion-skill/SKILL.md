---
slug: notion-skill
name: notion-skill
version: "1.0.0"
displayName: Notion
summary: Work with Notion pages and databases via the official Notion API.
license: MIT
description: |-
  Work with Notion pages and databases via the official Notion API.

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: databases, notion, pages, skill
tags:
- Productivity
tools:
- read
- exec
---

# Notion

This skill lets the agent work with **Notion pages and databases** using the official Notion API.

The skill is declarative: it documents **safe, recommended operations** and assumes a local CLI
(`notion-cli`) that actually performs API calls.

## Authentication

* Create a Notion Integration at <https://www.notion.so/my-integrations>
* Copy the Internal Integration Token.
* Export it as:

```bash
export NOTION_API_KEY=secret_xxx
```

Share the integration with the pages or databases you want to access.
Unshared content is invisible to the API.

## Profiles (personal / work)

You may define multiple profiles (e.g. personal, work) via env or config.

Default profile: personal

Override via:

```bash
export NOTION_PROFILE=work
```

## Pages

**Read page:**

```bash
notion-cli page get <page_id>
```

**Append blocks:**

```bash
notion-cli block append <page_id> --markdown "..."
```

Prefer appending over rewriting content.

**Create page:**

```bash
notion-cli page create --parent <page_id> --title "..."
```

## Databases

**Inspect schema:**

```bash
notion-cli db get <database_id>
```

**Query database:**

```bash
notion-cli db query <database_id> --filter <json> --sort <json>
```

**Create row:**

```bash
notion-cli page create --database <database_id> --props <json>
```

**Update row:**

```bash
notion-cli page update <page_id> --props <json>
```

## Schema changes (advanced)

Always inspect diffs before applying schema changes.

Never modify database schema without explicit confirmation.

Recommended flow:

```bash
notion-cli db schema diff <database_id> --desired <json>
notion-cli db schema apply <database_id> --desired <json>
```

## Safety notes

* Notion API is rate-limited; batch carefully.
* Prefer append and updates over destructive operations.
* IDs are opaque; store them explicitly, do not infer from URLs.

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
