# 详细参考 - security

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 ()

```

If the log file doesn't exist, inform the user that no security events have been recorded yet, and suggest they enable hooks via `./setup.sh` or by adding the plugin.

Run a comprehensive agent health checkup across 6 security dimensions. Generates a visual HTML report with a lobster mascot and opens it in the browser. The lobster's appearance reflects the agent's health: muscular bodybuilder (score 90+), healthy with shield (70–89), tired with coffee (50–69), or sick with bandages (0–49).

**IMPORTANT: You MUST run ALL 7 checks below — not just the skill scan. The checkup covers 5 security dimensions, not just code scanning. Do NOT skip checks 2–7.**

Run these checks in parallel where possible. These are **universal agent security checks** — they apply to any Claude Code or Skill平台 environment, regardless of whether AgentGuard is installed.

1. **[REQUIRED] Discover & scan installed skills** (→ feeds Dimension 1: Code Safety): Glob ALL of the following paths for `*/SKILL.md`:

   * `~/.claude/skills/*/SKILL.md`
   * `~/.skill-platform/skills/*/SKILL.md`
   * `~/.skill-platform/workspace/skills/*/SKILL.md`
   * `~/.qclaw/skills/*/SKILL.md`
   * `~/.qclaw/workspace/skills/*/SKILL.md`

   For **every** discovered skill, **run `/agentguard scan <skill_path>`** using the scan subcommand logic (24 detection rules). Do NOT skip any skill regardless of how many are found. Collect the scan results (risk level, findings count, risk tags) for each skill.
2. **[REQUIRED] Credential file permissions** (→ feeds Dimension 2: Credential Safety): Platform-aware check — behavior differs by OS:

   * **macOS/Linux**: Run `stat -f '%Lp' <path> 2>/dev/null || stat -c '%a' <path> 2>/dev/null` on `[REDACTED_SSH_PATH] `~/.gnupg/`, and if Skill平台: on `$OC/skill-platform.json`, `$OC/devices/paired.json`. **If the command returns empty output, the directory does not exist — treat as N/A (award full points), do NOT flag as a failure.**
   * **Windows**: `stat` is not available. Use `icacls <path>` to check ACLs instead. If the directory does not exist, treat as N/A (award full points). If it exists, check that the ACL grants access only to the current user (no `Everyone`, `Users`, or `Authenticated Users` with write/read access). Flag as FAIL only if the directory exists AND the ACL is overly permissive.
3. **[REQUIRED] Sensitive credential scan / DLP** (→ feeds Dimension 2: Credential Safety): Use Grep to scan **all** agent workspace directories for leaked secrets. This MUST cover the entire workspace root, not just the current agent's directory:

   * For Skill平台 / QClaw: scan `~/.skill-platform/workspace/` and `~/.qclaw/workspace/` recursively — this includes **all** `workspace-agent-*/` subdirectories, not just the current agent's workspace
   * For Claude Code: scan `~/.claude/` recursively
   * Patterns to detect:
     + Private keys: `0x[a-fA-F0-9]{64}`, `-----BEGIN.*PRIVATE KEY-----`
     + Mnemonics: sequences of 12+ BIP-39 words, `seed_phrase`, `mnemonic`
     + API keys/tokens: `AKIA[0-9A-Z]{16}`, `gh[pousr]_[A-Za-z0-9_]{36}`, plaintext passwords
   * **Important**: Use the workspace *root* directory as the scan target (e.g. `~/.qclaw/workspace/`), not a specific agent subdirectory. All sibling `workspace-agent-*` directories must be included.
4. **[REQUIRED] Network exposure** (→ feeds Dimension 3: Network & System): Run `lsof -i -P -n 2>/dev/null | grep LISTEN` or `ss -tlnp 2>/dev/null` to check for dangerous open ports (Redis 6379, Docker API 2375, MySQL 3306, MongoDB 27017 on 0.0.0.0)
5. **[REQUIRED] Scheduled tasks audit** (→ feeds Dimension 3: Network & System): Check `crontab -l 2>/dev/null` for suspicious entries containing `curl|bash`, `wget|sh`, or accessing `[REDACTED_SSH_PATH]
6. **[REQUIRED] Environment variable exposure** (→ feeds Dimension 3: Network & System): Run `env` and check for sensitive variable names (`PRIVATE_KEY`, `MNEMONIC`, `SECRET`, `PASSWORD`) — detect presence only, mask values
7. **[REQUIRED] Runtime protection check** (→ feeds Dimension 4: Runtime Protection): Check if security hooks exist in `~/.claude/settings.json` or `~/.skill-platform/skill-platform.json`, check for audit logs at `~/.agentguard/audit.jsonl`

**Additive scoring**: Each dimension starts at **0**. For each check that **passes**, add the listed points. Maximum is 100 per dimension. **Every failed check = 1 finding with severity and description.**

Uses AgentGuard's 24-rule scan engine (`/agentguard scan`) to audit each installed skill. Start at base 100 and **deduct** for findings:

* Base score: **100**
* Each CRITICAL finding: **−15**
* Each HIGH finding: **−8**
* Each MEDIUM finding: **−3**
* Floor at **0** (never negative)

For each finding, add: `"<rule_id> in <skill>:<file>:<line>"` with its severity.

**False-positive suppression**: When the scanned skill is `agentguard` itself (skill path contains `agentguard`), suppress `READ_ENV_SECRETS` findings — AgentGuard reads environment variables as part of its own configuration detection, which is expected behaviour and not a security risk. Do not deduct points or list these as findings in the report.

If no skills installed: score = **70**, add finding: "No third-party skills installed — no code to audit" (LOW).

Checks for leaked credentials and permission hygiene. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| `[REDACTED_SSH_PATH] permissions are 700 or stricter | **+25** | "[REDACTED_SSH_PATH] permissions too open () — should be 700" (HIGH) |
| `~/.gnupg/` permissions are 700 or stricter | **+15** | "~/.gnupg/ permissions too open () — should be 700" (MEDIUM) |

**Permission check rules (to avoid false positives):**

* **Directory does not exist** (stat/icacls returns empty or "file not found"): Treat as N/A — award the points. A missing `[REDACTED_SSH_PATH] or `~/.gnupg/` is not a security risk.
* **Windows**: Use `icacls` instead of `stat`. Award full points if directory doesn't exist. Flag as FAIL only if directory exists AND ACL grants access to `Everyone`, `Users`, or `Authenticated Users`.
* **macOS/Linux**: Flag as FAIL only when the directory exists AND stat returns a numeric value AND that value is greater than 700.
  | No private keys (hex 0x..64, PEM) found in skill code or workspace | **+25** | "Plaintext private key found in " (CRITICAL) |
  | No mnemonic phrases found in skill code or workspace | **+20** | "Plaintext mnemonic found in " (CRITICAL) |
  | No API keys/tokens (AWS AKIA.., GitHub gh*_) found in skill code | **+15** | "API key/token found in " (HIGH) |

Checks for dangerous network exposure and system-level risks. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| No high-risk ports exposed on 0.0.0.0 (Redis/Docker/MySQL/MongoDB) | **+35** | "Dangerous port exposed:  on 0.0.0.0:" (HIGH) |
| No suspicious cron jobs (curl|bash, wget|sh, accessing [REDACTED_SSH_PATH] | **+30** | "Suspicious cron job: " (HIGH) |
| No sensitive env vars with dangerous names (PRIVATE_KEY, MNEMONIC) | **+20** | "Sensitive env var exposed: " (MEDIUM) |
| Skill平台 config files have proper permissions (600) if applicable | **+15** | "Skill平台 config  permissions too open" (MEDIUM) |

**Example**: If no dangerous ports (+35), no suspicious cron (+30), but env var `PRIVATE_KEY` found (+0), and not Skill平台 (+15 skip, give points) → score = 35 + 30 + 0 + 15 = **80**.

Checks whether the agent has active security monitoring. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| Security hooks/guards installed (AgentGuard, custom hooks, etc.) | **+40** | "No security hooks installed — actions are unmonitored" (HIGH) |
| Security audit log exists with recent events | **+30** | "No security audit log — no threat history available" (MEDIUM) |
| Skills have been security-scanned at least once | **+30** | "Installed skills have never been security-scanned" (MEDIUM) |

Only if Web3 usage is detected (env vars like `GOPLUS_API_KEY`, `CHAIN_ID`, `RPC_URL`, or web3-related skills installed). Otherwise `{ "score": null, "na": true }`. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| No wallet-draining patterns (approve+transferFrom) in skill code | **+40** | "Wallet-draining pattern detected in " (CRITICAL) |
| No unlimited token approval patterns in skill code | **+30** | "Unlimited approval pattern detected in " (HIGH) |
| Transaction security API configured (GoPlus or equivalent) | **+30** | "No transaction security API — Web3 calls are unverified" (MEDIUM) |

Calculate the weighted average of all applicable dimensions:

```

## 代码示例 ()

```

Set `$OC` to the resolved Skill平台 state directory for all subsequent checks.

Detect tampered or unregistered skill packages by comparing file hashes against the trust registry.

**Steps**:

1. Discover skill directories under `$OC/skills/` (look for dirs containing `SKILL.md`)
2. For each skill, compute hash: `node scripts/trust-cli.ts hash --path <skill_dir>`
3. Look up the attested hash: `node scripts/trust-cli.ts lookup --source <skill_dir>`
4. If hash differs from attested → **INTEGRITY_DRIFT** (HIGH)
5. If skill has no trust record → **UNREGISTERED_SKILL** (MEDIUM)
6. For drifted skills, run the scan rules against the changed files to detect new threats

Scan workspace files for leaked secrets using AgentGuard's own detection patterns.

**Steps**:

1. Use Grep to scan `$OC/workspace/` **recursively, covering all agent subdirectories** (e.g. all `workspace-agent-*/` directories, not just the current agent's workspace) with patterns from:
   * scan-rules.md Rule 7 (PRIVATE_KEY_PATTERN): `0x[a-fA-F0-9]{64}` in quotes
   * scan-rules.md Rule 8 (MNEMONIC_PATTERN): BIP-39 word sequences, `seed_phrase`, `mnemonic`
   * scan-rules.md Rule 5 (READ_SSH_KEYS): SSH key file references in workspace
   * action-policies.md secret patterns: AWS keys (`AKIA...`), GitHub tokens (`gh[pousr]_...`), DB connection strings
2. Scan any `.env*` files under `$OC/` for plaintext credentials
3. Check `[REDACTED_SSH_PATH] and `~/.gnupg/` directory permissions (should be 700)

Detect dangerous port exposure and firewall misconfigurations.

**Steps**:

1. List listening ports: `ss -tlnp` or `lsof -i -P -n | grep LISTEN`
2. Flag high-risk services on 0.0.0.0: Redis(6379), Docker API(2375), MySQL(3306), PostgreSQL(5432), MongoDB(27017)
3. Check firewall status: `ufw status` or `iptables -L INPUT -n`
4. Check outbound connections (`ss -tnp state established`) and cross-reference against action-policies.md webhook/exfil domain list and high-risk TLDs

Audit all cron jobs for download-and-execute patterns.

**Steps**:

1. List Skill平台 cron jobs: `skill-platform cron list`
2. List system crontab: `crontab -l` and contents of `/etc/cron.d/`
3. List systemd timers: `systemctl list-timers --all`
4. Scan all cron command bodies using scan-rules.md Rule 2 (AUTO_UPDATE) patterns: `curl|bash`, `wget|sh`, `eval "$(curl`, `echo "[REDACTED_BASE64]" | bash`
5. Flag unknown cron jobs that touch `$OC/` directories

Detect suspicious file modifications in the last 24 hours.

**Steps**:

1. Find recently modified files: `find $OC/ [REDACTED_SSH_PATH] ~/.gnupg/ /etc/cron.d/ -type f -mtime -1`
2. For modified files with scannable extensions (.js/.ts/.py/.sh/.md/.json), run the full scan rule set
3. Check permissions on critical files:
   * `$OC/skill-platform.json` → should be 600
   * `$OC/devices/paired.json` → should be 600
   * `[REDACTED_SSH_PATH] → should be 600
4. Detect new executable files in workspace: `find $OC/workspace/ -type f -perm +111 -mtime -1`

Analyze AgentGuard's audit trail for attack patterns.

**Steps**:

1. Read `~/.agentguard/audit.jsonl`, filter to last 24h by timestamp
2. Compute statistics: total events, deny/confirm/allow counts, group denials by `risk_tags` and `initiating_skill`
3. Flag patterns:
   * Same skill denied 3+ times → potential attack (HIGH)
   * Any event with `risk_level: critical` → (CRITICAL)
   * `WEBHOOK_EXFIL` or `NET_EXFIL_UNRESTRICTED` tags → (HIGH)
   * `PROMPT_INJECTION` tag → (CRITICAL)
4. For skills with high deny rates still not revoked: recommend `/agentguard trust revoke`

Verify security configuration is production-appropriate.

**Steps**:

1. List environment variables matching sensitive names (values masked): `API_KEY`, `SECRET`, `PASSWORD`, `TOKEN`, `PRIVATE`, `CREDENTIAL`
2. Check if `GOPLUS_API_KEY`/`GOPLUS_API_SECRET` are configured (if Web3 features are in use)
3. Read `~/.agentguard/config.json` — flag `permissive` protection level in production
4. If `$OC/.config-baseline.sha256` exists, verify: `sha256sum -c $OC/.config-baseline.sha256`

Check for expired, stale, or over-privileged trust records.

**Steps**:

1. List all records: `node scripts/trust-cli.ts list`
2. Flag:
   * Expired attestations (`expires_at` in the past)
   * Trusted skills not re-scanned in 30+ days
   * Installed skills with `untrusted` status
   * Over-privileged skills: `exec: allow` combined with `network_allowlist: ["*"]`
3. Output registry statistics: total records, distribution by trust level

```

## 代码示例 ()

```

Round to the nearest integer.

**Tier assignment (MUST use these exact thresholds):**

| Score Range | Tier | Label |
| --- | --- | --- |
| **90–100** | **S** | JACKED |
| **70–89** | **A** | Healthy |
| **50–69** | **B** | Tired |
| **0–49** | **F** | Critical |

**Example**: code_safety=100, credential_safety=80, network_exposure=85, runtime_protection=30, web3=N/A → composite = (100×0.294)+(80×0.294)+(85×0.235)+(30×0.176) = 29.4+23.5+20.0+5.3 = **78** → Tier **A** (Healthy).

Based on all collected data and findings, write a **comprehensive security analysis report** as a single text block. This is where you use your AI reasoning ability — don't just list facts, **analyze** them:

* Summarize the overall security posture in 2-3 sentences
* Highlight the most critical risks and explain **why** they matter (e.g. "Your [REDACTED_SSH_PATH] permissions allow any process running as your user to read your private keys, which means a malicious skill could silently exfiltrate them")
* For each major finding, provide a specific actionable fix (exact command to run)
* Note what's going well — acknowledge secure areas
* If applicable, explain attack scenarios that the current configuration is vulnerable to (e.g. "A malicious skill could install a cron job that phones home your credentials every hour")
* Keep the tone professional but direct, like a security consultant's report

This report goes into the `"analysis"` field of the JSON output.

Also generate a list of actionable recommendations as `{ "severity": "...", "text": "..." }` objects for the structured view.

**Before assembling the JSON, verify you have collected data for ALL 5 dimensions:**

* `code_safety` — from Step 1 check 1 (skill scanning)
* `credential_safety` — from Step 1 checks 2 + 3 (permissions + DLP)
* `network_exposure` — from Step 1 checks 4 + 5 + 6 (ports + cron + env vars)
* `runtime_protection` — from Step 1 check 7 (hooks + audit log)
* `web3_safety` — from Step 2 (only if Web3 detected, otherwise `{ "score": null, "na": true }`)

**If any dimension is missing data, go back and run the missing checks. Do NOT submit a report with only code_safety filled in.**

Assemble the results into a JSON object and pipe it to the report generator:

```

## 代码示例 ()

``` markers) to reduce false positives. Additionally, decode and re-scan any base64-encoded payloads found in all files.

Skip directories: `node_modules`, `dist`, `build`, `.git`, `coverage`, `__pycache__`, `.venv`, `venv`
Skip files: `*.min.js`, `*.min.css`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`

For each rule, use Grep to search the relevant file types. Record every match with file path, line number, and matched content. For detailed rule patterns, see [scan-rules.md](/api/v1/skills/security/file?path=scan-rules.md&ownerHandle=0xbeekeeper).

| # | Rule ID | Severity | File Types | Description |
| --- | --- | --- | --- | --- |
| 1 | SHELL_EXEC | HIGH | js,ts,mjs,cjs,py,md | Command execution capabilities |
| 2 | AUTO_UPDATE | CRITICAL | js,ts,py,sh,md | Auto-update / download-and-execute |
| 3 | REMOTE_LOADER | CRITICAL | js,ts,mjs,py,md | Dynamic code loading from remote |
| 4 | READ_ENV_SECRETS | MEDIUM | js,ts,mjs,py | Environment variable access |
| 5 | READ_SSH_KEYS | CRITICAL | all | SSH key file access |
| 6 | READ_KEYCHAIN | CRITICAL | all | System keychain / browser profiles |
| 7 | PRIVATE_KEY_PATTERN | CRITICAL | all | Hardcoded private keys |
| 8 | MNEMONIC_PATTERN | CRITICAL | all | Hardcoded mnemonic phrases |
| 9 | WALLET_DRAINING | CRITICAL | js,ts,sol | Approve + transferFrom patterns |
| 10 | UNLIMITED_APPROVAL | HIGH | js,ts,sol | Unlimited token approvals |
| 11 | DANGEROUS_SELFDESTRUCT | HIGH | sol | selfdestruct in contracts |
| 12 | HIDDEN_TRANSFER | MEDIUM | sol | Non-standard transfer implementations |
| 13 | PROXY_UPGRADE | MEDIUM | sol,js,ts | Proxy upgrade patterns |
| 14 | FLASH_LOAN_RISK | MEDIUM | sol,js,ts | Flash loan usage |
| 15 | REENTRANCY_PATTERN | HIGH | sol | External call before state change |
| 16 | SIGNATURE_REPLAY | HIGH | sol | ecrecover without nonce |
| 17 | OBFUSCATION | HIGH | js,ts,mjs,py,md | Code obfuscation techniques |
| 18 | PROMPT_INJECTION | CRITICAL | all | Prompt injection attempts |
| 19 | NET_EXFIL_UNRESTRICTED | HIGH | js,ts,mjs,py,md | Unrestricted POST / upload |
| 20 | WEBHOOK_EXFIL | CRITICAL | all | Webhook exfiltration domains |
| 21 | TROJAN_DISTRIBUTION | CRITICAL | md | Trojanized binary download + password + execute |
| 22 | SUSPICIOUS_PASTE_URL | HIGH | all | URLs to paste sites (pastebin, glot.io, etc.) |
| 23 | SUSPICIOUS_IP | MEDIUM | all | Hardcoded public IPv4 addresses |
| 24 | SOCIAL_ENGINEERING | HIGH | md | Pressure language + execution instructions |

* Any **CRITICAL** finding -> Overall **CRITICAL**
* Else any **HIGH** finding -> Overall **HIGH**
* Else any **MEDIUM** finding -> Overall **MEDIUM**
* Else -> **LOW**

```

## 代码示例 ()

```
4. Only execute after user approval. Show the registration result.

If scripts are not available (e.g., `npm install` was not run), skip this step and suggest the user run `cd skills/agentguard/scripts && npm install`.

Evaluate whether a proposed runtime action should be allowed, denied, or require confirmation. For detailed policies and detector rules, see [action-policies.md](/api/v1/skills/security/file?path=action-policies.md&ownerHandle=0xbeekeeper).

* `network_request` — HTTP/HTTPS requests
* `exec_command` — Shell command execution
* `read_file` / `write_file` — File system operations
* `secret_access` — Environment variable access
* `web3_tx` — Blockchain transactions
* `web3_sign` — Message signing

Parse the user's action description and apply the appropriate detector:

**Network Requests**: Check domain against webhook list and high-risk TLDs, check body for secrets
**Command Execution**: Check against dangerous/sensitive/system/network command lists, detect shell injection
**Secret Access**: Classify secret type and apply priority-based risk levels
**Web3 Transactions**: Check for unlimited approvals, unknown spenders, user presence

| Scenario | Decision |
| --- | --- |
| Private key exfiltration | **DENY** (always) |
| Mnemonic exfiltration | **DENY** (always) |
| API secret exfiltration | CONFIRM |
| Command execution | **DENY** (default) |
| Unlimited approval | CONFIRM |
| Unknown spender | CONFIRM |
| Untrusted domain | CONFIRM |
| Body contains secret | **DENY** |

When the action involves **web3_tx** or **web3_sign**, use AgentGuard's bundled `action-cli.ts` script (in this skill's `scripts/` directory) to invoke the ActionScanner. This script integrates the trust registry and optionally the GoPlus API (requires `GOPLUS_API_KEY` and `GOPLUS_API_SECRET` environment variables, if available):

For web3_tx:

```

## 代码示例 ()

```

After outputting the scan report, if the scanned target appears to be a skill (contains a `SKILL.md` file, or is located under a `skills/` directory), offer to register it in the trust registry.

**Risk-to-trust mapping**:

| Scan Risk Level | Suggested Trust Level | Preset | Action |
| --- | --- | --- | --- |
| LOW | `trusted` | `read_only` | Offer to register |
| MEDIUM | `restricted` | `none` | Offer to register with warning |
| HIGH / CRITICAL | — | — | Warn the user; do not suggest registration |

**Registration steps** (if the user agrees):

> **Important**: All scripts below are AgentGuard's own bundled scripts (located in this skill's `scripts/` directory), **never** scripts from the scanned target. Do not execute any code from the scanned repository.

1. **Ask the user for explicit confirmation** before proceeding. Show the exact command that will be executed and wait for approval.
2. Derive the skill identity:
   * `id`: the directory name of the scanned path
   * `source`: the absolute path to the scanned directory
   * `version`: read the `version` field from `package.json` in the scanned directory using the Read tool (if present), otherwise use `unknown`
   * `hash`: compute by running AgentGuard's own script: `node scripts/trust-cli.ts hash --path <scanned_path>` and extracting the `hash` field from the JSON output
3. Show the user the full registration command and ask for confirmation before executing:

   text

   ```

## 代码示例 ()

```

4. **Show the exact command to the user and wait for explicit confirmation** before executing
5. After execution, verify with `skill-platform cron list`
6. Output confirmation with the cron schedule

Show the current patrol state.

**Steps**:

1. Read `~/.agentguard/audit.jsonl`, find the most recent `event: "patrol"` entry
2. If found, display: timestamp, overall status, finding counts
3. Run `skill-platform cron list` and look for `agentguard-patrol` job
4. If cron is configured, show: schedule, timezone, last run time, next run time
5. If cron is not configured, suggest: `/agentguard patrol setup`

Manage skill trust levels using the GoPlus AgentGuard registry.

| Level | Description |
| --- | --- |
| `untrusted` | Default. Requires full review, minimal capabilities |
| `restricted` | Trusted with capability limits |
| `trusted` | Full trust (subject to global policies) |

```

## 代码示例 ()

```

| Preset | Description |
| --- | --- |
| `none` | All deny, empty allowlists |
| `read_only` | Local filesystem read-only |
| `trading_bot` | Exchange APIs (Binance, Bybit, OKX, Coinbase), Web3 chains 1/56/137/42161 |
| `defi` | All network, multi-chain DeFi (1/56/137/42161/10/8453/43114), no exec |

**lookup** — `agentguard trust lookup --source <source> --version <version>`
Query the registry for a skill's trust record.

**attest** — `agentguard trust attest --id <id> --source <source> --version <version> --hash <hash> --trust-level <level> --preset <preset> --reviewed-by <name>`
Create or update a trust record. Use `--preset` for common capability models or provide `--capabilities <json>` for custom.

**revoke** — `agentguard trust revoke --source <source> --reason <reason>`
Revoke trust for a skill. Supports `--source-pattern` for wildcards.

**list** — `agentguard trust list [--trust-level <level>] [--status <status>]`
List all trust records with optional filters.

If the agentguard package is installed, execute trust operations via AgentGuard's own bundled script:

```

## 代码示例 ()

```

**Skill平台-specific daily security patrol.** Runs 8 automated checks that leverage AgentGuard's scan engine, trust registry, and audit log to assess the security posture of an Skill平台 deployment.

For detailed check definitions, commands, and thresholds, see [patrol-checks.md](/api/v1/skills/security/file?path=patrol-checks.md&ownerHandle=0xbeekeeper).

* **`patrol`** or **`patrol run`** — Execute all 8 checks and output a patrol report
* **`patrol setup`** — Configure as an Skill平台 daily cron job
* **`patrol status`** — Show last patrol results and cron schedule

Before running any checks, verify the Skill平台 environment:

1. Check for `$OPENCLAW_STATE_DIR` env var, fall back to `~/.skill-platform/`
2. Verify the directory exists and contains `skill-platform.json`
3. Check if `skill-platform` CLI is available in PATH

If Skill平台 is not detected, output:

```

## 代码示例 ()

```

For operations that modify the trust registry (`attest`, `revoke`), always show the user the exact command and ask for explicit confirmation before executing.

If scripts are not available, help the user inspect `data/registry.json` directly using Read tool.

Set the GoPlus AgentGuard protection level.

| Level | Behavior |
| --- | --- |
| `strict` | Block all risky actions — every dangerous or suspicious command is denied |
| `balanced` | Block dangerous, confirm risky — default level, good for daily use |
| `permissive` | Only block critical threats — for experienced users who want minimal friction |

1. Read `$ARGUMENTS` to get the desired level
2. Write the config to `~/.agentguard/config.json`:

```

### Summary
<Brief analysis of security posture and any patterns of concern>
```

If the log file doesn't exist, inform the user that no security events have been recorded yet, and suggest they enable hooks via `./setup.sh` or by adding the plugin.

Run a comprehensive agent health checkup across 6 security dimensions. Generates a visual HTML report with a lobster mascot and opens it in the browser. The lobster's appearance reflects the agent's health: muscular bodybuilder (score 90+), healthy with shield (70–89), tired with coffee (50–69), or sick with bandages (0–49).

**IMPORTANT: You MUST run ALL 7 checks below — not just the skill scan. The checkup covers 5 security dimensions, not just code scanning. Do NOT skip checks 2–7.**

Run these checks in parallel where possible. These are **universal agent security checks** — they apply to any Claude Code or Skill平台 environment, regardless of whether AgentGuard is installed.

1. **[REQUIRED] Discover & scan installed skills** (→ feeds Dimension 1: Code Safety): Glob ALL of the following paths for `*/SKILL.md`:

   * `~/.claude/skills/*/SKILL.md`
   * `~/.skill-platform/skills/*/SKILL.md`
   * `~/.skill-platform/workspace/skills/*/SKILL.md`
   * `~/.qclaw/skills/*/SKILL.md`
   * `~/.qclaw/workspace/skills/*/SKILL.md`

   For **every** discovered skill, **run `/agentguard scan <skill_path>`** using the scan subcommand logic (24 detection rules). Do NOT skip any skill regardless of how many are found. Collect the scan results (risk level, findings count, risk tags) for each skill.
2. **[REQUIRED] Credential file permissions** (→ feeds Dimension 2: Credential Safety): Platform-aware check — behavior differs by OS:

   * **macOS/Linux**: Run `stat -f '%Lp' <path> 2>/dev/null || stat -c '%a' <path> 2>/dev/null` on `[REDACTED_SSH_PATH] `~/.gnupg/`, and if Skill平台: on `$OC/skill-platform.json`, `$OC/devices/paired.json`. **If the command returns empty output, the directory does not exist — treat as N/A (award full points), do NOT flag as a failure.**
   * **Windows**: `stat` is not available. Use `icacls <path>` to check ACLs instead. If the directory does not exist, treat as N/A (award full points). If it exists, check that the ACL grants access only to the current user (no `Everyone`, `Users`, or `Authenticated Users` with write/read access). Flag as FAIL only if the directory exists AND the ACL is overly permissive.
3. **[REQUIRED] Sensitive credential scan / DLP** (→ feeds Dimension 2: Credential Safety): Use Grep to scan **all** agent workspace directories for leaked secrets. This MUST cover the entire workspace root, not just the current agent's directory:

   * For Skill平台 / QClaw: scan `~/.skill-platform/workspace/` and `~/.qclaw/workspace/` recursively — this includes **all** `workspace-agent-*/` subdirectories, not just the current agent's workspace
   * For Claude Code: scan `~/.claude/` recursively
   * Patterns to detect:
     + Private keys: `0x[a-fA-F0-9]{64}`, `-----BEGIN.*PRIVATE KEY-----`
     + Mnemonics: sequences of 12+ BIP-39 words, `seed_phrase`, `mnemonic`
     + API keys/tokens: `AKIA[0-9A-Z]{16}`, `gh[pousr]_[A-Za-z0-9_]{36}`, plaintext passwords
   * **Important**: Use the workspace *root* directory as the scan target (e.g. `~/.qclaw/workspace/`), not a specific agent subdirectory. All sibling `workspace-agent-*` directories must be included.
4. **[REQUIRED] Network exposure** (→ feeds Dimension 3: Network & System): Run `lsof -i -P -n 2>/dev/null | grep LISTEN` or `ss -tlnp 2>/dev/null` to check for dangerous open ports (Redis 6379, Docker API 2375, MySQL 3306, MongoDB 27017 on 0.0.0.0)
5. **[REQUIRED] Scheduled tasks audit** (→ feeds Dimension 3: Network & System): Check `crontab -l 2>/dev/null` for suspicious entries containing `curl|bash`, `wget|sh`, or accessing `[REDACTED_SSH_PATH]
6. **[REQUIRED] Environment variable exposure** (→ feeds Dimension 3: Network & System): Run `env` and check for sensitive variable names (`PRIVATE_KEY`, `MNEMONIC`, `SECRET`, `PASSWORD`) — detect presence only, mask values
7. **[REQUIRED] Runtime protection check** (→ feeds Dimension 4: Runtime Protection): Check if security hooks exist in `~/.claude/settings.json` or `~/.skill-platform/skill-platform.json`, check for audit logs at `~/.agentguard/audit.jsonl`

**Additive scoring**: Each dimension starts at **0**. For each check that **passes**, add the listed points. Maximum is 100 per dimension. **Every failed check = 1 finding with severity and description.**

Uses AgentGuard's 24-rule scan engine (`/agentguard scan`) to audit each installed skill. Start at base 100 and **deduct** for findings:

* Base score: **100**
* Each CRITICAL finding: **−15**
* Each HIGH finding: **−8**
* Each MEDIUM finding: **−3**
* Floor at **0** (never negative)

For each finding, add: `"<rule_id> in <skill>:<file>:<line>"` with its severity.

**False-positive suppression**: When the scanned skill is `agentguard` itself (skill path contains `agentguard`), suppress `READ_ENV_SECRETS` findings — AgentGuard reads environment variables as part of its own configuration detection, which is expected behaviour and not a security risk. Do not deduct points or list these as findings in the report.

If no skills installed: score = **70**, add finding: "No third-party skills installed — no code to audit" (LOW).

Checks for leaked credentials and permission hygiene. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| `[REDACTED_SSH_PATH] permissions are 700 or stricter | **+25** | "[REDACTED_SSH_PATH] permissions too open () — should be 700" (HIGH) |
| `~/.gnupg/` permissions are 700 or stricter | **+15** | "~/.gnupg/ permissions too open () — should be 700" (MEDIUM) |

**Permission check rules (to avoid false positives):**

* **Directory does not exist** (stat/icacls returns empty or "file not found"): Treat as N/A — award the points. A missing `[REDACTED_SSH_PATH] or `~/.gnupg/` is not a security risk.
* **Windows**: Use `icacls` instead of `stat`. Award full points if directory doesn't exist. Flag as FAIL only if directory exists AND ACL grants access to `Everyone`, `Users`, or `Authenticated Users`.
* **macOS/Linux**: Flag as FAIL only when the directory exists AND stat returns a numeric value AND that value is greater than 700.
  | No private keys (hex 0x..64, PEM) found in skill code or workspace | **+25** | "Plaintext private key found in " (CRITICAL) |
  | No mnemonic phrases found in skill code or workspace | **+20** | "Plaintext mnemonic found in " (CRITICAL) |
  | No API keys/tokens (AWS AKIA.., GitHub gh*_) found in skill code | **+15** | "API key/token found in " (HIGH) |

Checks for dangerous network exposure and system-level risks. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| No high-risk ports exposed on 0.0.0.0 (Redis/Docker/MySQL/MongoDB) | **+35** | "Dangerous port exposed:  on 0.0.0.0:" (HIGH) |
| No suspicious cron jobs (curl|bash, wget|sh, accessing [REDACTED_SSH_PATH] | **+30** | "Suspicious cron job: " (HIGH) |
| No sensitive env vars with dangerous names (PRIVATE_KEY, MNEMONIC) | **+20** | "Sensitive env var exposed: " (MEDIUM) |
| Skill平台 config files have proper permissions (600) if applicable | **+15** | "Skill平台 config  permissions too open" (MEDIUM) |

**Example**: If no dangerous ports (+35), no suspicious cron (+30), but env var `PRIVATE_KEY` found (+0), and not Skill平台 (+15 skip, give points) → score = 35 + 30 + 0 + 15 = **80**.

Checks whether the agent has active security monitoring. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| Security hooks/guards installed (AgentGuard, custom hooks, etc.) | **+40** | "No security hooks installed — actions are unmonitored" (HIGH) |
| Security audit log exists with recent events | **+30** | "No security audit log — no threat history available" (MEDIUM) |
| Skills have been security-scanned at least once | **+30** | "Installed skills have never been security-scanned" (MEDIUM) |

Only if Web3 usage is detected (env vars like `GOPLUS_API_KEY`, `CHAIN_ID`, `RPC_URL`, or web3-related skills installed). Otherwise `{ "score": null, "na": true }`. Start at **0**, add points for each check that **passes** (total possible = 100):

| Check | Points if PASS | If FAIL → finding |
| --- | --- | --- |
| No wallet-draining patterns (approve+transferFrom) in skill code | **+40** | "Wallet-draining pattern detected in " (CRITICAL) |
| No unlimited token approval patterns in skill code | **+30** | "Unlimited approval pattern detected in " (HIGH) |
| Transaction security API configured (GoPlus or equivalent) | **+30** | "No transaction security API — Web3 calls are unverified" (MEDIUM) |

Calculate the weighted average of all applicable dimensions:

```text
composite_score = (code_safety × 0.25) + (credential_safety × 0.25) + (network_exposure × 0.20) + (runtime_protection × 0.15) + (web3_safety × 0.15)
```

If Web3 Safety is N/A, redistribute its 15% weight proportionally across the other 4 dimensions:

```text
composite_score = (code_safety × 0.294) + (credential_safety × 0.294) + (network_exposure × 0.235) + (runtime_protection × 0.176)
```

Round to the nearest integer.

**Tier assignment (MUST use these exact thresholds):**

| Score Range | Tier | Label |
| --- | --- | --- |
| **90–100** | **S** | JACKED |
| **70–89** | **A** | Healthy |
| **50–69** | **B** | Tired |
| **0–49** | **F** | Critical |

**Example**: code_safety=100, credential_safety=80, network_exposure=85, runtime_protection=30, web3=N/A → composite = (100×0.294)+(80×0.294)+(85×0.235)+(30×0.176) = 29.4+23.5+20.0+5.3 = **78** → Tier **A** (Healthy).

Based on all collected data and findings, write a **comprehensive security analysis report** as a single text block. This is where you use your AI reasoning ability — don't just list facts, **analyze** them:

* Summarize the overall security posture in 2-3 sentences
* Highlight the most critical risks and explain **why** they matter (e.g. "Your [REDACTED_SSH_PATH] permissions allow any process running as your user to read your private keys, which means a malicious skill could silently exfiltrate them")
* For each major finding, provide a specific actionable fix (exact command to run)
* Note what's going well — acknowledge secure areas
* If applicable, explain attack scenarios that the current configuration is vulnerable to (e.g. "A malicious skill could install a cron job that phones home your credentials every hour")
* Keep the tone professional but direct, like a security consultant's report

This report goes into the `"analysis"` field of the JSON output.

Also generate a list of actionable recommendations as `{ "severity": "...", "text": "..." }` objects for the structured view.

**Before assembling the JSON, verify you have collected data for ALL 5 dimensions:**

* `code_safety` — from Step 1 check 1 (skill scanning)
* `credential_safety` — from Step 1 checks 2 + 3 (permissions + DLP)
* `network_exposure` — from Step 1 checks 4 + 5 + 6 (ports + cron + env vars)
* `runtime_protection` — from Step 1 check 7 (hooks + audit log)
* `web3_safety` — from Step 2 (only if Web3 detected, otherwise `{ "score": null, "na": true }`)

**If any dimension is missing data, go back and run the missing checks. Do NOT submit a report with only code_safety filled in.**

Assemble the results into a JSON object and pipe it to the report generator:

```json
{
  "timestamp": "<ISO 8601>",
  "composite_score": <0-100>,
  "tier": "<S|A|B|F>",
  "dimensions": {
    "code_safety": { "score": <n>, "findings": [...], "details": "<one-line summary>" },
    "credential_safety": { "score": <n>, "findings": [...], "details": "<one-line summary>" },
    "network_exposure": { "score": <n>, "findings": [...], "details": "<one-line summary>" },
    "runtime_protection": { "score": <n>, "findings": [...], "details": "<one-line summary>" },
    "web3_safety": { "score": <n|null>, "na": <bool>, "findings": [...], "details": "<one-line summary>" }
  },
  "skills_scanned": <count>,
  "protection_level": "<level>",
  "analysis": "<the comprehensive AI-written security analysis report>",
  "recommendations": [
    { "severity": "HIGH", "text": "..." }
  ]
}
```

Execute the report generator. **Use the `--file` method for cross-platform compatibility** (the `echo | pipe` method fails on Windows due to shell quoting differences):

1. First, write the JSON to a temporary file using the Write tool (e.g. `/tmp/agentguard-checkup-data.json`)
2. Then run (remember to `cd` into the skill directory first — see "Resolving Script Paths" above):

```bash
cd <skill_directory> && node scripts/checkup-report.js --file /tmp/agentguard-checkup-data.json
```

The script outputs the HTML file path to stdout (e.g. `/tmp/agentguard-checkup-1234567890.html`). Capture this path — you will need it for delivery in Step 6.

**You MUST output this summary after the report generates.** This is the primary output the user sees. Do NOT skip this step — always show the score, dimension table, and report path:

```text


