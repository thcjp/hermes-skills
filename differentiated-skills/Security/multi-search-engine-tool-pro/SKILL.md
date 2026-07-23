---
slug: multi-search-engine-tool-pro
name: multi-search-engine-tool-pro
version: 1.0.0
displayName: 多搜索引擎专业版
summary: 企业级多搜索引擎聚合平台,支持16个引擎、结果去重排序、批量搜索、API访问与本地缓存,适合专业信息检索团队。
license: Proprietary
edition: pro
description: '多搜索引擎专业版,为专业用户提供全方位多搜索引擎聚合与检索能力。

  核心能力:16引擎聚合搜索、智能去重排序、批量关键词搜索、搜索API、本地结果缓存、JSON/CSV导出。

  适用场景:专业信息检索、市场调研、竞品分析、学术研究。

  差异化:专业版兼容免费版搜索配置,新增结果聚合分析与API能力,满足专业检索需求。

  适用关键词: 搜索聚合, 结果去重, 批量搜索, 搜索API, 结果缓存, search aggregation, dedup, batch search'
tags:
- 搜索
- 信息检索
- 企业版
- API
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "exec"]
tags: "安全,加密,工具"
---
专业版为专业用户提供完整的多搜索引擎聚合与检索平台,在免费版链接生成能力之上,新增16引擎结果聚合、智能去重与相关性排序、批量关键词搜索、搜索结果API、本地结果缓存与JSON/CSV导出。专业版完全兼容免费版搜索引擎配置,已有搜索脚本可无缝升级,适合专业信息检索与市场调研场景。

### 专业版核心优势
| 优势 | 说明 |
|---|---|
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

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供16引擎聚合搜索(专业版独有)所需的指令和必要参数。
**处理**: 解析16引擎聚合搜索(专业版独有)的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回16引擎聚合搜索(专业版独有)的响应数据,包含状态码、结果和日志。

### 2. 批量关键词搜索(专业版独有)

**输入**: 用户提供批量关键词搜索(专业版独有)所需的指令和必要参数。
**处理**: 解析批量关键词搜索(专业版独有)的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回批量关键词搜索(专业版独有)的响应数据,包含状态码、结果和日志。

### 3. 搜索结果缓存(专业版独有)
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 多搜索引擎专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
#!/usr/bin/env python3
"""专业版搜索结果缓存"""
# ...
import json
import os
import hashlib
from datetime import datetime, timedelta
# ...
class SearchCache:
    """搜索结果缓存"""
# ...
    def __init__(self, cache_dir="./search_cache", ttl_hours=24):
        self.cache_dir = cache_dir
        self.ttl = timedelta(hours=ttl_hours)
        os.makedirs(cache_dir, exist_ok=True)
# ...
    def _get_cache_key(self, query, engine=None):
        """生成缓存键"""
        key = f"{query}_{engine or 'all'}"
        return hashlib.md5(key.encode()).hexdigest()
# ...
    def get(self, query, engine=None):
        """获取缓存"""
        key = self._get_cache_key(query, engine)
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
# ...
        if not os.path.exists(cache_file):
            return None
# ...
        with open(cache_file, "r", encoding="utf-8") as f:
            cached = json.load(f)
# ...
        cached_time = datetime.fromisoformat(cached["timestamp"].replace("Z", "+00:00"))
        if datetime.utcnow() - cached_time > self.ttl:
            os.remove(cache_file)
            return None
# ...
        cached["from_cache"] = True
        return cached
# ...
    def set(self, query, result, engine=None):
        """设置缓存"""
        key = self._get_cache_key(query, engine)
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
# ...
        result["timestamp"] = datetime.utcnow().isoformat() + "Z"
# ...
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
# ...
    def clear(self):
        """清空缓存"""
        for f in os.listdir(self.cache_dir):
            if f.endswith(".json"):
                os.remove(os.path.join(self.cache_dir, f))
# ...
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

**输入**: 用户提供搜索结果缓存(专业版独有)所需的指令和必要参数。
**处理**: 解析搜索结果缓存(专业版独有)的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回搜索结果缓存(专业版独有)的响应数据,包含状态码、结果和日志。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. REST API服务(专业版独有)
```python
#!/usr/bin/env python3
"""专业版搜索REST API"""
# ...
from flask import Flask, request, jsonify
from pro_search import ProSearchAggregator
from batch_search import BatchSearchEngine
from search_cache import SearchCache
# ...
app = Flask(__name__)
aggregator = ProSearchAggregator()
batch_engine = BatchSearchEngine()
cache = SearchCache()
# ...
@app.route('/api/v1/search', methods=['GET'])
def search():
    """搜索接口"""
    query = request.args.get("q", "")
    engine = request.args.get("engine")
    engine_type = request.args.get("type")  # cn or global
    if not query:
        return jsonify({"error": "缺少参数 q"}), 400
# ...
    cached = cache.get(query, engine)
    if cached:
        return jsonify(cached)
# ...
    if engine:
        result = aggregator._search_engines(query, [engine])
    elif engine_type:
        result = aggregator.search_by_type(query, engine_type)
    else:
        result = aggregator.search_all(query)
# ...
    cache.set(query, result, engine)
# ...
    return jsonify(result)
# ...
@app.route('/api/v1/search/batch', methods=['POST'])
def batch_search():
    """批量搜索"""
    data = request.json
    keywords = data.get("keywords", [])
# ...
    if not keywords:
        return jsonify({"error": "缺少 keywords"}), 400
# ...
    result = batch_engine.batch_search(keywords)
    return jsonify(result)
# ...
@app.route('/api/v1/engines', methods=['GET'])
def list_engines():
    """获取引擎列表"""
    return jsonify(aggregator.get_engine_list())
# ...
@app.route('/api/v1/cache/stats', methods=['GET'])
def cache_stats():
    """缓存统计"""
    return jsonify(cache.stats())
# ...
if __name__ == '__main__':
    print("搜索API服务启动: http://localhost:5000")
    print("  GET  /api/v1/search?q=关键词     - 搜索")
    print("  POST /api/v1/search/batch        - 批量搜索")
    print("  GET  /api/v1/engines             - 引擎列表")
    print("  GET  /api/v1/cache/stats         - 缓存统计")
    app.run(host='0.0.0.0', port=5000)
```

**输入**: 用户提供REST API服务(专业版独有)所需的指令和必要参数。
**处理**: 解析REST API服务(专业版独有)的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回REST API服务(专业版独有)的响应数据,包含状态码、结果和日志。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级多搜索引擎、聚合平台、个引擎、结果去重排序、批量搜索、API、访问与本地缓存、适合专业信息检索、多搜索引擎专业版、为专业用户提供全、方位多搜索引擎聚、合与检索能力、核心能力、引擎聚合搜索、智能去重排序、批量关键词搜索、本地结果缓存、JSON、CSV、适用场景、专业信息检索、市场调研、竞品分析、学术研究、差异化、专业版兼容免费版、搜索配置、新增结果聚合分析、满足专业检索需求、适用关键词、搜索聚合、结果去重、结果缓存、search、aggregation、dedup、batch等。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一:市场调研多源搜索
```python
#!/usr/bin/env python3
"""市场调研多源搜索"""
# ...
import json
from pro_search import ProSearchAggregator
# ...
def market_research(topic):
    """市场调研:同一主题在多引擎搜索"""
    agg = ProSearchAggregator()
# ...
    cn_results = agg.search_by_type(topic, "cn")
    print(f"中文搜索引擎: {cn_results['engine_count']}个")
    for eid, info in cn_results["engines"].items():
        print(f"  {info['name']}: {info['url']}")
# ...
    global_results = agg.search_by_type(topic, "global")
    print(f"\n国际搜索引擎: {global_results['engine_count']}个")
    for eid, info in global_results["engines"].items():
        print(f"  {info['name']}: {info['url']}")
# ...
market_research("新能源汽车市场分析")
```

### 场景二:批量关键词搜索
```bash
#!/bin/bash
echo "=== 批量关键词搜索 ==="
# ...
KEYWORDS=("AI安全" "区块链应用" "云计算趋势" "物联网发展")
# ...
python3 -c "
import json
from batch_search import BatchSearchEngine
# ...
batch = BatchSearchEngine()
keywords = ['AI安全', '区块链应用', '云计算趋势', '物联网发展']
result = batch.batch_search(keywords)
# ...
print(f'批量搜索完成:')
print(f'  总数: {result[\"total_keywords\"]}')
print(f'  成功: {result[\"successful\"]}')
print(f'  失败: {result[\"failed\"]}')
# ...
for r in result['results']:
    if 'error' not in r:
        print(f'  关键词: {r[\"query\"]} -> {r[\"engine_count\"]}个引擎')
"
```

### 场景三:定时搜索任务
```bash
#!/bin/bash
QUERY="行业最新动态"
OUTPUT_DIR="./search-reports"
mkdir -p "$OUTPUT_DIR"
# ...
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
OUTPUT_FILE="${OUTPUT_DIR}/search_${TIMESTAMP}.json"
# ...
echo "执行定时搜索: ${QUERY}"
# ...
python3 -c "
import json
from pro_search import ProSearchAggregator
# ...
agg = ProSearchAggregator()
result = agg.search_all('${QUERY}')
# ...
with open('${OUTPUT_FILE}', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
# ...
print(f'搜索完成: ${OUTPUT_FILE}')
print(f'引擎数量: {result[\"engine_count\"]}')
"
```

## 不适用场景

以下场景多搜索引擎专业版不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求。

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级
```python
agg = MultiSearchAggregator()
result = agg.search("关键词")
# ...
agg = ProSearchAggregator()
result = agg.search_all("关键词")
```

## 示例
### 专业版功能矩阵
| 功能 | 免费版 | 专业版 | 说明 |
|---:|---:|---:|---:|
| 引擎数量 | 8个 | 16个 | 7中文+9国际 |
| 结果缓存 | 不支持 | 支持 | 24小时TTL |
| 批量搜索 | 不支持 | 支持 | 并行处理 |
| REST API | 不支持 | 支持 | 完整API |
| 导出格式 | 文本 | JSON/CSV | 多格式 |
| 定时搜索 | 不支持 | 支持 | Cron任务 |

### 支持的16个搜索引擎
| 类型 | 引擎 | 数量 |
|:---:|:---:|:---:|
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

### 已知限制
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

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "多搜索引擎专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "multi search engine pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
