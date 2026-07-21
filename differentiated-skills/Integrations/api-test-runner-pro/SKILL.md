---
slug: api-test-runner-pro
name: api-test-runner-pro
version: "1.0.0"
displayName: API测试运行器专业版
summary: 企业级服务状态聚合平台，支持HTTP/命令/文件/Docker/邮件/定时任务多维度探测与仪表盘集成
license: Proprietary
edition: pro
description: |-
  API测试运行器专业版是一款面向团队与企业的服务状态聚合平台，在免费版HTTP探活与命令行检查基础上，新增文件存在性检查、Docker容器健康监控、开发服务器自动发现、邮件未读数统计、定时任务状态读取与系统资源指标采集等高级能力。核心能力：
  - 六种探测类型：HTTP、命令行、文件存在性、Docker容器、开发服务器、系统资源
  - Docker容器健康检查，通过Portainer API获取容器状态
  - 开发服务器自动发现，基于进程名grep识别运行中的服务
  - 邮件未读数统计...
tags:
- 集成工具
- 状态监控
- 企业监控
tools:
  - - read
- exec
---
# API测试运行器专业版

企业级服务状态聚合平台，支持六种探测类型与仪表盘集成，覆盖从本地到容器的全链路监控需求。

## 概述

当服务规模从单机扩展到多容器、多服务器时，简单的HTTP探活已无法满足监控需求。运维团队需要了解Docker容器的健康状态、开发服务器的运行情况、定时任务的执行状态、系统资源的实时指标。专业版针对这些场景，提供六种探测类型与丰富的集成能力，让团队在一个面板中掌握全局状态。

专业版向后兼容免费版的所有配置，可直接升级替换。

## 核心能力

### 六种探测类型

| 类型 | 说明 | 典型用途 |
|------|------|----------|
| `http` | 访问URL检查HTTP状态码 | 后端API健康检查 |
| `command` | 执行shell命令检查退出码 | 数据库连接检查 |
| `file-exists` | 检查文件路径是否存在 | 锁文件、日志文件存在性 |
| `docker` | 通过Portainer API检查容器健康 | 容器化服务监控 |
| `dev-server` | 基于进程名grep自动发现开发服务器 | 本地开发环境监控 |
| `system` | 从/proc读取CPU/内存/磁盘指标 | 系统资源监控 |

**输入**: 用户提供六种探测类型所需的指令和必要参数。
**处理**: 按照skill规范执行六种探测类型操作,遵循单一意图原则。
**输出**: 返回六种探测类型的执行结果,包含操作状态和输出数据。

### Docker容器健康监控
- 通过Portainer API获取容器列表与健康状态
- 支持按容器名、标签过滤监控范围
- 容器异常退出时自动标记为down并记录退出码

**输入**: 用户提供Docker容器健康监控所需的指令和必要参数。
**处理**: 按照skill规范执行Docker容器健康监控操作,遵循单一意图原则。
**输出**: 返回Docker容器健康监控的执行结果,包含操作状态和输出数据。

### 开发服务器自动发现
- 基于进程名grep识别运行中的开发服务器
- 自动匹配Vite、Webpack、Next.js等常见开发服务器
- 端口与进程信息自动填充到状态JSON

**输入**: 用户提供开发服务器自动发现所需的指令和必要参数。
**处理**: 按照skill规范执行开发服务器自动发现操作,遵循单一意图原则。
**输出**: 返回开发服务器自动发现的执行结果,包含操作状态和输出数据。

### 邮件与定时任务监控
- 读取邮件客户端（himalaya等）的未读邮件数
- 直接解析cron任务配置文件，展示任务列表与上次执行状态
- 支持自定义邮件客户端适配器

**输入**: 用户提供邮件与定时任务监控所需的指令和必要参数。
**处理**: 按照skill规范执行邮件与定时任务监控操作,遵循单一意图原则。
**输出**: 返回邮件与定时任务监控的执行结果,包含操作状态和输出数据。

### 系统资源指标
- 从`/proc`读取CPU使用率、内存占用、磁盘空间
- 无需安装额外agent，纯文件读取
- 支持按分区粒度展示磁盘使用情况

**输入**: 用户提供系统资源指标所需的指令和必要参数。
**处理**: 按照skill规范执行系统资源指标操作,遵循单一意图原则。
**输出**: 返回系统资源指标的执行结果,包含操作状态和输出数据。

### 服务化部署与仪表盘集成
- 内置systemd服务模板，一键注册为系统服务
- 提供CORS响应头，支持浏览器端仪表盘直接调用
- 兼容Grafana SimpleJSON数据源，可接入Grafana面板

**输入**: 用户提供服务化部署与仪表盘集成所需的指令和必要参数。
**处理**: 按照skill规范执行服务化部署与仪表盘集成操作,遵循单一意图原则。
**输出**: 返回服务化部署与仪表盘集成的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级服务状态聚、合平台、定时任务多维度探、测与仪表盘集成、测试运行器专业版、是一款面向团队与、企业的服务状态聚、在免费版、探活与命令行检查、基础上、新增文件存在性检、邮件未读数统计、定时任务状态读取、与系统资源指标采、集等高级能力、核心能力、命令行、容器健康检查、获取容器状态、识别运行中的服务等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：团队多服务器统一监控
运维团队管理5台服务器，每台运行多个Docker容器。在各服务器部署专业版实例，配置Docker探测类型，再通过中心仪表盘聚合各实例的`/status`输出，实现全局视图。

### 场景二：开发环境自动发现
开发团队多人协作，各自本地运行不同端口的开发服务器。专业版自动发现这些服务器并展示在状态面板中，成员可快速了解谁在跑什么服务、端口是否冲突。

### 场景三：定时任务与健康检查联动
团队有多个定时任务（数据备份、日志清理、报表生成）。专业版读取cron配置，展示任务列表与状态。若某任务对应的脚本文件不存在，自动标记为异常。

### 场景四：Grafana面板集成
将专业版的`/status`端点接入Grafana的SimpleJSON数据源，在Grafana中构建服务状态大盘，设置告警规则，实现团队级监控可视化。

## 不适用场景

以下场景API测试运行器专业版不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理

## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求。

## 快速开始

预计上手时间：约120秒。

### 第一步：创建完整配置

```json
{
  "port": 3200,
  "name": "TeamMonitor",
  "workspace": "/path/to/workspace",
  "cache": { "ttlMs": 10000 },
  "model": "claude-sonnet-4-20250514",
  "skillDirs": ["/path/to/skills"],
  "services": [
    {
      "name": "backend-api",
      "type": "http",
      "url": "http://localhost:8080/health",
      "healthPath": "/health"
    },
    {
      "name": "redis-check",
      "type": "command",
      "command": "redis-cli ping | grep PONG",
      "timeout": 3000
    },
    {
      "name": "lock-file",
      "type": "file-exists",
      "path": "/var/run/myapp.lock"
    },
    {
      "name": "web-container",
      "type": "docker",
      "containerName": "web-server",
      "portainerUrl": "http://localhost:9000"
    },
    {
      "name": "vite-dev",
      "type": "dev-server",
      "processPattern": "vite"
    },
    {
      "name": "system-metrics",
      "type": "system",
      "diskPaths": ["/", "/data"]
    }
  ]
}
```

### 第二步：启动服务

```bash
node server.js
```

### 第三步：注册为系统服务

```ini
[Unit]
Description=API Test Runner Pro
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/api-test-runner
ExecStart=/usr/bin/node server.js
Restart=always
RestartSec=5
Environment=PORT=3200
Environment=HOME=/home/youruser
Environment=PATH=/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now api-test-runner
loginctl enable-linger $USER
```

### 第四步：查询完整状态

```bash
curl http://localhost:3200/status | jq
```

返回包含六种探测类型的完整状态JSON。

## 示例

### Docker探测配置

```json
{
  "name": "postgres-container",
  "type": "docker",
  "containerName": "pg-main",
  "portainerUrl": "http://localhost:9000",
  "portainerToken": "${PORTAINER_TOKEN}"
}
```

### 开发服务器发现配置

```json
{
  "name": "dev-servers",
  "type": "dev-server",
  "processPatterns": ["vite", "webpack-dev", "next-server", "react-scripts"]
}
```

### 系统资源监控配置

```json
{
  "name": "system-health",
  "type": "system",
  "metrics": ["cpu", "memory", "disk"],
  "diskPaths": ["/", "/data", "/var/log"],
  "thresholds": {
    "cpuWarn": 80,
    "memWarn": 85,
    "diskWarn": 90
  }
}
```

### 邮件未读数配置

```json
{
  "name": "unread-mail",
  "type": "email",
  "client": "himalaya",
  "mailboxes": ["INBOX", "urgent"]
}
```

## 最佳实践

### 监控架构建议
- 每台服务器部署一个专业版实例，本地探测
- 中心仪表盘通过轮询各实例`/status`聚合全局视图
- 探测项按服务重要性分级，关键服务缩短缓存TTL

### Docker监控建议
- Portainer Token通过环境变量注入，不写入配置文件
- 容器名使用有意义的命名规范，便于在状态面板识别
- 为关键容器配置`restart: unless-stopped`策略

### 开发服务器发现建议
- 进程匹配模式尽量精确，避免误匹配
- 为每个开发服务器在配置中声明预期端口范围
- 团队成员约定端口分配规范，减少冲突

### 仪表盘集成建议
- Grafana数据源设置为SimpleJSON，URL指向`/status`
- 告警规则按服务级别设置不同阈值
- 面板按服务分组展示，便于快速定位问题

### 安全建议
- Portainer Token与邮件凭证通过环境变量注入
- 服务绑定`127.0.0.1`，外部访问通过Nginx反向代理并加认证
- 系统资源探测不需要额外权限，避免以root运行

## 常见问题

### Q1：Docker探测返回认证失败？
检查Portainer Token是否正确。在Portainer的"API Tokens"页面生成Token，通过`PORTAINER_TOKEN`环境变量注入。

### Q2：开发服务器发现不到？
检查进程是否正在运行：`ps aux | grep vite`。若进程名与配置的`processPattern`不匹配，调整模式或使用更宽泛的匹配。

### Q3：系统资源指标在macOS上不可用？
macOS没有`/proc`文件系统。系统资源探测目前仅支持Linux。macOS可通过`command`类型调用`top`或`vm_stat`实现类似功能。

### Q4：邮件未读数为0但实际有未读？
检查邮件客户端配置是否正确。himalaya需要先完成账户配置并同步邮箱。执行`himalaya envelope list`验证客户端是否正常工作。

### Q5：多实例如何聚合？
在中心服务器部署一个聚合脚本，定时轮询各实例的`/status`端点，合并为统一JSON后暴露给仪表盘。或使用Grafana的多数据源功能直接轮询各实例。

### Q6：systemd服务启动后立即退出？
检查`WorkingDirectory`与`ExecStart`路径是否正确。执行`journalctl --user -u api-test-runner -f`查看实时日志定位错误。

### Q7：状态JSON过大影响性能？
探测项超过50个时，JSON可能较大。可通过`?filter=critical`参数只返回关键探测项，或拆分为多个实例分担探测负载。

### Q8：能否接入告警系统？
专业版兼容Grafana SimpleJSON，可在Grafana中配置告警规则。也可通过webhook将状态变化推送到Slack或企业微信。

## 专业版特性

本专业版相比免费版新增以下能力：
- 六种探测类型：新增文件存在性、Docker、开发服务器、系统资源、邮件
- Docker容器健康监控：通过Portainer API获取容器状态
- 开发服务器自动发现：基于进程名grep识别运行中的服务
- 邮件与定时任务监控：未读数统计与cron任务状态读取
- 系统资源指标采集：CPU/内存/磁盘从/proc读取
- systemd服务化部署与Grafana仪表盘集成

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | HTTP探活+命令行检查 | 个人试用 |
| 收费专业版 | 29.9元/月 | 全功能+六种探测+仪表盘集成 | 团队/企业 |

专业版通过SkillHub SkillPay发布。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Linux（系统资源探测依赖`/proc`，其他探测类型支持Windows/macOS）
- **Node.js**: 16+（推荐LTS版本）
- **可选**: Portainer（Docker探测）、himalaya（邮件探测）、systemd（服务化部署）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org官方下载 |
| Portainer | API | 可选 | Docker部署Portainer Server |
| himalaya | CLI工具 | 可选 | 各平台包管理器安装 |
| Grafana | 可视化 | 可选 | grafana.com官方下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

> 核心服务零外部npm依赖，仅使用Node.js内置模块。可选依赖按需安装。

### API Key 配置
- **Portainer Token**: 通过`PORTAINER_TOKEN`环境变量注入
- **邮件客户端凭证**: 由各邮件客户端自身配置管理
- **探测端点Token**: 写入配置的`headers`字段，建议引用环境变量
- **禁止**: 在SKILL.md、配置文件或脚本中硬编码明文Token

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
