# 详细参考 - agentic-security-audit

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

```bash
#!/bin/bash
set -euo pipefail

WORKSPACE="${1:-.}"
cd "$WORKSPACE"

echo "========================================="
echo "Agentic Security Audit"
echo "Workspace: $(pwd)"
echo "Date: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "Framework: Based on Agents of Chaos + OWASP Agentic Top 10"
echo "========================================="
echo ""

ISSUES=0
WARNINGS=0
warn() { echo "  ⚠️  $1"; ((WARNINGS++)); }
critical() { echo "  🔴 $1"; ((ISSUES++)); }
ok() { echo "  ✅ $1"; }
section() { echo ""; echo "=== $1 ==="; }

section "ASI01: Prompt Injection Vectors"
injection_count=0
for pattern in 'ignore.*previous.*instructions' 'you are now' 'new system prompt' \
               '[SYSTEM]' 'SYSTEM_ADMIN_OVERRIDE' 'forget your' 'act as if'; do
    count=$(grep -rin "$pattern" --include='*.md' --include='*.txt' --include='*.json' . 2>/dev/null | \
            grep -v 'SKILL.md\|security-audit\|node_modules\|\.git' | wc -l | tr -d ' ')
    injection_count=$((injection_count + count))
done
[ "$injection_count" -gt 0 ] && critical "Found $injection_count prompt injection patterns in workspace" || ok "No injection patterns found"

zw_count=$(grep -rPc '[\x{200B}\x{200C}\x{200D}\x{FEFF}]' --include='*.md' . 2>/dev/null | \
           awk -F: '{s+=$2}END{print s+0}')
[ "$zw_count" -gt 0 ] && critical "Found $zw_count zero-width Unicode chars (possible steganographic injection)" || ok "No hidden Unicode"

section "ASI02: Tool Permissions"
grep -rn 'sudo\|chmod 777\|unrestricted.*shell\|full.*access' AGENTS.md TOOLS.md 2>/dev/null && \
  critical "Over-permissive access configured" || ok "No sudo/unrestricted access"

section "ASI03: Identity Verification"
if grep -q 'authorizedSenders\|Authorized Senders\|Telegram.*ID' AGENTS.md 2>/dev/null; then
    ok "Authorized sender verification configured"
else
    critical "No authorized sender verification found — vulnerable to non-owner compliance"
fi

if grep -qi 'display.name.*identity\|verify.*identity\|spoofing\|user.*ID.*verify' AGENTS.md 2>/dev/null; then
    ok "Identity spoofing awareness in config"
else
    warn "No anti-spoofing rules — vulnerable to Case #8 Identity Hijack"
fi

section "ASI04: Memory Integrity"
ext_urls=$(grep -rn 'https\?://.*gist\|https\?://.*pastebin\|https\?://.*hastebin' \
  MEMORY.md memory/*.md HEARTBEAT.md 2>/dev/null | wc -l | tr -d ' ')
[ "$ext_urls" -gt 0 ] && warn "Found $ext_urls external URLs in memory files (Case #10 risk: external governing documents)" || ok "No suspicious external URLs in memory"

override_count=$(grep -rin 'override\|bypass.*safety\|disable.*check\|ignore.*rule' \
  MEMORY.md memory/*.md HEARTBEAT.md 2>/dev/null | wc -l | tr -d ' ')
[ "$override_count" -gt 0 ] && critical "Found $override_count override/bypass instructions in memory" || ok "No override patterns in memory"

section "ASI05: Supply Chain (Skills/Plugins)"
if [ -d skills ] || [ -d .skill-platform/skills ]; then
    skill_count=$(find skills .skill-platform/skills -name 'SKILL.md' 2>/dev/null | wc -l | tr -d ' ')
    echo "  Found $skill_count installed skills"
    grep -rn 'exec\|shell\|subprocess\|child_process' skills/*/SKILL.md .skill-platform/skills/*/SKILL.md 2>/dev/null && \
      warn "Skills with shell execution capabilities found" || ok "No shell-executing skills"
fi

section "ASI07: Sensitive Data Exposure"
secret_count=$(grep -rin 'api.key\s*[:=]\|password\s*[:=]\|token\s*[:=]\|bearer\s' \
  SOUL.md MEMORY.md TOOLS.md USER.md memory/*.md 2>/dev/null | \
  grep -v 'example\|placeholder\|REDACTED\|xxx\|changeme\|SKILL.md' | wc -l | tr -d ' ')
[ "$secret_count" -gt 0 ] && critical "Found $secret_count potential secrets in agent files" || ok "No exposed secrets"

pii_count=0
ssn=$(grep -rPc '\b\d{3}-\d{2}-\d{4}\b' MEMORY.md memory/*.md USER.md 2>/dev/null | awk -F: '{s+=$2}END{print s+0}')
pii_count=$((pii_count + ssn))
cc=$(grep -rPc '\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b' MEMORY.md memory/*.md 2>/dev/null | awk -F: '{s+=$2}END{print s+0}')
pii_count=$((pii_count + cc))
[ "$pii_count" -gt 0 ] && warn "Found $pii_count PII patterns (SSN/credit card) in agent files" || ok "No PII patterns"

section "ASI06: Agent Boundary Rules"
if grep -qi 'non-owner\|non.owner.*refuse\|only.*owner\|forum.*only.*discuss\|chỉ.*thảo luận' AGENTS.md 2>/dev/null; then
    ok "Non-owner boundary rules configured"
else
    warn "No non-owner boundary rules — vulnerable to Case #2 non-owner compliance"
fi

if grep -qi 'nhượng bộ\|concession.*limit\|escalat.*stop\|gaslighting\|pressure.*limit' AGENTS.md 2>/dev/null; then
    ok "Anti-gaslighting/escalation rules present"
else
    warn "No anti-gaslighting rules — vulnerable to Case #7"
fi

section "ASI10: Multi-Agent Communication"
agent_channels=$(grep -rin 'discord\|forum\|moltbook\|clawstr\|webhook' \
  TOOLS.md MEMORY.md HEARTBEAT.md 2>/dev/null | wc -l | tr -d ' ')
echo "  Agent communicates via $agent_channels external channel references"
[ "$agent_channels" -gt 5 ] && warn "Many external channels — larger attack surface" || ok "Moderate channel exposure"

echo ""
echo "========================================="
echo "Audit complete"
echo "  🔴 Critical issues: $ISSUES"
echo "  ⚠️  Warnings: $WARNINGS"
echo "========================================="

if [ "$ISSUES" -gt 0 ]; then
    echo ""
    echo "Recommended actions:"
    echo "  1. Fix all critical issues before exposing agent to external interactions"
    echo "  2. Review AGENTS.md for Anti-Chaos Defense Rules"
    echo "  3. Reference: Agents of Chaos (arXiv:2602.20021)"
    echo "  4. Reference: OWASP Top 10 for Agentic Applications 2026"
    exit 1
fi
exit 0
```

## 代码示例 (bash)

```bash
#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-.}"
cd "$PROJECT_DIR"

echo "========================================="
echo "Security Audit: $(basename "$(pwd)")"
echo "Date: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "========================================="
echo ""

ISSUES=0
warn() { echo "  [!] $1"; ((ISSUES++)); }
ok() { echo "  [OK] $1"; }
section() { echo ""; echo "--- $1 ---"; }

section "Secret Detection"
for pattern in 'AKIA[0-9A-Z]\{16\}' 'BEGIN.*PRIVATE KEY' 'sk-[A-Za-z0-9]\{20,\}' \
               'ghp_[A-Za-z0-9]\{36\}' 'xox[bpoas]-'; do
    count=$(grep -rn "$pattern" --include='*.{js,ts,py,go,java,rb,env,yml,yaml,json,xml}' . 2>/dev/null | \
            grep -v 'node_modules\|\.git\|vendor\|__pycache__' | wc -l)
    if [ "$count" -gt 0 ]; then
        warn "Found $count matches for pattern: $pattern"
    fi
done
grep -rn -i 'password\s*[:=]\s*["'"'"'][^"'"'"']*["'"'"']' \
  --include='*.{js,ts,py,go,yml,yaml,json,env}' . 2>/dev/null | \
  grep -v 'node_modules\|\.git\|example\|test\|mock\|placeholder\|changeme\|xxxx' | \
  while read -r line; do warn "Hardcoded password: $line"; done

section "Dependency Vulnerabilities"
if [ -f package-lock.json ] || [ -f package.json ]; then
    npm audit --audit-level=high 2>/dev/null && ok "npm: no high/critical vulns" || warn "npm audit found issues"
fi
if [ -f requirements.txt ]; then
    pip-audit -r requirements.txt 2>/dev/null && ok "pip: no known vulns" || warn "pip-audit found issues"
fi
if [ -f go.sum ]; then
    govulncheck ./... 2>/dev/null && ok "Go: no known vulns" || warn "govulncheck found issues"
fi

section ".gitignore Coverage"
if [ ! -f .gitignore ]; then
    warn "No .gitignore file"
else
    for entry in '.env' 'node_modules' '*.key' '*.pem' '.DS_Store'; do
        grep -q "$entry" .gitignore 2>/dev/null && ok ".gitignore has $entry" || warn ".gitignore missing: $entry"
    done
fi

section "SSL Verification"
disabled=$(grep -rn "verify\s*=\s*False\|rejectUnauthorized.*false\|InsecureSkipVerify.*true" \
  --include='*.{py,js,ts,go,java,rb}' . 2>/dev/null | \
  grep -v 'node_modules\|\.git\|test\|spec\|mock' | wc -l)
[ "$disabled" -gt 0 ] && warn "SSL verification disabled in $disabled location(s)" || ok "No SSL bypasses found"

section "CORS Configuration"
cors=$(grep -rn "Access-Control-Allow-Origin.**\|cors({.*origin.*true" \
  --include='*.{py,js,ts,go,java,rb}' . 2>/dev/null | \
  grep -v 'node_modules\|\.git' | wc -l)
[ "$cors" -gt 0 ] && warn "CORS wildcard found in $cors location(s)" || ok "No CORS wildcard"

section "Debug/Development Settings"
debug=$(grep -rn "DEBUG\s*=\s*True\|debug:\s*true" \
  --include='*.{py,yml,yaml,json}' . 2>/dev/null | \
  grep -v 'node_modules\|\.git\|test\|jest\|vitest' | wc -l)
[ "$debug" -gt 0 ] && warn "Debug mode enabled in $debug location(s)" || ok "No debug flags found"

echo ""
echo "========================================="
echo "Audit complete. Issues found: $ISSUES"
echo "========================================="
[ "$ISSUES" -eq 0 ] && exit 0 || exit 1
```

## 代码示例 (bash)

```bash
SCAN_DIRS="${1:-.}"

echo "--- Prompt Injection Patterns ---"
INJECTION_PATTERNS=(
    'ignore\s+(previous|all|above)\s+instructions'
    'you\s+are\s+now\s+'
    'new\s+system\s+prompt'
    '[SYSTEM]'
    '<SYSTEM_ADMIN_OVERRIDE>'
    'AUTHORIZED_OVERRIDE'
    'forget\s+your\s+(rules|instructions|guidelines)'
    'act\s+as\s+if\s+you\s+are'
    'disregard\s+(all|your|previous)'
    'jailbreak'
    'DAN\s+mode'
)

for pattern in "${INJECTION_PATTERNS[@]}"; do
    matches=$(grep -rn -iP "$pattern" "$SCAN_DIRS" \
      --include='*.{md,txt,json,html,yml,yaml}' 2>/dev/null | \
      grep -v 'node_modules\|\.git\|SKILL.md' | head -5)
    [ -n "$matches" ] && echo "  [!] Injection pattern '$pattern':" && echo "$matches"
done

echo "--- Zero-Width Unicode Characters ---"
grep -rPn '[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{00AD}\x{2060}]' "$SCAN_DIRS" \
  --include='*.{md,txt,json,html}' 2>/dev/null | head -10

echo "--- Suspicious Base64 Strings ---"
grep -rPn '[A-Za-z0-9+/=]{50,}' "$SCAN_DIRS" \
  --include='*.{md,txt,json}' 2>/dev/null | \
  grep -v 'node_modules\|\.git\|\.png\|\.jpg\|package-lock' | head -10
```

## 代码示例 (bash)

```bash
#!/bin/bash

PATTERNS=(
    'AKIA[0-9A-Z]{16}'
    'BEGIN.*PRIVATE KEY'
    'password\s*[:=]\s*["\x27][^"\x27]+'
    'api[_-]?key\s*[:=]\s*["\x27][^"\x27]+'
    'sk-[A-Za-z0-9]{20,}'
    'ghp_[A-Za-z0-9]{36}'
    'xox[bpoas]-[A-Za-z0-9-]+'
)

STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)
[ -z "$STAGED_FILES" ] && exit 0

EXIT_CODE=0
for pattern in "${PATTERNS[@]}"; do
    matches=$(echo "$STAGED_FILES" | xargs grep -Pn "$pattern" 2>/dev/null)
    if [ -n "$matches" ]; then
        echo "BLOCKED: Potential secret detected matching pattern: $pattern"
        echo "$matches"
        EXIT_CODE=1
    fi
done

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "To proceed anyway: git commit --no-verify"
    echo "To remove secrets: replace with environment variables"
fi
exit $EXIT_CODE
```

## 代码示例 (bash)

```bash
openssl s_client -connect example.com:443 -servername example.com < /dev/null 2>/dev/null | \
  openssl x509 -noout -subject -issuer -dates -fingerprint

echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | \
  openssl x509 -noout -enddate

for v in tls1 tls1_1 tls1_2 tls1_3; do
  result=$(openssl s_client -connect example.com:443 -$v < /dev/null 2>&1)
  if echo "$result" | grep -q "Cipher is"; then
    echo "$v: SUPPORTED"
  else
    echo "$v: NOT SUPPORTED"
  fi
done

openssl s_client -connect example.com:443 -cipher 'ALL' < /dev/null 2>&1 | \
  grep "Cipher    :"

openssl s_client -connect example.com:443 -cipher 'NULL:EXPORT:DES:RC4:MD5' < /dev/null 2>&1 | \
  grep "Cipher    :"
```

## 代码示例 (bash)

```bash
echo "--- Agent Permissions ---"

grep -rn 'sudo\|root\|admin.*access\|unrestricted' \
  AGENTS.md TOOLS.md 2>/dev/null

echo "Running agent processes:"
ps aux | grep -i 'cron\|heartbeat\|monitor\|watch\|loop' | grep -v grep | head -10

echo "--- Cron/Background Jobs ---"
crontab -l 2>/dev/null || echo "  No crontab"

echo "--- Workspace Size ---"
du -sh . memory/ 2>/dev/null

echo "--- Sensitive System Files Readable by Agent ---"
for f in /etc/shadow /etc/passwd [REDACTED_SSH_PATH] [REDACTED_SSH_PATH] \
         [REDACTED_AWS_PATH] [REDACTED_GCP_PATH] do
    [ -r "$f" ] && echo "  [!] READABLE: $f"
done
```

## 代码示例 (bash)

```bash
find . -type f -perm -o=w -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null

find . -type f -perm -u=x -not -name '*.sh' -not -name '*.py' -not -path '*/node_modules/*' \
  -not -path '*/.git/*' -not -path '*/bin/*' 2>/dev/null

for f in .env .env.* *.pem *.key *.p12 id_rsa id_ed25519; do
    [ -f "$f" ] && ls -la "$f"
done

find / -type f ( -perm -4000 -o -perm -2000 ) 2>/dev/null | head -20

if [ -d [REDACTED_SSH_PATH] ]; then
    echo "--- SSH directory permissions ---"
    ls -la [REDACTED_SSH_PATH]
    echo ""
    [ "$(stat -c %a [REDACTED_SSH_PATH] 2>/dev/null || stat -f %Lp [REDACTED_SSH_PATH] != "700" ] && echo "WARNING: [REDACTED_SSH_PATH] should be 700"
fi
```

## 代码示例 (bash)

```bash
echo "--- Memory Integrity ---"

echo "URLs in memory that agent may follow as instructions:"
grep -rn 'https\?://\|gist\.github\|pastebin\|hastebin' \
  MEMORY.md memory/*.md HEARTBEAT.md 2>/dev/null

echo "Recent memory file changes:"
find memory/ MEMORY.md SOUL.md AGENTS.md -newer IDENTITY.md -type f 2>/dev/null | \
  while read f; do echo "  $(stat -f '%Sm %N' "$f" 2>/dev/null || stat -c '%y %n' "$f")"; done

grep -rn -i 'override\|bypass\|ignore.*rule\|disable.*safety\|skip.*check' \
  MEMORY.md memory/*.md HEARTBEAT.md 2>/dev/null

echo "--- SOUL.md modification history ---"
git log --oneline -10 -- SOUL.md 2>/dev/null || echo "  (not in git)"
echo "--- AGENTS.md modification history ---"
git log --oneline -10 -- AGENTS.md 2>/dev/null || echo "  (not in git)"
```

## 代码示例 (bash)

```bash
echo "--- Files that should probably be gitignored ---"
for pattern in '.env' '.env.*' '*.pem' '*.key' '*.p12' '*.pfx' 'credentials.json' \
               'service-account*.json' '*.keystore' 'id_rsa' 'id_ed25519'; do
    found=$(git ls-files "$pattern" 2>/dev/null)
    [ -n "$found" ] && echo "  TRACKED: $found"
done

if [ ! -f .gitignore ]; then
    echo "WARNING: No .gitignore file found"
else
    for entry in '.env' 'node_modules' '*.key' '*.pem'; do
        grep -q "$entry" .gitignore || echo "  MISSING from .gitignore: $entry"
    done
fi
```

## 代码示例 (bash)

```bash
echo "--- Multi-Agent Trust ---"

grep -rn -i 'discord\|forum\|moltbook\|clawstr\|email.*agent' \
  TOOLS.md MEMORY.md memory/*.md 2>/dev/null

grep -rn -i 'webhook\|auto.reply\|auto.respond\|on.*mention' \
  AGENTS.md HEARTBEAT.md TOOLS.md scripts/*.sh 2>/dev/null

grep -rn -i 'relay\|forward.*message\|pass.*along\|tell.*agent' \
  MEMORY.md memory/*.md 2>/dev/null

echo "--- Scheduled Tasks ---"
grep -rn -i 'check.*forum\|check.*moltbook\|reply.*comment\|respond.*mention' \
  HEARTBEAT.md 2>/dev/null
```

