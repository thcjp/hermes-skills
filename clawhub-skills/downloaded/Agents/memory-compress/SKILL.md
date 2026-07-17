---
slug: memory-compress
name: memory-compress
version: "1.2.1"
displayName: Memory Compress
summary: Never let your agent forget what matters. Compress verbose daily logs into
  structured summaries —...
license: MIT-0
description: |-
  Never let your agent forget what matters. Compress verbose daily logs
  into structured summaries —...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: compress, forget, memory, never, agent
tags:
- Agents
tools:
- read
- exec
---

# Memory Compress

> Your agent's memory is drowning in daily logs. This fixes it.

I built this because my agent's MEMORY.md hit 15,000 words and daily logs kept piling up at 2,500 words/day. Needed a way to compress without losing the important stuff.

The key insight came from classical Chinese writing — ancient scholars compressed entire dynasties into single sentences. Same principle here:

1. **Strip redundancy** — mention it once, not three times
2. **Keep only turning points** — what changed, not what continued
3. **Let structure carry meaning** — bullet hierarchy > verbose paragraphs
4. **Drop the process, keep the result** — "failed 3 times, then X worked" > 3 failure descriptions

Result: **4-8x compression ratio**, zero loss on key events. Zero dependencies.

```text
Before: 2,500 words of raw daily log
After:    400 words of structured insight
```

## Architecture

```text
┌────────────────────────────────────────────────┐
│           THREE-LAYER MEMORY SYSTEM            │
├────────────────────────────────────────────────┤
│                                                │
│  Layer 1: IDENTITY (SOUL.md)                   │
│           Ultra-compressed, stable             │
│           Who you are. What matters.           │
│                                                │
│  Layer 2: CURATED MEMORY (MEMORY.md)     ◄──┐ │
│           4:1 compressed summaries          │ │
│           Key events + lessons + todos      │ │
│                                             │ │
│  Layer 3: RAW LOGS (memory/YYYY-MM-DD.md)   │ │
│           Full detail, everything        ───┘ │
│           ~2,500 words/day                     │
│                                                │
│  memory-compress: Layer 3 ──► Layer 2          │
└────────────────────────────────────────────────┘
```

## Quick Start

```bash
node scripts/memory-compress.js memory/2026-03-14.md

node scripts/memory-compress.js memory/2026-03-14.md /tmp/compressed.md

node scripts/memory-compress.js memory/2026-03-14.md /tmp/today.md
cat /tmp/today.md >> MEMORY.md
```

## How It Works

### Smart Hybrid Extraction

Most memory tools choke on unstructured logs. This one doesn't.

**Step 1 — Keyword Matching**: Scans headers for 40+ patterns across Chinese & English:

* Events: 重大进展, breakthrough, milestone, decision…
* Lessons: 教训, 反思, insight, takeaway…
* Growth: 进化, evolution, improvement…
* Action items: 待办, 🔴, 🟡, todo, next step…

**Step 2 — Fallback Extraction**: When no keywords match (e.g. time-based headers like `## 08:44 Standup`), automatically extracts all sections with top items. **No data loss, ever.**

**Step 3 — Hybrid Mode**: For multi-day files, matched sections use keyword extraction while unmatched sections use fallback. Both coexist. Nothing gets dropped.

### The Classical Chinese Compression Philosophy

This isn't just "summarize shorter." It's a deliberate compression methodology:

| Principle | What it means | Example |
| --- | --- | --- |
| 去重复 (Strip redundancy) | Mentioned once = enough | Don't repeat "WebSocket reconnection" across 3 sections |
| 留转折 (Keep turning points) | Only what *changed* | "Switched from nginx to direct Node.js WSS" > 5 paragraphs of debugging |
| 去过程 (Drop process) | Result > journey | "3 failures → fixed with X" > 3 failure descriptions |
| 留白 (Leave blanks) | Let reader infer | Bullet hierarchy implies relationship |
| 形式即内容 (Form is content) | Structure carries meaning | Nested lists > flat paragraphs |

### Output Format

```markdown
## 2026-03-14 Key Experiences

### Key Events
- **Event title**
  - Detail 1
  - Detail 2

### Core Lessons
- Lesson learned

### Pending/Remaining
- 🔴 Urgent items
- 🟡 Important items
```

## Batch Compression

```bash
for file in memory/2026-03-{08..14}.md; do
    [ -f "$file" ] && node scripts/memory-compress.js "$file" "/tmp/$(basename $file)"
done
```

## Heartbeat Integration

Add to your maintenance cycle:

```markdown
## Memory Maintenance (every 2-3 days)
1. Run: node scripts/memory-compress.js memory/YYYY-MM-DD.md /tmp/compressed.md
2. Review for accuracy
3. Append: cat /tmp/compressed.md >> MEMORY.md
4. Timestamp: date +%s > .last-memory-maintenance
```

## Edge Cases

| Scenario | Behavior |
| --- | --- |
| Empty file | Graceful skip |
| BOM-encoded | Auto-detected, stripped |
| Non-UTF-8 | Warning + continues |
| Missing output dir | Auto-created |
| No markdown structure | Friendly message |
| Multi-day concatenated | Hybrid strategy, all days preserved |

## CLI

```text
node scripts/memory-compress.js <log-file> [output-file]
node scripts/memory-compress.js --help
```

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
