---
slug: mongodb
name: mongodb
version: "1.0.1"
displayName: MongoDB
summary: Design schemas, write queries, and configure MongoDB for consistency and
  performance.
license: MIT
description: |-
  Design schemas, write queries, and configure MongoDB for consistency
  and performance。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,...
tags:
- Integrations
tools:
  - - read
- exec
---

# MongoDB

## When to Use

User needs MongoDB expertise — from schema design to production optimization. Agent handles document modeling, indexing strategies, aggregation pipelines, consistency patterns, and scaling.

## Quick Reference

| Topic | File |
| --- | --- |
| Schema design patterns | `schema.md` |
| Index strategies | `indexes.md` |
| Aggregation pipeline | `aggregation.md` |
| Production configuration | `production.md` |

## Schema Design Philosophy

* Embed when data is queried together and doesn't grow unboundedly
* Reference when data is large, accessed independently, or many-to-many
* Denormalize for read performance, accept update complexity—no JOINs means duplicate data
* Design for your queries, not for normalized elegance

## Document Size Traps

* 16MB max per document—plan for this from day one; use GridFS for large files
* Arrays that grow infinitely = disaster—use bucketing pattern instead
* BSON overhead: field names repeated per document—short names save space at scale
* Nested depth limit 100 levels—rarely hit but exists

## Array Traps

* Arrays > 1000 elements hurt performance—pagination inside documents is hard
* `$push` without `$slice` = unbounded growth; use `$push: {$each: [...], $slice: -100}`
* Multikey indexes on arrays: index entry per element—can explode index size
* Can't have multikey index on more than one array field in compound index

## $lookup Traps

* `$lookup` performance degrades with collection size—no index on foreign collection (until 5.0)
* One `$lookup` per pipeline stage—nested lookups get complex and slow
* `$lookup` with pipeline (5.0+) can filter before joining—massive improvement
* Consider: if you $lookup frequently, maybe embed instead

## Index Strategy

* ESR rule: Equality fields first, Sort fields next, Range fields last
* MongoDB doesn't do efficient index intersection—single compound index often better
* Only one text index per collection—plan carefully; use Atlas Search for complex text
* TTL index for auto-expiration: `{createdAt: 1}, {expireAfterSeconds: 86400}`

## Consistency Traps

* Default read/write concern not fully consistent—`{w: "majority", readConcern: "majority"}` for strong
* Multi-document transactions since 4.0—but add latency and lock overhead; design to minimize
* Single-document operations are atomic—exploit this by embedding related data
* `retryWrites: true` in connection string—handles transient failures automatically

## Read Preference Traps

* Stale reads on secondaries—replication lag can be seconds
* `nearest` for lowest latency—but may read stale data
* Write always goes to primary—read preference doesn't affect writes
* Read your own writes: use `primary` or session-based causal consistency

## ObjectId Traps

* Contains timestamp: `ObjectId.getTimestamp()`—extract creation time without extra field
* Roughly time-ordered—can sort by `_id` for creation order without createdAt
* Not random—predictable if you know creation time; don't rely on for security tokens

## Performance Mindset

* `explain("executionStats")` shows actual execution—not just theoretical plan
* `totalDocsExamined` vs `nReturned` ratio should be ~1—otherwise index missing
* `COLLSCAN` in explain = full collection scan—add appropriate index
* Covered queries: `IXSCAN` + `totalDocsExamined: 0`—all data from index

## Aggregation Philosophy

* Pipeline stages are transformations—think of data flowing through
* Filter early (`$match`), project early (`$project`)—reduce data volume ASAP
* `$match` at start can use indexes; `$match` after `$unwind` cannot
* Test complex pipelines stage by stage—build incrementally

## Common Mistakes

* Treating MongoDB as "schemaless"—still need schema design; just enforced in app not DB
* Not adding indexes—scans entire collection; every query pattern needs index
* Giant documents via array pushes—hit 16MB limit or slow BSON parsing
* Ignoring write concern—data may appear written but not persisted/replicated

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

- Design schemas, write queries, and configure MongoDB for consistency
  and performance
- 触发关键词: write, mongodb, configure, queries, design, schemas

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

### Q1: 如何开始使用MongoDB？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: MongoDB有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
