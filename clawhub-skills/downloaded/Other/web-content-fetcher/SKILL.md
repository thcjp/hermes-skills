---
slug: web-content-fetcher
name: web-content-fetcher
version: "1.0.1"
displayName: Web Content Fetcher
summary: 网页内容获取工具 | 当常规爬虫被过滤时，使用替代服务获取网页内容。支持：1) r.jina.ai - 最稳定 2) markdown.new -
  Cloudflare 专用 3) defudd...
license: MIT
description: |-
  网页内容获取工具 | 当常规爬虫被过滤时，使用替代服务获取网页内容。支持：1) r。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Web Content Fetcher

当常规 web_fetch/web_search 无法获取内容时，使用替代服务获取网页 Markdown 格式内容。

## 支持的服务

| 优先级 | 服务 | 用法 | 适用场景 |
| --- | --- | --- | --- |
| 1 | **r.jina.ai** | `https://r.jina.ai/{url}` | 最稳定，通用性强 |
| 2 | **markdown.new** | `https://markdown.new/{url}` | Cloudflare 保护网站 |
| 3 | **defuddle.md** | `https://defuddle.md/{url}` | 备用方案 |

## 使用方法

### 直接调用

当需要获取网页内容时，按顺序尝试：

1. 首先用 `web_fetch` 尝试获取
2. 如果失败或被过滤，调用本工具

```bash
curl -s "https://r.jina.ai/https://example.com"

curl -s "https://markdown.new/https://example.com"

curl -s "https://defuddle.md/https://example.com"
```

### API 格式

```bash
fetch_webpage <url>

fetch_webpage <url> --method jina|markdown|defuddle
```

## 示例

```text
用户: 帮我获取 https://news.example.com/article/123 的内容
助手: (使用 r.jina.ai 获取)
```

## 工具脚本

本目录包含 `fetch.sh` 脚本，可直接调用：

```bash
./fetch.sh https://example.com
./fetch.sh https://example.com jina
```

---

*让网页内容获取不再受限 🌐*

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 网页内容获取工具 | 当常规爬虫被过滤时，使用替代服务获取网页内容
- ai - 最稳定 2) markdown
- new
  - Cloudflare 专用 3) defudd
- 触发关键词: web, fetcher, jina, content, 网页内容获取, 当常规爬虫被, defudd, cloudflare

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Web Content Fetcher？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Web Content Fetcher有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
