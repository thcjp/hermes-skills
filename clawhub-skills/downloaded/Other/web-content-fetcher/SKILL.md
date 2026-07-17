---
slug: web-content-fetcher
name: web-content-fetcher
version: "1.0.1"
displayName: Web Content Fetcher
summary: 网页内容获取工具 | 当常规爬虫被过滤时，使用替代服务获取网页内容。支持：1) r.jina.ai - 最稳定 2) markdown.new -
  Cloudflare 专用 3) defudd...
license: MIT
description: |-
  网页内容获取工具 | 当常规爬虫被过滤时，使用替代服务获取网页内容。支持：1) r.jina.ai - 最稳定 2) markdown.new
  - Cloudflare 专用 3) defudd...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: web, fetcher, jina, content, 网页内容获取, 当常规爬虫被, defudd, cloudflare
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
