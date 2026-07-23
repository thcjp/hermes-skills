---
slug: discrawl
name: discrawl
version: "1.0.0"
displayName: Discrawl
summary: "Discord archive: search, sync freshness, DMs, channel slices, SQL counts."
license: MIT
description: |-
  Discord archive: search, sync freshness, DMs, channel slices, SQL counts。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Discord archive: search, sync freshness, DMs, channel slices, SQL counts
- 触发关键词: discord, sync, archive, discrawl, freshness, search

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

### Q1: 如何开始使用Discrawl？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Discrawl有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
