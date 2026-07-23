---
slug: feishu-card
name: feishu-card
version: "1.4.11"
displayName: Feishu Card
summary: "发富交互飞书卡片,含markdown/标题/按钮/图片/样式"
  and styled persona me...
license: MIT
description: |-
  Send rich interactive Feishu cards with markdown, headers, buttons,
  images, and styled persona me。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Feishu Card

Send rich interactive cards to Feishu (Lark) users or groups. Supports Markdown (code blocks, tables), titles, color headers, and buttons.

## Prerequisites

* Install `feishu-common` first.
* This skill depends on `../feishu-common/index.js` for token and API auth.

## Usage

### 1. Simple Text (No special characters)

```bash
node skills/feishu-card/send.js --target "ou_..." --text "Hello World"
```

### 2. Complex/Markdown Text (RECOMMENDED)

**⚠️ CRITICAL:** To prevent shell escaping issues (e.g., swallowed backticks), ALWAYS write content to a file first.

1. Write content to a temp file:

```bash
write temp/msg.md "Here is some code:\n\`\`\`js\nconsole.log('hi');\n\`\`\`"
```

2. Send using `--text-file`:

```bash
node skills/feishu-card/send.js --target "ou_..." --text-file "temp/msg.md"
```

### 3. Safe Send (Automated Temp File)

Use this wrapper to safely send raw text without manually creating a file. It handles file creation and cleanup automatically.

```bash
node skills/feishu-card/send_safe.js --target "ou_..." --text "Raw content with \`backticks\` and *markdown*" --title "Safe Message"
```

### Options

* `-t, --target <id>`: User Open ID (`ou_...`) or Group Chat ID (`oc_...`).
* `-x, --text <string>`: Simple text content.
* `-f, --text-file <path>`: Path to text file (Markdown supported). **Use this for code/logs.**
* `--title <string>`: Card header title.
* `--color <string>`: Header color (blue/red/orange/green/purple/grey). Default: blue.
* `--button-text <string>`: Text for a bottom action button.
* `--button-url <url>`: URL for the button.
* `--image-path <path>`: Path to a local image to upload and embed.

## Troubleshooting

* **Missing Text**: Did you use backticks in `--text`? The shell likely ate them. Use `--text-file` instead.

## 4. Persona Messaging

Send stylized messages from different AI personas. Adds themed headers, colors, and formatting automatically.

```bash
node skills/feishu-card/send_persona.js --target "ou_..." --persona "d-guide" --text "Critical error detected."
```

### Supported Personas

* **d-guide**: Red warning header, bold/code prefix. Snarky suffix.
* **green-tea**: Carmine header, soft/cutesy style.
* **mad-dog**: Grey header, raw runtime error style.
* **default**: Standard blue header.

### Usage

* `-p, --persona <type>`: Select persona (d-guide, green-tea, mad-dog).
* `-x, --text <string>`: Message content.
* `-f, --text-file <path>`: Message content from file (supports markdown).

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

- Send rich interactive Feishu cards with markdown, headers, buttons,
  images, and styled persona me
- 触发关键词: interactive, feishu, cards, card, rich, send

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

### Q1: 如何开始使用Feishu Card？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Feishu Card有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
