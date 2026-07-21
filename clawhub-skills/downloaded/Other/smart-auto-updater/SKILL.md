---
slug: smart-auto-updater
name: smart-auto-updater
version: "1.0.0"
displayName: Smart Auto Updater
summary: Smart auto-updater with AI-powered impact assessment. Checks updates, analyzes
  changes, evaluates...
license: MIT
description: |-
  Smart auto-updater with AI-powered impact assessment。Checks updates,
  analyzes changes, evaluates。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Other
tools:
  - - read
- exec
---

# Smart Auto Updater

AI-powered auto-updater that intelligently decides whether to update based on impact assessment. Safe, intelligent, and configurable.

## What it does

### 1. Check Phase

* Checks for Skill平台 updates
* Checks for skill updates via SkillHub
* Fetches changelog and diff

### 2. AI Analysis Phase

* Analyzes changes using LLM
* Evaluates system impact (架构/性能/兼容性)
* Classifies risk level (HIGH/MEDIUM/LOW)

### 3. Decision Phase

| Risk Level | Action |
| --- | --- |
| **HIGH** | Skip update, send detailed report |
| **MEDIUM** | Skip update, send warning + report |
| **LOW** | Auto-update, send summary |

### 4. Report Phase

* Generates readable update report
* Includes risk assessment
* Provides upgrade recommendations

## Quick Start

### Basic usage

```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Run smart update check"
```

### With custom parameters

```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Check updates with custom settings: auto-update LOW risk, report MEDIUM risk"
```

## Configuration

### Environment Variables

```bash
export SMART_UPDATER_MODEL="minimax-portal/MiniMax-M2.1"

export SMART_UPDATER_AUTO_UPDATE="LOW"

export SMART_UPDATER_RISK_TOLERANCE="MEDIUM"

export SMART_UPDATER_REPORT_LEVEL="detailed"
```

## Report Format

### High Risk Report

```text
🔴 Smart Auto-Updater Report

Update Available: v1.2.3 → v1.3.0

⚠️ Risk Level: HIGH

📋 Changes Summary:
- Breaking API changes detected
- Database migration required
- 3 files modified

🏗️ Impact Assessment:
- Architecture: MAJOR changes to core components
- Performance: Potential impact on startup time
- Compatibility: Breaks backward compatibility

🚫 Decision: SKIPPED

💡 Recommendations:
1. Review changelog manually
2. Test in staging environment
3. Schedule maintenance window

🗓️ Next Check: 24 hours
```

### Low Risk Auto-Update

```text
🟢 Smart Auto-Updater Report

Updated: v1.2.3 → v1.2.4

✅ Risk Level: LOW

📋 Changes:
- Bug fixes (2)
- Performance improvements (1)

🏗️ Impact Assessment:
- Architecture: No changes
- Performance: Minor improvement
- Compatibility: Fully compatible

✅ Decision: AUTO-UPDATED

📊 Summary:
- Skill平台: v1.2.3 → v1.2.4
- Skills updated: 2
- Skills unchanged: 15
- Errors: none

⏱️ Next Check: 24 hours
```

## Architecture

```text
┌──────────────────┐
│  Trigger (Cron)  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Check Updates    │ ← SkillHub update --dry-run
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  AI Analysis     │ ← Analyze changes, assess risk
└────────┬─────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐  ┌───────┐
│ HIGH  │  │ MEDIUM│
│ Skip  │  │ Skip  │
└───┬───┘  └───┬───┘
    │          │
    ▼          ▼
┌───────┐  ┌───────┐
│ LOW   │  │ Report│
│ Update│  │ Only  │
└───┬───┘  └───────┘
    │          │
    └────┬─────┘
         │
         ▼
┌──────────────────┐
│  Generate Report  │ ← Send summary
└──────────────────┘
```

## 核心能力

1. **Dry Run First** - Always check before acting
2. **Risk Classification** - AI-powered impact assessment
3. **Configurable Thresholds** - Set your own risk tolerance
4. **Detailed Logging** - Every decision is logged
5. **Manual Override** - Always can review before updating

## Troubleshooting

### Updates keep being skipped

* Check risk tolerance setting
* Verify AI model is available
* Review changelog manually

### False positives (too many HIGH risk)

* Lower risk tolerance
* Check AI model prompts
* Review specific change patterns

### Reports not being delivered

* Verify delivery channel configuration
* Check gateway status
* Review session configuration

## References

* `references/risk-assessment.md` → AI risk assessment methodology
* `references/report-templates.md` → Report format examples
* `references/integration.md` → Integration with cron/jobs

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### Basic usage

```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Run smart update check"
```

### With custom parameters

```bash
skill-platform sessions spawn \
  --agentId smart-auto-updater \
  --message "Check updates with custom settings: auto-update LOW risk, report MEDIUM risk"
```
```

## 常见问题

### Q1: 如何开始使用Smart Auto Updater？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Smart Auto Updater有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
