---
slug: juejin-tool-free
name: juejin-tool-free
version: "1.0.0"
displayName: 掘金工具
summary: 面向个人用户的掘金社区只读与草稿发布工具，支持热门排行。
license: MIT
edition: free
description: |-
  面向个人用户的掘金技术社区操作工具。

  核心能力:
  - 热门文章排行榜与分类查询（只读）
  - 单篇/作者文章下载为 Markdown
  - Markdown 草稿发布（默认仅草稿）
  - 浏览器登录与 Cookie 管理

  适用场景:
  - 个人查看掘金热门文章与分类
  - 下载单篇/少量文章本地存档
  - 把本地 Markdown 作为草稿发到掘金

  差异化: 免费版聚焦个人只读与草稿场景，默认仅创建草稿，安全限制严格，零成本使用。

  触发关键词: 掘金, 热门文章, 排行榜, 文章下载, 草稿发布, juejin, hot articles, draft
tags:
- 掘金
- 内容工具
- 个人效率
- 其他工具
tools:
- read
- exec
---

# 掘金工具（免费版）

## 概述

本工具面向个人用户操作掘金技术社区，覆盖热门文章排行榜查询（只读）、单篇/作者文章下载、Markdown 草稿发布。默认仅创建草稿，公开发布需双重确认，安全限制严格。

## 核心能力

| 能力 | 说明 | 免费版范围 |
|:-----|:-----|:-----------|
| 热门排行 | 分类/全站热门文章 | 只读 |
| 文章下载 | 单篇/作者文章转 Markdown | 单篇/少量 |
| 草稿发布 | 本地 md 发布为草稿 | 默认草稿 |
| 登录管理 | Playwright 浏览器登录 | Cookie 0600 |

## 使用场景

### 场景一：查询热门文章

```text
用户: 获取掘金前端分类的热门文章排行榜
AI: 正在获取掘金前端分类的热门文章...
```

```bash
# 分类列表
GET https://api.juejin.cn/tag_api/v1/query_category_briefs

# 热门文章
POST https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed
```

### 场景二：下载单篇文章

```text
用户: 下载这篇掘金文章 https://juejin.cn/post/7300000000000000000
AI: 正在下载文章并转换为 Markdown 格式...
```

下载结果保存到 `./output/` 目录，保留标题、作者、发布时间等元信息。

### 场景三：草稿发布

```text
用户: 把 ./my-article.md 发布到掘金，分类选前端，标签加 Vue.js
AI: 正在登录掘金账号并发布草稿...
```

> 默认只创建草稿，不公开发布。

## 快速开始

1. 用户明确提到「掘金」与具体动作。
2. 只读操作直接执行；写操作需登录态。
3. 发布默认草稿，公开需双重确认。
4. 下载结果写入 `./output/`。

## 配置示例

激活条件（严格字面匹配）：

| 场景 | 触发要求 |
|:-----|:---------|
| 热门排行 | 字面含「掘金」+ 热门/排行榜 |
| 草稿发布 | 字面含「发布/草稿」+ 掘金 + md 路径 |
| 文章下载 | 字面给 juejin.cn 链接 + 下载 |

## 最佳实践

- **默认草稿**：发布默认只存草稿，避免误公开。
- **路径要显式**：用户必须显式给 md 路径，AI 不代填。
- **下载限 output**：下载结果只写 `./output/`，防越权。
- **Cookie 及时清**：用完执行 `rm ~/.juejin_cookie.json` 撤销登录态。
- **别在共享环境登录**：Cookie 明文存本地，避免共享/CI 环境。

## 常见问题

**Q1：能批量下载吗？**
A：免费版单篇/少量。批量下载（需显式确认，上限 50）支持，但默认 20 篇硬上限。

**Q2：能直接公开发布吗？**
A：不能。默认草稿，公开需 `save_draft_only=False` 且 `allow_public_publish=True` 双重确认。

**Q3：Cookie 安全吗？**
A：文件权限 `0600` 仅本人可读写，用完及时删除，勿提交版本库。

**Q4：免费版支持多账号吗？**
A：不支持。多账号与团队批量发布为专业版能力。

**Q5：非掘金链接能下载吗？**
A：不能。仅接受 juejin.cn 域名链接。

## 进阶用法

### 热门排行查询进阶

```bash
# 全站热门
POST https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed
  body: {"cursor":"0","limit":20}

# 分类热门（如前端 category_id=6809637767543259144）
POST https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed
  body: {"cate_id":"6809637767543259144","cursor":"0","limit":20}
```

### 文章下载为 Markdown

```bash
# 下载单篇（保留元信息）
{baseDir}/scripts/juejin.sh download https://juejin.cn/post/7300000000000000000

# 下载作者全部文章（默认上限 20 篇，需显式确认）
{baseDir}/scripts/juejin.sh download-author --user-id XXX --confirm
```

```text
下载产物（./output/）:
  7300000000000000000.md
  ---
  title: 文章标题
  author: 作者
  published: 2026-07-01
  ---
  正文 Markdown...
```

### 草稿发布安全流程

```text
发布流程:
  1. 用户提供 md 路径 + 分类 + 标签
  2. Playwright 登录（Cookie 存 0600）
  3. 创建草稿（save_draft_only=True 默认）
  4. 返回草稿链接供用户预览
  5. 公开发布需双重确认（默认拒绝）
```

## 安全限制

- **默认草稿**：发布默认只存草稿，不公开。
- **路径显式**：用户必须显式给 md 路径，AI 不代填。
- **下载限 output**：下载结果只写 `./output/`。
- **批量上限**：批量下载默认 20 篇硬上限，需确认。
- **域名限制**：仅接受 juejin.cn 链接。

## 工作流分类

| 操作类别 | 处理方式 | 示例 |
|:---------|:---------|:-----|
| 信息查询 | 直接执行 | 热门排行 |
| 设置调整 | 直接执行 | 草稿配置 |
| 破坏性 | 先确认 | 公开发布 |
| 需登录 | 先登录态 | 草稿发布 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+
- **网络**: 可访问 juejin.cn

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python | 运行时 | 必需 | python.org |
| Playwright | 浏览器自动化 | 登录时必需 | `pip install playwright` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 无需额外 API Key
- 登录后掘金会话 Cookie 保存到 `~/.juejin_cookie.json`（权限 0600）

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 调用掘金 API 完成只读与草稿操作
