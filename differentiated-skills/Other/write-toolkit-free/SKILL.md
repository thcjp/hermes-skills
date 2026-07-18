---
slug: write-toolkit-free
name: write-toolkit-free
version: "1.0.0"
displayName: 写作工具免费版
summary: 规划、起草、版本化与精炼写作内容，强制版本管理与质量审计，适合个人创作者。
license: MIT
edition: free
description: |-
  写作工具免费版，面向个人创作者的轻量级写作流程管理工具。

  核心能力:
  - 规划-起草-审计-精炼-交付五步工作流
  - 强制版本化管理与自动备份
  - 质量审计与多维度检查
  - 子代理委派写作，主代理保持自由

  适用场景:
  - 个人博客与文章写作
  - 技术文档与产品说明
  - 长篇内容的版本化管理

  差异化: 免费版聚焦核心写作流程与版本管理，去除所有外部平台与作者引用，强化中文本地化与触发关键词，适合个人用户零成本上手。

  触发关键词: 写作, 起草, 版本管理, 质量审计, 内容精炼, 子代理写作, 文档规划
tags:
- 写作
- 版本管理
- 质量审计
- 免费版
tools:
- read
- exec
---

# 写作工具（免费版）

## 概述

写作工具免费版帮助你规划、起草、版本化与精炼写作内容。遵循「规划-起草-审计-精炼-交付」五步工作流，强制版本化管理确保每次编辑都有备份，质量审计在交付前检查多维度质量。

## 核心能力

| 能力 | 说明 |
|:-----|:-----|
| 五步工作流 | 规划 → 起草 → 审计 → 精炼 → 交付 |
| 版本管理 | 强制版本备份，支持历史回滚 |
| 质量审计 | 多维度质量检查，生成审计报告 |
| 子代理委派 | 写作委派给子代理，主代理保持自由 |
| 配置管理 | 深度（快速/标准/深入）与自动审计开关 |

## 使用场景

### 场景一：撰写技术博客

从规划到交付的完整写作流程。

```bash
# 1. 初始化工作区
./scripts/init-workspace.sh ~/writing

# 2. 创建新作品
./scripts/new-piece.sh "async-programming-guide"

# 3. 编辑（自动版本备份）
./scripts/edit.sh async-programming-guide "添加异步基础概念部分"

# 4. 质量审计
./scripts/audit.sh async-programming-guide

# 5. 列出所有版本
./scripts/list.sh async-programming-guide

# 6. 交付（用户确认后清理）
./scripts/cleanup.sh async-programming-guide
```

### 场景二：长篇内容的版本管理

长篇内容需要多次迭代，每次保留版本。

```bash
# 编辑时自动创建版本备份
./scripts/edit.sh long-article "精炼第三章的逻辑表述"

# 查看历史版本
./scripts/list.sh long-article
# 输出:
# v1.0 - 2026-07-15 初稿
# v1.1 - 2026-07-16 修订第二章
# v1.2 - 2026-07-18 精炼第三章

# 回滚至历史版本
./scripts/restore.sh long-article v1.1
```

### 场景三：交付前质量审计

交付前执行多维度质量审计。

```bash
# 执行质量审计
./scripts/audit.sh my-article

# 输出审计报告
# 📊 质量审计报告
# 文章: my-article
# 版本: v1.3
# 审计维度:
#   - 结构完整性: 92/100
#   - 逻辑连贯性: 88/100
#   - 语言流畅度: 90/100
#   - 术语一致性: 95/100
#   - 引用准确性: 85/100
# 综合评分: 90/100
# 💡 建议: 第三章过渡可加强
```

## 快速开始

```bash
# 1. 初始化工作区
./scripts/init-workspace.sh ~/writing

# 2. 创建新作品（带 ID）
./scripts/new-piece.sh "article-slug"

# 3. 编辑（强制版本化）
./scripts/edit.sh article-slug "编辑说明"

# 4. 审计
./scripts/audit.sh article-slug

# 5. 列出作品与版本
./scripts/list.sh

# 6. 回滚
./scripts/restore.sh article-slug v1.0

# 7. 清理（用户确认后）
./scripts/cleanup.sh article-slug
```

## 配置示例

```json
{
  "depth": "standard",
  "auto_audit": true,
  "versioning": {
    "enabled": true,
    "max_versions": 20,
    "auto_backup": true
  },
  "audit": {
    "dimensions": ["structure", "logic", "fluency", "terminology", "citation"],
    "threshold": 80
  }
}
```

## 最佳实践

* 所有写作委派给子代理，主代理保持自由处理其他任务。
* 永远不要直接编辑文件，使用 `edit.sh` 强制版本化。
* 长篇内容交付前务必运行质量审计。
* 清理旧版本前确认作品已最终定稿。
* 深度配置根据内容重要性选择（快速/标准/深入）。
* 启用自动审计，确保每次草稿后都检查质量。
* 版本回滚前先查看历史版本的审计报告。

## 常见问题

**Q：免费版支持多人协作吗？**
A：免费版面向个人写作。如需多人协作与评论，请考虑 PRO 版本。

**Q：免费版支持自定义审计维度吗？**
A：免费版使用固定五维度。如需自定义维度与权重，请使用 PRO 版本。

**Q：版本有数量上限吗？**
A：默认保留 20 个版本，超出后自动清理最旧版本。可通过配置调整。

**Q：可以导出为其他格式吗？**
A：免费版以 Markdown 为主。如需 PDF/DOCX 导出，请使用 PRO 版本。

**Q：子代理委派是什么意思？**
A：写作任务交给子代理执行，主代理可以继续处理其他指令，提升效率。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: bash（脚本依赖）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| bash | 运行时 | 必需 | 系统自带 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + Shell脚本执行）
- **说明**: 基于Markdown的AI Skill，通过 Shell 脚本管理写作流程与版本
