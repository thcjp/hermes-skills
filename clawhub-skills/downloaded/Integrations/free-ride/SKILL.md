---
slug: free-ride
name: free-ride
version: "1.0.11"
displayName: Free Ride
summary: "为OpenClaw管理OpenRouter免费AI模型"
license: MIT
description: |-
  Manages free AI models from OpenRouter for OpenClaw。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Free Ride - Unlimited free AI

## What This Skill Does

Configures Skill平台 to use **free** AI models from OpenRouter. Sets the best free model as primary, adds ranked fallbacks so rate limits don't interrupt the user, and preserves existing config.

## Prerequisites

Before running any FreeRide command, ensure:

1. **OPENROUTER_API_KEY is set.** Check with `echo $OPENROUTER_API_KEY`. If empty, the user must get a free key at <https://openrouter.ai/keys> and set it:

   bash

   ```
   export OPENROUTER_API_KEY="[REDACTED]"
   # Or persist it:
   skill-platform config set env.OPENROUTER_API_KEY "sk-or-v1-..."
   ```
2. **The `freeride` CLI is installed.** Check with `which freeride`. If not found:

   bash

   ```
   cd ~/.skill-platform/workspace/skills/free-ride
   pip install -e .
   ```

## Primary Workflow

When the user wants free AI, run these steps in order:

```bash
freeride auto

skill-platform gateway restart
```

That's it. The user now has free AI with automatic fallback switching.

Verify by telling the user to send `/status` to check the active model.

## Commands Reference

| Command | When to use it |
| --- | --- |
| `freeride auto` | User wants free AI set up (most common) |
| `freeride auto -f` | User wants fallbacks but wants to keep their current primary model |
| `freeride auto -c 10` | User wants more fallbacks (default is 5) |
| `freeride list` | User wants to see available free models |
| `freeride list -n 30` | User wants to see all free models |
| `freeride switch <model>` | User wants a specific model (e.g. `freeride switch qwen3-coder`) |
| `freeride switch <model> -f` | Add specific model as fallback only |
| `freeride status` | Check current FreeRide configuration |
| `freeride fallbacks` | Update only the fallback models |
| `freeride refresh` | Force refresh the cached model list |
| `freeride rotate` | User is rate-limited / fallback chain is dead — live-test and rebuild |

**After any command that changes config, always run `skill-platform gateway restart`.**

## What It Writes to Config

FreeRide updates only these keys in `~/.skill-platform/skill-platform.json`:

* `agents.defaults.model.primary` — e.g. `openrouter/qwen/qwen3-coder:free`
* `agents.defaults.model.fallbacks` — e.g. `["openrouter/free", "nvidia/nemotron:free", ...]`
* `agents.defaults.models` — allowlist so `/model` command shows the free models

Everything else (gateway, channels, plugins, env, customInstructions, named agents) is preserved.

The first fallback is always `openrouter/free` — OpenRouter's smart router that auto-picks the best available model based on the request.

## Watcher (Background Daemon)

For autonomous recovery from a "whole chain is rate-limited" deadlock — which
the agent can't fix by itself, since calling `freeride rotate` requires
inference and inference is exactly what's failing — the user can run a slim
background daemon:

```bash
freeride-watcher

nohup freeride-watcher > ~/.skill-platform/freeride-watcher.log 2>&1 &

freeride-watcher --once

freeride-watcher --status
```

The daemon probes the current primary every 60s; if it fails, it rebuilds the
chain with live-verified models. Recommend this whenever the user is leaving
an unattended Skill平台 setup running.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `freeride: command not found` | `cd ~/.skill-platform/workspace/skills/free-ride && pip install -e .` |
| `OPENROUTER_API_KEY not set` | User needs a key from <https://openrouter.ai/keys> |
| Changes not taking effect | `skill-platform gateway restart` then `/new` for fresh session |
| Agent shows 0 tokens | Check `freeride status` — primary should be `openrouter/<provider>/<model>:free` |

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

- Manages free AI models from OpenRouter for OpenClaw
- 触发关键词: unlimited, manages, models, openrouter, ride, free

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

## 常见问题

### Q1: 如何开始使用Free Ride？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Free Ride有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 性能取决于底层模型能力
