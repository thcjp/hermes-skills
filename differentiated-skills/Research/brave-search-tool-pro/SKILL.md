---
slug: brave-search-tool-pro
name: brave-search-tool-pro
version: "1.0.0"
displayName: Brave搜索工具-专业版
summary: 企业级Brave搜索,支持批量查询、并发搜索、结果缓存与搜索分析,面向团队生产场景
license: MIT
edition: pro
description: |-
  企业级 Brave Search 网页搜索工具,在免费版核心能力之上,提供批量查询、
  并发搜索、结果缓存、搜索历史、内容聚合与 API 访问能力。

  核心能力:
  - 免费版全部能力(完全兼容)
  - 批量查询与并发搜索
  - 智能结果缓存与去重
  - 搜索历史与审计
  - 内容聚合与报告生成
  - API 访问与第三方集成

  适用场景:
  - 企业级信息调研
  - 批量知识采集
  - 竞品动态监控
  - 团队共享搜索

  差异化:专业版面向团队与企业,提供批量、并发、缓存、分析等高阶能力,并保持与免费版完全兼容。

  触发关键词: 网页搜索, 批量搜索, 并发查询, 结果缓存, 搜索分析, Brave, brave-search
tags:
- 研究工具
- 网页搜索
- 企业级
- 批量操作
tools:
- read
- exec
---

# Brave搜索工具(专业版)

## 概述

本工具是企业级 Brave Search 网页搜索工具,在免费版核心能力之上,扩展了批量查询、并发搜索、结果缓存、搜索历史、内容聚合与 API 访问能力,适合企业级信息调研、批量知识采集、竞品动态监控与团队共享搜索场景。专业版与免费版完全兼容:免费版的所有命令、脚本调用均可直接在专业版中使用。

### 免费版 vs 专业版对比

| 能力 | 免费版 | 专业版 |
|:-----|:------|:------|
| 基础搜索(search.js) | 支持 | 支持 |
| 内容提取(content.js) | 支持 | 支持 |
| 结果数量配置 | 支持 | 支持 |
| `--content` 全文提取 | 支持 | 支持 |
| 批量查询 | 不支持 | 支持 |
| 并发搜索 | 不支持 | 支持 |
| 结果缓存 | 不支持 | 支持 |
| 搜索历史 | 不支持 | 支持 |
| 内容聚合与报告 | 不支持 | 支持 |
| API 访问 | 不支持 | 支持 |
| 优先技术支持 | 不支持 | 支持 |

## 核心能力

### 1. 批量查询与并发搜索(专业版新增)

```bash
# 批量查询(从文件读取)
brave-pro batch-search --file queries.txt --concurrency 5

# 批量查询(命令行传入)
brave-pro batch-search "AI智能体" "大模型" "向量数据库" --concurrency 3

# 批量查询带内容提取
brave-pro batch-search --file queries.txt --content --concurrency 3
```

### 2. 智能结果缓存与去重(专业版新增)

```bash
# 启用缓存
brave-pro search "Python asyncio" --cache

# 自定义缓存时间
brave-pro search "Python asyncio" --cache --ttl 3600

# 跨查询去重
brave-pro batch-search --file queries.txt --dedup

# 清理缓存
brave-pro cache cleanup
```

### 3. 搜索历史与审计(专业版新增)

```bash
# 查看搜索历史
brave-pro history --limit 50

# 按时间筛选
brave-pro history --from 2026-03-01 --to 2026-03-10

# 按成员筛选
brave-pro history --member alice

# 导出历史
brave-pro history --export json > search-history.json
```

### 4. 内容聚合与报告生成(专业版新增)

```bash
# 多查询结果聚合
brave-pro aggregate "AI智能体" "智能体框架" "多智能体" --top 10

# 生成调研报告
brave-pro report "AI智能体调研" --queries "AI智能体,智能体框架" --format markdown

# 内容深度提取(批量提取多个URL)
brave-pro extract-batch --file urls.txt --format markdown
```

### 5. API 访问与第三方集成(专业版新增)

```bash
# 启用 API 服务
brave-pro api start --port 8080

# API 查询示例
curl -s "http://localhost:8080/api/search?q=AI智能体&count=10"
curl -s -X POST "http://localhost:8080/api/batch" -d '{"queries":["AI","大模型"]}'
curl -s "http://localhost:8080/api/extract?url=https://example.com/article"
```

## 使用场景

### 场景一:企业批量信息调研

企业需要对多个主题进行批量调研,并发搜索提升效率。

```bash
#!/bin/bash
# batch-research.sh - 批量信息调研
TOPICS_FILE="topics.txt"
OUTPUT_DIR="research-results"
mkdir -p "$OUTPUT_DIR"

# 批量并发搜索(5个并发),带内容提取
brave-pro batch-search \
  --file "$TOPICS_FILE" \
  --concurrency 5 \
  --count 10 \
  --content \
  --dedup \
  --format json \
  --output "$OUTPUT_DIR/results.json"

# 生成调研报告
brave-pro report \
  --input "$OUTPUT_DIR/results.json" \
  --format markdown \
  --output "$OUTPUT_DIR/research-report.md"

echo "批量调研完成,报告: $OUTPUT_DIR/research-report.md"
```

```python
#!/usr/bin/env python3
"""企业批量调研编排示例"""
import subprocess
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

RESEARCH_TOPICS = [
    {"query": "AI智能体市场格局 2026", "count": 15, "purpose": "市场分析"},
    {"query": "大模型微调技术对比", "count": 10, "purpose": "技术选型"},
    {"query": "向量数据库性能评测", "count": 10, "purpose": "技术选型"},
    {"query": "RAG技术最佳实践", "count": 15, "purpose": "方案设计"},
    {"query": "AI智能体安全风险", "count": 10, "purpose": "风险评估"},
]

def research_topic(topic):
    """调研单个主题"""
    result = subprocess.run([
        "brave-pro", "search",
        topic["query"],
        "--count", str(topic["count"]),
        "--content",
        "--cache",
        "--format", "json"
    ], capture_output=True, text=True)

    try:
        data = json.loads(result.stdout)
        return {
            "query": topic["query"],
            "purpose": topic["purpose"],
            "result_count": len(data.get("results", [])),
            "results": data.get("results", [])
        }
    except json.JSONDecodeError:
        return {"query": topic["query"], "purpose": topic["purpose"], "error": "解析失败"}

# 并发调研,最大并发3
results = []
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(research_topic, t): t for t in RESEARCH_TOPICS}
    for future in as_completed(futures):
        result = future.result()
        results.append(result)
        print(f"[OK] {result['query']} ({result.get('result_count', 0)} 条结果)")

# 生成综合报告
report = brave_pro_generate_report(results)
with open("research-report.md", "w") as f:
    f.write(report)
print(f"\n调研完成: {len(results)} 个主题,报告已保存")
```

### 场景二:竞品动态持续监控

持续监控竞品相关动态,结合内容提取深入分析。

```bash
#!/bin/bash
# competitor-monitor.sh - 竞品动态监控
COMPETITORS=("竞品A" "竞品B" "竞品C")
ALERT_WEBHOOK="https://hooks.example.com/alerts"

for comp in "${COMPETITORS[@]}"; do
  # 搜索竞品最新动态(带缓存,6小时有效)
  RESULTS=$(brave-pro search "${comp} 最新动态 融资 发布" \
    --count 10 \
    --content \
    --cache \
    --ttl 21600 \
    --format json)

  # 提取关键动态
  echo "$RESULTS" | jq -r '.results[] | "[\(.title)] \(.url)"' | while read line; do
    echo "[$comp] $line"
  done

  # 深度提取重要文章内容
  echo "$RESULTS" | jq -r '.results[0:3][].url' | while read url; do
    CONTENT=$(brave-pro extract "$url" --format markdown --cache)
    echo "$CONTENT" >> "reports/${comp}_$(date +%Y%m%d).md"
  done

done

echo "竞品监控完成,报告已归档"
```

### 场景三:团队共享搜索与知识沉淀

团队共享搜索历史与结果,避免重复搜索,沉淀调研成果。

```bash
#!/bin/bash
# team-shared-search.sh - 团队共享搜索
SHARED_DIR="/shared/search-results"
mkdir -p "$SHARED_DIR/cache"

QUERY="$1"
MEMBER="${USER:-anonymous}"
DATE=$(date +%Y-%m-%d)
HASH=$(echo -n "$QUERY" | md5sum | awk '{print $1}')

# 检查团队缓存
if [ -f "$SHARED_DIR/cache/${HASH}.json" ]; then
  echo "[缓存命中] 使用团队已有结果"
  cat "$SHARED_DIR/cache/${HASH}.json"
else
  # 执行搜索(带内容提取)
  brave-pro search "$QUERY" --count 10 --content --format json > "$SHARED_DIR/cache/${HASH}.json"

  # 记录搜索历史
  echo "{\"date\":\"$DATE\",\"member\":\"$MEMBER\",\"query\":\"$QUERY\",\"file\":\"cache/${HASH}.json\"}" \
    >> "$SHARED_DIR/history.jsonl"

  echo "[新搜索] 结果已归档到共享库"
  cat "$SHARED_DIR/cache/${HASH}.json"
fi

# 查看团队搜索统计
brave-pro history --shared --stats
```

## 快速开始

### 1. 安装与初始化

```bash
cd /path/to/brave-search-tool
npm ci

# 专业版初始化
brave-pro init

# 配置
brave-pro config set api.key "$BRAVE_API_KEY"
brave-pro config set cache.enabled true
brave-pro config set cache.ttl 86400
brave-pro config set batch.max_concurrency 5
```

### 2. 批量搜索工作流

```bash
# 单次搜索(带缓存与内容)
brave-pro search "AI智能体" --count 10 --content --cache

# 批量搜索(并发)
brave-pro batch-search --file queries.txt --concurrency 5 --dedup

# 生成调研报告
brave-pro report --input results.json --format markdown
```

### 3. 启用 API 服务

```bash
# 启动 API
brave-pro api start --port 8080 --auth token

# 生成 Token
brave-pro api token create --name "integration" --scope "read"

# 验证
curl -s -H "Authorization: Bearer <token>" "http://localhost:8080/api/health"
```

## 配置示例

### 企业级配置文件

```yaml
# ~/.brave-pro/config.yaml
edition: pro
api:
  key: ${BRAVE_API_KEY}
  endpoint: https://api.search.brave.com
  timeout: 30
  max_results: 50
cache:
  enabled: true
  ttl: 86400
  path: ~/.brave-pro/cache
  max_size_mb: 1024
batch:
  max_concurrency: 5
  retry: 3
  retry_delay: 5
  dedup: true
history:
  enabled: true
  path: ~/.brave-pro/history.jsonl
  retention_days: 365
  shared: /shared/search-history.jsonl
api_server:
  enabled: true
  port: 8080
  auth: token
  cors: ["https://app.example.com"]
alerts:
  webhook: https://hooks.example.com/search-alerts
extract:
  cache: true
  format: markdown
  max_content_length: 50000
```

### 监控统计示例

```bash
# 搜索统计
brave-pro stats
# 输出示例:
# === 搜索统计 ===
# 总搜索次数: 2345
# 本月搜索: 123
# 缓存命中率: 72%
# 内容提取次数: 456
# 批量搜索: 34 次
# 热门查询: AI智能体(56), 大模型(38), 向量数据库(31)
# 活跃成员: alice(56), bob(38), charlie(31)
# API 调用: 2345(配额使用: 78%)

# 导出统计
brave-pro stats --export json > stats.json
```

## 最佳实践

### 批量搜索优化
1. **合理并发**:并发数不超过 `max_concurrency`(默认5),避免触发 API 限流。
2. **启用缓存**:重复查询走缓存,减少 API 调用与成本。
3. **结果去重**:批量搜索启用 `--dedup`,避免跨查询重复内容。
4. **按需提取内容**:仅对重要结果启用 `--content`,减少 API 调用。

### 团队协作
1. **共享缓存**:团队共享缓存库,避免重复搜索。
2. **搜索历史**:记录搜索历史,便于复盘与知识沉淀。
3. **调研报告**:批量搜索后生成调研报告,归档共享。
4. **告警集成**:重要内容通过 webhook 即时通知团队。

### 成本控制
1. **缓存优先**:优先走缓存,减少 API 调用。
2. **配额监控**:监控 API 配额使用率,避免超额。
3. **按需搜索**:事实查询用少量结果,深度调研才用大量结果。
4. **定期清理**:定期清理过期缓存,控制存储成本。

## 常见问题

### Q1: 专业版是否兼容免费版?
完全兼容。免费版的所有 `search.js` / `content.js` 调用在专业版中均可直接使用。专业版在原有能力之上扩展高阶特性。

### Q2: 如何从免费版升级?
```bash
brave-pro init --migrate
```
升级过程保留全部历史缓存与配置。

### Q3: 批量搜索如何控制并发?
通过 `--concurrency` 参数或配置文件 `batch.max_concurrency` 设置。建议 3-5,避免触发 API 限流。

### Q4: API 配额快用完了怎么办?
- 启用缓存,减少重复查询的 API 调用
- 降低批量搜索并发数
- 优先使用摘要搜索,仅对重要结果启用 `--content`
- 监控配额使用率,设置告警阈值

### Q5: 如何接入现有系统?
通过 API 服务集成:
```bash
brave-pro api start --port 8080
curl "http://localhost:8080/api/search?q=AI&count=10"
curl "http://localhost:8080/api/extract?url=https://example.com"
```
支持 RESTful API,可集成到任何系统。

### Q6: 内容提取失败怎么办?
- 部分页面有反爬机制,可能限制内容提取
- 检查 URL 是否可访问
- 对动态加载内容,可结合浏览器自动化工具获取
- 查看错误日志,确认是否为 API 限制

## 与免费版的兼容性

| 维度 | 兼容性 |
|:-----|:------|
| 命令语法 | 100% 兼容(search.js / content.js 可用) |
| 脚本调用 | 100% 兼容(无需修改即可运行) |
| API 返回格式 | 100% 兼容 |
| 配置文件 | 向后兼容(专业版新增字段可选) |
| 升级路径 | 平滑升级(保留全部历史数据) |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 Brave Search API
- **Node.js**: >= 16.0.0
- **推荐内存**: >= 1GB(批量搜索场景建议 2GB+)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| brave-pro | CLI 工具 | 必需 | 随 Skill 安装 |
| Node.js | 运行环境 | 必需 | 系统包管理器安装 |
| npm 依赖包 | Node 包 | 必需 | `npm ci` 安装 |
| Brave Search API | 数据源 | 必需 | Brave Search API 订阅 |
| BRAVE_API_KEY | API Key | 必需 | Brave Search API 控制台获取 |
| jq | JSON 处理 | 推荐 | 系统包管理器安装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 监控系统 | 可观测性 | 可选 | Prometheus / Grafana |

### API Key 配置
- **BRAVE_API_KEY**:Brave Search API Key
  - 获取方式:Brave Search API 官网注册
  - 配置方式:环境变量或配置文件
- API 服务 Token:为第三方集成生成独立 Token
- 告警 webhook:配置团队 IM 通知地址

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
- **版本**: 专业版(兼容免费版全部能力)
