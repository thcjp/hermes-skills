---
slug: lh-video-gen
name: lh-video-gen
version: "1.0.0"
displayName: LH Video Gen
summary: Generate vertical short videos (9:16) from a Markdown script. Parses script
  sections, generates T...
license: MIT
description: |-
  Generate vertical short videos (9:16) from a Markdown script。Parses
  script sections, generates T。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。
tags:
- Creative
tools:
  - - read
- exec
---

# LH Video Gen

从视频脚本 Markdown 文件一键生成竖版短视频（9:16）。

**核心思路：以图定音**

* 每段脚本的画面说明 -> 字幕卡片图
* 每段口播文案 -> TTS 配音
* 每张图展示时长 = 对应音频时长，音画天然同步

## 快速开始

```bash
python3 generate.py script.md -o output.mp4
```

### 使用预制图片（跳过 Chrome 截图）

```bash
python3 generate.py script.md --images-dir ./my-slides -o output.mp4
```

图片命名规则：`slide_01.png`, `slide_02.png`...，与脚本分段一一对应。

### 自定义 TTS 命令

```bash
python3 generate.py script.md --tts-command "my-tts {text} -o {output} -v {voice} -r {rate}"
```

占位符：`{text}` 口播文案、`{output}` 输出路径、`{voice}` 音色、`{rate}` 语速。

## 参数说明

```text
python3 generate.py <脚本路径> [选项]

选项：
  -o, --output        输出 MP4 路径（默认：tmp/video-output.mp4）
  -v, --voice         TTS 音色（默认：zh-CN-YunxiNeural）
  -r, --rate          语速（默认：+0%，如 +10%、-10%）
  -w, --width         视频宽度（默认：1080）
  --height            视频高度（默认：1920，9:16）
  --images-dir        使用已有图片目录，跳过 Chrome 截图
  --tts-command       自定义 TTS 命令模板（占位符：{text} {output} {voice} {rate}）
  --keep-temp         保留临时文件（图片、音频、片段）
  --no-subs           不烧录字幕
```

## 依赖

### 依赖说明

* **FFmpeg**：视频合成（`brew install ffmpeg`）
* **Chrome**：HTML 截图（仅在未使用 `--images-dir` 时需要）
  + 自动检测 macOS/Linux 常见路径，或通过 `CHROME_PATH` 环境变量指定

### 推荐搭配的 Skill

以下 Skill 非必需，但搭配使用效果更佳：

* **lh-edge-tts**：TTS 配音生成。自动检测同级目录 `../lh-edge-tts/scripts/tts_converter.py`，或通过 `EDGE_TTS_PATH` 环境变量指定，或用 `--tts-command` 替换为任意 TTS 工具
* **lh-html-to-image**：如需自定义更复杂的字幕卡片，可用此 Skill 生成图片后通过 `--images-dir` 传入

## 脚本格式

用 `---` 分隔各段，每段包含 `**口播**`、`**字幕**`、`**画面**` 字段：

```markdown

---

## 开场
**画面**：场景描述
**口播**：TTS 配音文案
**字幕**：屏幕显示文字\n支持换行

---

## 结尾
**画面**：场景描述
**口播**：TTS 配音文案
**字幕**：屏幕显示文字
```

完整模板：`templates/script-template.md`

## 工作流程

1. 解析脚本 Markdown，提取各分段
2. 每段口播 -> TTS 生成 mp3
3. 每段字幕 -> HTML 模板截图生成 9:16 图片（或从 `--images-dir` 加载）
4. 每张图 + 对应音频 -> FFmpeg 合成视频片段
5. 拼接所有片段 -> 输出 MP4

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

## 核心能力

- Generate vertical short videos (9:16) from a Markdown script
- Parses
  script sections, generates T
- 触发关键词: generate, short, vertical, video, gen, videos

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
```bash
python3 generate.py script.md -o output.mp4
```

### 使用预制图片（跳过 Chrome 截图）

```bash
python3 generate.py script.md --images-dir ./my-slides -o output.mp4
```

图片命名规则：`slide_01.png`, `slide_02.png`...，与脚本分段一一对应。

### 自定义 TTS 命令

```bash
python3 generate.py script.md --tts-command "my-tts {text} -o {output} -v {voice} -r {rate}"
```

占位符：`{text}` 口播文案、`{output}` 输出路径、`{voice}` 音色、`{rate}` 语速。
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用LH Video Gen？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: LH Video Gen有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
