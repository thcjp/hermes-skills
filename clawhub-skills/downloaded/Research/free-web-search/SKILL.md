---
slug: free-web-search
name: free-web-search
version: "8.1.0"
displayName: Free Web Search
summary: 基于 Bing 国内版 / DuckDuckGo 的联网搜索工具，中文环境优化，可按需抓取目标网页正文，返回结构化结果。仅在用户明确请求联网搜索时调用。
license: MIT-0
description: |-
  基于 Bing 国内版 / DuckDuckGo 的联网搜索工具，中文环境优化，可按需抓取目标网页正文，返回结构化结果。仅在用户明确请求联网搜索时调用。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Research
tools:
  - - read
- exec
---

# Free Web Search

基于 Playwright 的 Bing 国内版 / DuckDuckGo 搜索工具。专注于**搜索 + 可选正文抓取**两件事，无副作用。

## 触发方式

仅在用户**明确请求联网搜索**时调用，例如：

* "用 free-web-search 查一下 Python 异步教程"
* "联网搜索 2026 年中国大型邮轮"
* "web search: latest LLM benchmarks"

trigger_keywords 已经收窄到只识别 `free-web-search`、`联网搜索`、`网页搜索`、`web search`，不会因为消息里出现"新闻"、"最新消息"这些常见词就把对话内容发到外部搜索引擎。

## 核心能力

* **中文环境优化**：默认 `mkt=zh-CN`，结果以中文为主
* **可选全文抓取**：通过 `--full=N` 抓取前 N 条结果正文（默认 0 不抓取）
* **智能路由**：基于 IP 地理位置自动选择 Bing CN（国内）或 DuckDuckGo（国外），单引擎失败时自动兜底
* **Headless 浏览器**：服务器/容器可用，仅开 `--no-sandbox`、`--disable-gpu`、`--disable-dev-shm-usage` 三个标准稳定性参数

## 安装

**所有依赖必须在使用前手动安装。脚本运行时不会自动安装任何 npm/pip 包，也不会修改宿主环境。**

### 依赖说明

| 依赖 | 用途 | 备注 |
| --- | --- | --- |
| Python 3.8+ | 运行时 | — |
| playwright | 浏览器自动化 | `pip install playwright` |
| Chromium | Playwright 浏览器引擎 | `playwright install chromium`（约 150 MB） |

### 一键安装

```bash
bash scripts/setup.sh
```

### 手动安装

```bash
pip install playwright
playwright install chromium
```

## 示例

```bash
python scripts/web_search.py "Python 异步编程 最佳实践 2026" --max=10

python scripts/web_search.py "中国大型邮轮 花城号 出坞" --full=3

python scripts/web_search.py "技术教程" --region=cn    # 强制 Bing CN
python scripts/web_search.py "技术教程" --region=intl  # 强制 DuckDuckGo
```

## 搜索 Query 优化建议

搜索效果取决于 Query 是否合理：

1. **简洁精准**：2-5 个核心词组合，避免长句、反问句
2. **限定明确**：需要时效性/地区内容时加上对应限定词
3. **格式正确**：中文关键词 + 数字/英文限定词

| 场景 | 推荐 | 不推荐 |
| --- | --- | --- |
| 时效新闻 | `2026年04月 美伊局势` | `最近美伊之间发生了什么` |
| 技术教程 | `Python 异步编程 2026` | `我想学 Python 异步编程` |
| 本地内容 | `广东东莞 今日天气` | `东莞今天天气怎么样啊` |
| 官方信息 | `华为云 ModelArts 文档` | `华为云那个 ModelArts 怎么看` |

## 参数说明

| 参数 | 类型 | 默认 | 范围 | 说明 |
| --- | --- | --- | --- | --- |
| `query` | 字符串 | — | 必填 | 搜索关键词 |
| `--max` | 整数 | 10 | 1-20 | 最多返回条数 |
| `--full` | 整数 | 0 | 0-5 | 抓取前 N 条全文 |
| `--region` | 字符串 | auto | auto/cn/intl | 区域覆盖（auto = IP 探测，cn = Bing CN，intl = DuckDuckGo） |

## 隐私与网络说明

启用此工具会产生以下出站请求，使用前请确认你的环境允许：

| 目的 | 端点 | 数据 |
| --- | --- | --- |
| IP 地理位置探测 | `myip.ipip.net`, `cip.cc`, `ipinfo.io/json`, `ipapi.co/json` | 你的 IP、UA |
| Bing 搜索（国内 IP 默认） | `cn.bing.com` | 你的 query 文本、IP、UA |
| DuckDuckGo 搜索（国外 IP 默认） | `duckduckgo.com` | 你的 query 文本、IP、UA |
| 抓取目标页（仅当 `--full > 0`） | 各搜索结果对应的站点 | 你的 IP、UA、Referer |

工具本身：

* 不收集 telemetry、不写日志到第三方
* 不在运行时安装 pip 包、不修改宿主目录之外的文件
* 浏览器 cookie 仅在当前 Playwright 上下文内使用，进程退出即销毁

如果你不希望抓取目标页，把 `--full` 留在默认值 `0` 即可，工具只会访问搜索引擎和 IP 探测服务。

## 与 free-web-search-js 的区别

**free-web-search**（本工具）：

* 轻量级 Python 实现，无需 Node.js
* 依赖 Playwright + Chromium（~150 MB）
* 适合简单查询、快速结果
* 不支持复杂 JS 渲染的单页应用

**free-web-search-js**：

* 基于 Puppeteer 的 Node.js 实现
* 完整浏览器环境，支持重度 JS 渲染
* 适合需要完整 DOM 交互的场景

选择建议：优先使用本工具（free-web-search），仅在遇到 JS 渲染问题时切换到 free-web-search-js。

## 测试

当前版本无自动化测试覆盖。欢迎贡献测试用例。

## 常见问题

### 搜索返回空结果

* 检查网络（Bing 国内版偶发限流，工具已内置 3s 节流和指数退避）
* 如果在国外但被误判为国内，试 `--region=intl` 强制 DuckDuckGo
* 检查 query 是否过于冗长

### 浏览器启动失败

脚本不会自动安装。手动跑：

```bash
pip install playwright
playwright install chromium
```

### 全文抓取失败

* 部分站点 JS 渲染较重或返回非 HTML，工具不会做特殊处理
* 考虑使用 free-web-search-js（基于 Puppeteer，JS 渲染能力更强）

### IP 探测失败或被误判

* 工具依次探测 4 个公开 IP 服务（myip.ipip.net、cip.cc、ipinfo.io、ipapi.co）
* 如果所有探测失败，默认使用 DuckDuckGo（国外）
* 可通过 `--region=cn` 或 `--region=intl` 手动覆盖

## 已知限制

* **VPN/代理**：可能影响 Bing 国内版的可达性
* **headless**：默认 `headless=True`，无 GUI 依赖
* **DDG 国内不可达**：DuckDuckGo 在中国大陆需要科学上网，超时单次 10s 快速失败
* **抓取上限**：`--full` 最多 5 条，单页正文截断到 8000 字

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

**所有依赖必须在使用前手动安装。脚本运行时不会自动安装任何 npm/pip 包，也不会修改宿主环境。**

### 依赖说明

| 依赖 | 用途 | 备注 |
| --- | --- | --- |
| Python 3.8+ | 运行时 | — |
| playwright | 浏览器自动化 | `pip install playwright` |
| Chromium | Playwright 浏览器引擎 | `playwright install chromium`（约 150 MB） |

### 一键安装

```bash
bash scripts/setup.sh
```

### 手动安装

```bash
pip install playwright
playwright install chromium
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
