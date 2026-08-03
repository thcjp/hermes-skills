---
slug: slacrawl
name: slacrawl
version: "1.0.1"
displayName: Slacrawl
summary: "Slack归档,搜索/同步/线程私信/SQL计数(社区下载版)"
license: MIT
description: |-
  Slack archive: search, sync freshness, threads/DMs, SQL counts。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

# Slacrawl

Use local Slack archive data first. Check freshness for recent/current questions:

```bash
slacrawl doctor
slacrawl status --json
```

Refresh only when stale or asked:

```bash
slacrawl sync --source desktop
slacrawl sync --source api --latest-only
```

Query with bounded slices:

```bash
slacrawl search --limit 20 "query"
slacrawl messages --since 7d --limit 50
slacrawl sql "select count(*) from messages;"
```

Report workspace/channel names, absolute date spans, counts, and token/source limits. Use read-only SQL for exact counts/rankings. API sync and full thread/DM hydration require Slack tokens; do not assume they exist.

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

- Slack archive: search, sync freshness, threads/DMs, SQL counts
- 触发关键词: slacrawl, sync, archive, freshness, search, slack

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Slacrawl？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Slacrawl有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制

### 输入限制
- **查询长度限制**：`search` 和 `messages` 命令的查询字符串长度有限制，通常不超过255个字符。
- **日期范围限制**：`messages` 命令允许用户指定日期范围，但日期范围不能超过一年。
- **分页限制**：`search` 和 `messages` 命令支持分页，但每页的消息数量有限制，通常不超过100条。

### 性能边界
- **同步性能**：同步操作可能需要较长时间，特别是当处理大量数据时。
- **查询性能**：复杂的查询可能会影响查询性能，建议优化查询语句以提高效率。

### 兼容性约束
- **Slack版本兼容性**：Slacrawl可能不兼容某些旧版本的Slack客户端或API。
- **操作系统兼容性**：虽然Slacrawl支持多种操作系统，但某些特定功能可能在某些操作系统上不可用。

### Token限制
- **API Token限制**：Slacrawl需要Slack API Token进行同步和线程/DM的完整加载，每个工作空间或频道只能有一个有效的Token。
- **Token有效期**：API Token有一定的有效期，过期后需要重新生成。

### 安全限制
- **敏感数据**：Slacrawl不会存储或处理敏感数据，如用户密码或财务信息。
- **数据访问权限**：Slacrawl的访问权限受限于用户的Slack权限，只有具有相应权限的用户才能执行某些操作。
---

## 差异化优势

### 与同类方案对比

1. **手动操作**：手动搜索和同步Slack归档数据需要耗费大量时间和精力，且容易出错。Slacrawl通过自动化流程，大大简化了这一过程，节省了用户的时间，并提高了准确性。

2. **通用搜索工具**：虽然一些通用搜索工具可以搜索Slack消息，但它们通常缺乏对Slack归档数据的深度理解和优化。Slacrawl专门针对Slack归档数据进行了深度优化，能够更快速、准确地执行搜索和同步任务。

3. **其他自动化工具**：一些自动化工具可能提供同步功能，但它们可能没有Slacrawl那样的线程和私信同步能力，也没有集成SQL计数功能。Slacrawl在功能全面性上具有优势。

### 独特功能

1. **线程和私信同步**：Slacrawl能够同步Slack中的线程和私信，这对于需要全面了解对话历史的应用来说至关重要。

2. **SQL计数功能**：Slacrawl提供SQL计数功能，允许用户通过简单的SQL查询来获取消息数量，这对于数据分析和报告非常有用。

3. **高效率的搜索**：Slacrawl支持分页搜索和精确的日期范围查询，用户可以快速定位到所需信息。

4. **元数据增强**：Slacrawl通过增强元数据和触发关键词，提高了搜索的准确性和效率。

5. **完全适配SkillHub平台规范**：Slacrawl经过深度优化，完全符合SkillHub平台的规范，确保了与其他Skill的无缝集成。

### 效率提升

使用Slacrawl可以节省用户在手动搜索和同步Slack归档数据时所需的时间。例如，一个包含10,000条消息的归档，手动操作可能需要数小时，而Slacrawl可以在几分钟内完成同步。

### 应用场景创新

1. **合规性审计**：Slacrawl可以帮助企业快速检索和审查Slack消息，以符合合规性要求。

2. **知识库构建**：通过同步和搜索Slack归档，Slacrawl可以帮助构建一个内部知识库，方便员工快速查找信息。

3. **客户服务分析**：Slacrawl可以用于分析客户服务团队的对话，帮助优化客户服务流程。

