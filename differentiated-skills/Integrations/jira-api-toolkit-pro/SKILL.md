---
slug: jira-api-toolkit-pro
name: jira-api-toolkit-pro
version: "1.0.0"
displayName: Jira工具箱(专业版)
summary: 全功能 Jira Cloud 集成，含创建/更新/流转/批量/自动化与多连接管理。
license: Proprietary
edition: pro
description: |-
  全功能 Jira Cloud 集成，含创建/更新/流转/批量/自动化与多连接管理。核心能力：
  - 全部只读能力 + 创建/更新/删除议题
  - 流转议题状态与评论管理
  - 用户搜索与分配
  - 批量操作与自动化工作流
  - 多连接高级管理与优先支持

  适用场景：
  - 团队自动化议题创建与状态同步
  - 项目经理批量流转与分配
  - DevOps 流水线议题状态驱动
  - 企业多团队多 Jira 实例管理

  差异化：相比免费版新增写操作、批量、自动化三大能力，覆盖团队与企业级 Jira 自动化需求，配套多连接管理与优先支持
tags:
- 集成工具
- 项目管理
- 企业效率
- 自动化
tools:
  - - read
- exec
---
# Jira 工具箱（专业版）

## 概述

专业版在免费版只读能力之上，扩展了写操作、批量处理、自动化工作流三大能力，覆盖团队与企业级 Jira 自动化场景。支持创建/更新/删除议题、流转状态、管理评论、用户搜索与分配，配套多连接高级管理，让"创建一次、流转自动、批量高效"成为 Jira 管理的默认体验。

## 核心能力

| 能力 | 说明 | 免费版 | 专业版 |
|------|------|--------|--------|
| 托管 OAuth 认证 | 自动注入令牌 | 是 | 是 |
| JQL 搜索 | 字段过滤与分页 | 是 | 是 |
| 查看议题详情 | 读取全部字段 | 是 | 是 |
| 项目/类型/状态元数据 | 只读元数据 | 是 | 是 |
| 创建议题 | 新建议题 | 否 | 是 |
| 更新/删除议题 | 修改与删除 | 否 | 是 |
| 流转议题 | 改变状态 | 否 | 是 |
| 评论管理 | 添加/查看评论 | 否 | 是 |
| 用户搜索 | 查找用户 | 否 | 是 |
| 议题分配 | 指派负责人 | 否 | 是 |
| 批量操作 | 批量创建/更新 | 否 | 是 |
| 多连接高级管理 | 多账号切换 | 基础 | 高级 |
| 优先支持 | 优先响应 | 否 | 是 |

## 使用场景

### 场景 1：团队自动化议题创建与状态同步
Scrum Master 每周从需求文档批量创建议题，自动分配到对应负责人与冲刺。专业版的批量创建避免逐条手动录入，状态流转配合 CI/CD 实现"代码合并即议题关闭"。

### 场景 2：项目经理批量流转与分配
版本发布后，项目经理批量流转"待发布"议题为"已发布"，批量分配回归测试议题给 QA 团队。专业版的批量操作一次完成，避免逐条点击。

### 场景 3：DevOps 流水线议题状态驱动
CI/CD 流水线在部署成功后自动流转关联议题为"已上线"，部署失败自动添加评论记录失败原因与日志链接。评论管理能力让流水线状态可追溯。

### 场景 4：企业多团队多 Jira 实例管理
企业有多个 Jira 实例（如研发、运维、客服各一套），专业版的多连接高级管理支持按团队切换连接，批量同步跨实例的关联议题。

## 不适用场景

以下场景Jira工具箱(专业版)不适合处理：

- 逆向工程闭源API
- API安全渗透测试
- 非标准协议集成


## 触发条件

需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于非本工具能力范围的需求。


## 快速开始

> 上手时间：< 120 秒。专业版在免费版只读基础上新增写操作，建议先熟悉只读命令再启用写操作。

### 依赖说明

```bash
npm install -g @maton/cli
maton login
maton connection create jira
maton jira cloud list
```

### 步骤 2：创建议题

```bash
maton jira issue create --cloud-id abc-123 --project PROJ --summary '修复登录失败' --type Task
```

### 步骤 3：更新与分配议题

```bash
maton jira issue update PROJ-123 --cloud-id abc-123 --summary '修复登录失败（含验证码）' --assignee 712020:5aff718e-6fe0-4548-82f4-f44ec481e5e7
```

### 步骤 4：流转议题状态

```bash
maton jira transition list PROJ-123 --cloud-id abc-123
maton jira transition apply PROJ-123 --cloud-id abc-123 --id 31
```

### 步骤 5：添加评论

```bash
maton jira comment add PROJ-123 --cloud-id abc-123 --body '已在测试环境验证通过，请安排上线'
```

## 示例

### 写操作命令速查

| 命令 | 用途 | 示例 |
|------|------|------|
| `issue create` | 创建议题 | `maton jira issue create --cloud-id abc-123 --project PROJ --summary '标题' --type Task` |
| `issue update` | 更新议题 | `maton jira issue update PROJ-123 --cloud-id abc-123 --summary '新标题'` |
| `issue delete` | 删除议题 | `maton jira issue delete PROJ-123 --cloud-id abc-123` |
| `issue update --assignee` | 分配议题 | `maton jira issue update PROJ-123 --cloud-id abc-123 --assignee <accountId>` |
| `transition list` | 查看可用流转 | `maton jira transition list PROJ-123 --cloud-id abc-123` |
| `transition apply` | 流转状态 | `maton jira transition apply PROJ-123 --cloud-id abc-123 --id 31` |
| `comment add` | 添加评论 | `maton jira comment add PROJ-123 --cloud-id abc-123 --body '评论内容'` |
| `comment list` | 查看评论 | `maton jira comment list PROJ-123 --cloud-id abc-123` |
| `user search` | 搜索用户 | `maton jira user search john --cloud-id abc-123` |

### 创建议题请求体

```json
{
  "fields": {
    "project": {"key": "PROJ"},
    "summary": "修复登录失败",
    "issuetype": {"name": "Task"},
    "priority": {"name": "High"},
    "assignee": {"accountId": "712020:5aff718e-6fe0-4548-82f4-f44ec481e5e7"}
  }
}
```

### 流转议题请求体

```json
{
  "transition": {"id": "31"}
}
```

### 多连接管理

| 命令 | 用途 |
|------|------|
| `maton connection list jira --status ACTIVE` | 列出活跃 Jira 连接 |
| `maton connection create jira` | 创建新连接 |
| `maton connection view {id}` | 查看连接详情 |
| `maton connection delete {id}` | 删除连接 |
| `--connection {id}` | 操作时指定连接 |

## 最佳实践

1. **写操作需用户确认**：所有创建、更新、删除操作前，向用户确认目标资源与预期效果，避免误操作。
2. **权限范围明确**：访问范围限于已连接 Jira 账号内的议题、项目、看板、冲刺与用户。
3. **批量操作分批**：批量创建/更新建议每批 20-50 条，避免触发 429 速率限制（10 请求/秒/账号）。
4. **流转前查可用状态**：不同工作流的可用流转不同，先 `transition list` 再 `transition apply`，避免流转到不可达状态。
5. **评论留痕**：自动化操作务必添加评论记录操作者、时间、原因，便于审计与追溯。
6. **多连接显式指定**：多个 Jira 账号时务必 `--connection <id>` 指定，确保请求到正确账号。
7. **更新/删除返回 204**：更新、删除、流转成功返回 HTTP 204（无内容），勿误判为失败。
8. **Agile API 需额外 scope**：敏捷 API（看板、冲刺）需额外 OAuth scope，报错时联系支持申请。
9. **curl 用 -g**：URL 含方括号（`fields[]`）时用 `curl -g` 禁用 glob 解析。
10. **环境变量管道注意**：管道输出到 `jq` 时 `$MATON_API_KEY` 可能不展开，导致 Invalid API key，建议直接用 CLI。

## 常见问题

### Q1：创建议题报 400 字段校验错误？

A：(1) `project.key` 必须存在且大写；(2) `issuetype.name` 必须是该项目可用的类型；(3) 必填字段（如 priority）未传。建议先 `issuetype list` 确认可用类型。

### Q2：流转报 400 无效 transition id？

A：transition id 因工作流而异。先 `transition list PROJ-123` 获取该议题可用流转与对应 id，再用返回的 id 流转。

### Q3：分配议题报 400 无效 accountId？

A：(1) `user search` 获取目标用户的 accountId；(2) accountId 格式为 `712020:uuid`；(3) 确保用户在该项目有可分配权限。

### Q4：批量操作触发 429？

A：Jira Cloud 限制 10 请求/秒/账号。建议：(1) 每批 20-50 条，批次间间隔 1 秒；(2) 使用重试机制处理 429；(3) 大批量任务在非高峰时段执行。

### Q5：删除议题后能否恢复？

A：Jira 删除议题默认不可恢复（除非启用回收站）。专业版建议删除前先 `comment add` 记录删除原因，或使用"关闭"替代"删除"。

### Q6：评论支持富文本吗？

A：支持。评论 body 使用 Atlassian Document Format（ADF），可包含段落、列表、代码块等。CLI 的 `--body` 字符串会自动包装为段落。

### Q7：多连接如何默认指定？

A：通过环境变量 `MATON_DEFAULT_CONNECTION` 设置默认连接 id，未指定 `--connection` 时使用默认。适合单人多账号场景。

### Q8：Agile API 报 scope 错误？

A：敏捷 API（看板、冲刺、epic）需额外 OAuth scope。报错时联系 maton 支持并提供所需操作与用例，申请扩展 scope。

### Q9：更新议题返回 204 算成功吗？

A：是。更新、删除、流转成功返回 HTTP 204 No Content，表示操作成功且无返回体。误判为失败是常见错误。

### Q10：专业版支持自动化触发吗？

A：支持。配合 CI/CD 与 cron 可实现自动化：代码合并触发议题流转、定时批量创建周期议题、部署失败自动添加评论等。

## 错误处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 401 Invalid API key | 未登录 / Key 过期 | `maton login` 重新登录 | P1 |
| 400 Missing connection | 未创建 Jira 连接 | `maton connection create jira` | P1 |
| 400 Invalid transition id | 工作流不可达 | `transition list` 获取可用流转 | P2 |
| 400 Invalid accountId | 用户不存在 / 无权限 | `user search` 重新获取 accountId | P2 |
| 429 Rate limited | 超过 10 请求/秒 | 降速、分批、重试 | P2 |
| 204 误判失败 | 204 为成功 | 确认 204 即成功 | P3 |
| Agile API scope 错误 | 缺少 OAuth scope | 联系支持申请扩展 scope | P2 |
| 管道 Invalid API key | 环境变量未展开 | 直接用 CLI 或显式 export | P3 |

## 专业版特性

本专业版相比免费版新增以下能力：
- 创建议题：支持自定义类型、优先级、分配人、自定义字段
- 更新/删除议题：批量修改字段，删除带评论留痕
- 流转议题状态：查询可用流转并应用，适配各工作流
- 评论管理：添加富文本评论，记录自动化操作痕迹
- 用户搜索与分配：按姓名搜索用户并分配议题
- 批量操作：批量创建/更新/流转，分批处理避免限流
- 多连接高级管理：多 Jira 实例切换，默认连接配置
- 优先支持：优先响应企业级支持需求

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 只读查询 + JQL 搜索 + 元数据浏览 | 个人试用 |
| 收费专业版 | ¥29.9/月 | 全功能 + 写操作 + 批量 + 自动化 + 多连接 + 优先支持 | 团队 / 企业 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Node.js**：16+（用于运行 CLI）
- **cron / 任务计划**：用于自动化触发（Linux 用 cron，Windows 用任务计划程序）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| maton CLI | 命令行工具 | 必需 | `npm install -g @maton/cli` 或 `brew install maton-ai/cli/maton` |
| Jira Cloud 账号 | SaaS 账号 | 必需 | Atlassian 账号，用于 OAuth 授权 |
| Node.js | 运行时 | 必需 | Node.js 官方渠道下载 |
| jq（可选） | 命令行工具 | 可选 | 用于 JSON 结果处理与管道 |

### API Key 配置
- **maton API Key**：通过 `maton login` 获取，存储于环境变量 `MATON_API_KEY`，禁止硬编码
- **Jira OAuth 连接**：通过 `maton connection create jira` 在浏览器完成授权
- **默认连接**：可选设置环境变量 `MATON_DEFAULT_CONNECTION` 指定默认连接
- **禁止**：在 SKILL.md 或脚本中硬编码 API Key 与 OAuth 令牌

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务，支持读写操作与自动化工作流

## 已知限制

- 依赖云服务，需要网络连接
