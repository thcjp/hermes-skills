---
slug: python3
name: python3
version: "1.0.0"
displayName: python
summary: Use Python for practical project setup, dependency install, script execution,
  and environment tro...
license: MIT-0
description: |-
  Use Python for practical project setup, dependency install, script execution,
  and environment tro...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: setup, project, python, practical, python3, dependency
tags:
- Productivity
tools:
- read
- exec
---

# python

Use this skill to keep Python workflows reproducible and low-risk across local/dev shells.

## Safety Defaults

* Prefer project-local virtual environments (`.venv`) over global installs.
* Prefer `python3 -m pip ...` to avoid interpreter and pip mismatch.
* Inspect dependency files before install (`requirements*.txt`, `pyproject.toml`).
* Avoid executing unknown setup hooks or random install scripts without user approval.

## Standard Workflow

1. Detect current environment:

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
{baseDir}/scripts/python_env_tool.py doctor
```

2. Create or refresh a venv:

```bash
{baseDir}/scripts/python_env_tool.py bootstrap --venv .venv --requirements requirements.txt
```

3. Install project package (if `pyproject.toml` exists):

```bash
{baseDir}/scripts/python_env_tool.py install --venv .venv --editable
```

4. Run tests/tools from the venv interpreter:

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m pip list --outdated
```

## Task Recipes

```bash
{baseDir}/scripts/python_env_tool.py install --venv .venv --package requests --package pydantic

{baseDir}/scripts/python_env_tool.py install --venv .venv --requirements requirements-dev.txt

{baseDir}/scripts/python_env_tool.py bootstrap --venv .venv --recreate --requirements requirements.txt
```

## Troubleshooting Rules

* `ModuleNotFoundError`: verify command is run via `.venv/bin/python`, then reinstall deps.
* `externally-managed-environment`: stop global install attempts; use venv.
* Build failures on native deps: upgrade `pip setuptools wheel`, then retry.
* Multiple Python versions: always print and confirm `sys.executable` before fixes.

## Bundled Helper

Use the helper for repeatable environment setup and diagnosis:

```bash
{baseDir}/scripts/python_env_tool.py --help
{baseDir}/scripts/python_env_tool.py doctor
```

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
