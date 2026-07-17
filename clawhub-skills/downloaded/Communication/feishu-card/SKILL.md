---
slug: feishu-card
name: feishu-card
version: "1.4.11"
displayName: Feishu Card
summary: Send rich interactive Feishu cards with markdown, headers, buttons, images,
  and styled persona me...
license: MIT
description: |-
  Send rich interactive Feishu cards with markdown, headers, buttons,
  images, and styled persona me...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: interactive, feishu, cards, card, rich, send
tags:
- Communication
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
