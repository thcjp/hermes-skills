---
slug: note-taker
name: note-taker
version: "2.0.1"
displayName: Note Taker
summary: 笔记整理助手。康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理。Note-taking with
  Cornell method, Zettelka...
license: MIT-0
description: |-
  笔记整理助手。康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Note Taker

A productivity and task management tool. Add items, manage a to-do list, set priorities, track daily and weekly views, set reminders, view statistics, clear completed tasks, and export data — all from the command line with persistent local storage.

## Commands

### Task Management

| Command | Description | Usage |
| --- | --- | --- |
| `add` | Add a new item to your task list | `note-taker add <text>` |
| `list` | List all current items | `note-taker list` |
| `done` | Mark an item as completed | `note-taker done <item>` |
| `priority` | Set priority level for an item | `note-taker priority <item> <level>` |
| `clear` | Clear all completed items from the list | `note-taker clear` |

### Views & Planning

| Command | Description | Usage |
| --- | --- | --- |
| `today` | Show today's items and schedule | `note-taker today` |
| `week` | Show the weekly overview | `note-taker week` |
| `remind` | Set a reminder for an item | `note-taker remind <item> <time>` |

### Data & Management

| Command | Description | Usage |
| --- | --- | --- |
| `stats` | Show total item count and statistics | `note-taker stats` |
| `export` | Export all data to stdout | `note-taker export` |
| `help` | Show the built-in help message | `note-taker help` |
| `version` | Print the current version (v2.0.0) | `note-taker version` |

## How It Works

* **`add`** appends a date-stamped line to the data file and confirms with "Added: ..."
* **`list`** prints all items from the data file, or "(empty)" if nothing exists yet
* **`done`** marks a given item as completed and logs the action
* **`priority`** assigns a priority level (default: medium) to the specified item
* **`today`** filters the data file for today's date and displays matching items
* **`week`** shows a weekly overview of scheduled items
* **`remind`** sets a reminder for an item at a specified time (default: tomorrow)
* **`stats`** prints the total line count from the data file
* **`clear`** removes completed items from the active list
* **`export`** dumps the entire data file contents to stdout

## Data Storage

All data is stored locally in `~/.local/share/note-taker/`:

* **`data.log`** — the main data file containing all items (one per line, date-prefixed)
* **`history.log`** — tracks all command activity with timestamps
* Entries in data.log are formatted as `YYYY-MM-DD <content>`
* Set `NOTE_TAKER_DIR` environment variable to change the data directory
* Also respects `XDG_DATA_HOME` if set (defaults to `~/.local/share`)

## Requirements

* Bash (any modern version)
* No external dependencies — pure shell script
* Works on Linux and macOS
* Standard Unix utilities: `date`, `wc`, `grep`, `cat`

## When to Use

1. **Daily task tracking** — use `add` to capture tasks throughout the day, `today` to see what's on your plate, and `done` to check off completed work
2. **Weekly planning sessions** — use `week` for an overview, `priority` to rank what matters most, and `remind` for upcoming deadlines
3. **Quick capture from terminal** — when you're already in the terminal and want to jot something down without switching apps, `add` is instant
4. **Reviewing progress** — use `list` to see everything, `stats` for totals, and `export` to pipe data into other tools for analysis
5. **Maintaining a clean list** — use `clear` to remove completed items and keep your active list focused on what still needs attention

## 示例

```bash
note-taker add "Review pull request for auth module"

note-taker add "Prepare slides for Friday meeting"

note-taker list

note-taker done "Review pull request for auth module"

note-taker priority "Prepare slides for Friday meeting" high

note-taker today

note-taker remind "Submit expense report" "Friday 5pm"

note-taker stats

note-taker export > backup.txt
```

## Output

Commands print concise confirmations to stdout. `list` and `export` output the full data file. `stats` shows a total count. All actions are also logged to `history.log` for auditing. Redirect output with standard shell operators: `note-taker list > tasks.txt`.

## Configuration

| Variable | Description | Default |
| --- | --- | --- |
| `NOTE_TAKER_DIR` | Override the data directory path | `~/.local/share/note-taker` |
| `XDG_DATA_HOME` | XDG base directory (used if `NOTE_TAKER_DIR` is not set) | `~/.local/share` |

---

Powered by BytesAgain | bytesagain.com | [hello@bytesagain.com](mailto:hello@bytesagain.com)

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

- 康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理
- Note-taking
  with Cornell method, Zettelka
- 触发关键词: 康奈尔笔记法, 会议笔记, taking, 卡片盒笔记, taker, note, 思维导图笔记, cornell

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

### Q1: 如何开始使用Note Taker？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Note Taker有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

Note Taker技能在设计和使用过程中存在一些边界条件和限制，以下列出了一些具体的情况：

### 输入限制

- **文本长度限制**：Note Taker技能对于输入的文本长度有限制，过长的文本可能会导致处理错误或响应延迟。
- **格式要求**：输入文本应遵循一定的格式规范，如使用正确的命令格式和参数，否则可能导致技能无法正确解析。

### 性能边界

- **并发处理能力**：Note Taker技能在处理大量并发请求时，可能会出现响应速度下降的情况。
- **数据处理能力**：对于需要大量数据处理和分析的任务，Note Taker技能的响应时间可能会受到影响。

### 兼容性约束

- **操作系统兼容性**：Note Taker技能主要支持Linux和macOS操作系统，Windows用户可能需要额外配置。
- **终端兼容性**：Note Taker技能依赖于终端环境，不支持在图形界面环境中直接使用。

### 功能限制

- **复杂决策支持**：Note Taker技能不适用于需要人工判断的复杂决策场景，如风险评估、战略规划等。
- **外部API依赖**：Note Taker技能依赖于LLM API，无LLM环境无法使用。

### 数据存储限制

- **本地存储容量**：Note Taker技能的数据存储依赖于本地文件系统，存储容量受限于系统配置。
- **数据安全性**：Note Taker技能不提供数据加密功能，用户需自行确保数据安全性。

---

