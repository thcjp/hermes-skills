---
slug: write
name: write
version: "1.0.0"
displayName: Write
summary: Plan, draft, version, and refine written content with enforced versioning
  and quality audits.
license: MIT
description: |-
  Plan, draft, version, and refine written content with enforced versioning
  and quality audits.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: written, write, draft, plan, refine, version
tags:
- Other
tools:
- read
- exec
---

# Write

## Setup

On first use, create workspace:

```bash
./scripts/init-workspace.sh ~/writing
```

## Workflow

```text
Request → Plan → Draft → Audit → Refine → Deliver
```

**Rules:**

* Delegate all writing to sub-agents — main stays free
* NEVER edit files directly — use `./scripts/edit.sh` (enforces versioning)
* Run quality audit before delivering anything long (see `audit.md`)
* Offer cleanup only after user confirms piece is final

## Configuration

Set in `config.json`:

* `depth`: "quick" | "standard" | "thorough" — controls research and revision passes
* `auto_audit`: true/false — run audits automatically after drafts

## Scripts (Enforced)

| Script | Purpose |
| --- | --- |
| `init-workspace.sh` | Create project structure |
| `new-piece.sh` | Start new writing piece with ID |
| `edit.sh` | Edit with automatic version backup |
| `audit.sh` | Run quality audit, generate report |
| `list.sh` | Show all pieces and versions |
| `restore.sh` | Restore previous version |
| `cleanup.sh` | Remove old versions (with confirmation) |

References: `brief.md` for planning, `execution.md` for drafting, `verification.md` for quality checks, `state.md` for tracking, `research.md` for investigation, `versioning.md` for version rules, `audit.md` for dimensions, `criteria.md` for preferences. Scripts in `scripts/`: `scripts/init-workspace.sh`, `scripts/new-piece.sh`, `scripts/edit.sh`, `scripts/audit.sh`, `scripts/list.sh`, `scripts/restore.sh`, `scripts/cleanup.sh`.

---

### Preferences

### Never

---

*Empty sections = observe and fill.*

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
