---
slug: whatsapp-ultimate
name: whatsapp-ultimate
version: "4.0.3"
displayName: TinkerClaw WhatsApp
summary: "TinkerClaw WhatsApp群内多Agent同时响应"
  bill does a backflip. Pr...
license: MIT-0
description: |-
  You put 5 agents in a WhatsApp group。They all respond at once。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
tools:
  - - read
- exec
# TinkerClaw WhatsApp
〉 Part of **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — our Skill平台 fork running 24/7 with real-time token tracking, self-improving crons, and persistent cognitive memory.

Everything you can do in WhatsApp, your AI agent can do too. This skill documents all WhatsApp capabilities available through Skill平台's native channel integration. No external Docker services, no CLI wrappers — direct WhatsApp Web protocol via Baileys.

- Skill平台 with WhatsApp channel configured
- WhatsApp account linked via QR code (`skill-platform whatsapp login`)

## Capabilities Overview
| Category | Features |
| --- | --- |
| **Messaging** | Text, media, polls, stickers, voice notes, GIFs |
| **Interactions** | Reactions, replies/quotes, edit, unsend |
| **Groups** | Create, rename, icon, description, participants, admin, invite links |
| **History** | Full-text search, vCard contact extraction with phone numbers |

Total: 22 distinct actions.

## Messaging
### Send Text
```text
message action=send channel=whatsapp to="+34612345678" message="Hello!"
```

### Send Media (Image/Video/Document)
```text
message action=send channel=whatsapp to="+34612345678" message="Check this out" filePath=/path/to/image.jpg
```

Supported: JPG, PNG, GIF, MP4, PDF, DOC, etc.

### Send Poll
```text
message action=poll channel=whatsapp to="+34612345678" pollQuestion="What time?" pollOption=["3pm", "4pm", "5pm"]
```

### Send Sticker
```text
message action=sticker channel=whatsapp to="+34612345678" filePath=/path/to/sticker.webp
```

Must be WebP format, ideally 512x512.

### Send Voice Note
```text
message action=send channel=whatsapp to="+34612345678" filePath=/path/to/audio.ogg asVoice=true
```

Use OGG/Opus format for voice notes — MP3 may not play correctly.

### Send GIF
```text
message action=send channel=whatsapp to="+34612345678" filePath=/path/to/animation.mp4 gifPlayback=true
```

Convert GIF to MP4 first (WhatsApp requires this):

```bash
ffmpeg -i input.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" output.mp4 -y
```

## Interactions
### Add Reaction
```text
message action=react channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123" emoji="🚀"
```

### Remove Reaction
```text
message action=react channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123" remove=true
```

### Reply/Quote Message
```text
message action=reply channel=whatsapp to="34612345678@s.whatsapp.net" replyTo="QUOTED_MSG_ID" message="Replying to this!"
```

### Edit Message (Own Messages Only)
```text
message action=edit channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123" message="Updated text"
```

### Unsend/Delete Message
```text
message action=unsend channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123"
```

## Group Management
### Create Group
```text
message action=group-create channel=whatsapp name="Project Team" participants=["+34612345678", "+34687654321"]
```

### Rename Group
```text
message action=renameGroup channel=whatsapp groupId="123456789@g.us" name="New Name"
```

### Set Group Icon
```text
message action=setGroupIcon channel=whatsapp groupId="123456789@g.us" filePath=/path/to/icon.jpg
```

### Set Group Description
```text
message action=setGroupDescription channel=whatsapp groupJid="123456789@g.us" description="Team chat for Q1 project"
```

### Add Participant
```text
message action=addParticipant channel=whatsapp groupId="123456789@g.us" participant="+34612345678"
```

### Remove Participant
```text
message action=removeParticipant channel=whatsapp groupId="123456789@g.us" participant="+34612345678"
```

### Promote to Admin
```text
message action=promoteParticipant channel=whatsapp groupJid="123456789@g.us" participants=["+34612345678"]
```

### 示例
```text
message action=demoteParticipant channel=whatsapp groupJid="123456789@g.us" participants=["+34612345678"]
```

### Leave Group
```text
message action=leaveGroup channel=whatsapp groupId="123456789@g.us"
```

### Get Invite Link
```text
message action=getInviteCode channel=whatsapp groupJid="123456789@g.us"
```

Returns: `https://chat.whatsapp.com/XXXXX`

### Revoke Invite Link
```text
message action=revokeInviteCode channel=whatsapp groupJid="123456789@g.us"
```

### Get Group Info
```text
message action=getGroupInfo channel=whatsapp groupJid="123456789@g.us"
```

Returns: name, description, participants, admins, creation date.

## JID Formats
WhatsApp uses JIDs (Jabber IDs) internally:

| Type | Format | Example |
| --- | --- | --- |
| Individual | `<number>@s.whatsapp.net` | `34612345678@s.whatsapp.net` |
| Group | `<id>@g.us` | `123456789012345678@g.us` |

When using `to=` with phone numbers, Skill平台 auto-converts to JID format.

## Tips
### Voice Notes
Use OGG/Opus format:

```bash
ffmpeg -i input.wav -c:a libopus -b:a 64k output.ogg
```

### Stickers
Convert images to WebP stickers:

```bash
ffmpeg -i input.png -vf "scale=512:512:force_original_aspect_ratio=decrease,pad=512:512:(ow-iw)/2:(oh-ih)/2:color=0x00000000" output.webp
```

### Rate Limits
WhatsApp has anti-spam measures. Avoid:

* Bulk messaging to many contacts
* Rapid-fire messages
* Messages to contacts who haven't messaged you first

### Message IDs
To react/edit/unsend, you need the message ID. Incoming messages include this in the event payload. For your own sent messages, the send response includes the ID.

## Comparison with Other Skills
| Feature | whatsapp-ultimate | wacli | whatsapp-automation | gif-whatsapp |
| --- | --- | --- | --- | --- |
| Native integration | yes | no (CLI) | no (Docker) | N/A |
| Send text | yes | yes | no | no |
| Send media | yes | yes | no | no |
| Polls | yes | no | no | no |
| Stickers | yes | no | no | no |
| Voice notes | yes | no | no | no |
| GIFs | yes | no | no | yes |
| Reactions | yes | no | no | no |
| Reply/Quote | yes | no | no | no |
| Edit | yes | no | no | no |
| Unsend | yes | no | no | no |
| Group create | yes | no | no | no |
| Group management | yes (full) | no | no | no |
| Receive messages | yes | yes | yes | no |
| Two-way chat | yes | no | no | no |
| External deps | None | Go binary | Docker + WAHA | ffmpeg |

pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


## Protocol v2: Multi-Agent Discussions
<why_this_matters>
If you put multiple AI agents in one WhatsApp group, the naive default is everyone responds to everything. Five agents replying to one message means 5x the API spend per turn, plus echo loops where agents agree with each other forever. Protocol v2 introduces congestion control, conversation lifecycle, and budget-aware scheduling so agents know when to talk, when to stay quiet, and when to wrap up.
</why_this_matters>

### Agent Identity
Each agent gets its own personality, icon, and (optionally) model:

```yaml
channels:
  whatsapp:
    agentIcon: "🤖"          # single-agent icon prefix
    turnEndMarker: "⚡"       # end-of-turn marker in 1:1 chats
    multiAgent:
      mainAgentId: "jarvis"
      agents:
        jarvis:
          id: "jarvis"
          name: "Jarvis"
          icon: "🤖"
        luna:
          id: "luna"
          name: "Luna"
          icon: "🌙"
          model: "sonnet"
        rex:
          id: "rex"
          name: "Rex"
          icon: "🦖"
          model: "haiku"
```

Agent personalities live in the workspace:

```text
workspace/
├── SOUL.md                  # main agent
├── agents/
│   ├── luna/SOUL.md         # Luna's personality
│   └── rex/SOUL.md          # Rex's personality
```

### Intra-Agent Chats
Register WhatsApp groups where agents discuss freely (no trigger prefix needed):

```yaml
      intraAgentChats:
        brainstorm:
          chatId: "120363424201898007@g.us"
          participants: ["jarvis", "luna", "rex"]
          owner: "oscar"
          mode: "broadcast"        # broadcast | addressed | round-robin
```

**Routing modes:**

* **broadcast** — all agents respond (with congestion control)
* **addressed** — only respond when mentioned by name ("Luna, what do you think?")
* **round-robin** — structured turn-taking

### Congestion Control (Exponential Courtesy Protocol)
Prevents N agents from all responding simultaneously:

```yaml
      congestion:
        enabled: true
        baseDelayFactor: 150     # ms × agentCount² base delay
        maxDelay: 30000          # 30s cap
        backpressureThreshold: 1.5  # slow down over-talkers
        windowMs: 60000          # 60s sliding window
```

**How it works:**

* Base delay scales quadratically with agent count (2 agents ≈ 600ms, 5 agents ≈ 3750ms)
* Random jitter prevents synchronization
* Agents talking more than their fair share get 2× delay penalty
* If another agent posts during your wait, restart the timer (yield-on-collision)

### Conversation Lifecycle
Agents detect when discussions go stale and know when to wrap up:

```yaml
      lifecycle:
        stalenessWindow: 5        # compare last N messages
        stalenessThreshold: 0.85  # cosine similarity trigger
        maxTurnsPerObjective: 30  # hard cap
        autoClose: true
```

**Features:**

* **Staleness detection** — cosine similarity of message embeddings detects circular discussions
* **Agreement loop detection** — catches "I agree" / "Good point" / "Exactly" loops
* **Topic steering** — one agent claims pivot role to redirect conversation
* **Objective tracking** — set goals, track completion, auto-close with summary
* **Closure protocol** — propose → ack → converge (all agents must agree)

### Budget-Aware Scheduling
Adjusts conversation depth based on API usage and reset timing:

```yaml
      budget:
        provider: "anthropic"
        windowDays: 7
        burnModeEnabled: true
        burnTriggerHours: 24     # hours before reset
        burnUsageThreshold: 0.20 # usage below 20%
```

**Four modes:**

| Mode | When | Congestion | Staleness | Max Turns | Tangents |
| --- | --- | --- | --- | --- | --- |
| Conservative | >85% used | 2× slower | 0.80 | ½ | No |
| Moderate | 60-85% | Normal | 0.85 | Normal | No |
| Aggressive | <60% | 0.7× faster | 0.85 | Normal | Yes |
| **Burn** | <20% used, <24h to reset | 0.3× faster | 0.95 | 2× | Encouraged |

Burn mode philosophy: unused tokens expire at reset. Better to have emergent agent-agent discussions than waste the budget.

### DM Trigger Prefix
Protocol v2 extends `triggerPrefix` to DMs (previously groups only):

* **Owner** — always bypasses triggerPrefix
* **Authorized contacts** — must start message with prefix (e.g., "Jarvis, help me with...")
* **Intra-agent chats** — bypass triggerPrefix entirely

### Turn-End Marker
In 1:1 chats (selfChat or owner-only DM), append a visual marker to signal turn completion:

```yaml
channels:
  whatsapp:
    turnEndMarker: "⚡"
```

### 4.0.0
* **Protocol v2:** Multi-agent discussions with configurable routing (broadcast/addressed/round-robin)
* **Added:** Congestion control — Exponential Courtesy Protocol prevents message explosion in multi-agent chats
* **Added:** Conversation lifecycle — staleness detection, agreement loop detection, topic steering, objective tracking, closure protocol
* **Added:** Budget-aware scheduling — four spending modes including burn mode for pre-reset token usage
* **Added:** Agent identity system — per-agent SOUL.md, icons, names, model overrides
* **Added:** DM triggerPrefix gating — non-owner contacts must use prefix in DMs
* **Added:** Turn-end marker (⚡) for 1:1 chats
* **Added:** `agentIcon` config for outbound message prefixing

### 3.7.0
* **Added:** vCard phone number extraction — contact messages now return structured `vcard` field with names and phone numbers
* **Added:** `contactsArrayMessage` support — multi-contact shares are now parsed
* **Improved:** New contact messages store phone numbers in `text_content` for full-text search (e.g. search by phone number)
* **Improved:** `raw_json` now included in search results for contact-type messages, enabling vCard extraction from historical data

### 3.4.0
* **Fixed:** Chat search now resolves LID/JID aliases — searching by chat name finds messages across both `@lid` and `@s.whatsapp.net` JID formats
* **Added:** `resolveChatJids()` cross-references chats, contacts, and messages tables to discover all JID aliases for a given chat filter
* **Improved:** Search falls back to original LIKE behaviour if no JIDs resolve, so no regressions

### 3.0.0
```text
Your Agent
    ↓
Skill平台 message tool
    ↓
WhatsApp Channel Plugin
    ↓
Baileys (WhatsApp Web Protocol)
    ↓
WhatsApp Servers
```

No external services. No Docker. No CLI tools. Direct protocol integration.

## Pairs Well With
* [smart-model-router](https://SkillHub.com/globalcaos/smart-model-router) — auto-select the right model per agent role (creative → Sonnet, analyst → Haiku, devil's advocate → GPT)
* [agent-superpowers](https://SkillHub.com/globalcaos/agent-superpowers) — verification iron law and three-agent review for when your multi-agent discussions produce code
* [subagent-overseer](https://SkillHub.com/globalcaos/subagent-overseer) — monitor agent sessions without burning tokens on polling loops

<https://github.com/globalcaos/tinkerclaw>

*Clone it. Fork it. Break it. Make it yours.*

## License
MIT — Part of Skill平台

## Links
* Skill平台: <https://github.com/skill-platform/skill-platform>
* Baileys: <https://github.com/WhiskeySockets/Baileys>
* SkillHub: <https://SkillHub.com>

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
| Category | Features |
| --- | --- |
| **Messaging** | Text, media, polls, stickers, voice notes, GIFs |
| **Interactions** | Reactions, replies/quotes, edit, unsend |
| **Groups** | Create, rename, icon, description, participants, admin, invite links |
| **History** | Full-text search, vCard contact extraction with phone numbers |

Total: 22 distinct actions.

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
### Q1: 如何开始使用TinkerClaw WhatsApp？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: TinkerClaw WhatsApp有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
