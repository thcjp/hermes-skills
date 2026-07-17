---
slug: merge-check
name: merge-check
version: "1.0.0"
displayName: Merge Check
summary: Analyze a GitHub pull request for mergeability — predict whether it will
  get merged based on tech...
license: MIT
description: |-
  Analyze a GitHub pull request for mergeability — predict whether it
  will get merged based on tech...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: merge, github, pull, check, request, analyze, mergeability
tags:
- Development
tools:
- read
- exec
---

# Merge Check

Predicts whether a GitHub PR will get merged by analyzing it against a comprehensive rejection vector taxonomy. Not a generic code quality tool — this answers: **"Will this PR get merged by the maintainer?"**

## Quick Start

1. Run the data gathering script:

   bash

   ```
   bash skills/merge-check/scripts/merge-check.sh owner/repo#123
   # or
   bash skills/merge-check/scripts/merge-check.sh https://github.com/owner/repo/pull/123
   ```
2. Parse the JSON output
3. Analyze against the dimensions below
4. Produce the mergeability report

## Analysis Dimensions

After gathering data, analyze across ALL of these dimensions. Load `skills/merge-check/references/rejection-taxonomy.md` for the detailed rejection vector framework.

### 1. Technical Signals (Automated Gates)

* **CI status**: Are all checks passing? Any failed or pending?
* **Build status**: Does it compile/build?
* **Coverage**: Any coverage regression indicated?

### 2. PR Hygiene

* **Size** (most predictive single factor):
  + 🟢 <400 LOC changed — ideal, easy to review
  + 🟡 400–1000 LOC — risky, reviewer fatigue
  + 🔴 >1000 LOC — danger zone, likely to stall or get rejected
* **File spread**: Concentrated in one area or scattered across directories?
* **Single concern**: Does it do one thing, or is it a kitchen-sink PR?
* **Title & description**: Clear, descriptive? Or vague/empty?
* **Linked issue**: Does it reference an issue? (Signals intentionality)
* **Commit hygiene**: Clean messages? Reasonable count? Squash-ready?

### 3. Architectural Fit

* **Pattern consistency**: Does it follow repo conventions? (language, directory structure, naming)
* **Dependencies**: New dependencies introduced? (High friction signal)
* **Scope creep**: Does it touch things outside its stated purpose?
* **File types**: Consistent with repo's tech stack?

### 4. Review Status

* **Approvals**: Any already? How many required?
* **Changes requested**: Outstanding and unaddressed? (Strong rejection signal)
* **Reviewer assignment**: Are required reviewers assigned?
* **Review comment sentiment**: Positive, neutral, or adversarial?
* **CODEOWNERS**: Does the PR touch files with code owners? Are they reviewing?

### 5. Process Compliance

* **Draft status**: Draft PRs won't merge
* **Blocking labels**: WIP, do-not-merge, needs-work, etc.
* **PR template**: Was it followed? (Empty template = red flag)
* **CLA/DCO**: If repo requires it, is it signed?

### 6. Social/Meta Signals

* **Author merge history**: What % of this author's recent PRs were merged in this repo?
* **Staleness**: How long has it been open? (>2 weeks = concern, >30 days = likely abandoned)
* **Activity level**: Recent comments/updates, or radio silence?
* **First-time contributor**: Higher rejection rate for newcomers

## Output Format

Produce a structured report:

### Mergeability Score

* 🟢 **High** (>80% likely to merge) — No blockers, reviews positive, CI green
* 🟡 **Medium** (40–80%) — Some concerns but addressable
* 🔴 **Low** (<40%) — Significant blockers present

### Report Sections

1. **Mergeability Score**: 🟢/🟡/🔴 with percentage estimate
2. **Risk Factors**: Bullet list of specific concerns, ordered by severity
3. **Strengths**: What's working in the PR's favor
4. **Recommendations**: Actionable steps to improve mergeability (if not already 🟢)
5. **Verdict**: One-sentence summary

### Example Output

```text
## PR Mergeability Report: owner/repo#123

**Score: 🟡 Medium (~55%)**

### Risk Factors
- ⚠️ 847 lines changed — approaching reviewer fatigue threshold
- ⚠️ Changes requested by @maintainer not yet addressed
- ⚠️ Touches 12 files across 6 directories — scattered scope
- ℹ️ No linked issue

### Strengths
- ✅ All 14 CI checks passing
- ✅ Clear title and detailed description
- ✅ Author has 73% merge rate in this repo (8/11 recent PRs)
- ✅ Active discussion — last update 2 hours ago

### Recommendations
1. Address @maintainer's review comments before requesting re-review
2. Consider splitting into smaller PRs (config changes vs logic changes)
3. Link the relevant issue for traceability

### Verdict
Solid PR with passing CI and an active author, but stalled on unaddressed review feedback — resolving those comments is the critical path to merge.
```

## Script Reference

The script (`scripts/merge-check.sh`) gathers all data via `gh` CLI and outputs a single JSON object with these keys:

| Key | Contents |
| --- | --- |
| `pr` | Full PR metadata (title, body, author, state, draft, labels, reviewers) |
| `files` | List of changed files with patch stats |
| `diff_stats` | Total additions, deletions, changed files count |
| `checks` | CI/check run results for the head commit |
| `reviews` | All reviews (approved, changes_requested, commented) |
| `review_comments` | Inline review comments |
| `issue_comments` | PR conversation comments |
| `commits` | Commit list with messages |
| `repo` | Repository metadata (language, size, defaults) |
| `author_history` | Author's recent closed PRs and merge rate |
| `has_codeowners` | Boolean |
| `has_contributing` | Boolean |

## Error Handling

The script outputs `"error"` fields when individual API calls fail (e.g., rate limits, 404s). Analyze what's available and note any missing data in the report.

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
