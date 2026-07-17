---
slug: python
name: python
version: "1.0.0"
displayName: Python Coding Guidelines
summary: Python coding guidelines and best practices. Use when writing, reviewing,
  or refactoring Python c...
license: MIT
description: |-
  Python coding guidelines and best practices. Use when writing, reviewing,
  or refactoring Python c...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: guidelines, python, practices, coding, best
tags:
- Development
tools:
- read
- exec
---

# Python Coding Guidelines

## Code Style (PEP 8)

* 4 spaces for indentation (never tabs)
* Max line length: 88 chars (Black default) or 79 (strict PEP 8)
* Two blank lines before top-level definitions, one within classes
* Imports: stdlib → third-party → local, alphabetized within groups
* Snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants

## Before Committing

```bash
python -m py_compile *.py

python -m pytest tests/ -v 2>/dev/null || python -m unittest discover -v 2>/dev/null || echo "No tests found"

ruff check . --fix 2>/dev/null || python -m black --check . 2>/dev/null
```

## Python Version

* **Minimum:** Python 3.10+ (3.9 EOL Oct 2025)
* **Target:** Python 3.11-3.13 for new projects
* Never use Python 2 syntax or patterns
* Use modern features: match statements, walrus operator, type hints

## Dependency Management

Check for uv first, fall back to pip:

```bash
if command -v uv &>/dev/null; then
    uv pip install <package>
    uv pip compile requirements.in -o requirements.txt
else
    pip install <package>
fi
```

For new projects with uv: `uv init` or `uv venv && source .venv/bin/activate`

## Pythonic Patterns

```python
squares = [x**2 for x in range(10)]
lookup = {item.id: item for item in items}

with open("file.txt") as f:
    data = f.read()

first, *rest = items
a, b = b, a  # swap

try:
    value = d[key]
except KeyError:
    value = default

msg = f"Hello {name}, you have {count} items"

def process(items: list[str]) -> dict[str, int]:
    ...

from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    active: bool = True

from pathlib import Path
config = Path.home() / ".config" / "app.json"

for i, item in enumerate(items):
    ...
for a, b in zip(list1, list2, strict=True):
    ...
```

## Anti-patterns to Avoid

```python
def bad(items=[]):  # Bug: shared across calls
    ...
def good(items=None):
    items = items or []

try:
    ...
except:  # Catches SystemExit, KeyboardInterrupt
    ...
except Exception:  # Better
    ...

```

## Testing

* Use pytest (preferred) or unittest
* Name test files `test_*.py`, test functions `test_*`
* Aim for focused unit tests, mock external dependencies
* Run before every commit: `python -m pytest -v`

## Docstrings

```python
def fetch_user(user_id: int, include_deleted: bool = False) -> User | None:
    """Fetch a user by ID from the database.

    Args:
        user_id: The unique user identifier.
        include_deleted: If True, include soft-deleted users.

    Returns:
        User object if found, None otherwise.

    Raises:
        DatabaseError: If connection fails.
    """
```

## Quick Checklist

* Syntax valid (`py_compile`)
* Tests pass (`pytest`)
* Type hints on public functions
* No hardcoded secrets
* f-strings, not `.format()` or `%`
* `pathlib` for file paths
* Context managers for I/O
* No mutable default args

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
