---
slug: "discord-voice"
name: "discord-voice"
version: 0.1.7
displayName: "Discord语音助手"
summary: "Discord语音对话助手,覆盖STT/TTS/VAD/打断/自动重连与流式转录全流程"
license: "Proprietary"
description: |-
  Discord 语音对话专业版 —— 在 Discord 语音频道中实现实时双向语音对话的端到端助手.
  覆盖语音活动检测(VAD)、语音转文字(STT)、文字转语音(TTS)、打断响应(Barge-in)、
  自动重连与流式转录等核心能力.
  核心能力:
  - 多 STT 引擎:OpenAI Whisper API、Deepgram 流式转录、本地 Whisper 离线模式
  - 多 TTS 引擎:OpenAI TTS、ElevenLabs 多语言、Kokoro 本地离线
  - 语音活动检测(VAD):低/中/高三档灵敏度,自动识别说话开始与结束
  - 打断响应(Barge-in):用户开口立即停止 TTS 播放,实现自然对话节奏
  - 自动重连:30 秒心跳检查,断线后指数退避重试(最多 3 次)
  - 流式 STT:Deepgram WebSocket 实时转录,端到端延迟降低约 1 秒
  - 多入口控制:斜杠命令、CLI、Agent Tool 三种调用方式

  适用场景:
  - 社区语音助手:在公会语音频道中提供 AI 问答与陪伴对话
  - 直播间互动:实时转写主播发言并合成 TTS 回复
  - 无障碍辅助:为听障用户将语音转为文字并将文字回复合成语音

  不适用于:多频道并发语音(每公会仅支持 1 个语音频道)、长时间录音(大于30 秒)与无网络环境.
tags:
  - Communication
  - 语音对话
  - AI助手
  - 实时转录
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "write", "exec"]
tags: "Discord,社交,通信"
category: "Communication"
---
# Discord 语音助手

在 Discord 语音频道中实现端到端语音对话:VAD 检测说话 → 录音缓冲 → STT 转写 → Agent 处理 → TTS 合成 → 频道播放。支持打断响应与自动重连,提供斜杠命令、CLI、Agent Tool 三种入口.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Discord语音助手处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 核心能力
### 1. 先验证系统依赖与 Bot 权限
```bash
# 必需系统依赖
ffmpeg -version          # 音频处理
node -e "require('@discordjs/opus')"  # Opus 编解码
node -e "require('sodium-native')"    # 加密
```

Bot 必须具备三项权限:`Connect`(加入频道)、`Speak`(播放音频)、`Use Voice Activity`(检测语音活动)。在 Discord Developer Portal > OAuth2 > Permissions 中勾选.
**输入**: 用户提供先验证系统依赖与 Bot 权限所需的指令和必要参数.
**输出**: 返回先验证系统依赖与 Bot 权限的处理结果,包含执行状态码、结果数据和执行日志.
### 2. STT/TTS 引擎必须配置 API Key
| 引擎 | 类型 | 必需环境变量 |
|---:|---:|---:|
| Whisper API | STT | `OPENAI_API_KEY` |
| Deepgram | STT | `DEEPGRAM_API_KEY` |
| Local Whisper | STT | 无需 API Key,需本地模型 |
| OpenAI TTS | TTS | `OPENAI_API_KEY` |
| ElevenLabs | TTS | `ELEVENLABS_API_KEY` |
| Kokoro | TTS | 无需 API Key,需本地模型 |

未配置 Key 的引擎会在调用时返回 `provider_api_key_missing`.
**输入**: 用户提供STT/TTS 引擎必须配置 API Key所需的指令和必要参数.
### 3. 单公会单频道约束

每个公会同一时间仅允许 Bot 加入 1 个语音频道。重复调用 `join` 会返回 `already_in_voice_channel`,需先 `leave` 再切换。- 验证返回数据的完整性和格式正确性
#
## 适用场景

| 场景 | 输入 | 输出 |
|:---:|:---:|:---:|
| 社区语音问答 | 用户在语音频道提问 | STT 转写 + Agent 回复 + TTS 合成播放 |
| 直播间实时字幕 | 主播语音流 | 流式转写文本(延迟约 1 秒) |
| 无障碍对话辅助 | 听障用户文字输入 | TTS 合成语音在频道播放 |
| 语音状态监控 | 无参数 | 当前连接状态、频道 ID、重连次数 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill基于Agent平台内置LLM,通常无需额外API Key配置

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 使用流程

1. 安装系统依赖:`ffmpeg`、`build-essential`、`python3`
2. 在 `agent-cli.json` 中配置 `discord-voice` 插件与 STT/TTS 引擎
3. 设置环境变量 `DISCORD_TOKEN` 与所选引擎的 API Key
4. 用斜杠命令 `/discord_voice join <channel>` 或 CLI `agent-cli discord_voice join <channelId>` 加入频道
5. 监听 VAD 事件 → 录音缓冲 → 静默触发 STT → Agent 处理 → TTS 播放
6. 退出时调用 `/discord_voice leave` 释放频道资源

#
## 核心配置

| 选项 | 类型 | 默认值 | 说明 |
|---:|:---|---:|---:|
| `enabled` | boolean | `true` | 启用/禁用插件 |
| `sttProvider` | string | `"local-whisper"` | `"whisper"` / `"deepgram"` / `"local-whisper"` |
| `streamingSTT` | boolean | `true` | 流式 STT(仅 Deepgram,延迟降低约 1 秒) |
| `ttsProvider` | string | `"openai"` | `"openai"` / `"elevenlabs"` / `"kokoro"` |
| `ttsVoice` | string | `"nova"` | TTS 语音 ID |
| `vadSensitivity` | string | `"medium"` | `"low"` / `"medium"` / `"high"` |
| `bargeIn` | boolean | `true` | 用户开口立即停止 TTS |
| `allowedUsers` | string[] | `[]` | 允许的用户 ID(空 = 全部) |
| `silenceThresholdMs` | number | `1500` | 静默多久后触发处理(毫秒) |
| `maxRecordingMs` | number | `30000` | 单次录音最大长度(毫秒) |
| `heartbeatIntervalMs` | number | `30000` | 心跳检查间隔(毫秒) |
| `autoJoinChannel` | string | `undefined` | 启动时自动加入的频道 ID |

## 工作原理

```text
1. Join        Bot 加入指定语音频道
2. Listen      VAD 检测用户说话开始/结束
3. Record      音频缓冲(最长 30 秒)
4. Transcribe  静默触发,音频送 STT 引擎
5. Process     转写文本路由至 Clawdbot Agent
6. Synthesize  Agent 回复经 TTS 合成音频
7. Play        音频在频道播放(支持打断响应)
```

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

### Agent Tool

```text
discord_voice join 1234567890
discord_voice leave
discord_voice speak "你好,欢迎加入频道"
discord_voice status
```

支持动作:`join`(需 channelId)、`leave`、`speak`(需文本)、`status`.
## 案例展示

### 案例1: 社区语音问答助手

公会成员在语音频道提问,Bot 自动转写并通过 Agent 回答,适合技术社区答疑场景.
```bash
# 1. 配置 local-whisper + openai TTS(无需外部 STT Key)
# agent-cli.json 片段:
# {
#   "discord-voice": {
#     "enabled": true,
#     "config": {
#       "sttProvider": "local-whisper",
#       "ttsProvider": "openai",
#       "ttsVoice": "nova",
#       "vadSensitivity": "medium",
#       "silenceThresholdMs": 1500,
#       "bargeIn": true
#     }
#   }
# }
# ...
# 2. 加入语音频道
agent-cli discord_voice join 1234567890123456
# 输出: [discord-voice] Joined channel "General" (1234567890123456)
# ...
# 3. 用户说话 -> VAD 检测 -> STT 转写
# 日志: [discord-voice] VAD: speech started
# 日志: [discord-voice] VAD: speech ended (duration: 4.2s)
# 日志: [discord-voice] STT: "如何用 Python 读取 CSV 文件?"
# ...
# 4. Agent 处理 -> TTS 合成 -> 频道播放
# 日志: [discord-voice] TTS: synthesizing 87 chars
# 日志: [discord-voice] Playing audio (3.1s)
# ...
# 5. 查看状态
agent-cli discord_voice status
# 输出: Connected to "General" | Latency: 89ms | Uptime: 12m
```

输出: 完整的语音问答循环,延迟约 2-3 秒(含 STT + Agent + TTS).
### 案例2: 直播间实时字幕(Deepgram 流式 STT)

主播语音需要实时转为字幕显示在直播间,要求延迟 < 2 秒.
```bash
# 1. 配置 Deepgram 流式 STT(端到端延迟降低约 1 秒)
# agent-cli.json 片段:
# {
#   "discord-voice": {
#     "config": {
#       "sttProvider": "deepgram",
#       "streamingSTT": true,
#       "deepgram": { "apiKey": "...", "model": "nova-2" }
#     }
#   }
# }
# ...
# 2. 加入频道并启用流式转录
agent-cli discord_voice join 1234567890123456
# 日志: [discord-voice] Streaming STT enabled (Deepgram nova-2)
# 日志: [discord-voice] Interim: "欢迎来到"
# 日志: [discord-voice] Interim: "欢迎来到今天的"
# 日志: [discord-voice] Final:  "欢迎来到今天的直播"
# ...
# 3. 流式失败时自动降级为批量转录
# 日志: [discord-voice] Streaming STT failed, fallback to batch
```

输出: 实时字幕流,延迟约 1-2 秒;流式失败自动降级为批量转录保证可用性.
### 案例3: 无障碍对话辅助

听障用户通过文字输入,Bot 合成语音在频道播放,实现双向交流.
```text
# 用户通过 Agent Tool 输入文本
discord_voice speak "大家好,我是新成员,请多关照"
# ...
# Bot 合成并播放
# 日志: [discord-voice] TTS: synthesizing 18 chars
# 日志: [discord-voice] Playing audio (2.4s)
# ...
# 其他成员语音回复时,Bot 转写为文字显示给听障用户
# 日志: [discord-voice] STT: "欢迎加入!有问题随时问"
```

输出: 文字 → 语音 → 频道播放,反向语音 → 文字 → 用户终端显示.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| `Discord client not available` | Discord 频道未配置或 Bot 未连接 | 检查 `DISCORD_TOKEN` 与频道配置,重启 gateway |
| Opus/Sodium build errors | 缺少原生编译工具 | `npm install -g node-gyp` 后 `npm rebuild @discordjs/opus sodium-native` |
| No audio heard | Bot 缺少 Speak 权限或被服务器静音 | 在 Developer Portal 勾选 Speak;检查服务器是否 mute 了 Bot |
| Transcription not working | STT API Key 无效或音频未录制 | 验证 API Key,开启 debug 日志确认音频缓冲 |
| `provider_api_key_missing` | 未设置引擎对应的环境变量 | 按引擎表设置 `OPENAI_API_KEY` / `DEEPGRAM_API_KEY` / `ELEVENLABS_API_KEY` |
| `already_in_voice_channel` | 同公会重复调用 join | 先调用 `leave` 释放当前频道,再 `join` 新频道 |
| `Recording exceeded max length` | 单次录音超过 30 秒 | 调高 `maxRecordingMs`,或拆分长语音为多段 |
| `Reconnection failed after 3 attempts` | 网络不稳定或频道被删除 | ,确认频道存在后手动重新 join |

## 常见问题

### Q1: 如何降低端到端延迟?
A: 三个杠杆:(1) STT 改用 Deepgram 流式模式(`streamingSTT: true`),延迟降低约 1 秒;(2) TTS 选用 OpenAI `tts-1` 而非 `tts-1-hd`,合成更快;(3) 调低 `silenceThresholdMs`(如 800ms)加快触发,但可能误判短停顿.
### Q2: VAD 灵敏度如何选择?
A: `low` 适合安静环境,可拾取轻声说话但易被背景噪声触发;`medium` 为默认平衡值,推荐大多数场景;`high` 适合嘈杂环境,需更大声清晰说话。若频繁误触发,先尝试 `medium` 再升 `high`.
### Q3: Barge-in(打断响应)如何工作?
A: 启用后(`bargeIn: true`,默认),Bot 播放 TTS 时若检测到用户开口,立即停止播放并开始录音。这模拟了人类对话中的插话行为。若需让 Bot 完整播完,设置 `bargeIn: false`.
### Q4: 自动重连的退避策略是什么?
A: 心跳检查每 30 秒(可配置 `heartbeatIntervalMs`)执行一次。断线后按指数退避重试:第 1 次 1 秒、第 2 次 2 秒、第 3 次 4 秒。3 次失败后放弃,需手动 `join`。日志会输出 `Reconnection attempt 1/3` 等进度.
### Q5: 流式 STT 失败时如何降级?
A: Deepgram 流式连接失败时,自动降级为批量转录模式(完整录音后一次性送 STT)。日志会显示 `Streaming STT failed, fallback to batch`。降级后延迟增加约 1 秒,但保证对话不中断.
### Q6: 如何限制只有特定用户能触发对话?
A: 在 `agent-cli.json` 中配置 `allowedUsers: ["user_id_1", "user_id_2"]`。空数组表示允许所有用户。用户 ID 可在 Discord 开发者模式右键用户复制.
## 已知限制

- 每个公会同一时间仅支持 1 个语音频道,无法多频道并发
- 单次录音最大长度 30 秒(可配置 `maxRecordingMs` 上限受 Discord 限制)
- 实时音频需稳定网络,弱网环境可能丢字或重连失败
- TTS 合成存在约 0.5-1 秒延迟,长文本合成更慢
- 本地 Whisper 与 Kokoro 模型首次加载需下载(数百 MB),建议预下载
- 不支持多人同时说话场景,VAD 会因混音导致转写质量下降
- 不支持语音消息存档与回放,仅实时对话

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Discord语音助手处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "discord-voice"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
