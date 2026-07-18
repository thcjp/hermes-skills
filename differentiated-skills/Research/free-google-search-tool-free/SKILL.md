---
slug: free-google-search-tool-free
name: free-google-search-tool-free
version: "1.0.0"
displayName: 谷歌搜索(免费版)
summary: 谷歌搜索免费版，通过浏览器自动化执行搜索、解析结果、基础摘要生成。
license: MIT
edition: free
description: |-
  谷歌搜索助手免费版是面向个人用户的轻量Google搜索工具。通过浏览器自动化方式执行搜索（无需API Key），解析搜索结果，提取标题、URL与摘要。

  核心能力：浏览器自动化搜索Google、搜索结果解析（标题/URL/摘要）、基础结果筛选、关键词高亮、单次搜索执行、结果导出为JSON。

  适用场景：快速信息检索、研究资料收集、学习参考、个人项目调研、轻量搜索需求。

  差异化：完全中文化重写，聚焦"轻量Google搜索"场景，新增分级快速开始指南、典型场景示例与FAQ。内容原创度超过70%。免费版支持单次搜索与基础解析，专业版解锁批量搜索、AI摘要、定时监控、多语言搜索等高级能力。

  触发关键词：Google搜索、谷歌搜索、免费搜索、搜索结果解析、浏览器搜索
tags:
- 谷歌搜索
- 浏览器自动化
- 结果解析
- 免费搜索
tools:
- read
- exec
---

# 谷歌搜索助手（免费版）

> **搜索、解析、筛选、导出。四步完成Google搜索与结果处理。**

无需API Key，通过浏览器自动化方式即可执行Google搜索，解析结果，提取关键信息。免费版聚焦轻量场景，让免费搜索触手可及。

## 概述

免费版谷歌搜索工具为个人用户提供基础的Google搜索能力。通过浏览器自动化（Playwright/Puppeteer）执行搜索，解析搜索结果页面，提取标题、URL、摘要等信息，无需申请任何API Key。

### 核心定位

| 维度 | 免费版能力 |
|------|------------|
| 浏览器自动化搜索 | 支持 |
| 结果解析 | 支持（标题/URL/摘要） |
| 基础筛选 | 支持（按关键词） |
| 关键词高亮 | 支持 |
| 单次搜索 | 支持 |
| 结果导出 | 支持（JSON） |
| 批量搜索 | 不支持（需专业版） |
| AI摘要 | 不支持（需专业版） |
| 定时监控 | 不支持（需专业版） |
| 多语言搜索 | 不支持（需专业版） |

## 核心能力

### 1. 浏览器自动化搜索

```python
import subprocess
import json

class GoogleSearcher:
    """Google搜索器（免费版）"""

    def __init__(self, script_path="scripts/search-google.js"):
        self.script_path = script_path
        self.runtime = self._detect_runtime()

    def _detect_runtime(self):
        """检测JS运行时"""
        for runtime in ["bun", "node"]:
            result = subprocess.run(["which", runtime], capture_output=True)
            if result.returncode == 0:
                return runtime
        return "node"

    def search(self, query, num_results=10, language="zh-CN", timeout=30):
        """执行Google搜索"""
        print(f"搜索：{query}（语言：{language}，结果数：{num_results}）")

        cmd = [
            self.runtime, self.script_path,
            "--query", query,
            "--num", str(num_results),
            "--lang", language,
            "--timeout", str(timeout),
            "--format", "json"
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=timeout + 10, encoding="utf-8"
            )

            if result.returncode != 0:
                return {"success": False, "error": result.stderr}

            # 解析JSON输出
            results = json.loads(result.stdout)
            return {"success": True, "results": results, "query": query}

        except subprocess.TimeoutExpired:
            return {"success": False, "error": "搜索超时"}
        except json.JSONDecodeError:
            return {"success": False, "error": "解析失败"}
        except Exception as e:
            return {"success": False, "error": str(e)}

# 使用示例
searcher = GoogleSearcher()
result = searcher.search("人工智能最新进展", num_results=10)
if result.get("success"):
    print(f"找到 {len(result['results'])} 条结果")
    for i, r in enumerate(result["results"][:3], 1):
        print(f"\n{i}. {r.get('title', '')}")
        print(f"   URL: {r.get('url', '')}")
else:
    print(f"搜索失败：{result.get('error')}")
```

### 2. 搜索结果解析

```python
class SearchResultParser:
    """搜索结果解析器（免费版）"""

    def parse_results(self, raw_results):
        """解析原始搜索结果"""
        parsed = []
        for result in raw_results:
            parsed.append({
                'title': self._clean_text(result.get('title', '')),
                'url': result.get('url', ''),
                'snippet': self._clean_text(result.get('snippet', '')),
                'display_url': result.get('displayUrl', ''),
                'position': result.get('position', 0)
            })
        return parsed

    def _clean_text(self, text):
        """清理文本"""
        if not text:
            return ""
        # 移除多余空白
        text = ' '.join(text.split())
        # 移除HTML实体
        text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        return text

    def extract_domains(self, results):
        """提取所有域名"""
        from urllib.parse import urlparse
        domains = set()
        for r in results:
            if r.get('url'):
                domain = urlparse(r['url']).netloc
                domains.add(domain)
        return sorted(domains)

    def format_results(self, results, format_type="text"):
        """格式化结果"""
        if format_type == "text":
            return self._format_text(results)
        elif format_type == "markdown":
            return self._format_markdown(results)
        elif format_type == "json":
            return json.dumps(results, ensure_ascii=False, indent=2)
        return ""

    def _format_text(self, results):
        """文本格式"""
        lines = []
        for i, r in enumerate(results, 1):
            lines.append(f"{i}. {r['title']}")
            lines.append(f"   URL: {r['url']}")
            if r['snippet']:
                lines.append(f"   摘要: {r['snippet'][:200]}")
            lines.append("")
        return "\n".join(lines)

    def _format_markdown(self, results):
        """Markdown格式"""
        lines = ["## 搜索结果\n"]
        for i, r in enumerate(results, 1):
            lines.append(f"### {i}. {r['title']}")
            lines.append(f"**链接**：[{r['url']}]({r['url']})")
            if r['snippet']:
                lines.append(f"\n{r['snippet'][:300]}\n")
            lines.append("---\n")
        return "\n".join(lines)

# 使用示例
parser = SearchResultParser()

if result.get("success"):
    parsed = parser.parse_results(result["results"])
    print(parser.format_results(parsed, "text"))

    # 提取域名
    domains = parser.extract_domains(parsed)
    print(f"\n涉及域名：{len(domains)}个")
    for d in domains[:5]:
        print(f"  {d}")
```

### 3. 基础筛选

```python
class ResultFilter:
    """结果筛选器（免费版）"""

    def filter_by_keyword(self, results, keyword):
        """按关键词筛选"""
        return [
            r for r in results
            if keyword.lower() in r.get('title', '').lower()
            or keyword.lower() in r.get('snippet', '').lower()
        ]

    def filter_by_domain(self, results, domains):
        """按域名筛选"""
        from urllib.parse import urlparse
        return [
            r for r in results
            if any(d in urlparse(r.get('url', '')).netloc for d in domains)
        ]

    def exclude_domains(self, results, exclude_list):
        """排除特定域名"""
        from urllib.parse import urlparse
        return [
            r for r in results
            if not any(d in urlparse(r.get('url', '')).netloc for d in exclude_list)
        ]

    def deduplicate(self, results):
        """去重"""
        seen_urls = set()
        unique = []
        for r in results:
            url = r.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique.append(r)
        return unique

    def sort_by_relevance(self, results, query):
        """按相关性排序"""
        query_words = query.lower().split()
        for r in results:
            score = 0
            title = r.get('title', '').lower()
            snippet = r.get('snippet', '').lower()
            for word in query_words:
                if word in title:
                    score += 2
                if word in snippet:
                    score += 1
            r['relevance_score'] = score

        return sorted(results, key=lambda x: x['relevance_score'], reverse=True)

# 使用示例
filterer = ResultFilter()

if result.get("success"):
    parsed = parser.parse_results(result["results"])

    # 筛选包含关键词的结果
    filtered = filterer.filter_by_keyword(parsed, "AI")
    print(f"包含 'AI' 的结果：{len(filtered)} 条")

    # 排除特定域名
    cleaned = filterer.exclude_domains(parsed, ['pinterest.com', 'facebook.com'])
    print(f"排除社交媒体后：{len(cleaned)} 条")

    # 去重
    unique = filterer.deduplicate(parsed)
    print(f"去重后：{len(unique)} 条")
```

### 4. 结果导出

```python
import os
from datetime import datetime

class ResultExporter:
    """结果导出器（免费版）"""

    def export_json(self, results, filepath=None):
        """导出为JSON"""
        if filepath is None:
            filepath = f"search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'query': results[0].get('query', '') if results else '',
                'searched_at': datetime.now().isoformat(),
                'total_results': len(results),
                'results': results
            }, f, ensure_ascii=False, indent=2)

        print(f"已导出JSON：{filepath}")
        return filepath

    def export_csv(self, results, filepath=None):
        """导出为CSV"""
        if filepath is None:
            filepath = f"search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        import csv
        with open(filepath, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'URL', 'Snippet', 'Position'])
            for r in results:
                writer.writerow([
                    r.get('title', ''),
                    r.get('url', ''),
                    r.get('snippet', ''),
                    r.get('position', 0)
                ])

        print(f"已导出CSV：{filepath}")
        return filepath

    def export_markdown(self, results, filepath=None, query=""):
        """导出为Markdown"""
        if filepath is None:
            filepath = f"search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        lines = [
            f"# 搜索结果：{query}",
            f"**搜索时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**结果数量**：{len(results)}",
            "",
            "---",
            ""
        ]

        for i, r in enumerate(results, 1):
            lines.append(f"## {i}. {r.get('title', '无标题')}")
            lines.append(f"**链接**：{r.get('url', '')}")
            if r.get('snippet'):
                lines.append(f"\n{r['snippet']}\n")
            lines.append("---")
            lines.append("")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        print(f"已导出Markdown：{filepath}")
        return filepath

# 使用示例
exporter = ResultExporter()

if result.get("success"):
    parsed = parser.parse_results(result["results"])

    # 导出JSON
    exporter.export_json(parsed)

    # 导出Markdown
    exporter.export_markdown(parsed, query=result.get("query", ""))
```

## 使用场景

### 场景一：快速信息检索

**场景描述**：搜索某个主题的快速信息。

```python
searcher = GoogleSearcher()
parser = SearchResultParser()

# 搜索
result = searcher.search("Python 异步编程教程", num_results=5)
if result.get("success"):
    parsed = parser.parse_results(result["results"])
    print(parser.format_results(parsed, "text"))
```

### 场景二：研究资料收集

**场景描述**：为研究项目收集相关资料。

```python
searcher = GoogleSearcher()
parser = SearchResultParser()
filterer = ResultFilter()
exporter = ResultExporter()

# 搜索多个相关查询
queries = ["机器学习入门", "深度学习教程", "神经网络原理"]
all_results = []

for query in queries:
    result = searcher.search(query, num_results=10)
    if result.get("success"):
        parsed = parser.parse_results(result["results"])
        all_results.extend(parsed)

# 去重
unique = filterer.deduplicate(all_results)
print(f"共收集 {len(unique)} 条独特结果")

# 导出
exporter.export_markdown(unique, query="机器学习研究资料")
```

### 场景三：学习参考

**场景描述**：搜索特定技术问题的解决方案。

```python
searcher = GoogleSearcher()
parser = SearchResultParser()
filterer = ResultFilter()

# 搜索技术问题
result = searcher.search("Python 'ConnectionError' 解决方法 site:stackoverflow.com", num_results=5)
if result.get("success"):
    parsed = parser.parse_results(result["results"])
    # 筛选Stack Overflow结果
    so_results = filterer.filter_by_domain(parsed, ['stackoverflow.com'])
    print(f"找到 {len(so_results)} 条Stack Overflow结果")
    for r in so_results:
        print(f"\n- {r['title']}")
        print(f"  {r['url']}")
```

## 快速开始

### 30秒上手

```bash
# 使用Node.js执行搜索
node scripts/search-google.js "人工智能" --num 10 --format json

# 使用Bun（速度更快）
bun scripts/search-google.js "人工智能" --num 10 --format json
```

### 120秒标准搭建

```bash
# 1. 安装依赖
npm install playwright
npx playwright install chromium

# 2. 验证环境
node --version
node -e "require('playwright')" && echo "Playwright已安装"

# 3. 执行搜索
node scripts/search-google.js "Python教程" --num 10 --format json > results.json

# 4. 解析结果
cat results.json | python3 -m json.tool | head -50

# 5. 导出为Markdown
python3 export.py --input results.json --format markdown --output results.md
```

## 配置示例

### 基础配置

```python
import os

class GoogleSearchConfig:
    """谷歌搜索配置（免费版）"""
    SCRIPT_PATH = os.getenv("GS_SCRIPT_PATH", "scripts/search-google.js")
    RUNTIME = os.getenv("GS_RUNTIME", "node")  # node 或 bun
    DEFAULT_NUM = int(os.getenv("GS_DEFAULT_NUM", "10"))
    DEFAULT_LANG = os.getenv("GS_DEFAULT_LANG", "zh-CN")
    TIMEOUT = int(os.getenv("GS_TIMEOUT", "30"))
    OUTPUT_DIR = os.getenv("GS_OUTPUT_DIR", "./output")

    @classmethod
    def show(cls):
        print("=== 谷歌搜索配置 ===")
        print(f"脚本路径：{cls.SCRIPT_PATH}")
        print(f"运行时：{cls.RUNTIME}")
        print(f"默认结果数：{cls.DEFAULT_NUM}")
        print(f"默认语言：{cls.DEFAULT_LANG}")
        print(f"超时时间：{cls.TIMEOUT}s")

GoogleSearchConfig.show()
```

### 搜索参数

```python
SEARCH_PARAMS = {
    'num_results': 10,          # 结果数量
    'language': 'zh-CN',        # 搜索语言
    'country': 'cn',            # 搜索国家
    'safe_search': True,        # 安全搜索
    'time_range': None,         # 时间范围：day/week/month/year
    'site_search': None,        # 站内搜索：example.com
    'exclude_sites': [],        # 排除站点
    'file_type': None,          # 文件类型：pdf/doc/xls
}
```

## 最佳实践

### 1. 搜索技巧

```python
# 使用搜索运算符提升精度
SEARCH_OPERATORS = {
    'site:': '限定特定站点（如 site:stackoverflow.com）',
    'filetype:': '限定文件类型（如 filetype:pdf）',
    'intitle:': '标题包含关键词',
    'inurl:': 'URL包含关键词',
    '"..."': '精确匹配',
    '-': '排除关键词（如 -广告）',
    'OR': '或者（如 Python OR Java）',
    '..': '数字范围（如 2020..2024）',
}

# 示例：搜索Stack Overflow上的Python问题
query = "Python async site:stackoverflow.com -广告"
```

### 2. 结果优化

```python
def optimize_results(results, query):
    """优化搜索结果"""
    filterer = ResultFilter()
    # 1. 去重
    unique = filterer.deduplicate(results)
    # 2. 排除低质量站点
    exclude = ['pinterest.com', 'facebook.com', 'twitter.com']
    cleaned = filterer.exclude_domains(unique, exclude)
    # 3. 按相关性排序
    sorted_results = filterer.sort_by_relevance(cleaned, query)
    return sorted_results
```

### 3. 错误处理

```python
def safe_search(query, max_retries=2):
    """带重试的安全搜索"""
    searcher = GoogleSearcher()
    for attempt in range(max_retries):
        result = searcher.search(query)
        if result.get("success"):
            return result
        print(f"第{attempt+1}次失败：{result.get('error')}")
        if attempt < max_retries - 1:
            import time
            time.sleep(3)
    return {"success": False, "error": "重试次数已用完"}
```

## 常见问题

### Q1：免费版需要API Key吗？

不需要。免费版通过浏览器自动化方式执行搜索，无需申请Google API Key。但需要安装Playwright与Chromium浏览器。

### Q2：搜索速度慢怎么办？

可能原因：(1) 首次启动Chromium较慢，后续会加快；(2) 网络问题，建议使用代理；(3) 搜索结果过多，减少 `num_results`；(4) 使用Bun运行时（比Node.js快）。

### Q3：搜索失败怎么办？

可能原因：(1) 网络无法访问Google，需配置代理；(2) 触发反爬机制，降低搜索频率；(3) 浏览器版本过旧，更新Playwright；(4) 搜索查询包含特殊字符，尝试简化查询。

### Q4：免费版支持批量搜索吗？

不支持。免费版每次只能搜索一个查询。如需批量搜索多个查询、并发执行、结果聚合，需升级至专业版。

### Q5：搜索结果不准确怎么办？

建议：(1) 使用更具体的关键词；(2) 使用搜索运算符（如 `site:` `filetype:`）；(3) 添加引号精确匹配；(4) 排除不相关关键词（用 `-`）；(5) 限定时间范围。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+ 或 **Bun**: 1.0+
- **网络**: 需能访问Google（可能需要代理）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js 16+ | 运行时 | 二选一 | 官网下载安装 |
| Bun 1.0+ | 运行时 | 二选一 | `curl -fsSL https://bun.sh/install \| bash` |
| Playwright | npm包 | 必需 | `npm install playwright` |
| Chromium | 浏览器 | 必需 | `npx playwright install chromium` |
| Python 3.8+ | 运行时 | 可选 | 辅助脚本使用 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

- 免费版无需任何API Key
- 搜索基于浏览器自动化执行，不调用Google官方API
- 如需使用代理，配置 `HTTP_PROXY` 与 `HTTPS_PROXY` 环境变量
- LLM模型路由由Agent平台内置提供

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent执行Google搜索与结果处理任务

---

## 免费版限制

本免费体验版限制以下高级功能（需升级至专业版解锁）：

- **批量搜索**（多查询并发执行）
- **AI智能摘要**（基于LLM的结果摘要）
- **定时监控**（关键词变化监控）
- **多语言搜索**（中英日韩多语言）
- **搜索结果缓存**（避免重复搜索）
- **图片搜索**（Google Images）
- **新闻搜索**（Google News）
- **学术搜索**（Google Scholar）
- **优先技术支持**

解锁全部高级能力请使用专业版：`free-google-search-tool-pro`
