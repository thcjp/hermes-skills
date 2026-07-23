---
slug: free-google-search-with-browser
name: free-google-search-with-browser
version: "0.0.1"
displayName: Free Google Search W
summary: Search Google using scrapling and return structured results (title, link,
  snippet). Invoke when u...
license: MIT-0
description: |-
  Search Google using scrapling and return structured results (title,
  link, snippet)。Invoke when u。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# free_google_search_with_browser

This skill searches Google using a stealthy fetcher and returns structured results suitable for LLM consumption.

## Usage

Run the python script `google_search.py` with the query as an argument.

```bash
python google_search.py "<query>"
```

## File Structure

* **google_search.py**: The main script. It uses `scrapling` to perform the Google search. It launches a browser instance to fetch results, ensuring high success rates by mimicking real user behavior.
* **verify_search.py**: A debugging script. It runs a predefined set of queries to verify that the search functionality works correctly.
* **requirements.txt**: Lists the Python dependencies required for the project.

## Requirements

* Python 3
* `scrapling` package installed (with `playwright` and `curl_cffi` dependencies)

To install dependencies:

```bash
pip install -r requirements.txt
playwright install  # Required for browser automation. If slow, consider downloading manually.
```

## 错误处理

### Browser Environment (Headless=False)

This skill is configured to run with **`headless=False`** (see `google_search.py`). This means:

1. **GUI Required**: The environment where this code runs **must** support a Graphical User Interface (GUI). It will launch a visible browser window.
2. **No Headless Servers**: It will likely fail on headless servers (like standard CI/CD runners or SSH-only servers) unless X11 forwarding or a virtual display (like `xvfb`) is configured.

### Debugging with `verify_search.py`

If you encounter issues or want to test if the setup is working:

1. Run `python verify_search.py`.
2. This script will execute several test queries (e.g., "python tutorial", mixed English/Chinese).
3. Watch the browser window to see if it opens and loads Google results.
4. Check the console output for success messages or error logs.

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

- Search Google using scrapling and return structured results (title,
  link, snippet)
- Invoke when u
- 触发关键词: return, using, browser, search, scrapling, google, free_google_search_with_browser,
  free

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

### Q1: 如何开始使用Free Google Search W？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Free Google Search W有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
