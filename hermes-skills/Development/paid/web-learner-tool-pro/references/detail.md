# 详细参考 - web-learner-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
{
  "edition": "pro",
  "batch": {
    "max_concurrency": 20,
    "timeout": 120,
    "retry_attempts": 3,
    "sources_per_topic": 5
  },
  "knowledge_base": {
    "enabled": true,
    "versioning": true,
    "deduplication": true,
    "auto_merge": true,
    "retention_days": 365
  },
  "scheduling": {
    "enabled": true,
    "max_tasks": 50,
    "retry_attempts": 3
  },
  "integration": {
    "cross_validate": true,
    "merge_threshold": 0.8,
    "language_priority": ["zh", "en"]
  },
  "team": {
    "enabled": true,
    "shared_kb": true,
    "collaborative_editing": true,
    "role_based_access": true
  },
  "scoring": {
    "weights": {
      "relevance": 0.3,
      "credibility": 0.3,
      "freshness": 0.2,
      "completeness": 0.2
    },
    "min_threshold": 0.7
  }
}
```

## 代码示例 (bash)

```bash
cat > research_topics.json << 'EOF'
{
  "topics": [
    {"id": "r001", "topic": "深度学习优化算法", "field": "AI"},
    {"id": "r002", "topic": "推荐系统最新研究", "field": "AI"},
    {"id": "r003", "topic": "自然语言处理进展", "field": "AI"}
  ],
  "concurrency": 20,
  "depth": "deep",
  "cross_validate": true
}
EOF

web-learner batch learn research_topics.json --output raw_knowledge/

web-learner integrate \
  --input raw_knowledge/ \
  --deduplicate \
  --merge-similar \
  --output integrated_knowledge.json

web-learner graph build \
  --input integrated_knowledge.json \
  --output knowledge_graph.json

web-learner graph visualize \
  --graph knowledge_graph.json \
  --format interactive \
  --output knowledge_graph.html
```

## 代码示例 (bash)

```bash
cat > tech_intel.json << 'EOF'
{
  "topics": [
    {"id": "ai", "topic": "人工智能最新进展", "depth": "detailed"},
    {"id": "blockchain", "topic": "区块链技术应用", "depth": "detailed"},
    {"id": "quantum", "topic": "量子计算研究", "depth": "overview"},
    {"id": "iot", "topic": "物联网发展", "depth": "overview"}
  ],
  "concurrency": 10,
  "sources_per_topic": 5,
  "schedule": "0 9 * * 1"
}
EOF

web-learner schedule start tech_intel.json

web-learner report weekly \
  --config tech_intel.json \
  --period "2026-07-11:2026-07-17" \
  --output tech_intel_weekly.html

web-learner knowledge update \
  --input latest_learnings.json \
  --auto-merge \
  --deduplicate
```

## 代码示例 (bash)

```bash
web-learner knowledge create \
  --name "team_knowledge_base" \
  --category "general" \
  --versioning true

cat > team_config.json << 'EOF'
{
  "team": {
    "name": "learning_team",
    "members": [
      {"email": "lead@company.com", "role": "admin"},
      {"email": "researcher1@company.com", "role": "editor"},
      {"email": "researcher2@company.com", "role": "editor"}
    ]
  },
  "knowledge_base": {
    "shared": true,
    "versioning": true,
    "categories": ["technology", "market", "science", "policy"]
  }
}
EOF

web-learner team init team_config.json
```

## 代码示例 (json)

```json
{
  "knowledge_base": {
    "storage": {
      "type": "database",
      "host": "localhost",
      "port": 5432,
      "name": "knowledge_base"
    },
    "versioning": {
      "enabled": true,
      "max_versions": 50,
      "auto_cleanup": true
    },
    "search": {
      "enabled": true,
      "index_type": "fulltext",
      "language": "zh"
    },
    "export": {
      "formats": ["json", "csv", "markdown"],
      "include_metadata": true
    }
  }
}
```

