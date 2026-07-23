---
slug: cloud-storage
name: cloud-storage
version: "1.0.1"
displayName: Cloud Storage
summary: Manage files across cloud providers with authentication, cost awareness,
  and multi-provider opera...
license: MIT
description: |-
  Manage files across cloud providers with authentication, cost awareness,
  and multi-provider opera。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Cloud Storage

## When to Use

User needs to upload, download, sync, or manage files across cloud storage providers. Agent handles multi-provider operations with cost awareness.

## Quick Reference

| Topic | File |
| --- | --- |
| Provider-specific patterns | `providers.md` |
| Authentication setup | `auth.md` |
| Cost calculation | `costs.md` |

## Scope

This skill covers operational cloud storage tasks across providers:

* S3, GCS, Azure Blob, Backblaze B2, Cloudflare R2
* Google Drive, Dropbox, OneDrive, iCloud

For storage architecture decisions, see `storage` skill.
For S3-specific deep patterns, see `s3` skill.

## Critical Rules

1. **Verify operations completed** — API 200 ≠ success; check file exists with correct size/checksum
2. **Calculate ALL costs before large transfers** — egress fees often exceed storage costs; check `costs.md`
3. **Never delete without backup verification** — confirm backup exists AND is restorable before removing source
4. **Handle partial failures** — long operations fail mid-way; implement checkpoints and resume logic
5. **Rate limits vary wildly** — Google 750GB/day upload, Dropbox batch limits, S3 3500 PUT/s per prefix

## Authentication Traps

* **OAuth tokens expire** — refresh before long operations, not during
* **Service account ≠ user account** — different quotas, permissions, audit trails
* **Wrong region/endpoint** — S3 bucket in `eu-west-1` won't work with `s3.amazonaws.com`
* **MFA required** — some operations need session tokens, plan for interactive auth

## Multi-Provider Gotchas

| Concept | Translates differently |
| --- | --- |
| Shared folder | Drive "Shared with me" ≠ Dropbox "Team Folders" ≠ OneDrive "SharePoint" |
| File ID | Drive uses IDs; Dropbox uses paths; S3 uses keys |
| Versioning | S3 explicit enable; Drive automatic; Dropbox 180 days |
| Permissions | S3 ACLs + policies; Drive roles; Dropbox link-based |

## Before Any Bulk Operation

* Estimated time calculated (size ÷ bandwidth)
* Rate limits checked for both source AND destination
* Cost estimate including egress + API calls
* Checkpoint/resume strategy for failures
* Verification method defined (checksum, count, spot-check)

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

- Manage files across cloud providers with authentication, cost awareness,
  and multi-provider opera
- 触发关键词: files, providers, manage, storage, across, cloud

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

### Q1: 如何开始使用Cloud Storage？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Cloud Storage有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
