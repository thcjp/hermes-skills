---
slug: docker-ctl
name: docker-ctl
version: "1.0.0"
displayName: Docker Ctl
summary: Inspect containers, logs, and images via podman
license: MIT
description: |-
  Inspect containers, logs, and images via podman

  核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: podman, ctl, containers, docker, images, inspect, logs
tags:
- Operations
tools:
- read
- exec
---

# Docker Ctl

Inspect containers, logs, and images via podman. On Bazzite/Fedora, podman is the default container runtime and is always available.

## Commands

```bash
docker-ctl ps

docker-ctl logs <container>

docker-ctl images

docker-ctl inspect <container>
```

## Install

No installation needed. Bazzite uses `podman` as its container runtime and it is pre-installed.

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
