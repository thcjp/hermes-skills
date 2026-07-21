---
slug: sql-generator
name: sql-generator
version: "2.3.7"
displayName: Sql Generator
summary: SQL生成器。自然语言转SQL、SQL解释、性能优化、建表语句、测试数据生成、数据库迁移、SQL速查表。SQL generator from natural
  language, explaine...
license: MIT-0
description: |-
  SQL生成器。自然语言转SQL、SQL解释、性能优化、建表语句、测试数据生成、数据库迁移、SQL速查表。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。
tags:
- Integrations
tools:
  - - read
- exec
---

# Sql Generator

SQL生成器。自然语言转SQL、SQL解释、性能优化、建表语句、测试数据生成、数据库迁移、SQL速查表。SQL generator from natural language, explainer, optimizer, DDL creator, mock data, migration scripts, cheatsheet. SQL、数据库、MySQL。

## 常见问题

**Q: 这个工具适合谁用？**
A: 任何需要sql generator的人，无论是个人还是企业用户。

**Q: 输出格式是什么？**
A: 主要输出Markdown格式，方便复制和编辑。

## 可用命令

* **query** — query
* **explain** — explain
* **optimize** — optimize
* **create** — create
* **mock** — mock
* **migrate** — migrate
* **cheatsheet** — cheatsheet

## 专业建议

* SELECT/WHERE/ORDER BY
* INSERT/UPDATE/DELETE
* 基本聚合（COUNT/SUM/AVG）
* GROUP BY + HAVING
* JOIN（INNER/LEFT/RIGHT/FULL）

---

## *SQL Generator by BytesAgain*

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

## 示例

```bash
sql-generator help

sql-generator run
```

## Commands

Run `sql-generator help` to see all available commands.

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

- 自然语言转SQL、SQL解释、性能优化、建表语句、测试数据生成、数据库迁移、SQL速查表
- SQL generator from
  natural language, explaine
- 触发关键词: 生成器, generator, 自然语言转, 解释, 建表语句, language, explaine, natural

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
