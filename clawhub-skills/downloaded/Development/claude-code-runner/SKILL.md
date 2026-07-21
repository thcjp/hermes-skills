---
slug: ai-assistant-code-runner
name: claude-code-runner
version: "0.1.0"
displayName: ai-assistant Code Ru
summary: Execute programming tasks via ai-assistant Code using PTY-based invocation. Handles
  non-TTY environment...
license: MIT
description: |-
  Execute programming tasks via ai-assistant Code using PTY-based invocation。Handles non-TTY environment。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Development
tools:
  - - read
- exec
---

# ai-assistant Code Runner

## Overview

A wrapper skill for running ai-assistant Code programmatically in non-interactive environments. Uses PTY (pseudo-terminal) to handle TTY-required operations and automatically responds to confirmation prompts.

## Features

* **PTY-based execution**: Works in non-TTY environments (containers, CI/CD, background processes)
* **Auto-respond to prompts**: Automatically answers "Do you want to..." confirmations
* **User switching**: Runs as specified non-root user
* **File synchronization**: Copies project to temp directory, executes, syncs changes back
* **Timeout handling**: Configurable timeout with proper cleanup
* **Output capture**: Captures and returns full stdout/stderr

## Installation

```bash
git clone https://github.com/lhl09120/ai-assistant-code-runner-en.git

chmod +x ai-assistant-code-runner-en/scripts/run_claude.py
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

Execute a ai-assistant Code task in a PTY environment.

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
3. Executes ai-assistant Code via PTY
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

### 核心能力

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
* ai-assistant Code installed and in PATH
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

### ai-assistant Code not found

Make sure ai-assistant Code is installed and in the system PATH:

```bash
which ai-assistant
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
* ai-assistant Code must be installed separately
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
* PTY-based ai-assistant Code execution
* Auto-response to confirmation prompts
* File synchronization
* User switching support

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

### Q1: 如何开始使用Claude Code Runner？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: ai-assistant Code Runner有什么限制？
A: 请参考已知限制章节了解具体限制。
