---
slug: jellyfin-control
name: jellyfin-control
version: "1.3.0"
displayName: Jellyfin Control
summary: Control Jellyfin media server and TV. Search content, resume playback, manage
  sessions, control T...
license: MIT
description: |-
  Control Jellyfin media server and TV。Search content, resume playback,
  manage sessions, control T。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
tools:
  - - read
- exec
---

# Jellyfin Control

A robust skill to control Jellyfin playback and TV power via CLI.

## Features

* **🎯 One-Command Play:** `tv play "Breaking Bad"` — turns on TV, launches Jellyfin, finds the next episode, and plays it.
* **Smart Resume:** Automatically finds the next unplayed episode for series.
* **Resume Position:** Resumes Movies/Episodes exactly where left off (with `Seek` fallback for LG WebOS/Tizen).
* **Device Discovery:** Auto-detects controllable sessions (TVs, Phones, Web).
* **Remote Control:** Full playback control (play, pause, stop, next, prev, volume, mute).
* **TV Power & Apps:** Turn TV on/off, launch apps — works with or without Home Assistant.
* **Two TV Backends:** Home Assistant integration or direct WebOS (LG TVs, no HA needed).
* **Android TV Support:** Direct ADB backend for Chromecast w/ Google TV, Nvidia Shield, Fire TV, Mi Box — no HA needed.
* **Three connection modes:** Home Assistant (any TV), direct WebOS (LG), direct ADB (Android TV/Fire TV).

## Quick Start

### Minimal setup (Jellyfin only, no TV control)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://YOUR_IP:8096",
          "JF_API_KEY": "your-api-key-here",
          "JF_USER": "your-username"
        }
      }
    }
  }
}
```

### With Home Assistant (recommended for TV control)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_API_KEY": "your-jellyfin-api-key",
          "JF_USER": "victor",
          "HA_URL": "http://192.168.1.138:8123",
          "HA_TOKEN": "your-ha-long-lived-token",
          "HA_TV_ENTITY": "media_player.lg_webos_tv_oled48c34la",
          "TV_MAC": "AA:BB:CC:DD:EE:FF"
        }
      }
    }
  }
}
```

### Direct WebOS (LG TV, no Home Assistant needed)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_API_KEY": "your-jellyfin-api-key",
          "JF_USER": "victor",
          "TV_IP": "192.168.1.100",
          "TV_MAC": "AA:BB:CC:DD:EE:FF"
        }
      }
    }
  }
}
```

> **First time with WebOS direct:** The TV will show a pairing prompt. Accept it and save the `TV_CLIENT_KEY` the skill prints — add it to your env to skip the prompt next time.

### Direct ADB (Android TV / Fire TV / Chromecast with Google TV, no HA needed)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_API_KEY": "your-jellyfin-api-key",
          "JF_USER": "victor",
          "ADB_DEVICE": "192.168.1.100:5555",
          "TV_MAC": "AA:BB:CC:DD:EE:FF"
        }
      }
    }
  }
}
```

> **First time with ADB:** Enable Developer Options on your TV (Settings → About → tap Build Number 7 times), then enable Network/USB debugging. First connection will show "Allow debugging?" on the TV — accept it. Requires `adb` installed on the Skill平台 host (`sudo apt install adb`).

## Environment Variables

### Jellyfin (required)

| Variable | Required | Description |
| --- | --- | --- |
| `JF_URL` | **Yes** | Base URL of your Jellyfin server, e.g. `http://192.168.1.50:8096` |
| `JF_API_KEY` | **Yes** | API key from Jellyfin Dashboard → Advanced → API Keys |
| `JF_USER` | No | Username — used to resolve user ID for user-specific endpoints |
| `JF_USER_ID` | No | User ID directly — avoids needing to call `/Users` |
| `JF_PASS` | No | Password — only if authenticating by user session |

### TV Control (optional — choose one backend)

| Variable | Backend | Description |
| --- | --- | --- |
| `TV_BACKEND` | All | Force backend: `homeassistant`, `webos`, `androidtv`, or `auto` |
| `TV_PLATFORM` | HA | Force platform: `webos` or `androidtv` (auto-detected from entity) |
| `HA_URL` | HA | Home Assistant URL, e.g. `http://192.168.1.138:8123` |
| `HA_TOKEN` | HA | HA long-lived access token (Profile → Long-Lived Access Tokens) |
| `HA_TV_ENTITY` | HA | Entity ID of your TV, e.g. `media_player.lg_webos_tv_oled48c34la` |
| `TV_IP` | WebOS | LG TV IP address for direct WebOS SSAP connection |
| `TV_CLIENT_KEY` | WebOS | Pairing key (printed on first connection — save it!) |
| `ADB_DEVICE` | AndroidTV | TV address for ADB, e.g. `192.168.1.100:5555` |
| `TV_MAC` | All | TV MAC address for Wake-on-LAN (needed to turn on TV) |
| `TV_JELLYFIN_APP` | All | Override Jellyfin app ID (auto: `org.jellyfin.webos` / `org.jellyfin.androidtv`) |
| `TV_BOOT_DELAY` | All | Seconds to wait after TV wake (default: 10) |
| `TV_APP_DELAY` | All | Seconds to wait after launching Jellyfin (default: 8) |

**Auto-detection:** If `TV_BACKEND` is `auto` (default):

1. `HA_URL` + `HA_TOKEN` + `HA_TV_ENTITY` set → Home Assistant backend
2. `ADB_DEVICE` set → direct ADB (Android TV)
3. `TV_IP` set → direct WebOS (LG)
4. Nothing set → TV commands disabled, Jellyfin-only mode

## Usage

### 🎯 One-Command Play (the magic)

Turn on TV → launch Jellyfin → find next episode → play it. All in one command:

```bash
node skills/jellyfin-control/cli.js tv play "Breaking Bad"
node skills/jellyfin-control/cli.js tv play "The Matrix"
```

The skill validates the content exists BEFORE turning on the TV (fail fast).

### Resume / Play Smart

If TV and Jellyfin are already running:

```bash
node skills/jellyfin-control/cli.js resume "Breaking Bad"
node skills/jellyfin-control/cli.js resume "Matrix" --device "Chromecast"
```

### TV Control

```bash
node skills/jellyfin-control/cli.js tv on           # Turn on (Wake-on-LAN)
node skills/jellyfin-control/cli.js tv off          # Turn off
node skills/jellyfin-control/cli.js tv launch       # Launch Jellyfin app
node skills/jellyfin-control/cli.js tv launch com.webos.app.hdmi1  # Launch specific app
node skills/jellyfin-control/cli.js tv apps         # List installed apps
```

### Remote Control

```bash
node skills/jellyfin-control/cli.js control pause
node skills/jellyfin-control/cli.js control play
node skills/jellyfin-control/cli.js control next
node skills/jellyfin-control/cli.js control vol 50
```

### Search Content

```bash
node skills/jellyfin-control/cli.js search "Star Wars"
```

### Library Stats & Scan

```bash
node skills/jellyfin-control/cli.js stats
node skills/jellyfin-control/cli.js scan            # requires admin API key
```

### User History (requires admin API key)

```bash
node skills/jellyfin-control/cli.js history
node skills/jellyfin-control/cli.js history jorge --days 7
```

## Choosing a TV Backend

| Feature | Home Assistant | Direct WebOS | Direct ADB (Android TV) | No Backend |
| --- | --- | --- | --- | --- |
| TV brands | Any (via HA) | LG only | Android TV, Fire TV, CCwGTV | — |
| Turn on (WoL) | ✅ | ✅ | ✅ (WoL or ADB wakeup) | — |
| Turn off | ✅ | ✅ | ✅ | — |
| Launch apps | ✅ | ✅ | ✅ | — |
| List apps | ✅ (via HA logs) | ✅ (direct output) | ✅ (direct output) | — |
| Extra dependency | None | `npm install ws` | `apt install adb` | None |
| Setup complexity | Medium (need HA) | Low (TV IP + MAC) | Low (enable ADB on TV) | None |
| Jellyfin playback | ✅ | ✅ | ✅ | ✅ |

**Recommendation:**

* Already have Home Assistant? → Use HA backend (most versatile, any TV brand)
* LG WebOS TV, no HA? → Use direct WebOS backend
* Android TV / Fire TV / Chromecast with Google TV, no HA? → Use direct ADB backend
* No smart TV control needed? → Skip TV config, `resume` works if Jellyfin app is already open

## Security Notes

* **API keys only in `skill-platform.json` env** — never in workspace files, `.env` files, or markdown docs.
* **HA tokens** are long-lived and powerful. Create a dedicated HA user with limited permissions if possible.
* **TV_CLIENT_KEY** (WebOS) is sensitive — it allows full control of your TV. Treat it like a password.
* **ADB access** grants full control of your Android TV. Ensure your network is secured — anyone on the same network could connect via ADB if debugging is enabled.
* **Admin operations** (`history`, `scan`) require an admin-level Jellyfin API key and will fail gracefully with 403 if permissions are insufficient.

## Architecture

* `lib/jellyfin.js` — Jellyfin REST API (auth, search, sessions, playback control)
* `lib/tv.js` — TV control abstraction (HA backend, WebOS backend, Wake-on-LAN)
* `cli.js` — User-friendly CLI with all commands

## Workflow: Agent says "Play Star Trek on TV"

```text
Agent → cli.js tv play "Star Trek"
         │
         ├── 1. Search Jellyfin for "Star Trek" (fail fast)
         ├── 2. Find next unplayed episode
         ├── 3. Wake-on-LAN → TV turns on
         ├── 4. Wait 10s for boot
         ├── 5. Launch Jellyfin app (HA or WebOS)
         ├── 6. Wait 8s for session registration
         ├── 7. Find Jellyfin session (retry 3x)
         └── 8. Play episode on session
```

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### Minimal setup (Jellyfin only, no TV control)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://YOUR_IP:8096",
          "JF_API_KEY": "your-api-key-here",
          "JF_USER": "your-username"
        }
      }
    }
  }
}
```

### With Home Assistant (recommended for TV control)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_AP
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Jellyfin Control？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Jellyfin Control有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
