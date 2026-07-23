---
slug: knowledge-graph-skill
name: knowledge-graph-skill
version: "1.1.1"
displayName: Knowledge Graph
summary: "嵌入式知识图谱,持久结构化知识,主动使用"
  proactively — do NOT wai...
license: MIT
description: |-
  Embedded knowledge graph for persistent structured knowledge。ALWAYS
  use proactively — do NOT wai。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Development
- Agents
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Knowledge Graph

Personal KG stored as JSON, queried via CLI scripts. Produces a compact KGML summary for session context.
Core instructions are in AGENTS.md (auto-injected by install). This file covers setup, advanced usage, and reference only.

## First-Time Setup

```bash
node scripts/install.mjs [--workspace /path/to/workspace] [--platform skill-platform|claude|gemini]
```

Auto-detects platform and patches the agent instructions file (`AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`) with KG instructions + graph summary. Idempotent.

## KGML Format Reference

```text
#KGML v2 | <count>e <count>r | depth:<N> | <date>
[category]
Label(Alias):type — attr1,attr2
  ChildLabel(CA):type — attrs    ← indent = parent>child
%rels
A>verb>B C>verb>D                ← cross-branch relations (aliases)
%vault key1,key2                 ← vault key names (no values)
```

## Advanced Query Commands

Beyond the basics in AGENTS.md (`find`, `traverse`, `rels`):

```bash
node scripts/query.mjs children <id>      # Direct children
node scripts/query.mjs type <type>         # All entities of a type
node scripts/query.mjs cat <category>      # All in category
node scripts/query.mjs orphans             # Unlinked entities
node scripts/query.mjs stats               # Graph statistics
node scripts/query.mjs recent [--days 7]   # Created/updated recently
node scripts/query.mjs timeline [--from YYYY-MM-DD] [--to YYYY-MM-DD]
node scripts/query.mjs changed             # Modified after creation
node scripts/query.mjs uncertain           # Confidence < 0.5
```

## Merge

```bash
node scripts/merge.mjs --target <id> --source <id> --mode absorb|nest
```

## Vault (secrets)

```bash
node scripts/vault.mjs set <key> <value> --note "description"
node scripts/vault.mjs get <key>          # Raw value (for piping)
node scripts/vault.mjs list               # Keys only
node scripts/vault.mjs del <key>
```

## Depth Heuristic — How Many Layers to Extract

Before adding a rich knowledge item (article, paper, report, system description), assess complexity first:

```bash
node scripts/depth-check.mjs "paste text or summary here"
echo "article text" | node scripts/depth-check.mjs
node scripts/depth-check.mjs --file /path/to/article.txt
node scripts/depth-check.mjs --json    # machine-readable

```

**Key rule:** Never stop at 2 layers for complex content. If score ≥ 4, extract all named orgs, events, policies, and cross-relations — not just the top-level themes.

## Visualization

```bash
node scripts/visualize.mjs                # → data/kg-viz.html
node scripts/visualize.mjs --output /tmp/graph.html
```

ALWAYS use this script. Do NOT write custom HTML. Output is self-contained, offline, no CDN.

Parent edges render as **blue dashed arrows** (60% opacity). Regular edges are red solid arrows.

## Configuration

All settings have sensible defaults. Override only what you need — config stores only your changes.

```bash
node scripts/config.mjs                       # list all settings with current values
node scripts/config.mjs get <key>              # get a value (e.g. summary.tokenBudget)
node scripts/config.mjs set <key> <value>      # set a value
node scripts/config.mjs reset <key>            # reset single key to default
node scripts/config.mjs reset --all            # reset everything
node scripts/config.mjs --json                 # full config as JSON
```

### Available Settings

| Section | Key | Default | Description |
| --- | --- | --- | --- |
| **summary** | `tokenBudget` | 5000 | Max tokens for kg-summary.md |
|  | `maxChildDepth` | auto | Tree depth (null=auto: 3/<100, 2/100-400, 1/>400) |
|  | `maxAttrLen` | 40 | Max characters for attribute values |
|  | `maxPerRoot` | 4 | Max relations shown per root subtree |
|  | `compactThreshold` | 400 | Entity count for compact mode |
|  | `mediumThreshold` | 200 | Entity count for medium depth |
| **validation** | `minEntities` | 30 | Min entities for extraction PASS |
|  | `minRelationRatio` | 0.5 | Relations per entity ratio |
|  | `minDepth` | 3 | Min hierarchy depth for PASS |
|  | `minEvents` | 3 | Min event nodes for PASS |
| **depthCheck** | `entityCapForEstimate` | 50 | Cap NER count for target estimation |
|  | `minEntitiesMultiplier` | 1.0 | Named entities → min target multiplier |
|  | `extraEntities` | 30 | Added to min for max entity range |
| **consolidation** | `autoNest` | true | Auto-nest single-relation orphans |
|  | `mergeSuggestions` | true | Suggest merges for similar labels |
|  | `pruneEmptyAttrs` | true | Remove empty/null attrs |
|  | `levenshteinThreshold` | 2 | Max edit distance for merge suggestions |
| **visualization** | `repulsion` | 5000 | Physics repulsion force |
|  | `edgeRestLength` | 160 | Default edge rest length |
|  | `overlapPenalty` | 3 | Overlap repulsion multiplier |
|  | `simulationSteps` | 500 | Physics simulation iterations |
|  | `initialSpread` | 1.5 | Initial node spread multiplier |
|  | `zoomAnimationMs` | 400 | Zoom-to-node animation duration |

Config file: `data/kg-config.json` (per-agent, gitignored).

## Cross-Agent Access (read-only)

```javascript
import { createReader } from '<path-to-skill>/lib/reader.mjs';
const kg = createReader();
kg.search("query"); kg.traverse("id", { depth: 2 }); kg.stats();
```

Or CLI: `node scripts/export.mjs --format json --target /path/to/output.json`

## Memory Import

```bash
node scripts/import-memory.mjs            # dry-run
node scripts/import-memory.mjs --apply    # add with confidence 0.5
```

Then: `node scripts/query.mjs uncertain` to review auto-imported entities.

## Knowledge Entity Guide

The `knowledge` type covers both declarative and procedural knowledge. Use attrs and tags to differentiate:

| Kind | Tags | Key attrs | Example |
| --- | --- | --- | --- |
| Fact/finding | `#fact`, `#til` | `source`, `field`, `summary` | "LLMs use ~4 chars per token" |
| Research/paper | `#paper`, `#research` | `source`, `field`, `summary`, `author` | AI alignment paper findings |
| Idea | `#idea` | `summary`, `status` | "Build a CLI for KG queries" |
| How-to/procedure | `#howto`, `#procedure` | `steps`, `context`, `summary` | "How to deploy on Pi" |
| Mental model | `#mental-model`, `#framework` | `steps`, `context`, `summary` | "Debug network: ping→DNS→firewall" |
| Workflow | `#workflow` | `steps`, `context`, `summary` | "Code review: tests first, then impl" |

**Attrs for procedural knowledge:**

* `steps`: ordered procedure as string (use `→` or numbered: `"1. Check logs → 2. Reproduce → 3. Fix → 4. Test"`)
* `context`: when/where to apply this knowledge (e.g. `"when network is down"`, `"during code review"`)
* `summary`: short description of what this knowledge is about

## Consolidation

Run `node scripts/consolidate.mjs` weekly or when entity count > 80. Then `summarize.mjs`.

## Security

* NEVER print vault values in chat or log to memory/ files
* vault.enc.json and .vault-key must never be in context
* Other agents: read-only via reader.mjs, NO write access

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

- Embedded knowledge graph for persistent structured knowledge
- ALWAYS
  use proactively — do NOT wai
- 触发关键词: graph, knowledge, persistent, structured, embedded, skill

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

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
