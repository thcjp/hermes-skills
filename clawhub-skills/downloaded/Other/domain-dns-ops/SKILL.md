---
slug: domain-dns-ops
name: domain-dns-ops
version: "1.0.0"
displayName: Domain Dns Ops
summary: Domain/DNS ops across Cloudflare, DNSimple, Namecheap for Peter. Use for
  onboarding zones to Clou...
license: MIT
description: |-
  Domain/DNS ops across Cloudflare, DNSimple, Namecheap for Peter. Use
  for onboarding zones to Clou...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: domain, ops, dns, cloudflare, namecheap, dnsimple, across
tags:
- Other
tools:
- read
- exec
---

# Domain Dns Ops

This skill is a thin router: use `~/Projects/manager` as truth, run the repo scripts, follow the checklists.

## Source of truth (read first)

* `~/Projects/manager/DOMAINS.md` (domain -> target map; registrar hints; exclusions)
* `~/Projects/manager/DNS.md` (Cloudflare onboarding + DNS/redirect checklist)
* `~/Projects/manager/redirect-worker.ts` + `~/Projects/manager/redirect-worker-mapping.md` (worker redirects)

## Golden path (new vanity domain -> Cloudflare -> redirect)

1. **Decide routing model**
   * Page Rule redirect (small scale, per-zone).
   * Rulesets / Bulk Redirects (account-level; needs token perms).
   * Worker route (fallback; uses `redirect-worker`).
2. **Cloudflare zone**
   * Create zone (UI), then confirm with `cli4`:
     + `cli4 --get name=example.com /zones`
3. **Nameservers**
   * If registrar = Namecheap: `cd ~/Projects/manager && source profile && bin/namecheap-set-ns example.com emma.ns.cloudflare.com scott.ns.cloudflare.com`
   * If registrar = DNSimple: see `~/Projects/manager/DNS.md` for delegation API notes.
4. **DNS placeholders (so CF can terminate HTTPS)**
   * Proxied apex `A` + wildcard `A` → `192.0.2.1` (see `~/Projects/manager/DNS.md` for exact `cli4` calls).
5. **Redirect**
   * If using Page Rules: use the `cli4 --post ... /pagerules` template from `~/Projects/manager/DNS.md`.
   * If using Worker: update mapping (`~/Projects/manager/redirect-worker-mapping.md`), deploy/bind routes per `~/Projects/manager/DNS.md`.
6. **Verify**
   * DNS: `dig +short example.com @1.1.1.1` (expect CF anycast).
   * HTTPS redirect: `curl -I https://example.com` (expect `301`).

## Common ops

* **Cloudflare token sanity**: `source ~/.profile` (prefer `CLOUDFLARE_API_TOKEN`; `CF_API_TOKEN` fallback).
* **Disable “Block AI bots”**: `cd ~/Projects/manager && source profile && bin/cloudflare-ai-bots status` / `bin/cloudflare-ai-bots disable`.

## After edits (commit/push)

If you changed anything in `~/Projects/manager` (docs, worker, scripts, mappings): commit there too.

1. Review: `cd ~/Projects/manager && git status && git diff`
2. Stage: `git add <paths>`
3. Commit (Conventional Commits): `git commit -m "feat: …"` / `fix:` / `docs:` / `chore:`
4. Push only when explicitly asked: `git push origin main`

## Guardrails

* Don’t touch `.md` lore domains or `steipete.md` unless explicitly asked; check `~/Projects/manager/DOMAINS.md`.
* Confirm registrar before debugging CF “invalid nameservers” (often “wrong registrar”).
* Prefer reversible steps; verify after each change (NS → DNS → redirect).

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
