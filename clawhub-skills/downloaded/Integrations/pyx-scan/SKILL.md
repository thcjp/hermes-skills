---
slug: pyx-scan
name: pyx-scan
version: "1.1.0"
displayName: Pyx Scan
summary: "装用前查AI Agent技能是否安全,调PYX Scanner API"
  the PYX Scanner API ...
license: MIT
description: |-
  Check whether an AI agent skill is safe before installing or using it。Calls the PYX Scanner API。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Pyx Scan

Verify whether an AI agent skill is safe before installing or using it by querying the PYX Scanner API.

## Workflow

### Step 1: Parse Input

Extract `owner` and `name` from `$ARGUMENTS`.

* Expected format: `owner/name` (e.g., `anthropic/web-search`)
* If `$ARGUMENTS` is empty or missing the `/` separator, ask the user:
  *"Which skill do you want to check? Provide it as `owner/name` (e.g., `anthropic/web-search`)."*
* Trim whitespace. Reject if either part is empty after trimming.

### Step 2: Call the PYX Scanner API

Fetch the safety data:

```text
WebFetch URL: https://scanner.pyxmate.com/api/v1/check/{owner}/{name}
Prompt: "Return the full JSON response body exactly as-is. Do not summarize."
```

If `WebFetch` fails (tool unavailable, network error), fall back to:

```bash
curl -s "https://scanner.pyxmate.com/api/v1/check/{owner}/{name}"
```

### Step 3: Handle Errors

| HTTP Status | Meaning | Action |
| --- | --- | --- |
| **200** | Skill found | Proceed to Step 4 |
| **404** | Skill not in database | Verdict = **UNSCANNED** |
| **429** | Rate limited | Verdict = **ERROR** — "Rate limited. Try again shortly." |
| **5xx** | Server error | Verdict = **ERROR** — "PYX Scanner is temporarily unavailable." |
| Network failure | Cannot reach API | Verdict = **ERROR** — "Could not connect to PYX Scanner." |

### Step 4: Determine Verdict

Use the JSON response fields to determine the verdict:

| Condition | Verdict |
| --- | --- |
| `recommendation == "safe"` AND `is_outdated == false` | **SAFE** |
| `recommendation == "safe"` AND `is_outdated == true` | **OUTDATED** |
| `recommendation == "caution"` | **CAUTION** |
| `recommendation == "danger"` | **FAILED** |
| `recommendation == "unknown"` | **UNSCANNED** |

### Step 5: Output Report

Format the report as structured markdown. Omit any section where the data is null or empty.

**For SAFE verdict:**

```text
## PYX Scan: {owner}/{name}

**Verdict: SAFE** — This skill has been scanned and verified safe.

**Trust Score:** {trust_score}/10 | **Risk Score:** {risk_score}/10 | **Confidence:** {confidence}%
**Intent:** {intent} | **Status:** {status}

### Summary
{summary}

### About
**Purpose:** {about.purpose}
**Capabilities:** {about.capabilities as bullet list}
**Permissions Required:** {about.permissions_required as bullet list}

[View full report]({detail_url}) | [Badge]({badge_url})
```

**For OUTDATED verdict:**

```text
## PYX Scan: {owner}/{name}

**Verdict: OUTDATED** — Last scan was safe, but the skill has been updated since.

The scanned commit (`{scanned_commit}`) no longer matches the latest (`{latest_commit}`).
The new version has NOT been reviewed. Proceed with caution.

**Trust Score:** {trust_score}/10 | **Risk Score:** {risk_score}/10
**Last Safe Commit:** {last_safe_commit}

### Summary
{summary}

[View full report]({detail_url})
```

**For CAUTION verdict:**

```text
## PYX Scan: {owner}/{name}

**Verdict: CAUTION** — This skill has potential risks that need your attention.

**Trust Score:** {trust_score}/10 | **Risk Score:** {risk_score}/10 | **Confidence:** {confidence}%
**Intent:** {intent} | **Status:** {status}

### Summary
{summary}

### About
**Purpose:** {about.purpose}
**Permissions Required:** {about.permissions_required as bullet list}
**Security Notes:** {about.security_notes}

**Do you want to proceed despite the caution rating?** Please confirm before installing or using this skill.

[View full report]({detail_url})
```

**For FAILED verdict:**

```text
## PYX Scan: {owner}/{name}

**Verdict: FAILED** — This skill has been flagged as dangerous. Do NOT install or use it.

**Trust Score:** {trust_score}/10 | **Risk Score:** {risk_score}/10 | **Confidence:** {confidence}%
**Intent:** {intent} | **Status:** {status}

### Summary
{summary}

### About
**Security Notes:** {about.security_notes}

[View full report]({detail_url})
```

**For UNSCANNED verdict:**

```text
## PYX Scan: {owner}/{name}

**Verdict: UNSCANNED** — This skill has not been scanned by PYX Scanner.

No safety data is available. You should:
1. Review the skill's source code manually before use
2. Check the skill's repository for known issues
3. Request a scan at https://scanner.pyxmate.com
```

**For ERROR verdict:**

```text
## PYX Scan: {owner}/{name}

**Verdict: ERROR** — {error_message}

Safety could not be verified. Treat this skill as unverified until you can confirm its safety.
```

## Behavioral Rules

1. **Always call the API** — never skip the check or return a cached/assumed result.
2. **Never soften a FAILED verdict** — if the scan says danger, report danger. Do not add qualifiers like "but it might be fine."
3. **Always ask user confirmation on CAUTION** — the user must explicitly agree before proceeding.
4. **Keep reports concise** — omit null/empty sections rather than showing "N/A."
5. **No raw JSON** — always format the response as the structured markdown report above.

## Self-Scan Awareness

When `$ARGUMENTS` is `pyxmate/pyx-scan`, `pyxmate/pyx-scanner`, or refers to this skill itself, still call the API honestly and report whatever comes back. If the result is UNSCANNED, append:

> *"Yes, even the security scanner's own skill hasn't been scanned yet. We practice what we preach — treat unscanned skills with caution."*

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

- Check whether an AI agent skill is safe before installing or using it
- Calls the PYX Scanner API
- 触发关键词: safe, scan, pyx, check, whether, agent, skill

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

### Q1: 如何开始使用Pyx Scan？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Pyx Scan有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
