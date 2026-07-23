---
slug: wenxiang-2d5-banner
name: wenxiang-2d5-banner
version: "1.0.0"
displayName: Wenxiang 2d5 Banner
summary: Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image). Use for image
  create/modify reque...
license: MIT-0
description: |-
  Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image)。Use\
  \ for image create/modify reque。Use when 用户需要Wenxiang 2d5 Banner相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags: '[''Other'']'
tools:
  - read
  - exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# éä¹ä¸ç¸ 2.5D æ¨ªå¹æç»

Generate new images or edit existing ones using Google's Nano Banana Pro API (Gemini 3 Pro Image).

## Usage

Run the script using absolute path (do NOT cd to skill directory first):

**Generate new image:**

```bash
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt "your image description" --filename "output-name.png" [--resolution 1K|2K|4K] [--api-key KEY]
```

**Edit existing image:**

```bash
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt "editing instructions" --filename "output-name.png" --input-image "path/to/input.png" [--resolution 1K|2K|4K] [--api-key KEY]
```

**Important:** Always run from the user's current working directory so images are saved where the user is working, not in the skill directory.

## Default Workflow (draft → iterate → final)

Goal: fast iteration without burning time on 4K until the prompt is correct.

* Draft (1K): quick feedback loop
  + `uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt "<draft prompt>" --filename "yyyy-mm-dd-hh-mm-ss-draft.png" --resolution 1K`
* Iterate: adjust prompt in small diffs; keep filename new per run
  + If editing: keep the same `--input-image` for every iteration until you’re happy.
* Final (4K): only when prompt is locked
  + `uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt "<final prompt>" --filename "yyyy-mm-dd-hh-mm-ss-final.png" --resolution 4K`

## Resolution Options

The Gemini 3 Pro Image API supports three resolutions (uppercase K required):

* **1K** (default) - ~1024px resolution
* **2K** - ~2048px resolution
* **4K** - ~4096px resolution

Map user requests to API parameters:

* No mention of resolution → `1K`
* "low resolution", "1080", "1080p", "1K" → `1K`
* "2K", "2048", "normal", "medium resolution" → `2K`
* "high resolution", "high-res", "hi-res", "4K", "ultra" → `4K`

## API Key

The script checks for API key in this order:

1. `--api-key` argument (use if user provided key in chat)
2. `GEMINI_API_KEY` environment variable

If neither is available, the script exits with an error message.

## Preflight + Common Failures (fast fixes)

* Preflight:

  + `command -v uv` (must exist)
  + `test -n \"$GEMINI_API_KEY\"` (or pass `--api-key`)
  + If editing: `test -f \"path/to/input.png\"`
* Common failures:

  + `Error: No API key provided.` → set `GEMINI_API_KEY` or pass `--api-key`
  + `Error loading input image:` → wrong path / unreadable file; verify `--input-image` points to a real image
  + “quota/permission/403” style API errors → wrong key, no access, or quota exceeded; try a different key/account

## Filename Generation

Generate filenames with the pattern: `yyyy-mm-dd-hh-mm-ss-name.png`

**Format:** `{timestamp}-{descriptive-name}.png`

* Timestamp: Current date/time in format `yyyy-mm-dd-hh-mm-ss` (24-hour format)
* Name: Descriptive lowercase text with hyphens
* Keep the descriptive part concise (1-5 words typically)
* Use context from user's prompt or conversation
* If unclear, use random identifier (e.g., `x9k2`, `a7b3`)

Examples:

* Prompt "A serene Japanese garden" → `2025-11-23-14-23-05-japanese-garden.png`
* Prompt "sunset over mountains" → `2025-11-23-15-30-12-sunset-mountains.png`
* Prompt "create an image of a robot" → `2025-11-23-16-45-33-robot.png`
* Unclear context → `2025-11-23-17-12-48-x9k2.png`

## Image Editing

When the user wants to modify an existing image:

1. Check if they provide an image path or reference an image in the current directory
2. Use `--input-image` parameter with the path to the image
3. The prompt should contain editing instructions (e.g., "make the sky more dramatic", "remove the person", "change to cartoon style")
4. Common editing tasks: add/remove elements, change style, adjust colors, blur background, etc.

## Prompt Handling

**For generation:** Pass user's image description as-is to `--prompt`. Only rework if clearly insufficient.

**For editing:** Pass editing instructions in `--prompt` (e.g., "add a rainbow in the sky", "make it look like a watercolor painting")

Preserve user's creative intent in both cases.

## Prompt Templates (high hit-rate)

Use templates when the user is vague or when edits must be precise.

* Generation template:

  + “Create an image of: . Style: . Composition: <camera/shot>. Lighting: <lighting>. Background: <background>. Color palette: <palette>. Avoid: <list>.”
* Editing template (preserve everything else):

  + “Change ONLY: . Keep identical: subject, composition/crop, pose, lighting, color palette, background, text, and overall style. Do not add new objects. If text exists, keep it unchanged.”

## Output

* Saves PNG to current directory (or specified path if filename includes directory)
* Script outputs the full path to the generated image
* **Do not read the image back** - just inform the user of the saved path

## 示例

**Generate new image:**

```bash
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt "A serene Japanese garden with cherry blossoms" --filename "2025-11-23-14-23-05-japanese-garden.png" --resolution 4K
```

**Edit existing image:**

```bash
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py --prompt "make the sky more dramatic with storm clouds" --filename "2025-11-23-14-25-30-dramatic-sky.png" --input-image "original-photo.jpg" --resolution 2K
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

## 核心能力

- Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image)
- Use\
  \ for image create/modify reque

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

### Q1: 如何开始使用Wenxiang 2d5 Banner？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Wenxiang 2d5 Banner有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
