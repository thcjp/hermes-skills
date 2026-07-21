---
slug: vector-control
name: vector-control
version: "1.0.1"
displayName: Vector Control
summary: Control a Vector robot via Wirepod’s local HTTP API on the same network.
  Use when you need to mov...
license: MIT
description: |-
  Control a Vector robot via Wirepod’s local HTTP API on the same network。Use when you need to mov。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
tools:
  - - read
- exec
---

# Vector Control

## Overview

Control Vector through Wirepod’s `/api-sdk/*` endpoints and the camera stream at `/cam-stream`. Use this skill for movement, speech, camera snapshots, patrols, and exploration from the Pi.

## 使用流程

Use the bundled script:

```bash
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> assume
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> say --text "Hello Dom"
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> move --lw 160 --rw 160 --time 1.5
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> snapshot --out /tmp/vector.mjpg
```

### Find ESN/serial

If you don’t have it, read:

* `/etc/wire-pod/wire-pod/jdocs/botSdkInfo.json`

## Tasks

### 1) Assume / Release control

Always assume before movement, and release if the bot tips or a human needs manual control.

```bash
python3 .../vector_control.py --serial <ESN> assume
python3 .../vector_control.py --serial <ESN> release
```

### 2) Movement

* `move` sends wheel speeds (0–200 typical). Use short timed moves.

```bash
python3 .../vector_control.py --serial <ESN> move --lw 120 --rw 120 --time 1.0
```

### 3) Head / Lift

```bash
python3 .../vector_control.py --serial <ESN> head --speed -2 --time 1.0
python3 .../vector_control.py --serial <ESN> lift --speed 2 --time 1.0
```

### 4) Speech

Speech can be interrupted by motion/camera. If it fails, pause after speaking before moving.

```bash
python3 .../vector_control.py --serial <ESN> say --text "Sneaking forward"
```

### 5) Camera snapshot

`/cam-stream` returns MJPG. Save it and convert to JPEG if needed (ffmpeg).

```bash
python3 .../vector_control.py --serial <ESN> snapshot --out /tmp/vector.mjpg
ffmpeg -y -loglevel error -i /tmp/vector.mjpg -frames:v 1 /tmp/vector.jpg
```

### 6) Play Audio (MP3/WAV)

Streams an audio file through Vector's speaker. Automatically converts to the required format (8kHz mono WAV).

```bash
python3 .../vector_control.py --serial <ESN> play --file /path/to/music.mp3
```

### 7) Patrol (deterministic sweep)

```bash
python3 .../vector_control.py --serial <ESN> patrol --steps 6 --speed 140 --step-time 1.2 --turn-time 0.8 --speak --phrase "Patrolling"
```

### 8) Explore (randomized wander)

```bash
python3 .../vector_control.py --serial <ESN> explore --steps 8 --speak --phrase "Exploring"
```

## References

* `references/wirepod-api.md` — endpoint list and notes.

## Resources

### scripts/

* `vector_control.py` — CLI for basic control + patrol/explore routines.

### references/

* `wirepod-api.md` — HTTP API endpoints and usage notes.

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

Control Vector through Wirepod’s `/api-sdk/*` endpoints and the camera stream at `/cam-stream`. Use this skill for movement, speech, camera snapshots, patrols, and exploration from the Pi.

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
Use the bundled script:

```bash
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> assume
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> say --text "Hello Dom"
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> move --lw 160 --rw 160 --time 1.5
python3 skills/vector-control/scripts/vector_control.py --serial <ESN> snapshot --out /tmp/vector.mjpg
```

### Find ESN/serial

If you don’t have it, read:

* `/etc/wire-pod/wire-pod/jdocs/
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Vector Control？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Vector Control有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
