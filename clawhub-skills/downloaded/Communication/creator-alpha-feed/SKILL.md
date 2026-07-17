---
slug: creator-alpha-feed
name: creator-alpha-feed
version: "1.0.8"
displayName: Creator Alpha Feed
summary: Collect and rank daily AI content for creator-focused publishing workflows.
  Use when users ask fo...
license: MIT
description: |-
  Collect and rank daily AI content for creator-focused publishing workflows.
  Use when users ask fo...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: collect, feed, content, alpha, creator, daily, rank
tags:
- Communication
tools:
- read
- exec
---

# Creator Alpha Feed

1. Read config first:
   * `${OBSIDIAN_CONFIG_PATH:-<your_obsidian_vault>/Skill平台/项目/AI内容日报/采集配置.md}`
2. Execute collection in this order for X:
   * homepage feed → whitelist accounts → keywords
3. Prefer API where available; fallback to browser when unavailable.
4. Enforce browser tab cap:
   * max 7 concurrent tabs; close finished tabs first; end with 0 tabs (close all temporary tabs before finishing).
5. Build ranked outputs by configured structure (default):
   * KOL TOP3 (last 6h)
   * Practical/Tutorial/Opinion TOP10
   * Industry TOP3 (last 6h)
6. Push concise results to group channel; write full report to Obsidian path.
7. Name report files with timestamp format: `YYYY-MM-DD_HHMM.md`.
8. Prefer real Obsidian Vault path (not workspace mirror) when available.
9. Use structured Obsidian directories:
   * `Skill平台/项目/AI内容日报/01-日报/` for final reports
   * `Skill平台/项目/AI内容日报/02-运行记录/` for verification/debug runs
   * `Skill平台/项目/AI内容日报/03-文档/` for installation/operational docs
10. If login is required for a source, pause and notify user to log in; wait up to 3 minutes with periodic checks, then continue remaining sources if still unavailable.

## Bundled scripts

Use `scripts/collect-v4.sh` and related scripts for deterministic fallback/automation when needed.

## Required output checks

* Include must-track account status for `@xiaohu @dotey @marclou`
* Include fallback/degradation notes
* Include final report path
* In group replies, mention the question asker (`@who asked`) when channel supports mentions

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
