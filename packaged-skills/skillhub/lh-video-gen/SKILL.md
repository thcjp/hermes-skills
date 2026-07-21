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

## 核心能力

- Generate vertical short videos (9:16) from a Markdown script
- Parses
  script sections, generates T
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Use、需要视频处理、音频编辑、媒体转换、配音生成时使用、不适用于版权受保、护的媒体内容处理。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

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

## 输入格式

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

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

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

## 常见问题

### Q1: 如何开始使用LH Video Gen？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: LH Video Gen有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
