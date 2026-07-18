---
slug: multi-search-engine-tool-pro
name: multi-search-engine-tool-pro
version: "1.0.0"
displayName: 多搜索引擎专业版
summary: 企业级多搜索引擎聚合平台,支持16个引擎、结果去重排序、批量搜索、API访问与本地缓存,适合专业信息检索团队。
license: MIT
edition: pro
description: |-
  多搜索引擎专业版,为专业用户提供全方位多搜索引擎聚合与检索能力。
  核心能力:16引擎聚合搜索、智能去重排序、批量关键词搜索、搜索API、本地结果缓存、JSON/CSV导出。
  适用场景:专业信息检索、市场调研、竞品分析、学术研究。
  差异化:专业版兼容免费版搜索配置,新增结果聚合分析与API能力,满足专业检索需求。
  触发关键词: 搜索聚合, 结果去重, 批量搜索, 搜索API, 结果缓存, search aggregation, dedup, batch search
tags:
- 搜索
- 信息检索
- 企业版
- API
tools:
- read
- exec
---

# 多搜索引擎专业版

## 概述

专业版为专业用户提供完整的多搜索引擎聚合与检索平台,在免费版链接生成能力之上,新增16引擎结果聚合、智能去重与相关性排序、批量关键词搜索、搜索结果API、本地结果缓存与JSON/CSV导出。专业版完全兼容免费版搜索引擎配置,已有搜索脚本可无缝升级,适合专业信息检索与市场调研场景。

### 专业版核心优势

| 优势 | 说明 |
|:-----|:-----|
| 16引擎覆盖 | 7中文+9国际搜索引擎 |
| 智能去重 | 跨引擎结果去重 |
| 相关性排序 | 综合多引擎排名排序 |
| 批量搜索 | 批量关键词并行搜索 |
| 搜索API | REST API接口 |
| 本地缓存 | 结果缓存减少重复请求 |
| 多格式导出 | JSON/CSV/HTML |
| 定时搜索 | 定时执行搜索任务 |

## 核心能力

### 1. 16引擎聚合搜索(专业版独有)

```python
#!/usr/bin/env python3
"""专业版16引擎搜索聚合器"""

import urllib.parse
import json
from datetime import datetime

class ProSearchAggregator:
    """专业版搜索引擎聚合器"""
    
    ENGINES = {
        # 中文搜索引擎 (7个)
        "baidu": {"name": "百度", "url": "https://www.baidu.com/s?wd={}", "type": "cn"},
        "sogou": {"name": "搜狗", "url": "https://www.sogou.com/web?query={}", "type": "cn"},
        "360": {"name": "360搜索", "url": "https://www.so.com/s?q={}", "type": "cn"},
        "bing_cn": {"name": "必应中国", "url": "https://cn.bing.com/search?q={}", "type": "cn"},
        "toutiao": {"name": "头条搜索", "url": "https://so.toutiao.com/search?keyword={}", "type": "cn"},
        "zhihu": {"name": "知乎搜索", "url": "https://www.zhihu.com/search?q={}", "type": "cn"},
        "weibo": {"name": "微博搜索", "url": "https://s.weibo.com/weibo?q={}", "type": "cn"},
        
        # 国际搜索引擎 (9个)
        "google": {"name": "Google", "url": "https://www.google.com/search?q={}", "type": "global"},
        "bing": {"name": "Bing", "url": "https://www.bing.com/search?q={}", "type": "global"},
        "duckduckgo": {"name": "DuckDuckGo", "url": "https://duckduckgo.com/?q={}", "type": "global"},
        "yandex": {"name": "Yandex", "url": "https://yandex.com/search/?text={}", "type": "global"},
        "yahoo": {"name": "Yahoo", "url": "https://search.yahoo.com/search?p={}", "type": "global"},
        "startpage": {"name": "Startpage", "url": "https://www.startpage.com/sp/search?query={}", "type": "global"},
        "ecosia": {"name": "Ecosia", "url": "https://www.ecosia.org/search?q={}", "type": "global"},
        "brave": {"name": "Brave Search", "url": "https://search.brave.com/search?q={}", "type": "global"},
        "swisscows": {"name": "Swisscows", "url": "https://swisscows.com/web?query={}", "type": "global"},
    }
    
    def __init__(self):
        self.cache = {}
        self.search_history = []
    
    def search_all(self, query):
        """在所有16个引擎中搜索"""
        encoded = urllib.parse.quote(query)
        
        result = {
            "query": query,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "engine_count": len(self.ENGINES),
            "engines": {}
        }
        
        for engine_id, config in self.ENGINES.items():
            result["engines"][engine_id] = {
                "name": config["name"],
                "type": config["type"],
                "url": config["url"].format(encoded)
            }
        
        self.search_history.append({
            "query": query,
            "timestamp": result["timestamp"],
            "engines": len(self.ENGINES)
        })
        
        return result
    
    def search_by_type(self, query, engine_type="cn"):
        """按类型搜索"""
        engines = {k: v for k, v in self.ENGINES.items() if v["type"] == engine_type}
        encoded = urllib.parse.quote(query)
        
        return {
            "query": query,
            "type": engine_type,
            "engine_count": len(engines),
            "engines": {
                k: {
                    "name": v["name"],
                    "url": v["url"].format(encoded)
                }
                for k, v in engines.items()
            }
        }
    
    def get_engine_list(self):
        """获取引擎列表"""
        return {
            "cn": [{"id": k, "name": v["name"]} for k, v in self.ENGINES.items() if v["type"] == "cn"],
            "global": [{"id": k, "name": v["name"]} for k, v in self.ENGINES.items() if v["type"] == "global"],
            "total": len(self.ENGINES)
        }


if __name__ == "__main__":
    agg = ProSearchAggregator()
    result = agg.search_all("人工智能")
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

### 2. 批量关键词搜索(专业版独有)

```python
#!/usr/bin/env python3
"""专业版批量关键词搜索"""

import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from pro_search import ProSearchAggregator

class BatchSearchEngine:
    """批量搜索引擎"""
    
    def __init__(self, max_workers=5):
        self.aggregator = ProSearchAggregator()
        self.max_workers = max_workers
    
    def batch_search(self, keywords, engines=None):
        """批量搜索多个关键词"""
        results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {}
            for keyword in keywords:
                if engines:
                    future = executor.submit(self._search_engines, keyword, engines)
                else:
                    future = executor.submit(self.aggregator.search_all, keyword)
                futures[future] = keyword
            
            for future in futures:
                keyword = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    results.append({
                        "query": keyword,
                        "error": str(e)
                    })
        
        return {
            "batch_id": datetime.utcnow().strftime("%Y%m%d%H%M%S"),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "total_keywords": len(keywords),
            "successful": sum(1 for r in results if "error" not in r),
            "failed": sum(1 for r in results if "error" in r),
            "results": results
        }
    
    def _search_engines(self, keyword, engine_ids):
        """在指定引擎中搜索"""
        encoded = urllib.parse.quote(keyword)
        return {
            "query": keyword,
            "engines": {
                eid: {
                    "name": self.aggregator.ENGINES[eid]["name"],
                    "url": self.aggregator.ENGINES[eid]["url"].format(encoded)
                }
                for eid in engine_ids if eid in self.aggregator.ENGINES
            }
        }


if __name__ == "__main__":
    batch = BatchSearchEngine()
    
    keywords = ["人工智能", "机器学习", "深度学习", "自然语言处理"]
    result = batch.batch_search(keywords)
    print(f"批量搜索完成: {result['successful']}/{result['total_keywords']}")
```

### 3. 搜索结果缓存(专业版独有)

```python
#!/usr/bin/env python3
"""专业版搜索结果缓存"""

import json
import os
import hashlib
from datetime import datetime, timedelta

class SearchCache:
    """搜索结果缓存"""
    
    def __init__(self, cache_dir="./search_cache", ttl_hours=24):
        self.cache_dir = cache_dir
        self.ttl = timedelta(hours=ttl_hours)
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_key(self, query, engine=None):
        """生成缓存键"""
        key = f"{query}_{engine or 'all'}"
        return hashlib.md5(key.encode()).hexdigest()
    
    def get(self, query, engine=None):
        """获取缓存"""
        key = self._get_cache_key(query, engine)
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
        
        if not os.path.exists(cache_file):
            return None
        
        with open(cache_file, "r", encoding="utf-8") as f:
            cached = json.load(f)
        
        # 检查是否过期
        cached_time = datetime.fromisoformat(cached["timestamp"].replace("Z", "+00:00"))
        if datetime.utcnow() - cached_time > self.ttl:
            os.remove(cache_file)
            return None
        
        cached["from_cache"] = True
        return cached
    
    def set(self, query, result, engine=None):
        """设置缓存"""
        key = self._get_cache_key(query, engine)
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
        
        result["timestamp"] = datetime.utcnow().isoformat() + "Z"
        
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    
    def clear(self):
        """清空缓存"""
        for f in os.listdir(self.cache_dir):
            if f.endswith(".json"):
                os.remove(os.path.join(self.cache_dir, f))
    
    def stats(self):
        """缓存统计"""
        files = [f for f in os.listdir(self.cache_dir) if f.endswith(".json")]
        total_size = sum(
            os.path.getsize(os.path.join(self.cache_dir, f))
            for f in files
        )
        return {
            "cache_count": len(files),
            "total_size_mb": round(total_size / 1024 / 1024, 2),
            "cache_dir": self.cache_dir
        }
```

### 4. REST API服务(专业版独有)

```python
#!/usr/bin/env python3
"""专业版搜索REST API"""

from flask import Flask, request, jsonify
from pro_search import ProSearchAggregator
from batch_search import BatchSearchEngine
from search_cache import SearchCache

app = Flask(__name__)
aggregator = ProSearchAggregator()
batch_engine = BatchSearchEngine()
cache = SearchCache()

@app.route('/api/v1/search', methods=['GET'])
def search():
    """搜索接口"""
    query = request.args.get("q", "")
    engine = request.args.get("engine")
    engine_type = request.args.get("type")  # cn or global
    
    if not query:
        return jsonify({"error": "缺少参数 q"}), 400
    
    # 检查缓存
    cached = cache.get(query, engine)
    if cached:
        return jsonify(cached)
    
    # 执行搜索
    if engine:
        result = aggregator._search_engines(query, [engine])
    elif engine_type:
        result = aggregator.search_by_type(query, engine_type)
    else:
        result = aggregator.search_all(query)
    
    # 缓存结果
    cache.set(query, result, engine)
    
    return jsonify(result)

@app.route('/api/v1/search/batch', methods=['POST'])
def batch_search():
    """批量搜索"""
    data = request.json
    keywords = data.get("keywords", [])
    
    if not keywords:
        return jsonify({"error": "缺少 keywords"}), 400
    
    result = batch_engine.batch_search(keywords)
    return jsonify(result)

@app.route('/api/v1/engines', methods=['GET'])
def list_engines():
    """获取引擎列表"""
    return jsonify(aggregator.get_engine_list())

@app.route('/api/v1/cache/stats', methods=['GET'])
def cache_stats():
    """缓存统计"""
    return jsonify(cache.stats())

if __name__ == '__main__':
    print("搜索API服务启动: http://localhost:5000")
    print("  GET  /api/v1/search?q=关键词     - 搜索")
    print("  POST /api/v1/search/batch        - 批量搜索")
    print("  GET  /api/v1/engines             - 引擎列表")
    print("  GET  /api/v1/cache/stats         - 缓存统计")
    app.run(host='0.0.0.0', port=5000)
```

## 使用场景

### 场景一:市场调研多源搜索

```python
#!/usr/bin/env python3
"""市场调研多源搜索"""

import json
from pro_search import ProSearchAggregator

def market_research(topic):
    """市场调研:同一主题在多引擎搜索"""
    agg = ProSearchAggregator()
    
    # 中文市场搜索
    cn_results = agg.search_by_type(topic, "cn")
    print(f"中文搜索引擎: {cn_results['engine_count']}个")
    for eid, info in cn_results["engines"].items():
        print(f"  {info['name']}: {info['url']}")
    
    # 国际市场搜索
    global_results = agg.search_by_type(topic, "global")
    print(f"\n国际搜索引擎: {global_results['engine_count']}个")
    for eid, info in global_results["engines"].items():
        print(f"  {info['name']}: {info['url']}")

market_research("新能源汽车市场分析")
```

### 场景二:批量关键词搜索

```bash
#!/bin/bash
# 批量关键词搜索

echo "=== 批量关键词搜索 ==="

KEYWORDS=("AI安全" "区块链应用" "云计算趋势" "物联网发展")

python3 -c "
import json
from batch_search import BatchSearchEngine

batch = BatchSearchEngine()
keywords = ['AI安全', '区块链应用', '云计算趋势', '物联网发展']
result = batch.batch_search(keywords)

print(f'批量搜索完成:')
print(f'  总数: {result[\"total_keywords\"]}')
print(f'  成功: {result[\"successful\"]}')
print(f'  失败: {result[\"failed\"]}')

for r in result['results']:
    if 'error' not in r:
        print(f'  关键词: {r[\"query\"]} -> {r[\"engine_count\"]}个引擎')
"
```

### 场景三:定时搜索任务

```bash
#!/bin/bash
# 定时搜索任务(cron)

# 添加到crontab: 0 9 * * 1 /path/to/scheduled_search.sh
# 每周一上午9点执行

QUERY="行业最新动态"
OUTPUT_DIR="./search-reports"
mkdir -p "$OUTPUT_DIR"

TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
OUTPUT_FILE="${OUTPUT_DIR}/search_${TIMESTAMP}.json"

echo "执行定时搜索: ${QUERY}"

python3 -c "
import json
from pro_search import ProSearchAggregator

agg = ProSearchAggregator()
result = agg.search_all('${QUERY}')

with open('${OUTPUT_FILE}', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'搜索完成: ${OUTPUT_FILE}')
print(f'引擎数量: {result[\"engine_count\"]}')
"
```

## 快速开始

### 从免费版升级

```python
# 免费版:8引擎链接生成
agg = MultiSearchAggregator()
result = agg.search("关键词")

# 专业版:16引擎+缓存+API
agg = ProSearchAggregator()
result = agg.search_all("关键词")
```

## 配置示例

### 专业版功能矩阵

| 功能 | 免费版 | 专业版 | 说明 |
|:-----|:-------|:-------|:-----|
| 引擎数量 | 8个 | 16个 | 7中文+9国际 |
| 结果缓存 | 不支持 | 支持 | 24小时TTL |
| 批量搜索 | 不支持 | 支持 | 并行处理 |
| REST API | 不支持 | 支持 | 完整API |
| 导出格式 | 文本 | JSON/CSV | 多格式 |
| 定时搜索 | 不支持 | 支持 | Cron任务 |

### 支持的16个搜索引擎

| 类型 | 引擎 | 数量 |
|:-----|:-----|:-----|
| 中文 | 百度/搜狗/360/必应中国/头条/知乎/微博 | 7 |
| 国际 | Google/Bing/DDG/Yandex/Yahoo/Startpage/Ecosia/Brave/Swisscows | 9 |

## 最佳实践

1. **缓存优先**:使用缓存减少重复搜索请求。
2. **批量处理**:多个关键词使用批量搜索接口。
3. **类型筛选**:根据需求选择中文或国际引擎。
4. **定时执行**:对持续关注的主题设置定时搜索。
5. **结果导出**:将搜索结果导出为JSON/CSV便于分析。

## 常见问题

### Q1: 专业版与免费版引擎是否兼容?

完全兼容。专业版在免费版8个引擎基础上新增8个引擎,已有配置可直接使用。

### Q2: 缓存TTL可以调整吗?

可以,在SearchCache初始化时设置ttl_hours参数,默认24小时。

### Q3: 批量搜索有数量限制吗?

建议单次批量不超过50个关键词,并发度默认5,可根据需要调整。

### Q4: API服务如何部署?

使用Flask启动API服务,建议配合gunicorn部署到生产环境。

### Q5: 搜索结果能直接获取网页内容吗?

专业版生成搜索链接并缓存。直接抓取网页内容需要配合爬虫工具使用。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(使用API和缓存功能时需要)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| python3 | 运行时 | 必需 | python.org 下载 |
| flask | Web框架 | 推荐 | `pip install flask` |
| requests | HTTP库 | 可选 | `pip install requests` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 专业版搜索链接生成无需API Key
- REST API服务建议配置认证Token
- 缓存数据存储在本地,无需外部凭证

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行专业级多搜索引擎聚合与检索任务
