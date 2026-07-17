---
slug: sonoscli
name: sonoscli
version: "1.0.0"
displayName: Sonoscli
summary: Control Sonos speakers (discover/status/play/volume/group).
license: MIT
description: |-
  Control Sonos speakers (discover/status/play/volume/group).

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: sonoscli, speakers, status, sonos, discover, control
tags:
- Other
tools:
- read
- exec
---

# Sonoscli

Use `sonos` to control Sonos speakers on the local network.

Quick start

* `sonos discover`
* `sonos status --name "Kitchen"`
* `sonos play|pause|stop --name "Kitchen"`
* `sonos volume set 15 --name "Kitchen"`

Common tasks

* Grouping: `sonos group status|join|unjoin|party|solo`
* Favorites: `sonos favorites list|open`
* Queue: `sonos queue list|play|clear`
* Spotify search (via SMAPI): `sonos smapi search --service "Spotify" --category tracks "query"`

Notes

* If SSDP fails, specify `--ip <speaker-ip>`.
* Spotify Web API search is optional and requires `SPOTIFY_CLIENT_ID/SECRET`.

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
