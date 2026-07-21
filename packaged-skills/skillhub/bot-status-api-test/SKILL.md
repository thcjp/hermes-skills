---
slug: bot-status-api-test
name: bot-status-api-test
version: "1.0.0"
displayName: Bot状态监控API
summary: 可配置HTTP服务,暴露Bot运行状态为JSON,含服务健康检查、Docker监控、系统指标与Cron任务
license: MIT
description: |-
  Bot 状态监控 API 服务。可配置的 HTTP 服务,将 Bot 的运行状态暴露为 JSON,设计用于仪表盘集成、监控与透明度。
  覆盖 Bot 核心（在线状态、模型、上下文使用、运行时间、心跳）、服务健康检查（HTTP/CLI/文件路径）、
  邮件未读计数、Cron 任务、Docker 容器健康、开发服务器检测、已安装 Skills 列表与系统指标（CPU/RAM/Disk）。
  零依赖（Node.js 内置模块）、非阻塞异步架构、后台缓存刷新（默认 10 秒 TTL）、配置驱动。
  适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Integrations
  - Monitoring
tools:
  - read
  - exec
---

# Bot 状态监控 API

可配置的 HTTP 服务,将 Bot 的运行状态暴露为 JSON。设计用于仪表盘集成、监控与透明度。零依赖、非阻塞、配置驱动。

**范围外**（本技能不做）: 实时流数据处理、Bot 远程控制、日志聚合与搜索、告警通知分发。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux（系统指标读取需 Linux `/proc`）
- **运行时**: Node.js（建议 18+）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 系统包管理器或官网安装 |
| `config.json` | 配置文件 | 必需 | 从 `config.example.json` 复制并自定义 |
| `heartbeat-state.json` | 数据文件 | 可选 | Bot 周期性写入,缺失则上下文指标为空 |

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令驱动,需 exec 执行 Node.js 脚本）
- **说明**: 基于自然语言指令驱动 Agent 启动监控服务,暴露 Bot 状态 JSON

## 核心能力

- **Bot 核心**: 在线状态、模型名称、上下文使用率（`contextPercent`）、运行时间、心跳时间
- **服务健康检查**: 支持 `http`（HTTP 200 检测）、`command`（退出码 0 检测）、`file-exists`（路径存在检测）三种类型
- **邮件未读计数**: 从邮件客户端（himalaya、gog 等）读取未读邮件数
- **Cron 任务**: 直接读取 `cron/jobs.json` 展示定时任务状态
- **Docker 监控**: 通过 Portainer API 检查容器健康状态
- **开发服务器检测**: 通过进程 grep 自动检测运行中的开发服务器
- **Skills 列表**: 列出已安装与可用的 Skills
- **系统指标**: 从 `/proc` 读取 CPU、RAM、Disk 使用率

## 架构特性

- **零依赖**: 仅使用 Node.js 内置模块（`http`、`fs`、`child_process`）
- **非阻塞**: 所有 shell 命令使用异步 `exec`,永不使用 `execSync`
- **后台刷新**: 缓存按间隔刷新,请求始终从缓存读取（约 10ms 响应）
- **配置驱动**: 所有配置在 `config.json` 中,无硬编码值

## 配置文件

从 `config.example.json` 复制为 `config.json` 并自定义:

```json
{
  "port": 3200,
  "name": "MyBot",
  "workspace": "/path/to/.skill-platform/workspace",
  "skill-platformHome": "/path/to/.skill-platform",
  "cache": { "ttlMs": 10000 },
  "model": "claude-sonnet-4-20250514",
  "skillDirs": ["/path/to/skill-platform/skills"],
  "services": [
    { "name": "myservice", "type": "http", "url": "http://...", "healthPath": "/health" }
  ]
}
```

### 服务检查类型

| 类型 | 说明 | 配置字段 |
|------|------|---------|
| `http` | 请求 URL,检查 HTTP 200 | `url`, `healthPath`, `method`, `headers`, `body` |
| `command` | 执行 shell 命令,检查退出码 0 | `command`, `timeout` |
| `file-exists` | 检查路径是否存在 | `path` |

## API 端点

| 端点 | 说明 |
|------|------|
| `GET /status` | 完整状态 JSON（缓存读取,约 10ms 响应） |
| `GET /health` | 简单健康检查,返回 `{"status":"ok"}` |

## 使用流程

### Step 1: 复制服务文件
将 `server.js`、`collectors/` 与 `package.json` 复制到目标位置。

### Step 2: 创建配置文件
```bash
cp config.example.json config.json
```
编辑 `config.json`,设置 `port`、`name`、`workspace`、`services` 等字段。

### Step 3: 启动服务
```bash
node server.js
```

### Step 4: 持久化（systemd 用户服务）
```ini
[Unit]
Description=Bot Status API
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/bot-status
ExecStart=/usr/bin/node server.js
Restart=always
RestartSec=5
Environment=PORT=3200
Environment=HOME=/home/youruser

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now bot-status
loginctl enable-linger $USER
```

### Step 5: 配置 Bot 心跳数据
Bot 周期性将运行指标写入 `heartbeat-state.json`:
```json
{
  "vitals": {
    "contextPercent": 62,
    "contextUsed": 124000,
    "contextMax": 200000,
    "model": "claude-opus-4-5",
    "updatedAt": 1770304500000
  }
}
```
将此逻辑加入 Bot 的 HEARTBEAT.md,每次心跳周期更新。

## 案例展示

### 案例1: 基础启动与状态查询
**场景**: 开发者需要查看 Bot 的运行状态

```bash
# 启动服务
node server.js

# 查询完整状态
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
    "uptime": 3600,
    "vitals": {
      "contextPercent": 62,
      "contextUsed": 124000,
      "contextMax": 200000
    }
  },
  "services": [
    { "name": "myservice", "type": "http", "healthy": true }
  ],
  "system": {
    "cpu": 45.2,
    "ram": 68.5,
    "disk": 72.1
  }
}
```

**说明**: 端口 3200,缓存 TTL 10000ms,从缓存读取约 10ms 响应。`contextPercent` 62% 表示上下文已使用过半。

### 案例2: 配置 HTTP 服务健康检查
**场景**: 监控多个 HTTP 服务的健康状态

```json
{
  "services": [
    { "name": "api-gateway", "type": "http", "url": "http://api.example.com", "healthPath": "/health" },
    { "name": "web-frontend", "type": "http", "url": "http://web.example.com", "healthPath": "/healthz" }
  ]
}
```

**说明**: `http` 类型请求 `url + healthPath`,检查响应是否为 HTTP 200。 unhealthy 的服务在 `/status` 响应中 `healthy: false`。

### 案例3: 配置命令与文件检查
**场景**: 监控 CLI 工具可用性与配置文件存在性

```json
{
  "services": [
    { "name": "redis", "type": "command", "command": "redis-cli ping", "timeout": 5000 },
    { "name": "ssl-cert", "type": "file-exists", "path": "/etc/ssl/certs/myapp.pem" }
  ]
}
```

**说明**: `command` 类型执行 shell 命令,退出码 0 为健康;`file-exists` 类型检查路径是否存在。命令执行使用异步 `exec`,不阻塞主线程。

### 案例4: systemd 持久化部署
**场景**: 将监控服务设为系统服务,开机自启

```bash
systemctl --user daemon-reload
systemctl --user enable --now bot-status
loginctl enable-linger $USER
```

**说明**: `enable-linger` 确保用户注销后服务继续运行。`Restart=always` 与 `RestartSec=5` 在服务异常退出时 5 秒后自动重启。

## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|---------|---------|---------|---------|
| config.json 不存在 | `Cannot find module './config.json'` | 未从 `config.example.json` 复制 | 执行 `cp config.example.json config.json` 并编辑 |
| 端口被占用 | `EADDRINUSE: address already in use :::3200` | 端口 3200 被其他进程占用 | 修改 `config.json` 中 `port` 字段换端口 |
| 服务检查超时 | `command timed out after 5000ms` | `command` 类型检查超过 `timeout` | 增加 `timeout` 值,或检查目标服务是否响应 |
| heartbeat-state.json 格式错误 | `SyntaxError: Unexpected token` | Bot 写入的文件非合法 JSON | 检查 Bot 心跳写入逻辑,确保输出合法 JSON |
| /proc 不可读 | `ENOENT: no such file /proc/stat` | 非 Linux 系统或权限不足 | 系统指标功能需 Linux 环境,Windows/macOS 下该字段为空 |
| Portainer API 不可达 | Docker 容器状态显示 `unknown` | Portainer 服务未运行或 URL 错误 | 检查 Portainer 服务状态与 `config.json` 中 URL |
| cron/jobs.json 不存在 | Cron 任务列表为空 | Bot 未配置定时任务或路径错误 | 检查 `workspace` 路径是否正确指向 Bot 工作区 |

## 常见问题

### Q1: 这个服务需要安装 npm 依赖吗?
A: 不需要。服务仅使用 Node.js 内置模块（`http`、`fs`、`child_process`）,零依赖。只需安装 Node.js（建议 18+）即可运行。

### Q2: 缓存刷新间隔是多少? 能自定义吗?
A: 默认缓存 TTL 为 10000ms（10 秒）。可在 `config.json` 的 `cache.ttlMs` 字段自定义。请求始终从缓存读取（约 10ms 响应）,后台按 TTL 间隔刷新缓存。

### Q3: `contextPercent` 是什么意思?
A: 表示 Bot 的上下文窗口使用百分比。例如 `contextPercent: 62` 表示已使用 62% 的上下文窗口（`contextUsed: 124000` / `contextMax: 200000`）。接近 100% 时需考虑压缩对话或开启新会话。

### Q4: 服务检查的三种类型有什么区别?
A: `http` 类型请求 URL 检查 HTTP 200;`command` 类型执行 shell 命令检查退出码 0;`file-exists` 类型检查文件路径是否存在。所有检查使用异步 `exec`,不阻塞主线程。

### Q5: 如何让 Bot 写入心跳数据?
A: 在 Bot 的 HEARTBEAT.md 中添加逻辑,每次心跳周期将运行指标写入 `heartbeat-state.json`。文件包含 `vitals` 对象,含 `contextPercent`、`contextUsed`、`contextMax`、`model`、`updatedAt` 字段。

### Q6: 系统指标在 Windows 上能用吗?
A: 系统指标（CPU/RAM/Disk）通过读取 Linux `/proc` 文件系统获取。在 Windows/macOS 上该字段为空。如需跨平台系统指标,可扩展 `collectors/` 添加平台特定的采集器。

## 已知限制

1. **系统指标需 Linux**: CPU/RAM/Disk 指标从 `/proc` 读取,Windows/macOS 下为空
2. **依赖外部数据源**: Bot 心跳数据需 Bot 主动写入 `heartbeat-state.json`
3. **无认证保护**: `GET /status` 与 `GET /health` 无认证,部署时需通过网络层限制访问
4. **缓存延迟**: 数据有最长 10 秒（可配置）的缓存延迟,非实时
5. **单实例设计**: 不支持集群部署与负载均衡
6. **Docker 监控依赖 Portainer**: 容器健康检查需 Portainer API 运行
