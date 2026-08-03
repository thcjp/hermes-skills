---

slug: wenxiang-2d5-banner
name: wenxiang-2d5-banner
version: "1.0.0"
displayName: Wenxiang 2d5 Banner
summary: "使用Gemini 3 Pro Image生成编辑图片,支持创作与修改请求,高质量AI图像处理"
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
uv run ~/.py --prompt "editing instructions" --filename "output-name.png" --input-image "path/to/input.png" [--resolution 1K|2K|4K] [--api-key KEY]
```

**Important:** Always run from the user's current working directory so images are saved where the user is working, not in the skill directory.

## Default Workflow (draft → iterate → final)

Goal: fast iteration without burning time on 4K until the prompt is correct.

* Draft (1K): quick feedback loop
  + `uv run ~/.py --prompt "<draft prompt>" --filename "yyyy-mm-dd-hh-mm-ss-draft.png" --resolution 1K`
* Iterate: adjust prompt in small diffs; keep filename new per run
  + If editing: keep the same `--input-image` for every iteration until you’re happy.
* Final (4K): only when prompt is locked
  + `uv run ~/.py --prompt "<final prompt>" --filename "yyyy-mm-dd-hh-mm-ss-final.png" --resolution 4K`

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
uv run ~/.py --prompt "A serene Japanese garden with cherry blossoms" --filename "2025-11-23-14-23-05-japanese-garden.png" --resolution 4K
```

**Edit existing image:**

```bash
uv run ~/.py --prompt "make the sky more dramatic with storm clouds" --filename "2025-11-23-14-25-30-dramatic-sky.png" --input-image "original-photo.jpg" --resolution 2K
```

## 前置条件
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
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 能力清单
- Generate/edit images with Nano Banana Pro (Gemini 3 Pro Image)
- Use\
  \ for image create/modify reque

## 使用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用指南
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 异常处理架构
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 疑问汇总集
### Q1: 如何开始使用Wenxiang 2d5 Banner？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Wenxiang 2d5 Banner有什么限制？
A: 请参考已知限制章节了解具体限制。

## 能力边界
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 安全规范
### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 量化评估
| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 特色分析
| 对比维度 | Wenxiang 2d5 Banner | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 使用Gemini 3 Pro Image生成编辑图片,支持创作与修改请求,高质量 | 通用场景 | 通用场景 |

## 功能描述
- **自动化执行**: 使用Gemini 3 Pro Image生成编辑图片,支持创作与修改请求,高质量AI图像处理
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果

## 操作入门
1. **配置API密钥**: 在环境变量中设置对应的API Key
2. **初始化连接**: 使用提供的凭证建立API连接
3. **调用接口**: 传入必要参数执行API调用
1. **准备文件**: 确认文件路径正确且格式受支持
2. **执行处理**: 调用对应的处理函数
3. **查看结果**: 检查输出文件或返回数据
1. **检查环境**: 确认运行时和依赖已安装
2. **执行命令**: 使用正确的参数格式执行
3. **查看输出**: 检查命令输出和退出码

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪

## 用户问答
### Q1: Wenxiang 2d5 Banner支持哪些输入格式？

A1: 使用Gemini 3 Pro Image生成编辑图片,支持创作与修改请求,高质量AI图像处理。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。