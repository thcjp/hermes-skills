# 详细参考 - game-dev-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import os
import requests
from datetime import datetime

API_BASE = "https://api.game-dev-pro.local/v1"
ADMIN_KEY = os.environ["GAME_DEV_ADMIN_KEY"]

class GameStudio:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key, "X-Edition": "pro"}

    def create_project(self, name, team_members):
        """创建协作项目"""
        payload = {
            "name": name,
            "members": team_members,
            "roles": {
                "producer": ["review", "assign", "manage"],
                "designer": ["design", "review"],
                "programmer": ["code", "review"],
                "artist": ["assets", "review"],
                "qa": ["test", "report"],
            },
            "workflow": {
                "version_control": "git",
                "branch_strategy": "git_flow",
                "code_review": {"required": True, "min_reviewers": 2},
                "ci_cd": True,
            },
        }
        resp = requests.post(
            f"{API_BASE}/projects",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()

    def assign_task(self, project_id, title, assignee, priority, due):
        """分配任务"""
        payload = {
            "project_id": project_id,
            "title": title,
            "assignee": assignee,
            "priority": priority,
            "due": due,
            "reviewers": ["tech_lead"],
        }
        resp = requests.post(
            f"{API_BASE}/tasks",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()

    def project_dashboard(self, project_id):
        """获取项目仪表盘"""
        resp = requests.get(
            f"{API_BASE}/projects/{project_id}/dashboard",
            headers=self.headers,
            timeout=60,
        )
        return resp.json()

studio = GameStudio(ADMIN_KEY)
project = studio.create_project("Project Aurora", [
    {"name": "alice", "role": "producer"},
    {"name": "bob", "role": "designer"},
    {"name": "carol", "role": "programmer"},
    {"name": "dave", "role": "artist"},
])
```

## 代码示例 (yaml)

```yaml
edition: pro
api:
  base_url: https://api.game-dev-pro.local/v1
  admin_key: ${GAME_DEV_ADMIN_KEY}
  org_id: ${GAME_DEV_ORG_ID}
  timeout: 120

team:
  max_members: 100
  roles: [producer, designer, programmer, artist, qa, marketing]
  permissions:
    producer: [manage_all, assign_tasks, review]
    designer: [design, review_design]
    programmer: [code, review_code, manage_builds]
    artist: [assets, review_assets]
    qa: [test, report_bugs, approve_release]

asset_management:
  storage: s3
  versioning: git_lfs
  preview: automatic
  pipeline:
    - import
    - optimize
    - compress
    - distribute

analytics:
  enabled: true
  metrics: [dau, mau, retention, revenue, funnel, cohort]
  data_warehouse: bigquery
  dashboards: [realtime, daily, weekly]

ci_cd:
  runner: self_hosted
  parallel_jobs: 8
  cache: true
  artifacts_retention: 90d

release:
  platforms: [steam, epic, gog, app_store, google_play, xbox, psn, switch]
  localization: [zh, en, ja, ko, fr, de, es]
  age_ratings: [esrb, pegi, cero, grac]
```

## 代码示例 (python)

```python
def upload_asset(project_id, asset_path, metadata):
    """上传游戏资产"""
    import mimetypes
    mime = mimetypes.guess_type(asset_path)[0]

    payload = {
        "project_id": project_id,
        "asset_path": asset_path,
        "metadata": metadata,
        "versioning": True,
        "preview": True,
    }
    with open(asset_path, "rb") as f:
        resp = requests.post(
            f"{API_BASE}/assets/upload",
            headers={**studio.headers, "Content-Type": mime},
            data=f,
            params=payload,
            timeout=300,
        )
    return resp.json()

def asset_pipeline(asset_id):
    """资产处理流水线"""
    payload = {
        "asset_id": asset_id,
        "steps": [
            {"name": "import", "tool": "auto_detect"},
            {"name": "optimize", "settings": {"texture_compress": "bc7", "mesh_decimate": 0.5}},
            {"name": "preview", "format": "webp"},
            {"name": "distribute", "targets": ["all_platforms"]},
        ],
    }
    resp = requests.post(
        f"{API_BASE}/assets/pipeline",
        headers=studio.headers,
        json=payload,
        timeout=120,
    )
    return resp.json()
```

