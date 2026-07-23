---
slug: gitcrawl
name: gitcrawl
version: "1.0.0"
displayName: Gitcrawl
summary: "GitHub归档:issue/PR搜索、同步新鲜度、重复聚类,深度挖掘代码仓库信息"
license: MIT
description: |-
  GitHub archive: issue/PR search, sync freshness, duplicate clusters。核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
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

- GitHub archive: issue/PR search, sync freshness, duplicate clusters
- 触发关键词: sync, issue, github, archive, search, gitcrawl

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

### Q1: 如何开始使用Gitcrawl？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Gitcrawl有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
