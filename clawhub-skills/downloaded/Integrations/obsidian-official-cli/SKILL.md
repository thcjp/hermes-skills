---
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
summary: "Obsidian官方CLI,命令行做Obsidian一切"
---
# Obsidian Official CLI Skill

Official command-line interface for Obsidian. Anything you can do in Obsidian can be done from the command line — including developer commands for debugging, screenshots, and plugin reloading.

## Prerequisites

* **Obsidian 1.12+** and **Catalyst license** required
* **Settings → General → Command line interface** → Enable
* Follow prompt to register the `obsidian` command
* Restart terminal or `source ~/.zprofile` (macOS)
* **Note:** Obsidian must be running for CLI to work

Test setup: `obsidian version`

## Core Patterns

### Command Structure

```bash
obsidian <command> [parameters] [flags]

obsidian  # Enter TUI with autocomplete and history

obsidian vault=Notes <command>
obsidian vault="My Vault" <command>
```

### Parameter Types

* **Parameters:** `name=value` (quote values with spaces)
* **Flags:** Boolean switches (just include to enable)
* **Multiline:** Use  for newlines, `\t` for tabs
* **Copy output:** Add `--copy` to copy to clipboard

## File Operations

### Basic File Management

```bash
obsidian file                          # Active file info
obsidian file file=Recipe              # Specific file info
obsidian files                         # List all files
obsidian files folder=Projects/        # Filter by folder
obsidian folders                       # List folders

obsidian open file=Recipe              # Open file
obsidian open path="Inbox/Note.md" newtab
obsidian read                          # Read active file
obsidian read file=Recipe --copy       # Read and copy to clipboard

obsidian create name="New Note"
obsidian create name="Note" content="# Title Body"
obsidian create path="Inbox/Idea.md" template=Daily
obsidian create name="Note" silent overwrite

obsidian append file=Note content="New line"
obsidian append file=Note content="Same line" inline
obsidian prepend file=Note content="After frontmatter"

obsidian move file=Note to=Archive/
obsidian move path="Inbox/Old.md" to="Projects/New.md"
obsidian delete file=Note              # To trash
obsidian delete file=Note permanent
```

### File Targeting

* `file=<name>` — Wikilink resolution (matches by name)
* `path=<path>` — Exact path from vault root

## Search and Discovery

### Text Search

```bash
obsidian search query="meeting notes"
obsidian search query="TODO" matches    # Show context
obsidian search query="project" path=Projects/
obsidian search query="urgent" limit=10 case
obsidian search query="API" format=json
obsidian search:open query="search term"  # Open in Obsidian
```

### Tags and Properties

```bash
obsidian tags                          # Active file tags
obsidian tags all                      # All vault tags
obsidian tags all counts sort=count    # By frequency
obsidian tag name=project              # Tag info

obsidian properties file=Note
obsidian property:read name=status file=Note
obsidian property:set name=status value=done file=Note
obsidian property:set name=tags value="a,b,c" type=list file=Note
obsidian property:remove name=draft file=Note
```

### Links and Structure

```bash
obsidian backlinks file=Note           # What links to this
obsidian links file=Note               # Outgoing links

obsidian orphans                       # No incoming links
obsidian deadends                      # No outgoing links
obsidian unresolved                    # Broken links
obsidian unresolved verbose counts
```

## Daily Notes and Tasks

### Daily Notes

```bash
obsidian daily                         # Open today's note
obsidian daily paneType=split          # Open in split
obsidian daily:read                    # Print contents
obsidian daily:append content="- [ ] New task"
obsidian daily:prepend content="## Morning"
```

### Task Management

```bash
obsidian tasks                         # Active file
obsidian tasks all                     # All vault tasks
obsidian tasks all todo                # Incomplete only
obsidian tasks file=Recipe             # Specific file
obsidian tasks daily                   # Daily note tasks

obsidian task ref="Recipe.md:8" toggle
obsidian task file=Recipe line=8 done
obsidian task file=Recipe line=8 todo
obsidian task file=Note line=5 status="-"  # Custom [-]
```

## Templates and Bookmarks

### Templates

```bash
obsidian templates                     # List all templates
obsidian template:read name=Daily
obsidian template:read name=Daily resolve title="My Note"
obsidian template:insert name=Daily    # Insert into active file
obsidian create name="Meeting Notes" template=Meeting
```

### Bookmarks

```bash
obsidian bookmarks                     # List all
obsidian bookmark file="Important.md"
obsidian bookmark file=Note subpath="#Section"
obsidian bookmark folder="Projects/"
obsidian bookmark search="TODO"
obsidian bookmark url="https://..." title="Reference"
```

## Plugin and Theme Management

### Plugins

```bash
obsidian plugins                       # All installed
obsidian plugins:enabled               # Only enabled
obsidian plugin id=dataview            # Plugin info

obsidian plugin:enable id=dataview
obsidian plugin:disable id=dataview
obsidian plugin:install id=dataview enable
obsidian plugin:uninstall id=dataview
obsidian plugin:reload id=my-plugin    # Development
```

### Themes and CSS

```bash
obsidian themes                        # List installed
obsidian theme                         # Active theme
obsidian theme:set name=Minimal
obsidian theme:install name="Theme Name" enable

obsidian snippets                      # List all
obsidian snippet:enable name=my-snippet
obsidian snippet:disable name=my-snippet
```

## 核心能力

### Obsidian Sync

```bash
obsidian sync:status                   # Status and usage
obsidian sync on/off                   # Resume/pause
obsidian sync:history file=Note
obsidian sync:restore file=Note version=2
obsidian sync:deleted                  # Deleted files
```

### File History

```bash
obsidian history file=Note             # List versions
obsidian history:read file=Note version=1
obsidian history:restore file=Note version=2
obsidian diff file=Note from=2 to=1   # Compare versions
```

### Developer Tools

```bash
obsidian devtools                      # Toggle dev tools
obsidian dev:console                   # Show console
obsidian dev:errors                    # JS errors
obsidian eval code="app.vault.getFiles().length"

obsidian dev:screenshot path=screenshot.png
obsidian dev:dom selector=".workspace-leaf"
obsidian dev:css selector=".mod-active" prop=background

obsidian dev:mobile on/off
obsidian dev:debug on/off
```

## Utility Commands

### Workspace and Navigation

```bash
obsidian workspace                     # Current layout
obsidian workspace:save name="coding"
obsidian workspace:load name="coding"
obsidian tabs                          # Open tabs
obsidian tab:open file=Note

obsidian random                        # Open random note
obsidian random folder=Inbox newtab
obsidian unique                        # Create unique name
obsidian wordcount file=Note           # Word count
```

### Command Palette

```bash
obsidian commands                      # List all command IDs
obsidian commands filter=editor        # Filter commands
obsidian command id=editor:toggle-bold
obsidian hotkeys                       # List hotkeys
```

## TUI Mode

Interactive terminal UI with enhanced features:

```bash
obsidian                               # Enter TUI mode
```

**TUI Shortcuts:**

* **Navigation:** ←/→ (Ctrl+B/F), Home/End (Ctrl+A/E)
* **Editing:** Ctrl+U (delete to start), Ctrl+K (delete to end)
* **Autocomplete:** Tab/↓ (enter), Shift+Tab/Esc (exit)
* **History:** ↑/↓ (Ctrl+P/N), Ctrl+R (reverse search)
* **Other:** Enter (execute), Ctrl+L (clear), Ctrl+C/D (exit)

## Troubleshooting

### Setup Issues

* Use latest installer (1.11.7+) with early access (1.12.x)
* Restart terminal after CLI registration
* Ensure Obsidian is running before using CLI

### Platform-Specific

**macOS:** PATH added to `~/.zprofile`

```bash
export PATH="$PATH:/Applications/Obsidian.app/Contents/MacOS"
```

**Linux:** Symlink at `/usr/local/bin/obsidian`

```bash
sudo ln -s /path/to/obsidian /usr/local/bin/obsidian
```

**Windows:** Requires `Obsidian.com` terminal redirector (Catalyst Discord)

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

### Q1: 如何开始使用Obsidian Official Cl？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Obsidian Official Cl有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
