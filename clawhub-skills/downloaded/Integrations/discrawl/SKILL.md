---
slug: discrawl
name: discrawl
version: "1.0.0"
displayName: Discrawl
summary: "Discord archive: search, sync freshness, DMs, channel slices, SQL counts."
license: MIT
description: |-
  Discord archive: search, sync freshness, DMs, channel slices, SQL counts.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: discord, sync, archive, discrawl, freshness, search
tags:
- Integrations
tools:
- read
- exec
---

# Discrawl

Use local Discord archive data before live Discord APIs. Check freshness for recent/current questions:

```bash
discrawl status --json
discrawl doctor
```

Refresh only when stale or asked:

```bash
discrawl sync --source wiretap
discrawl sync
```

Query with bounded slices:

```bash
DISCRAWL_NO_AUTO_UPDATE=1 discrawl search --limit 20 "query"
discrawl messages --channel '#maintainers' --days 7 --all
discrawl dms --last 20
DISCRAWL_NO_AUTO_UPDATE=1 discrawl --json sql "select count(*) from messages;"
```

Report absolute date spans, channel/DM names, counts, and known gaps. Use read-only SQL for exact counts/rankings. Never use `--unsafe --confirm` unless the user explicitly requests a reviewed DB mutation.

Boundaries: bot sync needs configured Discord bot credentials. Wiretap reads local Discord Desktop artifacts only; do not extract user tokens, call Discord as the user, or write to Discord storage. Git-share snapshots must not include secrets or `@me` DM rows.

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
