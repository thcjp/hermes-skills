---
slug: "dlazy-audio"
name: "dlazy-audio"
version: "1.0.0"
displayName: "音频生成工具-专业版"
summary: "全功能音频生成引擎，支持TTS、语音克隆、音乐生成、多角色对话与管道链接批量处理。"
license: "Proprietary"
edition: "pro"
description: |-
  音频生成工具专业版，面向专业内容团队的全功能音频生成平台。核心能力：
  - 15+ 音频模型全覆盖（TTS、语音克隆、音乐生成、音效、对话）
  - 多角色对话一次性渲染（最多10个角色）
  - 语音克隆（ElevenLabs IVC、Qwen、Kling、Vidu）
  - 原创音乐生成（Suno V5
tags:
  - Creative
  - Audio
  - Enterprise
  - VoiceClone
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 音频生成工具-专业版

## 核心能力

### 模型覆盖对比

| 模型类别 | 免费版 | 专业版 | 代表模型 |
|:---------|:-------|:-------|:---------|
| 基础TTS | 3个 | 5个 | doubao-tts, keling-tts, gemini-2.5-tts, elevenlabs-tts, qwen-tts |
| 语音克隆 | 不支持 | 4个 | elevenlabs-voice-clone, qwen-audio-clone, kling-audio-clone, vidu-audio-clone |
| 音乐生成 | 不支持 | 2个 | suno-music, elevenlabs-music |
| 音效生成 | 1个 | 2个 | keling-sfx, elevenlabs-sfx |
| 多角色对话 | 不支持 | 1个 | elevenlabs-dialogue |
| 声音搜索 | 不支持 | 1个 | elevenlabs-search |
| 管道链接 | 不支持 | 支持 | 多步骤串联 |- 验证执行结果，确认输出符合预期格式
- 参考`核心能力`相关配置参数进行设置
### 核心能力
```text
语音克隆:
  - ElevenLabs IVC（即时语音克隆）
  - Qwen3-TTS 语音克隆（阿里百炼）
  - Kling 自定义音色克隆
  - Vidu 真人声音克隆

音乐生成:
  - Suno V5.5（灵感模式/自定义模式）
  - ElevenLabs Music（10-300秒原创音乐）

多角色对话:
  - ElevenLabs Dialogue（最多10角色）
  - 支持音频标签: [giggling] [whispers] 等
  - 一键渲染整段对话

音效生成:
  - ElevenLabs SFX（1-22秒音效）
  - Keling SFX（文本转音效 + 视频匹配）

声音库搜索:
  - ElevenLabs Search（关键词/来源/分类）
  - 返回可试听的预览音频

管道链接:
  - 步骤间自动传递输出
  - 支持管道引用: -, @N, @N.path, @*, @stdin
```

**输入**: 用户提供核心能力所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `核心能力` 选项
- 处理流程: 接收输入 -> 执行核心能力 -> 返回结果
- 输入: 用户提供核心能力所需的参数和指令
- 输出: 返回核心能力的执行结果,包含操作状态和输出数据

### 模型类别

执行模型类别操作,处理用户输入并返回结果。

**输入**: 用户提供模型类别所需的参数和指令。

**输出**: 返回模型类别的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`模型类别`相关配置参数进行设置
#
## 适用场景

### 场景一：播客全流程制作

从文案到成品音频的完整播客制作工作流。

```bash
# 第1步: 克隆主持人声音（一次性操作）
dlazy elevenlabs-voice-clone \
  --audio-file "./samples/host-voice-sample.wav" \
  --name "host-voice"

# 第2步: 使用克隆声音生成主持人台词
dlazy elevenlabs-tts \
  --text "欢迎收听本期播客，今天我们聊聊AI音频技术的最新进展。" \
  --voice "host-voice" \
  --stability 0.7 \
  --similarity 0.8

# 第3步: 生成背景音乐
dlazy suno-music \
  --mode "custom" \
  --style "lo-fi chill ambient" \
  --title "Podcast Intro" \
  --instrumental true \
  --duration 30

# 第4步: 生成过渡音效
dlazy elevenlabs-sfx \
  --prompt "soft whoosh transition sound, gentle fade" \
  --duration 3
```

### 场景二：多角色广播剧

一次性渲染多角色对话场景。

```bash
# 多角色对话生成
dlazy elevenlabs-dialogue \
  --dialogue '[
    {"voice": "storyteller", "text": "夜深了，城市的灯火渐渐熄灭。"},
    {"voice": "detective", "text": "这案子不简单，[pauses] 凶手一定还在现场。"},
    {"voice": "assistant", "text": "[whispers] 长官，窗外好像有人影！"},
    {"voice": "detective", "text": "[urgently] 快，跟上去！"}
  ]' \
  --output "scene-01.wav"
```

### 场景三：管道链接自动化工作流

将多个生成步骤串联为自动化流水线。

```bash
# 示例
dlazy seedream-4.5 --prompt "lighthouse at dawn" \
  | dlazy keling-tts --text "Welcome to the coast." --image @0.url

# 管道链接示例2: 批量生成多张图片 → 超分辨率
dlazy seedream-4.5 --prompt "city skyline" --n 4 \
  | dlazy superres --images @*

# 管道链接示例3: 搜索声音 → 用选中声音生成TTS
dlazy elevenlabs-search \
  --keyword "warm female narrator" \
  --category "audiobook" \
  | dlazy elevenlabs-tts --text "优秀章 初次相遇" --voice @0.voice_id
```

### 管道引用速查

| 引用 | 解析为 |
|:-----|:-------|
| `-` | 上游输出的自然值 |
| `@N` | 第N个输出的主值（@0 = 优秀个输出URL） |
| `@N.path` | 深入第N个输出（@0.url, @1.meta.fps） |
| `@*` | 所有输出的主值数组 |
| `@stdin` | 完整上游JSON信封 |
| `@stdin:path` | JSON路径深入（@stdin:result.outputs[0].url） |

## 使用流程

### 依赖说明

### 运行环境
1. **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
2. **操作系统**: Windows / macOS / Linux
3. **Node.js**: 16+（dlazy CLI 运行需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js 16+ | 运行时 | 必需 | nodejs.org 官方下载 |
| @dlazy/cli | CLI工具 | 必需 | `npm install -g @dlazy/cli@latest` |
| dlazy API Key | 认证 | 必需 | dlazy.com/dashboard 获取 |
| FFmpeg（可选） | 工具 | 推荐 | 用于音频拼接与格式转换 |

### API Key 配置
4. **必需**: dlazy API Key（与免费版共用）
5. **获取方式**: 访问 dlazy.com/dashboard/organization/api-key
6. **配置方式**: `dlazy auth set YOUR_API_KEY` 或环境变量 `DLAZY_API_KEY`
7. **安全说明**: 配置文件权限限制为当前用户；Key 可随时轮换或撤销
8. **余额说明**: 专业版模型消耗较高，建议定期检查余额

### 可用性分类
9. **分类**: MD+EXEC+API（Markdown指令 + 命令行 + 外部API调用）
10. **说明**: 企业级AI Skill，支持全模型音频生成、管道链接与批量处理
11. **适用规模**: 专业内容团队，批量音频生产
12. **兼容性**: 与免费版完全兼容，API Key 和配置无缝共用

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q: 语音克隆需要什么样的声音样本？

A: 需要 30 秒以上的干净语音样本，无背景音乐和噪音。WAV 格式效果优秀。样本越清晰，克隆质量越高。

### Q: 管道链接中 stdin 为空怎么办？

A: 上游命令未输出 JSON 信封时，CLI 会返回 `code: "no_stdin"` 错误。检查上游命令是否执行成功。

### Q: 多角色对话的角色数上限是多少？

A: ElevenLabs Dialogue 单次最多支持 10 个不同角色。超过 10 个角色请分多次渲染后拼接。

### Q: Suno 音乐生成支持多长？

A: ElevenLabs Music 支持 10-300 秒原创音乐。Suno V5.5 支持完整歌曲结构（主歌+副歌+桥段）。

### Q: 如何从免费版升级？

A: API Key 和 CLI 配置无需变更，直接使用专业版的全部模型即可。免费版的 TTS 功能在专业版中完全保留。

### Q: 生成的音频 URL 有效期多久？

A: dlazy 文件服务托管的 URL 有一定有效期。建议生成后通过 `--output` 参数下载到本地保存。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

