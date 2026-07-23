---
slug: sequential-read
name: sequential-read
version: "1.0.0"
displayName: Sequential Read
summary: Read prose sequentially with structured reflections to simulate the reading
  experience
license: MIT
description: |-
  Read prose sequentially with structured reflections to simulate the
  reading experience

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词...
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Sequential Read

Read prose (novels, non-fiction, articles) by ingesting content in semantic chunks and building structured reflections iteratively. The output captures how your perspective developed over the course of reading — predictions that were wrong, questions that got answered, opinions that shifted — not just a retroactive summary.

## Invocation

| Command | Description |
| --- | --- |
| `/sequential-read <path-to-file>` | Run a full reading session |
| `/sequential-read <path-to-file> --lens <persona>` | Read with a perspective (e.g., "skeptic", "literary critic", "student") |
| `/sequential-read list` | List all sessions |
| `/sequential-read show <session-id>` | Show the synthesis for a completed session |

## Execution Model

**The pipeline runs in spawned sub-agents.** Novel-length reads are a two-phase process: a main reader that handles the bulk of chunks, then a finisher that completes the remaining chunks and writes synthesis. This is the normal flow, not an error.

When the user invokes `/sequential-read`:

1. Parse the command to extract the file path and optional lens
2. Pre-create the session:

   bash

   ```
   python3 {baseDir}/scripts/session_manager.py create <source-file>
   ```
3. Spawn the **main reader** sub-agent:

   text

   ```
   sessions_spawn with label: reader-{session-id}
   Tell the agent: "Session already exists at {session-id}. Do NOT create it again."
   ```
4. Tell the user the session has started and they'll be notified when it's done
5. **When the main reader returns** (whether it completed or died mid-read):
   * Check session status: `python3 {baseDir}/scripts/session_manager.py get <session-id>`
   * Check how many reflections exist vs total chunks
   * **If synthesis exists:** Done. Present results.
   * **If chunks remain or synthesis is missing:** Spawn a **finisher** sub-agent (see below). This is the expected path for novels.
6. When the finisher returns, present the synthesis and session path.

### The Two-Phase Pattern

For novels (~20+ chunks), the main reader typically handles ~17-20 chunks before its context fills and the session ends. This is **expected behavior**, not failure. The finisher picks up the remaining 2-5 chunks and writes the synthesis with full context of all prior reflections.

**Spawning the finisher:**

```text
sessions_spawn with label: finisher-{session-id}, model: "opus"
Task: "Resume reading session {session-id} at {baseDir path}.
  Read reflections written so far to understand context.
  Continue from chunk N (the next unwritten chunk).
  Write remaining reflections, then run synthesis.
  Session path: {session-path}"
```

**Do not wait or ask the user** between the main reader and finisher. When the main reader returns without a synthesis, immediately spawn the finisher. The whole pipeline should be hands-off.

## Script Paths

All Python scripts are in `{baseDir}/scripts/`:

* `{baseDir}/scripts/session_manager.py`
* `{baseDir}/scripts/chunk_manager.py`
* `{baseDir}/scripts/state_manager.py`

Templates are in `{baseDir}/templates/`:

* `{baseDir}/templates/reflection_prompt.md`
* `{baseDir}/templates/synthesis_prompt.md`

## Commands

### `/sequential-read <path-to-file> [--lens <persona>]`

#### 1. Create or Resume Session

```bash
python3 {baseDir}/scripts/session_manager.py create <source-file> [--lens <persona>]
```

This command handles resume detection automatically:

* If an in-progress session exists for the same source filename, it prints the existing session-id and path
* Otherwise it creates a new session

Capture the session-id from the first line of output.

#### 2. Check Session Status (for resumed sessions)

```bash
python3 {baseDir}/scripts/session_manager.py get <session-id>
```

Check the `status` field to determine where to resume:

| Status | Action |
| --- | --- |
| `preread` | Run preread phase from the start |
| `chunked` | Run reading phase (resumes from current_chunk) |
| `read` | Run synthesis phase |
| `complete` | Display the existing synthesis |

#### 3. Run the Pipeline

**For a new session or `preread` status:**

Run the preread sub-skill (`{baseDir}/preread/SKILL.md`) with:

* `SESSION_ID` = the session-id
* `SOURCE_FILE` = path to the source text
* `BASE_DIR` = `{baseDir}`

**For `chunked` status (or after preread completes):**

Run the reading sub-skill (`{baseDir}/reading/SKILL.md`) with:

* `SESSION_ID` = the session-id
* `BASE_DIR` = `{baseDir}`
* `LENS` = the lens value (or null)

**For `read` status (or after reading completes):**

Run the synthesis sub-skill (`{baseDir}/synthesis/SKILL.md`) with:

* `SESSION_ID` = the session-id
* `BASE_DIR` = `{baseDir}`

#### 4. Present Results

After synthesis completes, send the user:

* The full synthesis text
* The session path: `memory/sequential_read/<session-id>/`
* A brief note: how many chunks, whether a lens was used

### `/sequential-read list`

```bash
python3 {baseDir}/scripts/session_manager.py list
```

Print the output to the user.

### `/sequential-read show <session-id>`

```bash
python3 {baseDir}/scripts/session_manager.py get <session-id>
```

If status is `complete`, read and display:

```text
memory/sequential_read/<session-id>/output/synthesis.md
```

If not complete, show the session status and progress.

## Model Guidance

The reading phase is the most demanding — it runs for many iterations and must sustain quality throughout. Choose the model based on source length:

| Source Length | Recommended Model | Rationale |
| --- | --- | --- |
| Novel (10k+ lines, 20+ chunks) | **Opus** | Sustained quality over many iterations; large context window handles accumulated state |
| Novella / long essay (3k-10k lines) | Opus or Sonnet | Either works; Sonnet is fine if chunks stay under 15 |
| Article / short work (<3k lines) | Sonnet | Few chunks, context stays manageable |

When spawning the sub-agent, set the model explicitly: `model: "opus"` for novels.

**Why this matters:** Lighter models degrade over long reading sessions — reflections become stubs as context accumulates. The first test run of this skill on Sonnet with a 35-chunk novel produced 4 genuine reflections and 31 placeholders. Opus is required for novel-length works.

**Chunk sizing:** The structural chunker targets ~550 lines per chunk (range 200-700). For a typical novel (~10-12k lines), this produces ~20 chunks. Longer texts (15k+ lines) may produce 35+ chunks and will need a finisher session (see below).

**The two-phase pattern is standard.** For novel-length works (20+ chunks), always expect to spawn a finisher after the main reader. The main reader handles ~80-90% of chunks; the finisher handles the rest plus synthesis. For very long texts (35+ chunks), the main reader may only get ~25 chunks. Plan accordingly -- this is the normal pipeline, not error recovery.

**Pre-create sessions:** Always create the session with `session_manager.py create` BEFORE spawning the sub-agent. Tell the agent the session already exists and not to create it again. This avoids failures from duplicate creation attempts.

## Reader Context (Optional)

If you maintain **reader-mind files** (accumulated reading context — character knowledge, thematic threads, critical framework), load them into the sub-agent's task prompt as preamble. This gives the reader continuity across books in a series.

Include context in the spawn task:

```text
"Before you begin reading, here is your accumulated reader context:

=== READING CONTEXT ===
[contents of reader-mind file]

Now read [book title]..."
```

**After synthesis, update reader-mind files** with new character knowledge, thematic thread updates, and cross-reference observations. Revise rather than append. Keep under ~4000 words per file.

## Important Guidelines for the Reading Agent

* **No peeking.** Each reflection must be written from the perspective of not knowing what comes next. Do not reference content from later chunks.
* **Be honest.** Confusion, boredom, excitement, disagreement are all valid reactions. Don't perform engagement.
* **Be specific in revisions.** "I was wrong about X because Y" beats "my view has evolved."
* **The lens is a suggestion.** If the lens feels forced for a particular chunk, note that in the reaction rather than straining to apply it.
* **Run autonomously.** Do not stop to ask the user questions between chunks. The entire pipeline is set-and-forget.
* **Persist everything.** Every reflection and state update is saved to disk before moving to the next chunk, enabling resume on interruption.

## Post-Synthesis

After synthesis is complete, you can integrate the output into whatever workflow you prefer — blog posts, reading logs, knowledge graphs, series trackers, etc. The synthesis file at `output/synthesis.md` is self-contained and portable.

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

- 触发关键词: read, prose, sequentially, structured, sequential

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

### Q1: 如何开始使用Sequential Read？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Sequential Read有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
