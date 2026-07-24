# 详细参考 - web-browsing-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

```bash
cat > competitor_monitor.json << 'EOF'
{
  "monitors": [
    {
      "name": "竞品A价格监控",
      "url": "https://competitor-a.example.com/pricing",
      "check_interval": "daily",
      "extract": {"prices": ".price-list", "products": ".product-name"},
      "alert_condition": "price_change > 5%"
    },
    {
      "name": "竞品B产品监控",
      "url": "https://competitor-b.example.com/products",
      "check_interval": "daily",
      "extract": {"products": ".product-item", "features": ".feature-list"},
      "alert_condition": "new_product_detected == true"
    }
  ]
}
EOF

web-browsing monitor start competitor_monitor.json

web-browsing report daily \
  --config competitor_monitor.json \
  --date $(date +%Y-%m-%d) \
  --output competitor_intel_$(date +%Y%m%d).html

web-browsing report trend \
  --config competitor_monitor.json \
  --period "2026-07-11:2026-07-17" \
  --output weekly_trend.html
```

## 代码示例 (json)

```json
{
  "edition": "pro",
  "batch": {
    "max_concurrency": 20,
    "timeout": 120,
    "retry_attempts": 3,
    "rate_limit": "premium"
  },
  "monitoring": {
    "enabled": true,
    "check_interval": 3600,
    "change_detection": true,
    "alert_channels": ["email", "webhook"]
  },
  "analysis": {
    "dimensions": ["sentiment", "entities", "topics", "summary"],
    "language_detection": true,
    "custom_models": true
  },
  "team": {
    "enabled": true,
    "shared_results": true,
    "knowledge_base": true,
    "role_based_access": true
  },
  "extraction": {
    "custom_rules": true,
    "data_pipeline": true,
    "output_formats": ["json", "csv", "excel"]
  }
}
```

## 代码示例 (bash)

```bash
cat > extraction_rules.json << 'EOF'
{
  "rules": [
    {
      "name": "product_info",
      "url_pattern": "*/product/*",
      "fields": {
        "title": "h1.product-title",
        "price": ".price-current",
        "rating": ".rating-score",
        "availability": ".stock-status"
      },
      "output_format": "json"
    }
  ]
}
EOF

web-browsing extract custom \
  --rules extraction_rules.json \
  --url "https://shop.example.com/product/123"

web-browsing batch extract \
  --rules extraction_rules.json \
  --input product_urls.json \
  --output products.json
```

## 代码示例 (json)

```json
{
  "monitoring": {
    "monitors": [
      {
        "name": "网页变化监控",
        "url": "https://target.example.com",
        "check_interval": "hourly",
        "detect_changes": {
          "content": true,
          "structure": true,
          "specific_elements": [".price", ".availability"]
        },
        "alert_conditions": [
          {"metric": "content_change", "threshold": 0.1, "action": "immediate"},
          {"metric": "price_change", "threshold": 0.05, "action": "summary"}
        ],
        "notification_channels": {
          "immediate": ["webhook", "email"],
          "summary": ["email"]
        }
      }
    ]
  }
}
```

