---
slug: python3
name: python3
version: "1.0.0"
displayName: python
summary: "Python项目搭建、依赖安装、脚本执行、环境排查,解决开发环境配置痛点"
  and environment tro...
license: MIT-0
description: |-
  Use Python for practical project setup, dependency install, script execution,
  and environment tro。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

## 错误处理

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

- Use Python for practical project setup, dependency install, script execution,
  and environment tro
- 触发关键词: setup, project, python, practical, python3, dependency

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

### Q1: 如何开始使用python？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: python有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
