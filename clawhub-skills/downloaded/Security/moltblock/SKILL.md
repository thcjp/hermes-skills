---
slug: moltblock
name: moltblock
version: "0.11.9"
displayName: Skill
summary: Verification gating for AI-generated artifacts. Policy checks to catch dangerous
  patterns before ...
license: MIT-0
description: |-
  Verification gating for AI-generated artifacts. Policy checks to catch
  dangerous patterns before ...

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: verification, policy, artifacts, gating, moltblock, generated
tags:
- Security
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
