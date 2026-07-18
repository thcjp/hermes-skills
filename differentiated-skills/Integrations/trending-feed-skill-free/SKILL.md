---
slug: trending-feed-skill-free
name: trending-feed-skill-free
version: "1.0.0"
displayName: 热榜订阅(免费版)
summary: 获取 GitHub Trending 热门仓库列表，支持语言过滤，返回结构化 JSON 数据。
license: MIT
edition: free
description: |-
  获取 GitHub Trending 热门仓库列表，支持语言过滤，返回结构化 JSON 数据。

  核心能力：
  - 抓取 GitHub Trending 页面并解析仓库元信息
  - 调用 GitHub REST API 补全描述、星标数、主语言
  - 支持按编程语言过滤，返回结构化 JSON
  - 适配飞书、Discord、Telegram 等多平台消息格式

  适用场景：
  - 每日技术动态聚合与推送
  - 关注特定语言生态的流行项目
  - 团队周会技术分享素材准备
  - 个人开发者发现新工具与框架

  差异化：采用结构化输出与多平台格式化模板，配合本地缓存降低 API 速率限制影响，针对免费用户提供核心能力与可扩展的接入点。

  触发关键词：github trending、热榜、热门仓库、trending、每日热门
tags:
- 集成工具
- 数据聚合
- 开发者效率
tools:
- read
- exec
---

# 热榜订阅（免费版）

## 概述

本 Skill 帮助 Agent 快速获取 GitHub Trending 热门仓库列表，并通过 GitHub REST API 补全仓库详情，最终输出结构化 JSON。免费版聚焦"每日浏览一次、了解技术风向"的核心场景，提供完整的抓取、解析、格式化能力，适合个人开发者与技术爱好者快速试水。

## 核心能力

| 能力 | 说明 | 免费版支持 |
|------|------|-----------|
| 页面抓取 | 抓取 GitHub Trending 默认页面 | 是 |
| 语言过滤 | 按编程语言筛选热门仓库 | 是 |
| 字段补全 | 调用 REST API 补全描述、星标、语言 | 是 |
| 结构化输出 | 统一 JSON 数组结构 | 是 |
| 多平台格式化 | 飞书 / Discord / Telegram / 控制台 | 是 |
| 批量抓取 | 一次抓取多语言、多时间窗 | 否（专业版） |
| 高级缓存 | 多级缓存与命中率统计 | 否（专业版） |
| 定时推送 | 定时抓取并推送到 IM 渠道 | 否（专业版） |

## 使用场景

1. **每日技术晨会素材**：上班前抓取当日热榜，挑选 3-5 个项目在团队晨会分享，保持技术敏感度。
2. **语言生态观察**：长期关注 Python、Rust、Go 等语言，发现新兴框架与工具链演进趋势。
3. **内容创作选题**：技术博主或自媒体从热榜中挖掘选题，撰写趋势分析或项目解读文章。
4. **招聘与团队建设**：技术负责人通过热榜了解候选人所在技术栈的流行度，校准岗位要求。

## 快速开始

> 上手时间：< 60 秒。本 Skill 为纯指令型，无需安装额外依赖。

### 步骤 1：抓取默认热榜

```bash
python3 ~/.skill-platform/workspace/skills/trending-feed/scripts/fetch_trending.py
```

### 步骤 2：按语言过滤

```bash
python3 ~/.skill-platform/workspace/skills/trending-feed/scripts/fetch_trending.py python
python3 ~/.skill-platform/workspace/skills/trending-feed/scripts/fetch_trending.py javascript
python3 ~/.skill-platform/workspace/skills/trending-feed/scripts/fetch_trending.py rust
```

### 步骤 3：查看输出结构

返回 JSON 数组，每个元素结构如下：

```json
{
  "full_name": "owner/repo",
  "description": "仓库一句话描述",
  "language": "Python",
  "stars": 12345,
  "url": "https://github.com/owner/repo"
}
```

### 步骤 4：按平台格式化

获取数据后，由 Agent 根据所在平台格式化输出：

**飞书 / 钉钉**：
```text
GitHub Trending · 今日热榜
1. owner/repo - 描述 ⭐ 12345 | Python
   https://github.com/owner/repo
```

**Discord / Telegram**：
```text
GitHub Trending 今日热榜
1. owner/repo - 描述 ⭐ 12345 | Python | https://github.com/owner/repo
```

**控制台**：
```text
1. owner/repo (⭐ 12345 | Python)
   描述
   https://github.com/owner/repo
```

## 配置示例

### 语言过滤参数

| 参数值 | 含义 | 示例 |
|--------|------|------|
| 不传 | 默认全语言热榜 | `fetch_trending.py` |
| `python` | Python 项目 | `fetch_trending.py python` |
| `javascript` | JavaScript 项目 | `fetch_trending.py javascript` |
| `go` | Go 项目 | `fetch_trending.py go` |
| `rust` | Rust 项目 | `fetch_trending.py rust` |

### 输出条数

- 默认全语言热榜：返回 9 个仓库
- 语言过滤时：返回 10 个仓库
- 免费版暂不支持自定义条数（专业版支持 `--limit` 参数）

## 最佳实践

1. **每日固定时间抓取**：建议在工作日早晨执行一次，避免频繁调用触发 GitHub API 速率限制（未认证 60 次/小时）。
2. **优先使用语言过滤**：关注特定语言时使用语言参数，结果更聚焦，命中率更高。
3. **结合本地缓存复用**：同一日内重复查询时复用上次结果，免费版建议手动缓存到本地文件。
4. **失败时使用 fallback 数据**：脚本在 API 出错时会返回 fallback 数据，请检查日志中的错误标记。
5. **输出前做去重**：同一仓库可能在不同时间窗重复出现，输出前按 `full_name` 去重。

## 常见问题

### Q1：抓取返回空列表怎么办？

A：请检查网络连接与 GitHub 站点可达性。若在公司网络下，可能需要配置代理。可尝试在脚本中设置 `HTTPS_PROXY` 环境变量。

### Q2：API 报 403 速率限制错误怎么办？

A：GitHub 未认证请求限制为 60 次/小时。建议：(1) 降低抓取频率；(2) 使用本地缓存复用结果；(3) 升级到专业版使用 GitHub Token 认证提升到 5000 次/小时。

### Q3：语言过滤后结果不准确？

A：部分仓库未标注主语言，会被过滤掉。建议同时抓取全语言热榜对比，或使用专业版的多语言并集模式。

### Q4：如何在飞书机器人中自动推送？

A：免费版需手动调用脚本并将输出粘贴到机器人。如需定时自动推送，请使用专业版的定时任务能力。

### Q5：为什么默认只返回 9 个仓库？

A：免费版遵循 GitHub Trending 页面默认展示数量，便于快速浏览。专业版支持自定义条数与分页。

### Q6：能否抓取历史热榜？

A：GitHub Trending 仅展示当前时段，不提供历史数据。免费版建议每日抓取后本地存档，形成历史序列。专业版支持定时抓取与增量对比，自动构建历史档案。

### Q7：抓取结果如何持久化？

A：免费版可将 JSON 输出重定向到本地文件，例如 `fetch_trending.py python > trending-$(date +%F).json`，按日期归档便于后续分析。

## 免费版限制

本免费体验版限制以下高级功能：
- 批量抓取多语言、多时间窗（专业版支持）
- 高级缓存策略与命中率统计（专业版支持）
- 定时抓取并自动推送到 IM 渠道（专业版支持）
- 自定义输出模板与字段映射（专业版支持）
- GitHub Token 认证提升速率限制（专业版支持）

解锁全部功能请使用专业版：trending-feed-skill-pro

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（用于运行抓取脚本）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| Python 标准库 | 运行时 | 必需 | Python 自带（urllib / json / re） |
| requests（可选） | Python 包 | 可选 | `pip install requests`，用于更稳定的 HTTP 请求 |
| GitHub REST API | 外部 API | 必需 | 公开 API，未认证 60 次/小时 |

### API Key 配置
- **GitHub Token（可选）**：免费版可不配置；如需提升速率限制，可在环境变量中设置 `GITHUB_TOKEN`，由专业版完整支持
- **本 Skill 基于指令驱动**：除上述可选 Token 外无需额外 API Key

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
