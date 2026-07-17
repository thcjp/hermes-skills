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
  and performance.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: write, mongodb, configure, queries, design, schemas
tags:
- Integrations
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
