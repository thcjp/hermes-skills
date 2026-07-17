---
slug: gitcrawl
name: gitcrawl
version: "1.0.0"
displayName: Gitcrawl
summary: "GitHub archive: issue/PR search, sync freshness, duplicate clusters."
license: MIT
description: |-
  GitHub archive: issue/PR search, sync freshness, duplicate clusters.

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: sync, issue, github, archive, search, gitcrawl
tags:
- Research
tools:
- read
- exec
---

# Gitcrawl

Use local GitHub issue/PR archives before live GitHub search. Check freshness first:

```bash
gitcrawl doctor --json
```

Find candidates:

```bash
gitcrawl threads skill-platform/skill-platform --numbers <issue-or-pr-number> --include-closed --json
gitcrawl neighbors skill-platform/skill-platform --number <issue-or-pr-number> --limit 12 --json
gitcrawl search issues "query" -R skill-platform/skill-platform --state open --json number,title,url
gitcrawl clusters skill-platform/skill-platform --sort size --min-size 5
gitcrawl cluster-detail skill-platform/skill-platform --id <cluster-id>
```

For PR triage, start cached and go live only before mutation/merge decisions:

```bash
gitcrawl gh pr status <number-or-url> -R skill-platform/skill-platform --compact
gitcrawl gh pr view <number-or-url> -R skill-platform/skill-platform --json number,title,state,url,isDraft,headRef,headSha
gitcrawl gh --live pr status <number-or-url> -R skill-platform/skill-platform --compact
```

Use live `gh` plus checkout proof before commenting, labeling, closing, reopening, merging, or filing a PR review:

```bash
gh pr view <number> --json number,title,state,mergedAt,body,files,comments,reviews,statusCheckRollup
gh issue view <number> --json number,title,state,body,comments,closedAt
```

Report absolute dates, repo names, issue/PR numbers, cluster ids, and source gaps. Do not close/label from similarity alone; require matching intent plus live verification.

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
