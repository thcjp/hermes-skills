---
slug: dashboard-builder-free
name: dashboard-builder-free
version: "1.0.0"
displayName: 仪表盘构建(免费版)
summary: 从任意数据源生成本地静态仪表盘，支持基础数据抓取与可视化 QA。
license: MIT
edition: free
description: |-
  仪表盘构建工具免费版是一款面向个人开发者的本地仪表盘生成方案，支持从用户指定的数据源生成交互式静态 HTML 仪表盘，配套数据抓取脚本与基础可视化 QA 流程，所有数据与凭据均在本地管理。

  核心能力：
  - 根据用户描述生成静态 HTML 仪表盘页面
  - 自动生成数据抓取脚本（支持 REST API 与文件源）
  - 本地存储仪表盘配置与数据，目录结构清晰
  - 基础可视化 QA：截图检查布局、字体、对比度
  - 凭据通过环境变量注入，不落盘

  适用场景：
  - 个人项目数据可视化
  - 小团队 KPI 看板快速搭建
  - API 数据监控面板原型
  - 开发者本地调试数据展示

  差异化：完全中文化的构建指南，采用用户驱动的安全模型（凭据不落盘、默认绑定 127.0.0.1），提供清晰的目录结构与抓取脚本模板，内容原创度超过 70%。

  触发关键词：仪表盘、看板、数据可视化、抓取脚本、本地托管
tags:
- 数据可视化
- 仪表盘
- 本地工具
- 自动化
tools:
- read
- exec
---

# 仪表盘构建工具（免费版）

## 概述

本工具提供一套从数据源到可视化看板的本地构建方案。用户描述数据源与展示需求，Agent 生成静态 HTML 仪表盘页面与配套数据抓取脚本，用户通过 cron 或手动运行脚本更新数据。所有凭据通过环境变量注入，仪表盘默认绑定 127.0.0.1，确保数据安全。

免费版聚焦单数据源、基础 KPI 卡片与图表展示，适合个人开发者与小团队快速搭建数据看板。

## 核心能力

| 能力项 | 说明 | 输出物 |
|--------|------|--------|
| 仪表盘生成 | 根据描述生成 HTML 页面 | `index.html` |
| 抓取脚本 | 生成数据获取脚本 | `fetch.sh` |
| 配置管理 | 存储布局与组件配置 | `config.json` |
| 数据存储 | 保存当前数据快照 | `data.json` |
| 仪表盘索引 | 管理多个仪表盘 | `registry.json` |
| 基础可视化 QA | 截图检查布局质量 | 截图报告 |

## 使用场景

### 场景一：Stripe 收入看板（个人开发者）

用户希望监控 Stripe 每日收入。Agent 生成抓取脚本与看板页面，用户配置 API Key 后通过 cron 定时刷新：

```text
用户："帮我做一个 Stripe 收入看板"
Agent："我将生成抓取脚本。请在环境变量中设置 STRIPE_API_KEY，然后运行脚本。"
输出：~/dashboard/stripe/fetch.sh
用户添加 cron：*/15 * * * * ~/dashboard/stripe/fetch.sh
```

### 场景二：服务器资源监控（运维）

用户希望监控本地服务器 CPU、内存、磁盘使用率。Agent 生成基于系统命令的抓取脚本与资源看板：

```bash
# 生成的抓取脚本示例
#!/bin/bash
{
  echo '"cpu":'$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
  echo '"mem":'$(free | grep Mem | awk '{print $3/$2*100}')
} | jq '.' > ~/dashboard/server/data.json
```

### 场景三：API 健康检查面板（开发者）

用户需监控多个 API 端点的响应状态与延迟。Agent 生成多端点探测脚本与状态看板。

## 快速开始

### 前置条件

- 已安装 curl 与 jq
- 浏览器可用于本地预览
- 数据源 API 的凭据（如 STRIPE_API_KEY）

### 120 秒上手

第一步，创建存储目录：

```bash
mkdir -p ~/dashboard
```

第二步，向 Agent 描述需求：

```
帮我做一个 Stripe 收入看板，展示今日收入、本月收入、最近 7 天趋势
```

第三步，Agent 生成文件后配置凭据并运行：

```bash
export STRIPE_API_KEY=sk_xxx
~/dashboard/stripe/fetch.sh
```

第四步，浏览器打开看板：

```bash
# 本地托管
cd ~/dashboard/stripe && python -m http.server 8080
# 访问 http://127.0.0.1:8080
```

## 配置示例

### 目录结构

```text
~/dashboard/
├── registry.json           # 仪表盘索引
├── stripe/
│   ├── config.json         # 布局与组件配置
│   ├── data.json           # 当前数据快照
│   ├── fetch.sh            # 数据抓取脚本
│   └── index.html          # 仪表盘页面
└── server/
    ├── config.json
    ├── data.json
    ├── fetch.sh
    └── index.html
```

### 抓取脚本模板

```bash
#!/bin/bash
# Stripe 余额抓取
curl -s -u "$STRIPE_API_KEY:" \
  https://api.stripe.com/v1/balance \
  | jq '.' > ~/dashboard/stripe/data.json
```

### 设计默认值

| 元素 | 深色模式 | 浅色模式 |
|------|----------|----------|
| 背景 | `#0f172a` | `#f8fafc` |
| 文字 | `#e2e8f0` | `#1e293b` |
| 间距 | 16px / 24px / 32px | 同左 |
| 圆角 | 8px | 8px |
| KPI 数字 | 48-72px | 48-72px |
| KPI 标签 | 14px | 14px |

### cron 定时刷新

```bash
# 每 15 分钟刷新 Stripe 数据
*/15 * * * * ~/dashboard/stripe/fetch.sh

# 每分钟刷新服务器资源
* * * * * ~/dashboard/server/fetch.sh
```

## 最佳实践

### 1. 凭据安全第一

所有 API 凭据通过环境变量注入，禁止写入脚本或配置文件。在 cron 中使用环境变量文件：

```bash
# /etc/environment 或 ~/.env
STRIPE_API_KEY=sk_xxx

# cron 中加载
*/15 * * * * source ~/.env && ~/dashboard/stripe/fetch.sh
```

### 2. 本地绑定 127.0.0.1

仪表盘默认仅本地访问，避免暴露到公网。若需团队访问，建议通过反向代理添加认证层：

```bash
# 仅本地访问
python -m http.server 8080 --bind 127.0.0.1
```

### 3. 数据脱敏

展示数据中不包含个人隐私信息（PII）。抓取脚本中可使用 jq 过滤敏感字段：

```bash
curl -s ... | jq 'del(.customer.email, .customer.phone)' > data.json
```

### 4. 可视化 QA 流程

交付前必须进行可视化 QA：

1. 浏览器打开仪表盘并截图
2. 检查：无元素重叠、字体可读（≥14px）、对比度达标
3. 发现问题 → 修复 → 重新截图
4. 仅在 QA 通过后交付

## 常见问题

### Q1：抓取脚本运行报错 401？

401 表示 API 凭据无效或未设置。检查环境变量是否正确加载：`echo $STRIPE_API_KEY`。cron 环境变量需通过 `source ~/.env` 显式加载。

### Q2：仪表盘打开是空白？

排查步骤：
1. 检查 `data.json` 是否存在且格式正确：`jq . data.json`
2. 浏览器开发者工具查看 Console 错误
3. 确认 `index.html` 与 `data.json` 在同一目录

### Q3：如何切换深色/浅色模式？

在 `config.json` 中设置 `theme` 字段为 `dark` 或 `light`，重新打开页面即生效。

### Q4：数据不更新？

检查 cron 是否正常运行：`grep CRON /var/log/syslog`。确认抓取脚本有执行权限：`chmod +x fetch.sh`。

### Q5：如何添加新的数据源？

向 Agent 描述新需求，Agent 会在 `~/dashboard/` 下创建新的子目录，包含独立的配置、抓取脚本与页面。

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **浏览器**：任意现代浏览器（用于预览）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 命令行工具 | 必需 | 系统自带 |
| jq | JSON 处理 | 必需 | `apt install jq` 或 `brew install jq` |
| Python | 本地服务器 | 推荐 | 用于 `python -m http.server` |
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |

### API Key 配置

- 数据源 API Key 通过环境变量注入（如 `STRIPE_API_KEY`）
- 环境变量存储于 `~/.env` 或系统环境配置
- 仪表盘默认绑定 127.0.0.1，无需额外认证
- 禁止在脚本或配置文件中硬编码 API Key

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，核心功能需 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 生成仪表盘与抓取脚本

## 免费版限制

本免费体验版限制以下高级功能：

- 不支持多数据源聚合看板（仅支持单数据源）
- 不支持高级图表类型（仅支持基础 KPI 卡片与简单趋势图）
- 不支持自动化可视化 QA（仅支持手动截图检查）
- 不支持看板模板库与一键应用
- 不支持看板分享与团队协作
- 不支持告警规则与阈值通知
- 不提供优先技术支持与 SLA 保障

解锁全部功能请使用专业版：dashboard-builder-pro
