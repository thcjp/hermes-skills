---
slug: github-trending-feed
name: github-trending-feed
version: "1.0.0"
displayName: GitHub Trending Feed
summary: 获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用。支持可选语言过滤，返回结构化 J...
license: MIT-0
description: |-
  获取 GitHub Trending 热门仓库列表。当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---

# GitHub Trending Feed

## 工作流程

1. **抓取 Trending 页面**：获取 GitHub 热门仓库列表
2. **获取仓库详情**：对每个仓库调用 GitHub REST API 获取 description、stars、language
3. **返回 JSON**：agent 自行格式化为目标平台的消息

## 使用方法

### 基础用法

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py
```

### 语言过滤

```bash
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py python
python3 ~/.skill-platform/workspace/skills/github-trending/scripts/fetch_trending.py javascript
```

### 输出格式

返回 JSON 数组，每个元素：

```json
{
  "full_name": "owner/repo",
  "description": "仓库描述",
  "language": "Python",
  "stars": 12345,
  "url": "https://github.com/owner/repo"
}
```

### Agent 使用建议

获取数据后，根据所在平台格式化输出：

**飞书**：

```text
📊 **GitHub Trending · 今日热榜**
🔥 1. owner/repo - 描述 ⭐ 12345 | Python 🔗 https://github.com/owner/repo
```

**Discord/Telegram**：

```text
📊 GitHub Trending 今日热榜
1. owner/repo - 描述 ⭐ 12345 | Python | https://github.com/owner/repo
```

**控制台**：

```text
1. owner/repo (⭐ 12345 | Python)
   描述
   https://github.com/owner/repo
```

## 注意事项

* GitHub API 有速率限制，高频使用建议配合缓存
* 脚本自动处理 API 错误，失败时会返回 fallback 数据
* 默认返回 9 个仓库，语言过滤时返回 10 个

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

- 获取 GitHub Trending 热门仓库列表
- 当用户要求查看 GitHub 热榜、每日 GitHub trending、推送 GitHub
  热门项目时使用
- 支持可选语言过滤，返回结构化 J
- 触发关键词: 当用户要求查, github, feed, trending, 热门仓库列表, 热榜, 获取, 每日

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
1. **抓取 Trending 页面**：获取 GitHub 热门仓库列表
2. **获取仓库详情**：对每个仓库调用 GitHub REST API 获取 description、stars、language
3. **返回 JSON**：agent 自行格式化为目标平台的消息
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用GitHub Trending Feed？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: GitHub Trending Feed有什么限制？
A: 请参考已知限制章节了解具体限制。
