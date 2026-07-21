# 详细参考 - afrexai-knowledge-management

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
knowledge_taxonomy:
  types:
    how_to:
      description: "Step-by-step procedures and guides"
      examples: ["Deploy to production", "Process a refund", "Set up dev environment"]
      template: "runbook"

    reference:
      description: "Facts, specs, configurations to look up"
      examples: ["API endpoints", "Config values", "Vendor contacts", "Pricing tables"]
      template: "reference_doc"

    explanation:
      description: "Why things work the way they do"
      examples: ["Architecture decisions", "Policy rationale", "Historical context"]
      template: "explainer"

    decision:
      description: "How to make specific judgment calls"
      examples: ["Escalation criteria", "Approval thresholds", "Priority frameworks"]
      template: "decision_tree"

    troubleshooting:
      description: "Diagnosis and fix for known problems"
      examples: ["Error codes", "Common failures", "Debug procedures"]
      template: "troubleshooting_guide"

  domains:
    - engineering
    - product
    - sales
    - operations
    - finance
    - hr_people
    - customer_success
    - security
    - legal_compliance

  engineering_topics:
    - architecture
    - deployment
    - monitoring
    - incident_response
    - development_workflow
    - testing
    - security
    - infrastructure
```

## 代码示例 (yaml)

```yaml
kb_health:
  date: "[YYYY-MM-DD]"

  coverage:
    total_documents: 0
    by_type:
      howto: 0
      reference: 0
      explanation: 0
      decision: 0
      troubleshooting: 0
    by_domain: {}
    gaps_identified: []

  freshness:
    current: 0  # Reviewed within policy
    needs_review: 0  # Due for review
    stale: 0  # Past review deadline
    deprecated: 0
    freshness_rate: "0%"  # current / (current + needs_review + stale)
  quality:
    peer_reviewed: "0%"
    using_templates: "0%"
    has_owner: "0%"
    has_tags: "0%"

  usage:
    searches_per_week: 0
    failed_searches: 0  # Searches with no results
    top_10_pages: []
    pages_never_accessed: 0

  contribution:
    docs_created_this_month: 0
    docs_updated_this_month: 0
    unique_contributors: 0
    contribution_rate: "0%"  # contributors / total team size
```

## 代码示例 (yaml)

```yaml
knowledge_map:
  engineering:
    produces: ["Architecture docs", "Runbooks", "API specs", "ADRs"]
    consumes_from:
      product: ["PRDs", "User research", "Roadmap"]
      customer_success: ["Bug patterns", "Feature requests", "Usage data"]
      sales: ["Technical requirements", "Integration needs"]

  product:
    produces: ["PRDs", "User research", "Roadmap", "Release notes"]
    consumes_from:
      engineering: ["Technical feasibility", "Architecture constraints"]
      customer_success: ["Feature requests", "Churn reasons"]
      sales: ["Deal requirements", "Competitive intel"]

  customer_success:
    produces: ["FAQ", "Troubleshooting guides", "Best practices"]
    consumes_from:
      engineering: ["Release notes", "Known issues"]
      product: ["Feature docs", "Roadmap"]

  sales:
    produces: ["Battlecards", "Competitive intel", "Use case docs"]
    consumes_from:
      product: ["Feature docs", "Roadmap", "Pricing"]
      customer_success: ["Case studies", "Success metrics"]
      engineering: ["Technical capabilities", "Integration docs"]
```

## 代码示例 (yaml)

```yaml
contribution_workflow:
  create:
    trigger: "New knowledge identified (incident learnings, process change, new tool)"
    steps:
      - choose_template: "Match content type to template"
      - draft: "Write using template structure"
      - self_review: "Run 4C Test checklist"
      - peer_review: "SME validates accuracy"
      - publish: "Add to knowledge base in correct location"
      - announce: "Notify relevant teams/channels"

  update:
    trigger: "Existing doc is wrong, incomplete, or stale"
    steps:
      - flag: "Mark as needs-update with reason"
      - update: "Make changes, update 'Last verified' date"
      - review: "If significant change, get peer review"
      - publish: "Update in place"
      - notify: "If behavioral change, announce"

  retire:
    trigger: "Doc no longer relevant (deprecated system, changed process)"
    steps:
      - mark: "Status: Deprecated, add redirect to replacement"
      - archive: "Move to archive after 30 days"
      - redirect: "Ensure all links point to replacement"
```

## 代码示例 (markdown)

```markdown

**Owner:** [Name]
**Last verified:** [YYYY-MM-DD]
**Estimated time:** [X minutes]
**Difficulty:** Easy | Medium | Advanced

- [ ] [Access/tool/permission needed]
- [ ] [Knowledge assumed]

[Specific instruction with exact commands, clicks, or actions]

[Instructions]

**Expected result:** [What you should see/get]

- [ ] [How to confirm it worked]
- [ ] [What to check]

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| [Symptom] | [Why] | [Steps] |

- [Link to related runbook]
- [Link to reference doc]
```

## 代码示例 (yaml)

```yaml
automation_triggers:
  incident_resolved:
    action: "Create task: 'Write troubleshooting guide for [incident title]'"
    assignee: "Incident commander"
    due: "+10 days"

  new_hire_started:
    action: "Generate personalized onboarding reading list from KB by role"

  doc_stale:
    action: "Notify owner, CC manager if unreviewed after 14 days"

  repeated_question:
    threshold: "Same question asked 3+ times in support/Slack"
    action: "Create task: 'Document answer to [question]'"

  process_changed:
    trigger: "PR merged that changes workflow/process"
    action: "Check if related docs need updating, create task if yes"

  failed_search:
    threshold: "Same search term fails 5+ times/week"
    action: "Flag as gap, create task to write missing doc"
```

## 代码示例 (yaml)

```yaml
knowledge_risk:
  single_points_of_failure:
    - person: "[Name]"
      unique_knowledge: "[What only they know]"
      risk_if_leaves: "high|medium|low"
      extraction_priority: 1
      extraction_method: "interview|shadowing|recording|pair-work"

  undocumented_processes:
    - process: "[Name]"
      frequency: "daily|weekly|monthly|quarterly"
      complexity: "high|medium|low"
      current_owner: "[Name]"
      documentation_priority: 1

  tribal_knowledge:
    - topic: "[What people 'just know']"
      holders: ["[Name1]", "[Name2]"]
      impact_area: "[What breaks without it]"
      capture_method: "interview|workshop|write-up"
```

## 代码示例 (markdown)

```markdown

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-[NNN]
**Date:** [YYYY-MM-DD]
**Deciders:** [Names]

[What situation or problem prompted this decision?]

[What was decided and why?]

| Option | Pros | Cons | Why rejected |
|--------|------|------|-------------|
| [A] | | | |
| [B] | | | |

- **Positive:** [Benefits]
- **Negative:** [Tradeoffs accepted]
- **Risks:** [What could go wrong]

[When should this be revisited?]
```

## 代码示例 (text)

```text
Knowledge Management ROI:

Time Saved:
  Reduced question-answering = [hours/week] × [avg hourly cost] × 52
  Faster onboarding = [weeks saved] × [new hires/year] × [weekly cost]
  Faster incident resolution = [hours saved/incident] × [incidents/year] × [hourly cost]

Risk Reduced:
  Key person dependency = [probability of departure] × [knowledge reconstruction cost]
  Compliance documentation = [audit prep hours saved] × [hourly cost]

Quality Improved:
  Fewer repeated mistakes = [error rate reduction] × [cost per error]
  Consistent processes = [variance reduction] × [rework cost]

Total Annual Value = Time Saved + Risk Reduced + Quality Improved
Investment = Tool cost + Time spent maintaining KB + Training
ROI = (Total Annual Value - Investment) / Investment × 100
```

## 代码示例 (markdown)

```markdown

**Owner:** [Name]
**Last verified:** [YYYY-MM-DD]

[Situation that triggers this decision]

- **If [condition A]** → [Action/next step]
- **If [condition B]** → [Action/next step]
- **If unsure** → [Default action or escalation]

[Continue branching]

[When to ignore this guide and escalate instead]

| Scenario | Decision | Reasoning |
|----------|----------|-----------|
| [Real example] | [What was decided] | [Why] |
```

## 代码示例 (markdown)

```markdown

**Owner:** [Name]
**Last verified:** [YYYY-MM-DD]
**Scope:** [What this covers and doesn't cover]

[1-2 sentence summary of what this reference contains]

| Item | Value | Notes |
|------|-------|-------|
| | | |

[Most frequently needed items at the top]

| Date | Change | By |
|------|--------|-----|
| | | |
```

## 代码示例 (yaml)

```yaml
kb_chatbot:
  flow:
    1_receive_question: "User asks in designated channel"
    2_search: "Semantic search across KB"
    3_respond:
      found_match: "Return relevant doc link + summary"
      partial_match: "Return closest docs + 'Did you mean...?'"
      no_match: "Log as gap, route to human expert, create doc task"
    4_feedback: "Was this helpful? 👍/👎"
    5_improve: "Use feedback to tune search, identify doc improvements"

  sources:
    - knowledge_base_docs
    - slack_saved_answers  # Curated from Slack threads
    - incident_postmortems
    - meeting_notes_tagged_as_knowledge
```

## 代码示例 (yaml)

```yaml
freshness_policy:
  review_frequency:
    critical_operations: "quarterly"  # Deployment, incident response, security
    standard_processes: "semi-annually"  # Regular workflows
    reference_docs: "annually"  # Specs, contacts, architecture
    explanations: "annually"  # Background, history, rationale
  review_process:
    - owner_notified: "2 weeks before due date"
    - review_actions:
        - verify: "Is this still accurate? Test/confirm."
        - update: "Fix any outdated information"
        - stamp: "Update 'Last verified' date"
        - skip: "If can't review, reassign or flag"
    - escalation: "Unreviewed after 30 days → manager notified"
    - stale_threshold: "2x review period without update → flagged as stale"
```

## 代码示例 (text)

```text
**Likely causes (in order of probability):**
1. [Most common cause]
2. [Second most common]
3. [Rare but possible]

**Fix for Cause 1:**
[Step-by-step resolution]

**Fix for Cause 2:**
[Step-by-step resolution]

**Escalation:** If none of the above work → [who to contact, what info to provide]

[Same structure]
```

### Taxonomy Design
```yaml
knowledge_taxonomy:
  types:
    how_to:
      description: "Step-by-step procedures and guides"
      examples: ["Deploy to production", "Process a refund", "Set up dev environment"]
      template: "runbook"

    reference:
      description: "Facts, specs, configurations to look up"
      examples: ["API endpoints", "Config values", "Vendor contacts", "Pricing tables"]
      template: "reference_doc"

    explanation:
      description: "Why things work the way they do"
      examples: ["Architecture decisions", "Policy rationale", "Historical context"]
      template: "explainer"

    decision:
      description: "How to make specific judgment calls"
      examples: ["Escalation criteria", "Approval thresholds", "Priority frameworks"]
      template: "decision_tree"

    troubleshooting:
      description: "Diagnosis and fix for known problems"
      examples: ["Error codes", "Common failures", "Debug procedures"]
      template: "troubleshooting_guide"

  domains:
    - engineering
    - product
    - sales
    - operations
    - finance
    - hr_people
    - customer_success
    - security
    - legal_compliance

  engineering_topics:
    - architecture
    - deployment
    - monitoring
    - incident_response
    - development_workflow
    - testing
    - security
    - infrastructure
```



