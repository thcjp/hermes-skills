---
slug: ai-assistant-code-runner
name: claude-code-runner
version: "0.1.0"
displayName: ai-assistant Code Ru
summary: "经PTY调用ai-assistant Code执行编程任务,搞定非TTY"
  non-TTY environment...
license: MIT
description: |-
  Execute programming tasks via ai-assistant Code using PTY-based invocation。Handles non-TTY environment。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# AI-Assistant Code Runner

## Overview

The AI-Assistant Code Runner is a sophisticated tool that enables developers to execute programming tasks using AI-Assistant Code in environments where interactive TTY sessions are not available. It is particularly useful for automating tasks in non-interactive contexts such as CI/CD pipelines, background jobs, and containerized applications.

## Features

* **PTY-based Execution**: The AI-Assistant Code Runner uses PTY to simulate a TTY session, allowing for the execution of tasks that require TTY interaction in non-TTY environments.
* **Auto-Confirmation**: The tool can automatically respond to confirmation prompts, reducing manual intervention and streamlining the execution process.
* **User Switching**: It supports running tasks as a specified non-root user, enhancing security and access control.
* **File Synchronization**: The AI-Assistant Code Runner copies projects to a temporary directory, executes the task, and then syncs any changes back to the original directory.
* **Timeout Handling**: Tasks can be configured with a timeout, ensuring that resources are not tied up indefinitely.
* **Output Capture**: It captures and returns the full stdout and stderr output, providing comprehensive feedback on the task execution.

## Installation

To install the AI-Assistant Code Runner, follow these steps:

```bash
git clone https://github.com/lhl09120/ai-assistant-code-runner.git
cd ai-assistant-code-runner
chmod +x scripts/run_claude.py
```

## Usage

### Basic Usage

```python
from ai_assistant_code_runner import run_claude_code

result = run_claude_code(
    workdir='/path/to/project',
    prompt='Refactor the authentication module to use JWT tokens',
    user='lighthouse',
    timeout=300
)

print(result)
```

### Command Line

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

This function executes a task using AI-Assistant Code in a PTY environment.

**Parameters:**

* `workdir` (str): The path to the working directory containing the project.
* `prompt` (str): The natural language description of the task to be executed.
* `user` (str): The user under which the task should be run (default: 'lighthouse').
* `timeout` (int): The maximum time allowed for the task to complete (default: 300 seconds).

**Returns:**

* `str`: The combined stdout and stderr output from the task execution.

**Behavior:**

1. Copies the project to a temporary directory.
2. Changes ownership to the specified user.
3. Executes AI-Assistant Code via PTY.
4. Auto-responds to confirmation prompts.
5. Syncs changes back to the original directory.
6. Cleans up temporary files.

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

### 3. Core Capabilities

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
* AI-Assistant Code installed and in PATH
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

### AI-Assistant Code not found

Make sure AI-Assistant Code is installed and in the system PATH:

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
* AI-Assistant Code must be installed separately
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
* PTY-based AI-Assistant Code execution
* Auto-response to confirmation prompts
* File synchronization
* User switching support

## Dependencies

### Operating System

- **Agent Platform**: Supports any SKILL.md compatible AI Agent (AI-Assistant Code / Cursor / Codex / Gemini CLI, etc.)
- **Operating System**: Windows / macOS / Linux

### Dependencies

| Dependency | Type | Required | Acquisition Method |
|:-----------|:-----|:---------|:------------------|
| LLM API | API | Required | Provided by the integrated LLM of the Agent |

### API Key Configuration

- This Skill uses Markdown instructions and does not require an additional API key (unless explicitly stated for external APIs).

### Availability Classification

- **Classification**: MD+EXEC (Pure Markdown instructions, some functions require exec command-line execution capabilities)
- **Description**: An AI Skill based on Markdown that drives Agent execution with natural language instructions.

## Usage Process

1. Confirm that the environment meets the requirements specified in the Dependency section.
2. Choose the appropriate usage method based on the application scenario.
3. Execute the operation and check the output results.
4. If an error occurs, refer to the Troubleshooting section for guidance.

## Examples

### Example 1: Basic Usage

```
Input: User request
Processing: Execute according to the usage process
Output: Processing result
```

## Common Questions

### Q1: How do I start using Claude Code Runner?
A: Please refer to the Usage Process section and ensure that the environment meets the requirements.

### Q2: What should I do if I encounter an error?
A: Refer to the Troubleshooting section for troubleshooting steps.

### Q3: What are the limitations of Claude Code Runner?
A: Refer to the Limitations section to understand the specific restrictions.