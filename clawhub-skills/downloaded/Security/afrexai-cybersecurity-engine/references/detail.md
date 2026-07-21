# 详细参考 - afrexai-cybersecurity-engine

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
network_hardening:
  firewall:
    default_policy: "deny-all"
    allowed_inbound:
      - port: 443
        source: "0.0.0.0/0"
        service: "HTTPS"
      - port: 22
        source: "[admin_ip_range]"
        service: "SSH"
    rules:
      - "No direct database access from internet"
      - "Internal services communicate on private subnet"
      - "Egress filtering — block unnecessary outbound"

  ssh:
    password_auth: false
    root_login: false
    key_type: "ed25519"
    port: "[non-standard recommended]"
    fail2ban: true
    max_auth_tries: 3

  dns:
    dnssec: true
    caa_records: true  # restrict who can issue TLS certs
    no_zone_transfer: true

  tls:
    min_version: "1.2"
    preferred: "1.3"
    cipher_suites: "ECDHE+AESGCM:ECDHE+CHACHA20"
    hsts: "max-age=31536000; includeSubDomains; preload"
    certificate_monitoring: true
    auto_renewal: true
```

## 代码示例 (yaml)

```yaml
cloud_security_baseline:
  identity:
    - root_account_mfa: true
    - no_root_access_keys: true
    - least_privilege_iam: true
    - service_accounts_scoped: true
    - temporary_credentials: true  # assume role, not long-lived keys
    - sso_enforced: true

  data:
    - encryption_at_rest: "default on all storage"
    - encryption_in_transit: "TLS everywhere"
    - backup_encryption: true
    - key_management: "cloud KMS, not self-managed"
    - data_classification: true

  network:
    - vpc_flow_logs: true
    - private_subnets_for_databases: true
    - nat_gateway_for_outbound: true
    - waf_on_public_endpoints: true
    - ddos_protection: true

  monitoring:
    - cloudtrail_enabled: true  # or equivalent
    - config_rules: true
    - guardduty_enabled: true  # or equivalent
    - cost_alerts: true
    - unused_resource_alerts: true

  storage:
    - no_public_buckets: true
    - versioning_on_critical: true
    - lifecycle_policies: true
    - access_logging: true
```

## 代码示例 (yaml)

```yaml
report:
  executive_summary:
    overall_risk: "critical|high|medium|low"
    critical_findings: 0
    high_findings: 0
    medium_findings: 0
    low_findings: 0
    key_recommendations:
      - "[top 3 fixes by impact]"

  scope:
    targets: "[URLs, IPs, apps tested]"
    methodology: "OWASP Testing Guide v4.2 + PTES"
    dates: "YYYY-MM-DD to YYYY-MM-DD"
    type: "black-box|grey-box|white-box"
    exclusions: "[what was out of scope]"

  findings:
    - id: "F-001"
      title: "[descriptive title]"
      severity: "critical|high|medium|low|info"
      cvss: 0.0
      location: "[URL/endpoint/component]"
      description: "[what the vulnerability is]"
      impact: "[what an attacker could do]"
      evidence: "[screenshots, request/response pairs]"
      reproduction_steps:
        - "[step by step]"
      remediation: "[specific fix with code examples]"
      references:
        - "[OWASP, CWE, CVE links]"

  positive_observations:
    - "[security controls that were effective]"
```

## 代码示例 (yaml)

```yaml
assessment:
  name: "[Project/Org Name] Security Assessment"
  date: "YYYY-MM-DD"
  assessor: "[Agent/Person]"
  scope:
    applications:
      - name: "[App Name]"
        type: "web|api|mobile|desktop|iot"
        tech_stack: "[languages, frameworks, DBs]"
        hosting: "cloud|on-prem|hybrid"
        cloud_provider: "aws|gcp|azure|other"
        internet_facing: true|false
        handles_pii: true|false
        handles_payments: true|false
        handles_phi: true|false  # health data
    infrastructure:
      - servers: "[count, OS types]"
        containers: true|false
        orchestration: "k8s|ecs|nomad|none"
        cdn: "[provider or none]"
        dns: "[provider]"
    third_parties:
      - name: "[service]"
        data_shared: "[what data]"
        criticality: "high|medium|low"
  compliance_requirements:
    - "SOC 2|ISO 27001|GDPR|HIPAA|PCI DSS|SOX|none"
  previous_incidents:
    - date: "YYYY-MM-DD"
      type: "[breach|vuln|misconfiguration]"
      severity: "critical|high|medium|low"
      resolution: "[what was done]"
  risk_tolerance: "conservative|moderate|aggressive"
```

## 代码示例 (yaml)

```yaml
security_dashboard:
  vulnerability_management:
    - open_critical: 0  # Target: always 0
    - open_high: 0      # Target: < 5
    - mean_time_to_remediate:
        critical: "24h"  # Target
        high: "7d"
        medium: "30d"
    - scan_coverage: "100%"  # % of repos with automated scanning
  incident_management:
    - incidents_this_quarter: 0
    - mean_time_to_detect: "< 1h"
    - mean_time_to_respond: "< 4h"
    - mean_time_to_recover: "< 24h"

  access_control:
    - mfa_adoption: "100%"
    - privileged_accounts: 0  # Count, minimize
    - stale_accounts: 0       # Accounts unused > 90 days
    - access_reviews_completed: "on schedule"

  code_security:
    - repos_with_sast: "100%"
    - repos_with_dependency_scanning: "100%"
    - secret_detection_coverage: "100%"
    - security_review_for_critical_changes: "100%"

  training:
    - security_awareness_completion: "100%"
    - phishing_simulation_click_rate: "< 5%"
    - security_champions_per_team: ">= 1"
```

## 代码示例 (yaml)

```yaml
post_mortem:
  incident_id: "INC-YYYY-NNN"
  date: "YYYY-MM-DD"
  severity: "SEV-1|2|3|4"
  duration: "[detection to resolution]"
  impact:
    users_affected: 0
    data_compromised: "[type and volume]"
    financial_impact: "$0"
    regulatory_notification_required: true|false
  timeline:
    - time: "HH:MM"
      event: "[what happened]"
      action: "[what we did]"
  root_cause: "[specific technical cause]"
  contributing_factors:
    - "[what made it possible or worse]"
  what_went_well:
    - "[detection, response, communication]"
  what_went_poorly:
    - "[gaps, delays, confusion]"
  action_items:
    - action: "[specific improvement]"
      owner: "[person]"
      due: "YYYY-MM-DD"
      status: "open|done"
  lessons_learned:
    - "[distilled insight]"
```

## 代码示例 (yaml)

```yaml
supply_chain:
  dependencies:
    - lock_files: "always commit (package-lock.json, poetry.lock, go.sum)"
    - pin_versions: "exact versions, not ranges"
    - audit_frequency: "every CI build"
    - auto_update: "Dependabot/Renovate with auto-merge for patch, review for minor/major"
    - review_new_deps:
        check: "maintainer count, last update, download count, known issues"
        rule: "no single-maintainer deps for critical paths"
    - sbom: "generate SPDX or CycloneDX on every release"

  build_pipeline:
    - reproducible_builds: true
    - artifact_signing: true
    - build_provenance: true  # SLSA Level 2+
    - no_curl_pipe_bash: true  # Never pipe internet scripts to shell
    - verify_checksums: true

  ci_cd:
    - pin_action_versions: "use SHA, not tags (actions/checkout@SHA)"
    - least_privilege_tokens: true
    - no_secrets_in_logs: true
    - protected_branches: true
    - required_reviews: true
    - signed_commits: "recommended"
```

## 代码示例 (yaml)

```yaml
container_hardening:
  image:
    - base: "distroless or alpine (minimal)"
    - user: "non-root (USER 1000:1000)"
    - scan: "trivy image before push"
    - sign: "cosign or Notary"
    - pins: "use SHA256 digests, not :latest"
    - secrets: "NEVER in Dockerfile or image layers"
    - layers: "multi-stage builds, minimal final image"

  runtime:
    - read_only_rootfs: true
    - no_new_privileges: true
    - drop_all_capabilities: true
    - add_only: ["NET_BIND_SERVICE"]  # if needed
    - resource_limits: true
    - seccomp_profile: "default"
    - network_policy: "deny by default"

  registry:
    - private: true
    - vulnerability_scanning: true
    - image_signing: true
    - tag_immutability: true
```

## 代码示例 (yaml)

```yaml
vulnerability:
  id: "VULN-YYYY-NNN"
  title: "[descriptive title]"
  discovered: "YYYY-MM-DD"
  discoverer: "[scanner/person/bounty]"
  severity: "critical|high|medium|low|info"
  cvss_score: 0.0
  cvss_vector: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
  cve: "[if applicable]"
  affected:
    - component: "[app/service/library]"
      version: "[affected versions]"
      environment: "production|staging|dev"
  description: "[what the vulnerability is]"
  impact: "[what an attacker could do]"
  proof_of_concept: "[steps to reproduce]"
  remediation:
    fix: "[specific fix]"
    workaround: "[temporary mitigation]"
    compensating_control: "[if fix isn't immediate]"
  status: "open|in-progress|fixed|accepted|false-positive"
  fixed_date: "YYYY-MM-DD"
  verified_by: "[person who confirmed fix]"
```

## 代码示例 (text)

```text
Need to store passwords?
  → bcrypt (cost 12+) or Argon2id
  → NEVER: MD5, SHA1, SHA256 without salt

Need to encrypt data at rest?
  → AES-256-GCM (authenticated encryption)
  → NEVER: ECB mode, DES, RC4

Need to encrypt in transit?
  → TLS 1.2+ (prefer 1.3)
  → HSTS with includeSubDomains
  → Certificate pinning for mobile apps

Need to generate random values?
  → crypto.randomBytes() / secrets.token_bytes()
  → NEVER: Math.random(), random.random()

Need to sign/verify?
  → HMAC-SHA256 for symmetric
  → Ed25519 or RSA-PSS (2048+ bits) for asymmetric
  → NEVER: RSA PKCS#1 v1.5 for new systems
```

## 代码示例 (yaml)

```yaml
web_server:
  - remove_default_pages: true
  - disable_directory_listing: true
  - remove_server_version_header: true
  - disable_TRACE_method: true
  - custom_error_pages: true  # no stack traces
application:
  - debug_mode: false  # NEVER in production
  - verbose_errors: false
  - default_accounts_removed: true
  - unnecessary_features_disabled: true
  - admin_panel_ip_restricted: true

cloud:
  - public_buckets: none
  - security_groups_least_privilege: true
  - imds_v2_enforced: true  # AWS
  - logging_enabled: true
  - mfa_on_root: true
  - billing_alerts: true
```

## 代码示例 (yaml)

```yaml
jwt_security:
  signing:
    algorithm: "RS256 or EdDSA"  # NEVER HS256 with shared secrets in distributed systems
    key_rotation: "quarterly"
    verify_algorithm: true  # Reject alg=none
  claims:
    exp: "required — 15 min for access, 7d for refresh"
    iss: "required — validate on every request"
    aud: "required — validate matches expected service"
    iat: "required"
    jti: "recommended — for revocation"
    nbf: "recommended"
  storage:
    access_token: "memory only (never localStorage)"
    refresh_token: "httpOnly secure cookie"
  revocation:
    method: "token blacklist with Redis TTL matching exp"
    on_password_change: "revoke all tokens"
    on_permission_change: "revoke all tokens"
```

## 代码示例 (text)

```text
PASSIVE (no direct interaction with target):
1. DNS enumeration: subdomains, MX, TXT, CNAME
   - Tools: subfinder, amass, crt.sh, dnsdumpster
2. Technology fingerprinting
   - Check: Wappalyzer, BuiltWith, HTTP headers
3. Public exposure
   - Shodan/Censys for open ports/services
   - GitHub/GitLab for leaked code/secrets
   - Wayback Machine for old endpoints
4. Employee OSINT (for social engineering scope)
   - LinkedIn for tech stack clues
   - Job postings reveal internal tools

ACTIVE (interacting with target — requires permission):
1. Port scanning: full TCP + top 1000 UDP
2. Service enumeration: version detection
3. Web crawling: sitemap, robots.txt, directory brute-force
4. API discovery: /api, /v1, /graphql, /swagger, /openapi
```

## 代码示例 (yaml)

```yaml
password_policy:
  minimum_length: 12  # NIST minimum is 8, 12+ recommended
  maximum_length: 128  # Must support long passwords
  complexity_rules: false  # NIST says don't require special chars
  check_against_breached: true  # HaveIBeenPwned API
  no_password_hints: true
  no_security_questions: true  # Easy to social engineer
  allow_paste: true  # For password managers
  rate_limit_attempts: "5 per 15 minutes"
  lockout_duration: "progressive (1min, 5min, 15min, 1hr)"
  mfa_required: "all accounts"
  mfa_methods:
    preferred: "TOTP or WebAuthn/passkeys"
    acceptable: "push notification"
    discouraged: "SMS (SIM swap risk)"
  storage: "Argon2id or bcrypt cost 12+"
```

## 代码示例 (yaml)

```yaml
threats:
  - id: "T-001"
    component: "[affected component]"
    category: "S|T|R|I|D|E"
    description: "[specific attack scenario]"
    attacker_profile: "external-unauthenticated|external-authenticated|internal|insider"
    likelihood: 1-5  # 1=rare, 5=almost certain
    impact: 1-5      # 1=negligible, 5=catastrophic
    risk_score: 0     # likelihood × impact
    existing_controls: "[what's already in place]"
    residual_risk: "accept|mitigate|transfer|avoid"
    mitigation: "[specific fix]"
    priority: "P0|P1|P2|P3"
    owner: "[person/team]"
    status: "open|in-progress|mitigated|accepted"
```

### Incident Response Playbook
**Phase 1 — Detection & Triage (first 15 minutes)**

```text
1. Confirm incident is real (not false positive)
2. Classify severity (SEV-1 through SEV-4)
3. Assign incident commander
4. Open incident channel (Slack/Teams)
5. Start incident log with timestamps
6. Notify stakeholders per severity
```

**Phase 2 — Containment (first hour)**

```text
SHORT-TERM (stop the bleeding):
- Isolate affected systems (network segmentation)
- Revoke compromised credentials immediately
- Block attacking IP/user agent
- Enable enhanced logging on affected systems
- Preserve forensic evidence (DON'T reboot/wipe yet)

LONG-TERM (prevent spread):
- Patch the vulnerability that was exploited
- Rotate ALL credentials that may be compromised
- Update firewall/WAF rules
- Deploy additional monitoring
```

**Phase 3 — Eradication**

```text
1. Identify root cause
2. Remove all attacker artifacts (backdoors, malware, new accounts)
3. Patch all instances of the vulnerability
4. Verify no lateral movement occurred
5. Confirm all compromised credentials rotated
```

**Phase 4 — Recovery**

```text
1. Restore from clean backups (verify backup integrity first)
2. Rebuild compromised systems from scratch (don't trust cleanup)
3. Monitor restored systems with enhanced logging
4. Gradual return to production (staged rollback)
5. Confirm normal operations for 48 hours
```

**Phase 5 — Post-Incident**

```yaml
post_mortem:
  incident_id: "INC-YYYY-NNN"
  date: "YYYY-MM-DD"
  severity: "SEV-1|2|3|4"
  duration: "[detection to resolution]"
  impact:
    users_affected: 0
    data_compromised: "[type and volume]"
    financial_impact: "$0"
    regulatory_notification_required: true|false
  timeline:
    - time: "HH:MM"
      event: "[what happened]"
      action: "[what we did]"
  root_cause: "[specific technical cause]"
  contributing_factors:
    - "[what made it possible or worse]"
  what_went_well:
    - "[detection, response, communication]"
  what_went_poorly:
    - "[gaps, delays, confusion]"
  action_items:
    - action: "[specific improvement]"
      owner: "[person]"
      due: "YYYY-MM-DD"
      status: "open|done"
  lessons_learned:
    - "[distilled insight]"
```




### Quick Health Check (5 minutes)
Run through these three tiers:

**Tier 1 — Critical (fix today):**

* Default credentials in production
* Secrets in source code or environment files committed to git
* No authentication on admin endpoints
* SQL injection in user-facing forms
* Unencrypted sensitive data at rest
* Public S3 buckets or cloud storage
* No HTTPS enforcement
* Root/admin running application processes

**Tier 2 — High (fix this week):**

* Dependencies with known CVEs (CVSS ≥ 7.0)
* No rate limiting on authentication endpoints
* Missing CSRF protection on state-changing operations
* Verbose error messages leaking stack traces
* No input validation on API endpoints
* Weak password policy (< 12 chars, no complexity)
* Session tokens in URL parameters
* No logging of authentication events

**Tier 3 — Medium (fix this sprint):**

* Missing security headers (CSP, HSTS, X-Frame-Options)
* No automated dependency scanning in CI
* Overprivileged service accounts
* No secret rotation policy
* Missing account lockout after failed attempts
* No security.txt or responsible disclosure policy
* Cookies without Secure/HttpOnly/SameSite flags

**Score:** Count failures. 0-2 = solid. 3-5 = needs work. 6+ = stop shipping features, fix security.



---

### Step 1 — Decompose the System
For each application, draw the data flow:

```text
[User] → [CDN/WAF] → [Load Balancer] → [Web Server] → [App Server] → [Database]
                                                     ↘ [Cache]
                                                     ↘ [Message Queue] → [Worker]
                                                     ↘ [Third-party API]
                                                     ↘ [Object Storage]
```

**Identify trust boundaries** — where privilege level changes:

* Internet → DMZ (public-facing services)
* DMZ → Internal network (app servers, DBs)
* App → Database (credential boundary)
* User → Admin (role boundary)
* Service → Service (API key boundary)
* Your infra → Third-party (trust boundary)



---

### A01: Broken Access Control
**Test checklist:**

* Can user A access user B's resources by changing ID? (IDOR)
* Can non-admin access admin endpoints?
* Do API endpoints enforce authorization, not just authentication?
* Are directory listings disabled?
* Is CORS properly configured (not `*` with credentials)?
* Can JWT be tampered with (alg=none, key confusion)?
* Is rate limiting applied to sensitive endpoints?
* Do file uploads validate type server-side?

**Fix patterns:**

```text
1. Authenticate → verify identity
2. Authorize → verify permission for THIS resource
3. Validate → verify input is within allowed bounds
4. Execute → perform the action
5. Audit → log who did what

- NEVER use sequential IDs in URLs — use UUIDs
- ALWAYS verify resource ownership server-side
- Use middleware that auto-checks resource.owner === request.user
```



---

### A03: Injection
**SQL Injection prevention:**

```text
✅ db.query("SELECT * FROM users WHERE id = $1", [userId])
❌ db.query("SELECT * FROM users WHERE id = " + userId)

' OR '1'='1
'; DROP TABLE users;--
' UNION SELECT password FROM users--
1; WAITFOR DELAY '0:0:5'--
```

**XSS prevention:**

```text
HTML body    → HTML entity encode (&lt; &gt; &amp; &quot; &#x27;)
HTML attr    → Attribute encode + always quote attributes
JavaScript   → JavaScript encode (\\xHH)
URL          → Percent encode (%HH)
CSS          → CSS encode (\\HHHHHH)

Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' https://api.yourdomain.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
```

**Command injection prevention:**

```text
✅ execFile('convert', ['-resize', size, inputFile, outputFile])
❌ exec('convert -resize ' + size + ' ' + inputFile + ' ' + outputFile)

- Whitelist allowed characters (alphanumeric only)
- Use library wrappers, never string concatenation
```



---

### Communication Templates
**Internal notification (SEV-1/2):**

```text
🚨 SECURITY INCIDENT — [severity]
What: [brief description]
Impact: [what's affected]
Status: [containment/investigation/resolved]
Incident Commander: [name]
Channel: #incident-[id]
Next update: [time]

DO NOT discuss outside this channel.
```

**Customer notification (if required):**

```text
Subject: Security Notice — [Company Name]

We're writing to inform you of a security incident that [may have|affected] your account.

What happened: [brief, honest description]
When: [date range]
What data was involved: [specific data types]
What we've done: [remediation steps]
What you should do: [password reset, monitor accounts, etc.]
Contact: [security team email/phone]

We take the security of your data seriously and have [specific improvements].
```



---

### Building a Security Program from Scratch
**Quarter 1 — Foundation:**

```text
Week 1-2: Asset inventory (what do we have?)
Week 3-4: Risk assessment (what matters most?)
Week 5-6: Critical controls (authentication, secrets, backups)
Week 7-8: Basic scanning (dependencies, secrets in code)
Week 9-10: Incident response plan (what if something happens?)
Week 11-12: Security awareness basics (phishing, passwords)
```

**Quarter 2 — Automation:**

```text
- CI/CD security scanning (SAST, dependency audit)
- Automated secret detection (pre-commit hooks)
- Centralized logging and basic alerting
- Access reviews (quarterly)
- Vulnerability management process
```

**Quarter 3 — Maturity:**

```text
- Penetration testing (first external assessment)
- Security architecture review
- Data classification and handling policies
- Vendor security assessments
- Bug bounty program (start small)
```

**Quarter 4 — Optimization:**

```text
- Compliance framework alignment (SOC 2, ISO 27001)
- Red team exercise
- Security metrics dashboard
- Security champion program (devs with security training)
- Supply chain security (SBOM, signed artifacts)
```



---

### Testing Phases
**Phase 1 — Authentication Testing**

```text
- Credential stuffing resistance (rate limiting)
- Password reset flow (token guessability, expiry, reuse)
- Account enumeration (different responses for valid/invalid users)
- Session management (token entropy, fixation, timeout)
- MFA bypass attempts (backup codes, race conditions)
- OAuth flow attacks (redirect URI manipulation, scope escalation)
```

**Phase 2 — Authorization Testing**

```text
- Horizontal privilege escalation (access other users' data)
- Vertical privilege escalation (user → admin)
- Missing function-level access control (direct API calls)
- IDOR on every resource endpoint (change IDs systematically)
- GraphQL introspection + unauthorized field access
- Mass assignment (send extra fields in requests)
```

**Phase 3 — Injection Testing**

```text
- SQL injection on all user inputs (including headers, cookies)
- XSS (reflected, stored, DOM-based) on all output points
- Command injection on any server-side execution
- SSRF on any URL input or file fetch
- Template injection (if server-side templating)
- LDAP/XML/XXE injection where applicable
```

**Phase 4 — Business Logic Testing**

```text
- Price manipulation (change prices in requests)
- Quantity manipulation (negative numbers, decimals, MAX_INT)
- Race conditions (concurrent requests for same resource)
- Workflow bypass (skip steps in multi-step processes)
- Coupon/discount abuse (reuse, stacking)
- Rate limit bypass (header rotation, distributed requests)
```



---

## Phase 12: Security Scoring Rubric
Rate any application/system 0-100:

| Dimension | Weight | 0 (Critical) | 5 (Adequate) | 10 (Excellent) |
| --- | --- | --- | --- | --- |
| Authentication & Access | 20% | No auth or default creds | Password + basic RBAC | MFA + ABAC + zero trust |
| Data Protection | 15% | Plaintext secrets, no encryption | Encryption at rest + transit | E2E encryption, key rotation, classification |
| Vulnerability Management | 15% | No scanning, known CVEs | Automated scanning, SLAs met | Full coverage, MTTD < 1h, bug bounty |
| Infrastructure Security | 15% | Open ports, no firewall | Hardened baseline, least privilege | Zero trust, microsegmentation, IaC |
| Logging & Monitoring | 10% | No security logging | Centralized logs, basic alerts | SIEM, anomaly detection, 24/7 SOC |
| Incident Response | 10% | No plan | Documented plan, tested annually | Automated response, < 1h MTTR |
| Code Security | 10% | No reviews, injection vulns | SAST in CI, peer review | Full pipeline, threat modeling, security champions |
| Supply Chain | 5% | No dependency management | Lock files, automated scanning | SBOM, signed artifacts, SLSA |

**Score interpretation:**

* 90-100: Excellent — security is a competitive advantage
* 70-89: Good — solid foundation, keep improving
* 50-69: Needs work — significant gaps exist
* Below 50: Critical — stop feature work, fix security



---
