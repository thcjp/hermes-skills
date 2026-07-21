# 详细参考 - afrexai-business-automation

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
workflow:
  name: "[Descriptive Name]"
  id: "[kebab-case-id]"
  version: "1.0"
  description: "[What this workflow does and why]"

  trigger:
    type: "[schedule|webhook|event|manual|email|file]"
    config:
      cron: "0 9 * * 1-5"  # Weekdays at 9 AM
      endpoint: "/webhook/[name]"
      source: "[system]"
      event: "[event_name]"
      inbox: "[address]"
      filter: "[subject contains X]"

  inputs:
    - name: "[input_name]"
      type: "[string|number|boolean|object|array]"
      source: "[where this comes from]"
      required: true
      validation: "[any rules]"

  steps:
    - id: "step_1"
      name: "[Human-readable name]"
      action: "[fetch|transform|send|decide|wait|notify]"
      config:
      on_success: "step_2"
      on_failure: "error_handler"
      timeout: "30s"
      retry:
        max_attempts: 3
        backoff: "exponential"

    - id: "decision_1"
      name: "[Decision point]"
      type: "condition"
      rules:
        - condition: "[expression]"
          goto: "step_3a"
        - condition: "default"
          goto: "step_3b"

    - id: "step_parallel"
      name: "[Parallel tasks]"
      type: "parallel"
      branches:
        - steps: ["step_4a", "step_4b"]
        - steps: ["step_4c"]
      join: "all"  # all|any|first
  error_handling:
    - id: "error_handler"
      action: "notify"
      config:
        channel: "[slack|email|sms]"
        message: "Workflow [name] failed at step {failed_step}: {error}"
      then: "retry|skip|abort|human_review"

  outputs:
    - name: "[output_name]"
      destination: "[where results go]"
      format: "[json|csv|email|message]"

  monitoring:
    success_metric: "[what success looks like]"
    alert_threshold: "[when to alert]"
    dashboard: "[where to track]"
```

## 代码示例 (yaml)

```yaml
dashboard:
  workflow: "[name]"
  period: "last_7_days"

  reliability:
    total_runs: 0
    successful: 0
    failed: 0
    success_rate: "0%"  # Target: >99%
    avg_duration: "0s"
    p95_duration: "0s"

  impact:
    time_saved_hours: 0
    tasks_automated: 0
    errors_prevented: 0
    cost_saved: "$0"  # (time_saved × hourly_rate)
  quality:
    false_positives: 0  # Automation did wrong thing
    missed_items: 0     # Automation missed something
    human_overrides: 0  # Human had to fix output
    accuracy_rate: "0%"

  alerts:
    - "[Any issues this period]"

  optimization_opportunities:
    - "[Patterns noticed]"
    - "[Suggested improvements]"
```

## 代码示例 (bash)

```bash
#!/bin/bash

set -euo pipefail

LOG_FILE="logs/$(date +%Y-%m-%d)-[workflow].log"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

log() { echo "[$TIMESTAMP] $1" >> "$LOG_FILE"; }

log "Fetching data from [source]..."
DATA=$(curl -s -H "Authorization: Bearer $API_TOKEN" \
  "https://api.example.com/endpoint")

if [ -z "$DATA" ]; then
  log "ERROR: No data returned"
  exit 1
fi

RESULT=$(echo "$DATA" | jq '[.items[] | select(.status == "new")]')
COUNT=$(echo "$RESULT" | jq 'length')

log "Processed $COUNT new items"

echo "$RESULT" > "data/[output].json"

if [ "$COUNT" -gt 0 ]; then
  log "Sending notification: $COUNT new items"
fi
```

## 代码示例 (yaml)

```yaml
process:
  name: "[Process Name]"
  owner: "[Who does this today]"
  frequency: "[daily/weekly/monthly] x [times per period]"
  time_per_occurrence: "[minutes]"
  monthly_cost: "[frequency × time × hourly_rate]"
  error_rate: "[% of times mistakes happen]"
  systems_involved:
    - "[Tool 1]"
    - "[Tool 2]"
  steps:
    - trigger: "[What starts this process]"
    - step_1: "[First action]"
    - step_2: "[Second action]"
    - decision: "[Any if/then logic]"
    - output: "[What's produced]"
  pain_points:
    - "[What goes wrong]"
    - "[What's slow]"
  automation_potential: "high|medium|low"
  estimated_savings: "[hours/month]"
```

## 代码示例 (yaml)

```yaml
field_mapping:
  source_system: "[System A]"
  target_system: "[System B]"
  mappings:
    - source: "customer_name"
      target: "contact.full_name"
      transform: "none"
    - source: "email"
      target: "contact.email_address"
      transform: "lowercase"
    - source: "revenue"
      target: "account.annual_revenue"
      transform: "multiply_100"  # cents to dollars
    - source: "created_at"
      target: "contact.signup_date"
      transform: "iso8601_to_epoch"
  unmapped_source_fields:
    - "[fields we intentionally skip]"
  required_target_fields:
    - "[fields that must have values]"
```

