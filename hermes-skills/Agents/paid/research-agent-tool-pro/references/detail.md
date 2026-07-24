# 详细参考 - research-agent-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import requests

class ResearchAgentProClient:
    def __init__(self, api_key, base_url="https://api.research-agent-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url

    def create_research(self, topic, mode="interactive"):
        """创建研究任务"""
        resp = requests.post(
            f"{self.base_url}/v1/research",
            headers=self.headers,
            json={"topic": topic, "mode": mode}
        )
        return resp.json()

    def batch_research(self, topics, mode="deep"):
        """批量多主题研究"""
        resp = requests.post(
            f"{self.base_url}/v1/research/batch",
            headers=self.headers,
            json={"topics": topics, "mode": mode}
        )
        return resp.json()

    def get_status(self, run_id):
        """获取研究状态"""
        resp = requests.get(
            f"{self.base_url}/v1/research/{run_id}/status",
            headers=self.headers
        )
        return resp.json()

    def get_result(self, run_id, format="markdown"):
        """获取研究结果"""
        resp = requests.get(
            f"{self.base_url}/v1/research/{run_id}/result",
            headers=self.headers,
            params={"format": format}
        )
        return resp.json()

    def create_schedule(self, config):
        """创建定时研究任务"""
        resp = requests.post(
            f"{self.base_url}/v1/schedules",
            headers=self.headers,
            json=config
        )
        return resp.json()

    def search_history(self, query):
        """搜索历史研究"""
        resp = requests.get(
            f"{self.base_url}/v1/history",
            headers=self.headers,
            params={"q": query}
        )
        return resp.json()

    def graduate_research(self, run_id, project_name):
        """将研究毕业为项目spec"""
        resp = requests.post(
            f"{self.base_url}/v1/research/{run_id}/graduate",
            headers=self.headers,
            json={"project_name": project_name}
        )
        return resp.json()
```

## 代码示例 (bash)

```bash
mkdir -p ~/research-agent-pro/{research,results,reports,schedules,templates,history,config}

cat > ~/research-agent-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

workspace:
  path: "~/research-agent-pro/research"
  naming: "slug"

research:
  modes: ["interactive", "deep"]
  default_mode: "interactive"
  max_concurrent: 10
  checkpoint_interval: 5

  deep_research:
    enabled: true
    default_timeout_hours: 24
    auto_check_interval: 300  # 5分钟自动检查
    notify_on_complete: true

  principles:
    atomic_findings: true
    link_everything: true
    capture_context: true
    note_confidence: true
    date_findings: true

scheduling:
  enabled: true
  timezone: "Asia/Shanghai"
  config_path: "~/research-agent-pro/schedules/"

export:
  formats: ["pdf", "word", "html", "markdown"]
  path: "~/research-agent-pro/reports/"
  template_path: "~/research-agent-pro/templates/"

history:
  enabled: true
  retention_days: 365
  version_control: true
  searchable: true
  path: "~/research-agent-pro/history/"

team:
  enabled: true
  config_path: "~/research-agent-pro/config/team.yaml"

api:
  enabled: true
  rate_limit: "100/hour"
  auth: "bearer_token"
EOF
```

