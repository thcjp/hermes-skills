---
slug: control-ikea-lightbulb
name: control-ikea-lightbulb
version: "1.0.1"
displayName: Control Ikea Lightbu
summary: Control IKEA/TP-Link Kasa smart bulbs (set on/off, brightness, and color).
  Use when you want to p...
license: MIT
description: |-
  Control IKEA/TP-Link Kasa smart bulbs (set on/off, brightness, and color)。Use when you want to p。Use when 用户需要Control Ikea Lightbu相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
- Other
tools:
  - - read
- exec
---

# Control Ikea Lightbulb

This skill provides a lightweight Python script to control a local smart bulb (supports TP-Link Kasa-compatible bulbs via python-kasa). It is intended for local LAN devices that do not require cloud credentials; control is by IP address.

When to use this skill

* When you want to turn a bulb on or off
* When you want to set brightness (0-100)
* When you want to set color (HSV)
* When you have the bulb's local IP and it's accessible from this machine

Contents

* scripts/control_kasa_light.py — main runnable script (Python 3.9+)
* scripts/light_show.py — small light-show controller for sequences (uses python-kasa). Changes include:
  + Default white uses a high color temperature (9000K) to make white appear "whiter"; pass --white-temp to override.
  + Bug fixes: the off-flash between blue→red now ignores transitions to white (saturation==0) to avoid white<->blue ping-pong, and white-temp is only applied to white steps (fixes red being skipped during off-flash). White steps also set brightness even without --double-write.
* scripts/run_test_light_show.sh — helper to run light_show via uv

Notes

* This repo is set up for uv (no manual environment activation). Dependencies live in `pyproject.toml` and wrappers prefer `uv run`.
  Example:
  uv run --project ./skills/control-ikea-lightbulb python ./skills/control-ikea-lightbulb/scripts/control_kasa_light.py --ip 192.168.4.69 --on --hsv 0 100 80 --brightness 80
* Install uv:
  + `brew install uv` (macOS)
  + `pipx install uv` (cross-platform)
* The provided wrapper script requires uv:
  ./skills/control-ikea-lightbulb/scripts/run_control_kasa.sh --ip 192.168.4.69 --on --hsv 0 100 80 --brightness 80
* The test helper also prefers uv:
  ./skills/control-ikea-lightbulb/scripts/run_test_light_show.sh --ip 192.168.4.69 --duration 6 --transition 1 --off-flash --verbose
* If your device is actually an IKEA TRADFRI device (not Kasa), this script is a starting point; tell me and I will add TRADFRI support.
* No cloud credentials are required; control happens over LAN to the device's IP.

Quick start

1. Install uv (macOS):
   `brew install uv`
2. Turn the bulb on (replace the IP):
   `./skills/control-ikea-lightbulb/scripts/run_control_kasa.sh --ip 192.168.4.69 --on`
3. Set color and brightness:
   `./skills/control-ikea-lightbulb/scripts/run_control_kasa.sh --ip 192.168.4.69 --hsv 0 100 80 --brightness 80`

Git note

* No local environment artifacts are tracked; use uv.

Note about Python requirements and recent change

* The skill previously declared python-kasa>=0.13.0 which caused dependency resolution failures on this machine. To make the skill runnable locally the project's pyproject.toml was adjusted to:
  + requires-python = ">=3.11, <4.0"
  + python-kasa>=0.10.2
* This allows the resolver to pick a compatible python-kasa on machines with Python 3.11+. If you prefer a different constraint (or want me to revert this change), tell me and I will update the pyproject.toml and README accordingly.

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

- Control IKEA/TP-Link Kasa smart bulbs (set on/off, brightness, and color)
- Use when you want to p
- 触发关键词: kasa, ikea, lightbulb, control, smart, link

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

### Q1: 如何开始使用Control Ikea Lightbu？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Control Ikea Lightbu有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
