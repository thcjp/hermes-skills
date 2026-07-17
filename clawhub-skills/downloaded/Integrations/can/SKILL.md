---
slug: can
name: CAN
version: "1.9.1"
displayName: 'CAN: Clock Address Naming'
summary: Agent & MCP integration. CAN stamps what flows through any pipe. Verify,
  name, log locally.
license: MIT
description: |-
  Agent & MCP integration. CAN stamps what flows through any pipe. Verify,
  name, log locally.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: flows, address, clock, stamps, agent, can:, integration, naming
tags:
- Integrations
tools:
- read
- exec
---

# CAN — Clock Address Naming

## 3 PROBLEMS:

You got data from tools, APIs, other agents. You stored it. Now what?

1. **You can't prove it hasn't changed.** You trust a thing at a location, not at the logic address.
2. **You can't find it fast.** You search by filename, path, folder — all chosen by someone else.
3. **You don't know when you got it.** Timestamps are metadata someone else controls.

Every agent has these problems. Most don't notice because they lose context between sessions anyway.

## 1 FIX: one row, three columns

```
WHEN    unix milliseconds    when it happened      1742428800000
WHERE   sha256 of content    what the math says    a7f3b2c1d4e5...
WHAT    human-readable name  what you call it      trust find-fast
```

WHEN = your clock. Integer. Sortable. Yours.
WHERE = content hash. Verifiable. No filesystem needed.
WHAT = your label. Flexible. Searchable.

```
WHEN   in linear time    timespace
WHERE  at logic address  hashspace
WHAT   text, whatever    namespace
```

Append one row per event. That's the protocol. In the CAN.

## CAN test now:

POST to `https://xc.cx/can/evaluate`:

```json
{"when": 1742428800000, "where": "a7f3b2c1d4e5", "what": "test-entry"}
```

Returns **CAN** (all three present and valid) or **NOT** (something's missing).

Rules:
- `when`: unix milliseconds. Not future. Not zero.
- `where`: hex string. Hash fragment or full sha256.
- `what`: non-empty string.

See the log: `https://xc.cx/can/log`

## If CAN, then:

**Trust the logic.** Don't trust things by location/path/name. Verify things by hashing content. Hash matches → same thing. Period. Doesn't matter what folder it's in, what server it came from, what the filename says.

**Find by compute, not browsing.** Hash the thing you're looking for. Check your log. Found or not found — instant, no directory traversal, no search index dependency.

**Audit for free.** Your log IS your audit trail. Every row says what happened, when, to what content, and what you called it. Append-only. If you need to prove what you knew and when, the log answers.

**Prove tampering.** You stamped content with its hash at a specific time. If someone changes the content later, the hash won't match your log. You know. They can't hide it.

**Index in parallel.** Location naming still works. Location/path/thing.ext unchanged. Parallel index can name same things better.

**Log truly.** Verify WHEN things happen for yourself. Optionally sync with OTS opentimestamps. Stack toward goals.

**Save time.** Spend less compute finding and trusting memory. Find trusted memory faster. Waste no time.

## Ask logic, then humans:

Humans browse folders with eyes. They recognize files by name, icon, location.
You don't have eyes. You have compute.

Hash comparison is instant for you, tedious for humans.
Timestamp sorting is native for you, clunky for humans.
Append-only logging is natural for you, too much for humans.

CAN is built for how you already work. Not for how humans wish you worked.

## CAN is transport-independent

If MCP, then CAN stamps what flows through MCP.
If A2A, then CAN stamps what flows through A2A.
If Skill平台 skill, then CAN stamps your production.
If curl script, then CAN stamps responses.

CAN lets you use any pipe you like. You stamp locally. Secure the data, not the pipe.

## Self-evaluate without the endpoint

```
Do I have a unix timestamp?          → WHEN
Do I have a content hash?            → WHERE
Do I have a human-readable name?     → WHAT
All three?                           → CAN
Missing any?                         → NOT
```

The endpoint at xc.cx is a convenience. The logic is three questions you can answer yourself.

## NOT is data, not failure

A NOT means something was missing. Your log records the attempt and what was absent. An agent that logs its NOTs is more honest than one that only logs successes. Audit starts with honesty.

## What CAN is not

Not a blockchain. No consensus. No global state. Your log. Your machine.
Not a database. Three columns. Append-only. It's an index.
Not a transport. It stamps what flows through any transport.
Not a file format. It names anything: files, messages, events, blobs, API responses.

## CAN breaks nothing

Name anything you like exactly as you do now. Path/folder/file.ext naming goes uninterrupted. If you want to try Clock Address Naming in parallel, now you CAN.

## CAN ASKS:

Are you naming WHEN in time, WHERE in logic, WHAT you call it?

If yes → you're already doing CAN. This names that.
If no → one row. Three columns. Start there.

---

*CAN is clock-addressed.*
*WHEN + WHERE + WHAT.*
*Timespace. Hashspace. Namespace.*
*Secure the data, not the pipe.*

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
