---
slug: claude-tmux
name: claude-tmux
version: "1.0.0"
displayName: Claude Code within tmux
summary: This skill is an instruction-only tmux helper that does what it advertises,
  though users should b...
license: MIT
description: |-
  This skill is an instruction-only tmux helper that does what it advertises,
  though users should b...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: within, code, claude, tmux, instruction, skill
tags:
- Development
tools:
- read
- exec
---

# Claude Code within tmux

## Goal

Give Codex a repeatable checklist for interacting with Claude Code when it’s running inside tmux. Everything happens with standard tmux commands—no helper scripts. Follow these steps any time you see instructions like “check Claude in session X” or “run /compact on Claude.”

## Conventions

1. **Session naming** – We refer to tmux sessions by their tmux session name. Session names can be assigned using `tmux new-session -s <session_name>`. E.g. if we had created a tmux session for project FooBar using `tmux new-session -s foobar`, then we will refer to this session by the name `foobar`.
2. **Claude pane** – Within a session, there should be exactly one pane whose *window title* or *pane title* is `claude`. If the pane isn’t named, rename it first (`Ctrl-b : select-pane -T claude`).
3. **Standard markers** – Claude Code prints user prompts with `❯ …` and its replies with `⏺ …`. We rely on that to spot the latest exchange.

## Workflow

### 1. Locate the Claude pane

```text
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index} #{pane_title}' | grep "^<session_name>" | grep -i claude
```

* If nothing matches, say “No pane titled ‘claude’ found inside session .”
* If multiple panes match, pick the one with the lowest `window_index/pane_index` unless context says otherwise.
* Record the target as `<session>:<window>.<pane>` for subsequent commands.

### 2. View the latest exchange

```text
tmux capture-pane -p -J -t <target> -S -200
```

* Scan from the bottom upward for the last `❯` block (user) followed by `⏺` (Claude). Quote those lines back to the user.
* If no `❯/⏺` pair exists, say “No exchange found yet.”

### 3. Send a prompt

```text
tmux send-keys -t <target> -l -- "<prompt>"
sleep 0.1
 tmux send-keys -t <target> Enter
```

* After sending, poll using capture-pane until a new `⏺` block appears (or a sensible timeout, e.g., 3 minutes). Report the reply verbatim.
* If the timeout expires, say “Claude hasn’t replied yet—still waiting.”

### 4. Run `/compact`

Same as sending any prompt, but send `/compact`. Confirm with “Triggered /compact in session .” (Claude will respond in-pane; no need to quote unless asked.)

### 5. Dump raw buffer (debug)

```text
tmux capture-pane -p -J -t <target> -S -400
```

Use this when the user wants the entire scrollback or when parsing fails.

## Tips

* Always double-check you’re addressing the right pane before sending commands—especially in shared sessions.
* If the Claude pane lives on a non-default tmux socket, prefix every tmux command with `tmux -S /path/to/socket …`.
* When summarizing results, mention the session/pane you used—for traceability.
* If the user wants multiple sessions handled, repeat the workflow per session.

This skill keeps things simple: pure tmux, no external code. Use it whenever you need hands-on access to Claude Code running inside tmux.

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
