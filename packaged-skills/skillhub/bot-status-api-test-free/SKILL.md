---
slug: bot-status-api-test-free
name: bot-status-api-test-free
version: "1.0.0"
displayName: Bot状态监控免费版
summary: 可配置HTTP服务,暴露Bot核心运行状态为JSON,含HTTP健康检查与基础端点
license: MIT
description: |-
  Bot 状态监控 API 服务免费版。可配置的 HTTP 服务,将 Bot 的核心运行状态暴露为 JSON。
  覆盖 Bot 核心（在线状态、模型、运行时间）与 HTTP 服务健康检查。
  command/file-exists 检查、邮件未读计数、Cron 任务、Docker 监控、系统指标等高级功能需升级付费版。
  零依赖（Node.js 内置模块）、非阻塞异步架构、配置驱动。
tags:
  - Integrations
  - Monitoring
tools:
  - read
  - exec
---

# Bot 状态监控 API（免费版）

可配置的 HTTP 服务,将 Bot 的核心运行状态暴露为 JSON。零依赖、非阻塞、配置驱动。

> **升级提示**: command/file-exists 检查、邮件未读计数、Cron 任务、Docker 监控、系统指标、systemd 持久化等高级功能为付费版专享。升级付费版解锁完整能力。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

- **Bot 核心**: 在线状态、模型名称、运行时间
- **HTTP 服务健康检查**: `http` 类型,请求 URL 检查 HTTP 200
- **状态端点**: `GET /status` 返回状态 JSON,`GET /health` 返回健康检查
- **零依赖**: 仅使用 Node.js 内置模块（`http`、`fs`、`child_process`）
- **非阻塞**: 所有 shell 命令使用异步 `exec`

### 付费版专享功能
以下功能在免费版中不可用,升级付费版解锁:

- **上下文使用率**: `contextPercent`、`contextUsed`、`contextMax` 等上下文指标
- **command 检查**: 执行 shell 命令检查退出码 0
- **file-exists 检查**: 检查文件路径是否存在
- **邮件未读计数**: 从邮件客户端（himalaya、gog 等）读取未读邮件数
- **Cron 任务**: 读取 `cron/jobs.json` 展示定时任务状态
- **Docker 监控**: 通过 Portainer API 检查容器健康状态
- **开发服务器检测**: 通过进程 grep 自动检测运行中的开发服务器
- **Skills 列表**: 列出已安装与可用的 Skills
- **系统指标**: 从 `/proc` 读取 CPU、RAM、Disk 使用率
- **systemd 持久化**: 系统服务部署与开机自启
- **自定义缓存 TTL**: 自定义 `cache.ttlMs` 缓存刷新间隔

**输入**: 用户提供付费版专享功能所需的指令和必要参数。
**输出**: 返回付费版专享功能的执行结果,包含操作状态和输出数据。
### Bot 核心

执行Bot 核心操作,处理用户输入并返回结果。

**输入**: 用户提供Bot 核心所需的参数和指令。

**输出**: 返回Bot 核心的处理结果。

- 执行`Bot 核心`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`Bot 核心`相关配置参数进行设置
### HTTP 服务健康检查

执行HTTP 服务健康检查操作,处理用户输入并返回结果。

**输入**: 用户提供HTTP 服务健康检查所需的参数和指令。

**输出**: 返回HTTP 服务健康检查的处理结果。

- 执行`HTTP 服务健康检查`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`HTTP 服务健康检查`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 可配置、核心运行状态为、健康检查与基础端、状态监控、服务免费版、可配置的、的核心运行状态暴、系统指标等高级功、能需升级付费版、非阻塞异步架构、配置驱动。这些能力在上述核心功能中均有对应处理逻辑。
## 配置文件

从 `config.example.json` 复制为 `config.json` 并自定义:

```json
{
  "port": 3200,
  "name": "MyBot",
  "services": [
    { "name": "myservice", "type": "http", "url": "http://...", "healthPath": "/health" }
  ]
}
```

> **升级提示**: 付费版支持 `command` 与 `file-exists` 检查类型,以及 `cache.ttlMs` 自定义缓存间隔。

## API 端点

| 端点 | 说明 |
|------|------|
| `GET /status` | Bot 核心状态与服务健康检查 JSON |
| `GET /health` | 简单健康检查,返回 `{"status":"ok"}` |

## 使用流程

### Step 1: 复制服务文件
将 `server.js`、`collectors/` 与 `package.json` 复制到目标位置。

### Step 2: 创建配置文件
```bash
cp config.example.json config.json
```
编辑 `config.json`,设置 `port`、`name`、`services` 等字段。

### Step 3: 启动服务
```bash
node server.js
```

### Step 4: 查询状态
```bash
curl http://localhost:3200/status
curl http://localhost:3200/health
```

> **提示**: 如需 command/file-exists 检查、Docker 监控、系统指标等高级功能,请升级付费版。

### 命令参数说明

- `-sonnet-4-20250514`: 命令参数,用于指定操作选项
- `-gateway`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 案例展示

### 案例1: 基础启动与状态查询
**场景**: 开发者需要查看 Bot 的基本运行状态

```bash
# 启动服务
node server.js

# 查询状态
curl http://localhost:3200/status

# 健康检查
curl http://localhost:3200/health
```

**`GET /status` 响应示例**:
```json
{
  "bot": {
    "name": "MyBot",
    "online": true,
    "model": "claude-sonnet-4-20250514",
    "uptime": 3600
  },
  "services": [
    { "name": "myservice", "type": "http", "healthy": true }
  ]
}
```

**说明**: 端口 3200,返回 Bot 在线状态、模型名称与运行时间。`http` 类型服务检查返回 `healthy: true`。

> **升级提示**: 付费版额外返回 `vitals`（`contextPercent`、`contextUsed`、`contextMax`）上下文使用率与 `system`（CPU/RAM/Disk）系统指标。

### 案例2: 配置 HTTP 服务健康检查
**场景**: 监控 HTTP 服务的健康状态

```json
{
  "services": [
    { "name": "api-gateway", "type": "http", "url": "http://api.example.com", "healthPath": "/health" }
  ]
}
```

**说明**: `http` 类型请求 `url + healthPath`,检查响应是否为 HTTP 200。

> **升级提示**: 付费版支持 `command` 类型（执行 shell 命令检查退出码 0）与 `file-exists` 类型（检查路径是否存在）。

## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|---------|---------|---------|---------|
| config.json 不存在 | `Cannot find module './config.json'` | 未从 `config.example.json` 复制 | 执行 `cp config.example.json config.json` 并编辑 |
| 端口被占用 | `EADDRINUSE: address already in use :::3200` | 端口 3200 被占用 | 修改 `config.json` 中 `port` 字段 |
| HTTP 检查失败 | 服务 `healthy: false` | 目标 URL 返回非 200 | 检查目标服务是否正常运行 |
| 功能不可用 | — | 需 command/file-exists 检查、Docker 监控等 | 升级付费版解锁高级功能 |
| 上下文指标缺失 | `vitals` 字段为空 | 免费版不含上下文使用率 | 升级付费版获取 `contextPercent` 等指标 |

## 常见问题

### Q1: 免费版支持哪些服务检查类型?
A: 免费版仅支持 `http` 类型（请求 URL 检查 HTTP 200）。`command`（执行 shell 命令检查退出码 0）与 `file-exists`（检查路径是否存在）为付费版专享。

### Q2: 免费版包含上下文使用率吗?
A: 不包含。`contextPercent`、`contextUsed`、`contextMax` 等上下文指标需 Bot 写入 `heartbeat-state.json`,为付费版专享功能。

### Q3: 免费版能监控 Docker 容器吗?
A: 不能。通过 Portainer API 检查容器健康状态为付费版专享。免费版仅支持 HTTP 服务健康检查。

### Q4: 免费版能读取系统指标吗?
A: 不能。CPU/RAM/Disk 系统指标（从 `/proc` 读取）为付费版专享。免费版不包含系统指标采集。

### Q5: 免费版支持 systemd 持久化部署吗?
A: 不支持。systemd 用户服务部署与开机自启为付费版专享。免费版需手动启动 `node server.js`。

### Q6: 缓存刷新间隔能自定义吗?
A: 免费版使用默认缓存 TTL（10000ms）,不可自定义。升级付费版可通过 `config.json` 的 `cache.ttlMs` 字段自定义缓存刷新间隔。

## 已知限制

1. **仅 HTTP 检查**: 不支持 `command` 与 `file-exists` 检查类型
2. **无上下文指标**: 不含 `contextPercent` 等上下文使用率
3. **无邮件计数**: 不含未读邮件计数功能
4. **无 Cron 任务**: 不含 `cron/jobs.json` 读取
5. **无 Docker 监控**: 不含 Portainer API 容器健康检查
6. **无系统指标**: 不含 CPU/RAM/Disk 指标采集
7. **无 systemd 持久化**: 不含系统服务部署
8. **固定缓存 TTL**: 不可自定义缓存刷新间隔

---

> **升级付费版** 解锁: command/file-exists 检查、上下文使用率、邮件未读计数、Cron 任务、Docker 监控、系统指标、systemd 持久化、自定义缓存 TTL 等完整能力。
