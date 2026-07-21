---
slug: join-meeting
name: join-meeting
version: "1.1.15"
displayName: Join meeting
summary: AgentCall (agentcall.dev) — Join a video meeting (Google Meet, Teams, Zoom)
  as an AI bot with voi...
license: MIT
description: |-
  AgentCall (agentcall。dev) — Join a video meeting (Google Meet, Teams,
  Zoom) as an AI bot with voi。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Creative
tools:
  - - read
- exec
# join-meeting
---
**IMPORTANT: Read this entire document before joining a meeting.** This file
contains the CALL_LOOP algorithm (mandatory), active participation rules,
safety requirements (leave/cleanup), and mode-specific guidance. Skipping
sections will result in broken meeting experiences — the user will be left
talking to silence.

**IMPORTANT: Read the whole document on every session, not just the parts you
remember.** This skill is updated frequently — new commands, new events, new
recommended patterns (like the event-driven `tail -f` + Monitor flow in
"How to read events") are added often. Do NOT rely on what you remember from
previous sessions. Re-read this document each time you start a meeting so you
pick up the latest guidance. If unsure whether you are on the latest version,
run `python scripts/python/check_update.py` (see "Checking for Skill Updates").

Join a video meeting as an AI bot with voice and visual presence.

## Prerequisites
- Python 3.10+ (preferred) or Node.js 18+
- Python dependencies: `pip install aiohttp websockets`
- Node.js dependencies: `cd scripts/node && npm install`
- For webpage modes: a local HTTP server running on the specified port

### API Key Setup
> 详细内容已移至 `references/detail.md`

### User Preferences
> 详细内容已移至 `references/detail.md`

## Usage
```bash
./scripts/run.sh <meet-url> [options]
```

## Options
| Option | Default | Description |
|--------|---------|-------------|
| `--mode` | `audio` | `audio` (voice only, simplest), `webpage-audio` (audio from webpage), `webpage-av` (visual avatar), `webpage-av-screenshare` (avatar + screenshare). See Modes Explained below. |
| `--voice-strategy` | `direct` | `collaborative`, `direct` |
| `--bot-name` | `Agent` | Display name in the meeting participant list |
| `--port` | `3000` | Local port for webpage modes (your UI server) |
| `--screenshare-port` | `3001` | Local port for screenshare content |
| `--template` | `pattern` | Built-in UI: `pattern` (default, radial sunburst with per-state colors and the work-in-progress task list), `ring` (neon ring), `orb`, `avatar`, `dashboard`, `blank`, `voice-agent` (no local server needed) |
| `--transcription` | on | Real-time `transcript.final` and `transcript.partial` events. Required for most workflows. Disable with `--no-transcription` to save STT billing if you only need lifecycle events. |
| `--trigger-words` | | Comma-separated aliases for collaborative mode: `june,juno,hey june` |
| `--context` | | Initial context for voice intelligence (max 4000 chars) |
| `--webpage-url` | | Public URL for webpage modes (no tunnel needed) |
| `--screenshare-url` | | Public URL for screenshare content (no tunnel needed) |
| `--max-duration` | plan limit | Max call duration in minutes. Cannot exceed your plan's limit. Check https://agentcall.dev for current limits. |
| `--alone-timeout` | 120 | Leave if alone for N seconds. |
| `--silence-timeout` | 300 | Leave if silent for N seconds. |
| `--api-url` | `https://api.agentcall.dev` | Override API URL for development |

## Bot Naming
Choose STT-friendly names — short, distinctive, real-sounding words that
speech-to-text can reliably capture. Avoid generic phrases like "AI Assistant"
or "Hey Bot" — transcription often garbles these.

**Good names:** Juno, June, Nova, Sage, Atlas, Claude, Aria, Echo
**Avoid:** AI Assistant, My Bot, Hey Agent, Assistant Bot

**Always set trigger words** in collaborative mode to cover STT mishearings:
```
--bot-name "Juno" --trigger-words "juno,june,you know,junior"
--bot-name "Claude" --trigger-words "claude,cloud,clod,clawed"
--bot-name "Nova" --trigger-words "nova,no va,over"
```

The display name in the participant list can be longer (e.g., "Juno - AI Assistant")
but the trigger words should be the short phonetic variants that STT might produce.

## Modes Explained
### audio (default)
Voice only. Bot has no video. Best for: AI assistants, note-takers, voice agents.
No local server needed. Simplest setup.

### webpage-audio
Your local webpage provides audio. Bot's video is black. The webpage can play audio
that meeting participants will hear. Best for: audio-only web apps.
Requires: `--port` pointing to your local HTTP server.

If your webpage is publicly hosted, pass `--webpage-url https://your-site.com/bot`
instead of `--port`. No tunnel or local server needed.

### webpage-av
Your webpage IS the bot's video feed — what renders on the page is what meeting
participants see as the bot's camera. Audio from the page is also captured into
the meeting. The page is loaded once and runs continuously. All updates must come
via WebSocket events from your agent — it does not auto-refresh.

Best for: animated avatars, branded visual presence, agent-controlled dynamic UIs.

The webpage can also be a standalone voice-to-voice agent: it receives the meeting's
audio as microphone input, processes it with its own AI backend, and replies through
the browser's speaker — which FirstCall (meeting infrastructure) captures into the meeting. This means any
existing voice agent webpage can join meetings with zero modification.

Keep it simple. The agent controls the page via WebSocket. The page renders what
the agent tells it to. Use `--template orb` or `--template avatar` for built-in options.

For slides or screen-sharing content, use `webpage-av-screenshare` instead.

> 详细内容已移至 `references/detail.md` - ### webpage-av-screenshare

### Which mode should I use?
> 详细内容已移至 `references/detail.md`

## How the Tunnel Works (Webpage Modes)
For webpage modes, AgentCall creates a secure tunnel from the cloud to your localhost:
1. You run a local HTTP server (or use `--template` which starts one automatically).
2. The bridge script connects a tunnel client to AgentCall's tunnel server via WebSocket.
3. The bot's browser (running in the cloud) loads your page via the tunnel URL.
4. HTTP requests to the tunnel URL are proxied through the tunnel to your localhost.

You do NOT need to expose your machine to the internet. The tunnel handles it.
When using `--template`, the bridge starts a local server and tunnel automatically — no manual setup.
When using `--webpage-url` (public URL), no tunnel is needed — FirstCall loads it directly.

**Port conflicts:** Before starting a local server on a specific port, verify it's available: `lsof -i :PORT`. If another process (e.g., Node.js on port 3000) is already bound, the tunnel will proxy to the wrong server, causing unexpected 404 errors. Use a different port or use `--template` which auto-selects a free port.

### Tunnel Authentication
When creating a call with `ui_port`, the API response includes:
- `tunnel_id` — unique identifier for this tunnel
- `tunnel_access_key` — per-call credential for tunnel authentication
- `tunnel_url` — the public URL where FirstCall loads your page

The tunnel client registers with the server using `tunnel_id` + `tunnel_access_key`.

**IMPORTANT:** The `tunnel_access_key` is NOT your API key (`ak_ac_...`). It is a separate, per-call credential generated specifically for tunnel authentication. Using your API key will fail with an error message explaining the correct credential to use. If using `bridge-visual.py`, this is handled automatically.

## Mic Permissions (Webpage Modes)
> 详细内容已移至 `references/detail.md`

## Voice Strategies Explained

### collaborative (group meetings)
> 详细内容已移至 `references/detail.md`

## Events (stdout)
Each line is a JSON object.

**Event key convention:** Lifecycle events use the `"event"` field. Transcription, meeting, and media events use the `"type"` field. Always check both: `event.get("event") or event.get("type")` (Python) or `event.event || event.type` (JS). **Tip:** `bridge.py` normalizes all events to use the `"event"` field — if using `join.py` directly, always check both fields.

**Startup time:** After creating a call, the bot takes 30-90 seconds to join the meeting (varies by platform — Google Meet is fastest, Teams/Zoom can take longer). During this time you'll see lifecycle events: `call.created` → `call.bot_joining` → `call.bot_joining_meeting` → `call.bot_ready`. The agent MUST wait patiently and NOT timeout or assume failure during this window. If using `bridge.py`, it handles this automatically — the agent simply waits for the first `user.message` or `greeting.prompt` event.

### Lifecycle
> 详细内容已移至 `references/detail.md`

### Transcription
```json
{"type": "transcript.final", "text": "What do you think about Q3?", "speaker": {"id": "p-1", "name": "Alice"}, "timestamp": "2026-03-25T10:05:23.456Z"}
{"type": "transcript.partial", "text": "What do you thi", "speaker": {"id": "p-1", "name": "Alice"}, "timestamp": "2026-03-25T10:05:22.100Z"}
```
Note: `transcript.partial` in direct mode only. Includes `speaker.id`, `speaker.name`, and `timestamp`.

### Meeting Awareness
```json
{"type": "participant.joined", "participant": {"id": "p-1", "name": "Alice"}, "participants": [{"id": "p-1", "name": "Alice"}]}
{"type": "participant.left", "participant": {"id": "p-2", "name": "Bob"}, "participants": [{"id": "p-1", "name": "Alice"}]}
{"type": "active_speaker", "speaker": {"id": "p-1", "name": "Alice"}}
{"type": "chat.message", "sender": "Alice", "message": "Can everyone hear me?", "message_id": "msg-123"}
```

### Voice State (collaborative only)
```json
{"event": "voice.state", "state": "listening"}
{"event": "voice.text", "text": "The revenue was 2.4 million dollars."}
```
7 states (collaborative mode only — GetSun (collaborative voice intelligence)):

| State | Meaning |
|-------|---------|
| `listening` | Default — hearing the conversation, not engaged |
| `actively_listening` | Trigger word detected, capturing the full question |
| `thinking` | Processing a response |
| `waiting_to_speak` | Response ready, waiting for silence (barge-in prevention) |
| `speaking` | Speaking via TTS |
| `interrupted` | Someone talked over the bot, stopped speaking |
| `contextually_aware` | Just responded — actively monitoring conversation for follow-up questions or related discussion. Lasts ~20 seconds after speaking. |

`voice.text` shows each sentence the bot is speaking (for agent awareness).

### TTS Events
```json
{"event": "tts.started", "destination": "meeting"}
{"event": "tts.done", "destination": "meeting"}
{"event": "tts.audio", "data": "base64-pcm-24khz...", "chunk_index": 0, "is_last": false, "duration_ms": 2500}
{"event": "tts.webpage_audio", "data": "base64-pcm-24khz..."}
{"event": "tts.error", "reason": "tts_unavailable"}
{"event": "tts.interrupted", "reason": "user_speaking", "played": ["..."], "not_played": ["..."]}
```
- `tts.started/done` — bracket TTS generation with destination info.
- `tts.interrupted` — bot audio was stopped because a human started sustained speech (webpage modes, direct only). `played` lists sentences the participant heard fully; `not_played` lists sentences cut mid-way or never started. See "Interruption handling" above for the full debounce mechanic.
- `tts.audio` — raw 24kHz PCM chunks returned to agent (when `destination: "agent"`).
- `tts.webpage_audio` — audio sent to webpage via tunnel (when `destination: "webpage"`).

### Media
```json
{"type": "audio.chunk", "data": "base64-pcm-16khz...", "timestamp": "..."}
{"type": "screenshot.result", "data": "base64-jpeg...", "width": 1920, "height": 1080, "request_id": "req-1"}
{"type": "capture.started", "interval_ms": 1000}
{"type": "capture.frame", "data": "base64-jpeg...", "frame_number": 5}
{"type": "capture.stopped", "total_frames": 30}
{"type": "screenshare.started", "url": "https://..."}
{"type": "screenshare.stopped"}
{"type": "screenshare.error", "message": "Failed to load URL"}
```
`audio.chunk` requires `audio_streaming: true` in the call creation request (REST API only — not available as a CLI flag). This streams raw 16kHz PCM meeting audio to the agent. Most workflows don't need this — use `transcript.final` instead. See the [Multilingual Note-Taker](examples/notetaker-multilingual/) example for a use case.

### System
```json
{"type": "command.ack", "command": "meeting.send_chat", "request_id": "req-1"}
{"type": "command.error", "message": "Bot container not connected", "command": "meeting.send_chat"}
```

## Commands (stdin)
> 详细内容已移至 `references/detail.md`

### Voice Intelligence (collaborative only)
> 详细内容已移至 `references/detail.md`

### TTS (direct mode)
> 详细内容已移至 `references/detail.md`

### Raw Audio (direct mode)
```json
{"type": "audio.inject", "data": "base64-pcm-16khz-16bit-mono..."}
{"type": "audio.clear"}
```

### Meeting Actions (all modes)

`voice.state_update` manually sets the avatar's voice state in direct mode (webpage modes only). Broadcast as `voice.state` event to all connected clients including the avatar template. States: `listening`, `actively_listening`, `thinking`, `waiting_to_speak`, `speaking`, `interrupted`, `contextually_aware`. Note: `speaking` and `listening` are set automatically around `tts.speak` — use this for custom states like `thinking` while processing.

`events.replay` requests buffered events for crash recovery. Returns last 200 events or 5 minutes. See Crash Recovery section.

## Default Behavior: Active Participation
> 详细内容已移至 `references/detail.md`

## Interaction Patterns
### Pattern 1: Meeting Assistant (collaborative)

**Follow THE CALL_LOOP algorithm (see Pattern 5 → Method 1 below — event-driven, recommended).**

### Pattern 2: Customer Support (direct)
```
Agent joins → CALL_LOOP:
  → greeting.prompt received: tts.speak "Hi [name]! I'm [bot]. How can I help you today?"
  → Check events (every 2-3s)
  → user.message received:
    → Simple question: tts.speak with answer
    → Complex question: tts.speak "Let me look into that"
      → Do ONE step → check call → next step → check call → tts.speak with answer
  → No new events: sleep 2 → check again
  → call.ended: exit loop

Agent IS the voice. Every second without checking = silence.
Always greet, always respond, always participate.
```
**Follow THE CALL_LOOP algorithm (see Pattern 5 → Method 1 below — event-driven, recommended).**

### Pattern 3: Voice Agent Webpage (direct + webpage-av)
```
Agent joins with voice agent page on --port 3000 or --webpage-url
  → Page receives meeting audio as mic input
  → Page's AI processes and generates response
  → Page plays response audio → participants hear it
  → Agent monitors via transcript.final for logging/context updates
```

### Pattern 4: Silent Observer (opt-in only)
**Use ONLY when the user explicitly asks for notetaking, silent observation, or passive mode.**
Keywords: "just take notes", "don't speak", "silent mode", "passive", "notetaker".
If the user does not explicitly request silent mode, use Pattern 1, 2, or 5 instead.
```
Agent joins with --transcription
  → Collects all transcript.final events
  → Never speaks
  → After call.ended: process transcript, generate action items
```

## Crash Recovery
If the agent process crashes:
1. On startup, checks `.agentcall-state.json` for an active call (expires after 24h)
2. Calls `GET /v1/calls/{call_id}` to verify call is still active
3. Reconnects to the WebSocket
4. Receives enriched `call.state` snapshot (status, participants, active speaker)
5. Sends `{"type": "events.replay"}` to get missed events (last 200 or 5 min)
6. Deduplicates and processes missed events
7. (Optional) Gets full transcript via `GET /v1/calls/{id}/transcript`

The state file is automatically cleaned up on normal exit.
See [Crash Recovery Guide](references/guides/crash-recovery.md) for full examples and deduplication patterns.

## Built-in UI Templates
Use `--template` instead of `--port` to use a built-in template (no local server needed):

| Template | Description |
|----------|-------------|
| `ring` | **Default.** Neon ring with glow, pulses on speak/think, 7 voice state colors |
| `orb` | Pulsing filled orb that reacts to voice state (8 colors) |
| `avatar` | Circular avatar image with all 7 voice states + status text |
| `dashboard` | Participant list + live transcript + connection status (monitor tool) |
| `blank` | Bot name on black background (placeholder) |
| `voice-agent` | Mic-enabled voice agent base with auto-start getUserMedia |

## Transcript Retrieval
After the call ends, the full transcript is available:
```bash
curl https://api.agentcall.dev/v1/calls/{call_id}/transcript?format=json \
  -H "Authorization: Bearer ak_ac_xxx"
```

Transcripts are stored by FirstCall (meeting infrastructure) for `transcript_retention_hours` (default 24h, max 7 days).

## Safety
| Feature | Default |
|---------|---------|
| Auto-leave when alone | 2 minutes |
| Silence timeout | 5 minutes |
| Max duration | Plan limit (check https://agentcall.dev for current limits) |
| Transcription | On (required for agent to receive speech as text) |
| Bot visible in participant list | Always |
| Meeting host can kick bot | Always |

**Always clean up:** Send `{"command": "leave"}` or `DELETE /v1/calls/{id}` when
done. The safety timeouts above are last resorts — they don't trigger immediately.
An orphaned bot with participants in the meeting will run until `max_duration` (1 hour),
accumulating charges the entire time.

## Pricing
Base plan: 6 hours (audio mode), 1 concurrent call. All features included.
Paid: per-minute billing. Base rate varies by mode (audio cheapest, screenshare
most expensive). Add-ons: transcription, voice intelligence, TTS.
Check https://agentcall.dev for current rates and plan limits.

## Checking for Skill Updates (optional)
> 详细内容已移至 `references/detail.md`

## 示例
- [Simple Note-Taker](examples/notetaker-simple/) — join a meeting, save the transcript to a file (Python + Node.js)
- [Smart Note-Taker](examples/notetaker-smart/) — transcript + LLM summarization with action items (Python + Node.js, works with Claude/GPT-4o/Gemini)
- [Multilingual Note-Taker](examples/notetaker-multilingual/) — collect raw audio, send to Gemini for multilingual transcription + translation + summary (Python)
- [Customer Support Agent](examples/support-agent/) — 1-on-1 support bot with TTS, LLM decision making, knowledge base, and call logging (Python)
- [Meeting Assistant](examples/meeting-assistant/) — collaborative mode with avatar, trigger words, barge-in prevention, and autonomous voice intelligence (Python)
- [Smart Meeting Assistant](examples/meeting-assistant-smart/) — collaborative mode + background task execution with tools, instant acknowledgment, context updates, and result injection (Python)
- [Voice Bridge for Coding Agents](examples/coding-companion/) — mid-session voice I/O for AI coding agents (Claude Code, Cursor, Codex). No separate LLM — the agent framework IS the intelligence. Includes VAD buffering, chat I/O, skill definition (Python)

## Guides
- [Collaborative Mode Guide](references/guides/collaborative-mode.md) — context system, inject patterns, background tasks
- [Webpage Audio Guide](references/guides/webpage-audio.md) — audio queue, interruption handling, AgentCallAudio player
- [Interruption Handling Guide](references/guides/interruption-handling.md) — VAD, sentence tracking, resume patterns
- [Webpage AV Guide](references/guides/webpage-av.md) — avatar, brand, voice agent webpage
- [Webpage AV Screenshare Guide](references/guides/webpage-av-screenshare.md) — dual visual presence, screenshare control
- [UI Templates Guide](references/guides/ui-templates.md) — all templates, voice states, mic setup
- [Crash Recovery Guide](references/guides/crash-recovery.md) — event replay, deduplication, recovery example

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
- AgentCall (agentcall
- dev) — Join a video meeting (Google Meet, Teams,
  Zoom) as an AI bot with voi
- 触发关键词: video, agentcall, join, meeting

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
### Q1: 如何开始使用Join meeting？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Join meeting有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
