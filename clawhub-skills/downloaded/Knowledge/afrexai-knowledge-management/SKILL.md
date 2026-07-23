---
slug: afrexai-knowledge-management
name: afrexai-knowledge-management
version: "1.0.0"
displayName: Afrexai Knowledge Ma
summary: "组织文档维护关键组织知识,审计/分类/模板"
  taxonomy, templat...
license: MIT
description: |-
  Organize, document, and maintain critical organizational knowledge with
  audits, taxonomy, templat。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
# Knowledge Management System
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

> Turn tribal knowledge into searchable, maintained organizational intelligence. Stop losing expertise when people leave.

## Phase 1: Knowledge Audit
### Current State Assessment
Score each dimension 1-5 (1=nonexistent, 5=excellent):

| Dimension | Score | Evidence |
| --- | --- | --- |
| Documentation coverage |  | % of processes documented |
| Findability |  | Can new hire find answers in <5 min? |
| Freshness |  | % of docs updated in last 6 months |
| Contribution culture |  | % of team actively contributing |
| Onboarding effectiveness |  | Time to productivity for new hires |
| Knowledge retention |  | Impact when someone leaves |
| Cross-team sharing |  | Teams accessing other teams' knowledge |

**Total Score: ___/35**

Interpretation:

* 28-35: Mature — optimize and maintain
* 21-27: Developing — fill gaps systematically
* 14-20: Basic — needs foundational work
* 7-13: Critical — knowledge is at risk

### Knowledge Risk Register

> 详细代码示例已移至 `references/detail.md`

### Knowledge Extraction Interview Guide
For each single-point-of-failure person:

1. **Context**: "I'm documenting [X] so the team isn't dependent on any one person. This protects you too — less interruptions."
2. **Process walk**: "Walk me through [X] from start to finish. I'll record/note."
3. **Decision points**: "Where do you make judgment calls? What factors do you consider?"
4. **Edge cases**: "What are the weird situations that come up? How do you handle them?"
5. **Tools & access**: "What tools, credentials, or access do you need?"
6. **History**: "Why is it done this way? What was tried before?"
7. **Gotchas**: "What are the things that trip people up?"

**Output format**: Write up as a runbook (see Phase 3 templates).

## Phase 2: Knowledge Architecture

> 详细内容已移至 `references/detail.md` - ### Taxonomy Design
### Information Architecture Rules
1. **Maximum 3 levels deep** — if deeper, reorganize
2. **One canonical location per topic** — link, don't duplicate
3. **Every page has an owner** — no orphan docs
4. **Every page has a freshness date** — reviewed within 6 months or flagged
5. **Cross-references over duplication** — "See [X]" beats copy-paste
6. **Search-first design** — assume people search, not browse

### Naming Conventions
```text
[DOMAIN]-[TYPE]-[TOPIC]-[SPECIFICS]

Examples:
eng-howto-deploy-production
eng-ref-api-endpoints-v3
sales-decision-pricing-enterprise
ops-troubleshoot-billing-failed-charges
product-explain-auth-architecture
```

### Navigation Structure
```yaml
knowledge_base:
  homepage:
    - quick_links:  # Top 10 most-accessed pages
    - recently_updated:  # Last 10 changes
    - needs_review:  # Stale docs flagged
  by_audience:
    new_hire: "[Onboarding path → essential reading list]"
    engineer: "[Dev setup → architecture → deployment → debugging]"
    manager: "[Policies → processes → templates → reports]"
    customer_facing: "[Product knowledge → troubleshooting → escalation]"

  by_domain: "[Taxonomy Level 2 domains]"
  by_type: "[How-to | Reference | Explanations | Decisions | Troubleshooting]"
```

## Phase 3: Document Templates
### Runbook Template (How-To)

> 详细代码示例已移至 `references/detail.md`

### Reference Document Template

> 详细代码示例已移至 `references/detail.md`

### Architecture Decision Record (ADR)

> 详细代码示例已移至 `references/detail.md`

### 错误处理
```markdown

**Owner:** [Name]
**Last verified:** [YYYY-MM-DD]

```

[Flowchart as text]
Is [X] happening?
→ YES: Go to Problem A
→ NO: Is [Y] happening?
→ YES: Go to Problem B
→ NO: Go to Problem C

> 详细代码示例已移至 `references/detail.md`

### Decision Tree Template

> 详细代码示例已移至 `references/detail.md`

## Phase 4: Contribution System
### Writing Standards
**The 4C Test** (every document must pass all four):

1. **Clear** — Would a new hire understand this? No jargon without definitions.
2. **Correct** — Has this been verified by doing/testing? Not from memory.
3. **Current** — Does this reflect how things work TODAY? Not 6 months ago.
4. **Concise** — Can anything be cut without losing meaning? Cut it.

**Formatting rules:**

* Headers: action-oriented ("Deploy to Production" not "Production Deployment")
* Steps: numbered, one action per step, imperative mood
* Warnings: callout boxes, before the step (not after)
* Code/commands: exact, copy-pasteable, tested
* Screenshots: only if truly needed (they go stale fast)
* Links: to canonical sources, never paste full URLs inline

### Contribution Workflow

> 详细代码示例已移至 `references/detail.md`

### Incentivizing Contributions
**Making it easy (remove friction):**

* Templates pre-filled with structure
* "Quick capture" channel — dump raw notes, someone structures later
* Post-incident: "What would have helped?" → becomes a doc
* Post-onboarding: new hire documents what was confusing
* Meeting notes → action items include "document [X]"

**Making it visible (social proof):**

* Monthly "top contributors" shoutout
* "Docs champion" rotating role — each sprint, one person owns doc health
* Include documentation in performance criteria
* Knowledge sharing in team meetings (5-min "TIL" segment)

**Making it expected (cultural norms):**

* "If you answered a question twice, write it down"
* PR template includes "Documentation updated? Y/N"
* Incident postmortem includes "Docs to create/update"
* Onboarding feedback includes "What couldn't you find?"

## Phase 5: Search & Discovery
### Search Optimization
**Every document should be findable by:**

1. **Title** — descriptive, includes key terms
2. **Tags** — domain, type, audience, technology
3. **Synonyms** — include alternate terms people might search
4. **Problem description** — "When [X] happens" phrasing

**Tag schema:**

```yaml
document_tags:
  domain: "[engineering|product|sales|ops|finance|hr|cs|security|legal]"
  type: "[howto|reference|explanation|decision|troubleshooting]"
  audience: "[all|engineering|management|customer-facing|new-hire]"
  technology: "[list relevant tools/systems]"
  status: "[current|needs-review|deprecated]"
  difficulty: "[beginner|intermediate|advanced]"
```

### Discovery Mechanisms
1. **Contextual links** — Related docs linked at bottom of every page
2. **FAQ collections** — Per-domain "frequently asked" with links to full docs
3. **Onboarding paths** — Curated reading lists by role
4. **Slack/chat bot** — "Ask the KB" — searches and returns relevant docs
5. **Weekly digest** — "New & updated docs this week" email/message
6. **Error-page links** — Application errors link to troubleshooting docs

### Quality Signals
Prioritize search results by:

* **Freshness** — Recently updated > stale
* **Verification** — Peer-reviewed > unreviewed
* **Usage** — Frequently accessed > rarely accessed
* **Completeness** — Fully structured > quick notes

## Phase 6: Knowledge Capture Workflows
### Post-Incident Knowledge Capture
After every incident:

1. **Immediate** (within 24h): Raw timeline and resolution steps
2. **Postmortem** (within 5 days): Root cause, contributing factors, action items
3. **Knowledge extraction** (within 10 days):
   * New troubleshooting guide? → Create from postmortem
   * New runbook needed? → Create from resolution steps
   * Existing doc wrong? → Update with correct information
   * Architecture decision needed? → Write ADR
   * Monitoring gap? → Document what to monitor

### Post-Meeting Knowledge Capture
Meeting types that MUST produce knowledge artifacts:

* **Architecture review** → ADR
* **Process change** → Updated runbook
* **Strategy decision** → Decision record
* **Customer feedback pattern** → Product knowledge update
* **Retrospective** → Process improvement doc

### New Employee Knowledge Capture
**First 30 days — new hire documents:**

* What was confusing during onboarding
* Questions that weren't answered by existing docs
* Things that were wrong in existing docs
* Suggestions for improvement

**Template for new hire feedback:**

```yaml
onboarding_feedback:
  week: "[1|2|3|4]"
  couldnt_find:
    - topic: "[What they looked for]"
      where_looked: "[Where they searched]"
      how_resolved: "[Asked someone? Found eventually? Still unclear?]"
  wrong_or_outdated:
    - doc: "[Which document]"
      issue: "[What's wrong]"
  suggestions:
    - "[Free text improvements]"
```

### Exit Knowledge Transfer
When someone is leaving:

1. **Identify unique knowledge** — What do they know that no one else does?
2. **Schedule extraction sessions** — 1-2 hours per major topic area
3. **Record if possible** — Video walkthroughs of complex processes
4. **Pair them** — Have successor shadow for final 2 weeks
5. **Review their authored docs** — Are they complete? Assign new owners
6. **Document tribal knowledge** — "Why" questions only they can answer

## Phase 7: Maintenance & Freshness
### Freshness Policy

> 详细代码示例已移至 `references/detail.md`

### Content Health Dashboard

> 详细代码示例已移至 `references/detail.md`

### Quarterly Knowledge Review
**Agenda (60 min):**

1. Dashboard review (10 min) — health metrics trend
2. Gap analysis (15 min) — what's missing? What questions keep being asked?
3. Stale doc triage (15 min) — update, deprecate, or reassign owners
4. Failed searches review (10 min) — what are people searching for and not finding?
5. Process improvements (10 min) — what's working, what isn't?

## Phase 8: Knowledge-Driven Automation
### Automated Knowledge Triggers

> 详细代码示例已移至 `references/detail.md`

### Knowledge-Powered Chatbot Design

> 详细代码示例已移至 `references/detail.md`

## Phase 9: Cross-Team Knowledge Sharing
### Knowledge Sharing Mechanisms
| Mechanism | Frequency | Format | Audience |
| --- | --- | --- | --- |
| "TIL" channel | Daily | Short post (1-3 sentences + link) | All |
| Brown bag lunch | Bi-weekly | 20-min presentation + Q&A | Cross-team |
| Architecture review | Monthly | 45-min deep dive + ADR | Engineering |
| Customer insight share | Monthly | Top 5 patterns + implications | Product + CS + Sales |
| Postmortem review | Per incident | Written + optional walkthrough | Engineering + ops |
| New tool/technique demo | As needed | 15-min demo + doc link | Relevant teams |
| Quarterly knowledge review | Quarterly | Dashboard + gap analysis | Leadership |

### Cross-Team Knowledge Map

> 详细代码示例已移至 `references/detail.md`

## Phase 10: Metrics & ROI
### Knowledge Management KPIs
| Metric | Target | Measurement |
| --- | --- | --- |
| Time to answer | <5 min for documented topics | Sample timing tests |
| New hire time to productivity | Reduce by 30% | First solo task date |
| Repeated questions | Decrease 50% in 6 months | Support ticket analysis |
| Doc coverage | >80% of critical processes | Audit against process list |
| Freshness rate | >85% within review policy | Dashboard metric |
| Contribution rate | >40% of team contributing monthly | Contributor count |
| Search success rate | >80% find what they need | Search analytics |
| Failed search rate | <10% of searches | Search analytics |
| Knowledge reuse | >60% of team using KB weekly | Usage analytics |

### ROI Calculation

> 详细代码示例已移至 `references/detail.md`

## Phase 11: Scoring & Quality
### Document Quality Rubric (0-100)
| Dimension | Weight | 0-2 (Poor) | 3-5 (Adequate) | 6-8 (Good) | 9-10 (Excellent) |
| --- | --- | --- | --- | --- | --- |
| Accuracy | 20% | Unverified, possibly wrong | Mostly correct | Verified, accurate | Tested, peer-reviewed |
| Completeness | 15% | Major gaps | Covers basics | Comprehensive | Edge cases included |
| Clarity | 15% | Confusing, jargon-heavy | Understandable | Clear, well-structured | A new hire gets it |
| Findability | 10% | No tags, bad title | Some tags | Good tags, clear title | Synonyms, cross-refs |
| Freshness | 15% | >12 months stale | Within annual review | Within semi-annual | Within quarterly |
| Template compliance | 10% | No structure | Partial template | Full template | Template + extras |
| Actionability | 10% | Theory only | Some steps | Clear steps | Copy-paste ready |
| Ownership | 5% | No owner | Owner assigned | Owner active | Owner + backup |

**Score interpretation:**

* 90-100: Exemplary — reference model for other docs
* 75-89: Good — meets standards
* 60-74: Acceptable — needs minor improvements
* 40-59: Below standard — needs significant work
* 0-39: Critical — rewrite from scratch

### Knowledge Base Health Score (0-100)
| Dimension | Weight | Metric |
| --- | --- | --- |
| Coverage | 20% | % of critical processes documented |
| Freshness | 20% | % of docs within review policy |
| Quality | 15% | Average document quality score |
| Usage | 15% | % of team using KB weekly |
| Contribution | 15% | % of team contributing monthly |
| Search effectiveness | 15% | % of searches finding results |

## Edge Cases
### Small Team (<10 people)
* Start with a single shared doc/wiki, not a full KB platform
* Focus on: runbooks for critical processes, onboarding guide, decision log
* One person owns KB health (part-time, not full-time)
* Review quarterly, not monthly

### Remote/Distributed Teams
* Default to written over verbal knowledge sharing
* Record important meetings/decisions (not all meetings)
* Async-first: every decision documented, not just discussed
* Time zone coverage: ensure docs cover "what to do when the expert is asleep"

### Rapid Growth (Doubling in 6 months)
* Prioritize onboarding docs above all else
* Implement "new hire documents what they learn" from day 1
* Assign knowledge buddies — each new person paired with a doc mentor
* Weekly new-hire cohort Q&A → captured and documented

### Regulated Industry
* Map compliance requirements to documentation requirements
* Version control with audit trail (who changed what, when)
* Approval workflows for regulated content
* Retention policies aligned with regulations

### Post-Merger/Acquisition
* Map both organizations' knowledge structures
* Identify overlaps and gaps
* Prioritize: "how do we work NOW" docs over historical
* Freeze archives of legacy systems/processes

### Migrating from Scattered Docs
* Don't try to migrate everything — start fresh with new structure
* Import only: still-accurate, frequently-used docs
* Redirect old locations to new ones
* Set a sunset date for old system
* "If it's not in the new KB, it doesn't exist" (after migration period)

## Natural Language Commands
| Command | Action |
| --- | --- |
| "Audit our knowledge management" | Run Phase 1 assessment, generate risk register |
| "Design our KB structure" | Create taxonomy and navigation architecture |
| "Write a runbook for [X]" | Generate using runbook template |
| "Write an ADR for [X]" | Generate architecture decision record |
| "Create a troubleshooting guide for [X]" | Generate using troubleshooting template |
| "Review KB health" | Generate health dashboard and identify gaps |
| "Plan knowledge extraction for [person]" | Generate interview guide and schedule |
| "Set up freshness tracking" | Create review schedule and notification rules |
| "Design onboarding knowledge path for [role]" | Curate reading list from KB |
| "Analyze failed searches" | Review search gaps and create tasks |
| "Generate quarterly KB report" | Full metrics dashboard with recommendations |
| "Plan KB migration from [source]" | Create migration plan with prioritization |

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
[1-2 sentence summary of what this reference contains]

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

## 常见问题
### Q1: 如何开始使用Afrexai Knowledge Ma？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Afrexai Knowledge Ma有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
