---
slug: multi-search-tool-pro
name: multi-search-tool-pro
version: "1.0.0"
displayName: 多搜索引擎工具专业版
summary: 集成20+全球搜索引擎，支持批量搜索、结果自动聚合去重与企业级API集成
license: MIT
edition: pro
description: |-
  多搜索引擎工具专业版，集成20+全球搜索引擎，支持批量关键词搜索、结果自动抓取聚合、去重排序与企业级API集成。

  核心能力:
  - 集成20+搜索引擎（国内10个 + 海外10+个）
  - 批量关键词并行搜索
  - 搜索结果自动抓取、去重与智能排序
  - 搜索历史记录与趋势分析
  - 自定义搜索引擎编排与路由策略
  - REST API 集成与自动化工作流

  适用场景:
  - 企业市场调研与竞品分析
  - 研究机构多源数据采集
  - SEO监控与品牌舆情追踪
  - 跨境电商市场情报收集

  差异化:
  - PRO 版本与免费版完全兼容，支持平滑升级
  - 新增海外搜索引擎与批量搜索能力
  - 支持结果聚合去重与智能排序
  - 提供API集成与自动化工作流支持

  触发关键词: 全球搜索, 批量搜索, 搜索聚合, 海外搜索, Google搜索, 去重排序, 搜索API, multi search pro
tags:
- 搜索
- 研究
- 企业级
- 全球搜索
- 信息聚合
tools:
- read
- exec
---

# 多搜索引擎工具（专业版）

## 概述

多搜索引擎工具专业版在免费版 10 个国内搜索引擎的基础上，新增 10+ 个海外搜索引擎，并提供批量关键词搜索、结果自动抓取聚合、去重排序、搜索历史记录与 REST API 集成等企业级能力，满足专业研究与商业情报收集场景的深度需求。

PRO 版本与免费版完全兼容，用户可随时从免费版平滑升级，原有搜索引擎配置均可无缝迁移。

## 核心能力

### 能力矩阵

| 能力项 | 免费版 | PRO 版本 |
|:-------|:-------|:---------|
| 搜索引擎数量 | 10个（国内） | 20+个（国内+海外） |
| 海外引擎 | 部分（必应国际） | 完整（Google、DuckDuckGo等） |
| 批量搜索 | 不支持 | 支持批量关键词并行 |
| 结果抓取 | 仅链接 | 自动抓取网页内容 |
| 去重排序 | 不支持 | 智能去重 + 相关度排序 |
| 搜索历史 | 不支持 | 完整历史记录与趋势 |
| 自定义路由 | 不支持 | 按场景智能路由 |
| API 集成 | 不支持 | REST API + Webhook |
| 导出格式 | Markdown | Markdown/JSON/CSV/PDF |

### PRO 专属搜索引擎

```text
[PRO] Google Search        - 全球最大搜索引擎
[PRO] DuckDuckGo           - 隐私优先搜索
[PRO] Brave Search         - 独立索引引擎
[PRO] Startpage            - 隐私代理搜索
[PRO] Yandex               - 俄罗斯搜索引擎
[PRO] Naver                - 韩国搜索引擎
[PRO] Yahoo Search         - 雅虎搜索
[PRO] Ask.com              - 问答式搜索
[PRO] Baidu Scholar        - 百度学术
[PRO] Google Scholar       - 谷歌学术
[PRO] Semantic Scholar     - 语义学术搜索
[PRO] PubMed               - 医学文献搜索
```

## 使用场景

### 场景一：企业竞品调研

市场部门需要全面调研竞争对手的线上信息，覆盖国内外多个搜索引擎。

```text
用户：帮我调研"AI编程助手"领域的主要竞品，覆盖国内外搜索引擎

Agent 执行流程：
1. 生成多组关键词（中英文）
2. 并行查询 Google、百度、必应、DuckDuckGo
3. 自动抓取搜索结果页面
4. 去重并按相关度排序
5. 生成竞品调研报告
```

示例输出：

```markdown
## 竞品调研报告："AI编程助手"

### 搜索引擎覆盖
| 引擎 | 结果数 | 去重后 | 高相关 |
|:-----|:-------|:-------|:-------|
| Google | 45 | 32 | 18 |
| 百度 | 38 | 25 | 12 |
| 必应 | 30 | 22 | 10 |
| DuckDuckGo | 28 | 20 | 8 |
| **合计** | **141** | **68** | **35** |

### 核心竞品清单（去重排序后）
1. **GitHub Copilot** - 出现频率: 4/4引擎
   - 来源：Google、百度、必应、DuckDuckGo
   - 摘要：GitHub与OpenAI合作的AI编程助手...

2. **Cursor** - 出现频率: 4/4引擎
   - 来源：Google、百度、必应、DuckDuckGo
   - 摘要：AI驱动的代码编辑器...
```

### 场景二：批量关键词搜索

SEO 团队需要监控大量关键词在多个搜索引擎中的排名表现。

```python
# batch_search.py - 批量搜索脚本
import json
from datetime import datetime

class BatchSearcher:
    def __init__(self, config_path="~/multi-search-pro/config.yaml"):
        self.engines = ["google", "baidu", "bing", "duckduckgo"]
        self.keywords = []

    def load_keywords(self, file_path):
        """加载批量关键词"""
        with open(file_path, 'r', encoding='utf-8') as f:
            self.keywords = [line.strip() for line in f if line.strip()]

    def batch_search(self):
        """执行批量搜索"""
        results = {}
        for kw in self.keywords:
            results[kw] = {}
            for engine in self.engines:
                results[kw][engine] = self._search(engine, kw)
        return results

    def generate_report(self, results):
        """生成SEO监控报告"""
        report = {
            "date": datetime.now().isoformat(),
            "total_keywords": len(self.keywords),
            "engines": self.engines,
            "results": results
        }
        return report
```

### 场景三：学术文献多源检索

研究人员需要从多个学术搜索引擎同时检索文献。

```text
用户：帮我搜索"大语言模型推理优化"的学术论文，覆盖Google Scholar、百度学术、Semantic Scholar

Agent：
1. 在三个学术引擎并行搜索
2. 去重合并结果
3. 按引用数/发表时间排序
4. 生成文献综述清单
5. 导出为BibTeX格式
```

## 快速开始

### 步骤一：初始化 PRO 环境

```bash
# 创建 PRO 版本工作目录
mkdir -p ~/multi-search-pro/{config,history,reports,exports}

# 初始化配置文件
cat > ~/multi-search-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

engines:
  domestic:
    - baidu
    - bing_cn
    - bing_int
    - "360"
    - sogou
    - weixin
    - toutiao
    - jisilu
    - ecosia
    - wolframalpha
  international:
    - google
    - duckduckgo
    - brave
    - startpage
    - yandex
    - naver
    - yahoo
    - ask
  academic:
    - baidu_scholar
    - google_scholar
    - semantic_scholar
    - pubmed

routing:
  default_group: [baidu, bing_cn, google]
  tech: [google, bing_int, baidu, duckduckgo]
  academic: [google_scholar, semantic_scholar, baidu_scholar]
  social: [weixin, sogou, toutiao]

limits:
  max_keywords_per_batch: 50
  max_engines_per_query: 5
  timeout_seconds: 60
  concurrency: 10

history:
  enabled: true
  retention_days: 90
  path: "~/multi-search-pro/history"

export:
  formats: ["markdown", "json", "csv", "pdf"]
  path: "~/multi-search-pro/exports"
EOF
```

### 步骤二：从免费版迁移

```bash
# 迁移免费版配置
if [ -f ~/multi-search/config.yaml ]; then
    cp ~/multi-search/config.yaml ~/multi-search-pro/config/free_config.yaml.bak
    echo "免费版配置已备份，PRO版本将自动合并引擎列表"
fi
```

### 步骤三：执行首次批量搜索

```text
用户：执行批量搜索，关键词列表见 ~/keywords.txt

Agent：
1. 读取关键词文件
2. 按路由策略分配搜索引擎
3. 并行执行搜索
4. 去重排序
5. 生成报告并保存至 ~/multi-search-pro/reports/
```

## 配置示例

### 智能路由策略

```yaml
# routing.yaml - 智能路由配置
routing_rules:
  - name: 技术文档搜索
    condition:
      keywords_match: ["API", "SDK", "文档", "tutorial", "文档"]
    engines: [google, bing_int, baidu, duckduckgo]
    priority: relevance

  - name: 学术文献搜索
    condition:
      keywords_match: ["论文", "paper", "research", "研究", "综述"]
    engines: [google_scholar, semantic_scholar, baidu_scholar]
    priority: citations

  - name: 中文资讯搜索
    condition:
      keywords_match: ["新闻", "资讯", "动态", "最新"]
    engines: [baidu, toutiao, sogou]
    priority: recency

  - name: 社交媒体搜索
    condition:
      keywords_match: ["公众号", "微博", "知乎", "小红书"]
    engines: [weixin, sogou, baidu]
    priority: engagement
```

### 去重与排序算法

```python
# dedup.py - 搜索结果去重与排序
from urllib.parse import urlparse
from difflib import SequenceMatcher

class ResultAggregator:
    def __init__(self):
        self.results = []

    def add_results(self, engine, items):
        for item in items:
            item['engine'] = engine
            self.results.append(item)

    def deduplicate(self, threshold=0.85):
        """基于URL域名和标题相似度去重"""
        unique = []
        for item in self.results:
            is_dup = False
            for existing in unique:
                # URL域名匹配
                if self._same_domain(item['url'], existing['url']):
                    # 标题相似度
                    ratio = SequenceMatcher(
                        None, item['title'], existing['title']
                    ).ratio()
                    if ratio > threshold:
                        is_dup = True
                        existing['sources'].append(item['engine'])
                        break
            if not is_dup:
                item['sources'] = [item['engine']]
                unique.append(item)
        return unique

    def rank(self, results):
        """多维度排序：相关度 x 引擎数量 x 时效性"""
        for r in results:
            score = (
                r.get('relevance', 0) * 0.4 +
                len(r.get('sources', [])) * 0.3 +
                r.get('recency_score', 0) * 0.3
            )
            r['rank_score'] = score
        return sorted(results, key=lambda x: x['rank_score'], reverse=True)

    def _same_domain(self, url1, url2):
        return urlparse(url1).netloc == urlparse(url2).netloc
```

### REST API 集成

```python
# api_server.py - PRO 版本 API 服务
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Multi Search Tool PRO API")

class SearchRequest(BaseModel):
    keywords: list[str]
    engines: list[str] = []
    max_results: int = 10
    deduplicate: bool = True
    export_format: str = "json"

@app.post("/v1/search")
async def batch_search(request: SearchRequest):
    """批量搜索接口"""
    results = await execute_batch_search(
        keywords=request.keywords,
        engines=request.engines,
        max_results=request.max_results
    )
    if request.deduplicate:
        results = deduplicate_results(results)
    return {"status": "ok", "results": results}

@app.get("/v1/engines")
async def list_engines():
    """列出所有可用搜索引擎"""
    return {"domestic": [...], "international": [...], "academic": [...]}

@app.get("/v1/history")
async def get_history(days: int = 7):
    """获取搜索历史"""
    return {"history": load_history(days)}
```

## 最佳实践

### 1. 按场景配置引擎组合

```python
# 推荐的引擎组合配置
SCENE_PRESETS = {
    "竞品调研": {
        "engines": ["google", "baidu", "bing", "duckduckgo"],
        "max_results": 20,
        "deduplicate": True
    },
    "学术研究": {
        "engines": ["google_scholar", "semantic_scholar", "baidu_scholar"],
        "max_results": 15,
        "deduplicate": True,
        "sort_by": "citations"
    },
    "舆情监控": {
        "engines": ["baidu", "sogou", "toutiao", "weixin"],
        "max_results": 30,
        "deduplicate": True,
        "sort_by": "recency"
    }
}
```

### 2. 利用历史记录进行趋势分析

```text
用户：分析过去30天"AI编程"这个关键词在百度和Google的搜索热度变化

Agent：
1. 调取30天内该关键词的搜索历史
2. 统计每日搜索结果数量变化
3. 分析相关结果的主题趋势
4. 生成趋势分析报告
```

### 3. 设置自动化工作流

```bash
# 每日自动搜索并生成报告
cat > ~/multi-search-pro/daily_search.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d)
python3 ~/multi-search-pro/scripts/batch_search.py \
    --keywords ~/multi-search-pro/keywords/watchlist.txt \
    --engines google baidu bing \
    --output ~/multi-search-pro/reports/daily_${DATE}.json \
    --format json
EOF

# 添加定时任务
(crontab -l 2>/dev/null; echo "0 9 * * * ~/multi-search-pro/daily_search.sh") | crontab -
```

## 常见问题

### Q1：PRO 版本如何访问 Google 等海外搜索引擎？

PRO 版本支持通过代理或 API 方式访问海外搜索引擎。需在配置文件中设置代理参数。

```yaml
# 代理配置
proxy:
  enabled: true
  http_proxy: "http://127.0.0.1:7890"
  https_proxy: "http://127.0.0.1:7890"
```

### Q2：批量搜索最多支持多少个关键词？

PRO 版本单次批量搜索支持最多 50 个关键词，可配置并发数（默认 10）。如需更大批量，建议分批执行或使用 API 接口。

### Q3：去重算法的原理是什么？

PRO 版本采用 URL 域名匹配 + 标题文本相似度（SequenceMatcher）双重去重，默认相似度阈值为 85%，可配置调整。

### Q4：搜索历史保留多久？

默认保留 90 天，可通过配置文件调整 `retention_days` 参数。

### Q5：API 接口支持哪些认证方式？

支持 Bearer Token 认证和 API Key 认证两种方式。

```bash
# API 调用示例
curl -X POST https://api.multi-search.local/v1/search \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords":["AI","LLM"], "engines":["google","baidu"]}'
```

### Q6：免费版配置如何迁移至 PRO 版本？

PRO 版本初始化时会自动检测免费版配置文件并提示迁移，也可手动执行迁移命令。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.10 及以上（推荐 3.12）
- **网络连接**: 稳定的互联网连接，访问海外引擎需配置代理
- **存储空间**: 至少 200MB 用于历史记录与报告存储

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| 网络浏览器 | 工具 | 必需 | Agent 内置浏览器能力 |
| Python 3.10+ | 运行时 | 必需 | 系统包管理器安装 |
| requests | Python 包 | 可选 | `pip install requests` |
| fastapi | Python 包 | 可选 | `pip install fastapi` |
| beautifulsoup4 | Python 包 | 可选 | `pip install beautifulsoup4` |
| 网络代理 | 服务 | 可选 | 用于访问海外搜索引擎 |

### API Key 配置

PRO 版本支持 API 集成，需配置相关密钥：

```bash
# 配置 API 认证
export MULTI_SEARCH_PRO_API_KEY="your_api_key"

# 配置代理（访问海外引擎）
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

# 或写入配置文件
cat > ~/multi-search-pro/.env << 'EOF'
MULTI_SEARCH_PRO_API_KEY=your_api_key
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
EOF
```

### 可用性分类

- **分类**: MD+EXEC+API（Markdown 指令 + 命令行执行 + API 集成）
- **说明**: PRO 版本支持批量搜索、结果聚合去重、历史记录与 REST API 集成
- **适用规模**: 企业市场调研、研究机构数据采集、SEO 监控团队
- **兼容性**: 与 multi-search-tool-free 完全兼容，支持配置迁移与平滑升级
- **支持级别**: 优先技术支持，提供搜索引擎定制接入服务
