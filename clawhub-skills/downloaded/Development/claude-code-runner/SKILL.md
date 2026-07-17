---
slug: claude-code-runner
name: claude-code-runner
version: "0.1.0"
displayName: Claude Code Runner
summary: Execute programming tasks via Claude Code using PTY-based invocation. Handles
  non-TTY environment...
license: MIT
description: |-
  Execute programming tasks via Claude Code using PTY-based invocation.
  Handles non-TTY environment...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: programming, runner, execute, code, tasks, claude
tags:
- Development
tools:
- read
- exec
---

# Claude Code Runner

## Overview

A wrapper skill for running Claude Code programmatically in non-interactive environments. Uses PTY (pseudo-terminal) to handle TTY-required operations and automatically responds to confirmation prompts.

## Features

* **PTY-based execution**: Works in non-TTY environments (containers, CI/CD, background processes)
* **Auto-respond to prompts**: Automatically answers "Do you want to..." confirmations
* **User switching**: Runs as specified non-root user
* **File synchronization**: Copies project to temp directory, executes, syncs changes back
* **Timeout handling**: Configurable timeout with proper cleanup
* **Output capture**: Captures and returns full stdout/stderr

## Installation

```bash
git clone https://github.com/lhl09120/claude-code-runner-en.git

chmod +x claude-code-runner-en/scripts/run_claude.py
```

## Usage

### Basic Usage

```python
from claude_code_runner import run_claude_code

result = run_claude_code(
    workdir='/path/to/project',
    prompt='Refactor the authentication module to use JWT tokens',
    user='lighthouse',
    timeout=300
)

print(result)
```

### Via Command Line

```bash
python3 scripts/run_claude.py /path/to/project "Your task description here"
```

### Advanced Options

```python
result = run_claude_code(
    workdir='/root/repo/my-project',
    prompt='''
    1. Review the codebase
    2. Identify security vulnerabilities
    3. Fix any issues found
    4. Add appropriate tests
    ''',
    user='developer',
    timeout=600  # 10 minutes
)
```

## API Reference

### `run_claude_code(workdir, prompt, user='lighthouse', timeout=300)`

Execute a Claude Code task in a PTY environment.

**Parameters:**

* `workdir` (str): Working directory containing the project
* `prompt` (str): Natural language task description
* `user` (str): User to run as (default: 'lighthouse')
* `timeout` (int): Timeout in seconds (default: 300)

**Returns:**

* `str`: Combined stdout and stderr output

**Behavior:**

1. Copies project to temporary directory
2. Changes ownership to specified user
3. Executes Claude Code via PTY
4. Auto-responds to confirmation prompts
5. Syncs changes back to original directory
6. Cleans up temporary files

## Use Cases

### 1. Automated Code Review

```python
result = run_claude_code(
    workdir='/root/repo/project',
    prompt='Review this codebase and identify potential bugs or improvements'
)
```

### 2. Refactoring Tasks

```python
result = run_claude_code(
    workdir='/root/repo/legacy-app',
    prompt='Refactor the database layer to use SQLAlchemy ORM instead of raw SQL'
)
```

### 3. Adding Features

```python
result = run_claude_code(
    workdir='/root/repo/api-service',
    prompt='''
    Add a new REST endpoint for user profile management:
    - GET /api/users/{id}/profile
    - PUT /api/users/{id}/profile
    - Include validation and error handling
    - Add unit tests
    '''
)
```

### 4. Bug Fixes

```python
result = run_claude_code(
    workdir='/root/repo/web-app',
    prompt='Fix the memory leak in the WebSocket connection handler'
)
```

## Requirements

* Python 3.8+
* Claude Code installed and in PATH
* Unix-like environment (Linux/macOS)
* Root or sudo access (for user switching)

## Configuration

### Environment Variables

* `CLAUDE_CODE_USER`: Default user to run as (default: 'lighthouse')
* `CLAUDE_CODE_TIMEOUT`: Default timeout in seconds (default: 300)

### Customization

Edit `scripts/run_claude.py` to customize:

* Auto-response keywords
* Temp directory location
* Sync behavior
* Output formatting

## Troubleshooting

### "Permission denied" errors

Ensure the script is run with sufficient privileges to:

* Create temporary directories
* Change file ownership
* Switch to target user

### Claude Code not found

Make sure Claude Code is installed and in the system PATH:

```bash
which claude
```

### Task timeout

Increase the timeout for long-running tasks:

```python
run_claude_code(workdir, prompt, timeout=600)  # 10 minutes
```

### Interactive prompts not auto-responded

Add new prompt patterns to the auto-respond logic:

```python
if b'new prompt text' in output:
    os.write(master_fd, b'y\n')
```

## Limitations

* Requires Unix-like environment (uses PTY)
* Requires root/sudo for user switching
* Claude Code must be installed separately
* May not handle all edge cases of interactive prompts

## License

MIT License

Copyright (c) 2026 lhl09120

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

See LICENSE file for full details.

## Changelog

### v1.0.0 (2026-02-27)

* Initial release
* PTY-based Claude Code execution
* Auto-response to confirmation prompts
* File synchronization
* User switching support

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
