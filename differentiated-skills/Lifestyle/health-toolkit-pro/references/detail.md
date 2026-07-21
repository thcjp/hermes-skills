# 详细参考 - health-toolkit-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import os
import requests
from datetime import datetime

API_BASE = "https://api.health-toolkit-pro.local/v1"
ADMIN_KEY = os.environ["HEALTH_ADMIN_KEY"]

class FamilyHealthManager:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key, "X-Edition": "pro"}

    def add_member(self, name, age, gender, relation):
        """添加家庭成员"""
        payload = {
            "name": name,
            "age": age,
            "gender": gender,
            "relation": relation,  # self, spouse, child, parent
            "health_profile": {
                "height_cm": None,
                "weight_kg": None,
                "blood_type": None,
                "allergies": [],
                "medications": [],
                "chronic_conditions": [],
            },
        }
        resp = requests.post(
            f"{API_BASE}/members",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()

    def family_dashboard(self):
        """家庭健康仪表盘"""
        resp = requests.get(
            f"{API_BASE}/family/dashboard",
            headers=self.headers,
            timeout=60,
        )
        return resp.json()

    def member_report(self, member_id, period="month"):
        """生成成员健康报告"""
        resp = requests.get(
            f"{API_BASE}/members/{member_id}/report",
            headers=self.headers,
            params={"period": period},
            timeout=120,
        )
        return resp.json()

    def health_alerts(self):
        """获取健康预警"""
        resp = requests.get(
            f"{API_BASE}/alerts",
            headers=self.headers,
            timeout=30,
        )
        return resp.json()

manager = FamilyHealthManager(ADMIN_KEY)
manager.add_member("张三", 35, "male", "self")
manager.add_member("李四", 33, "female", "spouse")
manager.add_member("张小明", 8, "male", "child")
```

## 代码示例 (yaml)

```yaml
edition: pro
api:
  base_url: https://api.health-toolkit-pro.local/v1
  admin_key: ${HEALTH_ADMIN_KEY}
  org_id: ${HEALTH_ORG_ID}
  timeout: 120

family:
  max_members: 20
  roles: [admin, member, viewer]
  permissions:
    admin: [manage_all, view_all, edit_all]
    member: [view_own, edit_own]
    viewer: [view_own]

devices:
  supported: [apple_watch, fitbit, garmin, huawei_band, xiaomi_band]
  sync_frequency: realtime
  data_types: [heart_rate, steps, sleep, workout, blood_oxygen, ecg, stress]

ai_advice:
  enabled: true
  models: [exercise, nutrition, sleep, stress, risk]
  personalization: high
  update_frequency: daily

medical_reports:
  formats: [pdf, hl7_fhir]
  share_with_doctor: true
  include_charts: true
  language: zh

alerts:
  enabled: true
  thresholds:
    heart_rate_high: 120
    heart_rate_low: 50
    blood_pressure_high: "140/90"
    sleep_deficit_hours: 6
    inactivity_days: 3
  channels: [push, email, sms]

chronic_disease:
  supported: [diabetes, hypertension, hyperlipidemia, asthma]
  tracking_metrics: [...]
  medication_reminder: true
  doctor_sharing: true

data_security:
  encryption: AES-256
  hipaa_compliant: true
  gdpr_compliant: true
  data_residency: cn
```

