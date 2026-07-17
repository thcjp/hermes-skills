---
slug: note-taker
name: note-taker
version: "2.0.1"
displayName: Note Taker
summary: 笔记整理助手。康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理。Note-taking with
  Cornell method, Zettelka...
license: MIT-0
description: |-
  笔记整理助手。康奈尔笔记法、卡片盒笔记(Zettelkasten)、思维导图笔记、会议笔记、课堂笔记、笔记整理。Note-taking
  with Cornell method, Zettelka...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 康奈尔笔记法, 会议笔记, taking, 卡片盒笔记, taker, note, 思维导图笔记, cornell
tags:
- Productivity
tools:
- read
- exec
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

## Examples

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
