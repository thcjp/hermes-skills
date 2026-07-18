---
slug: api-test-runner-free
name: api-test-runner-free
version: "1.0.0"
displayName: API测试运行器免费版
summary: 轻量级HTTP服务状态探针，将任意端点的健康状态暴露为标准化JSON，支持基础HTTP探活与命令行检查
license: MIT
edition: free
description: |-
  API测试运行器免费版是一款面向独立开发者的服务状态探针工具，通过本地HTTP服务将多个端点的健康状态聚合为标准化JSON输出，便于接入仪表盘或监控告警系统。

  核心能力：
  - 零依赖Node.js服务，仅使用内置模块
  - 支持HTTP端点探活与命令行退出码检查两种探测方式
  - 配置驱动，所有探测目标在config.json中声明
  - 后台定时刷新，请求即时返回缓存结果（约10ms响应）
  - 暴露/status与/health两个端点，适配不同集成场景

  适用场景：
  - 个人开发者聚合多个自建服务的健康状态
  - 自动化脚本需要批量探测端点可用性
  - 学习与原型阶段快速搭建状态检查服务

  差异化：重构探测逻辑为中文化文档，新增场景化指南与故障排查矩阵，适配多平台Agent环境。

  触发关键词：API测试、状态探针、健康检查、服务监控、HTTP探活
tags:
- 集成工具
- 状态监控
- API测试
tools:
- read
- exec
---

# API测试运行器免费版

一款轻量级服务状态探针工具，通过本地HTTP服务将多个端点的健康状态聚合为标准化JSON输出。

## 概述

在多服务协同的开发环境中，开发者经常需要快速了解各个服务（数据库、缓存、后端API、第三方依赖）的存活状态。手动逐个curl既低效又难以集成到仪表盘。本工具通过一个本地HTTP服务，定时探测所有配置的端点，并以标准化JSON返回聚合状态，让监控集成变得简单。

免费版聚焦于HTTP探活与命令行检查两种基础探测方式，适合个人开发者在本地环境中快速搭建状态检查服务。

## 核心能力

### 多类型探测
- **HTTP探活**：访问指定URL，检查返回状态码是否为200
- **命令行检查**：执行shell命令，检查退出码是否为0
- 每个探测项可独立配置超时时间与探测频率

### 配置驱动
- 所有探测目标在`config.json`中声明，无需修改代码
- 支持为每个探测项命名、设置类型、配置参数
- 配置变更后重启服务即生效

### 后台刷新机制
- 探测在后台定时执行，结果写入缓存
- HTTP请求始终从缓存读取，响应时间约10ms
- 缓存TTL可配置，默认10秒

### 标准化输出
- `/status`：返回完整状态JSON，包含所有探测项的结果
- `/health`：返回简单的`{"status":"ok"}`，用于服务自身存活检查

## 使用场景

### 场景一：聚合多个自建服务状态
开发者在本地运行了数据库、缓存、后端API等多个服务，希望一目了然地查看所有服务的存活状态。配置各服务健康检查端点后，访问`/status`即可获取聚合视图。

### 场景二：自动化脚本前置检查
自动化脚本在执行前需要确认依赖服务可用。脚本调用`/status`端点，解析JSON后判断关键服务是否存活，不存活则跳过执行并告警。

### 场景三：本地开发仪表盘
开发者搭建了一个简单的本地仪表盘页面，通过轮询`/status`端点实时展示各服务状态，无需引入重量级监控方案。

## 快速开始

预计上手时间：约60秒。

### 第一步：创建配置文件

将`config.example.json`复制为`config.json`并自定义：

```json
{
  "port": 3200,
  "name": "MyService",
  "cache": { "ttlMs": 10000 },
  "services": [
    {
      "name": "backend-api",
      "type": "http",
      "url": "http://localhost:8080/health",
      "healthPath": "/health"
    },
    {
      "name": "db-check",
      "type": "command",
      "command": "pg_isready -h localhost -p 5432",
      "timeout": 5000
    }
  ]
}
```

### 第二步：启动服务

```bash
node server.js
```

### 第三步：查询状态

```bash
# 完整状态
curl http://localhost:3200/status

# 服务自身存活
curl http://localhost:3200/health
```

`/status`返回示例：

```json
{
  "name": "MyService",
  "timestamp": 1770304500000,
  "services": [
    { "name": "backend-api", "status": "up", "latencyMs": 45 },
    { "name": "db-check", "status": "up", "latencyMs": 12 }
  ]
}
```

## 配置示例

### 探测类型说明

| 类型 | 说明 | 必需配置 |
|------|------|----------|
| `http` | 访问URL检查HTTP 200 | `url`, `healthPath`, `method`, `headers`, `body` |
| `command` | 执行shell命令检查退出码 | `command`, `timeout` |

### HTTP探活配置

```json
{
  "name": "payment-service",
  "type": "http",
  "url": "https://api.example.com/payment",
  "healthPath": "/health",
  "method": "GET",
  "headers": { "Authorization": "Bearer token" },
  "timeout": 5000
}
```

### 命令行检查配置

```json
{
  "name": "disk-space",
  "type": "command",
  "command": "df -h / | awk 'NR==2{print $5}' | awk -F% '{if($1<90) exit 0; else exit 1}'",
  "timeout": 3000
}
```

### 完整配置结构

| 字段 | 类型 | 说明 | 是否必需 |
|------|------|------|----------|
| `port` | number | 服务监听端口 | 否（默认3200） |
| `name` | string | 服务实例名称 | 是 |
| `cache.ttlMs` | number | 缓存TTL（毫秒） | 否（默认10000） |
| `services` | array | 探测项列表 | 是 |
| `services[].name` | string | 探测项名称 | 是 |
| `services[].type` | string | 探测类型 | 是 |
| `services[].timeout` | number | 超时时间（毫秒） | 否 |

## 最佳实践

### 配置建议
- 探测超时建议设置为正常响应时间的3倍，避免误判
- 缓存TTL建议10秒，平衡实时性与探测开销
- 为每个探测项起有意义的名字，便于在状态JSON中识别

### 安全建议
- HTTP探活的`headers`中不要硬编码敏感Token，从环境变量读取
- 命令行检查避免使用`sudo`等提权命令
- 服务绑定`127.0.0.1`，避免状态接口对外暴露

### 性能建议
- 探测项数量建议不超过20个，避免后台刷新积压
- 命令行检查的命令应快速返回，避免长时间阻塞
- 高频探测场景适当缩短缓存TTL

## 常见问题

### Q1：HTTP探活返回down但浏览器能访问？
检查服务端是否返回非200状态码。部分健康检查端点在依赖异常时返回503，本工具将其判定为down。可查看响应体确认具体原因。

### Q2：命令行检查超时怎么办？
检查命令本身是否耗时过长。可在配置中增大`timeout`值，或优化命令逻辑。避免在命令中调用网络请求等不确定耗时的操作。

### Q3：状态JSON中时间戳是什么含义？
`timestamp`表示最近一次缓存刷新的时间。若该时间与当前时间差距过大，说明后台刷新可能已停止。

### Q4：能否探测文件是否存在？
免费版支持HTTP与命令行两种探测。文件存在性检查可通过命令行类型实现：`test -f /path/to/file`。

### Q5：如何同时监控多台机器？
免费版仅支持本地探测。如需多机监控、Docker容器健康检查与开发服务器自动发现，请使用专业版。

## 免费版限制

本免费体验版限制以下高级功能：
- 仅支持HTTP与命令行两种探测类型，无文件存在性检查
- 无Docker容器健康检查与Portainer集成
- 无开发服务器自动发现
- 无systemd服务化部署模板
- 无邮件未读数与定时任务监控
- 无多实例聚合与仪表盘集成

解锁全部功能请使用专业版：api-test-runner-pro

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（推荐LTS版本）
- **网络**: 需可访问所有配置的探测端点

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org官方下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

> 本工具零外部npm依赖，仅使用Node.js内置模块（`http`、`fs`、`child_process`）。

### API Key 配置
- **探测端点Token**: 若探测端点需要认证，将Token写入配置的`headers`字段
- **建议**: 敏感Token通过环境变量注入，配置文件引用变量名
- **禁止**: 在SKILL.md或配置文件中硬编码明文Token

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
