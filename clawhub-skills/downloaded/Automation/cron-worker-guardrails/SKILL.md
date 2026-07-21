---
slug: cron-worker-guardrails
name: cron-worker-guardrails
version: "1.0.5"
displayName: Cron Worker Guardrai
summary: "Use when: hardening OpenClaw cron/background workers (POSIX shells: bash/sh)
  against brittle quot"
license: MIT
description: |-
  Use when: hardening OpenClaw cron/background workers (POSIX shells:
  bash/sh) against brittle quot。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Automation
tools:
  - - read
- exec
---

# Cron Worker Guardrails

A reliability-first checklist for **Skill平台 cron workers** and any unattended automation.

## Scope (important)

* This skill is **POSIX-focused** (bash/sh examples).
* The *principles* are portable, but if you're on Windows/PowerShell you'll need equivalent patterns.

## The `NO_REPLY` convention

Many Skill平台 setups treat emitting exactly `NO_REPLY` as "silent success" (no human notification).

* If your runtime does not support `NO_REPLY`, interpret it as: **print nothing on success**.

## Quick Start

1. **Scripts-first:** move logic into a repo script (recommended: `tools/<job>.py` or `tools/<job>.sh`).
2. **One command in cron:** cron should run *one short command* (no multi-line `bash -lc '...'`).
3. **Deterministic cwd/env:** `cd` to the repo (or have the script do it), and document required env vars.
4. **Silent on success:** print nothing (or exactly `NO_REPLY`) when OK; only emit a short alert when broken.

Also see:

* `references/cron-agent-contract.md`
* `references/pitfalls.md`

## Why this skill exists

Cron failures are rarely "logic bugs". In practice they're often:

* brittle shell quoting (`bash -lc '...'` nested quotes)
* command substitution surprises (`$(...)`)
* one-liners that hide escaping bugs (`python -c "..."`)
* cwd/env drift ("works locally, fails in cron")
* pipelines that fail for the wrong reason (`pipefail` + `head` / SIGPIPE)

The fix is boring but effective: **scripts-first + deterministic execution + silent-on-success**.

## Portability rules (still apply)

Even on POSIX, do **not** hardcode deployment-specific absolute paths tied to one machine.

Prefer:

* repo-relative paths
* environment variables you document
* minimal wrappers that `cd` into the repo

## Common failure patterns -> fixes

### 1) `unexpected EOF while looking for matching ')'`

Likely causes:

* unclosed `$(...)` from command substitution
* broken nested quotes in `bash -lc ' ... '`

Fix pattern:

* Replace the whole multi-line shell block with a script.
* Cron calls exactly one short command, for example:
  + `python3 tools/<job>.py`

### 2) False failure from `pipefail` + `head` (SIGPIPE)

Symptom:

* command exits non-zero even though the output you wanted is fine

Fix pattern:

* avoid `pipefail` when piping into `head`
* or better: do the filtering in a script (read only what you need)

### 3) "Works locally, fails in cron"

Common causes:

* wrong working directory
* missing env vars
* different PATH

Fix pattern:

* `cd` into the repo (or have the script do it)
* keep dependencies explicit and documented

## Git footgun: `git push` rejected (non-fast-forward)

Symptom:

* `! [rejected] ... (non-fast-forward)` when automation pushes to a **long-lived PR/feature branch**.

Conservative fix (no force-push):

* On rejection, fetch the remote branch, transplant your new local commits onto it (cherry-pick), then retry push once.

## Copy/paste hardening header (portable)

Use this near the top of a cron prompt (2 lines, low-noise):

* **Hardening (MUST):** follow `references/cron-agent-contract.md` (scripts-first, deterministic cwd, silent-on-success).
* Also apply the `cron-worker-guardrails` skill. If parsing/multi-step logic is needed, write/run a small `tools/*.py` script.

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

- Use when: hardening OpenClaw cron/background workers (POSIX shells:
  bash/sh) against brittle quot
- 触发关键词: hardening, background, cron, guardrails, openclaw, worker

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
1. **Scripts-first:** move logic into a repo script (recommended: `tools/<job>.py` or `tools/<job>.sh`).
2. **One command in cron:** cron should run *one short command* (no multi-line `bash -lc '...'`).
3. **Deterministic cwd/env:** `cd` to the repo (or have the script do it), and document required env vars.
4. **Silent on success:** print nothing (or exactly `NO_REPLY`) when OK; only emit a short alert when broken.

Also see:

* `references/cron-agent-contract.md`
* `references/pitfalls.md`
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Cron Worker Guardrai？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Cron Worker Guardrai有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
