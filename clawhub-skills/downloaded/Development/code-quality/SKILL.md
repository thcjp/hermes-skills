---
slug: code-quality
name: code-quality
version: "1.0.0"
displayName: Code Quality
summary: Coding style standards, security guidelines, and accessibility requirements.
  Use when (1) Writing...
license: MIT-0
description: |-
  Coding style standards, security guidelines, and accessibility requirements.
  Use when (1) Writing...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: style, guidelines, standards, quality, code, coding, security
tags:
- Development
tools:
- read
- exec
---

# Code Quality

## Coding Style

* **Naming:** camelCase for vars/functions; PascalCase for classes/types
* **Formatting:** 4-space indentation; target ≤80 chars (wrap thoughtfully)
* **Comments:** Meaningful, current; delete stale comments
* **Security:** Never log secrets/PII; validate inputs; least privilege by default
* **Errors/Logs:** Explicit error types; structured logs by level; actionable messages

## Accessibility & UX Quality

* Favor semantic roles/labels; keyboard nav and focus order must work
* Include responsive checks at **375, 768, 1024, 1440** with notes/screenshots
* Use deterministic test IDs; avoid brittle CSS/XPath

## Security & Compliance Guardrails

* No real credentials in code, tests, or screenshots
* Use test accounts/fixtures; redact secrets
* Follow least-privilege and input validation
* Document threat considerations in PR when relevant

## Reference Files

See `references/coding-style.md` for detailed style guide, formatting rules, comment standards.

See `references/security-checklist.md` for security validation checklist, threat modeling, PII handling.

See `references/accessibility-standards.md` for WCAG compliance, semantic HTML patterns, keyboard nav testing.

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
