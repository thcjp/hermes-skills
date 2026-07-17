---
slug: sql-generator
name: sql-generator
version: "2.3.7"
displayName: Sql Generator
summary: SQL生成器。自然语言转SQL、SQL解释、性能优化、建表语句、测试数据生成、数据库迁移、SQL速查表。SQL generator from natural
  language, explaine...
license: MIT-0
description: |-
  SQL生成器。自然语言转SQL、SQL解释、性能优化、建表语句、测试数据生成、数据库迁移、SQL速查表。SQL generator from
  natural language, explaine...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 生成器, generator, 自然语言转, 解释, 建表语句, language, explaine, natural
tags:
- Integrations
tools:
- read
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

## Examples

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
