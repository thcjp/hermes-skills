---
slug: docker
name: docker
version: "1.0.4"
displayName: Docker
summary: Docker containers, images, Compose stacks, networking, volumes, debugging,
  production hardening, ...
license: MIT-0
description: |-
  Docker containers, images, Compose stacks, networking, volumes, debugging,
  production hardening, 。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Operations
- Development
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Docker

## When to Use

Use when the task involves Docker, Dockerfiles, container builds, Compose, image publishing, networking, volumes, logs, debugging, or production container operations. This skill is stateless and should be applied directly whenever Docker work appears.

## Quick Reference

| Topic | File |
| --- | --- |
| Essential commands | `commands.md` |
| Dockerfile patterns | `images.md` |
| Compose orchestration | `compose.md` |
| Networking & volumes | `infrastructure.md` |
| Security hardening | `security.md` |

## Core Rules

### 1. Pin Image Versions

* `python:3.11.5-slim` not `python:latest`
* Today's latest differs from tomorrow's — breaks immutable builds

### 2. Combine RUN Commands

* `apt-get update && apt-get install -y pkg` in ONE layer
* Separate layers = stale package cache weeks later

### 3. Non-Root by Default

* Add `USER nonroot` in Dockerfile
* Running as root fails security scans and platform policies

### 4. Set Resource Limits

* `-m 512m` on every container
* OOM killer strikes without warning otherwise

### 5. Configure Log Rotation

* Default json-file driver has no size limit
* One chatty container fills disk and crashes host

## Image Traps

* Multi-stage builds: forgotten `--from=builder` copies from wrong stage silently
* COPY before RUN invalidates cache on every file change — copy requirements first, install, then copy code
* `ADD` extracts archives automatically — use `COPY` unless you need extraction
* Build args visible in image history — never use for secrets

## Runtime Traps

* `localhost` inside container is container's localhost — bind to `0.0.0.0`
* Port already in use: previous container still stopping — wait or force remove
* Exit code 137 = OOM killed, 139 = segfault — check with `docker inspect --format='{{.State.ExitCode}}'`
* No shell in distroless images — `docker cp` files out or use debug sidecar

## Networking Traps

* Container DNS only works on custom networks — default bridge can't resolve names
* Published ports bind to `0.0.0.0` — use `127.0.0.1:5432:5432` for local-only
* Zombie connections from killed containers — set health checks and restart policies

## Compose Traps

* `depends_on` waits for container start, not service ready — use `condition: service_healthy`
* `.env` file in wrong directory silently ignored — must be next to docker-compose.yml
* Volume mounts overwrite container files — empty host dir = empty container dir
* YAML anchors don't work across files — use multiple compose files instead

## Volume Traps

* Anonymous volumes accumulate silently — use named volumes
* Bind mounts have permission issues — container user must match host user
* `docker system prune` doesn't remove named volumes — add `--volumes` flag
* Stopped container data persists until container removed

## Resource Leaks

* Dangling images grow unbounded — `docker image prune` regularly
* Build cache grows forever — `docker builder prune` reclaims space
* Stopped containers consume disk — `docker container prune` or `--rm` on run
* Networks pile up from compose projects — `docker network prune`

## Secrets and Security

* ENV and COPY bake secrets into layer history permanently — use secrets mount or runtime env
* `--privileged` disables all security — almost never needed, find specific capability instead
* Images from unknown registries may be malicious — verify sources
* Build args visible in image history — don't use for secrets

## Debugging

* Exit code 137 = OOM killed, 139 = segfault — check `docker inspect --format='{{.State.ExitCode}}'`
* Container won't start: check logs even for failed containers — `docker logs <container>`
* No shell in distroless images — `docker cp` files out or use debug sidecar
* Inspect filesystem of dead container — `docker cp deadcontainer:/path ./local`

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `devops` — deployment pipelines
* `linux` — host system management
* `server` — server administration

## Feedback

* If useful: `
* Stay updated: `

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

- Docker containers, images, Compose stacks, networking, volumes, debugging,
  production hardening,
- 触发关键词: compose, containers, docker, images, stacks

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

### Q1: 如何开始使用Docker？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Docker有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
