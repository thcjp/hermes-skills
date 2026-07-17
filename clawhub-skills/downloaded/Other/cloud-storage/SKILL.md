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
  and multi-provider opera...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: files, providers, manage, storage, across, cloud
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
