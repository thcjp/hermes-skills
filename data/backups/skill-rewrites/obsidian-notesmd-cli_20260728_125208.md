---
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
summary: "经notesmd-cli管Obsidian笔记库"
---
# Obsidian via notesmd-cli (obsidian-cli)

Obsidian vault = a normal folder on disk.

Vault structure (typical)

* Notes: `*.md` (plain text Markdown; edit with any editor)
* Config: `.obsidian/` (workspace + plugin settings; usually don’t touch from scripts)
* Canvases: `*.canvas` (JSON)
* Attachments: whatever folder you chose in Obsidian settings (images/PDFs/etc.)

## Find the active vault(s)

Obsidian desktop tracks vaults here (source of truth):

* `~/Library/Application Support/obsidian/obsidian.json`

`notesmd-cli` resolves vaults from that file; vault name is typically the **folder name** (path suffix).

Fast “what vault is active / where are the notes?”

* If you’ve already set a default: `notesmd-cli print-default --path-only`
* Otherwise, read `~/Library/Application Support/obsidian/obsidian.json` and use the vault entry with `"open": true`.

## 使用流程

Pick a default vault and open behavior (once):

* `notesmd-cli set-default "<vault-folder-name>"`
* `notesmd-cli set-default --open-type editor` (Sets default to use your terminal/GUI `$EDITOR` instead of opening the Obsidian app)
* `notesmd-cli print-default` / `notesmd-cli print-default --path-only`

Search

* `notesmd-cli search` (Interactive fuzzy search for notes; respects Obsidian's excluded files)
* `notesmd-cli search-content "query"` (Searches inside notes; shows snippets + lines)

Create

* `notesmd-cli create "Folder/New note" --content "..."`
* `notesmd-cli create "New note" --open` (Opens in Obsidian, or `$EDITOR` if `--editor` flag is passed)
* **Note:** Works directly on disk (headless supported); Obsidian does *not* need to be running. Reads `.obsidian/app.json` for default new file locations.

Daily Notes

* `notesmd-cli daily` (Creates or opens today's daily note directly on disk)
* Automatically reads your `.obsidian/daily-notes.json` for folder, format, and template configurations.

Frontmatter (YAML Metadata)

* `notesmd-cli frontmatter "NoteName" --print`
* `notesmd-cli frontmatter "NoteName" --edit --key "status" --value "done"`
* `notesmd-cli frontmatter "NoteName" --delete --key "draft"`

Move/rename (safe refactor)

* `notesmd-cli move "old/path/note" "new/path/note"`
* Updates `[[wikilinks]]` and common Markdown links across the vault (this is the main win vs standard `mv`).

Delete

* `notesmd-cli delete "path/note"`

Prefer direct edits when appropriate: open the `.md` file in any editor (`notesmd-cli open "note" --editor`) and change it; Obsidian will automatically pick it up.

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

- Work with Obsidian vaults (plain Markdown notes) and automate via notesmd-cli
- 触发关键词: via, obsidian, notesmd, vaults, plain, notesmd-cli, (obsidian-cli), cli

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
Pick a default vault and open behavior (once):

* `notesmd-cli set-default "<vault-folder-name>"`
* `notesmd-cli set-default --open-type editor` (Sets default to use your terminal/GUI `$EDITOR` instead of opening the Obsidian app)
* `notesmd-cli print-default` / `notesmd-cli print-default --path-only`

Search

* `notesmd-cli search` (Interactive fuzzy search for notes; respects Obsidian's excluded files)
* `notesmd-cli search-content "query"` (Searches inside notes; shows snippets + lines)

Crea
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Obsidian Notesmd Cli？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Obsidian Notesmd Cli有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
