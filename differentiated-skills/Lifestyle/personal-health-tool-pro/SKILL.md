---
slug: personal-health-tool-pro
name: personal-health-tool-pro
version: "1.0.0"
displayName: 个人健康管家专业版
summary: 企业级健康管家,支持慢病管理、医生共享、AI诊断与穿戴设备同步
license: MIT
edition: pro
description: |-
  面向家庭、慢病患者与健康机构的企业级健康管家平台。
  核心能力: 慢病管理、医生数据共享、AI辅助诊断、穿戴设备同步、家庭多成员管理
  适用场景: 慢病管理、家庭健康关怀、术后康复、企业员工健康、医疗机构
  差异化: 专业版支持慢病管理与医疗协作,与免费版数据格式兼容
  触发关键词: 慢病管理, 医生共享, AI诊断, 穿戴设备, 家庭健康, 术后康复
tags:
- 健康管理
- 企业级
- 慢病管理
- AI诊断
- 穿戴设备
- 医疗协作
tools:
- read
- exec
---

# 个人健康管家 (专业版)

## 概述

专业版面向家庭、慢病患者与健康机构,在免费版个人健康管理之上,扩展慢病管理、医生数据共享、AI 辅助诊断、穿戴设备同步、家庭多成员管理等企业级能力。支持构建完整的个人健康档案,与医疗系统协作,适合慢病管理、术后康复、家庭健康关怀等专业场景。

专业版与免费版数据格式完全兼容,个人用户升级后历史数据无缝迁移。

## 核心能力

| 能力模块 | 描述 | 免费版 | 专业版 |
|:--------|:-----|:------:|:------:|
| 健康数据记录 | 运动、睡眠、饮食 | 支持 | 支持 |
| 体检报告解读 | 指标分析 | 支持 | 支持 |
| 运动计划 | 个性化方案 | 支持 | 支持 |
| 慢病管理 | 慢性病跟踪 | 不支持 | 支持 |
| 医生共享 | 与医生共享数据 | 不支持 | 支持 |
| AI 诊断 | AI 辅助诊断 | 不支持 | 支持 |
| 穿戴设备 | 设备同步 | 不支持 | 支持 |
| 家庭管理 | 多成员管理 | 不支持 | 支持 |
| 医疗报告 | 医疗级报告 | 不支持 | 支持 |
| 异常预警 | 健康风险预警 | 不支持 | 支持 |
| 用药管理 | 药物提醒 | 不支持 | 支持 |
| 优先支持 | 专属支持 | 不支持 | 支持 |

## 使用场景

### 场景一: 慢病管理

为慢病患者提供完整管理方案。

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
# 配置糖尿病管理
cdm.setup_diabetes_management("p001", {
    "age": 55,
    "weight_kg": 75,
    "hba1c": 8.2,
    "fasting_glucose": 8.5,
})
```

### 场景二: 医生协作

与主治医生共享健康数据,远程协作管理。

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

### 场景三: AI 辅助诊断

基于健康数据进行 AI 辅助诊断。

```python
def ai_diagnosis(patient_id, symptoms):
    """AI 辅助诊断"""
    payload = {
        "patient_id": patient_id,
        "symptoms": symptoms,
        "based_on": [
            "health_history",
            "recent_lab_results",
            "vital_signs_trends",
            "medication_history",
            "family_history",
        ],
        "analysis": [
            "possible_conditions",
            "risk_stratification",
            "recommended_tests",
            "urgency_assessment",
        ],
        "disclaimer": "AI 辅助诊断仅供参考,不替代医生诊断",
    }
    resp = requests.post(
        f"{API_BASE}/ai/diagnosis",
        headers=self.headers,
        json=payload,
        timeout=120,
    )
    return resp.json()

# 输出示例
# {
#   "possible_conditions": [
#     {"name": "2型糖尿病", "probability": 0.65, "icd10": "E11"},
#     {"name": "高血压", "probability": 0.45, "icd10": "I10"},
#   ],
#   "risk_stratification": {"level": "medium", "factors": [...]},
#   "recommended_tests": ["糖化血红蛋白", "动态血压监测"],
#   "urgency": "建议 2 周内就诊",
# }
```

## 快速开始

### 步骤 1: 申请专业版账户

联系销售开通专业版,获取管理员凭证与租户 ID。

### 步骤 2: 配置凭证

```bash
export HEALTH_ADMIN_KEY="sk_pro_admin_xxx"
export HEALTH_ORG_ID="org_your_id"
export HEALTH_EDITION="pro"
```

### 步骤 3: 配置慢病管理

```bash
curl -X POST -H "X-API-Key: $HEALTH_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"patient_id":"p001","condition":"diabetes","type":"type_2"}' \
  "https://api.health-pro.local/v1/chronic/setup"
```

### 步骤 4: 连接穿戴设备

```bash
curl -X POST -H "X-API-Key: $HEALTH_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"patient_id":"p001","device":"apple_watch","sync":"realtime"}' \
  "https://api.health-pro.local/v1/devices/connect"
```

## 配置示例

### 企业级配置

```yaml
# /etc/health-pro/pro.yaml
edition: pro
api:
  base_url: https://api.health-pro.local/v1
  admin_key: ${HEALTH_ADMIN_KEY}
  org_id: ${HEALTH_ORG_ID}
  timeout: 120

family:
  max_members: 20
  permissions:
    admin: [manage_all, view_all]
    member: [view_own, edit_own]
    caregiver: [view_assigned, log_data]

chronic_diseases:
  supported: [diabetes, hypertension, hyperlipidemia, copd, asthma]
  tracking: comprehensive
  medication_management: true
  alert_thresholds: customizable

medical_collaboration:
  doctor_sharing: true
  hl7_fhir: true
  electronic_health_record: true
  telemedicine: true

ai_diagnosis:
  enabled: true
  models: [risk_stratification, symptom_analysis, trend_prediction]
  icd10_codes: true
  disclaimer: required

devices:
  supported: [apple_watch, fitbit, garmin, huawei_band, xiaomi_band, omron_bp]
  sync_frequency: realtime
  data_types: [heart_rate, steps, sleep, blood_pressure, blood_glucose, ecg]

alerts:
  channels: [push, email, sms, emergency_call]
  levels: [info, warning, critical, emergency]
  escalation: true

data_security:
  encryption: AES-256
  hipaa_compliant: true
  gdpr_compliant: true
  data_residency: cn
  audit_log: 7_years
```

### 慢病管理配置

```python
CHRONIC_DISEASE_TEMPLATES = {
    "diabetes": {
        "metrics": ["fasting_glucose", "postprandial_glucose", "hba1c", "weight"],
        "medications": ["metformin", "insulin", "sglt2_inhibitors"],
        "complications": ["neuropathy", "nephropathy", "retinopathy"],
        "lifestyle": ["diet", "exercise", "foot_care"],
    },
    "hypertension": {
        "metrics": ["blood_pressure", "heart_rate", "weight"],
        "medications": ["ace_inhibitors", "arb", "ccb", "diuretics"],
        "complications": ["stroke", "heart_failure", "kidney_disease"],
        "lifestyle": ["low_salt_diet", "exercise", "stress_management"],
    },
}
```

### 异常预警

```python
def configure_emergency_alerts(patient_id):
    """配置紧急预警"""
    payload = {
        "patient_id": patient_id,
        "alerts": [
            {
                "metric": "blood_glucose",
                "critical_low": 3.3,  # 低血糖紧急
                "critical_high": 16.7,  # 高血糖紧急
                "action": "call_emergency_contact",
            },
            {
                "metric": "blood_pressure",
                "critical_high": "180/120",  # 高血压危象
                "action": "call_emergency_contact",
            },
            {
                "metric": "heart_rate",
                "critical_low": 40,
                "critical_high": 150,
                "action": "notify_doctor",
            },
        ],
        "emergency_contacts": [
            {"name": "家属", "phone": "13800000000", "priority": 1},
            {"name": "主治医生", "phone": "13900000000", "priority": 2},
            {"name": "急救", "phone": "120", "priority": 3},
        ],
    }
    resp = requests.post(
        f"{API_BASE}/alerts/emergency",
        headers=self.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()
```

## 最佳实践

### 1. 用药管理

```python
def medication_reminder(patient_id, medication):
    """用药提醒"""
    payload = {
        "patient_id": patient_id,
        "medication": medication,
        "schedule": "每日两次,饭前 30 分钟",
        "reminder_times": ["07:30", "18:30"],
        "refill_alert": {"when_remaining_days": 7, "pharmacy_contact": "..."},
    }
    resp = requests.post(
        f"{API_BASE}/medications/reminder",
        headers=self.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()
```

### 2. 数据安全

```python
def secure_health_data_sharing(patient_id, recipient, scope):
    """安全健康数据共享"""
    payload = {
        "patient_id": patient_id,
        "recipient": recipient,
        "scope": scope,  # 限定数据范围
        "duration": "30_days",
        "revocable": True,
        "audit_log": True,
        "encryption": "AES-256",
    }
    resp = requests.post(
        f"{API_BASE}/sharing/secure",
        headers=self.headers,
        json=payload,
        timeout=30,
    )
    return resp.json()
```

### 3. 家庭健康管理

```python
def setup_family_health(family_members):
    """配置家庭健康管理"""
    payload = {
        "members": family_members,
        "shared_dashboard": True,
        "caregiver_assignments": [
            {"caregiver": "parent", "patients": ["grandparent_1", "grandparent_2"]},
        ],
        "family_health_history": True,
        "genetic_risk_assessment": True,
    }
    resp = requests.post(
        f"{API_BASE}/family/setup",
        headers=self.headers,
        json=payload,
        timeout=60,
    )
    return resp.json()
```

## 常见问题

### Q1: 专业版与免费版数据兼容吗?

完全兼容。专业版在免费版数据格式上扩展,升级后历史数据无缝迁移。

### Q2: 慢病管理支持哪些疾病?

糖尿病、高血压、高血脂、COPD、哮喘等常见慢性病。

### Q3: AI 诊断可信吗?

AI 诊断提供参考,准确度约 80%,但不能替代医生诊断。请咨询专业医生。

### Q4: 医生共享数据安全吗?

使用 HL7 FHIR 医疗标准、AES-256 加密、权限控制、审计日志,符合 HIPAA 等合规要求。

### Q5: 穿戴设备支持哪些?

Apple Watch、Fitbit、Garmin、华为手环、小米手环、欧姆龙血压计等主流设备。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 规范的任意 AI Agent (Claude Code、Cursor、Codex、Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux (生产环境推荐 Linux)
- **网络**: 需访问专业版服务
- **Python**: 3.9+ (用于脚本化操作)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Health Pro API | 在线 API | 必需 | 联系销售开通专业版 |
| LLM API | 推理服务 | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.9+ | 运行时 | 推荐 | python.org 下载 |
| requests 库 | Python 库 | 推荐 | `pip install requests` |
| cryptography | Python 库 | 可选 | `pip install cryptography` |
| 数据库 | 持久化 | 可选 | 兼容主流关系型数据库 (使用 `数据库` 上下文) |

### API Key 配置

```bash
# 专业版凭证
export HEALTH_ADMIN_KEY="sk_pro_admin_xxx"
export HEALTH_ORG_ID="org_your_id"
export HEALTH_EDITION="pro"

# 可选: 穿戴设备
export APPLE_HEALTH_TOKEN="..."
export FITBIT_TOKEN="..."
export OMRON_DEVICE_ID="..."

# 可选: 医疗系统对接
export HL7_FHIR_ENDPOINT="https://fhir.hospital.com"
export EMR_API_KEY="..."

# 可选: 紧急通知
export EMERGENCY_SMS_API="https://sms-api.example.com"
```

### 可用性分类

- **分类**: MD+EXEC (Markdown 指令 + 命令行执行)
- **说明**: 本 Skill 面向家庭、慢病患者与医疗场景,通过自然语言指令驱动 Agent 调用 Pro API,完成慢病管理、医疗协作等企业级场景
- **专业版特性**: 慢病管理、医生共享、AI 诊断、穿戴设备、家庭管理、医疗报告、异常预警、用药管理
- **兼容性**: 与免费版数据格式完全兼容,支持平滑升级
