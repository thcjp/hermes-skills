---
slug: gitcrawl-tool-free
name: gitcrawl-tool-free
version: "1.0.0"
displayName: 仓库归档搜索
summary: 轻量级代码仓库 issue/PR 归档搜索工具，支持本地缓存查询与新鲜度检测，适合个人开发者日常代码仓库管理。
license: MIT
edition: free
description: |-
  轻量级代码仓库 issue/PR 归档搜索工具，支持本地缓存查询与新鲜度检测，适合个人开发者日常代码仓库管理。

  核心能力:
  - 本地缓存 GitHub issue/PR 归档数据
  - 检测归档数据新鲜度，提示更新需求
  - 按关键词搜索 issue 和 PR
  - 查看相邻 issue 关联关系

  适用场景:
  - 个人开发者查询项目历史 issue
  - 开源项目贡献者了解 PR 状态
  - 技术调研与代码考古

  差异化:
  - 免费版聚焦单仓库查询，操作简单
  - 优先使用本地缓存，减少 API 调用
  - 支持基础搜索与关联查询

  触发关键词: 仓库搜索, issue查询, PR搜索, 代码归档, gitcrawl, 仓库归档
tags:
- 开发工具
- 代码仓库
- issue管理
- PR查询
tools:
- read
- exec
---

# 仓库归档搜索（免费版）

## 概述

仓库归档搜索免费版是一款面向个人开发者的代码仓库 issue/PR 查询工具。通过本地缓存归档数据，优先使用缓存查询而非实时拉取，减少 GitHub API 调用次数。支持按关键词搜索、查看相邻关联、检测数据新鲜度等核心功能，帮助开发者快速了解项目历史与当前状态。

## 核心能力

| 能力 | 说明 | 免费版支持 |
| --- | --- | --- |
| 本地归档缓存 | 缓存 issue/PR 数据到本地 | 是 |
| 新鲜度检测 | 检测缓存是否需要更新 | 是 |
| 关键词搜索 | 按关键词搜索 issue 和 PR | 是 |
| 相邻查询 | 查看 issue 的关联讨论 | 是 |
| 重复聚类 | 识别重复或相似的 issue | 否 |
| 多仓库管理 | 同时管理多个仓库 | 否 |
| 实时同步 | 自动定时同步归档数据 | 否 |
| 团队协作 | 多人共享归档数据 | 否 |

### 免费版限制说明

- 单次仅支持查询 1 个仓库
- 归档数据需手动更新同步
- 不支持重复 issue 聚类分析
- 不支持多仓库批量管理
- 不支持团队协作共享

## 使用场景

### 场景一：查询项目历史 issue

开发者想了解某个开源项目的特定问题历史。

```bash
# 检查归档数据新鲜度
gitcrawl doctor --json

# 搜索包含特定关键词的 issue
gitcrawl search issues "memory leak" \
  -R owner/repo \
  --state all \
  --json number,title,url
```

预期输出包含所有匹配的 issue 编号、标题和链接，帮助快速定位相关讨论。

### 场景二：查看 PR 状态

贡献者想了解某个 PR 的当前状态和关联信息。

```bash
# 查看 PR 基本信息
gitcrawl gh pr status 123 \
  -R owner/repo \
  --compact

# 查看 PR 详细信息
gitcrawl gh pr view 123 \
  -R owner/repo \
  --json number,title,state,url,isDraft,headRef,headSha
```

### 场景三：了解 issue 关联讨论

开发者想查看某个 issue 周边的相关讨论。

```bash
# 查看相邻 issue
gitcrawl neighbors owner/repo \
  --number 456 \
  --limit 12 \
  --json
```

返回与指定 issue 相邻的 12 条讨论，帮助理解上下文。

## 快速开始

### 安装与初始化

```bash
# 安装 gitcrawl
# 参考官方文档进行安装

# 初始化本地归档
gitcrawl init --storage ~/.gitcrawl/archive

# 验证安装
gitcrawl doctor --json
```

### 执行首次查询

```bash
# 搜索指定仓库的 open issue
gitcrawl search issues "bug report" \
  -R owner/repo \
  --state open \
  --json number,title,url
```

### 更新归档数据

```bash
# 手动同步最新数据
gitcrawl sync owner/repo

# 验证数据新鲜度
gitcrawl doctor --json
```

## 配置示例

### 基础查询配置

```bash
# 搜索 open 状态的 issue
gitcrawl search issues "feature request" \
  -R owner/repo \
  --state open

# 搜索包含 closed 状态的 issue
gitcrawl search issues "fixed" \
  -R owner/repo \
  --include-closed

# 查看指定 issue 详情
gitcrawl threads owner/repo \
  --numbers 123,456 \
  --include-closed \
  --json
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `-R` | 字符串 | 无 | 仓库地址 owner/repo |
| `--state` | 字符串 | all | 状态过滤 open/closed/all |
| `--include-closed` | 布尔 | false | 包含已关闭的 |
| `--json` | 字符串 | 无 | 输出 JSON 格式字段 |
| `--numbers` | 字符串 | 无 | 指定 issue/PR 编号 |
| `--limit` | 整数 | 10 | 返回条数上限 |

## 最佳实践

### 查询流程优化

1. **先查缓存**：优先使用 `gitcrawl` 本地查询
2. **检测新鲜度**：使用 `gitcrawl doctor` 确认数据时效
3. **必要时实时**：仅在需要最新数据时使用 `--live` 参数
4. **验证后再操作**：关闭/合并前用 `gh` 实时验证

```bash
# 推荐的查询流程
gitcrawl doctor --json                          # 1. 检查新鲜度
gitcrawl search issues "query" -R owner/repo    # 2. 缓存搜索
gitcrawl gh pr view 123 -R owner/repo --compact # 3. 查看详情
gh pr view 123 --json                           # 4. 实时验证（操作前）
```

### 搜索关键词优化

| 场景 | 推荐关键词 | 说明 |
| --- | --- | --- |
| Bug 查找 | `bug`, `error`, `crash`, `fix` | 定位问题相关 |
| 功能请求 | `feature`, `enhancement`, `request` | 了解需求 |
| 性能问题 | `performance`, `slow`, `memory`, `cpu` | 性能优化 |
| 文档相关 | `docs`, `documentation`, `readme` | 文档改进 |

### 数据新鲜度管理

```bash
# 定期检查数据新鲜度
gitcrawl doctor --json | python -m json.tool

# 数据过期时手动更新
gitcrawl sync owner/repo

# 查看最后同步时间
gitcrawl status owner/repo
```

## 常见问题

### 归档数据过期

```bash
# 检查新鲜度
gitcrawl doctor --json

# 更新归档
gitcrawl sync owner/repo

# 验证更新
gitcrawl doctor --json
```

### 搜索无结果

```bash
# 检查仓库地址是否正确
gitcrawl list-repos

# 尝试更宽泛的关键词
gitcrawl search issues "bug" -R owner/repo --state all

# 包含已关闭的 issue
gitcrawl search issues "keyword" -R owner/repo --include-closed
```

### 实时查询失败

```bash
# 检查 GitHub 认证
gh auth status

# 重新认证
gh auth login

# 使用缓存模式（非实时）
gitcrawl search issues "query" -R owner/repo
```

### 查询速度慢

```bash
# 使用缓存优先模式
gitcrawl search issues "query" -R owner/repo --cached

# 减少 JSON 输出字段
gitcrawl search issues "query" -R owner/repo --json number,title

# 限制返回数量
gitcrawl search issues "query" -R owner/repo --limit 5
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络环境**：需可访问 GitHub（实时查询时）
- **存储空间**：至少 500MB 用于归档缓存

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
| --- | --- | --- | --- |
| gitcrawl | CLI 工具 | 是 | 参考官方文档安装 |
| gh | GitHub CLI | 是（实时查询） | `brew install gh` 或 `apt install gh` |
| Git | 版本控制 | 是 | 系统自带 |
| LLM API | API | 是 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本地缓存查询无需 API Key
- 实时查询需配置 GitHub Token：

```bash
# 配置 GitHub CLI 认证
gh auth login

# 或使用环境变量
export GITHUB_TOKEN=your_token_here
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **适用人群**：个人开发者、开源贡献者、技术调研人员
- **升级建议**：如需多仓库管理、重复聚类、实时同步等高级功能，请使用 PRO 版本
