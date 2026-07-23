---
slug: knowledge-graph
name: knowledge-graph
version: "1.0.0"
displayName: Knowledge Graph
summary: "维护Clawdbot复利知识图谱,增删与替代原子笔记"
  atomic ...
license: MIT
description: |-
  Maintain Clawdbot's compounding knowledge graph under life/areas/**
  by adding/superseding atomic 。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Knowledge Graph

Use the bundled Python script to safely update `life/areas/**`.

## Commands

Add a new fact:

```bash
python3 skills/knowledge-graph/scripts/kg.py add \
  --entity people/safa \
  --category status \
  --fact "Runs Clawdbot on a Raspberry Pi" \
  --source conversation
```

Supersede an old fact (mark old as superseded + create new fact):

```bash
python3 skills/knowledge-graph/scripts/kg.py supersede \
  --entity people/safa \
  --old safa-002 \
  --category status \
  --fact "Moved Clawdbot from Pi to a Mac mini"
```

Regenerate an entity summary from active facts:

```bash
python3 skills/knowledge-graph/scripts/kg.py summarize --entity people/safa
```

## Notes

* Entities live under: `life/areas/<kind>/<slug>/`
* Facts live in `items.json` (array). Summaries live in `summary.md`.
* IDs auto-increment per entity: `<slug>-001`, `<slug>-002`, ...
* Never delete facts; supersede them.

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

- Maintain Clawdbot's compounding knowledge graph under life/areas/**
  by adding/superseding atomic
- 触发关键词: graph, knowledge, clawdbot, compounding, maintain'

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

### Q1: 如何开始使用Knowledge Graph？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Knowledge Graph有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
