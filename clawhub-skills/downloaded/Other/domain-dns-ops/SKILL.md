---
slug: domain-dns-ops
name: domain-dns-ops
version: "1.0.0"
displayName: Domain Dns Ops
summary: Domain/DNS ops across Cloudflare, DNSimple, Namecheap for Peter. Use for
  onboarding zones to Clou...
license: MIT
description: |-
  Domain/DNS ops across Cloudflare, DNSimple, Namecheap for Peter。Use
  for onboarding zones to Clou。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Domain/DNS ops across Cloudflare, DNSimple, Namecheap for Peter
- Use
  for onboarding zones to Clou
- 触发关键词: domain, ops, dns, cloudflare, namecheap, dnsimple, across

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

### Q1: 如何开始使用Domain Dns Ops？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Domain Dns Ops有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
