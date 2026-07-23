---
slug: agentic-security-audit
name: agentic-security-audit
version: "1.0.0"
displayName: Agentic Security Aud
summary: Audit codebases, infrastructure, AND agentic AI systems for security issues.
  Covers traditional s...
license: MIT
description: |-
  Audit codebases, infrastructure, AND agentic AI systems for security
  issues。Covers traditional s。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Security
- Agents
tools:
  - - read
- exec
# Agentic Security Audit
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

Scan, detect, and fix security issues in codebases and infrastructure. Covers dependency vulnerabilities, secret detection, OWASP top 10, SSL/TLS verification, file permissions, and secure coding patterns.

## When to Use
* Scanning project dependencies for known vulnerabilities
* Detecting hardcoded secrets, API keys, or credentials in source code
* Reviewing code for OWASP top 10 vulnerabilities (injection, XSS, CSRF, etc.)
* Verifying SSL/TLS configuration for endpoints
* Auditing file and directory permissions
* Checking authentication and authorization patterns
* Preparing for a security review or compliance audit

## Dependency Vulnerability Scanning
### Node.js
```bash
npm audit
npm audit --json | jq '.vulnerabilities | to_entries[] | {name: .key, severity: .value.severity, via: .value.via[0]}'

npm audit fix

npm audit --audit-level=high

npm audit --package-lock-only

npx audit-ci --high
```

### Python
```bash
pip install pip-audit
pip-audit
pip-audit -r requirements.txt
pip-audit --format=json

pip install safety
safety check
safety check -r requirements.txt --json

pip-audit --requirement=- <<< "requests==2.25.0"
```

### Go
```bash
go install golang.org/x/vuln/cmd/govulncheck@latest
govulncheck ./...

govulncheck -mode=binary ./myapp
```

### Rust
```bash
cargo install cargo-audit
cargo audit

cargo audit fix
```

### Universal: Trivy (scans any project)
```bash
trivy fs .

trivy fs --scanners vuln --severity HIGH,CRITICAL .

trivy image myapp:latest

trivy fs --format json -o results.json .
```

## Secret Detection
### Manual grep patterns
```bash
grep -rn 'AKIA[0-9A-Z]\{16\}' --include='*.{js,ts,py,go,java,rb,env,yml,yaml,json,xml,cfg,conf,ini}' .

grep -rn -i 'api[_-]\?key\|api[_-]\?secret\|access[_-]\?token\|auth[_-]\?token\|bearer ' \
  --include='*.{js,ts,py,go,java,rb,env,yml,yaml,json}' .

grep -rn 'BEGIN.*PRIVATE KEY' .

grep -rn -i 'password\s*[:=]' --include='*.{env,yml,yaml,json,xml,cfg,conf,ini,toml}' .

grep -rn -i 'mongodb://\|mysql://\|postgres://\|redis://' --include='*.{js,ts,py,go,env,yml,yaml,json}' . | grep -v 'localhost\|127.0.0.1\|example'

grep -rn 'eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.' --include='*.{js,ts,py,go,log,json}' .
```

### Automated scanning with git
```bash
git log -p --all | grep -n -i 'api.key\|password\|secret\|token' | head -50

git diff --cached --name-only | xargs grep -l -i 'api.key\|password\|secret\|token' 2>/dev/null
```

### Pre-commit hook for secrets

> 详细代码示例已移至 `references/detail.md`

### .gitignore audit

> 详细代码示例已移至 `references/detail.md`

## OWASP Top 10 Code Patterns
### 1. Injection (SQL, Command, LDAP)
```bash
grep -rn "query\|execute\|cursor" --include='*.{py,js,ts,go,java,rb}' . | \
  grep -i "f\"\|format(\|%s\|\${\|+ \"\|concat\|sprintf" | \
  grep -iv "parameterized\|placeholder\|prepared"

grep -rn "exec(\|spawn(\|system(\|popen(\|subprocess\|os\.system\|child_process" \
  --include='*.{py,js,ts,go,java,rb}' .

grep -rn "\\$[0-9]\|\\?\|%s\|:param\|@param\|prepared" --include='*.{py,js,ts,go,java,rb}' .
```

### 2. Broken Authentication
```bash
grep -rn "md5\|sha1\|sha256" --include='*.{py,js,ts,go,java,rb}' . | grep -i "password\|passwd"

grep -rn -i "admin.*password\|password.*admin\|default.*password" \
  --include='*.{py,js,ts,go,java,rb,yml,yaml,json}' .

grep -rn "session\|token\|jwt" --include='*.{py,js,ts,go,java,rb}' . | grep -i "url\|query\|param\|GET"

grep -rn -i "rate.limit\|throttle\|brute" --include='*.{py,js,ts,go,java,rb}' .
```

### 3. Cross-Site Scripting (XSS)
```bash
grep -rn "innerHTML\|dangerouslySetInnerHTML\|v-html\|\|html(" \
  --include='*.{js,ts,jsx,tsx,vue,html}' .

grep -rn "{{{.*}}}\|<%=\|<%-\|\$\!{" --include='*.{html,ejs,hbs,pug,erb}' .

grep -rn "document\.write\|document\.writeln" --include='*.{js,ts,html}' .

grep -rn "/* REMOVED: eval */ (\|new Function(\|setTimeout.*string\|setInterval.*string" \
  --include='*.{js,ts}' .
```

### 4. Insecure Direct Object References
```bash
grep -rn "params\.id\|params[.id.]\|req\.params\.\|request\.args\.\|request\.GET\." \
  --include='*.{py,js,ts,go,java,rb}' . | \
  grep -i "user\|account\|profile\|order\|document"
```

### 5. Security Misconfiguration
```bash
grep -rn "Access-Control-Allow-Origin.**\|cors({.*origin.*true\|cors()" \
  --include='*.{py,js,ts,go,java,rb}' .

grep -rn "DEBUG\s*=\s*True\|debug:\s*true\|NODE_ENV.*development" \
  --include='*.{py,js,ts,yml,yaml,json,env}' .

grep -rn "stack\|traceback\|stackTrace" --include='*.{py,js,ts,go,java,rb}' . | \
  grep -i "response\|send\|return\|res\."
```

## SSL/TLS Verification
### Check endpoint SSL

> 详细代码示例已移至 `references/detail.md`

### Verify certificate chain
```bash
openssl s_client -connect example.com:443 -showcerts < /dev/null 2>/dev/null | \
  awk '/BEGIN CERTIFICATE/,/END CERTIFICATE/{print}' > chain.pem

openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt chain.pem

openssl x509 -in chain.pem -noout -text | grep -A2 "Subject:\|Issuer:\|Not Before\|Not After\|DNS:"
```

### Check SSL from code
```bash
grep -rn "verify\s*=\s*False\|rejectUnauthorized.*false\|InsecureSkipVerify.*true\|CURLOPT_SSL_VERIFYPEER.*false\|NODE_TLS_REJECT_UNAUTHORIZED.*0" \
  --include='*.{py,js,ts,go,java,rb,yml,yaml}' .
```

## File Permission Audit

> 详细代码示例已移至 `references/detail.md`

## Full Project Security Audit Script

> 详细代码示例已移至 `references/detail.md`

## Secure Coding Quick Reference
### Environment variables instead of hardcoded secrets
```bash
API_KEY="[REDACTED]"

API_KEY="[REDACTED]"

API_KEY=sk-abc123...
.env
```

### Input validation checklist
```text
- [ ] All user input validated (type, length, format)
- [ ] SQL queries use parameterized statements (never string concat)
- [ ] Shell commands never include user input directly
- [ ] File paths validated (no path traversal: ../)
- [ ] URLs validated (no SSRF: restrict to expected domains)
- [ ] HTML output escaped (no XSS: use framework auto-escaping)
- [ ] JSON parsing has error handling (no crash on malformed input)
- [ ] File uploads checked (type, size, no executable content)
```

### HTTP security headers
```bash
curl -sI https://example.com | grep -i 'strict-transport\|content-security\|x-frame\|x-content-type\|referrer-policy\|permissions-policy'

```

## Tips
* Run `npm audit` / `pip-audit` / `govulncheck` in CI on every pull request, not just occasionally.
* Secret detection in git history matters: even if a secret is removed from HEAD, it exists in git history. Use `git filter-branch` or `git-filter-repo` to purge, then rotate the credential.
* The most dangerous vulnerabilities are often the simplest: SQL injection via string concatenation, command injection via unsanitized input, XSS via `innerHTML`.
* CORS `Access-Control-Allow-Origin: *` is safe for truly public, read-only APIs. It's dangerous for anything that uses cookies or auth tokens.
* Always verify SSL in production. `verify=False` or `rejectUnauthorized: false` should only appear in test code, never in production paths.
* Defense in depth: validate input, escape output, use parameterized queries, enforce least privilege, and assume every layer might be bypassed.

## 🤖 Agentic Security Audit (Bổ sung 25/02/2026)
> *Từ paper "Agents of Chaos" (arXiv:2602.20021) + OWASP Top 10 for Agentic Applications 2026.*
> *Traditional security audit chỉ cover code/infra. Agentic systems có attack surface hoàn toàn mới.*

### When to Use (Agentic)
* Auditing Skill平台/agent workspace configuration
* Reviewing agent permissions and access boundaries
* Scanning for prompt injection vectors in agent-facing content
* Assessing multi-agent communication security
* Evaluating identity verification mechanisms
* Checking persistent memory for poisoning

### OWASP Agentic Top 10 Checklist (2026)
```text
- [ ] ASI01: Agent Goal Hijack (prompt injection — direct & indirect)
- [ ] ASI02: Tool Misuse and Exploitation (shell, filesystem, API abuse)
- [ ] ASI03: Identity and Privilege Abuse (confused deputy, over-privilege)
- [ ] ASI04: Memory Poisoning (SOUL.md, MEMORY.md, persistent context)
- [ ] ASI05: Supply Chain Attacks (malicious skills/plugins — e.g., SkillHub)
- [ ] ASI06: Rogue Agents (operating outside intended boundaries)
- [ ] ASI07: Data Leakage via Agentic Channels (cross-channel PII exposure)
- [ ] ASI08: Orchestration Manipulation (sub-agent hijacking)
- [ ] ASI09: Insufficient Logging and Observability
- [ ] ASI10: Insecure Agent Communication (agent-to-agent trust)
```

### 1. Workspace Configuration Audit
```bash
echo "--- Agent Config Permissions ---"
for f in SOUL.md MEMORY.md AGENTS.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md; do
    [ -f "$f" ] && echo "$(stat -f '%Sp %N' "$f" 2>/dev/null || stat -c '%A %n' "$f")" || echo "  NOT FOUND: $f"
done

echo "--- Secrets in Agent Files ---"
grep -rn -i 'api.key\|password\|token\|secret\|bearer' \
  SOUL.md MEMORY.md TOOLS.md IDENTITY.md USER.md memory/*.md 2>/dev/null | \
  grep -v 'example\|placeholder\|REDACTED'

echo "--- Shell Access Check ---"
grep -rn -i 'sudo\|chmod 777\|unrestricted' AGENTS.md TOOLS.md 2>/dev/null
```

### 2. Prompt Injection Scan (Agent-Facing Content)

> 详细代码示例已移至 `references/detail.md`

### 3. Identity & Authorization Audit
```bash
echo "--- Identity Verification ---"

grep -n 'authorizedSenders\|authorized_senders\|allowlist' \
  ~/.config/skill-platform/config.yaml ~/.skill-platform/config.* 2>/dev/null

grep -rn -i 'display.name\|username\|sender.name' \
  AGENTS.md SOUL.md TOOLS.md 2>/dev/null | \
  grep -iv 'user.id\|sender.id\|verified'

echo "--- Cross-Channel Trust ---"
grep -rn -i 'if.*channel\|trust.*channel\|verify.*channel' \
  AGENTS.md SOUL.md 2>/dev/null
```

### 4. Memory Poisoning Check

> 详细代码示例已移至 `references/detail.md`

### 5. Multi-Agent Communication Audit

> 详细代码示例已移至 `references/detail.md`

### 6. Resource & Privilege Audit

> 详细代码示例已移至 `references/detail.md`

### 7. Semantic Reframing Detection (Advanced)
```bash
echo "--- Content-Based Safety Rules ---"
grep -rn -i 'content.*evaluat\|semantic.*refram\|forward.*email.*sensitive\|assess.*content' \
  AGENTS.md SOUL.md 2>/dev/null

echo "--- PII in Agent-Accessible Files ---"
grep -rPn '\b\d{3}-\d{2}-\d{4}\b' MEMORY.md memory/*.md 2>/dev/null
grep -rPn '\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b' MEMORY.md memory/*.md 2>/dev/null
grep -rPn '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z]{2,}\b' \
  MEMORY.md memory/*.md USER.md 2>/dev/null | \
  grep -v 'example\|test\|placeholder'
```

### Full Agentic Security Audit Script

> 详细代码示例已移至 `references/detail.md`

### References
* [Agents of Chaos — arXiv:2602.20021](https://arxiv.org/abs/2602.20021) — Live red-teaming of Skill平台 agents
* [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
* [NIST AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative)
* [Skill平台 Security Crisis — Conscia](https://conscia.com/blog/the-skill-platform-security-crisis/)

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
- Audit codebases, infrastructure, AND agentic AI systems for security
  issues
- Covers traditional s
- 触发关键词: systems, agentic, audit, infrastructure, codebases, security

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

## 示例
### 示例1：基础用法
```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Agentic Security Aud？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Agentic Security Aud有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
