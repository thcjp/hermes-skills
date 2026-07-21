---
slug: ai-assistant-tmux
name: claude-tmux
version: "1.0.0"
displayName: ai-assistant Tmux
summary: This skill is an instruction-only tmux helper that does what it advertises,
  though users should b...
license: MIT
description: |-
  This skill is an instruction-only tmux helper that does what it advertises,
  though users should b。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Development
tools:
  - - read
- exec
---

# ai-assistant Code within tmux

## Goal

Give Codex a repeatable checklist for interacting with ai-assistant Code when it’s running inside tmux. Everything happens with standard tmux commands—no helper scripts. Follow these steps any time you see instructions like “check ai-assistant in session X” or “run /compact on ai-assistant.”

## Conventions

1. **Session naming** – We refer to tmux sessions by their tmux session name. Session names can be assigned using `tmux new-session -s <session_name>`. E.g. if we had created a tmux session for project FooBar using `tmux new-session -s foobar`, then we will refer to this session by the name `foobar`.
2. **ai-assistant pane** – Within a session, there should be exactly one pane whose *window title* or *pane title* is `ai-assistant`. If the pane isn’t named, rename it first (`Ctrl-b : select-pane -T ai-assistant`).
3. **Standard markers** – ai-assistant Code prints user prompts with `❯ …` and its replies with `⏺ …`. We rely on that to spot the latest exchange.

## Workflow

### 1. Locate the ai-assistant pane

```text
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index} #{pane_title}' | grep "^<session_name>" | grep -i ai-assistant
```

* If nothing matches, say “No pane titled ‘ai-assistant’ found inside session .”
* If multiple panes match, pick the one with the lowest `window_index/pane_index` unless context says otherwise.
* Record the target as `<session>:<window>.<pane>` for subsequent commands.

### 2. View the latest exchange

```text
tmux capture-pane -p -J -t <target> -S -200
```

* Scan from the bottom upward for the last `❯` block (user) followed by `⏺` (ai-assistant). Quote those lines back to the user.
* If no `❯/⏺` pair exists, say “No exchange found yet.”

### 3. Send a prompt

```text
tmux send-keys -t <target> -l -- "<prompt>"
sleep 0.1
 tmux send-keys -t <target> Enter
```

* After sending, poll using capture-pane until a new `⏺` block appears (or a sensible timeout, e.g., 3 minutes). Report the reply verbatim.
* If the timeout expires, say “ai-assistant hasn’t replied yet—still waiting.”

### 4. Run `/compact`

Same as sending any prompt, but send `/compact`. Confirm with “Triggered /compact in session .” (ai-assistant will respond in-pane; no need to quote unless asked.)

### 5. Dump raw buffer (debug)

```text
tmux capture-pane -p -J -t <target> -S -400
```

Use this when the user wants the entire scrollback or when parsing fails.

## Tips

* Always double-check you’re addressing the right pane before sending commands—especially in shared sessions.
* If the ai-assistant pane lives on a non-default tmux socket, prefix every tmux command with `tmux -S /path/to/socket …`.
* When summarizing results, mention the session/pane you used—for traceability.
* If the user wants multiple sessions handled, repeat the workflow per session.

This skill keeps things simple: pure tmux, no external code. Use it whenever you need hands-on access to ai-assistant Code running inside tmux.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
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

- This skill is an instruction-only tmux helper that does what it advertises,
  though users should b
- 触发关键词: within, code, ai-assistant, tmux, instruction, skill

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Claude Tmux？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: ai-assistant Tmux有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
