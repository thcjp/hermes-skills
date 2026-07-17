---
slug: control-ikea-lightbulb
name: control-ikea-lightbulb
version: "1.0.1"
displayName: Control Ikea Lightbulb
summary: Control IKEA/TP-Link Kasa smart bulbs (set on/off, brightness, and color).
  Use when you want to p...
license: MIT
description: |-
  Control IKEA/TP-Link Kasa smart bulbs (set on/off, brightness, and color).
  Use when you want to p...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: kasa, ikea, lightbulb, control, smart, link
tags:
- Other
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
