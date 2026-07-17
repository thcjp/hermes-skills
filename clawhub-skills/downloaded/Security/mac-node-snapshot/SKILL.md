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
  screen.record. Ideal f...

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: node, mac-node-snapshot, method, capture, mac, robust, permission, friendly
tags:
- Security
tools:
- read
- exec
---

# mac-node-snapshot

## Overview

Uses node screen.record to record a 1-second clip and extract a high-quality PNG frame. This workflow bypasses common screencapture permission issues and ensures a reliable image return.

## Quick start (single command, no scripts)

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
