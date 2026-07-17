---
slug: encryption
name: encryption
version: "1.0.0"
displayName: Encryption
summary: Encrypt files, secure passwords, manage keys, and audit code for cryptographic
  best practices.
license: MIT
description: |-
  Encrypt files, secure passwords, manage keys, and audit code for cryptographic
  best practices.

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: files, passwords, encrypt, secure, manage, encryption
tags:
- Development
tools:
- read
- exec
---

# Encryption

## When to Use

* Encrypting files, database fields, or app storage
* Password hashing (bcrypt, argon2)
* Key management, rotation, derivation
* TLS/certificate configuration
* Auditing code for crypto mistakes
* Mobile secure storage (Keychain, Keystore)

## Algorithm Selection

| Purpose | Use | Avoid |
| --- | --- | --- |
| Passwords | argon2id, bcrypt (cost≥12) | MD5, SHA1, plain SHA256 |
| Symmetric | AES-256-GCM, ChaCha20-Poly1305 | AES-ECB, DES, RC4 |
| Asymmetric | RSA-4096+OAEP, Ed25519, P-256 | RSA-1024, PKCS#1 v1.5 |
| Key derivation | PBKDF2 (≥600k), scrypt, argon2 | Single-pass hash |
| JWT signing | RS256, ES256 | HS256 with weak secret |
| TLS | 1.2+ only | TLS 1.0/1.1, SSLv3 |

## Critical Rules

1. **Never reuse IVs/nonces** — AES-GCM + repeated nonce = catastrophic
2. **Use authenticated encryption (AEAD)** — Plain CBC enables padding oracles
3. **Hash passwords, don't encrypt** — Hashing is one-way
4. **No hardcoded keys** — Use env vars, KMS, or Vault
5. **No Math.random() for crypto** — Use CSPRNG only
6. **Constant-time comparisons** — Prevent timing attacks on secrets
7. **Separate keys by purpose** — Encryption ≠ signing ≠ backup

## File Encryption (CLI)

```bash
age -p -o file.age file.txt
age -d -o file.txt file.age

gpg -c --cipher-algo AES256 file.txt
```

## Platform-Specific

See `patterns.md` for code snippets:

* Password hashing (Node, Python, Go)
* Envelope encryption with KMS
* JWT with RS256 key rotation
* Secure token generation

See `mobile.md` for:

* iOS Keychain wrapper
* Android EncryptedSharedPreferences
* SQLCipher setup
* Biometric auth integration
* Certificate pinning

See `infra.md` for:

* TLS certificate auto-renewal
* HashiCorp Vault policies
* mTLS between services
* Backup encryption verification

## Audit Checklist

* No plaintext passwords in DB/logs/env
* No secrets in git history
* No hardcoded keys in source
* No Math.random() for security
* No deprecated algorithms (MD5, SHA1, DES)
* No disabled cert validation
* IVs/nonces never reused
* PBKDF2 iterations ≥600k / bcrypt cost ≥12
* TLS 1.2+ enforced, old protocols disabled
* Key rotation procedure documented

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
