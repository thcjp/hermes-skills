---
slug: google-workspace-mcp
name: google-workspace-mcp
version: "1.0.0"
displayName: Google Workspace (No Cloud Console)
summary: Gmail, Calendar, Drive, Docs, Sheets — NO Google Cloud Console required.
  Just OAuth sign-in. Zero...
license: MIT
description: |-
  Gmail, Calendar, Drive, Docs, Sheets — NO Google Cloud Console required.
  Just OAuth sign-in. Zero...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: docs, gmail, drive, calendar, (no, mcp, sheets, console)
tags:
- Communication
tools:
- read
- exec
---

# Google Workspace (No Cloud Console)

**Why this skill?** Traditional Google API access requires creating a project in Google Cloud Console, enabling APIs, creating OAuth credentials, and downloading client_secret.json. This skill skips ALL of that.

Uses `@presto-ai/google-workspace-mcp` — just sign in with your Google account and go.

## Key Advantage

| Traditional Approach | This Skill |
| --- | --- |
| Create Google Cloud Project | ❌ Not needed |
| Enable individual APIs | ❌ Not needed |
| Create OAuth credentials | ❌ Not needed |
| Download client_secret.json | ❌ Not needed |
| Configure redirect URIs | ❌ Not needed |
| **Just sign in with Google** | ✅ That's it |

## Setup (Already Done)

```bash
npm install -g @presto-ai/google-workspace-mcp
mcporter config add google-workspace --command "npx" --arg "-y" --arg "@presto-ai/google-workspace-mcp" --scope home
```

On first use, it opens a browser for Google OAuth. Credentials stored in `~/.config/google-workspace-mcp/`

## Quick Commands

### Gmail

```bash
mcporter call --server google-workspace --tool "gmail.search" query="is:unread" maxResults=10

mcporter call --server google-workspace --tool "gmail.get" messageId="<id>"

mcporter call --server google-workspace --tool "gmail.send" to="email@example.com" subject="Hi" body="Hello"

mcporter call --server google-workspace --tool "gmail.createDraft" to="email@example.com" subject="Hi" body="Hello"
```

### Calendar

```bash
mcporter call --server google-workspace --tool "calendar.list"

mcporter call --server google-workspace --tool "calendar.listEvents" calendarId="your@email.com" timeMin="2026-01-27T00:00:00Z" timeMax="2026-01-27T23:59:59Z"

mcporter call --server google-workspace --tool "calendar.createEvent" calendarId="your@email.com" summary="Meeting" start='{"dateTime":"2026-01-28T10:00:00Z"}' end='{"dateTime":"2026-01-28T11:00:00Z"}'

mcporter call --server google-workspace --tool "calendar.findFreeTime" attendees='["a@example.com","b@example.com"]' timeMin="2026-01-28T09:00:00Z" timeMax="2026-01-28T18:00:00Z" duration=30
```

### Drive

```bash
mcporter call --server google-workspace --tool "drive.search" query="Budget Q3"

mcporter call --server google-workspace --tool "drive.downloadFile" fileId="<id>" localPath="/tmp/file.pdf"
```

### Docs

```bash
mcporter call --server google-workspace --tool "docs.find" query="meeting notes"

mcporter call --server google-workspace --tool "docs.getText" documentId="<id>"

mcporter call --server google-workspace --tool "docs.create" title="New Doc" markdown="# Hello"
```

### Sheets

```bash
mcporter call --server google-workspace --tool "sheets.getText" spreadsheetId="<id>"

mcporter call --server google-workspace --tool "sheets.getRange" spreadsheetId="<id>" range="Sheet1!A1:B10"
```

## Available Tools (49 total)

**Auth:** auth.clear, auth.refreshToken
**Docs:** docs.create, docs.find, docs.getText, docs.insertText, docs.appendText, docs.replaceText, docs.move, docs.extractIdFromUrl
**Drive:** drive.search, drive.downloadFile, drive.findFolder
**Sheets:** sheets.getText, sheets.getRange, sheets.find, sheets.getMetadata
**Slides:** slides.getText, slides.find, slides.getMetadata
**Calendar:** calendar.list, calendar.listEvents, calendar.getEvent, calendar.createEvent, calendar.updateEvent, calendar.deleteEvent, calendar.findFreeTime, calendar.respondToEvent
**Gmail:** gmail.search, gmail.get, gmail.send, gmail.createDraft, gmail.sendDraft, gmail.modify, gmail.listLabels, gmail.downloadAttachment
**Chat:** chat.listSpaces, chat.findSpaceByName, chat.sendMessage, chat.getMessages, chat.sendDm, chat.findDmByEmail, chat.listThreads, chat.setUpSpace
**People:** people.getUserProfile, people.getMe
**Time:** time.getCurrentDate, time.getCurrentTime, time.getTimeZone

## Troubleshooting

### Re-authenticate

```bash
mcporter call --server google-workspace --tool "auth.clear"
```

Then run any command to trigger re-auth.

### Token refresh

```bash
mcporter call --server google-workspace --tool "auth.refreshToken"
```

### Delete credentials

```bash
rm -rf ~/.config/google-workspace-mcp
```

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
