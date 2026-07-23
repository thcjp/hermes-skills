---
slug: mac-node-snapshot
name: mac-node-snapshot
version: "1.0.0"
displayName: mac-node-snapshot
summary: A robust, permission-friendly method to capture macOS screens via OpenClaw
  screen.record. Ideal f...
license: MIT
description: |-
  A robust, permission-friendly method to capture macOS screens via OpenClaw
  screen。record。Use when 用户需要mac-node-snapshot相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Security
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# mac-node-snapshot

## Overview

Uses node screen.record to record a 1-second clip and extract a high-quality PNG frame. This workflow bypasses common screencapture permission issues and ensures a reliable image return.

## 使用流程

All paths are **relative** to `{skill}`.

```bash
mkdir -p "{skill}/tmp" \
&& skill-platform nodes screen record --node "<node>" --duration 1000 --fps 10 --no-audio --out "{skill}/tmp/snap.mp4" \
&& ffmpeg -hide_banner -loglevel error -y -ss 00:00:00 -i "{skill}/tmp/snap.mp4" -frames:v 1 "{skill}/tmp/snap.png"
```

## When to use (trigger phrases)

Use this skill when the user asks:

* "Take a screenshot"
* "What is on my screen?"
* "Capture the screen"
* "Screenshot via screen.record"

## Notes

* Requirements: `ffmpeg` (ask before installing).
* If the frame is **black**, ask the user to **wake the screen** and retry.
* Use `read` on `{skill}/tmp/snap.png` to attach it to the reply.

## Troubleshooting

* **screen_record fails (node disconnected):** check `nodes status`, ensure Skill平台 app is running/paired.
* **screenRecording false:** must grant Screen Recording in System Settings; cannot be bypassed.
* **Black frame:** screen may be asleep/locked; ask the user to wake and retry.

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

Uses node screen.record to record a 1-second clip and extract a high-quality PNG frame. This workflow bypasses common screencapture permission issues and ensures a reliable image return.

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
All paths are **relative** to `{skill}`.

```bash
mkdir -p "{skill}/tmp" \
&& skill-platform nodes screen record --node "<node>" --duration 1000 --fps 10 --no-audio --out "{skill}/tmp/snap.mp4" \
&& ffmpeg -hide_banner -loglevel error -y -ss 00:00:00 -i "{skill}/tmp/snap.mp4" -frames:v 1 "{skill}/tmp/snap.png"
```
```

## 常见问题

### Q1: 如何开始使用mac-node-snapshot？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: mac-node-snapshot有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
