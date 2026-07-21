# 详细参考 - multi-search-engine-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
#!/usr/bin/env python3
"""专业版16引擎搜索聚合器"""

import urllib.parse
import json
from datetime import datetime

class ProSearchAggregator:
    """专业版搜索引擎聚合器"""

    ENGINES = {
        "baidu": {"name": "百度", "url": "https://www.baidu.com/s?wd={}", "type": "cn"},
        "sogou": {"name": "搜狗", "url": "https://www.sogou.com/web?query={}", "type": "cn"},
        "360": {"name": "360搜索", "url": "https://www.so.com/s?q={}", "type": "cn"},
        "bing_cn": {"name": "必应中国", "url": "https://cn.bing.com/search?q={}", "type": "cn"},
        "toutiao": {"name": "头条搜索", "url": "https://so.toutiao.com/search?keyword={}", "type": "cn"},
        "zhihu": {"name": "知乎搜索", "url": "https://www.zhihu.com/search?q={}", "type": "cn"},
        "weibo": {"name": "微博搜索", "url": "https://s.weibo.com/weibo?q={}", "type": "cn"},

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

## 代码示例 (python)

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

