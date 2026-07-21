# 详细参考 - news-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
departments = {
    "tech": {
        "name": "技术部",
        "interests": {
            "AI编程工具": 0.4,
            "云计算": 0.3,
            "网络安全": 0.3
        },
        "schedule": {
            "morning": "08:00",
            "evening": "18:00"
        },
        "format": "bullet_points",
        "language": "zh-CN",
        "members": ["dev1@company.com", "dev2@company.com"]
    },
    "market": {
        "name": "市场部",
        "interests": {
            "行业竞品": 0.5,
            "营销趋势": 0.3,
            "消费者行为": 0.2
        },
        "schedule": {
            "morning": "09:00"
        },
        "format": "narrative",
        "language": "zh-CN",
        "members": ["market1@company.com"]
    },
    "finance": {
        "name": "财务部",
        "interests": {
            "A股市场": 0.4,
            "宏观经济": 0.3,
            "监管政策": 0.3
        },
        "schedule": {
            "morning": "07:30",
            "noon": "12:00",
            "close": "15:30"
        },
        "format": "bullet_points",
        "language": "zh-CN",
        "members": ["cfo@company.com"]
    }
}
```

## 代码示例 (python)

```python
import requests

class NewsProClient:
    def __init__(self, api_key, base_url="https://api.news-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url

    def create_user(self, user_data):
        """创建新用户"""
        resp = requests.post(
            f"{self.base_url}/v1/users",
            headers=self.headers,
            json=user_data
        )
        return resp.json()

    def create_schedule(self, schedule_config):
        """创建定时推送"""
        resp = requests.post(
            f"{self.base_url}/v1/schedules",
            headers=self.headers,
            json=schedule_config
        )
        return resp.json()

    def get_analytics(self, user_id, period="monthly"):
        """获取阅读分析报告"""
        resp = requests.get(
            f"{self.base_url}/v1/analytics/{user_id}",
            headers=self.headers,
            params={"period": period}
        )
        return resp.json()

    def search_history(self, query, days=90):
        """搜索历史新闻"""
        resp = requests.get(
            f"{self.base_url}/v1/history",
            headers=self.headers,
            params={"q": query, "days": days}
        )
        return resp.json()
```

## 代码示例 (bash)

```bash
mkdir -p ~/news-pro/{users,schedules,reports,analytics,exports,templates}

cat > ~/news-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

multi_user:
  enabled: true
  max_users: 100
  data_isolation: strict

scheduling:
  enabled: true
  timezone: "Asia/Shanghai"
  min_interval_minutes: 30

sources:
  custom_enabled: true
  quality_rating: true
  max_sources: 50

analytics:
  enabled: true
  retention_days: 90
  report_frequency: "monthly"

export:
  formats: ["markdown", "pdf", "email", "webhook"]
  template_path: "~/news-pro/templates/"

api:
  enabled: true
  rate_limit: "100/hour"
  auth: "bearer_token"

languages: ["zh-CN", "en-US", "ja-JP", "ko-KR"]
EOF
```

