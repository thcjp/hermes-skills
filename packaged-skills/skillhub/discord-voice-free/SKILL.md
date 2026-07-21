---
slug: discord-voice-free
name: discord-voice-free
version: "1.0.0"
displayName: Discord语音免费
summary: Discord语音助手免费版,提供基础加入/离开/状态查询与本地Whisper转写
license: MIT
description: |-
  Discord 语音对话助手(免费版),提供基础的语音频道加入、离开、状态查询与本地
  Whisper 离线转写能力。覆盖 VAD 语音检测、静默触发 STT、TTS 播放的最小闭环。

  核心能力:
  - 频道加入/离开:斜杠命令与 CLI 两种入口
  - VAD 语音检测:medium 灵敏度默认值,自动识别说话开始与结束
  - 本地 Whisper STT:离线转写,无需外部 API Key
  - OpenAI TTS 播放:基础语音合成与频道播放
  - 状态查询:当前连接状态、频道 ID、连接时长

  不含 Deepgram 流式 STT、ElevenLabs 多语言 TTS、Barge-in 打断响应、
  自动重连、allowedUsers 用户白名单等高级功能。
  如需完整能力请升级付费版。
  适用于个人开发者快速搭建基础语音问答原型。
  不适用于低延迟直播字幕与企业级多用户场景。
tags:
  - Communication
  - 语音对话
tools:
  - read
  - exec
---

# Discord 语音助手 (免费版)

在 Discord 语音频道中提供基础的语音对话能力:VAD 检测 → 本地 Whisper 转写 → OpenAI TTS 播放。仅支持 `medium` 灵敏度与默认配置,适合个人开发者快速验证原型。

## 核心能力
### 1. 先验证系统依赖与 Bot 权限
```bash
# 必需系统依赖
ffmpeg -version          # 音频处理
node -e "require('@discordjs/opus')"  # Opus 编解码
```

Bot 必须具备三项权限:`Connect`(加入频道)、`Speak`(播放音频)、`Use Voice Activity`(检测语音活动)。在 Discord Developer Portal > OAuth2 > Permissions 中勾选。

**输入**: 用户提供先验证系统依赖与 Bot 权限所需的指令和必要参数。
**输出**: 返回先验证系统依赖与 Bot 权限的执行结果,包含操作状态和输出数据。
### 2. 仅支持本地 Whisper STT
免费版仅支持 `sttProvider: "local-whisper"`,无需外部 API Key。Deepgram 流式 STT 与 Whisper API 需升级付费版。本地模型首次加载需下载(数百 MB)。

**输入**: 用户提供仅支持本地 Whisper STT所需的指令和必要参数。
**处理**: 按照skill规范执行仅支持本地 Whisper STT操作,遵循单一意图原则。
**输出**: 返回仅支持本地 Whisper STT的执行结果,包含操作状态和输出数据。

- 执行`仅支持本地 Whisper STT`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`仅支持本地 Whisper STT`相关配置参数进行设置
### 3. 仅支持默认配置
免费版使用固定默认配置:`vadSensitivity: "medium"`、`silenceThresholdMs: 1500`、`maxRecordingMs: 30000`。不可调整 Barge-in 与 allowedUsers 等高级选项。

**处理**: 按照skill规范执行仅支持默认配置操作,遵循单一意图原则。
**输出**: 返回仅支持默认配置的执行结果,包含操作状态和输出数据。

- 执行`仅支持默认配置`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`仅支持默认配置`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 语音助手免费版、提供基础加入、状态查询与本地、语音对话助手、提供基础的语音频、道加入、离线转写能力、语音检测、静默触发、TTS、播放的最小闭环。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础语音问答 | 用户在语音频道提问 | 本地转写 + Agent 回复 + TTS 播放 |
| 语音状态查询 | 无参数 | 当前连接状态、频道 ID、连接时长 |

**不适用于**: 直播间实时字幕、无障碍对话辅助、多用户白名单场景(需升级付费版)。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 使用流程

1. 安装系统依赖:`ffmpeg`、`build-essential`、`python3`
2. 在 `agent-cli.json` 中启用 `discord-voice` 插件,使用默认 `local-whisper` 配置
3. 设置环境变量 `DISCORD_TOKEN` 与 `OPENAI_API_KEY`(用于 TTS)
4. 用斜杠命令 `/discord_voice join <channel>` 或 CLI `agent-cli discord_voice join <channelId>` 加入频道
5. 用户说话 → VAD 检测 → 本地 Whisper 转写 → Agent 处理 → TTS 播放
6. 退出时调用 `/discord_voice leave` 释放频道资源

### 命令参数说明

- `--guild`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 核心配置(免费版固定值)

| 选项 | 默认值 | 说明 |
|------|--------|------|
| `enabled` | `true` | 启用/禁用插件 |
| `sttProvider` | `"local-whisper"` | 仅支持本地 Whisper |
| `ttsProvider` | `"openai"` | 仅支持 OpenAI TTS |
| `ttsVoice` | `"nova"` | 固定语音 ID |
| `vadSensitivity` | `"medium"` | 固定 medium 灵敏度 |
| `silenceThresholdMs` | `1500` | 固定静默阈值 |
| `maxRecordingMs` | `30000` | 固定最大录音 30 秒 |

## 入口与命令

### 斜杠命令(Discord)

```text
/discord_voice join <channel>   # 加入语音频道
/discord_voice leave             # 离开当前语音频道
/discord_voice status            # 查看语音连接状态
```

### CLI 命令

```bash
agent-cli discord_voice join <channelId>
agent-cli discord_voice leave --guild <guildId>
agent-cli discord_voice status
```

## 案例展示

### 案例1: 基础语音问答原型

个人开发者快速验证语音问答能力,使用本地 Whisper 避免外部 API 费用。

```bash
# 1. 配置 local-whisper + openai TTS(免费版默认)
# agent-cli.json 片段:
# {
#   "discord-voice": {
#     "enabled": true,
#     "config": {
#       "sttProvider": "local-whisper",
#       "ttsProvider": "openai",
#       "ttsVoice": "nova"
#     }
#   }
# }

# 2. 加入语音频道
agent-cli discord_voice join 1234567890123456
# 输出: [discord-voice] Joined channel "General" (1234567890123456)

# 3. 用户说话 -> VAD 检测 -> 本地 Whisper 转写
# 日志: [discord-voice] VAD: speech started
# 日志: [discord-voice] VAD: speech ended (duration: 3.8s)
# 日志: [discord-voice] STT (local): "今天天气怎么样?"

# 4. Agent 处理 -> TTS 合成 -> 频道播放
# 日志: [discord-voice] TTS: synthesizing 64 chars
# 日志: [discord-voice] Playing audio (2.7s)

# 5. 查看状态
agent-cli discord_voice status
# 输出: Connected to "General" | Uptime: 5m
```

输出: 基础语音问答循环,延迟约 3-5 秒(本地 Whisper 转写较慢)。适合原型验证,生产场景建议升级付费版使用 Deepgram 流式 STT。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `Discord client not available` | Discord 频道未配置或 Bot 未连接 | 检查 `DISCORD_TOKEN` 与频道配置,重启 gateway |
| Opus build errors | 缺少原生编译工具 | `npm install -g node-gyp` 后 `npm rebuild @discordjs/opus` |
| No audio heard | Bot 缺少 Speak 权限或被服务器静音 | 在 Developer Portal 勾选 Speak;检查服务器是否 mute 了 Bot |
| Local model download failed | 本地 Whisper 模型下载失败 | 执行ping命令测试网络连通性,检查防火墙和代理设置,手动下载模型至 `~/.agent-cli/models/` 目录 |
| `OPENAI_API_KEY missing` | 未设置 TTS 所需 API Key | 设置 `OPENAI_API_KEY` 环境变量后重启服务 |

## 常见问题

### Q1: 免费版与付费版有何区别?
A: 免费版仅支持本地 Whisper STT 与 OpenAI TTS,固定 medium 灵敏度,无 Barge-in 打断响应与自动重连。付费版增加 Deepgram 流式 STT(延迟降 1 秒)、ElevenLabs/Kokoro 多引擎 TTS、可调 VAD 灵敏度、自动重连、用户白名单等高级能力。

### Q2: 为什么本地 Whisper 转写延迟较高?
A: 本地模型在 CPU 上推理较慢,通常需 2-3 秒处理一段 4 秒音频。GPU 加速可显著降低延迟,但需额外配置。若需低延迟(<1 秒),建议升级付费版使用 Deepgram 流式 STT。

### Q3: 免费版能调整 VAD 灵敏度吗?
A: 不能。免费版固定使用 `medium` 灵敏度,适合大多数安静到中等噪声环境。若需 `low`(拾取轻声)或 `high`(嘈杂环境),请升级付费版。

### Q4: 单次录音最长能录多久?
A: 免费版固定为 30 秒(`maxRecordingMs: 30000`)。超过 30 秒的语音会被截断。若需更长录音,请升级付费版调整 `maxRecordingMs`。

## 已知限制

- 仅支持本地 Whisper STT,延迟约 2-3 秒,不适合实时字幕场景
- 仅支持 OpenAI TTS,无法使用 ElevenLabs 多语言或 Kokoro 本地离线
- VAD 灵敏度固定为 medium,无法调整
- 不支持 Barge-in 打断响应,Bot 会完整播完 TTS
- 不支持自动重连,断线后需手动重新 join
- 不支持 allowedUsers 用户白名单,所有用户均可触发
- 每个公会同一时间仅支持 1 个语音频道
- 依赖 ffmpeg、@discordjs/opus 与有效 `DISCORD_TOKEN`

## 升级提示

> 本免费版提供基础语音问答原型能力。如需 Deepgram 流式 STT(延迟降 1 秒)、
> ElevenLabs/Kokoro 多引擎 TTS、可调 VAD 灵敏度、Barge-in 打断响应、
> 自动重连(指数退避)、用户白名单、完整配置项与 3 个进阶案例等高级能力,
> 请升级至 **Discord 语音助手付费版**。
