---
slug: knowledge-agent-tool-free
name: knowledge-agent-tool-free
version: "1.0.0"
displayName: 知识管理工具-免费版
summary: 基于文件的知识捕获与检索工具,支持URL、视频、文章、社交内容收藏与搜索
license: MIT
edition: free
description: |-
  基于文件的知识组织工具,实现快速捕获、后续检索与自动整理。
  支持 URL 收藏、视频/文章/论文摘要、社交帖子与研究笔记管理。

  核心能力:
  - 多类型知识捕获(URL/视频/文章/帖子/研究)
  - 基于标签与全文的检索
  - 自动维护索引与整理
  - Markdown 文件存储,易于迁移

  适用场景:
  - 个人知识库构建
  - 研究资料收集与整理
  - 独立开发者的信息管理

  差异化:免费版提供核心知识捕获与检索能力,适合个人用户构建轻量知识库。

  触发关键词: 知识管理, 知识库, 收藏, 检索, 笔记, know, 标签管理
tags:
- 研究工具
- 知识管理
- 信息收集
tools:
- read
- exec
---

# 知识管理工具(免费版)

## 概述

本工具是基于文件的知识组织工具,实现"快速捕获、后续检索、自动整理"的工作流。用户可将 URL、视频、文章、论文、社交帖子与研究笔记快速保存到本地知识库,通过标签与全文检索随时找回。免费版面向个人用户,提供核心的捕获、检索与整理能力。

### 与其他工具的定位差异

| 工具 | 定位 | 与本工具的区别 |
|:-----|:-----|:--------------|
| 本工具 | 保存外部内容为知识条目 | 捕获完整内容,带标签与摘要 |
| 书签管理 | 仅保存 URL | 本工具保存完整内容与元数据 |
| 笔记应用 | 演进式笔记 | 本工具保存原始素材快照 |
| 记忆系统 | Agent 上下文记忆 | 本工具是持久化知识库 |

## 核心能力

### 命令总览

| 命令 | 说明 | 示例 |
|:-----|:-----|:-----|
| `know add url` | 收藏 URL | `know add url <url> --title "..." --tags "a,b"` |
| `know add video` | 收藏视频 | `know add video <url> --title "..." --tags "a,b"` |
| `know add extract` | 添加摘要 | `know add extract --source <url> --type article` |
| `know add post` | 添加帖子 | `know add post --source <url> --title "..."` |
| `know add research` | 添加研究 | `know add research --title "..." --tags "a,b"` |
| `know search` | 搜索 | `know search "query"` |
| `know recent` | 最近条目 | `know recent --limit 10` |
| `know list` | 按标签列出 | `know list --tags security` |
| `know tidy` | 整理 | `know tidy --fix` |
| `know validate` | 校验 | `know validate` |
| `know reindex` | 重建索引 | `know reindex` |

## 使用场景

### 场景一:快速收藏 URL

浏览时发现有用的网页,快速收藏并打标签。

```bash
# 收藏一个 URL,附带标题、标签与摘要
know add url https://example.com/article \
  --title "AI 智能体入门指南" \
  --tags "ai,agent,tutorial" \
  --summary "介绍 AI 智能体的基础概念与开发流程"

# 收藏一个视频
know add video https://example.com/video \
  --title "Python 异步编程教程" \
  --tags "python,async,tutorial" \
  --summary "讲解 asyncio 与 async/await 的使用"
```

### 场景二:检索历史知识

需要找回之前保存的内容,按关键词或标签检索。

```bash
# 全文搜索
know search "智能体"

# 按标签筛选
know list --tags ai,agent

# 查看最近条目
know recent --limit 10
```

### 场景三:添加研究笔记

将研究过程中产生的内容保存为知识条目。

```bash
know add research \
  --title "2026 年 AI 智能体市场调研" \
  --tags "research,ai,market" \
  --summary "调研 2026 年 AI 智能体市场规模、主要玩家与趋势"
```

## 快速开始

### 1. 存储位置

默认存储路径:`~/.knowledge-base/`(可通过环境变量 `KNOWLEDGE_DIR` 配置)。

```text
knowledge/
├── INDEX.md      # 自动维护的浏览索引
├── urls/         # 收藏的 URL
├── extracts/     # 视频/文章/论文摘要
├── posts/        # 社交内容(推文/帖子)
└── research/     # 研究笔记
```

### 2. 添加内容

```bash
# 收藏 URL
know add url <url> --title "标题" --tags "标签1,标签2" --summary "摘要"

# 添加文章摘要
know add extract --source <url> --type article --title "标题" --tags "标签"

# 添加研究笔记
know add research --title "标题" --tags "标签" --summary "摘要"
```

每次 `add` 操作都会:
1. 生成一个带 YAML frontmatter 的 Markdown 文件
2. 自动更新 `INDEX.md` 索引

### 3. 检索与浏览

```bash
# 全文搜索
know search "查询关键词"

# 查看最近条目
know recent --limit 10

# 按标签筛选
know list --tags security,ai
```

## 配置示例

### 数据模型(frontmatter)

每个知识条目以 Markdown 文件存储,带 YAML frontmatter:

```yaml
---
type: url                    # 类型: url|extract|post|research
title: "条目标题"
source_url: "https://..."
source_kind: url             # 来源类型: url|video|article|paper|post|research
tags: ["标签1", "标签2"]
added: "2026-02-26"
added_by: "agent-name"
summary: "一行摘要"
---

## 正文内容
...
```

### 配置文件

```bash
# ~/.config/know/config
KNOWLEDGE_DIR=~/.knowledge-base
DEFAULT_TAGS=personal
INDEX_FORMAT=markdown
```

### 索引文件(INDEX.md)

```markdown
# 知识库索引

## 最近添加
- [AI 智能体入门指南](urls/2026-02-26-ai-agent-guide.md) - ai,agent,tutorial
- [Python 异步编程](extracts/2026-02-26-python-async.md) - python,async

## 按标签
### #ai
- [AI 智能体入门指南](urls/2026-02-26-ai-agent-guide.md)
- [AI 市场调研](research/2026-02-26-ai-market.md)

### #python
- [Python 异步编程](extracts/2026-02-26-python-async.md)
```

## 最佳实践

### 知识捕获纪律
1. **有用就立即保存**:发现可能有用的内容,立即 `know add`,不要只留在记忆里。
2. **每条必带标签与摘要**:标签便于检索,摘要便于快速判断相关性。
3. **不要只存链接**:尽量提取完整内容或摘要,避免链接失效后无法找回。
4. **定期整理**:运行 `know tidy --fix` 规范化标签与文件位置。

### 检索技巧
1. **用语义搜索**:不必记忆精确关键词,用概念性查询即可。
2. **组合标签筛选**:`know list --tags ai,agent` 交集筛选。
3. **按时间浏览**:`know recent --limit 20` 查看最近添加。
4. **定期回顾**:每周浏览索引,重新发现有用内容。

### 维护规范
1. **自动整理**:将 `know tidy --fix` 加入定时任务,定期执行。
2. **校验完整性**:`know validate` 检查 frontmatter 规范。
3. **重建索引**:大量变更后 `know reindex` 重建索引。
4. **查看配置**:`know config` 确认当前配置路径。

## 常见问题

### Q1: 如何备份知识库?
知识库是纯 Markdown 文件,直接备份目录即可:
```bash
# 备份到云盘或版本控制
cp -r ~/.knowledge-base/ /backup/knowledge-$(date +%Y%m%d)/
# 或纳入 Git 管理
cd ~/.knowledge-base && git add . && git commit -m "知识库更新"
```

### Q2: 标签如何规范化?
运行 `know tidy --fix` 自动规范化标签(统一小写、去重、合并同义词)。

### Q3: 搜索结果太多怎么办?
- 增加标签筛选:`know list --tags specific-tag`
- 使用更精确的查询词
- 按时间范围缩小:`know recent --limit 5`

### Q4: 免费版的限制?
免费版提供核心知识捕获与检索能力,适合个人用户。如需团队共享、全文语义检索、自动摘要生成、知识图谱等高阶能力,请升级至专业版。

### Q5: 如何迁移到其他工具?
知识库是标准 Markdown 文件,可直接导入 Obsidian、Notion、Logseq 等支持 Markdown 的工具。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: Bash / Zsh(用于运行 `know` 脚本)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| know | CLI 脚本 | 必需 | 随 Skill 安装 |
| grep | 系统工具 | 必需 | 系统自带(用于全文搜索) |
| Markdown 编辑器 | 可选 | 可选 | Obsidian / VS Code 等 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本 Skill 基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
