---
slug: web-content-fetcher-tool-pro
name: web-content-fetcher-tool-pro
version: "1.0.0"
displayName: 网页内容获取专业版
summary: 批量获取、本地缓存、内容解析与质量评分，适合数据团队与内容聚合场景。
license: MIT
edition: pro
description: |-
  网页内容获取工具专业版，面向数据团队与内容聚合的高阶网页抓取平台。

  核心能力:
  - 批量 URL 获取与并发控制
  - 本地缓存与去重
  - 内容解析与正文提取
  - 质量评分与自动重试
  - 自定义请求头与认证支持

  适用场景:
  - 数据团队的批量内容采集
  - 内容聚合平台的定期抓取
  - 竞品监测与价格追踪

  差异化: 专业版在免费版核心获取能力之上扩展批量与缓存，新增内容解析、质量评分、认证支持等企业级能力，并与免费版服务优先级兼容。

  触发关键词: 网页抓取, 批量获取, 本地缓存, 内容解析, 质量评分, 内容聚合, 竞品监测, 认证支持
tags:
- 网页抓取
- 批量采集
- 内容聚合
- 专业版
tools:
- read
- exec
---

# 网页内容获取工具（专业版）

## 概述

专业版在免费版的三服务降级获取之上，扩展为面向数据团队与内容聚合的完整网页抓取平台。新增批量获取、本地缓存、内容解析、质量评分与认证支持，同时与免费版的服务优先级保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 获取模式 | 单 URL | 单 URL + 批量 + 定时 |
| 缓存 | 不支持 | 本地缓存 + 去重 |
| 内容解析 | 原始 Markdown | 正文提取 + 元数据 |
| 质量评分 | 不支持 | 自动评分 + 重试 |
| 认证 | 不支持 | 自定义请求头 + Cookie |
| 并发控制 | 不支持 | 可配置并发数 |
| 监控 | 不支持 | 抓取统计 + 失败告警 |
| 报告 | 不支持 | 抓取报告 + 导出 |

## 使用场景

### 场景一：批量内容采集

数据团队需要批量采集多个 URL 的内容。

```bash
# 批量获取
web-fetcher-pro batch fetch \
  --file urls.txt \
  --output ./content/ \
  --concurrent 5 \
  --format markdown \
  --cache

# urls.txt 示例
# https://example.com/article/1
# https://example.com/article/2
# https://example.com/article/3

# 输出
# 📊 批量获取报告
# 总 URL: 50
# 成功: 45
# 失败: 3（已记录至 failed.log）
# 缓存命中: 2（跳过重复获取）
# ⏱️ 耗时: 32.5s
```

### 场景二：正文提取与元数据

获取网页时自动提取正文与元数据。

```bash
# 获取并解析正文
web-fetcher-pro fetch \
  --url "https://example.com/article" \
  --extract-body \
  --extract-metadata \
  --output ./article.md

# 输出元数据
# 📄 元数据
# 标题: 文章标题
# 作者: 作者名
# 发布时间: 2026-07-15
# 描述: 文章摘要
# 关键词: 关键词1, 关键词2
# 正文长度: 3,256 字
# 质量评分: 87/100
```

### 场景三：定时内容监测

定期监测竞品网站的内容变化。

```bash
# 设置定时监测
web-fetcher-pro monitor add \
  --name "竞品监测" \
  --urls "https://competitor.com/blog,https://competitor.com/pricing" \
  --schedule "0 9 * * *" \
  --diff \
  --notify webhook

# 每日 9 点检查指定页面，内容变化时通知
# 输出
# 📊 竞品监测报告
# 监测页面: 2
# 内容变化: 1
#   - https://competitor.com/pricing: 价格更新
#     新增: 企业版套餐 ¥999/月
#     移除: 团队版套餐 ¥299/月
```

## 快速开始

```bash
# 1. 初始化专业版工作区
web-fetcher-pro init --workspace ~/web-fetcher-pro

# 2. 单 URL 获取（兼容免费版）
web-fetcher-pro fetch --url "https://example.com" --format markdown

# 3. 批量获取
web-fetcher-pro batch fetch --file urls.txt --output ./content/ --concurrent 5

# 4. 正文提取
web-fetcher-pro fetch --url "https://example.com/article" --extract-body --extract-metadata

# 5. 设置定时监测
web-fetcher-pro monitor add --name "监测" --urls "url1,url2" --schedule "0 9 * * *"

# 6. 生成报告
web-fetcher-pro report generate --format markdown --output fetch-report.md
```

## 配置示例

```yaml
# ~/web-fetcher-pro/config.yaml
edition: pro
services:
  priority: [jina, markdown, defuddle]
  timeout: 30
  retry: 2
batch:
  max_concurrent: 5
  retry_failed: true
  output_format: markdown
cache:
  enabled: true
  path: ~/web-fetcher-pro/cache/
  ttl: 86400
  deduplicate: true
extract:
  body: true
  metadata: true
  remove_nav: true
  remove_ads: true
quality:
  scoring: true
  min_score: 60
  auto_retry_below: 50
auth:
  default_headers:
    User-Agent: "WebFetcherPro/1.0"
  cookies:
    enabled: false
    path: ~/web-fetcher-pro/cookies/
monitor:
  enabled: true
  diff: true
  notify:
    - console
    - webhook
report:
  formats: [markdown, json, csv]
  include_stats: true
```

## 质量评分维度

| 维度 | 权重 | 说明 |
|:-----|:-----|:-----|
| 正文完整性 | 30% | 正文是否完整提取 |
| 格式质量 | 20% | Markdown 格式是否规范 |
| 元数据完整 | 20% | 标题、作者、时间是否提取 |
| 噪音去除 | 15% | 导航、广告是否清理 |
| 编码正确 | 15% | 中文等字符是否正确显示 |

## 最佳实践

* 批量获取时控制并发数（建议 5），避免被限流。
* 启用缓存，避免重复获取相同 URL。
* 正文提取启用 `--extract-body`，去除导航与广告噪音。
* 质量评分低于 60 的内容建议人工 review。
* 定时监测设置在低峰时段，避免影响目标站点。
* 认证场景使用 Cookie，避免明文存储密码。
* 频繁请求的目标站点建议设置间隔（1-2 秒）。
* 失败的 URL 记录日志，便于后续重试。

## 常见问题

**Q：专业版与免费版的服务优先级兼容吗？**
A：兼容。免费版的 jina → markdown → defuddle 优先级在专业版中默认使用，专业版额外支持自定义优先级。

**Q：批量获取有 URL 数量上限吗？**
A：无硬性上限，建议单批不超过 500 个 URL。可通过 `--concurrent` 控制并发。

**Q：缓存数据存储在哪里？**
A：所有缓存数据存储在本地 `~/web-fetcher-pro/cache` 目录，默认 TTL 24 小时。

**Q：正文提取的准确率如何？**
A：对常规文章页面准确率约 90%+。复杂布局或动态内容可能需要人工 review。

**Q：支持需要登录的页面吗？**
A：支持。通过配置 Cookie 或自定义请求头实现认证。Cookie 文件需手动维护。

**Q：定时监测需要额外的服务吗？**
A：需要系统支持 cron 调度（Linux/macOS 自带，Windows 需使用任务计划程序）。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（批量与缓存功能需要）
- **网络**: 可访问 jina.ai、markdown.new、defuddle.md

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方站点下载 |
| curl | 工具 | 可选 | 系统自带 |
| r.jina.ai | 服务 | 必需 | 公共服务，免费 |
| cron | 调度器 | 可选 | 系统自带 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）
- 认证场景需配置 Cookie 或自定义请求头
- 告警通知若使用 Webhook，需配置 Webhook URL

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 脚本执行 + cron调度）
- **说明**: 专业版在 Markdown 指令基础上，提供批量获取、缓存、解析与监测能力
