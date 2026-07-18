---
slug: hot-news-tool-free
name: hot-news-tool-free
version: "1.0.0"
displayName: 热点新闻聚合
summary: 轻量级新闻聚合工具，自动搜索筛选国内外科技、军事、社会新闻要点，适合个人用户快速了解时事动态。
license: MIT
edition: free
description: |-
  轻量级新闻聚合工具，自动搜索筛选国内外科技、军事、社会新闻要点，适合个人用户快速了解时事动态。

  核心能力:
  - 聚合国内外主流科技、军事、社会新闻源
  - 自动筛选与去重，过滤低质量内容
  - 按类别整理，每条含标题、来源、要点
  - 生成结构化 Markdown 汇总报告

  适用场景:
  - 个人每日新闻速览
  - 科技行业动态跟踪
  - 军事爱好者资讯获取

  差异化:
  - 免费版聚焦核心新闻聚合，覆盖主流源
  - 自动过滤重复与低可信度内容
  - 输出格式清晰，便于快速阅读

  触发关键词: 新闻聚合, 热点新闻, 科技新闻, 军事新闻, 新闻汇总, 今日要闻
tags:
- 新闻
- 信息聚合
- 研究工具
- 资讯
tools:
- read
- exec
---

# 热点新闻聚合（免费版）

## 概述

热点新闻聚合免费版是一款面向个人用户的新闻资讯聚合工具。自动从国内外主流新闻源搜索、筛选、整理科技、军事、社会类新闻要点，按类别生成结构化汇总报告。内置可信度评估规则，优先展示权威来源，帮助用户高效获取有价值的时事信息。

## 核心能力

| 能力 | 说明 | 免费版支持 |
| --- | --- | --- |
| 多源聚合 | 聚合国内外主流新闻源 | 是（10+ 源） |
| 自动筛选 | 过滤重复与低质量内容 | 是 |
| 分类整理 | 按科技/军事/社会分类 | 是 |
| 可信度评估 | 标注来源可信度 | 是 |
| 定时更新 | 定时自动抓取最新新闻 | 否 |
| 自定义源 | 添加自定义新闻源 | 否 |
| 实时推送 | 新闻实时推送通知 | 否 |
| 舆情分析 | 新闻趋势分析 | 否 |

### 免费版限制说明

- 单次聚合最多覆盖 10 个新闻源
- 不支持定时自动更新
- 不支持自定义新闻源
- 不支持实时推送通知
- 不支持舆情趋势分析

## 使用场景

### 场景一：每日科技新闻速览

用户希望每天快速了解科技行业动态。

```bash
# 获取科技类新闻汇总
python scripts/news_aggregator.py --category=tech --max=10
```

预期输出包含 36 氪、机器之心、IT 之家等来源的最新科技新闻，每条含标题、来源、时间、要点摘要。

### 场景二：军事资讯获取

军事爱好者关注最新军事动态。

```bash
# 获取军事类新闻
python scripts/news_aggregator.py --category=military --max=5
```

返回观察者网、澎湃新闻等来源的军事新闻，包含国内外军事动态。

### 场景三：综合新闻浏览

用户希望获取所有类别的新闻概览。

```bash
# 获取所有类别新闻
python scripts/news_aggregator.py --category=all --max=15
```

返回科技、军事、社会三大类别的综合新闻汇总。

## 快速开始

### 安装依赖

```bash
# 安装 Python 依赖
pip install requests beautifulsoup4 markdown

# 验证安装
python scripts/news_aggregator.py --version
```

### 执行首次新闻聚合

```bash
# 获取今日科技新闻
python scripts/news_aggregator.py --category=tech
```

### 查看支持的新闻源

```bash
# 列出所有新闻源
python scripts/news_aggregator.py --list-sources
```

## 配置示例

### 新闻源配置

| 类别 | 来源 | 说明 |
| --- | --- | --- |
| 国内科技 | 36 氪 | 科技创业资讯 |
| 国内科技 | 机器之心 | AI 技术报道 |
| 国内科技 | IT 之家 | 综合科技新闻 |
| 国内军事 | 观察者网 | 军事评论 |
| 国内军事 | 澎湃新闻 | 时事新闻 |
| 国际科技 | TechCrunch | 科技创业 |
| 国际科技 | The Verge | 科技产品 |
| 国际科技 | Wired | 科技文化 |
| 国际军事 | Defense News | 防务新闻 |
| 国际军事 | Military Times | 军事资讯 |

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `--category` | 字符串 | all | 类别 tech/military/social/all |
| `--max` | 整数 | 10 | 每类最多返回条数 |
| `--format` | 字符串 | markdown | 输出格式 |
| `--lang` | 字符串 | zh | 语言偏好 |

## 最佳实践

### 新闻筛选原则

**优先展示：**
- 官方媒体报道
- 权威机构发布
- 一手新闻源

**谨慎对待：**
- 论坛帖子
- 匿名消息
- 二手转载
- 标题党内容

### 输出格式示例

```markdown
## 科技新闻

1. [标题](链接)
   来源：36氪 | 时间：2026-01-15
   要点：核心内容摘要，3-5 句话概括

2. [标题](链接)
   来源：机器之心 | 时间：2026-01-15
   要点：核心内容摘要
```

### 阅读效率优化

1. **先看要点**：摘要包含核心信息
2. **关注来源**：优先阅读权威来源
3. **注意时间**：判断新闻时效性
4. **分类阅读**：按兴趣选择类别

## 常见问题

### 新闻源访问失败

```bash
# 检查网络连通性
python scripts/news_aggregator.py --check-sources

# 切换可用源
python scripts/news_aggregator.py --category=tech --fallback
```

可能原因：
- 网络连接问题
- 新闻源临时不可用
- 被反爬虫机制拦截

### 新闻内容过时

```bash
# 强制刷新缓存
python scripts/news_aggregator.py --category=tech --no-cache

# 指定时间范围
python scripts/news_aggregator.py --category=tech --hours=24
```

### 返回结果为空

```bash
# 检查新闻源状态
python scripts/news_aggregator.py --diagnose

# 尝试其他类别
python scripts/news_aggregator.py --category=social

# 增加抓取深度
python scripts/news_aggregator.py --category=tech --depth=2
```

### 中文乱码

```bash
# 设置编码
export PYTHONIOENCODING=utf-8
python scripts/news_aggregator.py --category=tech

# 或在脚本中指定
python scripts/news_aggregator.py --encoding=utf-8
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python 版本**：3.7 及以上
- **网络环境**：需可访问国内外新闻网站

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
| --- | --- | --- | --- |
| Python 3.7+ | 运行时 | 是 | 系统包管理器安装 |
| requests | HTTP 库 | 是 | `pip install requests` |
| beautifulsoup4 | HTML 解析 | 是 | `pip install beautifulsoup4` |
| markdown | 格式化 | 否（推荐） | `pip install markdown` |
| LLM API | API | 是 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 免费版无需额外 API Key
- 新闻源通过公开网页抓取，无需认证
- 如使用搜索 API 辅助，参考对应服务文档

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **适用人群**：个人用户、新闻爱好者、行业关注者
- **升级建议**：如需定时更新、自定义源、实时推送等高级功能，请使用 PRO 版本
