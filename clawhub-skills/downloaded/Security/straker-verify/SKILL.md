---
slug: straker-verify
name: straker-verify
version: "1.0.0"
displayName: Straker Verify - AI Translation & Human Review
summary: Professional AI-powered translation with optional human verification. Supports
  100+ languages. Qu...
license: MIT
description: |-
  Professional AI-powered translation with optional human verification.
  Supports 100+ languages. Qu...

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: human, straker, powered, verify, professional, translation, optional, review
tags:
- translation
- localization
- i18n
- internationalization
- l10n
- language
- translate
- multilingual
- quality-assurance
- human-verification
- ai-translation
- straker
- verify
- enterprise
- professional
- api
- nlp
- language-services
- content-localization
- translation-management
tools:
- read
- exec
---

# Straker Verify - AI Translation & Human Review

Professional translation, quality evaluation, and human verification services by [Straker.ai](https://straker.ai).

## Features

- **AI Translation**: Translate content to 100+ languages with enterprise-grade accuracy
- **Quality Boost**: AI-powered enhancement for existing translations
- **Human Verification**: Professional human review for critical content
- **File Support**: Documents, text files, and more
- **Project Management**: Track translation projects from submission to delivery

## Quick Start

1. Get your API key from [Straker.ai](https://straker.ai)
2. Set the environment variable: `STRAKER_VERIFY_API_KEY=your-key`
3. Ask your AI assistant: "Translate 'Hello world' to French"

## API Reference

**Base URL:** `https://api-verify.straker.ai`

### Authentication

All requests (except `/languages`) require Bearer token authentication:

```bash
curl -H "Authorization: Bearer $STRAKER_VERIFY_API_KEY" https://api-verify.straker.ai/endpoint
```

### Get Available Languages

```bash
curl https://api-verify.straker.ai/languages
```

Returns a list of supported language pairs with UUIDs for use in other endpoints.

### Create Translation Project

```bash
curl -X POST https://api-verify.straker.ai/project \
  -H "Authorization: Bearer $STRAKER_VERIFY_API_KEY" \
  -F "files=@document.txt" \
  -F "languages=<language-uuid>" \
  -F "title=My Translation Project" \
  -F "confirmation_required=true"
```

### Confirm Project

Required when `confirmation_required=true`:

```bash
curl -X POST https://api-verify.straker.ai/project/confirm \
  -H "Authorization: Bearer $STRAKER_VERIFY_API_KEY" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "project_id=<project-uuid>"
```

### Check Project Status

```bash
curl https://api-verify.straker.ai/project/<project-uuid> \
  -H "Authorization: Bearer $STRAKER_VERIFY_API_KEY"
```

### Download Completed Files

```bash
curl https://api-verify.straker.ai/project/<project-uuid>/download \
  -H "Authorization: Bearer $STRAKER_VERIFY_API_KEY" \
  -o translations.zip
```

### AI Quality Boost

Enhance existing translations with AI:

```bash
curl -X POST https://api-verify.straker.ai/quality-boost \
  -H "Authorization: Bearer $STRAKER_VERIFY_API_KEY" \
  -F "files=@source.txt" \
  -F "language=<language-uuid>"
```

### Human Verification

Add professional human review to translations:

```bash
curl -X POST https://api-verify.straker.ai/human-verify \
  -H "Authorization: Bearer $STRAKER_VERIFY_API_KEY" \
  -F "files=@translated.txt" \
  -F "language=<language-uuid>"
```

## Response Format

**Success:**
```json
{
  "success": true,
  "data": { ... }
}
```

**Error:**
```json
{
  "success": false,
  "error": "Error message"
}
```

## Example Prompts

- "What languages can I translate to?"
- "Translate this text to Spanish: Hello, how are you?"
- "Create a translation project for my document"
- "Check the status of my translation project"
- "Run a quality boost on this French translation"
- "Add human verification to my German translation"

## Support

- Website: [straker.ai](https://straker.ai)
- API Docs: [api-verify.straker.ai/docs](https://api-verify.straker.ai/docs)

## Environment

The API key is available as `$STRAKER_VERIFY_API_KEY` environment variable.

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
