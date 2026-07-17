---
slug: cloud
name: cloud
version: "1.0.0"
displayName: Cloud
summary: Choose, organize, sync, share, and back up personal files across iCloud,
  Google Drive, Dropbox, a...
license: MIT
description: |-
  Choose, organize, sync, share, and back up personal files across iCloud,
  Google Drive, Dropbox, a...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: sync, cloud, organize, choose, share
tags:
- Integrations
tools:
- read
- exec
---

# Cloud

## Triggers

Activate on: iCloud full, cloud storage, backup photos, sync between devices, share folder, Google Drive help, Dropbox issues, "where are my files", storage plan comparison.

## Scope

This skill covers **consumer cloud storage** — the services regular people use for photos, documents, and backups.

**Not this skill:** AWS, Azure, S3 buckets, VPS, Docker, APIs → use `infrastructure`, `s3`, or `server`.

## Quick Service Picker

| Your devices | Best fit | Why |
| --- | --- | --- |
| iPhone + Mac | iCloud | Native integration, seamless |
| Android + Chrome | Google Drive | Included with Gmail, auto photo backup |
| Windows PC | OneDrive | Built into Windows, Office integration |
| Mixed devices | Dropbox | Works equally well everywhere |

For detailed pricing and features, see `services.md`.

## Common Confusions

| What you think | What's actually happening |
| --- | --- |
| "I deleted it from my phone and now it's gone from my laptop" | Sync works as designed — one file, everywhere |
| "iCloud storage full but my phone has space" | Phone storage ≠ iCloud storage |
| "My photos are duplicated everywhere" | Multiple services backing up the same camera roll |
| "I pay for 3 cloud services" | Pick one primary, cancel the rest |

## Storage Full — What to Do

1. **Check what's using space** — Photos usually dominate
2. **Empty trash** — Deleted files count until trash is emptied
3. **Disable duplicate backups** — Pick one photo backup service
4. **Offload old files** — Move archives to external drive

For service-specific cleanup steps, see `cleanup.md`.

## Backup Strategy

* **3-2-1 rule:** 3 copies, 2 different media, 1 offsite
* **Cloud counts as offsite** — but also keep a local backup
* **Check backup status monthly** — don't assume it's working

What to back up and what NOT to store in cloud: see `backup.md`.

## Sharing Files

| Need | Method |
| --- | --- |
| Quick share with anyone | Link (set expiration) |
| Ongoing family access | Shared folder |
| Sensitive documents | Don't use cloud, or encrypt first |

Step-by-step per service: see `sharing.md`.

## Security Basics

* **Enable 2FA** on all cloud accounts
* **Review shared links** quarterly — revoke old ones
* **Don't store unencrypted:** passwords, IDs, financial documents

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
