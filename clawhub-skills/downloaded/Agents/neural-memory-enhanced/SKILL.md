---
slug: neural-memory-enhanced
name: neural-memory-enhanced
version: "1.0.0"
displayName: Neural Memory Enhanced
summary: Associative memory with spreading activation for persistent, intelligent
  recall. Use PROACTIVELY ...
license: MIT
description: |-
  Associative memory with spreading activation for persistent, intelligent
  recall. Use PROACTIVELY ...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: neural, associative, memory, spreading, enhanced, activation
tags:
- Agents
tools:
- read
- exec
---

# Neural Memory Enhanced

A biologically-inspired memory system that uses spreading activation instead of keyword/vector search. Memories form a neural graph where neurons connect via 20 typed synapses. Frequently co-accessed memories strengthen their connections (Hebbian learning). Stale memories decay naturally. Contradictions are auto-detected.

**Why not just vector search?** Vector search finds documents similar to your query. NeuralMemory finds *conceptually related* memories through graph traversal — even when there's no keyword or embedding overlap. "What decision did we make about auth?" activates time + entity + concept neurons simultaneously and finds the intersection.

## Setup

### 1. Install NeuralMemory

```bash
pip install neural-memory
nmem init
```

This creates `~/.neuralmemory/` with a default brain and configures MCP automatically.

### 2. Configure MCP for Skill平台

Add to your Skill平台 MCP configuration (`~/.skill-platform/mcp.json` or project `skill-platform.json`):

```json
{
  "mcpServers": {
    "neural-memory": {
      "command": "python3",
      "args": ["-m", "neural_memory.mcp"],
      "env": {
        "NEURALMEMORY_BRAIN": "default"
      }
    }
  }
}
```

### 3. Verify

```bash
nmem stats
```

You should see brain statistics (neurons, synapses, fibers).

## Tools Reference

### Core Memory Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| `nmem_remember` | Store a memory | After decisions, errors, facts, insights, user preferences |
| `nmem_recall` | Query memories | Before tasks, when user references past context, "do you remember..." |
| `nmem_context` | Get recent memories | At session start, inject fresh context |
| `nmem_todo` | Quick TODO with 30-day expiry | Task tracking |

### Intelligence Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| `nmem_auto` | Auto-extract memories from text | After important conversations — captures decisions, errors, TODOs automatically |
| `nmem_recall` (depth=3) | Deep associative recall | Complex questions requiring cross-domain connections |
| `nmem_habits` | Workflow pattern suggestions | When user repeats similar action sequences |

### Management Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| `nmem_health` | Brain health diagnostics | Periodic checkup, before sharing brain |
| `nmem_stats` | Brain statistics | Quick overview of memory counts |
| `nmem_version` | Brain snapshots and rollback | Before risky operations, version checkpoints |
| `nmem_transplant` | Transfer memories between brains | Cross-project knowledge sharing |

## Workflow

### At Session Start

1. Call `nmem_context` to inject recent memories into your awareness
2. If user mentions a specific topic, call `nmem_recall` with that topic

### During Conversation

3. When a decision is made: `nmem_remember` with type="decision"
4. When an error occurs: `nmem_remember` with type="error"
5. When user states a preference: `nmem_remember` with type="preference"
6. When asked about past events: `nmem_recall` with appropriate depth

### At Session End

7. Call `nmem_auto` with action="process" on important conversation segments
8. This auto-extracts facts, decisions, errors, and TODOs

## Examples

### Remember a decision

```text
nmem_remember(
  content="Use PostgreSQL for production, SQLite for development",
  type="decision",
  tags=["database", "infrastructure"],
  priority=8
)
```

### Recall with spreading activation

```text
nmem_recall(
  query="database configuration for production",
  depth=1,
  max_tokens=500
)
```

Returns memories found via graph traversal, not keyword matching. Related memories (e.g., "deploy uses Docker with pg_dump backups") surface even without shared keywords.

### Trace causal chains

```text
nmem_recall(
  query="why did the deployment fail last week?",
  depth=2
)
```

Follows CAUSED_BY and LEADS_TO synapses to trace cause-and-effect chains.

### Auto-capture from conversation

```text
nmem_auto(
  action="process",
  text="We decided to switch from REST to GraphQL because the frontend needs flexible queries. The migration will take 2 sprints. TODO: update API docs."
)
```

Automatically extracts: 1 decision, 1 fact, 1 TODO.

## Key Features

* **Zero LLM dependency** — Pure algorithmic: regex, graph traversal, Hebbian learning
* **Spreading activation** — Associative recall through neural graph, not keyword/vector search
* **20 synapse types** — Temporal (BEFORE/AFTER), causal (CAUSED_BY/LEADS_TO), semantic (IS_A/HAS_PROPERTY), emotional (FELT/EVOKES), conflict (CONTRADICTS)
* **Memory lifecycle** — Short-term → Working → Episodic → Semantic with Ebbinghaus decay
* **Contradiction detection** — Auto-detects conflicting memories, deprioritizes outdated ones
* **Hebbian learning** — "Neurons that fire together wire together" — memory improves with use
* **Temporal reasoning** — Causal chain traversal, event sequences, temporal range queries
* **Brain versioning** — Snapshot, rollback, diff brain state
* **Brain transplant** — Transfer filtered knowledge between brains
* **Vietnamese + English** — Full bilingual support for extraction and sentiment

## Depth Levels

| Depth | Name | Speed | Use Case |
| --- | --- | --- | --- |
| 0 | Instant | <10ms | Quick facts, recent context |
| 1 | Context | ~50ms | Standard recall (default) |
| 2 | Habit | ~200ms | Pattern matching, workflow suggestions |
| 3 | Deep | ~500ms | Cross-domain associations, causal chains |

## Notes

* Memories are stored locally in SQLite at `~/.neuralmemory/brains/<brain>.db`
* No data is sent to external services (unless optional embedding provider is configured)
* Brain isolation: each brain is independent, no cross-contamination
* `nmem_remember` returns fiber_id for reference tracking
* Priority scale: 0 (trivial) to 10 (critical), default 5
* Memory types: fact, decision, preference, todo, insight, context, instruction, error, workflow, reference

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
