---
slug: free-google-search-with-browser
name: free-google-search-with-browser
version: "0.0.1"
displayName: Free Google Search W
summary: "使用scrapling搜索Google并返回结构化结果(标题、链接、摘要),免费搜索方案"
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

---
## 边界条件与限制

### 输入限制
- **查询长度**: 输入查询字符串的长度不应超过特定限制，例如100个字符，以避免过度加载服务器资源。
- **特殊字符**: 输入中不应包含特殊字符或控制字符，这些可能导致解析错误或搜索结果不准确。
- **频率限制**: 搜索请求的频率不应过高，以防止触发Google的反爬虫机制。

### 性能边界
- **响应时间**: 搜索请求的响应时间不应超过5秒，以确保用户体验。
- **结果数量**: 搜索结果的数量通常限制在10-20个，以提供足够的信息而不会过于冗长。

### 兼容性约束
- **浏览器支持**: 技能可能不支持所有类型的浏览器，尤其是较旧的浏览器版本。
- **操作系统**: 技能可能在某些操作系统（如Windows Server）上运行不佳，因为这些系统可能不支持图形用户界面。

### 资源限制
- **内存使用**: 技能运行时，内存使用不应超过系统可用内存的一定比例，例如50%，以防止资源耗尽。
- **并发请求**: 同时处理的并发搜索请求不应超过一定数量，例如5个，以避免过载服务器。

### 地理限制
- **地理位置**: 技能可能不适用于所有地理位置，特别是那些有严格的网络审查或访问限制的地区。

### 模型能力
- **语言支持**: 技能可能不支持所有语言的搜索查询，尤其是那些在Google上没有广泛支持的稀有语言。
- **准确性**: 技能返回的搜索结果的准确性受限于底层模型的性能和Google搜索算法的变化。

### 依赖性
- **LLM环境**: 技能依赖于LLM支持，因此在没有LLM环境的平台上无法使用。

### 其他限制
- **法律遵从性**: 技能的使用必须遵守适用的法律和法规，包括但不限于版权法和隐私法。
- **道德使用**: 技能的使用不得用于任何非法或道德上可疑的活动，如数据挖掘、垃圾邮件发送等。

