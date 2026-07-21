---
slug: remix-api-key-auth
name: remix-api-key-auth
version: "0.1.0"
displayName: Remix Api Key Auth
summary: Configure and verify bearer API key authentication for Remix agent publishing
  workflows.
license: MIT
description: |-
  Configure and verify bearer API key authentication for Remix agent publishing
  workflows。核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关...
tags:
- Integrations
tools:
  - - read
- exec
---

# Remix Api Key Auth

Use this skill when a user needs to authenticate an external service/agent for Remix server APIs.

## Steps

1. Log in to your Remix account.
2. Go to `https://remix.gg/api-keys`.
3. Create a new API key.
4. Store it as a secret in your service runtime.
5. Send:
   * `Authorization: Bearer <api_key>`
6. Use base URL `https://api.remix.gg`.

## Verification

Run a cheap authenticated call first (for example, `POST /v1/agents/games` in a test project) to verify the key works.

## 错误处理

* Check `Authorization` is formatted as `Bearer <api_key>`.
* Re-copy the key from `https://remix.gg/api-keys` and rotate if needed.
* Verify your service is reading the expected secret/env var in the current runtime.
* Confirm the request is server-side and not exposed through browser code.
* If behavior seems inconsistent with local docs, use `https://api.remix.gg/docs` as source of truth.

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

- Configure and verify bearer API key authentication for Remix agent publishing
  workflows
- 触发关键词: api, configure, auth, verify, authentication, remix, bearer, key

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

## 常见问题

### Q1: 如何开始使用Remix Api Key Auth？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Remix Api Key Auth有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
