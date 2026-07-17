---
slug: graincrawl
name: graincrawl
version: "1.0.1"
displayName: Graincrawl
summary: "Granola archive: search, sync freshness, notes, transcripts, panels, SQL."
license: MIT
description: |-
  Granola archive: search, sync freshness, notes, transcripts, panels,
  SQL.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: sync, graincrawl, granola, archive, freshness, search
tags:
- Integrations
tools:
- read
- exec
---

# Graincrawl

Use local Granola archive data first. Check freshness for recent/current questions:

```bash
graincrawl doctor --json
graincrawl status --json
```

Refresh only when stale or asked:

```bash
graincrawl sync --source private-api
graincrawl sync --source desktop-cache
```

Query with bounded reads:

```bash
graincrawl search "query"
graincrawl notes --json
graincrawl note get <id>
graincrawl transcripts get <id>
graincrawl panels get <id>
graincrawl --json sql "select count(*) as notes from notes;"
```

Report absolute date spans, note titles, source gaps, and transcript/panel availability. Use read-only SQL for exact counts/rankings. Before encrypted source debugging, run explicit unlock/secrets checks; do not surprise-prompt Keychain.

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
