---
slug: discord-voice-paid
name: discord-voice-paid
version: "1.0.0"
displayName: Discord语音工具专业版
summary: 企业级 Discord 语音 AI 对话,支持多服务商、流式转写、自动重连与批量频道管理。
license: Proprietary
edition: pro
description: |-
  面向企业与社区运营团队的 Discord 语音 AI 全功能对话工具。核心能力:
  - 多 STT/TTS 服务商切换(OpenAI/Deepgram/ElevenLabs/本地)
  - Deepgram 流式实时转写(延迟降低约 1 秒)
  - 自动心跳监控与断线重连(指数退避)
  - 智能打断(barge-in)、自动加入与多频道调度
  - 企业级权限白名单与审计日志

  适用场景:
  - 企业语音会议室的 AI 实时助理
  - 大型语音社区的多频道 AI 互动
  - 高并发低延迟的实时语音问答

  差异化: Pro 版在免...
tags:
- Discord
- 语音对话
- Communication
- 流式转写
- 企业级
tools:
  - - read
- exec
---
# Discord语音工具专业版

## 核心能力

| 能力模块 | 说明 | 免费版 | Pro 版 |
|:-------|:-----|:------:|:------:|
| 加入/离开频道 | 语音频道进出 | 支持 | 支持+自动加入 |
| 语音活动检测 | 自动检测说话 | 支持 | 支持(可调) |
| 语音转文字 | STT 服务商 | 本地 Whisper | 多服务商(OpenAI/Deepgram/本地) |
| 流式转写 | 实时低延迟 | 不支持 | 支持(Deepgram) |
| 文字转语音 | TTS 服务商 | 本地 Kokoro | 多服务商(OpenAI/ElevenLabs/本地) |
| 打断支持 | barge-in | 支持 | 支持(可调) |
| 自动重连 | 断线恢复 | 不支持 | 支持(指数退避) |
| 心跳监控 | 连接健康检查 | 基础 | 支持(可配置) |
| 多频道调度 | 多实例管理 | 不支持 | 支持 |
| 权限白名单 | 用户限制 | 支持 | 支持+审计 |
| 审计日志 | 操作记录 | 不支持 | 支持 |

## 适用场景

### 场景一:企业语音会议室 AI 助理

企业使用 Discord 语音频道作为远程会议室,需要 AI 助理实时记录会议要点并语音回答提问。

```json5
{
  sttProvider: "deepgram",
  streamingSTT: true,  // 流式转写,延迟更低
  ttsProvider: "elevenlabs",
  ttsVoice: "21m00Tcm4TlvDq8ikWAM",  // Rachel,自然女声
  vadSensitivity: "medium",
  bargeIn: true,
  autoJoinChannel: "1234567890",  // 启动自动加入
  heartbeatIntervalMs: 30000,
  allowedUsers: ["user1", "user2"],  // 仅限团队成员
  deepgram: {
    apiKey: process.env.DEEPGRAM_API_KEY,
    model: "nova-2"
  },
  elevenlabs: {
    apiKey: process.env.ELEVENLABS_API_KEY,
    voiceId: "21m00Tcm4TlvDq8ikWAM",
    modelId: "eleven_multilingual_v2"
  }
}
```

配置后机器人启动即自动加入指定频道,流式转写确保提问后约 1 秒内开始响应。

### 场景二:大型语音社区多频道互动

大型社区有多个语音频道(技术讨论、闲聊、答疑),需要 AI 在不同频道间轮换或并行服务。

```bash
# 实例 A 服务技术讨论频道
discord_voice join 1111111 --profile=tech-profile

# 实例 B 服务答疑频道
discord_voice join 2222222 --profile=support-profile
```

不同频道使用不同服务商配置(如技术频道用 Deepgram 追求低延迟,答疑频道用本地 Whisper 控制成本)。

### 常见问题

### Q1: 流式 STT 比批量快多少?

使用 Deepgram 流式模式,端到端延迟降低约 1 秒。原因是流式模式在用户说话过程中就开始传输和识别,而非等静音后整段发送。此外还提供实时中间结果反馈。流式失败会自动回退批量模式,无需人工干预。

### Q2: 自动重连会重试几次?

Pro 版自动重连采用指数退避策略,最多重试 3 次。第 1 次立即重试,第 2 次延迟增加,第 3 次延迟更长。3 次仍失败则放弃并记录错误日志,需人工介入。心跳检查间隔通过 `heartbeatIntervalMs` 配置(默认 30 秒)。

### Q3: 多服务商能否运行时切换?

支持。可通过 Agent 工具或配置热更新切换 `sttProvider` 和 `ttsProvider`。切换后下一段对话即生效。建议非高峰时段切换,避免切换瞬间影响正在进行的对话。

### Q4: ElevenLabs 和 OpenAI TTS 怎么选?

ElevenLabs 语音自然度更高,支持语音克隆和多语言,适合对音质要求高的场景,但成本较高;OpenAI TTS 性价比高,延迟较低,适合高频对话场景。两者可按频道配置不同服务商。

### Q5: 自动加入(autoJoinChannel)有何风险?

自动加入会在 Agent 启动时立即连接指定频道。风险:若频道当时有私密会议,机器人突然加入可能打扰用户。建议:仅在专属 AI 频道启用自动加入;或加入后静默等待被 @提及再说话;配置 `allowedUsers` 限制触发用户。

### Q6: 多频道并行如何部署?

Discord 限制单机器人在单服务器同时只能在一个语音频道。多频道并行需部署多个机器人实例(不同 Token),每个实例服务一个频道。不同实例可配置不同服务商和语音,实现差异化服务。

### Q7: 审计日志记录哪些内容?

Pro 版审计日志记录:会话开始/结束时间、频道 ID、参与者列表、STT/TTS 服务商、识别/合成耗时、错误事件(含错误类型和堆栈)、重连事件。日志建议加密存储,保留 30-90 天,用于运营分析和问题追溯。

### Q8: Pro 版如何与免费版共存?

两者配置兼容,可共存。Pro 版包含免费版的本地方案能力,额外支持多服务商和流式转写。建议生产环境统一使用 Pro 版,免费版仅用于本地开发测试。两者可共用同一机器人令牌。

## 使用流程

### 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux(推荐 Linux 用于生产环境)
- **系统依赖**: `ffmpeg`、构建工具(`build-essential` / Xcode CLT)、Python 3
- **硬件**: 云方案对本地硬件要求低;本地方案建议 8GB 以上内存
- **网络**: 需稳定访问 Discord API 及所选 STT/TTS 服务商 API

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| Discord Bot Token | 凭证 | 必需 | Discord Developer Portal 创建机器人获取 |
| ffmpeg | 系统依赖 | 必需 | 系统包管理器安装 |
| OpenAI API | API | 可选 | OpenAI 平台申请 API Key |
| Deepgram API | API | 可选 | Deepgram 平台申请 API Key |
| ElevenLabs API | API | 可选 | ElevenLabs 平台申请 API Key |
| Node.js 原生模块 | 库 | 必需 | npm install 编译 |

### API Key 配置

- **Discord Bot Token**: 通过环境变量 `DISCORD_TOKEN` 配置(必需)。
- **OpenAI API Key**: 通过环境变量 `OPENAI_API_KEY` 配置(使用 OpenAI Whisper/TTS 时必需)。
- **Deepgram API Key**: 通过环境变量 `DEEPGRAM_API_KEY` 配置(使用 Deepgram STT 时必需,流式模式依赖此项)。
- **ElevenLabs API Key**: 通过环境变量 `ELEVENLABS_API_KEY` 配置(使用 ElevenLabs TTS 时必需)。
- **密钥安全**: 所有 API Key 必须通过环境变量注入,切勿硬编码。建议使用密钥管理服务,定期轮换。审计日志不记录完整 Key。
- **本地方案**: 使用本地 Whisper/Kokoro 时无需任何 API Key,与免费版一致。

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 执行能力)
- **说明**: 以自然语言指令驱动 Agent 调用语音工具,多服务商处理音频,支持流式与自动重连
- **适用规模**: 企业级、多频道、高并发实时语音场景
- **兼容性**: 与 `discord-voice-tool-free` 配置兼容,可平滑升级
- **支持级别**: 优先支持(Pro 版享有问题优先响应与功能迭代建议通道)

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| `references/checklist.md` | 文件 | 是 | 相关说明 |
| `references/scoring.md` | 文件 | 否 | 相关说明 |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## 案例展示

### 服务商配置

#### OpenAI(Whisper + TTS)

```json5
{
  openai: {
    apiKey: process.env.OPENAI_API_KEY,
    whisperModel: "whisper-1",
    ttsModel: "tts-1"
  }
}
```

#### Deepgram(STT,支持流式)

```json5
{
  deepgram: {
    apiKey: process.env.DEEPGRAM_API_KEY,
    model: "nova-2"
  }
}
```

#### ElevenLabs(TTS)

```json5
{
  elevenlabs: {
    apiKey: process.env.ELEVENLABS_API_KEY,
    voiceId: "21m00Tcm4TlvDq8ikWAM",  // Rachel
    modelId: "eleven_multilingual_v2"
  }
}
```

### 流式 STT 配置

```json5
{
  sttProvider: "deepgram",
  streamingSTT: true,  // 默认开启
  deepgram: {
    apiKey: process.env.DEEPGRAM_API_KEY,
    model: "nova-2"
  }
}
```

流式模式提供:

- 端到端延迟降低约 1 秒
- 实时中间转录结果反馈
- 自动 keep-alive 防止连接超时
- 流式失败时自动回退批量转录

### 自动重连配置

```json5
{
  heartbeatIntervalMs: 30000,  // 心跳间隔(可调)
  // 内置: 断线后指数退避重连,最多 3 次
}
```

断线时日志:

```text
[discord-voice] Disconnected from voice channel
[discord-voice] Reconnection attempt 1/3
[discord-voice] Reconnected successfully
```

### 自动加入配置

```json5
{
  autoJoinChannel: "1234567890"  // 启动时自动加入此频道
}
```

### 环境变量

| 变量 | 说明 |
|:-----|:-----|
| `DISCORD_TOKEN` | Discord 机器人令牌(必需) |
| `OPENAI_API_KEY` | OpenAI API Key(Whisper + TTS) |
| `ELEVENLABS_API_KEY` | ElevenLabs API Key(TTS) |
| `DEEPGRAM_API_KEY` | Deepgram API Key(STT) |

## 常见问题

### Q: 如何使用此Skill?
A: 请参考使用流程章节

### Q: 如何使用此Skill?
A: 请参考使用流程章节

### Q: 如何使用此Skill?
A: 请参考使用流程章节

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
