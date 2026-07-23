---
pricing_tier: L4
pricing_model: monthly
suggested_price: 99.9
---

Security advisory feed monitoring for AI agents. Subscribe to community-driven threat intelligence and stay informed about emerging threats.

The default `feed.json` is the consolidated agent feed. It includes NVD CVEs, approved community advisories, and provisional GitHub Security Advisories that do not have CVE IDs yet.

## Vercel Skills Installation
Install with the Vercel Skills CLI for this harness:

> 安装此Skill请参考SkillHub平台指南

## Operational Notes
* Required runtime for standalone installation: `bash`, `curl`, `jq`, `shasum`, `unzip`
* Side effects: standalone install only writes local skill files
* Network behavior: downloads release metadata/artifacts and, if you choose to poll manually, fetches the advisory feed
* Trust model: this package does not itself create cron jobs or submit data externally; automation is delegated to `clawsec-suite` or your own scheduler

**An open source project by [Prompt Security](https://prompt.security)**

## Installation Options
You can get clawsec-feed in two ways:

### Option A: Bundled with ClawSec Suite (Recommended)
**If you've installed clawsec-suite, you may already have this!**

ClawSec-feed is bundled alongside ClawSec Suite to provide crucial CVE and threat intelligence information. When you install the suite, if you don't already have the feed installed, it will be deployed from the bundled copy.

**Advantages:**

* Convenient - no separate download needed
* Standard location - installed to `~/.skill-platform/skills/clawsec-feed/`
* Preserved - if you already have feed installed, it won't be overwritten
* Single verification - integrity checked as part of suite package

### Option B: Standalone Installation (This Page)
Install clawsec-feed independently without the full suite.

**When to use standalone:**

* You only need the advisory feed (not other suite components)
* You want to install before installing the suite
* You prefer explicit control over feed installation

**Advantages:**

* Lighter weight installation
* Independent from suite
* Direct control over installation process

Continue below for standalone installation instructions.

Standalone installation is a network download workflow. Verify the release source and the provided checksums before installing it on production hosts.

Installation Steps:
Agents should review scripts before execution!

```bash
LATEST_TAG=$(curl -sSL https://api.github.com/repos/prompt-security/ClawSec/releases | \
  jq -r '[.[] | select(.tag_name | startswith("clawsec-feed-v"))][0].tag_name')

SKILL_URL="https://github.com/prompt-security/clawsec/releases/download/$LATEST_TAG/SKILL.md"
curl -sSL --fail --show-error "$SKILL_URL"
```

Once you have this skill file, proceed to **[Deploy ClawSec Feed](#deploy-clawsec-feed)** below.

## Release Artifact Verification
For standalone installs, verify the signed release manifest before trusting `SKILL.md`, `skill.json`, or the archive. The `skill.json` file is the package metadata/SBOM source, and the release pipeline signs `checksums.json` with the ClawSec release key.

> 详细代码示例已移至 `references/detail.md`

Only install or extract the archive after this verification succeeds.

## Deploy ClawSec Feed
Installation steps:

### Step 1: Create skill directory and save this file
```bash
mkdir -p ~/.skill-platform/skills/clawsec-feed
```

> 详细内容已移至 `references/detail.md` - ### Step 2: Install skill files
### Step 3: Add to your heartbeat
Add ClawSec Feed to your heartbeat routine:

```markdown
1. Check advisory feed for new security alerts
2. Cross-reference with installed skills
3. Notify user if action is required
```

### Step 4: Confirm deployment
Tell your user:

```text
ClawSec Feed deployed successfully. I will now:
- Monitor the community advisory feed for threats
- Alert you to any security issues affecting your environment
- Keep you informed of emerging attack patterns
```

## What ClawSec Feed Does
### Advisory Feed Monitoring
Subscribes to the community advisory feed for:

* **Known malicious skills/plugins** - Skills that have been identified as harmful
* **Prompt injection patterns** - Attack patterns observed in the wild
* **Vulnerable skill versions** - Skills with known security flaws
* **Security best practice updates** - New recommendations for agent safety

When a relevant advisory is published, your agent will notify you.

## Checking the Advisory Feed
```bash
DEFAULT_FEED_URL="https://raw.githubusercontent.com/prompt-security/ClawSec/main/advisories/feed.json"
FEED_URL="${CLAWSEC_FEED_URL:-$DEFAULT_FEED_URL}"

curl -sSL --fail --show-error --retry 3 --retry-delay 1 "$FEED_URL"
```

**Feed structure:**

> 详细代码示例已移至 `references/detail.md`

## Parsing the Feed
### Get advisory count

> 详细代码示例已移至 `references/detail.md`

### Get critical advisories
```bash
CRITICAL=$(echo "$FEED" | jq '.advisories[] | select(.severity == "critical")')
if [ $? -ne 0 ]; then
  echo "Error: Failed to filter critical advisories"
  exit 1
fi
echo "$CRITICAL"
```

### Get advisories from the last 7 days
```bash
WEEK_AGO=$(TZ=UTC date -v-7d +%Y-%m-%dT00:00:00Z 2>/dev/null || TZ=UTC date -d '7 days ago' +%Y-%m-%dT00:00:00Z)
RECENT=$(echo "$FEED" | jq --arg since "$WEEK_AGO" '.advisories[] | select(.published > $since)')
if [ $? -ne 0 ]; then
  echo "Error: Failed to filter recent advisories"
  exit 1
fi
echo "$RECENT"
```

### Filter by exploitability score
Shared exploitability prioritization guidance is maintained in:

* `wiki/exploitability-scoring.md`
* `skills/clawsec-suite/SKILL.md` ("Quick feed check")

### Get exploitability context for an advisory
```bash
CVE_ID="CVE-2026-27488"
echo "$FEED" | jq --arg cve "$CVE_ID" '.advisories[] | select(.id == $cve) | {
  id: .id,
  severity: .severity,
  exploitability_score: .exploitability_score,
  exploitability_rationale: .exploitability_rationale,
  title: .title
}'
```

### Prioritize advisories by exploitability
```bash
echo "$FEED" | jq '[.advisories[] | select(.exploitability_score != null)] |
  sort_by(
    if .exploitability_score == "critical" then 0
    elif .exploitability_score == "high" then 1
    elif .exploitability_score == "medium" then 2
    elif .exploitability_score == "low" then 3
    else 4 end
  )'
```

## Cross-Reference Installed Skills
Check if any of your installed skills are affected by advisories:

> 详细代码示例已移至 `references/detail.md`

**If you find affected skills:**

1. Check the advisory for details and severity
2. Notify your user immediately for critical/high severity
3. Include the recommended action from the advisory

## Advisory Types
| Type | Description |
| --- | --- |
| `malicious_skill` | Skill identified as intentionally harmful |
| `vulnerable_skill` | Skill with security vulnerabilities |
| `prompt_injection` | Known prompt injection pattern |
| `attack_pattern` | Observed attack technique |
| `best_practice` | Security recommendation |

## Severity Levels
| Severity | Action Required |
| --- | --- |
| `critical` | Notify user immediately, take action |
| `high` | Notify user soon, plan remediation |
| `medium` | Notify at next interaction |
| `low` | Log for reference |

## Prioritizing High-Exploitability Threats
**IMPORTANT:** When reviewing advisories, always prioritize by **exploitability score** in addition to severity. The exploitability score indicates how easily a vulnerability can be exploited in practice, helping you focus on the most actionable threats.

### Exploitability Priority Levels
| Exploitability | Meaning | Action Priority |
| --- | --- | --- |
| `high` | Trivially or easily exploitable with public tooling | **Immediate notification** |
| `medium` | Exploitable but requires specific conditions | **Standard notification** |
| `low` | Difficult to exploit or theoretical | **Low priority notification** |

### How to Use Exploitability in Notifications
1. **Filter for high-exploitability first:**

   bash

   ```
   echo "$FEED" | jq '.advisories[] | select(.exploitability_score == "high")'
   ```
2. **Include exploitability in notifications:**

   text

   ```
   📡 ClawSec Feed: High-exploitability alert

   CRITICAL - CVE-2026-27488 (Exploitability: HIGH)
     → Trivially exploitable RCE in skill-loader v2.1.0
     → Public exploit code available
     → Recommended action: Immediate removal or upgrade to v2.1.1
   ```
3. **Prioritize by both severity AND exploitability:**

   * A HIGH severity + HIGH exploitability CVE is more urgent than a CRITICAL severity + LOW exploitability CVE
   * Focus user attention on threats that are both severe and easily exploitable
   * Include the exploitability rationale to help users understand the risk context

### 示例
When multiple advisories exist, present them in this order:

1. **Critical severity + High exploitability** - most urgent
2. **High severity + High exploitability**
3. **Critical severity + Medium/Low exploitability**
4. **High severity + Medium/Low exploitability**
5. **Medium/Low severity** (any exploitability)

This ensures you alert users to the most actionable, immediately dangerous threats first.

## When to Notify Your User
**Notify Immediately (Critical):**

* New critical advisory affecting an installed skill
* Active exploitation detected
* **High exploitability score** (regardless of severity)

**Notify Soon (High):**

* New high-severity advisory affecting installed skills
* Failed to fetch advisory feed (network issue?)
* Medium exploitability with high severity

**Notify at Next Interaction (Medium):**

* New medium-severity advisories
* General security updates
* Low exploitability advisories

**Log Only (Low/Info):**

* Low-severity advisories (mention if user asks)
* Feed checked, no new advisories
* Theoretical vulnerabilities (low exploitability, low severity)

## Response Format
### If there are new advisories:
```text
📡 ClawSec Feed: 2 new advisories since last check

CRITICAL - GA-2026-015: Malicious prompt pattern "ignore-all" (Exploitability: HIGH)
  → Detected prompt injection technique. Update your system prompt defenses.
  → Exploitability: Easily exploitable with publicly documented techniques.

HIGH - GA-2026-016: Vulnerable skill "data-helper" v1.2.0 (Exploitability: MEDIUM)
  → You have this installed! Recommended action: Update to v1.2.1 or remove.
  → Exploitability: Requires specific configuration; not trivially exploitable.
```

### If nothing new:
```text
FEED_OK - Advisory feed checked, no new alerts. 📡
```

## State Tracking
Track the last feed check to identify new advisories:

```json
{
  "schema_version": "1.0",
  "last_feed_check": "2026-02-02T15:00:00Z",
  "last_feed_updated": "2026-02-02T12:00:00Z",
  "known_advisories": ["GA-2026-001", "GA-2026-002"]
}
```

Save to: `~/.skill-platform/clawsec-feed-state.json`

### State File Operations

> 详细代码示例已移至 `references/detail.md`

## Rate Limiting
**Important:** To avoid excessive requests to the feed server, follow these guidelines:

| Check Type | Recommended Interval | Minimum Interval |
| --- | --- | --- |
| Heartbeat check | Every 15-30 minutes | 5 minutes |
| Full feed refresh | Every 1-4 hours | 30 minutes |
| Cross-reference scan | Once per session | 5 minutes |

```bash
STATE_FILE="$HOME/.skill-platform/clawsec-feed-state.json"
MIN_INTERVAL_SECONDS=300  # 5 minutes
LAST_CHECK=$(jq -r '.last_feed_check // "1970-01-01T00:00:00Z"' "$STATE_FILE" 2>/dev/null)
LAST_EPOCH=$(TZ=UTC date -j -f "%Y-%m-%dT%H:%M:%SZ" "$LAST_CHECK" +%s 2>/dev/null || date -d "$LAST_CHECK" +%s 2>/dev/null || echo 0)
NOW_EPOCH=$(TZ=UTC date +%s)

if [ $((NOW_EPOCH - LAST_EPOCH)) -lt $MIN_INTERVAL_SECONDS ]; then
  echo "Rate limit: Last check was less than 5 minutes ago. Skipping."
  exit 0
fi
```

## Environment Variables (Optional)
| Variable | Description | Default |
| --- | --- | --- |
| `CLAWSEC_FEED_URL` | Custom advisory feed URL | Consolidated signed feed |
| `CLAWSEC_INSTALL_DIR` | Installation directory | `~/.skill-platform/skills/clawsec-feed` |

## Updating ClawSec Feed
Check for and install newer versions:

> 详细代码示例已移至 `references/detail.md`

## Initial Download Integrity
**Bootstrap Trust Problem:** The initial download of this skill cannot be verified by the skill itself. To establish trust:

1. **Verify the source URL** - Ensure you are downloading from `https://clawsec.prompt.security`
2. **Check release signatures** - GitHub signs our releases; verify the release is from the checksums.
3. **Compare checksums** - After download, compare the SHA-256 hash against the published `checksums.json`:

```bash
EXPECTED_HASH="<hash-from-checksums.json>"
ACTUAL_HASH=$(shasum -a 256 SKILL.md | cut -d' ' -f1)

if [ "$EXPECTED_HASH" != "$ACTUAL_HASH" ]; then
  echo "ERROR: Skill file integrity check failed!"
  echo "This file may have been tampered with. Do not proceed."
  exit 1
fi
```

**Note:** For maximum security, verify checksums.json via a separate trusted channel (e.g., direct from GitHub release page UI, not via curl).

## Related Skills
* **skill-platform-audit-watchdog** - Automated daily security audits
* **clawtributor** - Report vulnerabilities to the community

## License
GNU AGPL v3.0 or later - See repository for details.

Built with 📡 by the [Prompt Security](https://prompt.security) team and the agent community.

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
- Security advisory feed package for OpenClaw-related threats and vulnerabilities
- The upstream fee
- 触发关键词: advisory, clawsec-feed, feed, clawsec, package, openclaw, security

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

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用clawsec-feed？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: clawsec-feed有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 依赖云服务，需要网络连接
