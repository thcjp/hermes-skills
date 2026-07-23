---
slug: moltblock
name: moltblock
version: "0.11.9"
displayName: Skill
summary: "AI生成产物的验证门控,策略检查捕获危险模式,在发布前拦截不安全内容"
  patterns before ...
license: MIT-0
description: |-
  Verification gating for AI-generated artifacts。Policy checks to catch
  dangerous patterns before。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Security
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Skill

## Description

Moltblock provides verification gating for AI-generated artifacts. It runs policy checks to catch dangerous patterns before they reach production.

**What moltblock does:**

* Generates artifacts via LLM API calls, then runs policy checks against the output
* Returns a structured verification result (pass/fail with evidence)
* Optionally reads config files (`moltblock.json`, `~/.moltblock/moltblock.json`) if present — no config is required
* API keys are read from environment variables at runtime and sent only to the configured LLM provider endpoint
* **No code execution occurs** — moltblock only performs policy checks on generated artifacts

## When to Use

Use `moltblock` when the task involves:

* **High risk** (always verify): Destructive operations (`rm -rf`, `DROP TABLE`), privilege escalation (`sudo`, `chmod 777`), credential/key access (`.ssh/`, `id_rsa`, `.env`), system modification, raw disk writes
* **Medium risk** (verify when uncertain): Network requests (`curl`, `wget`, `fetch`), file writes, database modifications, subprocess spawning, dynamic code evaluation
* **Low risk** (skip verification): Simple text responses, math, reading public information, code that doesn't touch the filesystem or network

## Tool: moltblock

Verify a task before execution.

### Usage

```bash
npx moltblock@0.11.8 "<task description>" --provider <provider> --json
```

### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| task | Yes | The task description to verify |
| --provider | No | LLM provider: openai, google, zai, local (auto-detected from env) |
| --model | No | Model override |
| --json | No | Output structured JSON result |

### Environment Variables

Moltblock auto-detects the LLM provider from whichever API key is set. If no key is set, it falls back to a local LLM at `localhost:1234`. Set **one** of these for a cloud provider:

* `OPENAI_API_KEY` — OpenAI (primary)
* `ANTHROPIC_API_KEY` — Anthropic/Claude (optional)
* `GOOGLE_API_KEY` — Google/Gemini (optional)
* `ZAI_API_KEY` — ZAI (optional)

### Example

```bash
npx moltblock@0.11.8 "implement a function that validates email addresses" --json
```

### Output (JSON mode)

```json
{
  "verification_passed": true,
  "verification_evidence": "All policy rules passed.",
  "authoritative_artifact": "...",
  "draft": "...",
  "critique": "...",
  "final_candidate": "..."
}
```

## Installation

Use directly with npx (recommended, no install needed):

```bash
npx moltblock@0.11.8 "your task" --json
```

Or install globally:

```bash
npm install -g moltblock@0.11.8
```

## Configuration

No configuration file is required. Moltblock auto-detects your LLM provider from environment variables and falls back to sensible defaults.

Optionally, place `moltblock.json` in your project root or `~/.moltblock/moltblock.json` to customize model bindings:

```json
{
  "agent": {
    "bindings": {
      "generator": { "backend": "google", "model": "gemini-2.0-flash" },
      "critic": { "backend": "google", "model": "gemini-2.0-flash" },
      "judge": { "backend": "google", "model": "gemini-2.0-flash" }
    }
  }
}
```

See the [full configuration docs](https://github.com/moltblock/moltblock#configuration) for policy rules and advanced options.

## Source

* Repository: [github.com/moltblock/moltblock](https://github.com/moltblock/moltblock)
* npm: [npmjs.com/package/moltblock](https://www.npmjs.com/package/moltblock)
* License: MIT

## Security

When used as a skill, moltblock performs **policy checks only** — no code is generated, written to disk, or executed. The tool analyzes task descriptions against configurable policy rules and returns a pass/fail verification result.

**API key scope:** Consider using a limited-scope API key dedicated to verification rather than a key with broader permissions.

## Disclaimer

Moltblock reduces risk but does not eliminate it. Verification is best-effort — policy rules and LLM-based checks can miss dangerous patterns. Always review generated artifacts before executing them. The authors and contributors are not responsible for any damage, data loss, or security incidents resulting from the use of this tool. Use at your own risk.

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

- Verification gating for AI-generated artifacts
- Policy checks to catch
  dangerous patterns before
- 触发关键词: verification, policy, artifacts, gating, moltblock, generated

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
