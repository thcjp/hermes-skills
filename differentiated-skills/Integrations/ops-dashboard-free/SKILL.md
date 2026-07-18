---
slug: ops-dashboard-free
name: ops-dashboard-free
version: "1.0.0"
displayName: 运维看板(免费版)
summary: 实时运维监控看板免费版，支持会话查看、定时任务监控与基础健康检查
license: MIT
edition: free
description: |-
  运维看板免费版是一款面向个人开发者和小团队的实时运维监控辅助Skill，让AI Agent能够查看会话状态、监控定时任务执行情况和检查系统健康度，实现轻量级的运维可视化。

  核心能力：会话列表查看、定时任务状态监控、网关健康检查、基础安全扫描、配置文件管理。覆盖日常运维巡检的高频需求。

  适用场景：个人项目运维巡检、定时任务执行监控、会话状态快速查看、安全配置审查、本地开发环境健康检查。

  差异化：相比重量级运维平台，本工具轻量易部署，通过AI Agent自然语言驱动即可完成日常巡检。免费版聚焦只读监控和基础检查，满足个人运维需求。

  触发关键词：运维看板、监控、会话管理、定时任务、健康检查、巡检、dashboard
tags:
- 运维监控
- 健康检查
- 定时任务
- 集成工具
tools:
- read
- exec
---

# 运维看板（免费版）

通过命令行驱动AI Agent执行运维巡检任务，查看会话状态、监控定时任务和检查系统健康度。免费版提供只读监控和基础安全检查功能。

## 概述

在AI Agent驱动的自动化工作流中，运维可见性是保障系统稳定运行的关键。运维看板将分散的运维信息（会话状态、任务执行、网关健康、安全配置）聚合为统一的命令行接口，让AI Agent能够通过自然语言指令快速完成日常巡检。

免费版聚焦只读监控能力，提供会话查看、任务状态检查和健康巡检功能，适合个人开发者和小团队的轻量级运维场景。

## 核心能力

| 能力模块 | 免费版支持 | 说明 |
|:---------|:-----------|:-----|
| 会话查看 | 支持 | 列出和查看Agent会话状态 |
| 定时任务监控 | 支持 | 查看cron任务执行状态 |
| 健康检查 | 支持 | 网关和服务健康状态检查 |
| 安全扫描 | 基础 | 敏感信息扫描和报告 |
| 配置查看 | 支持 | 读取环境配置和默认值 |
| 成本分析 | 不支持 | 专业版提供 |
| 变更操作 | 不支持 | 专业版提供 |
| 告警通知 | 不支持 | 专业版提供 |
| 批量管理 | 不支持 | 专业版提供 |
| 审计日志 | 不支持 | 专业版提供 |

## 使用场景

### 场景一：每日运维巡检

每天快速检查系统运行状态，确认会话正常、定时任务按预期执行、网关健康。

### 场景二：定时任务监控

查看cron任务的最近执行结果，发现失败任务并及时处理。

### 场景三：安全配置审查

扫描配置文件中的敏感信息泄露风险，确保没有硬编码的Token或密钥。

## 快速开始

### 前置条件

- Node.js 18+ 已安装
- 运维看板服务已部署并运行
- 服务默认监听`http://localhost:3000`

### 验证安装

```bash
# 检查服务是否运行
curl http://localhost:3000/api/health

# 查看帮助
node api-server.js --help
```

### 60秒上手

```bash
# 1. 检查服务健康状态
curl http://localhost:3000/api/health

# 2. 查看活跃会话
curl http://localhost:3000/api/sessions

# 3. 查看定时任务状态
curl http://localhost:3000/api/cron

# 4. 查看网关健康
curl http://localhost:3000/api/gateway/health

# 5. 执行安全扫描
curl http://localhost:3000/api/security/scan
```

## 配置示例

### 环境变量配置

创建`.env`文件配置基础运行参数：

```bash
# .env 文件
DASHBOARD_PORT=3000
DASHBOARD_HOST=localhost

# 认证Token（推荐设置）
OPS_DASHBOARD_AUTH_TOKEN=your_secure_token_here

# CORS配置（默认仅允许本地访问）
DASHBOARD_CORS_ORIGINS=http://localhost:3000
```

### 会话查看

```bash
# 列出所有会话
curl http://localhost:3000/api/sessions

# 查看指定会话详情
curl http://localhost:3000/api/sessions/session-id

# 查看活跃会话
curl http://localhost:3000/api/sessions?status=active

# 带认证Token的请求
curl -H "Authorization: Bearer $OPS_DASHBOARD_AUTH_TOKEN" \
     http://localhost:3000/api/sessions
```

### 定时任务监控

```bash
# 查看所有cron任务
curl http://localhost:3000/api/cron

# 查看任务执行历史
curl http://localhost:3000/api/cron/history

# 查看指定任务详情
curl http://localhost:3000/api/cron/task-name

# 查看失败的任务
curl http://localhost:3000/api/cron?status=failed
```

### 健康检查

```bash
# 检查整体健康状态
curl http://localhost:3000/api/health

# 检查网关健康
curl http://localhost:3000/api/gateway/health

# 检查服务依赖
curl http://localhost:3000/api/health/dependencies
```

### 安全扫描

```bash
# 扫描配置文件中的敏感信息
curl http://localhost:3000/api/security/scan

# 检查环境变量安全性
curl http://localhost:3000/api/security/env-check

# 查看安全配置状态
curl http://localhost:3000/api/security/config
```

### 配置查看

```bash
# 查看当前运行配置
curl http://localhost:3000/api/config

# 查看环境变量（脱敏后）
curl http://localhost:3000/api/config/env

# 查看服务信息
curl http://localhost:3000/api/info
```

## 最佳实践

1. **设置认证Token**：即使本地使用也建议设置`OPS_DASHBOARD_AUTH_TOKEN`，防止未授权访问。
2. **限制CORS来源**：通过`DASHBOARD_CORS_ORIGINS`明确指定允许的来源，避免使用通配符`*`。
3. **定期执行安全扫描**：将安全扫描纳入每日巡检流程，及时发现敏感信息泄露。
4. **监控定时任务失败率**：关注cron任务的执行成功率，失败率突增时及时排查。
5. **配置文件脱敏**：确保`.env`文件不包含明文密钥，使用占位符代替真实Token。

## 常见问题

### Q1: 启动后无法访问页面？

检查服务是否正常监听。执行`curl http://localhost:3000/api/health`确认服务响应。若端口被占用，修改`DASHBOARD_PORT`环境变量。

### Q2: API返回401未授权？

设置了`OPS_DASHBOARD_AUTH_TOKEN`后，所有请求需携带`Authorization: Bearer <token>`头。确认Token值正确且未过期。

### Q3: CORS错误导致前端无法访问？

默认仅允许本地来源访问。如需跨域访问，设置`DASHBOARD_CORS_ORIGINS`为逗号分隔的允许来源列表。

### Q4: 安全扫描报告显示敏感信息？

检查配置文件中是否有硬编码的Token、密钥或绝对路径。将敏感值替换为环境变量引用或占位符。

### Q5: 定时任务状态显示"unknown"？

任务可能尚未执行或执行超时。检查任务配置和执行日志，确认cron表达式正确且任务脚本可正常执行。

## 依赖说明

### 运行环境

- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **Node.js**：18.0及以上版本
- **运行时**：运维看板服务需持续运行

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 从Node.js官网下载安装 |
| Express | npm包 | 必需 | 通过`npm install express`安装 |
| curl | 命令行工具 | 必需 | 系统通常自带 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

- **运维看板Token**：通过`OPS_DASHBOARD_AUTH_TOKEN`环境变量配置
- **存储位置**：建议存储在`.env`文件中（已加入.gitignore）
- **禁止**：在代码或配置文件中硬编码Token
- **默认行为**：未设置Token时仅允许本地访问，设置后需在请求头中携带

### 可用性分类

- **分类**：MD+EXEC（纯Markdown指令，需要exec命令行执行能力）
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行运维看板API调用

## 免费版限制

本免费体验版限制以下高级功能：
- 成本分析与用量统计（专业版提供Token消耗和API成本追踪）
- 变更操作与备份管理（专业版支持任务执行、备份创建和模型切换）
- 告警通知与自动响应（专业版支持阈值告警和自动重启）
- 批量会话管理（专业版支持批量终止、归档和清理）
- 审计日志与操作追踪（专业版提供完整操作审计链）
- 服务商审计集成（专业版支持调用AI服务商组织API）
- 系统级操作（专业版支持systemctl重启等系统管理操作）

解锁全部功能请使用专业版：ops-dashboard-pro
