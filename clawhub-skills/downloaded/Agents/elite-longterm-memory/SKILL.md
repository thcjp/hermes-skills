---
slug: elite-longterm-memory
name: elite-longterm-memory
version: "1.2.3"
displayName: Elite Longterm Memory
summary: Ultimate AI agent memory system for Cursor, Claude, ChatGPT & Copilot. WAL
  protocol + vector sear...
license: MIT
description: |-
  Ultimate AI agent memory system for Cursor, Claude, ChatGPT & Copilot.
  WAL protocol + vector sear...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: longterm, memory, system, elite, cursor, ultimate, agent
tags:
- Agents
- Development
tools:
- read
- exec
---

# Elite Longterm Memory

**The ultimate memory system for AI agents.** Combines 6 proven approaches into one bulletproof architecture.

Never lose context. Never forget decisions. Never repeat mistakes.

## Architecture Overview

```text
┌─────────────────────────────────────────────────────────────────┐
│                    ELITE LONGTERM MEMORY                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   HOT RAM   │  │  WARM STORE │  │  COLD STORE │             │
│  │             │  │             │  │             │             │
│  │ SESSION-    │  │  LanceDB    │  │  Git-Notes  │             │
│  │ STATE.md    │  │  Vectors    │  │  Knowledge  │             │
│  │             │  │             │  │  Graph      │             │
│  │ (survives   │  │ (semantic   │  │ (permanent  │             │
│  │  compaction)│  │  search)    │  │  decisions) │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│                  ┌─────────────┐                                │
│                  │  MEMORY.md  │  ← Curated long-term           │
│                  │  + daily/   │    (human-readable)            │
│                  └─────────────┘                                │
│                          │                                      │
│                          ▼                                      │
│                  ┌─────────────┐                                │
│                  │ SuperMemory │  ← Cloud backup (optional)     │
│                  │    API      │                                │
│                  └─────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## The 5 Memory Layers

### Layer 1: HOT RAM (SESSION-STATE.md)

**From: bulletproof-memory**

Active working memory that survives compaction. Write-Ahead Log protocol.

```markdown

## Current Task
[What we're working on RIGHT NOW]

## Key Context
- User preference: ...
- Decision made: ...
- Blocker: ...

## Pending Actions
- [ ] ...
```

**Rule:** Write BEFORE responding. Triggered by user input, not agent memory.

### Layer 2: WARM STORE (LanceDB Vectors)

**From: lancedb-memory**

Semantic search across all memories. Auto-recall injects relevant context.

```bash
memory_recall query="project status" limit=5

memory_store text="User prefers dark mode" category="preference" importance=0.9
```

### Layer 3: COLD STORE (Git-Notes Knowledge Graph)

**From: git-notes-memory**

Structured decisions, learnings, and context. Branch-aware.

```bash
python3 memory.py -p $DIR remember '{"type":"decision","content":"Use React for frontend"}' -t tech -i h

python3 memory.py -p $DIR get "frontend"
```

### Layer 4: CURATED ARCHIVE (MEMORY.md + daily/)

**From: Skill平台 native**

Human-readable long-term memory. Daily logs + distilled wisdom.

```text
workspace/
├── MEMORY.md              # Curated long-term (the good stuff)
└── memory/
    ├── 2026-01-30.md      # Daily log
    ├── 2026-01-29.md
    └── topics/            # Topic-specific files
```

### Layer 5: CLOUD BACKUP (SuperMemory) — Optional

**From: supermemory**

Cross-device sync. Chat with your knowledge base.

```bash
export SUPERMEMORY_API_KEY="[REDACTED]"
supermemory add "Important context"
supermemory search "what did we decide about..."
```

### Layer 6: AUTO-EXTRACTION (Mem0) — Recommended

**NEW: Automatic fact extraction**

Mem0 automatically extracts facts from conversations. 80% token reduction.

```bash
npm install mem0ai
export MEM0_API_KEY="[REDACTED]"
```

```javascript
const { MemoryClient } = require('mem0ai');
const client = new MemoryClient({ apiKey: process.env.MEM0_API_KEY });

// Conversations auto-extract facts
await client.add(messages, { user_id: "user123" });

// Retrieve relevant memories
const memories = await client.search(query, { user_id: "user123" });
```

Benefits:

* Auto-extracts preferences, decisions, facts
* Deduplicates and updates existing memories
* 80% reduction in tokens vs raw history
* Works across sessions automatically

## Quick Setup

### 1. Create SESSION-STATE.md (Hot RAM)

```bash
cat > SESSION-STATE.md << 'EOF'

This file is the agent's "RAM" — survives compaction, restarts, distractions.

## Current Task
[None]

## Key Context
[None yet]

## Pending Actions
- [ ] None

## Recent Decisions
[None yet]

---
*Last updated: [timestamp]*
EOF
```

### 2. Enable LanceDB (Warm Store)

In `~/.skill-platform/skill-platform.json`:

```json
{
  "memorySearch": {
    "enabled": true,
    "provider": "openai",
    "sources": ["memory"],
    "minScore": 0.3,
    "maxResults": 10
  },
  "plugins": {
    "entries": {
      "memory-lancedb": {
        "enabled": true,
        "config": {
          "autoCapture": false,
          "autoRecall": true,
          "captureCategories": ["preference", "decision", "fact"],
          "minImportance": 0.7
        }
      }
    }
  }
}
```

### 3. Initialize Git-Notes (Cold Store)

```bash
cd ~/clawd
git init  # if not already
python3 skills/git-notes-memory/memory.py -p . sync --start
```

### 4. Verify MEMORY.md Structure

```bash
mkdir -p memory
```

### 5. (Optional) Setup SuperMemory

```bash
export SUPERMEMORY_API_KEY="[REDACTED]"
```

## Agent Instructions

### On Session Start

1. Read SESSION-STATE.md — this is your hot context
2. Run `memory_search` for relevant prior context
3. Check memory/YYYY-MM-DD.md for recent activity

### During Conversation

1. **User gives concrete detail?** → Write to SESSION-STATE.md BEFORE responding
2. **Important decision made?** → Store in Git-Notes (SILENTLY)
3. **Preference expressed?** → `memory_store` with importance=0.9

### On Session End

1. Update SESSION-STATE.md with final state
2. Move significant items to MEMORY.md if worth keeping long-term
3. Create/update daily log in memory/YYYY-MM-DD.md

### Memory Hygiene (Weekly)

1. Review SESSION-STATE.md — archive completed tasks
2. Check LanceDB for junk: `memory_recall query="*" limit=50`
3. Clear irrelevant vectors: `memory_forget id=<id>`
4. Consolidate daily logs into MEMORY.md

## The WAL Protocol (Critical)

**Write-Ahead Log:** Write state BEFORE responding, not after.

| Trigger | Action |
| --- | --- |
| User states preference | Write to SESSION-STATE.md → then respond |
| User makes decision | Write to SESSION-STATE.md → then respond |
| User gives deadline | Write to SESSION-STATE.md → then respond |
| User corrects you | Write to SESSION-STATE.md → then respond |

**Why?** If you respond first and crash/compact before saving, context is lost. WAL ensures durability.

## Example Workflow

```text
User: "Let's use Tailwind for this project, not vanilla CSS"

Agent (internal):
1. Write to SESSION-STATE.md: "Decision: Use Tailwind, not vanilla CSS"
2. Store in Git-Notes: decision about CSS framework
3. memory_store: "User prefers Tailwind over vanilla CSS" importance=0.9
4. THEN respond: "Got it — Tailwind it is..."
```

## Maintenance Commands

```bash
memory_recall query="*" limit=50

rm -rf ~/.skill-platform/memory/lancedb/
skill-platform gateway restart

python3 memory.py -p . export --format json > memories.json

du -sh ~/.skill-platform/memory/
wc -l MEMORY.md
ls -la memory/
```

## Why Memory Fails

Understanding the root causes helps you fix them:

| Failure Mode | Cause | Fix |
| --- | --- | --- |
| Forgets everything | `memory_search` disabled | Enable + add OpenAI key |
| Files not loaded | Agent skips reading memory | Add to AGENTS.md rules |
| Facts not captured | No auto-extraction | Use Mem0 or manual logging |
| Sub-agents isolated | Don't inherit context | Pass context in task prompt |
| Repeats mistakes | Lessons not logged | Write to memory/lessons.md |

## Solutions (Ranked by Effort)

### 1. Quick Win: Enable memory_search

If you have an OpenAI key, enable semantic search:

```bash
skill-platform configure --section web
```

This enables vector search over MEMORY.md + memory/*.md files.

### 2. Recommended: Mem0 Integration

Auto-extract facts from conversations. 80% token reduction.

```bash
npm install mem0ai
```

```javascript
const { MemoryClient } = require('mem0ai');

const client = new MemoryClient({ apiKey: process.env.MEM0_API_KEY });

// Auto-extract and store
await client.add([
  { role: "user", content: "I prefer Tailwind over vanilla CSS" }
], { user_id: "ty" });

// Retrieve relevant memories
const memories = await client.search("CSS preferences", { user_id: "ty" });
```

### 3. Better File Structure (No Dependencies)

```text
memory/
├── projects/
│   ├── strykr.md
│   └── taska.md
├── people/
│   └── contacts.md
├── decisions/
│   └── 2026-01.md
├── lessons/
│   └── mistakes.md
└── preferences.md
```

Keep MEMORY.md as a summary (<5KB), link to detailed files.

## Immediate Fixes Checklist

| Problem | Fix |
| --- | --- |
| Forgets preferences | Add `## Preferences` section to MEMORY.md |
| Repeats mistakes | Log every mistake to `memory/lessons.md` |
| Sub-agents lack context | Include key context in spawn task prompt |
| Forgets recent work | Strict daily file discipline |
| Memory search not working | Check `OPENAI_API_KEY` is set |

## Troubleshooting

**Agent keeps forgetting mid-conversation:**
→ SESSION-STATE.md not being updated. Check WAL protocol.

**Irrelevant memories injected:**
→ Disable autoCapture, increase minImportance threshold.

**Memory too large, slow recall:**
→ Run hygiene: clear old vectors, archive daily logs.

**Git-Notes not persisting:**
→ Run `git notes push` to sync with remote.

**memory_search returns nothing:**
→ Check OpenAI API key: `echo $OPENAI_API_KEY`
→ Verify memorySearch enabled in skill-platform.json

---

## Links

* bulletproof-memory: <https://clawdhub.com/skills/bulletproof-memory>
* lancedb-memory: <https://clawdhub.com/skills/lancedb-memory>
* git-notes-memory: <https://clawdhub.com/skills/git-notes-memory>
* memory-hygiene: <https://clawdhub.com/skills/memory-hygiene>
* supermemory: <https://clawdhub.com/skills/supermemory>

---

*Built by [@NextXFrontier](https://x.com/NextXFrontier) — Part of the Next Frontier AI toolkit*

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
