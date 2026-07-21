# 详细参考 - personal-health-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import os
import requests
from datetime import datetime

API_BASE = "https://api.health-pro.local/v1"
ADMIN_KEY = os.environ["HEALTH_ADMIN_KEY"]

class ChronicDiseaseManager:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key, "X-Edition": "pro"}

    def setup_diabetes_management(self, patient_id, baseline):
        """配置糖尿病管理"""
        payload = {
            "patient_id": patient_id,
            "condition": "diabetes",
            "type": "type_2",
            "baseline": baseline,
            "tracking": {
                "fasting_glucose": "daily_morning",
                "postprandial_glucose": "after_each_meal",
                "hba1c": "quarterly",
                "weight": "weekly",
                "blood_pressure": "daily",
            },
            "targets": {
                "fasting_glucose_mmol": [4.4, 7.0],
                "postprandial_glucose_mmol": [4.4, 10.0],
                "hba1c_pct": 7.0,
                "blood_pressure": "130/80",
            },
            "medications": [
                {"name": "二甲双胍", "dose": "500mg", "schedule": "每日两次,饭后"},
            ],
            "alerts": {
                "glucose_high": 10.0,
                "glucose_low": 3.9,
                "bp_high": "140/90",
            },
        }
        resp = requests.post(
            f"{API_BASE}/chronic/setup",
            headers=self.headers,
            json=payload,
            timeout=60,
        )
        return resp.json()

    def log_glucose(self, patient_id, value, measurement_type, meal_context):
        """记录血糖"""
        payload = {
            "patient_id": patient_id,
            "value": value,
            "type": measurement_type,  # fasting, postprandial
            "meal_context": meal_context,
            "timestamp": datetime.now().isoformat(),
        }
        resp = requests.post(
            f"{API_BASE}/chronic/glucose/log",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()

    def trend_analysis(self, patient_id, metric, period="month"):
        """趋势分析"""
        resp = requests.get(
            f"{API_BASE}/chronic/{patient_id}/trend",
            headers=self.headers,
            params={"metric": metric, "period": period},
            timeout=60,
        )
        return resp.json()

cdm = ChronicDiseaseManager(ADMIN_KEY)
cdm.setup_diabetes_management("p001", {
    "age": 55,
    "weight_kg": 75,
    "hba1c": 8.2,
    "fasting_glucose": 8.5,
})
```

## 代码示例 (python)

```python
class DoctorCollaboration:
    def share_with_doctor(self, patient_id, doctor_email, data_range):
        """与医生共享数据"""
        payload = {
            "patient_id": patient_id,
            "doctor_email": doctor_email,
            "data_range": data_range,
            "data_types": [
                "glucose_logs", "blood_pressure", "weight",
                "medication_adherence", "lab_reports",
            ],
            "format": "hl7_fhir",  # 医疗标准格式
            "expiry": "30_days",
        }
        resp = requests.post(
            f"{API_BASE}/sharing/doctor",
            headers=self.headers,
            json=payload,
            timeout=60,
        )
        return resp.json()

    def generate_doctor_report(self, patient_id, period):
        """生成医生报告"""
        payload = {
            "patient_id": patient_id,
            "period": period,
            "format": "medical_pdf",
            "sections": [
                "patient_summary",
                "vital_signs_trends",
                "lab_results",
                "medication_adherence",
                "symptom_diary",
                "risk_assessment",
                "recommendations_for_doctor",
            ],
            "hl7_compliant": True,
        }
        resp = requests.post(
            f"{API_BASE}/reports/doctor",
            headers=self.headers,
            json=payload,
            timeout=300,
        )
        return resp.json()

    def doctor_feedback(self, patient_id, doctor_id, feedback):
        """医生反馈"""
        payload = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "feedback": feedback,
            "timestamp": datetime.now().isoformat(),
        }
        resp = requests.post(
            f"{API_BASE}/sharing/doctor-feedback",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()
```

