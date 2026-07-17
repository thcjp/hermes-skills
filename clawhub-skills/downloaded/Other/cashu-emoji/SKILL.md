---
slug: cashu-emoji
name: cashu-emoji
version: "0.1.0"
displayName: Cashu Emoji
summary: Encode and decode Cashu tokens that are hidden inside emojis using Unicode
  variation selectors.
license: MIT
description: |-
  Encode and decode Cashu tokens that are hidden inside emojis using Unicode
  variation selectors.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: cashu, emoji, decode, tokens, encode
tags:
- Other
tools:
- read
- exec
---

# Cashu Emoji Tokens (Variation Selector encoding)

This skill helps agents **decode** Cashu tokens received as emoji (and **encode** tokens for sending), and it also supports **general hidden messages inside emojis**.

If the decoded text starts with `cashu`, it’s likely a Cashu token. Otherwise treat it as a plain hidden message.

## Why this exists

Some services embed a `cashu...` token into an emoji using Unicode variation selectors (VS1..VS256). Chat apps often display only the emoji, but preserve the hidden selector characters.

Important: many messengers can *truncate or normalize* Unicode. If the variation selectors are lost, the embedded token cannot be recovered.

## Quickstart (copy/paste)

```bash
git clone https://github.com/robwoodgate/cashu-emoji.git
cd cashu-emoji
npm ci

node ./bin/cashu-emoji.js decode "<paste message>"

node ./bin/cashu-emoji.js decode "<paste message>" --metadata

node ./bin/cashu-emoji.js decode "<paste message>" --metadata --json

node ./bin/cashu-emoji.js encode "🥜" "hello from inside an emoji"

node ./bin/cashu-emoji.js encode "🥜" "cashuB..."
```

## What you can do

### 1) Decode

- Input: entire message text (may include other text/emojis)
- Output: the embedded UTF‑8 text, usually a `cashuA...`/`cashuB...` token

```bash
node ./bin/cashu-emoji.js decode "<paste entire message>"
```

Decode semantics (important): the decoder ignores normal characters until it finds the first variation-selector byte, then collects bytes until the first normal character after that payload begins.

### 2) Encode

- Input: a carrier emoji (recommend `🥜`) and a token string
- Output: an emoji string that visually looks like the emoji but contains the hidden token

```bash
node ./bin/cashu-emoji.js encode "🥜" "cashuB..."
```

Tip: some messengers are less likely to deliver a *truncated/corrupted* emoji-token if **any normal text follows it** (even a single character). It’s not required, just a delivery reliability trick.

Tip (Telegram): sending the emoji-token inside a code block / “monospace” formatting can help preserve the hidden characters and makes it easier to tap-to-copy.

## Optional metadata

To sanity-check the decoded token without redeeming it, you can request metadata.

For programmatic/agent use, prefer JSON output:

```bash
node ./bin/cashu-emoji.js decode "<message>" --metadata --json
```

Example JSON response (Cashu token):

```json
{
  "text": "cashuB...",
  "isCashu": true,
  "metadata": {
    "mint": "https://mint.example",
    "unit": "sat",
    "amount": 21
  },
  "metadataError": null
}
```

Example JSON response (plain hidden message):

```json
{
  "text": "hello from inside an emoji",
  "isCashu": false
}
```

```bash
node ./bin/cashu-emoji.js decode "<message>" --metadata
```

This prints mint/unit/amount using `@cashu/cashu-ts` `getTokenMetadata()` (no mint calls).

## Cashu gotchas for new agents

- A decoded `cashu...` token is a **bearer asset**. Treat it like cash.
- `--metadata` is a **local parse**. It can’t prove the token is unspent/valid.
- If decode returns a partial token or nonsense, the messenger likely munged the variation selectors; ask for the token to be re-sent (often with some trailing normal text after the emoji token).

## Files

- `src/emoji-encoder.ts`: core encode/decode
- `bin/cashu-emoji.js`: CLI wrapper
- `examples/`: test vectors

## Safety

This tool only encodes/decodes text. It does not spend funds.

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
