---
slug: video-translator
name: video-translator
version: "1.0.5"
displayName: Video Translator
summary: Real time video translation / dubbing skill. Translate user-provided video
  (file or URL) and retu...
license: MIT-0
description: |-
  Real time video translation / dubbing skill。Translate user-provided
  video (file or URL) and retu。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Video Translator

在用户需要“视频翻译 / 视频配音 / 字幕翻译出片，并返回可预览链接”时使用此 skill。

## 检索关键词

* 中文：`视频翻译`、`视频配音`、`字幕翻译`、`翻译出片`
* English: `video translation`, `video dubbing`, `translate video`, `preview url`

## 固定服务地址

* Base URL 固定为：`https://audiox-api-global.luoji.cn`
* 不使用本地服务地址。

## 何时调用

* 用户给了视频文件，或给了可访问的视频 URL。
* 用户目标是拿到翻译后视频的 `preview_url`。

## 输入要求

* 必须二选一：
* `video`：二进制视频文件（multipart 字段名固定 `video`）
* `video_url`：可访问的 `http(s)` 视频链接
* `api_key`：请求头 `Authorization: Bearer <api_key>`
* 如果使用脚本，必须设置环境变量 `VIDEO_TRANSLATE_SERVICE_API_KEY`
* 可选：`targetLanguage` / `target_language`（目标语言，默认 `en`）
* 可选：`sourceLanguage` / `source_language`（源语言，不传时按目标语言推断）
* 可选：`show`（是否显示字幕，布尔值，默认 `false`）
* 可选：`bilingual`（是否双语字幕，布尔值，默认 `false`）

## 目标语言规则（必须遵守）

* 当前目标语言仅支持：中文、英文
* 若用户明确指定目标语言，必须提取并传 `targetLanguage` 代码：
  + 中文 -> `zh`
  + 英文 -> `en`
* 若用户未指定目标语言：默认 `targetLanguage=en`
* 若用户指定了不支持的目标语言：提示仅支持 `zh/en`

## 源语言规则（必须遵守）

* 源语言支持：`en`、`zh`、`ko`、`ja`、`fr`、`ru`、`es`、`de`
* 若用户明确指定源语言，必须提取并传 `sourceLanguage` 代码：
  + 中文 -> `zh`
  + 英文 -> `en`
  + 韩语 -> `ko`
  + 日语 -> `ja`
  + 法语 -> `fr`
  + 俄语 -> `ru`
  + 西班牙语 -> `es`
  + 德语 -> `de`
* 若用户未指定源语言：按目标语言默认推断
  + `targetLanguage=en` -> `sourceLanguage=zh`
  + `targetLanguage=zh` -> `sourceLanguage=en`
* 若用户指定了不支持的源语言：提示仅支持 `en/zh/ko/ja/fr/ru/es/de`

## 字幕参数规则

* 默认不显示字幕：`show=false`、`bilingual=false`
* 用户要求显示字幕、带字幕、烧字幕时：传 `show=true`
* 用户要求双语字幕时：传 `show=true` 且 `bilingual=true`
* 用户未提字幕需求时不要主动开启字幕

## 接口调用方式

1. 健康检查：`GET /video-trans/health`
2. 提交任务：`POST /video-trans/orchestrate`（带 `sourceLanguage`、`targetLanguage`、`show`、`bilingual`）
3. 从响应获取 `job_id`
4. 轮询任务：`GET /video-trans/jobs/{job_id}`
5. 直到 `status` 为 `succeeded` 或 `failed`

## 返回结果处理

* `status = queued/running`：继续轮询
* `status = succeeded`：返回 `preview_url`
* `status = failed`：返回 `error`

## 错误处理

* 没有 API Key，或者 APIKey 无效：
  + 中国地区：引导到 `https://luoji.cn`
  + 非中国地区：引导到 `https://luoji.cn?lang=en-US`
* token 不足：
  + 中国地区：引导到 `https://luoji.cn`
  + 非中国地区：引导到 `https://luoji.cn?lang=en-US`
* 其他失败：直接返回接口 `error` 文本

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

- Real time video translation / dubbing skill
- Translate user-provided
  video (file or URL) and retu
- 触发关键词: translator, video, dubbing, real, translation, time

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 常见问题

### Q1: 如何开始使用Video Translator？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Video Translator有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
