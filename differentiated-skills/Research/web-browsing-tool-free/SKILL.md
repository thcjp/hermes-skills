---
slug: web-browsing-tool-free
name: web-browsing-tool-free
version: "1.0.0"
displayName: 网页浏览助手免费版
summary: 浏览和总结网站内容,从 URL 提取信息,搜索网络获取实时资讯,适合个人日常使用
license: MIT
edition: free
description: |-
  网页浏览助手免费版,面向个人用户提供基础的网页浏览和信息提取能力。
  支持网站访问、内容总结、URL 内容提取、网络搜索等核心功能。

  核心能力:
  - 直接访问指定 URL,获取网页内容
  - 网页内容智能总结,快速把握要点
  - 网络搜索,获取实时信息
  - 结构化数据提取,从网页中提取特定信息
  - 多种输出格式(摘要、详细分析、特定数据)

  适用场景:
  - 个人用户获取网页信息
  - 学生与研究者收集资料
  - 自媒体创作者获取素材
  - 快速了解网页内容

  差异化:
  - 免费版聚焦个人日常浏览场景,功能精炼实用
  - 移除外部平台依赖,纯净调用
  - 增强中文触发关键词,提升中文环境识别率
  - 完全适配 SkillHub 平台规范

  触发关键词: 网页浏览, 内容总结, URL 提取, 网络搜索, 资讯获取, web browsing, summarize, extract content, web search
tags:
- 研究工具
- 网页浏览
- 信息获取
tools:
- read
- exec
---

# 网页浏览助手免费版

## 概述

网页浏览助手免费版是一款面向个人用户的网页信息获取工具。它能够访问指定的网站、总结网页内容、从 URL 中提取结构化信息,并支持网络搜索获取实时资讯,让 AI 成为您的智能网页浏览助手。

本工具特别适合个人用户日常的网页信息获取需求,例如查看网站内容、了解最新资讯、收集研究资料等。免费版聚焦核心浏览和提取功能,无需注册,开箱即用。

## 核心能力

### 1. 直接 URL 访问

访问指定 URL,获取网页主要内容。

```bash
# 访问指定网页
web-browsing fetch "https://example.com"

# 获取网页内容并总结
web-browsing fetch "https://news.example.com" --summarize

# 获取特定格式的输出
web-browsing fetch "https://docs.example.com" --format markdown
```

### 2. 网页内容智能总结

自动提取网页主要内容并生成摘要。

```bash
# 总结网页内容
web-browsing summarize "https://long-article.example.com"

# 指定总结长度
web-browsing summarize "https://article.example.com" --length short
web-browsing summarize "https://article.example.com" --length detailed
```

### 3. 网络搜索

搜索网络获取实时信息。

```bash
# 基础搜索
web-browsing search "最新人工智能研究进展"

# 搜索并总结
web-browsing search "气候变化最新报告" --summarize

# 指定搜索结果数量
web-browsing search "React 教程" --limit 5
```

### 4. 结构化数据提取

从网页中提取特定的结构化数据。

```bash
# 提取特定数据
web-browsing extract "https://product.example.com" --fields "name,price,rating"

# 提取表格数据
web-browsing extract "https://data.example.com" --selector "table" --format csv

# 提取列表数据
web-browsing extract "https://list.example.com" --selector ".item" --format json
```

## 使用场景

### 场景一:个人用户获取网页信息

小王想快速了解某个网站的内容,无需逐页浏览。

```bash
# 步骤1:访问网站并获取内容
web-browsing fetch "https://target-website.com"

# 步骤2:总结网站主要内容
web-browsing summarize "https://target-website.com"

# 步骤3:提取特定信息
web-browsing extract "https://target-website.com" --fields "title,author,date"
```

### 场景二:学生收集研究资料

小李是学生,需要从多个网站收集特定主题的资料。

```bash
# 步骤1:搜索相关内容
web-browsing search "深度学习优化算法" --limit 10

# 步骤2:访问搜索结果中的网页
web-browsing fetch "https://result1.example.com" --summarize
web-browsing fetch "https://result2.example.com" --summarize

# 步骤3:提取结构化数据
web-browsing extract "https://paper.example.com" --fields "title,abstract,authors"
```

### 场景三:快速了解新闻资讯

小张想快速了解今天的科技新闻。

```bash
# 步骤1:搜索最新科技新闻
web-browsing search "今日科技新闻" --freshness today

# 步骤2:访问新闻网站
web-browsing fetch "https://tech-news.example.com"

# 步骤3:总结新闻要点
web-browsing summarize "https://tech-news.example.com" --length short
```

## 快速开始

### 第一步:查看可用命令

```bash
# 查看所有命令
web-browsing help

# 查看特定命令用法
web-browsing fetch --help
web-browsing search --help
```

### 第二步:执行首次访问

```bash
# 访问简单网页
web-browsing fetch "https://example.com"

# 总结网页内容
web-browsing summarize "https://example.com"
```

### 第三步:执行首次搜索

```bash
# 搜索网络
web-browsing search "人工智能最新进展"

# 搜索并总结
web-browsing search "人工智能最新进展" --summarize --limit 3
```

## 配置示例

### 个人偏好配置

```bash
# config.json - 个人浏览偏好
{
  "fetch": {
    "timeout": 30,
    "user_agent": "Mozilla/5.0",
    "follow_redirects": true
  },
  "summarize": {
    "default_length": "medium",
    "language": "zh"
  },
  "search": {
    "default_limit": 5,
    "language": "zh-CN",
    "safe_search": true
  }
}
```

### 搜索配置

```bash
# 配置搜索引擎偏好
web-browsing config set-search \
  --engine "default" \
  --language "zh-CN" \
  --safe-search true \
  --default-limit 5
```

## 最佳实践

### 1. 明确获取目标

```bash
# 正确做法:明确说明需要什么
web-browsing fetch "https://example.com" --fields "title,price,availability"

# 错误做法:目标不明确
web-browsing fetch "https://example.com"  # 不知道需要什么内容
```

### 2. 善用总结功能

```bash
# 长文章用总结
web-browsing summarize "https://long-article.example.com" --length short

# 需要详情时直接获取
web-browsing fetch "https://article.example.com" --format markdown
```

### 3. 合理使用搜索过滤

```bash
# 搜索时限定时间范围
web-browsing search "最新新闻" --freshness today
web-browsing search "本周热点" --freshness week

# 限定语言
web-browsing search "AI research" --language en
web-browsing search "人工智能研究" --language zh
```

### 4. 批量处理多个 URL

```bash
# 批量获取多个网页
for url in "url1" "url2" "url3"; do
  echo "=== $url ==="
  web-browsing summarize "$url"
done
```

## 常见问题

### Q1: 无法访问某些网站怎么办?

**A:** 部分网站可能阻止自动化访问。建议:

1. 尝试不同的 User-Agent
2. 检查网站是否需要登录
3. 使用网络搜索替代直接访问

### Q2: 内容提取不完整?

**A:** 可能原因和解决方案:

1. 网站使用 JavaScript 动态加载内容 -> 尝试使用浏览器自动化工具
2. 内容需要登录才能查看 -> 提供登录态或使用真实浏览器控制工具
3. 选择器不正确 -> 检查网页结构,调整选择器

### Q3: 搜索结果质量不高?

**A:** 优化搜索:

1. 使用更具体的关键词
2. 添加引号搜索精确短语:web-browsing search '"深度学习优化"'
3. 限定语言和地区

### Q4: 支持哪些输出格式?

**A:** 免费版支持多种输出格式:

- text:纯文本
- markdown:Markdown 格式
- json:JSON 结构化数据
- csv:CSV 表格格式

### Q5: 免费版有哪些限制?

**A:** 免费版主要面向个人日常浏览场景,具备完整的网页访问和搜索能力。如需批量处理、定时监控、深度分析、团队协作等高级功能,请考虑升级到 PRO 版本。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需要可访问互联网

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | HTTP 工具 | 必需 | 系统自带 |
| web_search | 搜索工具 | 必需 | Agent 内置或外部搜索 API |
| web_fetch | 网页抓取 | 必需 | Agent 内置或外部抓取工具 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

免费版使用 Agent 内置工具,无需额外 API Key。部分高级搜索功能可能需要搜索引擎 API Key。

```bash
# 可选:配置搜索引擎 API(提升搜索质量)
SEARCH_API_KEY=your_search_api_key
```

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,通过 exec 执行 HTTP 请求和网页抓取)
- **说明**: 基于网页浏览的信息获取工具,通过自然语言指令驱动 Agent 访问网页和搜索信息
- **适用规模**: 个人用户、单次查询、本地运行
