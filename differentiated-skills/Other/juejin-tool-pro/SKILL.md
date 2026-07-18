---
slug: juejin-tool-pro
name: juejin-tool-pro
version: "1.0.0"
displayName: 掘金工具专业版
summary: 面向团队的多账号批量发布、内容矩阵与数据分析工具。
license: MIT
edition: pro
description: |-
  面向团队的掘金多账号批量发布与内容矩阵治理专业工具。

  核心能力:
  - 多账号矩阵与批量草稿/定时发布
  - 内容选题趋势分析与热度看板
  - 团队发布审批与权限治理
  - 文章数据回流与效果分析

  适用场景:
  - 团队多账号内容矩阵运营
  - 选题趋势分析与热度看板
  - 发布审批流与效果追踪

  差异化: 专业版在免费版单账号草稿上扩展多账号矩阵、批量定时发布、审批流与效果分析，兼容免费版安全限制。

  触发关键词: 多账号矩阵, 批量发布, 定时发布, 选题趋势, 热度看板, 审批流, juejin pro, content matrix
tags:
- 掘金
- 企业级
- 内容运营
- 数据分析
- 其他工具
tools:
- read
- exec
---

# 掘金工具（专业版）

## 概述

专业版面向内容团队与企业，在免费版单账号草稿基础上，扩展多账号矩阵、批量定时发布、选题趋势分析、团队发布审批与文章效果回流。安全限制与免费版兼容，默认草稿逻辑保留，公开发布走审批流。

## 核心能力

| 能力 | 说明 | 专业版增强 |
|:-----|:-----|:-----------|
| 账号矩阵 | 多账号统一管理 | RBAC 权限 |
| 批量发布 | 多篇草稿/定时发布 | 审批流 |
| 选题趋势 | 热度趋势与关键词分析 | 看板 |
| 效果分析 | 阅读/点赞/收藏回流 | 数据看板 |
| 审批治理 | 公开发布审批与留痕 | 团队协同 |

## 使用场景

### 场景一：多账号矩阵发布

```python
# 批量草稿发布（专业版）
import json
matrix = json.load(open("accounts.json"))
for acc in matrix["accounts"]:
    # login(acc) + publish_draft(acc, article, category, tags)
    print(f"{acc['name']}: 草稿已创建")
```

```json
{
  "accounts": [
    {"name": "前端号", "cookie": "acc1.json", "default_category": "前端"},
    {"name": "后端号", "cookie": "acc2.json", "default_category": "后端"}
  ],
  "publish_mode": "draft",
  "schedule": "2026-07-20T10:00:00+08:00"
}
```

### 场景二：选题趋势分析

```text
热度看板（近 7 天）:
─────────────────────────────
TOP 关键词: Vue3.5、Rust、AI Agent
上升最快: AI Agent（+180%）
 decline: jQuery（-12%）
推荐选题: AI Agent 工程化实践
─────────────────────────────
分类热度: 前端 > 后端 > Android
```

### 场景三：发布审批流

```text
审批流:
  作者提交草稿 → 编辑审核 → 公开发布
  审批记录: 申请人/审核人/时间/意见 全留痕
  权限: 仅审核人可触发公开发布
```

## 快速开始

1. 将免费版单账号配置纳入账号矩阵。
2. 配置多账号 Cookie 与默认分类。
3. 设定发布模式（草稿/定时/审批）。
4. 启用选题趋势与效果看板。

## 配置示例

矩阵配置（`accounts.json`）：

```json
{
  "team": "content-team",
  "accounts": [{"name": "前端号", "cookie": "acc1.json"}],
  "publish": {"mode": "draft", "require_approval_for_public": true},
  "dashboard": {"metrics": ["views", "likes", "collects"], "refresh": 3600}
}
```

## 最佳实践

- **默认草稿**：批量发布默认草稿，公开走审批，避免误发。
- **定时错峰**：定时发布错开高峰与账号，避免限流。
- **选题看趋势**：优先上升关键词，避开 decline 话题。
- **效果看回流**：阅读/点赞/收藏回流指导后续选题。
- **Cookie 集中管**：多账号 Cookie 集中加密存储，RBAC 控权限。

## 免费版兼容性

| 项目 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 安全限制 | 相同 | 相同（默认草稿） |
| 账号数 | 单账号 | 多账号矩阵 |
| 发布 | 手动草稿 | 批量/定时/审批 |
| 分析 | 不支持 | 趋势与效果看板 |

## 常见问题

**Q1：多账号 Cookie 怎么管？**
A：集中加密存储，RBAC 分配访问权限，定期轮换。

**Q2：定时发布准吗？**
A：按设定时间触发，错峰发布避免限流。

**Q3：免费版能升级矩阵吗？**
A：能。单账号配置作为矩阵一项，扩展多账号即可。

**Q4：审批流能自定义吗？**
A：能。审核人、层级、字段均可配置。

**Q5：专业版有优先支持吗？**
A：有。专业版享矩阵运营与选题策略咨询。

## 进阶用法

### 多账号矩阵发布

```python
# 矩阵批量草稿发布
import json
matrix = json.load(open("accounts.json"))
for acc in matrix["accounts"]:
    login(acc["cookie"])
    for article in matrix["articles"]:
        publish_draft(acc, article, article["category"], article["tags"])
    logout()
```

```text
矩阵发布原则:
  - 默认草稿，公开走审批
  - 错峰发布，避免限流
  - 各账号默认分类与标签预设
  - 失败项标注原因，可重试
```

### 选题趋势分析

```bash
# 抓取近 7 天热门，统计关键词趋势
{baseDir}/scripts/juejin-pro.sh trend --days 7 --top 20

# 输出趋势报告
{baseDir}/scripts/juejin-pro.sh trend --report trend.json
```

```python
# 趋势计算
from collections import Counter
articles = fetch_hot(days=7)
keywords = Counter()
for a in articles:
    keywords.update(a["keywords"])
# 上升最快 = 本周占比 / 上周占比
rising = [(k, v) for k, v in keywords.most_common(20)]
```

### 效果数据回流

```text
效果看板:
  文章: 25 篇
  总阅读: 48,200
  总点赞: 1,250
  总收藏: 860
  TOP 文章: 「Vue3.5 新特性」阅读 8,200
  建议: 多产 Vue3/AI Agent 选题
```

## 审批流治理

```text
审批流程:
  作者提交草稿 → 编辑审核（内容/合规）→ 通过则可公开发布
  审批记录: 申请人/审核人/时间/意见 全留痕
  权限: 仅审核人可触发公开发布
  SLA: 草稿提交后 24h 内审核
```

## 运营策略

- **选题看趋势**：优先上升关键词，避开 decline 话题。
- **错峰发布**：避开高峰与账号密集发布，防限流。
- **效果看回流**：阅读/点赞/收藏指导后续选题。
- **矩阵分工**：各账号定位不同领域，避免内耗。
- **Cookie 集中管**：多账号 Cookie 集中加密，RBAC 控权限。

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
- 多账号 Cookie 集中加密存储，按 RBAC 分配访问

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成矩阵发布与效果分析
